---
name: "field-instrument-interface"
description: "Design rules for Forager's interface as a field instrument. Use when adding or changing any screen, control, overlay, alert or readout, alongside prior-art-before-interface."
---

# Field instrument interface

Forager is used outdoors, often one-handed, by someone whose attention is on the ground and the trees. The interface is an instrument, and an instrument is judged by how little it asks of the person holding it, and by whether it can be trusted.

## Two governing rules, in this order

### First: honesty is never traded for ease
The interface does not hide, round away, smooth over, or imply certainty it does not have in order to be simpler. A readout that is easy and wrong is worse than one that is harder and true, because the user acts on it in the field. This covers:

- No fabricated or plausible stand-in values. Unsupported shows as unsupported.
- No presenting a partial, stale or failed result as a current, complete one.
- No dropping an uncertainty indicator because it clutters the screen.
- No wording that claims more than the code does.

### Second: don't make the user think
Within what is honest, every element should cost the user as little thought as possible. Before proposing any interface change, answer for each element:

- What question does the user have at this moment?
- Does the screen answer it without reading, calculating, remembering, or deciding?
- If the user must interpret something, can the app do that interpretation instead, without losing or distorting what is true?

If an element makes the user stop and work something out, that is a defect to fix or to report, even when the element is correct.

### When they conflict
Honesty is the constraint; ease is the goal inside it. Look first for a form that is both: most conflicts are a presentation problem, not a real trade. If no such form is found, keep the honest version and report the usability cost. Do not resolve it by simplifying the truth. When two of the seven rules below conflict with each other and honesty is not at stake, the option that costs the user less thought wins; if that is not obvious, it is a stop-and-ask.

## The seven rules, each read through the governing rules

### 1. Glanceable first
A screen used while walking answers its question in about a second. One primary figure per readout, large type, plain units. Prefer "12 min back to car" over a distance and a pace the user must combine. If the combined figure is an estimate, it reads as an estimate.

### 2. Field conditions are constraints
Design for sunlight, wet or gloved fingers, and one-thumb reach. Controls used in motion sit above the 48dp Material minimum and within thumb reach. The user should never have to think about aiming. A finger is not a point: see the coordinate-touch rule in CLAUDE.md for how this is tested.

### 3. The map is the content
Anything drawn over the map must earn its space and must not intercept touches meant for the map. The user should not have to wonder why a long-press did nothing. Bound overlay containers explicitly and cover them with a real long-press test, per CLAUDE.md.

### 4. Honest instruments, pre-interpreted
Show uncertainty, never false precision: GPS accuracy, compass reliability, stale fixes, unsupported capabilities. Show it in a form that needs no interpretation where one exists: an accuracy circle, a dimmed stale value, "compass unreliable" in words. Pre-interpretation may change the form of a fact and may not remove or soften it. If the simplified form would mislead in any case the app can actually be in, show the harder truth instead.

### 5. User-set state persists
What the user dragged, snapped, collapsed or chose survives navigating away and back. The user should never have to remember how they had things and set them up again. This is the UX default in CLAUDE.md; persistence across restarts remains a per-case decision.

### 6. Offline and failure are designed states
No signal is the normal case in the woods. Every networked feature has a designed empty, loading and failed state that says what happened and what still works, in plain words. Cached or old data is labelled as such, not shown as live.

### 7. Battery is a design cost
Screen-on time, update rates and animation are interface decisions. The user should not have to manage the app to get through a day. State the battery cost of any design that keeps the screen, GPS or a listener active longer.

## How to apply

1. Run prior-art-before-interface first. A convention people already know is the cheapest way to avoid making them think.
2. For each new or changed element, write one line per relevant rule: the user's question, and how the element answers it without thought.
3. For each element that simplifies, summarises or estimates, state what was left out and confirm nothing shown is untrue in any reachable state.
4. Report any element that fails either governing rule, and any conflict between rules, rather than resolving it silently.
5. Say which parts of the design can only be confirmed on a device or in the field, and route those to device-check-authoring.

## Evidence status of these rules

The honesty rule and rules 3, 4, 5 and 7 trace to CLAUDE.md or recorded project findings. Rules 1, 2 and 6 are inferred from the app's purpose and general mobile practice, not from field data on Forager. Tester feedback or field walks that contradict any rule supersede it; record the finding per record-and-supersede.