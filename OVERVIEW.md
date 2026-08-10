# Evidence Gated Development: Overview

This is the document to read first, and one of only two written for you. PHILOSOPHY.md, ENFORCEMENT.md, and BOOTSTRAP.md are written for the agents: the principles, what an agent does about each one, and the short version an agent loads at every session start. GLOSSARY.md is the machine-checked index binding the first two together, plus the marker vocabulary. You can read any of them, and the philosophy is worth reading once, but they are instructions to be followed, not explanations. The explaining happens here.

## The problem this solves

AI coding agents are fast, confident, and occasionally wrong in ways that look exactly like being right. That combination is the whole problem. A slow agent that failed loudly would be easy to manage. What you get instead is a plausible answer, delivered at speed, with no signal attached telling you which category it falls in.

The usual response is better prompting. Longer instructions, more examples, more warnings about what not to do. That works until the session gets long or the task gets unfamiliar, and then it quietly stops working, and you find out later.

EGD takes a different route. Instead of trying to make the agent more careful, it changes what counts as done. A change is not done because the agent says it works. It is done when evidence exists that it works, produced in a form you can check. The agent can still be wrong. It just cannot be wrong invisibly.

That is the whole idea. Everything else is mechanism.

## Why the gates are where they are

Some of these principles came from a specific failure that cost real time. Others were generalized outward from those failures and have not themselves been tested. Worth knowing which is which, and the philosophy says so about itself rather than presenting the whole set as hard-won.

The four below are in the first category.

Confirm the check fails before you fix the bug. If you write the fix first and the check passes, you have learned nothing. Maybe the fix worked. Maybe the check never tested the thing. You cannot tell those apart after the fact, and an agent will report both as success.

Two failed fixes means stop and get data. Not three, not five. Two consecutive misses on the same symptom is strong evidence the model of the problem is wrong, and a third guess built on a wrong model is just a slower way to arrive at the same place.

Record intent before touching a file. Sessions get interrupted. Context windows fill. If the only record of your work is the finished work, an interruption leaves you with half a change and no idea what it was for.

Append only, never overwrite. The value of a record is that it tells you what you believed at the time. Edit it to match what you believe now and you have destroyed the only thing it was good for.

You will notice none of these require the agent to be smart. They require it to be observed. That is on purpose.

## The three roles

Three roles, and the separation between them is doing real work. Blur them and the failure modes come back.

**The operator.** That is you. The coder runs code and reports results, so it does see some real output. What it cannot see is anything outside the run it was told to make. You notice the number that is off by a factor of two in a place nobody thought to look. You catch the thing that only shows up on the third day. Every fact about the system that was not produced by an instructed run enters this project through you.

That is a narrower claim than owning reality outright, and it is the one that holds. It is also the one that matters, because unexamined behavior is where the expensive problems live.

**The planner.** An agent that discusses bugs, weighs designs, plans task sequences, and writes the prompts the coder receives. It never touches files and never runs anything. Its job is thinking, and keeping it away from execution is what protects the thinking. An agent that can act on an idea tends to act on it before the idea is finished.

Use this role to argue. Bring it a symptom and let it propose three explanations. Ask it what evidence would distinguish them. That conversation is where the value is.

**The coder.** An agent that executes code and edits documents. It is the only role that does either. It works from a prompt the planner wrote and you approved, it reports what happened, and it makes no architectural decisions. If it hits an ambiguity it stops and asks rather than picking.

One rule holds the whole structure together: the coder never decides, and the planner never touches. Everything the operator needs to know flows through those two constraints.

## What a run actually looks like

Abstract roles are easy to nod at and hard to use. Here is the loop with a real shape to it. The feature is resume capability for a long running batch job, and the details do not matter much. The rhythm does.

**You open with the planner.**

> I want the batch job to be resumable. If it dies at item 400 of 1000, I want to restart and pick up where it left off.

**The planner asks rather than builds.** This is the part that feels slow and is not.

> A few things I need before this is worth planning. When a run dies mid item, is that item's output partial on disk or absent? What identifies an item, an index or something stable? And is a restart allowed to assume nothing else changed, or should it detect that the input set moved under it?

**You answer from the machine.** Two of those you know cold. One you have to go check, and that checking is the whole reason this step exists.

> Output is partial. I have seen truncated files after a kill. Items have stable IDs, not just indices. Input set changing under a restart is possible but rare, and I would rather it refuse than guess.

**The planner may surface something you were not thinking about.**

> The partial file is the interesting one. If resume skips items that have output present, a truncated file gets counted as done and the run finishes with silent corruption. That is worse than not having resume at all. Options are a completion marker written after the file closes, or verifying each existing output before skipping it. The marker is cheaper. Verification catches more.

That is the payoff for asking. You would have found it eventually, most likely at a bad moment.

**You close the decision.**

> Marker. Verification is more than this needs and I do not want the read cost on every resume. Refuse on changed input set, do not guess.

**The planner signals readiness.** It does not just start writing.

> That is everything I needed. Ready to write the coder prompt. How do you want it formatted?

**You approve and set the format.**

> Go ahead. Numbered steps, checks first, and call out anything I have to verify on the machine myself.

**The planner writes the prompt.** You read it before it goes anywhere. This is a real gate, not a formality. If the prompt contains a decision you did not make, that is the moment to catch it, and it is much cheaper here than in a diff.

**You pass it to the coder.** The coder executes and reports back. What you want out of that report is what happened, not reassurance.

> Wrote the check for resume-skips-completed first. Confirmed failing (no marker logic exists). Implemented marker write after file close, added the input set fingerprint comparison on startup. Check passes. Note: I did not touch the cleanup path for orphaned partials, since your scope boundary did not cover it. Flagging it because a resume now leaves those files in place indefinitely.

**Back to the planner with the report.** The flag at the end is the thing to carry over. That is a real gap the coder correctly refused to decide about.

> The orphaned partial issue is legitimate. Options are cleaning them at resume, cleaning them at completion, or leaving them and documenting it. Cleaning at resume is the only one that bounds disk growth, but it deletes data on startup, which is a destructive default.

**And around again.** You decide, the planner prompts, the coder executes, the report comes back. The loop keeps running until the feature is done or you decide it is done enough.

Notice what did not happen. Nobody decided anything except you. The planner surfaced a corruption risk and named the options. The coder found a real gap and stopped instead of solving it. Both of those are the roles working, not the roles failing.

Notice also how much conversation happened before a line of code got written. That ratio is normal here, and it is where the savings come from, even though it does not feel like it at the time.

## You are in charge

This part matters more than the mechanics, so read it twice if you skim.

Agents will ask you for permission constantly. Should I proceed. Would you like me to. Shall I go ahead and refactor this. It is a habit of the format, and it quietly inverts the relationship if you let it. You start waiting on the agent to tell you what is next.

You approve. You do not ask.

Practically, that means a few things.

You decide when a decision is closed. If the planner keeps reopening a choice you already made, tell it the call is closed and move on. Open questions are the agent's job to surface. Closed ones are yours to declare.

You decide what evidence is enough. An agent will happily report a test passing. Whether that test proves anything is your judgment. If it does not convince you, it is not enough, and no amount of confident phrasing from the agent changes that.

You are allowed to say no to your own tooling. If a gate is slowing you down on a throwaway experiment, skip it and say so out loud in the record. EGD is not a compliance regime you answer to. It is a set of defaults you chose because they saved you time, and you can suspend one deliberately. The thing to avoid is drifting past a gate without noticing, which is different.

You correct the agent, not the other way around. When an agent tells you your approach is wrong, that is input. Sometimes it is right and you should update. But it is arguing from text and you are arguing from the machine in front of you, so weigh it accordingly.

Being in charge is not the same as being right. Those are separate things and it helps to keep them separate. Deciding is your job. Being correct every time was never part of it, and a workflow that required it would have fallen over already.

## Working the problem together

The roles are partitioned so nobody has to carry the whole thing alone. You hold ground truth, the planner holds breadth, the coder holds execution. None of those is sufficient by itself, which is the point.

An agent has read a great deal of code that you have not. Sometimes it will surface an approach you had not considered, or name a failure mode that has a well known solution, or point out that the thing you are building by hand already exists. That is worth having. The value is not that the agent knows better. It is that it knows differently, and different is where the useful surprises come from.

So when a gate turns out to be impractical, treat it as a problem to solve rather than a test you failed. Say what is not working. The record store entry can be one line: this gate cost more than it caught, here is what happened. Then ask what else would get the same coverage. There is usually a cheaper version, and sometimes the answer is that the gate was aimed at the wrong risk in the first place.

The same goes for the plan. If a task sequence feels wrong when you get into it, that reaction is data, and you are the only one holding it. Bring it back to the planner as a symptom rather than a verdict. What is bothering me is this. Something along those lines opens the conversation where an announcement closes it, and you frequently learn the reason on the way.

What you are not doing is waiting for permission, and what you are also not doing is going it alone. The middle ground is the one that works: you decide, and you decide with better information because you asked first.

## What you cannot hand off

Delegating the typing does not delegate the judgment. You moved from writing the code to owning the direction, and reviewing prompts and results is what that job consists of. It is real work and there is no version of this where it disappears.

Two places carry weight that nothing else can cover.

The prompt, before it goes out. The coder validates its prompt structurally, but it cannot notice a decision it was never told about. Only you know what you closed last week. If a decision is missing from the prompt, nothing downstream will catch it, and the coder will make that decision without knowing it was making one.

The result, when it comes back. A report can be complete, accurate, and still describe something you did not want. Every gate in this system checks whether the work matches its instructions. None of them check whether the instructions matched your intent.

Sometimes you cannot verify. The thing needs expertise you do not have, or instruments you do not have, and no amount of care changes that. You have three honest options: get the means, get a person who has them, or record the output as unverified and let that label travel with it. Unverified is a legitimate state. What is not legitimate is unverified work entering the record as though someone checked it.

## About running on autopilot

You can hand an agent a long task and let it run. Sometimes that is the right call, and the gates will keep it from the worst outcomes. A good agent will try to hold your intent while you are away.

Understand what you get back. The work will be internally consistent, checked against its own instructions, and unvetted against your vision. Nobody compared it to what you actually wanted, because the only party who could was not in the room.

Trying is not the same as succeeding. These documents reduce how often an agent goes wrong and how far it gets before someone notices. They do not make it reliable in the sense of not needing to be checked, and a methodology that claimed otherwise would be selling something. Nothing here is one hundred percent. Run the long unattended sessions when the cost of a wrong result is low, and read the output before it becomes a foundation for anything.

## When things go wrong

A few failure patterns come up often enough to name.

**The agent is confidently wrong about your system.** It will state facts about your code that are not true, usually because it inferred them from a pattern rather than reading. Fix: make it cite. Ask which file and which line. Confident claims collapse quickly under a request for a source.

**Fixes keep almost working.** Two attempts, two near misses, each with a good story. Stop. The rule exists precisely because the third attempt feels so reasonable. Go get logs, instrument the live path, build the minimal reproduction. It feels slower and it is not.

**Scope creeps mid task.** You asked for one change and the diff has six. Reject the whole thing rather than picking through it. A diff you have to audit line by line costs more than a redo, and accepting a bloated change teaches the pattern.

**The agent loses the thread.** Long sessions decay. Earlier decisions get forgotten or silently reversed. When you feel it happening, stop and restate the closed decisions explicitly, or start fresh from the record store. Do not try to nurse a degraded session back to health.

Starting fresh has a procedure, because a fresh agent absorbing the wrong context is just a degraded session with better manners.

1. Drain the working document first. Any `LESSON:` lines from the dying session go to the record store now, since they exist nowhere else.
2. Hand the new agent, in order: the bootstrap file, its role, the current intent record, and the closed decisions relevant to the task. Not the whole history. A fresh session's advantage is a clean context, and flooding it recreates the problem you left.
3. Confirm absorption before work starts. Ask it to state the task, the scope boundary, and the closed decisions in its own words. Reading back is cheap, and an agent that nods along without absorbing is the failure you are checking for.
4. If the old session produced uncommitted work, check its intent record for a terminal entry. Unterminated means the work's status is unknown: you rule on it before anyone builds on it. Terminated as completed means the new agent verifies it against the record. Abandoned means the record itself says whether it is safe to build on.

**You realize a past decision was wrong.** Append a superseding entry. Do not go back and edit the old one to look correct. The wrong decision and the reason it was wrong are frequently more useful later than the right one.

## When not to use this

EGD is built for code whose outputs get reported, published, or relied on. That is a real category and it is not every category. Some honest exclusions:

Throwaway experiments. If the code exists to answer a question and then be deleted, the answer is the output and the code needs no provenance. Gate the finding, not the script: the result that survives goes in the record store, the script does not need a changelog.

Exploratory spikes. When you do not yet know what you are building, intent records ahead of every change just document your confusion in longhand. Spike freely, then bring the survivors through the gates when they graduate to real code.

Code nobody measures with. A convenience script, a one-off formatter, a demo. If no number it produces will ever be trusted, the traceability machinery is cost without benefit.

The test is simple: will anyone, including future you, rely on what this code reports? Yes means the gates apply. No means they are optional, and saying so out loud is cheaper than pretending otherwise. A methodology that claims to apply everywhere usually applies nowhere in particular.

And per the philosophy's own standard: note which gates keep catching things and which never fire. That record is the difference between a methodology you have evidence for and one you merely like.

## Getting started

First, install the agent-facing documents where the agents will actually see them. BOOTSTRAP.md goes wherever your tooling injects standing instructions: a CLAUDE.md at the repo root, the project instructions of a chat project, or the system prompt of whatever harness you use. The planner and coder both get it. ENFORCEMENT.md, PHILOSOPHY.md, and GLOSSARY.md live in the repo where agents can read them on demand; they are not loaded into every session, and the bootstrap's reading protocol says when each is consulted. If your setup separates the planner from the coder (different projects, different tools), install the bootstrap in both, since it is the one document each role always has.

Then set up the four pieces of infrastructure in the enforcement companion. That is one afternoon. While you are there, agree on your marker prefixes; the working set and what each drains to is the small table at the bottom of GLOSSARY.md, and `LESSON:`, `OPEN:`, `CLOSED:`, and `DEFER:` are enough to start.

Then run one small task through the full loop. Record intent, write the check, watch it fail, make the change, watch it pass, log the deviation from what you planned. The first pass will feel like too much ceremony for the size of the change. Do it anyway, once, so you have felt the whole shape of it.

After that, the honest advice is to adopt the gates that keep catching things and stay skeptical of the ones that never do. The philosophy is a hypothesis, and it says so about itself. Treat your own experience with it as evidence, which is what it asks of everything else.

## Testing the methodology itself

If you are trialing EGD (on a branch, a side project, anywhere reversible), hold the trial to the same standard as any change: an intent record with a prediction and a finish line, written before the trial starts. Otherwise the test of the methodology violates the methodology, and worse, you will not be able to say afterward what you learned.

A minimal trial record looks like this. Prediction: which gates you expect to fire, and roughly how often, over the trial. Finish line: a fixed number of tasks or a fixed duration, stated up front, not extended because things feel promising. Abort conditions: what would make you stop early. Log: every gate that fires and what it caught, every gate that costs time and catches nothing, every time you bypass a gate deliberately.

At the finish line, compare against the prediction and write the terminal entry. Gates that fired earn their place. Gates that never fired are candidates for the appendix, not automatically failures, since a gate can be load-bearing and rare. Gates you kept bypassing are telling you something about either the gate or the project, and the log is what lets you tell which.

One cheap experiment worth folding in: run part of the trial with PHILOSOPHY.md available to the agents and part with only BOOTSTRAP.md and enforcement entries. Whether rationale in context improves agent judgment on unanticipated cases, or just spends tokens, is an open question these documents cannot answer about themselves. Your trial can.
