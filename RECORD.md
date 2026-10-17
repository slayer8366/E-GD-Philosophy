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

**Kind:** intent

**ID:** 2026-08-13-05

**Timestamp:** 2026-08-13T15:11:14Z

**Title:** Create CLAUDE.md at the repo root

**Change:** Create `CLAUDE.md` at the root of E-GD-Philosophy, from the text dictated in this task's governing prompt verbatim. BOOTSTRAP.md says it is loaded every session at session start; nothing loads it, so every convention it carries has instead been repeated in each task prompt, which is why a fresh session starts with none of them. A `CLAUDE.md` at the repo root is read automatically. This points it at the documents that already exist rather than duplicating them.

**Scope boundary:** `CLAUDE.md`, created once, from the dictated text, plus this entry pair. Nothing else. Out of scope, explicitly: `~/imx` and its own CLAUDE.md, BOOTSTRAP.md, PROTOCOL.md, any philosophy document, and anything in OSCam. The dictated text is not to be edited to imply PROTOCOL.md or OPERATOR_PROFILE.template.md exist when they do not.

**Baseline:** `CLAUDE.md` confirmed absent from the working tree (no abort condition triggered). Confirmed present: BOOTSTRAP.md, ENFORCEMENT.md, GLOSSARY.md, PHILOSOPHY.md, RECORD.md, REGISTER.md, DURABILITY.md, check_record.py, check_register.py, check_glossary.py. Confirmed absent, matching what the dictated text itself accounts for: PROTOCOL.md, OPERATOR_PROFILE.template.md. `/home/bwann83/imx/CLAUDE.md` confirmed present and confirmed to contain a "Write permissions" section (`grep -c "Write permissions"` returned 1), matching the dictated text's reference to it. Repo clean at commit 9a8e552 on branch Test-1; local Test-1 HEAD confirmed equal to `origin/Test-1` HEAD (both 9a8e552) via `git ls-remote` and `git rev-parse origin/Test-1` -- nothing unpushed going in.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** `CLAUDE.md` will be written as a single `Write` call reproducing the dictated block-2 text exactly, not templated or regenerated from the other documents -- the closed decision is "point, do not duplicate," so the file's own content stays static regardless of what BOOTSTRAP.md/ENFORCEMENT.md/GLOSSARY.md/PHILOSOPHY.md say. Checks 1 and 2 (every dictated section present; every named file exists or is marked not-yet-rebuilt) will be written as structural checks against the actual file text -- grepping section headers and the named filenames -- rather than trusting the copy-paste, since RECORD.md's own header collision showed that raw substring search over prose is fragile and the check_glossary.py precedent in this repo already favors structural inspection over text scanning. Check 3 (check_record.py and check_glossary.py still pass) is expected to be unaffected by CLAUDE.md's existence, since neither script reads or references CLAUDE.md anywhere in its logic -- confirmed by grep before this entry was written, not assumed. Check 4 (only CLAUDE.md, RECORD.md, and REGISTER.md changed) will be a `git diff --stat` / `git status` comparison against 9a8e552, the commit confirmed above as this task's own pre-task HEAD; REGISTER.md is the only file check_register.py's wrapper ever appends to, so no other file should appear in that diff. The one real risk going in: the dictated text's OSCam/`~/imx` cross-reference is a claim about a second repository, and confirming it means reading that repository's actual CLAUDE.md rather than trusting the prompt's description of it -- already done in the baseline above, not deferred to the checks.

**Finish line:** `CLAUDE.md` created, four checks verified and registered, intent and terminal entries in RECORD.md, committed and pushed, confirmed with `git ls-remote`.

**Abort conditions:** If a file the dictated text names as existing does not exist, stop and report rather than adjusting the text. If `CLAUDE.md` already exists in this repository, stop and report rather than overwriting.

---

**Kind:** terminal

**ID:** 2026-08-13-06

**Timestamp:** 2026-08-13T15:19:27Z

**Closes:** 2026-08-13-05

**Outcome:** completed

**Observed:** `CLAUDE.md` created at the repo root (commit to follow this entry) as a single `Write` reproducing the dictated block-2 text exactly, no templating. Neither abort condition triggered: `CLAUDE.md` was confirmed absent before writing, and every file the text names as existing was confirmed present.

Four required checks, all run through `check_register.py` and landing in REGISTER.md (18 entries total, `grep -c "^\*\*Check:\*\*" REGISTER.md`), sabotage-and-revert for the two checks that inspect this task's own new construction and a third for the scope guard, positive-case-only for the fourth (pre-existing tooling this task did not build):

(1) *Every dictated section present*, expected failure named before running: sabotaging by deleting the `## Stop conditions` header line produced exactly the predicted failure (`FAIL: missing section header(s): ['## Stop conditions']`, exit 1); reverting reproduced the predicted pass (all six headers present, exit 0).

(2) *Every named file exists or is marked not-yet-rebuilt*, expected failure named before running: sabotaging by deleting the "Not yet rebuilt after the store was lost" sentence produced exactly the predicted failure (both `PROTOCOL.md` and `OPERATOR_PROFILE.template.md` reported as named-but-absent, exit 1); reverting reproduced the predicted pass, including the cross-repo reference -- `/home/bwann83/imx/CLAUDE.md` confirmed present with its own "Write permissions" section, matching the dictated text's claim about it.

(3) *`check_record.py` and `check_glossary.py` still pass*, positive case, no sabotage (pre-existing tooling, not built by this task): both ran clean through `check_register.py` -- `check_record.py` reported all 5 entries structurally valid, working-tree and 4-commit history-walk append-only clean; `check_glossary.py` reported 43/42/43 unchanged from the prior task's own terminal entry. Neither script references `CLAUDE.md` anywhere, confirmed by grep before this task's intent entry was written, and neither result changed because of its presence.

(4) *Only `CLAUDE.md`, `RECORD.md`, and `REGISTER.md` changed, diffed against this task's own pre-task commit* (9a8e552, confirmed fresh from `git log` and equal to `origin/Test-1` before this task began): sabotaging by appending a blank line to `README.md` produced exactly the predicted failure (`README.md` named as unexpected, exit 1); `git checkout -- README.md` reverted it. A second, unpredicted failure mode surfaced on the revert-confirm run and is recorded under Deviations below, not folded into this pass/fail pair.

**Deviations:** DISCOVERED: `check_register.py`'s own `import check_record as cr` regenerates an untracked `__pycache__/` directory as a side effect of every wrapped run, including a run of Check 4 through `check_register.py` itself -- the wrapping process pollutes the exact repo-scope state Check 4 inspects. This was not predicted in the intent entry's mechanism prediction. First observed as a genuine FAIL (`scope_diff` run, `__pycache__/` named alongside the still-present `README.md` sabotage), then isolated as its own FAIL after `README.md` was reverted and `__pycache__/` was the only remaining unexpected entry. Resolved by adding a narrow, named exclusion to the check-4 script for paths under `__pycache__/` -- reported separately from the real `ALLOWED` set in both the pass and fail branches, never silently dropped -- rather than by loosening what counts as in-scope. The substantive `ALLOWED`-diff logic that Check 4 exists to enforce was already sabotage-tested and caught `README.md` correctly before this fix; the fix touches only the noise-exclusion layer. `__pycache__/` was deleted from the working tree after each observation and does not appear in this task's commits (confirmed: it is a compiled bytecode cache, never staged, and this repo carries no `.gitignore` to have suppressed it from `git status` on its own).

The scratch check scripts (`/tmp/check1.py`, `/tmp/check2.py`, `/tmp/check4.py`) live outside the repo tree, per this task's own scope boundary ("Nothing else" besides `CLAUDE.md` and this entry pair) and per the general convention that scratch tooling does not ride into the working directory the changelog/record does not account for. They are not committed and are not part of this repository's history.

---

**Kind:** intent

**ID:** 2026-08-13-07

**Timestamp:** 2026-08-13T15:32:33Z

**Title:** Add .gitignore to suppress the __pycache__ noise discovered in the prior task

**Change:** Create a `.gitignore` at the repo root listing `__pycache__/`, so that `check_register.py`'s own `import check_record as cr` -- which regenerates `__pycache__/` as an untracked side effect of every wrapped run -- stops appearing in `git status`. The prior task (2026-08-13-05/06) discovered this and flagged it under "noticed but not acted on"; this closes that gap on the operator's direct instruction.

**Scope boundary:** `.gitignore` only, plus this entry pair. Deleting the repo's own already-untracked `__pycache__/` directory, if present, is in scope as verification cleanup, not as a tracked change -- it was never tracked and this task does not change that. No other file touched.

**Baseline:** `.gitignore` confirmed absent from repo root. Repo clean at commit fa542d3 on Test-1, matching origin/Test-1 (confirmed via `git ls-remote`). No `__pycache__/` present on disk (removed at the end of the prior task).

**Prediction (outcome — planner):** A single untracked directory (`__pycache__/`) stops appearing in `git status --porcelain` after any script in this repo triggers the `check_record` import, without needing the per-check exclusion logic the prior task added ad hoc to a scratch script outside the repo. Closes a real, if minor, rough edge the prior task's terminal entry flagged and left open.

**Prediction (mechanism — coder):** A `.gitignore` containing `__pycache__/` is sufficient -- git's own ignore matching suppresses the directory from `git status` regardless of which script triggers its creation, with no change needed to `check_record.py`, `check_register.py`, or the scratch check scripts. Verification: trigger the import for real (running `check_glossary.py` wrapped through `check_register.py`, as the prior task did) and confirm `git status --porcelain` reports nothing for `__pycache__/` afterward; sabotage by temporarily renaming `.gitignore` aside and confirming `__pycache__/` reappears in status, then restore.

**Finish line:** `.gitignore` created, its suppression of `__pycache__/` confirmed against a real triggering run (not assumed), `check_record.py` and `check_glossary.py` still pass, intent and terminal entries in RECORD.md, committed and pushed, confirmed with `git ls-remote`.

**Abort conditions:** If `.gitignore` would need to suppress anything beyond `__pycache__/` to solve this, stop and report rather than broadening scope unasked.

---

**Kind:** terminal

**ID:** 2026-08-13-08

**Timestamp:** 2026-08-13T16:00:07Z

**Closes:** 2026-08-13-07

**Outcome:** completed

**Observed:** `.gitignore` created at the repo root containing exactly one line, `__pycache__/`. No broader suppression was needed; the abort condition did not trigger.

Sabotage-and-revert, real trigger both times (not assumed): with `.gitignore` moved aside to `/tmp/gitignore.aside` and `__pycache__/` deleted first, wrapping `check_glossary.py` through `check_register.py` (which itself does `import check_record as cr`) regenerated `__pycache__/`, and a small assertion script (`/tmp/check_gitignore.py`, checking `git status --porcelain` for any line containing `__pycache__`) reported the predicted FAIL, `__pycache__/` visible as `??`. `.gitignore` restored; `__pycache__/` deleted again and the same trigger re-run; the assertion script reported the predicted PASS -- confirmed non-vacuous by `ls -d __pycache__` immediately after, showing the directory genuinely exists on disk at that moment and git simply no longer reports it.

`check_record.py` and `check_glossary.py` both still pass, run for real through `check_register.py` (5 RECORD.md entries valid at the time, 43/42/43 glossary contract unchanged) -- unaffected by `.gitignore`'s presence, as expected since neither script reads it.

Diffed against this task's own pre-task commit (fa542d3): only `RECORD.md` and `REGISTER.md` changed, plus `.gitignore` newly present -- exactly this task's scope, nothing else.

**Deviations:** None. The mechanism prediction held without correction this time: a bare `__pycache__/` line was sufficient, no script changes were needed, and the ad hoc per-check exclusion added to the prior task's scratch `check4.py` (never part of this repository's tracked history) is now genuinely unnecessary for any future check run in this repo, though it was not itself touched since it lives outside the repo tree and this task's scope was `.gitignore` only.

`__pycache__/` deleted from the working tree after the final observation; confirmed absent before this entry's commit.

---

**Kind:** intent

**ID:** 2026-08-13-09

**Timestamp:** 2026-08-13T16:22:34Z

**Title:** Create prompts/ as a preserved dispatch store, and check_prompts.py to verify its binding to RECORD.md

**Change:** Create `prompts/`, a store of dispatched-prompt files, and preserve this task's own governing prompt into it verbatim -- including anything in it that turns out to be wrong, not corrected while storing. Create `check_prompts.py`, which verifies only existence and binding between `RECORD.md` entries and files in `prompts/`: every entry that records a dispatch has a corresponding file, every file maps to an entry that exists, no orphans in either direction. It does not and cannot verify that a stored file holds the text actually dispatched -- that is not checkable from inside the repository, and its own header says so plainly rather than implying otherwise.

**Naming and binding scheme (mine to decide, recorded here per the governing prompt's instruction):** A new, non-required intent-entry field, `**Dispatch-file:**`, whose value is a path relative to `prompts/`. Adding it is safe because `check_record.py`'s `validate_entries` only enforces presence of its `INTENT_REQUIRED` list and does not reject or even inspect extra fields -- confirmed by reading the function before choosing this, not assumed. Only entries that carry this field are "entries that record a dispatch"; entries 2026-08-13-01 through -08 predate this store and carry no such field, so they are correctly excluded rather than retroactively required to have one. The store starts from this prompt forward, not reconstructed backward.

**Recovered versus preserved:** Marked by subdirectory, not by a second field: `prompts/preserved/<name>` for a prompt captured verbatim at dispatch time (this task's own case), `prompts/recovered/<name>` for one reconstructed afterward from a transcript. The directory is the single source of truth for provenance -- a second field naming the same fact could drift out of sync with the file's real location and there is no need for two places to hold one answer. `check_prompts.py` reports the count of each separately by listing each subdirectory, not by trusting a claim inside the entry.

This task's own prompt is preserved at `prompts/preserved/2026-08-13-09.md`, referenced from this entry as `**Dispatch-file:** preserved/2026-08-13-09.md`.

**Scope boundary:** `prompts/`, `check_prompts.py`, and this entry pair in `RECORD.md` (append only). Nothing else. No changes to `PHILOSOPHY.md`, `ENFORCEMENT.md`, `BOOTSTRAP.md`, `GLOSSARY.md`, `README.md`, `check_record.py`, `check_register.py`, or anything under `~/imx`. No reconstruction of any prior prompt in this task.

**Baseline:** `prompts/` and `check_prompts.py` confirmed absent before this entry was written. `check_record.py` and `check_glossary.py` both confirmed passing before any file was touched (8 entries valid, 7-commit history walk clean; 43/42/43 glossary contract intact) -- the abort condition on a dirty starting state did not trigger. Repo clean at commit 6125142 on Test-1, matching `origin/Test-1`. Running on the Pi (hostname `raspberrypi`), not a cloud sandbox -- confirmed by `hostname`, not assumed, since this task's own reasoning for running here is that the store must survive where the pushing happens.

**Known defect carried forward, not fixed here:** `check_prompts.py` reuses `check_record.split_entries` and `check_record.parse_fields` unmodified via `import check_record as cr`, inheriting the raw-substring `## Entries` heading-search fragility documented in `check_record.py`'s own header and in this repository's `CLAUDE.md` -- prose naming that heading before the real one would produce a phantom entry. Not fixed in this task; the same logic is duplicated in OSCam's `ledger_validator_core.py` and fixing it is out of scope there too, per this task's own instruction.

**Prediction (outcome — planner):** withheld

**Prediction (mechanism — coder):** `check_prompts.py` will reuse `check_record.split_entries`/`parse_fields` to extract every entry's `Dispatch-file` field (if present), resolve each value against `prompts/`, and separately walk `prompts/preserved/` and `prompts/recovered/` to confirm every physical file is named by exactly one entry -- duplicate claims on one file treated as their own error class, not silently allowed. On this first run: 1 preserved, 0 recovered, reported as a fact, not a failure, matching this project's existing vacuous-reporting convention. Verification will be sabotage-and-revert against real files: delete the stored prompt file and confirm the check names it as missing/orphaned by path; separately point `Dispatch-file` at a wrong path and confirm the same failure shape; revert both, reconfirm clean. Main risk expected going in: keeping the orphan check symmetric in both directions without conflating "entry names a file that doesn't exist" with "file exists that no entry names" -- these are different failure shapes and the report should not collapse them.

**Finish line:** `prompts/` exists and holds at least this prompt; `check_prompts.py` exists, runs, and passes against the current store; `RECORD.md` carries an opened and terminated entry for this work; everything committed and pushed, confirmed by the observed remote ref.

**Abort conditions:** If `check_record.py` or `check_glossary.py` had failed before anything was touched, stop and report (checked above; did not trigger). If the naming scheme adopted here required renaming or editing any existing `RECORD.md` entry, stop and ask (it does not -- the scheme is purely additive, a new optional field on new entries only).

---

**Kind:** terminal

**ID:** 2026-08-13-10

**Timestamp:** 2026-08-13T16:25:28Z

**Closes:** 2026-08-13-09

**Outcome:** completed

**Dispatch-file:** preserved/2026-08-13-09.md

**Observed:** `prompts/preserved/2026-08-13-09.md` exists and holds this task's own governing prompt, preserved verbatim, including its instruction to report CLAUDE.md's "write-permissions table" even though this repository's CLAUDE.md has no such table -- not corrected while storing, per the prompt's own instruction not to. `check_prompts.py` exists at the repo root, reuses `check_record.split_entries`/`parse_fields` unmodified (known heading-search defect inherited knowingly, not fixed here, matching the same logic's out-of-scope status in OSCam's `ledger_validator_core.py`), and answers existence-and-binding questions only -- its own header states plainly that it cannot and does not verify stored text against what was actually dispatched.

A real defect was caught by running `check_prompts.py` against the actual store, not assumed: the intent entry (2026-08-13-09) described the `Dispatch-file` binding in prose but never wrote it as an actual `**Dispatch-file:**` field line -- it was embedded mid-paragraph inside two prose sentences, not at line-start, so `parse_fields` (which matches only `^\*\*Label:\*\*`) never recognized it. The first real run of `check_prompts.py` reported `dispatch-recording entries found: 0` and correctly flagged `prompts/preserved/2026-08-13-09.md` as an orphaned file. Since 2026-08-13-09 is already committed and this store is append-only, that entry cannot be edited to add the missing field; the real `**Dispatch-file:**` field is declared here instead, in the terminal entry that records what this task actually produced. This is not treated as a correction requiring `Outcome: superseded` -- the intent entry's plan, scope, and reasoning are all still accurate and stand unedited; only the mechanical field declaration it described was never actually written, and it is supplied here for the first time, not fixed retroactively.

Sabotage-and-revert, four real runs against the real files, each in the working tree before this entry pair was committed:

(1) *Missing file*: `prompts/preserved/2026-08-13-09.md` moved aside; `check_prompts.py` reported the predicted FAIL, naming the entry and the missing path exactly. Restored; rerun confirmed PASS.

(2) *Wrong path in the field*: this entry's own `Dispatch-file` value temporarily changed (in the uncommitted working tree only) to a nonexistent filename; `check_prompts.py` reported two violations, correctly, not one -- the wrong value named as missing, and the real file now also named as orphaned since nothing claimed it anymore with the value changed. Reverted to `preserved/2026-08-13-09.md`; rerun confirmed PASS.

(3) *Orphan file*: an extra, unclaimed file temporarily added under `prompts/preserved/`; `check_prompts.py` reported the predicted, distinct FAIL shape ("exists but no RECORD.md entry's 'Dispatch-file' field names it"), confirming the two orphan directions are not conflated. Removed; rerun confirmed PASS.

(4) *Duplicate claim*: a second, temporary `**Dispatch-file:** preserved/2026-08-13-09.md` field added elsewhere in the working tree; `check_prompts.py` reported the predicted FAIL, naming both claiming entries. Removed; rerun confirmed PASS.

Final real run: `dispatch-recording entries found: 1`; `files under prompts/: preserved=1, recovered=0`; PASS. `check_record.py` and `check_glossary.py` both re-run after this entry pair was appended: `check_record.py` reports 10 entries structurally valid, working-tree and history-walk append-only both clean; `check_glossary.py` reports 43/42/43 unchanged.

**Deviations:** Checks were run directly (`python3 check_prompts.py`, `python3 check_record.py`, `python3 check_glossary.py`), not wrapped through `check_register.py`, despite CLAUDE.md's Verification section recommending that wrapping so observations survive the session. This task's own WRITE PERMISSIONS section lists exactly `prompts/`, `check_prompts.py`, and `RECORD.md` (append only), followed by "Nothing else" -- `REGISTER.md` is not in that list. Flagged as a real conflict between the governing document and this task's explicit scope rather than silently resolved either way: the narrower, explicitly-enumerated task scope was followed, on the reasoning that a specific, itemized permission list ending in "Nothing else" is a deliberate restriction and should not be read as silently permitting an unlisted file via a general standing recommendation.

The em dash used in this repository's existing `Prediction (outcome — planner)` / `Prediction (mechanism — coder)` field labels was checked as a possible confound for the missing-field defect above and ruled out -- `Dispatch-file` uses no such character; the actual cause was purely the field being mid-paragraph rather than at line-start, confirmed by grep before writing this explanation, not assumed.

---

**Kind:** intent

**ID:** 2026-08-13-11

**Timestamp:** 2026-08-13T18:37:36Z

**Title:** Record and grade the operator's withheld outcome prediction for 2026-08-13-09, received after its terminal entry had already closed it

**Change:** The operator's outcome prediction for 2026-08-13-09 (authored before dispatch, withheld per that entry's own sentinel, per this repository's stated convention for the `withheld` value) arrived after 2026-08-13-10 had already closed 2026-08-13-09 and been committed and pushed. `check_record.py`'s own sentinel-resolution logic (`validate_entries`, the block handling `SUPPLIED_FIELD`/`Closes`) requires the `Prediction-outcome-supplied` field to live in *the* terminal entry that `Closes` the intent whose prediction is being resolved. That terminal entry (2026-08-13-10) is already committed and RECORD.md is append-only, so the field cannot be added to it. A second terminal entry with `Closes: 2026-08-13-09` is not an option either -- `check_duplicate_terminals` treats more than one terminal entry closing the same intent as an error, not a normal state. This entry records the prediction verbatim, grades it against what 2026-08-13-09/-10 actually show, and names this as a discovered gap in the store's own mechanism rather than working around it silently.

**Scope boundary:** This entry pair only. No file outside `RECORD.md` is touched. `2026-08-13-09`'s outcome-prediction sentinel remains `withheld` in the store, permanently unresolved by the built-in mechanism -- not edited, not worked around by inventing a field the validator does not recognize.

**Baseline:** Repo clean at commit f1be0be on Test-1, matching `origin/Test-1`. `2026-08-13-09` (intent) carries `Prediction (outcome — planner): withheld`, still unresolved. `2026-08-13-10` (terminal) closes it, already committed, carries no `Prediction-outcome-supplied` field.

**Prediction (outcome — planner):** not authored -- this entry records and grades a prediction already received; there is no forward outcome to predict, the same reasoning entry 2026-08-13-01 gives for its own retrospective case.

**Prediction (mechanism — coder):** Quote the operator's prediction in full in the terminal entry's Observed field (not stored under `prompts/`, since it is not a work-dispatch bound by `Dispatch-file` -- it is a retrospective grading document, a different kind of artifact, and forcing it into that store would blur a distinction `check_prompts.py` does not exist to draw). Grade each "WILL BE TRUE AT CLOSE" item and each of the four "ACTUAL BETS" against the real, already-committed state of 2026-08-13-09/-10 and the working tree, citing the actual run output rather than re-describing from memory. Expect bet 4 to grade as wrong, as the operator predicted they might be wrong about -- but distinguish precisely between "the run failed" (true: the first real run of `check_prompts.py` returned FAIL) and "the script had a defect" (false: `check_prompts.py`'s code was never modified after being written; the failure was a correctly-caught defect in my own RECORD.md authorship, not in the check). Collapsing those two would misgrade the operator's own stated reasoning, which was specifically about verification-script bugs.

**Finish line:** This entry pair committed and pushed, confirmed by an observed remote ref, matching the standard this task's own subject (2026-08-13-09/-10) was held to.

**Abort conditions:** None anticipated; this is a recording task over already-known facts, not new construction.

---

**Kind:** terminal

**ID:** 2026-08-13-12

**Timestamp:** 2026-08-13T18:38:26Z

**Closes:** 2026-08-13-11

**Outcome:** completed

**Observed:** The operator's outcome prediction, quoted in full:

    OUTCOME PREDICTION -- prompts/ store and check_prompts.py
    Authored by: operator
    Authored: before dispatch. Withheld until the coder's mechanism
    prediction is committed.

    WILL BE TRUE AT CLOSE
    prompts/ exists on Test-1 and contains one file, this task's own
    prompt, stored verbatim including its errors, and marked as preserved at
    dispatch rather than recovered.

    check_prompts.py exists, runs to completion, and passes. It reports
    preserved and recovered counts separately, as 1 and 0.

    Its header states that it does not verify a stored prompt matches what was
    dispatched.

    RECORD.md carries one new entry, opened and terminated, recording the
    naming scheme and the preserved/recovered decision with reasoning.

    check_record.py and check_glossary.py still pass after the append.

    README.md, PHILOSOPHY.md, ENFORCEMENT.md, BOOTSTRAP.md, GLOSSARY.md,
    check_record.py, check_register.py are unchanged. Nothing under ~/imx is
    touched.

    The push is confirmed by an observed remote ref, not by a report that the
    command ran.

    THE ACTUAL BETS
    1. The naming scheme will embed the RECORD.md entry ID in the filename
       rather than using a date, a sequence number, or a hash.
    2. check_prompts.py will reuse or adapt split_entries() from
       check_record.py, and the report will disclose it rather than carry it
       silently.
    3. No abort. CLAUDE.md in this repository will not forbid anything the
       prompt instructs, and the coder will not need to stop and ask on the
       naming decision.
    4. check_prompts.py will pass on its first run, without a defect requiring
       a second pass.

    WHERE I EXPECT TO BE WRONG
    Bet 4. Six consecutive tasks have shipped a bug in a verification script,
    and this one is written last, as they all were. If it passes clean on the
    first run I will treat that as the surprising result, not the expected
    one.

    NOT PREDICTED
    How the work goes, which step is hard, what the coder reasons through.
    That is the mechanism prediction and belongs to the coder.

Grading, against the real, already-committed state of 2026-08-13-09/-10 and the current working tree, not from memory:

WILL BE TRUE AT CLOSE -- all seven items TRUE, one with a nuance worth naming. `prompts/preserved/2026-08-13-09.md` is the only file under `prompts/`, verbatim including the CLAUDE.md-write-permissions-table error, marked preserved. `check_prompts.py` exists, passes, and its final real run reported `files under prompts/: preserved=1, recovered=0` exactly. Its header states plainly it does not verify stored text against what was dispatched. `check_record.py` and `check_glossary.py` both pass at the current commit. `README.md`, `PHILOSOPHY.md`, `ENFORCEMENT.md`, `BOOTSTRAP.md`, `GLOSSARY.md`, `check_record.py`, `check_register.py` are all untouched by 2026-08-13-09/-10's commits, and nothing under `~/imx` was touched. The push was confirmed by `git ls-remote` returning `f1be0be036fc8f29d9d9ff6aca815f49ae89463b`, not by reporting that `git push` was run. The nuance: "RECORD.md carries one new entry, opened and terminated, recording the naming scheme and the preserved/recovered decision with reasoning" is true as one governed unit of work (2026-08-13-09 intent, 2026-08-13-10 terminal), and the naming scheme and preserved/recovered reasoning are indeed both in the intent entry as predicted -- but the actual `**Dispatch-file:**` field that makes the binding real ended up living in the terminal entry instead, because the intent entry's own version of it was written as prose, not as parseable field syntax, and `check_prompts.py`'s first real run caught that. The prediction did not anticipate this, and could not have -- it is a fact about how the entry was drafted, not about the store's design.

THE ACTUAL BETS -- three of four correct, one wrong as the operator anticipated.

Bet 1 (entry ID embedded in the filename, not a hash/sequence/plain date): correct. The file is `prompts/preserved/2026-08-13-09.md`, named after the RECORD.md entry ID.

Bet 2 (check_prompts.py reuses/adapts split_entries() and discloses it): correct. `check_prompts.py` imports `check_record` and calls `split_entries`/`parse_fields` directly, unmodified; its own header states this and names the inherited heading-search defect explicitly, and so did this task's own chat report.

Bet 3 (no abort; CLAUDE.md forbids nothing; no stop-and-ask on the naming decision): correct on its own terms -- there was no abort and no stop-and-ask blocking the naming decision. Adjacent but distinct, not a failure of this bet: a real conflict was found and flagged (not blocked on) between CLAUDE.md's `check_register.py` recommendation and 2026-08-13-09's own explicit WRITE PERMISSIONS list, which excluded `REGISTER.md`. That conflict was about check tooling, not the naming decision the bet names, and was resolved and disclosed rather than asked about, consistent with that task's "send now, single block, nothing held" disposition.

Bet 4 (check_prompts.py passes on its first run, no defect requiring a second pass): wrong, as the operator predicted they might be. The first real run of `check_prompts.py` returned `FAIL` (exit 1), reporting `dispatch-recording entries found: 0` and naming `prompts/preserved/2026-08-13-09.md` as orphaned. Multiple runs followed before a clean PASS. The literal claim is false. What should not be conflated with it, because the operator's own stated reasoning was specifically about *verification-script* bugs ("six consecutive tasks have shipped a bug in a verification script"): `check_prompts.py`'s code was never modified after being written -- zero lines changed between its first run and its last. The FAIL was a correct, accurate detection of a real defect in how 2026-08-13-09 was drafted (the `Dispatch-file` field written as prose, not as a `**Label:**` line), not a bug in the check itself. The pattern the operator cited did not recur here; a different, narrower failure did, one the check was specifically built to catch and did catch, correctly, on its very first exposure to real data.

**Deviations:** The `Prediction-outcome-supplied`/`Closes` sentinel-resolution mechanism `check_record.py` provides could not be used for 2026-08-13-09's `withheld` outcome prediction, because it arrived after 2026-08-13-10 (the terminal entry that closes 2026-08-13-09) was already committed and pushed. That mechanism requires the supplied value to live in *the* terminal entry that closes the relevant intent; editing an already-committed terminal entry violates append-only, and a second terminal entry with `Closes: 2026-08-13-09` would trigger `check_duplicate_terminals`'s "closed by more than one terminal entry" error. DISCOVERED: the store has no built-in path to resolve a `withheld` outcome-prediction sentinel that arrives after its intent's terminal entry has already landed -- a timing gap the sentinel vocabulary's own documentation does not anticipate. Not fixed here (would mean changing `check_record.py`'s validation rules, out of scope for a recording task); worked around by grading the prediction in a separate, self-contained entry pair instead, with 2026-08-13-09's own sentinel left genuinely `withheld` and unresolved in the store, permanently, rather than forcing a resolution the validator was not built to accept. `check_record.py` at the current commit still reports it as `pending`, correctly -- that report is accurate to the store's actual state, not a defect.

The operator's prediction was quoted in full above rather than in `prompts/`, on the reasoning given in this entry's own Prediction (mechanism -- coder) field: it is not a work dispatch bound by `Dispatch-file`, and `check_prompts.py`'s binding logic was not extended to cover it.

---

**Kind:** intent

**ID:** 2026-08-13-13

**Timestamp:** 2026-08-13T21:40:00Z

**Title:** Create PROTOCOL.md, transcribing eight recovered rules

**Change:** Create `PROTOCOL.md` at the repository root, transcribing the eight-rule "Working Protocol" document supplied verbatim in this task's own governing prompt: the "Where these came from" section, the numbered rules 1 through 8 with rule 5's and rule 6's stated enforceability limits and rule 8's empty caveats section left exactly as given, the "What these do not fix" section, and the "Standing" section. Not improved, reordered, renumbered, or softened. Preserve this task's own governing prompt verbatim under `prompts/preserved/`.

**Dispatch-file:** preserved/2026-08-13-13.md

**Scope boundary:** `PROTOCOL.md`, `RECORD.md` (append only), `REGISTER.md`, `prompts/preserved/`, and this entry pair. Nothing else. No changes to `PHILOSOPHY.md`, `ENFORCEMENT.md`, `BOOTSTRAP.md`, `GLOSSARY.md`, `OVERVIEW.md`, `README.md`, `CLAUDE.md`, `DURABILITY.md`, or any check script. Nothing under `~/imx`. Out of scope: promoting, testing, or applying any of the eight rules; any ninth rule; editing any existing `RECORD.md` entry, including 2026-08-13-09; any glossary row or headword; the README's outstanding honesty edits; Phase 3.

**Baseline:** `PROTOCOL.md` confirmed absent from the working tree (abort condition did not trigger). `check_glossary.py` confirmed passing: 43 philosophy headwords, 42 enforcement entries, 43 glossary rows, PASS. `check_record.py` confirmed passing: 12 entries structurally valid, working-tree check clean, 11-commit history walk clean (each a byte-prefix extension), Superseded-by cross-reference vacuously PASS, duplicate-terminal check PASS; three pending outcome-prediction sentinels reported (2026-08-13-01, 2026-08-13-05: `not authored`; 2026-08-13-09: `withheld`, permanently unresolved by the store's own mechanism per 2026-08-13-11/-12's Deviations) — reported as expected output, not failures. `check_prompts.py` confirmed passing: 1 dispatch-recording entry, 1 file under `prompts/preserved/`, 0 under `prompts/recovered/`, no orphans either direction. The headword "Role Partition" confirmed present in `PHILOSOPHY.md` (line 13): "Planning and execution are held by separate actors. The planning role discusses, designs, and writes prompts, and never edits files or runs code. The executing role edits and runs, and never makes architectural decisions...." — rule 7's stated standing ("this is a replacement for Role Partition, not a supplement to it") is thus a reference to a real headword, not a phantom one; the pre-write stop condition on this point did not trigger. `CLAUDE.md` (line 13) confirmed to reference `PROTOCOL.md` by name: "Not yet rebuilt after the store was lost: `PROTOCOL.md` (eight untested working rules) and `OPERATOR_PROFILE.template.md`. When they return, both are read at session start too." Highest `RECORD.md` entry ID in use before this entry: 2026-08-13-12, all six intent/terminal pairs (01/02, 03/04, 05/06, 07/08, 09/10, 11/12) closed, no unterminated intent record found on scan. Repo clean at commit `81de364ac852babbd24aaf39ec60fb65c8cee274` on Test-1, confirmed equal to `origin/Test-1` via `git ls-remote --heads origin`.

**Departures, decided by the operator, not reopened here (recorded per the governing prompt's own instruction):** (1) The supplied document's opening line reads "Four rules governing how the operator and planner work together," but the document defines eight, numbered 1 through 8, with its own Standing section describing them as added in three groups (1-4, then 5-7, then 8). The governing prompt directs writing "Eight rules" in place of "Four rules" and recording the departure here rather than transcribing the stale count. Reason given: the opening line is stale relative to the body it introduces. (2) The recovered material this document is drawn from ended prior dispatches "committed locally, nothing pushed." This repository's own `CLAUDE.md` Non-negotiables state "Every task pushes," tied directly to this repository's own data-loss incident recorded at 2026-08-13-02 (a store of roughly thirty entries lost because it lived in exactly one place). `CLAUDE.md` governs this repository; this task commits and pushes, departing from the recovered convention.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** `PROTOCOL.md` will be written as a single `Write` call reproducing the supplied document's text with exactly one substitution (the opening line's rule count) and no other change — comments, internal inconsistencies (the "ten errors" / "eleven times" figures across two sections), rule 5's and rule 6's stated limits, and rule 8's empty "Caveats discovered: none yet." line all carried through unmodified, since the task states these are deliberate and not mine to correct. Check 1 (rules 1-8 present, both the opening line and the Standing section's rule-count language reflect eight) will be a structural grep for the numbered rule headers and for the substituted opening line, not a trust-the-copy assumption. Check 2 (rule 8's caveats section present and empty) will grep for the literal "Caveats discovered: none yet." line and confirm no text follows it before the next section header. Check 3 (`check_glossary.py` unchanged) is expected to be unaffected, since `PROTOCOL.md` touches no philosophy/enforcement/glossary file and the script does not read it — will assert against the exact 43/42/43 counts observed in this entry's Baseline, not against any number restated elsewhere. Check 4 (`check_record.py`/`check_prompts.py` still pass) is expected to pass with the same three pending sentinels reported as expected output. Check 5 (only `PROTOCOL.md`, `RECORD.md`, `REGISTER.md`, and one new file under `prompts/preserved/` changed) will be a `git diff --stat`/`git status` comparison against this entry's own baseline commit `81de364`, not against any earlier task's baseline. Main risk expected going in: transcribing a long supplied document by hand risks an unintended edit; verification will be a direct diff of the written file's body against the supplied text (minus the one authorized substitution) rather than a read-through assumption.

**Finish line:** `PROTOCOL.md` exists at repository root with rules 1 through 8 and the standing statement; the checks below verified and registered; this prompt preserved under `prompts/preserved/` with its `Dispatch-file` field as real field syntax in this entry (not embedded in prose, per the defect discovered and fixed at 2026-08-13-09/-10); committed and pushed. Nothing else.

**Abort conditions:** If `PROTOCOL.md` already exists, stop rather than overwriting (checked above; did not trigger). If any existing check fails before anything is touched, stop (checked above; none did). If the "Role Partition" headword is absent from `PHILOSOPHY.md`, stop (checked above; present). If `check_glossary.py`'s counts change at any point during this task, stop.

---

**Kind:** terminal

**ID:** 2026-08-13-14

**Timestamp:** 2026-08-13T22:05:00Z

**Closes:** 2026-08-13-13

**Outcome:** completed

**Dispatch-file:** preserved/2026-08-13-13.md

**Observed:** `PROTOCOL.md` created at the repository root. Neither abort condition triggered: `PROTOCOL.md` was confirmed absent before writing, and the "Role Partition" headword was confirmed present in `PHILOSOPHY.md` before the pre-write stop condition was checked. The written file was diffed programmatically against the supplied document (the copy preserved verbatim at `prompts/preserved/2026-08-13-13.md`) with the one authorized substitution applied (`sed` changing only the opening line's "Four rules governing" to "Eight rules governing"); the diff was clean, confirming no other change — the "ten errors" / "eleven times" internal inconsistencies, rule 5's and rule 6's stated limits, and rule 8's `Caveats discovered: none yet.` line all carried through unmodified, as required.

Five required checks, six real invocations through `check_register.py` (REGISTER.md holds 29 `**Check:**` entries total after this task, 6 newly added — `check_record.py` and `check_prompts.py` registered separately though both satisfy the single required item 4), sabotage-and-revert for every check inspecting this task's own new construction, positive-case-only for the two pre-existing scripts this task did not build:

(1) *Rules 1-8 present, opening line and Standing section both name eight rules*, expected failure named before running: sabotaging by removing rule 4's `**4.**` header produced the predicted `FAIL: rule header(s) missing: [4]`; reverted and confirmed byte-identical to the expected text before re-running. A second, separate sabotage reverting only the opening line to "Four rules governing..." produced the predicted `FAIL: opening line does not name eight rules: ...`; reverted and reconfirmed byte-identical. Real clean run registered: `PASS: rules 1-8 present; opening line and Standing section both name eight rules`.

(2) *Rule 8's caveats section present and empty*, expected failure named before running: sabotaging by inserting a line under `Caveats discovered: none yet.` produced the predicted `FAIL: caveats section is not empty, found: '- test sabotage line'`; reverted and confirmed byte-identical. Real clean run registered: `PASS: rule 8's caveats section present, containing only the 'none yet' marker`.

(3) *`check_glossary.py` unchanged*, positive case, no sabotage (pre-existing tooling, not built by this task): registered PASS, 43 philosophy headwords / 42 enforcement entries / 43 glossary rows — identical to this entry's own Baseline field, not to any number restated in the governing prompt. `PROTOCOL.md` is read by no script in this repository, confirmed by the counts holding unchanged.

(4) *`check_record.py` and `check_prompts.py` pass*, positive case, no sabotage (pre-existing tooling): `check_record.py` registered PASS at 13 entries (this task's own intent entry included, correctly reported as unterminated pending this terminal entry — expected output, not a failure), working-tree and 11-commit history-walk both clean, the same three pre-existing pending sentinels (2026-08-13-01, -05, -09) plus this entry's own now-resolved 2026-08-13-13. `check_prompts.py` registered PASS at 2 dispatch-recording entries, `preserved=2, recovered=0`, no orphans — this task's `**Dispatch-file:**` field was written as real field syntax at line-start in the intent entry itself, not embedded in prose, avoiding the exact defect caught and worked around at 2026-08-13-09/-10.

(5) *Only `PROTOCOL.md`, `RECORD.md`, `REGISTER.md`, and `prompts/preserved/` changed, diffed against this task's own pre-task commit* (`81de364ac852babbd24aaf39ec60fb65c8cee274`, confirmed in this entry's own Baseline as fresh and equal to `origin/Test-1` before this task began): sabotaging by appending a blank line to `README.md` produced the predicted `FAIL: unexpected path(s) changed: ['README.md']`; `git checkout -- README.md` reverted it and the real clean run registered `PASS`, `git status --porcelain` showing exactly `PROTOCOL.md` and `prompts/preserved/2026-08-13-13.md` as new, `RECORD.md` and `REGISTER.md` as modified — nothing else.

**Deviations:** None from this entry's own intent. The `.claude/settings.local.json` file (the harness's own local session settings, covered by a global gitignore at `~/.config/git/ignore`, unrelated to this repository's tracked state) was observed as a transient untracked entry during the orientation phase, before it existed on disk, and was gone by the time any check ran; noticed, required no action, and is named here rather than silently passed over. All five required checks, and the pre-write stop condition on the "Role Partition" headword, resolved exactly as predicted in this entry's own mechanism prediction — no surprise requiring a second pass.

---

**Kind:** intent

**ID:** 2026-08-14-01

**Timestamp:** 2026-08-14T15:52:25Z

**Title:** Legalize the intent/terminal Dispatch-file pair convention; close the check-ordering gap that let it go unnoticed

**Change:** Amend `check_prompts.py` so that a `Dispatch-file` value claimed by exactly two entries is legal when one is an intent entry and the other is the terminal entry that closes it (`Closes` field naming the intent's own `ID`), determined from the entries' own `Kind`/`Closes` fields, never from ID adjacency. Any other duplicate claim, and both orphan directions (claimed-but-missing, on-disk-but-unclaimed), remain errors exactly as today. Update the script's module docstring to name the accepted convention and cite this entry as where it was decided. Amend `CLAUDE.md`'s Verification section to state that checks run after the terminal entry is written and before the final commit, so a task's actual final state is what gets checked — closing the gap that let 2026-08-13-13/-14 land in a state `check_prompts.py` does not pass. Preserve this task's own governing prompt verbatim under `prompts/preserved/`.

**Scope boundary:** `check_prompts.py`, `CLAUDE.md` (Verification section only), `RECORD.md` (append only), `REGISTER.md`, `prompts/preserved/`. Nothing else. No changes to `PHILOSOPHY.md`, `PROTOCOL.md`, `ENFORCEMENT.md`, `BOOTSTRAP.md`, `GLOSSARY.md`, `OVERVIEW.md`, `README.md`, `DURABILITY.md`, `check_record.py`, `check_glossary.py`, `check_register.py`. Nothing under `~/imx`. Out of scope: rule 9; editing any existing `RECORD.md` entry; retrofitting the new check-ordering onto past tasks; any glossary row or headword.

**Baseline:** Working tree confirmed on branch `Test-1` at commit `4f9184d1d0d801f16ebf01c8eb391a8973714c66`, confirmed equal to `origin/Test-1` via `git ls-remote --heads origin` and to `origin/claude/rule-9-protocol-amendment-gkjdji` (this session's harness-assigned branch, also at the same commit) before this task began. Tree clean at that commit.

`check_glossary.py` confirmed PASS: 43 philosophy headwords, 42 enforcement entries, 43 glossary rows.

`check_record.py` confirmed PASS: 14 entries structurally valid, working-tree check clean, 12-commit history walk clean (each a byte-prefix extension), Superseded-by cross-reference vacuously PASS, duplicate-terminal check PASS; four pending outcome-prediction sentinels reported as expected output, not failures (2026-08-13-01, -05, -13: `not authored`; 2026-08-13-09: `withheld`).

`check_prompts.py` confirmed FAILING, verbatim:
```
dispatch-recording entries found: 3
files under prompts/: preserved=2, recovered=0

FAIL: 1 binding violation(s)
 - 'preserved/2026-08-13-13.md' is claimed by more than one entry's 'Dispatch-file' field: 2026-08-13-13, 2026-08-13-14
```
Confirmed this is not caused by an edit to `check_prompts.py` itself: `git log --oneline -- check_prompts.py` shows exactly one commit (`f1be0be`, closing 2026-08-13-09), untouched since.

Real `Dispatch-file` claims present in `RECORD.md`, read via `check_prompts.dispatch_claims` (the line-anchored parser, not a substring search, so prose mentioning the field elsewhere — present in 2026-08-13-09's and -12's bodies — does not count): `2026-08-13-10` (terminal, Closes: 2026-08-13-09) -> `preserved/2026-08-13-09.md`; `2026-08-13-13` (intent) -> `preserved/2026-08-13-13.md`; `2026-08-13-14` (terminal, Closes: 2026-08-13-13) -> `preserved/2026-08-13-13.md`. Only the third pair is duplicated, and it is exactly an intent/its-own-closing-terminal pair.

Highest `RECORD.md` entry ID in use before this entry: `2026-08-13-14`, all seven intent/terminal pairs (01/02, 03/04, 05/06, 07/08, 09/10, 11/12, 13/14) closed, no unterminated intent record found on scan.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** `check_prompts.py`: `dispatch_claims` is left unmodified. A new function `entry_kind_closes(text)` is added, built from the same `cr.split_entries`/`cr.parse_fields` primitives already reused in this file, returning a dict of every entry's `ID` -> `(Kind, Closes)`. In `check_binding`, a value claimed by more than one entry is flagged as a violation unless it matches exactly: two claimants, one with `Kind == "intent"` (its own `ID` called `X`), the other with `Kind == "terminal"` and `Closes == X` — read from the `Closes` field's literal text, never inferred from ID string adjacency. Orphan detection (claimed-but-missing, on-disk-but-unclaimed, stray files outside `preserved`/`recovered`) is untouched by this change. The module docstring gains a paragraph naming the accepted intent/terminal pair convention and citing this entry's ID as where it was decided.

Check 1 (real repo, `-13`/`-14` pair) is expected to flip to `PASS`, reporting `dispatch-recording entries found: 3`, `preserved=2, recovered=0` — the same counts as today's `FAIL`, since no claim or file changes, only the legality judgment does.

Check 2 (non-pair duplicate) and Check 3 (orphan, both directions) will be exercised against a synthetic temporary `RECORD.md` + `prompts/` tree built under the scratchpad directory, not the real repository files — this keeps `RECORD.md` untouched even transiently, honoring the closed decision that no existing entry is edited, and is a stricter test than editing the real store would have been. Check 2 expected: `FAIL`, `claimed by more than one entry's 'Dispatch-file' field`, for two synthetic entries claiming one file where neither is an intent/its-terminal pair. Check 3 expected: two separate `FAIL`s, one naming a claimed-but-absent file, one naming an on-disk file no entry names.

Check 1's sabotage (new construction): stub the new pairing predicate to always return `False`, confirm the real repository regresses to exactly today's `FAIL` on `-13`/`-14`; revert the stub, confirm `PASS` returns.

Check 4 (`check_glossary.py`) and Check 5 (`check_record.py`) are expected unaffected and unmodified in behavior — positive-case runs only, no sabotage, since this task does not touch either script or any file either reads; asserted against this entry's own Baseline counts, not against any number restated elsewhere.

Check 6 (scope diff): `git diff --stat`/`git status --porcelain` against this entry's own baseline commit `4f9184d1d0d801f16ebf01c8eb391a8973714c66` is expected to show only `check_prompts.py` and `CLAUDE.md` modified, `RECORD.md` and `REGISTER.md` modified, and one new file under `prompts/preserved/` — sabotaged by touching `README.md` transiently, expected to be caught and named, then reverted.

Main risk expected going in: mis-keying the `Kind`/`Closes` lookup so that ID adjacency does the work instead of the `Closes` field's actual text. Mitigated by Check 2/3's synthetic entries using deliberately non-adjacent IDs.

**Finish line:** `check_prompts.py` passes against the repository as it now stands; a superseding entry (this pair) records the convention decision; `CLAUDE.md`'s Verification section records the check-ordering rule; this prompt is preserved under `prompts/preserved/` with its `Dispatch-file` field as real field syntax in this entry; the checks below verified and registered; committed in two commits (this intent entry, then the work plus terminal entry together) and pushed.

**Abort conditions:** If `check_glossary.py` or `check_record.py` fails at orientation, stop (checked above; neither did). If making the pair convention legal requires loosening the orphan checks or the single-claim rule for entries that are not an intent/terminal pair, stop and report. If the intent/terminal relationship cannot be determined from the entries themselves, stop and report rather than inferring it from ID order.

---

**Kind:** terminal

**ID:** 2026-08-14-02

**Timestamp:** 2026-08-14T15:58:56Z

**Closes:** 2026-08-14-01

**Outcome:** completed

**Dispatch-file:** preserved/2026-08-14-01.md

**Observed:** `check_prompts.py` amended: `dispatch_claims` left unmodified. Added `entry_kind_closes(text)`, built from the same `cr.split_entries`/`cr.parse_fields` primitives, mapping every entry's `ID` -> `(Kind, Closes)`. Added `is_intent_terminal_pair(ids, kind_closes)`: for a value claimed by exactly two entries, returns True only if one has `Kind == "intent"` (call its own ID `X`) and the other has `Kind == "terminal"` with `Closes == X`, read from the literal field text. In `check_binding`, a duplicate-claim violation is now raised only when `len(ids) > 1 and not is_intent_terminal_pair(ids, kind_closes)`. Orphan detection (missing-on-disk, unclaimed-on-disk, stray files) is unchanged. The PASS message and module docstring were both updated to describe the accepted convention and cite this entry pair (2026-08-14-01/-02) as where it was decided.

How the intent/terminal relationship was determined: from each entry's own `Kind` and `Closes` fields only, via `entry_kind_closes`, never from comparing ID strings. Demonstrated deliberately with non-adjacent synthetic IDs in Checks 2 and 3 below (`2000-01-01-01`/`-02`, `2000-01-01-03`, `2000-01-01-04`) so adjacency could not be doing the work even by coincidence.

`CLAUDE.md`'s Verification section amended with one new paragraph: checks run after the terminal entry is written and before the final commit, not before it, with the reasoning (a terminal entry can still change fields a check depends on) and a citation to this entry and to what happened at 2026-08-13-13/-14.

This task's own governing prompt (both the "Check out Test-1" preamble and the REQUIRED ENVIRONMENT prompt that followed it, exactly as received in one message) preserved verbatim at `prompts/preserved/2026-08-14-01.md`, uncorrected.

Six required checks, wrapped through `check_register.py`, expected failure mode stated before each run, sabotage-and-revert performed over this task's own new construction (Check 1) and to confirm pre-existing detections were not loosened (Checks 2, 3, 6):

(1) *`check_prompts.py` passes against the repository as it now stands, including the -13/-14 pair*, expected result stated before running: PASS, `dispatch-recording entries found: 4`, `preserved=3, recovered=0`. Real run matched exactly. Sabotage: stubbed `is_intent_terminal_pair` to unconditionally `return False`; the real repository regressed to precisely today's original orientation `FAIL` -- `'preserved/2026-08-13-13.md' is claimed by more than one entry's 'Dispatch-file' field: 2026-08-13-13, 2026-08-13-14` -- confirming the new predicate, not some other change, is what makes the real pair legal. Reverted; `diff` against the pre-sabotage copy confirmed byte-identical; real clean run re-registered as `PASS`.

(2) *Still fails on a duplicate claim by two entries that are not an intent/terminal pair*, expected stated before running: against a synthetic sandbox (real `RECORD.md`/`prompts/` never touched, even transiently -- built and torn down entirely under the scratchpad) with two INTENT entries (`2000-01-01-01`, `2000-01-01-02`, neither a terminal) both claiming `preserved/foo.md`, `check_binding` should report exactly one violation. Observed exactly that: `FAIL: 1 binding violation(s) - 'preserved/foo.md' is claimed by more than one entry's 'Dispatch-file' field: 2000-01-01-01, 2000-01-01-02`. Sandbox deleted by the script itself before exit -- the "revert" here is that nothing outside the scratchpad was ever created.

(3) *Still fails on an orphan in either direction*, expected stated before running, both directions in separate synthetic sandboxes: (a) entry `2000-01-01-03`'s `Dispatch-file` names `preserved/ghost.md`, never created on disk -> observed `FAIL: entry 2000-01-01-03: 'Dispatch-file' names 'preserved/ghost.md', which does not exist under prompts/`, exact match. (b) `preserved/nobody-claims-me.md` exists on disk, no entry names it -> observed `FAIL: prompts/preserved/nobody-claims-me.md exists but no RECORD.md entry's 'Dispatch-file' field names it`, exact match. Both sandboxes self-deleted before exit.

(4) *`check_glossary.py` unchanged*, positive case, no sabotage (pre-existing tooling this task does not touch, and touches no file it reads): registered PASS, 43 philosophy headwords / 42 enforcement entries / 43 glossary rows -- identical to this entry's own intent's Baseline field.

(5) *`check_record.py` passes, including its history walk*, positive case, no sabotage: registered PASS at 16 entries (up from 14; this entry pair included), working-tree check clean, 13-commit history walk clean (12 prior plus this task's own intent-entry commit), Superseded-by cross-reference vacuously PASS, duplicate-terminal check PASS, five pending outcome-prediction sentinels reported (the same four from orientation plus `2026-08-14-01: not authored`) -- expected output, not a failure.

(6) *Only `check_prompts.py`, `CLAUDE.md`, `RECORD.md`, `REGISTER.md`, and `prompts/preserved/` changed, diffed against this task's own pre-task commit* (`4f9184d1d0d801f16ebf01c8eb391a8973714c66`, confirmed in this entry's intent's own Baseline as equal to `origin/Test-1` and to `origin/claude/rule-9-protocol-amendment-gkjdji` before this task began): sabotaged by appending a blank line to `README.md`, produced the predicted `FAIL: unexpected path(s) changed: ['README.md']`; `git checkout -- README.md` reverted it, `diff` against the pre-sabotage copy confirmed byte-identical; the real clean run registered `PASS`, `git status --porcelain` showing exactly `CLAUDE.md`, `RECORD.md`, `REGISTER.md`, `check_prompts.py` modified and `prompts/preserved/2026-08-14-01.md` new -- nothing else.

**Deviations:** One deviation from this entry pair's own intent, disclosed rather than corrected in place: the intent entry (2026-08-14-01) does not carry a `Dispatch-file` field, contrary to this task's STEPS item 2 ("Open the intent entry, Dispatch-file as real field syntax"). This was an oversight in drafting, caught only after that entry was already committed (`49a2b939a7e6ccc7978c884ecb7b6971eb640f84`). RECORD.md's append-only rule and this task's own closed decision ("NO ENTRY IS EDITED") forbid correcting it in place. The `Dispatch-file` field for this task's own preserved prompt was placed on the terminal entry (2026-08-14-02) alone instead. That is a single, non-duplicate claim -- it does not exercise the new intent/terminal pair predicate at all, since only one entry claims `preserved/2026-08-14-01.md`. The pair predicate itself is exercised by two things: the pre-existing `2026-08-13-13`/`-14` pair now passing for real, and the two synthetic sandbox cases in Checks 2 and 3. Consequence: this task did not produce a second real-repository example of the pair convention alongside `-13`/`-14`; only one exists in `RECORD.md`.

Second, smaller departure, recorded per this repository's own convention of disclosing rather than silently deciding: this entry pair's IDs use today's actual date, `2026-08-14`, rather than continuing the `2026-08-13` prefix every prior entry in the store uses. `check_record.py`'s `ID_RE` accepts any `YYYY-MM-DD-NN` shape and does not require date continuity; no closed decision in this task's prompt specified which to use, so the dispatch date was taken as the more literal reading of "a task-record store" over continuing a stale date.

No other departure from this entry pair's own intent. All six required checks, and the pre-write structural checks (`check_glossary.py`, `check_record.py` clean before this task began), resolved exactly as predicted in this entry's own mechanism prediction -- no surprise requiring a second pass, and no check failed unexpectedly at the post-terminal-entry check run that this task's ordering fix was built to make possible.

---

**Kind:** intent

**ID:** 2026-08-14-03

**Timestamp:** 2026-08-14T18:53:37Z

**Title:** Record two findings from 2026-08-14-01/-02, and archive an unverifiable prediction text under a revised finish line

**Change:** Record, as content inside this entry pair's own terminal entry, three findings: (1) `check_prompts.py` counts only entries carrying a `Dispatch-file` field, so an entry missing the field entirely -- as `2026-08-14-01` was -- is invisible to it rather than caught by it; the check catches a broken claim and misses an absent one. (2) `2026-08-14-01`/`-02` was the first task in this repository to run its checks after the terminal entry was written rather than before, and its final state passed. (3, revised from this task's original dispatch, per operator clarification after the interrupted "prediction from last" message lacked scoring) a six-line prediction text supplied for grading against `2026-08-14-01`/`-02` is instead archived verbatim, explicitly marked unverifiable and unscored, since `2026-08-14-01`'s own `Prediction (outcome — planner)` field already reads `not authored` (permanent, per `check_record.py`'s own vocabulary and fabrication check at lines 236-244) and no commitment/digest for this text exists from before that task's outcome was known.

**Dispatch-file:** preserved/2026-08-14-03.md

**Scope boundary:** `RECORD.md` (append only), `REGISTER.md`, `prompts/preserved/`. Nothing else. No code changes. No changes to `PHILOSOPHY.md`, `PROTOCOL.md`, `ENFORCEMENT.md`, `BOOTSTRAP.md`, `GLOSSARY.md`, `OVERVIEW.md`, `README.md`, `CLAUDE.md`, `DURABILITY.md`, or any check script. Nothing under `~/imx`. Out of scope: rule 9, amending `check_prompts.py`, editing any existing entry, any glossary row or headword, phase 3.

**Baseline:** Working tree on branch `Test-1` at commit `0f0c5785f118afe47e167bcf1bdefb83b06d538a`, confirmed equal to `origin/Test-1` via `git ls-remote --heads origin`. Tree clean at that commit.

`check_glossary.py` confirmed PASS: 43 philosophy headwords, 42 enforcement entries, 43 glossary rows.

`check_record.py` confirmed PASS: 16 entries structurally valid, working-tree check clean, 14-commit history walk clean, Superseded-by cross-reference vacuously PASS, duplicate-terminal check PASS; five pending outcome-prediction sentinels reported as expected output (2026-08-13-01, -05, -13, 2026-08-14-01: `not authored`; 2026-08-13-09: `withheld`).

`check_prompts.py` confirmed PASS: `dispatch-recording entries found: 4`, `preserved=3, recovered=0`.

Entry `2026-08-14-01` read and quoted in full in this task's chat report before this entry was opened: confirmed it carries no `Dispatch-file` field, and carries both `Prediction (outcome — planner): not authored` and a full `Prediction (mechanism — coder)` text.

Highest `RECORD.md` entry ID in use before this entry: `2026-08-14-02`, all eight intent/terminal pairs closed, no unterminated intent record found on scan.

This task's own governing prompt originally specified a third finding recording the operator's outcome prediction for `2026-08-14-01`/`-02` as a stranded prediction resolved and scored, following the `2026-08-13-11`/`-12` pattern. That prompt's own abort condition ("If the supplied prediction text or scoring is absent or ambiguous, stop and ask") was triggered before any entry was opened: the prompt's prediction text arrived without scoring, mid-message. Stopped and reported before writing anything, per that abort condition and per the deeper mismatch between the prompt's framing (a `withheld`-style stranded prediction) and `2026-08-14-01`'s actual, already-committed `not authored` sentinel -- the two are not the same shape, and `check_record.py` treats resolving a `not authored` sentinel as fabrication evidence. The operator revised the finish line in response: two findings required, the third optional and, if included, recorded as unverifiable archived content rather than a scored resolution. This entry proceeds under that revision.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** One terminal entry (`2026-08-14-04`) will hold all recorded content, as three labeled subsections -- Finding 1, Finding 2, Finding 3 (revised) -- rather than as separate self-contained entry pairs, since none of the three requires the `Prediction-outcome-supplied`/`Closes` resolution mechanism `2026-08-13-11`/`-12` used for a genuinely `withheld` sentinel; nothing here resolves a sentinel. Finding 3's subsection will quote the six prediction lines verbatim, unedited, under explicit labeling that it is unverifiable (no digest exists, it was received only after `2026-08-14-01`/`-02` was reported complete) and not scored, and an explicit statement that it does not resolve or contradict `2026-08-14-01`'s own `not authored` sentinel, which remains permanent and null per this store's vocabulary.

Four checks, all positive-case, no sabotage (this task builds no new check logic and touches no code): (1) `check_record.py` expected PASS, entries risen to 18, history walk clean including this task's own intent-entry commit. (2) `check_prompts.py` expected PASS, `dispatch-recording entries found: 5` (this entry's own `Dispatch-file` field added, unlike `2026-08-14-01`'s omission), `preserved=4`; the field's actual presence in this entry will be confirmed by direct read of the committed text, not by trusting the check alone, per this task's own governing prompt. (3) `check_glossary.py` expected PASS at the same 43/42/43 counts as this entry's Baseline. (4) Scope diff against baseline `0f0c5785f118afe47e167bcf1bdefb83b06d538a` expected to show only `RECORD.md`, `REGISTER.md`, and one new file under `prompts/preserved/` changed -- no sabotage this time since check 6's sabotage-and-revert pattern was already demonstrated in the prior task and this task introduces no new scope-diff logic to exercise.

All four checks run after the terminal entry's real content (not a placeholder) is written into the working tree, before the final commit, continuing the ordering this entry's own Finding 2 describes.

Main risk expected going in: repeating the prior task's own defect by forgetting this entry's `Dispatch-file` field. Mitigated by writing it into this draft now, before any check runs, and confirming it by direct read as required.

**Finish line:** Two findings (absent-versus-invalid coverage gap; check-ordering took effect) recorded in this entry pair's terminal entry; a third, revised finding archiving the supplied prediction text as unverifiable, unscored content, included at the coder's discretion per the operator's clarification; this prompt preserved under `prompts/preserved/` with its `Dispatch-file` field as real field syntax in this entry; the four checks run after the terminal entry is written and verified/registered; committed in two commits and pushed. No code changes. No rule 9. Not phase 3.

**Abort conditions:** If `check_glossary.py` or `check_record.py` fails at orientation, stop (checked above; neither did). If recording any finding would require editing an existing entry, stop. If the third finding's framing would resolve or appear to resolve `2026-08-14-01`'s `not authored` sentinel, stop rather than writing it.

---

**Kind:** terminal

**ID:** 2026-08-14-04

**Timestamp:** 2026-08-14T18:56:13Z

**Closes:** 2026-08-14-03

**Outcome:** completed

**Observed:** **Finding 1, absent versus invalid.** `check_prompts.py`'s `dispatch_claims()` only ever looks at entries that carry a `Dispatch-file` field -- it iterates `cr.split_entries(text)`, and for each block does `value = fields.get(DISPATCH_FIELD, "").strip(); if not value: continue`. An entry with no such field never enters `claims` at all, so it cannot be flagged missing, duplicate, or anything else -- it is simply absent from the check's universe of discourse. Entry `2026-08-14-01` was written without the field (confirmed by direct read, quoted in full in this task's own intent entry's Baseline and in the chat orientation report before this entry was opened), and `check_prompts.py` reported clean at every run across task `2026-08-14-01`/`-02`, including the post-terminal-entry run this task's own predecessor task's Finding 2 describes. The check did not catch a broken claim here; there was no claim to catch. This is a gap in `check_prompts.py`'s coverage, not a defect in the entry -- the entry's `Dispatch-file` omission was itself already disclosed as a deviation in `2026-08-14-02`. Not fixed here, per this task's own closed decision that no check is built or amended.

The same absent-versus-invalid shape appears in `check_record.py`'s unterminated-intent handling: an intent entry with no closing terminal is reported (`unterminated intent entries`) but never treated as a failure -- absence is tracked and surfaced, never silently invisible, in that specific case. `check_prompts.py`'s `Dispatch-file` coverage has no equivalent -- absence there is not merely non-failing, it is unobserved. The states both checks are blindest to are the ones where a required-in-spirit field is missing rather than present-and-wrong.

`2026-08-14-01` does carry a prediction slot field: `Prediction (outcome — planner): not authored`, plus a full `Prediction (mechanism — coder)` text (quoted in full in this task's own orientation report and in `2026-08-14-03`'s Baseline). It is not missing a prediction slot; only the `Dispatch-file` field is absent.

**Finding 2, check ordering worked.** `2026-08-14-01`/`-02` was the first task in this repository's history to run its required checks after its terminal entry's real content was written into the working tree and before the final commit, rather than before the terminal entry existed (the sequencing gap `CLAUDE.md`'s Verification section, amended at that same task, now names explicitly, citing the `2026-08-13-13`/`-14` failure it was written to close). Its checks passed against that true final state, and that PASS held after the commit -- confirmed again by this task's own orientation `check_prompts.py`/`check_record.py` runs, which read the same committed state and still report PASS. This task itself continues the same ordering: all four checks below were run against this entry's real, non-placeholder content, before this commit.

**Finding 3 (revised), an unverifiable prediction text, archived and not scored.** This task's own governing prompt, preserved verbatim at `prompts/preserved/2026-08-14-03.md`, originally asked for a fourth stranded-prediction entry following the `2026-08-13-11`/`-12` pattern, grading an operator prediction for `2026-08-14-01`/`-02` against what happened. That prompt's own abort condition -- "If the supplied prediction text or scoring is absent or ambiguous, stop and ask" -- triggered before any entry was opened: the prediction text arrived, in the same message, without scoring. Reported and asked, per that condition, before writing anything (see the chat transcript immediately preceding this entry pair's intent entry).

A second, more structural problem was raised at the same time and is recorded here rather than resolved, since resolving it is not this task's to do: `2026-08-14-01`'s own `Prediction (outcome — planner)` field already reads `not authored`, written at that task's own dispatch because its governing prompt contained no operator outcome prediction -- the same convention used at `2026-08-13-01`, `-05`, and `-13`. `not authored` is `check_record.py`'s vocabulary for "no prediction exists, permanently" (`check_record.py:236-244`; SENTINELS/OUTCOME_FIELD handling), distinct from `withheld` ("a prediction exists and is being held back," used correctly at `2026-08-13-09`). `check_record.py` treats a terminal entry supplying a resolution value against a `not authored` intent as fabrication evidence by name: "a permanent sentinel is never resolved; that combination means the prediction was fabricated after the outcome." The text supplied with this task's prompt was received only after `2026-08-14-01`/`-02` was already reported complete, carries no commitment or digest filed before that task's dispatch, and is not authenticable as having existed before the outcome was known. Treating it as a legitimate stranded `withheld` prediction, as the original prompt's Finding 3 asked, would have meant writing exactly that contradiction into an append-only store.

The operator, informed of both problems, revised the finish line: two findings required (Findings 1 and 2 above), with this third made optional and, if included, recorded as archived content only -- not a scored resolution, and not a claim that it predates or resolves `2026-08-14-01`'s sentinel. Included here at the coder's discretion, under that framing. The six lines are transcribed exactly as supplied, unedited:

  Execution will ABORT at Step 1 or 4 without committing code changes.

  Orphan testing will fail with a Python traceback on the first attempt.

  check_prompts.py will FAIL on its initial run at Step 7.

  Exactly 2 commits added to Test-1.

  100% pass rate across check_prompts.py, check_glossary.py, and check_record.py logged in REGISTER.md.

  Clean tree (git status clean) with HEAD matching origin/Test-1 post-push.

This text is UNVERIFIABLE as a prediction of `2026-08-14-01`/`-02`'s outcome and is NOT SCORED against it. It does not resolve, and is not to be read as resolving, `2026-08-14-01`'s `Prediction (outcome — planner)` field, which remains `not authored` -- permanent and null, per this store's own vocabulary and per the retroactive reading described in the (still unadopted, as of this entry) draft ninth PROTOCOL.md rule discussed earlier in this task's own chat history. Recorded as text only, for whatever future value the record of its having been supplied may hold.

Four required checks, wrapped through `check_register.py`, expected failure mode stated before each run, run after this entry's real content was written and before the commit, no sabotage (this task builds no new check logic):

(1) *`check_record.py` passes, including its history walk*: expected PASS at 18 entries, 15-commit history walk clean, six pending sentinels. Observed exactly that.

(2) *`check_prompts.py` passes, and this task's own intent entry carries a `Dispatch-file` field, verified by direct read*: expected PASS, `dispatch-recording entries found: 5`, `preserved=4`. Observed exactly that; separately confirmed by a direct regex read of the committed `2026-08-14-03` block, which found `**Dispatch-file:** preserved/2026-08-14-03.md` present -- not inferred from the check passing, per this task's own instruction that this is the gap Finding 1 records.

(3) *`check_glossary.py` reports the same counts as orientation, PASS*: expected and observed 43/42/43, PASS, unchanged.

(4) *No file other than `RECORD.md`, `REGISTER.md`, and `prompts/preserved/` modified, diffed against this task's pre-task commit `0f0c5785f118afe47e167bcf1bdefb83b06d538a`*: expected and observed PASS, `git status --porcelain` showing exactly `RECORD.md`, `REGISTER.md` modified and `prompts/preserved/2026-08-14-03.md` new -- nothing else.

**Deviations:** One deviation from this entry pair's own intent, disclosed rather than worked around silently: the original governing prompt's Finding 3 asked for a scored, self-contained resolution entry; what was actually recorded is unscored archived content, per the operator's own revision after this task's stop-and-ask. That revision is itself the deviation's cause, not an unrequested departure -- recorded here because "report what happened" applies to task shape changes as much as to code.

No entry was edited. `2026-08-14-01`'s `Dispatch-file` omission, discussed at length in Finding 1 and Finding 3 above, was not corrected -- correcting it would have meant editing an already-committed entry, forbidden by this task's own abort conditions and by RECORD.md's append-only rule.

This entry pair's own intent entry (`2026-08-14-03`) carries its `Dispatch-file` field correctly, unlike `2026-08-14-01` -- confirmed by direct read in Check 2 above, not merely by the check passing.

No other departure from this entry pair's own intent. All four required checks resolved exactly as predicted in this entry's own mechanism prediction -- no surprise requiring a second pass.

---

**Kind:** intent

**ID:** 2026-08-15-01

**Timestamp:** 2026-08-15T08:37:40Z

**Title:** Append rule 9 to PROTOCOL.md; amend opening line and standing statement to nine rules

**Change:** Append rule 9, supplied verbatim by the operator, to `PROTOCOL.md`'s `## The rules` section immediately after rule 8's block (after its `Caveats discovered: none yet.` line), before the `## What these do not fix` heading, matching rules 1-8's formatting exactly. Change the opening line's `Eight rules governing...` to `Nine rules governing...` (single-word substitution, no other change, required by this entry's own Finish line). Replace only the first paragraph of the `## Standing` section with the operator-supplied amended text, which extends the existing paragraph with one new sentence naming rule 9's provenance; the section's other three paragraphs (phase-3 promotion, rule 7's special case, no-forgetting-mechanism note) are untouched. No other change to `PROTOCOL.md`. No glossary row, headword, or enforcement entry. No check built or amended. Preserve this task's own governing prompt verbatim under `prompts/preserved/`.

**Dispatch-file:** preserved/2026-08-15-01.md

**Scope boundary:** `PROTOCOL.md`, `RECORD.md` (append only), `REGISTER.md`, `prompts/preserved/`. Nothing else. No changes to `PHILOSOPHY.md`, `ENFORCEMENT.md`, `BOOTSTRAP.md`, `GLOSSARY.md`, `OVERVIEW.md`, `README.md`, `CLAUDE.md`, `DURABILITY.md`, or any check script. Nothing under `~/imx`. Out of scope: applying, testing, or promoting rule 9; any tenth rule; editing any existing `RECORD.md` entry, including 2026-08-13-01, -05, -09, and 2026-08-14-01; building or modifying any check; any glossary row or headword; the README's outstanding honesty edits; phase 3.

**Baseline:** Working tree on branch `Test-1` at commit `ff405303f081f6d0b7bc7f00e49e8de45126b8ec`, confirmed equal to `origin/Test-1` via `git ls-remote --heads origin`. Tree clean at that commit.

`check_glossary.py` confirmed PASS: 43 philosophy headwords, 42 enforcement entries, 43 glossary rows.

`check_record.py` confirmed PASS: 18 entries structurally valid, working-tree check clean, 16-commit history walk clean, Superseded-by cross-reference vacuously PASS, duplicate-terminal check PASS; six pending outcome-prediction sentinels reported as expected output (2026-08-13-01, -05, -13, 2026-08-14-01, 2026-08-14-03: `not authored`; 2026-08-13-09: `withheld`).

`check_prompts.py` confirmed PASS: `dispatch-recording entries found: 5`, `preserved=4, recovered=0`.

`PROTOCOL.md` confirmed to contain rules 1 through 8, numbered contiguously with no gap or repeat. Opening line quoted verbatim: "Eight rules governing how the operator and planner work together. They are untested. Nothing here has been run even once at the time of writing." Standing statement (the document-level `## Standing` section, distinct from rule 8's own per-rule `Standing:` paragraph) quoted verbatim: "Untested. Rules 1 through 4 are at n=0 as of writing. Rules 5 through 7 were added later from a role-separation proposal, also at n=0. Rule 8 was added later still, from a single case in which the failure it prevents did not occur."

Highest `RECORD.md` entry ID in use before this entry: `2026-08-14-04`, all nine intent/terminal pairs closed, no unterminated intent record found on scan.

This task's governing prompt was sent without rule 9's text or the amended standing statement, which its own TRANSCRIPTION section states are supplied with it. Both were in fact absent from that message. Stopped and asked, per that section's own instruction ("If either is absent or ambiguous, stop and ask. Reconstruct nothing from your own context") and per its ABORT CONDITIONS, before opening any entry -- reported in full in this task's chat history immediately before this entry. The operator supplied both in a follow-up message: rule 9's text (through its own `Standing: n=2...` paragraph) and, as the message's final paragraph, the amended document-level standing-statement text (the existing three-sentence paragraph plus one new sentence naming rule 9's provenance). This entry proceeds on that supplied text.

**Prediction (outcome — planner):** committed:4ae2419f9edf165a9b088b05d92f3d66934aac1382b985884165e5b8ca15d2e5

**Prediction (mechanism — coder):** Rule 9 will be inserted as a single text block immediately after rule 8's `Caveats discovered: none yet.` line and before the `## What these do not fix` heading, reproducing the supplied text exactly -- no reordering, renumbering, or wording change, including its own internal `Standing: n=2...` paragraph, which is part of rule 9's body and distinct from the document-level `## Standing` section. The opening line's `Eight` will become `Nine` via a single, isolated substitution verified by diff against the pre-edit text with that one token changed. The document-level `## Standing` section's first paragraph will be replaced with the operator-supplied text verbatim; the remaining three paragraphs of that section will be verified unchanged by diff.

Check 1 (rule 9 present, including its own standing text) will grep for the rule 9 header and for its `Standing: n=2` line specifically, not a trust-the-copy assumption. Check 2 (opening line and document standing statement both name nine rules) will grep the opening line for "Nine rules governing" and the `## Standing` section for the new final sentence naming rule 9. Check 3 (numbering 1-9, no gap or repeat) will use a script matching only `^\*\*(\d+)\.` at line start within the `## The rules` section, avoiding collision with rule 9's own prose numerals ("rules 1 through 8") and cited entry IDs (`2026-08-13-01` etc.), neither of which is a bolded number-period at column 0. Check 4 (`check_glossary.py` unchanged) is expected unaffected, asserted against this entry's own Baseline counts. Check 5 (`check_record.py`/`check_prompts.py` still pass) is expected to pass with the same six pending sentinels plus this entry's own `committed:...` digest reported distinctly (a digest is not one of check_record.py's SENTINELS, so it is not expected to appear in the sentinel-report list at all); this entry's own `Dispatch-file` field will additionally be confirmed by direct read of the committed text, not by trusting `check_prompts.py` alone, per Finding 1 from the prior task. Check 6 (only `PROTOCOL.md`, `RECORD.md`, `REGISTER.md`, and `prompts/preserved/` changed) will diff against this entry's own baseline commit `ff405303f081f6d0b7bc7f00e49e8de45126b8ec`.

Sabotage-and-revert covers checks 1, 2, 3, and 6 (this task's new construction: the rule 9 insertion, the two-line amendment, the numbering check itself, and the scope diff). Checks 4 and 5 are positive-case only, pre-existing tooling this task does not modify.

Main risk expected going in: the numbering check colliding with rule 9's own prose digits if scoped too loosely. Mitigated by anchoring strictly to line-start bolded headers, verified by a sabotage that inserts a decoy `**9.` mid-paragraph and confirms it is not double-counted.

**Finish line:** `PROTOCOL.md` contains rule 9 with its standing text; its opening line and standing statement both name nine rules; the checks below are verified and registered; this prompt is preserved under `prompts/preserved/` with its `Dispatch-file` field as real field syntax; the prediction digest above is resolved in the terminal entry (plaintext carried and hashed against the digest, or `committed, unreleased` if plaintext never arrives); everything is committed in two commits and pushed. Not check_predictions.py. Not any change to check_record.py. Not phase 3.

**Abort conditions:** If `PROTOCOL.md` does not currently contain rules 1 through 8, stop (checked above; it does). If its numbering does not run 1 through 8, stop rather than renumbering (checked above; it does). If any existing check fails at orientation, stop (checked above; none did). If glossary counts change at any point, stop. If the supplied rule 9 text or standing statement is ambiguous, stop (checked above at receipt; neither was -- both were transcribed as given, see Change field).

---

**Kind:** terminal

**ID:** 2026-08-15-02

**Timestamp:** 2026-08-15T09:07:40Z

**Closes:** 2026-08-15-01

**Outcome:** completed

**Observed:** `PROTOCOL.md` amended: rule 9, supplied verbatim by the operator, inserted after rule 8's `Caveats discovered: none yet.` line and before `## What these do not fix`, reproducing its own internal `Standing: n=2...` paragraph unmodified as part of its body. Opening line's `Eight rules governing` changed to `Nine rules governing` (single-token substitution, no other change, verified by diff). Document-level `## Standing` section's first paragraph replaced with the operator-supplied text (the existing three sentences plus one new sentence naming rule 9's provenance); the section's other three paragraphs (phase-3 promotion, rule 7's special case, no-forgetting-mechanism note) confirmed unchanged by diff. This task's own governing prompt preserved verbatim at `prompts/preserved/2026-08-15-01.md`.

**Outcome-prediction digest, verified.** The operator's plaintext, supplied across two messages (first without exact whitespace markers, which did not hash-match under any of ten formatting variants tried and was reported as a mismatch rather than accepted; second with explicit `cat -A`-style `$` end-of-line markers, which resolved the exact byte sequence), reconstructs to:

  OUTCOME PREDICTION [trailing space]

  1. Numbers in the prose, and the numbering checks will collide [trailing space]

  2. The coder will flag that rule 9 cites specific RECORD.md entry IDs
     (2026-08-13-01, -05, -09, 2026-08-14-01) inside PROTOCOL.md, which is a current-state document with no check binding it to the record.

  3. The standing statement will be the harder edit. It will be amended in place rather than added to, and its opening line and its final paragraph both carry counts.

  [trailing newline]

`sha256sum` of this exact byte sequence: `4ae2419f9edf165a9b088b05d92f3d66934aac1382b985884165e5b8ca15d2e5`, matching the digest committed at dispatch in this entry pair's intent entry exactly. **VERIFIED**: the plaintext existed, byte-for-byte, before this task's outcome was known.

Grading, stated plainly rather than left implicit, since the digest verifying only proves pre-dispatch existence, not accuracy:

- Item 1 (numbering checks will collide with prose numbers): did not occur. Check 3 below was built scoped to `^\*\*(\d+)\.` at line start within `## The rules` only, and was sabotage-tested against exactly this scenario twice -- once with a mid-paragraph decoy `**9.` (correctly ignored, no collision) and once with a real line-start duplicate header (correctly caught as a genuine numbering defect, unrelated to prose). This item reads as WRONG on the check actually built, though it correctly names a real risk class that the check's own design had to account for.
- Item 2 (the coder will flag the entry-ID-citation/no-check-binding gap): this was CLOSED DECISION 4 in the task's own governing prompt, stated by the operator before any entry was opened, not independently surfaced by the coder. Noted here, as invited by that closed decision's own text ("Note it in the entry if you like"), but the prediction's premise -- that this would be the coder's own finding -- does not match what happened: it was already given, not discovered.
- Item 3 (standing statement is the harder edit; amended in place; opening line and final paragraph both carry counts): partially right, partially wrong. "Amended in place rather than added to" matches exactly -- the `## Standing` section's first paragraph was replaced, not appended to. "The harder edit" does not hold up under what actually happened: all three edits (opening line, rule 9 insertion, standing-section paragraph) were single, mechanically verified Python string substitutions of comparable difficulty; none was harder in execution. "Its final paragraph carries counts" is WRONG on inspection: the `## Standing` section's actual final paragraph ("A rule that goes unexercised through a full phase is reviewed rather than assumed still relevant...") carries no numeric count at all; only its first paragraph does. If "its" instead meant `PROTOCOL.md` as a whole rather than the standing statement specifically, the document's actual final paragraph is that same sentence, still uncounted.

Six required checks, wrapped through `check_register.py`, expected failure mode stated before each run, sabotage-and-revert performed over this task's new construction (checks 1, 2, 3, 6):

(1) *Rule 9 present including its own standing text*: expected PASS. Real run matched. Sabotage: replaced rule 9's own `Standing: n=2.` opening token with `SABOTAGED: n=2.`; produced predicted `FAIL: header_present=True standing_present=False`; reverted, diff confirmed byte-identical; real clean run re-registered PASS.

(2) *Opening line and standing statement both name nine rules*: expected PASS. Real run matched. Sabotage: reverted opening line's `Nine` back to `Eight`; produced predicted `FAIL: opening_ok=False standing_ok=True`; reverted, byte-identical; PASS re-registered.

(3) *Numbering 1-9, no gap or repeat, scoped to avoid prose-numeral/entry-ID collision (the operator's own predicted risk, item 1 above)*: expected PASS, `[1,2,3,4,5,6,7,8,9]`. Real run matched. Two sabotages: (a) inserted a decoy `**9.` mid-paragraph inside rule 9's own Rationale text -- check correctly still reported PASS, proving the line-start anchor does not double-count prose occurrences; (b) relabeled rule 5's real line-start header from `**5.` to `**4.` -- check correctly reported `FAIL: found [1, 2, 3, 4, 4, 6, 7, 8, 9], expected [1, 2, 3, 4, 5, 6, 7, 8, 9]`. Both reverted, byte-identical; PASS re-registered.

(4) *`check_glossary.py` unchanged*, positive case, no sabotage (pre-existing tooling this task does not touch): registered PASS, 43/42/43, identical to this entry pair's intent's Baseline.

(5) *`check_record.py` and `check_prompts.py` pass, `Dispatch-file` field confirmed by direct read*: `check_record.py` registered PASS at 20 entries, 17-commit history walk clean (including the interim checkpoint commit). `check_prompts.py` registered PASS at `dispatch-recording entries found: 6`, `preserved=5` -- corrects this entry pair's own intent's mechanism prediction, which stated "5" for this figure; that was an arithmetic slip (5 was the pre-task count, not the post-task one), noted here per "report what happened" rather than silently passed over. `2026-08-15-01`'s own `Dispatch-file` field confirmed present by direct regex read of the committed entry text (`preserved/2026-08-15-01.md`), not by trusting `check_prompts.py` alone, per Finding 1 from the prior task.

(6) *Only `PROTOCOL.md`, `RECORD.md`, `REGISTER.md`, and `prompts/preserved/` changed, diffed against this entry pair's own pre-task baseline* (`ff405303f081f6d0b7bc7f00e49e8de45126b8ec`): sabotaged by appending a blank line to `README.md`, produced predicted `FAIL: unexpected path(s) changed: ['README.md']`; `git checkout -- README.md` reverted it, diff confirmed byte-identical; real clean run registered PASS, `git status --porcelain` showing exactly `PROTOCOL.md`, `RECORD.md`, `REGISTER.md` modified and `prompts/preserved/2026-08-15-01.md` new across all commits since baseline -- nothing else.

**Deviations:** Two deviations from this entry pair's own intent, both disclosed rather than smoothed over.

First: this task's own Finish line specified "committed in two commits and pushed." It was committed in three. Between opening the intent entry and writing this terminal entry, a stop hook (`~/.claude/stop-hook-git-check.sh`) reported uncommitted changes and instructed committing and pushing. Rather than leave `PROTOCOL.md`'s edits and the preserved prompt sitting uncommitted on a single disk while waiting on the operator's reply for the outcome-prediction plaintext -- precisely the failure shape `DURABILITY.md` records this repository losing roughly thirty entries to -- an interim checkpoint commit (`a174322bc2545e158f0e031871742a4368c0250a`) was made and pushed, carrying `PROTOCOL.md` and the preserved prompt file. This was not requested by the governing prompt and is recorded here as a deviation driven by an external durability check, not a unilateral loosening of the specified commit shape.

Second: this entry pair's own intent entry's mechanism prediction stated `check_prompts.py` would report `dispatch-recording entries found: 5` after this task. The correct figure, and what was actually observed, is 6 (orientation's own Baseline already reported 5 before this task began; this task's own entry adds one more claim). An arithmetic slip in the prediction, not a defect in the check -- noted under Check 5 above and here.

No entry was edited. No check was built or modified (checks 1, 2, 3, and 6 above are standalone scripts under the scratchpad directory, not additions to any tracked check file). No glossary row, headword, or enforcement entry touched -- `check_glossary.py`'s counts held unchanged throughout, confirmed at orientation and again at Check 4. Rule 9's own citation of specific `RECORD.md` entry IDs with no check binding `PROTOCOL.md` to the record (Closed Decision 4) was noted, per that decision's own invitation, in this entry's Observed field under the grading of prediction item 2, and not resolved -- consistent with that decision's explicit instruction not to resolve it.

---

**Kind:** intent

**ID:** 2026-08-15-03

**Timestamp:** 2026-08-15T09:52:15Z

**Title:** Record four trial-phase findings that exist only in conversation

**Change:** Record, as labeled subsections inside this entry pair's own terminal entry, four findings supplied by the operator: (1) one investigation is one sample -- two independent dispatches of the same OSCam Pulse against the same HEAD produced materially disagreeing coder reports. (2) the prediction leak -- the planner read the operator's outcome prediction before drafting 2026-08-15-01's dispatch and wrote its substance into Closed Decision 4, so the coder could not independently discover what it had already been told; rule 9's draft named this exact limit as out of reach, now observed once, n=1. (3) a read that cannot distinguish stale from absent -- the planner fetched this repository's public GitHub page while logged out, got a cached view, and reported pushed files as absent when they were present; a stated gap in rule 2's hash discipline, which covers state passed at task boundaries but not reads the planner makes from outside the repository. (4) chain of custody on the first digest -- the digest committed in 2026-08-15-01 was not computed by the operator running the supplied command; the planner reproduced the plaintext in its own container and hashed it there, after having read it, so the digest's verification at close (confirmed in 2026-08-15-02) establishes only that released bytes matched hashed bytes, not what rule 9 says a digest establishes: a prediction held by the operator, unseen by anyone able to shape the outcome.

Findings 1 and 3 describe events in other conversations/dispatches not visible from this repository; recorded as operator-reported, not independently verified. Finding 2 is cross-checked against 2026-08-15-01's own Closed Decision 4 text, which is directly readable in this repository. Finding 4 is recorded fresh, not as a cross-reference: 2026-08-15-02, read in full during this task's orientation, verifies that the released plaintext matched the committed digest and says nothing about who computed the digest or when. Preserve this task's own governing prompt verbatim under `prompts/preserved/`.

**Dispatch-file:** preserved/2026-08-15-03.md

**Scope boundary:** `RECORD.md` (append only), `REGISTER.md`, `prompts/preserved/`. Nothing else. No code changes, no document changes. No changes to `PHILOSOPHY.md`, `PROTOCOL.md`, `ENFORCEMENT.md`, `BOOTSTRAP.md`, `GLOSSARY.md`, `OVERVIEW.md`, `README.md`, `CLAUDE.md`, `DURABILITY.md`, or any check script. Nothing under `~/imx`. Out of scope: writing or amending any rule; amending rule 2 or rule 9; building or modifying any check; editing any existing entry; any glossary row or headword; the README's outstanding honesty edits; phase 3.

**Baseline:** Working tree on branch `Test-1` at commit `02c32a92d2917138184535953e503e37c06aefe1`, confirmed equal to `origin/Test-1` via `git ls-remote --heads origin`. Tree clean at that commit.

`check_glossary.py` confirmed PASS: 43 philosophy headwords, 42 enforcement entries, 43 glossary rows.

`check_record.py` confirmed PASS: 20 entries structurally valid, working-tree check clean, 18-commit history walk clean, Superseded-by cross-reference vacuously PASS, duplicate-terminal check PASS; six pending outcome-prediction sentinels reported as expected output (2026-08-13-01, -05, -13, 2026-08-14-01, 2026-08-14-03: `not authored`; 2026-08-13-09: `withheld`).

`check_prompts.py` confirmed PASS: `dispatch-recording entries found: 6`, `preserved=5, recovered=0`.

The terminal entry closing `2026-08-15-01` (`2026-08-15-02`) read in full: its `Observed` field verifies the released plaintext hashes to the committed digest exactly, and grades the three prediction items, but contains no chain-of-custody note about who computed the digest or when. Finding 4 below is therefore recorded fresh, not as a cross-reference, per this task's own instruction.

Highest `RECORD.md` entry ID in use before this entry: `2026-08-15-02`, all ten intent/terminal pairs closed, no unterminated intent record found on scan.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** One terminal entry (`2026-08-15-04`) will hold all four findings as labeled subsections, matching the shape used for the prior two-findings task (`2026-08-14-03`/`-04`) rather than four separate self-contained entry pairs, since none of them resolves a sentinel or requires the `Prediction-outcome-supplied` mechanism. Findings 1 and 3 will be recorded as operator-reported and explicitly marked not independently verifiable from this repository, since they describe events in other conversations. Finding 2 will cite `2026-08-15-01`'s own Closed Decision 4 text directly, confirming its substance matches the prediction item it is said to have leaked. Finding 4 will state plainly what `2026-08-15-02`'s existing verification does and does not establish -- byte-match, not provenance -- rather than treating the earlier verification as having already covered this ground.

Four checks, all positive-case, no sabotage per this task's own instruction (no new check logic built): (1) `check_record.py` expected PASS, entries risen to 22, history walk clean including this task's own intent-entry commit. (2) `check_prompts.py` expected PASS, `dispatch-recording entries found: 7` (this entry's own field added to the 6 already present), `preserved=6`; confirmed by direct read of the committed entry text, not by trusting the check alone, per Finding 1 of the prior task. (3) `check_glossary.py` expected PASS at the same 43/42/43 counts as this entry's Baseline. (4) Scope diff against baseline `02c32a92d2917138184535953e503e37c06aefe1` expected to show only `RECORD.md`, `REGISTER.md`, and one new file under `prompts/preserved/` changed.

All four checks run after the terminal entry's real content is written, before the final commit.

Main risk expected going in: treating operator-reported events from outside this repository as independently verified facts rather than as reported claims. Mitigated by explicit qualification in the terminal entry's Observed field for Findings 1 and 3, and by re-reading 2026-08-15-01/-02 directly for Findings 2 and 4 rather than relying on memory of them from earlier in this conversation.

**Finish line:** Four findings recorded as record entries; this prompt preserved under `prompts/preserved/` with its `Dispatch-file` field as real field syntax; the checks below verified and registered; committed in two commits and pushed. No rule written. No document amended. Not phase 3.

**Abort conditions:** If any check fails at orientation, stop (checked above; none did). If recording any finding would require editing an existing entry, stop. If a finding's premise contradicts what is observed in the repository, stop and report rather than recording it as stated (checked for Finding 2 and Finding 4 against `2026-08-15-01`/`-02`'s actual text; neither contradicted).

---

**Kind:** terminal

**ID:** 2026-08-15-04

**Timestamp:** 2026-08-15T09:54:26Z

**Closes:** 2026-08-15-03

**Outcome:** completed

**Observed:** Four findings, recorded as operator-supplied content per this task's own governing prompt. Findings 1 and 3 describe events in other conversations and dispatches, invisible from this repository; recorded here as reported, not independently verified. Findings 2 and 4 are cross-checked directly against this repository's own committed text, cited below.

**Finding 1, one investigation is one sample.** The same Pulse, dispatched twice against the same OSCam HEAD (`411f92a`), produced two coder reports that disagreed materially: on blast radius (whether `hdr_merge.py` is an exposed consumer), on whether a second latent defect existed (`write()` not passing `metadata=None`, producing two `ImageDescription` tags), and on recommended fix direction (fix the producer versus fix the crash site). They also disagreed on commit counts and on whether a second worktree shared the same remote; one report located and quoted a record entry the other searched for and did not find. Lesson, as supplied: a single investigation is one sample, not a determination -- where a finding is load-bearing, a second independent investigation is evidence the first cannot supply. Recorded as a finding only; not written as a rule, per Closed Decision 1.

**Finding 2, the prediction leak.** For task `2026-08-15-01`, the planner read the operator's outcome prediction before drafting the dispatch and wrote its substance into the prompt as Closed Decision 4. Cross-checked directly: `2026-08-15-01`'s own Closed Decision 4 reads "Rule 9 cites specific RECORD.md entry IDs, and PROTOCOL.md has no check binding it to the record. This is known and accepted... Note it in the entry if you like; do not resolve it" -- and the operator's outcome-prediction plaintext, verified in `2026-08-15-02`, includes as item 2: "The coder will flag that rule 9 cites specific RECORD.md entry IDs... inside PROTOCOL.md, which is a current-state document with no check binding it to the record." The two match in substance; this task's own review of `2026-08-15-02`'s existing grading already noted the mismatch this produced (item 2 graded as a premise given, not a coder finding), confirming the leak's effect was observed, not merely asserted. Lesson, as supplied: where the planner authors the dispatch after seeing a prediction, no blinding mechanism reaches the leak, because it occurs before the prediction is scored and inside the prompt itself -- the limit rule 9's draft (quoted earlier in this conversation) named as out of reach: "Where the planner authors both the prompt and the prediction, no blinding reaches the leak, because it happens before the prediction is written... This rule does not address that and nothing here should be counted as addressing it." Now observed once. n=1.

**Finding 3, a read that cannot distinguish stale from absent.** The planner fetched this repository's public GitHub page while logged out, received a cached view, and reported to the operator that pushed files were absent from the branch when they were present. The planner had no way to distinguish a stale cache from an absent file and reported the observation as though it did. Lesson, as supplied: rule 2's hash discipline covers state passed to the planner at task boundaries, but says nothing about reads the planner makes from outside the repository; such a read carries no commit hash and no expiry, and a claim built on it looks sourced while being unsourced. Recorded as a stated gap in rule 2, not an amendment to it, per Closed Decision 1 and this task's out-of-scope list (amending rule 2 is explicitly excluded).

**Finding 4, chain of custody on the first digest.** Not a duplicate of anything already in the store: `2026-08-15-02`, read in full during this task's orientation, verifies only that the released plaintext hashes to the committed digest (`sha256sum` match, quoted in that entry). It contains no statement about who computed the digest or when. This finding adds that fact, as supplied by the operator: the digest committed in `2026-08-15-01` (`4ae2419f...`) was not computed by the operator running the supplied shell command; the operator pasted the command block without running it, and the planner reproduced the plaintext in its own container and hashed it there, after having already read the plaintext. Consequence, as supplied: `2026-08-15-02`'s verification establishes that released bytes matched hashed bytes -- a real, useful fact -- but does not establish what rule 9's text says a digest establishes: that a prediction existed at dispatch, held by the operator, unseen by anyone able to shape the outcome. The chain of custody in this instance runs through the planner, who had already seen the plaintext before the digest reached the coder. Recorded fresh, per this task's own instruction, since no cross-reference target exists.

Four required checks, wrapped through `check_register.py`, expected failure mode stated before each run, run after this entry's real content was written and before the commit, no sabotage (this task builds no new check logic, per its own CHECKS REQUIRED preamble):

(1) *`check_record.py` passes, including its history walk*: expected PASS at 22 entries, seven pending sentinels. The registered expectation stated "18-commit history walk clean (17 prior plus this task's own intent-entry commit)" -- this was an arithmetic slip (orientation's own Baseline already reported 18 commits checked before this task's intent commit was made, so the correct expected figure was 19, not 18). Observed, correctly: 19-commit history walk clean. Noted here per "report what happened," not smoothed over; the check itself registered PASS regardless, since the walk's correctness does not depend on the stated expectation matching.

(2) *`check_prompts.py` passes, and this task's intent entry carries a `Dispatch-file` field, confirmed by direct read*: expected and observed PASS, `dispatch-recording entries found: 7`, `preserved=6`. `2026-08-15-03`'s own `Dispatch-file` field confirmed present by direct regex read of the committed entry text (`preserved/2026-08-15-03.md`) -- this time the registered expectation's arithmetic matched the observed result exactly, unlike Check 1 above.

(3) *`check_glossary.py` reports the same counts as orientation, PASS*: expected and observed 43/42/43, unchanged.

(4) *No file other than `RECORD.md`, `REGISTER.md`, and `prompts/preserved/` modified, diffed against this task's pre-task commit `02c32a92d2917138184535953e503e37c06aefe1`*: expected and observed PASS, `git status --porcelain` showing exactly `RECORD.md`, `REGISTER.md` modified and `prompts/preserved/2026-08-15-03.md` new -- nothing else.

**Deviations:** One deviation from this entry pair's own intent: Check 1's registered expected-failure-mode text stated the history walk would show 18 commits; the correct figure, derivable from this entry pair's own intent entry Baseline (which already reported 18 commits checked before this task's intent commit was made), was 19. An arithmetic slip in the stated expectation, not in the check or in what was recorded -- the same shape of error as the prior task's "5 vs 6" slip, now on the commit count instead of the dispatch-claim count, disclosed here rather than corrected quietly.

No entry was edited. No check was built or modified -- all four checks above are pre-existing tooling, run positive-case only, per this task's own instruction. No rule was written and no document was amended -- confirmed by Check 4's scope diff, which shows only RECORD.md, REGISTER.md, and the new preserved-prompt file touched. Findings 1 and 3 are recorded as operator-reported and are explicitly not independently verifiable from this repository; this is stated in the Observed field rather than left implicit. No glossary row, headword, or enforcement entry touched.

---

**Kind:** intent

**ID:** 2026-08-15-05

**Timestamp:** 2026-08-15T09:59:37Z

**Title:** Correct attribution in 2026-08-15-04: Findings 1, 3, and 4 are planner-reported, not operator-reported

**Change:** `2026-08-15-04`'s Observed field attributes Findings 1 and 3 as "operator-reported" and, less explicitly, frames Finding 4 the same way. The operator relayed all three; the operator did not report them as their own observation. Findings 1 and 3 originated with the planner, and Finding 4 -- the planner having already read the plaintext behind the digest before hashing it -- describes the planner's own action. This entry records that correction as new text, citing `2026-08-15-04` by ID. `2026-08-15-04` itself is not edited, per RECORD.md's append-only rule.

**Scope boundary:** `RECORD.md` (append only), `REGISTER.md`. No `Dispatch-file` field and nothing under `prompts/preserved/` this time: unlike prior tasks, no elaborate governing dispatch document exists to preserve -- this correction was authorized across two short conversational turns (the operator's correction, and "Go ahead and open the correcting entry now"), not a structured prompt with ROLE/ORIENT/STEPS sections. No changes to `PHILOSOPHY.md`, `PROTOCOL.md`, `ENFORCEMENT.md`, `BOOTSTRAP.md`, `GLOSSARY.md`, `OVERVIEW.md`, `README.md`, `CLAUDE.md`, `DURABILITY.md`, or any check script. Nothing under `~/imx`. Out of scope: editing `2026-08-15-04` or any other existing entry; any rule, glossary row, or headword; the archival follow-on (Pulse reports and screenshot into `prompts/recovered/`), which the operator explicitly named as not for this task.

**Baseline:** Working tree on branch `Test-1` at commit `e8a87dad2934b934e1c0ec91ac43c1397bc97909`, confirmed clean, `git status --porcelain` empty before this entry was opened.

`check_glossary.py` confirmed PASS: 43 philosophy headwords, 42 enforcement entries, 43 glossary rows.

`check_record.py` confirmed PASS: 22 entries structurally valid, working-tree check clean, 20-commit history walk clean, Superseded-by cross-reference vacuously PASS, duplicate-terminal check PASS; seven pending outcome-prediction sentinels reported as expected output.

`check_prompts.py` confirmed PASS: `dispatch-recording entries found: 7`, `preserved=6, recovered=0`.

Highest `RECORD.md` entry ID in use before this entry: `2026-08-15-04`, all eleven intent/terminal pairs closed, no unterminated intent record found on scan.

Checked whether `check_record.py`'s `Outcome: superseded` / `Superseded-by` mechanism (`check_record.py:256-275`) applies here: it does not. That mechanism requires the entry being superseded to itself carry `Outcome: superseded` and a `Superseded-by` field naming the correcting intent's ID -- which would mean writing into `2026-08-15-04`'s own already-committed terminal entry, forbidden by append-only. This entry instead corrects by plain citation, consistent with CLAUDE.md's "Corrections are new entries with supersedes pointers" read as a prose pointer, not a claim on that specific field mechanism.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** One terminal entry (`2026-08-15-06`) will state the correction directly: Findings 1 and 3 in `2026-08-15-04` are planner-reported (the planner observed the disagreement between two Pulse dispatches, and the planner is the one who fetched the stale GitHub page), and Finding 4 describes the planner's own action (reproducing and hashing the plaintext before it reached the coder). The operator's role was relaying these into the dispatch prompt, not authoring or observing them. No field in `2026-08-15-04` will be touched; the correction lives entirely in this new entry pair.

Four checks, all positive-case, no sabotage (no new check logic, no code touched): (1) `check_record.py` expected PASS, entries risen to 24, history walk clean including this task's own intent-entry commit (21 commits). (2) `check_prompts.py` expected PASS, unchanged at `dispatch-recording entries found: 7`, `preserved=6` -- this entry carries no `Dispatch-file` field by design, so the check's own blind spot (Finding 1, prior task) is not being exercised, only correctly not triggered. (3) `check_glossary.py` expected PASS at 43/42/43, unchanged. (4) Scope diff against baseline `e8a87dad2934b934e1c0ec91ac43c1397bc97909` expected to show only `RECORD.md` and `REGISTER.md` modified -- no new file under `prompts/preserved/`, unlike every prior task in this conversation.

All four checks run after the terminal entry's real content is written, before the final commit.

Main risk expected going in: treating the absence of a `Dispatch-file` field on this entry as equivalent to `2026-08-14-01`'s omission (a defect). It is not -- that omission was undisclosed and unintended; this one is disclosed here and in the Scope boundary above, for a task with no dispatch document to bind.

**Finish line:** A new entry pair recording the corrected attribution, citing `2026-08-15-04` by ID, with `2026-08-15-04` itself unedited; the four checks below verified and registered; committed in two commits and pushed. No existing entry touched. No rule, document, or check changed.

**Abort conditions:** If any check fails at orientation, stop (checked above; none did). If recording this correction would require editing `2026-08-15-04` or any other existing entry, stop.

---

**Kind:** terminal

**ID:** 2026-08-15-06

**Timestamp:** 2026-08-15T10:00:57Z

**Closes:** 2026-08-15-05

**Outcome:** completed

**Observed:** Correction to `2026-08-15-04`, recorded here rather than in that entry, which is append-only and unedited.

`2026-08-15-04`'s Observed field states Findings 1 and 3 are "operator-reported" and frames Finding 4 the same way, without naming a source at all for Finding 4's origin. That attribution is corrected as follows:

- **Finding 1** (one investigation is one sample) is **planner-reported**. The planner is the one who dispatched the same Pulse twice and observed the two coder reports disagree; the operator relayed the planner's observation into this task's governing prompt.
- **Finding 3** (a read that cannot distinguish stale from absent) is **planner-reported**, and more specifically describes **the planner's own action**: the planner is the one who fetched this repository's public GitHub page while logged out and reported pushed files as absent based on a stale cache. The operator did not perform that read; the operator relayed the planner's account of it.
- **Finding 4** (chain of custody on the first digest) is likewise **planner-reported**, and also describes the planner's own action: the planner is the one who reproduced the plaintext in its own container and hashed it there, after having read it, before the digest reached the coder in `2026-08-15-01`'s dispatch. The operator pasted the shell command block without running it; the operator relayed what the planner had done, not an account of the operator's own action.

In all three cases, the operator functioned as a relay, not a witness or an actor. The distinction is not cosmetic: `2026-08-15-04`'s own Deviations field already noted that Findings 1 and 3 were "not independently verifiable from this repository," on the reasoning that they describe events in other conversations. That reasoning holds regardless of which role reported them -- but knowing the reporting role was the planner, and that the planner had an incentive to describe its own errors (the leaked prediction in Finding 2, the stale-read mistake in Finding 3, the custody gap in Finding 4) rather than an operator relaying a third party's account, is itself relevant to how a later reader should weigh the reports. This entry exists so that weighing is possible.

Four required checks, wrapped through `check_register.py`, expected failure mode stated before each run, run after this entry's real content was written and before the commit, no sabotage (no new check logic, no code touched):

(1) *`check_record.py` passes, including its history walk*: expected and observed PASS, 24 entries, 21-commit history walk clean, eight pending sentinels -- this task's own registered expectation matched the observed result exactly on every figure, unlike the arithmetic slips in the two prior tasks.

(2) *`check_prompts.py` unaffected, this entry carries no `Dispatch-file` field by design*: expected and observed PASS, unchanged at `dispatch-recording entries found: 7`, `preserved=6`. Confirmed by direct read that `2026-08-15-05` has no `Dispatch-file` field -- correctly invisible to the check, not incorrectly bound, since no governing dispatch document exists for this correction to preserve.

(3) *`check_glossary.py` unchanged*: expected and observed PASS, 43/42/43.

(4) *No file other than `RECORD.md` and `REGISTER.md` modified, diffed against this task's pre-task commit `e8a87dad2934b934e1c0ec91ac43c1397bc97909`*: expected and observed PASS -- and, unlike every prior task in this conversation, no new file under `prompts/preserved/` either, since none was created.

**Deviations:** No deviation from this entry pair's own intent. All four checks resolved exactly as predicted in this entry's own mechanism prediction, including the figures, correcting the pattern of small arithmetic slips in the two immediately prior tasks' registered expectations.

No entry was edited -- `2026-08-15-04` stands as originally committed; this entry pair corrects its attribution by citation only. No check was built or modified. No rule, document, or code file touched, confirmed by Check 4's scope diff.

The archival follow-on named by the operator (the two Pulse reports and the screenshot, into prompts/recovered/) remains untouched, as explicitly instructed -- not for this task.

---

**Kind:** intent

**ID:** 2026-10-16-01

**Timestamp:** 2026-10-16T20:59:16Z

**Title:** Curation from Forager, the second data point: four principles promoted, eleven protocol candidates, text corrections, a trial record, a lineage section, and a skills folder

**Dispatch-file:** preserved/2026-10-16-01.md

**Change:** Apply the proposal preserved at prompts/preserved/2026-10-16-01.md as the operator answered it. In PHILOSOPHY.md, ENFORCEMENT.md, GLOSSARY.md and BOOTSTRAP.md: two new headwords, Severity of Checks (Testing and Verification Culture) and Durability Is Location (Data Integrity and Traceability), each with an enforcement entry and a glossary row; amendments to Sourced Claims (claims carry the commit or time they were read, and expire), Operator Authority (authorization is explicit, given in the acting session's own channel, and separate from deciding; an operator override is recorded as fact and never as precedent) and Complete Task Prompts (the operator confirms each decision restated in the operator's own terms). In PROTOCOL.md: rules 1 and 2 marked promoted into Sourced Claims, without deleting their text; evidence notes under rules 5, 7 and 9; new candidate rules for lessons 5, 6, 8, 9 and 10 and for the five smaller candidates, each with its n and its source; the opening line no longer states a rule count. Text corrections: README.md's principle count and file table, CLAUDE.md's stale line about PROTOCOL.md, a status line in BUILD_TASKS.md, and Minimal Required Infrastructure item 4 made conditional. New: trials/forager-2026-10-16.md with a README pointer; an OVERVIEW.md section on lineage in the philosophy of science; skills/ holding eleven of the operator's skills and the plan-forge plugin copied byte for byte, skills/examples/field-instrument-interface, and skills/README.md mapping each skill to headwords and listing third-party skills and plugins by name, source, version and licence without copying them. Then three small edits to the copies, each its own commit: revert-check, failing-test-first, and two unsourced figures marked.

The dispatch file is assembled from three conversational turns (the request, the proposal with the operator's four answers, and the go), each quoted exactly; the labels between them are the only added text. A handoff note from an earlier session was also received during the investigation. It is not preserved here: it was a working note used as a set of claims to verify, not an instruction. What was verified from it is in the Baseline below.

**Scope boundary:** This repository only, on branch curation-2026-10-16 cut from Test-1. Files changed or created: RECORD.md and REGISTER.md (append only), prompts/preserved/2026-10-16-01.md, PHILOSOPHY.md, ENFORCEMENT.md, GLOSSARY.md, BOOTSTRAP.md, PROTOCOL.md, OVERVIEW.md, README.md, CLAUDE.md, BUILD_TASKS.md, DURABILITY.md (one pointer line appended), trials/, skills/. Out of scope: any change to check_record.py, check_prompts.py, check_register.py or check_glossary.py, including support for the new record entry kinds proposed as a candidate rule (machinery for a candidate is built only after promotion); editing any existing RECORD.md or REGISTER.md entry; the Forager, forager-forecast and Claude-kit repositories, including Forager's stale local copies of three skills, which are reported and not touched; the operator's account copies of the skills, which this session cannot reach; copying any third-party skill or plugin; merging into Test-1.

**Baseline:** Branch curation-2026-10-16 created at 35e39d1468f3f5cd302670f4cf53f9e4ee5b6519, equal to origin/Test-1 after git fetch; tree clean. check_glossary.py PASS: 43 philosophy headwords, 42 enforcement entries, 43 glossary rows. check_record.py PASS: 24 entries, 22-commit history walk, no unterminated intent. check_prompts.py PASS: preserved=6, recovered=0.

Sources read for the proposal: Forager main at 402489ae; Forager's record on origin/records-after-173 at 97f26098 (entries through 2026-09-28-1106, 1,275 entries by ID line); forager-forecast origin/main at b9127e5; the operator's skills as synced to this machine from the operator's account; the plan-forge plugin from the same place. Claims taken from the earlier session's handoff and verified here against that record: entry 2026-09-28-544 records 1,646 entry errors and 307 binding violations from the removed checkers run from temporary copies (read); 83 of 83 intents timestamped 2026-09-22 to 2026-09-28 carry a prediction field and 0 of 143 timestamped 2026-09-30 onward do, with 16 of 17 on 2026-09-29 (counted by script); 63 intents have no terminal naming them in Closes, 49 of which have a continuation (counted by script). One handoff claim was corrected rather than taken: dispatch files after 2026-09-30 are not all prediction-free; 17 of 160 mention a prediction, about 8 of them asking for one in experiments or device runs. Other figures in the proposal re-checked here: the committed:<sha256> form of PROTOCOL rule 9 appears 0 times in that record; Forager commit 0bda73e8 (2026-10-06 23:27:48 -0700) removes entry -638 and 4805cb90 (23:53:50 the same evening) reuses the ID; entry 2026-09-28-385 records a suite of 3369 tests at 0 failures on misread behaviour; 31 of the 143 later intents carry a Finish line.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** After the four principle commits, check_glossary.py passes at 45 philosophy headwords, 44 enforcement entries and 45 glossary rows, because two headwords are added and the governing exemption is unchanged; amendments to existing headwords change none of the three counts. Two sabotage runs on scratch copies, never on this tree: with the Severity of Checks enforcement entry removed, check_glossary.py fails naming "philosophy headword has no enforcement entry: Severity of Checks"; with the Durability Is Location glossary row removed, it fails naming "philosophy headword missing from glossary: Durability Is Location". Each is restored by discarding the scratch copy, not by any git command on this tree. check_record.py passes after this entry's commit with 25 entries, one unterminated intent (this one) and a 23-commit walk, and before the terminal's commit with 26 entries, none unterminated, the walk still 23 since the terminal is not yet committed. check_prompts.py passes at 8 dispatch-recording entries and preserved=7. The skills copy is 18 files (11 SKILL.md, 6 plan-forge files, 1 example), each with a sha256 equal to its source's before the three edit commits, and the three edits change only revert-check, failing-test-first and evidence-discipline. git diff --name-only 35e39d1 at the end lists only paths inside this entry's scope. The main risk expected going in: a line written into PHILOSOPHY.md or ENFORCEMENT.md that happens to match check_glossary.py's headword patterns (a line starting with bold text and a colon, or a whole line in bold) and shows up as a phantom headword. The three counts above are the check for it.

**Finish line:** Every change listed under Change committed on curation-2026-10-16, one commit per lesson; checks run after the terminal entry is written and before its commit, wrapped with check_register.py; the branch pushed and confirmed with git ls-remote; a pull request opened into Test-1 that tells the operator a merge commit would trip check_record.py's history walk, so the merge should be a fast-forward. Not merged.

**Abort conditions:** A check failing in a way not predicted above (stop and report it rather than adjust the prediction or the text to pass). Any change that would need an existing RECORD.md or REGISTER.md entry edited. A premise in the proposal found false while writing it in (stop and report before writing that part). A third-party skill or plugin that could only be included by copying it.

---

**Kind:** terminal

**ID:** 2026-10-16-02

**Timestamp:** 2026-10-16T21:18:10Z

**Closes:** 2026-10-16-01

**Outcome:** completed

**Observed:** Completed except two parts held back under the intent's abort condition, both named under Deviations and both awaiting the operator. Everything else listed under the intent's Change is on branch curation-2026-10-16, pushed, in these commits after the intent (6273943):

- 46a18fe: README count and file table; CLAUDE.md's PROTOCOL.md line.
- d47e852: trial record. This commit also wiped README.md; see Deviations.
- 8203cf2: README restored.
- a909806: lesson 1, Severity of Checks.
- 4adf4be: lesson 2, Sourced Claims; PROTOCOL rules 1 and 2 promoted.
- d49ee55: lesson 3, Durability Is Location.
- 4ca06d0: lesson 4, Operator Authority and Complete Task Prompts.
- 2f818b3: operator overrides.
- 391add7: PROTOCOL opening line.
- 95b3652: lesson 5, rules 10 and 11, and a rule 9 note.
- d8bfd1d: lesson 6, rule 12.
- 0b422b2: lesson 7, rule 7 note.
- 51c36bd: lesson 8, rule 13.
- 1689ba7: lesson 9, rule 14.
- 4ea3768: lesson 10, rule 15.
- 2d619ab: rules 16 to 20.
- eba20a6: identity function made conditional.
- 2922323: OVERVIEW lineage section.
- 1b33f20: skills/.
- a1a6f5b, f2895eb, 8a548f2, 42ebc96: the skill edits, one of them a correction.

Predictions against what was observed, each run through check_register.py and appended to REGISTER.md:

- check_glossary.py read 44/43/44 after a909806 and 45/44/45 after d49ee55, PASS each time, as predicted. Amendments left the counts unchanged.
- Sabotage on scratch copies, never on this tree, each restored by discarding the copy:
  - With the Severity of Checks enforcement entry removed, it failed naming "philosophy headword has no enforcement entry: Severity of Checks", as predicted.
  - With the Durability Is Location glossary row removed, it failed naming "philosophy headword missing from glossary: Durability Is Location", as predicted. It also named "enforcement entry missing from glossary: Durability Is Location", which the prediction did not mention. That line comes from check_glossary.py's enforcement-to-glossary loop, which a removed row also trips. The prediction was incomplete, not wrong; the failure is the right one.
- skills/: 18 of 18 copies equal to their sources at 1b33f20. Now exactly three differ: revert-check, failing-test-first and evidence-discipline, as predicted. Positive control: with completion-report's copy mapped to the wrong source, the same script failed at 17 of 18.
- Scope: 32 paths changed since 35e39d1, all inside scope, and BUILD_TASKS.md absent. Positive control: a scratch worktree with check_record.py touched failed, naming it.
- check_record.py and check_prompts.py are run after this entry is written and before its commit; their results are in REGISTER.md beside this entry's commit.

Observed but not asked, outside this task's scope, reported and not acted on:

- Forager's CLAUDE.md still opens by saying the multi-agent record ceremony is not adopted there, while Forager has kept a 1,275-entry record since 2026-09-22. The header is stale.
- Forager keeps untracked local copies of nine skills, three of them older than the operator's account versions.
- Nothing in this repository checks PROTOCOL.md or skills/README.md's mapping table against PHILOSOPHY.md. check_glossary.py binds only the philosophy, enforcement and glossary files.
- Forager's decision to give its planner read access was to be measured and never was, so what read access changed is unknown.

**Deviations:** Two premises in the proposal proved false while being written in, and per the abort condition neither part was written.

(1) BUILD_TASKS.md: the proposal said both tasks were built on 2026-08-13. Task 2 was, as check_register.py (2026-08-13-03/-04). Task 1, a structural validator for coder prompts, was never built. check_prompts.py (2026-08-13-09/-10) checks a different property: the binding between record entries and preserved prompts. Proposed status line for the operator: "Status, 2026-10-16: Task 2 was built as check_register.py (RECORD.md 2026-08-13-03/-04), departing from this record where that entry says. Task 1 was never built; check_prompts.py (RECORD.md 2026-08-13-09/-10) checks a different property. The text below is kept as written."

(2) The trial record: the proposal said five data-pipeline principles were never exercised in Forager. None is cited by name in its CLAUDE.md, audits or record, and content-addressed hashing is declined by name. But atomic writes appear as a design concern in Forager's audits, in log rotation and in writing an entry together with its photos, so Atomic State Mutations was practised without being cited. Proposed sentence for the operator: "None of the five data-pipeline principles is cited by name in Forager's CLAUDE.md, audits or record. Content-addressed hashing is declined by name. Atomic writes appear as a design concern in at least two audit documents, so Atomic State Mutations was practised without being cited."

Corrections made in the course of the work, all disclosed in their commits:

- The authorization lesson's count is 9 (5 in Forager's record, 4 operator-reported), not the proposal's 10. The reader session's audit-index line numbers for three of its instances did not match the index, and were not cited.
- Three other reader-supplied claims could not be verified and were left out: number ranges reserved per task in forager-forecast, a record entry about model-named co-author lines, and a fourth instance for rule 16.
- d47e852 wiped README.md to one line. A sed command was run with -n and -i together, and the commit was pushed without its diff being read. It was fixed forward at 8203cf2, not rewritten, and that fix also corrected "four days later" to "five". Twice afterwards an edit to the trial record dropped the heading it was anchored on; both were caught by reading the diff before commit, and neither was committed.
- f2895eb described the voided red inaccurately; 8a548f2 corrects it.

Process differences from the intent:

- The trial record was committed before the principle changes rather than after, so that each principle cites evidence already in the tree.
- Commit authorship: this repository's earlier commits are authored "Claude <noreply@anthropic.com>". This clone had no git identity, so the first commit attempt failed; at that moment the push sent the bare branch at 35e39d1. Forager's local identity was copied into this clone's local config, and this branch's commits are authored slayer8366, each ending with the co-author line.
- A merge commit into Test-1 touching RECORD.md would stop check_record.py's history walk (MergeCommitEncountered), so the pull request asks for a fast-forward.

No existing RECORD.md or REGISTER.md entry was edited. No check script was changed.

---

**Kind:** intent

**ID:** 2026-10-16-03

**Timestamp:** 2026-10-16T21:24:53Z

**Title:** The operator's account of why Forager's hooks were removed, their stated approach since, and the two parts held back from 2026-10-16-01

**Dispatch-file:** preserved/2026-10-16-03.md

**Change:** Four changes on branch curation-2026-10-16, one commit each.

(1) Correct how the branch states the reason Forager's hooks were removed. README.md, trials/forager-2026-10-16.md and PROTOCOL.md rule 12 say they went "because of usage limits", from Forager's 2026-09-27 note. The operator's account, 2026-10-16 (quoted in full in the dispatch file): "The hooks were removed because actions agents are expected to perform were being hindered. The operator had to hold the agent's hand every step of the way, which was the opposite of the kit's intentions." Each place is changed to give the operator's account, and the 2026-09-27 note's words stay quoted as what was recorded then. Rule 12 gains the sharper form of its lesson: a gate that blocks actions the agent is expected to take turns delegation into hand-holding.

(2) Record the operator's stated approach, "So now I let philosophy, precise methodology, and evidence gating drive the agent". It goes in the trial record, and as a new PROTOCOL candidate, rule 21: gate on the evidence the work produces, not on the agent's actions. No principle text changes (the operator's answer, "Protocol + trial").

(3) BUILD_TASKS.md gains the status line proposed in 2026-10-16-02's Deviations.

(4) The trial record gains the sentence proposed there about the five data-pipeline principles.

This entry corrects 2026-10-16-01's characterization by citation; 2026-10-16-01 and -02 are not edited.

**Scope boundary:** RECORD.md and REGISTER.md (append only), prompts/preserved/2026-10-16-03.md, README.md, trials/forager-2026-10-16.md, PROTOCOL.md, BUILD_TASKS.md. Out of scope: PHILOSOPHY.md, ENFORCEMENT.md, GLOSSARY.md and BOOTSTRAP.md (no principle changes, by the operator's answer); any check script; Forager's own 2026-09-27 note, which is in another repository; merging into Test-1, which waits for the operator's go.

**Baseline:** Branch curation-2026-10-16 at e098f94f6f335e4b9ce811e1f8b0ba92b7357b3f, equal to origin/curation-2026-10-16 after git fetch; tree clean; Test-1 still at 35e39d1. check_record.py PASS at 26 entries, none unterminated, a 24-commit walk; check_prompts.py PASS at 8 entries, preserved=7; check_glossary.py PASS at 45/44/45. The usage-limits wording appears in README.md ("removed them five days later because of usage limits"), in the trial record's 2026-09-27 table row and its README pointer, and in rule 12's evidence list.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** After the four commits and this entry's terminal, check_glossary.py is unchanged at 45/44/45, since no principle file is touched. check_record.py passes at 28 entries with none unterminated; its walk counts 25 commits before the terminal's commit (24 plus this intent's). check_prompts.py passes at 9 dispatch-recording entries and preserved=8. A scope diff against e098f94 lists only the paths in this entry's scope. A grep of README.md, the trial record and PROTOCOL.md finds no remaining statement that the hooks were removed because of usage limits; every remaining mention of the limits is attributed to the 2026-09-27 note. Rule 21 is the only new rule, and the protocol then holds 21 numbered rules.

**Finish line:** The four commits and the terminal pushed and confirmed with git ls-remote; the checks above run after the terminal is written and before its commit, through check_register.py; PR #1's description updated to match. Not merged.

**Abort conditions:** A check failing in a way not predicted. Any edit that would need 2026-10-16-01 or -02 changed. Wording for the operator's approach that goes beyond what the operator said: stop and ask rather than extend it.

---

**Kind:** terminal

**ID:** 2026-10-16-04

**Timestamp:** 2026-10-16T21:27:55Z

**Closes:** 2026-10-16-03

**Outcome:** completed

**Observed:** All four changes are on branch curation-2026-10-16, pushed, after the intent (15122af):

- 7b296df corrects the stated reason for Forager's hook removal in README.md, the trial record's 2026-09-27 row and PROTOCOL rule 12. Each now gives the operator's account; the 2026-09-27 note's "weekly limits" stays quoted and attributed to the note; rule 12 gains the sharper form of its lesson.
- e793915 adds PROTOCOL candidate 21 and a trial-record section quoting the operator in full.
- af9ea9a adds BUILD_TASKS.md's status line.
- 0dd2193 adds the trial-record section on the five data-pipeline principles.

This entry corrects 2026-10-16-01's and -02's characterization of the removal by citation; neither is edited. The "usage limits" wording also stands in the preserved proposal (prompts/preserved/2026-10-16-01.md) and in the file contents of earlier commits on this branch: README.md from 8203cf2, and rule 12 from d8bfd1d. Those are history and are not changed; this entry is the correction to read beside them.

Checks, run after this entry was written and before its commit, through check_register.py:

- Wording check: every mention of usage or weekly limits in README.md, the trial record and PROTOCOL.md is either attributed to the 2026-09-27 note (two lines) or names a kind of cost (one line, rule 12's list). PASS, as predicted. Positive control: the same check on a scratch copy holding README.md as of 8203cf2 failed, naming README.md:57.
- Scope against e098f94: 7 paths, all in scope, PASS. The registered expectation was muddled about REGISTER.md, saying it would not appear yet; it appears because the register run itself modifies it in the working tree, and it is in scope either way.
- PROTOCOL.md holds 21 numbered rules, as predicted.
- check_glossary.py, check_record.py and check_prompts.py results are in REGISTER.md beside this commit.

Observed but not asked: Forager's own 2026-09-27 note still gives only the weekly limits. Adding the operator's account there is a change to another repository, and is the operator's to direct.

**Deviations:** One addition beyond the operator's words, labelled as such in rule 21: a paragraph marked "the curator's reading, not the operator's words". It reconciles rule 21 with Operator Authority by saying the operator's explicit go at a decision point is not an action gate in this rule's sense. Without it, rule 21 and the Operator Authority amendment of 2026-10-16-01 read as contradicting each other. It is offered for the operator to strike or keep.

No existing RECORD.md or REGISTER.md entry was edited. No check script or principle file was changed.

---

**Kind:** intent

**ID:** 2026-10-16-05

**Timestamp:** 2026-10-16T22:56:18Z

**Title:** Forager's recording method written into E-GD as RECORDING.md: twelve entry types as Forager used them, backups before merges, the index, the report disclosure sections, and a fourth terminal outcome, partial

**Dispatch-file:** preserved/2026-10-16-05.md

**Change:** A new RECORDING.md holds the method, in one commit per section:

- what every entry carries and the admission rule (PROTOCOL rule 14, promoted);
- the twelve entry types, defined from the fields Forager's record actually uses: intent, terminal, continuation, decision, outcome, observation, finding, device-note, correction, merge, dispatch-note, handoff. These are kept as twelve, synonyms included, by the operator's ruling "Keep all twelve";
- backups before merges;
- the index;
- the report disclosure sections;
- how this repository's own record stands until its checker is updated.

Other edits:

- ENFORCEMENT.md: the record-store infrastructure item, Immutable Append-Only History and Complete Execution Reports point to RECORDING.md, with pointers to this entry.
- The principle Terminal Intent Entries gains a fourth outcome, partial, with a Deferred field, in PHILOSOPHY.md, ENFORCEMENT.md and BOOTSTRAP.md (the operator's ruling "Add partial").
- BOOTSTRAP.md's report rule names the disclosure sections.
- PROTOCOL.md rule 14 is marked promoted.
- README.md gains a row.

**Scope boundary:** RECORD.md and REGISTER.md (append only), prompts/preserved/2026-10-16-05.md, RECORDING.md (new), ENFORCEMENT.md, PHILOSOPHY.md (Terminal Intent Entries only), BOOTSTRAP.md, PROTOCOL.md, README.md, on branch recording-method-2026-10-16 cut from Test-1 at 57af78f.

Out of scope:

- check_record.py and every other check script. Updating them is a separate change, on its own go, by the operator's ruling.
- Writing any of the new entry types into this repository's own RECORD.md, which the current checker would fail.
- Forager's record, including its 63 intents with no terminal.
- Merging into Test-1, which waits for the operator's go.

**Baseline:** Branch recording-method-2026-10-16 created at 57af78fe4fd73576132280d5e98016909a92a308, equal to origin/Test-1 after git fetch; tree clean. check_record.py PASS at 28 entries, none unterminated, a 26-commit walk; check_prompts.py PASS at 9 entries, preserved=8; check_glossary.py PASS at 45/44/45. RECORDING.md does not exist.

Forager's record at 97f26098, counted by script: 1,275 entries; per type, intent 243, terminal 166, continuation 330, decision 224, outcome 40, observation 21, finding 3, device-note 11, correction 13, merge 91, dispatch-note 128, handoff 5. Terminal outcomes as written: completed 150 (8 of them with trailing punctuation), abandoned 6, superseded 5, partial 3, parked 1, both 1. Outcome entries: 35 carry Continues, 4 carry Closes, 1 neither. 1,004 entries say who wrote them; 548 name the next free ID. Claude-kit v0.2's check_record.py defines intent, terminal (outcomes completed, partial, superseded, abandoned; partial requires Deferred), dispatch-note, continuation, merge and revert.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** check_glossary.py stays at 45/44/45, PASS: no headword is added, and no line written into PHILOSOPHY.md or ENFORCEMENT.md starts with bold text and a colon or is a whole line of bold. check_record.py passes at 30 entries after the terminal, none unterminated, with a 27-commit walk before the terminal's commit (26 plus this intent's); it accepts a terminal whose Outcome is partial, because it validates only superseded and abandoned outcomes, so this repository can already write partial. check_prompts.py passes at 10 entries, preserved=9. RECORDING.md defines exactly twelve types, each with its Forager count, and those counts sum to 1,275. A scope diff against 57af78f lists only paths inside this entry's scope.

**Finish line:** Every section committed and pushed; checks run after the terminal is written and before its commit, through check_register.py; a pull request opened into Test-1. Not merged.

**Abort conditions:** A check failing in a way not predicted. A type that cannot be defined from Forager's actual entries without inventing fields (stop and report it rather than fill it in). Any wording that would make this repository's checker fail its own record.

---

**Kind:** terminal

**ID:** 2026-10-16-06

**Timestamp:** 2026-10-16T23:00:11Z

**Closes:** 2026-10-16-05

**Outcome:** completed

**Observed:** RECORDING.md is E-GD's recording method, on branch recording-method-2026-10-16, pushed, in these commits after the intent (8fc3569):

- ec9c167: what every entry carries, what goes in, the twelve entry types and this repository's own record; with the pointers from ENFORCEMENT.md, README.md and PROTOCOL rule 14.
- dcbef0a: backups before merges, with a pointer from Immutable Append-Only History.
- 7a6d89d: the index.
- 9b398a6: the report disclosure sections, also in Complete Execution Reports and BOOTSTRAP.md's non-negotiable 5.
- d749650: correction of a claim in 9b398a6.
- 5c6b56f: the fourth terminal outcome, partial, in PHILOSOPHY.md, ENFORCEMENT.md and BOOTSTRAP.md.

Checks, through check_register.py, each with a positive control:

- RECORDING.md's twelve types and counts equal a count by script over Forager's record at 97f26098, summing to 1,275. Control: one count changed to 6 failed, naming handoff.
- Scope against 57af78f: 9 paths, all in scope, and PHILOSOPHY.md changed on its Terminal Intent Entries line only. Control: a second principle line changed in a scratch worktree failed, naming it.
- check_record.validate_entries accepts a terminal with Outcome partial and a Deferred field. Control: an abandoned terminal with no Working-state was rejected, naming the missing field.
- check_glossary.py, check_record.py and check_prompts.py are run after this entry is written and before its commit; their results are in REGISTER.md beside this commit.

The five disclosure sections, as RECORDING.md now asks of a report:

Confirmed against inferred. The twelve types, their counts and the share of entries carrying each field are counted by script from Forager's record. Each type's purpose is read from its fields and from one recent example of each, and is inferred for the types with few entries (finding, 3; handoff, 5). The provenance labels are read from forager-forecast's decision log; the five report sections from Forager's operating guide.

Could not determine. Whether Forager's later dispatch-note form, a change to a running dispatch, was ever ruled on as a change of meaning, or just drifted into use.

Premises that were wrong. Two, both in the proposal preserved at prompts/preserved/2026-10-16-05.md. (a) "One ('outcome') closes an intent exactly like a terminal does", and the table's "Absorbs Forager's 'outcome' type, which did the same job": of the 40 outcome entries, 35 carry Continues, 4 Closes and 1 neither, so outcome mostly reports a result against open work. The operator's ruling kept it as its own type, and RECORDING.md states the real counts. (b) "Claude-kit v0.2's checker, where four of the types were first defined": intent and terminal are this repository's own; the kit added three (continuation, merge, dispatch-note), and also revert, which Forager never used and RECORDING.md does not adopt.

Decided beyond scope. The kit's revert type was left out: it is not one of Forager's twelve, and Forager never used it. The overlaps between types (outcome with terminal, finding with observation, correction as a field) were stated in RECORDING.md rather than resolved, in keeping with the ruling to keep all twelve.

Observed, not asked. Forager's own RECORD.md header still names check_record.py and check_prompts.py as the place its format is defined, and neither is in its tree. Forager's terminals carry two outcomes no list allows ("parked", "both") and eight written "completed;". RECORDING.md, like PROTOCOL.md, is checked by nothing.

**Deviations:** The proposal's two wrong premises above, corrected in what was written. 9b398a6 claimed that Forager added the fifth report section on 2026-09-12; its index records the gap that day, not a section, and d749650 corrects the claim without amending 9b398a6. No existing RECORD.md or REGISTER.md entry was edited. No check script was changed. This repository's own record still writes only intent and terminal entries, as RECORDING.md says it will until the checker is updated on the operator's go.

---

**Kind:** intent

**ID:** 2026-10-16-07

**Timestamp:** 2026-10-16T23:19:29Z

**Title:** E-GD's record checker accepts the twelve entry types of RECORDING.md with minimal required fields; Forager's record header text prepared for its planner

**Dispatch-file:** preserved/2026-10-16-07.md

**Change:** check_record.py's validate_entries and check_duplicate_terminals are extended to RECORDING.md, with minimal required fields by the operator's answer:

- All twelve types are accepted: intent, terminal, continuation, decision, outcome, observation, finding, device-note, correction, merge, dispatch-note, handoff.
- Every type other than intent and terminal requires Kind, ID, Timestamp and Notes (the who-wrote-it line), plus its link field:
  - continuation: Continues, naming an intent earlier in the file and still open there, and carrying no Closes, Outcome, Superseded-by, Finish line or prediction field (the kit's rule);
  - finding: Continues;
  - correction: Corrects, every ID in it naming an earlier entry;
  - outcome: Continues or Closes;
  - merge: Merge-commit and Backup, the two RECORDING.md makes essential;
  - dispatch-note: Dispatch-file or Dispatch, its two forms.
- A Continues on any other type names an earlier entry.
- Closes is allowed only on terminal and outcome. An outcome with Closes counts as the intent's closing entry, both for the unterminated list and for the check that an intent is closed only once.
- A terminal's Outcome must be completed, partial, superseded or abandoned. Partial requires Deferred, and completed may not carry it.
- Intent and terminal requirements are otherwise unchanged.

The self-test suite (--render-check) gains a check for each rule, written and committed first and observed failing. The file's docstring stops saying validate_entries and check_duplicate_terminals are unmodified from the vendored copy. RECORDING.md's section on this repository's own record states what the checker now requires.

The text of a new header for Forager's RECORD.md, to the operator's answer "Forager's own record header", is written here and handed to the operator for the Forager planner to place (the operator's answer "The planner writes it"). This session writes nothing in Forager.

**Scope boundary:** check_record.py, RECORDING.md, RECORD.md and REGISTER.md (append only), prompts/preserved/2026-10-16-07.md, on branch record-checker-2026-10-16 cut from Test-1 at 5b9ffdd.

Out of scope:

- check_prompts.py, check_glossary.py, check_register.py.
- The ID format: it stays YYYY-MM-DD-NN, although Forager's IDs carry three or four digits after the date.
- Forager's repository in any form.
- Merging into Test-1, which waits for the operator's go.

**Baseline:** Branch record-checker-2026-10-16 at 5b9ffdd2d62d71bb7823a5e344d81b98faa92e97, equal to origin/Test-1 after git fetch; tree clean. check_record.py PASS at 30 entries, none unterminated, a 28-commit walk; its --render-check PASS at 18 of 18; check_prompts.py PASS at 10, preserved=9; check_glossary.py PASS at 45/44/45. Every existing entry in this repository's record is an intent or a terminal, and every terminal's Outcome is completed.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):**

- Tests-first commit: --render-check runs 36 checks. Checks 1 to 18 pass. 17 of the 18 new checks fail, each with an assertion message naming the rule that is missing. The exception is the guard that an unknown kind is still rejected, which passes before and after by design and is reported as a guard, not as evidence.
- After the change: 36 of 36 pass, and check_record.py on this repository's own record still passes at 31 entries and later 32, because nothing in it uses the new types.
- Sabotage runs on copies in a temporary directory, never on this tree's file: each new rule disabled by a one-line edit makes its own check fail, and the run's summary line is present (no syntax error) before any result is read.
- The forward change is confirmed present by sha256 after the runs. check_prompts.py goes to 11 entries and preserved=10.

**Finish line:** Tests-first commit, implementation commit and RECORDING.md commit pushed; the sabotage runs and the checks recorded through check_register.py after the terminal is written and before its commit; a pull request into Test-1; the Forager header text given to the operator. Not merged.

**Abort conditions:** A new check that does not fail first for its stated reason (repair the check before writing the rule). An existing check 1 to 18 failing after the change. The repository's own record failing under the new rules. A sabotage run whose build errors (stop and report rather than read its results).

---

**Kind:** terminal

**ID:** 2026-10-16-08

**Timestamp:** 2026-10-16T23:25:08Z

**Closes:** 2026-10-16-07

**Outcome:** completed

**Observed:** check_record.py now accepts RECORDING.md's twelve entry types with minimal required fields, on branch record-checker-2026-10-16, pushed, in these commits after the intent (f0e383a):

- e4e3382: checks 19 to 36, committed failing. 17 of 36 failed, each an AssertionError naming its missing rule. Check 20, the guard that an unknown kind is still rejected, passed before and after by design.
- 9ae699f: the rules. 36 of 36 pass, and this repository's record still passes.
- 9aa5287: checks 37 and 38, for rules the first eighteen did not cover.
- 41f871c: RECORDING.md's section on this repository's record, now listing what the checker requires.

Revert run, through check_register.py: 20 sabotages, each disabling one rule in a copy of the committed file inside a temporary directory; this tree's file was never edited.

- Every run printed its summary line, so none was a build or run error.
- Every sabotage made its own check fail. Nineteen failed only their named checks. The kinds allow-list sabotage failed 16 checks, since every new type is then rejected.
- The repository file equalled the committed copy at the start and at the end.
- Positive control on the runner itself: a no-op edit was reported as not biting, and an edit that broke the file's syntax was reported as not run, with its results unread.

check_record.py, check_prompts.py and check_glossary.py results are in REGISTER.md beside this commit.

Forager's record header, as handed to the operator for the Forager planner to place (the operator's answer "The planner writes it"). This session wrote nothing in Forager. <ID> is for the planner to fill with the entry that quotes the header being replaced:

    # RECORD.md
    
    Forager's record of dispatched work, decisions and what happened. Each piece
    of work opens with an intent entry, written before anything is built, stating
    what will change, where the change stops, what it is expected to do, and when
    it counts as finished or abandoned. It closes with exactly one closing entry:
    a terminal, or an outcome that carries Closes. Twelve entry types are in use:
    intent, terminal, continuation, decision, outcome, observation, finding,
    device-note, correction, merge, dispatch-note and handoff. Every entry carries
    its Kind, its ID and a Timestamp read from the clock, and ends by saying who
    wrote it and on which branch. A decision quotes the owner verbatim and is
    recorded once, after any clarifying, not once for every re-ask.
    
    This file is append-only. Nothing already committed is edited or removed; a
    correction is a new entry that points at the one it corrects. The one
    exception is this header, rewritten on 2026-10-16 at the owner's word
    ("Update both formats to match current standards"); entry <ID> quotes the
    header it replaced.
    
    What makes an entry well formed is defined in E-GD's RECORDING.md
    (github.com/slayer8366/E-GD-Philosophy, branch Test-1), which was written
    from this record's own practice. The check_record.py and check_prompts.py
    this header used to name were removed from this repository on 2026-09-27,
    with the hooks (docs/audits/2026-09-27-kit-hooks-disabled.md). E-GD's
    check_record.py implements RECORDING.md for E-GD's own record, but it expects
    IDs of the form YYYY-MM-DD-NN, so it is not run here, and entries here are
    checked by reading. The existing records in docs/audits/ stay where they are
    and are not migrated into this store; docs/audits/README.md indexes them.
    
    Design: docs/process/accountability-design.md. Method: RECORDING.md in E-GD.

Confirmed against inferred. Every rule and its check were observed failing and passing, by run. That this repository's record is unaffected was run, not inferred. The header text is written from RECORDING.md and from Forager's current header at origin/records-after-173 72fddfb9, read here.

Could not determine. Whether the Forager planner will want the operator's go in its own window before placing the header. Its standing rule, as the operator's notes record it, is to act only on the operator's word given there.

Premises that were wrong. The intent predicted 36 checks; there are 38, because checks 37 and 38 were added after the rules, when the gaps were seen before the revert run. Their evidence is the revert run, not a red before the change.

Decided beyond scope:

- The three kit types were given the same minimal rule the operator chose for the seven practice types (Kind, ID, Timestamp, Notes, link field). For a merge, the link fields are Merge-commit and Backup, the two RECORDING.md's text makes essential.
- A Continues value is read by the ID it starts with, since Forager's practice sometimes follows the ID with a parenthesis.
- A completed terminal carrying Deferred is an error, as RECORDING.md says it may not carry one.

Observed, not asked:

- check_prompts.py pairs a file claimed by an intent with its terminal, but not with an outcome that closes it. RECORDING.md now states this.
- The checker's ID pattern rejects Forager's IDs.

**Deviations:** Two checks more than predicted (37 and 38), as above. No existing RECORD.md or REGISTER.md entry was edited. check_prompts.py, check_glossary.py and check_register.py were not changed.

---

**Kind:** intent

**ID:** 2026-10-16-09

**Timestamp:** 2026-10-17T00:12:26Z

**Title:** Check from source, not memory: a rule for writing dispatches, in E-GD's dispatch rules, the bootstrap and the dispatch-authoring skill copy

**Dispatch-file:** preserved/2026-10-16-09.md

**Change:** Three edits, as the operator's answer "E-GD + text for Forager" sets out:

- ENFORCEMENT.md's Complete Task Prompts entry gains the rule, worded as the proposal quotes it in the dispatch file, with the operator's words and a pointer to this entry.
- BOOTSTRAP.md's planner line gains its short form.
- skills/dispatch-authoring/SKILL.md gains a section of the same name, logged in skills/README.md's list of edits made after copying.

The text of a matching line for Forager's planner profile is written here and handed to the operator, who passes it to the Forager planner. This session writes nothing in Forager.

**Scope boundary:** ENFORCEMENT.md, BOOTSTRAP.md, skills/dispatch-authoring/SKILL.md, skills/README.md, RECORD.md and REGISTER.md (append only), prompts/preserved/2026-10-16-09.md, on branch check-from-source-2026-10-16 cut from Test-1 at f120944.

Out of scope:

- PHILOSOPHY.md: the principle is already Sourced Claims, as amended at 2026-10-16-01, which says an agent cannot tell its memory of a read from the read itself.
- GLOSSARY.md and every check script.
- The operator's account copy of the skill, which this session cannot reach.
- Forager's repository.
- Merging, which waits for the operator's go.

**Baseline:** Branch check-from-source-2026-10-16 at f12094401c253ba8d7c55d52d95396b6748f312a, equal to origin/Test-1 after git fetch; tree clean. check_record.py PASS at 32 entries, none unterminated, a 30-commit walk, --render-check 38 of 38; check_prompts.py PASS at 11, preserved=10; check_glossary.py PASS at 45/44/45.

Evidence behind the rule, read from this repository's record and history rather than recalled: claims written from memory or relay, found wrong only when checked against their source.

- 2026-10-16-02, Deviations:
  - BUILD_TASKS.md's Task 1 called built;
  - five data-pipeline principles called never exercised in Forager;
  - an authorization count of 10 that was 9;
  - a reader's audit-index line numbers that did not match the index;
  - three reader claims that could not be verified.
- 2026-10-16-06, Premises that were wrong:
  - outcome entries called closing like terminals;
  - the kit's count of entry types;
  - 9b398a6's account of the fifth report section.
- Commit 57af78f's message: a sentence claiming three commit messages carried wording none did, corrected before commit.
- This entry's own first draft also cited 2026-10-16-04 and -08 as instances, which neither records. That was found by reading both entries before this one was committed, and removed: one more instance.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** check_glossary.py stays at 45/44/45, PASS: no headword is added, and the new enforcement line is a bullet, not a line of bold. check_record.py passes at 34 entries after the terminal, none unterminated, with a 31-commit walk before the terminal's commit; --render-check stays at 38 of 38. check_prompts.py passes at 12 entries, preserved=11. A scope diff against f120944 lists only paths inside this entry's scope. skills/dispatch-authoring/SKILL.md differs from the operator's account copy only by the new section; the other ten account-synced skills stay byte-identical to their sources.

**Finish line:** The edits committed and pushed; checks run after the terminal is written and before its commit, through check_register.py; a pull request into Test-1; the Forager line given to the operator. Not merged.

**Abort conditions:** A check failing in a way not predicted. A claim in the rule's evidence that does not match the entry it cites.

---

**Kind:** terminal

**ID:** 2026-10-16-10

**Timestamp:** 2026-10-17T00:14:01Z

**Closes:** 2026-10-16-09

**Outcome:** completed

**Observed:** The rule is in E-GD, on branch check-from-source-2026-10-16, pushed, in 35efb6b after the intent (6c3e67d):

- ENFORCEMENT.md's Complete Task Prompts gains it, worded as in the dispatch file, as the writer's side of Sourced Claims.
- BOOTSTRAP.md's planner line carries the short form.
- skills/dispatch-authoring/SKILL.md gains a section "Check from source, not memory", logged in skills/README.md.

The line for Forager's planner profile, handed to the operator for the Forager planner. It goes in the "Dispatching work" section of docs/process/planner-profile.md, after "Verify first, then build". That section reads the same on Forager's origin/pre-main (last change to the file 40459be6) and origin/main (fbd34689), read here:

    - **Check from source, not memory.** Every fact a dispatch states (a path, a line, an ID, a count, a branch or commit, what a RECORD entry or ruling says, whether something exists) is read from its source while the dispatch is written, and cited with the commit or time read. Recall, summaries, handoffs, earlier reports, a coder's reading and the memory notes are pointers to where to look, not sources; anything that can't be checked first is marked unverified and listed as a premise to re-check. The owner, 2026-10-16: "Memory drifts, so always check from source".

Confirmed against inferred:

- The four record entries the intent cites were read before it was committed.
- The planner-profile section was read from both Forager branches, not recalled.
- That skills/dispatch-authoring differs from the account copy only by the new section is checked by the run below.

Could not determine: none.

Premises that were wrong: the intent's first draft cited 2026-10-16-04 and -08 as instances of memory drift, and neither records one. It was corrected before commit, as the intent states.

Decided beyond scope: none.

Observed, not asked: none.

**Deviations:** None. No existing RECORD.md or REGISTER.md entry was edited; no check script changed.

---

**Kind:** intent

**ID:** 2026-10-16-11

**Timestamp:** 2026-10-17T01:48:28Z

**Title:** A spec for a read-only records lookup tool over Forager's and forager-forecast's records, for the operator's approval; no code

**Dispatch-file:** preserved/2026-10-16-11.md

**Change:** Write specs/2026-10-16-records-lookup.md in the form of the operator's plan-forge spec template (Goal, Scope, Out of scope, Decisions, Requirements with a check each, Constraints, Acceptance, Unverified, Open questions), under 600 words. Add a README.md row for specs/. Nothing is built.

**Scope boundary:** specs/2026-10-16-records-lookup.md (new), README.md, RECORD.md and REGISTER.md (append only), prompts/preserved/2026-10-16-11.md, on branch records-lookup-spec-2026-10-16 cut from Test-1 at 6ceefbf. Out of scope: any code; any change in Forager or forager-forecast; E-GD's own record as a source of the tool (the operator's scope answer names Forager and forager-forecast only).

**Baseline:** Read for the spec, 2026-10-16:

- Forager origin/records-after-173 at efef0e46: RECORD.md 1,287 entries, prompts/preserved/ 385 files, docs/audits/README.md 280 dated rows.
- Forager origin/pre-main at 462bb8ba: RECORD.md 735 entries, prompts/preserved/ 295 files, docs/audits/README.md 356 dated rows. origin/main and origin/dev carry the same counts.
- forager-forecast origin/main at b9127e5: no RECORD.md; docs/planning/DECISIONS.md 124 decision rows; docs/audits/README.md 147 dated rows; docs/dispatch/ 57 files. DECISIONS.md contains 63 references of the form "Forager RECORD -NNNN".
- At 97f26098, 63 intents had no closing entry and 6 decisions carried Supersedes (counted earlier this session).

The proposal's "Hand out the next free ID safely, so two planners can't take the same one" overclaims for a read-only tool. Reading can only report the next free ID as of a fetched commit and detect duplicates; reserving one is a write. The spec states this and leaves reservation as an open question.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** The spec file is under 600 words and every requirement names its check. check_record.py passes at 36 entries after the terminal, none unterminated, with a 33-commit walk before the terminal's commit; --render-check 38 of 38. check_prompts.py passes at 13 entries, preserved=12. check_glossary.py stays at 45/44/45. A scope diff against 6ceefbf lists only paths in scope.

**Finish line:** Spec and README row committed and pushed; checks run through check_register.py; a pull request into Test-1; the spec shown to the operator for approval. Not merged; nothing built.

**Abort conditions:** A figure in the spec that does not match its source when re-read before commit.

---

**Kind:** terminal

**ID:** 2026-10-16-12

**Timestamp:** 2026-10-17T01:49:47Z

**Closes:** 2026-10-16-11

**Outcome:** completed

**Observed:** specs/2026-10-16-records-lookup.md is committed on branch records-lookup-spec-2026-10-16, pushed (3b51dd5, after the intent at ac933a8), with a README.md row for specs/.

- 592 words, under the template's 600.
- Seven requirements, each with its check.
- Three open questions for the operator: where the tool lives, whether next-id reserves IDs, and whether forager-forecast's START_HERE.md session log is a source.

Nothing is built. Approving the spec is the operator's, and building on it needs its own go.

Confirmed against inferred. Every figure in the spec was re-counted at the commit it cites before commit:

- efef0e46: 1,287 entries, 385 prompts, 280 audit rows;
- 462bb8ba: 735 entries, 295 prompts, 356 audit rows;
- 97f26098: 63 intents with no closing entry, and 8 entries carrying Supersedes, 6 of them decisions;
- b9127e5: 63 "Forager RECORD -NNNN" references.

Inferred, not checked: that pre-main's audit index holds every row of the records branch's. The spec lists this as unverified.

Could not determine: what forager-forecast's START_HERE.md session log holds. It was not read, and the spec says so.

Premises that were wrong:

- The draft said "only 6 Forager decisions carry an explicit Supersedes", where the property that matters to the tool is any entry carrying one: 8. It was corrected before commit.
- The reply preserved in the dispatch file promised "Hand out the next free ID safely". A read-only tool can only report the next free ID and warn on duplicates; the spec says so, as the intent anticipated.

Decided beyond scope: the per-source default refs (RECORD.md and prompts from records-after-173, the audit index from pre-main). This follows from the counts above, and the spec states it as a decision the operator can overturn.

Observed, not asked: no Forager branch holds all of its record sources at their newest. records-after-173 has the full record and prompts but 76 fewer audit rows than pre-main, main and dev. pre-main, main and dev hold 552 fewer record entries.

**Deviations:** None. No existing RECORD.md or REGISTER.md entry was edited; no code was written.

---

**Kind:** intent

**ID:** 2026-10-16-13

**Timestamp:** 2026-10-17T01:54:45Z

**Title:** Fold the operator's answers into the records lookup spec, record the reading of forager-forecast's START_HERE.md, and merge the approved spec

**Dispatch-file:** preserved/2026-10-16-13.md

**Change:** specs/2026-10-16-records-lookup.md changes as follows:

- Open questions 1 and 2 become decisions: the tool lives in E-GD and is run against each repository; next-id only reports, with no reservation.
- Open question 3 becomes a pending item. It states the curator's reading of forager-forecast's START_HERE.md and the recommendation, and awaits the operator's decision.
- The spec stays under 600 words.

On the operator's "Approve, merge the spec", Test-1 is then fast-forwarded to this branch. Building waits for a separate go.

**Scope boundary:** specs/2026-10-16-records-lookup.md, RECORD.md and REGISTER.md (append only), prompts/preserved/2026-10-16-13.md, on branch records-lookup-spec-2026-10-16. Out of scope: any code; any change in Forager or forager-forecast.

**Baseline:** Branch records-lookup-spec-2026-10-16 at 44865cf; Test-1 at 6ceefbf.

forager-forecast's docs/planning/START_HERE.md at b9127e5, read for this entry: 101 lines, in five sections:

- "Where things stand": maintained prose. Its first line reads "As of 2026-09-18; date and next-up line corrected 2026-10-09", and the section still says "Planning is complete enough to start".
- "Fixed terms", "Working rules" and "How we work": maintained prose.
- "Session log": a table of Date, What was done and What is next, with 29 dated rows from 2026-09-18 to 2026-10-15.

forager-forecast's docs/audits/README.md tells every session to append a session-log row and never rewrite the table. 29 commits have touched the file.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** The spec stays under 600 words with seven requirements, each with its check. check_record.py passes at 38 entries after the terminal, none unterminated; --render-check 38 of 38; check_prompts.py at 14 entries, preserved=13; check_glossary.py 45/44/45. After the fast-forward, Test-1 equals this branch's head, with no merge commit since 35e39d1.

**Finish line:** The spec amended, the terminal written and checks run through check_register.py, the branch pushed, Test-1 fast-forwarded and confirmed on the remote, PR #5 shown as merged.

**Abort conditions:** Test-1 has moved off 6ceefbf, so a fast-forward is impossible: stop and report. Any check failing.

---

**Kind:** terminal

**ID:** 2026-10-16-14

**Timestamp:** 2026-10-17T01:55:27Z

**Closes:** 2026-10-16-13

**Outcome:** completed

**Observed:** The records lookup spec now carries the operator's answers: it lives in E-GD and is run against each repository, and next-id only reports. It also carries the curator's reading of forager-forecast's START_HERE.md, with the recommendation to take the session log and exclude the prose, pending the operator. 599 words, seven requirements, each with its check. The operator approved the spec ("Approve, merge the spec"); Test-1 is fast-forwarded after this entry's commit, and the result is confirmed in the hand-back rather than here, since this entry is committed before the push.

Confirmed against inferred. START_HERE.md was read at b9127e5: sections, line count, the first line's date, and the session log's rows and range. That the session log is append-only is read from forager-forecast's audit index, which says so, and was not checked against the file's history row by row.

Could not determine: none.

Premises that were wrong: none.

Decided beyond scope: the spec edit was written in the working tree in the same step as the intent, after it, and committed separately so that the intent landed first.

Observed, not asked: "Where things stand" in forager-forecast's START_HERE.md is a stale current-state claim. It says "Planning is complete enough to start", dated 2026-09-18 and corrected 2026-10-09. That is forager-forecast's to update.

**Deviations:** None. No existing RECORD.md or REGISTER.md entry was edited; no code was written.

---

**Kind:** intent

**ID:** 2026-10-16-15

**Timestamp:** 2026-10-17T01:58:43Z

**Title:** The records lookup spec takes forager-forecast's session log as a seventh source, prose excluded

**Dispatch-file:** preserved/2026-10-16-15.md

**Change:** In specs/2026-10-16-records-lookup.md:

- Scope adds the session-log table of forager-forecast's docs/planning/START_HERE.md, without the prose above it.
- R3 searches seven sources, not six.
- The pending item becomes a decision.
- The spec stays under 600 words.

Test-1 is then fast-forwarded, as the third of the three answers the operator's "Approve, merge the spec" said would be folded in before merging.

**Scope boundary:** specs/2026-10-16-records-lookup.md, RECORD.md and REGISTER.md (append only), prompts/preserved/2026-10-16-15.md, on branch records-lookup-spec-log-2026-10-16 cut from Test-1 at 84397ea. Out of scope: any code; Forager and forager-forecast.

**Baseline:** Test-1 at 84397ea3063c3a73519aabbbd0fd84a343a1611a, equal to origin/Test-1 after fetch. The spec is 599 words and carries a pending item for START_HERE.md, read at b9127e5.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** The spec stays under 600 words with seven requirements, each with its check, and no "Pending" section. check_record.py passes at 40 entries after the terminal, none unterminated; --render-check 38 of 38; check_prompts.py at 15 entries, preserved=14; check_glossary.py at 45/44/45. After the fast-forward, Test-1 equals this branch's head, with no merge commit.

**Finish line:** Spec amended, terminal written, checks run through check_register.py, pushed, Test-1 fast-forwarded and confirmed on the remote.

**Abort conditions:** Test-1 has moved off 84397ea. Any check failing.

---

**Kind:** terminal

**ID:** 2026-10-16-16

**Timestamp:** 2026-10-17T01:59:13Z

**Closes:** 2026-10-16-15

**Outcome:** completed

**Observed:** The records lookup spec takes forager-forecast's session log as its seventh source, with the prose above it excluded, by the operator's answer "Log only". The spec has no pending item left; it is 583 words, with seven requirements, each with its check. Test-1 is fast-forwarded after this entry's commit, as the operator's "Approve, merge the spec" covered all three answers.

Confirmed against inferred: the spec's word count, its requirement checks, and the absence of the pending section were read from the file before commit.

Could not determine: none.

Premises that were wrong: none.

Decided beyond scope: none.

Observed, not asked: in this round a base-commit check printed an error and checked nothing, because --short takes one revision. That was found from the error line, and the base (84397ea, origin/Test-1) was confirmed separately before this entry was written.

**Deviations:** None. No existing RECORD.md or REGISTER.md entry was edited; no code was written.

---

**Kind:** intent

**ID:** 2026-10-16-17

**Timestamp:** 2026-10-17T02:09:34Z

**Title:** A monthly record layout in RECORDING.md, the lookup spec reading monthly files, and the Forager split steps and index text for its planner

**Dispatch-file:** preserved/2026-10-16-17.md

**Change:**

- RECORDING.md gains a section "Layout: one file per month", as the proposal in the dispatch file sets out.
- specs/2026-10-16-records-lookup.md reads Forager's RECORD.md or, once split, the monthly files it indexes, and next-id reads every month. The spec stays under 600 words.
- The Forager split steps and a revised RECORD.md index text, updated for monthly files and superseding the header text handed over at 2026-10-16-08, are written into this entry's terminal and handed to the operator for the Forager planner. Nothing is written in Forager.

**Scope boundary:** RECORDING.md, specs/2026-10-16-records-lookup.md, RECORD.md and REGISTER.md (append only), prompts/preserved/2026-10-16-17.md, on branch monthly-layout-2026-10-16 cut from Test-1 at ec31535.

Out of scope:

- check_record.py and check_prompts.py, which still read one RECORD.md; their update is code, on its own go.
- E-GD's own record, which stays one file.
- Any change in Forager or forager-forecast.
- Merging, which waits for the operator's go.

**Baseline:** Test-1 at ec3153519c2a477a82bc82d9fce77af50c7bebdf, equal to origin/Test-1 after fetch. Read from Forager for the proposal:

- origin/records-after-173 at f09ff09c holds 1,288 entries in 19,122 lines. 1,109 IDs start 2026-09-28.
- 1,245 entries carry a Timestamp: 468 in 2026-09, about 7,600 lines; 777 in 2026-10, about 8,500 lines. All 777 October entries carry September IDs.
- 43 entries have no Timestamp, all dispatch-notes, with IDs from 2026-09-22-04 to 2026-09-28-96.
- File order never steps back a month.
- 10 of 709 Continues, Closes, Corrects and Supersedes links cross the month boundary.
- origin/pre-main 462bb8ba's RECORD.md is not a byte-prefix of the records branch's. Since their merge base 84804be3, pre-main changed it only in dc4ef1c1 (2 lines replaced). The records branch's own RECORD.md is not append-only since that base either: 0bda73e8 removed -638, and fe3f3ae3 removed a maker's name from -844.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** check_glossary.py stays at 45/44/45. check_record.py passes at 42 entries after the terminal, none unterminated; --render-check 38 of 38. check_prompts.py passes at 16 entries, preserved=15. The spec stays under 600 words, with seven requirements, each with its check. The terminal's quoted Forager texts are indented four spaces, so none of their lines is read as a field, an entry separator or the entries heading; check_record.py's entry count is the proof. A scope diff against ec31535 lists only paths in scope.

**Finish line:** Edits and terminal committed and pushed; checks run through check_register.py; a pull request into Test-1; the Forager steps and index text given to the operator. Not merged until the operator's go.

**Abort conditions:** A check failing. A figure that does not match its source when re-read before commit.

---

**Kind:** terminal

**ID:** 2026-10-16-18

**Timestamp:** 2026-10-17T02:10:28Z

**Closes:** 2026-10-16-17

**Outcome:** completed

**Observed:** Done on branch monthly-layout-2026-10-16, pushed, after the intent (3735a0f):

- RECORDING.md gains "Layout: one file per month".
- specs/2026-10-16-records-lookup.md reads Forager's RECORD.md or its monthly files, and next-id reads across every month. 598 words.

For the Forager planner, handed to the operator; nothing was written in Forager. The revised RECORD.md index text supersedes the header text handed over at 2026-10-16-08, if that text has not yet been placed:

    # RECORD.md
    
    Forager's record of dispatched work, decisions and what happened, kept in one
    file per month under records/: records/YYYY-MM.md, by the month of each
    entry's Timestamp in UTC. This file is the index. IDs carry on as one running
    sequence across the months, so the next free ID is read from every monthly
    file, not only the current one.
    
    Each piece of work opens with an intent entry, written before anything is
    built, stating what will change, where the change stops, what it is expected
    to do, and when it counts as finished or abandoned. It closes with exactly one
    closing entry: a terminal, or an outcome that carries Closes. Twelve entry
    types are in use: intent, terminal, continuation, decision, outcome,
    observation, finding, device-note, correction, merge, dispatch-note and
    handoff. Every entry carries its Kind, its ID and a Timestamp read from the
    clock, and ends by saying who wrote it and on which branch. A decision quotes
    the owner verbatim and is recorded once, after any clarifying, not once for
    every re-ask.
    
    The monthly files are append-only. Nothing already committed is edited or
    removed; a correction is a new entry that points at the one it corrects. New
    entries go in the file for their Timestamp's month. On <date>, at the owner's
    word, the single RECORD.md was split into the monthly files below and this
    header rewritten; entry <ID> records the split, the commit before it and the
    counts, and quotes the header it replaced. That is the one exception to
    append-only.
    
    What makes an entry well formed is defined in E-GD's RECORDING.md
    (github.com/slayer8366/E-GD-Philosophy, branch Test-1), which was written
    from this record's own practice. The check_record.py and check_prompts.py
    this header used to name were removed from this repository on 2026-09-27,
    with the hooks (docs/audits/2026-09-27-kit-hooks-disabled.md). E-GD's
    check_record.py does not yet read monthly files or this record's IDs, so
    entries here are checked by reading. The existing records in docs/audits/
    stay where they are and are not migrated into this store;
    docs/audits/README.md indexes them.
    
    Design: docs/process/accountability-design.md. Method: RECORDING.md in E-GD.
    
    ## Monthly files
    
    | File | First entry | Last entry |
    |---|---|---|
    | records/2026-09.md | <first ID> | <last ID> |
    | records/2026-10.md | <first ID> | (current) |

The monthly file header, shown here for October:

    # Forager record, 2026-10
    
    Entries whose Timestamp falls in October 2026 (UTC). Part of the record
    indexed by RECORD.md. Append-only.
    
    ## Entries
    
    ---

The split steps:

    1. Fetch. Merge origin/pre-main into records-after-173 (a merge, never a
       rebase; keep every row). pre-main's dc4ef1c1 replaced 2 lines of
       RECORD.md that the records branch does not have; reconcile them before
       anything else, so the split starts from one file.
    2. Note the commit and RECORD.md's entry count before the split.
    3. Cut RECORD.md at the first entry whose Timestamp falls in October 2026.
       Entries before it go to records/2026-09.md, it and the rest to
       records/2026-10.md, each under the monthly header (month name changed
       for September). The 43 undated early dispatch notes all lie before the
       cut, in September.
    4. Replace RECORD.md with the index text, filling <date>, <ID> and the
       first and last IDs.
    5. Verify, and say how in the entry: the two files' entry counts sum to
       the count in step 2; the two files' entries, joined in order, equal the
       entries of RECORD.md at the step-2 commit byte for byte; no ID appears
       twice.
    6. Write the entry recording the split in records/2026-10.md: the owner's
       words, the commit before the split, the counts, the old header quoted
       in full, and that append-only for the single RECORD.md is lifted this
       once, at the owner's word, as no precedent. Take its ID after
       fetching, as the next free across both files.
    7. From then on, each new entry goes in the file for its Timestamp's month.

Confirmed against inferred. These were all read from Forager at f09ff09c, 462bb8ba and 84804be3, by script:

- the month counts, the 43 undated entries, the ID prefixes and the monotonic file order;
- the 10 cross-month links;
- the two branches' divergence: dc4ef1c1 on pre-main; 0bda73e8 and fe3f3ae3 on the records branch.

That merging pre-main into the records branch will conflict exactly on dc4ef1c1's 2 lines is inferred, not run.

Could not determine. Whether the header text handed over at 2026-10-16-08 has already been placed in Forager. This entry's index text supersedes it either way.

Premises that were wrong: none.

Decided beyond scope:

- The monthly header's wording.
- That the split's own entry goes in records/2026-10.md.
- That the 43 undated entries stay in September by position. They lie before the cut, as file order shows.

Observed, not asked: the records branch's RECORD.md has not been append-only since its fork from pre-main (0bda73e8, fe3f3ae3). Both were owner-directed removals, recorded in Forager.

**Deviations:** None. No existing RECORD.md or REGISTER.md entry was edited; no code was written.

---

**Kind:** intent

**ID:** 2026-10-16-19

**Timestamp:** 2026-10-17T04:54:31Z

**Title:** PROTOCOL candidate 22, roles name themselves from their project and scope and keep a profile written from the record; the curator's profile as Clio Ledger

**Dispatch-file:** preserved/2026-10-16-19.md

**Change:**

- PROTOCOL.md gains rule 22, as the proposal in the dispatch file sets out, with its evidence and standing. The curator's addition is labelled as such.
- profiles/curator.md, the profile of E-GD's curator, Clio Ledger (the operator's pick), is written from this repository's record, entries 2026-10-16-01 to -18 and their commits. Every practice in it cites its entry, and it follows the structure of Forager's docs/process/planner-profile.md.
- README.md gains a row for profiles/.

**Scope boundary:** PROTOCOL.md, profiles/curator.md (new), README.md, RECORD.md and REGISTER.md (append only), prompts/preserved/2026-10-16-19.md, on branch role-names-profiles-2026-10-16 cut from Test-1 at f6f21a9.

Out of scope:

- CLAUDE.md, including any line telling a curator session to read the profile at start. That is brought to the operator as a question, not written.
- The auditor framework Forager's planner wrote for E-GD.
- Forager.
- Merging, which waits for the operator's go.

**Baseline:** Test-1 at f6f21a9d39da465f69d4ad12b8cec4223c3ac1e9, equal to origin/Test-1 after fetch.

Read from Forager for the proposal:

- origin/records-after-173 at 28a1dc49 holds entries -1141 and -1142, quoted in the dispatch file.
- prompts/preserved/2026-10-16-05b-auditor-framework-addendum.md, section 5.
- origin/pre-main's docs/process/planner-profile.md, last changed at 5cb91fbf. Its sections run from the name through to talking to the owner, and its line 7 says CLAUDE.md governs.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** check_glossary.py stays at 45/44/45. check_record.py passes at 44 entries after the terminal, none unterminated; --render-check 38 of 38. check_prompts.py passes at 17 entries, preserved=16. The protocol holds 22 numbered rules. Every bullet of practice in profiles/curator.md cites a RECORD.md entry or commit of this repository, and each cited ID exists. A script lists the citations and checks each against the record before commit. A scope diff against f6f21a9 lists only paths in scope.

**Finish line:** Rule, profile and README row committed and pushed; terminal and checks through check_register.py; a pull request into Test-1. Not merged until the operator's go.

**Abort conditions:** A practice in the profile that its cited entry does not show. A check failing.

---

**Kind:** terminal

**ID:** 2026-10-16-20

**Timestamp:** 2026-10-17T04:57:26Z

**Closes:** 2026-10-16-19

**Outcome:** completed

**Observed:** Done on branch role-names-profiles-2026-10-16, pushed, after the intent (752eacb):

- PROTOCOL.md gains rule 22 (83ad0c8), and the protocol now holds 22 numbered rules.
- The rule's quote of Forager's planner-profile name line was corrected from a peer's relay to the source (6da5b1d).
- profiles/curator.md, the profile of the curator Clio Ledger (58 lines, the operator's pick), is written from this repository's record, with a README.md row (e075cb0).

Checks, through check_register.py: every record ID, commit and preserved prompt the profile cites exists, with a positive control below; check_record.py, check_prompts.py and check_glossary.py are run before this commit.

Confirmed against inferred. Each practice's citation was read against its entry before commit. Six did not show what they were cited for, and were corrected:

- 2026-10-16-14 does not record re-running checks on Test-1, so that clause was removed.
- 2026-10-16-02 quotes no withdrawn wording, so the citation is now 4ca06d0 and 5c6b56f.
- The 2026-10-16-07 round had no separate go question, so it was removed from that citation.
- "Reported in the next message" is in the chat, not the record, so it is now "listed in the closing entry".
- Timestamps now cite the Sourced Claims rule (4adf4be), since no entry says how its timestamp was read.
- The practices on talking to the operator now cite Forager's planner profile, where the operator's preferences are recorded.

Could not determine: none.

Premises that were wrong: rule 22 first quoted the planner profile's name line as a peer's message gave it, not as the profile has it. It was corrected in 6da5b1d.

Decided beyond scope: the profile's section headings, adapted from Forager's planner profile to the curator's work.

Observed, not asked: nothing tells a curator session to read profiles/curator.md at its start. E-GD's CLAUDE.md lists what is read at session start, and changing it is the operator's call.

**Deviations:** None. No existing RECORD.md or REGISTER.md entry was edited; no code was written.

---

**Kind:** intent

**ID:** 2026-10-16-21

**Timestamp:** 2026-10-17T04:59:06Z

**Title:** CLAUDE.md tells a curator session to read profiles/curator.md before its first action

**Dispatch-file:** preserved/2026-10-16-21.md

**Change:** One paragraph is added to CLAUDE.md's "Read at session start" section, after the PROTOCOL.md paragraph. It says a session working as E-GD's curator reads profiles/curator.md before its first action, and that a session in any other role named under PROTOCOL rule 22 reads its own profile in profiles/. Nothing else in CLAUDE.md changes.

**Scope boundary:** CLAUDE.md, RECORD.md and REGISTER.md (append only), prompts/preserved/2026-10-16-21.md, on branch curator-profile-at-start-2026-10-16 cut from Test-1 at 1943478. Out of scope: the profile itself, CLAUDE.md's other sections, and merging, which waits for the operator's go.

**Baseline:** Test-1 at 1943478df35c313c32888bc32d64c8f88adf29c4 after the fast-forward of PR #7 on the operator's go. CLAUDE.md's "Read at session start" section names BOOTSTRAP.md, ENFORCEMENT.md, GLOSSARY.md, PHILOSOPHY.md and PROTOCOL.md, and not profiles/.

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** git diff of CLAUDE.md shows one hunk of added lines and none removed. check_record.py passes at 46 entries after the terminal, none unterminated; check_prompts.py passes at 18 entries, preserved=17; check_glossary.py stays at 45/44/45.

**Finish line:** The line committed and pushed, the terminal and checks through check_register.py, a pull request shown to the operator. Not merged until the operator's go.

**Abort conditions:** A check failing.

---

**Kind:** terminal

**ID:** 2026-10-16-22

**Timestamp:** 2026-10-17T04:59:23Z

**Closes:** 2026-10-16-21

**Outcome:** completed

**Observed:** CLAUDE.md's "Read at session start" gains one paragraph, on branch curator-profile-at-start-2026-10-16, pushed. It says:

- a session working as E-GD's curator reads profiles/curator.md before its first action;
- a session in any other role named under PROTOCOL rule 22 reads its own profile in profiles/;
- where a profile and CLAUDE.md disagree, CLAUDE.md wins.

The diff of CLAUDE.md shows two added lines and none removed. The checks are run through check_register.py before this commit.

Confirmed against inferred: the diff was read before commit.

Could not determine: none.

Premises that were wrong: none.

Decided beyond scope: the sentence that CLAUDE.md wins over a profile. It repeats what the profile itself says, so a session reading CLAUDE.md alone also knows it.

Observed, not asked: none.

**Deviations:** None. No existing RECORD.md or REGISTER.md entry was edited.

---

**Kind:** intent

**ID:** 2026-10-16-23

**Timestamp:** 2026-10-17T05:14:41Z

**Title:** PROTOCOL candidate 23: a release passes an evidence gate (checks, an independent audit, the operator's approval), from Forager's production gate and auditor

**Dispatch-file:** preserved/2026-10-16-23.md

**Change:**

- PROTOCOL.md gains rule 23, as the proposal in the dispatch file sets out. It follows the addendum where the addendum changed the original document, cites both documents at their Forager source rather than copying them, and quotes the owner only from Forager record entries.
- trials/forager-2026-10-16.md gains a short section on the gate.

**Scope boundary:** PROTOCOL.md, trials/forager-2026-10-16.md, RECORD.md and REGISTER.md (append only), prompts/preserved/2026-10-16-23.md, on branch release-gate-2026-10-16 cut from Test-1 at 9f9c494. Out of scope: copying the framework documents into E-GD; any change in Forager; merging, which waits for the operator's go.

**Baseline:** Test-1 at 9f9c494c9c9cbac1a397fb54ad70af384b08eb66.

Read from Forager's origin/records-after-173 at 830638c3:

- prompts/preserved/2026-10-16-05-auditor-framework-for-egd.md, last changed f09ff09c, sha256 beginning e4a430061c2f.
- prompts/preserved/2026-10-16-05b-auditor-framework-addendum.md, last changed 7d6cdd45, sha256 beginning 896e06bd7e07.
- Entries -1085, -1086, -1087, -1092, -1094, -1097, -1100, -1131 to -1136 and -1138 all exist.

Quotes the rule will use, each found verbatim in its entry:

- "Advises, you decide" (-1086);
- "to reflect workability" (-1087);
- "Field walks and device checks aren't always necessary" (-1133);
- "the same model shares blind spots" (-1134);
- "the rules we have are simply what we already do. Just codified" (-1138).

**Prediction (outcome — planner):** not authored

**Prediction (mechanism — coder):** The protocol holds 23 numbered rules. check_glossary.py stays at 45/44/45. check_record.py passes at 48 entries after the terminal, none unterminated; --render-check 38 of 38. check_prompts.py passes at 19 entries, preserved=18. A scope diff against 9f9c494 lists only paths in scope.

**Finish line:** Rule 23 and the trial section committed and pushed; the terminal and checks through check_register.py; a pull request into Test-1. Not merged until the operator's go.

**Abort conditions:** A quote not found verbatim in its cited entry. A check failing.

---

**Kind:** terminal

**ID:** 2026-10-16-24

**Timestamp:** 2026-10-17T05:15:55Z

**Closes:** 2026-10-16-23

**Outcome:** completed

**Observed:** Done on branch release-gate-2026-10-16, pushed, after the intent (4cecd8a):

- PROTOCOL.md gains rule 23 (84393cf); the protocol holds 23 numbered rules.
- trials/forager-2026-10-16.md gains a section on Forager's production gate and a row in its lessons table (ad85fd1).

The two framework documents are cited at their Forager source, not copied.

Confirmed against inferred:

- Each of rule 23's five quotes was found verbatim in the Forager record entry it cites, by script, before commit.
- The rest of the rule follows the framework document and its addendum, read at Forager's 830638c3, and follows the addendum where the two differ.
- That rule 23 is rule 11 applied at release time is the curator's reading, and is stated as such in the rule.

Could not determine: none.

Premises that were wrong. The proposal said the first audit "caught two gaps in the planner's documents", in the addendum's word. The record entry it cites, -1132, calls them "two notes on the documents, neither blocking". The rule and the trial section use -1132's words.

Decided beyond scope: the ordering and headings inside rule 23, and leaving out a product name the owner used when quoting -1085.

Observed, not asked: the framework documents sit in Forager's prompts/preserved/, named as dispatches, though they are documents written for E-GD. Where they belong is Forager's to decide.

**Deviations:** None. No existing RECORD.md or REGISTER.md entry was edited; no code was written.

---
