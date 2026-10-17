#!/usr/bin/env python3
"""records_lookup.py -- read-only lookup over Forager's and forager-forecast's
records, as specs/2026-10-16-records-lookup.md sets out (RECORD.md
2026-10-17-03). STUB: the tests below are written first; main() answers
nothing yet.
"""
import io
import subprocess
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path


def main(argv=None):
    return 2


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
        assert "The prose above the log" not in out, "search read START_HERE.md's prose, not only the log"
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
