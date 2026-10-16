# Skills

Procedures an agent loads when its task calls for them. The bootstrap is loaded every session, and enforcement entries are meant to be pulled by headword; a skill does the same thing through the agent harness itself. Each skill carries a description of when it applies, and the harness loads it when that trigger fires. That is the selective loading the bootstrap's reading protocol describes, delivered by the harness instead of by the agent's own discipline.

## Where these came from

Copied byte for byte on 2026-10-16 (RECORD.md 2026-10-16-01) from the operator's account, as synced to the operator's machine. Each copy's sha256 matched its source when copied. The account copies are the live versions: a change made there does not reach this folder, and a change made here does not reach the account. Edits made here after copying are listed at the end of this file.

The operator authored all of these. The plan-forge plugin was uploaded by the operator on 2026-09-16; the skills were last updated in the account on 2026-09-16, except field-instrument-interface (2026-10-08).

## The skills, and the principles they carry out

| Skill | Use it when | Carries out |
|---|---|---|
| `evidence-discipline` | investigating code, answering how something works, asserting that behaviour does or does not exist | Sourced Claims; Operator Observation (read, observed and inferred kept apart); Separate Execution Contexts |
| `stop-and-ask` | a premise is wrong, no path exists, a fix would reverse a decision, two designs both fit | Early Flagging of Ambiguities; Operator Authority; Role Partition |
| `failing-test-first` | before any fix; before trusting any check, script or guard | Confirm Failure Before Applying Fixes; Severity of Checks (positive controls; fixtures that contain the case) |
| `revert-check` | after writing a test meant to guard a behaviour; before reporting a fix done | Severity of Checks; Checks Decay |
| `record-and-supersede` | finishing a dispatch, recording a decision, correcting a recorded claim | Immutable Append-Only History; Document the Reasoning; Durability Is Location (findings get their own row) |
| `dispatch-authoring` | handing off implementation work | Complete Task Prompts; Intent-Driven Engineering; Early Flagging of Ambiguities |
| `dispatch-as-file` | any handoff; any decision made in conversation that will shape code | Complete Task Prompts; Durability Is Location; Knowledge Harvest Before Rewrite |
| `pulse-before-plan` | before planning against a repository read hours or days ago | Sourced Claims (claims carry when they were read); PROTOCOL rule 3 |
| `completion-report` | finishing any task; any work reviewed by someone who was not watching | Complete Execution Reports; Separate Execution Contexts |
| `device-check-authoring` | work that can only be confirmed on real hardware | Separate Execution Contexts; Operator Observation; Validate Real Event Paths |
| `prior-art-before-interface` | placing a control, naming a setting, choosing a gesture | No headword. See below. |

The plan-forge plugin (`plan-forge/`) holds three more, which hand off to the skills above rather than restating them:

| Skill | Use it when | Carries out |
|---|---|---|
| `spec` | turning an idea into a decision-complete specification | Intent-Driven Engineering; Early Flagging of Ambiguities; Sourced Claims |
| `breakdown` | splitting a spec into ordered, verifiable tasks | Intent-Driven Engineering; Complete Task Prompts |
| `plan-review` | auditing a plan for unmade decisions, stale claims, untestable items, hidden scope | Early Flagging of Ambiguities; Sourced Claims; Complete Task Prompts |

**Flagged: `prior-art-before-interface` binds to no headword.** GLOSSARY.md's rule is that an action with no principle behind it is unjustified and must be flagged rather than forced into a row. This skill's premise is that an established convention is accumulated evidence from use, and departing from it is a decision to record with its reason. That is close to Document the Reasoning and Evidence-Based Feature Addition, and it is neither. It is kept, flagged, until the evidence for a principle of its own exists or the operator binds it.

## Example: a project-specific skill

`examples/field-instrument-interface/` is Forager's interface rules for a field app, built on these principles: honesty is never traded for ease, then "don't make me think". It is here as an example of deriving a project's own skill from the general ones, not as a general skill. It bears on Truthful Interface Contracts and Explicit Failure Reporting, and on PROTOCOL rule 15. It says itself which of its rules are inferred rather than drawn from field data.

## Third-party skills and plugins in use, not copied

These were in use in the same environment on 2026-10-16. They are listed so a reader knows what else shaped the work, and they are not copied: their publishers maintain them, and two carry no licence file permitting redistribution.

| Name | Source | Version | Licence |
|---|---|---|---|
| design | knowledge-work-plugins marketplace | 0040 | no licence file in the synced copy |
| engineering | knowledge-work-plugins marketplace | 0040 | no licence file in the synced copy |
| cowork-plugin-management | knowledge-work-plugins marketplace | 0040 | Apache-2.0 |
| mobile-design-system | Anthropic plugin directory; author rikucherry1993 | 0.2.1 | MIT |
| Built-in skills: docs, docx, pdf, pptx, xlsx, skill-creator, deep-research, import-memory, morning, google-workspace, computer-use, built-in-browser, chrome-browser | Anthropic | as synced | the publisher's |

## Found while copying, not changed

Forager keeps untracked local copies of nine of these skills. Three of them (completion-report, dispatch-authoring, prior-art-before-interface) are older than the account's and lack the Conventions field the account versions added. They were reported to the operator and not touched.

## Edits made here after copying
- `revert-check`, protocol step 5: after restoring, confirm the forward change is still present. From Forager's CLAUDE.md, where a restore from git discarded an uncommitted change the check had just vouched for. The account copy does not have this edit.
