# Evidence Gated Development: Philosophy

Companion documents: ENFORCEMENT.md (what an agent does about each principle), GLOSSARY.md (the bidirectional index), BOOTSTRAP.md (the agent-facing minimum), OVERVIEW.md (the operator's introduction).

## Governing Principle

**Traceability of Reported Results:** Every reported result must be traceable to its raw inputs and to the exact configuration or calibration that produced it. This covers any output the project asserts as true: measurements, classifications, decisions, and derived artifacts alike. All principles below are instruments of this rule.

**Inseparability of Result and Conditions:** A result without the conditions that produced it is not a result. A value and its calibration, configuration, and input identities travel together or not at all.

## Roles and Authority

**Role Partition:** Planning and execution are held by separate actors. The planning role discusses, designs, and writes prompts, and never edits files or runs code. The executing role edits and runs, and never makes architectural decisions. Separation is structural, not a matter of discipline: an actor able to act on an idea will act before the idea is finished, and an actor able to decide will decide rather than surface an ambiguity. Planning is singular per line of work; executors may be plural. Where executors run in parallel, each is told what other work is in flight that it could collide with, and reconciling contradictory prompts belongs to the planning role, triggered by an executor reporting a conflict rather than resolving it.

**Operator Authority:** Decision authority rests with the human operator. Agents surface options, evidence, and ambiguities; the operator closes decisions. An agent may argue against a decision and must not silently reverse or reopen one. Closed decisions are recorded, and reopening requires a superseding entry. Authority is not a release from work. Delegating execution promotes the operator from writing the code to owning the direction, and the verification of prompts and results is the work that role consists of.

**Operator Observation:** The operator is the only actor that observes the system outside what an agent was instructed to run. Agents report on the paths they exercised; the operator sees behavior nobody thought to check. Facts about the live system that were not produced by an instructed run enter the project only through the operator.

## Data Integrity and Traceability

**Content-Addressed Identification:** Key derived data and outputs to cryptographic hashes of raw input payloads rather than mutable metadata like file paths, names, or timestamps. If inputs change, identity changes. Environmental context (see Capture Environmental Context) is recorded as accompanying metadata alongside the identity, never folded into the hash itself.

**Immutable Append-Only History:** Never overwrite or delete historical data, logs, or project records. Record updates, corrections, abandonments, or merge reconciliations as new entries containing explicit supersedes pointers referencing the entry being replaced. This applies uniformly to audit trails and project logs; there is no distinction between the two.

**Archival Without Loss:** An append-only store that nobody can read has stopped being a record. Archival relocates superseded and terminated entries to a separate store under the same append-only rules, leaving a pointer in the active store for every entry moved. What changes is where an entry lives, never whether it exists. Archival is never a side effect of other work.

**Atomic State Mutations:** Execute all disk and store writes atomically (write to a temporary location before performing an atomic swap) to prevent data truncation during unexpected crashes.

**Capture Environmental Context:** Record explicit runtime configurations, environmental conditions, and dependencies alongside output results rather than storing standalone values. Credentials, tokens, keys, and personal data are recorded by name and fingerprint or version identifier, never by value: an append-only store is the one place a recorded secret can never be unrecorded.

**Reconstructable Environments:** Recording dependencies shows what was used; only pinning them allows a rerun. Dependency sets are captured as exact resolved versions identified by hash, not as ranges. Output produced against an environment that cannot be reconstructed is labeled as such in the artifact itself; the label is the truthful degradation, and blocking the run is not required.

**Pipeline Substrate Discipline:** Perform analytical operations and measurements strictly on unmodified raw data or standardized canonical substrates, never on lossy, display-formatted, or post-processed derivatives.

**Explicit Canonicalization:** When identity or comparison depends on a canonical form, perform the normalization explicitly. Never delegate it to a type system or library that may treat two distinct forms as equivalent and silently skip the conversion.

## Architecture and System Separation

**Isolated Hardware and Integration Layers:** Contain platform-specific, vendor, or hardware calls behind strict abstraction drivers. Core domain logic must interact only with generalized driver interfaces.

**Decouple Business Logic from Presentation:** Core computational and domain logic must remain free of UI bindings and display frameworks to enable independent execution in headless testing environments.

**Presentation Is Not Acquisition:** Display and preview paths may transform data freely for operator use. Acquisition and measurement paths must never inherit those transforms. The two paths are separated structurally, not by convention.

**Truthful Interface Contracts:** Driver methods must enumerate backend capabilities dynamically. Unsupported features should degrade gracefully and return degenerate, truthful answers rather than fabricated values.

**Capability Ranges Are Not Operating Envelopes:** Vendor-reported or hardware-reported ranges describe what a device can be commanded to do, not what it should be commanded to do. Consumers must apply explicit operating limits rather than trusting reported capability as a safe envelope.

**Observable Configuration References:** Reference mutable module-level or global configuration through its owning namespace, never by binding a local copy at load time. A detached binding silently stops tracking reassignment, including reassignment performed by test isolation.

**Concurrency Awareness:** Before approving parallel work, flag exclusive-access resource constraints, shared mutable stores that fall outside per-agent isolation, and potential working-state conflicts between actors. Concurrent access hazards must be surfaced explicitly, not discovered mid-build.

**Automated Boundary Enforcement:** Guard structural boundaries using automated programmatic checks (static assertions checking import rules, for example) to prevent architectural erosion.

## Software Engineering Principles

**Explicit Failure Reporting:** Report partial or failed pipeline executions explicitly. Never silently swallow errors, substitute default fallbacks without recording them, or present incomplete results as successful.

**Unattended Execution Discipline:** Any code path that can run unattended must never block on interactive input. Prompts belong behind an explicit interactive flag, and their absence must not change the result of work already completed.

**Surface Anomaly Evidence:** Detect and highlight configuration drift or data anomalies for user or operator evaluation. Avoid making automated, destructive decisions on top of detection heuristics.

**Uniform Code Paths:** Pass single inputs and batched inputs through the same standard processing path rather than short-circuiting logic with special-case branches.

**Additive Enhancements:** Introduce new capabilities as new modules, functions, or paths rather than overwriting or branching inside existing working code. A new capability that would otherwise require a conditional branch inside a shared path must be factored out to its own path instead. Additive means new surface area, not new special cases layered on old surface area. See Uniform Code Paths for the governing rule once that new surface area must handle both single and batched inputs.

**Evidence-Based Feature Addition:** Delay building advanced processing or correction logic until representative raw execution data exists to validate the implementation.

## Testing and Verification Culture

**Separate Execution Contexts:** Distinguish between passing headless unit tests and verifying runtime behavior in live production environments. Headless success does not guarantee live functionality.

**Confirm Failure Before Applying Fixes:** Reproduce bugs in test setups prior to writing fix code, verifying that the failing assertion trips before passing. The expected failure mode is stated before the check is run, and the observed failure is compared against it. A check that fails for an unexpected reason has demonstrated a defect in itself, not a fact about the code, and its observation is void until the check is repaired. This is the prediction requirement of Intent-Driven Engineering applied one level down, for the same reason: an outcome you did not predict cannot confirm anything.

**Data-Driven Debugging:** Confirm Failure Before Applying Fixes governs every individual fix attempt. This principle governs what happens when that discipline has been followed and has failed twice in a row on the same symptom: stop forming further speculative hypotheses. Gather raw runtime logs, step through live code, and construct a minimal reproduction before attempting a third fix.

**Validate Real Event Paths:** Exercise code through application entry points and event dispatchers in the exact system states present during live runtime, rather than calling isolated methods directly.

**Assert Structural and Semantic Truths:** Assert directly on output data payloads, types, and schema structures rather than proxy indicators like file creation or source text strings.

**Checks Decay:** A check is verified once, at birth, by its observed failure. Nothing keeps it verified. A check that can no longer fail has silently stopped protecting anything, and it looks identical to one that is protecting everything. The suite is not a fixed asset; its coverage is a claim that decays without evidence.

**Severity of Checks:** A check is evidence for a claim only to the degree that it would have failed had the claim been false. Passing is not the property that matters; the capacity to fail is. That capacity is lost whenever something between the check and its subject decouples them: a default that gives the same answer either way, a stale artifact read as this run's output, a filter that drops the cases that would disagree, a fixture or simulated environment that cannot represent the failing state, a path nothing calls, or a tool whose output describes some state other than the one claimed. None of these shows in the check's own output, which looks the same coupled or not, so the decoupling is found only by counting the check's input against something outside it. Confirm Failure Before Applying Fixes and Checks Decay apply this at a check's birth and over its life; this principle governs every citation of a check as evidence, including checks on checks. It is Popper's demand that a claim be exposed to refutation, made operational by Mayo's severity requirement. Of everything in this document it has the most recorded instances: fifteen or more across two projects (trials/forager-2026-10-16.md).

**Sourced Claims:** A claim about the state of the system names the source that establishes it, or is marked as unverified. Inference from familiar patterns is not a source. An unsourced claim carries no evidentiary weight regardless of how confidently it is stated.

## Workflow and Documentation

**Intent-Driven Engineering:** Document planned changes, exact scope boundaries, and measurable baselines before writing code. Every intent record states a prediction (what will be observed if the change works, concretely enough to be wrong) and a finish line (the state that ends the task, and the conditions that abort it). An intent record governs a task, not every step inside one: the edits, runs, and check iterations within a task's stated scope proceed under its single record. Record the intent before any file is touched, so an interrupted session leaves a trace of intent rather than only finished work. Review the finished build against the prediction, and record a wrong prediction as wrong rather than replacing it with what happened.

**Complete Task Prompts:** The prompt that carries a task from planner to executor is a governed artifact, not free text. It carries the role assignment, the scope boundary, the closed decisions that bear on the task, the prediction and finish line from the intent record, the checks required, and what is explicitly out of scope. A prompt missing a closed decision does not delegate that decision; it forces the executor to violate its role. Executor validation catches missing structural elements and cannot catch a missing decision, because an executor cannot know what it was never told. Operator review of the prompt is therefore the only control that closes that gap, and it is a required step rather than a recommended one.

**Decisions Have Standing Conditions:** A closed decision rests on conditions that were true when it was made. Those conditions can stop being true without anyone noticing, and a decision resting on a vanished condition is indistinguishable from a live one. Closures record what they depend on, and later work that touches a recorded condition surfaces the decisions standing on it. Surfacing is the whole action; reopening remains the operator's.

**Terminal Intent Entries:** Every intent record is closed by exactly one terminal entry: completed, superseded, or abandoned. An abandoned entry states what was left in the working state and whether it is safe to build on. An intent record with no terminal entry marks work whose status is unknown, and unknown status is a hazard, not a default.

**Complete Execution Reports:** A report of executed work states what was done, what was verified and how, and what was left undone. Omission is misreporting. A report that reads as reassurance rather than record has failed at its only job.

**Knowledge Harvest Before Rewrite:** Working documents accumulate hard-won findings. Before any rewrite or condensation, explicitly harvest marked findings into durable records. The harvest is a gate, not a suggestion: the rewrite does not proceed until the drain is complete.

**Document the Reasoning:** Record why a design decision was made, along with dead-ends and failed approaches, so future maintainers understand the rationale behind constraints.

**Early Flagging of Ambiguities:** Pause and resolve ambiguous requirements or architectural gaps before writing code on top of unverified assumptions.

## Self-Application

**Evidentiary Standing of This Document:** These principles are held to their own standard. Claims that this philosophy generalizes across domains, or that it improves agent reliability, are currently hypotheses supported by a single sustained case study. Individual principles vary in support: some were derived from specific documented failures, others were generalized outward from those cases and have not themselves been tested. That standing is stated here because Evidence-Based Feature Addition applies to philosophies as much as to features: confidence beyond the evidence is a defect, in a document like this one most of all.
