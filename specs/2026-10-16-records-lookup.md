# Spec: records lookup tool

**Read against:**

- E-GD `Test-1` at `6ceefbf`.
- Forager `origin/records-after-173` at `efef0e46` and `origin/pre-main` at `462bb8ba`.
- forager-forecast `origin/main` at `b9127e5`.

Read 2026-10-16. Rulings: `prompts/preserved/2026-10-16-11.md`, `-13`, `-15`, `-17`. Approved 2026-10-16.

## Goal

"Check from source" becomes one command: each lookup returns the text, its links, and its citation (repository, ref, commit, file, line).

## Scope

- Reads these sources, and writes nothing:
  - Forager: `RECORD.md`, or the monthly `records/` files it indexes once split; `docs/audits/README.md`; `prompts/preserved/`;
  - forager-forecast: `docs/planning/DECISIONS.md`, `docs/audits/README.md`, `docs/dispatch/`, and the session-log table in `docs/planning/START_HERE.md`.
- Reads each source from a named ref after `git fetch`, with no checkout.
- Commands: `show`, `links`, `search`, `open`, `next-id`.

## Out of scope

- Writing, reserving or editing anything, IDs included.
- One file per entry (option B), or a hosted service (option C).
- E-GD's own record (outside the operator's scope).
- Judging what an entry means: it returns text and links.

## Decisions

- The markdown in git stays the source of truth (option A).
- Every answer carries its citation. An answer without one is a defect.
- **Per-source default refs,** because no Forager branch holds every source at its newest:
  - `RECORD.md` and the preserved prompts from `records-after-173` (1,287 entries and 385 prompts, against 735 and 295 elsewhere);
  - the audit index from `pre-main` (356 rows, against 280).
  - Each can be overridden per run.
- Standard library only.
- **Lives in E-GD,** one copy run against each repository (operator, 2026-10-16).
- **`next-id` only reports;** it reserves nothing (operator, 2026-10-16).
- **The forecast session log** is a source; the maintained prose above it, which decays, is not (operator, 2026-10-16).

## Requirements

- **R1. `show <ID>`** prints the entry verbatim with its citation. *Check:* the output equals `git show <ref>:<file>` at the cited lines.
- **R2. `links <ID>`** lists the entries naming it in `Continues`, `Closes`, `Corrects` or `Supersedes`, and the entries it names, each with a citation. *Check:* a fixture with one link of each type; a revert of each link type fails its test.
- **R3. `search <words>`** searches all seven sources, newest first, each hit cited, with any explicit `Supersedes` or `Corrects` link beside it. *Check:* a fixture term in each source is found in each.
- **R4. `open`** lists intents with no closing entry, where a closing entry is a terminal, or an outcome carrying `Closes`. *Check:* matches an independent script's count on the same commit (63 at `97f26098`).
- **R5. `next-id`** fetches, then prints the next free ID across every monthly file with the commit it read, and warns on duplicates. *Check:* fixtures with a duplicate, and with the highest ID in an earlier month.
- **R6. Cross-repository references resolve:** "Forager RECORD -1054" in forager-forecast's decision log (63 such references) resolves to the Forager entry, cited. *Check:* one real reference resolved and verified.
- **R7. Unread sources are reported,** never skipped silently. *Check:* a run with a bad ref names it.

## Constraints

- No writes, and no network use except `git fetch`.
- Accepts Forager's IDs (`YYYY-MM-DD-NNNN`) and forager-forecast's D-numbers.
- Built tests-first, with every requirement revert-checked (E-GD's method).

## Acceptance

- R1 to R7 pass, and each requirement's revert makes its test fail.
- On real data, `show` and `links` for five entries the operator picks match a reading by hand.

## Unverified

- That `pre-main`'s audit index holds every row of `records-after-173`'s: counted, not compared.
- How far "current ruling" can go: only 8 Forager entries carry an explicit `Supersedes` (6 of them decisions, at `97f26098`). Replacements stated in prose cannot be followed.
