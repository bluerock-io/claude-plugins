# Session 7 — checkpoint verification spec

**This session has the weakest verification in the path, and the spec has to be
honest about it.** The routine lives outside the project, in Anthropic's cloud.
No command you run from here can see that it exists, when it runs next, or
whether the browser grant was given. Two kinds of evidence, and never blur them:

- **Inspectable** — a state you can check from this session with a command. The
  only evidence that can mark a checkpoint passed on its own.
- **Reported** — a state that lives off this machine (the Routines page, a browser
  consent window). Ask what the builder *sees*, never "did it work?", and treat
  the description as provisional until its nearest inspectable consequence
  appears. **For this session that consequence is checkpoint 5**, which is why
  step 5 fires the routine by hand instead of waiting for the clock. A clock does
  not produce evidence for twenty-four hours; a manual fire produces it now.

Run inspection commands quietly; the builder sees conclusions, not plumbing.
`<project>` is the project's absolute path.

## Checkpoint 1 — a job, a cadence, and the trigger it earned

- **Conversational:** they name one job they already dispatch by hand, its
  cadence, and which of `/schedule`, `/loop`, or "stays ad hoc" it earned.
- **"This one stays ad hoc" is a full pass.** If the job only repeats when
  something happens rather than on a clock, choosing not to schedule it is the
  correct answer to the step's question — they still learned the decision. Then
  find a second job for the rest of the session, or schedule `daily-brew` as the
  worked example and let their real one stay manual.
- Vague cadence ("regularly") isn't ready: push once for a day and a time. The
  command in step 4 needs it.

## Checkpoint 2 — two sentences, the second naming a real path

- **Conversational, or inspectable if they drafted it in a scratch file.**
- **Pass spec, both halves:**
  1. the job sentence names a specific agent and what it should do;
  2. the destination sentence names a **path inside their project**, plus commit
     and push.
- **Hold the second sentence hard — this is the highest-value check in the
  session.** A missing or vague destination is the single most common reason a
  first routine "does nothing," and the failure is invisible: the routine runs
  faithfully into a transcript nobody opens. `briefs/<today's date>.md` passes.
  "Save it to my project" does not — which folder, which filename?
- If they can't say the whole thing in one breath, it isn't ready. Tighten before
  step 4 rather than debugging a live routine.

## Checkpoint 3 — the fallback, found and understood

- **Inspectable:** the relevant spec has a scheduled-dispatch branch.
  - For `daily-brew` (the default): `.claude/agents/daily-brew.md` contains its
    scheduled-dispatch instruction — do not ask a question, produce a stub brief
    from `CLAUDE.md` alone. It ships with the project, so this passes on a
    fresh workspace; the work of the step is that **they read it**.
  - For their own agent: they added such a branch, and it's in the file now.
- **Conversational half, required:** they can say in one sentence what the agent
  does when a scheduled run has no inputs, and **why that branch must not ask a
  question.** The "why" is the checkpoint. "It does a short brief instead" is
  half an answer; "because there's nobody there to answer, so a question would
  just stall it" is the whole one.
- If they added a fallback to their own agent, verify it says both things: don't
  ask, and don't invent. A fallback that asks is not a fallback.

## Checkpoint 4 — the routine exists

- **Reported, and it cannot be otherwise.** Ask what their Routines page shows:
  the routine listed, with a next run time. Take their description.
- **Also reported: the browser grant** (first routine only). You cannot complete
  it, confirm it, or see its result. Ask what they saw. If they never saw an
  authorization window, treat that as unresolved rather than fine — it is the
  most likely reason checkpoint 5 will fail, and catching it here saves a
  confusing failure later.
- **Do not mark this checkpoint complete on the command having been typed.**
  `/schedule` running without an error is not evidence the routine was created.
  The nearest inspectable consequence is checkpoint 5; say so and move straight
  there rather than declaring success.
- If they report a next run time that doesn't match what they intended, fix it
  now — that's cheaper than discovering it on Saturday.

## Checkpoint 5 — the result landed where the instruction said

**The real checkpoint of the session, and the only fully inspectable one.**

- **Inspectable, after the pull:** the file named in their instruction exists
  under the project, with fresh content and a recent timestamp — e.g.
  `briefs/<today>.md`. Check the path they actually specified in checkpoint 2, not
  a path you assume.
- **The pull is a required step, not a detail.** The routine backed its result up
  to GitHub; the builder's own copy does not have it until they pull. **A missing
  file before a pull proves nothing** — pull first (`git -C <project> pull`, or
  have them ask Claude Code to), then look. Diagnosing "the routine didn't work"
  on an un-pulled repo is the easiest wrong conclusion in this session.
- **Then the schedule read-back**, also part of the checkpoint: the next run time
  means what they meant. "Daily" and "weekdays" disagree on Saturday morning.
  Ask which they intended.
- **Failure diagnosis, in order:**
  1. File absent after a pull → the instruction's destination was too vague.
     Tighten the path, fire again. This is the common case.
  2. No commit pushed at all → the grant is missing or was declined. Back to
     checkpoint 4.
  3. File present but thin → check whether the fallback fired. No notes filed
     yesterday produces a short honest brief, which is **the system working
     correctly.** Read the brief's own line saying so, and pass. Do not treat an
     honest stub as a failure; that inverts the lesson.
- **If the manual fire is impossible** for an environment reason, the session
  stays `in_progress` at checkpoint 4 and you say so plainly. Do not mark the
  session complete on a routine that has never produced a file — that is exactly
  the courtesy completion the honest-state rule exists to prevent, and the builder
  will find out at 7am.

## Marking progress

After each verified checkpoint N:
`sessions["7"] = { "status": "in_progress", "checkpoint": N }` — and on
checkpoint 5, `{ "status": "complete", "completed": "<today>", "artifact":
"<their routine> on <cadence>, landing in <path>" }`. Write valid JSON; never
delete history. Never mark a checkpoint you didn't verify — honest state beats a
green dashboard, and in this session that rule does most of its work.
