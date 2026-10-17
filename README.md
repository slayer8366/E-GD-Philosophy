# Evidence Gated Development

A working method for AI-assisted development where the output has to be correct and reconstructable.

## The problem

AI coding agents are fast, confident, and occasionally wrong in ways that look exactly like being right. That combination is the whole problem. A slow agent that failed loudly would be easy to manage. What you get instead is a plausible answer, delivered at speed, with no signal attached telling you which category it falls in.

The usual response is better prompting. Longer instructions, more examples, more warnings about what not to do. That works until the session gets long or the task gets unfamiliar, and then it quietly stops working, and you find out later.

EGD takes a different route. Instead of trying to make the agent more careful, it changes what counts as done. A change is not done because the agent says it works. It is done when evidence exists that it works, produced in a form you can check. The agent can still be wrong. It just cannot be wrong invisibly.

## How it works

Three roles, and the separation between them does real work.

The **operator** is you. You hold the goal, you close decisions, and you observe the system outside what an agent was told to run. The **planner** discusses, designs, and writes prompts, and never touches a file. The **coder** executes and edits, and never makes a design decision. An ambiguity is a stop-and-ask, not a judgment call.

Around that sit the gates. Record intent before touching a file, including a prediction that can turn out wrong and a finish line stated up front. Watch a check fail before you write the fix. Append to the record, never edit it. After two failed fixes on one symptom, stop guessing and go get data.

None of these require the agent to be smart. They require it to be observed. That is on purpose.

## What's here

| File | For | What it is |
|---|---|---|
| `OVERVIEW.md` | Humans | Start here. Why any of this exists and how you run it. |
| `PHILOSOPHY.md` | Agents | 45 principles, each stating what is true. |
| `ENFORCEMENT.md` | Agents | What an agent does about each principle. |
| `BOOTSTRAP.md` | Agents | One page, loaded every session. |
| `GLOSSARY.md` | Machines | The index binding philosophy to enforcement, verified by script. |
| `check_*.py` | Machines | The boundary checks. |
| `ADOPTING.md` | Both | How to run the record checkers on any repository, shaped to its own record by a `records.json`. |
| `records_lookup.py` | Both | Read-only lookup over Forager's and forager-forecast's records (show, links, search, open, next-id), every answer cited by repository, ref, commit, file and line (`specs/2026-10-16-records-lookup.md`). |
| `RECORD.md` | Both | The append-only record store. |
| `prompts/` | Both | Every prompt dispatched, preserved verbatim. |
| `PROTOCOL.md` | Both | Working rules on probation: candidates that have not yet earned a place in the philosophy, each with its evidence. |
| `DURABILITY.md` | Both | What an unpushed record store cost, and the rule that followed. |
| `REGISTER.md` | Machines | The append-only log of observed check failures, written by `check_register.py`. |
| `BUILD_TASKS.md` | Both | Two early tooling task records, kept as written. |
| `RECORDING.md` | Both | How the record is kept: what every entry carries, what goes in, and the twelve entry types. |
| `trials/` | Both | Readings of projects that have run the method: what fired, what was dropped, what decayed. |
| `skills/` | Agents | The operator's skills, which the agent harness loads when their triggers fire, mapped to the principles they carry out. |
| `specs/` | Both | Specifications awaiting or carrying the operator's approval, each read against named commits. A spec is not a go to build. |
| `profiles/` | Agents | Role profiles, each named by its role from the project's scope and written from the record (PROTOCOL rule 22). |

`OPERATOR_PROFILE.md`, listed in this table until 2026-10-16, was lost with the first record store (see `DURABILITY.md`) and has not been rebuilt.

## What it has actually been through

The documents were reasoned into existence, then run against real work on this branch for two phases. That trial is in `RECORD.md`, prompts and all, including the parts that went badly.

Some of what it found:

Six planner errors were caught by an agent stopping to ask. None were caught by a check. Five of the six were the same shape: the planner asserting the state of the repository from memory instead of from the repository.

One mechanism passed all eight of its checks and turned out to be impossible to use, because the fixture that verified it encoded a state the system forbids. That shape recurred three times through three different discovery routes before anyone named it.

One intent record is permanently unterminated. Its prediction was never written, so nothing can honestly close it, and it sits there unresolved rather than tidied away.

The prompts in `prompts/` are preserved exactly as dispatched, including a reference to a file that never existed, two contradictory section names in one document, and an instruction to close a record that was never opened. A prompt store that quietly fixes the planner's mistakes destroys its own evidentiary value.

A second project has since run it. Forager, a field app, adopted the method in September 2026, installed its gates as harness hooks on 2026-09-22, removed them five days later because they blocked actions the agents were expected to take, leaving the operator to hold the agent's hand at every step, and kept going without them. What fired, what was dropped, and what decayed once the checkers were gone is in `trials/forager-2026-10-16.md`. Its lessons are what the October 2026 changes to the philosophy and the protocol rest on.

## What this does not claim

The trial was scoped to whether the set surfaces gaps. It did. It says nothing about which of the 45 principles are load-bearing, and anyone reading this should not infer that they all are. Several were generalized outward from a single incident and have never been tested.

This is one sustained case study. Treat it as a hypothesis with a paper trail, not a framework with a track record. The documents say the same thing about themselves, which is either reassuring or a bad sign, depending on your priors.

## Trying it

Read `OVERVIEW.md`. Set up the infrastructure it describes, four pieces or three if your outputs are not data artifacts, which is one afternoon. Run one small task through the whole loop, ceremony included, so you have felt the shape of it.

Then adopt the gates that keep catching things and stay skeptical of the ones that never do. Your own experience with it is evidence, which is what this asks of everything else.

## Contributing

The most useful contribution is a second data point. If you run this on your own work, the trial record matters more than an opinion about the principles. Open an issue with what fired, what cost time and caught nothing, and what you bypassed.

Disagreement with a principle is welcome and should come with the case. Every one of these can be wrong, and several probably are.
