---
name: breakdown
description: >
  This skill should be used when the user asks to "break this down", "split into tasks",
  "make a task list from this spec", "what's the order of work", or "/breakdown". Splits a
  spec into ordered, handoff-ready tasks with dependencies and a verification step each.
metadata:
  version: "0.1.0"
---

# Breakdown

Turn a spec into tasks that can each be handed off and verified independently.

## Procedure

1. Read the spec. If it has open questions that block ordering, stop and list them instead of guessing.
2. Identify the smallest slices that each produce an observable result. A task with no observable result is not a task; merge it into one that has.
3. Order by dependency, then by risk. Put the task most likely to overturn the plan first, so a wrong premise is found before work piles on it.
4. For each task write:
   - `T<n>. <title>`
   - Depends on: task ids or "none"
   - Does: two lines max
   - Verify: the check that proves it landed
   - Device-only: yes/no (if yes, note what needs real hardware)
5. Flag any task that rests on an unconfirmed diagnosis. Those get a "verify before building" line.
6. Keep the whole breakdown under 400 words for a typical feature. If it runs longer, the spec is probably too big; say so.

## Rules

- No task longer than one working session.
- Each task names its own evidence. Reuse the completion-report skill format if the user has it.
- When handing a task to an agent, write it using the dispatch-authoring skill if available, and commit it as a file (dispatch-as-file skill). Do not paste task text into chat as the handoff.
