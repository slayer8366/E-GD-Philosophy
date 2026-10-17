#!/usr/bin/env python3
"""records_lookup.py -- read-only lookup over a project's records, in any
set of repositories a config names: specs/2026-10-16-records-lookup.md,
built under RECORD.md 2026-10-17-03 for Forager and forager-forecast, and
generalized under 2026-10-17-07.

  records_lookup.py COMMAND [ARGS] [--config FILE | --preset NAME]
                    [--repo NAME=PATH ...] [--ref NAME=REF ...] [--no-fetch]

  show ID       an entry verbatim, with its citation (a full ID, a short
                form -NNNN of a dated ID, or the ID of a table row)
  links ID      what names this entry, and what it names
  search WORDS  every source, newest first, each hit cited
  open          intents with no closing entry
  next-id       the next free ID after the record's last, across every
                record file

With no config the tool reads one repository's record at HEAD: the current
directory, or the folder --repo repo=PATH names. --preset forager reads
Forager's and forager-forecast's records (lookups/forager.json; give
--repo forager=PATH and --repo forecast=PATH). --print-config prints the
config in use. A config is one JSON object:

  repos    each repository's name, with a path or null (--repo NAME=PATH
           gives or replaces it)
  record   name, repo, ref; shape: check_record's config keys, or null to
           read records.json from the repository at the ref (check_record's
           default when there is none); links: each link field, "first" or
           "all", or null for the shape's backward links and closes field;
           replaced_by: the words search shows beside an entry that a
           field names, e.g. {"Supersedes": "superseded by"}
  tables   each: name, repo, ref, path, row_pattern (two groups: an ID,
           which may be empty, and a YYYY-MM-DD date); optional section
           (only rows under that heading), id_pattern (show finds rows by
           ID), supersedes_column (0 is the first), record_reference (a
           pattern whose group names a record entry)
  folders  each: name, repo, ref, path; files searched whole

--ref NAME=REF overrides the ref of one source by its name, or of every
source in a repository by the repository's name; a source's own wins.

Every answer carries repository, ref, commit, file and line. Sources are
read with git show and git ls-tree at a resolved commit, after git fetch
for origin/ refs, and never checked out or written. A source that cannot
be read is reported as NOT READ, never skipped. A command the record's
shape cannot answer says it is unsupported.

A "first" link is read by the ID its value starts with, since Forager's
practice sometimes follows the ID with a parenthesis; an "all" link is read
for every ID it carries.
"""
import argparse
import copy
import io
import json
import re
import subprocess
import sys
import tempfile
from collections import Counter
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_record as cr  # noqa: E402

SHORT_RE = re.compile(r"^-\d+$")
DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")
MONTH_NAME_RE = re.compile(r"^\d{4}-\d{2}\.md$")
TRAILING_NUMBER_RE = re.compile(r"^(.*?)(\d+)$")
PRESETS_DIR = Path(__file__).resolve().parent / "lookups"

# With no config: one repository's record at HEAD, shaped by its records.json
# or check_record's default (2026-10-17-07).
DEFAULT_LOOKUP = {
    "repos": {"repo": "."},
    "record": {"name": "record", "repo": "repo", "ref": "HEAD", "shape": None,
               "links": None,
               "replaced_by": {"Supersedes": "superseded by", "Corrects": "corrected by"}},
    "tables": [],
    "folders": [],
}


class LookupConfigError(Exception):
    """A lookup config, or a --repo/--ref value, that cannot be used. The
    message names the key; main() reports it and exits 2, reading nothing."""


def _need(cond, key, msg):
    if not cond:
        raise LookupConfigError(f"{key}: {msg}")


def _pattern(value, key, groups=0):
    _need(isinstance(value, str) and value, key, "must be a non-empty pattern")
    try:
        rx = re.compile(value)
    except re.error as e:
        raise LookupConfigError(f"{key}: does not compile ({e})") from e
    _need(rx.groups >= groups, key, f"needs {groups} group(s), has {rx.groups}")


def _source_def(obj, key, required, optional, repos):
    _need(isinstance(obj, dict), key, "must be an object")
    unknown = sorted(set(obj) - set(required) - set(optional))
    _need(not unknown, key, f"unknown key(s) {unknown}; allowed: "
          f"{', '.join(required + optional)}")
    for k in required:
        _need(isinstance(obj.get(k), str) and obj[k], f"{key}.{k}", "must be a non-empty string")
    _need(obj["repo"] in repos, f"{key}.repo", f"names {obj['repo']!r}, which is not in "
          f"repos ({', '.join(repos)})")


def validate_lookup(cfg):
    """Raises LookupConfigError naming the first key that is wrong."""
    unknown = sorted(set(cfg) - set(DEFAULT_LOOKUP))
    _need(not unknown, "config", f"unknown key(s) {unknown}; known keys: "
          f"{', '.join(DEFAULT_LOOKUP)}")
    repos = cfg["repos"]
    _need(isinstance(repos, dict) and repos and all(
        isinstance(k, str) and k and (v is None or isinstance(v, str)) for k, v in repos.items()),
          "repos", "must map repository names to a path or null")
    rec = cfg["record"]
    _source_def(rec, "record", ["name", "repo", "ref"], ["shape", "links", "replaced_by"], repos)
    if rec.get("shape") is not None:
        _need(isinstance(rec["shape"], dict), "record.shape",
              "must be an object of check_record config keys, or null")
        merged = copy.deepcopy(cr.DEFAULT_CONFIG)
        merged.update(rec["shape"])
        try:
            cr.validate_config(merged)
        except cr.ConfigError as e:
            raise LookupConfigError(f"record.shape: {e}") from e
    links = rec.get("links")
    _need(links is None or (isinstance(links, dict) and all(
        isinstance(k, str) and k and v in ("first", "all") for k, v in links.items())),
          "record.links", 'must map field names to "first" or "all", or be null')
    replaced = rec.get("replaced_by", {})
    _need(isinstance(replaced, dict) and all(
        isinstance(k, str) and k and isinstance(v, str) and v for k, v in replaced.items()),
          "record.replaced_by", "must map field names to the words shown")
    names = [rec["name"]]
    _need(isinstance(cfg["tables"], list), "tables", "must be a list")
    for i, t in enumerate(cfg["tables"]):
        key = f"tables[{i}]"
        _source_def(t, key, ["name", "repo", "ref", "path", "row_pattern"],
                    ["section", "id_pattern", "supersedes_column", "record_reference"], repos)
        _pattern(t["row_pattern"], f"{key}.row_pattern", groups=2)
        if t.get("id_pattern") is not None:
            _pattern(t["id_pattern"], f"{key}.id_pattern")
        if t.get("record_reference") is not None:
            _pattern(t["record_reference"], f"{key}.record_reference", groups=1)
        _need(t.get("section") is None or (isinstance(t["section"], str) and t["section"]),
              f"{key}.section", "must be a heading line or null")
        col = t.get("supersedes_column")
        _need(col is None or (isinstance(col, int) and not isinstance(col, bool) and col >= 0),
              f"{key}.supersedes_column", "must be a column index (0 for the first) or null")
        names.append(t["name"])
    _need(isinstance(cfg["folders"], list), "folders", "must be a list")
    for i, f in enumerate(cfg["folders"]):
        _source_def(f, f"folders[{i}]", ["name", "repo", "ref", "path"], [], repos)
        names.append(f["name"])
    repeated = sorted({n for n in names if names.count(n) > 1})
    _need(not repeated, "config", f"source names must differ; repeated: {repeated}")
    clash = sorted(set(names) & set(repos))
    _need(not clash, "config", f"a source and a repository share a name, so --ref "
          f"would be ambiguous: {clash}")
    return cfg


def load_lookup(config=None, preset=None):
    """(config, source file or None). A config's top-level keys replace the
    default's whole."""
    _need(not (config and preset), "--config", "and --preset cannot both be given")
    if preset:
        path = PRESETS_DIR / f"{preset}.json"
        _need(path.is_file(), "--preset", f"no preset {preset!r} ({path} does not exist)")
    elif config:
        path = Path(config)
        _need(path.is_file(), "--config", f"{config} does not exist")
    else:
        return copy.deepcopy(DEFAULT_LOOKUP), None
    try:
        user = json.loads(path.read_text())
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
        raise LookupConfigError(f"{path}: not readable as JSON ({e})") from e
    _need(isinstance(user, dict), str(path), "must hold one JSON object")
    merged = copy.deepcopy(DEFAULT_LOOKUP)
    merged.update(user)
    return validate_lookup(merged), str(path)


def _pairs(values, flag):
    out = {}
    for v in values or []:
        name, sep, val = v.partition("=")
        _need(sep and name and val, flag, f"{v!r} is not NAME=VALUE")
        out[name] = val
    return out


def _run_git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)


class Source:
    """One repository at one ref, resolved to a commit."""

    def __init__(self, repo_label, repo, ref, fetch):
        self.repo_label, self.repo, self.ref = repo_label, repo, ref
        self.commit, self.note, self.error = None, "", ""
        if repo is None:
            self.error = f"no path given for repo {repo_label} (--repo {repo_label}=PATH)"
            return
        if not Path(repo).is_dir():
            self.error = f"{repo} is not a directory"
            return
        if fetch and ref.startswith("origin/"):
            r = _run_git(repo, "fetch", "-q", "origin", ref.split("/", 1)[1])
            if r.returncode != 0:
                self.note = f"; fetch failed, the local copy of {ref} was read"
        r = _run_git(repo, "rev-parse", "--verify", "-q", f"{ref}^{{commit}}")
        if r.returncode != 0:
            self.error = f"ref {ref} not found in {repo}"
            return
        self.commit = r.stdout.strip()

    def show(self, path):
        r = _run_git(self.repo, "show", f"{self.commit}:{path}")
        return r.stdout if r.returncode == 0 else None

    def ls(self, directory):
        r = _run_git(self.repo, "ls-tree", "--name-only", f"{self.commit}", f"{directory}/")
        return [Path(p).name for p in r.stdout.split()] if r.returncode == 0 else []

    def cite(self, path, start, end=None):
        end = start if end is None else end
        return f"{self.repo_label} {self.ref}@{self.commit[:8]} {path}:{start}-{end}"


def _entries_with_lines(text):
    """Entries of a record file as (start, end, block): 1-based line
    numbers of the first and last non-blank line, and the block text,
    found the same way check_record.split_entries finds them."""
    marker = text.find("## Entries")
    if marker == -1:
        return []
    lines = text.split("\n")
    first = text[:marker].count("\n") + 1  # the heading's own line
    out, group = [], []
    for n in range(first + 1, len(lines) + 1):
        line = lines[n - 1]
        if line == "---":
            if group:
                out.append(group)
            group = []
        else:
            group.append((n, line))
    if group:
        out.append(group)
    result = []
    for g in out:
        body = [(n, l) for n, l in g if l.strip()]
        if not body:
            continue
        start, end = body[0][0], body[-1][0]
        result.append((start, end, "\n".join(lines[start - 1:end])))
    assert len(result) == len(cr.split_entries(text)), "entry split disagrees with check_record"
    return result


class Records:
    def __init__(self, cfg, repo_paths, refs, fetch):
        self.cfg = cfg
        paths = dict(cfg["repos"])
        paths.update(repo_paths)
        self.sources, cache = {}, {}
        for d in [cfg["record"]] + cfg["tables"] + cfg["folders"]:
            ref = refs.get(d["name"]) or refs.get(d["repo"]) or d["ref"]
            if (d["repo"], ref) not in cache:
                cache[(d["repo"], ref)] = Source(d["repo"], paths.get(d["repo"]), ref, fetch)
            self.sources[d["name"]] = cache[(d["repo"], ref)]
        self.entries, self.read_errors = [], []
        rec_def = cfg["record"]
        self.record_name = rec_def["name"]
        rec = self.sources[self.record_name]
        self.shape_ok = True
        self.shape = self._shape(rec_def, rec)
        self.token = re.compile(self.shape["id_token_pattern"])
        self.links = (rec_def["links"] if rec_def.get("links") is not None else
                      {**self.shape["backward_links"], self.shape["closes_field"]: "first"})
        self.replaced_by = rec_def.get("replaced_by", {})
        if rec.commit and self.shape_ok:
            record_file, mdir = self.shape["record_file"], self.shape["monthly_dir"]
            files = [record_file] if rec.show(record_file) is not None else []
            if mdir:
                files += sorted(f"{mdir}/{n}" for n in rec.ls(mdir) if MONTH_NAME_RE.match(n))
            if not files:
                self.read_errors.append(f"{self.record_name}: no {record_file}"
                                        f"{' or ' + mdir + '/YYYY-MM.md' if mdir else ''} "
                                        f"at {rec.ref}")
            for path in files:
                for start, end, block in _entries_with_lines(rec.show(path)):
                    f = cr.parse_fields(block)
                    eid = f.get("ID", "").strip()
                    ts = f.get("Timestamp", "").strip()
                    self.entries.append({
                        "id": eid, "kind": f.get("Kind", "").strip(), "fields": f,
                        "path": path, "start": start, "end": end, "text": block,
                        "date": (ts or eid)[:10], "cite": rec.cite(path, start, end)})
        self.by_id = {}
        for e in self.entries:
            self.by_id.setdefault(e["id"], e)
        self.tables = [(t, self._rows(t)) for t in cfg["tables"]]

    def _shape(self, rec_def, rec):
        """The record's check_record config: the lookup config's shape, else
        records.json in the record repository at the ref, else the default.
        A records.json that is not a usable config leaves the record unread,
        reported, rather than read with the default instead."""
        shape = copy.deepcopy(cr.DEFAULT_CONFIG)
        if rec_def.get("shape") is not None:
            shape.update(rec_def["shape"])
            return shape
        text = rec.show(cr.CONFIG_NAME) if rec.commit else None
        if text is None:
            return shape
        try:
            user = json.loads(text)
            if not isinstance(user, dict):
                raise cr.ConfigError("must hold one JSON object")
            shape.update(user)
            return cr.validate_config(shape)
        except (json.JSONDecodeError, cr.ConfigError) as e:
            self.read_errors.append(f"{self.record_name}: {cr.CONFIG_NAME} at {rec.ref} is "
                                    f"not a usable config ({e}); the record was not read")
            self.shape_ok = False
            return copy.deepcopy(cr.DEFAULT_CONFIG)

    def _rows(self, t):
        src = self.sources[t["name"]]
        if not src.commit:
            return []
        text = src.show(t["path"])
        if text is None:
            self.read_errors.append(f"{t['name']}: {t['path']} not found at {src.ref}")
            return []
        section = t.get("section")
        rows, inside = [], section is None
        for n, line in enumerate(text.split("\n"), 1):
            if section is not None and line.startswith("## "):
                inside = line.strip() == section
                continue
            m = re.match(t["row_pattern"], line) if inside else None
            if m:
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                rows.append({"id": m.group(1), "date": m.group(2), "text": line, "cells": cells,
                             "label": t["name"], "cite": src.cite(t["path"], n)})
        return rows

    def header(self):
        for name, src in self.sources.items():
            if src.commit:
                print(f"source {name}: {src.repo_label} {src.ref}@{src.commit[:8]}{src.note}")
            else:
                print(f"source {name}: NOT READ ({src.error})")
        for err in self.read_errors:
            print(f"source {err}: NOT READ")
        print()

    def resolve(self, key):
        """A full ID, or a short form -NNNN; returns (entry or None, message)."""
        if SHORT_RE.match(key):
            cands = [e for e in self.entries if e["id"].endswith(key)
                     and re.fullmatch(r"\d{4}-\d{2}-\d{2}" + re.escape(key), e["id"])]
            ids = sorted({e["id"] for e in cands})
            if len(ids) == 1:
                return self.by_id[ids[0]], ""
            if len(ids) > 1:
                return None, f"ambiguous: {key} matches {', '.join(ids)}"
            return None, f"not found: {key}"
        e = self.by_id.get(key)
        return (e, "") if e else (None, f"not found: {key}")

    def links_from(self, e):
        """(field, target ID) pairs this entry names."""
        out = []
        for label, value in e["fields"].items():
            base = re.split(r"[,(]", label)[0].strip()
            mode = self.links.get(base)
            if mode is None:
                continue
            if mode == "first":
                m = self.token.match(value.strip())
                toks = [m.group(0)] if m else []
            else:
                toks = self.token.findall(value)
            out += [(base, t) for t in toks]
        return out


def cmd_show(r, key):
    for t, rows in r.tables:
        if t.get("id_pattern") is None or not re.fullmatch(t["id_pattern"], key):
            continue
        hit = [d for d in rows if d["id"] == key]
        if not hit:
            print(f"not found: {key} in {t['name']}")
            return 1
        d = hit[0]
        print(f"citation: {d['cite']}")
        print(d["text"])
        if t.get("record_reference") is not None:
            for m in re.finditer(t["record_reference"], d["text"]):
                e, msg = r.resolve(m.group(1))
                print(f"references: {m.group(0)} -> {e['id']} — {e['cite']}" if e
                      else f"references: {m.group(0)} -> {msg}")
        return 0
    if _record_unread(r, f"show {key}"):
        return 1
    e, msg = r.resolve(key)
    if not e:
        print(msg)
        return 1
    print(f"citation: {e['cite']}")
    print(e["text"])
    for t, rows in r.tables:
        if t.get("record_reference") is None:
            continue
        for d in rows:
            if any(r.resolve(m.group(1))[0] is e
                   for m in re.finditer(t["record_reference"], d["text"])):
                print(f"referenced by: {t['repo']} {d['id']} — {d['cite']}")
    return 0


def cmd_links(r, key):
    if _record_unread(r, f"links of {key}"):
        return 1
    e, msg = r.resolve(key)
    if not e:
        print(msg)
        return 1
    print(f"links of {e['id']} — {e['cite']}")
    for other in r.entries:
        for field, target in r.links_from(other):
            if target == e["id"] and other is not e:
                print(f"named by: {field} {other['id']} — {other['cite']}")
    for field, target in r.links_from(e):
        t = r.by_id.get(target)
        print(f"names: {field} {target} — {t['cite'] if t else 'not in the record'}")
    return 0


def _hits_text(units, words):
    return [u for u in units if all(w in u["text"].lower() for w in words)]


def cmd_search(r, words):
    words = [w.lower() for w in words]
    hits = []
    for e in _hits_text(r.entries, words):
        title = e["fields"].get("Title") or e["fields"].get("Subject") or e["text"].split("\n")[0]
        extra = []
        for other in r.entries:
            for field, target in r.links_from(other):
                if target == e["id"] and field in r.replaced_by:
                    extra.append(f"    {r.replaced_by[field]} {other['id']} — {other['cite']}")
        for field, target in r.links_from(e):
            if field in r.replaced_by:
                extra.append(f"    {field.lower()} {target}")
        hits.append((e["date"], r.record_name, e["cite"], f"{e['id']} {title[:120]}", extra))
    for t, rows in r.tables:
        col = t.get("supersedes_column")
        for row in _hits_text(rows, words):
            extra = []
            if col is not None:
                sup = row["cells"][col] if len(row["cells"]) > col else ""
                if sup and sup.lower() not in ("none", "-", ""):
                    extra.append(f"    supersedes {sup[:120]}")
                for other in rows:
                    sup_o = other["cells"][col] if len(other["cells"]) > col else ""
                    if other is not row and re.search(rf"\b{re.escape(row['id'])}\b", sup_o):
                        extra.append(f"    superseded by {other['id']} — {other['cite']}")
            hits.append((row["date"], row["label"], row["cite"], row["text"][:140], extra))
    for f in r.cfg["folders"]:
        src = r.sources[f["name"]]
        if not src.commit:
            continue
        for fname in src.ls(f["path"]):
            text = src.show(f"{f['path']}/{fname}") or ""
            if all(w in text.lower() for w in words):
                lines = text.split("\n")
                n = next((i for i, l in enumerate(lines, 1) if any(w in l.lower() for w in words)), 1)
                m = DATE_RE.match(fname)
                hits.append((m.group(1) if m else "", f["name"], src.cite(f"{f['path']}/{fname}", n),
                             lines[n - 1][:140], []))
    hits.sort(key=lambda h: h[0], reverse=True)
    for date, label, cite, excerpt, extra in hits:
        print(f"{date or '(undated)'}  {label}  {cite}  {excerpt}")
        for x in extra:
            print(x)
    print(f"hits: {len(hits)}")
    return 0


def _record_unread(r, what):
    """True, after saying so, when the record could not be read: an answer
    drawn from it would be a plausible value standing in for nothing."""
    if r.sources[r.record_name].commit and r.entries:
        return False
    print(f"{what}: unknown, the record was not read")
    return True


def cmd_open(r):
    sh = r.shape
    if not sh["intent_kind"]:
        print("open intents: unsupported, the record's shape has no intent type "
              "(intent_kind is null)")
        return 1
    if _record_unread(r, "open intents"):
        return 1
    closed = set()
    for e in r.entries:
        if e["kind"] in sh["closing_kinds"]:
            m = r.token.match(e["fields"].get(sh["closes_field"], "").strip())
            if m:
                closed.add(m.group(0))
    opened = [e for e in r.entries if e["kind"] == sh["intent_kind"] and e["id"] not in closed]
    for e in opened:
        print(f"open intent: {e['id']} — {e['cite']}")
    print(f"open intents: {len(opened)}")
    return 0


def cmd_next_id(r):
    src = r.sources[r.record_name]
    if _record_unread(r, "next free ID"):
        return 1
    counts = Counter(e["id"] for e in r.entries)
    for eid, n in sorted(counts.items()):
        if n > 1:
            where = ", ".join(e["cite"] for e in r.entries if e["id"] == eid)
            print(f"warning: duplicate ID {eid} ({n} times): {where}")
    last = TRAILING_NUMBER_RE.match(r.entries[-1]["id"])
    if not last:
        print(f"next free ID: unsupported, the last entry's ID "
              f"{r.entries[-1]['id']!r} does not end in a number")
        return 1
    prefix = last.group(1)
    nums = [m.group(2) for m in (TRAILING_NUMBER_RE.match(e["id"]) for e in r.entries)
            if m and m.group(1) == prefix]
    top = max(nums, key=int)
    width = len(top) if top.startswith("0") else 0
    print(f"next free ID: {prefix}{int(top) + 1:0{width}d} "
          f"(read at {src.ref}@{src.commit[:8]})")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="records_lookup.py", description=__doc__.split("\n")[0])
    p.add_argument("command", nargs="?", choices=["show", "links", "search", "open", "next-id"])
    p.add_argument("args", nargs="*")
    p.add_argument("--config", help="a lookup config file")
    p.add_argument("--preset", help="a config in lookups/, by name (e.g. forager)")
    p.add_argument("--repo", action="append", metavar="NAME=PATH",
                   help="a repository's path, by its name in the config")
    p.add_argument("--ref", action="append", metavar="NAME=REF",
                   help="a source's ref by its name, or every source's in a repository")
    p.add_argument("--no-fetch", action="store_true")
    p.add_argument("--print-config", action="store_true", help="print the config in use")
    args = p.parse_intermixed_args(argv)
    try:
        cfg, _ = load_lookup(args.config, args.preset)
        if args.print_config:
            print(json.dumps(cfg, indent=2, ensure_ascii=False))
            return 0
        repo_paths = _pairs(args.repo, "--repo")
        for name in repo_paths:
            _need(name in cfg["repos"], "--repo", f"{name!r} is not a repository in the config "
                  f"({', '.join(cfg['repos'])})")
        refs = _pairs(args.ref, "--ref")
        known = {d["name"] for d in [cfg["record"]] + cfg["tables"] + cfg["folders"]}
        for name in refs:
            _need(name in known or name in cfg["repos"], "--ref", f"{name!r} names no source "
                  f"or repository in the config")
    except LookupConfigError as e:
        print(f"config error: {e}\nNothing was read.")
        return 2
    if not args.command:
        print("give a command: show, links, search, open or next-id")
        return 2
    r = Records(cfg, repo_paths, refs, not args.no_fetch)
    r.header()
    if args.command in ("show", "links") and len(args.args) != 1:
        print(f"{args.command} takes one ID")
        return 2
    if args.command == "show":
        return cmd_show(r, args.args[0])
    if args.command == "links":
        return cmd_links(r, args.args[0])
    if args.command == "search":
        return cmd_search(r, args.args)
    if args.command == "open":
        return cmd_open(r)
    return cmd_next_id(r)


# --------------------------------------------------------------------------
# Self-tests (--render-check). Every fixture is a git repository under
# tempfile.mkdtemp(); every test runs through main(), the real entry point.
# --------------------------------------------------------------------------

def _git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True,
                          text=True, check=True).stdout.strip()


def _commit_branch(repo, branch, files):
    """Write files on a new or existing branch and commit them."""
    repo = Path(repo)
    if not (repo / ".git").exists():
        _git(repo, "init", "-q")
        _git(repo, "checkout", "-q", "-b", branch)
    else:
        try:
            _git(repo, "checkout", "-q", branch)
        except subprocess.CalledProcessError:
            _git(repo, "checkout", "-q", "-b", branch)
    for rel, text in files.items():
        p = repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    _git(repo, "add", "-A")
    _git(repo, "-c", "user.name=t", "-c", "user.email=t@example.invalid",
         "commit", "-q", "-m", f"fixture {branch}")
    return _git(repo, "rev-parse", "HEAD")


def _entry(**fields):
    return "\n".join(f"**{k}:** {v}" for k, v in fields.items())


def _record(*entries, title="RECORD.md"):
    parts = [f"# {title}", "", "## Entries", "", "---", ""]
    for e in entries:
        parts += [e, "", "---", ""]
    return "\n".join(parts)


INTENT_FIELDS = dict(Title="t", Change="c", **{"Scope boundary": "s"}, Baseline="b",
                     **{"Prediction (outcome — planner)": "po",
                        "Prediction (mechanism — coder)": "pm"},
                     **{"Finish line": "f", "Abort conditions": "a"})


def _intent(id_, ts, **extra):
    fields = dict(INTENT_FIELDS)
    fields.update(extra)
    return _entry(Kind="intent", ID=id_, Timestamp=ts, **fields)


def _run(argv):
    """main(argv) with its stdout; an argument error's exit and message are
    returned rather than raised (2026-10-17-07), so a flag that does not
    exist yet fails a check by assertion instead of ending the run."""
    from contextlib import redirect_stderr
    buf, err = io.StringIO(), io.StringIO()
    with redirect_stdout(buf), redirect_stderr(err):
        try:
            code = main(argv)
        except SystemExit as e:
            code = e.code
    return code, buf.getvalue() + err.getvalue()


def _fixture_forager(entries_by_file, audits_rows=(), prompts=None):
    """A Forager-like repository: record and prompts on branch 'rec', the
    audit index on branch 'pre'. Returns (path, rec_commit, pre_commit)."""
    repo = Path(tempfile.mkdtemp())
    files = dict(entries_by_file)
    for name, text in (prompts or {}).items():
        files[f"prompts/preserved/{name}"] = text
    rec = _commit_branch(repo, "rec", files)
    audits = "# Audits\n\n| Date | Scope | File |\n|---|---|---|\n" + "".join(
        f"| {d} | {s} | `{f}` |\n" for d, s, f in audits_rows)
    pre = _commit_branch(repo, "pre", {"docs/audits/README.md": audits})
    return repo, rec, pre


def _fixture_forecast(decisions=(), audits_rows=(), dispatches=None, log_rows=()):
    repo = Path(tempfile.mkdtemp())
    dec = ("# Decision log\n\n| ID | Date | Decision | Reason | Alternatives considered | Supersedes |\n"
           "| --- | --- | --- | --- | --- | --- |\n" + "".join(
               f"| {i} | {d} | {text} | r | a | {sup} |\n" for i, d, text, sup in decisions))
    audits = "# Audits\n\n| Date | Record | File |\n|---|---|---|\n" + "".join(
        f"| {d} | {s} | `{f}` |\n" for d, s, f in audits_rows)
    start = ("# Start here\n\n## Where things stand\n\nThe prose above the log mentions zebrafish too.\n\n"
             "| Date | Note | Ref |\n| --- | --- | --- |\n"
             "| 2026-09-08 | a zebrafish row in the maintained prose | p |\n\n"
             "## Session log\n\n| Date | What was done | What is next |\n| --- | --- | --- |\n" + "".join(
                 f"| {d} | {w} | {n} |\n" for d, w, n in log_rows))
    files = {"docs/planning/DECISIONS.md": dec, "docs/audits/README.md": audits,
             "docs/planning/START_HERE.md": start}
    for name, text in (dispatches or {}).items():
        files[f"docs/dispatch/{name}"] = text
    main_commit = _commit_branch(repo, "main", files)
    return repo, main_commit


def _base_args(forager=None, forecast=None):
    """r1-r7 run through the Forager preset (2026-10-17-07)."""
    args = ["--no-fetch", "--preset", "forager"]
    if forager:
        args += ["--repo", f"forager={forager}", "--ref", "forager=rec",
                 "--ref", "forager audits=pre"]
    if forecast:
        args += ["--repo", f"forecast={forecast}", "--ref", "forecast=main"]
    return args


def render_check():
    print("records_lookup.py --render-check")
    failures = []

    def check(name, expect_fail_msg, fn):
        print(f"\n[{name}] expected failure mode if broken: {expect_fail_msg}")
        try:
            fn()
            print(f"[{name}] PASS")
        except Exception as e:
            print(f"[{name}] FAIL: {e!r}")
            failures.append(name)

    def r1():
        e1 = _intent("2026-09-28-01", "2026-09-30T00:00:00Z")
        e2 = _entry(Kind="decision", ID="2026-09-28-02", Timestamp="2026-10-01T00:00:00Z",
                    Title="pinch zoom", Notes="Written by the test.")
        repo, rec, _ = _fixture_forager({"RECORD.md": _record(e1, e2)})
        code, out = _run(["show", "-02"] + _base_args(forager=repo))
        lines = out.splitlines()
        cite = [l for l in lines if l.startswith("citation: forager rec@")]
        assert cite, f"show printed no citation line: {out!r}"
        span = cite[0].rsplit(" ", 1)[1]
        assert span.startswith("RECORD.md:"), f"citation names no file and lines: {cite[0]!r}"
        a, b = (int(x) for x in span.split(":", 1)[1].split("-"))
        source = _git(repo, "show", f"{rec}:RECORD.md").splitlines()[a - 1:b]
        body = lines[lines.index(cite[0]) + 1:lines.index(cite[0]) + 1 + len(source)]
        assert body == source and any("pinch zoom" in l for l in body), (
            f"show's text is not the cited lines verbatim: {body!r} vs {source!r}")

    check("r1_show_verbatim_with_citation",
          "show does not print the entry verbatim under a citation that git show confirms",
          r1)

    def r2():
        e = [_intent("2026-09-28-01", "2026-09-30T00:00:00Z"),
             _entry(Kind="continuation", ID="2026-09-28-02", Timestamp="2026-10-01T00:00:00Z",
                    Continues="2026-09-28-01", Notes="n"),
             _entry(Kind="terminal", ID="2026-09-28-03", Timestamp="2026-10-02T00:00:00Z",
                    Closes="2026-09-28-01 (the test)", Outcome="completed", Observed="o",
                    Deviations="d"),
             _entry(Kind="correction", ID="2026-09-28-04", Timestamp="2026-10-03T00:00:00Z",
                    Corrects="2026-09-28-01, its title", Notes="n"),
             _entry(Kind="decision", ID="2026-09-28-05", Timestamp="2026-10-04T00:00:00Z",
                    Supersedes="2026-09-28-01, its scope", Notes="n")]
        repo, _, _ = _fixture_forager({"RECORD.md": _record(*e)})
        code, out = _run(["links", "2026-09-28-01"] + _base_args(forager=repo))
        for field, src in [("Continues", "02"), ("Closes", "03"), ("Corrects", "04"),
                           ("Supersedes", "05")]:
            hit = [l for l in out.splitlines()
                   if f"{field} 2026-09-28-{src}" in l and "forager rec@" in l]
            assert hit, f"links does not list the {field} link from -{src} with a citation: {out!r}"
        code, out = _run(["links", "2026-09-28-03"] + _base_args(forager=repo))
        assert any("names: Closes 2026-09-28-01" in l and "forager rec@" in l
                   for l in out.splitlines()), f"links does not list what -03 names: {out!r}"

    check("r2_links_each_type",
          "links misses a Continues, Closes, Corrects or Supersedes link, or what an entry names",
          r2)

    def r3():
        term = "zebrafish"
        e1 = _intent("2026-09-28-01", "2026-09-01T00:00:00Z", Change=f"a {term} change")
        e2 = _entry(Kind="decision", ID="2026-09-28-02", Timestamp="2026-10-05T00:00:00Z",
                    Title=f"later {term} ruling", Supersedes="2026-09-28-01", Notes="n")
        fr, _, _ = _fixture_forager({"RECORD.md": _record(e1, e2)},
                                    audits_rows=[("2026-09-02", f"a {term} audit", "a.md")],
                                    prompts={"2026-09-03-01.md": f"a {term} dispatch\n"})
        fc, _ = _fixture_forecast(decisions=[("D7", "2026-09-04", f"a {term} decision", "")],
                                  audits_rows=[("2026-09-05", f"a {term} review", "r.md")],
                                  dispatches={"2026-09-06-x.md": f"a {term} task\n"},
                                  log_rows=[("2026-09-07", f"{term} work", "next")])
        code, out = _run(["search", term] + _base_args(forager=fr, forecast=fc))
        for label in ["forager record", "forager audits", "forager prompts", "forecast decisions",
                      "forecast audits", "forecast dispatch", "forecast session log"]:
            assert any(l.startswith("20") and f" {label} " in l for l in out.splitlines()), (
                f"search found no hit in {label}: {out!r}")
        assert "maintained prose" not in out, (
            "search read a dated row from START_HERE.md's prose, not only the session log")
        dated = [l[:10] for l in out.splitlines() if l[:2] == "20"]
        assert dated == sorted(dated, reverse=True), f"hits not newest first: {dated}"
        assert any("superseded by 2026-09-28-02" in l for l in out.splitlines()), (
            f"search shows no explicit Supersedes link beside the superseded hit: {out!r}")

    check("r3_search_seven_sources_newest_first",
          "search misses a source, reads the session log's prose, is not newest first, "
          "or shows no Supersedes link",
          r3)

    def r4():
        e = [_intent("2026-09-28-01", "2026-09-30T00:00:00Z"),
             _intent("2026-09-28-02", "2026-09-30T00:00:00Z"),
             _intent("2026-09-28-03", "2026-09-30T00:00:00Z"),
             _intent("2026-09-28-04", "2026-09-30T00:00:00Z"),
             _entry(Kind="terminal", ID="2026-09-28-05", Timestamp="2026-10-01T00:00:00Z",
                    Closes="2026-09-28-01", Outcome="completed", Observed="o", Deviations="d"),
             _entry(Kind="outcome", ID="2026-09-28-06", Timestamp="2026-10-01T00:00:00Z",
                    Closes="2026-09-28-02 (a note)", Title="t", Notes="n"),
             _entry(Kind="continuation", ID="2026-09-28-07", Timestamp="2026-10-01T00:00:00Z",
                    Continues="2026-09-28-03", Notes="n")]
        repo, _, _ = _fixture_forager({"RECORD.md": _record(*e)})
        code, out = _run(["open"] + _base_args(forager=repo))
        opened = sorted(l.split()[2] for l in out.splitlines() if l.startswith("open intent: "))
        assert opened == ["2026-09-28-03", "2026-09-28-04"], f"open listed {opened}: {out!r}"
        assert "open intents: 2" in out, f"open printed no count: {out!r}"

    check("r4_open_intents",
          "open lists a closed intent (by terminal, or by outcome with Closes) or misses an open one",
          r4)

    def r5():
        sep = _record(_intent("2026-09-28-09", "2026-09-30T00:00:00Z"), title="Record, 2026-09")
        octo = _record(_intent("2026-09-28-05", "2026-10-01T00:00:00Z"),
                       _intent("2026-09-28-05", "2026-10-02T00:00:00Z"), title="Record, 2026-10")
        repo, rec, _ = _fixture_forager({"RECORD.md": "# RECORD.md\n\nThe index.\n",
                                         "records/2026-09.md": sep, "records/2026-10.md": octo})
        code, out = _run(["next-id"] + _base_args(forager=repo))
        assert f"next free ID: 2026-09-28-10 (read at rec@{rec[:8]})" in out, (
            f"next-id did not read every month or name its commit: {out!r}")
        assert "warning: duplicate ID 2026-09-28-05" in out, f"no duplicate warning: {out!r}"

    check("r5_next_id_across_months_with_duplicates",
          "next-id reads only the current month, omits the commit read, or misses a duplicate",
          r5)

    def r6():
        repo, _, _ = _fixture_forager({"RECORD.md": _record(
            _intent("2026-09-28-01", "2026-09-30T00:00:00Z"),
            _entry(Kind="decision", ID="2026-09-28-02", Timestamp="2026-10-01T00:00:00Z",
                   Title="the owner's ruling", Notes="n"))})
        fc, _ = _fixture_forecast(decisions=[("D200", "2026-10-02",
                                              "Owner's ruling (Forager RECORD -02).", "")])
        code, out = _run(["show", "D200"] + _base_args(forager=repo, forecast=fc))
        assert any(l.startswith("citation: forecast main@") for l in out.splitlines()), (
            f"show D200 printed no forecast citation: {out!r}")
        assert any("Forager RECORD -02 -> 2026-09-28-02" in l and "forager rec@" in l
                   for l in out.splitlines()), f"the Forager reference was not resolved: {out!r}"

    check("r6_cross_repository_reference_resolves",
          "a forecast decision's 'Forager RECORD -NN' is not resolved to the Forager entry, cited",
          r6)

    def r7():
        repo, _, _ = _fixture_forager({"RECORD.md": _record(
            _intent("2026-09-28-01", "2026-09-30T00:00:00Z"))})
        args = _base_args(forager=repo) + ["--ref", "forager record=no-such-ref"]
        code, out = _run(["open"] + args)
        assert any("forager record" in l and "NOT READ" in l and "no-such-ref" in l
                   for l in out.splitlines()), f"an unreadable source was not reported: {out!r}"
        assert "open intents: 0" not in out and "open intents: unknown" in out, (
            f"open answered a count from a record it could not read: {out!r}")

    check("r7_unread_source_reported",
          "a source whose ref cannot be read is skipped silently instead of reported",
          r7)


    # c1-c8 (2026-10-17-07): sources from a config, for any repositories.
    # Written before the behaviour; all run through main().
    import json
    import os

    def plain_repo(files):
        repo = Path(tempfile.mkdtemp())
        _commit_branch(repo, "main", files)
        return repo

    def write_config(cfg):
        p = Path(tempfile.mkdtemp()) / "lookup.json"
        p.write_text(json.dumps(cfg))
        return str(p)

    def c1():
        repo = plain_repo({"RECORD.md": _record(
            _intent("2026-01-01-01", "2026-01-01T00:00:00Z"),
            _entry(Kind="decision", ID="2026-01-01-02", Timestamp="2026-01-01T01:00:00Z",
                   Title="lamp colour", Notes="n"))})
        code, out = _run(["show", "2026-01-01-02", "--repo", f"repo={repo}"])
        assert code == 0 and "citation: repo HEAD@" in out and "lamp colour" in out, (
            f"with no config, --repo's record was not read at HEAD: {out!r}")
        here = os.getcwd()
        try:
            os.chdir(repo)
            code, out = _run(["show", "2026-01-01-02"])
        finally:
            os.chdir(here)
        assert code == 0 and "lamp colour" in out, (
            f"with no config and no --repo, the current directory was not read: {out!r}")

    check("c1_default_reads_one_repository_at_head",
          "with no config the tool does not read the given (or current) repository's record at HEAD",
          c1)

    NOTES_SHAPE = {"record_file": "LOG.md", "monthly_dir": None, "id_pattern": "^N\\d+$",
                   "id_token_pattern": "N\\d+", "backward_links": {"Follows": "first"},
                   "intent_kind": None, "terminal_kind": None, "continuation_kind": None,
                   "closing_kinds": [],
                   "kinds": {"note": {"required": ["Kind", "ID"]}}}

    def notes_repo(with_records_json=False):
        log = _record(_entry(Kind="note", ID="N1", Timestamp="2026-02-01T00:00:00Z", Body="first kestrel"),
                      _entry(Kind="note", ID="N2", Timestamp="2026-02-02T00:00:00Z", Body="kestrel nest"),
                      _entry(Kind="note", ID="N9", Timestamp="2026-02-03T00:00:00Z", Body="b",
                             Follows="N2 (the nest)"), title="LOG.md")
        files = {"LOG.md": log,
                 "LEDGER.md": "# Ledger\n\n| ID | Date | Entry |\n|---|---|---|\n"
                              "| X1 | 2026-02-04 | kestrel count, see N2 |\n",
                 "drafts/2026-02-05-plan.md": "a kestrel survey plan\n"}
        if with_records_json:
            files["records.json"] = json.dumps(NOTES_SHAPE)
        return plain_repo(files)

    def notes_config(shape):
        return {"repos": {"notes": None},
                "record": {"name": "notes log", "repo": "notes", "ref": "HEAD", "shape": shape,
                           "links": None, "replaced_by": {}},
                "tables": [{"name": "ledger", "repo": "notes", "ref": "HEAD", "path": "LEDGER.md",
                            "row_pattern": "^\\| (X\\d+) \\| (\\d{4}-\\d{2}-\\d{2})",
                            "id_pattern": "^X\\d+$", "record_reference": "see (N\\d+)"}],
                "folders": [{"name": "drafts", "repo": "notes", "ref": "HEAD", "path": "drafts"}]}

    def c2():
        repo = notes_repo()
        args = ["--config", write_config(notes_config(NOTES_SHAPE)), "--repo", f"notes={repo}"]
        code, out = _run(["links", "N2"] + args)
        assert code == 0 and any("named by: Follows N9" in l and "notes HEAD@" in l for l in out.splitlines()), (
            f"a configured record's own link field was not read: {out!r}")
        code, out = _run(["show", "X1"] + args)
        assert code == 0 and "citation: notes HEAD@" in out and "LEDGER.md:" in out, (
            f"a configured table's row was not shown by its ID: {out!r}")
        assert any("references: see N2 -> N2" in l for l in out.splitlines()), (
            f"a configured table's reference to the record was not resolved: {out!r}")
        code, out = _run(["search", "kestrel"] + args)
        for label in ("notes log", "ledger", "drafts"):
            assert any(f" {label} " in l for l in out.splitlines() if l[:2] == "20"), (
                f"search found no hit in the configured source {label}: {out!r}")

    check("c2_config_names_the_sources",
          "a config's record, table and folder, under its own names and ID scheme, are not read",
          c2)

    def c3():
        repo = notes_repo(with_records_json=True)
        cfg = notes_config(None)
        code, out = _run(["show", "N2", "--config", write_config(cfg), "--repo", f"notes={repo}"])
        assert code == 0 and "kestrel nest" in out and "LOG.md:" in out, (
            f"with no shape in the config, the record repository's records.json was not used: {out!r}")

    check("c3_shape_from_records_json_at_the_ref",
          "a record repository's records.json is not read when the lookup config gives no shape",
          c3)

    def c4():
        repo = notes_repo()
        args = ["--config", write_config(notes_config(NOTES_SHAPE)), "--repo", f"notes={repo}"]
        code, out = _run(["open"] + args)
        assert code == 1 and "open intents: unsupported" in out and "open intents: 0" not in out, (
            f"open on a record with no intent type answered a count: {out!r}")

    check("c4_open_unsupported_without_an_intent_type",
          "open on a record whose shape has no intent type prints a count instead of 'unsupported'",
          c4)

    def c5():
        repo = notes_repo()
        args = ["--config", write_config(notes_config(NOTES_SHAPE)), "--repo", f"notes={repo}"]
        code, out = _run(["next-id"] + args)
        assert code == 0 and "next free ID: N10 " in out, (
            f"next-id did not work for an ID scheme other than the dated one: {out!r}")

    check("c5_next_id_for_any_trailing_number",
          "next-id assumes YYYY-MM-DD-NN IDs and fails or misnumbers another scheme",
          c5)

    def c6():
        code, out = _run(["open", "--config", write_config({"tabels": []})])
        assert code == 2 and "tabels" in out, f"an unknown config key was not refused by name: {out!r}"
        cfg = notes_config(NOTES_SHAPE)
        cfg["tables"][0]["repo"] = "nowhere"
        code, out = _run(["open", "--config", write_config(cfg)])
        assert code == 2 and "nowhere" in out, f"a source naming an unknown repository was not refused: {out!r}"

    check("c6_config_refused_by_name",
          "an unknown key, or a source naming a repository the config does not define, is accepted",
          c6)

    def c7():
        code, out = _run(["open", "--print-config"])
        default = globals().get("DEFAULT_LOOKUP")
        assert default is not None and code == 0 and json.loads(out) == json.loads(json.dumps(default)), (
            f"--print-config does not print DEFAULT_LOOKUP: {out[:300]!r}")
        preset = Path(__file__).resolve().parent / "lookups" / "forager.json"
        assert preset.is_file(), "lookups/forager.json does not exist"
        code, out = _run(["open", "--print-config", "--preset", "forager"])
        assert code == 0 and json.loads(out) == json.loads(preset.read_text()), (
            "--preset forager does not load lookups/forager.json")

    check("c7_print_config_and_preset",
          "--print-config does not print the default, or --preset forager does not load lookups/forager.json",
          c7)

    def c8():
        fc, _ = _fixture_forecast(decisions=[("D1", "2026-09-04", "x", "")])
        _commit_branch(fc, "other", {"docs/planning/DECISIONS.md":
                                     "# Decision log\n\n| ID | Date | Decision |\n|---|---|---|\n"
                                     "| D2 | 2026-09-05 | y |\n"})
        code, out = _run(["show", "D2", "--no-fetch", "--preset", "forager", "--repo", f"forecast={fc}",
                          "--ref", "forecast decisions=other", "--ref", "forecast=main"])
        assert any(l.startswith("source forecast decisions: forecast other@") for l in out.splitlines()), (
            f"a source's own --ref did not win over its repository's: {out!r}")
        assert any(l.startswith("source forecast audits: forecast main@") for l in out.splitlines()), (
            f"a repository-wide --ref did not reach that repository's other sources: {out!r}")
        assert code == 0 and "| D2 |" in out, f"D2 was not read at the overriding ref: {out!r}"

    check("c8_ref_overrides_source_over_repository",
          "--ref by repository does not reach every source in it, or does not yield to a source's own --ref",
          c8)

    print(f"\n{'FAIL' if failures else 'PASS'}: {len(failures)} of "
          f"{15} checks failed{': ' + ', '.join(failures) if failures else ''}")
    return 1 if failures else 0


if __name__ == "__main__":
    if "--render-check" in sys.argv:
        sys.exit(render_check())
    sys.exit(main(sys.argv[1:]))
