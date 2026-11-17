# Spec: the project-neutral rewrite of E-GD's method text

Under RECORD.md 2026-11-17-02.
- **The operator's approval of the change:** on 2026-11-05, "yes" to the method documents becoming project-neutral, with the evidence moving into `trials/` (RECORD.md 2026-11-05-03).
- **The operator's choice of this as the next work:** on 2026-11-17, "project neutral text".

**A spec is not a go.** Nothing below is changed until the operator approves this text. Then it goes in under its own intent.

Drafted against Test-1 at 584a8c9. Every "Now" line is quoted from that commit, and every "Proposed" line is generated from the same table of exact substitutions the rewrite will use. What is shown here is what would be written.

## How the rewrite reads

- **Projects are named by what they are.** PROTOCOL.md says "the field-app project" and "the research project descended from it". RECORDING.md calls the project its entry types were taken from "the source project", defined where it is first mentioned. PROTOCOL.md gains a short paragraph near its top saying so, and RECORDING.md's opening paragraph does the same.
- **Paths, commits, record IDs and line numbers are removed from the method text.** They are not lost:
  - every original line is kept verbatim in `trials/method-text-evidence-2026-11-17.md`, grouped by rule or section;
  - each rule whose citations were removed ends with a pointer to it ("Sources: … rule N");
  - that file is committed before the rewrite, under Knowledge Harvest Before Rewrite. The documents carry no harvest markers, so nothing else needed draining.
- **The operator's words are kept verbatim.** Only the project path after a quote is removed.
- **Counts are kept.** They are the evidence, now attributed to "the field-app project" or "the source project".
- **The trial files' own names** (`trials/forager-…`) stay as the pointers to the evidence, as the last spec allowed.

## Checks run on a throwaway copy of Test-1

- **Exact matches:** every substitution matched exactly once in its line.
- **Coverage:** a survey found 100 lines naming a project, a project path or a record ID. All 100 are covered: 93 rewritten and 7 kept, with reasons below. Four more lines were found beyond the survey:
  - two example commit hashes in ADOPTING.md;
  - one record ID the survey's pattern missed;
  - the definition fix below.

  That makes 97 changed in all.
- **No project name, path or record ID remains** after the rewrite outside the 7 kept lines.
- **No commit hash from either project remains** in the method documents. Each hash was tested against both projects' repositories and this one.
  - **Positive control:** on the current text the same scan finds 8 such hashes, 7 from the field-app project and 1 from the research project.

## Two corrections folded in

PROTOCOL.md:229 and RECORDING.md:59 state the first reading's "63 unclosed, 49 continued" as counted by terminal and continuation entries. The recount showed those figures count a `Closes` field on any kind of entry; by terminals alone they are 79 and 41 (RECORD.md 2026-11-16-03, trials/recount-2026-11-16.md). The rewrite gives both, with their definitions. This goes beyond making the text neutral, so it is listed for the operator to accept or strike.

## Left as they are

- **Records and working material:** `trials/`, `RECORD.md`, `REGISTER.md`, `prompts/`, `specs/` and `paper/`.
- **`skills/examples/field-instrument-interface/`:** one project's own skill, kept as the example it is. skills/README.md now introduces it without naming the project.
- **`lookups/forager.json` and its preset name** (`--preset forager`): this is the operator's own tool configuration, and renaming it would break its use. README.md and ADOPTING.md now describe the preset generically. Whether to keep the name is the operator's call.
- **The seven kept lines**, listed at the end with their reasons. They are this repository's own history, generic examples, and its agent instructions.

## A premise that was wrong

On 2026-11-05 the curator told the operator that "PROTOCOL.md, RECORDING.md and OVERVIEW.md cite Forager throughout". OVERVIEW.md has no project references. The text to change is mostly in PROTOCOL.md (45 lines) and RECORDING.md (37 lines), with a few lines in six other files.

## Every line, now and proposed

### PROTOCOL.md

**New paragraph after line 5** ("These are not principles. …"):

> The evidence notes below describe the projects they came from by what each is: the field-app project, and the research project descended from it. The project names, paths, commits and record IDs that stood in them until 2026-11-17 are kept verbatim in trials/method-text-evidence-2026-11-17.md, by rule (RECORD.md 2026-11-05-03).

**PROTOCOL.md:23** (rule 1)

Now:

> Promoted 2026-10-16 into PHILOSOPHY.md's Sourced Claims (RECORD.md 2026-10-16-01), with rule 2. Forager gave its planner read access to remove this rule's premise and the premise held anyway: at least 24 of its record entries describe planner slips about repository state, and a claim that a file had zero references decayed inside its own pull request (trials/forager-2026-10-16.md; Forager CLAUDE.md at 402489ae, the pitfall on a planner's picture of the repository). The text above stays as written.

Proposed:

> Promoted 2026-10-16 into PHILOSOPHY.md's Sourced Claims (RECORD.md 2026-10-16-01), with rule 2. The field-app project gave its planner read access to remove this rule's premise, and the premise held anyway: at least 24 of its record entries describe planner slips about repository state, and a claim that a file had zero references decayed inside its own pull request (trials/forager-2026-10-16.md; sources: trials/method-text-evidence-2026-11-17.md, rule 1). The text above stays as written.

**PROTOCOL.md:35** (rule 2)

Now:

> Promoted 2026-10-16 into PHILOSOPHY.md's Sourced Claims (RECORD.md 2026-10-16-01), with rule 1. Forager's practice is this rule's general form: a dispatch states the base commit it assumes, and the executing session verifies that base before acting on any claim about what exists. The text above stays as written.

Proposed:

> Promoted 2026-10-16 into PHILOSOPHY.md's Sourced Claims (RECORD.md 2026-10-16-01), with rule 1. The field-app project's practice is this rule's general form: a dispatch states the base commit it assumes, and the executing session verifies that base before acting on any claim about what exists. The text above stays as written.

**PROTOCOL.md:67** (rule 5)

Now:

> Evidence, added 2026-10-16 (RECORD.md 2026-10-16-01): Forager supports this rule's premise at n of 5 or more. A simulated test environment reported zero for a quantity that is never zero on a device, and a fixed constant matching that zero passed the suite and failed on the device. A fake camera defaulted to ready, so the deadlock under test could not be represented. A test harness supplied a value from outside the component under test. A device reported a constant positional accuracy. The `assumed` marker this rule prescribes was never tried there, so the marking practice is still untested. Severity of Checks now carries the premise as a principle; this rule stays here for its marking practice.

Proposed:

> Evidence, added 2026-10-16 (RECORD.md 2026-10-16-01): the field-app project supports this rule's premise at n of 5 or more. A simulated test environment reported zero for a quantity that is never zero on a device, and a fixed constant matching that zero passed the suite and failed on the device. A fake camera defaulted to ready, so the deadlock under test could not be represented. A test harness supplied a value from outside the component under test. A device reported a constant positional accuracy. The `assumed` marker this rule prescribes was never tried there, so the marking practice is still untested. Severity of Checks now carries the premise as a principle; this rule stays here for its marking practice.

**PROTOCOL.md:89** (rule 7)

Now:

> Forager evidence, added 2026-10-16 (RECORD.md 2026-10-16-01): this rule's axis became Forager's working partition, in a form one step finer than the table above. The operator decides behaviour, scope, design, wording, licences, merges and anything public. The planner decides technical routes that change nothing the operator would see or rule on, records each call, and says so in its next message. "When unsure which it is, it's the owner's" (`docs/process/planner-profile.md:13-15` at `402489ae`). forager-forecast labels such a row as the planner's call with "no rule changed" (`docs/planning/DECISIONS.md`, D118, at `b9127e5`). The same project departed from Role Partition in two recorded ways: its planner reads the repository and writes the record. It also added two roles the partition does not have: a read-only scout that answers questions about the repository without changing it, and an independent reviewer (rule 11). What has not been shown is a case this axis decided that the installed partition could not have, which is this rule's own bar for promotion. It stays here.

Proposed:

> Evidence from the field-app project, added 2026-10-16 (RECORD.md 2026-10-16-01): this rule's axis became its working partition, in a form one step finer than the table above. The operator decides behaviour, scope, design, wording, licences, merges and anything public. The planner decides technical routes that change nothing the operator would see or rule on, records each call, and says so in its next message. "When unsure which it is, it's the owner's". The research project descended from it labels such a row as the planner's call with "no rule changed". The field-app project departed from Role Partition in two recorded ways: its planner reads the repository and writes the record. It also added two roles the partition does not have: a read-only scout that answers questions about the repository without changing it, and an independent reviewer (rule 11). What has not been shown is a case this axis decided that the installed partition could not have, which is this rule's own bar for promotion. It stays here. Sources: trials/method-text-evidence-2026-11-17.md, rule 7.

**PROTOCOL.md:127** (rule 9)

Now:

> Forager evidence, added 2026-10-16 (RECORD.md 2026-10-16-01): the `committed:<sha256>` form appears 0 times in Forager's record of 1,275 entries. forager-forecast reached the same end, a choice provably fixed before the outcome, by public commits whose order a reviewer checks (rule 10). That route was used and this one was not; rule 10 is the working method, and this rule's withheld hash remains for a prediction that must stay hidden from the executor until it has run.

Proposed:

> Evidence from the field-app project, added 2026-10-16 (RECORD.md 2026-10-16-01): the `committed:<sha256>` form appears 0 times in its record of 1,275 entries. The research project descended from it reached the same end, a choice provably fixed before the outcome, by public commits whose order a reviewer checks (rule 10). That route was used and this one was not; rule 10 is the working method, and this rule's withheld hash remains for a prediction that must stay hidden from the executor until it has run. Sources: trials/method-text-evidence-2026-11-17.md, rule 9.

**PROTOCOL.md:137** (rule 10)

Now:

> Evidence: forager-forecast fixes its production seed and a 20-configuration tuning grid before any model is fit, rejecting the alternative because it "invites tuning until it wins" (`docs/planning/DECISIONS.md:101`, D31 at `b9127e5`), and does the same for its evaluation, filters and licence tracks (D33, D26, D29). Reviewers confirmed that the commit came before the first count in four cases. The rule held when the result pulled the other way (D109, D90), and caught a committed tolerance that would have failed before any value was read. Forager's planner profile carries the same rule: "Fix choices before data" (`docs/process/planner-profile.md:38` at `402489ae`).

Proposed:

> Evidence: the research project fixes its production seed and a 20-configuration tuning grid before any model is fit, rejecting the alternative because it "invites tuning until it wins", and does the same for its evaluation, filters and licence tracks. Reviewers confirmed that the commit came before the first count in four cases. The rule held when the result pulled the other way, and caught a committed tolerance that would have failed before any value was read. The field-app project's planner profile carries the same rule: "Fix choices before data". Sources: trials/method-text-evidence-2026-11-17.md, rule 10.

**PROTOCOL.md:145** (rule 11)

Now:

> Evidence: forager-forecast decision D18 (`docs/planning/DECISIONS.md:114` at `b9127e5`) and its standing review protocol (`docs/dispatch/2026-09-18-review-protocol.md`; the quoted sentence is at `:17`). It has 21 review files on main, 14 of which led to a fix, a correction or a decision traceable in its record (a reader session's classification, 17 of the 21 from index rows). In its decision D35, an independent review found two things the builder's self-check had missed, while the self-check re-ran a count the reviewer could not reach; both documents were kept, because each saw something the other could not. In Forager, an independent review caught 37 guessed record timestamps (record 2026-09-28-608). This repository's own record named the need first: RECORD.md 2026-08-15-04, Finding 1, "a single investigation is one sample, not a determination".

Proposed:

> Evidence: the research project's decision setting up independent review, and its standing review protocol. It has 21 review files on its main branch, 14 of which led to a fix, a correction or a decision traceable in its record (a reader session's classification, 17 of the 21 from index rows). In one of its decisions, an independent review found two things the builder's self-check had missed, while the self-check re-ran a count the reviewer could not reach; both documents were kept, because each saw something the other could not. In the field-app project, an independent review caught 37 guessed record timestamps. This repository's own record named the need first: RECORD.md 2026-08-15-04, Finding 1, "a single investigation is one sample, not a determination". Sources: trials/method-text-evidence-2026-11-17.md, rule 11.

**PROTOCOL.md:171** (rule 12)

Now:

> Evidence, all from Forager (trials/forager-2026-10-16.md):

Proposed:

> Evidence, all from the field-app project (trials/forager-2026-10-16.md; sources: trials/method-text-evidence-2026-11-17.md, rule 12):

**PROTOCOL.md:173** (rule 12)

Now:

> - Per-dispatch operator approval was removed four days after it began. The operator: "Can't have me hitting buttons. Those hooks need to change" (`docs/audits/2026-09-26-approval-exempt-build-device.md`).

Proposed:

> - Per-dispatch operator approval was removed four days after it began. The operator: "Can't have me hitting buttons. Those hooks need to change".

**PROTOCOL.md:174** (rule 12)

Now:

> - The whole hook kit was disabled and deleted on 2026-09-27. The operator's account, 2026-10-16: "The hooks were removed because actions agents are expected to perform were being hindered. The operator had to hold the agent's hand every step of the way, which was the opposite of the kit's intentions." (prompts/preserved/2026-10-16-03.md). The note written on 2026-09-27 records the operator's words then, "to work around weekly limits" (`docs/audits/2026-09-27-kit-hooks-disabled.md`). That note is the model for recording a removal: its section 3 lists what stops being enforced.

Proposed:

> - The whole hook kit was disabled and deleted on 2026-09-27. The operator's account, 2026-10-16: "The hooks were removed because actions agents are expected to perform were being hindered. The operator had to hold the agent's hand every step of the way, which was the opposite of the kit's intentions." (prompts/preserved/2026-10-16-03.md). The note written on 2026-09-27 records the operator's words then, "to work around weekly limits". That note is the model for recording a removal: its section 3 lists what stops being enforced.

**PROTOCOL.md:182** (rule 12)

Now:

> The operator ruled the loss of predictions to be drift, not a decision (prompts/preserved/2026-10-16-01.md), so Intent-Driven Engineering's prediction requirement stands unchanged. Forager is recorded as a gate lost once its checker was removed.

Proposed:

> The operator ruled the loss of predictions to be drift, not a decision (prompts/preserved/2026-10-16-01.md), so Intent-Driven Engineering's prediction requirement stands unchanged. The field-app project is recorded as a gate lost once its checker was removed.

**PROTOCOL.md:202** (rule 13)

Now:

> Evidence, from Forager (Forager `CLAUDE.md` at `402489ae` and trials/forager-2026-10-16.md):

Proposed:

> Evidence, from the field-app project and the research project descended from it (trials/forager-2026-10-16.md; sources: trials/method-text-evidence-2026-11-17.md, rule 13):

**PROTOCOL.md:204** (rule 13)

Now:

> - A planner session believed dead reconnected and kept writing to the same record branch, so two record IDs were each used twice (`docs/audits/2026-10-05-planner-handoff.md`).

Proposed:

> - A planner session believed dead reconnected and kept writing to the same record branch, so two record IDs were each used twice.

**PROTOCOL.md:205** (rule 13)

Now:

> - An entry was deleted with its ID declared retired, and the ID was used again 26 minutes later (Forager commits `0bda73e8` and `4805cb90`).

Proposed:

> - An entry was deleted with its ID declared retired, and the ID was used again 26 minutes later.

**PROTOCOL.md:206** (rule 13)

Now:

> - A hook numbered each preserved prompt by counting only its own checkout, so parallel worktrees took the same numbers (Forager `RECORD.md` on `main`, 2026-09-23 finding on the dispatch guard).

Proposed:

> - A hook numbered each preserved prompt by counting only its own checkout, so parallel worktrees took the same numbers.

**PROTOCOL.md:207** (rule 13)

Now:

> - Two branches each declared the same schema version with different migrations, which no file-level merge detects (Forager `CLAUDE.md`, the base-branch pitfall).

Proposed:

> - Two branches each declared the same schema version with different migrations, which no file-level merge detects.

**PROTOCOL.md:208** (rule 13)

Now:

> - The audit index conflicted on every push after the first when two sessions ran in parallel (Forager `CLAUDE.md`, the serialization-point pitfall).

Proposed:

> - The audit index conflicted on every push after the first when two sessions ran in parallel.

**PROTOCOL.md:209** (rule 13)

Now:

> - From forager-forecast: a decision filed on one branch had to be renumbered the same day, because the number had already been taken on another (`docs/planning/DECISIONS.md:17`, D123, at `b9127e5`).

Proposed:

> - From the research project: a decision filed on one branch had to be renumbered the same day, because the number had already been taken on another.

**PROTOCOL.md:227** (rule 14)

Now:

> - Forager's record held, at the first reading, 12 entry kinds, with 224 decisions and 330 continuations among 1,275 entries (fifteen by the second reading, trials/forager-2026-11-05.md).

Proposed:

> - The field-app project's record held, at the first reading, 12 entry kinds, with 224 decisions and 330 continuations among 1,275 entries (fifteen by the second reading, trials/forager-2026-11-05.md).

**PROTOCOL.md:228** (rule 14)

Now:

> - The operator had one entry deleted from it as clutter (Forager commit `0bda73e8`).

Proposed:

> - The operator had one entry deleted from it as clutter.

**PROTOCOL.md:229** (rule 14)

Now:

> - 63 of its intents have no terminal entry; 49 of those were continued instead (trials/forager-2026-10-16.md).

Proposed:

> - 63 of its intents have no entry closing them, counting a Closes field on any kind of entry, and 49 of those were continued instead (trials/forager-2026-10-16.md). Counted by terminal entries alone, the figures are 79 and 41 (trials/recount-2026-11-16.md).

**PROTOCOL.md:231** (rule 14)

Now:

> - forager-forecast's decision rows carry the provenance labels above (`docs/planning/DECISIONS.md` at `b9127e5`).

Proposed:

> - The research project's decision rows carry the provenance labels above. Sources: trials/method-text-evidence-2026-11-17.md, rule 14.

**PROTOCOL.md:235** (rule 14)

Now:

> Promoted 2026-10-16 into RECORDING.md (RECORD.md 2026-10-16-05), on the operator's ruling, with the twelve entry types kept as Forager used them rather than reduced to the two this rule proposed. The text above stays as written.

Proposed:

> Promoted 2026-10-16 into RECORDING.md (RECORD.md 2026-10-16-05), on the operator's ruling, with the twelve entry types kept as the field-app project used them rather than reduced to the two this rule proposed. The text above stays as written.

**PROTOCOL.md:247** (rule 15)

Now:

> Evidence: Forager's field-instrument skill states two governing rules in this order, "honesty is never traded for ease" and then "don't make me think" (`skills/examples/field-instrument-interface/SKILL.md`). The operator's design principle "Don't make me think" is recorded in Forager's `CLAUDE.md` (2026-09-30). The skill itself says three of its seven rules are inferred from the app's purpose and general practice, not from field data.

Proposed:

> Evidence: the field-app project's field-instrument skill states two governing rules in this order, "honesty is never traded for ease" and then "don't make me think" (`skills/examples/field-instrument-interface/SKILL.md`). The operator's design principle "Don't make me think" is recorded in that project's standing instructions (2026-09-30). The skill itself says three of its seven rules are inferred from the app's purpose and general practice, not from field data. Sources: trials/method-text-evidence-2026-11-17.md, rule 15.

**PROTOCOL.md:255** (rule 16)

Now:

> Evidence: a tree check counted the outcome labels correctly and never asked what one label meant. That label carried four reasons, one of which was the mechanism working, so a device check built on the count would have filed correct behaviour as a fault (Forager `CLAUDE.md`, testing section; index line 145). Three more instances in one week of a correct observation produced by an incorrect mechanism are at index line 165. Standing: four instances, in one project. This sits beside Severity of Checks: that principle asks whether a check could fail, and this asks what a passing check licenses.

Proposed:

> Evidence: a tree check counted the outcome labels correctly and never asked what one label meant. That label carried four reasons, one of which was the mechanism working, so a device check built on the count would have filed correct behaviour as a fault. Three more instances in one week of a correct observation produced by an incorrect mechanism are in the same project's audit index. Standing: four instances, in one project. This sits beside Severity of Checks: that principle asks whether a check could fail, and this asks what a passing check licenses. Sources: trials/method-text-evidence-2026-11-17.md, rule 16.

**PROTOCOL.md:261** (rule 17)

Now:

> Evidence: Forager, index line 110, where the operator ruled that this general form supersedes the instance it came from "because it predicts recurrence rather than recording one occurrence". Standing: one instance.

Proposed:

> Evidence: in the field-app project, the operator ruled that this general form supersedes the instance it came from "because it predicts recurrence rather than recording one occurrence". Standing: one instance. Sources: trials/method-text-evidence-2026-11-17.md, rule 17.

**PROTOCOL.md:267** (rule 18)

Now:

> Evidence: in Forager, an alias chosen for coder sessions resolved to a different model than the one the planner had told the operator (`docs/audits/2026-09-29-planner-handoff.md:55`). The operator later used two builds of one dispatch as a comparison between models: "we are measuring [model B] vs [model A]" (`docs/audits/2026-09-29-f5-landed-and-redo-compared.md`). Standing: two instances. If promoted, this extends Capture Environmental Context to the agents themselves.

Proposed:

> Evidence: in the field-app project, an alias chosen for coder sessions resolved to a different model than the one the planner had told the operator. The operator later used two builds of one dispatch as a comparison between models: "we are measuring [model B] vs [model A]". Standing: two instances. If promoted, this extends Capture Environmental Context to the agents themselves. Sources: trials/method-text-evidence-2026-11-17.md, rule 18.

**PROTOCOL.md:279** (rule 20)

Now:

> Evidence: Forager `CLAUDE.md`, testing section, where the rule is written. A coder deleted 26 tests without reporting it, and they were restored at the next merge (index line 335). Standing: two instances.

Proposed:

> Evidence: the field-app project's standing instructions, testing section, where the rule is written. A coder deleted 26 tests without reporting it, and they were restored at the next merge. Standing: two instances. Sources: trials/method-text-evidence-2026-11-17.md, rule 20.

**PROTOCOL.md:283** (rule 21)

Now:

> The operator's stated approach since Forager's hooks were removed: "So now I let philosophy, precise methodology, and evidence gating drive the agent" (2026-10-16, prompts/preserved/2026-10-16-03.md).

Proposed:

> The operator's stated approach since the field-app project's hooks were removed: "So now I let philosophy, precise methodology, and evidence gating drive the agent" (2026-10-16, prompts/preserved/2026-10-16-03.md).

**PROTOCOL.md:301** (rule 21)

Now:

> - Forager's release gate of 2026-10-16 is an evidence gate at a boundary: CI, both test phones, an advisory interface audit, and the operator's approval (Forager record 2026-09-28-1085 to -1087).

Proposed:

> - The field-app project's release gate of 2026-10-16 is an evidence gate at a boundary: CI, both test phones, an advisory interface audit, and the operator's approval.

**PROTOCOL.md:302** (rule 21)

Now:

> - forager-forecast's dependent tasks wait for their prerequisite's review to be filed (rule 11).

Proposed:

> - The research project's dependent tasks wait for their prerequisite's review to be filed (rule 11). Sources: trials/method-text-evidence-2026-11-17.md, rule 21.

**PROTOCOL.md:329** (rule 22)

Now:

> Evidence: Forager's docs/process/planner-profile.md, written on 2026-10-07 at the owner's request. Its planner was named from Forager's world, which is woods, foraging and wayfinding: "A rowan is the guardian tree at the edge of the woods. A waymark is the blaze that keeps the next walker on the trail." (planner-profile.md:5). The owner's words:

Proposed:

> Evidence: the field-app project's planner profile, written on 2026-10-07 at the operator's request. Its planner was named from that project's world, woods, foraging and wayfinding, with one plain line on why. The operator's words:

**PROTOCOL.md:331** (rule 22)

Now:

> - "That way each role can have a profile that models their behavior" (Forager record 2026-09-28-1141);

Proposed:

> - "That way each role can have a profile that models their behavior";

**PROTOCOL.md:333** (rule 22)

Now:

> - "EGD may adopt it but to make it general, the profiles should have the roles name themselves based on the project and its scope" (2026-09-28-1142).

Proposed:

> - "EGD may adopt it but to make it general, the profiles should have the roles name themselves based on the project and its scope". Sources: trials/method-text-evidence-2026-11-17.md, rule 22.

**PROTOCOL.md:337** (rule 22)

Now:

> Standing: one profile has been in use for about nine days; three more are being written in Forager, and E-GD's curator profile is new. Untested as a general method.

Proposed:

> Standing: one profile has been in use for about nine days; three more are being written in the field-app project, and E-GD's curator profile is new. Untested as a general method.

**PROTOCOL.md:349** (rule 23)

Now:

> - An experiments branch is production plus developer tools plus running experiments. It is rebased onto production after every release, "to reflect workability" (Forager record 2026-09-28-1087), and never merged anywhere. An experiment chosen to ship is carried onto the working branch without the tools.

Proposed:

> - An experiments branch is production plus developer tools plus running experiments. It is rebased onto production after every release, "to reflect workability", and never merged anywhere. An experiment chosen to ship is carried onto the working branch without the tools.

**PROTOCOL.md:360** (rule 23)

Now:

> A device check or field walk is proposed by the planner when a promotion needs one, and the operator decides. It is not a standing step: "Field walks and device checks aren't always necessary" (-1133). An urgent fix takes the same gate, at the front of the queue, and is then carried into the working branch.

Proposed:

> A device check or field walk is proposed by the planner when a promotion needs one, and the operator decides. It is not a standing step: "Field walks and device checks aren't always necessary". An urgent fix takes the same gate, at the front of the queue, and is then carried into the working branch.

**PROTOCOL.md:364** (rule 23)

Now:

> - **Who.** A fresh session for each promotion. It is never the session that built the work, and it runs on a different model from the one that built it, because "the same model shares blind spots" (-1134).

Proposed:

> - **Who.** A fresh session for each promotion. It is never the session that built the work, and it runs on a different model from the one that built it, because "the same model shares blind spots".

**PROTOCOL.md:371** (rule 23)

Now:

> - **"Advises, you decide"** (-1086). The verdict goes to the operator, who decides; it is not a veto. The auditor writes no product code, fixes and merges nothing, never weakens a test, and never settles a conflict between two of the operator's rulings: it puts both sides to the operator.

Proposed:

> - **"Advises, you decide"**. The verdict goes to the operator, who decides; it is not a veto. The auditor writes no product code, fixes and merges nothing, never weakens a test, and never settles a conflict between two of the operator's rulings: it puts both sides to the operator.

**PROTOCOL.md:372** (rule 23)

Now:

> - **Devices.** A real device comes first. An emulator run is labelled "emulator, not a device", and what an emulator cannot stand in for is listed (-1094).

Proposed:

> - **Devices.** A real device comes first. An emulator run is labelled "emulator, not a device", and what an emulator cannot stand in for is listed.

**PROTOCOL.md:374** (rule 23)

Now:

> **The QA philosophy it audits against.** If none exists, the auditor's first task is to draft one (-1085):

Proposed:

> **The QA philosophy it audits against.** If none exists, the auditor's first task is to draft one:

**PROTOCOL.md:378** (rule 23)

Now:

> - an adopted proposal stays marked as adopted from the auditor's proposal, never as the operator's words (-1092, -1097).

Proposed:

> - an adopted proposal stays marked as adopted from the auditor's proposal, never as the operator's words.

**PROTOCOL.md:382** (rule 23)

Now:

> **Sources.** Forager's planner wrote the framework for this repository: prompts/preserved/2026-10-16-05-auditor-framework-for-egd.md and its addendum, -05b, on Forager's origin/records-after-173 (f09ff09c, 7d6cdd45). They are cited there rather than copied here. Where the addendum changed the original, this rule follows the addendum: the original lists a device check as step 2 of the gate, and the addendum removes it (-1133). The owner's view of the whole: "the rules we have are simply what we already do. Just codified" (-1138).

Proposed:

> **Sources.** The field-app project's planner wrote the framework for this repository, with an addendum. Both are cited in trials/method-text-evidence-2026-11-17.md, rule 23, rather than copied here. Where the addendum changed the original, this rule follows the addendum: the original lists a device check as step 2 of the gate, and the addendum removes it. The owner's view of the whole: "the rules we have are simply what we already do. Just codified".

**PROTOCOL.md:386** (rule 23)

Now:

> Standing: one promotion has run through the gate. It was documents only, and passed with two notes on the planner's own documents, neither blocking (-1131, -1132). No release with code has been audited, and the device path is untested.

Proposed:

> Standing: one promotion has run through the gate. It was documents only, and passed with two notes on the planner's own documents, neither blocking. No release with code has been audited, and the device path is untested.

**PROTOCOL.md:446** (rule 30)

Now:

> Rules 10 onward were added on 2026-10-16 (RECORD.md 2026-10-16-01) from the records of Forager and forager-forecast (trials/forager-2026-10-16.md). Their evidence comes from one further project family, read after the fact. It is not a test in this repository, and none of them is enforced by a check.

Proposed:

> Rules 10 onward were added on 2026-10-16 (RECORD.md 2026-10-16-01) from the records of a field-app project and a research project descended from it (trials/forager-2026-10-16.md). Their evidence comes from one further project family, read after the fact. It is not a test in this repository, and none of them is enforced by a check.

### RECORDING.md

**RECORDING.md:5** (top)

Now:

> It was adopted on 2026-10-16 (RECORD.md 2026-10-16-05), on the operator's ruling, from Forager's record. There these methods ran for about four weeks and 1,275 entries (trials/forager-2026-10-16.md). The operator, on the methods: "These recording methods have been invaluable" (prompts/preserved/2026-10-16-05.md).

Proposed:

> It was adopted on 2026-10-16 (RECORD.md 2026-10-16-05), on the operator's ruling, from the record of a field-app project, called here the source project. There these methods ran for about four weeks and 1,275 entries (trials/forager-2026-10-16.md). The operator, on the methods: "These recording methods have been invaluable" (prompts/preserved/2026-10-16-05.md). The project paths and record IDs that stood in this document until 2026-11-17 are kept verbatim in trials/method-text-evidence-2026-11-17.md (RECORD.md 2026-11-05-03).

**RECORDING.md:7** (top)

Now:

> Two of the entry types, intent and terminal, are this repository's own. Three more, continuation, merge and dispatch-note, were first defined in the checker of Claude-kit v0.2, the kit that carried this method's gates into Forager as harness hooks; the kit also added partial to the terminal outcomes. The other seven are written down here for the first time, from how Forager used them. Each type below says which it is.

Proposed:

> Two of the entry types, intent and terminal, are this repository's own. Three more, continuation, merge and dispatch-note, were first defined in the checker of Claude-kit v0.2, the kit that carried this method's gates into the source project as harness hooks; the kit also added partial to the terminal outcomes. The other seven are written down here for the first time, from how the source project used them. Each type below says which it is.

**RECORDING.md:12** (What every entry carries)

Now:

> - **Who wrote it, and where.** A closing `Notes` line such as "Written by the planner by hand, on branch records-after-173". 1,004 of Forager's 1,275 entries carry one.

Proposed:

> - **Who wrote it, and where.** A closing `Notes` line such as "Written by the planner by hand, on branch records". 1,004 of the source project's 1,275 entries carry one.

**RECORDING.md:13** (What every entry carries)

Now:

> - **The next free ID**, wherever IDs can collide between parallel sessions or branches. It is stated at the end of the entry and checked against the remote before it is used (PROTOCOL rule 13). 548 of Forager's entries name it.

Proposed:

> - **The next free ID**, wherever IDs can collide between parallel sessions or branches. It is stated at the end of the entry and checked against the remote before it is used (PROTOCOL rule 13). 548 of the source project's entries name it.

**RECORDING.md:28** (Entry types)

Now:

> Twelve, kept as Forager used them, synonyms included, by the operator's ruling ("Keep all twelve", prompts/preserved/2026-10-16-05.md). Where two types overlap, both are described as Forager wrote them, and the overlap is stated. Counts are from Forager's record at `97f26098`. "(this repository)" marks the two this repository's record already had, "(kit)" the three Claude-kit v0.2 added, and "(practice)" the seven defined here from Forager's usage. Projects add kinds of their own as they need them. A kind enters this method only when it is harvested and approved; until then it stays the project's (trials/forager-2026-11-05.md, R5).

Proposed:

> Twelve, kept as the source project used them, synonyms included, by the operator's ruling ("Keep all twelve", prompts/preserved/2026-10-16-05.md). Where two types overlap, both are described as the source project wrote them, and the overlap is stated. Counts are from its record at the first reading (trials/forager-2026-10-16.md). "(this repository)" marks the two this repository's record already had, "(kit)" the three Claude-kit v0.2 added, and "(practice)" the seven defined here from the source project's usage. Projects add kinds of their own as they need them. A kind enters this method only when it is harvested and approved; until then it stays the project's (trials/forager-2026-11-05.md, R5).

**RECORDING.md:30** (intent (this repository) — 243 in Forager)

Now:

> ### intent (this repository) — 243 in Forager

Proposed:

> ### intent (this repository) — 243 in the source project

**RECORDING.md:40** (terminal (this repository; partial from the kit) — 166 in Forager)

Now:

> ### terminal (this repository; partial from the kit) — 166 in Forager

Proposed:

> ### terminal (this repository; partial from the kit) — 166 in the source project

**RECORDING.md:53** (continuation (kit) — 330 in Forager)

Now:

> ### continuation (kit) — 330 in Forager

Proposed:

> ### continuation (kit) — 330 in the source project

**RECORDING.md:61** (decision (practice) — 224 in Forager)

Now:

> ### decision (practice) — 224 in Forager

Proposed:

> ### decision (practice) — 224 in the source project

**RECORDING.md:78** (outcome (practice) — 40 in Forager)

Now:

> ### outcome (practice) — 40 in Forager

Proposed:

> ### outcome (practice) — 40 in the source project

**RECORDING.md:85** (observation (practice) — 21 in Forager)

Now:

> ### observation (practice) — 21 in Forager

Proposed:

> ### observation (practice) — 21 in the source project

**RECORDING.md:91** (finding (practice) — 3 in Forager)

Now:

> ### finding (practice) — 3 in Forager

Proposed:

> ### finding (practice) — 3 in the source project

**RECORDING.md:98** (device-note (practice) — 11 in Forager)

Now:

> ### device-note (practice) — 11 in Forager

Proposed:

> ### device-note (practice) — 11 in the source project

**RECORDING.md:109** (correction (practice) — 13 in Forager)

Now:

> ### correction (practice) — 13 in Forager

Proposed:

> ### correction (practice) — 13 in the source project

**RECORDING.md:116** (merge (kit) — 91 in Forager)

Now:

> ### merge (kit) — 91 in Forager

Proposed:

> ### merge (kit) — 91 in the source project

**RECORDING.md:129** (dispatch-note (kit) — 128 in Forager)

Now:

> ### dispatch-note (kit) — 128 in Forager

Proposed:

> ### dispatch-note (kit) — 128 in the source project

**RECORDING.md:142** (handoff (practice) — 5 in Forager)

Now:

> ### handoff (practice) — 5 in Forager

Proposed:

> ### handoff (practice) — 5 in the source project

**RECORDING.md:35** (intent (this repository) — 243 in Forager)

Now:

> - **The prediction is required.** Forager's intents stopped carrying predictions, finish lines and abort conditions after its checker was removed; the cause is inferred, not recorded. The operator ruled that drift, not a decision (prompts/preserved/2026-10-16-01.md), so the requirement stands.

Proposed:

> - **The prediction is required.** The source project's intents stopped carrying predictions, finish lines and abort conditions after its checker was removed; the cause is inferred, not recorded. The operator ruled that drift, not a decision (prompts/preserved/2026-10-16-01.md), so the requirement stands.

**RECORDING.md:51** (terminal (this repository; partial from the kit) — 166 in Forager)

Now:

> - **Forager's usage:** completed 150, abandoned 6, superseded 5, partial 3. It also wrote "parked" and "both" once each. No outcome list allows those, and this method does not adopt them.

Proposed:

> - **The source project's usage:** completed 150, abandoned 6, superseded 5, partial 3. It also wrote "parked" and "both" once each. No outcome list allows those, and this method does not adopt them.

**RECORDING.md:57** (continuation (kit) — 330 in Forager)

Now:

> - **Fields:** `Continues`, naming an intent still open at that point in the record. The kit's form adds `Dispatch-file`, `Reason` and `Changes`; 26% of Forager's continuations carry them. The rest record the step in prose.

Proposed:

> - **Fields:** `Continues`, naming an intent still open at that point in the record. The kit's form adds `Dispatch-file`, `Reason` and `Changes`; 26% of the source project's continuations carry them. The rest record the step in prose.

**RECORDING.md:59** (continuation (kit) — 330 in Forager)

Now:

> - **It never stands in for a terminal.** 49 of the 63 Forager intents that have no terminal had been continued instead, so their status still reads as open.

Proposed:

> - **It never stands in for a terminal.** In the source project, 63 intents had no entry closing them, counting a `Closes` field on any kind of entry, and 49 of those had been continued instead, so their status still reads as open. Counted by terminal entries alone, the figures are 79 and 41 (trials/recount-2026-11-16.md).

**RECORDING.md:65** (decision (practice) — 224 in Forager)

Now:

> - **Fields as Forager used them:**

Proposed:

> - **Fields as the source project used them:**

**RECORDING.md:71** (decision (practice) — 224 in Forager)

Now:

> - **Practices seen in Forager and adopted:**

Proposed:

> - **Practices seen in the source project and adopted:**

**RECORDING.md:76** (decision (practice) — 224 in Forager)

Now:

> - **Who decided** is labelled: the operator's ruling, quoted; a planner's call within a delegation; proposed; or provisional until review. These are forager-forecast's labels (`docs/planning/DECISIONS.md`).

Proposed:

> - **Who decided** is labelled: the operator's ruling, quoted; a planner's call within a delegation; proposed; or provisional until review. These are the labels of a research project in the same family.

**RECORDING.md:96** (finding (practice) — 3 in Forager)

Now:

> - **Overlap with observation:** two Forager sessions once wrote a finding and an observation about the same event under the same ID. A correction entry then said which to cite.

Proposed:

> - **Overlap with observation:** two of the source project's sessions once wrote a finding and an observation about the same event under the same ID. A correction entry then said which to cite.

**RECORDING.md:127** (merge (kit) — 91 in Forager)

Now:

> - About 70% of Forager's merge entries carry `PR`, `Head`, `Base`, `Merge-commit`, `Pre-merge` and `Backup`; 28% carry `Merged-by` and `Carries`.

Proposed:

> - About 70% of the source project's merge entries carry `PR`, `Head`, `Base`, `Merge-commit`, `Pre-merge` and `Backup`; 28% carry `Merged-by` and `Carries`.

**RECORDING.md:133** (dispatch-note (kit) — 128 in Forager)

Now:

> - **The kit's form,** about a third of Forager's:

Proposed:

> - **The kit's form,** about a third of the source project's:

**RECORDING.md:139** (dispatch-note (kit) — 128 in Forager)

Now:

> - **Forager's later form,** about two thirds: a change to a dispatch already running. Fields: `Dispatch` (the dispatch changed), `Reason`, `Changes`, and the operator's answer.

Proposed:

> - **The source project's later form,** about two thirds: a change to a dispatch already running. Fields: `Dispatch` (the dispatch changed), `Reason`, `Changes`, and the operator's answer.

**RECORDING.md:159** (Backups before merges)

Now:

> Sources: Forager's accountability design (`docs/process/accountability-design.md`, "Where backups live"), and the merge procedure of Claude-kit v0.2. 74% of Forager's merge entries name a backup.

Proposed:

> Sources: the source project's accountability design ("Where backups live"), and the merge procedure of Claude-kit v0.2. 74% of the source project's merge entries name a backup.

**RECORDING.md:170** (The index)

Now:

> Forager's index is `docs/audits/README.md`, with 356 dated rows at `402489ae`. A project that files every dispatch in one folder and indexes it in one table avoids a second index drifting out of step with the first, as long as every new dispatch gets its row. One project's index went unchanged while its later dispatches went unindexed (trials/forager-2026-11-05.md, R3).

Proposed:

> The source project's index held 356 dated rows at the first reading. A project that files every dispatch in one folder and indexes it in one table avoids a second index drifting out of step with the first, as long as every new dispatch gets its row. One project's index went unchanged while its later dispatches went unindexed (trials/forager-2026-11-05.md, R3).

**RECORDING.md:186** (Reports)

Now:

> Source: Forager's planner operating guide of 2026-08-25, which asked of every report "the disclosure norm: confirmed vs. inferred, could-not-determine, any premise that turned out wrong, anything decided the dispatch didn't cover" (`docs/qc/planner-operating-guide-2026-08-25.md`). The first four were in use in roughly 90 to 100 of Forager's 258 audit documents, with nothing enforcing them (pattern counts). The fifth comes from Forager's finding of 2026-09-12: four findings existed only in transcripts, and only one of 80 reports had a slot for something noticed in passing (Forager's audit index, line 113 at `402489ae`). This method added it on 2026-10-16 (Durability Is Location).

Proposed:

> Source: the source project's planner operating guide of 2026-08-25, which asked of every report "the disclosure norm: confirmed vs. inferred, could-not-determine, any premise that turned out wrong, anything decided the dispatch didn't cover". The first four were in use in roughly 90 to 100 of its 258 audit documents, with nothing enforcing them (pattern counts). The fifth comes from its finding of 2026-09-12: four findings existed only in transcripts, and only one of 80 reports had a slot for something noticed in passing. This method added it on 2026-10-16 (Durability Is Location).

**RECORDING.md:192** (Layout: one file per month)

Now:

> - **An entry's month is the month of its Timestamp, in UTC, not its ID.** An ID scheme can freeze its date: Forager's IDs have begun `2026-09-28` since that day, so its 777 October entries carry September IDs. An entry with no Timestamp goes in the month of the entries around it.

Proposed:

> - **An entry's month is the month of its Timestamp, in UTC, not its ID.** An ID scheme can freeze its date: the source project's IDs have begun `2026-09-28` since that day, so its 777 October entries carry September IDs. An entry with no Timestamp goes in the month of the entries around it.

**RECORDING.md:195** (Layout: one file per month)

Now:

> - **Links may point into an earlier month.** `Continues`, `Closes`, `Corrects` and `Supersedes` are resolved across all the files. In Forager, 10 of 709 such links crossed the first month boundary.

Proposed:

> - **Links may point into an earlier month.** `Continues`, `Closes`, `Corrects` and `Supersedes` are resolved across all the files. In the source project, 10 of 709 such links crossed the first month boundary.

**RECORDING.md:202** (Layout: one file per month)

Now:

> - **What it does not fix.** Two sessions writing at once still meet in the current month's file (PROTOCOL rule 13). A busy month is still large: Forager's October reached about 8,500 lines in its first 16 days.

Proposed:

> - **What it does not fix.** Two sessions writing at once still meet in the current month's file (PROTOCOL rule 13). A busy month is still large: the source project's October reached about 8,500 lines in its first 16 days.

**RECORDING.md:210** (Accepting a past violation)

Now:

> - **The field.** `Accepts-violation`, with one line per commit: the commit's hash, 7 or more hex characters, then the reason. For example: `0bda73e8 RECORD -638 removed at the owner's instruction`.

Proposed:

> - **The field.** `Accepts-violation`, with one line per commit: the commit's hash, 7 or more hex characters, then the reason. For example: `1a2b3c4d RECORD 2026-01-15-07 removed at the operator's instruction`.

**RECORDING.md:242** (This repository's own record)

Now:

> - **Longer IDs.** IDs may carry two or more digits after the date, as Forager's do.

Proposed:

> - **Longer IDs.** IDs may carry two or more digits after the date, as the source project's do.

**RECORDING.md:251** (This repository's own record)

Now:

> Forager kept all twelve types without a checker after 2026-09-27. Run later from copies, its old checkers reported 1,646 entry errors (Forager record 2026-09-28-544). Much of that figure is types the old checkers did not know, so it measures the gap between practice and checker, not only mistakes.

Proposed:

> The source project kept all twelve types without a checker after 2026-09-27. Run later from copies, its old checkers reported 1,646 entry errors. Much of that figure is types the old checkers did not know, so it measures the gap between practice and checker, not only mistakes.

### README.md

**README.md:37** (What's here)

Now:

> | `lookups/` | Machines | Lookup configs for `records_lookup.py`, chosen with `--preset`: `forager.json` reads Forager's and forager-forecast's records. |

Proposed:

> | `lookups/` | Machines | Lookup configs for `records_lookup.py`, chosen with `--preset`. One preset ships, for the operator's own projects. |

**README.md:66** (What it has actually been through)

Now:

> A second project has since run it. Forager, a field app, adopted the method in September 2026, installed its gates as harness hooks on 2026-09-22, removed them five days later because they blocked actions the agents were expected to take, leaving the operator to hold the agent's hand at every step, and kept going without them. What fired, what was dropped, and what decayed once the checkers were gone is in `trials/forager-2026-10-16.md`. Its lessons are what the October 2026 changes to the philosophy and the protocol rest on.

Proposed:

> A second project has since run it. A field app adopted the method in September 2026, installed its gates as harness hooks on 2026-09-22, removed them five days later because they blocked actions the agents were expected to take, leaving the operator to hold the agent's hand at every step, and kept going without them. What fired, what was dropped, and what decayed once the checkers were gone is in `trials/forager-2026-10-16.md`. Its lessons are what the October 2026 changes to the philosophy and the protocol rest on.

### ADOPTING.md

**ADOPTING.md:148** (Accepting a past violation)

Now:

>     0bda73e8 an entry removed at the owner's instruction

Proposed:

>     1a2b3c4d an entry removed at the owner's instruction

**ADOPTING.md:149** (Accepting a past violation)

Now:

>     bebeb573 an entry written inside a merge, kept as it was

Proposed:

>     5e6f7a8b an entry written inside a merge, kept as it was

**ADOPTING.md:260** (The lookup tool)

Now:

> **More sources, in any repositories,** come from a lookup config given with `--config FILE`. `--print-config` prints the config in use, and `--preset forager` loads `lookups/forager.json`, which reads Forager's and forager-forecast's records. A config names:

Proposed:

> **More sources, in any repositories,** come from a lookup config given with `--config FILE`. `--print-config` prints the config in use, and `--preset NAME` loads `lookups/NAME.json`. One preset ships, for the operator's own projects. A config names:

### profiles/curator.md

**profiles/curator.md:16** (The role)

Now:

> - **The curator writes nothing in another project's repository.** Text meant for Forager is written into this record and handed to the operator, for Forager's own planner to place (2026-10-16-07, -08, -18).

Proposed:

> - **The curator writes nothing in another project's repository.** Text meant for a project is written into this record and handed to the operator, for that project's own planner to place (2026-10-16-07, -08, -18).

**profiles/curator.md:37** (Checking from source)

Now:

> - **Read a source before recommending on it,** for example forager-forecast's session log (2026-10-16-13, -14).

Proposed:

> - **Read a source before recommending on it,** for example a project's session log (2026-10-16-13, -14).

**profiles/curator.md:38** (Checking from source)

Now:

> - **Look at every branch that holds a record before planning a change to it.** That is how the divergence between Forager's two record branches was found (2026-10-16-18).

Proposed:

> - **Look at every branch that holds a record before planning a change to it.** That is how the divergence between one project's two record branches was found (2026-10-16-18).

**profiles/curator.md:70** (Talking to the operator)

Now:

> - **Lead with the outcome,** then what it means, then the one decision needed. Describe behaviour and consequences, not code names. These are the operator's preferences as Forager's planner profile records them ("Asking the owner" and "Talking to the owner", docs/process/planner-profile.md on Forager's pre-main), followed here.

Proposed:

> - **Lead with the outcome,** then what it means, then the one decision needed. Describe behaviour and consequences, not code names. These are the operator's preferences as a project's planner profile records them, followed here.

### skills/README.md

**skills/README.md:48** (Example: a project-specific skill)

Now:

> `examples/field-instrument-interface/` is Forager's interface rules for a field app, built on these principles: honesty is never traded for ease, then "don't make me think". It is here as an example of deriving a project's own skill from the general ones, not as a general skill. It bears on Truthful Interface Contracts and Explicit Failure Reporting, and on PROTOCOL rule 15. It says itself which of its rules are inferred rather than drawn from field data.

Proposed:

> `examples/field-instrument-interface/` is one project's interface rules for a field app, built on these principles: honesty is never traded for ease, then "don't make me think". It is here as an example of deriving a project's own skill from the general ones, not as a general skill. It bears on Truthful Interface Contracts and Explicit Failure Reporting, and on PROTOCOL rule 15. It says itself which of its rules are inferred rather than drawn from field data.

**skills/README.md:64** (Found while copying, not changed)

Now:

> Forager keeps untracked local copies of nine of these skills. Three of them (completion-report, dispatch-authoring, prior-art-before-interface) are older than the account's and lack the Conventions field the account versions added. They were reported to the operator and not touched.

Proposed:

> One project keeps untracked local copies of nine of these skills. Three of them (completion-report, dispatch-authoring, prior-art-before-interface) are older than the account's and lack the Conventions field the account versions added. They were reported to the operator and not touched.

**skills/README.md:67** (Edits made here after copying)

Now:

> - `revert-check`, protocol step 5: after restoring, confirm the forward change is still present. From Forager's CLAUDE.md, where a restore from git discarded an uncommitted change the check had just vouched for. The account copy does not have this edit.

Proposed:

> - `revert-check`, protocol step 5: after restoring, confirm the forward change is still present. From a project's standing instructions, where a restore from git discarded an uncommitted change the check had just vouched for. The account copy does not have this edit.

**skills/README.md:68** (Edits made here after copying)

Now:

> - `failing-test-first`, after "Read the message and say why it is the right one.": the red must come from the same unchanged test that later goes green. From Forager's "red that proves nothing" (its audit index, 2026-09-12), where the rule was followed and the red still belonged to an earlier version of the test. Corrected in a follow-up commit to say the test was edited after the fix, and that a red counts only if the same test could have passed. The account copy does not have this edit.

Proposed:

> - `failing-test-first`, after "Read the message and say why it is the right one.": the red must come from the same unchanged test that later goes green. From a project's finding of 2026-09-12, "red that proves nothing", where the rule was followed and the red still belonged to an earlier version of the test. Corrected in a follow-up commit to say the test was edited after the fix, and that a red counts only if the same test could have passed. The account copy does not have this edit.

### DURABILITY.md

**DURABILITY.md:58** (The rule)

Now:

> Promoted on 2026-10-16 to PHILOSOPHY.md as Durability Is Location, with Forager's instances (RECORD.md 2026-10-16-01; trials/forager-2026-10-16.md).

Proposed:

> Promoted on 2026-10-16 to PHILOSOPHY.md as Durability Is Location, with a field-app project's instances (RECORD.md 2026-10-16-01; trials/forager-2026-10-16.md).

### ENFORCEMENT.md

**ENFORCEMENT.md:23** (Minimal Required Infrastructure)

Now:

> 4. **Identity function.** One canonical content-hash routine for the project's data artifacts, owned in one module, used everywhere identity is needed. No second implementation is ever written; consumers import the one that exists. Conditional: this applies where the project's outputs are data artifacts whose identity matters, such as measurements, datasets or derived files. A project whose outputs are not such artifacts records that it has no identity function and why; Forager, an app, declined it on those grounds (trials/forager-2026-10-16.md). Made conditional 2026-10-16 under RECORD.md 2026-10-16-01.

Proposed:

> 4. **Identity function.** One canonical content-hash routine for the project's data artifacts, owned in one module, used everywhere identity is needed. No second implementation is ever written; consumers import the one that exists. Conditional: this applies where the project's outputs are data artifacts whose identity matters, such as measurements, datasets or derived files. A project whose outputs are not such artifacts records that it has no identity function and why; one project, an app, declined it on those grounds (trials/forager-2026-10-16.md). Made conditional 2026-10-16 under RECORD.md 2026-10-16-01.

### Kept as they are

- **ADOPTING.md:216**: a generic example config ("docs/dispatches"), not a project reference.
- **ADOPTING.md:284**: a generic example config ("app audits", "docs/audits/README.md"), not a project reference.
- **DURABILITY.md:13**: this repository's own history: the other workspace that kept the last fragment of its first record.
- **DURABILITY.md:14**: this repository's own history, as above.
- **DURABILITY.md:26**: this repository's own history, as above.
- **ONBOARDING.md:26**: a generic example path ("docs/process/operator-profile.md"), not a project reference.
- **CLAUDE.md:3**: standing instructions for agents in this repository, naming the operator's other workspace; not method text.
