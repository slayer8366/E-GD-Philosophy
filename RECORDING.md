# Recording

How a project working under this method keeps its record. The record store is the first of the four pieces of infrastructure (ENFORCEMENT.md, Minimal Required Infrastructure), and this document is its method: what goes in, in what form, and what travels with it.

It was adopted on 2026-10-16 (RECORD.md 2026-10-16-05), on the operator's ruling, from Forager's record. There these methods ran for about four weeks and 1,275 entries (trials/forager-2026-10-16.md). The operator, on the methods: "These recording methods have been invaluable" (prompts/preserved/2026-10-16-05.md).

Two of the entry types, intent and terminal, are this repository's own. Three more, continuation, merge and dispatch-note, were first defined in the checker of Claude-kit v0.2, the kit that carried this method's gates into Forager as harness hooks; the kit also added partial to the terminal outcomes. The other seven are written down here for the first time, from how Forager used them. Each type below says which it is.

## What every entry carries

- **Kind, ID and Timestamp.** The timestamp is read from a clock at the time of writing, never estimated (Sourced Claims).
- **Who wrote it, and where.** A closing `Notes` line such as "Written by the planner by hand, on branch records-after-173". 1,004 of Forager's 1,275 entries carry one.
- **The next free ID**, wherever IDs can collide between parallel sessions or branches. It is stated at the end of the entry and checked against the remote before it is used (PROTOCOL rule 13). 548 of Forager's entries name it.
- **The operator's words,** wherever they bear on the entry, quoted verbatim with their date. They are never paraphrased, and an answer is never relabelled as a rule (Operator Authority).
- **The field form.** Each field is a line starting `**Label:**`, and its value runs to the next such line. Any other line that starts that way is read as a field, so prose inside an entry does not.

## What goes in

The record holds what was decided and what happened. Clarify first, then record once:

- one entry per settled decision, carrying the deciding words;
- none for a re-ask that changed nothing, for a misreading, or for the rounds of explanation that fixed it.

When an answer is partial, unclear or surprising, the question is asked again until the decision is settled, and only then recorded. This is PROTOCOL rule 14, promoted here.

## Entry types

Twelve, kept as Forager used them, synonyms included, by the operator's ruling ("Keep all twelve", prompts/preserved/2026-10-16-05.md). Where two types overlap, both are described as Forager wrote them, and the overlap is stated. Counts are from Forager's record at `97f26098`. "(this repository)" marks the two this repository's record already had, "(kit)" the three Claude-kit v0.2 added, and "(practice)" the seven defined here from Forager's usage.

### intent (this repository) — 243 in Forager

Opens a piece of work, before anything is built.

- **Fields:** `Title`, `Change`, `Scope boundary`, `Baseline`, `Prediction (outcome — planner)`, `Prediction (mechanism — coder)`, `Finish line`, `Abort conditions`, and `Dispatch-file` when a dispatch governs it.
- **The prediction is required.** Forager's intents stopped carrying predictions, finish lines and abort conditions after its checker was removed; the cause is inferred, not recorded. The operator ruled that drift, not a decision (prompts/preserved/2026-10-16-01.md), so the requirement stands.
- **Closing:** every intent is closed by exactly one closing entry. That is a terminal, or an outcome that carries `Closes`.

### terminal (this repository; partial from the kit) — 166 in Forager

Closes exactly one intent and says what happened.

- **Fields:** `Closes`, `Outcome`, `Observed`, `Deviations`.
- **Outcomes,** one of four:
  - completed;
  - partial, which carries `Deferred`, naming what was left undone and why;
  - superseded, which carries `Superseded-by`;
  - abandoned, which carries `Working-state`: what was left behind, and whether it is safe to build on.
- A completed terminal does not carry `Deferred`.
- **Forager's usage:** completed 150, abandoned 6, superseded 5, partial 3. It also wrote "parked" and "both" once each. No outcome list allows those, and this method does not adopt them.

### continuation (kit) — 330 in Forager

Carries on an open intent under a new dispatch or a new step.

- **Fields:** `Continues`, naming an intent still open at that point in the record. The kit's form adds `Dispatch-file`, `Reason` and `Changes`; 26% of Forager's continuations carry them. The rest record the step in prose.
- **It opens and closes nothing.** It carries no `Closes`, `Outcome`, prediction or finish line; the scope and predictions stay the intent's.
- **It never stands in for a terminal.** 49 of the 63 Forager intents that have no terminal had been continued instead, so their status still reads as open.

### decision (practice) — 224 in Forager

One settled decision.

- **Fields as Forager used them:**
  - `Title` (74%);
  - `The owner, verbatim` (71%), written here as `The operator, verbatim` with its date;
  - `What it sets` (61%), the decision itself;
  - `Continues` (45%), when the decision belongs to open work;
  - `Context` (30%).
- **Practices seen in Forager and adopted:**
  - `What the owner was told before answering`: the question the answer responded to, so that the answer can be read against it;
  - `Supersedes`, naming the decision it replaces and quoting that decision's words (6 entries);
  - `Not authorised by this`, stating that the decision is not permission to build (3);
  - `Before build, unverified`, listing what the decision rests on that nobody has checked.
- **Who decided** is labelled: the operator's ruling, quoted; a planner's call within a delegation; proposed; or provisional until review. These are forager-forecast's labels (`docs/planning/DECISIONS.md`).

### outcome (practice) — 40 in Forager

The result of a report or a check, filed against open work.

- **Fields:** `Title`, `Observed` (77%), `Continues` (87%), `Report-file` when the report is filed beside the entry, `The owner, verbatim` (30%), `For the owner` (27%: what goes back to the operator), and `Corrects` where it withdraws an earlier premise.
- **Overlap with terminal:** 4 of the 40 carry `Closes` instead of `Continues`, and close their intent as its terminal would. One carries neither.

### observation (practice) — 21 in Forager

Something seen that is not itself a task.

- **Fields:** `Title` (90%) and `Observed` (66%), keeping what was read apart from what was inferred, what was not checked, and what is open for the operator.

### finding (practice) — 3 in Forager

A diagnosis worth an entry of its own.

- **Fields:** `Continues`, then the evidence in labelled parts (read, inferred, confirmed, withdrawn), why it matters, and what is open for the operator.
- **Overlap with observation:** two Forager sessions once wrote a finding and an observation about the same event under the same ID. A correction entry then said which to cite.

### device-note (practice) — 11 in Forager

A build put on a test device.

- **Fields:**
  - `Covers`: what the build is on the device for;
  - `The build`: version, commit, how it was built, and the checks on it;
  - `The install`: device, time, the operator's words authorizing it, and the state before and after;
  - `Not done`: what the writer deliberately did not do on the device;
  - `Run by`.

### correction (practice) — 13 in Forager

Fixes earlier entries without editing them.

- **Fields:** `Corrects` (the IDs, and the claim corrected); `What was wrong` (61%), quoting it; and `What it corrects` or which entry to cite instead.
- **Overlap:** corrections also appear as a `Corrects` field inside other entries, an outcome's for example.

### merge (kit) — 91 in Forager

One merge into a protected branch.

- **Fields:**
  - `PR`, `Head` and `Base`;
  - `Merge-commit`;
  - `Pre-merge`, the base commit before the merge;
  - `Backup`, naming the backup taken before the merge (see "Backups before merges");
  - `Merged-by`, the operator, or an agent together with the dispatch that authorized it;
  - `Carries`, the record entries the merge brings into the base.
- About 70% of Forager's merge entries carry `PR`, `Head`, `Base`, `Merge-commit`, `Pre-merge` and `Backup`; 28% carry `Merged-by` and `Carries`.

### dispatch-note (kit) — 128 in Forager

Accounts for a dispatch that opens no intent, in one of two forms.

- **The kit's form,** about a third of Forager's:
  - `Dispatch-file`;
  - `Type`: build, device or pulse;
  - `Outcome`: answered, declined, exercise, stopped or merged;
  - `Report`;
  - and no `Closes`, prediction or finish line.
- **Forager's later form,** about two thirds: a change to a dispatch already running. Fields: `Dispatch` (the dispatch changed), `Reason`, `Changes`, and the operator's answer.

### handoff (practice) — 5 in Forager

One planner session handing to the next.

- **Fields:** `Title`, `Handoff-file` (the handoff document, filed in the record's own store), the operator's words asking for it, and the next free ID.

## Backups before merges

Before a merge into a protected branch, the base branch is saved, so the merge can be undone from something other than memory.

1. **Make the backup.** The base is written as a bundle to a backup directory outside the repository, and the bundle is verified (`git bundle verify`). It goes outside the repository because a backup can hold things that must never reach the remote. It never goes in a temporary directory, since that does not survive a reboot.
2. **Describe it.** A manifest of hashes is written beside the bundle.
3. **Index it.** One line is appended to the backups index, an append-only file in the same directory. The line says what the backup holds, which merge it guards, which dispatch it belongs to, and how to restore it. A backup nobody can find is not a way back.
4. **Name it.** The merge entry's `Backup` field names the backup.

Agents create backups and never delete, move or overwrite them; a backup an agent can erase does not protect against the agent. Pruning is the operator's, by hand. When the operator directs a removal, whether a backup of the removed material is kept, and where, is the operator's decision, and no agent makes one on its own.

Sources: Forager's accountability design (`docs/process/accountability-design.md`, "Where backups live"), and the merge procedure of Claude-kit v0.2. 74% of Forager's merge entries name a backup.

## The index

One append-only table for the dated records that live outside the record store itself: dispatches, reports, audits, findings and decision write-ups. Each gets one row: the date, a one-line statement of what it found or decided, and the file. It is how a fresh session finds the reasoning without reading every document.

- **A row that supersedes another names the row it replaces.** A stale row nobody marked is worse than no row.
- **A finding outside a task's scope gets its own row,** not a sentence inside an unrelated report, where nobody searching for it would look (Durability Is Location).
- **The index is a serialization point for parallel work.** Sessions that append to it are sequenced, or the index is split so each appends to its own fragment. On a merge conflict, every row from both sides is kept (PROTOCOL rule 13).

Forager's index is `docs/audits/README.md`, with 356 dated rows at `402489ae`. forager-forecast files every dispatch byte-identical under `docs/dispatch/` and indexes it in that same single table, rather than keeping a second index that would drift out of step with the first.

This repository has no separate index. At its present size, RECORD.md and `prompts/` do the job.

## Reports

Every report that answers a dispatch carries, beside what landed and the evidence for it, five disclosure sections:

- **Confirmed against inferred:** which claims were read or observed, and which were reasoned.
- **Could not determine:** what was looked for and not settled, and why.
- **Premises that were wrong:** each premise of the dispatch found false, with the line that shows it.
- **Decided beyond scope:** every choice the dispatch did not make and the writer did (PROTOCOL rule 6).
- **Observed, not asked:** findings outside the task's scope (Durability Is Location).

A section with nothing in it says "None". An empty section and a missing one both read as unchecked.

Source: Forager's planner operating guide of 2026-08-25, which asked of every report "the disclosure norm: confirmed vs. inferred, could-not-determine, any premise that turned out wrong, anything decided the dispatch didn't cover" (`docs/qc/planner-operating-guide-2026-08-25.md`). The first four were in use in roughly 90 to 100 of Forager's 258 audit documents, with nothing enforcing them (pattern counts). The fifth comes from Forager's finding of 2026-09-12: four findings existed only in transcripts, and only one of 80 reports had a slot for something noticed in passing (Forager's audit index, line 113 at `402489ae`). This method added it on 2026-10-16 (Durability Is Location).

## Layout: one file per month

A record that grows large is kept as one file per month, `records/YYYY-MM.md`. `RECORD.md` at the root becomes the index: its header, and a list of the monthly files with the first and last entry in each, so a link to `RECORD.md` still lands somewhere useful. Added 2026-10-16 (RECORD.md 2026-10-16-17), on the operator's ruling; one file per entry was judged excessive.

- **An entry's month is the month of its Timestamp, in UTC, not its ID.** An ID scheme can freeze its date: Forager's IDs have begun `2026-09-28` since that day, so its 777 October entries carry September IDs. An entry with no Timestamp goes in the month of the entries around it.
- **Each monthly file is append-only,** with a short header ending in the entries heading. New entries go in the file for their Timestamp's month, so only the current month's file grows.
- **IDs stay unique across all the files.** A running sequence carries on across months, so the next free ID is read from every file, not only the current one.
- **Links may point into an earlier month.** `Continues`, `Closes`, `Corrects` and `Supersedes` are resolved across all the files. In Forager, 10 of 709 such links crossed the first month boundary.
- **Splitting an existing single file is done once, on the operator's word,** as archival without loss:
  - Any other branch that edited the file is merged in first, so the split starts from one reconciled file.
  - Every entry is moved byte for byte.
  - The counts of entries per file sum to the original's count, and the monthly files' entries, joined in order, equal the original's entries exactly.
  - The split is recorded, with the commit before it, the counts, and what it stops enforcing: append-only for the original file, this once.
- **What it does not fix.** Two sessions writing at once still meet in the current month's file (PROTOCOL rule 13). A busy month is still large: Forager's October reached about 8,500 lines in its first 16 days.

This repository's own record stays one file at its present size. Its checker reads only `RECORD.md` until it is updated to read monthly files, which is code, on its own go.

## This repository's own record

Since 2026-10-16 (RECORD.md 2026-10-16-07), this repository's check_record.py accepts all twelve types, with the minimal required fields the operator chose. Everything beyond these is checked by reading.

| Type | Required fields |
|---|---|
| intent | Kind, ID, Timestamp, Title, Change, Scope boundary, Baseline, both predictions, Finish line, Abort conditions |
| terminal | Kind, ID, Timestamp, Closes, Outcome, Observed, Deviations; plus Deferred when partial, Superseded-by when superseded, Working-state when abandoned |
| continuation | Kind, ID, Timestamp, Notes, Continues |
| finding | Kind, ID, Timestamp, Notes, Continues |
| correction | Kind, ID, Timestamp, Notes, Corrects |
| outcome | Kind, ID, Timestamp, Notes, and Continues or Closes |
| merge | Kind, ID, Timestamp, Notes, Merge-commit, Backup |
| dispatch-note | Kind, ID, Timestamp, Notes, and Dispatch-file or Dispatch |
| decision, observation, device-note, handoff | Kind, ID, Timestamp, Notes |

It also checks the links between entries:

- **Continuations.** A continuation's `Continues` names an intent that appears earlier and is still open at that point. A continuation carries no `Closes`, `Outcome`, `Superseded-by`, `Finish line` or prediction field.
- **Other backward links.** A `Continues` on any other type names an earlier entry. Every ID in a `Corrects` names an earlier entry.
- **Closing an intent.** `Closes` appears only on a terminal or an outcome. An outcome with `Closes` counts as its intent's closing entry, so an intent closed by both a terminal and an outcome fails the closed-once check.
- **Terminal outcomes.** A terminal's `Outcome` is completed, partial, superseded or abandoned. A completed terminal may not carry `Deferred`.

Since 2026-10-17 (RECORD.md 2026-10-17-01), the checkers also read a record kept in monthly files:

- **Monthly files.** check_record.py reads `RECORD.md` and `records/YYYY-MM.md` as one record. An entry with a Timestamp must sit in its month's file. The working-tree check and the history walk run on each monthly file, and an entry-less `RECORD.md` is reported as the index rather than checked.
- **Longer IDs.** IDs may carry two or more digits after the date, as Forager's do.
- **Dispatch claims.** check_prompts.py reads them from every record file.

One limit remains: check_prompts.py accepts one prompt claimed by an intent and its terminal, but not by an intent and an outcome that closes it.

Since 2026-10-17 (RECORD.md 2026-10-17-05), the checkers run on any repository they are given, and a `records.json` there can reshape every rule in this section: the record's file names, its ID format, its entry types and their fields, and the closing, linking, outcome and sentinel rules. The rules above are the defaults, used when a repository has no config. ADOPTING.md explains how to adopt them.

Each rule above has a self-check in `--render-check`: checks 19 to 38 for the entry types, 39 to 46 for monthly files and IDs, 47 to 56 for any-repository use and the config, and check_prompts.py's own p1 to p4. Revert runs disabling each rule in turn made its own check fail (REGISTER.md, 2026-10-16 and 2026-10-17).

Forager kept all twelve types without a checker after 2026-09-27. Run later from copies, its old checkers reported 1,646 entry errors (Forager record 2026-09-28-544). Much of that figure is types the old checkers did not know, so it measures the gap between practice and checker, not only mistakes.
