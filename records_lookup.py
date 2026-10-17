#!/usr/bin/env python3
"""records_lookup.py -- read-only lookup over Forager's and forager-forecast's
records: specs/2026-10-16-records-lookup.md, built under RECORD.md
2026-10-17-03.

  records_lookup.py COMMAND [ARGS] --forager PATH --forecast PATH [options]

  show ID       an entry verbatim, with its citation (ID: a full Forager ID,
                a short form -NNNN, or a forager-forecast D-number)
  links ID      what names this entry, and what it names
  search WORDS  every source, newest first, each hit cited
  open          Forager intents with no closing entry
  next-id       the next free Forager ID across every record file

Every answer carries repository, ref, commit, file and line. Sources are
read with git show and git ls-tree at a resolved commit, after git fetch
for origin/ refs, and never checked out or written. A source that cannot
be read is reported as NOT READ, never skipped.

Default refs (the spec's per-source decision, each overridable):
  Forager record and prompts  origin/records-after-173
  Forager audit index         origin/pre-main
  forager-forecast            origin/main

A Continues or Closes value is read by the ID it starts with, since
Forager's practice sometimes follows the ID with a parenthesis; Corrects
and Supersedes are read for every ID they carry.
"""
import argparse
import io
import re
import subprocess
import sys
import tempfile
from collections import Counter
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_record as cr  # noqa: E402

ID_TOKEN = cr.ENTRY_ID_TOKEN_RE
LEADING_ONLY = ("Continues", "Closes")
LINK_FIELDS = ("Continues", "Closes", "Corrects", "Supersedes")
FORAGER_REF_RE = re.compile(r"Forager RECORD (-\d+)")
D_ID_RE = re.compile(r"^D\d+$")
SHORT_RE = re.compile(r"^-\d+$")
DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")
MONTH_NAME_RE = re.compile(r"^\d{4}-\d{2}\.md$")


def _run_git(repo, *args):
    return subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)


class Source:
    """One repository at one ref, resolved to a commit."""

    def __init__(self, repo_label, repo, ref, fetch):
        self.repo_label, self.repo, self.ref = repo_label, repo, ref
        self.commit, self.note, self.error = None, "", ""
        if repo is None:
            self.error = f"no --{repo_label} path given"
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
    def __init__(self, args):
        fetch = not args.no_fetch
        self.sources = {
            "forager record": Source("forager", args.forager, args.forager_record_ref, fetch),
            "forager prompts": Source("forager", args.forager, args.forager_prompts_ref, fetch),
            "forager audits": Source("forager", args.forager, args.forager_audits_ref, fetch),
            "forecast": Source("forecast", args.forecast, args.forecast_ref, fetch),
        }
        self.entries, self.read_errors = [], []
        rec = self.sources["forager record"]
        if rec.commit:
            files = []
            if rec.show(cr.RECORD_NAME) is not None:
                files.append(cr.RECORD_NAME)
            files += sorted(f"records/{n}" for n in rec.ls("records") if MONTH_NAME_RE.match(n))
            if not files:
                rec.error = f"no RECORD.md or records/YYYY-MM.md at {rec.ref}"
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
        self.decisions = self._rows("forecast", "docs/planning/DECISIONS.md",
                                    r"^\| (D\d+) \| (\d{4}-\d{2}-\d{2})", "forecast decisions")
        self.forecast_audits = self._rows("forecast", "docs/audits/README.md",
                                          r"^\| ()(\d{4}-\d{2}-\d{2})", "forecast audits")
        self.forager_audits = self._rows("forager audits", "docs/audits/README.md",
                                         r"^\| ()(\d{4}-\d{2}-\d{2})", "forager audits")
        self.session_log = self._rows("forecast", "docs/planning/START_HERE.md",
                                      r"^\| ()(\d{4}-\d{2}-\d{2})", "forecast session log",
                                      section="## Session log")

    def _rows(self, source_name, path, pattern, label, section=None):
        src = self.sources[source_name]
        if not src.commit:
            return []
        text = src.show(path)
        if text is None:
            self.read_errors.append(f"{label}: {path} not found at {src.ref}")
            return []
        rows, inside = [], section is None
        for n, line in enumerate(text.split("\n"), 1):
            if section is not None and line.startswith("## "):
                inside = line.strip() == section
                continue
            m = re.match(pattern, line) if inside else None
            if m:
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                rows.append({"id": m.group(1), "date": m.group(2), "text": line, "cells": cells,
                             "label": label, "cite": src.cite(path, n)})
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
            if base not in LINK_FIELDS:
                continue
            toks = ID_TOKEN.findall(value)
            if base in LEADING_ONLY:
                m = ID_TOKEN.match(value.strip())
                toks = [m.group(0)] if m else []
            out += [(base, t) for t in toks]
        return out


def cmd_show(r, key):
    if D_ID_RE.match(key):
        rows = [d for d in r.decisions if d["id"] == key]
        if not rows:
            print(f"not found: {key} in forecast decisions")
            return 1
        d = rows[0]
        print(f"citation: {d['cite']}")
        print(d["text"])
        for ref in FORAGER_REF_RE.findall(d["text"]):
            e, msg = r.resolve(ref)
            print(f"references: Forager RECORD {ref} -> {e['id']} — {e['cite']}" if e
                  else f"references: Forager RECORD {ref} -> {msg}")
        return 0
    if _record_unread(r, f"show {key}"):
        return 1
    e, msg = r.resolve(key)
    if not e:
        print(msg)
        return 1
    print(f"citation: {e['cite']}")
    print(e["text"])
    num = "-" + e["id"].rsplit("-", 1)[1]
    for d in r.decisions:
        if num in FORAGER_REF_RE.findall(d["text"]):
            print(f"referenced by: forecast {d['id']} — {d['cite']}")
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
                if target == e["id"] and field in ("Supersedes", "Corrects"):
                    verb = "superseded by" if field == "Supersedes" else "corrected by"
                    extra.append(f"    {verb} {other['id']} — {other['cite']}")
        for field, target in r.links_from(e):
            if field in ("Supersedes", "Corrects"):
                extra.append(f"    {field.lower()} {target}")
        hits.append((e["date"], "forager record", e["cite"], f"{e['id']} {title[:120]}", extra))
    for rows in (r.forager_audits, r.decisions, r.forecast_audits, r.session_log):
        for row in _hits_text(rows, words):
            extra = []
            if row["label"] == "forecast decisions":
                sup = row["cells"][5] if len(row["cells"]) > 5 else ""
                if sup and sup.lower() not in ("none", "-", ""):
                    extra.append(f"    supersedes {sup[:120]}")
                for other in r.decisions:
                    sup_o = other["cells"][5] if len(other["cells"]) > 5 else ""
                    if other is not row and re.search(rf"\b{re.escape(row['id'])}\b", sup_o):
                        extra.append(f"    superseded by {other['id']} — {other['cite']}")
            hits.append((row["date"], row["label"], row["cite"], row["text"][:140], extra))
    for name, directory, label in (("forager prompts", "prompts/preserved", "forager prompts"),
                                   ("forecast", "docs/dispatch", "forecast dispatch")):
        src = r.sources[name]
        if not src.commit:
            continue
        for fname in src.ls(directory):
            text = src.show(f"{directory}/{fname}") or ""
            if all(w in text.lower() for w in words):
                lines = text.split("\n")
                n = next((i for i, l in enumerate(lines, 1) if any(w in l.lower() for w in words)), 1)
                m = DATE_RE.match(fname)
                hits.append((m.group(1) if m else "", label, src.cite(f"{directory}/{fname}", n),
                             lines[n - 1][:140], []))
    hits.sort(key=lambda h: h[0], reverse=True)
    for date, label, cite, excerpt, extra in hits:
        print(f"{date or '(undated)'}  {label}  {cite}  {excerpt}")
        for x in extra:
            print(x)
    print(f"hits: {len(hits)}")
    return 0


def _record_unread(r, what):
    """True, after saying so, when the Forager record could not be read: an
    answer drawn from it would be a plausible value standing in for
    nothing."""
    if r.sources["forager record"].commit and r.entries:
        return False
    print(f"{what}: unknown, the Forager record was not read")
    return True


def cmd_open(r):
    if _record_unread(r, "open intents"):
        return 1
    closed = set()
    for e in r.entries:
        if e["kind"] in ("terminal", "outcome"):
            m = ID_TOKEN.match(e["fields"].get("Closes", "").strip())
            if m:
                closed.add(m.group(0))
    opened = [e for e in r.entries if e["kind"] == "intent" and e["id"] not in closed]
    for e in opened:
        print(f"open intent: {e['id']} — {e['cite']}")
    print(f"open intents: {len(opened)}")
    return 0


def cmd_next_id(r):
    src = r.sources["forager record"]
    if _record_unread(r, "next free ID"):
        return 1
    counts = Counter(e["id"] for e in r.entries)
    for eid, n in sorted(counts.items()):
        if n > 1:
            where = ", ".join(e["cite"] for e in r.entries if e["id"] == eid)
            print(f"warning: duplicate ID {eid} ({n} times): {where}")
    prefix = r.entries[-1]["id"][:10]
    nums = [e["id"][11:] for e in r.entries if e["id"][:10] == prefix and e["id"][11:].isdigit()]
    top = max(nums, key=int)
    print(f"next free ID: {prefix}-{int(top) + 1:0{max(2, len(top))}d} "
          f"(read at {src.ref}@{src.commit[:8]})")
    return 0


def main(argv=None):
    p = argparse.ArgumentParser(prog="records_lookup.py", description=__doc__.split("\n")[0])
    p.add_argument("command", choices=["show", "links", "search", "open", "next-id"])
    p.add_argument("args", nargs="*")
    p.add_argument("--forager")
    p.add_argument("--forecast")
    p.add_argument("--forager-record-ref", default="origin/records-after-173")
    p.add_argument("--forager-prompts-ref", default="origin/records-after-173")
    p.add_argument("--forager-audits-ref", default="origin/pre-main")
    p.add_argument("--forecast-ref", default="origin/main")
    p.add_argument("--no-fetch", action="store_true")
    args = p.parse_intermixed_args(argv)
    r = Records(args)
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
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = main(argv)
    return code, buf.getvalue()


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
    args = ["--no-fetch"]
    if forager:
        args += ["--forager", str(forager), "--forager-record-ref", "rec",
                 "--forager-prompts-ref", "rec", "--forager-audits-ref", "pre"]
    if forecast:
        args += ["--forecast", str(forecast), "--forecast-ref", "main"]
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
        args = _base_args(forager=repo)
        args[args.index("--forager-record-ref") + 1] = "no-such-ref"
        code, out = _run(["open"] + args)
        assert any("forager record" in l and "NOT READ" in l and "no-such-ref" in l
                   for l in out.splitlines()), f"an unreadable source was not reported: {out!r}"
        assert "open intents: 0" not in out and "open intents: unknown" in out, (
            f"open answered a count from a record it could not read: {out!r}")

    check("r7_unread_source_reported",
          "a source whose ref cannot be read is skipped silently instead of reported",
          r7)

    print(f"\n{'FAIL' if failures else 'PASS'}: {len(failures)} of "
          f"{7} checks failed{': ' + ', '.join(failures) if failures else ''}")
    return 1 if failures else 0


if __name__ == "__main__":
    if "--render-check" in sys.argv:
        sys.exit(render_check())
    sys.exit(main(sys.argv[1:]))
