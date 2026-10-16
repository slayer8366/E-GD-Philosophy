# Durability

Written after the fact, from what a direct check found, not from a plan.

## What happened

This repository's `Test-1` branch, on GitHub, holds three commits and
eight template files — `README.md`, `OVERVIEW.md`, `PHILOSOPHY.md`,
`ENFORCEMENT.md`, `BOOTSTRAP.md`, `GLOSSARY.md`, `check_glossary.py`,
`LICENSE`. That is the entire real state of this repository as of this
commit.

It is not the only work that existed. A separate project (`OSCam`,
`~/imx`) vendored code from this repository's `check_record.py` at a
commit it names as `5d7af96`, and cites two entries from a `RECORD.md`
this repository does not contain — `2026-08-10-24` and `2026-08-10-29`.
Neither the commit, nor `check_record.py`, nor `RECORD.md` exists
anywhere in this repository's reachable history. `git cat-file -t` on
`5d7af96` returns "not a valid object" — not stale, not on another
branch, not reachable by any ref this remote holds.

The only explanation consistent with what's checkable: that work was
done in a clone that lived in a container's `/tmp`, was never pushed,
and stopped existing the moment the container did. Roughly a session's
worth of work — a task-record store, a validator script, the specific
history OSCam's own vendored copy is the last surviving fragment of —
is gone. Not hard to find. Not recoverable. Gone, in the ordinary sense
of the word.

## The rule

**A commit that has not been pushed is not durable. Treat it as if it
does not exist, because for planning purposes it doesn't.** `git commit`
guarantees the work survives the next command in the same shell. It
guarantees nothing about surviving the environment that shell is running
in. `/tmp`, a container filesystem, a sandbox workspace — none of them
are promises, and a local branch sitting unpushed in one of them is
exactly as fragile as no branch at all the moment that environment goes
away, which it will, on a schedule nobody working inside it controls.

Two things follow, both mechanical:

1. **Clone anything meant to outlive the session into a path that
   survives a reboot** — this machine's home directory, not `/tmp`, not
   `/workspace`, not anywhere a container's own lifecycle owns. Ask,
   before the first commit, whether the working directory is one of
   those places. If it might be, it is.
2. **Push after committing, not after a batch of commits, not at the
   end of a task.** The gap between commit and push is exactly the
   window this failure lived in. A push is the only step in this loop
   that leaves the machine, and leaving the machine is the only thing
   that makes work survive the machine disappearing.

Nothing here is a claim that this will not happen again for some other
reason. It is a claim that it will not happen again for *this* reason,
because this reason is now checked instead of assumed.

Promoted on 2026-10-16 to PHILOSOPHY.md as Durability Is Location, with Forager's instances (RECORD.md 2026-10-16-01; trials/forager-2026-10-16.md).
