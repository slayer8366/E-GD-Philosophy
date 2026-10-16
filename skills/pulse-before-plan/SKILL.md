---
name: pulse-before-plan
description: How to get a fresh, read-only reading of a repository's current state before writing a plan that depends on it, by sending a pulse the coding agent answers with file-and-line evidence. Use this whenever you are about to specify work against a repo you last read hours or days ago, whenever a plan hinges on where something lives or whether it exists, and whenever you catch yourself writing "it's probably at" or "the convention is likely". Use it especially when you feel confident, because a confident stale read is indistinguishable from a current one until it costs a dispatch.
---

# Pulse before plan

A plan written against a remembered repository is a plan built on a snapshot. Branches move, files get renamed, decisions land. The gap between what you last read and what is true now is invisible from where you sit, and it does not announce itself — it shows up as a dispatch that asks for something impossible, or specifies a path that no longer exists, or reverses a decision made an hour ago.

The fix is cheap. Before writing the plan, ask.

## What a pulse is

A short, read-only request for facts. No code changes, no commits, no judgment calls. The agent checks the repo and reports back with file-and-line evidence, and you write the real plan against what comes back.

It is not a dispatch. Nothing is built. Nothing is decided. If the answer surprises you, that is the pulse working.

## What belongs in a pulse

Things a grep, a `git log`, or a file read can settle:

- Where something lives, and what the surrounding convention is
- Whether a file, function, or path exists at all
- The current branch head and what has landed since a known commit
- The state of something in flight — a probe, a run, a question left open
- What an existing document's form is, when you are about to write one to match it

Ask for plain answers, including negative ones. "There is no such directory" is a complete and useful reply. What you want to prevent is an agent inferring what you probably meant and answering that instead.

## What does not belong in a pulse

If you are asking the agent to make a judgment — which of three designs, whether a fix is worth it, how something should be structured — that is a stop-and-ask or a dispatch. A pulse that smuggles in a decision gets one made, and it will be defensible and not yours.

If you are asking something you could check yourself in the time it takes to write the question, check it.

## Bundle

One pulse with six questions costs one round trip. Six pulses cost six.

Bundling also gives the agent enough context to notice what you did not think to ask. This is consistently the most valuable part: the reconnaissance that answers your six questions and adds a seventh finding you needed and did not know to request.

Say what the plan hinges on, briefly, so the agent can tell you when your framing is wrong rather than only answering the literal question.

## Then write the plan against the answer

Not against your memory of the answer, and not against the answer plus the assumptions you were already carrying. If the pulse contradicts something you believed, carry the correction forward explicitly rather than quietly absorbing it.

When a plan still rests on something the pulse did not settle, say so in the plan and ask for it to be verified before building. Uncertainty that is marked is survivable. Uncertainty that reads as fact is what costs the dispatch.

## Stale reads age faster than they feel

An hour is enough on an active branch. If a report has arrived since your last read — a fix landed, a branch moved, a question closed — your picture is already behind it.

The tell is the phrasing you reach for: "it's probably at", "the convention is likely", "as of when I looked". Each of those is a pulse you have not sent yet.
