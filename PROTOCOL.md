# Working Protocol

Rules governing how the operator, planner and coder work together that have not yet earned a place in PHILOSOPHY.md. Rules 1 through 9 were untested when written; nothing in them had been run even once. Rules 10 onward were added on 2026-10-16 from a second project's record, and each states its own evidence and standing. A rule promoted into the philosophy keeps its text here, with a note saying where it went.

These are not principles. PHILOSOPHY.md holds rules that have earned their place; this document holds rules that have not. They live apart on purpose: a rule installed in the philosophy can only be removed by archival, and these are likely enough to be wrong that installing them would be building ahead of the evidence.

## Where these came from

The planning role in this project has no access to the repository. It cannot read a file, run a check, or observe a commit. Every claim it makes about repository state comes from memory of what it dispatched rather than from what exists.

That produced ten errors of one shape: a file asserted to exist that did not, an entry ID asserted free that was taken, a task asserted complete that never ran, a count asserted from a running list rather than from the record, a finding number cited that was never real. Each was caught by an executing agent stopping to ask or by a read-only audit. None by a check.

The condition underneath is worth stating plainly, because the rules only make sense against it: the planning role cannot distinguish memory from observation. A false claim about repository state does not feel like a guess. It feels exactly like knowing.

## The rules

**1. The planner asserts no repository state.**

The planner does not state what a file contains, which IDs are in use, what a prior task produced, or whether something exists. Where a determination depends on state, the planner names where to look and defers the determination to whoever can look.

In practice this means writing "confirm the archive count and use what you find" rather than "the archive contains two entries." Both point at the same place. Only one can be wrong.

Promoted 2026-10-16 into PHILOSOPHY.md's Sourced Claims (RECORD.md 2026-10-16-01), with rule 2. Forager gave its planner read access to remove this rule's premise and the premise held anyway: at least 24 of its record entries describe planner slips about repository state, and a claim that a file had zero references decayed inside its own pull request (trials/forager-2026-10-16.md; Forager CLAUDE.md at 402489ae, the pitfall on a planner's picture of the repository). The text above stays as written.

**2. State reaches the planner at task boundaries, carrying a commit hash.**

Before drafting a prompt, the operator passes the planner the files that prompt will concern. Every passback names the commit it came from.

Claims made from a passback cite that hash: "as of 7c6f32f, RECORD.md holds 20 entries." A claim that cannot name its source is unsourced whether or not a file was read.

A snapshot expires at the next commit. During a task the executor is authoritative for anything that changed, and the planner makes no new state claims.

Where a prompt would dictate edits to a file the planner has not been passed at the current hash, the planner says so and stops. Working from memory is the failure this rule exists to prevent, and doing it while holding a stale file is worse, because it looks sourced.

Promoted 2026-10-16 into PHILOSOPHY.md's Sourced Claims (RECORD.md 2026-10-16-01), with rule 1. Forager's practice is this rule's general form: a dispatch states the base commit it assumes, and the executing session verifies that base before acting on any claim about what exists. The text above stays as written.

**3. Investigation precedes planning.**

For work whose shape depends on repository state, the sequence is: the executor investigates and reports what it found, together with candidate options; the planner adjudicates and drafts; the operator approves; the executor acts.

The report carries findings alongside options, not options alone. An option set is a framing, and a framing constrains the answer. The planner needs to see what was found in order to judge whether the options exhaust it.

The executor proposes. It does not choose. Choosing is the planner's and approving is the operator's, and this sequence changes what the planner reasons over, not who decides.

This costs a round trip. It is worth paying where the plan would otherwise rest on remembered state, and not worth paying where the relevant facts are already in front of the executor.

**4. Every factual claim in a proposed entry is checked before it lands.**

Errors before a write to an append-only store are cheap. Errors after are permanent: nothing can be corrected, only appended beside.

So before appending any entry, each factual claim in it is verified against the repository. Identifiers appear where claimed. Quoted text matches its source. Counts match what is actually there.

Two defects in this project's own store came from skipping this: a cited finding number that was invented, and an archive entry whose claim contradicted the text quoted directly beneath it. Neither was caught by a check or by the agent that wrote it. Both are immutable now.

**5. A constant standing in for the world is a claim about the world.**

A hardcoded value, a mock, or a fixture representing hardware or specimen properties asserts something about reality, written in the visual language of code. A test suite built around an assumed sensor behavior is evidence about the assumption, not about the sensor, and the two look identical.

The test for whether a value falls under this rule: would a different sensor, specimen, or optical setup make it wrong? A CFA pattern, a white level, a pixel pitch, a fixture's quad means all answer yes. A loop bound, a buffer size, a string length answer no.

Values that answer yes carry their source: a capture identifier, a datasheet reference, or the literal marker `assumed`. An agent introducing one states which. A value marked `assumed` does not reach a reported result without the operator ruling on it.

The executor cannot verify these by any amount of care or capability, because it cannot observe the thing being claimed. That is what distinguishes them from every other claim in the codebase.

Evidence, added 2026-10-16 (RECORD.md 2026-10-16-01): Forager supports this rule's premise at n of 5 or more. A simulated test environment reported zero for a quantity that is never zero on a device, and a fixed constant matching that zero passed the suite and failed on the device. A fake camera defaulted to ready, so the deadlock under test could not be represented. A test harness supplied a value from outside the component under test. A device reported a constant positional accuracy. The `assumed` marker this rule prescribes was never tried there, so the marking practice is still untested. Severity of Checks now carries the premise as a principle; this rule stays here for its marking practice.

**6. Deciding above your authority produces output identical to deciding within it.**

A role that decides something it was not authorized to decide leaves no mark. The build is coherent, the checks pass, and no later inspection of the artifact recovers where the decision was made. This is why the prohibitions in this project depend on an agent stopping to ask rather than on anything downstream catching it.

An agent that finds itself choosing rather than executing reports it at that moment, naming what it decided and what would have been needed to decide it properly. This is reported even when the decision was correct, because correctness is not what is being tracked.

Stated limit: this rule asks an agent to notice something that may not feel like a decision. The planning role in this project asserted repository state eleven times, and each time it felt like knowing rather than choosing. If self-detection were reliable, the prohibition would already work. This is a habit worth cultivating, not a detection mechanism, and it should not be counted as one.

**7. Roles divide by what a decision depends on, not by task type.**

| The decision depends on | Belongs to |
|---|---|
| The supplied text and code alone | Executor |
| Goals and tradeoffs | Planner proposes, operator ratifies |
| The physical world, or what counts as true | Operator, non-delegable |

This axis is decidable: a decision can be placed on it, and disagreements about placement are arguable rather than a matter of taste.

Stated standing: this is a replacement for Role Partition, not a supplement to it. It is here rather than in PHILOSOPHY.md because replacing a load-bearing principle on the strength of an untested draft is what Evidence-Based Feature Addition exists to prevent. It is promoted only if it decides cases the installed partition cannot, and that has not been demonstrated.

**8. A record is testimony about a source, not the source.**

An intent entry is written from a prompt. A changelog entry is written from a diff. Both are faithful until they aren't, and a check consulting the derived copy verifies against whatever the transcription said rather than against what was actually specified.

Before consulting a record for a working reference — a baseline commit, a scope boundary, a stated parameter — look for the source it was derived from. Prompts are persisted in `prompts/`; diffs are in git. Use the source.

Where the source cannot be found, the derived copy is not used as a substitute. If the reference is required to complete the task, stop and report which source was missing and what needed it. If it is not required, proceed without it and report the same. A check that could not reach its source did not run, and reporting it as having run against a copy is worse than not running it.

This does not diminish the record. A record's authority is historical: it says what was intended at the time, and nothing else can say that. Using it as a live reference during work is asking it for something it was never the best source of.

Standing: this rule is deliberately over-strict. Its boundary has not been mapped, and it is expected to stop work that could have proceeded. Such a stop is a finding, not a fault. When the operator rules a stop unnecessary, the condition is appended below as a named caveat stating what was missing, what needed it, and why proceeding was acceptable. The rule accumulates its own boundary through use.

Caveats discovered: none yet.

**9. An entry's closing conditions are fixed at dispatch, not discovered at close.**

Nothing an entry needs in order to close may arrive after its terminal entry. A field whose resolving value can only land in a terminal entry that is already committed leaves the entry permanently unresolvable, and an append-only store cannot repair it.

The outcome prediction slot therefore takes one of exactly two values in the intent entry:

`committed:<sha256>` — a prediction exists and is withheld. The digest proves it existed at dispatch and tells the executor nothing. Plaintext is released after the executor's mechanism prediction is committed and before the terminal entry is written. The terminal entry carries the plaintext and the result of hashing it against the digest.

`not authored` — no prediction exists. The terminal entry closes the intent on its own. The prediction's uses are null, and every consumer reports them as null rather than as pending.

Where a prediction was committed and plaintext never arrives, the terminal entry records `committed, unreleased`. The entry closes. The digest stands as evidence a prediction existed and was withheld. Unscoreable, not unclosable.

Absence is not a third value. An intent entry with no prediction field is a defect, not an entry declining to predict.

The digest is the mechanism, not a formality. Where a prediction exists but nothing records its existence at dispatch, the entry is written `not authored` in good faith by whoever can only see what was supplied, and the prediction becomes permanently unprovable as pre-dispatch. Releasing it afterward is indistinguishable from writing it afterward, which is why `check_record.py` treats a permanent sentinel resolved by a supplied value as fabrication.

Retroactive reading: entries written before this rule are read under it. `not authored` means null and closed wherever it appears, including in entries 2026-08-13-01, 2026-08-13-05, and 2026-08-14-01. No entry is edited to make this true; only the vocabulary used to read them changes. Entry 2026-08-13-09 is unaffected, since its sentinel reads `withheld` rather than `not authored`, and this rule does not invent a value for it.

Rationale: a check that reports a permanently unresolvable state as pending does not merely fail to help. It teaches its reader to skim past that section, and once that habit forms the check has stopped working while still printing. A check can rot by being ignored as readily as by going stale.

Standing: n=2. One case in which an outcome prediction was authored before dispatch, released after the terminal entry was already committed, and stranded permanently. One in which a prediction existed and was held, no mechanism conveyed its existence, the intent entry recorded `not authored` correctly on the evidence available, and the prediction is now unverifiable as pre-dispatch. No check enforces this rule. Rules 1 through 8 are likewise unenforced, and building machinery for a rule at n=2 is what Evidence-Based Feature Addition exists to prevent.

Forager evidence, added 2026-10-16 (RECORD.md 2026-10-16-01): the `committed:<sha256>` form appears 0 times in Forager's record of 1,275 entries. forager-forecast reached the same end, a choice provably fixed before the outcome, by public commits whose order a reviewer checks (rule 10). That route was used and this one was not; rule 10 is the working method, and this rule's withheld hash remains for a prediction that must stay hidden from the executor until it has run.

**10. Choices that could be tuned to a result are committed before the result is read.**

Thresholds, tolerances, samples, seeds, exclusions, tuning grids and the evaluation itself are written into the repository and committed before any count of the outcome is read. Changing one afterwards turns a test into a search. So a change after the data is a stop for the operator, and when one is made the old and new verdicts are both recorded. How each outcome will be read is stated before the run, and a null or negative result is a deliverable, not a failure to deliver.

The evidence that the order held is the commit order, checked by someone other than the author. That needs no withheld plaintext and no release step, which is why it was used where rule 9's hash was not.

This extends Intent-Driven Engineering's prediction from the outcome to the analysis that will judge the outcome.

Evidence: forager-forecast fixes its production seed and a 20-configuration tuning grid before any model is fit, rejecting the alternative because it "invites tuning until it wins" (`docs/planning/DECISIONS.md:101`, D31 at `b9127e5`), and does the same for its evaluation, filters and licence tracks (D33, D26, D29). Reviewers confirmed that the commit came before the first count in four cases. The rule held when the result pulled the other way (D109, D90), and caught a committed tolerance that would have failed before any value was read. Forager's planner profile carries the same rule: "Fix choices before data" (`docs/process/planner-profile.md:38` at `402489ae`).

Standing: four checked orderings and three holds or catches, in one project. Untested here.

**11. A load-bearing result is re-derived by a separate session, from the repository, with its own code.**

A finding that later work will stand on is reviewed by a session that did not produce it, working from the repository rather than from the producer's conversation. The reviewer recomputes headline figures with its own code, runs its own revert checks, and fixes its own samples and tolerances before reading the data. Finding nothing is an acceptable result; saying what was checked is mandatory. A builder's own check is kept and labelled as a self-check; it is not a review. A dependent task waits for its prerequisite's review to be filed.

Evidence: forager-forecast decision D18 (`docs/planning/DECISIONS.md:114` at `b9127e5`) and its standing review protocol (`docs/dispatch/2026-09-18-review-protocol.md`; the quoted sentence is at `:17`). It has 21 review files on main, 14 of which led to a fix, a correction or a decision traceable in its record (a reader session's classification, 17 of the 21 from index rows). In its decision D35, an independent review found two things the builder's self-check had missed, while the self-check re-ran a count the reviewer could not reach; both documents were kept, because each saw something the other could not. In Forager, an independent review caught 37 guessed record timestamps (record 2026-09-28-608). This repository's own record named the need first: RECORD.md 2026-08-15-04, Finding 1, "a single investigation is one sample, not a determination".

Standing: the strongest of the candidates, in one project family. Role Partition has no reviewer role, so promoting this would amend it.

**12. What a gate costs decides whether it survives.**

Every gate has a running cost, paid in operator attention, compute, latency or usage limits. A gate whose cost is paid on every action is the first to be removed, and it is often removed wholesale, taking the cheap gates down with the expensive one. So a gate's running cost is priced before it is installed, and checks that run at commit or in CI are preferred over checks that run on every action.

A guard enforced only in some checkouts, sessions or command routes protects only those. The routes it does not see are listed when it is installed.

When a gate is removed or disabled, the removal records what stops being enforced. A required field with no checker behind it should be expected to disappear at the next change of session, so whoever removes a checker says which fields it was holding.

Evidence, all from Forager (trials/forager-2026-10-16.md):

- Per-dispatch operator approval was removed four days after it began. The operator: "Can't have me hitting buttons. Those hooks need to change" (`docs/audits/2026-09-26-approval-exempt-build-device.md`).
- The whole hook kit was disabled and deleted on 2026-09-27 "to work around weekly limits" (`docs/audits/2026-09-27-kit-hooks-disabled.md`). That note is the model for recording a removal: its section 3 lists what stops being enforced.
- The guards' own bypass table: a script, a subshell, a split variable or a build alias passed every guard except the planner's tool restriction. A merge went through the hosting service's API from a checkout that carried no hooks.
- What decayed after the checkers went:
  - Prediction fields fell from 99 of 100 intents to 0 of 143, and Finish line to 31 of 143.
  - 1,646 entry errors and 307 binding violations accumulated unseen.
  - The working trunk was bypassed for about two weeks.
- What survived without enforcement: dispatches as files, verbatim quotes, revert checks, and the pre-build disclosure sections.

The operator ruled the loss of predictions to be drift, not a decision (prompts/preserved/2026-10-16-01.md), so Intent-Driven Engineering's prediction requirement stands unchanged. Forager is recorded as a gate lost once its checker was removed.

Standing: four removals or bypasses, plus the decay above, in one project. If promoted, this amends Automated Boundary Enforcement, which says a boundary defended only by convention is undefended but says nothing about what a defence costs.

## What these do not fix

They relocate an error class rather than eliminating it. A planner holding a file can still misread it, cite the wrong hash, or reason correctly from a premise that was wrong before anyone wrote it down.

Where the operator's specification and the planner's model are wrong in the same way, every one of these rules passes and the work is wrong anyway. Nothing here addresses that, and it may not be addressable.

## Standing

Untested. Rules 1 through 4 are at n=0 as of writing. (Rules 1 and 2 were promoted into Sourced Claims on 2026-10-16; see the notes under each.) Rules 5 through 7 were added later from a role-separation proposal, also at n=0. Rule 8 was added later still, from a single case in which the failure it prevents did not occur. Rule 9 was added later still, at n=2, from two cases in which the failure it prevents did occur.

To be exercised in phase 3 and reviewed afterward. Rules that earn their place are candidates for promotion to PHILOSOPHY.md, with the evidence recorded. Rules that cost more than they catch are deleted from this document, which is possible precisely because they were never installed as principles.

Rule 7 is a special case: it does not supplement PHILOSOPHY.md but replaces part of it, so promoting it means archiving Role Partition. That raises the bar for its promotion rather than lowering it.

Rules 10 onward were added on 2026-10-16 (RECORD.md 2026-10-16-01) from the records of Forager and forager-forecast (trials/forager-2026-10-16.md). Their evidence comes from one further project family, read after the fact. It is not a test in this repository, and none of them is enforced by a check.

A rule that goes unexercised through a full phase is reviewed rather than assumed still relevant. This document has no forgetting mechanism of its own, and an untested rule that persists indefinitely looks like anticipation while being accumulation.
