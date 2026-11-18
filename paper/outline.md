# Outline: the method paper on E-GD

Step 4 of the paper's preparation, under RECORD.md 2026-11-18-02. The operator's framing, 2026-11-05: "A method paper presenting EGD as a foundation" (RECORD.md 2026-11-05-02). And on how projects relate to it: "EGD acts as a basis on which projects can build on and add back" (2026-11-05-03).

**An outline is not a go to draft.** The operator approves it first. Every figure named below is one the recount reproduced, or one that correction 2026-11-16-03 says may be cited, with its source.

---

## Working title

**Evidence Gated Development: a foundation for directing AI coding agents**

The closest prior work uses the same words: Proof-or-Stop's subtitle has "Evidence-Gated Lifecycle Control" (paper/related-work.md, S44), and it was posted 24 days before E-GD's first commit. The title is the operator's to settle; see question 2.

## 1. Abstract (about 200 words, written last)

- **The problem:** AI coding agents are fast, confident and sometimes wrong in ways that look right.
- **The move:** change what counts as done. Work is done when checkable evidence of it exists, not when an agent says so.
- **What the paper gives:**
  - the method, as 47 principles with their enforcement entries and 30 working rules on probation;
  - how projects adopt it, keep their own rules, and feed lessons back;
  - the record of one project family that ran it for about two months;
  - what that record does and does not show.

## 2. Introduction

- **The problem, with the evidence for it:**
  - confidence and correctness come apart (S23, S24);
  - developers' own sense of speed is unreliable (S21);
  - reviewers prefer convincing answers to correct ones (S26);
  - agents defeat their own tests (S31, S32);
  - passing benchmarks overstate success (S30).
- **The usual response and its limit:** better prompting holds until the session gets long or the task unfamiliar.
- **E-GD's response:** roles separated by what a decision depends on; intent and prediction before action; checks seen failing before they are trusted; a record that keeps what was believed and when.
- **The contributions,** stated against prior work (section 3). These are the candidates from paper/related-work.md, "Closest prior work and novelty":
  1. Severity of Checks, as a rule about citing a check, with its list of the ways a check can lose touch with what it checks.
  2. Sourced Claims, stated as rules for agents: a claim carries when it was read, and expires.
  3. Operator Authority: what counts as a go, and why an answer, a continuation or a paraphrase is not one.
  4. Gating on the evidence work produces rather than on the agent's actions, and the record of a gate removed for its cost.
  5. The combination, in one method with a long record of use.

## 3. Related work

Taken from paper/related-work.md, where each quote was checked against its source.

- **Testing:** test-first (S1–S3, with S3's caution that test-first sequencing itself is not shown to matter); mutation testing and checks that cannot fail (S4–S8).
- **Decision records and supersession:** S9–S12.
- **Records that keep corrections visible:** event logs, regulated audit trails, laboratory notebooks and reproducibility (S13–S20). S15's "testing into compliance" corresponds to PROTOCOL rule 10.
- **AI coding agents:**
  - empirical studies (S21–S33);
  - practice and methods (S34–S43), including vendor guidance that recommends hooks (S35), against E-GD's experience of their cost.
- **Closest prior work, named:**
  - Proof-or-Stop (S44): a method with mechanical, freshness-checked evidence gates and a pre-registered ablation;
  - superpowers (S45): agent skills that, before E-GD existed, already said to watch the test fail, revert the fix and confirm it fails, and give no claim without fresh evidence;
  - Agentic Software Engineering (S46) and The Evidence Gate (S47).
- **What E-GD adds beyond them,** stated plainly, and what it does not claim to add.

## 4. The method

- **Roles and authority:**
  - Role Partition and Operator Authority, including the rule that a recommendation is itself a reading of the operator's words;
  - Operator Observation;
  - Verify Premises Before Building and Independent Review, the two principles promoted on 2026-11-16, as a worked example of a rule earning promotion.
- **Intent and the record:**
  - an intent carries a prediction that can turn out wrong, a finish line and abort conditions;
  - every intent is closed exactly once;
  - the twelve entry types (RECORDING.md);
  - append-only history, with corrections as new entries, and backups before merges.
- **Checks:** Confirm Failure Before Applying Fixes; Severity of Checks; Checks Decay; the revert check and the two ways it failed in use.
- **Claims:** Sourced Claims and Durability Is Location.
- **The documents:** BOOTSTRAP for agents at session start; PHILOSOPHY, ENFORCEMENT and GLOSSARY bound one-to-one and checked by script; PROTOCOL for rules on probation; the skills.
- **The 47 principles,** in one table by section. The full text is in an appendix.

## 5. How projects build on it

- E-GD is a basis. Each project keeps its own rules until a harvest. The curator then curates what is useful in general wording, and the operator approves what enters (ADOPTING.md, "Building on E-GD").
- **Worked example:** the field-app project corrects record entries in place by its operator's rule, while E-GD keeps corrections as new entries. Both stand, and the trial reading records the departure.
- **The harvest of 2026-11-05 to 2026-11-17, as a worked example of the method applied to itself:**
  - two readers and a researcher, all read-only;
  - every quote re-matched at source, with positive controls;
  - an independent recount on a different model, with its counting rules committed before it counted;
  - lessons proposed, then their wording, each approved by the operator before it entered;
  - the project-neutral rewrite, with every removed line kept in trials/.

## 6. Evidence: one project family, read after the fact

All figures are from Forager's record as recounted (trials/recount-2026-11-16.md), and are cited as correction 2026-11-16-03 allows.

- **The setting:** one operator, who is not a programmer; a field app and a research project descended from it; planner and coder sessions.
- **Adoption and the cost of gates:**
  - the gates were installed as hooks on 2026-09-22 and removed five days later, because they blocked actions the agents were expected to take;
  - the operator then gated on evidence (PROTOCOL rules 12 and 21).
- **What decayed once the checkers went:**
  - predictions fell from 99 of 100 intents to 0 of 143;
  - finish lines fell to 31 of 143;
  - whole kinds of entry stopped for days.
- **What held with no enforcement:** dispatches as files, the operator quoted word for word, revert checks, and the disclosure sections.
- **What came back:** at the second reading, 66 of 93 intents state a prediction, after the planner returned to the recording method.
- **Where the project departed:** 48 of 296 record commits since 2026-11-01 delete a committed line, against 10 of 1,904 before. That is the operator's in-place rule.
- **Collisions on shared state:** 43 record IDs name different entries in the two projects' records.
- **The release gate:** 11 of 11 audits passed "with items". The gate has not yet been seen to fail.
- **Unclosed intents,** with both definitions: 63, or 79 counted by terminal entries alone.
- **Counts that depend on how they are searched are not quoted as figures.** Mentions of verify-first and the share of owner quotes are examples. Where the paper needs one, it gives the pattern beside it.

## 7. Limits

E-GD's own Self-Application principle, as written: "Claims that this philosophy generalizes across domains, or that it improves agent reliability, are currently hypotheses supported by a single sustained case study."

- **The evidence:** one operator and one project family, read after the fact by the method's own curator. There was no controlled comparison. Proof-or-Stop has a pre-registered ablation, and E-GD has none.
- **The standing of the rules:** 30 rules are still on probation, many backed by one or two instances. Five principles written for data pipelines are not cited in that project's record.
- **Who wrote the method:** agent sessions, directed by the operator. That bears on authorship and on blind spots. The independent recount and the different-model rule are the controls used, and they are partial.
- **What would test it:** a second operator; a controlled comparison on one task set; the PHILOSOPHY-in-context experiment that OVERVIEW.md proposes.

## 8. Conclusion

A foundation to adopt and build on, with its evidence stated. An invitation to run it, keep your own rules, and send back what you learn (the E-GD issues page).

## Appendices

- **A.** The 47 principles, with their enforcement entries.
- **B.** The working rules on probation, 1 to 30, with their standing.
- **C.** The record's entry types and fields.
- **D.** How each figure was produced: the trial readings, the recount's committed rules and report, and the checks.
- **E.** Reproducibility: the frozen E-GD release the paper cites (step 5), with its DOI. Every commit and line cited resolves there.

---

## For the draft stage (the operator's, not decided here)

- Authors, and how the agent sessions' part in writing is disclosed.
- Whether the paper names the projects or describes them, as the method text now does. See question 3.
- The paper's licence (the repository is GPL-3.0; papers usually use CC BY 4.0).
- Patents: publishing makes the method prior art.
- Length and venue: Zenodo as a preprint, and whether anything else follows.
