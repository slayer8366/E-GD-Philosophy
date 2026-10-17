---
name: record-checking
description: How to check an append-only project record (a RECORD.md, decision log or similar markdown record kept in git) with E-GD's check_record.py and check_prompts.py, on any repository, and how to shape them to that record with a records.json. Use this before citing a record as evidence, after appending entries and before committing them, before merging a branch that touches the record, when setting up a new record, and whenever someone asks whether a record is well formed. Use it especially when a record has no checker running on it, since a record nothing checks drifts without anyone seeing it.
---

# Record checking

A record is only evidence while it is well formed and has only grown. Entries missing the fields that make them checkable, links to entries that do not exist, and a committed line quietly edited all look fine to a reader. The checkers find them. ADOPTING.md in E-GD is the full reference; this is the procedure.

## Running it

1. **Find the checkers.** `check_record.py` and `check_prompts.py` sit together at the top of an E-GD clone (github.com/slayer8366/E-GD-Philosophy). They need Python 3 and git, and nothing else.
2. **Find the record's shape.** If the repository has a `records.json` at its top, the checkers use it. If not, they expect E-GD's RECORDING.md format. If the record looks nothing like that and has no config, ask the record's owner before writing one. A config says what entries must carry, which is their decision.
3. **Run both on the repository's top folder:** `python3 check_record.py REPO --json`, then the same for `check_prompts.py`. A subfolder is refused, because the history checks resolve paths from the top.
4. **Read the exit status and the JSON together.** 0 is a pass, 1 a failure with every problem listed, and 2 means nothing was checked; the message says why.

## Reading the result

- **Vacuous is not a pass.** With `"vacuous": true`, no record was found or no entries were read, so the entry rules checked nothing. Report it as that, never as "the record checks clean". The same goes for any single check marked vacuous.
- **Unclosed intents are reported, not failed.** Open work is normal. Say how many, and which.
- **Name what failed exactly**, using the checker's own message and the entry ID. Don't summarise five failures as "a few formatting issues".
- **A history-walk failure naming a merge commit** means two branches both added to the record and were merged. The walk cannot compare across that. It is a known limit, not damage. Report it, and leave the history alone.

## Fixing what it finds

- **Never edit a committed entry to make the check pass.** Append a correction entry that names the old entry and says what was wrong. The append-only checks exist to catch exactly that edit.
- **Never loosen the config to reach a pass.** Removing a required field or widening the ID pattern changes what the record must hold. That is the owner's decision. Bring it as a question, with the failures that prompted it.
- **Uncommitted entries can still be fixed in place.** The working-tree check compares against the last commit, so a mistake in an entry not yet committed is corrected before committing.

## Setting up a new record

1. Start from `python3 check_record.py --print-config > REPO/records.json`, and edit only the keys that differ. Every key you leave out keeps its default.
2. Run the self-checks: `python3 check_record.py --render-check` and `python3 check_prompts.py --render-check`.
3. **Check the checker on a copy.** In a copy of the repository, never the original, break one rule the config sets: drop a required field, or edit a committed line and commit it. The checker must fail and name it. A config you have never seen fail has not been shown to check anything.
4. Commit `records.json` beside the record, so whoever checks the record next uses the same rules.

## Looking things up

To cite an entry, follow its links, list what is still open or find the next free ID, use `records_lookup.py` from the same folder. Every answer carries the repository, ref, commit, file and lines it was read from. An answer reading "unknown" or "unsupported" says exactly that; report it as such, never as zero. ADOPTING.md's section "The lookup tool" covers its config.

## What it cannot tell you

Whether an entry is true. The checkers verify shape, links and history. A record that passes can still say something false, in perfect form. Treat a pass as "well formed and only grown", and verify claims inside entries from their sources.

## Feedback

This skill and the checkers are looked after by Clio, E-GD's curator. If something here is wrong, unclear, or got in the way, say so: open an issue at github.com/slayer8366/E-GD-Philosophy/issues (the "Feedback for Clio" form), or tell your operator. Clio brings each piece of feedback, quoted as written, with a recommendation, to E-GD's operator, who decides what changes.
