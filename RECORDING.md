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

## This repository's own record

This repository's check_record.py accepts only intent and terminal entries. Updating it is a separate change, made on its own go, by the operator's ruling (prompts/preserved/2026-10-16-05.md). Until then, this repository's own record writes intent and terminal entries only, and records decisions, corrections and observations inside them. The other ten types are for adopters' records, and a checker that does not know them fails them.

The checker does already accept a terminal whose outcome is partial, since it validates only the superseded and abandoned outcomes.

Forager kept all twelve types without a checker after 2026-09-27. Run later from copies, its old checkers reported 1,646 entry errors (Forager record 2026-09-28-544). Much of that figure is types the old checkers did not know, so it measures the gap between practice and checker, not only mistakes.
