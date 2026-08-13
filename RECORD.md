# RECORD.md

E-GD-Philosophy's append-only task-record store. Validated by
`check_record.py` -- see that file, not this header, for the current
required-field list, sentinel vocabulary, and field-label text. That
split is deliberate: the header of an append-only file is frozen from
its first commit, and a prior version of this store learned, in the
entry below, that a header enumerating specifics goes stale the
moment those specifics change and can never be corrected in place --
only ever superseded by more text, never edited. `check_record.py`
is ordinary version-controlled code, not append-only, so it can carry
the specifics and actually stay current. This header states only
what should never need revising.

This file is append-only, enforced by `check_record.py`: no existing
line is ever removed or modified. Additions land at the end.

## Entry format

Two entry kinds. An **intent** entry is written before work begins.
A **terminal** entry closes exactly one intent, referenced by its
`ID` in a `Closes` field, and records what actually happened.

Entries are separated by bare `---` lines, found after the Entries
section heading below. Within an entry, fields use
`**Label:** value` syntax; a value runs from immediately after its
label line to the next label line or the entry's end, so it may span
multiple lines and paragraphs without any indentation convention.

Certain prediction fields in intent entries may carry a sentinel
value instead of real content, standing in for a prediction not yet
released or never intended to be authored. Which fields, which
sentinel strings, and what each means: `check_record.py`'s own
header and its `SENTINELS`/`SENTINEL_PREDICTION_FIELDS` constants.

## Entries

---

**Kind:** intent

**ID:** 2026-08-13-01

**Timestamp:** 2026-08-13T10:56:02Z

**Title:** Record store rebuilt after total loss of the prior store

**Change:** Create RECORD.md fresh. Record what was lost and why, and record that nothing before this entry is being reconstructed.

**Scope boundary:** This entry and its terminal. No prior entry is rebuilt. The philosophy amendments, PROTOCOL.md, and the remaining tooling are separate tasks and are restored from surviving text on their own merits, not as record entries.

**Baseline:** RECORD.md does not exist. E-GD-Philosophy on GitHub holds four commits: three from 2026-08-09 and 2026-08-10 carrying the 43-headword document set, and one adding DURABILITY.md. check_record.py was rebuilt at 7ffdd27 from a vendored copy of itself found in OSCam.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** As recorded in this task's report.

**Finish line:** Both entries written and validated by check_record.py, pushed to origin.

**Abort conditions:** If the dictated text cannot satisfy the validator, stop rather than editing the text or loosening the validator.

---

**Kind:** terminal

**ID:** 2026-08-13-02

**Timestamp:** 2026-08-13T10:57:18Z

**Closes:** 2026-08-13-01

**Outcome:** completed

**Observed:**

A record store containing roughly thirty entries was lost. It had lived only in a container's `/tmp`, worked in across a long session, and never pushed. The container was reclaimed. Also lost: REGISTER.md, PROTOCOL.md, PHILOSOPHY_ARCHIVE.md, OPERATOR_PROFILE.template.md, prompts/, check_record.py, check_register.py, and every amendment carrying the philosophy from 43 headwords to 47.

Every task in that session ended with the instruction that nothing be pushed, on the reasoning that the operator controls pushes. That instruction was followed exactly and is what caused the loss. The planning role wrote it repeatedly without ever considering that unpushed means one disk. The executing agent reported clean trees and unpushed commits as compliance. Neither participant held the thought that a thing existing in exactly one place is precarious.

The store had every integrity property it claimed. Append-only, byte-prefix verified, history-walked, duplicate-checked. All of it was real and none of it mattered, because immutability is a property of a file and durability is a property of where the file lives. Nothing in the methodology asked the second question.

What survives: the reasoning. Every finding, every adjudication, and the dictated text of every amendment exist outside the store and can be restored. What does not survive: when each was discovered, in what order, against which commit, and the append-only chain that made those claims checkable. A methodology whose central claim is that provenance is everything has lost its own provenance and kept its conclusions. Whether that argues against the claim or shows that the reasoning was load-bearing and the paperwork was not is left open here rather than settled.

One artifact survived by being copied. OSCam's ledger_validator_core.py is a vendored copy of check_record.py's portable core, taken from a commit that no longer exists anywhere. The vendored copy outlived its source, and check_record.py at 7ffdd27 was rebuilt from it. Redundancy did what the append-only guarantee could not.

**Deviations:**

This entry pair records a completed fact rather than governing work. The store has two entry kinds, intent and terminal, and neither fits a pure retrospective. Two agents have now reached for a kind that does not exist. The two available kinds are used here and the fit is imperfect; noted rather than resolved.

No intent record governed the task that wrote this entry, since the store did not exist to hold one.

The outcome prediction field carries `not authored`, which is accurate. No outcome prediction was written for a task whose outcome was already a fact.

---

**Kind:** intent

**ID:** 2026-08-13-03

**Timestamp:** 2026-08-13T11:04:55Z

**Title:** Build check_register.py and REGISTER.md

**Change:** Create check_register.py, a capture-only wrapper that runs a check command and appends one observation to REGISTER.md pairing the stated expected failure mode with the actual captured exit code, stdout, and stderr. Create REGISTER.md itself: header, format documentation, no entries yet -- every entry that lands in it is produced by check_register.py during this task's own verification and real use, not hand-authored.

**Scope boundary:** check_register.py, REGISTER.md, and this entry pair. In scope: reusing check_record.py's check_append_only/check_history_append_only for REGISTER.md's own append-only verification, confirmed beforehand not to require refactoring either function (both already accept an explicit record_name). Out of scope: any comparison or matching of an observed failure against its stated expectation (Confirm Failure Before Applying Fixes stays an agent's judgment, not this tool's); retroactively registering any check observation from before this task; PROTOCOL.md, check_prompt.py, or any philosophy amendment; fixing check_record.py's split_entries() heading-collision fragility beyond not repeating its shape here; ~/imx.

**Baseline:** REGISTER.md and check_register.py do not exist. RECORD.md holds two entries (2026-08-13-01/-02) at commit 56a840c; check_record.py and check_glossary.py both pass. BUILD_TASKS.md's own Task 2 record for check_register.py predates this task, was never executed, and undercounts this task's field list -- it names check name/date/expected-failure-text/exit-code/stdout/stderr (five fields, no UTC timestamp, no command field, no vacuous flag) and says the wrapper should be "documented in the register file's header." This task's own governing prompt adds the command-run field and the vacuous flag (neither existed as a concept until RECORD.md/check_record.py were built) and deliberately keeps that documentation out of the header, in check_register.py's docstring instead, for the same frozen-header reason RECORD.md's own header gives. Where the two disagree, this task's prompt governs; both are named here rather than the older one silently overridden.

**Prediction (outcome — planner):** When this is done, the check register that Checks Decay has required since the philosophy was written will exist as an artifact rather than as prose scattered across task reports, and every future observation of a check failing will have a place to land that survives the session. The register will be append-only, verified by the same machinery as RECORD.md, and reusing that machinery rather than duplicating it. The wrapper will record without judging, so no future agent is blocked by a brittle pattern match on failure text. Its header will not repeat the heading-collision hazard the store hit this morning. It will have been used once for real before being called complete, and that use will be visible in REGISTER.md rather than described in a report.

**Prediction (mechanism — coder):** Written before formally engaging with this task's closed decisions, on what BUILD_TASKS.md's own Task 2 record and the shape of check_record.py/ledger_cli.py already implied: check_register.py will be a thin subprocess.run(capture_output=True) wrapper appending one **Label:** value entry per call to REGISTER.md, reusing check_append_only/check_history_append_only directly by passing record_name="REGISTER.md" -- both already parameterized for this, no refactor. The append path will never search REGISTER.md's text for an insertion marker; it opens the file in append mode and writes at the literal end, which avoids the heading-collision hazard structurally, not by carefulness alone, since nothing is searched for. The real risk area expected going in: "greppable by check name, returns only that check's entries" is a stronger claim than plain grep gives against a multi-line entry, and confirming it needs real captured output, not an assumption.

**Finish line:** check_register.py and REGISTER.md exist, all eight required checks verified, the real-use requirement satisfied (at least one of this task's own checks wrapped in its real position, landing in REGISTER.md), py_compile clean. Intent and terminal entries in RECORD.md. Committed and pushed, confirmed with git ls-remote.

**Abort conditions:** If capturing output cannot be done without altering how the wrapped check runs, stop and report the options rather than accepting the alteration. If reusing check_record.py's append-only functions requires refactoring it, stop and report the scope before proceeding -- checked before this entry was written: it does not. If real use surfaces a defect that cannot be fixed within this task's scope, stop and report rather than expanding scope to fix it.

---

**Kind:** terminal

**ID:** 2026-08-13-04

**Timestamp:** 2026-08-13T11:12:40Z

**Closes:** 2026-08-13-03

**Outcome:** completed

**Observed:** check_register.py and REGISTER.md exist (commit 07a5094). No refactor of check_record.py was needed for the append-only reuse, confirmed both before the intent entry and again here: check_append_only/check_history_append_only already accept an explicit record_name and were called with "REGISTER.md" unmodified.

Eight required checks, all confirmed against real runs, not asserted: (1) a deliberately failing dummy check produced exactly one entry pairing its stated expectation with the real captured output; (2) re-running it appended a second entry, confirmed by direct byte-prefix diff that the first was untouched; (3) wrapped exit status matched a direct, unwrapped run for both a failing (1) and a passing (0) command; (4) a vacuous and a non-vacuous observation recorded distinguishable `**Vacuous:** yes`/`no` fields; (5) greppable by check name -- with a real, deliberately constructed collision, not an assumed one: a wrapped command's stdout printed another entry's own field-line text verbatim, and a plain unanchored `grep` false-positived on it three separate ways (the mimicry line itself, the unescaped Command field, and simple substring overlap with a longer check name), while the anchored form (`^\*\*Check:\*\* name$`) returned exactly the two real entries and nothing from the mimicry, because captured stdout/stderr is four-space indented and can never start with `**` at column 0; (6) REGISTER.md passed check_record.py's reused check_append_only (real, non-vacuous) and check_history_append_only (vacuous, one commit, said so) exactly as RECORD.md does; (7) sabotaging an already-committed REGISTER.md line was caught and named by line number, then reverted via `git checkout` and reconfirmed clean; (8) check_record.py and check_glossary.py both still pass (43/42/43 unchanged) -- and both of those real runs were themselves wrapped through check_register.py, in their real position verifying this task, satisfying the real-use requirement twice rather than through a constructed stand-in.

REGISTER.md's own append-only path never searches its text for an insertion marker -- observations are appended at the literal end of the file, opened in append mode. There was nothing for this file's own prose to collide with, unlike RECORD.md's header.

**Deviations:** One real conflict between this task's closed decisions and BUILD_TASKS.md's original Task 2 record, named rather than silently resolved: BUILD_TASKS.md's field list (check name, date, expected-failure text, exit code, stdout/stderr) predates the vacuous-flag and command-run fields entirely, and its finish line says the wrapper should be "documented in the register file's header" -- this task's own governing prompt keeps that documentation in check_register.py's docstring instead, deliberately, for the frozen-header reason RECORD.md's header itself states. The closed decisions governed; BUILD_TASKS.md's original record is superseded for this tool by this entry pair, not edited.

A second collision risk, distinct from the heading-search hazard named in the intent entry, was raised before building and confirmed real rather than theoretical: captured stdout is arbitrary and can carry text shaped like this file's own field syntax, including another entry's own field labels as data. Four-space indentation of captured stdout/stderr resolves this for the anchored-query case, empirically, against a real constructed instance -- not for a bare substring grep, which remains unreliable against free text generally, and not for the Command/Expected-failure-mode fields, which are caller-supplied text trusted the same way every RECORD.md field already is. Documented in both files' headers.

REGISTER.md already carries genuine observations from this task's own verification (named `dummy_*` where constructed, plain check names where wrapping this task's own real checks) rather than being seeded empty or with placeholders. Left in place.

---
