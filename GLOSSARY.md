# EGD Glossary

This file is machine-facing. It exists for two mechanical uses: check_glossary.py verifies the bidirectional contract against it, and agents use the table as a headword lookup to load enforcement entries selectively instead of reading ENFORCEMENT.md whole. Humans wanting to understand the principles should read OVERVIEW.md and PHILOSOPHY.md; this table will not teach anything, by design.

The bidirectional index. Every philosophy headword maps to its enforcement entry, and every enforcement entry binds to a headword. A headword with no enforcement entry is unenforced and must be flagged. An enforcement action with no headword is unjustified and must be flagged. This file is the mechanical check for both directions: a row with an empty cell is a violation by definition.

Headwords are the stable identifiers. Section numbers, ordering, and filenames may change; headwords may not. To retire a headword, supersede it in the record store and mark it here as superseded with a pointer, leaving the row in place.

Mapping is one-to-one. Where two principles jointly govern an area, each still owns its own enforcement entry. A row that would list two enforcement entries means the principles are not cleanly separated and must be revised rather than cross-listed.

| Headword | Philosophy section | Enforcement entry | Status |
|---|---|---|---|
| Traceability of Reported Results | Governing Principle | (governing; no direct entry, enforced through all others) | Active |
| Inseparability of Result and Conditions | Governing Principle | Inseparability of Result and Conditions | Active |
| Role Partition | Roles and Authority | Role Partition | Active |
| Operator Authority | Roles and Authority | Operator Authority | Active |
| Operator Observation | Roles and Authority | Operator Observation | Active |
| Content-Addressed Identification | Data Integrity and Traceability | Content-Addressed Identification | Active |
| Immutable Append-Only History | Data Integrity and Traceability | Immutable Append-Only History | Active |
| Archival Without Loss | Data Integrity and Traceability | Archival Without Loss | Active |
| Atomic State Mutations | Data Integrity and Traceability | Atomic State Mutations | Active |
| Capture Environmental Context | Data Integrity and Traceability | Capture Environmental Context | Active |
| Reconstructable Environments | Data Integrity and Traceability | Reconstructable Environments | Active |
| Pipeline Substrate Discipline | Data Integrity and Traceability | Pipeline Substrate Discipline | Active |
| Explicit Canonicalization | Data Integrity and Traceability | Explicit Canonicalization | Active |
| Isolated Hardware and Integration Layers | Architecture and System Separation | Isolated Hardware and Integration Layers | Active |
| Decouple Business Logic from Presentation | Architecture and System Separation | Decouple Business Logic from Presentation | Active |
| Presentation Is Not Acquisition | Architecture and System Separation | Presentation Is Not Acquisition | Active |
| Truthful Interface Contracts | Architecture and System Separation | Truthful Interface Contracts | Active |
| Capability Ranges Are Not Operating Envelopes | Architecture and System Separation | Capability Ranges Are Not Operating Envelopes | Active |
| Observable Configuration References | Architecture and System Separation | Observable Configuration References | Active |
| Concurrency Awareness | Architecture and System Separation | Concurrency Awareness | Active |
| Automated Boundary Enforcement | Architecture and System Separation | Automated Boundary Enforcement | Active |
| Explicit Failure Reporting | Software Engineering Principles | Explicit Failure Reporting | Active |
| Unattended Execution Discipline | Software Engineering Principles | Unattended Execution Discipline | Active |
| Surface Anomaly Evidence | Software Engineering Principles | Surface Anomaly Evidence | Active |
| Uniform Code Paths | Software Engineering Principles | Uniform Code Paths | Active |
| Additive Enhancements | Software Engineering Principles | Additive Enhancements | Active |
| Evidence-Based Feature Addition | Software Engineering Principles | Evidence-Based Feature Addition | Active |
| Separate Execution Contexts | Testing and Verification Culture | Separate Execution Contexts | Active |
| Confirm Failure Before Applying Fixes | Testing and Verification Culture | Confirm Failure Before Applying Fixes | Active |
| Checks Decay | Testing and Verification Culture | Checks Decay | Active |
| Severity of Checks | Testing and Verification Culture | Severity of Checks | Active |
| Data-Driven Debugging | Testing and Verification Culture | Data-Driven Debugging | Active |
| Validate Real Event Paths | Testing and Verification Culture | Validate Real Event Paths | Active |
| Assert Structural and Semantic Truths | Testing and Verification Culture | Assert Structural and Semantic Truths | Active |
| Sourced Claims | Testing and Verification Culture | Sourced Claims | Active |
| Intent-Driven Engineering | Workflow and Documentation | Intent-Driven Engineering | Active |
| Complete Task Prompts | Workflow and Documentation | Complete Task Prompts | Active |
| Decisions Have Standing Conditions | Workflow and Documentation | Decisions Have Standing Conditions | Active |
| Terminal Intent Entries | Workflow and Documentation | Terminal Intent Entries | Active |
| Complete Execution Reports | Workflow and Documentation | Complete Execution Reports | Active |
| Knowledge Harvest Before Rewrite | Workflow and Documentation | Knowledge Harvest Before Rewrite | Active |
| Document the Reasoning | Workflow and Documentation | Document the Reasoning | Active |
| Early Flagging of Ambiguities | Workflow and Documentation | Early Flagging of Ambiguities | Active |
| Evidentiary Standing of This Document | Self-Application | Evidentiary Standing of This Document | Active |

The single exception to the one-to-one rule is Traceability of Reported Results, which is the governing principle and has no direct enforcement entry by design; every other entry enforces it indirectly. That exemption is stated here rather than left as an empty cell, because an unexplained gap and a justified one look identical in a table.

## Marker vocabulary

The agreed marker prefixes for working documents. Markers are greppable by construction; a finding without a marker is invisible to the harvest gate.

| Marker | Meaning | Drained to |
|---|---|---|
| `LESSON:` | A finding that must survive any rewrite | Record store, before rewrite |
| `OPEN:` | An unresolved question awaiting a decision | Closed by the operator; closure recorded |
| `CLOSED:` | A decision that has been made; do not reopen without a superseding entry | Record store at time of closure |
| `DEFER:` | Recognized work intentionally not being done now | Record store or task backlog |

Adopters may add markers. Each addition is recorded in the record store and added to this table.
