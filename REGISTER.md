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

