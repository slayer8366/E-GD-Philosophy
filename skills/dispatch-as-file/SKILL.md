---
name: dispatch-as-file
description: How to deliver a task as a committed document in the repository rather than a chat message, so the agent reads the original instead of a relay and a later session can cite it. Use this whenever you hand off implementation work, whenever a specification would otherwise live only in a transcript, and whenever a decision you make in conversation will shape code someone writes later. Use it especially for small tasks, because a one-line ask in chat is exactly the kind that gets reconstructed wrongly a day later.
---

# Dispatch as file

A task sent as a chat message exists in one place, is readable by one party, and cannot be cited. A task committed to the repository is read by the agent directly, quoted in the report that answers it, and findable by a session that starts fresh six months later.

The failure this prevents is concrete: a specification that lives only in a transcript gets paraphrased into a one-line ask, the agent cannot find it, and it has to reconstruct the requirement by inference. Sometimes the inference is right. The cost of finding out is a full round trip, and sometimes the inference is wrong in a way nobody notices.

## Establish the convention before writing the first one

Where dispatch documents live and how they are named is a property of the repository, not something to assume. Ask, or check, before writing the file. If an existing dispatch document exists, match its form.

Date-plus-slug naming keeps them sorted and greppable, and matches how most audit and decision directories already work.

## Open with the state it was written against

A dispatch read later, without context, reads as though its premises were timeless. They are not. Several are superseded within a day.

The first lines should say: the commit or branch head, the PR it belongs to, what had been established at the time, and what was still open. This is what lets a future reader tell whether the dispatch's reasoning still applies or was overtaken.

## Do not state repo facts you have not checked

A dispatch written from a remembered read will contain paths and line numbers that were true once. Put those in a verification section rather than in the instructions: ask the agent to confirm them and report before building, rather than asserting them as the ground the work stands on.

Where you are reasoning from a stale read, mark it as such. An instruction that quietly contains a wrong premise gets built on.

## Structure

The body is a normal dispatch: verify first, what to build, what not to touch, the alternatives already rejected, the evidence required, and the device-only items enumerated separately. Writing it as a file changes none of that — it changes who can read it and when.

What the file form adds is that the report answering it can cite it by path, and the index row can point at both.

## Decisions belong in the record too

When a conversation resolves an open question — which of three designs, whether a cost is acceptable, what a setting should mean — that resolution shapes code. Left in a transcript, it becomes a claim someone half-remembers.

Commit it: a decision record, an index row, a line in the dispatch that carries it. The test is whether a fresh session could find the reasoning without asking anyone.

## What not to put in the repo

Credentials, tokens, and anything else that should not outlive the moment. The point of committing a dispatch is durability, which is exactly wrong for a secret.
