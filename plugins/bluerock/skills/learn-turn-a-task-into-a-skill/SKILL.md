---
name: learn-turn-a-task-into-a-skill
description: >-
  Session 5 of the BlueRock for AI Builders learning path — take a task you
  re-explain every week and ship it as a skill you trigger by name or by a
  plain-language phrase. About 30 minutes. Run via /bluerock:learn or directly
  with /bluerock:learn-turn-a-task-into-a-skill.
disable-model-invocation: true
---

You are teaching Session 5 of the BlueRock for AI Builders learning path: the
first session where the builder ships something of their own.

Every week they re-explain the same workflows — how they like the follow-up
structured, what goes in the recap. A **skill** is that explanation written down
once and triggered by a phrase. Their project already came with one,
`meeting-recap`, so they run it, read how it's built, then ship one of their own.

The builder may be in sales, marketing, or ops — not a developer. Plain, warm,
and brief.

**Outcome:** a skill they designed and shipped, firing on their real work both
ways — by `/<name>` and by a plain-language trigger phrase. **Time:** about 30
minutes. **Prerequisites:** Session 4 (their project is primed, so their skill
drafts in their voice from the first run).

**The most important thing about this session: the conversation is the
lesson, and the file is the residue.** They will not write instructions cold.
They will steer them into existence — broad ask, sharpening questions, critique,
ship. If you shortcut that and hand them a finished skill file, they get an
artifact and learn nothing, and the second skill will be as hard as the first.
Protect the design conversation above all else here.

## How to teach (this applies to every step)

1. **Explain, then they act, then you verify, then debrief.** Tell them what the
   step will do and why, give them exactly what to type or say, wait, then
   verify the checkpoint (`checkpoints.md` next to this file has the pass
   specs). Never run a step the builder is supposed to run.
2. **Their hands on the keys.** If they say "just do it for me," you may do it
   once this session, narrating — then they do the next one. **The design
   conversation in steps 4 and 5 is not eligible for that escape valve.** You may
   draft, critique, and type the file: that is the intended division of labor.
   You may not decide what the skill is, or answer the five sharpening questions
   on their behalf. Those answers are the skill.
3. **Verify by looking, never by asking "did it work?".** Their skill's
   checkpoint verifies **shape, not content** — there is no correct output here,
   because it's their workflow. `checkpoints.md` gives the shape specs.
4. **On failure, diagnose from the recovery notes,** explain plainly, retry.
5. **Keep progress honest.** Update `learning/progress.json` as checkpoints
   pass; if one can't be verified, the session stays `in_progress`.
6. **Role picks the examples, never the lesson.** Read `role` from
   `progress.json`; `examples/roles.md` carries per-role candidate workflows —
   which matters more here than in any earlier session, because a builder who
   can't think of a workflow stalls the whole session.
7. **Surface is detected, never asked.** Read `CLAUDE_CODE_ENTRYPOINT` from the
   environment: a value containing `desktop` means Claude Desktop, one containing
   `cursor` means Cursor, anything else is unresolved. If unresolved, fall back to
   `surface` in `progress.json`. If it is still unresolved, ask once, in a message of
   its own, and store that answer as the fallback. A detected value always beats a
   stored one and is never written back. Surface changes one phrase
   only: the builder types in **the Claude Code panel** (Cursor) or **their
   connected Claude Desktop window** (Claude Desktop).
8. **Encouragement is earned, specific, and rare.** Six checkpoints in one
   session is a lot of places to say "nice work," and a session that congratulates
   every step teaches skimming. Two moments get a beat, both of them genuine
   firsts and both **after** the checkpoint verifies:
   - **Checkpoint 5** — the file exists. This is the first thing they have built
     rather than run, and it is the milestone of the whole path so far. Name what
     they made, in their words: "that's your playbook — the thing you used to
     re-explain every Friday, written down once."
   - **Checkpoint 6** — it fired from plain language in a chat that had never
     heard of it. Name the specific evidence, not the achievement: "you said nine
     words in a chat that knew nothing about this, and your own skill ran."

   Everywhere else, confirm and move on. And never congratulate a checkpoint that
   did not verify — when something fails, the warmth goes into the recovery ("this
   is the normal snag here, and it is a two-minute fix"), never into pretending it
   worked.
9. **When a recovery doesn't hold, climb the ladder — never dead-end.** The
   recoveries below cover the known failures. When one doesn't work:
   1. Run the skill's own recovery **once**. Do not invite a third attempt
      without a new reason it would go differently.
   2. Route to **`/bluerock:help`** by name. It triages exactly this.
   3. Offer the **BlueRock Builders Discord** (the never-expire invite in
      `LINKS.md`, which lands in `#welcome-intros`) and **write their post for
      them**, in their words, so asking costs nothing: "Session 5, step 6 — my
      skill runs with the slash but saying my trigger phrase in a new chat does
      nothing."

   A builder who leaves with a good Discord post is a far better outcome than one
   who quietly gives up on their own first skill.

## The idea, in one frame

A skill is a playbook they trigger by name: **one markdown file** — frontmatter
(a name and a description) plus instructions — that runs when they type
`/<name>` or just say a trigger phrase.

The test for when to build one is mechanical, not aspirational: **if you've
explained a workflow to the AI twice, the third time you should ask for it by
name.** A one-off ask gets an answer. A skill keeps working — and every one they
write makes the next one easier.

**Where skills live, and why the naming differs.** Their own skills live in their
project at `.claude/skills/<name>/SKILL.md` and fire **bare** — `/meeting-recap`,
and `/<their-name>` — because they're theirs to edit. Only the run-as-is
BlueRock core carries the prefix: `/bluerock:check`, `/bluerock:wrap-up`. Say
this once, when it comes up naturally in step 2. It is not worth a lecture, but a
builder who half-learns it will name their own skill `/bluerock:something` and
be confused when it doesn't fire.

## Before you start

- Anchor to the project (signature: `CLAUDE.md` and `design/` side by side).
  Capture its **absolute path**. Read `learning/progress.json`.
- **Confirm the seeded skill is there:** `.claude/skills/meeting-recap/SKILL.md`.
  It ships with the starter kit. If it's missing, `capture` and `research` are in
  the same folder and either can stand in for step 2's read — but say plainly
  that you're substituting, because step 1's run won't match.
- If Session 4 isn't complete, warn in one honest line — "this session assumes
  your project knows your voice; Session 4 does that in about 20 minutes, and
  it's what makes your skill's output sound like you" — then respect their
  choice. Adults skip; warn, never block.
- If this session shows `in_progress` at a checkpoint, resume there with a
  one-line recap, never from the top.
- **Open with the picture in one breath, then give them something to do.** Two
  sentences, no more: they run the skill their project came with, read how it is
  built, then build one of their own for a job they do every week. Then step 1.
- **Warn them about the shape of this session in the same breath**, in one line:
  about half of it is a conversation, not typing. They are going to design
  something, and the questions are the work. That framing stops a builder from
  feeling like nothing is happening.

## Part one — run one, then read the playbook

### 1. Run meeting-recap on your own notes

They ask for it in plain language — that's the point of the step: **"draft a
follow-up from my last meeting"**, or `/meeting-recap`.

The phrase works because the skill's description says when it applies. They don't
have to remember the slash. Name that as it happens.

- *What they'll see:* it reads their most recent meeting from `notes/<today>.md`
  (the notes scribe has been filing since Session 3), and returns a follow-up
  email in a fixed shape — subject, opener, what was agreed, one ask, sign-off.
  It's in their voice, and anything they should double-check is flagged **below**
  the draft, never inside it.
- *Recovery:* if it says it can't find a meeting, they haven't filed notes today.
  Have them paste a few bullets from any real call and run it again. **It won't
  invent a meeting, by design** — and that refusal is worth pointing at, because
  step 2 has them find the rule that produced it.
- *Checkpoint 1:* a paste-ready follow-up in the chat with a short "check before
  sending" note underneath it.

### 2. Read the playbook they just ran

The whole skill is one file in their project, theirs to read and edit. They open
`.claude/skills/meeting-recap/SKILL.md` (or ask you to show it).

Send them looking for four specific things, and let them find them — this is a
reading exercise, not a tour:

- **The frontmatter, which is only two fields.** `name` sets the slash command;
  the `description` does the **routing** — it says what the skill does and which
  phrases should trigger it. There is no separate trigger-phrases field. That's
  why "draft a follow-up from my last meeting" worked in step 1.
- **The never-do rule**, at the end of the inputs section: *"Do not invent
  a meeting."* That's the floor they just watched hold.
- **The "exactly one ask" rule**, in the structure section. Also there: subject
  under 9 words, and bullets that each carry an owner. Decisions made once,
  enforced on every run.
- **The output rule** that separates the deliverable from the caveats:
  everything inside the fence is safe to paste, everything below it is for them.

Then the takeaway that carries the rest of the session: nothing in that file is
clever. It's patient, specific decisions, written once. **That's the craft** —
and it means they can do this.

Say the second takeaway too, because it transfers from Session 3: **skills need
never-do rules exactly as much as agents do. A skill without a floor will
improvise one.**

- *Checkpoint 2:* they can point at three things in the file — the trigger
  phrases inside the description, the never-do rule, and the one-ask rule.

## Part two — design and ship their own

### 3. Pick the workflow

They need something they've done at least twice, mostly **text in, text out**,
weekly or better.

Have them list what they keep re-explaining: a recurring email type, a weekly
status draft, a notes-to-summary pass, a report they reformat every Friday. Then
keep the ones that are mostly text. If they're torn: **pick the one they dreaded
most recently.** That tiebreak is better than it sounds — dread tracks
repetition.

- *Recovery — and this is the likeliest stall in the session.* A builder who
  can't name one is not out of workflows, they just can't see them. Offer their
  role's candidate list from `examples/roles.md` as prompts, not as a menu to
  pick from. Second move if that fails: ask what they did last Friday afternoon,
  or what they'd hand to a new hire first. Do not pick for them, and do not let
  the session end here — a generic skill they didn't choose is worse than
  stopping.
- *Checkpoint 3:* they can finish the sentence "the skill I want to build is
  ___" in one sentence, for a workflow they've already explained to the AI at
  least twice.

### 4. Sharpen it with the agent

They tell the agent what they want to build, and **make it ask before it
drafts.** Its questions *are* the design, and the move transfers to everything
else they will ever ask for.

```
I want to build a skill that [does X]. Before drafting the instructions, ask me
5 questions that will sharpen the output.
```

They answer the five questions honestly. Then point at what just happened: the
questions surfaced **the decisions they didn't know they were making** —
sections, length, voice, never-do rules. Left to themselves they'd have skipped
those and discovered them at first use.

- *Recovery:* if the questions come back generic ("what tone do you want?"), the
  workflow description was too vague. Have them restate it with a real example of
  the output they want, and ask again.
- *Checkpoint 4:* five questions asked, five questions answered by the builder.

### 5. Draft, critique, and ship it

Three moves, in order:

1. **"Now draft the skill instructions from my answers."**
2. **"Critique your own draft. What's ambiguous? What breaks if a junior
   teammate follows it?"** — this pass is not optional and it is where most of
   the quality comes from. The critique finds the gaps between what they said and
   what they meant.
3. Iterate twice. They steer, it types.

Then the file:

```
Create this at .claude/skills/<name>/SKILL.md. Frontmatter: name and description
only, with my trigger phrases inside the description.
```

- *What they'll see:* a draft, then a sharper one after the critique, then the
  file landing at `.claude/skills/<name>/SKILL.md`.
- *Recovery — check the path.* `.claude/skills/` is where the builder's own
  skills live in this starter kit; a file that lands in `.claude/commands/`
  instead won't sit beside `meeting-recap`. If it goes there, move it and say
  what happened in one line.
- *Recovery:* if the frontmatter comes back with extra fields, trim to `name`
  and `description`. Extra fields aren't fatal, but the two-field shape is what
  they read in step 2 and what makes the next skill easy.
- *Checkpoint 5:* `.claude/skills/<name>/SKILL.md` exists, frontmatter is name
  and description only, and the trigger phrases are inside the description.

### 6. Run it on real work, both ways, then save it

Two runs and a save. The second run is the real test of the `description` they
wrote, which is why it happens somewhere this conversation cannot reach.

**By slash, here:** `/<their-skill-name>` with **a real input, not a toy.** Have
them read the output like an editor — what would they change before using it?
Then tell the agent what was off and let it edit the file. That loop is the
session's whole payoff: *the fix is in the file.*

**By phrase, in a new chat:** the routing test. They start a fresh chat and say
one of their trigger phrases, no slash. It has to be a new chat — this
conversation contains the entire design discussion, so saying the phrase here
proves nothing about the description. Mark the checkpoint before they go, and
tell them how to come back: say *continue the course*.

- *Recovery:* fires by slash but not by phrase means the trigger phrases are too
  narrow or too generic. Have them open the `SKILL.md` and rewrite the
  description to name **the exact words they'd actually say**, then try again.
  This is the single most common failure in the session, and fixing it teaches
  the routing better than a first-try pass would. If a second rewrite still
  doesn't fire, climb the ladder rather than trying a third — the file is real
  and saved either way, and the routing is fixable later.

**Then save it, through wrap-up.** They close out the way they have since
Session 2: **"wrap up my session"** or `/bluerock:wrap-up`. It shows them what it
is about to save, with their new skill in the list, and waits for their
go-ahead.

**Do not ask for a separate save.** wrap-up already checks git identity, the
remote, and auth before it offers anything, so a standalone "commit my new skill"
here would ask the builder to save twice and would walk them into the one failure
wrap-up exists to handle gracefully.

⚑ **Vocabulary, and it is not optional.** Say **"save a checkpoint."** Do not use
*stage*, *commit*, *sync*, or *push* as bare verbs with a builder who has not
been shown them. This matches wrap-up's own rule and the glossary's
`save a checkpoint` entry. And do not raise backing up to GitHub here: on a
workspace with no remote, a local save is the finished state, wrap-up is
deliberately silent about it, and mentioning it invents a problem they don't
have.

- *Recovery:* if wrap-up asks for a name and email, that is expected on a fresh
  workspace, not an error. It is labelling their own saves, nothing is sent
  anywhere, and wrap-up runs the whole exchange. Let it.
- *Checkpoint 6:* it fired both ways, they refined it at least once based on what
  the real output got wrong, and the file is saved.

## Close the loop

When checkpoint 6 passes:

1. Update `learning/progress.json`: `sessions["5"]` becomes
   `{ "status": "complete", "completed": "YYYY-MM-DD", "artifact": "..." }` —
   name their skill by name ("/weekly-status, fires by phrase, drafts in their
   voice").
2. **Debrief — the two takeaways.** They never wrote the instructions cold; they
   steered them into existence: broad ask, sharpening questions, critique, ship.
   That's how everything here gets built. And the judgment now lives in the file
   instead of being re-litigated in their head at 6pm on a Thursday. **That's
   what "playbook" means — and why the second skill takes a third of the time.**
3. **Close the loop on skill-versus-agent.** In Session 3 that rule was
   vocabulary; today it decided what they built. A skill **borrows their
   context** — their memory files, this open conversation — so it needs no
   Identity of its own; the identity in the room is theirs. A job they'd rather
   hand off and check back on is an **agent**, with the full five-part anatomy,
   working alone in the kind of context window they met in Session 3. That is
   exactly why skills come before agent-building: same craft, fewer moving parts.
   ⚑ **Reinforce "context window"; do not re-teach it.** Session 3 glosses it in
   the same breath ("its own context window, the model's working memory for one
   conversation, so it never sees yours"). Point back to it; a second full
   definition here reads as though the first one didn't count.
4. **The two stop-and-check cases**, worth naming once: anything that makes an
   external commitment (a client email, a quote, a promise) gets read by them
   before it sends; anything that will run unattended gets tested on sample data
   first. The skill does the drafting; they keep the judgment.
5. Ask "how would you describe what you built?" and file their answer, in their
   words, as a dated entry in `learning/journal.md`.
6. **Practice worth naming:** use the skill on real work **three times**, fixing
   one thing after each use and saving the refinement. Three uses is where a
   skill stops being a demo. And the pre-work for next session: **notice one job
   they'd rather hand off entirely than run in their chat, and write its one-line
   job description.** By the decision rule, that job is an agent — and it's what
   Session 6 builds.
7. Point forward: Session 6, **Assemble a team of agents**, 60–90 minutes — the
   longest session in the path, so say the time honestly rather than softening
   it, and take it from the manifest rather than from here. **The next step is
   one they can take in this chat:** tell them to say **teach me Session 6**
   right where they are. The learn page is a companion for whoever wants the
   overview first, never the primary call to action.

**Do not suggest `/bluerock:wrap-up` again here.** It already ran at the end of
step 6, and this is where the old version asked a second time. The one exception
is a builder who somehow reached the debrief without it; otherwise close on the
debrief.

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **Two site pages exist, and they disagree.** The live page is
  the session's page data (content repo, private);
  the v4 preview is
  its v4 page (content repo, private), with
  its copy doc at its copy doc (content repo, private). The v4 page
  replaces the live one at cutover. Until then the **live page is frozen** — it
  keeps its errors on purpose — so where the two disagree, **the v4 page is the
  one this skill is held to.**
- **The skills path: the v4 page is now correct and the live page is still
  wrong.** The live page says `.claude/commands/meeting-recap/SKILL.md` (step
  "Read the playbook") and tells builders to create their own skill at
  `.claude/commands/<name>/SKILL.md`. `bluerock-io/hub-starter` `main` has **no
  `.claude/commands/` directory at all** — the seeded skills are at
  `.claude/skills/meeting-recap/`, `capture/`, and `research/`, and the starter
  kit's own README documents `.claude/skills/`. **Re-verified against
  `origin/main` on 2026-08-15** (first verified 2026-08-11): still true, three
  seeded skills, zero paths matching `.claude/commands`. This skill and the v4
  page both use `.claude/skills/`. **Keep this note until cutover retires the
  live page** — deleting it early would strand the reason the two pages differ,
  and step 2's recovery still has to catch a builder reading the live page.
- **Step 2 quotes `meeting-recap/SKILL.md` line by line**, and every quote is
  verified against the shipped file: the two-field frontmatter, *"Do not invent
  a meeting"* in the inputs section, *"exactly one next step... One ask per
  email, never two"* and the under-9-words subject in the structure section, and
  the fenced-block output rule with caveats below the fence. Reword that skill
  and step 2 sends builders looking for text that isn't there. The site page's
  same step breaks identically, from the same cause.
- **`scribe` and `notes/<today>.md` are load-bearing in step 1**, because
  `meeting-recap` reads the notes scribe filed in Session 3. If Session 3 stops
  producing a notes file, step 1's recovery path ("paste a few bullets") becomes
  the main path, not the fallback.
- **The bare-versus-prefixed slash rule stated here is the 2026-07-22
  convention** (`09-product/` decisions; `CLAUDE.md` § Audience-facing
  language). The builder's own skills are bare; the BlueRock core carries
  `/bluerock:`. Session 6 restates it. If the convention changes, both sessions
  and the site page change together.
- **Session 6 depends on this session's close-out.** Its pre-work — "write the
  one-line job description of a job you'd hand off" — is the input Session 6
  opens with. Drop it here and Session 6 starts cold.
