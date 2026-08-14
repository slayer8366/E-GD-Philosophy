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
