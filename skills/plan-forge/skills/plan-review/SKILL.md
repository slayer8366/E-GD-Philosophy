---
name: plan-review
description: >
  This skill should be used when the user asks to "review this plan", "audit the plan",
  "is this plan missing anything", "check my spec", "what's stale in this plan", or
  "/plan-review". Audits an existing spec or task list for unmade decisions, stale
  assumptions, untestable items, and hidden scope.
metadata:
  version: "0.1.0"
---

# Plan Review

Find the places where a plan will fail before it is executed. Output findings, not a rewrite.

## Procedure

1. Read the plan once. Do not fix anything on the first pass.
2. Check each item against these four questions:
   - Decision: does this item quietly pick between options the author never chose?
   - Evidence: does it assert something about code or data that was not read this session? Mark it stale or unverified.
   - Test: could someone say whether this is done without asking the author?
   - Scope: does it add work not present in the goal?
3. Report only findings. Format each as one line: `<item id> | <category> | <problem> | <suggested fix or question>`.
4. Rank findings by cost of being wrong, highest first. Cap at ten. If more exist, say how many were cut.
5. End with a verdict: `Ready`, `Ready with fixes`, or `Not ready`, and the single most important reason.

## Rules

- Do not rewrite the plan unless asked. Findings are cheaper to read than a diff.
- Do not praise sections that are fine. Silence means pass.
- Where a finding is a real unmade decision, phrase it as the question the author needs to answer, not as your preferred answer.
