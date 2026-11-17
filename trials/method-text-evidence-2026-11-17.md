# Evidence moved out of the method text, 2026-11-17

Under RECORD.md 2026-11-17-04, carrying out decision 2026-11-05-03: the method documents become project-neutral, and their project evidence moves into `trials/`, so nothing is lost.

This file holds every line the project-neutral rewrite changed, verbatim as it stood at E-GD commit 584a8c9577062147869c1c237a17cf18b0de65cb. The lines are grouped by file and by rule or section, and quoted with `> `. It was committed before the rewrite (Knowledge Harvest Before Rewrite). The rewritten text points here with "Sources: trials/method-text-evidence-2026-11-17.md, rule N" wherever a citation was removed.

The projects named below are the field-app project (Forager) and the research project descended from it (forager-forecast). The method text now calls them that, and RECORDING.md calls the first "the source project". The approved before-and-after of every line is in `specs/2026-11-17-project-neutral.md`.

---

## PROTOCOL.md, rule 1

Line 23 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Promoted 2026-10-16 into PHILOSOPHY.md's Sourced Claims (RECORD.md 2026-10-16-01), with rule 2. Forager gave its planner read access to remove this rule's premise and the premise held anyway: at least 24 of its record entries describe planner slips about repository state, and a claim that a file had zero references decayed inside its own pull request (trials/forager-2026-10-16.md; Forager CLAUDE.md at 402489ae, the pitfall on a planner's picture of the repository). The text above stays as written.

## PROTOCOL.md, rule 2

Line 35 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Promoted 2026-10-16 into PHILOSOPHY.md's Sourced Claims (RECORD.md 2026-10-16-01), with rule 1. Forager's practice is this rule's general form: a dispatch states the base commit it assumes, and the executing session verifies that base before acting on any claim about what exists. The text above stays as written.

## PROTOCOL.md, rule 5

Line 67 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Evidence, added 2026-10-16 (RECORD.md 2026-10-16-01): Forager supports this rule's premise at n of 5 or more. A simulated test environment reported zero for a quantity that is never zero on a device, and a fixed constant matching that zero passed the suite and failed on the device. A fake camera defaulted to ready, so the deadlock under test could not be represented. A test harness supplied a value from outside the component under test. A device reported a constant positional accuracy. The `assumed` marker this rule prescribes was never tried there, so the marking practice is still untested. Severity of Checks now carries the premise as a principle; this rule stays here for its marking practice.

## PROTOCOL.md, rule 7

Line 89 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Forager evidence, added 2026-10-16 (RECORD.md 2026-10-16-01): this rule's axis became Forager's working partition, in a form one step finer than the table above. The operator decides behaviour, scope, design, wording, licences, merges and anything public. The planner decides technical routes that change nothing the operator would see or rule on, records each call, and says so in its next message. "When unsure which it is, it's the owner's" (`docs/process/planner-profile.md:13-15` at `402489ae`). forager-forecast labels such a row as the planner's call with "no rule changed" (`docs/planning/DECISIONS.md`, D118, at `b9127e5`). The same project departed from Role Partition in two recorded ways: its planner reads the repository and writes the record. It also added two roles the partition does not have: a read-only scout that answers questions about the repository without changing it, and an independent reviewer (rule 11). What has not been shown is a case this axis decided that the installed partition could not have, which is this rule's own bar for promotion. It stays here.

## PROTOCOL.md, rule 9

Line 127 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Forager evidence, added 2026-10-16 (RECORD.md 2026-10-16-01): the `committed:<sha256>` form appears 0 times in Forager's record of 1,275 entries. forager-forecast reached the same end, a choice provably fixed before the outcome, by public commits whose order a reviewer checks (rule 10). That route was used and this one was not; rule 10 is the working method, and this rule's withheld hash remains for a prediction that must stay hidden from the executor until it has run.

## PROTOCOL.md, rule 10

Line 137 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Evidence: forager-forecast fixes its production seed and a 20-configuration tuning grid before any model is fit, rejecting the alternative because it "invites tuning until it wins" (`docs/planning/DECISIONS.md:101`, D31 at `b9127e5`), and does the same for its evaluation, filters and licence tracks (D33, D26, D29). Reviewers confirmed that the commit came before the first count in four cases. The rule held when the result pulled the other way (D109, D90), and caught a committed tolerance that would have failed before any value was read. Forager's planner profile carries the same rule: "Fix choices before data" (`docs/process/planner-profile.md:38` at `402489ae`).

## PROTOCOL.md, rule 11

Line 145 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Evidence: forager-forecast decision D18 (`docs/planning/DECISIONS.md:114` at `b9127e5`) and its standing review protocol (`docs/dispatch/2026-09-18-review-protocol.md`; the quoted sentence is at `:17`). It has 21 review files on main, 14 of which led to a fix, a correction or a decision traceable in its record (a reader session's classification, 17 of the 21 from index rows). In its decision D35, an independent review found two things the builder's self-check had missed, while the self-check re-ran a count the reviewer could not reach; both documents were kept, because each saw something the other could not. In Forager, an independent review caught 37 guessed record timestamps (record 2026-09-28-608). This repository's own record named the need first: RECORD.md 2026-08-15-04, Finding 1, "a single investigation is one sample, not a determination".

## PROTOCOL.md, rule 12

Line 171 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Evidence, all from Forager (trials/forager-2026-10-16.md):

Line 173 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - Per-dispatch operator approval was removed four days after it began. The operator: "Can't have me hitting buttons. Those hooks need to change" (`docs/audits/2026-09-26-approval-exempt-build-device.md`).

Line 174 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - The whole hook kit was disabled and deleted on 2026-09-27. The operator's account, 2026-10-16: "The hooks were removed because actions agents are expected to perform were being hindered. The operator had to hold the agent's hand every step of the way, which was the opposite of the kit's intentions." (prompts/preserved/2026-10-16-03.md). The note written on 2026-09-27 records the operator's words then, "to work around weekly limits" (`docs/audits/2026-09-27-kit-hooks-disabled.md`). That note is the model for recording a removal: its section 3 lists what stops being enforced.

Line 182 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> The operator ruled the loss of predictions to be drift, not a decision (prompts/preserved/2026-10-16-01.md), so Intent-Driven Engineering's prediction requirement stands unchanged. Forager is recorded as a gate lost once its checker was removed.

## PROTOCOL.md, rule 13

Line 202 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Evidence, from Forager (Forager `CLAUDE.md` at `402489ae` and trials/forager-2026-10-16.md):

Line 204 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - A planner session believed dead reconnected and kept writing to the same record branch, so two record IDs were each used twice (`docs/audits/2026-10-05-planner-handoff.md`).

Line 205 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - An entry was deleted with its ID declared retired, and the ID was used again 26 minutes later (Forager commits `0bda73e8` and `4805cb90`).

Line 206 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - A hook numbered each preserved prompt by counting only its own checkout, so parallel worktrees took the same numbers (Forager `RECORD.md` on `main`, 2026-09-23 finding on the dispatch guard).

Line 207 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - Two branches each declared the same schema version with different migrations, which no file-level merge detects (Forager `CLAUDE.md`, the base-branch pitfall).

Line 208 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - The audit index conflicted on every push after the first when two sessions ran in parallel (Forager `CLAUDE.md`, the serialization-point pitfall).

Line 209 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - From forager-forecast: a decision filed on one branch had to be renumbered the same day, because the number had already been taken on another (`docs/planning/DECISIONS.md:17`, D123, at `b9127e5`).

## PROTOCOL.md, rule 14

Line 227 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - Forager's record held, at the first reading, 12 entry kinds, with 224 decisions and 330 continuations among 1,275 entries (fifteen by the second reading, trials/forager-2026-11-05.md).

Line 228 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - The operator had one entry deleted from it as clutter (Forager commit `0bda73e8`).

Line 229 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - 63 of its intents have no terminal entry; 49 of those were continued instead (trials/forager-2026-10-16.md).

Line 231 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - forager-forecast's decision rows carry the provenance labels above (`docs/planning/DECISIONS.md` at `b9127e5`).

Line 235 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Promoted 2026-10-16 into RECORDING.md (RECORD.md 2026-10-16-05), on the operator's ruling, with the twelve entry types kept as Forager used them rather than reduced to the two this rule proposed. The text above stays as written.

## PROTOCOL.md, rule 15

Line 247 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Evidence: Forager's field-instrument skill states two governing rules in this order, "honesty is never traded for ease" and then "don't make me think" (`skills/examples/field-instrument-interface/SKILL.md`). The operator's design principle "Don't make me think" is recorded in Forager's `CLAUDE.md` (2026-09-30). The skill itself says three of its seven rules are inferred from the app's purpose and general practice, not from field data.

## PROTOCOL.md, rule 16

Line 255 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Evidence: a tree check counted the outcome labels correctly and never asked what one label meant. That label carried four reasons, one of which was the mechanism working, so a device check built on the count would have filed correct behaviour as a fault (Forager `CLAUDE.md`, testing section; index line 145). Three more instances in one week of a correct observation produced by an incorrect mechanism are at index line 165. Standing: four instances, in one project. This sits beside Severity of Checks: that principle asks whether a check could fail, and this asks what a passing check licenses.

## PROTOCOL.md, rule 17

Line 261 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Evidence: Forager, index line 110, where the operator ruled that this general form supersedes the instance it came from "because it predicts recurrence rather than recording one occurrence". Standing: one instance.

## PROTOCOL.md, rule 18

Line 267 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Evidence: in Forager, an alias chosen for coder sessions resolved to a different model than the one the planner had told the operator (`docs/audits/2026-09-29-planner-handoff.md:55`). The operator later used two builds of one dispatch as a comparison between models: "we are measuring [model B] vs [model A]" (`docs/audits/2026-09-29-f5-landed-and-redo-compared.md`). Standing: two instances. If promoted, this extends Capture Environmental Context to the agents themselves.

## PROTOCOL.md, rule 20

Line 279 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Evidence: Forager `CLAUDE.md`, testing section, where the rule is written. A coder deleted 26 tests without reporting it, and they were restored at the next merge (index line 335). Standing: two instances.

## PROTOCOL.md, rule 21

Line 283 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> The operator's stated approach since Forager's hooks were removed: "So now I let philosophy, precise methodology, and evidence gating drive the agent" (2026-10-16, prompts/preserved/2026-10-16-03.md).

Line 301 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - Forager's release gate of 2026-10-16 is an evidence gate at a boundary: CI, both test phones, an advisory interface audit, and the operator's approval (Forager record 2026-09-28-1085 to -1087).

Line 302 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - forager-forecast's dependent tasks wait for their prerequisite's review to be filed (rule 11).

## PROTOCOL.md, rule 22

Line 329 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Evidence: Forager's docs/process/planner-profile.md, written on 2026-10-07 at the owner's request. Its planner was named from Forager's world, which is woods, foraging and wayfinding: "A rowan is the guardian tree at the edge of the woods. A waymark is the blaze that keeps the next walker on the trail." (planner-profile.md:5). The owner's words:

Line 331 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - "That way each role can have a profile that models their behavior" (Forager record 2026-09-28-1141);

Line 333 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - "EGD may adopt it but to make it general, the profiles should have the roles name themselves based on the project and its scope" (2026-09-28-1142).

Line 337 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Standing: one profile has been in use for about nine days; three more are being written in Forager, and E-GD's curator profile is new. Untested as a general method.

## PROTOCOL.md, rule 23

Line 349 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - An experiments branch is production plus developer tools plus running experiments. It is rebased onto production after every release, "to reflect workability" (Forager record 2026-09-28-1087), and never merged anywhere. An experiment chosen to ship is carried onto the working branch without the tools.

Line 360 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> A device check or field walk is proposed by the planner when a promotion needs one, and the operator decides. It is not a standing step: "Field walks and device checks aren't always necessary" (-1133). An urgent fix takes the same gate, at the front of the queue, and is then carried into the working branch.

Line 364 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Who.** A fresh session for each promotion. It is never the session that built the work, and it runs on a different model from the one that built it, because "the same model shares blind spots" (-1134).

Line 371 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **"Advises, you decide"** (-1086). The verdict goes to the operator, who decides; it is not a veto. The auditor writes no product code, fixes and merges nothing, never weakens a test, and never settles a conflict between two of the operator's rulings: it puts both sides to the operator.

Line 372 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Devices.** A real device comes first. An emulator run is labelled "emulator, not a device", and what an emulator cannot stand in for is listed (-1094).

Line 374 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> **The QA philosophy it audits against.** If none exists, the auditor's first task is to draft one (-1085):

Line 378 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - an adopted proposal stays marked as adopted from the auditor's proposal, never as the operator's words (-1092, -1097).

Line 382 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> **Sources.** Forager's planner wrote the framework for this repository: prompts/preserved/2026-10-16-05-auditor-framework-for-egd.md and its addendum, -05b, on Forager's origin/records-after-173 (f09ff09c, 7d6cdd45). They are cited there rather than copied here. Where the addendum changed the original, this rule follows the addendum: the original lists a device check as step 2 of the gate, and the addendum removes it (-1133). The owner's view of the whole: "the rules we have are simply what we already do. Just codified" (-1138).

Line 386 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Standing: one promotion has run through the gate. It was documents only, and passed with two notes on the planner's own documents, neither blocking (-1131, -1132). No release with code has been audited, and the device path is untested.

## PROTOCOL.md, rule 30

Line 446 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Rules 10 onward were added on 2026-10-16 (RECORD.md 2026-10-16-01) from the records of Forager and forager-forecast (trials/forager-2026-10-16.md). Their evidence comes from one further project family, read after the fact. It is not a test in this repository, and none of them is enforced by a check.

## RECORDING.md, top

Line 5 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> It was adopted on 2026-10-16 (RECORD.md 2026-10-16-05), on the operator's ruling, from Forager's record. There these methods ran for about four weeks and 1,275 entries (trials/forager-2026-10-16.md). The operator, on the methods: "These recording methods have been invaluable" (prompts/preserved/2026-10-16-05.md).

Line 7 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Two of the entry types, intent and terminal, are this repository's own. Three more, continuation, merge and dispatch-note, were first defined in the checker of Claude-kit v0.2, the kit that carried this method's gates into Forager as harness hooks; the kit also added partial to the terminal outcomes. The other seven are written down here for the first time, from how Forager used them. Each type below says which it is.

## RECORDING.md, What every entry carries

Line 12 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Who wrote it, and where.** A closing `Notes` line such as "Written by the planner by hand, on branch records-after-173". 1,004 of Forager's 1,275 entries carry one.

Line 13 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **The next free ID**, wherever IDs can collide between parallel sessions or branches. It is stated at the end of the entry and checked against the remote before it is used (PROTOCOL rule 13). 548 of Forager's entries name it.

## RECORDING.md, Entry types

Line 28 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Twelve, kept as Forager used them, synonyms included, by the operator's ruling ("Keep all twelve", prompts/preserved/2026-10-16-05.md). Where two types overlap, both are described as Forager wrote them, and the overlap is stated. Counts are from Forager's record at `97f26098`. "(this repository)" marks the two this repository's record already had, "(kit)" the three Claude-kit v0.2 added, and "(practice)" the seven defined here from Forager's usage. Projects add kinds of their own as they need them. A kind enters this method only when it is harvested and approved; until then it stays the project's (trials/forager-2026-11-05.md, R5).

## RECORDING.md, intent (this repository) — 243 in Forager

Line 30 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> ### intent (this repository) — 243 in Forager

Line 35 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **The prediction is required.** Forager's intents stopped carrying predictions, finish lines and abort conditions after its checker was removed; the cause is inferred, not recorded. The operator ruled that drift, not a decision (prompts/preserved/2026-10-16-01.md), so the requirement stands.

## RECORDING.md, terminal (this repository; partial from the kit) — 166 in Forager

Line 40 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> ### terminal (this repository; partial from the kit) — 166 in Forager

Line 51 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Forager's usage:** completed 150, abandoned 6, superseded 5, partial 3. It also wrote "parked" and "both" once each. No outcome list allows those, and this method does not adopt them.

## RECORDING.md, continuation (kit) — 330 in Forager

Line 53 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> ### continuation (kit) — 330 in Forager

Line 57 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Fields:** `Continues`, naming an intent still open at that point in the record. The kit's form adds `Dispatch-file`, `Reason` and `Changes`; 26% of Forager's continuations carry them. The rest record the step in prose.

Line 59 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **It never stands in for a terminal.** 49 of the 63 Forager intents that have no terminal had been continued instead, so their status still reads as open.

## RECORDING.md, decision (practice) — 224 in Forager

Line 61 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> ### decision (practice) — 224 in Forager

Line 65 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Fields as Forager used them:**

Line 71 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Practices seen in Forager and adopted:**

Line 76 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Who decided** is labelled: the operator's ruling, quoted; a planner's call within a delegation; proposed; or provisional until review. These are forager-forecast's labels (`docs/planning/DECISIONS.md`).

## RECORDING.md, outcome (practice) — 40 in Forager

Line 78 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> ### outcome (practice) — 40 in Forager

## RECORDING.md, observation (practice) — 21 in Forager

Line 85 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> ### observation (practice) — 21 in Forager

## RECORDING.md, finding (practice) — 3 in Forager

Line 91 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> ### finding (practice) — 3 in Forager

Line 96 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Overlap with observation:** two Forager sessions once wrote a finding and an observation about the same event under the same ID. A correction entry then said which to cite.

## RECORDING.md, device-note (practice) — 11 in Forager

Line 98 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> ### device-note (practice) — 11 in Forager

## RECORDING.md, correction (practice) — 13 in Forager

Line 109 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> ### correction (practice) — 13 in Forager

## RECORDING.md, merge (kit) — 91 in Forager

Line 116 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> ### merge (kit) — 91 in Forager

Line 127 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - About 70% of Forager's merge entries carry `PR`, `Head`, `Base`, `Merge-commit`, `Pre-merge` and `Backup`; 28% carry `Merged-by` and `Carries`.

## RECORDING.md, dispatch-note (kit) — 128 in Forager

Line 129 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> ### dispatch-note (kit) — 128 in Forager

Line 133 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **The kit's form,** about a third of Forager's:

Line 139 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Forager's later form,** about two thirds: a change to a dispatch already running. Fields: `Dispatch` (the dispatch changed), `Reason`, `Changes`, and the operator's answer.

## RECORDING.md, handoff (practice) — 5 in Forager

Line 142 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> ### handoff (practice) — 5 in Forager

## RECORDING.md, Backups before merges

Line 159 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Sources: Forager's accountability design (`docs/process/accountability-design.md`, "Where backups live"), and the merge procedure of Claude-kit v0.2. 74% of Forager's merge entries name a backup.

## RECORDING.md, The index

Line 170 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Forager's index is `docs/audits/README.md`, with 356 dated rows at `402489ae`. A project that files every dispatch in one folder and indexes it in one table avoids a second index drifting out of step with the first, as long as every new dispatch gets its row. One project's index went unchanged while its later dispatches went unindexed (trials/forager-2026-11-05.md, R3).

## RECORDING.md, Reports

Line 186 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Source: Forager's planner operating guide of 2026-08-25, which asked of every report "the disclosure norm: confirmed vs. inferred, could-not-determine, any premise that turned out wrong, anything decided the dispatch didn't cover" (`docs/qc/planner-operating-guide-2026-08-25.md`). The first four were in use in roughly 90 to 100 of Forager's 258 audit documents, with nothing enforcing them (pattern counts). The fifth comes from Forager's finding of 2026-09-12: four findings existed only in transcripts, and only one of 80 reports had a slot for something noticed in passing (Forager's audit index, line 113 at `402489ae`). This method added it on 2026-10-16 (Durability Is Location).

## RECORDING.md, Layout: one file per month

Line 192 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **An entry's month is the month of its Timestamp, in UTC, not its ID.** An ID scheme can freeze its date: Forager's IDs have begun `2026-09-28` since that day, so its 777 October entries carry September IDs. An entry with no Timestamp goes in the month of the entries around it.

Line 195 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Links may point into an earlier month.** `Continues`, `Closes`, `Corrects` and `Supersedes` are resolved across all the files. In Forager, 10 of 709 such links crossed the first month boundary.

Line 202 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **What it does not fix.** Two sessions writing at once still meet in the current month's file (PROTOCOL rule 13). A busy month is still large: Forager's October reached about 8,500 lines in its first 16 days.

## RECORDING.md, Accepting a past violation

Line 210 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **The field.** `Accepts-violation`, with one line per commit: the commit's hash, 7 or more hex characters, then the reason. For example: `0bda73e8 RECORD -638 removed at the owner's instruction`.

## RECORDING.md, This repository's own record

Line 242 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Longer IDs.** IDs may carry two or more digits after the date, as Forager's do.

Line 251 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Forager kept all twelve types without a checker after 2026-09-27. Run later from copies, its old checkers reported 1,646 entry errors (Forager record 2026-09-28-544). Much of that figure is types the old checkers did not know, so it measures the gap between practice and checker, not only mistakes.

## README.md, What's here

Line 37 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> | `lookups/` | Machines | Lookup configs for `records_lookup.py`, chosen with `--preset`: `forager.json` reads Forager's and forager-forecast's records. |

## README.md, What it has actually been through

Line 66 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> A second project has since run it. Forager, a field app, adopted the method in September 2026, installed its gates as harness hooks on 2026-09-22, removed them five days later because they blocked actions the agents were expected to take, leaving the operator to hold the agent's hand at every step, and kept going without them. What fired, what was dropped, and what decayed once the checkers were gone is in `trials/forager-2026-10-16.md`. Its lessons are what the October 2026 changes to the philosophy and the protocol rest on.

## ADOPTING.md, Accepting a past violation

Line 148 at 584a8c9577062147869c1c237a17cf18b0de65cb:

>     0bda73e8 an entry removed at the owner's instruction

Line 149 at 584a8c9577062147869c1c237a17cf18b0de65cb:

>     bebeb573 an entry written inside a merge, kept as it was

## ADOPTING.md, The lookup tool

Line 260 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> **More sources, in any repositories,** come from a lookup config given with `--config FILE`. `--print-config` prints the config in use, and `--preset forager` loads `lookups/forager.json`, which reads Forager's and forager-forecast's records. A config names:

## profiles/curator.md, The role

Line 16 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **The curator writes nothing in another project's repository.** Text meant for Forager is written into this record and handed to the operator, for Forager's own planner to place (2026-10-16-07, -08, -18).

## profiles/curator.md, Checking from source

Line 37 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Read a source before recommending on it,** for example forager-forecast's session log (2026-10-16-13, -14).

Line 38 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Look at every branch that holds a record before planning a change to it.** That is how the divergence between Forager's two record branches was found (2026-10-16-18).

## profiles/curator.md, Talking to the operator

Line 70 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - **Lead with the outcome,** then what it means, then the one decision needed. Describe behaviour and consequences, not code names. These are the operator's preferences as Forager's planner profile records them ("Asking the owner" and "Talking to the owner", docs/process/planner-profile.md on Forager's pre-main), followed here.

## skills/README.md, Example: a project-specific skill

Line 48 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> `examples/field-instrument-interface/` is Forager's interface rules for a field app, built on these principles: honesty is never traded for ease, then "don't make me think". It is here as an example of deriving a project's own skill from the general ones, not as a general skill. It bears on Truthful Interface Contracts and Explicit Failure Reporting, and on PROTOCOL rule 15. It says itself which of its rules are inferred rather than drawn from field data.

## skills/README.md, Found while copying, not changed

Line 64 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Forager keeps untracked local copies of nine of these skills. Three of them (completion-report, dispatch-authoring, prior-art-before-interface) are older than the account's and lack the Conventions field the account versions added. They were reported to the operator and not touched.

## skills/README.md, Edits made here after copying

Line 67 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - `revert-check`, protocol step 5: after restoring, confirm the forward change is still present. From Forager's CLAUDE.md, where a restore from git discarded an uncommitted change the check had just vouched for. The account copy does not have this edit.

Line 68 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> - `failing-test-first`, after "Read the message and say why it is the right one.": the red must come from the same unchanged test that later goes green. From Forager's "red that proves nothing" (its audit index, 2026-09-12), where the rule was followed and the red still belonged to an earlier version of the test. Corrected in a follow-up commit to say the test was edited after the fix, and that a red counts only if the same test could have passed. The account copy does not have this edit.

## DURABILITY.md, The rule

Line 58 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> Promoted on 2026-10-16 to PHILOSOPHY.md as Durability Is Location, with Forager's instances (RECORD.md 2026-10-16-01; trials/forager-2026-10-16.md).

## ENFORCEMENT.md, Minimal Required Infrastructure

Line 23 at 584a8c9577062147869c1c237a17cf18b0de65cb:

> 4. **Identity function.** One canonical content-hash routine for the project's data artifacts, owned in one module, used everywhere identity is needed. No second implementation is ever written; consumers import the one that exists. Conditional: this applies where the project's outputs are data artifacts whose identity matters, such as measurements, datasets or derived files. A project whose outputs are not such artifacts records that it has no identity function and why; Forager, an app, declined it on those grounds (trials/forager-2026-10-16.md). Made conditional 2026-10-16 under RECORD.md 2026-10-16-01.

