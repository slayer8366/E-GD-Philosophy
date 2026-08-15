# REGISTER.md

E-GD-Philosophy's append-only check-observation register. Records
what `check_register.py` captured when a check ran -- the check's own
name, when it ran, what failure was expected of it beforehand, the
exact command, and its real exit code, stdout, and stderr. It does
not judge whether the observation matched the expectation, does not
block on a mismatch, and does not alter the wrapped check's own exit
status. That judgment is Confirm Failure Before Applying Fixes, and
stays an agent's own act every time, not something this file or its
wrapper perform for it.

This file's exact field list and what each field means live in
`check_register.py`'s own docstring, not here. That split is
deliberate, for the same reason `RECORD.md`'s header gives: this
header is frozen from its first commit, and anything enumerated here
would go stale the moment it changed and could never be corrected in
place. `check_register.py` is ordinary version-controlled code and
can actually stay current.

This file is append-only, verified by `check_record.py`'s own
`check_append_only`/`check_history_append_only`, reused rather than
reimplemented, called against this file's name instead of
`RECORD.md`'s: no existing line is ever removed or modified.

New observations are appended by `check_register.py` at the literal
end of the file -- never inserted at a located marker. There is
nothing here for a future entry's own prose to accidentally collide
with the way `RECORD.md`'s did, because nothing in this file's own
append path searches its text for anything.

Captured stdout and stderr inside an entry are four-space indented,
so a captured line can never be mistaken for this file's own field
syntax. A query anchored to a specific entry's own field line is
reliable against that; a bare substring search for a name is not
made reliable by it, since the name can still appear as ordinary
captured data inside some other entry. See `check_register.py`'s own
header for why, in full.

## Observations

---

**Check:** dummy_deliberate_fail

**Timestamp:** 2026-08-13T11:08:12Z

**Expected failure mode:** exits 1, stdout contains 'deliberate failure', stderr contains 'deliberate stderr line'

**Command:** python3 -c import sys; print('deliberate failure'); print('deliberate stderr line', file=sys.stderr); sys.exit(1)

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    deliberate failure

**Stderr:**

    deliberate stderr line

---

**Check:** dummy_deliberate_fail

**Timestamp:** 2026-08-13T11:08:27Z

**Expected failure mode:** exits 1, stdout contains 'deliberate failure', stderr contains 'deliberate stderr line'

**Command:** python3 -c import sys; print('deliberate failure'); print('deliberate stderr line', file=sys.stderr); sys.exit(1)

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    deliberate failure

**Stderr:**

    deliberate stderr line

---

**Check:** dummy_deliberate_fail_exitcheck

**Timestamp:** 2026-08-13T11:08:42Z

**Expected failure mode:** exit-status-parity check

**Command:** python3 -c import sys; print('deliberate failure'); print('deliberate stderr line', file=sys.stderr); sys.exit(1)

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    deliberate failure

**Stderr:**

    deliberate stderr line

---

**Check:** dummy_pass_exitcheck

**Timestamp:** 2026-08-13T11:08:42Z

**Expected failure mode:** N/A -- positive exit-parity case

**Command:** python3 -c print('ok')

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    ok

**Stderr:**

    (nothing captured)

---

**Check:** dummy_vacuous_demo

**Timestamp:** 2026-08-13T11:08:54Z

**Expected failure mode:** N/A -- vacuous positive case: a check examining zero candidates

**Command:** python3 -c print('nothing to compare, vacuous pass')

**Exit code:** 0

**Vacuous:** yes

**Stdout:**

    nothing to compare, vacuous pass

**Stderr:**

    (nothing captured)

---

**Check:** dummy_nonvacuous_demo

**Timestamp:** 2026-08-13T11:08:54Z

**Expected failure mode:** N/A -- non-vacuous positive case

**Command:** python3 -c print('a real comparison happened')

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    a real comparison happened

**Stderr:**

    (nothing captured)

---

**Check:** dummy_mimic_carrier

**Timestamp:** 2026-08-13T11:10:03Z

**Expected failure mode:** N/A -- constructed to test grep collision, not a real check

**Command:** python3 -c print('**Check:** dummy_deliberate_fail'); print('some other check output here')

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    **Check:** dummy_deliberate_fail
    some other check output here

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_still_passes

**Timestamp:** 2026-08-13T11:11:30Z

**Expected failure mode:** N/A -- positive case: check_glossary.py should still report 43 headwords, 42 enforcement entries, 43 glossary rows, PASS, unchanged by this task

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 43
    enforcement entries:  42
    glossary rows:        43
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** check_record_still_passes

**Timestamp:** 2026-08-13T11:11:43Z

**Expected failure mode:** N/A -- positive case: check_record.py should still validate RECORD.md cleanly with 4 entries, one unterminated (2026-08-13-03), against the current HEAD

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 3
    unterminated intent entries (reported, not a failure): 2026-08-13-03
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 2 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** claude_md_sections_present_sabotage

**Timestamp:** 2026-08-13T15:15:34Z

**Expected failure mode:** FAIL, naming '## Stop conditions' as a missing required section header, after that header line is deleted from CLAUDE.md

**Command:** python3 /tmp/check1.py

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    FAIL: missing section header(s): ['## Stop conditions']

**Stderr:**

    (nothing captured)

---

**Check:** claude_md_sections_present

**Timestamp:** 2026-08-13T15:15:42Z

**Expected failure mode:** PASS, all six dictated section headers present, after the sabotaged header is restored

**Command:** python3 /tmp/check1.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    PASS: all dictated section headers present: ['# CLAUDE.md', '## Read at session start', '## Your role', '## Non-negotiables', '## Verification', '## Stop conditions']

**Stderr:**

    (nothing captured)

---

**Check:** claude_md_named_files_sabotage

**Timestamp:** 2026-08-13T15:15:54Z

**Expected failure mode:** FAIL, naming PROTOCOL.md and OPERATOR_PROFILE.template.md as named-but-absent, after the 'not yet rebuilt' marker text is removed from CLAUDE.md

**Command:** python3 /tmp/check2.py

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    FAIL:
     - PROTOCOL.md: text no longer marks this as not-yet-rebuilt, but file is absent on disk
     - OPERATOR_PROFILE.template.md: text no longer marks this as not-yet-rebuilt, but file is absent on disk

**Stderr:**

    (nothing captured)

---

**Check:** claude_md_named_files

**Timestamp:** 2026-08-13T15:16:02Z

**Expected failure mode:** PASS, every named file present or correctly marked not-yet-rebuilt, after the marker text is restored

**Command:** python3 /tmp/check2.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    PASS: every named file exists, or is correctly marked not-yet-rebuilt:
     - BOOTSTRAP.md
     - ENFORCEMENT.md
     - GLOSSARY.md
     - PHILOSOPHY.md
     - PROTOCOL.md
     - OPERATOR_PROFILE.template.md
     - RECORD.md
     - REGISTER.md
     - DURABILITY.md
     - check_record.py
     - check_register.py
     - check_glossary.py
     - ~/imx/CLAUDE.md (cross-repo reference, with Write permissions section)

**Stderr:**

    (nothing captured)

---

**Check:** check_record_still_passes

**Timestamp:** 2026-08-13T15:16:10Z

**Expected failure mode:** PASS/exit 0, RECORD.md structurally valid and append-only-clean, unaffected by CLAUDE.md's presence since check_record.py never reads CLAUDE.md

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 5
    unterminated intent entries (reported, not a failure): 2026-08-13-05
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 4 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_still_passes

**Timestamp:** 2026-08-13T15:16:17Z

**Expected failure mode:** PASS/exit 0, PHILOSOPHY.md/ENFORCEMENT.md/GLOSSARY.md bidirectional contract intact, unaffected by CLAUDE.md's presence since check_glossary.py never reads CLAUDE.md

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 43
    enforcement entries:  42
    glossary rows:        43
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** scope_diff_sabotage

**Timestamp:** 2026-08-13T15:16:41Z

**Expected failure mode:** FAIL, naming README.md as an unexpected out-of-scope change against baseline 9a8e552, after an extra blank line is appended to README.md

**Command:** python3 /tmp/check4.py 9a8e552

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    FAIL: files outside ['CLAUDE.md', 'RECORD.md', 'REGISTER.md'] changed since 9a8e552: ['README.md', '__pycache__/']

**Stderr:**

    (nothing captured)

---

**Check:** scope_diff

**Timestamp:** 2026-08-13T15:17:38Z

**Expected failure mode:** PASS, only CLAUDE.md, RECORD.md, and REGISTER.md changed since baseline 9a8e552, after README.md's sabotage is reverted

**Command:** python3 /tmp/check4.py 9a8e552

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    FAIL: files outside ['CLAUDE.md', 'RECORD.md', 'REGISTER.md'] changed since 9a8e552: ['__pycache__/']

**Stderr:**

    (nothing captured)

---

**Check:** scope_diff

**Timestamp:** 2026-08-13T15:19:02Z

**Expected failure mode:** PASS, only CLAUDE.md, RECORD.md, and REGISTER.md changed since baseline 9a8e552 (with __pycache__ noise from check_register.py's own import ignored by name, not silently)

**Command:** python3 /tmp/check4.py 9a8e552

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    PASS: only ['CLAUDE.md', 'RECORD.md', 'REGISTER.md'] changed since 9a8e552, nothing else
      (ignored as known tooling noise, not part of this check's scope: ['__pycache__/'])

**Stderr:**

    (nothing captured)

---

**Check:** gitignore_suppresses_pycache_sabotage

**Timestamp:** 2026-08-13T15:34:40Z

**Expected failure mode:** FAIL, __pycache__/ visible in git status --porcelain after triggering the check_record import, with .gitignore temporarily moved aside

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 43
    enforcement entries:  42
    glossary rows:        43
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** gitignore_suppresses_pycache_sabotage

**Timestamp:** 2026-08-13T15:59:49Z

**Expected failure mode:** FAIL, __pycache__/ visible in git status --porcelain, with .gitignore temporarily moved aside

**Command:** python3 /tmp/check_gitignore.py

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    FAIL: __pycache__/ is visible in git status --porcelain:
     M REGISTER.md
    ?? __pycache__/
    

**Stderr:**

    (nothing captured)

---

**Check:** gitignore_suppresses_pycache

**Timestamp:** 2026-08-13T15:59:57Z

**Expected failure mode:** PASS, __pycache__/ does not appear in git status --porcelain even though check_register.py's own import regenerates the directory, with .gitignore restored

**Command:** python3 /tmp/check_gitignore.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    PASS: __pycache__/ does not appear in git status --porcelain

**Stderr:**

    (nothing captured)

---

**Check:** check_record_still_passes_gitignore

**Timestamp:** 2026-08-13T16:00:02Z

**Expected failure mode:** PASS/exit 0, unaffected by .gitignore's presence

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 7
    unterminated intent entries (reported, not a failure): 2026-08-13-07
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 6 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_still_passes_gitignore

**Timestamp:** 2026-08-13T16:00:02Z

**Expected failure mode:** PASS/exit 0, unaffected by .gitignore's presence

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 43
    enforcement entries:  42
    glossary rows:        43
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** protocol_rules_1_8_present

**Timestamp:** 2026-08-14T04:38:24Z

**Expected failure mode:** would fail naming missing rule header(s) or an opening line/Standing section not naming eight rules; clean PROTOCOL.md expected to pass

**Command:** python3 /tmp/check1_protocol_rules.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    PASS: rules 1-8 present; opening line and Standing section both name eight rules

**Stderr:**

    (nothing captured)

---

**Check:** protocol_rule8_caveats_empty

**Timestamp:** 2026-08-14T04:38:28Z

**Expected failure mode:** would fail naming leftover text if the caveats section under rule 8 held anything besides the 'none yet' marker; clean PROTOCOL.md expected to pass

**Command:** python3 /tmp/check2_caveats_empty.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    PASS: rule 8's caveats section present, containing only the 'none yet' marker

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_unchanged

**Timestamp:** 2026-08-14T04:38:41Z

**Expected failure mode:** expected to still PASS with the exact baseline counts observed in this task's own RECORD.md entry (43 philosophy headwords, 42 enforcement entries, 43 glossary rows); PROTOCOL.md touches no philosophy/enforcement/glossary file and the script does not read it, so no change is expected. Pre-existing tooling, not built by this task -- positive case only, no sabotage

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 43
    enforcement entries:  42
    glossary rows:        43
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** check_record_passes

**Timestamp:** 2026-08-14T04:38:43Z

**Expected failure mode:** expected to PASS: 13 entries structurally valid (12 prior plus this task's new intent entry), working-tree and history-walk clean, the same three pending outcome-prediction sentinels (2026-08-13-01, -05, -09) reported as expected output, not failures. Pre-existing tooling -- positive case only

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 13
    unterminated intent entries (reported, not a failure): 2026-08-13-13
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 11 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_passes

**Timestamp:** 2026-08-14T04:38:45Z

**Expected failure mode:** expected to PASS: 2 dispatch-recording entries now (2026-08-13-09 and this task's 2026-08-13-13), 2 files under prompts/preserved/, 0 under prompts/recovered/, no orphans -- this task's Dispatch-file field was written as real field syntax at line-start, not embedded in prose, avoiding the defect caught at 2026-08-13-09/-10. Pre-existing tooling -- positive case only

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 2
    files under prompts/: preserved=2, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry, no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** scope_diff_only_allowed_files

**Timestamp:** 2026-08-14T04:39:17Z

**Expected failure mode:** would fail naming any path outside {PROTOCOL.md, RECORD.md, REGISTER.md, prompts/preserved/*} changed since baseline commit 81de364; clean working tree here expected to pass with exactly PROTOCOL.md (new), prompts/preserved/2026-08-13-13.md (new), RECORD.md and REGISTER.md (modified) showing

**Command:** python3 /tmp/check5_scope_diff.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    PASS: only PROTOCOL.md, RECORD.md, REGISTER.md, and/or files under prompts/preserved/ changed since baseline

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_real_repo_pair_legal

**Timestamp:** 2026-08-14T15:56:56Z

**Expected failure mode:** PASS with dispatch-recording entries found: 4, files under prompts/: preserved=3, recovered=0 -- the 2026-08-13-13/-14 pair now legal, plus the new 2026-08-14-01/-02 pair's single Dispatch-file claim on -02

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 4
    files under prompts/: preserved=3, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_pairing_predicate_sabotage

**Timestamp:** 2026-08-14T15:57:11Z

**Expected failure mode:** Stubbing is_intent_terminal_pair to always return False should reproduce today's original defect exactly: FAIL naming 'preserved/2026-08-13-13.md' claimed by 2026-08-13-13 and 2026-08-13-14. This run captures the POST-REVERT clean state (PASS); the sabotaged FAIL was observed directly in-session beforehand, byte-identical revert confirmed by diff before this run.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 4
    files under prompts/: preserved=3, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_nonpair_duplicate_still_fails

**Timestamp:** 2026-08-14T15:57:43Z

**Expected failure mode:** Against a synthetic sandbox (real RECORD.md/prompts/ untouched) with two INTENT entries (2000-01-01-01, 2000-01-01-02, neither a terminal) both claiming preserved/foo.md, check_binding should still report exactly 1 violation: 'preserved/foo.md' is claimed by more than one entry's Dispatch-file field. The pair predicate must not fire since neither claimant is a terminal. Wrapper script exits 0 to mean 'the expected FAIL occurred'; sandbox is deleted by the script itself before it exits, so nothing survives this run.

**Command:** python3 /tmp/claude-0/-home-user-E-GD-Philosophy/45075312-44d7-5830-82ae-fbde74048fe2/scratchpad/sabotage_nonpair_duplicate.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 2
    files under prompts/: preserved=1, recovered=0
    
    FAIL: 1 binding violation(s)
     - 'preserved/foo.md' is claimed by more than one entry's 'Dispatch-file' field: 2000-01-01-01, 2000-01-01-02

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_orphan_missing_direction

**Timestamp:** 2026-08-14T15:58:04Z

**Expected failure mode:** Synthetic sandbox, entry 2000-01-01-03's Dispatch-file names preserved/ghost.md which is never created on disk: check_binding should report exactly 1 violation naming the entry and the missing path. Wrapper exits 0 to mean the expected FAIL occurred; sandbox deleted before exit.

**Command:** python3 /tmp/claude-0/-home-user-E-GD-Philosophy/45075312-44d7-5830-82ae-fbde74048fe2/scratchpad/sabotage_orphan_missing.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 1
    files under prompts/: preserved=0, recovered=0
    
    FAIL: 1 binding violation(s)
     - entry 2000-01-01-03: 'Dispatch-file' names 'preserved/ghost.md', which does not exist under prompts/

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_orphan_unclaimed_direction

**Timestamp:** 2026-08-14T15:58:04Z

**Expected failure mode:** Synthetic sandbox, prompts/preserved/nobody-claims-me.md exists on disk but no entry's Dispatch-file names it: check_binding should report exactly 1 violation naming the orphaned file. Wrapper exits 0 to mean the expected FAIL occurred; sandbox deleted before exit.

**Command:** python3 /tmp/claude-0/-home-user-E-GD-Philosophy/45075312-44d7-5830-82ae-fbde74048fe2/scratchpad/sabotage_orphan_unclaimed.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 0
    files under prompts/: preserved=1, recovered=0
    
    FAIL: 1 binding violation(s)
     - prompts/preserved/nobody-claims-me.md exists but no RECORD.md entry's 'Dispatch-file' field names it

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_unaffected

**Timestamp:** 2026-08-14T15:58:07Z

**Expected failure mode:** This task touches no philosophy/enforcement/glossary file; expect PASS at the same counts observed at orientation: 43 philosophy headwords, 42 enforcement entries, 43 glossary rows.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 43
    enforcement entries:  42
    glossary rows:        43
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** check_record_passes_with_new_entries

**Timestamp:** 2026-08-14T15:58:11Z

**Expected failure mode:** 16 entries (up from 14), working-tree check clean (current file starts with HEAD's content unchanged -- both new entries are pure appends), 12-commit history walk still clean (no new commit yet), Superseded-by cross-reference vacuous PASS, duplicate-terminal check PASS, five pending outcome-prediction sentinels reported as expected output (adding 2026-08-14-01: not authored to the existing four), overall PASS.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 16
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 13 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** scope_diff_only_allowed_files

**Timestamp:** 2026-08-14T15:58:41Z

**Expected failure mode:** Against baseline 4f9184d1d0d801f16ebf01c8eb391a8973714c66: would fail naming any path outside {check_prompts.py, CLAUDE.md, RECORD.md, REGISTER.md, prompts/preserved/*} changed. Sabotaged by appending a blank line to README.md (confirmed caught, then git checkout -- README.md reverted it byte-identical). Clean run here expected to pass with exactly CLAUDE.md, RECORD.md, REGISTER.md, check_prompts.py modified and prompts/preserved/2026-08-14-01.md new -- nothing else.

**Command:** python3 /tmp/claude-0/-home-user-E-GD-Philosophy/45075312-44d7-5830-82ae-fbde74048fe2/scratchpad/check6_scope_diff.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

     CLAUDE.md        |   2 +
     RECORD.md        |  72 +++++++++++++++++++++
     REGISTER.md      | 189 +++++++++++++++++++++++++++++++++++++++++++++++++++++++
     check_prompts.py |  61 +++++++++++++++++-
     4 files changed, 322 insertions(+), 2 deletions(-)
    
    PASS: only check_prompts.py, CLAUDE.md, RECORD.md, REGISTER.md, and/or files under prompts/preserved/ changed since baseline

**Stderr:**

    (nothing captured)

---

**Check:** check_record_two_findings_task

**Timestamp:** 2026-08-14T18:55:10Z

**Expected failure mode:** 18 entries (up from 16), working-tree check clean, 15-commit history walk clean (14 prior plus this task's own intent-entry commit), Superseded-by cross-reference vacuous PASS, duplicate-terminal check PASS, six pending outcome-prediction sentinels (five prior plus 2026-08-14-03: not authored), overall PASS.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 18
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 15 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_new_entry_has_dispatch_file

**Timestamp:** 2026-08-14T18:55:16Z

**Expected failure mode:** PASS, dispatch-recording entries found: 5 (up from 4 -- this task's own intent entry 2026-08-14-03 now carries a Dispatch-file field, unlike 2026-08-14-01's omission), preserved=4, recovered=0. The field's actual presence will additionally be confirmed by a direct grep of the committed entry text, not by trusting this check alone, per this task's own governing prompt.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 5
    files under prompts/: preserved=4, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_unaffected_two_findings_task

**Timestamp:** 2026-08-14T18:55:20Z

**Expected failure mode:** This task touches no philosophy/enforcement/glossary file; expect PASS at the same counts observed at orientation: 43 philosophy headwords, 42 enforcement entries, 43 glossary rows.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 43
    enforcement entries:  42
    glossary rows:        43
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** scope_diff_record_only_two_findings_task

**Timestamp:** 2026-08-14T18:55:30Z

**Expected failure mode:** Against baseline 0f0c5785f118afe47e167bcf1bdefb83b06d538a: would fail naming any path outside {RECORD.md, REGISTER.md, prompts/preserved/*} changed. This task makes no code changes, so expect a clean PASS with exactly RECORD.md, REGISTER.md modified and prompts/preserved/2026-08-14-03.md new -- no sabotage this run, per this check's own docstring.

**Command:** python3 /tmp/claude-0/-home-user-E-GD-Philosophy/45075312-44d7-5830-82ae-fbde74048fe2/scratchpad/check4_scope_diff_task2.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

     RECORD.md   | 60 ++++++++++++++++++++++++++++++++++++++++++
     REGISTER.md | 87 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
     2 files changed, 147 insertions(+)
    
    PASS: only RECORD.md, REGISTER.md, and/or files under prompts/preserved/ changed since baseline

**Stderr:**

    (nothing captured)

---

**Check:** protocol_rule9_present

**Timestamp:** 2026-08-15T09:05:36Z

**Expected failure mode:** PASS: rule 9's bold header and its own internal 'Standing: n=2.' line both present in PROTOCOL.md.

**Command:** python3 /tmp/claude-0/-home-user-E-GD-Philosophy/45075312-44d7-5830-82ae-fbde74048fe2/scratchpad/check1_rule9_present.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    PASS: rule 9 header and its own Standing: n=2 line both present

**Stderr:**

    (nothing captured)

---

**Check:** protocol_counts_name_nine

**Timestamp:** 2026-08-15T09:05:36Z

**Expected failure mode:** PASS: opening line reads 'Nine rules governing...', and the document-level Standing section's addendum sentence naming rule 9's n=2 provenance is present.

**Command:** python3 /tmp/claude-0/-home-user-E-GD-Philosophy/45075312-44d7-5830-82ae-fbde74048fe2/scratchpad/check2_counts_nine.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    PASS: opening line says 'Nine rules governing', standing statement's addendum sentence present

**Stderr:**

    (nothing captured)

---

**Check:** protocol_numbering_1_through_9

**Timestamp:** 2026-08-15T09:05:57Z

**Expected failure mode:** PASS: [1,2,3,4,5,6,7,8,9], scoped to bold headers at line-start within '## The rules' section only, so rule 9's own prose numerals and cited entry IDs cannot be double-counted.

**Command:** python3 /tmp/claude-0/-home-user-E-GD-Philosophy/45075312-44d7-5830-82ae-fbde74048fe2/scratchpad/check3_numbering.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    PASS: rule numbering runs 1 through 9 with no gap or repeat: [1, 2, 3, 4, 5, 6, 7, 8, 9]

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_unaffected_rule9_task

**Timestamp:** 2026-08-15T09:06:22Z

**Expected failure mode:** This task touches no philosophy/enforcement/glossary file; expect PASS at the same counts observed at orientation: 43 philosophy headwords, 42 enforcement entries, 43 glossary rows.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 43
    enforcement entries:  42
    glossary rows:        43
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** check_record_and_prompts_rule9_task

**Timestamp:** 2026-08-15T09:06:28Z

**Expected failure mode:** check_record.py expected PASS, 20 entries, history walk clean including the checkpoint commit. check_prompts.py expected PASS, dispatch-recording entries found: 5, preserved=5 -- this task's own Dispatch-file field will additionally be confirmed by direct read of the committed 2026-08-15-01 entry text, not by trusting check_prompts.py alone, per Finding 1 from the prior task.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 20
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 17 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_rule9_task

**Timestamp:** 2026-08-15T09:06:28Z

**Expected failure mode:** PASS, dispatch-recording entries found: 5, preserved=5, recovered=0.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 6
    files under prompts/: preserved=5, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** scope_diff_rule9_task

**Timestamp:** 2026-08-15T09:06:54Z

**Expected failure mode:** Against baseline ff405303f081f6d0b7bc7f00e49e8de45126b8ec: would fail naming any path outside {PROTOCOL.md, RECORD.md, REGISTER.md, prompts/preserved/*} changed. Sabotaged by appending a blank line to README.md (confirmed caught, then git checkout -- README.md reverted it byte-identical). Clean run here expected to pass with exactly PROTOCOL.md, RECORD.md, REGISTER.md modified and prompts/preserved/2026-08-15-01.md new -- nothing else.

**Command:** python3 /tmp/claude-0/-home-user-E-GD-Philosophy/45075312-44d7-5830-82ae-fbde74048fe2/scratchpad/check6_scope_diff_rule9_task.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

     PROTOCOL.md                        |  26 ++++++-
     RECORD.md                          |  60 +++++++++++++++
     REGISTER.md                        | 153 +++++++++++++++++++++++++++++++++++++
     prompts/preserved/2026-08-15-01.md | 152 ++++++++++++++++++++++++++++++++++++
     4 files changed, 389 insertions(+), 2 deletions(-)
    
    PASS: only PROTOCOL.md, RECORD.md, REGISTER.md, and/or files under prompts/preserved/ changed since baseline

**Stderr:**

    (nothing captured)

---

**Check:** check_record_four_findings_task

**Timestamp:** 2026-08-15T09:53:31Z

**Expected failure mode:** 22 entries (up from 20), working-tree check clean, 18-commit history walk clean (17 prior plus this task's own intent-entry commit), Superseded-by cross-reference vacuous PASS, duplicate-terminal check PASS, seven pending outcome-prediction sentinels (six prior plus 2026-08-15-03: not authored), overall PASS.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 22
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 19 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_new_entry_dispatch_file_four_findings

**Timestamp:** 2026-08-15T09:53:39Z

**Expected failure mode:** PASS, dispatch-recording entries found: 7 (up from 6), preserved=6, recovered=0. Field presence on 2026-08-15-03 confirmed additionally by direct read, not by trusting this check alone.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 7
    files under prompts/: preserved=6, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_unaffected_four_findings_task

**Timestamp:** 2026-08-15T09:53:43Z

**Expected failure mode:** This task touches no philosophy/enforcement/glossary file; expect PASS at the same counts observed at orientation: 43 philosophy headwords, 42 enforcement entries, 43 glossary rows.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 43
    enforcement entries:  42
    glossary rows:        43
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** scope_diff_record_only_four_findings_task

**Timestamp:** 2026-08-15T09:53:52Z

**Expected failure mode:** Against baseline 02c32a92d2917138184535953e503e37c06aefe1: would fail naming any path outside {RECORD.md, REGISTER.md, prompts/preserved/*} changed. This task makes no code or document changes, so expect a clean PASS with exactly RECORD.md, REGISTER.md modified and prompts/preserved/2026-08-15-03.md new -- no sabotage this run, per this task's own instruction.

**Command:** python3 /tmp/claude-0/-home-user-E-GD-Philosophy/45075312-44d7-5830-82ae-fbde74048fe2/scratchpad/check4_scope_diff_four_findings.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

     RECORD.md   | 60 +++++++++++++++++++++++++++++++++++++++++
     REGISTER.md | 88 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
     2 files changed, 148 insertions(+)
    
    PASS: only RECORD.md, REGISTER.md, and/or files under prompts/preserved/ changed since baseline

**Stderr:**

    (nothing captured)

