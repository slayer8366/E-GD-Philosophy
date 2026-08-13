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
    record_path = repo_dir / RECORD_NAME
    errors = []
    report_lines = []

    if not record_path.is_file():
        return False, [f"{RECORD_NAME} does not exist in {repo_dir}"], [], {}

    text = record_path.read_text()
    claims = dispatch_claims(text)
    on_disk, stray = files_on_disk(repo_dir)

    claimed_paths = {}
    duplicate_errors = []
    for entry_id, value in claims:
        claimed_paths.setdefault(value, []).append(entry_id or "(no ID)")
    for value, ids in claimed_paths.items():
        if len(ids) > 1:
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
              f"is claimed by exactly one entry, no orphans in either "
              f"direction. This checks existence and binding only -- it "
              f"does not and cannot verify stored text matches what was "
              f"actually dispatched.")
        return 0

    print(f"FAIL: {len(errors)} binding violation(s)")
    for e in errors:
        print(" -", e)
    return 1


if __name__ == "__main__":
    sys.exit(main())
