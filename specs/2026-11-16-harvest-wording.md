# Spec: the wording for the lessons approved on 2026-11-16

Under RECORD.md 2026-11-16-02. The operator approved these groups from the second reading (trials/forager-2026-11-05.md): "1 both", "2 all of them", "3 yes" (prompts/preserved/2026-11-16-01.md). This spec gives the exact text proposed for each, and where it goes. **A spec is not a go.** Nothing below is in the method until the operator approves the wording; then it goes in under its own intent, one commit per item.

Drafted against E-GD Test-1 at 7e227d0, reading each target's current text first.

**How the wording is kept generic.**
- No project's name, record ID or path appears in the new method text. Each evidence note points to the trial reading that holds the evidence, by its item label (P1, M2 and so on).
- The trial files' own names include the project's name. They are the pointer, not part of the rule.
- Existing Forager references in the texts being amended are left for the project-neutral rewrite of decision 2026-11-05-03, which comes after this.

**Figures still to be checked.** The recount (RECORD.md 2026-11-16-01) is re-deriving the trial's figures. Every figure below is one counted by script and re-checked by the curator, or it is given as "several" with the trial as the pointer. Any figure the recount changes is corrected here before anything is written.

---

## Group 1: two promotions into the philosophy

### P1. Verify Premises Before Building (from PROTOCOL rule 3)

**PHILOSOPHY.md**, Workflow and Documentation, after Complete Task Prompts:

> **Verify Premises Before Building:** Every claim a task makes about the system it will change is a premise, not a fact. It was true when someone read it, or it was never read. Before building, the executor checks each premise against the source, with file and line, and reports what it found, which premises were false, and the options a false premise opens. The executor proposes and does not choose: the planner adjudicates and the operator approves. The check is worth most when the planner is most confident, because it does not depend on the planner being right. Where every relevant fact is already in front of the executor, the round trip is not needed.

**ENFORCEMENT.md**, Workflow and Documentation, after Complete Task Prompts:

> **Verify Premises Before Building**
> - Before writing anything, the executor reads at the source every premise its task states: a path, a caller, a count, a behaviour, whether something exists. It reports each as confirmed, false or not determined, with file and line and the commit read.
> - The report carries what was found as well as options. A false premise that leaves the task undecided stops the task. The executor builds nothing on it until the planner adjudicates and the operator approves.
> - The executor's mechanism prediction goes in the same report, before building.
> - Where every premise is already in front of the executor, it says so and goes on; the report still lists each premise as confirmed.
> - Promoted from PROTOCOL rule 3 under RECORD.md [the writing intent's ID]. Evidence: trials/forager-2026-11-05.md, P1.

**GLOSSARY.md**, a row after Complete Task Prompts:

> | Verify Premises Before Building | Workflow and Documentation | Verify Premises Before Building | Active |

**PROTOCOL.md**, rule 3: a closing note in the form rules 1 and 2 already use:

> Promoted [date] into PHILOSOPHY.md as Verify Premises Before Building (RECORD.md [the writing intent's ID]). The text above stays as written.

### P2. Independent Review (from PROTOCOL rule 11)

**PHILOSOPHY.md**, Testing and Verification Culture, after Severity of Checks:

> **Independent Review:** A result that later work will stand on is re-derived by a session that did not produce it. The reviewer works from the repository, not from the producer's account. It uses its own code and its own revert checks, and fixes its samples and tolerances before it reads the data. It runs on a different model from the builder's, because a model shares its own blind spots and favours its own output. A builder's own check is kept and labelled as a self-check; it is not a review. Finding nothing is a result, and saying what was checked is required. A review is filed in the reviewer's own words: a condensation by whoever commissioned it is testimony about the review, not the review.

**ENFORCEMENT.md**, Testing and Verification Culture, after Severity of Checks:

> **Independent Review**
> - A result that later work stands on, and each change before it is promoted to production, is reviewed by a session that did not build it, running on a different model from the builder's. The record names the model each ran on, as read from the session, not assumed.
> - The reviewer works from the repository at named commits. It recomputes headline figures with its own code, runs its own revert checks, and commits its samples, tolerances and counting rules before it reads the data (PROTOCOL rule 10).
> - A dependent task waits until its prerequisite's review is filed.
> - The review is filed unedited. A reviewer that may not write gives its report as its final message, and that message is filed byte for byte.
> - Where two reviews of one result run on different models, neither reads the other's until both are filed.
> - Promoted from PROTOCOL rule 11 under RECORD.md [the writing intent's ID]. Evidence: trials/forager-2026-11-05.md, P2; related work S27 and S28 (paper/related-work.md).

**GLOSSARY.md**, a row after Severity of Checks:

> | Independent Review | Testing and Verification Culture | Independent Review | Active |

**PROTOCOL.md**, rule 11, a closing note:

> Promoted [date] into PHILOSOPHY.md as Independent Review (RECORD.md [the writing intent's ID]). The text above stays as written.

**Counts that follow from these.** PHILOSOPHY.md goes from 45 principles to 47, ENFORCEMENT.md from 44 entries to 46, and GLOSSARY.md from 45 rows to 47. check_glossary.py should then pass at 47/46/47; that is the first check after writing. Two README.md lines also change:
- line 28, "45 principles, each stating what is true", becomes "47 principles…";
- line 70, "which of the 45 principles are load-bearing", becomes "which of the principles are load-bearing", since that sentence is about the trial of the 45.

---

## Group 2: PROTOCOL.md

### M1. Rule 12, what a gate costs: a new paragraph before its Evidence

> Fields are not the only thing that lapses. Without a checker, whole kinds of entry stop being written across a change of session: intents, closing entries, merge records, corrections. Work then runs with no marker of what is open until an outside reader finds it.
>
> A rule written down after a slip does not hold under pressure, even for the agent that wrote it, unless something checks it where it applies: a field in a template, a step in a checklist, a check at the point of use.
>
> A rule that names its own enforcement ("CI warns when…") says where that enforcement runs and when it was last seen to run. Enforcement that was only planned reads exactly like enforcement that exists.
>
> A one-time override records what it stopped enforcing, as a removal does.
>
> Evidence, added [date]: trials/forager-2026-11-05.md, M1. In one project, intents went unwritten for ten days, and merge and correction entries stopped and had not returned by the time of reading. Rules written after slips were breached again. One rule named enforcement that did not exist.

### M2. Rule 13, parallel work: three bullets added to its list

> - Identifiers shared between records are partitioned by namespace, such as a prefix per record, not by numeric range. A reserved range is a forecast of the other record's growth, and it fails silently when the forecast does.
> - A removed ID stays retired, and its removal is recorded where the entries citing it will be read.
> - Where several planners share one branch, every merge is recorded where the others read before they act.

and to its Evidence:

> Added [date]: trials/forager-2026-11-05.md, M2. A range partition between two records failed and left 43 IDs each naming two different entries. Five removed IDs were reused, and one removed entry is still cited.

### M3. Rule 23, the release gate

Step 1 of "The gate, in order" becomes:

> 1. Automated checks pass at the exact commit being promoted. Every check cited, automated or on a device, is bound to the artifact that ships: the commit, tree or build hash it checked is shown equal to what ships. A check run on another build is listed as a gap.

Two bullets added after the gate's steps:

> - A register of known defects ships with each release. It lists each defect's severity and whether users already have it. A defect already live may ship; a new one that risks a user's data, safety or trust fails the release.
> - The gate's verdicts are counted. A gate that has only ever passed has not been shown able to fail, and its standing says so.

A dated update after the current Standing line, which stays as written:

> Standing, updated [date]: releases with code have since passed through the gate, and every audit verdict recorded in the period read was "pass with items" (trials/forager-2026-11-05.md, M3). The gate has not yet been seen to fail. The device path is still untested as a gate step.

### M4. Operator Authority (PHILOSOPHY.md and ENFORCEMENT.md)

**PHILOSOPHY.md**, added at the end of the principle:

> Where the operator answers through options, the option marked as recommended usually decides. So a recommendation is itself a reading of the operator's words, and one that departs from a standing ruling overrides it unless the operator notices. The operator's own words are the first option, and no option that departs from them is marked recommended. A planner's restatement of a ruling is labelled as the planner's and is never carried forward as the ruling. A change to a device, account or data the operator uses is the operator's decision, whether or not it can be undone.

**ENFORCEMENT.md**, three bullets added to Operator Authority, before its "Amended" line:

> - Before offering options, the agent checks each against the operator's standing words on the matter, quoted. The operator's words are the first option. An option that departs from them is never marked recommended, and says in its own text that it departs, and from what.
> - A restatement of a ruling, in a prompt, a record or a report, sits beside the ruling quoted verbatim and is labelled as the restater's. It is never later cited as the ruling.
> - Changing settings or data on a device or account the operator uses needs the operator's go, whether or not the change can be undone.
> - Amended [date] under RECORD.md [the writing intent's ID]. Evidence: trials/forager-2026-11-05.md, M4.

### N1 to N7. New rules 24 to 30, added before "What these do not fix"

> **24. Exhausted resources let checks fail open, and an exit code is not a state.**
>
> Disk, memory, temporary storage and usage limits are shared state that every check depends on. When one runs out, a check can pass on truncated input, and a gated step can run past a failed precondition. So free space is checked before a gated step, and a tool's output is checked for completeness, not only its exit code. Success is read from the resulting state, and gated steps are chained so that a failure stops the next.
>
> Evidence: trials/forager-2026-11-05.md, N1. Exhaustion recurred in one project, twice letting a check or a gate fail open, once through a tool that stopped partway and still exited 0. Standing: one project.

> **25. A refused or interrupted action may have partly run.**
>
> A tool call shown as refused, a command interrupted, or a step that failed may have changed state before it stopped. Before running anything again, the agent reads the actual state and reports what had already happened.
>
> Evidence: trials/forager-2026-11-05.md, N2. In one instance, a call shown as refused had in fact landed, and its re-run landed a second time. Standing: three instances, in one project.

> **26. Process documents drift against each other, and an outside reader cross-reads them.**
>
> A clause saying which document wins settles a conflict once someone has found it. It does not find it. Profiles, process documents and standing instructions written at different times contradict each other silently. At intervals, and before any release of the method, a session from outside the project reads them against each other and lists every contradiction for the operator.
>
> Evidence: trials/forager-2026-11-05.md, N3. There were five contradictions across two projects' process documents; two were found by an outside reader. Standing: five instances.

> **27. A ruling about how work is done lives in the document that governs the work.**
>
> An operator ruling that changes how work is done is written, with the operator's words, into the governing document before it is applied. A copy in an agent's private notes is a pointer to the rule, not the rule, and a rule that lives only there is missed by the next session.
>
> Evidence: trials/forager-2026-11-05.md, N4. Standing: several instances, in two projects.

> **28. A session hands off at a context threshold, and the handoff carries the record.**
>
> A long session degrades, and its context and usage run out. An executor or planner hands off to a fresh session past a set context size, and before a usage limit, with all its work committed and pushed. The handoff names the dispatch, the record entries and the branch heads; it is not a summary. A session let run past the threshold gets closer review of what it produced.
>
> Evidence: trials/forager-2026-11-05.md, N5. Standing: a dozen handoffs and one session run far past its threshold, in one project.

> **29. Points of no return are named in the plan and asked at the point.**
>
> A plan names its points of no return: an irreversible step, a public one, or one that spends what cannot be recovered. The operator's go for each is asked when the work reaches it, never assumed from an earlier go for the plan.
>
> Evidence: trials/forager-2026-11-05.md, N6. Standing: two instances, in one project. This applies Operator Authority, which already holds that authorization is local.

> **30. Code refuses rather than choosing.**
>
> Where data needs a reading the fixed rules do not give, the program stops and names what needs a ruling, rather than picking a default. The refusal is the stop-and-ask, moved into code.
>
> Evidence: trials/forager-2026-11-05.md, N7. Two refusals became the operator's rulings. Standing: two instances, in one project.

The closing **Standing** section gains a sentence:

> Rules 24 to 30 were added on [date] from the second reading of the same project family (trials/forager-2026-11-05.md), on the operator's "all of them" (prompts/preserved/2026-11-16-01.md). None is enforced by a check.

---

## Group 3: RECORDING.md and ADOPTING.md

### RECORDING.md

**R1.** Under the intent type, a bullet after "The prediction is required":

> - **Predictions in both directions.** An intent may state its prediction as two: what will be seen if the change works, and what will be seen if it fails. Its terminal scores both. Where a record's header or a role's profile listed the prediction fields, predictions came back with no checker behind them (trials/forager-2026-11-05.md, R1).

**R2.** Under dispatch-note, a bullet at the end:

> - **Every dispatch is claimed.** A dispatch file is claimed by an intent or a dispatch-note before its work runs. check_prompts.py lists any that are not. A record that keeps dispatch files without running it should expect unclaimed dispatches to accumulate unseen (trials/forager-2026-11-05.md, R2).

**R3.** "The index": a bullet after the serialization-point bullet:

> - **Coverage decays when reports move.** An index covers only the store it was built for. Reports filed elsewhere, such as beside the dispatch they answer, get rows too, or the index states what it does not cover (trials/forager-2026-11-05.md, R3).

**R4.** "Layout: one file per month", a bullet after "Splitting an existing single file…":

> - **Splitting a record across repositories** copies rather than moves. The originals stay where other entries cite them, and the number of entries copied is predicted and then checked.

**R5.** "Entry types", a sentence after "Twelve, kept as Forager used them…":

> Projects add kinds of their own as they need them. A kind enters this method only when it is harvested and approved; until then it stays the project's (trials/forager-2026-11-05.md, R5).

**R6.** Under the intent type, a bullet after R1:

> - **Who writes the intent.** The plan and the outcome prediction are the planner's. The intent itself may be written by the executor. One operator's ruling: "Intent is different than plan, and can be written by the coder still, it's a good practice to. But planning is the planner task" (trials/forager-2026-11-05.md, R6).

### ADOPTING.md: a new section after "What you need", for decision 2026-11-05-03

> ## Building on E-GD
>
> E-GD is a basis. A project adopts it, builds on it, and adds back.
>
> - **Each project keeps its own rules.** Where a project needs something different from what E-GD says, its own rule stands in that project, and E-GD does not change on it.
> - **Harvest.** At intervals the curator reads what the projects have learned. What is useful is curated into E-GD in general wording, without the project's own references, and the operator approves what enters.
> - **Departures are recorded.** Where a project's rule departs from E-GD, the trial reading in `trials/` records it, so a reader can see where E-GD has been changed in use and why.
>
> The operator, 2026-11-05, verbatim: "each project keeps its own rule and the paper says so. EGD acts as a basis on which projects can build on and add back. But each project keeps its own rules until harvested, where you will curate it and add what is useful, and leave out project specific references." (RECORD.md 2026-11-05-03)

### ADOPTING.md: a section after "Building on E-GD", for AD1 to AD5

> ## Practices that have held in use
>
> Each is from a project running the method (trials/forager-2026-11-05.md, AD1 to AD5).
>
> - **Small files, each owned by one task at a time.** Parallel executors never share a file; a file over a size limit is split before anything is added to it.
> - **Messages between agent sessions are committed files.** A message in a session's transcript can be lost or never read; a file in the repository is durable and citable.
> - **Record entries are written with a quoted here-document or a file write.** An unquoted shell here-document runs backquoted text and silently corrupts the entry.
> - **Each role's profile states the model it runs on, and why.** The model is read from the session, not assumed from a configured name.
> - **Usage and machine limits are scheduling constraints.** Heavy jobs run one at a time under a memory cap. Handoffs are timed before usage limits (PROTOCOL rule 28), and free space is checked before a gated step (rule 24).

### profiles/curator.md: a line under "The role", which decision 2026-11-05-03 reserved for the operator to see first

> - **Projects keep their own rules until harvested.** The curator does not press E-GD's rules on a project, and a project's rules do not change E-GD. At a harvest the curator curates what is useful into E-GD in generic wording, and the operator approves what enters (RECORD.md 2026-11-05-03).

### Corrections: present-tense statements now false

There are four, not the three the curator told the operator on 2026-11-06; the fourth was found while drafting. Each keeps what it said, marked with when it held, and adds what is true now.

1. **PROTOCOL.md rule 23, Standing:** "No release with code has been audited". Corrected by M3's dated update.
2. **PROTOCOL.md rule 22, Standing:** "three more are being written in Forager". A dated update:
   > Standing, updated [date]: the project family now keeps nine role profiles, each naming the model it runs on (trials/forager-2026-11-05.md, AD4).
3. **PROTOCOL.md rule 14, Evidence:** "Forager's record holds 12 entry kinds…". "holds" becomes "held, at the first reading," with the clause:
   > (fifteen by the second reading, trials/forager-2026-11-05.md)
4. **RECORDING.md, "The index":** "forager-forecast files every dispatch byte-identical under `docs/dispatch/` and indexes it in that same single table". It becomes:
   > A project that files every dispatch in one folder and indexes it in one table avoids a second index drifting out of step with the first, as long as every new dispatch gets its row. One project's index went unchanged while its later dispatches went unindexed (trials/forager-2026-11-05.md, R3).

---

## Decided by the curator in drafting, for the operator to accept or strike

- **Placement.** P1 sits after Complete Task Prompts, as the executor's side of it. P2 sits after Severity of Checks.
- **Rule 29** overlaps Operator Authority ("authorization is local") and says so in its own text.
- **A clause left out of rule 24.** The second reading also shows evidence deleted to recover disk space. A clause against that was considered and left out, as beyond what was approved.
- **The README line about "the 45 principles"** loses its number rather than changing to 47, because it describes the trial of the 45.
