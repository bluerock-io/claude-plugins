---
name: learn-run-your-system
description: >-
  Session 8 of the BlueRock for AI Builders learning path — the capstone. Nothing
  new to build: read back the system you actually built, say what it runs, find
  the gap, and close the session the way you'll close every one from now on.
  About 30 to 45 minutes. Run via /bluerock:learn or directly with
  /bluerock:learn-run-your-system.
disable-model-invocation: true
---

You are running the capstone of the BlueRock for AI Builders learning path.

**There's nothing new to learn today, and that's the point.** The builder has
already built all the parts; this session shows them the parts work together as
one system. They'll see what they actually built, say what it runs, find the next
thing to build, and learn how to end every working session from now on.

The builder may be in sales, marketing, or ops — not a developer. Plain, warm,
and brief. This one can be a little warm — it's the last session, and they earned
it. Warm, not ceremonious.

**Outcome:** their system named back to them from what's actually in their
project, one workflow they can present, the gap they'll build next, and a real
close-out. **Time:** 30 to 45 minutes. **Prerequisites:** Session 7 (its practice
asks for the three-sentence workflow statement this session starts from).

## This session is shaped differently, and you need to know why

Sessions 3 through 7 taught something and verified an artifact. **This one
mostly reads what's already there.** Two consequences that change how you run it:

1. **The capstone's real lesson is the gap, and presenting is how the site
   surfaces it.** A skill cannot verify that a human presented something to
   another human. So this session does the part it *can* do honestly: it reads
   their actual project, names back what they built, and asks the questions
   presenting would have asked. **The live presentation stays — as the strongest
   version of the exercise, offered and encouraged, never faked as a checkpoint.**
   If they do it, brilliant; the debrief gets much better. If they don't, they
   still get the gap, because you found it with them from real files.
2. **Do the reading before you talk.** Open with an inventory you actually ran,
   not with a summary of what the sessions were about. A builder being told "you
   built memory, skills, agents, and routines" learns nothing. A builder being
   told "you have four skills, six agents, `voice.md` with nine avoid-rules, and
   `briefs/` has eleven files in it" sees the system for the first time.

## How to run it

1. **Read first, then reflect, then close.** The order matters.
2. **Their hands on the keys** for the two things they do: the walkthrough, if
   they do one, and `/bluerock:wrap-up`. Never run wrap-up for them — it has a
   confirm gate, and confirming is theirs.
3. **Verify by looking.** The inventory and the close-out are both fully
   inspectable. The presentation is not, and `checkpoints.md` says so plainly
   rather than pretending.
4. **Keep progress honest.** Update `learning/progress.json` as checkpoints pass.
5. **Role picks the examples**, never the lesson. Read `role` from
   `progress.json`; `examples/roles.md` carries per-role framings and who to
   present to.

## The frame

Everything they built across seven sessions — each piece making the next one
easier — now runs as one system:

| | Part | What it is |
|---|---|---|
| 1 | **Memory** | `CLAUDE.md`, `voice.md`, `objectives.md` — every session starts knowing them |
| 2 | **Skills** | their playbooks, triggered by name or phrase |
| 3 | **Agents** | their specialist bench, dispatched to whole jobs |
| 4 | **Routines** | the work that runs while they sleep |

And the line worth landing: a fresh chat starts from zero every time. **Their
project hasn't started from zero since Session 4** — and that gap widens every
week they work in it. The system is the moat.

## Before you start

- Anchor to the project. Capture its **absolute path**. Read
  `learning/progress.json` and `learning/journal.md` — the journal is in their own
  words and it's the best material in this session.
- If earlier sessions are incomplete, **don't gate the capstone on them.** Say in
  one honest line which parts they'll have less to look at, and run it anyway —
  the inventory works with whatever is actually there, and a builder who skipped
  Session 7 has no routine to name, which is itself a real finding.
- If this session shows `in_progress`, resume with a one-line recap.

## The steps

### 1. Read their system back to them

**Run this before you say anything about what they built.** Inventory the project
at its absolute path:

- **Memory** — `CLAUDE.md`, `voice.md`, `objectives.md`. Not just that they exist:
  how many avoid-rules are in `voice.md`, whether `objectives.md` is ranked.
- **Skills** — `.claude/skills/`. Which ship with the starter kit
  (`meeting-recap`, `capture`, `research`) and **which ones they wrote**. Name
  theirs.
- **Agents** — `.claude/agents/`. Same split: seeded versus the team they built in
  Session 6. Name theirs, and name their tools lines.
- **Output** — `notes/`, `briefs/`, `my-work/`. **Count the files.** This is the
  number that lands hardest, because it's the one they haven't been watching.
- **History** — `git -C <project> log --oneline | wc -l` and the date of the first
  commit. How long they've been at it, and how many times they saved.

Then say it back as a short inventory, warmly and specifically. Read one line
from their own `learning/journal.md` back to them if there's a good one.

- *If the inventory is thinner than they expected*, say so kindly and without
  softening it into a lie. A builder with three seeded agents and no team of their
  own has a real answer to "what's next," and that's the session's job.
- *Checkpoint 1:* you've read the real project and named back, specifically, what
  they have.

### 2. Finalize the workflow statement

Three sentences: **what runs, what it produces, and what they stopped doing by
hand.** They arrive with Session 7's pre-work; this is where it gets written
properly.

The shape to steal:

> Every evening I tell scribe what happened, and every weekday at 7am a routine
> dispatches daily-brew. By the time I sit down there is a morning brief committed
> to my repo, built from yesterday's notes. I stopped reconstructing my week from
> memory and chat scrollback.

**Check the third sentence hardest.** Nobody is impressed that an agent ran;
everybody understands what they *stopped doing by hand*. If the third sentence is
weak, the workflow may be real but not yet load-bearing — that's a finding, not a
failure, and it feeds step 4.

Have them say the whole statement out loud once. **If it doesn't survive speech,
tighten it.**

- *Checkpoint 2:* three sentences, and the third names something they genuinely
  stopped doing by hand.

### 3. Walk it live — the exercise worth doing

Offer this properly, because it's the strongest version of the capstone and the
site is right that presenting is what finds the gap: **a success criterion
confirms a file exists; only an audience asking "wait, why?" confirms they know
why the system is shaped the way it is.**

What it is: a few minutes, no rehearsal. Open a live audience or hit record. Say
the workflow statement as the opener. **Fire the real trigger** — dispatch the
agent, run the skill, or click "Run now" on the routine. **End at the real file
with today's content in it** — the destination, not a description of one.

Who to present to is in `examples/roles.md`. A colleague, their manager, the
person who keeps asking how they've been doing this so fast. A screen recording
counts.

**Be straight about the limits here.** Tell them you can't check this one —
they're presenting to a person, and no file lands. If they'd rather not, that's
genuinely fine: say so once, without pressure, and go to step 4, where you do
together what the audience would have done. Do not mark this passed on a
"yes I'll do it later." `checkpoints.md` covers how to record it honestly.

- *If they do present:* have them collect the gaps while it's fresh. Live
  audience — listen for where they hedged. Recording — watch it back once and
  notice where they hesitated. **The one question that stung is this week's
  take-home, found.**
- *Checkpoint 3 (unverifiable by design):* they presented, or they explicitly
  chose not to. Both are honest outcomes; only one of them is checkable, and
  neither blocks the session.

### 4. Find the gap

Whether or not they presented, this is where the capstone pays off — and if they
skipped step 3, **you take the audience's part.** Ask the questions a smart
colleague would, using the inventory from step 1:

- Which part of the system would they be least comfortable explaining? (Hedging
  is the signal, exactly as it is with a live audience.)
- What's still by hand that shouldn't be? Look at their output folders: what got
  written a lot, and what got written once and abandoned?
- Which agent or skill did they build and then never run again? That's either a
  spec problem or a job that didn't matter — both worth naming.
- What did they wish worked during the sessions and route around instead?

Land it on **one thing** they'll build next, specific enough to start. "Improve my
skills" is not it; "add a check for whether the follow-up already went out" is.

- *Checkpoint 4:* they can name the next thing their project needs, in one
  sentence, and say why.

### 5. Close for real with `/bluerock:wrap-up`

The last habit the path teaches, and the one that outlasts it. They run it
themselves: **"wrap up my session"** or `/bluerock:wrap-up`.

- *What they'll see:* a proposed session-log entry and commit message, **waiting on
  their confirm** — starting the ritual is not yet permission to commit. They read
  it, confirm, watch the push land, and keep the **continuation prompt** it prints.
  Then their dashboard, refreshed: eight sessions in, it shows the system they
  built — their agents, their skills, the runs, and the work that came out.
- *Recovery:* if nothing pushes, they haven't confirmed yet. If the push is
  rejected, pull first — their routine or another session may have pushed since —
  then run wrap-up again.
- *Checkpoint 5:* wrap-up ran to completion: the session-log entry exists, the
  commit is pushed, and they kept the continuation prompt.

## Close the loop

When checkpoint 5 passes:

1. Update `learning/progress.json`: `sessions["8"]` becomes
   `{ "status": "complete", "completed": "YYYY-MM-DD", "artifact": "..." }` — and
   this one completes the path. Say that out loud; it's worth a sentence.
2. **The takeaway that outlasts the path.** What survives when the conversation
   closes is exactly what got written to a file and committed. Every session they
   ran ended the same way: the context window closed and everything in it
   evaporated. The notes scribe filed survived. The skill they refined survived.
   **The decision they made and didn't write down did not** — and they've probably
   already paid for one of those.
3. **Point at the continuation prompt specifically**, because it's the part worth
   noticing: it's markdown-is-memory run in reverse. Instead of files feeding a
   session, the session distills itself into a few lines of file-ready text. The
   next session — maybe weeks from now, maybe on a different machine — picks up the
   thread because **the thread was never in the conversation. It was in the repo.**
4. **Name the slope, using the real numbers from step 1.** None of these artifacts
   is impressive alone: a markdown file, a sixty-line spec, a two-sentence
   schedule. What's impressive is that each one made the next one cheaper. The
   first skill took an evening; the second took a third of that. The agent reused
   the anatomy; the routine reused the agent. **They weren't collecting artifacts;
   they were compounding them.**
5. Ask "how would you describe what you built?" one last time and file their
   answer in `learning/journal.md`. This entry is the one they'll want later.
6. **The commitment, and it's the practice for this session:** write four lines and
   commit them — one skill to add, one agent to refine, one routine to keep,
   change, or kill, and one thing they'll stop doing by hand. Thirty days from now
   their session log is the record of whether it happened. And the habit that keeps
   the other four honest: **close every session with `/bluerock:wrap-up` from now
   on.**
7. **Where it goes next**, offered once and without a pitch:
   - **Keep building.** The next thing to grow is their project's reach. MCP
     (Model Context Protocol) is the open standard that lets agents connect to the
     tools they already work in — Slack, their customer relationship management
     (CRM), their analytics. Each connector is a new set of hands for their
     agents, and each one is a new permission they grant: **the tools-line
     question, one level up.**
   - **Stay in the program.** Registered builders get the live sessions and the
     community.
   - **Notice what they now know.** The discipline they practiced at one-project
     scale — what ran, what did it touch, what is it allowed to do — is the
     question BlueRock answers at company scale. Session 7 left it hanging; at the
     scale of one project they already have the answer, because they built it: a
     tools line they can defend, a fallback that refuses to invent, a destination
     named in the spec, a manual fire before trust, and a wrap ritual that leaves a
     trail. At company scale that question doesn't have a habit-sized answer. **The
     builders who run agents are the ones who understand why agents need rails.**
     Say this once, plainly, and don't oversell it. They spent eight sessions
     earning the right to hear it.

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **The site page is the canonical version of this session's content.** It lives
  in `marketing-hub/workbench/app/learn/_data/session-run-your-system.tsx` and gets
  edited weekly; this skill does not. When the two disagree, the site is right.
- **This skill is deliberately shaped differently from its site page, and the
  decision is recorded rather than implied.** The page's capstone is *present one
  workflow live*; a skill cannot verify that a human presented to another human,
  so an in-session version of that page would either fake a checkpoint or block
  the path at 7-of-8. This skill instead **reads the real project and does the
  reflection**, keeps the presentation as a strongly-offered exercise, and reaches
  `complete` on the inventory, the gap, and the wrap-up — all inspectable. This is
  option 1 of the three in
  `09-product/beta-plan/bfb-sessions-3-8-in-session-scope.md` §2, which recommends
  it as the only version where `progress.json` can honestly reach complete.
  **If someone later decides the capstone must be presentation-gated, that's a
  product decision, not a copy fix** — it changes what "complete" means for the
  whole path.
- **Step 1's inventory reads real paths**, and they are the shipped ones:
  `.claude/skills/` (not `.claude/commands/`), `.claude/agents/`, `notes/`,
  `briefs/`, `my-work/`, and the three memory files at the project root. The
  seeded-versus-theirs split names `meeting-recap`, `capture`, and `research` as
  shipped skills, and the six shipped agents. If `hub-starter` changes what it
  seeds, this inventory mislabels the builder's own work as seeded — which is the
  one error in this session that would actually sting.
- **`/bluerock:wrap-up`'s behavior is quoted in step 5**, verified against the
  shipped skill: it refreshes the dashboard, writes a dated `session-log.md`
  entry, **shows what's about to be saved and commits only after the builder
  confirms**, and prints a continuation prompt. The confirm gate is the part
  builders are told about explicitly ("starting the ritual is not yet permission
  to commit"); if that gate is ever removed, this session and the site page both
  become wrong in a way that matters.
- **Session 7's practice is this session's input** (the three-sentence workflow
  statement). If it moves, step 2 needs its own way to source one.
- **The closing BlueRock beat is deliberately one paragraph, once, at the very
  end**, after the builder has finished. It is the site's "Beyond your project"
  Learn-more, ported at the same register. **Do not move it earlier or repeat
  it** — the whole path's credibility rests on teaching first and connecting the
  dots last.
- **OPEN, inherited from the site page:** the 2026-07-31 decision gives Session 8
  a dated **monthly build prompt** slot, and the mechanism (who authors the
  month's prompt, where it lives so it rotates without a release) is still
  undefined. This skill carries the keep-building items instead. When that
  mechanism lands, this close-out gains the dated slot.
