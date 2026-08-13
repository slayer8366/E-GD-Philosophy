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

