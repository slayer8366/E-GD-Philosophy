"""check_prompts.py -- existence and binding check for prompts/.

Answers existence and binding questions only, nothing about content:

  - every RECORD.md entry that records a dispatch (carries a
    **Dispatch-file:** field) names a file that exists under prompts/
  - every file that physically exists under prompts/ is named by
    exactly one such entry -- unclaimed files and duplicate claims on
    the same file are both reported as errors, as distinct shapes
  - counts of prompts/preserved/ and prompts/recovered/ are reported
    separately, by listing each subdirectory, never by trusting a
    claim written inside an entry

This script does NOT and cannot verify that a stored file holds the
text actually dispatched to an agent. That fact lives outside this
repository, in whatever produced the dispatch, and nothing checkable
from inside a git working tree can confirm it. Do not read a passing
run of this script as evidence the stored text is accurate -- it is
evidence only that a file exists where an entry says one should, and
that no entry and no file are left dangling. See RECORD.md entry
2026-08-13-09 for the "recovered versus preserved" distinction this
script depends on: preserved/ holds a prompt captured verbatim at
dispatch time; recovered/ holds one reconstructed afterward from a
transcript. The directory is the single source of truth for that
distinction, not a second field that could drift out of sync with it.

One convention is accepted for a file claimed by more than one entry:
an intent entry and the terminal entry that closes it (its own
**Closes:** field naming the intent's **ID**) may both carry a
**Dispatch-file:** field pointing at the same file -- that is one
dispatch referenced twice, not two claims on one prompt. The pairing
is read from each entry's own Kind and Closes fields, never inferred
from ID adjacency. Any other file claimed by more than one entry,
including two entries that are both intents, both terminals, or a
terminal whose Closes does not name the other claimant, is still
reported as a violation. Decided at RECORD.md entry 2026-08-14-01,
which found 2026-08-13-13 (intent) and 2026-08-13-14 (its terminal)
both legitimately claiming prompts/preserved/2026-08-13-13.md and
this script, unaware of the convention, reporting it as a defect.

Reuses check_record.split_entries and check_record.parse_fields
unmodified, via `import check_record as cr`. This carries forward,
knowingly and not fixed here, the defect documented in check_record.py's
own header: split_entries() finds its '## Entries' heading by raw
substring search, with no markdown awareness, so prose naming that
heading before the real one produces a phantom entry. The same logic
is duplicated in OSCam's ledger_validator_core.py; fixing either is out
of scope for this task. Does not reuse validate_entries -- this script
asks a different question (dispatch-file binding) than that function
answers (intent/terminal shape and sentinel handling), and duplicating
its required-field logic here would only reintroduce a second copy of
rules that already live in check_record.py.
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_record as cr

RECORD_NAME = "RECORD.md"
PROMPTS_DIR = "prompts"
DISPATCH_FIELD = "Dispatch-file"
PROVENANCE_DIRS = ("preserved", "recovered")


def dispatch_claims(text):
    """List of (entry_id, dispatch_file_value) for every entry in
    RECORD.md that carries a Dispatch-file field, in entry order.
    entry_id is '' if the entry itself has no ID (already a distinct
    defect check_record.py's own validator reports separately)."""
    claims = []
    for block in cr.split_entries(text):
        fields = cr.parse_fields(block)
        value = fields.get(DISPATCH_FIELD, "").strip()
        if not value:
            continue
        claims.append((fields.get("ID", "").strip(), value))
    return claims


def entry_kind_closes(text):
    """Map entry_id -> (kind, closes) for every RECORD.md entry that
    carries an ID field. kind and closes are taken directly from that
    entry's own fields -- closes is '' for intent entries and for any
    terminal with no Closes field. This is the only place ID adjacency
    could have been used to guess a pairing and deliberately is not:
    the mapping is looked up by the literal Closes text, never by
    comparing ID strings to each other."""
    mapping = {}
    for block in cr.split_entries(text):
        fields = cr.parse_fields(block)
        entry_id = fields.get("ID", "").strip()
        if not entry_id:
            continue
        mapping[entry_id] = (
            fields.get("Kind", "").strip(),
            fields.get("Closes", "").strip(),
        )
    return mapping


def is_intent_terminal_pair(ids, kind_closes):
    """True if ids (the claimants of one Dispatch-file value) is
    exactly one intent entry and the terminal entry that closes it.
    ids containing a "(no ID)" placeholder, or any entry_id absent
    from kind_closes, can never match -- both fall through to False,
    so this only ever legalizes a claim between two well-formed,
    genuinely paired entries, not a loosening of the general rule."""
    if len(ids) != 2:
        return False
    a, b = ids
    ka, kb = kind_closes.get(a), kind_closes.get(b)
    if ka is None or kb is None:
        return False
    if ka[0] == "intent" and kb[0] == "terminal" and kb[1] == a:
        return True
    if kb[0] == "intent" and ka[0] == "terminal" and ka[1] == b:
        return True
    return False


def files_on_disk(repo_dir):
    """Set of paths relative to prompts/, for every regular file found
    under prompts/preserved/ and prompts/recovered/. A file placed
    directly under prompts/ (outside either subdirectory) is not
    counted as preserved or recovered by this walk and is reported
    separately -- provenance is mandatory, not inferred."""
    prompts_root = Path(repo_dir) / PROMPTS_DIR
    found = set()
    stray = set()
    if not prompts_root.is_dir():
        return found, stray
    for entry in sorted(prompts_root.rglob("*")):
        if not entry.is_file():
            continue
        rel = entry.relative_to(prompts_root)
        if rel.parts and rel.parts[0] in PROVENANCE_DIRS:
            found.add(rel.as_posix())
        else:
            stray.add(rel.as_posix())
    return found, stray


def check_binding(repo_dir=None):
    """(ok, errors, report_lines, counts). Pure existence/binding check,
    no content comparison. counts is {'preserved': n, 'recovered': n}."""
    repo_dir = Path(repo_dir) if repo_dir else HERE
    errors = []
    report_lines = []

    files = cr.record_files(repo_dir)
    if not files:
        return False, [f"{RECORD_NAME} does not exist in {repo_dir}"], [], {}

    # Every record file is read: RECORD.md and any records/YYYY-MM.md
    # (2026-10-17, RECORD.md 2026-10-17-01).
    claims = []
    kind_closes = {}
    for rel in files:
        text = (repo_dir / rel).read_text()
        claims += dispatch_claims(text)
        kind_closes.update(entry_kind_closes(text))
    on_disk, stray = files_on_disk(repo_dir)

    claimed_paths = {}
    duplicate_errors = []
    for entry_id, value in claims:
        claimed_paths.setdefault(value, []).append(entry_id or "(no ID)")
    for value, ids in claimed_paths.items():
        if len(ids) > 1 and not is_intent_terminal_pair(ids, kind_closes):
            duplicate_errors.append(
                f"{value!r} is claimed by more than one entry's "
                f"{DISPATCH_FIELD!r} field: {', '.join(ids)}")
    errors.extend(duplicate_errors)

    missing = []
    for entry_id, value in claims:
        if value not in on_disk:
            missing.append(
                f"entry {entry_id or '(no ID)'}: {DISPATCH_FIELD!r} names "
                f"{value!r}, which does not exist under {PROMPTS_DIR}/")
    errors.extend(missing)

    claimed_set = set(claimed_paths)
    orphaned_files = sorted(on_disk - claimed_set)
    for rel in orphaned_files:
        errors.append(
            f"{PROMPTS_DIR}/{rel} exists but no RECORD.md entry's "
            f"{DISPATCH_FIELD!r} field names it")

    if stray:
        errors.append(
            f"file(s) present directly under {PROMPTS_DIR}/, outside "
            f"{PROVENANCE_DIRS!r}, with no provenance directory: "
            f"{sorted(stray)}")

    counts = {name: 0 for name in PROVENANCE_DIRS}
    for rel in on_disk:
        top = rel.split("/", 1)[0]
        if top in counts:
            counts[top] += 1

    report_lines.append(f"dispatch-recording entries found: {len(claims)}")
    report_lines.append(f"files under {PROMPTS_DIR}/: "
                         + ", ".join(f"{k}={v}" for k, v in counts.items()))
    if stray:
        report_lines.append(f"stray files with no provenance directory "
                             f"(reported, always an error): {sorted(stray)}")

    return not errors, errors, report_lines, counts


def main():
    ok, errors, report_lines, counts = check_binding()

    for line in report_lines:
        print(line)
    print()

    if ok:
        print(f"PASS: every dispatch-recording entry's {DISPATCH_FIELD!r} "
              f"resolves to a real file, every file under {PROMPTS_DIR}/ "
              f"is claimed by exactly one entry (or by an intent/terminal "
              f"pair closing it), no orphans in either "
              f"direction. This checks existence and binding only -- it "
              f"does not and cannot verify stored text matches what was "
              f"actually dispatched.")
        return 0

    print(f"FAIL: {len(errors)} binding violation(s)")
    for e in errors:
        print(" -", e)
    return 1


def render_check():
    """Self-tests, added 2026-10-17 (RECORD.md 2026-10-17-01); written
    before monthly reading existed. Every fixture lives under
    tempfile.mkdtemp()."""
    import tempfile
    print("check_prompts.py --render-check")
    failures = []

    def check(name, expect_fail_msg, fn):
        print(f"\n[{name}] expected failure mode if broken: {expect_fail_msg}")
        try:
            fn()
            print(f"[{name}] PASS")
        except Exception as e:
            print(f"[{name}] FAIL: {e!r}")
            failures.append(name)

    def intent(id_, dispatch, ts="2026-10-02T00:00:00Z"):
        return "\n".join([
            "**Kind:** intent", f"**ID:** {id_}", f"**Timestamp:** {ts}",
            "**Title:** t", "**Change:** c", "**Scope boundary:** s",
            "**Baseline:** b", "**Prediction (outcome — planner):** po",
            "**Prediction (mechanism — coder):** pm", "**Finish line:** f",
            "**Abort conditions:** a", f"**Dispatch-file:** {dispatch}"])

    def record(title, *entries):
        parts = [f"# {title}", "", "## Entries", "", "---", ""]
        for e in entries:
            parts += [e, "", "---", ""]
        return "\n".join(parts)

    def prompt(tmp, name):
        d = Path(tmp) / PROMPTS_DIR / "preserved"
        d.mkdir(parents=True, exist_ok=True)
        (d / name).write_text("a dispatch\n")

    def p1():
        tmp = Path(tempfile.mkdtemp())
        (tmp / RECORD_NAME).write_text(record("RECORD.md", intent("2026-10-02-01", "preserved/x.md")))
        prompt(tmp, "x.md")
        ok, errors, _, _ = check_binding(tmp)
        assert ok, f"a single-file record binding its prompt failed: {errors}"

    check("p1_single_file_binding_unchanged",
          "a single RECORD.md claiming its one preserved prompt is reported as a violation",
          p1)

    def p2():
        tmp = Path(tempfile.mkdtemp())
        (tmp / RECORD_NAME).write_text("# RECORD.md\n\nThe index; entries are in records/.\n")
        (tmp / "records").mkdir()
        (tmp / "records" / "2026-10.md").write_text(
            record("Record, 2026-10", intent("2026-10-02-01", "preserved/y.md")))
        prompt(tmp, "y.md")
        ok, errors, _, _ = check_binding(tmp)
        assert ok, (f"a claim in a monthly file was not read; the prompt it "
                    f"claims reads as an orphan: {errors}")

    check("p2_claims_read_from_monthly_files",
          "a Dispatch-file claim in records/YYYY-MM.md is not read, so its prompt is reported orphaned",
          p2)

    # p3-p4 (2026-10-17-05): any repository, shaped by its records.json.
    import inspect, io, json
    from contextlib import redirect_stdout

    def run_main(argv):
        assert inspect.signature(main).parameters, (
            "main() takes no arguments: the repository argument is missing")
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = main(argv)
        return code, buf.getvalue()

    def p3():
        tmp = Path(tempfile.mkdtemp())
        (tmp / "records.json").write_text(json.dumps(
            {"record_file": "LOG.md", "prompts_dir": "dispatches", "dispatch_field": "Prompt-file"}))
        (tmp / "LOG.md").write_text(record("LOG.md", intent("2026-10-02-01", "x").replace(
            "**Dispatch-file:** x", "**Prompt-file:** preserved/a.md")))
        d = tmp / "dispatches" / "preserved"
        d.mkdir(parents=True)
        (d / "a.md").write_text("a dispatch\n")
        code, out = run_main([str(tmp)])
        assert code == 0, f"a renamed record, prompts folder and dispatch field were not applied: {out!r}"
        (d / "b.md").write_text("unclaimed\n")
        code, out = run_main([str(tmp)])
        assert code == 1 and "dispatches/preserved/b.md" in out, (
            f"an unclaimed prompt in the configured folder was not reported: {out!r}")

    check("p3_repository_and_config",
          "check_prompts ignores the given repository or its records.json",
          p3)

    def p4():
        tmp = Path(tempfile.mkdtemp())
        (tmp / RECORD_NAME).write_text(record("RECORD.md", intent("2026-10-02-01", "preserved/x.md")))
        code, out = run_main([str(tmp), "--json"])
        data = json.loads(out)
        assert data["ok"] is False and any("x.md" in e for e in data["errors"]), (
            f"--json lacks ok or errors: {data}")

    check("p4_json_output",
          "--json does not print one JSON object carrying ok and errors",
          p4)

    print(f"\n{'FAIL' if failures else 'PASS'}: {len(failures)} of "
          f"{4} checks failed{': ' + ', '.join(failures) if failures else ''}")
    return 1 if failures else 0


if __name__ == "__main__":
    if "--render-check" in sys.argv:
        sys.exit(render_check())
    sys.exit(main())
