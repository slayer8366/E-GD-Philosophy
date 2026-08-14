# Working Protocol

Eight rules governing how the operator and planner work together. They are untested. Nothing here has been run even once at the time of writing.

These are not principles. PHILOSOPHY.md holds rules that have earned their place; this document holds rules that have not. They live apart on purpose: a rule installed in the philosophy can only be removed by archival, and these are likely enough to be wrong that installing them would be building ahead of the evidence.

## Where these came from

The planning role in this project has no access to the repository. It cannot read a file, run a check, or observe a commit. Every claim it makes about repository state comes from memory of what it dispatched rather than from what exists.

That produced ten errors of one shape: a file asserted to exist that did not, an entry ID asserted free that was taken, a task asserted complete that never ran, a count asserted from a running list rather than from the record, a finding number cited that was never real. Each was caught by an executing agent stopping to ask or by a read-only audit. None by a check.

The condition underneath is worth stating plainly, because the rules only make sense against it: the planning role cannot distinguish memory from observation. A false claim about repository state does not feel like a guess. It feels exactly like knowing.

## The rules

**1. The planner asserts no repository state.**

The planner does not state what a file contains, which IDs are in use, what a prior task produced, or whether something exists. Where a determination depends on state, the planner names where to look and defers the determination to whoever can look.

In practice this means writing "confirm the archive count and use what you find" rather than "the archive contains two entries." Both point at the same place. Only one can be wrong.

**2. State reaches the planner at task boundaries, carrying a commit hash.**

Before drafting a prompt, the operator passes the planner the files that prompt will concern. Every passback names the commit it came from.

Claims made from a passback cite that hash: "as of 7c6f32f, RECORD.md holds 20 entries." A claim that cannot name its source is unsourced whether or not a file was read.

A snapshot expires at the next commit. During a task the executor is authoritative for anything that changed, and the planner makes no new state claims.

Where a prompt would dictate edits to a file the planner has not been passed at the current hash, the planner says so and stops. Working from memory is the failure this rule exists to prevent, and doing it while holding a stale file is worse, because it looks sourced.

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

## What these do not fix

They relocate an error class rather than eliminating it. A planner holding a file can still misread it, cite the wrong hash, or reason correctly from a premise that was wrong before anyone wrote it down.

Where the operator's specification and the planner's model are wrong in the same way, every one of these rules passes and the work is wrong anyway. Nothing here addresses that, and it may not be addressable.

## Standing

Untested. Rules 1 through 4 are at n=0 as of writing. Rules 5 through 7 were added later from a role-separation proposal, also at n=0. Rule 8 was added later still, from a single case in which the failure it prevents did not occur.

To be exercised in phase 3 and reviewed afterward. Rules that earn their place are candidates for promotion to PHILOSOPHY.md, with the evidence recorded. Rules that cost more than they catch are deleted from this document, which is possible precisely because they were never installed as principles.

Rule 7 is a special case: it does not supplement PHILOSOPHY.md but replaces part of it, so promoting it means archiving Role Partition. That raises the bar for its promotion rather than lowering it.

A rule that goes unexercised through a full phase is reviewed rather than assumed still relevant. This document has no forgetting mechanism of its own, and an untested rule that persists indefinitely looks like anticipation while being accumulation.
