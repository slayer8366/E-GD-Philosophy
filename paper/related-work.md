# Related work for the method paper

Working material for the paper's related-work section: step 3 of its preparation, under RECORD.md intent 2026-11-05-01. This is not method text, and nothing here changes a principle.

## How this was gathered and checked

- **Gathered** on 2026-11-05 by a read-only research session. Its brief: primary sources, verbatim quotes, and each source marked "read at source" or "snippet only". The relations (precedent, extends, contrast) and the novelty assessment are that session's reading, labelled as such.
- **Re-checked by the curator.** Each quote marked "re-matched" was fetched again from the URL given and found as a string in the page or PDF text. Matching ignores letter case, whitespace, HTML tags and the form of quotation marks and dashes.
  - It ran twice. The first pass matched 79 of 79 key phrases across 50 fetches. The second matched 63 of 63 full quotes, as written in this file, across 41 fetches.
  - Sources in the first pass only are re-matched by key phrase, not by full quote: S2's supporting source, S12, S17, S19, S25 and its companion, S29's abstract, S41's ChatDev venue, and S42's first post.
  - **Its positive control:**
    - two quotes altered by one word were reported missing, and their originals found;
    - a quote searched on the wrong page was reported missing;
    - a quote searched on a page that does not exist was reported missing.
  - The superpowers lines (S45) were re-checked through the GitHub API, at the repository's last commit before E-GD's first (44c9b2d6e).
- **Not re-checked** means the curator did not fetch it again: the session's own status stands, and the source is not cited until it has been.

E-GD's first commit is 1e0b50a, 2026-08-09.

## 1. Test-first development

**S1. Beck, K., "Canon TDD", 11 Dec 2023.** https://newsletter.kentbeck.com/p/canon-tdd
- **Status:** read at source; re-matched.
- **Quotes:** "Now that you have a failing test, change the system so the test passes." / "Mistake: delete assertions so the test pretends to pass. Make it pass for real."
- **Bears on:** Confirm Failure Before Applying Fixes; Checks Decay.
- **Relation:** precedent for test-first. The session's reading: Beck does not ask for the failure mode to be predicted before the run, and E-GD adds that.

**S2. Beck, K., *Test-Driven Development: By Example*, Addison-Wesley, 2002, ISBN 978-0-321-14653-3.**
- **Status:** snippet only. No quote.
- **Supporting source:** Fowler, "TestDrivenDevelopment", bliki, 11 Dec 2023, https://martinfowler.com/bliki/TestDrivenDevelopment.html. Read at source; re-matched: "It was developed by Kent Beck in the late 1990's as part of Extreme Programming."

**S3. Fucci, D., Erdogmus, H., Turhan, B., Oivo, M., Juristo, N., "A Dissection of the Test-Driven Development Process: Does It Really Matter to Test-First or to Test-Last?", *IEEE TSE* 43(7):597–614, 2017.** DOI 10.1109/TSE.2016.2616877; arXiv 1611.05994.
- **Status:** abstract read at source; re-matched.
- **Quotes:** "Sequencing, the order in which test and production code are written, had no important influence." / "The claimed benefits of TDD may not be due to its distinctive test-first dynamic, but rather due to the fact that TDD-like processes encourage fine-grained, steady steps that improve focus and flow."
- **Relation:** a caution. Test-first is not supported as a productivity or quality practice. E-GD's reason for seeing a failure first is evidential: what a pass is worth. So the argument rests on S5–S7 and on severity, not on TDD's outcome studies.

## 2. Mutation testing and revert checks

**S4. DeMillo, R.A., Lipton, R.J., Sayward, F.G., "Hints on Test Data Selection: Help for the Practicing Programmer", *Computer* 11(4):34–41, 1978.** DOI 10.1109/C-M.1978.218136.
- **Status:** snippet only. Cited as the origin of mutation analysis; not quoted.

**S5. Jia, Y., Harman, M., "An Analysis and Survey of the Development of Mutation Testing", *IEEE TSE* 37(5):649–678, 2011.** DOI 10.1109/TSE.2010.62.
- **Status:** read at source, from https://web.eecs.umich.edu/~weimerw/2020-481F/readings/mutation-testing.pdf; re-matched.
- **Quotes:** "If the result of running p′ is different from the result of running p for any test case in T , then the mutant p′ is said to be 'killed', otherwise it is said to have 'survived'." / "However, there are some mutants that can never be killed, because they always produce the same output as the original program."
- **Bears on:** Severity of Checks; Confirm Failure Before Applying Fixes; Checks Decay.
- **Relation:** precedent, extended. A revert check is one mutant chosen by hand: the fix's inverse. The equivalent mutant corresponds to one of Severity of Checks' decouplings, "a default that gives the same answer either way". Severity of Checks also covers links mutation analysis does not model: stale artifacts, lossy filters, and paths nothing calls.

**S6. Just, R., Jalali, D., Inozemtseva, L., Ernst, M.D., Holmes, R., Fraser, G., "Are mutants a valid substitute for real faults in software testing?", FSE 2014, 654–665.** DOI 10.1145/2635868.2635929.
- **Status:** read at source by the session; not re-checked.
- **Quote:** "The results show a statistically significant correlation between mutant detection and real fault detection, independently of code coverage."
- **Relation:** precedent. Fault datasets are built from tests that fail before a fix and pass after it.

**S7. Vera-Pérez, O.L., Danglot, B., Monperrus, M., Baudry, B., "A comprehensive study of pseudo-tested methods", *Empirical Software Engineering* 24(3):1195–1225, 2019.** DOI 10.1007/s10664-018-9653-2; arXiv 1807.05030.
- **Status:** abstract; re-matched.
- **Quote:** pseudo-tested methods "are covered by the test suite, yet no test case fails when the method body is removed".
- **Relation:** precedent. Checks that cannot fail, measured at scale.

**S8. Foster, C., Gulati, A., Harman, M., et al., "Mutation-Guided LLM-based Test Generation at Meta", arXiv 2501.12862.**
- **Status:** abstract; re-matched.
- **Quote:** "From these currently uncaught faults, ACH generates tests that can catch them, thereby `killing' the mutants and consequently hardening the platform against regressions."
- **Relation:** precedent in the AI setting. An LLM-written test is accepted once it is shown to fail on a fault.

## 3. Decision records

**S9. Nygard, M., "Documenting Architecture Decisions", 15 Nov 2011.** https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- **Status:** re-matched.
- **Quotes:** "If a decision is reversed, we will keep the old one around, but mark it as superseded." / "It's better to avoid either blind acceptance or blind reversal."
- **Bears on:** Document the Reasoning; Immutable Append-Only History; Operator Authority; Decisions Have Standing Conditions.
- **Relation:** precedent for supersession and recorded reasons. The session's reading: nothing in it asks later work to surface a decision when its context changes, which is the extension Decisions Have Standing Conditions makes.

**S10. Tyree, J., Akerman, A., "Architecture Decisions: Demystifying Architecture", *IEEE Software* 22(2):19–27, 2005.** DOI 10.1109/MS.2005.27.
- **Status:** metadata only. Not to be cited for its content until read.

**S11. Lago, P., van Vliet, H., "Explicit assumptions enrich architectural models", ICSE 2005, 206–214.** DOI 10.1145/1062455.1062503.
- **Status:** snippet only. A likely precedent for Decisions Have Standing Conditions; read it before citing.

**S12. Saint-Andre, P. (Ed.), RFC 9280, "RFC Editor Model (Version 3)", 2022.** DOI 10.17487/RFC9280.
- **Status:** re-matched.
- **Quote:** "Once published, RFC Series documents are not changed." Its header carries "Obsoletes: 8728".
- **Relation:** precedent. Documents never change, and explicit pointers mark what they supersede.

## 4. Append-only records and data integrity

**S13. Fowler, M., "Event Sourcing", 12 Dec 2005.** https://martinfowler.com/eaaDev/EventSourcing.html
- **Status:** re-matched.
- **Quotes:** "Capture all changes to an application state as a sequence of events." / "Not just can we query these events, we can also use the event log to reconstruct past states, and as a foundation to automatically adjust the state to cope with retroactive changes."
- **Relation:** precedent.

**S14. 21 CFR §11.10(e) (US FDA, electronic records).** https://www.govinfo.gov/content/pkg/CFR-2024-title21-vol1/xml/CFR-2024-title21-vol1-sec11-10.xml
- **Status:** re-matched.
- **Quote:** "(e) Use of secure, computer-generated, time-stamped audit trails to independently record the date and time of operator entries and actions that create, modify, or delete electronic records. Record changes shall not obscure previously recorded information."
- **Relation:** precedent. A legal requirement that a correction leave the original readable.

**S15. US FDA, *Data Integrity and Compliance With Drug CGMP: Questions and Answers*, Guidance for Industry, Dec 2018.** https://www.fda.gov/media/119570/download
- **Status:** re-matched.
- **Quotes:**
  - "Complete, consistent, and accurate data should be attributable, legible, contemporaneously recorded, original or a true copy, and accurate (ALCOA)."
  - "A data value is by itself meaningless without additional information about the data."
  - "FDA prohibits sampling and testing with the goal of achieving a specific result or to overcome an unacceptable result (e.g., testing different samples until the desired passing result is obtained)."
- **Bears on:** Inseparability of Result and Conditions, which the second quote states almost word for word; Traceability of Reported Results; Sourced Claims; PROTOCOL rule 10.
- **Relation:** strong precedent.

**S16. 17 CFR §240.17a-4(f)(2) (US SEC broker-dealer records).** https://www.govinfo.gov/content/pkg/CFR-2024-title17-vol4/xml/CFR-2024-title17-vol4-sec240-17a-4.xml
- **Status:** re-matched.
- **Quotes:** "Preserve the records exclusively in a non-rewriteable, non-erasable format" / "Include a backup electronic recordkeeping system that meets the other requirements of this paragraph (f)".
- **Relation:** precedent for write-once storage, and for Durability Is Location.

**S17. Laurie, B., Langley, A., Kasper, E., RFC 6962, "Certificate Transparency", 2013.**
- **Status:** re-matched.
- **Quote:** "Certificate transparency aims to mitigate the problem of misissued certificates by providing publicly auditable, append-only, untrusted logs of all issued certificates."
- **Relation:** contrast. Certificate Transparency makes append-only provable cryptographically. E-GD keeps it by rule and by a history check.

**S18. Schnell, S., "Ten Simple Rules for a Computational Biologist's Laboratory Notebook", *PLOS Comput Biol* 11(9):e1004385, 2015.** DOI 10.1371/journal.pcbi.1004385.
- **Status:** re-matched.
- **Quote:** "If you make a mistake in your paper lab notebook, put a thin line through the mistake and write the new information next to it [1]. Never erase or destroy an entry, because errors or mistakes are an important part of the scientific process."
- **Relation:** precedent.

**S19. Sandve, G.K., Nekrutenko, A., Taylor, J., Hovig, E., "Ten Simple Rules for Reproducible Computational Research", *PLOS Comput Biol* 9(10):e1003285, 2013.** DOI 10.1371/journal.pcbi.1003285.
- **Status:** re-matched. The author list is from the session's memory; confirm it.
- **Quotes:** "Rule 1: For Every Result, Keep Track of How It Was Produced"; "Rule 9: Connect Textual Statements to Underlying Results".
- **Bears on:** Traceability of Reported Results; Reconstructable Environments; Sourced Claims.

**S20. Reproducible Builds, "Definitions".** https://reproducible-builds.org/docs/definition/
- **Status:** re-matched.
- **Quote:** "A build is reproducible if given the same source code, build environment and build instructions, any party can recreate bit-by-bit identical copies of all specified artifacts."
- **Bears on:** Reconstructable Environments.

## 5. AI coding agents, empirical

**S21. Becker, J., Rush, N., Barnes, E., Rein, D., "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", arXiv 2507.09089, 2025.**
- **Status:** abstract; re-matched.
- **Quote:** "Before starting tasks, developers forecast that allowing AI will reduce completion time by 24%. After completing the study, developers estimate that allowing AI reduced completion time by 20%. Surprisingly, we find that allowing AI actually increases completion time by 19%--AI tooling slowed developers down."
- **Bears on:** the problem statement; Operator Observation.

**S22. Peng, S., Kalliamvakou, E., Cihon, P., Demirer, M., arXiv 2302.06590, 2023;** and **Paradis, E., et al., arXiv 2410.12944, 2024.**
- **Status:** abstracts; re-matched.
- **Quotes:** "The treatment group, with access to the AI pair programmer, completed the task 55.8% faster than the control group." / "We found that AI significantly shortened the time developers spent on task."
- **Relation:** context. Speed gains are real. E-GD's concern is correctness.

**S23. Perry, N., Srivastava, M., Kumar, D., Boneh, D., "Do Users Write More Insecure Code with AI Assistants?", CCS 2023.** DOI 10.1145/3576915.3623157; arXiv 2211.03622.
- **Status:** re-matched.
- **Quote:** "participants who had access to an AI assistant based on OpenAI's codex-davinci-002 model wrote significantly less secure code than those without access. Additionally, participants with access to an AI assistant were more likely to believe they wrote secure code than those without access to the AI assistant."
- **Relation:** precedent for the problem: confidence and correctness come apart.

**S24. Kabir, S., Udo-Imeh, D.N., Kou, B., Zhang, T., "Is Stack Overflow Obsolete?", CHI 2024.** DOI 10.1145/3613904.3642596; arXiv 2308.02312.
- **Status:** re-matched.
- **Quotes:** "Our analysis shows that 52% of ChatGPT answers contain incorrect information and 77% are verbose." / "However, they also overlooked the misinformation in the ChatGPT answers 39% of the time."

**S25. Spracklen, J., et al., "We Have a Package for You!", arXiv 2406.10279;** and **Liu, F., et al., "Beyond Functional Correctness", arXiv 2404.00971.**
- **Status:** both re-matched.
- **Quotes:** "the average percentage of hallucinated packages is at least 5.2% for commercial models and 21.7% for open-source models"; Liu: "12 specific categories".
- **Bears on:** Sourced Claims.

**S26. Sharma, M., Tong, M., Korbak, T., et al., "Towards Understanding Sycophancy in Language Models", arXiv 2310.13548.**
- **Status:** re-matched.
- **Quote:** "Moreover, both humans and preference models (PMs) prefer convincingly-written sycophantic responses over correct ones a non-negligible fraction of the time."
- **Bears on:** Complete Execution Reports; Operator Authority.

**S27. Huang, J., Chen, X., Mishra, S., et al., "Large Language Models Cannot Self-Correct Reasoning Yet", arXiv 2310.01798.**
- **Status:** re-matched.
- **Quote:** "our research indicates that LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction."
- **Bears on:** PROTOCOL rule 11: a self-check is not a review.

**S28. Panickssery, A., Bowman, S.R., Feng, S., "LLM Evaluators Recognize and Favor Their Own Generations", arXiv 2404.13076.**
- **Status:** re-matched. The venue is unverified.
- **Quote:** "One such bias is self-preference, where an LLM evaluator scores its own outputs higher than others' while human annotators consider them of equal quality."
- **Bears on:** PROTOCOL rules 11 and 23: the reviewer and the auditor run on a different model.

**S29. Jimenez, C.E., et al., "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?", arXiv 2310.06770.**
- **Status:** the abstract quote is re-matched. The fail-to-pass definition comes from the paper text and is not re-checked.
- **Quotes:** "We filter out task instances without at least one test where its status changes from a fail to pass (henceforth referred to as fail-to-pass test)." / "solve a mere" (abstract).
- **Also:** SWE-bench Verified, https://swebench.com/verified, re-matched: "A human-validated subset of 500 SWE-bench instances".
- **Relation:** precedent. The field's main agent benchmark is built on fail-to-pass.

**S30. Wang, Y., Pradel, M., Liu, Z., "Are 'Solved Issues' in SWE-bench Really Solved Correctly?", ICSE 2026.** arXiv 2503.15223.
- **Status:** re-matched.
- **Quotes:** "However, because testing is rarely exhaustive, a patch may pass the tests but nevertheless fail to match the developers' expectations." / "Combined, the different weaknesses lead to an inflation of reported resolution rates by 6.2 absolute percent points."
- **Bears on:** Severity of Checks.

**S31. Baker, B., Huizinga, J., Gao, L., et al., "Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation", arXiv 2503.11926.**
- **Status:** re-matched.
- **Quote:** "we found two particularly effective coding hacks: exit(0), where the agent exploited a bug that allowed it to exit from the environment early without running all unit tests, and raise SkipTest, in which the agent raised an exception from functions outside the testing framework in order to skip unit test evaluation."
- **Bears on:** Severity of Checks; PROTOCOL rule 20.

**S32. Zhong, Z., Raghunathan, A., Carlini, N., "ImpossibleBench", arXiv 2510.20270.**
- **Status:** re-matched.
- **Quote:** "For example, an LLM agent with access to unit tests may delete failing tests rather than fix the underlying bug."
- **Bears on:** PROTOCOL rule 20.

**S33. Google Cloud / DORA, "Announcing the 2024 DORA report", 22 Oct 2024.** https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report
- **Status:** re-matched.
- **Quote:** "As AI adoption increased, it was accompanied by an estimated decrease in delivery throughput by 1.5%, and an estimated reduction in delivery stability by 7.2%."
- **Relation:** context. This is a survey correlation.

## 6. AI coding agents, practice and methods

**S34. Schluntz, E., Zhang, B., "Building effective agents", Anthropic, 19 Dec 2024.** https://www.anthropic.com/engineering/building-effective-agents
- **Status:** re-matched.
- **Quotes:** "However, whereas automated testing helps verify functionality, human review remains crucial for ensuring solutions align with broader system requirements." / "you should consider adding complexity only when it demonstrably improves outcomes"

**S35. Anthropic, "Best practices for Claude Code", undated documentation, accessed 2026-11-05.** https://code.claude.com/docs/en/best-practices
- **Status:** re-matched.
- **Quotes:**
  - "Claude stops when the work looks done."
  - "ask Claude for *evidence*: the command it ran and its output, or the screenshot."
  - "after two failed corrections run `/clear` and write a better prompt instead of a third."
  - "It isn't swayed by the reasoning that produced the code."
  - "If something has to happen every time, make it a hook, a deny rule, or a managed setting."
- **Relation:** precedent for asking for evidence, for a fresh reviewer and for the two-failure stop. A contrast on hooks: E-GD's record says they were removed because of what they cost (PROTOCOL rules 12 and 21).

**S36. Delimarsky, D., "Spec-driven development with AI", GitHub Blog, 2 Sep 2025 (Spec Kit).** https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
- **Status:** re-matched.
- **Quotes:** "Crucially, your role isn't just to steer. It's to verify." / "We treat coding agents like search engines when we should be treating them more like literal-minded pair programmers."
- **Bears on:** Intent-Driven Engineering; Complete Task Prompts.

**S37. Böckeler, B., "Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl", 15 Oct 2025.** https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
- **Status:** re-matched.
- **Quotes:** "I frequently saw the agent ultimately not follow all the instructions." / "To be honest, I'd rather review code than all these markdown files."
- **Relation:** a caution. A complete prompt does not make an agent follow it, and paperwork costs review time (PROTOCOL rule 12).

**S38. AGENTS.md.** https://agents.md/
- **Status:** re-matched.
- **Quote:** "Think of AGENTS.md as a README for agents".
- **Relation:** precedent for the agent-facing document type.

**S39. AWS DevOps Blog, "AI-Driven Development Life Cycle", 31 Jul 2025, and "Open-sourcing adaptive workflows for AI-DLC", 29 Nov 2025.**
- **Status:** read at source by the session; not re-checked, and no URLs recorded. Find them before citing.
- **Quotes:** "AI systematically creates detailed work plans, actively seeks clarification and guidance, and defers critical decisions to humans." / "The AI-DLC workflow records every human action and approval".

**S40. Takerngsaksiri, W., et al., "Human-In-the-Loop Software Development Agents", ICSE SEIP 2025.** arXiv 2411.12924.
- **Status:** re-matched.
- **Quote:** "we introduce a Human-in-the-loop LLM-based Agents framework (HULA) for software development that allows software engineers to refine and guide LLMs when generating coding plans and source code for a given task."
- **Bears on:** Role Partition; Operator Authority.

**S41. Hong, S., et al., "MetaGPT", arXiv 2308.00352;** and **Qian, C., et al., "ChatDev", ACL 2024, arXiv 2307.07924.**
- **Status:** MetaGPT's quote and ChatDev's venue are re-matched. MetaGPT's venue is unverified.
- **Quote:** "MetaGPT encodes Standardized Operating Procedures (SOPs) into prompt sequences for more streamlined workflows".
- **Relation:** contrast. Their roles divide labour among agents, with no human operator holding authority.

**S42. Willison, S., "Not all AI-assisted programming is vibe coding", 19 Mar 2025, https://simonwillison.net/2025/Mar/19/vibe-coding/;** and **"Vibe engineering", 7 Oct 2025, https://simonwillison.net/2025/Oct/7/vibe-engineering/.**
- **Status:** re-matched.
- **Quotes:** Willison quoting Karpathy, whose original was not read: "fully give in to the vibes". Willison: "Your agent might claim something works without having actually tested it at all".

**S43. Beck, K., "Augmented Coding: Beyond the Vibes", 25 Jun 2025.** https://newsletter.kentbeck.com/p/augmented-coding-beyond-the-vibes
- **Status:** re-matched.
- **Quotes:** "In vibe coding you don't care about the code, just the behavior of the system." / "Any indication that the genie was cheating, for example by disabling or deleting tests."

## 7. Closest prior work

**S44. Huang, J., Hsia, J., Sun, J., Shi, F., Huang, W., White, I.H., "Proof-or-Stop: Don't Trust the Agent, Trust the Evidence -- Loop Engineering for Verifiable Evidence-Gated Lifecycle Control", arXiv 2607.14890v1, submitted 16 Jul 2026.**
- **Status:** abstract re-matched. The submission date was read from the arXiv page and its API. It is 24 days before E-GD's first commit.
- **Quotes:** "Autonomous coding agents increasingly execute multi-step software work, but lifecycle states such as reviewed, tested, DONE, and ready-to-merge remain claims unless supported by current evidence." / "The method treats agent outputs as claims rather than lifecycle state, and uses proof operationally to mean gate-admissible evidence under a stated trust model, not semantic program correctness." / "The evaluation is limited to one model family, 24 ablation tasks, and a self-hosted corpus."
- **Relation (the session's reading):** the closest prior work found. It calls itself a method, uses "evidence-gated" in its title, and has a pre-registered ablation. Its gates are mechanical, at lifecycle transitions; E-GD gates on evidence a person reads. Its freshness check covers stale evidence but not defaults, filters or uncalled paths. In the text searched, nothing was found on operator authority, supersession or standing conditions.

**S45. Vincent, J. (obra), "superpowers".** https://github.com/obra/superpowers. Created 2025-10-09; its skill files' history begins 2025-10-16.
- **Status:** re-checked by the curator through the GitHub API at 44c9b2d6e, its last commit before 2026-08-09. All five lines below are present there.
- **Lines:**
  - "If you didn't watch the test fail, you don't know if it tests the right thing";
  - "Failure message is expected";
  - "MUST FAIL", in its revert-the-fix sequence;
  - "NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE";
  - "If ≥ 3: STOP and question the architecture".
- **Relation:** a precedent for agents, nearly identical at the level of single practices. It stops after three failed fixes, where E-GD stops after two. The session's reading: its restore step does not say how to restore, and E-GD's two recorded ways the revert check itself failed are an extension. The repository had 313,003 stars on 2026-11-05, so reviewers will know it.

**S46. Hassan, A.E., et al., "Agentic Software Engineering: Foundational Pillars and a Research Roadmap", arXiv 2509.06216v2.**
- **Status:** re-matched against v2.
- **Quotes:** "Merge-Readiness Packs (MRPs): A structured evidence bundle submitted for human approval" / "human input is efficient, targeted, and becomes a durable part of the project record."
- **Relation:** precedent as a research roadmap, not an operated method.

**S47. Crosley, B., "The Evidence Gate", blog post, dated 28 Mar 2026 by the fetch tool.** https://blakecrosley.com/blog/the-evidence-gate
- **Status:** re-matched; the date is unverified.
- **Quotes:** "No work is complete until every claim in the completion report is backed by something observable." / "Evidence is a file path, a test result, a specific code reference, or a direct observation."

**S48. Bursuc, S., Ehrenborg, T., Lin, S., et al., "A benchmark for vericoding", arXiv 2509.22908.**
- **Status:** re-matched.
- **Quote:** "LLM-generation of formally verified code from formal specifications - in contrast to vibe coding, which generates potentially buggy code from a natural language description."
- **Relation:** contrast. Proof against a formal specification is the other route.

## 8. Further sources

- **S49. Gotel, O.C.Z., Finkelstein, A.C.W., "An analysis of the requirements traceability problem", ICRE 1994.** DOI 10.1109/ICRE.1994.292398. Re-matched: "Requirements traceability refers to the ability to describe and follow the life of a requirement, in both a forwards and backwards direction."
- **S50. RTCA DO-178C, 2011.** Snippet only. Quote the standard or FAA AC 20-115D before citing.
- **S51. W3C, PROV-DM, 2013.** https://www.w3.org/TR/prov-dm/. Re-matched: "Provenance is information about entities, activities, and people involved in producing a piece of data or thing, which can be used to form assessments about its quality, reliability or trustworthiness."
- **S52. Cockburn, A., "Hexagonal Architecture", 2005.** https://alistair.cockburn.us/hexagonal-architecture/. Re-matched: "Allow an application to equally be driven by users, programs, automated test or batch scripts, and to be developed and tested in isolation from its eventual run-time devices and databases."
- **S53. Mills, Dyer, Linger, "Cleanroom Software Engineering", *IEEE Software* 4(5), 1987.** DOI 10.1109/MS.1987.231413. Metadata only.
- **S54. IEEE Std 1012 (verification and validation).** Snippet only. Cite the standard itself on independence.
- **S55. Bainbridge, L., "Ironies of automation", *Automatica* 19(6):775–779, 1983.** DOI 10.1016/0005-1098(83)90046-8. Read by the session from a third-party copy; not re-checked. Quote: "The second irony is that the designer who tries to eliminate the operator still leaves the operator to do the tasks which the designer cannot think how to automate."

**Primary citations missing from OVERVIEW's lineage section.** Metadata only, content not read:
- Simmons, Nelson, Simonsohn 2011, DOI 10.1177/0956797611417632;
- Gelman and Loken, *American Scientist* 102(6):460, 2014, DOI 10.1511/2014.111.460;
- Cronbach and Meehl 1955, DOI 10.1037/h0040957;
- Mayo 2018, DOI 10.1017/9781107286184;
- Open Science Collaboration 2015, DOI 10.1126/science.aac4716;
- MacCoun and Perlmutter 2015, DOI 10.1038/526187a.

## The research session's novelty assessment, as given

Its reading, kept as it wrote it: the paper cannot claim novelty for test-first verification, revert checks, evidence before claims, or human approval gates for agents. S45, S44, S35, S46, S36 and S39 each have one or more of these first. What it did not find elsewhere, limited to the searches it ran:

1. Severity of Checks as a rule about *citing* a check. It comes with a list of the steps that decouple a check from its subject, and a remedy: count the check's input against something outside it.
2. Sourced Claims stated as rules for agents. A claim carries when it was read and expires, and a claim that something is absent names its search.
3. Operator Authority's account of what counts as an authorization. An answer is not permission; a go is local to its session; a paraphrase is not the ruling; an override is not a precedent.
4. Gating on produced evidence rather than on actions (PROTOCOL rules 12 and 21), reported against the vendor's "make it a hook" (S35).
5. The combination, in one method with a long operated record: laboratory record practice, decision records with standing conditions, and independent review on a different model.

It added: "Proof-or-Stop has something E-GD lacks: a pre-registered controlled ablation."

## Not found

- ALCOA+ at a regulator's own site; only the FDA's ALCOA was read.
- The full text of Beck 2002, DeMillo 1978, Cleanroom 1987, Tyree and Akerman 2005, Lago and van Vliet 2005, DO-178C, IEEE 1012, and OpenAI's SWE-bench Verified post.
- The original April 2025 Claude Code post, which now redirects.
- Mayo's severity applied to software testing (one search).
- Controlled studies of evidence-gated agent workflows, beyond S44's ablation.
- Research on what counts as authorization in human–agent work.

## Disclosures

- **Confirmed against inferred.** Confirmed: every quote marked re-matched, and S44's date. Inferred, the research session's reading: every precedent, extends and contrast judgement, and the novelty assessment.
- **Could not determine.** Whether E-GD's author knew S44, S45 or S46 before writing. When individual superpowers lines were first added before 44c9b2d6e.
- **Premises that were wrong.** The brief paired TDD with Confirm Failure; S3 shows TDD's outcome evidence does not carry that weight. The Claude Code post named in the brief now redirects. The brief expected precedents; one older than E-GD itself was found (S44).
- **Decided beyond scope.** The session read intent 2026-11-05-01, so its search was not blind to that intent's prediction 5. One of its search queries contained "evidence-gated development", close to the method's name. The fetch tool saved two PDFs to the session's own tool-results folder. One request using a browser user-agent was refused and not retried. It added sources beyond the listed topics.
- **Observed, not asked.** S44's title overlaps E-GD's name, which bears on the paper's title. The FDA's ban on testing until a passing result (S15) and the SEC's backup clause (S16) are close regulatory counterparts of PROTOCOL rule 10 and Durability Is Location.
