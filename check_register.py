"""check_register.py -- capture-only wrapper around checks.

Runs a check command, captures its real exit code, stdout, and
stderr, and appends one observation to REGISTER.md pairing the stated
expected failure mode with what was actually captured. Records; does
not judge. Whether the observation matches the expectation is Confirm
Failure Before Applying Fixes -- an agent's own judgment, every time,
never automated here. No comparison or pattern-matching logic exists
in this file, on purpose: a mechanical match against failure text
produces false blocks and teaches vague predictions.

Reuses check_record.py's check_append_only and check_history_append_only
for REGISTER.md's own append-only verification, rather than
reimplementing byte-prefix comparison here. Both already accept an
explicit record_name, so no refactor of check_record.py was needed --
confirmed before this file was written, not assumed. Does not reuse
split_entries/parse_fields/validate_entries: those assume RECORD.md's
intent/terminal entry shape (Kind, a required-field list per kind,
sentinels), which this file's flat observation log has no equivalent
of and does not need.

No insertion point is ever located by searching REGISTER.md's text
for a marker. New observations are appended at the literal end of the
file, opened in append mode. RECORD.md's own header hit a real defect
from exactly that kind of search -- split_entries()'s raw
text.find("## Entries") collided with prose that named the heading
before the real one. This file's append path has no equivalent search
to collide, by construction, not by carefulness alone.

Captured stdout/stderr is arbitrary program output and is treated as
hostile to this file's own syntax, not trusted to behave: every
captured line is indented four spaces before being written, so no
captured line can ever start with "**" at column 0 and be mistaken
for a real field line by a line-anchored reader. This matters
concretely: a check that wraps something which itself prints
REGISTER.md-shaped text (another entry, or this file's own content)
will have that text sitting inside its own entry as indented data,
not live field syntax. Grepping for a check name anchored to its own
field line (`^\\*\\*Check:\\*\\* name$`) is reliable because of this.
Grepping for the bare name as a substring is NOT made reliable by
this -- the name can still appear as ordinary indented data inside
some other entry's captured output, the same way any string can
appear anywhere in a free-text file. That is not a defect specific to
this tool; it is what grepping unstructured text always is. Anchor
the query if the distinction matters.
"""
import argparse
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_record as cr

REGISTER_NAME = "REGISTER.md"


def _indent(text):
    """Four-space-indent every line of captured output, so no captured
    line can start with '**' at column 0. An empty capture is written
    as an explicit indented marker, not an absent field -- absence and
    "captured nothing" are different facts and must stay distinguishable."""
    if not text:
        return "    (nothing captured)"
    lines = text.splitlines()
    return "\n".join("    " + line for line in lines)


def record_observation(check_name, expected_failure_mode, command, vacuous,
                        register_path=None):
    """Runs `command` (a list of argv) exactly as given -- no environment
    changes, no output redirection beyond capturing what subprocess.run
    already separates into stdout/stderr, no altered exit status.
    Appends one entry to REGISTER.md and returns (exit_code, stdout,
    stderr) unmodified, so a caller can use this exactly in place of
    running the command directly and get the same answer back.

    vacuous is supplied by the caller, never inferred from the
    captured output -- this function does not read stdout/stderr to
    decide whether the observation was vacuous; that is the caller's
    own knowledge of what it just ran."""
    register_path = Path(register_path) if register_path else (HERE / REGISTER_NAME)
    result = subprocess.run(command, capture_output=True, text=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    entry = (
        "---\n\n"
        f"**Check:** {check_name}\n\n"
        f"**Timestamp:** {timestamp}\n\n"
        f"**Expected failure mode:** {expected_failure_mode}\n\n"
        f"**Command:** {' '.join(command)}\n\n"
        f"**Exit code:** {result.returncode}\n\n"
        f"**Vacuous:** {'yes' if vacuous else 'no'}\n\n"
        f"**Stdout:**\n\n{_indent(result.stdout)}\n\n"
        f"**Stderr:**\n\n{_indent(result.stderr)}\n\n"
    )
    with open(register_path, "a") as f:
        f.write(entry)

    return result.returncode, result.stdout, result.stderr


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Run a check, capture what actually happened, and "
                    "append one observation to REGISTER.md. Records; "
                    "does not judge whether it matched the expectation.")
    ap.add_argument("--check-name", required=True)
    ap.add_argument("--expected", required=True, dest="expected_failure_mode")
    ap.add_argument("--vacuous", action="store_true")
    ap.add_argument("--register-path", default=None)
    ap.add_argument("command", nargs=argparse.REMAINDER,
                    help="the check command to run, e.g. -- python3 foo.py")
    args = ap.parse_args(argv)
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        ap.error("no command given to wrap")

    code, out, err = record_observation(
        args.check_name, args.expected_failure_mode, command, args.vacuous,
        register_path=args.register_path)

    # The wrapped check's own output is still shown -- wrapping it must
    # not make it disappear from whoever is watching this run.
    sys.stdout.write(out)
    sys.stderr.write(err)
    return code


if __name__ == "__main__":
    sys.exit(main())
