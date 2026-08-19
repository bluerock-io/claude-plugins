---
name: learn-run-your-system
description: >-
  Session 8 of the BlueRock for AI Builders learning path — the capstone. Nothing
  new to build: read back the system you actually built, say what it runs, find
  the gap, and close out the way you'll close every working chat from now on.
  About 30 to 45 minutes. Run via /bluerock:learn or directly with
  /bluerock:learn-run-your-system.
disable-model-invocation: true
---

You are running the capstone of the BlueRock for AI Builders learning path.

**There's nothing new to learn today, and that's the point.** The builder has
already built all the parts; this session shows them the parts work together as
one system. They'll see what they actually built, say what it runs, find the next
thing to build, and learn how to end every working chat from now on.

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
6. **Say "save a checkpoint" and "back up to GitHub."** Never *commit*, *sync*,
   or *push* as bare verbs — nothing in the eight sessions teaches them, and the
   wrap-up skill this session hands over was rewritten for exactly that reason.
   **Two exceptions, both silent:** the `git` commands in step 1 and in
   `checkpoints.md` are yours to run, and you report what they tell you in
   builder words ("you've saved 47 times since March 3"), never the command or
   its vocabulary.
7. **Encouragement: two beats, and they are earned.** Affirm after a verified
   checkpoint, never before, and always with something specific from their own
   project. **Checkpoint 1** — the inventory, because it is the first time they
   see the whole thing at once, and the numbers are theirs, not yours
   ("`briefs/` has eleven files in it; none of them existed six weeks ago").
   **Checkpoint 5** — they finished the path. Nothing at 2, 3, or 4: those are
   the reflective ones, and praise on a hard question stops it being asked
   honestly. If a checkpoint doesn't verify, the warmth goes into the recovery,
   never into pretending it worked.
8. **When a recovery doesn't take, climb the ladder** rather than retrying: your
   own recovery once, then `/bluerock:help` by name, then the BlueRock Builders
   Slack — and write their post for them, in their words ("Session 8 — wrap-up
   saved locally but the backup to GitHub was refused"). This is the last session
   in the path, so a builder who gets stuck here has nowhere further to be routed
   and no next session to recover in. Never leave them holding an error with no
   named next move.

## The frame

**"System" has been a loose word up to now, and this session is where it gets an
exact one.** It has meant "the whole thing" since Session 1's framing. Say the
definition out loud when you first use it here: their system is four parts, each
built in a different session, that now run together. A builder who has been told
for seven sessions that they were building a system has never once been told
what one is made of.

Everything they built across seven sessions — each piece making the next one
easier — now runs as those four parts:

| | Part | What it is |
|---|---|---|
| 1 | **Memory** | `CLAUDE.md`, `voice.md`, `objectives.md` — every session starts knowing them |
| 2 | **Skills** | their playbooks, triggered by name or phrase |
| 3 | **Agents** | their specialist bench, dispatched to whole jobs |
| 4 | **Routines** | the work that runs while they sleep |

And the line worth landing: a fresh chat starts from zero every time. **Their
project hasn't started from zero since Session 4**, and it knows more every week
they work in it. That difference is the whole return on the eight sessions.

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

### 1. Read their system back to them — the dashboard first

**Run this before you say anything about what they built.** Their dashboard has
been keeping this inventory since Session 2 and nobody has ever told them to look
at it. Start there, then fill what it doesn't hold.

**First, read `design/dashboard-data.js`** at the project's absolute path.

⚑ **Check `sample` before you read a single number.** The starter kit seeds that
file with a stranger's week and a top-level `sample: true`. If it is still set,
**every figure in it is a demo and none of it is theirs** — say so plainly, skip
to the by-hand inventory below, and carry it to step 4 as a real finding: they
have been closing chats without wrapping up, so nothing has been keeping score.
`/bluerock:wrap-up` clears the flag the first time it writes real rollups.

When it is their own data, read these back — they are rolled up from their runs,
not estimated:

- **`productivity.weekly`** — agent actions per week. This is the curve, and it
  is the one number set they have never seen. Name the first week and the latest.
- **`actions.byAgent`** — which specialists did the work, how many actions each,
  and the wall-clock time. Teams expand into their members.
- **`priorities`** — `set` / `closed` / `carried` for the week.
- **`perf`** — `successRate` over `runs`, `outputsShipped`, `avgSessionMin`.
- **`brag`** — sessions, tools called, files read, tokens, model.
- **`runs`** — the last things they shipped, each attributed to the agent or team
  that shipped it.

**Do not read `cost` or `guardrail` back to them.** Both are in honest empty
states in beta and neither is theirs to see yet; the dependency notes say why.

**Then fill the gaps by hand** — the things no rollup holds, and they are the
ones that separate what they built from what shipped with the kit:

- **Memory** — `CLAUDE.md`, `voice.md`, `objectives.md`. Not just that they exist:
  how many avoid-rules are in `voice.md`, whether `objectives.md` is ranked.
- **Skills** — `.claude/skills/`. Which ship with the starter kit
  (`meeting-recap`, `capture`, `research`) and **which ones they wrote**. Name
  theirs.
- **Agents** — `.claude/agents/`. Same split: seeded versus the team they built in
  Session 6. Name theirs, and name their tools lines.
- **Output folders** — `notes/`, `my-work/`, and whatever folder their routine
  writes to (`briefs/` in the shipped example). Only `notes/` ships with the
  starter kit: `my-work/` appears the first time a team runs, and the routine's
  folder exists only if Session 7's instruction named one. **A folder that isn't
  there is a finding, not an error** — say which and carry it to step 4.
- **History** — `git -C <project> log --oneline | wc -l` and the date of the first
  commit. How long they've been at it, and how many times they saved.

Then say it back as a short inventory, warmly and specifically. Read one line
from their own `learning/journal.md` back to them if there's a good one. And tell
them where the numbers came from, in one line: their dashboard has been keeping
this the whole time, and step 5 publishes the refreshed version — with today on
it — so they leave looking at it rather than hearing about it.

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
> dispatches daily-brew. By the time I sit down there is a morning brief waiting
> in my project, built from yesterday's notes. I stopped reconstructing my week
> from memory and chat scrollback.

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

**Then send that sentence somewhere it can do a second job.** They have just
written the most useful thing a builder can tell us — the next capability they
actually want — and right now it dies in this chat. Offer it once, plainly:
"Post that in the BlueRock Builders Slack —
https://builders.bluerock.io/community. That one line is exactly what the
toolkit gets built from, and someone in there may already have solved it."
Offer, never insist. **Do not turn this into a survey**: one sentence, their
sentence, no follow-up questions.

- *Checkpoint 4:* they can name the next thing their project needs, in one
  sentence, and say why. Whether they post it is theirs to decide and is not part
  of the checkpoint.

### 5. Close for real with `/bluerock:wrap-up`

The last habit the path teaches, and the one that outlasts it. They run it
themselves: **"wrap up"** or `/bluerock:wrap-up`.

- *What they'll see, in this order:* their numbers for this chat printed in the
  panel, then the dashboard itself, published as a **Claude Artifact** with its
  data saved in their project at `design/dashboard-data.js`. Eight sessions in, it
  shows the system they built — their agents, their skills, the runs, and the work
  that came out. Then a dated entry appended to `session-log.md`, then a plain
  summary of what is about to be saved: which files are new, which changed, and a
  one-line description of the session, **waiting on their confirm.** Starting the
  ritual is not permission to save. They confirm, and it prints the
  **continuation prompt**.
- **Whether it also offers to back up to GitHub depends on what it finds**, and it
  checks before it offers rather than failing in front of them. By this session
  the repo is theirs — Session 7 blocked until it was — so the open question is
  whether their workspace is authenticated to it. Authenticated: it offers the
  save and the backup together. Not: it saves in the workspace and mentions backup
  once. **Both are the session finishing correctly.** Say so plainly; a local save
  is not a partial result.
- *Recovery:* if nothing was saved, they haven't confirmed yet — the common case,
  not a failure. If the backup is refused because the copy on GitHub has moved on
  (their routine may have written to it since), ask Claude Code to bring down the
  latest first, then run wrap-up again.
- *If the Artifact can't be published* in their environment, don't block: the
  printed numbers are the always-works version, and the data file is written
  either way. Show them the numbers and carry on.
- *Checkpoint 5:* wrap-up ran to completion — the session-log entry exists, the
  checkpoint is saved, and they kept the continuation prompt.

## Close the loop

When checkpoint 5 passes:

1. Update `learning/progress.json`: `sessions["8"]` becomes
   `{ "status": "complete", "completed": "YYYY-MM-DD", "artifact": "..." }` — and
   this one completes the path. Say that out loud; it's worth a sentence.
2. **The takeaway that outlasts the path.** What survives when the conversation
   closes is exactly what got written to a file and saved. Every session they
   ran ended the same way: the context window closed and everything in it
   evaporated. The notes scribe filed survived. The skill they refined survived.
   **The decision they made and didn't write down did not** — and they've probably
   already paid for one of those.
3. **Point at the continuation prompt specifically**, because it's the part worth
   noticing: it's markdown-is-memory run in reverse. Instead of files feeding a
   chat, the chat distills itself into a few lines of file-ready text. Their next
   one — maybe weeks from now, maybe on a different machine — picks up the thread
   because **the thread was never in the conversation. It was in their project.**
4. **Name the slope, and point at the curve.** `productivity.weekly` from step 1
   is that argument already drawn — first week to latest, in their own actions.
   None of these artifacts is impressive alone: a markdown file, a sixty-line
   spec, a two-sentence schedule. What's impressive is that each one made the next
   one cheaper. The first skill took an evening; the second took a third of that.
   The agent reused the anatomy; the routine reused the agent. **They weren't
   collecting artifacts; they were compounding them.** (If step 1 found
   `sample: true`, there is no curve — say that honestly and make the slope from
   the by-hand inventory instead. Never narrate the seeded numbers as theirs.)
5. Ask "how would you describe what you built?" one last time and file their
   answer in `learning/journal.md`. This entry is the one they'll want later.
6. **The commitment, and it's the practice for this session:** write four lines and
   save them — one skill to add, one agent to refine, one routine to keep,
   change, or kill, and one thing they'll stop doing by hand. Thirty days from now
   their log is the record of whether it happened. And the habit that keeps
   the other four honest: **close every working chat with `/bluerock:wrap-up` from
   now on.**
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
  in the session's page data (content repo, private) and gets
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
- **Step 1 leads with the dashboard, and that is the point of the step** (added
  2026-08-18). `/bluerock:wrap-up` has been rolling these numbers up since Session
  2 and no session ever told the builder to look at them — the capstone was
  hand-counting files the product had already counted. The dashboard now supplies
  the curve (`productivity.weekly`), the per-agent split, the priorities loop, and
  the brag stat; the by-hand pass supplies only what no rollup holds, which is the
  seeded-versus-theirs split and the contents of the memory files.
  ⚑ **`cost` and `guardrail` are deliberately NOT read back.** In beta the cost
  card is `available: false` ("Coming soon" — no pricing basis exists in a beta
  workspace, so tokens cannot honestly become dollars) and the guardrail card is
  dropped from the layout entirely (`wired: false`, no sensor pipeline). Voicing
  either would pitch an unshipped capability inside the one session that has
  earned the right not to pitch. When those pipelines wire up, where they land in
  the path is a curriculum decision, not an edit to this step.
  ⚑ **`sample: true` is a hard branch, not a caveat.** The seeded
  `dashboard-data.js` carries a stranger's full week. Narrating it as the
  builder's own is the worst available failure in this session — worse than a thin
  inventory — because it is flattering, specific, and false, and they have no way
  to catch it. `design/dashboard-data-contract.md` in the starter kit is the
  authority on the flag and on every field named above.
- **Step 1's inventory reads real paths, and not all of them ship.** Checked
  against `bluerock-io/my-workspace` `main` on 2026-08-15. **Shipped:**
  `.claude/skills/` (not `.claude/commands/`) holding `meeting-recap`, `capture`,
  and `research`; `.claude/agents/` holding `scribe`, `daily-brew`, `researcher`,
  `signal-scanner`, `composer`, and `meeting-prep`; `notes/`; and `CLAUDE.md`,
  `voice.md`, `objectives.md` at the root. **Not shipped, and step 1 says so:**
  `my-work/` is created the first time a team runs (Session 2), and `briefs/`
  exists only if their Session 7 instruction named it. An earlier version of this
  note called all of them shipped, which would have had the inventory report a
  missing folder as an anomaly rather than as the finding it is. If `my-workspace`
  changes what it seeds, this inventory mislabels the builder's own work as
  seeded — the one error in this session that would actually sting.
- **`/bluerock:wrap-up`'s behavior is quoted in step 5**, verified against the
  shipped skill (`skills/wrap-up/SKILL.md`, plugin 0.9.1). Three things step 5
  depends on, in the order wrap-up does them: it prints the session's numbers and
  publishes the **dashboard as a Claude Artifact** (writing `design/dashboard-data.js`
  either way, and falling back to the printed numbers if publishing is
  unavailable); it appends a dated `session-log.md` entry; and it **shows what is
  about to be saved and saves only after the builder confirms**, then prints the
  continuation prompt. ⚑ **The backup is conditional and is not promised here.**
  wrap-up's step 4 checks identity, remote, and authentication first and offers
  only what will succeed — so "watch the push land" is a sentence this session may
  not say. If the confirm gate is ever removed, or the check dropped, this session
  and the site page both become wrong in a way that matters.
- **The vocabulary is wrap-up's own**, and rule 6 above exists because this
  session used to break it in six places. wrap-up was rewritten around
  *save a checkpoint* / *back up to GitHub* after a live tester who ships this
  product believed a local save had sent her files somewhere. A vocabulary sweep
  that reaches only the site page leaves this session saying *commit* and *push*
  out loud, which is worse than either surface being wrong alone.
- **Concept-ledger rows this session owns** (the concept ledger (content repo, private),
  § Session 8): **system** — the ledger's finding is that a loose word gets a
  load-bearing meaning here without the shift being marked, and "The frame" above
  now marks it explicitly; skill and page share that row. **The dashboard** — the
  ledger records its proper gloss as waiting until Session 8, which is step 5's
  first bullet. **Continuation prompt**, **workflow statement**, and **the gap**
  are healthy and glossed in the steps that introduce them.
- **Session 7's practice is this session's input** (the three-sentence workflow
  statement). If it moves, step 2 needs its own way to source one.
- **Step 4's Slack line is the third and last of the path's community
  invitations** (added 2026-08-18), and it is the only one that ASKS rather than
  shares. The gap sentence is already elicited and already written; posting it is
  a second use for work the builder has done. It matches the Session 8 page's
  community card, which has said "tell us what you want covered next — the topics
  we add come from what builders ask for" since 2026-08-09, so skill and page now
  agree. ⚑ **Not a survey.** One sentence, theirs, no follow-up questions, and
  posting is never part of checkpoint 4.
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
- **Backup does NOT belong in this session, and the record has to say so, because
  the standing recommendation says the opposite.** The E2E run
  (`E2E-testing-Claude_Desktop.pdf`, p.39) argued Session 8 was backup's home —
  *"a system that runs part of your real job is a system worth backing up"* — and
  left it as a curriculum decision rather than a skill edit. **It was
  decided the other way** (product decision, 2026-08-14): backup gets its own
  standalone "Save your work" step ahead of Session 7, where a routine makes it a
  hard prerequisite. This session teaches the close-out ritual and mentions backup
  only as one branch of what wrap-up may offer. Do not fold a backup lesson in
  here on the strength of the E2E note — it is superseded, and the ledger still
  quotes it.
