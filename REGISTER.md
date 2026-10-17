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

---

**Check:** check_record_attribution_correction

**Timestamp:** 2026-08-15T10:00:19Z

**Expected failure mode:** 24 entries (up from 22), working-tree check clean, 21-commit history walk clean (20 prior plus this task's own intent-entry commit), Superseded-by cross-reference vacuous PASS, duplicate-terminal check PASS, eight pending outcome-prediction sentinels (seven prior plus 2026-08-15-05: not authored), overall PASS.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 24
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 21 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_unaffected_attribution_correction

**Timestamp:** 2026-08-15T10:00:24Z

**Expected failure mode:** PASS, unchanged at dispatch-recording entries found: 7, preserved=6, recovered=0 -- this entry carries no Dispatch-file field by design (no governing dispatch document exists for this correction), so it is correctly invisible to this check rather than incorrectly bound.

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

**Check:** check_glossary_unaffected_attribution_correction

**Timestamp:** 2026-08-15T10:00:27Z

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

**Check:** scope_diff_attribution_correction

**Timestamp:** 2026-08-15T10:00:35Z

**Expected failure mode:** Against baseline e8a87dad2934b934e1c0ec91ac43c1397bc97909: would fail naming any path outside {RECORD.md, REGISTER.md} changed. No prompts/preserved/ file expected this time. Clean PASS with exactly RECORD.md, REGISTER.md modified -- nothing else, no new files.

**Command:** python3 /tmp/claude-0/-home-user-E-GD-Philosophy/45075312-44d7-5830-82ae-fbde74048fe2/scratchpad/check4_scope_diff_attribution.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

     RECORD.md   | 56 ++++++++++++++++++++++++++++++++++++++
     REGISTER.md | 89 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
     2 files changed, 145 insertions(+)
    
    PASS: only RECORD.md and/or REGISTER.md changed since baseline

**Stderr:**

    (nothing captured)

---

**Check:** sabotage_glossary_missing_severity_entry

**Timestamp:** 2026-10-16T21:17:06Z

**Expected failure mode:** Scratch copy with the Severity of Checks enforcement entry removed: check_glossary.py exits 1, prints FAIL, and names 'philosophy headword has no enforcement entry: Severity of Checks'; counts 45/43/45.

**Command:** python3 /tmp/egd-sabotage/a/check_glossary.py

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  43
    glossary rows:        45
    
    FAIL
      philosophy headword has no enforcement entry: Severity of Checks

**Stderr:**

    (nothing captured)

---

**Check:** sabotage_glossary_missing_durability_row

**Timestamp:** 2026-10-16T21:17:06Z

**Expected failure mode:** Scratch copy with the Durability Is Location glossary row removed: check_glossary.py exits 1, prints FAIL, and names 'philosophy headword missing from glossary: Durability Is Location'; counts 45/44/44.

**Command:** python3 /tmp/egd-sabotage/b/check_glossary.py

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        44
    
    FAIL
      philosophy headword missing from glossary: Durability Is Location
      enforcement entry missing from glossary: Durability Is Location

**Stderr:**

    (nothing captured)

---

**Check:** skills_copy_hashes

**Timestamp:** 2026-10-16T21:17:25Z

**Expected failure mode:** Would fail if any of the 18 copies differed from its source at the copy commit 1b33f20, or if anything other than revert-check, failing-test-first and evidence-discipline differs from its source now. Expected PASS: 18/18 at 1b33f20; exactly those 3 differ now.

**Command:** python3 -I /tmp/egd-scripts/skills_hash_check.py /home/zynergy-labs/Zynergy/E-GD-Philosophy 1b33f20 /tmp/egd-scripts/pairs.txt

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    pairs: 18
    equal to source at 1b33f20: 18/18
    differ from source now: 3
      skills/evidence-discipline/SKILL.md
      skills/failing-test-first/SKILL.md
      skills/revert-check/SKILL.md
    PASS

**Stderr:**

    (nothing captured)

---

**Check:** scope_diff_curation_2026_10_16

**Timestamp:** 2026-10-16T21:17:26Z

**Expected failure mode:** Against base 35e39d1: would fail naming any changed path outside RECORD.md 2026-10-16-01's scope. Expected PASS; BUILD_TASKS.md absent from the list, since it was held back.

**Command:** python3 -I /tmp/egd-scripts/scope_check.py /home/zynergy-labs/Zynergy/E-GD-Philosophy 35e39d1

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    paths changed since 35e39d1: 32
      BOOTSTRAP.md
      CLAUDE.md
      DURABILITY.md
      ENFORCEMENT.md
      GLOSSARY.md
      OVERVIEW.md
      PHILOSOPHY.md
      PROTOCOL.md
      README.md
      RECORD.md
      REGISTER.md
      prompts/preserved/2026-10-16-01.md
      skills/README.md
      skills/completion-report/SKILL.md
      skills/device-check-authoring/SKILL.md
      skills/dispatch-as-file/SKILL.md
      skills/dispatch-authoring/SKILL.md
      skills/evidence-discipline/SKILL.md
      skills/examples/field-instrument-interface/SKILL.md
      skills/failing-test-first/SKILL.md
      skills/plan-forge/.claude-plugin/plugin.json
      skills/plan-forge/README.md
      skills/plan-forge/skills/breakdown/SKILL.md
      skills/plan-forge/skills/plan-review/SKILL.md
      skills/plan-forge/skills/spec/SKILL.md
      skills/plan-forge/skills/spec/references/spec-template.md
      skills/prior-art-before-interface/SKILL.md
      skills/pulse-before-plan/SKILL.md
      skills/record-and-supersede/SKILL.md
      skills/revert-check/SKILL.md
      skills/stop-and-ask/SKILL.md
      trials/forager-2026-10-16.md
    PASS: all inside scope

**Stderr:**

    (nothing captured)

---

**Check:** control_scope_diff_catches_out_of_scope

**Timestamp:** 2026-10-16T21:17:42Z

**Expected failure mode:** Positive control: scratch worktree at HEAD with one line appended to check_record.py, which is outside scope. Expected exit 1, FAIL naming check_record.py.

**Command:** python3 -I /tmp/egd-scripts/scope_check.py /tmp/egd-sc-control 35e39d1

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    paths changed since 35e39d1: 32
      BOOTSTRAP.md
      CLAUDE.md
      DURABILITY.md
      ENFORCEMENT.md
      GLOSSARY.md
      OVERVIEW.md
      PHILOSOPHY.md
      PROTOCOL.md
      README.md
      RECORD.md
      check_record.py
      prompts/preserved/2026-10-16-01.md
      skills/README.md
      skills/completion-report/SKILL.md
      skills/device-check-authoring/SKILL.md
      skills/dispatch-as-file/SKILL.md
      skills/dispatch-authoring/SKILL.md
      skills/evidence-discipline/SKILL.md
      skills/examples/field-instrument-interface/SKILL.md
      skills/failing-test-first/SKILL.md
      skills/plan-forge/.claude-plugin/plugin.json
      skills/plan-forge/README.md
      skills/plan-forge/skills/breakdown/SKILL.md
      skills/plan-forge/skills/plan-review/SKILL.md
      skills/plan-forge/skills/spec/SKILL.md
      skills/plan-forge/skills/spec/references/spec-template.md
      skills/prior-art-before-interface/SKILL.md
      skills/pulse-before-plan/SKILL.md
      skills/record-and-supersede/SKILL.md
      skills/revert-check/SKILL.md
      skills/stop-and-ask/SKILL.md
      trials/forager-2026-10-16.md
    FAIL: outside scope: check_record.py

**Stderr:**

    (nothing captured)

---

**Check:** control_skills_hash_catches_wrong_source

**Timestamp:** 2026-10-16T21:17:42Z

**Expected failure mode:** Positive control: pairs file with completion-report's copy mapped to stop-and-ask's source. Expected exit 1, FAIL, 17/18 at the copy commit, and completion-report listed as differing now.

**Command:** python3 -I /tmp/egd-scripts/skills_hash_check.py /home/zynergy-labs/Zynergy/E-GD-Philosophy 1b33f20 /tmp/egd-scripts/pairs_control.txt

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    pairs: 18
    equal to source at 1b33f20: 17/18
    differ from source now: 4
      skills/completion-report/SKILL.md
      skills/evidence-discipline/SKILL.md
      skills/failing-test-first/SKILL.md
      skills/revert-check/SKILL.md
    FAIL

**Stderr:**

    (nothing captured)

---

**Check:** check_record_curation_terminal

**Timestamp:** 2026-10-16T21:18:38Z

**Expected failure mode:** Would fail on a malformed or duplicate entry, an edited earlier line, or a Closes naming no intent. Expected PASS: 26 entries, no unterminated intent, history walk 23 commits (the intent commit added to the 22 at baseline), working-tree check clean.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 26
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-01: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 23 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_curation_terminal

**Timestamp:** 2026-10-16T21:18:39Z

**Expected failure mode:** Would fail on an unclaimed or doubly claimed prompt file. Expected PASS: 8 dispatch-recording entries, preserved=7, recovered=0.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 8
    files under prompts/: preserved=7, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_curation_terminal

**Timestamp:** 2026-10-16T21:18:39Z

**Expected failure mode:** Would fail on any unbound headword, entry or row, or a section mismatch. Expected PASS at 45/44/45.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        45
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** reason_wording_hook_removal

**Timestamp:** 2026-10-16T21:27:27Z

**Expected failure mode:** Would fail naming any line in README.md, the trial record or PROTOCOL.md that gives usage or weekly limits as the reason for the hook removal without attributing them to the 2026-09-27 note. Expected PASS: one cost-kind line (rule 12's list), two attributed lines.

**Command:** python3 -I /tmp/egd-scripts/reason_check.py /home/zynergy-labs/Zynergy/E-GD-Philosophy

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    trials/forager-2026-10-16.md:31: attributed
    PROTOCOL.md:149: cost-kind
    PROTOCOL.md:160: attributed
    PASS

**Stderr:**

    (nothing captured)

---

**Check:** control_reason_wording_catches_old_readme

**Timestamp:** 2026-10-16T21:27:27Z

**Expected failure mode:** Positive control: scratch copy with README.md as of 8203cf2 ('removed them five days later because of usage limits'). Expected exit 1, FAIL naming README.md.

**Command:** python3 -I /tmp/egd-scripts/reason_check.py /tmp/egd-rc-control

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    README.md:57: UNATTRIBUTED
    trials/forager-2026-10-16.md:31: attributed
    PROTOCOL.md:149: cost-kind
    PROTOCOL.md:160: attributed
    FAIL: README.md:57

**Stderr:**

    (nothing captured)

---

**Check:** scope_diff_2026_10_16_03

**Timestamp:** 2026-10-16T21:27:27Z

**Expected failure mode:** Against e098f94: would fail naming any changed path outside 2026-10-16-03's scope. Expected PASS with RECORD.md, REGISTER.md not yet (register is appended by this very run, uncommitted), README.md, PROTOCOL.md, BUILD_TASKS.md, the trial record and the new preserved prompt.

**Command:** python3 -I /tmp/egd-scripts/scope_check2.py /home/zynergy-labs/Zynergy/E-GD-Philosophy e098f94

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    paths changed since e098f94: 7
      BUILD_TASKS.md
      PROTOCOL.md
      README.md
      RECORD.md
      REGISTER.md
      prompts/preserved/2026-10-16-03.md
      trials/forager-2026-10-16.md
    PASS: all inside scope

**Stderr:**

    (nothing captured)

---

**Check:** check_record_terminal_2026_10_16_04

**Timestamp:** 2026-10-16T21:27:56Z

**Expected failure mode:** Expected PASS: 28 entries, no unterminated intent, walk 25 commits (24 plus intent 2026-10-16-03's commit), working tree clean against HEAD's prefix.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 28
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-03: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 25 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_terminal_2026_10_16_04

**Timestamp:** 2026-10-16T21:27:56Z

**Expected failure mode:** Expected PASS: 9 dispatch-recording entries, preserved=8.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 9
    files under prompts/: preserved=8, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_terminal_2026_10_16_04

**Timestamp:** 2026-10-16T21:27:56Z

**Expected failure mode:** Expected PASS, unchanged at 45/44/45.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        45
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** partial_outcome_accepted_by_check_record

**Timestamp:** 2026-10-16T22:59:16Z

**Expected failure mode:** Would fail if check_record.validate_entries reported any error for a terminal with Outcome: partial and a Deferred field, or if the control (an abandoned terminal with no Working-state) were not rejected naming Working-state. Expected PASS.

**Command:** python3 -I /tmp/egd-scripts/partial_check.py /home/zynergy-labs/Zynergy/E-GD-Philosophy

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    partial with Deferred: errors [] unterminated []
    control, abandoned without Working-state: errors ["terminal 2026-01-01-02: outcome 'abandoned' requires field 'Working-state'"]
    PASS

**Stderr:**

    (nothing captured)

---

**Check:** recording_types_match_forager

**Timestamp:** 2026-10-16T22:59:33Z

**Expected failure mode:** Would fail if RECORDING.md's twelve types or their counts differ from a count by script over Forager's record at 97f26098, or do not sum to 1,275. Expected PASS.

**Command:** python3 -I /tmp/egd-scripts/types_check.py /home/zynergy-labs/Zynergy/E-GD-Philosophy/RECORDING.md /tmp/egd-curate/RECORD.md

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    defined: 12 sum 1275
    actual: 12 sum 1275
    mismatches: {}
    PASS

**Stderr:**

    (nothing captured)

---

**Check:** scope_diff_2026_10_16_05

**Timestamp:** 2026-10-16T22:59:33Z

**Expected failure mode:** Against 57af78f: would fail naming any path outside 2026-10-16-05's scope, or any PHILOSOPHY.md line changed other than Terminal Intent Entries. Expected PASS, with exactly two PHILOSOPHY.md diff lines (one removed, one added).

**Command:** python3 -I /tmp/egd-scripts/scope_check3.py /home/zynergy-labs/Zynergy/E-GD-Philosophy 57af78f

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    paths changed since 57af78f: 9
      BOOTSTRAP.md
      ENFORCEMENT.md
      PHILOSOPHY.md
      PROTOCOL.md
      README.md
      RECORD.md
      RECORDING.md
      REGISTER.md
      prompts/preserved/2026-10-16-05.md
    PHILOSOPHY.md changed lines: 2, outside Terminal Intent Entries: 0
    PASS

**Stderr:**

    (nothing captured)

---

**Check:** control_recording_types_catches_wrong_count

**Timestamp:** 2026-10-16T22:59:45Z

**Expected failure mode:** Positive control: a copy of RECORDING.md with handoff's count changed from 5 to 6. Expected exit 1, FAIL, mismatch handoff (6, 5), sum 1276.

**Command:** python3 -I /tmp/egd-scripts/types_check.py /tmp/egd-ctl/RECORDING.md /tmp/egd-curate/RECORD.md

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    defined: 12 sum 1276
    actual: 12 sum 1275
    mismatches: {'handoff': (6, 5)}
    FAIL

**Stderr:**

    (nothing captured)

---

**Check:** control_scope3_catches_other_philosophy_line

**Timestamp:** 2026-10-16T22:59:45Z

**Expected failure mode:** Positive control: scratch worktree at HEAD with a second PHILOSOPHY.md line (Checks Decay) changed. Expected exit 1, FAIL, 4 changed lines, 2 outside Terminal Intent Entries.

**Command:** python3 -I /tmp/egd-scripts/scope_check3.py /tmp/egd-ctl-wt 57af78f

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    paths changed since 57af78f: 8
      BOOTSTRAP.md
      ENFORCEMENT.md
      PHILOSOPHY.md
      PROTOCOL.md
      README.md
      RECORD.md
      RECORDING.md
      prompts/preserved/2026-10-16-05.md
    PHILOSOPHY.md changed lines: 4, outside Terminal Intent Entries: 2
    FAIL: [] ['-**Checks Decay:** A check is verified once, at birth, by it', '+**Checks Decay:** A check is verified at most once, at birt']

**Stderr:**

    (nothing captured)

---

**Check:** check_record_terminal_2026_10_16_06

**Timestamp:** 2026-10-16T23:00:12Z

**Expected failure mode:** Expected PASS: 30 entries, none unterminated, walk 27 commits (26 plus intent 2026-10-16-05's commit).

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 30
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-05: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 27 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_terminal_2026_10_16_06

**Timestamp:** 2026-10-16T23:00:12Z

**Expected failure mode:** Expected PASS: 10 dispatch-recording entries, preserved=9.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 10
    files under prompts/: preserved=9, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_terminal_2026_10_16_06

**Timestamp:** 2026-10-16T23:00:12Z

**Expected failure mode:** Expected PASS, unchanged at 45/44/45.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        45
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** render_check_tests_first_2026_10_16_07

**Timestamp:** 2026-10-16T23:20:35Z

**Expected failure mode:** Tests-first run, before any rule is written: exit 1, 17 of 36 checks fail (19 to 36 except 20), each an AssertionError naming the missing rule; checks 1 to 18 and the guard check 20 pass.

**Command:** python3 check_record.py --render-check

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    check_record.py --render-check
    
    [check1_well_formed_record_passes] expected failure mode if broken: N/A -- positive case, validated by the negative checks below catching sabotages of the same fixture
    [check1_well_formed_record_passes] PASS
    
    [check2_missing_field_names_fault] expected failure mode if broken: an entry missing a required field is accepted, or the error does not name both the entry and the missing field
    [check2_missing_field_names_fault] PASS
    
    [check3_missing_restored_prediction_field_caught] expected failure mode if broken: an intent entry missing the restored 'Prediction (outcome — planner)' field is accepted, or the error does not name it
    [check3_missing_restored_prediction_field_caught] PASS
    
    [check4_closes_resolution_catches_dangling_reference] expected failure mode if broken: a terminal entry's Closes field naming a nonexistent intent ID is accepted silently
    [check4_closes_resolution_catches_dangling_reference] PASS
    
    [check5_duplicate_id_caught] expected failure mode if broken: two entries sharing the same ID are accepted, or the error does not name the colliding ID
    [check5_duplicate_id_caught] PASS
    
    [check6_duplicate_terminal_names_both_closers] expected failure mode if broken: one intent closed by two terminal entries is accepted, or the error does not name both closing entries
    [check6_duplicate_terminal_names_both_closers] PASS
    
    [check7_withheld_sentinel_reported_pending] expected failure mode if broken: a 'withheld' outcome-prediction sentinel is either treated as an error or not surfaced in sentinel_reports as pending
    [check7_withheld_sentinel_reported_pending] PASS
    
    [check8_withheld_sentinel_resolved_by_terminal] expected failure mode if broken: a terminal entry supplying the outcome for an intent whose prediction was legitimately 'withheld' is not recognized as a resolution
    [check8_withheld_sentinel_resolved_by_terminal] PASS
    
    [check9_not_authored_plus_supplied_is_fabrication] expected failure mode if broken: an intent whose outcome prediction is permanently 'not authored' is not flagged when a terminal entry later supplies a value anyway
    [check9_not_authored_plus_supplied_is_fabrication] PASS
    
    [check10_sentinel_forbidden_in_terminal_entry] expected failure mode if broken: a terminal entry carrying a sentinel value in any field is accepted, or the error does not name the field and value
    [check10_sentinel_forbidden_in_terminal_entry] PASS
    
    [check11_working_tree_append_only_catches_modified_line] expected failure mode if broken: modifying an existing, already-committed line in RECORD.md is not caught, or the failure does not name the changed line
    [check11_working_tree_append_only_catches_modified_line] PASS
    
    [check12_working_tree_append_only_vacuous_before_first_commit] expected failure mode if broken: a RECORD.md that exists in the working tree but has never been committed is reported as a violation, or the vacuous case is not flagged as vacuous
    [check12_working_tree_append_only_vacuous_before_first_commit] PASS
    
    [check13_history_walk_real_repo] expected failure mode if broken: a genuinely append-only two-commit history is reported as violating, or the wrong commit count is walked
    [check13_history_walk_real_repo] PASS
    
    [check14_history_walk_vacuous_single_commit] expected failure mode if broken: a RECORD.md history with only one committed version performs a comparison anyway, or is not reported vacuous
    [check14_history_walk_vacuous_single_commit] PASS
    
    [check15_history_walk_catches_removed_line] expected failure mode if broken: a commit that removed an existing line from RECORD.md's history is accepted by the walk
    [check15_history_walk_catches_removed_line] PASS
    
    [check16_merge_commit_stops_the_walk] expected failure mode if broken: a merge commit touching RECORD.md is silently walked (wrong parent guessed) instead of raising MergeCommitEncountered
    [check16_merge_commit_stops_the_walk] PASS
    
    [check17_superseded_by_vacuous_when_none_declared] expected failure mode if broken: a record with no terminal entry declaring Outcome: superseded is not reported vacuous, or is reported as a failure
    [check17_superseded_by_vacuous_when_none_declared] PASS
    
    [check18_superseded_by_catches_dangling_reference] expected failure mode if broken: a terminal entry's Superseded-by field naming a nonexistent intent ID is accepted
    [check18_superseded_by_catches_dangling_reference] PASS
    
    [check19_all_twelve_kinds_accepted] expected failure mode if broken: a record using every RECORDING.md entry type with minimal fields is rejected
    [check19_all_twelve_kinds_accepted] FAIL: AssertionError('a record using all twelve types produced errors: ["2026-01-01-02: missing or invalid Kind (got \'continuation\')", "2026-01-01-03: missing or invalid Kind (got \'decision\')", "2026-01-01-04: missing or invalid Kind (got \'outcome\')", "2026-01-01-05: missing or invalid Kind (got \'observation\')", "2026-01-01-06: missing or invalid Kind (got \'finding\')", "2026-01-01-07: missing or invalid Kind (got \'device-note\')", "2026-01-01-08: missing or invalid Kind (got \'correction\')", "2026-01-01-09: missing or invalid Kind (got \'merge\')", "2026-01-01-10: missing or invalid Kind (got \'dispatch-note\')", "2026-01-01-11: missing or invalid Kind (got \'handoff\')"]')
    
    [check20_unknown_kind_still_rejected] expected failure mode if broken: a kind outside the twelve is accepted (guard: passes before and after the change by design, so it is not evidence for the change)
    [check20_unknown_kind_still_rejected] PASS
    
    [check21_new_kind_missing_notes_named] expected failure mode if broken: an entry of a new type without its Notes line is accepted
    [check21_new_kind_missing_notes_named] FAIL: AssertionError('decision without Notes not reported by ID and field: ["2026-01-01-01: missing or invalid Kind (got \'decision\')"]')
    
    [check22_continuation_missing_continues_named] expected failure mode if broken: a continuation with no Continues field is accepted
    [check22_continuation_missing_continues_named] FAIL: AssertionError('continuation without Continues not reported: ["2026-01-01-01: missing or invalid Kind (got \'continuation\')"]')
    
    [check23_continuation_of_closed_intent_caught] expected failure mode if broken: a continuation naming an intent already closed earlier in the file is accepted
    [check23_continuation_of_closed_intent_caught] FAIL: AssertionError('continuation of a closed intent not caught: ["2026-01-01-03: missing or invalid Kind (got \'continuation\')"]')
    
    [check24_continuation_of_non_intent_caught] expected failure mode if broken: a continuation naming an entry that is not an intent is accepted
    [check24_continuation_of_non_intent_caught] FAIL: AssertionError('continuation of a non-intent not caught: ["2026-01-01-01: missing or invalid Kind (got \'decision\')", "2026-01-01-02: missing or invalid Kind (got \'continuation\')"]')
    
    [check25_continuation_forbidden_field_caught] expected failure mode if broken: a continuation carrying a closing field (Outcome) is accepted
    [check25_continuation_forbidden_field_caught] FAIL: AssertionError('continuation carrying Outcome not caught: ["2026-01-01-02: missing or invalid Kind (got \'continuation\')"]')
    
    [check26_outcome_with_closes_closes_intent] expected failure mode if broken: an outcome carrying Closes is rejected, or leaves its intent unterminated
    [check26_outcome_with_closes_closes_intent] FAIL: AssertionError('outcome closing its intent produced errors: ["2026-01-01-02: missing or invalid Kind (got \'outcome\')"]')
    
    [check27_terminal_and_outcome_double_close_caught] expected failure mode if broken: an intent closed by both a terminal and an outcome passes the closed-once check
    [check27_terminal_and_outcome_double_close_caught] FAIL: AssertionError('terminal and outcome both closing one intent not caught: []')
    
    [check28_outcome_needs_continues_or_closes] expected failure mode if broken: an outcome with neither Continues nor Closes is accepted
    [check28_outcome_needs_continues_or_closes] FAIL: AssertionError('outcome with neither link not caught: ["2026-01-01-01: missing or invalid Kind (got \'outcome\')"]')
    
    [check29_correction_dangling_reference_caught] expected failure mode if broken: a correction whose Corrects names no existing entry is accepted
    [check29_correction_dangling_reference_caught] FAIL: AssertionError('correction naming a nonexistent entry not caught: ["2026-01-01-01: missing or invalid Kind (got \'correction\')"]')
    
    [check30_closes_on_other_kind_caught] expected failure mode if broken: a type other than terminal or outcome carrying Closes is accepted
    [check30_closes_on_other_kind_caught] FAIL: AssertionError('Closes on a decision not caught: ["2026-01-01-02: missing or invalid Kind (got \'decision\')"]')
    
    [check31_unknown_terminal_outcome_caught] expected failure mode if broken: a terminal Outcome outside completed, partial, superseded, abandoned is accepted
    [check31_unknown_terminal_outcome_caught] FAIL: AssertionError('terminal outcome outside the four not caught: []')
    
    [check32_partial_requires_deferred] expected failure mode if broken: a partial terminal without a Deferred field is accepted
    [check32_partial_requires_deferred] FAIL: AssertionError('partial without Deferred not caught: []')
    
    [check33_completed_with_deferred_caught] expected failure mode if broken: a completed terminal carrying Deferred is accepted
    [check33_completed_with_deferred_caught] FAIL: AssertionError('completed carrying Deferred not caught: []')
    
    [check34_merge_requires_backup] expected failure mode if broken: a merge entry that names no backup is accepted
    [check34_merge_requires_backup] FAIL: AssertionError('merge without Backup not caught: ["2026-01-01-01: missing or invalid Kind (got \'merge\')"]')
    
    [check35_dispatch_note_requires_dispatch_reference] expected failure mode if broken: a dispatch-note naming neither Dispatch-file nor Dispatch is accepted
    [check35_dispatch_note_requires_dispatch_reference] FAIL: AssertionError('dispatch-note with no dispatch reference not caught: ["2026-01-01-01: missing or invalid Kind (got \'dispatch-note\')"]')
    
    [check36_continues_dangling_on_other_kind_caught] expected failure mode if broken: a Continues on a decision naming no existing entry is accepted
    [check36_continues_dangling_on_other_kind_caught] FAIL: AssertionError('Continues naming a nonexistent entry not caught: ["2026-01-01-01: missing or invalid Kind (got \'decision\')"]')
    
    FAIL: 17 of 36 checks failed: check19_all_twelve_kinds_accepted, check21_new_kind_missing_notes_named, check22_continuation_missing_continues_named, check23_continuation_of_closed_intent_caught, check24_continuation_of_non_intent_caught, check25_continuation_forbidden_field_caught, check26_outcome_with_closes_closes_intent, check27_terminal_and_outcome_double_close_caught, check28_outcome_needs_continues_or_closes, check29_correction_dangling_reference_caught, check30_closes_on_other_kind_caught, check31_unknown_terminal_outcome_caught, check32_partial_requires_deferred, check33_completed_with_deferred_caught, check34_merge_requires_backup, check35_dispatch_note_requires_dispatch_reference, check36_continues_dangling_on_other_kind_caught

**Stderr:**

    (nothing captured)

---

**Check:** revert_runs_record_checker_2026_10_16_07

**Timestamp:** 2026-10-16T23:23:31Z

**Expected failure mode:** 20 sabotages, each disabling one rule in a temporary copy of the committed check_record.py: each makes its named check(s) fail, every run prints its summary line (no run error), and the repository file equals the committed copy at start and end. Expected PASS. Kinds allow-list sabotage is expected to fail many checks besides check19, since every new type is rejected.

**Command:** python3 -I /tmp/egd-scripts/revert_runner.py /home/zynergy-labs/Zynergy/E-GD-Philosophy

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    repo file equals committed copy at start: True
    [kinds_allow_list] BITES: expected ['check19_all_twelve_kinds_accepted']; failed 16 of 38; others failing: ['check21_new_kind_missing_notes_named', 'check22_continuation_missing_continues_named', 'check23_continuation_of_closed_intent_caught', 'check24_continuation_of_non_intent_caught', 'check25_continuation_forbidden_field_caught', 'check26_outcome_with_closes_closes_intent', 'check27_terminal_and_outcome_double_close_caught', 'check28_outcome_needs_continues_or_closes', 'check29_correction_dangling_reference_caught', 'check30_closes_on_other_kind_caught', 'check34_merge_requires_backup', 'check35_dispatch_note_requires_dispatch_reference', 'check36_continues_dangling_on_other_kind_caught', 'check37_every_new_kind_requires_notes', 'check38_link_fields_required']
    [decision_notes] BITES: expected ['check21_new_kind_missing_notes_named', 'check37_every_new_kind_requires_notes']; failed 2 of 38; others failing: []
    [handoff_notes] BITES: expected ['check37_every_new_kind_requires_notes']; failed 1 of 38; others failing: []
    [continuation_continues] BITES: expected ['check22_continuation_missing_continues_named']; failed 1 of 38; others failing: []
    [finding_continues] BITES: expected ['check38_link_fields_required']; failed 1 of 38; others failing: []
    [correction_corrects] BITES: expected ['check38_link_fields_required']; failed 1 of 38; others failing: []
    [merge_commit] BITES: expected ['check38_link_fields_required']; failed 1 of 38; others failing: []
    [merge_backup] BITES: expected ['check34_merge_requires_backup']; failed 1 of 38; others failing: []
    [continuation_of_closed] BITES: expected ['check23_continuation_of_closed_intent_caught']; failed 1 of 38; others failing: []
    [continuation_of_non_intent] BITES: expected ['check24_continuation_of_non_intent_caught']; failed 1 of 38; others failing: []
    [continuation_forbidden] BITES: expected ['check25_continuation_forbidden_field_caught']; failed 1 of 38; others failing: []
    [outcome_closes_intent] BITES: expected ['check26_outcome_with_closes_closes_intent']; failed 1 of 38; others failing: []
    [double_close] BITES: expected ['check27_terminal_and_outcome_double_close_caught']; failed 1 of 38; others failing: []
    [one_of_links] BITES: expected ['check28_outcome_needs_continues_or_closes', 'check35_dispatch_note_requires_dispatch_reference']; failed 2 of 38; others failing: []
    [corrects_backlink] BITES: expected ['check29_correction_dangling_reference_caught']; failed 1 of 38; others failing: []
    [closes_other_kind] BITES: expected ['check30_closes_on_other_kind_caught']; failed 1 of 38; others failing: []
    [outcome_vocabulary] BITES: expected ['check31_unknown_terminal_outcome_caught']; failed 1 of 38; others failing: []
    [partial_deferred] BITES: expected ['check32_partial_requires_deferred']; failed 1 of 38; others failing: []
    [completed_no_deferred] BITES: expected ['check33_completed_with_deferred_caught']; failed 1 of 38; others failing: []
    [continues_backlink] BITES: expected ['check36_continues_dangling_on_other_kind_caught']; failed 1 of 38; others failing: []
    repo file equals committed copy at end: True
    sabotages: 20, not biting or not run: 0
    PASS

**Stderr:**

    (nothing captured)

---

**Check:** control_revert_runner_reports_non_biting_and_broken

**Timestamp:** 2026-10-16T23:23:44Z

**Expected failure mode:** Positive control for the revert runner: a no-op edit must be reported DOES NOT BITE, and an edit that breaks the file's syntax must be reported NOT RUN with its results unread. Expected exit 1, FAIL, 2 of 2 not biting or not run.

**Command:** python3 -I /tmp/egd-scripts/revert_runner_control.py /home/zynergy-labs/Zynergy/E-GD-Philosophy

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    repo file equals committed copy at start: True
    [control_noop] DOES NOT BITE: expected ['check32_partial_requires_deferred']; failed 0 of 38; others failing: []
    [control_syntax_error] NOT RUN: no summary line (run error); results not read. tail: '  File "/tmp/tmphh372870/check_record.py", line 126\n    KINDS = (("intent", "terminal") + tuple(OTHER_REQUIRED)\n            ^\nSyntaxError: \'(\' was never closed\n'
    repo file equals committed copy at end: True
    sabotages: 2, not biting or not run: 2
    FAIL

**Stderr:**

    (nothing captured)

---

**Check:** check_record_terminal_2026_10_16_08

**Timestamp:** 2026-10-16T23:25:09Z

**Expected failure mode:** Expected PASS under the new rules: 32 entries, none unterminated, walk 29 commits (28 plus intent 2026-10-16-07's commit).

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 32
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-07: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 29 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_record_selftest_terminal_2026_10_16_08

**Timestamp:** 2026-10-16T23:25:09Z

**Expected failure mode:** Expected PASS: 0 of 38 checks failed.

**Command:** python3 check_record.py --render-check

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    check_record.py --render-check
    
    [check1_well_formed_record_passes] expected failure mode if broken: N/A -- positive case, validated by the negative checks below catching sabotages of the same fixture
    [check1_well_formed_record_passes] PASS
    
    [check2_missing_field_names_fault] expected failure mode if broken: an entry missing a required field is accepted, or the error does not name both the entry and the missing field
    [check2_missing_field_names_fault] PASS
    
    [check3_missing_restored_prediction_field_caught] expected failure mode if broken: an intent entry missing the restored 'Prediction (outcome — planner)' field is accepted, or the error does not name it
    [check3_missing_restored_prediction_field_caught] PASS
    
    [check4_closes_resolution_catches_dangling_reference] expected failure mode if broken: a terminal entry's Closes field naming a nonexistent intent ID is accepted silently
    [check4_closes_resolution_catches_dangling_reference] PASS
    
    [check5_duplicate_id_caught] expected failure mode if broken: two entries sharing the same ID are accepted, or the error does not name the colliding ID
    [check5_duplicate_id_caught] PASS
    
    [check6_duplicate_terminal_names_both_closers] expected failure mode if broken: one intent closed by two terminal entries is accepted, or the error does not name both closing entries
    [check6_duplicate_terminal_names_both_closers] PASS
    
    [check7_withheld_sentinel_reported_pending] expected failure mode if broken: a 'withheld' outcome-prediction sentinel is either treated as an error or not surfaced in sentinel_reports as pending
    [check7_withheld_sentinel_reported_pending] PASS
    
    [check8_withheld_sentinel_resolved_by_terminal] expected failure mode if broken: a terminal entry supplying the outcome for an intent whose prediction was legitimately 'withheld' is not recognized as a resolution
    [check8_withheld_sentinel_resolved_by_terminal] PASS
    
    [check9_not_authored_plus_supplied_is_fabrication] expected failure mode if broken: an intent whose outcome prediction is permanently 'not authored' is not flagged when a terminal entry later supplies a value anyway
    [check9_not_authored_plus_supplied_is_fabrication] PASS
    
    [check10_sentinel_forbidden_in_terminal_entry] expected failure mode if broken: a terminal entry carrying a sentinel value in any field is accepted, or the error does not name the field and value
    [check10_sentinel_forbidden_in_terminal_entry] PASS
    
    [check11_working_tree_append_only_catches_modified_line] expected failure mode if broken: modifying an existing, already-committed line in RECORD.md is not caught, or the failure does not name the changed line
    [check11_working_tree_append_only_catches_modified_line] PASS
    
    [check12_working_tree_append_only_vacuous_before_first_commit] expected failure mode if broken: a RECORD.md that exists in the working tree but has never been committed is reported as a violation, or the vacuous case is not flagged as vacuous
    [check12_working_tree_append_only_vacuous_before_first_commit] PASS
    
    [check13_history_walk_real_repo] expected failure mode if broken: a genuinely append-only two-commit history is reported as violating, or the wrong commit count is walked
    [check13_history_walk_real_repo] PASS
    
    [check14_history_walk_vacuous_single_commit] expected failure mode if broken: a RECORD.md history with only one committed version performs a comparison anyway, or is not reported vacuous
    [check14_history_walk_vacuous_single_commit] PASS
    
    [check15_history_walk_catches_removed_line] expected failure mode if broken: a commit that removed an existing line from RECORD.md's history is accepted by the walk
    [check15_history_walk_catches_removed_line] PASS
    
    [check16_merge_commit_stops_the_walk] expected failure mode if broken: a merge commit touching RECORD.md is silently walked (wrong parent guessed) instead of raising MergeCommitEncountered
    [check16_merge_commit_stops_the_walk] PASS
    
    [check17_superseded_by_vacuous_when_none_declared] expected failure mode if broken: a record with no terminal entry declaring Outcome: superseded is not reported vacuous, or is reported as a failure
    [check17_superseded_by_vacuous_when_none_declared] PASS
    
    [check18_superseded_by_catches_dangling_reference] expected failure mode if broken: a terminal entry's Superseded-by field naming a nonexistent intent ID is accepted
    [check18_superseded_by_catches_dangling_reference] PASS
    
    [check19_all_twelve_kinds_accepted] expected failure mode if broken: a record using every RECORDING.md entry type with minimal fields is rejected
    [check19_all_twelve_kinds_accepted] PASS
    
    [check20_unknown_kind_still_rejected] expected failure mode if broken: a kind outside the twelve is accepted (guard: passes before and after the change by design, so it is not evidence for the change)
    [check20_unknown_kind_still_rejected] PASS
    
    [check21_new_kind_missing_notes_named] expected failure mode if broken: an entry of a new type without its Notes line is accepted
    [check21_new_kind_missing_notes_named] PASS
    
    [check22_continuation_missing_continues_named] expected failure mode if broken: a continuation with no Continues field is accepted
    [check22_continuation_missing_continues_named] PASS
    
    [check23_continuation_of_closed_intent_caught] expected failure mode if broken: a continuation naming an intent already closed earlier in the file is accepted
    [check23_continuation_of_closed_intent_caught] PASS
    
    [check24_continuation_of_non_intent_caught] expected failure mode if broken: a continuation naming an entry that is not an intent is accepted
    [check24_continuation_of_non_intent_caught] PASS
    
    [check25_continuation_forbidden_field_caught] expected failure mode if broken: a continuation carrying a closing field (Outcome) is accepted
    [check25_continuation_forbidden_field_caught] PASS
    
    [check26_outcome_with_closes_closes_intent] expected failure mode if broken: an outcome carrying Closes is rejected, or leaves its intent unterminated
    [check26_outcome_with_closes_closes_intent] PASS
    
    [check27_terminal_and_outcome_double_close_caught] expected failure mode if broken: an intent closed by both a terminal and an outcome passes the closed-once check
    [check27_terminal_and_outcome_double_close_caught] PASS
    
    [check28_outcome_needs_continues_or_closes] expected failure mode if broken: an outcome with neither Continues nor Closes is accepted
    [check28_outcome_needs_continues_or_closes] PASS
    
    [check29_correction_dangling_reference_caught] expected failure mode if broken: a correction whose Corrects names no existing entry is accepted
    [check29_correction_dangling_reference_caught] PASS
    
    [check30_closes_on_other_kind_caught] expected failure mode if broken: a type other than terminal or outcome carrying Closes is accepted
    [check30_closes_on_other_kind_caught] PASS
    
    [check31_unknown_terminal_outcome_caught] expected failure mode if broken: a terminal Outcome outside completed, partial, superseded, abandoned is accepted
    [check31_unknown_terminal_outcome_caught] PASS
    
    [check32_partial_requires_deferred] expected failure mode if broken: a partial terminal without a Deferred field is accepted
    [check32_partial_requires_deferred] PASS
    
    [check33_completed_with_deferred_caught] expected failure mode if broken: a completed terminal carrying Deferred is accepted
    [check33_completed_with_deferred_caught] PASS
    
    [check34_merge_requires_backup] expected failure mode if broken: a merge entry that names no backup is accepted
    [check34_merge_requires_backup] PASS
    
    [check35_dispatch_note_requires_dispatch_reference] expected failure mode if broken: a dispatch-note naming neither Dispatch-file nor Dispatch is accepted
    [check35_dispatch_note_requires_dispatch_reference] PASS
    
    [check36_continues_dangling_on_other_kind_caught] expected failure mode if broken: a Continues on a decision naming no existing entry is accepted
    [check36_continues_dangling_on_other_kind_caught] PASS
    
    [check37_every_new_kind_requires_notes] expected failure mode if broken: some new entry type is accepted without its who-wrote-it Notes line
    [check37_every_new_kind_requires_notes] PASS
    
    [check38_link_fields_required] expected failure mode if broken: a finding without Continues, a correction without Corrects, or a merge without Merge-commit is accepted
    [check38_link_fields_required] PASS
    
    PASS: 0 of 38 checks failed

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_terminal_2026_10_16_08

**Timestamp:** 2026-10-16T23:25:10Z

**Expected failure mode:** Expected PASS: 11 dispatch-recording entries, preserved=10.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 11
    files under prompts/: preserved=10, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_terminal_2026_10_16_08

**Timestamp:** 2026-10-16T23:25:10Z

**Expected failure mode:** Expected PASS at 45/44/45.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        45
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** skill_copy_diff_2026_10_16_09

**Timestamp:** 2026-10-17T00:14:01Z

**Expected failure mode:** Would fail if any of the seven never-edited skills differs from its account source, or if dispatch-authoring loses any line of the account copy or lacks the new section. Expected PASS: 7 of 7 identical; dispatch-authoring adds lines only, including the heading 'Check from source, not memory'.

**Command:** python3 -I /tmp/egd-scripts/skill_diff_check.py /home/zynergy-labs/.claude/skills/synced/091d6a85-6af9-4953-8e61-48289169daf4_8865f9f7-6932-4670-a66e-dcd758fb2018 /home/zynergy-labs/Zynergy/E-GD-Philosophy

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    untouched skills identical to source: 7 of 7
    dispatch-authoring vs account copy: 8 lines added, 0 removed; first added: '+ '
    PASS

**Stderr:**

    (nothing captured)

---

**Check:** check_record_terminal_2026_10_16_10

**Timestamp:** 2026-10-17T00:14:01Z

**Expected failure mode:** Expected PASS: 34 entries, none unterminated, walk 31 commits.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 34
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-07: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-09: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 31 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_record_selftest_2026_10_16_10

**Timestamp:** 2026-10-17T00:14:02Z

**Expected failure mode:** Expected PASS: 0 of 38 checks failed.

**Command:** python3 check_record.py --render-check

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    check_record.py --render-check
    
    [check1_well_formed_record_passes] expected failure mode if broken: N/A -- positive case, validated by the negative checks below catching sabotages of the same fixture
    [check1_well_formed_record_passes] PASS
    
    [check2_missing_field_names_fault] expected failure mode if broken: an entry missing a required field is accepted, or the error does not name both the entry and the missing field
    [check2_missing_field_names_fault] PASS
    
    [check3_missing_restored_prediction_field_caught] expected failure mode if broken: an intent entry missing the restored 'Prediction (outcome — planner)' field is accepted, or the error does not name it
    [check3_missing_restored_prediction_field_caught] PASS
    
    [check4_closes_resolution_catches_dangling_reference] expected failure mode if broken: a terminal entry's Closes field naming a nonexistent intent ID is accepted silently
    [check4_closes_resolution_catches_dangling_reference] PASS
    
    [check5_duplicate_id_caught] expected failure mode if broken: two entries sharing the same ID are accepted, or the error does not name the colliding ID
    [check5_duplicate_id_caught] PASS
    
    [check6_duplicate_terminal_names_both_closers] expected failure mode if broken: one intent closed by two terminal entries is accepted, or the error does not name both closing entries
    [check6_duplicate_terminal_names_both_closers] PASS
    
    [check7_withheld_sentinel_reported_pending] expected failure mode if broken: a 'withheld' outcome-prediction sentinel is either treated as an error or not surfaced in sentinel_reports as pending
    [check7_withheld_sentinel_reported_pending] PASS
    
    [check8_withheld_sentinel_resolved_by_terminal] expected failure mode if broken: a terminal entry supplying the outcome for an intent whose prediction was legitimately 'withheld' is not recognized as a resolution
    [check8_withheld_sentinel_resolved_by_terminal] PASS
    
    [check9_not_authored_plus_supplied_is_fabrication] expected failure mode if broken: an intent whose outcome prediction is permanently 'not authored' is not flagged when a terminal entry later supplies a value anyway
    [check9_not_authored_plus_supplied_is_fabrication] PASS
    
    [check10_sentinel_forbidden_in_terminal_entry] expected failure mode if broken: a terminal entry carrying a sentinel value in any field is accepted, or the error does not name the field and value
    [check10_sentinel_forbidden_in_terminal_entry] PASS
    
    [check11_working_tree_append_only_catches_modified_line] expected failure mode if broken: modifying an existing, already-committed line in RECORD.md is not caught, or the failure does not name the changed line
    [check11_working_tree_append_only_catches_modified_line] PASS
    
    [check12_working_tree_append_only_vacuous_before_first_commit] expected failure mode if broken: a RECORD.md that exists in the working tree but has never been committed is reported as a violation, or the vacuous case is not flagged as vacuous
    [check12_working_tree_append_only_vacuous_before_first_commit] PASS
    
    [check13_history_walk_real_repo] expected failure mode if broken: a genuinely append-only two-commit history is reported as violating, or the wrong commit count is walked
    [check13_history_walk_real_repo] PASS
    
    [check14_history_walk_vacuous_single_commit] expected failure mode if broken: a RECORD.md history with only one committed version performs a comparison anyway, or is not reported vacuous
    [check14_history_walk_vacuous_single_commit] PASS
    
    [check15_history_walk_catches_removed_line] expected failure mode if broken: a commit that removed an existing line from RECORD.md's history is accepted by the walk
    [check15_history_walk_catches_removed_line] PASS
    
    [check16_merge_commit_stops_the_walk] expected failure mode if broken: a merge commit touching RECORD.md is silently walked (wrong parent guessed) instead of raising MergeCommitEncountered
    [check16_merge_commit_stops_the_walk] PASS
    
    [check17_superseded_by_vacuous_when_none_declared] expected failure mode if broken: a record with no terminal entry declaring Outcome: superseded is not reported vacuous, or is reported as a failure
    [check17_superseded_by_vacuous_when_none_declared] PASS
    
    [check18_superseded_by_catches_dangling_reference] expected failure mode if broken: a terminal entry's Superseded-by field naming a nonexistent intent ID is accepted
    [check18_superseded_by_catches_dangling_reference] PASS
    
    [check19_all_twelve_kinds_accepted] expected failure mode if broken: a record using every RECORDING.md entry type with minimal fields is rejected
    [check19_all_twelve_kinds_accepted] PASS
    
    [check20_unknown_kind_still_rejected] expected failure mode if broken: a kind outside the twelve is accepted (guard: passes before and after the change by design, so it is not evidence for the change)
    [check20_unknown_kind_still_rejected] PASS
    
    [check21_new_kind_missing_notes_named] expected failure mode if broken: an entry of a new type without its Notes line is accepted
    [check21_new_kind_missing_notes_named] PASS
    
    [check22_continuation_missing_continues_named] expected failure mode if broken: a continuation with no Continues field is accepted
    [check22_continuation_missing_continues_named] PASS
    
    [check23_continuation_of_closed_intent_caught] expected failure mode if broken: a continuation naming an intent already closed earlier in the file is accepted
    [check23_continuation_of_closed_intent_caught] PASS
    
    [check24_continuation_of_non_intent_caught] expected failure mode if broken: a continuation naming an entry that is not an intent is accepted
    [check24_continuation_of_non_intent_caught] PASS
    
    [check25_continuation_forbidden_field_caught] expected failure mode if broken: a continuation carrying a closing field (Outcome) is accepted
    [check25_continuation_forbidden_field_caught] PASS
    
    [check26_outcome_with_closes_closes_intent] expected failure mode if broken: an outcome carrying Closes is rejected, or leaves its intent unterminated
    [check26_outcome_with_closes_closes_intent] PASS
    
    [check27_terminal_and_outcome_double_close_caught] expected failure mode if broken: an intent closed by both a terminal and an outcome passes the closed-once check
    [check27_terminal_and_outcome_double_close_caught] PASS
    
    [check28_outcome_needs_continues_or_closes] expected failure mode if broken: an outcome with neither Continues nor Closes is accepted
    [check28_outcome_needs_continues_or_closes] PASS
    
    [check29_correction_dangling_reference_caught] expected failure mode if broken: a correction whose Corrects names no existing entry is accepted
    [check29_correction_dangling_reference_caught] PASS
    
    [check30_closes_on_other_kind_caught] expected failure mode if broken: a type other than terminal or outcome carrying Closes is accepted
    [check30_closes_on_other_kind_caught] PASS
    
    [check31_unknown_terminal_outcome_caught] expected failure mode if broken: a terminal Outcome outside completed, partial, superseded, abandoned is accepted
    [check31_unknown_terminal_outcome_caught] PASS
    
    [check32_partial_requires_deferred] expected failure mode if broken: a partial terminal without a Deferred field is accepted
    [check32_partial_requires_deferred] PASS
    
    [check33_completed_with_deferred_caught] expected failure mode if broken: a completed terminal carrying Deferred is accepted
    [check33_completed_with_deferred_caught] PASS
    
    [check34_merge_requires_backup] expected failure mode if broken: a merge entry that names no backup is accepted
    [check34_merge_requires_backup] PASS
    
    [check35_dispatch_note_requires_dispatch_reference] expected failure mode if broken: a dispatch-note naming neither Dispatch-file nor Dispatch is accepted
    [check35_dispatch_note_requires_dispatch_reference] PASS
    
    [check36_continues_dangling_on_other_kind_caught] expected failure mode if broken: a Continues on a decision naming no existing entry is accepted
    [check36_continues_dangling_on_other_kind_caught] PASS
    
    [check37_every_new_kind_requires_notes] expected failure mode if broken: some new entry type is accepted without its who-wrote-it Notes line
    [check37_every_new_kind_requires_notes] PASS
    
    [check38_link_fields_required] expected failure mode if broken: a finding without Continues, a correction without Corrects, or a merge without Merge-commit is accepted
    [check38_link_fields_required] PASS
    
    PASS: 0 of 38 checks failed

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_terminal_2026_10_16_10

**Timestamp:** 2026-10-17T00:14:02Z

**Expected failure mode:** Expected PASS: 12 entries, preserved=11.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 12
    files under prompts/: preserved=11, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_terminal_2026_10_16_10

**Timestamp:** 2026-10-17T00:14:02Z

**Expected failure mode:** Expected PASS at 45/44/45.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        45
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** check_record_terminal_2026_10_16_12

**Timestamp:** 2026-10-17T01:49:48Z

**Expected failure mode:** Expected PASS: 36 entries, none unterminated, walk 33 commits.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 36
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-07: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-09: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-11: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 33 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_record_selftest_2026_10_16_12

**Timestamp:** 2026-10-17T01:49:48Z

**Expected failure mode:** Expected PASS: 0 of 38.

**Command:** python3 check_record.py --render-check

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    check_record.py --render-check
    
    [check1_well_formed_record_passes] expected failure mode if broken: N/A -- positive case, validated by the negative checks below catching sabotages of the same fixture
    [check1_well_formed_record_passes] PASS
    
    [check2_missing_field_names_fault] expected failure mode if broken: an entry missing a required field is accepted, or the error does not name both the entry and the missing field
    [check2_missing_field_names_fault] PASS
    
    [check3_missing_restored_prediction_field_caught] expected failure mode if broken: an intent entry missing the restored 'Prediction (outcome — planner)' field is accepted, or the error does not name it
    [check3_missing_restored_prediction_field_caught] PASS
    
    [check4_closes_resolution_catches_dangling_reference] expected failure mode if broken: a terminal entry's Closes field naming a nonexistent intent ID is accepted silently
    [check4_closes_resolution_catches_dangling_reference] PASS
    
    [check5_duplicate_id_caught] expected failure mode if broken: two entries sharing the same ID are accepted, or the error does not name the colliding ID
    [check5_duplicate_id_caught] PASS
    
    [check6_duplicate_terminal_names_both_closers] expected failure mode if broken: one intent closed by two terminal entries is accepted, or the error does not name both closing entries
    [check6_duplicate_terminal_names_both_closers] PASS
    
    [check7_withheld_sentinel_reported_pending] expected failure mode if broken: a 'withheld' outcome-prediction sentinel is either treated as an error or not surfaced in sentinel_reports as pending
    [check7_withheld_sentinel_reported_pending] PASS
    
    [check8_withheld_sentinel_resolved_by_terminal] expected failure mode if broken: a terminal entry supplying the outcome for an intent whose prediction was legitimately 'withheld' is not recognized as a resolution
    [check8_withheld_sentinel_resolved_by_terminal] PASS
    
    [check9_not_authored_plus_supplied_is_fabrication] expected failure mode if broken: an intent whose outcome prediction is permanently 'not authored' is not flagged when a terminal entry later supplies a value anyway
    [check9_not_authored_plus_supplied_is_fabrication] PASS
    
    [check10_sentinel_forbidden_in_terminal_entry] expected failure mode if broken: a terminal entry carrying a sentinel value in any field is accepted, or the error does not name the field and value
    [check10_sentinel_forbidden_in_terminal_entry] PASS
    
    [check11_working_tree_append_only_catches_modified_line] expected failure mode if broken: modifying an existing, already-committed line in RECORD.md is not caught, or the failure does not name the changed line
    [check11_working_tree_append_only_catches_modified_line] PASS
    
    [check12_working_tree_append_only_vacuous_before_first_commit] expected failure mode if broken: a RECORD.md that exists in the working tree but has never been committed is reported as a violation, or the vacuous case is not flagged as vacuous
    [check12_working_tree_append_only_vacuous_before_first_commit] PASS
    
    [check13_history_walk_real_repo] expected failure mode if broken: a genuinely append-only two-commit history is reported as violating, or the wrong commit count is walked
    [check13_history_walk_real_repo] PASS
    
    [check14_history_walk_vacuous_single_commit] expected failure mode if broken: a RECORD.md history with only one committed version performs a comparison anyway, or is not reported vacuous
    [check14_history_walk_vacuous_single_commit] PASS
    
    [check15_history_walk_catches_removed_line] expected failure mode if broken: a commit that removed an existing line from RECORD.md's history is accepted by the walk
    [check15_history_walk_catches_removed_line] PASS
    
    [check16_merge_commit_stops_the_walk] expected failure mode if broken: a merge commit touching RECORD.md is silently walked (wrong parent guessed) instead of raising MergeCommitEncountered
    [check16_merge_commit_stops_the_walk] PASS
    
    [check17_superseded_by_vacuous_when_none_declared] expected failure mode if broken: a record with no terminal entry declaring Outcome: superseded is not reported vacuous, or is reported as a failure
    [check17_superseded_by_vacuous_when_none_declared] PASS
    
    [check18_superseded_by_catches_dangling_reference] expected failure mode if broken: a terminal entry's Superseded-by field naming a nonexistent intent ID is accepted
    [check18_superseded_by_catches_dangling_reference] PASS
    
    [check19_all_twelve_kinds_accepted] expected failure mode if broken: a record using every RECORDING.md entry type with minimal fields is rejected
    [check19_all_twelve_kinds_accepted] PASS
    
    [check20_unknown_kind_still_rejected] expected failure mode if broken: a kind outside the twelve is accepted (guard: passes before and after the change by design, so it is not evidence for the change)
    [check20_unknown_kind_still_rejected] PASS
    
    [check21_new_kind_missing_notes_named] expected failure mode if broken: an entry of a new type without its Notes line is accepted
    [check21_new_kind_missing_notes_named] PASS
    
    [check22_continuation_missing_continues_named] expected failure mode if broken: a continuation with no Continues field is accepted
    [check22_continuation_missing_continues_named] PASS
    
    [check23_continuation_of_closed_intent_caught] expected failure mode if broken: a continuation naming an intent already closed earlier in the file is accepted
    [check23_continuation_of_closed_intent_caught] PASS
    
    [check24_continuation_of_non_intent_caught] expected failure mode if broken: a continuation naming an entry that is not an intent is accepted
    [check24_continuation_of_non_intent_caught] PASS
    
    [check25_continuation_forbidden_field_caught] expected failure mode if broken: a continuation carrying a closing field (Outcome) is accepted
    [check25_continuation_forbidden_field_caught] PASS
    
    [check26_outcome_with_closes_closes_intent] expected failure mode if broken: an outcome carrying Closes is rejected, or leaves its intent unterminated
    [check26_outcome_with_closes_closes_intent] PASS
    
    [check27_terminal_and_outcome_double_close_caught] expected failure mode if broken: an intent closed by both a terminal and an outcome passes the closed-once check
    [check27_terminal_and_outcome_double_close_caught] PASS
    
    [check28_outcome_needs_continues_or_closes] expected failure mode if broken: an outcome with neither Continues nor Closes is accepted
    [check28_outcome_needs_continues_or_closes] PASS
    
    [check29_correction_dangling_reference_caught] expected failure mode if broken: a correction whose Corrects names no existing entry is accepted
    [check29_correction_dangling_reference_caught] PASS
    
    [check30_closes_on_other_kind_caught] expected failure mode if broken: a type other than terminal or outcome carrying Closes is accepted
    [check30_closes_on_other_kind_caught] PASS
    
    [check31_unknown_terminal_outcome_caught] expected failure mode if broken: a terminal Outcome outside completed, partial, superseded, abandoned is accepted
    [check31_unknown_terminal_outcome_caught] PASS
    
    [check32_partial_requires_deferred] expected failure mode if broken: a partial terminal without a Deferred field is accepted
    [check32_partial_requires_deferred] PASS
    
    [check33_completed_with_deferred_caught] expected failure mode if broken: a completed terminal carrying Deferred is accepted
    [check33_completed_with_deferred_caught] PASS
    
    [check34_merge_requires_backup] expected failure mode if broken: a merge entry that names no backup is accepted
    [check34_merge_requires_backup] PASS
    
    [check35_dispatch_note_requires_dispatch_reference] expected failure mode if broken: a dispatch-note naming neither Dispatch-file nor Dispatch is accepted
    [check35_dispatch_note_requires_dispatch_reference] PASS
    
    [check36_continues_dangling_on_other_kind_caught] expected failure mode if broken: a Continues on a decision naming no existing entry is accepted
    [check36_continues_dangling_on_other_kind_caught] PASS
    
    [check37_every_new_kind_requires_notes] expected failure mode if broken: some new entry type is accepted without its who-wrote-it Notes line
    [check37_every_new_kind_requires_notes] PASS
    
    [check38_link_fields_required] expected failure mode if broken: a finding without Continues, a correction without Corrects, or a merge without Merge-commit is accepted
    [check38_link_fields_required] PASS
    
    PASS: 0 of 38 checks failed

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_terminal_2026_10_16_12

**Timestamp:** 2026-10-17T01:49:49Z

**Expected failure mode:** Expected PASS: 13 entries, preserved=12.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 13
    files under prompts/: preserved=12, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_terminal_2026_10_16_12

**Timestamp:** 2026-10-17T01:49:49Z

**Expected failure mode:** Expected PASS at 45/44/45.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        45
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** check_record_terminal_2026_10_16_14

**Timestamp:** 2026-10-17T01:55:28Z

**Expected failure mode:** Expected PASS: 38 entries, none unterminated.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 38
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-07: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-09: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-11: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-13: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 35 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_record_selftest_2026_10_16_14

**Timestamp:** 2026-10-17T01:55:28Z

**Expected failure mode:** Expected PASS: 0 of 38.

**Command:** python3 check_record.py --render-check

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    check_record.py --render-check
    
    [check1_well_formed_record_passes] expected failure mode if broken: N/A -- positive case, validated by the negative checks below catching sabotages of the same fixture
    [check1_well_formed_record_passes] PASS
    
    [check2_missing_field_names_fault] expected failure mode if broken: an entry missing a required field is accepted, or the error does not name both the entry and the missing field
    [check2_missing_field_names_fault] PASS
    
    [check3_missing_restored_prediction_field_caught] expected failure mode if broken: an intent entry missing the restored 'Prediction (outcome — planner)' field is accepted, or the error does not name it
    [check3_missing_restored_prediction_field_caught] PASS
    
    [check4_closes_resolution_catches_dangling_reference] expected failure mode if broken: a terminal entry's Closes field naming a nonexistent intent ID is accepted silently
    [check4_closes_resolution_catches_dangling_reference] PASS
    
    [check5_duplicate_id_caught] expected failure mode if broken: two entries sharing the same ID are accepted, or the error does not name the colliding ID
    [check5_duplicate_id_caught] PASS
    
    [check6_duplicate_terminal_names_both_closers] expected failure mode if broken: one intent closed by two terminal entries is accepted, or the error does not name both closing entries
    [check6_duplicate_terminal_names_both_closers] PASS
    
    [check7_withheld_sentinel_reported_pending] expected failure mode if broken: a 'withheld' outcome-prediction sentinel is either treated as an error or not surfaced in sentinel_reports as pending
    [check7_withheld_sentinel_reported_pending] PASS
    
    [check8_withheld_sentinel_resolved_by_terminal] expected failure mode if broken: a terminal entry supplying the outcome for an intent whose prediction was legitimately 'withheld' is not recognized as a resolution
    [check8_withheld_sentinel_resolved_by_terminal] PASS
    
    [check9_not_authored_plus_supplied_is_fabrication] expected failure mode if broken: an intent whose outcome prediction is permanently 'not authored' is not flagged when a terminal entry later supplies a value anyway
    [check9_not_authored_plus_supplied_is_fabrication] PASS
    
    [check10_sentinel_forbidden_in_terminal_entry] expected failure mode if broken: a terminal entry carrying a sentinel value in any field is accepted, or the error does not name the field and value
    [check10_sentinel_forbidden_in_terminal_entry] PASS
    
    [check11_working_tree_append_only_catches_modified_line] expected failure mode if broken: modifying an existing, already-committed line in RECORD.md is not caught, or the failure does not name the changed line
    [check11_working_tree_append_only_catches_modified_line] PASS
    
    [check12_working_tree_append_only_vacuous_before_first_commit] expected failure mode if broken: a RECORD.md that exists in the working tree but has never been committed is reported as a violation, or the vacuous case is not flagged as vacuous
    [check12_working_tree_append_only_vacuous_before_first_commit] PASS
    
    [check13_history_walk_real_repo] expected failure mode if broken: a genuinely append-only two-commit history is reported as violating, or the wrong commit count is walked
    [check13_history_walk_real_repo] PASS
    
    [check14_history_walk_vacuous_single_commit] expected failure mode if broken: a RECORD.md history with only one committed version performs a comparison anyway, or is not reported vacuous
    [check14_history_walk_vacuous_single_commit] PASS
    
    [check15_history_walk_catches_removed_line] expected failure mode if broken: a commit that removed an existing line from RECORD.md's history is accepted by the walk
    [check15_history_walk_catches_removed_line] PASS
    
    [check16_merge_commit_stops_the_walk] expected failure mode if broken: a merge commit touching RECORD.md is silently walked (wrong parent guessed) instead of raising MergeCommitEncountered
    [check16_merge_commit_stops_the_walk] PASS
    
    [check17_superseded_by_vacuous_when_none_declared] expected failure mode if broken: a record with no terminal entry declaring Outcome: superseded is not reported vacuous, or is reported as a failure
    [check17_superseded_by_vacuous_when_none_declared] PASS
    
    [check18_superseded_by_catches_dangling_reference] expected failure mode if broken: a terminal entry's Superseded-by field naming a nonexistent intent ID is accepted
    [check18_superseded_by_catches_dangling_reference] PASS
    
    [check19_all_twelve_kinds_accepted] expected failure mode if broken: a record using every RECORDING.md entry type with minimal fields is rejected
    [check19_all_twelve_kinds_accepted] PASS
    
    [check20_unknown_kind_still_rejected] expected failure mode if broken: a kind outside the twelve is accepted (guard: passes before and after the change by design, so it is not evidence for the change)
    [check20_unknown_kind_still_rejected] PASS
    
    [check21_new_kind_missing_notes_named] expected failure mode if broken: an entry of a new type without its Notes line is accepted
    [check21_new_kind_missing_notes_named] PASS
    
    [check22_continuation_missing_continues_named] expected failure mode if broken: a continuation with no Continues field is accepted
    [check22_continuation_missing_continues_named] PASS
    
    [check23_continuation_of_closed_intent_caught] expected failure mode if broken: a continuation naming an intent already closed earlier in the file is accepted
    [check23_continuation_of_closed_intent_caught] PASS
    
    [check24_continuation_of_non_intent_caught] expected failure mode if broken: a continuation naming an entry that is not an intent is accepted
    [check24_continuation_of_non_intent_caught] PASS
    
    [check25_continuation_forbidden_field_caught] expected failure mode if broken: a continuation carrying a closing field (Outcome) is accepted
    [check25_continuation_forbidden_field_caught] PASS
    
    [check26_outcome_with_closes_closes_intent] expected failure mode if broken: an outcome carrying Closes is rejected, or leaves its intent unterminated
    [check26_outcome_with_closes_closes_intent] PASS
    
    [check27_terminal_and_outcome_double_close_caught] expected failure mode if broken: an intent closed by both a terminal and an outcome passes the closed-once check
    [check27_terminal_and_outcome_double_close_caught] PASS
    
    [check28_outcome_needs_continues_or_closes] expected failure mode if broken: an outcome with neither Continues nor Closes is accepted
    [check28_outcome_needs_continues_or_closes] PASS
    
    [check29_correction_dangling_reference_caught] expected failure mode if broken: a correction whose Corrects names no existing entry is accepted
    [check29_correction_dangling_reference_caught] PASS
    
    [check30_closes_on_other_kind_caught] expected failure mode if broken: a type other than terminal or outcome carrying Closes is accepted
    [check30_closes_on_other_kind_caught] PASS
    
    [check31_unknown_terminal_outcome_caught] expected failure mode if broken: a terminal Outcome outside completed, partial, superseded, abandoned is accepted
    [check31_unknown_terminal_outcome_caught] PASS
    
    [check32_partial_requires_deferred] expected failure mode if broken: a partial terminal without a Deferred field is accepted
    [check32_partial_requires_deferred] PASS
    
    [check33_completed_with_deferred_caught] expected failure mode if broken: a completed terminal carrying Deferred is accepted
    [check33_completed_with_deferred_caught] PASS
    
    [check34_merge_requires_backup] expected failure mode if broken: a merge entry that names no backup is accepted
    [check34_merge_requires_backup] PASS
    
    [check35_dispatch_note_requires_dispatch_reference] expected failure mode if broken: a dispatch-note naming neither Dispatch-file nor Dispatch is accepted
    [check35_dispatch_note_requires_dispatch_reference] PASS
    
    [check36_continues_dangling_on_other_kind_caught] expected failure mode if broken: a Continues on a decision naming no existing entry is accepted
    [check36_continues_dangling_on_other_kind_caught] PASS
    
    [check37_every_new_kind_requires_notes] expected failure mode if broken: some new entry type is accepted without its who-wrote-it Notes line
    [check37_every_new_kind_requires_notes] PASS
    
    [check38_link_fields_required] expected failure mode if broken: a finding without Continues, a correction without Corrects, or a merge without Merge-commit is accepted
    [check38_link_fields_required] PASS
    
    PASS: 0 of 38 checks failed

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_terminal_2026_10_16_14

**Timestamp:** 2026-10-17T01:55:28Z

**Expected failure mode:** Expected PASS: 14 entries, preserved=13.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 14
    files under prompts/: preserved=13, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_terminal_2026_10_16_14

**Timestamp:** 2026-10-17T01:55:29Z

**Expected failure mode:** Expected PASS at 45/44/45.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        45
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** check_record_terminal_2026_10_16_16

**Timestamp:** 2026-10-17T01:59:14Z

**Expected failure mode:** Expected PASS: 40 entries, none unterminated.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 40
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-07: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-09: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-11: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-15: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 37 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_record_selftest_2026_10_16_16

**Timestamp:** 2026-10-17T01:59:14Z

**Expected failure mode:** Expected PASS: 0 of 38.

**Command:** python3 check_record.py --render-check

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    check_record.py --render-check
    
    [check1_well_formed_record_passes] expected failure mode if broken: N/A -- positive case, validated by the negative checks below catching sabotages of the same fixture
    [check1_well_formed_record_passes] PASS
    
    [check2_missing_field_names_fault] expected failure mode if broken: an entry missing a required field is accepted, or the error does not name both the entry and the missing field
    [check2_missing_field_names_fault] PASS
    
    [check3_missing_restored_prediction_field_caught] expected failure mode if broken: an intent entry missing the restored 'Prediction (outcome — planner)' field is accepted, or the error does not name it
    [check3_missing_restored_prediction_field_caught] PASS
    
    [check4_closes_resolution_catches_dangling_reference] expected failure mode if broken: a terminal entry's Closes field naming a nonexistent intent ID is accepted silently
    [check4_closes_resolution_catches_dangling_reference] PASS
    
    [check5_duplicate_id_caught] expected failure mode if broken: two entries sharing the same ID are accepted, or the error does not name the colliding ID
    [check5_duplicate_id_caught] PASS
    
    [check6_duplicate_terminal_names_both_closers] expected failure mode if broken: one intent closed by two terminal entries is accepted, or the error does not name both closing entries
    [check6_duplicate_terminal_names_both_closers] PASS
    
    [check7_withheld_sentinel_reported_pending] expected failure mode if broken: a 'withheld' outcome-prediction sentinel is either treated as an error or not surfaced in sentinel_reports as pending
    [check7_withheld_sentinel_reported_pending] PASS
    
    [check8_withheld_sentinel_resolved_by_terminal] expected failure mode if broken: a terminal entry supplying the outcome for an intent whose prediction was legitimately 'withheld' is not recognized as a resolution
    [check8_withheld_sentinel_resolved_by_terminal] PASS
    
    [check9_not_authored_plus_supplied_is_fabrication] expected failure mode if broken: an intent whose outcome prediction is permanently 'not authored' is not flagged when a terminal entry later supplies a value anyway
    [check9_not_authored_plus_supplied_is_fabrication] PASS
    
    [check10_sentinel_forbidden_in_terminal_entry] expected failure mode if broken: a terminal entry carrying a sentinel value in any field is accepted, or the error does not name the field and value
    [check10_sentinel_forbidden_in_terminal_entry] PASS
    
    [check11_working_tree_append_only_catches_modified_line] expected failure mode if broken: modifying an existing, already-committed line in RECORD.md is not caught, or the failure does not name the changed line
    [check11_working_tree_append_only_catches_modified_line] PASS
    
    [check12_working_tree_append_only_vacuous_before_first_commit] expected failure mode if broken: a RECORD.md that exists in the working tree but has never been committed is reported as a violation, or the vacuous case is not flagged as vacuous
    [check12_working_tree_append_only_vacuous_before_first_commit] PASS
    
    [check13_history_walk_real_repo] expected failure mode if broken: a genuinely append-only two-commit history is reported as violating, or the wrong commit count is walked
    [check13_history_walk_real_repo] PASS
    
    [check14_history_walk_vacuous_single_commit] expected failure mode if broken: a RECORD.md history with only one committed version performs a comparison anyway, or is not reported vacuous
    [check14_history_walk_vacuous_single_commit] PASS
    
    [check15_history_walk_catches_removed_line] expected failure mode if broken: a commit that removed an existing line from RECORD.md's history is accepted by the walk
    [check15_history_walk_catches_removed_line] PASS
    
    [check16_merge_commit_stops_the_walk] expected failure mode if broken: a merge commit touching RECORD.md is silently walked (wrong parent guessed) instead of raising MergeCommitEncountered
    [check16_merge_commit_stops_the_walk] PASS
    
    [check17_superseded_by_vacuous_when_none_declared] expected failure mode if broken: a record with no terminal entry declaring Outcome: superseded is not reported vacuous, or is reported as a failure
    [check17_superseded_by_vacuous_when_none_declared] PASS
    
    [check18_superseded_by_catches_dangling_reference] expected failure mode if broken: a terminal entry's Superseded-by field naming a nonexistent intent ID is accepted
    [check18_superseded_by_catches_dangling_reference] PASS
    
    [check19_all_twelve_kinds_accepted] expected failure mode if broken: a record using every RECORDING.md entry type with minimal fields is rejected
    [check19_all_twelve_kinds_accepted] PASS
    
    [check20_unknown_kind_still_rejected] expected failure mode if broken: a kind outside the twelve is accepted (guard: passes before and after the change by design, so it is not evidence for the change)
    [check20_unknown_kind_still_rejected] PASS
    
    [check21_new_kind_missing_notes_named] expected failure mode if broken: an entry of a new type without its Notes line is accepted
    [check21_new_kind_missing_notes_named] PASS
    
    [check22_continuation_missing_continues_named] expected failure mode if broken: a continuation with no Continues field is accepted
    [check22_continuation_missing_continues_named] PASS
    
    [check23_continuation_of_closed_intent_caught] expected failure mode if broken: a continuation naming an intent already closed earlier in the file is accepted
    [check23_continuation_of_closed_intent_caught] PASS
    
    [check24_continuation_of_non_intent_caught] expected failure mode if broken: a continuation naming an entry that is not an intent is accepted
    [check24_continuation_of_non_intent_caught] PASS
    
    [check25_continuation_forbidden_field_caught] expected failure mode if broken: a continuation carrying a closing field (Outcome) is accepted
    [check25_continuation_forbidden_field_caught] PASS
    
    [check26_outcome_with_closes_closes_intent] expected failure mode if broken: an outcome carrying Closes is rejected, or leaves its intent unterminated
    [check26_outcome_with_closes_closes_intent] PASS
    
    [check27_terminal_and_outcome_double_close_caught] expected failure mode if broken: an intent closed by both a terminal and an outcome passes the closed-once check
    [check27_terminal_and_outcome_double_close_caught] PASS
    
    [check28_outcome_needs_continues_or_closes] expected failure mode if broken: an outcome with neither Continues nor Closes is accepted
    [check28_outcome_needs_continues_or_closes] PASS
    
    [check29_correction_dangling_reference_caught] expected failure mode if broken: a correction whose Corrects names no existing entry is accepted
    [check29_correction_dangling_reference_caught] PASS
    
    [check30_closes_on_other_kind_caught] expected failure mode if broken: a type other than terminal or outcome carrying Closes is accepted
    [check30_closes_on_other_kind_caught] PASS
    
    [check31_unknown_terminal_outcome_caught] expected failure mode if broken: a terminal Outcome outside completed, partial, superseded, abandoned is accepted
    [check31_unknown_terminal_outcome_caught] PASS
    
    [check32_partial_requires_deferred] expected failure mode if broken: a partial terminal without a Deferred field is accepted
    [check32_partial_requires_deferred] PASS
    
    [check33_completed_with_deferred_caught] expected failure mode if broken: a completed terminal carrying Deferred is accepted
    [check33_completed_with_deferred_caught] PASS
    
    [check34_merge_requires_backup] expected failure mode if broken: a merge entry that names no backup is accepted
    [check34_merge_requires_backup] PASS
    
    [check35_dispatch_note_requires_dispatch_reference] expected failure mode if broken: a dispatch-note naming neither Dispatch-file nor Dispatch is accepted
    [check35_dispatch_note_requires_dispatch_reference] PASS
    
    [check36_continues_dangling_on_other_kind_caught] expected failure mode if broken: a Continues on a decision naming no existing entry is accepted
    [check36_continues_dangling_on_other_kind_caught] PASS
    
    [check37_every_new_kind_requires_notes] expected failure mode if broken: some new entry type is accepted without its who-wrote-it Notes line
    [check37_every_new_kind_requires_notes] PASS
    
    [check38_link_fields_required] expected failure mode if broken: a finding without Continues, a correction without Corrects, or a merge without Merge-commit is accepted
    [check38_link_fields_required] PASS
    
    PASS: 0 of 38 checks failed

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_terminal_2026_10_16_16

**Timestamp:** 2026-10-17T01:59:14Z

**Expected failure mode:** Expected PASS: 15 entries, preserved=14.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 15
    files under prompts/: preserved=14, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_terminal_2026_10_16_16

**Timestamp:** 2026-10-17T01:59:14Z

**Expected failure mode:** Expected PASS at 45/44/45.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        45
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** check_record_terminal_2026_10_16_18

**Timestamp:** 2026-10-17T02:10:29Z

**Expected failure mode:** Expected PASS: 42 entries, none unterminated -- the quoted Forager texts, indented four spaces, add no entries, fields or headings.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 42
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-07: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-09: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-11: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-15: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-17: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 39 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_record_selftest_2026_10_16_18

**Timestamp:** 2026-10-17T02:10:29Z

**Expected failure mode:** Expected PASS: 0 of 38.

**Command:** python3 check_record.py --render-check

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    check_record.py --render-check
    
    [check1_well_formed_record_passes] expected failure mode if broken: N/A -- positive case, validated by the negative checks below catching sabotages of the same fixture
    [check1_well_formed_record_passes] PASS
    
    [check2_missing_field_names_fault] expected failure mode if broken: an entry missing a required field is accepted, or the error does not name both the entry and the missing field
    [check2_missing_field_names_fault] PASS
    
    [check3_missing_restored_prediction_field_caught] expected failure mode if broken: an intent entry missing the restored 'Prediction (outcome — planner)' field is accepted, or the error does not name it
    [check3_missing_restored_prediction_field_caught] PASS
    
    [check4_closes_resolution_catches_dangling_reference] expected failure mode if broken: a terminal entry's Closes field naming a nonexistent intent ID is accepted silently
    [check4_closes_resolution_catches_dangling_reference] PASS
    
    [check5_duplicate_id_caught] expected failure mode if broken: two entries sharing the same ID are accepted, or the error does not name the colliding ID
    [check5_duplicate_id_caught] PASS
    
    [check6_duplicate_terminal_names_both_closers] expected failure mode if broken: one intent closed by two terminal entries is accepted, or the error does not name both closing entries
    [check6_duplicate_terminal_names_both_closers] PASS
    
    [check7_withheld_sentinel_reported_pending] expected failure mode if broken: a 'withheld' outcome-prediction sentinel is either treated as an error or not surfaced in sentinel_reports as pending
    [check7_withheld_sentinel_reported_pending] PASS
    
    [check8_withheld_sentinel_resolved_by_terminal] expected failure mode if broken: a terminal entry supplying the outcome for an intent whose prediction was legitimately 'withheld' is not recognized as a resolution
    [check8_withheld_sentinel_resolved_by_terminal] PASS
    
    [check9_not_authored_plus_supplied_is_fabrication] expected failure mode if broken: an intent whose outcome prediction is permanently 'not authored' is not flagged when a terminal entry later supplies a value anyway
    [check9_not_authored_plus_supplied_is_fabrication] PASS
    
    [check10_sentinel_forbidden_in_terminal_entry] expected failure mode if broken: a terminal entry carrying a sentinel value in any field is accepted, or the error does not name the field and value
    [check10_sentinel_forbidden_in_terminal_entry] PASS
    
    [check11_working_tree_append_only_catches_modified_line] expected failure mode if broken: modifying an existing, already-committed line in RECORD.md is not caught, or the failure does not name the changed line
    [check11_working_tree_append_only_catches_modified_line] PASS
    
    [check12_working_tree_append_only_vacuous_before_first_commit] expected failure mode if broken: a RECORD.md that exists in the working tree but has never been committed is reported as a violation, or the vacuous case is not flagged as vacuous
    [check12_working_tree_append_only_vacuous_before_first_commit] PASS
    
    [check13_history_walk_real_repo] expected failure mode if broken: a genuinely append-only two-commit history is reported as violating, or the wrong commit count is walked
    [check13_history_walk_real_repo] PASS
    
    [check14_history_walk_vacuous_single_commit] expected failure mode if broken: a RECORD.md history with only one committed version performs a comparison anyway, or is not reported vacuous
    [check14_history_walk_vacuous_single_commit] PASS
    
    [check15_history_walk_catches_removed_line] expected failure mode if broken: a commit that removed an existing line from RECORD.md's history is accepted by the walk
    [check15_history_walk_catches_removed_line] PASS
    
    [check16_merge_commit_stops_the_walk] expected failure mode if broken: a merge commit touching RECORD.md is silently walked (wrong parent guessed) instead of raising MergeCommitEncountered
    [check16_merge_commit_stops_the_walk] PASS
    
    [check17_superseded_by_vacuous_when_none_declared] expected failure mode if broken: a record with no terminal entry declaring Outcome: superseded is not reported vacuous, or is reported as a failure
    [check17_superseded_by_vacuous_when_none_declared] PASS
    
    [check18_superseded_by_catches_dangling_reference] expected failure mode if broken: a terminal entry's Superseded-by field naming a nonexistent intent ID is accepted
    [check18_superseded_by_catches_dangling_reference] PASS
    
    [check19_all_twelve_kinds_accepted] expected failure mode if broken: a record using every RECORDING.md entry type with minimal fields is rejected
    [check19_all_twelve_kinds_accepted] PASS
    
    [check20_unknown_kind_still_rejected] expected failure mode if broken: a kind outside the twelve is accepted (guard: passes before and after the change by design, so it is not evidence for the change)
    [check20_unknown_kind_still_rejected] PASS
    
    [check21_new_kind_missing_notes_named] expected failure mode if broken: an entry of a new type without its Notes line is accepted
    [check21_new_kind_missing_notes_named] PASS
    
    [check22_continuation_missing_continues_named] expected failure mode if broken: a continuation with no Continues field is accepted
    [check22_continuation_missing_continues_named] PASS
    
    [check23_continuation_of_closed_intent_caught] expected failure mode if broken: a continuation naming an intent already closed earlier in the file is accepted
    [check23_continuation_of_closed_intent_caught] PASS
    
    [check24_continuation_of_non_intent_caught] expected failure mode if broken: a continuation naming an entry that is not an intent is accepted
    [check24_continuation_of_non_intent_caught] PASS
    
    [check25_continuation_forbidden_field_caught] expected failure mode if broken: a continuation carrying a closing field (Outcome) is accepted
    [check25_continuation_forbidden_field_caught] PASS
    
    [check26_outcome_with_closes_closes_intent] expected failure mode if broken: an outcome carrying Closes is rejected, or leaves its intent unterminated
    [check26_outcome_with_closes_closes_intent] PASS
    
    [check27_terminal_and_outcome_double_close_caught] expected failure mode if broken: an intent closed by both a terminal and an outcome passes the closed-once check
    [check27_terminal_and_outcome_double_close_caught] PASS
    
    [check28_outcome_needs_continues_or_closes] expected failure mode if broken: an outcome with neither Continues nor Closes is accepted
    [check28_outcome_needs_continues_or_closes] PASS
    
    [check29_correction_dangling_reference_caught] expected failure mode if broken: a correction whose Corrects names no existing entry is accepted
    [check29_correction_dangling_reference_caught] PASS
    
    [check30_closes_on_other_kind_caught] expected failure mode if broken: a type other than terminal or outcome carrying Closes is accepted
    [check30_closes_on_other_kind_caught] PASS
    
    [check31_unknown_terminal_outcome_caught] expected failure mode if broken: a terminal Outcome outside completed, partial, superseded, abandoned is accepted
    [check31_unknown_terminal_outcome_caught] PASS
    
    [check32_partial_requires_deferred] expected failure mode if broken: a partial terminal without a Deferred field is accepted
    [check32_partial_requires_deferred] PASS
    
    [check33_completed_with_deferred_caught] expected failure mode if broken: a completed terminal carrying Deferred is accepted
    [check33_completed_with_deferred_caught] PASS
    
    [check34_merge_requires_backup] expected failure mode if broken: a merge entry that names no backup is accepted
    [check34_merge_requires_backup] PASS
    
    [check35_dispatch_note_requires_dispatch_reference] expected failure mode if broken: a dispatch-note naming neither Dispatch-file nor Dispatch is accepted
    [check35_dispatch_note_requires_dispatch_reference] PASS
    
    [check36_continues_dangling_on_other_kind_caught] expected failure mode if broken: a Continues on a decision naming no existing entry is accepted
    [check36_continues_dangling_on_other_kind_caught] PASS
    
    [check37_every_new_kind_requires_notes] expected failure mode if broken: some new entry type is accepted without its who-wrote-it Notes line
    [check37_every_new_kind_requires_notes] PASS
    
    [check38_link_fields_required] expected failure mode if broken: a finding without Continues, a correction without Corrects, or a merge without Merge-commit is accepted
    [check38_link_fields_required] PASS
    
    PASS: 0 of 38 checks failed

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_terminal_2026_10_16_18

**Timestamp:** 2026-10-17T02:10:29Z

**Expected failure mode:** Expected PASS: 16 entries, preserved=15.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 16
    files under prompts/: preserved=15, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_terminal_2026_10_16_18

**Timestamp:** 2026-10-17T02:10:29Z

**Expected failure mode:** Expected PASS at 45/44/45.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        45
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** profile_citations_exist_2026_10_16_19

**Timestamp:** 2026-10-17T04:57:26Z

**Expected failure mode:** Would fail naming any record ID, commit or preserved prompt cited in profiles/curator.md that does not exist. Expected PASS: 14 IDs, 6 commits, 5 prompt files, none missing.

**Command:** python3 -I /tmp/egd-scripts/profile_cites.py /home/zynergy-labs/Zynergy/E-GD-Philosophy

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    record IDs cited: 14, missing: []
    commits cited: 6, missing: []
    prompt files cited: 5, missing: []
    PASS

**Stderr:**

    (nothing captured)

---

**Check:** control_profile_citations_catch_missing_id

**Timestamp:** 2026-10-17T04:57:26Z

**Expected failure mode:** Positive control: a copy of the profile citing 2026-10-16-99, which does not exist. Expected exit 1, FAIL naming 2026-10-16-99. (Commit citations also fail in the scratch copy, which has no git history; that is expected.)

**Command:** python3 -I /tmp/egd-scripts/profile_cites.py /tmp/egd-ctl2

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    record IDs cited: 15, missing: ['2026-10-16-99']
    commits cited: 6, missing: ['6da5b1d', '5c6b56f', '8203cf2', '8a548f2', '4ca06d0', '4adf4be']
    prompt files cited: 5, missing: ['2026-10-16-09', '2026-10-16-05', '2026-10-16-07', '2026-10-16-01', '2026-10-16-17']
    FAIL

**Stderr:**

    (nothing captured)

---

**Check:** check_record_terminal_2026_10_16_20

**Timestamp:** 2026-10-17T04:57:26Z

**Expected failure mode:** Expected PASS: 44 entries, none unterminated.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 44
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-07: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-09: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-11: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-15: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-17: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-19: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 41 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_record_selftest_2026_10_16_20

**Timestamp:** 2026-10-17T04:57:27Z

**Expected failure mode:** Expected PASS: 0 of 38.

**Command:** python3 check_record.py --render-check

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    check_record.py --render-check
    
    [check1_well_formed_record_passes] expected failure mode if broken: N/A -- positive case, validated by the negative checks below catching sabotages of the same fixture
    [check1_well_formed_record_passes] PASS
    
    [check2_missing_field_names_fault] expected failure mode if broken: an entry missing a required field is accepted, or the error does not name both the entry and the missing field
    [check2_missing_field_names_fault] PASS
    
    [check3_missing_restored_prediction_field_caught] expected failure mode if broken: an intent entry missing the restored 'Prediction (outcome — planner)' field is accepted, or the error does not name it
    [check3_missing_restored_prediction_field_caught] PASS
    
    [check4_closes_resolution_catches_dangling_reference] expected failure mode if broken: a terminal entry's Closes field naming a nonexistent intent ID is accepted silently
    [check4_closes_resolution_catches_dangling_reference] PASS
    
    [check5_duplicate_id_caught] expected failure mode if broken: two entries sharing the same ID are accepted, or the error does not name the colliding ID
    [check5_duplicate_id_caught] PASS
    
    [check6_duplicate_terminal_names_both_closers] expected failure mode if broken: one intent closed by two terminal entries is accepted, or the error does not name both closing entries
    [check6_duplicate_terminal_names_both_closers] PASS
    
    [check7_withheld_sentinel_reported_pending] expected failure mode if broken: a 'withheld' outcome-prediction sentinel is either treated as an error or not surfaced in sentinel_reports as pending
    [check7_withheld_sentinel_reported_pending] PASS
    
    [check8_withheld_sentinel_resolved_by_terminal] expected failure mode if broken: a terminal entry supplying the outcome for an intent whose prediction was legitimately 'withheld' is not recognized as a resolution
    [check8_withheld_sentinel_resolved_by_terminal] PASS
    
    [check9_not_authored_plus_supplied_is_fabrication] expected failure mode if broken: an intent whose outcome prediction is permanently 'not authored' is not flagged when a terminal entry later supplies a value anyway
    [check9_not_authored_plus_supplied_is_fabrication] PASS
    
    [check10_sentinel_forbidden_in_terminal_entry] expected failure mode if broken: a terminal entry carrying a sentinel value in any field is accepted, or the error does not name the field and value
    [check10_sentinel_forbidden_in_terminal_entry] PASS
    
    [check11_working_tree_append_only_catches_modified_line] expected failure mode if broken: modifying an existing, already-committed line in RECORD.md is not caught, or the failure does not name the changed line
    [check11_working_tree_append_only_catches_modified_line] PASS
    
    [check12_working_tree_append_only_vacuous_before_first_commit] expected failure mode if broken: a RECORD.md that exists in the working tree but has never been committed is reported as a violation, or the vacuous case is not flagged as vacuous
    [check12_working_tree_append_only_vacuous_before_first_commit] PASS
    
    [check13_history_walk_real_repo] expected failure mode if broken: a genuinely append-only two-commit history is reported as violating, or the wrong commit count is walked
    [check13_history_walk_real_repo] PASS
    
    [check14_history_walk_vacuous_single_commit] expected failure mode if broken: a RECORD.md history with only one committed version performs a comparison anyway, or is not reported vacuous
    [check14_history_walk_vacuous_single_commit] PASS
    
    [check15_history_walk_catches_removed_line] expected failure mode if broken: a commit that removed an existing line from RECORD.md's history is accepted by the walk
    [check15_history_walk_catches_removed_line] PASS
    
    [check16_merge_commit_stops_the_walk] expected failure mode if broken: a merge commit touching RECORD.md is silently walked (wrong parent guessed) instead of raising MergeCommitEncountered
    [check16_merge_commit_stops_the_walk] PASS
    
    [check17_superseded_by_vacuous_when_none_declared] expected failure mode if broken: a record with no terminal entry declaring Outcome: superseded is not reported vacuous, or is reported as a failure
    [check17_superseded_by_vacuous_when_none_declared] PASS
    
    [check18_superseded_by_catches_dangling_reference] expected failure mode if broken: a terminal entry's Superseded-by field naming a nonexistent intent ID is accepted
    [check18_superseded_by_catches_dangling_reference] PASS
    
    [check19_all_twelve_kinds_accepted] expected failure mode if broken: a record using every RECORDING.md entry type with minimal fields is rejected
    [check19_all_twelve_kinds_accepted] PASS
    
    [check20_unknown_kind_still_rejected] expected failure mode if broken: a kind outside the twelve is accepted (guard: passes before and after the change by design, so it is not evidence for the change)
    [check20_unknown_kind_still_rejected] PASS
    
    [check21_new_kind_missing_notes_named] expected failure mode if broken: an entry of a new type without its Notes line is accepted
    [check21_new_kind_missing_notes_named] PASS
    
    [check22_continuation_missing_continues_named] expected failure mode if broken: a continuation with no Continues field is accepted
    [check22_continuation_missing_continues_named] PASS
    
    [check23_continuation_of_closed_intent_caught] expected failure mode if broken: a continuation naming an intent already closed earlier in the file is accepted
    [check23_continuation_of_closed_intent_caught] PASS
    
    [check24_continuation_of_non_intent_caught] expected failure mode if broken: a continuation naming an entry that is not an intent is accepted
    [check24_continuation_of_non_intent_caught] PASS
    
    [check25_continuation_forbidden_field_caught] expected failure mode if broken: a continuation carrying a closing field (Outcome) is accepted
    [check25_continuation_forbidden_field_caught] PASS
    
    [check26_outcome_with_closes_closes_intent] expected failure mode if broken: an outcome carrying Closes is rejected, or leaves its intent unterminated
    [check26_outcome_with_closes_closes_intent] PASS
    
    [check27_terminal_and_outcome_double_close_caught] expected failure mode if broken: an intent closed by both a terminal and an outcome passes the closed-once check
    [check27_terminal_and_outcome_double_close_caught] PASS
    
    [check28_outcome_needs_continues_or_closes] expected failure mode if broken: an outcome with neither Continues nor Closes is accepted
    [check28_outcome_needs_continues_or_closes] PASS
    
    [check29_correction_dangling_reference_caught] expected failure mode if broken: a correction whose Corrects names no existing entry is accepted
    [check29_correction_dangling_reference_caught] PASS
    
    [check30_closes_on_other_kind_caught] expected failure mode if broken: a type other than terminal or outcome carrying Closes is accepted
    [check30_closes_on_other_kind_caught] PASS
    
    [check31_unknown_terminal_outcome_caught] expected failure mode if broken: a terminal Outcome outside completed, partial, superseded, abandoned is accepted
    [check31_unknown_terminal_outcome_caught] PASS
    
    [check32_partial_requires_deferred] expected failure mode if broken: a partial terminal without a Deferred field is accepted
    [check32_partial_requires_deferred] PASS
    
    [check33_completed_with_deferred_caught] expected failure mode if broken: a completed terminal carrying Deferred is accepted
    [check33_completed_with_deferred_caught] PASS
    
    [check34_merge_requires_backup] expected failure mode if broken: a merge entry that names no backup is accepted
    [check34_merge_requires_backup] PASS
    
    [check35_dispatch_note_requires_dispatch_reference] expected failure mode if broken: a dispatch-note naming neither Dispatch-file nor Dispatch is accepted
    [check35_dispatch_note_requires_dispatch_reference] PASS
    
    [check36_continues_dangling_on_other_kind_caught] expected failure mode if broken: a Continues on a decision naming no existing entry is accepted
    [check36_continues_dangling_on_other_kind_caught] PASS
    
    [check37_every_new_kind_requires_notes] expected failure mode if broken: some new entry type is accepted without its who-wrote-it Notes line
    [check37_every_new_kind_requires_notes] PASS
    
    [check38_link_fields_required] expected failure mode if broken: a finding without Continues, a correction without Corrects, or a merge without Merge-commit is accepted
    [check38_link_fields_required] PASS
    
    PASS: 0 of 38 checks failed

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_terminal_2026_10_16_20

**Timestamp:** 2026-10-17T04:57:27Z

**Expected failure mode:** Expected PASS: 17 entries, preserved=16.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 17
    files under prompts/: preserved=16, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_terminal_2026_10_16_20

**Timestamp:** 2026-10-17T04:57:27Z

**Expected failure mode:** Expected PASS at 45/44/45.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        45
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** check_record_terminal_2026_10_16_22

**Timestamp:** 2026-10-17T04:59:24Z

**Expected failure mode:** Expected PASS: 46 entries, none unterminated.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 46
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-07: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-09: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-11: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-15: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-17: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-19: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-21: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 43 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_terminal_2026_10_16_22

**Timestamp:** 2026-10-17T04:59:24Z

**Expected failure mode:** Expected PASS: 18 entries, preserved=17.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 18
    files under prompts/: preserved=17, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_terminal_2026_10_16_22

**Timestamp:** 2026-10-17T04:59:24Z

**Expected failure mode:** Expected PASS at 45/44/45.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        45
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** check_record_terminal_2026_10_16_24

**Timestamp:** 2026-10-17T05:15:55Z

**Expected failure mode:** Expected PASS: 48 entries, none unterminated.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 48
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-07: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-09: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-11: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-15: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-17: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-19: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-21: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-23: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 45 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_record_selftest_2026_10_16_24

**Timestamp:** 2026-10-17T05:15:55Z

**Expected failure mode:** Expected PASS: 0 of 38.

**Command:** python3 check_record.py --render-check

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    check_record.py --render-check
    
    [check1_well_formed_record_passes] expected failure mode if broken: N/A -- positive case, validated by the negative checks below catching sabotages of the same fixture
    [check1_well_formed_record_passes] PASS
    
    [check2_missing_field_names_fault] expected failure mode if broken: an entry missing a required field is accepted, or the error does not name both the entry and the missing field
    [check2_missing_field_names_fault] PASS
    
    [check3_missing_restored_prediction_field_caught] expected failure mode if broken: an intent entry missing the restored 'Prediction (outcome — planner)' field is accepted, or the error does not name it
    [check3_missing_restored_prediction_field_caught] PASS
    
    [check4_closes_resolution_catches_dangling_reference] expected failure mode if broken: a terminal entry's Closes field naming a nonexistent intent ID is accepted silently
    [check4_closes_resolution_catches_dangling_reference] PASS
    
    [check5_duplicate_id_caught] expected failure mode if broken: two entries sharing the same ID are accepted, or the error does not name the colliding ID
    [check5_duplicate_id_caught] PASS
    
    [check6_duplicate_terminal_names_both_closers] expected failure mode if broken: one intent closed by two terminal entries is accepted, or the error does not name both closing entries
    [check6_duplicate_terminal_names_both_closers] PASS
    
    [check7_withheld_sentinel_reported_pending] expected failure mode if broken: a 'withheld' outcome-prediction sentinel is either treated as an error or not surfaced in sentinel_reports as pending
    [check7_withheld_sentinel_reported_pending] PASS
    
    [check8_withheld_sentinel_resolved_by_terminal] expected failure mode if broken: a terminal entry supplying the outcome for an intent whose prediction was legitimately 'withheld' is not recognized as a resolution
    [check8_withheld_sentinel_resolved_by_terminal] PASS
    
    [check9_not_authored_plus_supplied_is_fabrication] expected failure mode if broken: an intent whose outcome prediction is permanently 'not authored' is not flagged when a terminal entry later supplies a value anyway
    [check9_not_authored_plus_supplied_is_fabrication] PASS
    
    [check10_sentinel_forbidden_in_terminal_entry] expected failure mode if broken: a terminal entry carrying a sentinel value in any field is accepted, or the error does not name the field and value
    [check10_sentinel_forbidden_in_terminal_entry] PASS
    
    [check11_working_tree_append_only_catches_modified_line] expected failure mode if broken: modifying an existing, already-committed line in RECORD.md is not caught, or the failure does not name the changed line
    [check11_working_tree_append_only_catches_modified_line] PASS
    
    [check12_working_tree_append_only_vacuous_before_first_commit] expected failure mode if broken: a RECORD.md that exists in the working tree but has never been committed is reported as a violation, or the vacuous case is not flagged as vacuous
    [check12_working_tree_append_only_vacuous_before_first_commit] PASS
    
    [check13_history_walk_real_repo] expected failure mode if broken: a genuinely append-only two-commit history is reported as violating, or the wrong commit count is walked
    [check13_history_walk_real_repo] PASS
    
    [check14_history_walk_vacuous_single_commit] expected failure mode if broken: a RECORD.md history with only one committed version performs a comparison anyway, or is not reported vacuous
    [check14_history_walk_vacuous_single_commit] PASS
    
    [check15_history_walk_catches_removed_line] expected failure mode if broken: a commit that removed an existing line from RECORD.md's history is accepted by the walk
    [check15_history_walk_catches_removed_line] PASS
    
    [check16_merge_commit_stops_the_walk] expected failure mode if broken: a merge commit touching RECORD.md is silently walked (wrong parent guessed) instead of raising MergeCommitEncountered
    [check16_merge_commit_stops_the_walk] PASS
    
    [check17_superseded_by_vacuous_when_none_declared] expected failure mode if broken: a record with no terminal entry declaring Outcome: superseded is not reported vacuous, or is reported as a failure
    [check17_superseded_by_vacuous_when_none_declared] PASS
    
    [check18_superseded_by_catches_dangling_reference] expected failure mode if broken: a terminal entry's Superseded-by field naming a nonexistent intent ID is accepted
    [check18_superseded_by_catches_dangling_reference] PASS
    
    [check19_all_twelve_kinds_accepted] expected failure mode if broken: a record using every RECORDING.md entry type with minimal fields is rejected
    [check19_all_twelve_kinds_accepted] PASS
    
    [check20_unknown_kind_still_rejected] expected failure mode if broken: a kind outside the twelve is accepted (guard: passes before and after the change by design, so it is not evidence for the change)
    [check20_unknown_kind_still_rejected] PASS
    
    [check21_new_kind_missing_notes_named] expected failure mode if broken: an entry of a new type without its Notes line is accepted
    [check21_new_kind_missing_notes_named] PASS
    
    [check22_continuation_missing_continues_named] expected failure mode if broken: a continuation with no Continues field is accepted
    [check22_continuation_missing_continues_named] PASS
    
    [check23_continuation_of_closed_intent_caught] expected failure mode if broken: a continuation naming an intent already closed earlier in the file is accepted
    [check23_continuation_of_closed_intent_caught] PASS
    
    [check24_continuation_of_non_intent_caught] expected failure mode if broken: a continuation naming an entry that is not an intent is accepted
    [check24_continuation_of_non_intent_caught] PASS
    
    [check25_continuation_forbidden_field_caught] expected failure mode if broken: a continuation carrying a closing field (Outcome) is accepted
    [check25_continuation_forbidden_field_caught] PASS
    
    [check26_outcome_with_closes_closes_intent] expected failure mode if broken: an outcome carrying Closes is rejected, or leaves its intent unterminated
    [check26_outcome_with_closes_closes_intent] PASS
    
    [check27_terminal_and_outcome_double_close_caught] expected failure mode if broken: an intent closed by both a terminal and an outcome passes the closed-once check
    [check27_terminal_and_outcome_double_close_caught] PASS
    
    [check28_outcome_needs_continues_or_closes] expected failure mode if broken: an outcome with neither Continues nor Closes is accepted
    [check28_outcome_needs_continues_or_closes] PASS
    
    [check29_correction_dangling_reference_caught] expected failure mode if broken: a correction whose Corrects names no existing entry is accepted
    [check29_correction_dangling_reference_caught] PASS
    
    [check30_closes_on_other_kind_caught] expected failure mode if broken: a type other than terminal or outcome carrying Closes is accepted
    [check30_closes_on_other_kind_caught] PASS
    
    [check31_unknown_terminal_outcome_caught] expected failure mode if broken: a terminal Outcome outside completed, partial, superseded, abandoned is accepted
    [check31_unknown_terminal_outcome_caught] PASS
    
    [check32_partial_requires_deferred] expected failure mode if broken: a partial terminal without a Deferred field is accepted
    [check32_partial_requires_deferred] PASS
    
    [check33_completed_with_deferred_caught] expected failure mode if broken: a completed terminal carrying Deferred is accepted
    [check33_completed_with_deferred_caught] PASS
    
    [check34_merge_requires_backup] expected failure mode if broken: a merge entry that names no backup is accepted
    [check34_merge_requires_backup] PASS
    
    [check35_dispatch_note_requires_dispatch_reference] expected failure mode if broken: a dispatch-note naming neither Dispatch-file nor Dispatch is accepted
    [check35_dispatch_note_requires_dispatch_reference] PASS
    
    [check36_continues_dangling_on_other_kind_caught] expected failure mode if broken: a Continues on a decision naming no existing entry is accepted
    [check36_continues_dangling_on_other_kind_caught] PASS
    
    [check37_every_new_kind_requires_notes] expected failure mode if broken: some new entry type is accepted without its who-wrote-it Notes line
    [check37_every_new_kind_requires_notes] PASS
    
    [check38_link_fields_required] expected failure mode if broken: a finding without Continues, a correction without Corrects, or a merge without Merge-commit is accepted
    [check38_link_fields_required] PASS
    
    PASS: 0 of 38 checks failed

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_terminal_2026_10_16_24

**Timestamp:** 2026-10-17T05:15:55Z

**Expected failure mode:** Expected PASS: 19 entries, preserved=18.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 19
    files under prompts/: preserved=18, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_terminal_2026_10_16_24

**Timestamp:** 2026-10-17T05:15:55Z

**Expected failure mode:** Expected PASS at 45/44/45.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        45
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** render_check_tests_first_2026_10_17_01

**Timestamp:** 2026-10-17T08:13:19Z

**Expected failure mode:** Tests-first, before any rule: exit 1, 7 of 46 fail (39, 41-46), each an AssertionError naming the missing rule; check 40 (one-digit guard) and checks 1-38 pass.

**Command:** python3 check_record.py --render-check

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    check_record.py --render-check
    
    [check1_well_formed_record_passes] expected failure mode if broken: N/A -- positive case, validated by the negative checks below catching sabotages of the same fixture
    [check1_well_formed_record_passes] PASS
    
    [check2_missing_field_names_fault] expected failure mode if broken: an entry missing a required field is accepted, or the error does not name both the entry and the missing field
    [check2_missing_field_names_fault] PASS
    
    [check3_missing_restored_prediction_field_caught] expected failure mode if broken: an intent entry missing the restored 'Prediction (outcome — planner)' field is accepted, or the error does not name it
    [check3_missing_restored_prediction_field_caught] PASS
    
    [check4_closes_resolution_catches_dangling_reference] expected failure mode if broken: a terminal entry's Closes field naming a nonexistent intent ID is accepted silently
    [check4_closes_resolution_catches_dangling_reference] PASS
    
    [check5_duplicate_id_caught] expected failure mode if broken: two entries sharing the same ID are accepted, or the error does not name the colliding ID
    [check5_duplicate_id_caught] PASS
    
    [check6_duplicate_terminal_names_both_closers] expected failure mode if broken: one intent closed by two terminal entries is accepted, or the error does not name both closing entries
    [check6_duplicate_terminal_names_both_closers] PASS
    
    [check7_withheld_sentinel_reported_pending] expected failure mode if broken: a 'withheld' outcome-prediction sentinel is either treated as an error or not surfaced in sentinel_reports as pending
    [check7_withheld_sentinel_reported_pending] PASS
    
    [check8_withheld_sentinel_resolved_by_terminal] expected failure mode if broken: a terminal entry supplying the outcome for an intent whose prediction was legitimately 'withheld' is not recognized as a resolution
    [check8_withheld_sentinel_resolved_by_terminal] PASS
    
    [check9_not_authored_plus_supplied_is_fabrication] expected failure mode if broken: an intent whose outcome prediction is permanently 'not authored' is not flagged when a terminal entry later supplies a value anyway
    [check9_not_authored_plus_supplied_is_fabrication] PASS
    
    [check10_sentinel_forbidden_in_terminal_entry] expected failure mode if broken: a terminal entry carrying a sentinel value in any field is accepted, or the error does not name the field and value
    [check10_sentinel_forbidden_in_terminal_entry] PASS
    
    [check11_working_tree_append_only_catches_modified_line] expected failure mode if broken: modifying an existing, already-committed line in RECORD.md is not caught, or the failure does not name the changed line
    [check11_working_tree_append_only_catches_modified_line] PASS
    
    [check12_working_tree_append_only_vacuous_before_first_commit] expected failure mode if broken: a RECORD.md that exists in the working tree but has never been committed is reported as a violation, or the vacuous case is not flagged as vacuous
    [check12_working_tree_append_only_vacuous_before_first_commit] PASS
    
    [check13_history_walk_real_repo] expected failure mode if broken: a genuinely append-only two-commit history is reported as violating, or the wrong commit count is walked
    [check13_history_walk_real_repo] PASS
    
    [check14_history_walk_vacuous_single_commit] expected failure mode if broken: a RECORD.md history with only one committed version performs a comparison anyway, or is not reported vacuous
    [check14_history_walk_vacuous_single_commit] PASS
    
    [check15_history_walk_catches_removed_line] expected failure mode if broken: a commit that removed an existing line from RECORD.md's history is accepted by the walk
    [check15_history_walk_catches_removed_line] PASS
    
    [check16_merge_commit_stops_the_walk] expected failure mode if broken: a merge commit touching RECORD.md is silently walked (wrong parent guessed) instead of raising MergeCommitEncountered
    [check16_merge_commit_stops_the_walk] PASS
    
    [check17_superseded_by_vacuous_when_none_declared] expected failure mode if broken: a record with no terminal entry declaring Outcome: superseded is not reported vacuous, or is reported as a failure
    [check17_superseded_by_vacuous_when_none_declared] PASS
    
    [check18_superseded_by_catches_dangling_reference] expected failure mode if broken: a terminal entry's Superseded-by field naming a nonexistent intent ID is accepted
    [check18_superseded_by_catches_dangling_reference] PASS
    
    [check19_all_twelve_kinds_accepted] expected failure mode if broken: a record using every RECORDING.md entry type with minimal fields is rejected
    [check19_all_twelve_kinds_accepted] PASS
    
    [check20_unknown_kind_still_rejected] expected failure mode if broken: a kind outside the twelve is accepted (guard: passes before and after the change by design, so it is not evidence for the change)
    [check20_unknown_kind_still_rejected] PASS
    
    [check21_new_kind_missing_notes_named] expected failure mode if broken: an entry of a new type without its Notes line is accepted
    [check21_new_kind_missing_notes_named] PASS
    
    [check22_continuation_missing_continues_named] expected failure mode if broken: a continuation with no Continues field is accepted
    [check22_continuation_missing_continues_named] PASS
    
    [check23_continuation_of_closed_intent_caught] expected failure mode if broken: a continuation naming an intent already closed earlier in the file is accepted
    [check23_continuation_of_closed_intent_caught] PASS
    
    [check24_continuation_of_non_intent_caught] expected failure mode if broken: a continuation naming an entry that is not an intent is accepted
    [check24_continuation_of_non_intent_caught] PASS
    
    [check25_continuation_forbidden_field_caught] expected failure mode if broken: a continuation carrying a closing field (Outcome) is accepted
    [check25_continuation_forbidden_field_caught] PASS
    
    [check26_outcome_with_closes_closes_intent] expected failure mode if broken: an outcome carrying Closes is rejected, or leaves its intent unterminated
    [check26_outcome_with_closes_closes_intent] PASS
    
    [check27_terminal_and_outcome_double_close_caught] expected failure mode if broken: an intent closed by both a terminal and an outcome passes the closed-once check
    [check27_terminal_and_outcome_double_close_caught] PASS
    
    [check28_outcome_needs_continues_or_closes] expected failure mode if broken: an outcome with neither Continues nor Closes is accepted
    [check28_outcome_needs_continues_or_closes] PASS
    
    [check29_correction_dangling_reference_caught] expected failure mode if broken: a correction whose Corrects names no existing entry is accepted
    [check29_correction_dangling_reference_caught] PASS
    
    [check30_closes_on_other_kind_caught] expected failure mode if broken: a type other than terminal or outcome carrying Closes is accepted
    [check30_closes_on_other_kind_caught] PASS
    
    [check31_unknown_terminal_outcome_caught] expected failure mode if broken: a terminal Outcome outside completed, partial, superseded, abandoned is accepted
    [check31_unknown_terminal_outcome_caught] PASS
    
    [check32_partial_requires_deferred] expected failure mode if broken: a partial terminal without a Deferred field is accepted
    [check32_partial_requires_deferred] PASS
    
    [check33_completed_with_deferred_caught] expected failure mode if broken: a completed terminal carrying Deferred is accepted
    [check33_completed_with_deferred_caught] PASS
    
    [check34_merge_requires_backup] expected failure mode if broken: a merge entry that names no backup is accepted
    [check34_merge_requires_backup] PASS
    
    [check35_dispatch_note_requires_dispatch_reference] expected failure mode if broken: a dispatch-note naming neither Dispatch-file nor Dispatch is accepted
    [check35_dispatch_note_requires_dispatch_reference] PASS
    
    [check36_continues_dangling_on_other_kind_caught] expected failure mode if broken: a Continues on a decision naming no existing entry is accepted
    [check36_continues_dangling_on_other_kind_caught] PASS
    
    [check37_every_new_kind_requires_notes] expected failure mode if broken: some new entry type is accepted without its who-wrote-it Notes line
    [check37_every_new_kind_requires_notes] PASS
    
    [check38_link_fields_required] expected failure mode if broken: a finding without Continues, a correction without Corrects, or a merge without Merge-commit is accepted
    [check38_link_fields_required] PASS
    
    [check39_four_digit_id_number_accepted] expected failure mode if broken: an ID like 2026-09-28-1106 (Forager's running sequence) is rejected as malformed
    [check39_four_digit_id_number_accepted] FAIL: AssertionError("a four-digit ID number is rejected: ['intent 2026-09-28-1106: malformed ID (expected YYYY-MM-DD-NN)']")
    
    [check40_one_digit_id_number_still_rejected] expected failure mode if broken: a one-digit ID number is accepted (guard: passes before and after by design)
    [check40_one_digit_id_number_still_rejected] PASS
    
    [check41_monthly_files_read_as_one_record] expected failure mode if broken: records/YYYY-MM.md files are not read, or not read as one record across months
    [check41_monthly_files_read_as_one_record] FAIL: AssertionError('validate_repo does not exist: the monthly-file rule is missing')
    
    [check42_duplicate_id_across_months_caught] expected failure mode if broken: the same ID in two monthly files is accepted
    [check42_duplicate_id_across_months_caught] FAIL: AssertionError('validate_repo does not exist: the monthly-file rule is missing')
    
    [check43_entry_in_wrong_month_caught] expected failure mode if broken: an entry whose Timestamp month differs from its monthly file's month is accepted
    [check43_entry_in_wrong_month_caught] FAIL: AssertionError('validate_repo does not exist: the monthly-file rule is missing')
    
    [check44_monthly_file_append_only_checked] expected failure mode if broken: an edit to a committed line of a monthly file passes the working-tree check
    [check44_monthly_file_append_only_checked] FAIL: AssertionError('append_only_checks does not exist: the monthly-file rule is missing')
    
    [check45_index_record_md_reported_not_checked] expected failure mode if broken: with monthly files and an entry-less RECORD.md, RECORD.md is not reported as the index
    [check45_index_record_md_reported_not_checked] FAIL: AssertionError('append_only_checks does not exist: the monthly-file rule is missing')
    
    [check46_monthly_file_history_walked] expected failure mode if broken: a line removed from a monthly file in a committed change passes the history walk
    [check46_monthly_file_history_walked] FAIL: AssertionError('history_checks does not exist: the monthly-file rule is missing')
    
    FAIL: 7 of 46 checks failed: check39_four_digit_id_number_accepted, check41_monthly_files_read_as_one_record, check42_duplicate_id_across_months_caught, check43_entry_in_wrong_month_caught, check44_monthly_file_append_only_checked, check45_index_record_md_reported_not_checked, check46_monthly_file_history_walked

**Stderr:**

    (nothing captured)

---

**Check:** prompts_render_check_tests_first_2026_10_17_01

**Timestamp:** 2026-10-17T08:13:19Z

**Expected failure mode:** Tests-first: exit 1, p2 fails because a monthly file's claim is unread and its prompt reads as an orphan; p1 passes.

**Command:** python3 check_prompts.py --render-check

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    check_prompts.py --render-check
    
    [p1_single_file_binding_unchanged] expected failure mode if broken: a single RECORD.md claiming its one preserved prompt is reported as a violation
    [p1_single_file_binding_unchanged] PASS
    
    [p2_claims_read_from_monthly_files] expected failure mode if broken: a Dispatch-file claim in records/YYYY-MM.md is not read, so its prompt is reported orphaned
    [p2_claims_read_from_monthly_files] FAIL: AssertionError('a claim in a monthly file was not read; the prompt it claims reads as an orphan: ["prompts/preserved/y.md exists but no RECORD.md entry\'s \'Dispatch-file\' field names it"]')
    
    FAIL: 1 of 2 checks failed: p2_claims_read_from_monthly_files

**Stderr:**

    (nothing captured)

---

**Check:** revert_runs_monthly_checkers_2026_10_17_01

**Timestamp:** 2026-10-17T08:15:11Z

**Expected failure mode:** 8 sabotages on temporary copies of the committed check_record.py and check_prompts.py, each disabling one new rule: each makes its named check fail, every run prints its summary line, and the repository files equal the committed copies at start and end. The monthly-files-read sabotage is expected to fail several monthly checks besides check41.

**Command:** python3 -I /tmp/egd-scripts/revert_runner2.py /home/zynergy-labs/Zynergy/E-GD-Philosophy

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    repo files equal committed copies at start: True
    [id_digits] BITES: expected ['check39_four_digit_id_number_accepted']; failed 1 of 46; others: []
    [month_check] BITES: expected ['check43_entry_in_wrong_month_caught']; failed 1 of 46; others: []
    [monthly_files_read] BITES: expected ['check41_monthly_files_read_as_one_record']; failed 6 of 46; others: ['check42_duplicate_id_across_months_caught', 'check43_entry_in_wrong_month_caught', 'check44_monthly_file_append_only_checked', 'check45_index_record_md_reported_not_checked', 'check46_monthly_file_history_walked']
    [cross_file_record] BITES: expected ['check42_duplicate_id_across_months_caught']; failed 2 of 46; others: ['check41_monthly_files_read_as_one_record']
    [index_reported] BITES: expected ['check45_index_record_md_reported_not_checked']; failed 1 of 46; others: []
    [per_file_append_only] BITES: expected ['check44_monthly_file_append_only_checked']; failed 1 of 46; others: []
    [per_file_history] BITES: expected ['check46_monthly_file_history_walked']; failed 1 of 46; others: []
    [prompts_monthly_claims] BITES: expected ['p2_claims_read_from_monthly_files']; failed 1 of 2; others: []
    repo files equal committed copies at end: True
    sabotages: 8, not biting or not run: 0
    PASS

**Stderr:**

    (nothing captured)

---

**Check:** forager_split_dry_run_2026_10_17_01

**Timestamp:** 2026-10-17T08:15:42Z

**Expected failure mode:** Read-only dry run on a copy of Forager's RECORD.md (records-after-173), split by Timestamp month: no step back a month; per-month counts sum to the total; the months' entries joined equal the original's byte for byte; validate_entries on the single file and validate_repo on the split give the same errors. Expected DRY RUN PASS; the errors themselves are Forager's existing record under E-GD's rules, reported as data.

**Command:** python3 -I /tmp/egd-scripts/dry_split.py /home/zynergy-labs/Zynergy/E-GD-Philosophy /tmp/egd-dry/single /tmp/egd-dry/split

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries 1341; months ['2026-09', '2026-10']; steps back a month: 0
    entries per month: {'2026-09': 511, '2026-10': 830} sum 1341 original 1341
    joined monthly entries equal the original's, byte for byte: True
    single file: 1341 entries validated, 1329 errors, 146 unterminated
    split files: 1341 entries validated, 1329 errors, 146 unterminated
    errors only in the split form: 0 []
    errors only in the single form: 0 []
    duplicate-ID errors: 2 ['duplicate ID 2026-09-28-540: used by entry #709 and entry #710', 'duplicate ID 2026-09-28-542: used by entry #712 and entry #713']
    most common error shapes (single file):
       893  intent <ID>: missing required field '…'
        82  continuation <ID>: Continues '…' names a continuation, not an intent
        80  terminal <ID>: missing required field '…'
        76  terminal <ID>: Closes names no existing intent ID (closes='…')
        47  merge <ID>: missing required field '…'
        46  dispatch-note <ID>: missing required field '…'
    DRY RUN PASS

**Stderr:**

    (nothing captured)

---

**Check:** check_record_terminal_2026_10_17_02

**Timestamp:** 2026-10-17T08:16:40Z

**Expected failure mode:** Expected PASS: 50 entries, none unterminated, single-file mode.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 50
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-07: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-09: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-11: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-15: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-17: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-19: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-21: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-23: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-17-01: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 47 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** check_record_selftest_2026_10_17_02

**Timestamp:** 2026-10-17T08:16:41Z

**Expected failure mode:** Expected PASS: 0 of 46.

**Command:** python3 check_record.py --render-check

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    check_record.py --render-check
    
    [check1_well_formed_record_passes] expected failure mode if broken: N/A -- positive case, validated by the negative checks below catching sabotages of the same fixture
    [check1_well_formed_record_passes] PASS
    
    [check2_missing_field_names_fault] expected failure mode if broken: an entry missing a required field is accepted, or the error does not name both the entry and the missing field
    [check2_missing_field_names_fault] PASS
    
    [check3_missing_restored_prediction_field_caught] expected failure mode if broken: an intent entry missing the restored 'Prediction (outcome — planner)' field is accepted, or the error does not name it
    [check3_missing_restored_prediction_field_caught] PASS
    
    [check4_closes_resolution_catches_dangling_reference] expected failure mode if broken: a terminal entry's Closes field naming a nonexistent intent ID is accepted silently
    [check4_closes_resolution_catches_dangling_reference] PASS
    
    [check5_duplicate_id_caught] expected failure mode if broken: two entries sharing the same ID are accepted, or the error does not name the colliding ID
    [check5_duplicate_id_caught] PASS
    
    [check6_duplicate_terminal_names_both_closers] expected failure mode if broken: one intent closed by two terminal entries is accepted, or the error does not name both closing entries
    [check6_duplicate_terminal_names_both_closers] PASS
    
    [check7_withheld_sentinel_reported_pending] expected failure mode if broken: a 'withheld' outcome-prediction sentinel is either treated as an error or not surfaced in sentinel_reports as pending
    [check7_withheld_sentinel_reported_pending] PASS
    
    [check8_withheld_sentinel_resolved_by_terminal] expected failure mode if broken: a terminal entry supplying the outcome for an intent whose prediction was legitimately 'withheld' is not recognized as a resolution
    [check8_withheld_sentinel_resolved_by_terminal] PASS
    
    [check9_not_authored_plus_supplied_is_fabrication] expected failure mode if broken: an intent whose outcome prediction is permanently 'not authored' is not flagged when a terminal entry later supplies a value anyway
    [check9_not_authored_plus_supplied_is_fabrication] PASS
    
    [check10_sentinel_forbidden_in_terminal_entry] expected failure mode if broken: a terminal entry carrying a sentinel value in any field is accepted, or the error does not name the field and value
    [check10_sentinel_forbidden_in_terminal_entry] PASS
    
    [check11_working_tree_append_only_catches_modified_line] expected failure mode if broken: modifying an existing, already-committed line in RECORD.md is not caught, or the failure does not name the changed line
    [check11_working_tree_append_only_catches_modified_line] PASS
    
    [check12_working_tree_append_only_vacuous_before_first_commit] expected failure mode if broken: a RECORD.md that exists in the working tree but has never been committed is reported as a violation, or the vacuous case is not flagged as vacuous
    [check12_working_tree_append_only_vacuous_before_first_commit] PASS
    
    [check13_history_walk_real_repo] expected failure mode if broken: a genuinely append-only two-commit history is reported as violating, or the wrong commit count is walked
    [check13_history_walk_real_repo] PASS
    
    [check14_history_walk_vacuous_single_commit] expected failure mode if broken: a RECORD.md history with only one committed version performs a comparison anyway, or is not reported vacuous
    [check14_history_walk_vacuous_single_commit] PASS
    
    [check15_history_walk_catches_removed_line] expected failure mode if broken: a commit that removed an existing line from RECORD.md's history is accepted by the walk
    [check15_history_walk_catches_removed_line] PASS
    
    [check16_merge_commit_stops_the_walk] expected failure mode if broken: a merge commit touching RECORD.md is silently walked (wrong parent guessed) instead of raising MergeCommitEncountered
    [check16_merge_commit_stops_the_walk] PASS
    
    [check17_superseded_by_vacuous_when_none_declared] expected failure mode if broken: a record with no terminal entry declaring Outcome: superseded is not reported vacuous, or is reported as a failure
    [check17_superseded_by_vacuous_when_none_declared] PASS
    
    [check18_superseded_by_catches_dangling_reference] expected failure mode if broken: a terminal entry's Superseded-by field naming a nonexistent intent ID is accepted
    [check18_superseded_by_catches_dangling_reference] PASS
    
    [check19_all_twelve_kinds_accepted] expected failure mode if broken: a record using every RECORDING.md entry type with minimal fields is rejected
    [check19_all_twelve_kinds_accepted] PASS
    
    [check20_unknown_kind_still_rejected] expected failure mode if broken: a kind outside the twelve is accepted (guard: passes before and after the change by design, so it is not evidence for the change)
    [check20_unknown_kind_still_rejected] PASS
    
    [check21_new_kind_missing_notes_named] expected failure mode if broken: an entry of a new type without its Notes line is accepted
    [check21_new_kind_missing_notes_named] PASS
    
    [check22_continuation_missing_continues_named] expected failure mode if broken: a continuation with no Continues field is accepted
    [check22_continuation_missing_continues_named] PASS
    
    [check23_continuation_of_closed_intent_caught] expected failure mode if broken: a continuation naming an intent already closed earlier in the file is accepted
    [check23_continuation_of_closed_intent_caught] PASS
    
    [check24_continuation_of_non_intent_caught] expected failure mode if broken: a continuation naming an entry that is not an intent is accepted
    [check24_continuation_of_non_intent_caught] PASS
    
    [check25_continuation_forbidden_field_caught] expected failure mode if broken: a continuation carrying a closing field (Outcome) is accepted
    [check25_continuation_forbidden_field_caught] PASS
    
    [check26_outcome_with_closes_closes_intent] expected failure mode if broken: an outcome carrying Closes is rejected, or leaves its intent unterminated
    [check26_outcome_with_closes_closes_intent] PASS
    
    [check27_terminal_and_outcome_double_close_caught] expected failure mode if broken: an intent closed by both a terminal and an outcome passes the closed-once check
    [check27_terminal_and_outcome_double_close_caught] PASS
    
    [check28_outcome_needs_continues_or_closes] expected failure mode if broken: an outcome with neither Continues nor Closes is accepted
    [check28_outcome_needs_continues_or_closes] PASS
    
    [check29_correction_dangling_reference_caught] expected failure mode if broken: a correction whose Corrects names no existing entry is accepted
    [check29_correction_dangling_reference_caught] PASS
    
    [check30_closes_on_other_kind_caught] expected failure mode if broken: a type other than terminal or outcome carrying Closes is accepted
    [check30_closes_on_other_kind_caught] PASS
    
    [check31_unknown_terminal_outcome_caught] expected failure mode if broken: a terminal Outcome outside completed, partial, superseded, abandoned is accepted
    [check31_unknown_terminal_outcome_caught] PASS
    
    [check32_partial_requires_deferred] expected failure mode if broken: a partial terminal without a Deferred field is accepted
    [check32_partial_requires_deferred] PASS
    
    [check33_completed_with_deferred_caught] expected failure mode if broken: a completed terminal carrying Deferred is accepted
    [check33_completed_with_deferred_caught] PASS
    
    [check34_merge_requires_backup] expected failure mode if broken: a merge entry that names no backup is accepted
    [check34_merge_requires_backup] PASS
    
    [check35_dispatch_note_requires_dispatch_reference] expected failure mode if broken: a dispatch-note naming neither Dispatch-file nor Dispatch is accepted
    [check35_dispatch_note_requires_dispatch_reference] PASS
    
    [check36_continues_dangling_on_other_kind_caught] expected failure mode if broken: a Continues on a decision naming no existing entry is accepted
    [check36_continues_dangling_on_other_kind_caught] PASS
    
    [check37_every_new_kind_requires_notes] expected failure mode if broken: some new entry type is accepted without its who-wrote-it Notes line
    [check37_every_new_kind_requires_notes] PASS
    
    [check38_link_fields_required] expected failure mode if broken: a finding without Continues, a correction without Corrects, or a merge without Merge-commit is accepted
    [check38_link_fields_required] PASS
    
    [check39_four_digit_id_number_accepted] expected failure mode if broken: an ID like 2026-09-28-1106 (Forager's running sequence) is rejected as malformed
    [check39_four_digit_id_number_accepted] PASS
    
    [check40_one_digit_id_number_still_rejected] expected failure mode if broken: a one-digit ID number is accepted (guard: passes before and after by design)
    [check40_one_digit_id_number_still_rejected] PASS
    
    [check41_monthly_files_read_as_one_record] expected failure mode if broken: records/YYYY-MM.md files are not read, or not read as one record across months
    [check41_monthly_files_read_as_one_record] PASS
    
    [check42_duplicate_id_across_months_caught] expected failure mode if broken: the same ID in two monthly files is accepted
    [check42_duplicate_id_across_months_caught] PASS
    
    [check43_entry_in_wrong_month_caught] expected failure mode if broken: an entry whose Timestamp month differs from its monthly file's month is accepted
    [check43_entry_in_wrong_month_caught] PASS
    
    [check44_monthly_file_append_only_checked] expected failure mode if broken: an edit to a committed line of a monthly file passes the working-tree check
    [check44_monthly_file_append_only_checked] PASS
    
    [check45_index_record_md_reported_not_checked] expected failure mode if broken: with monthly files and an entry-less RECORD.md, RECORD.md is not reported as the index
    [check45_index_record_md_reported_not_checked] PASS
    
    [check46_monthly_file_history_walked] expected failure mode if broken: a line removed from a monthly file in a committed change passes the history walk
    [check46_monthly_file_history_walked] PASS
    
    PASS: 0 of 46 checks failed

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_selftest_2026_10_17_02

**Timestamp:** 2026-10-17T08:16:41Z

**Expected failure mode:** Expected PASS: 0 of 2.

**Command:** python3 check_prompts.py --render-check

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    check_prompts.py --render-check
    
    [p1_single_file_binding_unchanged] expected failure mode if broken: a single RECORD.md claiming its one preserved prompt is reported as a violation
    [p1_single_file_binding_unchanged] PASS
    
    [p2_claims_read_from_monthly_files] expected failure mode if broken: a Dispatch-file claim in records/YYYY-MM.md is not read, so its prompt is reported orphaned
    [p2_claims_read_from_monthly_files] PASS
    
    PASS: 0 of 2 checks failed

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_terminal_2026_10_17_02

**Timestamp:** 2026-10-17T08:16:41Z

**Expected failure mode:** Expected PASS: 20 entries, preserved=19.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 20
    files under prompts/: preserved=19, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_terminal_2026_10_17_02

**Timestamp:** 2026-10-17T08:16:42Z

**Expected failure mode:** Expected PASS at 45/44/45.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        45
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

---

**Check:** records_lookup_tests_first_2026_10_17_03

**Timestamp:** 2026-10-17T08:19:45Z

**Expected failure mode:** Tests-first against a stub main() that prints nothing: exit 1, 7 of 7 fail, each an AssertionError naming the missing behaviour (no citation, no links, no hits, no open list, no next-id, no forecast citation, no NOT READ report). A first run had r3 fail with a TypeError from a fixture bug; repaired before this registered run.

**Command:** python3 records_lookup.py --render-check

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    records_lookup.py --render-check
    
    [r1_show_verbatim_with_citation] expected failure mode if broken: show does not print the entry verbatim under a citation that git show confirms
    [r1_show_verbatim_with_citation] FAIL: AssertionError("show printed no citation line: ''")
    
    [r2_links_each_type] expected failure mode if broken: links misses a Continues, Closes, Corrects or Supersedes link, or what an entry names
    [r2_links_each_type] FAIL: AssertionError("links does not list the Continues link from -02 with a citation: ''")
    
    [r3_search_seven_sources_newest_first] expected failure mode if broken: search misses a source, reads the session log's prose, is not newest first, or shows no Supersedes link
    [r3_search_seven_sources_newest_first] FAIL: AssertionError("search found no hit in forager record: ''")
    
    [r4_open_intents] expected failure mode if broken: open lists a closed intent (by terminal, or by outcome with Closes) or misses an open one
    [r4_open_intents] FAIL: AssertionError("open listed []: ''")
    
    [r5_next_id_across_months_with_duplicates] expected failure mode if broken: next-id reads only the current month, omits the commit read, or misses a duplicate
    [r5_next_id_across_months_with_duplicates] FAIL: AssertionError("next-id did not read every month or name its commit: ''")
    
    [r6_cross_repository_reference_resolves] expected failure mode if broken: a forecast decision's 'Forager RECORD -NN' is not resolved to the Forager entry, cited
    [r6_cross_repository_reference_resolves] FAIL: AssertionError("show D200 printed no forecast citation: ''")
    
    [r7_unread_source_reported] expected failure mode if broken: a source whose ref cannot be read is skipped silently instead of reported
    [r7_unread_source_reported] FAIL: AssertionError("an unreadable source was not reported: ''")
    
    FAIL: 7 of 7 checks failed: r1_show_verbatim_with_citation, r2_links_each_type, r3_search_seven_sources_newest_first, r4_open_intents, r5_next_id_across_months_with_duplicates, r6_cross_repository_reference_resolves, r7_unread_source_reported

**Stderr:**

    (nothing captured)

---

**Check:** revert_runs_records_lookup_2026_10_17_03

**Timestamp:** 2026-10-17T08:22:09Z

**Expected failure mode:** 14 sabotages on temporary copies of the committed records_lookup.py, one per requirement behaviour (four for R2's link types, four for R3): each makes its requirement's check fail, every run prints its summary line, and the repository files equal the committed copies at start and end.

**Command:** python3 -I /tmp/egd-scripts/revert_runner3.py /home/zynergy-labs/Zynergy/E-GD-Philosophy

**Exit code:** 1

**Vacuous:** no

**Stdout:**

    repo files equal committed copies at start: True
    [r1_verbatim] BITES: expected ['r1_show_verbatim_with_citation']; failed 1 of 7; others: []
    [r2_continues] BITES: expected ['r2_links_each_type']; failed 1 of 7; others: []
    [r2_closes] BITES: expected ['r2_links_each_type']; failed 1 of 7; others: []
    [r2_corrects] BITES: expected ['r2_links_each_type']; failed 1 of 7; others: []
    [r2_supersedes] BITES: expected ['r2_links_each_type']; failed 2 of 7; others: ['r3_search_seven_sources_newest_first']
    [r3_log_only] DOES NOT BITE: expected ['r3_search_seven_sources_newest_first']; failed 0 of 7; others: []
    [r3_newest_first] BITES: expected ['r3_search_seven_sources_newest_first']; failed 1 of 7; others: []
    [r3_supersede_beside] BITES: expected ['r3_search_seven_sources_newest_first']; failed 1 of 7; others: []
    [r3_prompts_source] BITES: expected ['r3_search_seven_sources_newest_first']; failed 1 of 7; others: []
    [r4_outcome_closes] BITES: expected ['r4_open_intents']; failed 1 of 7; others: []
    [r5_months] BITES: expected ['r5_next_id_across_months_with_duplicates']; failed 1 of 7; others: []
    [r5_duplicates] BITES: expected ['r5_next_id_across_months_with_duplicates']; failed 1 of 7; others: []
    [r6_forager_refs] BITES: expected ['r6_cross_repository_reference_resolves']; failed 1 of 7; others: []
    [r7_not_read] BITES: expected ['r7_unread_source_reported']; failed 1 of 7; others: []
    repo files equal committed copies at end: True
    sabotages: 14, not biting or not run: 1
    FAIL

**Stderr:**

    (nothing captured)

---

**Check:** revert_runs_records_lookup_rerun_2026_10_17_03

**Timestamp:** 2026-10-17T08:22:38Z

**Expected failure mode:** Re-run after repairing r3's fixture: 14 sabotages, each biting its requirement's check, including r3_log_only, which did not bite in the first run; repository files unchanged.

**Command:** python3 -I /tmp/egd-scripts/revert_runner3.py /home/zynergy-labs/Zynergy/E-GD-Philosophy

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    repo files equal committed copies at start: True
    [r1_verbatim] BITES: expected ['r1_show_verbatim_with_citation']; failed 1 of 7; others: []
    [r2_continues] BITES: expected ['r2_links_each_type']; failed 1 of 7; others: []
    [r2_closes] BITES: expected ['r2_links_each_type']; failed 1 of 7; others: []
    [r2_corrects] BITES: expected ['r2_links_each_type']; failed 1 of 7; others: []
    [r2_supersedes] BITES: expected ['r2_links_each_type']; failed 2 of 7; others: ['r3_search_seven_sources_newest_first']
    [r3_log_only] BITES: expected ['r3_search_seven_sources_newest_first']; failed 1 of 7; others: []
    [r3_newest_first] BITES: expected ['r3_search_seven_sources_newest_first']; failed 1 of 7; others: []
    [r3_supersede_beside] BITES: expected ['r3_search_seven_sources_newest_first']; failed 1 of 7; others: []
    [r3_prompts_source] BITES: expected ['r3_search_seven_sources_newest_first']; failed 1 of 7; others: []
    [r4_outcome_closes] BITES: expected ['r4_open_intents']; failed 1 of 7; others: []
    [r5_months] BITES: expected ['r5_next_id_across_months_with_duplicates']; failed 1 of 7; others: []
    [r5_duplicates] BITES: expected ['r5_next_id_across_months_with_duplicates']; failed 1 of 7; others: []
    [r6_forager_refs] BITES: expected ['r6_cross_repository_reference_resolves']; failed 1 of 7; others: []
    [r7_not_read] BITES: expected ['r7_unread_source_reported']; failed 1 of 7; others: []
    repo files equal committed copies at end: True
    sabotages: 14, not biting or not run: 0
    PASS

**Stderr:**

    (nothing captured)

---

**Check:** records_lookup_real_show_links_2026_10_17_03

**Timestamp:** 2026-10-17T08:23:54Z

**Expected failure mode:** On Forager's origin/records-after-173 (after fetch), show for -1142, -1104, -385, -544, -1106 prints each entry verbatim under a citation whose lines equal git show at that commit; links lists each entry's links. Expected PASS.

**Command:** python3 -I /tmp/egd-scripts/real_show_check.py /home/zynergy-labs/Zynergy/E-GD-Philosophy /home/zynergy-labs/Zynergy/Forager /home/zynergy-labs/Zynergy/forager-forecast -1142 -1104 -385 -544 -1106

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    -1142: **ID:** 2026-09-28-1142 at RECORD.md:19463-19470 — show matches git show: True; links: named by 0, names 1; forecast rows citing it: 0
    -1104: **ID:** 2026-09-28-1104 at RECORD.md:18861-18876 — show matches git show: True; links: named by 2, names 2; forecast rows citing it: 0
    -385: **ID:** 2026-09-28-385 at RECORD.md:9912-9922 — show matches git show: True; links: named by 0, names 1; forecast rows citing it: 0
    -544: **ID:** 2026-09-28-544 at RECORD.md:12008-12017 — show matches git show: True; links: named by 2, names 0; forecast rows citing it: 0
    -1106: **ID:** 2026-09-28-1106 at RECORD.md:18893-18917 — show matches git show: True; links: named by 1, names 2; forecast rows citing it: 0
    PASS

**Stderr:**

    (nothing captured)

---

**Check:** revert_runs_records_lookup_final_2026_10_17_03

**Timestamp:** 2026-10-17T08:24:45Z

**Expected failure mode:** 15 sabotages on temporary copies of the committed records_lookup.py, including the unread-record rule added after the real-data run: each bites its requirement's check; repository files unchanged.

**Command:** python3 -I /tmp/egd-scripts/revert_runner3.py /home/zynergy-labs/Zynergy/E-GD-Philosophy

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    repo files equal committed copies at start: True
    [r1_verbatim] BITES: expected ['r1_show_verbatim_with_citation']; failed 1 of 7; others: []
    [r2_continues] BITES: expected ['r2_links_each_type']; failed 1 of 7; others: []
    [r2_closes] BITES: expected ['r2_links_each_type']; failed 1 of 7; others: []
    [r2_corrects] BITES: expected ['r2_links_each_type']; failed 1 of 7; others: []
    [r2_supersedes] BITES: expected ['r2_links_each_type']; failed 2 of 7; others: ['r3_search_seven_sources_newest_first']
    [r3_log_only] BITES: expected ['r3_search_seven_sources_newest_first']; failed 1 of 7; others: []
    [r3_newest_first] BITES: expected ['r3_search_seven_sources_newest_first']; failed 1 of 7; others: []
    [r3_supersede_beside] BITES: expected ['r3_search_seven_sources_newest_first']; failed 1 of 7; others: []
    [r3_prompts_source] BITES: expected ['r3_search_seven_sources_newest_first']; failed 1 of 7; others: []
    [r4_outcome_closes] BITES: expected ['r4_open_intents']; failed 1 of 7; others: []
    [r5_months] BITES: expected ['r5_next_id_across_months_with_duplicates']; failed 1 of 7; others: []
    [r5_duplicates] BITES: expected ['r5_next_id_across_months_with_duplicates']; failed 1 of 7; others: []
    [r6_forager_refs] BITES: expected ['r6_cross_repository_reference_resolves']; failed 1 of 7; others: []
    [r7_unknown_not_zero] BITES: expected ['r7_unread_source_reported']; failed 1 of 7; others: []
    [r7_not_read] BITES: expected ['r7_unread_source_reported']; failed 1 of 7; others: []
    repo files equal committed copies at end: True
    sabotages: 15, not biting or not run: 0
    PASS

**Stderr:**

    (nothing captured)

---

**Check:** check_record_terminal_2026_10_17_04

**Timestamp:** 2026-10-17T08:25:09Z

**Expected failure mode:** Expected PASS: 52 entries, none unterminated.

**Command:** python3 check_record.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    entries: 52
    intent entries with prediction sentinels (reported, not a failure):
      2026-08-13-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-13-09: Prediction (outcome — planner) = 'withheld' (pending)
      2026-08-13-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-14-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-08-15-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-03: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-05: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-07: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-09: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-11: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-13: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-15: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-17: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-19: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-21: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-16-23: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-17-01: Prediction (outcome — planner) = 'not authored' (pending)
      2026-10-17-03: Prediction (outcome — planner) = 'not authored' (pending)
    
    [working-tree check -- covers changes since the last commit only] PASS: current file starts with HEAD's content unchanged
    [history walk -- covers every committed transition in RECORD.md's history] PASS: 49 commit(s) checked, each a byte-prefix extension of the one before it
    [Superseded-by cross-reference -- covers terminal entries declaring Outcome: superseded] PASS (vacuous: no entry declares Outcome: superseded)
    [duplicate-terminal check -- every intent closed by more than one terminal entry] PASS
    
    PASS: entries structurally valid; working-tree check, history walk, and Superseded-by cross-reference all clean

**Stderr:**

    (nothing captured)

---

**Check:** records_lookup_selftest_2026_10_17_04

**Timestamp:** 2026-10-17T08:25:10Z

**Expected failure mode:** Expected PASS: 0 of 7.

**Command:** python3 records_lookup.py --render-check

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    records_lookup.py --render-check
    
    [r1_show_verbatim_with_citation] expected failure mode if broken: show does not print the entry verbatim under a citation that git show confirms
    [r1_show_verbatim_with_citation] PASS
    
    [r2_links_each_type] expected failure mode if broken: links misses a Continues, Closes, Corrects or Supersedes link, or what an entry names
    [r2_links_each_type] PASS
    
    [r3_search_seven_sources_newest_first] expected failure mode if broken: search misses a source, reads the session log's prose, is not newest first, or shows no Supersedes link
    [r3_search_seven_sources_newest_first] PASS
    
    [r4_open_intents] expected failure mode if broken: open lists a closed intent (by terminal, or by outcome with Closes) or misses an open one
    [r4_open_intents] PASS
    
    [r5_next_id_across_months_with_duplicates] expected failure mode if broken: next-id reads only the current month, omits the commit read, or misses a duplicate
    [r5_next_id_across_months_with_duplicates] PASS
    
    [r6_cross_repository_reference_resolves] expected failure mode if broken: a forecast decision's 'Forager RECORD -NN' is not resolved to the Forager entry, cited
    [r6_cross_repository_reference_resolves] PASS
    
    [r7_unread_source_reported] expected failure mode if broken: a source whose ref cannot be read is skipped silently instead of reported
    [r7_unread_source_reported] PASS
    
    PASS: 0 of 7 checks failed

**Stderr:**

    (nothing captured)

---

**Check:** check_record_selftest_2026_10_17_04

**Timestamp:** 2026-10-17T08:25:10Z

**Expected failure mode:** Expected PASS: 0 of 46.

**Command:** python3 check_record.py --render-check

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    check_record.py --render-check
    
    [check1_well_formed_record_passes] expected failure mode if broken: N/A -- positive case, validated by the negative checks below catching sabotages of the same fixture
    [check1_well_formed_record_passes] PASS
    
    [check2_missing_field_names_fault] expected failure mode if broken: an entry missing a required field is accepted, or the error does not name both the entry and the missing field
    [check2_missing_field_names_fault] PASS
    
    [check3_missing_restored_prediction_field_caught] expected failure mode if broken: an intent entry missing the restored 'Prediction (outcome — planner)' field is accepted, or the error does not name it
    [check3_missing_restored_prediction_field_caught] PASS
    
    [check4_closes_resolution_catches_dangling_reference] expected failure mode if broken: a terminal entry's Closes field naming a nonexistent intent ID is accepted silently
    [check4_closes_resolution_catches_dangling_reference] PASS
    
    [check5_duplicate_id_caught] expected failure mode if broken: two entries sharing the same ID are accepted, or the error does not name the colliding ID
    [check5_duplicate_id_caught] PASS
    
    [check6_duplicate_terminal_names_both_closers] expected failure mode if broken: one intent closed by two terminal entries is accepted, or the error does not name both closing entries
    [check6_duplicate_terminal_names_both_closers] PASS
    
    [check7_withheld_sentinel_reported_pending] expected failure mode if broken: a 'withheld' outcome-prediction sentinel is either treated as an error or not surfaced in sentinel_reports as pending
    [check7_withheld_sentinel_reported_pending] PASS
    
    [check8_withheld_sentinel_resolved_by_terminal] expected failure mode if broken: a terminal entry supplying the outcome for an intent whose prediction was legitimately 'withheld' is not recognized as a resolution
    [check8_withheld_sentinel_resolved_by_terminal] PASS
    
    [check9_not_authored_plus_supplied_is_fabrication] expected failure mode if broken: an intent whose outcome prediction is permanently 'not authored' is not flagged when a terminal entry later supplies a value anyway
    [check9_not_authored_plus_supplied_is_fabrication] PASS
    
    [check10_sentinel_forbidden_in_terminal_entry] expected failure mode if broken: a terminal entry carrying a sentinel value in any field is accepted, or the error does not name the field and value
    [check10_sentinel_forbidden_in_terminal_entry] PASS
    
    [check11_working_tree_append_only_catches_modified_line] expected failure mode if broken: modifying an existing, already-committed line in RECORD.md is not caught, or the failure does not name the changed line
    [check11_working_tree_append_only_catches_modified_line] PASS
    
    [check12_working_tree_append_only_vacuous_before_first_commit] expected failure mode if broken: a RECORD.md that exists in the working tree but has never been committed is reported as a violation, or the vacuous case is not flagged as vacuous
    [check12_working_tree_append_only_vacuous_before_first_commit] PASS
    
    [check13_history_walk_real_repo] expected failure mode if broken: a genuinely append-only two-commit history is reported as violating, or the wrong commit count is walked
    [check13_history_walk_real_repo] PASS
    
    [check14_history_walk_vacuous_single_commit] expected failure mode if broken: a RECORD.md history with only one committed version performs a comparison anyway, or is not reported vacuous
    [check14_history_walk_vacuous_single_commit] PASS
    
    [check15_history_walk_catches_removed_line] expected failure mode if broken: a commit that removed an existing line from RECORD.md's history is accepted by the walk
    [check15_history_walk_catches_removed_line] PASS
    
    [check16_merge_commit_stops_the_walk] expected failure mode if broken: a merge commit touching RECORD.md is silently walked (wrong parent guessed) instead of raising MergeCommitEncountered
    [check16_merge_commit_stops_the_walk] PASS
    
    [check17_superseded_by_vacuous_when_none_declared] expected failure mode if broken: a record with no terminal entry declaring Outcome: superseded is not reported vacuous, or is reported as a failure
    [check17_superseded_by_vacuous_when_none_declared] PASS
    
    [check18_superseded_by_catches_dangling_reference] expected failure mode if broken: a terminal entry's Superseded-by field naming a nonexistent intent ID is accepted
    [check18_superseded_by_catches_dangling_reference] PASS
    
    [check19_all_twelve_kinds_accepted] expected failure mode if broken: a record using every RECORDING.md entry type with minimal fields is rejected
    [check19_all_twelve_kinds_accepted] PASS
    
    [check20_unknown_kind_still_rejected] expected failure mode if broken: a kind outside the twelve is accepted (guard: passes before and after the change by design, so it is not evidence for the change)
    [check20_unknown_kind_still_rejected] PASS
    
    [check21_new_kind_missing_notes_named] expected failure mode if broken: an entry of a new type without its Notes line is accepted
    [check21_new_kind_missing_notes_named] PASS
    
    [check22_continuation_missing_continues_named] expected failure mode if broken: a continuation with no Continues field is accepted
    [check22_continuation_missing_continues_named] PASS
    
    [check23_continuation_of_closed_intent_caught] expected failure mode if broken: a continuation naming an intent already closed earlier in the file is accepted
    [check23_continuation_of_closed_intent_caught] PASS
    
    [check24_continuation_of_non_intent_caught] expected failure mode if broken: a continuation naming an entry that is not an intent is accepted
    [check24_continuation_of_non_intent_caught] PASS
    
    [check25_continuation_forbidden_field_caught] expected failure mode if broken: a continuation carrying a closing field (Outcome) is accepted
    [check25_continuation_forbidden_field_caught] PASS
    
    [check26_outcome_with_closes_closes_intent] expected failure mode if broken: an outcome carrying Closes is rejected, or leaves its intent unterminated
    [check26_outcome_with_closes_closes_intent] PASS
    
    [check27_terminal_and_outcome_double_close_caught] expected failure mode if broken: an intent closed by both a terminal and an outcome passes the closed-once check
    [check27_terminal_and_outcome_double_close_caught] PASS
    
    [check28_outcome_needs_continues_or_closes] expected failure mode if broken: an outcome with neither Continues nor Closes is accepted
    [check28_outcome_needs_continues_or_closes] PASS
    
    [check29_correction_dangling_reference_caught] expected failure mode if broken: a correction whose Corrects names no existing entry is accepted
    [check29_correction_dangling_reference_caught] PASS
    
    [check30_closes_on_other_kind_caught] expected failure mode if broken: a type other than terminal or outcome carrying Closes is accepted
    [check30_closes_on_other_kind_caught] PASS
    
    [check31_unknown_terminal_outcome_caught] expected failure mode if broken: a terminal Outcome outside completed, partial, superseded, abandoned is accepted
    [check31_unknown_terminal_outcome_caught] PASS
    
    [check32_partial_requires_deferred] expected failure mode if broken: a partial terminal without a Deferred field is accepted
    [check32_partial_requires_deferred] PASS
    
    [check33_completed_with_deferred_caught] expected failure mode if broken: a completed terminal carrying Deferred is accepted
    [check33_completed_with_deferred_caught] PASS
    
    [check34_merge_requires_backup] expected failure mode if broken: a merge entry that names no backup is accepted
    [check34_merge_requires_backup] PASS
    
    [check35_dispatch_note_requires_dispatch_reference] expected failure mode if broken: a dispatch-note naming neither Dispatch-file nor Dispatch is accepted
    [check35_dispatch_note_requires_dispatch_reference] PASS
    
    [check36_continues_dangling_on_other_kind_caught] expected failure mode if broken: a Continues on a decision naming no existing entry is accepted
    [check36_continues_dangling_on_other_kind_caught] PASS
    
    [check37_every_new_kind_requires_notes] expected failure mode if broken: some new entry type is accepted without its who-wrote-it Notes line
    [check37_every_new_kind_requires_notes] PASS
    
    [check38_link_fields_required] expected failure mode if broken: a finding without Continues, a correction without Corrects, or a merge without Merge-commit is accepted
    [check38_link_fields_required] PASS
    
    [check39_four_digit_id_number_accepted] expected failure mode if broken: an ID like 2026-09-28-1106 (Forager's running sequence) is rejected as malformed
    [check39_four_digit_id_number_accepted] PASS
    
    [check40_one_digit_id_number_still_rejected] expected failure mode if broken: a one-digit ID number is accepted (guard: passes before and after by design)
    [check40_one_digit_id_number_still_rejected] PASS
    
    [check41_monthly_files_read_as_one_record] expected failure mode if broken: records/YYYY-MM.md files are not read, or not read as one record across months
    [check41_monthly_files_read_as_one_record] PASS
    
    [check42_duplicate_id_across_months_caught] expected failure mode if broken: the same ID in two monthly files is accepted
    [check42_duplicate_id_across_months_caught] PASS
    
    [check43_entry_in_wrong_month_caught] expected failure mode if broken: an entry whose Timestamp month differs from its monthly file's month is accepted
    [check43_entry_in_wrong_month_caught] PASS
    
    [check44_monthly_file_append_only_checked] expected failure mode if broken: an edit to a committed line of a monthly file passes the working-tree check
    [check44_monthly_file_append_only_checked] PASS
    
    [check45_index_record_md_reported_not_checked] expected failure mode if broken: with monthly files and an entry-less RECORD.md, RECORD.md is not reported as the index
    [check45_index_record_md_reported_not_checked] PASS
    
    [check46_monthly_file_history_walked] expected failure mode if broken: a line removed from a monthly file in a committed change passes the history walk
    [check46_monthly_file_history_walked] PASS
    
    PASS: 0 of 46 checks failed

**Stderr:**

    (nothing captured)

---

**Check:** check_prompts_2026_10_17_04

**Timestamp:** 2026-10-17T08:25:10Z

**Expected failure mode:** Expected PASS: 20 entries, preserved=19; self-tests 0 of 2.

**Command:** python3 check_prompts.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    dispatch-recording entries found: 20
    files under prompts/: preserved=19, recovered=0
    
    PASS: every dispatch-recording entry's 'Dispatch-file' resolves to a real file, every file under prompts/ is claimed by exactly one entry (or by an intent/terminal pair closing it), no orphans in either direction. This checks existence and binding only -- it does not and cannot verify stored text matches what was actually dispatched.

**Stderr:**

    (nothing captured)

---

**Check:** check_glossary_2026_10_17_04

**Timestamp:** 2026-10-17T08:25:11Z

**Expected failure mode:** Expected PASS at 45/44/45.

**Command:** python3 check_glossary.py

**Exit code:** 0

**Vacuous:** no

**Stdout:**

    philosophy headwords: 45
    enforcement entries:  44
    glossary rows:        45
    
    PASS: bidirectional contract holds, sections aligned

**Stderr:**

    (nothing captured)

