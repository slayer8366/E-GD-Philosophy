---
name: spec
description: >
  This skill should be used when the user asks to "write a spec", "spec this out",
  "turn this idea into a spec", "draft requirements for", or "/spec". Converts a rough
  feature idea into a short, decision-complete specification.
metadata:
  version: "0.1.0"
---

# Spec

Produce a spec short enough to read in two minutes and complete enough that no decision is left to the implementer.

## Procedure

1. Read the idea. Extract the goal, the user of the feature, and any constraints stated.
2. List unmade decisions. If any would change the architecture or reverse an earlier choice, stop and surface them (use the stop-and-ask skill if available). Do not guess.
3. If the spec depends on the current state of a codebase and that state was not read this session, say so and request a pulse (pulse-before-plan skill if available) before asserting where things live.
4. Write the spec using the template in `references/spec-template.md`. Load the template only at this step.
5. Keep it under 600 words. Cut background prose; keep decisions, scope edges, and acceptance checks.
6. End with a one-line list of open questions, or "No open questions."

## Rules

- Every requirement is testable. If you cannot name how it would be checked, rewrite it.
- Out of scope is a section, not an afterthought.
- Mark anything unverified as unverified. Do not upgrade an assumption to a fact.
- If the spec will be handed to an agent, deliver it as a file in the repo (dispatch-as-file skill if available), not as chat.
