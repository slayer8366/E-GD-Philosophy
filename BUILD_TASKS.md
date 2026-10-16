# Build Tasks: Intent Records

Status, 2026-10-16: Task 2 was built as check_register.py (RECORD.md 2026-08-13-03/-04), departing from this record where that entry says. Task 1 was never built; check_prompts.py (RECORD.md 2026-08-13-09/-10) checks a different property. The text below is kept as written.

Two tooling tasks for the EGD trial branch, written as intent records per Intent-Driven Engineering. Each is ready to become a coder prompt once the operator approves. Neither has been started; both records await their first entry in the record store when work begins.

---

## Task 1: Prompt structure hook (check_prompt.py)

**Change:** A standalone script that validates a coder prompt file against the Complete Task Prompts element list and the active intent record.

**Scope boundary:** Structural validation only. The script checks presence and consistency of: role assignment, scope boundary, closed decisions section (present, not empty), prediction, finish line, required checks, out-of-scope list, and in-flight work list when a parallel flag is set. It cross-checks the prediction and finish line against the referenced intent record for verbatim consistency. Out of scope: any judgment of whether the closed decisions are the right ones or complete. The script's output states this limit in its own header on every run.

**Closed decisions bearing on this task:**
- The hook automates the coder's structural check; it does not and cannot detect a missing decision (Complete Task Prompts).
- Its output must never be described as "prompt verified," only "structure validated" (Truthful Interface Contracts).
- Failure lists missing elements by name and exits nonzero; it fills nothing in.

**Prediction:** Given a prompt file missing its out-of-scope list, the script exits nonzero naming that element. Given a complete prompt whose prediction text differs from the intent record's, it exits nonzero naming the inconsistency. Given a complete, consistent prompt, it exits zero with the limit statement in its output.

**Finish line:** All three predicted behaviors observed, each check written and seen failing before the behavior existed. Script lives beside check_glossary.py in the boundary-check suite.

**Abort conditions:** If prompt format cannot be settled in one exchange with the operator (the script needs a defined prompt file format, which does not exist yet and is an operator decision), stop and surface rather than inventing one.

---

## Task 2: Prediction capture wrapper (check_register.py)

**Change:** A runner wrapper that executes a check and records the predicted failure mode alongside the actual captured output in the check register, appending one entry per observation.

**Scope boundary:** Capture and record only. The wrapper takes a check command and a stated expected-failure description, runs the command, and appends to the register: check name, date, expected failure text, actual exit code, and captured stdout/stderr. Out of scope: any comparison logic, any pass/fail judgment about whether the observed failure matches the prediction, and any blocking of subsequent actions. The comparison remains the agent's judgment per Confirm Failure Before Applying Fixes; this tool makes that judgment auditable, not automatic.

**Closed decisions bearing on this task:**
- No mechanical matching of failure output against predictions; pattern-matching gates produce false blocks and teach vague predictions (adjudicated this session).
- The register is append-only under Immutable Append-Only History; the wrapper appends and never rewrites.
- Register format: one entry per observation, plain text, greppable by check name.

**Prediction:** After wrapping a deliberately failing check, the register contains one new entry pairing the stated expectation with the actual captured output, and re-running appends a second entry rather than modifying the first.

**Finish line:** Predicted behavior observed; append-only property confirmed by diff across two runs; wrapper documented in the register file's header. Lives beside check_glossary.py.

**Abort conditions:** If capturing output requires interfering with how the check itself runs (environment changes, output redirection that alters behavior), stop and surface. The wrapper must be observationally inert with respect to the check's own result.

---

Both tasks are additive (new scripts, no existing paths modified), both produce their own checks failing-first, and neither touches the document set. Terminal entries for these records go in the record store when the work completes, is superseded, or is abandoned.
