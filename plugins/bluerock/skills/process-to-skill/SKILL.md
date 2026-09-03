---
name: process-to-skill
description: >-
  Process to Skill — walk through a process that only lives in your head, one
  question at a time, and walk away with two things: a working skill in your own
  project that runs it, and a printable runbook someone else could follow. Use when
  I say "turn my process into a skill", "make a skill for how I do <X>", "I do this
  every week by hand", "document my process", "write the runbook for <X>", "nobody
  else can do this when I'm out", "I'm the only one who knows how to do <X>", or
  describe a recurring job I keep re-explaining. Interview, then generates the skill
  into .claude/skills/ and the runbook into my-work/process-to-skill/. Runs
  understudy to cold-test the file before I do.
---

Interview the builder about a process that currently exists only in their head, then give
them back **two things that work**: a skill in their own project that runs it, and a
runbook someone else could follow. This is the odd one in the set — the other use cases
point agents at the outside world, and this one points at the builder. Everything it needs
is in their head, which is exactly the problem it solves.

**What it replaces:** the process being undocumented and unshareable — re-derived from
memory every run, explained again to whoever covers, and unavailable the week they're out.

**Time saved:** [PLACEHOLDER — DO NOT MERGE: this card's baseline is one timed manual run
of the builder's *process*, not of skill authoring (decision 2026-09-03, E6-26). Fill with
a named example and its provenance, e.g. "one builder's weekly pipeline hygiene pass: 40
minutes by hand, timed once; the skill runs it in 4." Never a bare "saves an hour", and
never a cross-builder average — this figure is per-process by construction.]

## First — anchor to the project

The skill file lands in the builder's own project, and so does the runbook, so the anchor
is not optional here — it is where the deliverable goes. Two generations exist: the project
ships inside the workspace image (usually the folder `my-workspace`); projects made before
2026-08 were cloned and carry whatever name the builder chose. **Assume neither — identify
it by its signature.** In an SSH/cloud container the chat may start in the project itself
or in the **home folder** with the project one level down — both are normal. Run `ls`; see
`CLAUDE.md` and `design/` side by side? You're in the project. If not, find it:
`ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`, else
`find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` in, capture the **absolute
path** with `pwd`, and use that full path throughout. Can't find it? Ask the builder which
folder their project is in.

## Before the questions — read what the builder already has

Check, without asking:

- `objectives.md` and `voice.md` at the project root. These sharpen the run — the skill you
  generate should draft in their voice and rank by what they care about — and they never
  gate it.
- **`.claude/skills/`** — the skills they already have. Two reasons, and both matter: a
  name collision must be caught before you write anything, and a builder who already has
  three skills gets a different framing than one who has none.
- A prior run's folder under `my-work/process-to-skill/`, if one exists. A returning
  builder is usually here for a *second* process, not a redo — say which one you found and
  ask, rather than assuming either.

If `objectives.md` / `voice.md` are placeholder templates or absent, say so once, plainly,
and keep moving: *"Your `voice.md` is still the placeholder, so I'll write this in neutral
language and you can sharpen it later — running `/bluerock:onboard` would tune future
runs."* Never make setup homework the price of the deliverable.

## The interview — one question at a time, in their words

**This is the run.** There is no scan stage, no research, nothing to wait for: the whole
input is what the builder tells you, so the quality of the interview is the quality of the
skill. Ask one thing, wait, listen, then ask the next. Never stack questions and never
explain the whole flow up front.

**Skip what they already gave you.** If the opening request already named the process
("turn my Monday pipeline review into a skill"), say what you're taking as given and pick
up at the first genuinely missing step.

**Which prompt shape for which step:** use the question picker (`AskUserQuestion`) only at
step 2, where the answer really is one of a few shapes. Everywhere else the answer is free
text in the builder's own words and a picker is the wrong instrument — ask in the message
and let them type. Where the picker isn't available in this client, ask in the message.

1. **The process, in one line.** "What's the job? One line is enough — the thing you do
   over and over that nobody else does." If they give you three, ask which one they did
   most recently, and park the others by name for a later run.

2. **What starts it.** "What kicks it off?" (options: it's on a schedule — a day or a time ·
   something arrives — a request, an email, a file · something changes and I notice · I do
   it before a recurring meeting). Then one follow-up in their words: *when*, exactly.
   "Monday" and "Monday before the 9am forecast call" produce different skills.

3. **The steps — let them talk first.** "Walk me through it, start to finish, the way you'd
   tell a new hire. Don't organise it — I'll do that." Let them run. Then **read it back as
   a numbered list** and hand it to them to fix: *"Here's what I heard. Correct anything
   that's wrong, and tell me what I've missed between any two steps."*

   The read-back is the technique, not a formality. A process someone has done two hundred
   times is compressed in their head, and the steps they skip in the telling are the ones
   they've stopped noticing they do. Probe only where the list has an actual gap — "what
   happens between 3 and 4?" — never with a generic "anything else?".

4. **The decision points.** "Where do you have to *decide* something? Any place you'd say
   'it depends'." Then, for each one: **what does it depend on?** Push once, gently, for a
   rule they'd stand behind — *"if it's more than 30 days past close"* is a rule;
   *"if it looks off"* is not. If they genuinely can't reduce it to a rule, that's fine and
   it's information: the skill will surface the call and hand it back to them rather than
   pretending to make it. Write it down that way.

5. **What done looks like.** "When it's finished, what exists that didn't before, and who
   gets it?" You want the artifact and its destination. If the answer ends in *send*,
   *post*, *update the CRM*, or anything else that reaches the outside world, note it now
   and read the scope line below before you go further — it changes what you generate.

6. **The edge cases.** "What goes wrong, or what's the exception you handle every time
   without thinking about it?" Every real process has one. If they say "none", ask the
   version that actually gets an answer: *"when was the last time this took longer than it
   should have, and why?"*

7. **One or two real examples.** "Paste me one real one — what went in, what came out. Two
   is better than one if you have them handy." **This is required, not optional**, and it
   is worth saying why in one line: the examples are what the skill copies the shape from,
   and they are what the understudy tests the file against. Without them you are writing
   from a description, and a description of an output is not the output. If they truly
   can't paste one, say plainly that the skill will be shaped from the description alone
   and will need a correction pass on its first real run.

8. **Who else runs it.** "If you were out for two weeks, who'd have to pick this up?" Their
   answer becomes the runbook's owner and cover lines, and it usually surfaces one more
   edge case ("well, they wouldn't know about the...") — which is the point of asking.

9. **Confirm before we build.** Play back the one-liner, the trigger, the numbered steps,
   the decision rules, done, the edge cases, and the owner as a short list, then: "Good to
   go, or anything to fix?" **Carry all of it forward verbatim from here.** These are the
   builder's own words about their own job, and paraphrasing is how a runbook ends up
   describing a process nobody runs.

### The scope line — read it when step 5 or step 8 crosses it

If the process ends in an action on the outside world, **the skill you generate stops one
step short of it, deliberately, and you say so at the time rather than at the end**:

> *"Your step 6 sends this to the regional leads. The skill will draft it and stop there —
> it won't send. Two reasons: anything that goes outward gets your eyes first, and a skill
> that can send is a skill that can send the wrong thing at 6am. You'll paste and send, and
> that stays a ten-second job."*

Same for anything that updates a system of record. The skill drafts the update and shows
it; the builder applies it. This is not a v1 limitation to apologise for — it is the line,
and a builder who understands it once will design their next skill around it.

## Name it — theirs, and bare

10. **Ask what they want to call it**, and give them the shape rather than a menu: short,
    lowercase, hyphens, the words they'd actually say. `/weekly-pipeline-review`,
    `/renewal-check`, `/board-numbers`. Offer one suggestion from their one-liner if
    they'd rather not think about it.

    **Say the naming rule once, in a line, because a builder who half-learns it names their
    own skill with a prefix and is then confused when it doesn't fire:** their own skills
    fire bare — `/<their-name>` — because they're theirs to edit. Only the run-as-is
    BlueRock core carries `/bluerock:`.

11. **Check for a collision** against the `.claude/skills/` listing you already have. If the
    name is taken, say which one and offer a different name or an explicit replace — and
    **never overwrite an existing skill without the builder saying so in the affirmative**.
    A skill they wrote in Session 5 is not yours to clobber.

## Set up the run

12. **Make the working folder:** `my-work/process-to-skill/<YYYY-MM-DD>-<slug>/`, where the
    slug is the skill's name. Dated on purpose — runs accumulate and are never overwritten;
    a process that changes in six months gets a second run beside the first, not on top of
    it. `my-work/` is builder-owned.
13. **Write `process.md`** into the working folder: the confirmed interview from step 9, in
    the builder's words, plus which project files were real enough to read. This is the
    record of what the skill was built from, and the seed a later run pre-fills from.
14. **Write the examples** into the working folder as `example-1.md` (and `example-2.md`),
    exactly as pasted. The understudy reads these; nothing else it reads is allowed to
    contain the interview.

## Generate the skill — you, in this conversation

15. **Write `.claude/skills/<name>/SKILL.md`** in the builder's project. Not a subagent's
    job: you are the only one who heard the interview, and a writer agent that didn't would
    be inventing, not drafting.

    **Frontmatter is two fields, `name` and `description`, and nothing else** — that's the
    shape their seeded skills use and the shape Session 5 teaches. The trigger phrases live
    **inside the description**, in the words the builder would actually say, taken from how
    they described the job in step 1. There is no separate trigger field.

    **The body carries, in this order:** what the skill does in one line · what it needs
    before it starts (the inputs from step 3, each with where it comes from) · the numbered
    steps · the decision rules from step 4, stated as rules · what done looks like from
    step 5 · the edge cases from step 6, each with what to do · and a **never-do section**.

    **Every generated skill gets never-do rules — this is not optional.** A skill without a
    floor will improvise one. Three of them are constant and go into every file you write,
    worded for their process:
    - never send, post, or submit anything — draft it and stop;
    - never write outside this project;
    - never invent an input that isn't there — say what's missing and stop.

    Then add the ones that came out of the interview: the thing they said should never
    happen, the exception that must always be checked, the phrase they'd never use.

16. **Show them the file before you go further**, in the chat, and say in one line what
    they're looking at: the decisions they've been making from memory, written down once.

## Cold-run it — the stand-in test

17. **Dispatch `understudy`**, one agent, with the **absolute path** of the skill file and
    of the working folder in the dispatch prompt itself (a subagent starts wherever the
    session started; the path you pass is the handoff). It reads the skill file and the
    examples — **and nothing else in the folder** — walks the file as written, and writes
    `cold-run.md`: where it stopped, what it had to guess, what it couldn't find, the
    decisions with no rule, the unstated exceptions, the guardrail findings, and what held.

    **Frame the wait honestly and briefly** — it's a minute, not a coffee break: *"I'm
    handing this to a stand-in who wasn't part of our conversation. Whatever they have to
    guess at is what your colleague would have to guess at."*

    The point is the contamination: you sat through the interview, so you will read your own
    draft as complete because you remember what they meant. The understudy remembers
    nothing, which is the only honest read available and the literal form of the problem
    this use case names.

18. **Work the findings with the builder, not around them.** Show the gaps as a short list
    in the builder's terms, and take them in order. Most resolve in a sentence they can
    give you off the top of their head, and that sentence goes into the file. Two rules:
    - **You may not answer these for them.** A gap the understudy found is a decision the
      builder makes automatically and has never written down; you supplying it invents
      their process. Ask, then write what they say.
    - **A gap they can't close stays open, visibly.** It goes into the skill as a step that
      surfaces the call and hands it back, and into the runbook's decision lane as an
      unwritten rule. An honest open question beats a rule nobody agreed to.

    **Guardrail findings are a scope conversation, not a bug fix.** If the understudy flags a
    step that would send, post, update a live record, or write outside the project, take it
    back to the builder with the scope line from above and change the file so it drafts and
    stops. Nothing that touches a live system ships in a generated skill.

19. **Patch the skill file**, then say in one line what changed and why — the builder should
    see that the cold read earned its place.

## Write the runbook

20. **Write `runbook.md`** into the working folder from the patched skill plus `process.md`:
    the process name, the owner and the cover, what starts it, the numbered steps with their
    inputs, the decision points with their rules, the edge cases with what to do, what done
    looks like, and how to run it (`/<name>`). Plus two short sections that are the honest
    part: **what the skill does and what you still do**, and **what the stand-in couldn't
    work out** (the findings that are closed, and any that stayed open).

## Publish the artifact — you, not the agent

21. Read `runbook.md` and **publish it as a Claude Artifact** yourself, in this
    conversation, following the design contract below. The agent writes markdown only; the
    finished, shareable view is yours to render. If artifact publishing isn't available in
    my environment, don't block — the markdown is saved; say so and give the path.

### The artifact — design contract (follow it exactly)

**The artifact is a tool the builder operates while doing the process, not a report they
scroll** (product decision, 2026-08-31). This one is also the thing they hand to whoever
covers for them, so it prints, and the printed page has to work with nobody to ask.

**Not tabs.** One process is one entity, and a runbook read out of order is not a runbook.
The form is a **spine**: every step visible in sequence, scannable by lane color before it
is read, with click-to-focus on a single step and lane filters for the two views that get
used under pressure. Interactivity is navigation, never chrome. **No checkboxes** — a
checkbox that saves nothing is a dead control, and this page cannot save.

A single self-contained HTML page. **CSP rules: exactly one external request, the Google
Fonts stylesheet below. All CSS in one `<style>` block, all JS inline (one small script for
focus and filters), no CDN scripts, no remote images.** Print-friendly: under `@media print`
the filter strip hides, every step renders expanded in sequence, and the focus state is
ignored.

**Fonts** — one Google Fonts link, every face with a real fallback: `DM Sans` (display +
body; fallback `system-ui, -apple-system, sans-serif`), `Source Serif 4` (the step actions,
the decision rules; fallback `Georgia, serif`), `JetBrains Mono` (step numbers, labels,
meta, chips, the command; fallback `ui-monospace, Menlo, monospace`).

**Theme — ship both, token-structured.** Bare `:root` carries the complete light palette;
`@media (prefers-color-scheme: dark)` guarded as `:root:not([data-theme="light"])`
redefines only the tokens; `:root[data-theme="dark"]` duplicates them. Every component rule
uses `var()` — no literal color outside the three token blocks. `body` background is
`var(--paper)`. **The token table is the one in `skills/competitive-intel/SKILL.md` § the
artifact, unchanged** — same palette, same names, so the Phase 1 tools read as one family.
The lane meanings here are what differ:

| Lane | Token | Means |
|---|---|---|
| Step | `neutral` | Do this. The spine itself. |
| Input | `accent` | What you need in hand before that step. |
| Decision | `mine` | A judgment call, with its rule. Amber because it's where a stand-in stops. |
| Edge case | `kill` | The exception, and what to do about it. |
| Done | `bullet` | What exists at the end, and who gets it. |

**Structure** (max width 1000px):

1. **Sticky masthead** — the process name as the uppercase display title, then a mono meta
   line (`<date> · OWNER: <name> · COVER: <name> · run N`), then the **filter strip**:
   `All steps` · `Decisions only` · `Edge cases only`. Buttons with `aria-pressed`, 3px
   accent underline on the active one; filtering toggles the `hidden` attribute on step
   cards and sub-cards, never `style.display`.
2. **The header block** — a bordered card with a dark bar header (`background: var(--ink)`,
   `color: var(--paper)`) and labeled grid rows (`128px + 1fr`; mono uppercase labels, serif
   values): **RUN IT** (the command, in mono, as literal text — never a button, because it
   cannot run anything from here), **STARTS WHEN**, **DONE WHEN**, **OWNER**, **COVER**.
3. **Legend row** naming the five lanes with color dots, in the order above.
4. **The step spine** — numbered step cards, each with a mono number and a 4px
   neutral-colored left stripe: the action in serif as the bold lead, then, only where they
   exist, three sub-blocks in fixed order — **inputs** (accent chips, each naming where it
   comes from), **decision** (a mine-colored sub-card: the call, then its rule in serif
   italic, or the honest line that the rule is unwritten and the runner should ask), and
   **edge case** (a kill-colored sub-card: the exception, then what to do). Clicking a step
   focuses it: the others collapse to their number and title. Clicking again restores.
5. **Decision points** — the `Decisions only` view: every decision from the spine in one
   place, each with its step number, its rule, and an explicit `RULE NOT WRITTEN — ask
   <owner>` marker where it stayed open. Never hide an open one.
6. **Edge cases** — the `Edge cases only` view, same shape.
7. **What the skill does, and what you still do** — two columns, bullet-colored and
   ink-colored: the drafting the skill handles, and the judgment, the sending, and the
   approvals that stay with a person. **The line that goes here verbatim: the skill drafts;
   nothing goes out, updates a record, or leaves this project without you.**
8. **What the stand-in couldn't work out** — an accent-soft callout carrying the
   understudy's findings, each marked closed (with the answer that closed it) or still open.
   On a clean cold run, one honest line saying so. **This section is never omitted** — it is
   the evidence the runbook is followable, and a runbook with nothing to declare should say
   that out loud.
9. **Footer** — the path of the skill file and the path of this runbook, the line
   **`Your process, written down once — edit the skill file when it changes`**, and
   `Built with BlueRock · Process to Skill · understudy`.

**The scan test:** the person covering for the builder is holding the printed page, the
process is in front of them, and the builder is unreachable. The lane colors, the step
spine, and the decision rules have to carry it before a single sentence is read.

## The first real run — this is the payoff

22. **Have them run their own skill, in this chat, on real material.** `/<their-name>`, or
    one of the trigger phrases. Use the second example if they gave you one, or something
    live from today — not a toy.

    This is the aha and it belongs to them, so hand it over rather than performing it:
    *"Type `/<name>`. That's a tool that didn't exist when we started this conversation, and
    it's yours."*

23. **Read the output together like an editor.** What would they change before using it?
    Then tell them the loop that makes this last, and let them do it once now: **the fix
    goes in the file.** They say what was off, you edit `.claude/skills/<name>/SKILL.md`,
    they run it again. A skill that gets corrected twice in its first week is a skill they
    will still be using in six months.

    *Recovery — it fired by slash but the output is wrong in shape:* the steps are right and
    the example wasn't strong enough. Ask for one more real example, and fix the file
    against it rather than adding instructions in the abstract.

    *Recovery — nothing fires:* check the file landed at `.claude/skills/<name>/SKILL.md` and
    not `.claude/commands/`, and that the frontmatter is exactly `name` and `description`.
    Those two are the whole of the common failure.

## Finish

24. The **runbook artifact** is the shareable half and **the skill file is the working
    half** — say both, and say where each lives. `process.md` beside the runbook is what the
    next run pre-fills from, and `cold-run.md` is the record of what the stand-in couldn't
    work out.
25. **Report:** the skill's command, the two paths, the one line that matters (the sharpest
    thing the understudy found, or the decision rule they'd never written down before
    today), and the artifact (or the fallback note). Don't reprint the runbook.
26. **Offer the depth, after the run — never before it.** One beat, two doors, then stop:
    *"Want to see how this works, so the next one is yours end to end? The turn-a-task-
    into-a-skill session builds one with you from scratch — say 'teach me Session 5'. And
    when this one has run a few times and you trust it, putting an agent on a schedule is
    the session that makes it run without you starting it."*

    **Session 7 is named as a next step, not offered as a feature.** Scheduling this process
    is not in this skill, and a builder who hears otherwise will go looking for a button.

## Honesty rules this skill carries

- **The builder's words are the source.** Every step, rule, and edge case in the file traces
  to something they said. You may tighten their wording; you may not add a step they didn't
  describe, and you may not resolve an ambiguity by choosing the sensible option.
- **A gap stays a gap until they close it.** The understudy's findings are answered by the
  builder or carried openly into the runbook. Neither you nor the understudy fills one.
- **Nothing generated reaches the outside world.** A generated skill drafts, shows, and
  stops. It never sends, posts, submits, or updates a system of record, and it never writes
  outside the builder's project. This holds even when the builder asks for it — the answer
  is the scope line, not a workaround.
- **Never overwrite their work.** A name collision is a question, not a merge. Existing
  files in `.claude/skills/` are theirs.
- **A short process gets a short runbook.** A three-step job written down honestly is a
  win; padding it to look like a system is how a runbook stops being trusted.
- **The time-saved line above ships only with a timed figure and its provenance**, and this
  card's baseline is one manual run of the *process* (E6-26 decision, 2026-09-03) — never
  a timed comparison of skill authoring, which measures a job the builder was never going
  to do.

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`agents/understudy.md` owns the `cold-run.md` section names** (How far I got, Had to
  guess, Couldn't find, Decisions with no rule, Unstated exceptions, Would go outside the
  project or touch something live, What held); step 18 and the artifact's § 8 read them by
  name. Reword them in either file and the findings go missing silently. The understudy's
  **do-not-read rule** (`process.md` and the interview notes are off limits) is the whole
  test — it is stated in both files on purpose, and softening it in either one makes the
  cold run worthless without failing loudly.
- **The generated skill's shape is Session 5's shape**, deliberately:
  `.claude/skills/<name>/SKILL.md`, two-field frontmatter, trigger phrases inside the
  `description`, bare `/<name>` invocation. `skills/learn-turn-a-task-into-a-skill/SKILL.md`
  teaches a builder to write that file by hand and is this skill's depth link. **The two
  must not drift**: if the seeded-skill shape changes in `bluerock-io/my-workspace`, both
  files change together. Session 5 carries `disable-model-invocation: true`, which is what
  keeps a builder saying "make me a skill" landing here rather than in the session.
- **Session 5's hard floor applies to step 18** — its rule that a builder's own design
  answers may never be supplied for them is the same rule, in a different wrapper. This
  skill does the typing; it does not do the deciding.
- **The three constant never-do rules in step 15** are the guardrail's only enforcement in
  the generated file, and the scope line, the understudy's guardrail check, and the
  artifact's § 7 line are the same rule stated four times on purpose. Weaken one and the
  other three are load-bearing alone.
- **The artifact's token table is `skills/competitive-intel/SKILL.md` § the artifact by
  reference, not by copy.** Change the palette there and this tool follows; change it here
  and the Phase 1 tools stop matching. The **lane meanings** in the table above are local
  to this skill.
- **`curriculum/manifest.json`** carries this skill's `one_liner`, `artifact`, `time_saved`,
  and `team` — the menu and the site read them; keep them in step with the opening lines
  here. **README.md § Process to Skill** quotes the intake shape and the two deliverables.
- The working folder shape `my-work/process-to-skill/<YYYY-MM-DD>-<slug>/` is what makes run
  history findable. `/bluerock:wrap-up` logs a run against **`understudy`** directly, not
  as a one-member team — the team roll-up shape in wrap-up's dashboard contract is for
  multi-agent teams, and a team bar with one member misreads.
- **This skill deliberately carries no Slack beat.** The path's three share/ask beats are
  set (Sessions 5, 7, and 8), Session 5 already owns the "first thing you built" share, and
  a fourth is one too many — the rule is in `skills/learn-turn-a-task-into-a-skill/SKILL.md`
  § Who depends. The use-case skills follow `competitive-intel` and close on the depth
  offer.
- **The flow doc mirrors this skill** (content repo, private:
  `09-product/use-case-flows/process-to-skill-flow.md`) — any change to the interview,
  generation, cold run, artifact, or close updates it in the same pass.
