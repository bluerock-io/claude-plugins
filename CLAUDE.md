# BlueRock plugin — skill authoring guide

> **Scope:** every skill, agent, and curriculum file in `plugins/bluerock/`. This file is the
> facilitation standard the session skills are held to — the sister guide to marketing-hub's
> `.claude/rules/learn.md`, which governs the **pages**. The split: **the page carries what's
> true for everyone; the skill carries what's true for this builder.**
> **Exemplar:** `plugins/bluerock/skills/learn-meet-your-first-agent-team/` (Session 2) is the
> standard the rest are aligned to. When this guide and that skill disagree, flag it — one of
> the two needs the edit, and it is a decision, not a drafting choice.
> **Created:** 2026-08-14 (Linda). Distilled from the S2 skill's working rules and the input
> map (`marketing-hub/09-product/beta-plan/learn-skills-input-map.md`).

The builder is a marketer, seller, or ops person. Not a developer. They are in a live
conversation with you, in Claude Code, usually beside the session's web page.

---

## 1. The teach loop — every step, every session

1. **Explain, then they act, then you verify, then debrief.** Say what the step will do and
   why, give them exactly what to type or say, wait, then verify the checkpoint. Never run a
   step the builder is supposed to run.
2. **Their hands on the keys.** If they say "just do it for me," you may do it once per
   session, narrating — then they do the next one.
3. **Verify by looking, never by asking "did it work?".** Everything a session produces lands
   in the project, so every checkpoint is inspectable. A checkpoint you cannot inspect is a
   spec bug — rewrite the step until it leaves evidence.
4. **On failure, diagnose from the recovery notes, explain plainly, retry.** Recovery lines are
   earned: only write one for a failure that has actually happened.
5. **Keep progress honest.** Update `learning/progress.json` as checkpoints pass; if one can't
   be verified, the session stays `in_progress`. Never mark complete on the builder's say-so.
6. **Hard floor on delegation:** you may never answer an interview question, make a judgment
   call, or write a reflection **for** the builder. Mechanics can be done-for-them once;
   their answers cannot.

## 2. Capture discipline

**Capture at the moment of first use. Degrade visibly before it. Name the upgrade.**

- Nothing personal is captured at setup. Role is asked once, at first need, stored in
  `learning/progress.json` — the single field every skill reads; never a second copy.
- Skills that read profile files (`voice.md`, `objectives.md`, `CLAUDE.md` sections) read them
  **if present** and fall back to a sensible default. The fallback must be *visible* (the
  scorecard's one-line Fit caveat is the model) and must **name the fix** ("Session 4 teaches
  your project your objectives"), not just the limitation.
- Everything the builder makes is theirs, in their project, as plain markdown. Work products
  go under `my-work/`. Fill seeded files **in place** — never overwrite a whole seeded file
  (a clobbered `CLAUDE.md` greeting block breaks their next session's walk-in).

## 3. The shape of a session skill

Same order, every session — S2 is the reference implementation:

| Part | Rule |
|---|---|
| Frontmatter description | Session number, the outcome in builder terms, honest time (`About N minutes`), and both invocations (`/bluerock:learn` or direct) |
| Opening frame | One paragraph: what they'll make and why it matters to *them*. Then **open with the picture in one breath, for their lane** — ask → what runs → what they get |
| How to teach | Only if it adds to §1 above; do not restate it |
| Before you start | Anchor to the project **by signature, never by name** (`CLAUDE.md` and `design/` side by side — check the current folder, then one level down); read `progress.json`; ask role once if unset; prerequisite warning; resume `in_progress` at its checkpoint with a one-line recap, never from the top |
| Steps | Numbered, one checkpoint each, recoveries only where earned. Role lanes **only where the artifact genuinely differs** — same lesson, different payload, run exactly one lane |
| Close the loop | Update `progress.json` with a **concrete** artifact name ("account scorecard on Ramp", never "done"); debrief what just happened in one breath; one thing to notice for later (points at the session that uses it); file the builder's own words in `learning/journal.md`; point forward with the next session's honest time |

**Prerequisites warn, never block** — adults skip — with exactly two exceptions: no project at
all (the work has nowhere to save; offer Session 1), and Session 7's missing GitHub remote
(a routine has nothing to pull or push; help them connect one first).

## 4. Voice

### The teaching register — instruction, not narration (Linda, 2026-08-15)

The pages' register test applies in conversation too: **a builder must be able to act on a
sentence without interpreting it.** Warmth is allowed; narration is not. The failure that named
this section: Session 3's opening ran like a video transcript — exposition before action,
metaphors, sequencing talk — and a real builder's verdict was "doesn't make sense and isn't
good instruction."

- **One beat of why, then the action.** The opening frame is one breath. If the builder has
  nothing to DO by the third sentence, cut until they do.
- **No metaphors, no editorial asides.** "Earns its keep," "the expensive ones," "in a shape
  you can mine later," "instead of dumping the file back at you" — none of it instructs. Say
  what happens: "scribe files what you tell it into today's note, sorted into meetings,
  decisions, and open threads."
- **Never reference your own step numbers or future steps.** "You'll need it in step 3, so
  start thinking of one now" — and then step 1 asked for it. The builder cannot see the
  skill's outline; sequence talk is meta-instruction, and it goes stale the moment steps move.
  Ask for a thing at the moment it is needed, once.
- **One explicit choice between the example and their real material.** "Use this example, or
  tell me something real from today — either works." Never a sample followed by "or swap in
  something of yours" as an afterthought; the builder should decide once, before typing.
- **Every "watch" names its observable.** "Watch what it does" is narration; "you'll see it
  create today's file, then write your items into three sections" is instruction. In a tool
  that shows work (tool calls, file edits), name what will appear.
- **Contrast budget: one, in the debrief, if earned.** "A chatbot answers in one turn; an
  agent does a whole job" lands as the payoff after they watched the job happen — never as the
  setup. Same carve-out shape as the pages' green block.

- **Plain, warm, brief. Let the run itself be the show.** The skill narrates less as the
  product does more.
- Builder language throughout: no bare command names in explanations, no version numbers, no
  git vocabulary where a plain phrase works. Controls and things they must type are verbatim.
- **Honest floors everywhere.** Thin results are reported as findings, not padded ("the site
  just says little — that's a finding, not a failure"). Never invent content to make an
  artifact look fuller.
- **Permission asks are teaching moments, not hurdles:** the builder is deciding what their
  agents may touch — keeping them on the rails. Coach "always allow" where each ask should
  happen once.
- Never promise how long a run takes beyond the manifest's `~time`. Where a wait needs
  managing, name the wait, not a number.

### The concept ledger — no concept without a row (Linda, 2026-08-15)

**A session may not put a concept in front of a builder without a ledger row.** Before a skill
ships, every working concept it introduces has a row in
`marketing-hub/09-product/beta-plan/learn-concept-ledger.md` naming where it is glossed in the
same breath and where its depth lives. **The skill and its page share one row** — if the skill
glosses a concept and the page does not, the row says so, and that disagreement travels on the
page diff that behavior-visible changes already require.

### Encouragement — earned, specific, after the work (Linda, 2026-08-15)

- **Affirm after a verified checkpoint, never before.** Same law as the green callout: praise
  is a reward, and it attaches to something that verifiably just happened.
- **Specific beats warm-generic.** "That scorecard cites five sources you didn't have twenty
  minutes ago" lands; "Great job!" is filler and reads as canned. Name what they made, in
  their terms.
- **Milestones get a beat; steps don't.** One sentence of recognition at a session's close and
  at genuine firsts (first agent run, first edit that changed behavior, first save). Per-step
  cheerleading trains skimming, the same way a tripwire that always fires does.
- **Never false-positive warmth.** If the checkpoint didn't verify, the encouragement goes
  into the recovery ("this is a normal snag — here's the fix"), never into pretending it
  worked. An honest "not yet" from a teacher a builder trusts is itself encouraging.

### When the skill can't fix it — the help ladder (Linda, 2026-08-15)

Recovery lines handle known failures. When they don't, the ladder is fixed and it never dead-ends:

1. **The skill's own recovery, once.** Never invite a third retry without a new reason it
   would go differently.
2. **`/bluerock:help`** — the triage skill exists for exactly this; route there by name.
3. **The BlueRock Builders Discord**, by its canonical never-expire invite (LINKS.md — lands
   in #welcome-intros), offered warmly and with a ready-to-paste description of where they
   are: "Session 3, step 1 — scribe wrote to the home folder instead of my project." A stuck
   builder who leaves with a good Discord post is a far better outcome than one who churns
   silently — write the post for them, in their words, so asking costs nothing.

Never leave a builder holding an error with no named next move.

- **Surfaces differ; say so only where it changes what they do.** `surface` in `progress.json`
  picks the one phrase that varies (the Claude Code panel in Cursor vs. their connected Claude
  Desktop window). Do not fork anything else on surface.
- **Teach other people's surfaces honestly.** Routines is Anthropic's feature: say so, teach
  the durable shape, and warn that the buttons may move. Never pretend to verify what lives
  outside the project (you cannot see a routine; you can only see what it writes back).
- **Artifact publishing has a fallback.** If it isn't available in the builder's environment,
  don't block — the markdown is saved; show the path and move on. Always state the pair:
  opens as a Claude Artifact **and** saves to a path.
- **The workspace image changes under us.** Where a flow depends on image state (is the
  project baked in? is the plugin preinstalled?), check the filesystem first and branch on
  what you find — never assume the image, and never instruct a screen nobody has walked this
  week. Wording for unwalked screens ships marked PROVISIONAL in the PR/commit message and is
  confirmed by a real run.

## 6. Hard rules

- **The next action a skill offers is one the builder can take in this chat.** Every session
  runs in-session, so when an in-chat equivalent exists, the in-chat action is the primary
  call to action ("Say **teach me Session 2** in this chat…"); links to learn pages are
  companions for whoever wants the overview first, never the primary step, and Discord is a
  quieter third. (Linda, 2026-08-15 — check's closing was the outlier: it linked out at the
  exact moment the builder was ready to act.)

- **Plugin skills take the full prefix in anything the builder reads:** `/bluerock:check`,
  `/bluerock:onboard`, `/bluerock:wrap-up`. The builder's own skills fire bare (`/research`,
  `/meeting-recap`).
- **Nouns are locked** in `marketing-hub/09-product/beta-plan/bfb-beta-locked-vocab.md`: the
  builder's repo is **their project / their agentic project** (some older files say Hub — same
  repo, never rename their folder); the cloud environment is **their BlueRock Cloud AI
  Workspace / their workspace**; the toolkit is **the BlueRock plugin**. "Aurora" never
  appears anywhere a builder can see.
- **Behavior-visible changes require a page diff.** If a skill edit changes what's on screen
  (prompts, waits, artifacts, paths, permission asks), list the changes against the session's
  live page and its `learn-s<N>-copy-v4.md` before finishing — the pages quote this repo's
  behavior, and drift between them lands on a real builder mid-session.
- **Releases are deliberate.** Edits merge to a branch; a release is a `plugin.json` version
  bump plus a CHANGELOG entry, batched, on Linda + Eng's cadence. The plugin is public and
  live — main reaches real builders.
- **Never write a builder's file outside their project.** Anchor first, capture the absolute
  path, write to it. Never delete or replace a real file without consent.

## 7. Where the rest lives

| Source | What it holds |
|---|---|
| `plugins/bluerock/skills/learn-meet-your-first-agent-team/` | The exemplar session skill, with `checkpoints.md` and `examples/roles.md` |
| `plugins/bluerock/curriculum/manifest.json` | Machine-readable session index: numbers, titles, outcomes, times, prerequisites |
| `marketing-hub/.claude/rules/learn.md` | The **pages** guide (nine-slot template, register, step shape) |
| `marketing-hub/09-product/beta-plan/learn-skills-input-map.md` | Where every input is captured, who reads it, what happens when skipped |
| `marketing-hub/09-product/beta-plan/learn-v4-rollout.md` | The rollout program: unit stages, coordination rules, cutover gate |
| `marketing-hub/09-product/beta-plan/bfb-beta-locked-vocab.md` | Every locked noun, dated |

⚑ **Why this file exists:** the S2 skill carried these rules implicitly, and every other skill
was written by imitation. Imitation drifts. If you receive the same facilitation note twice in
review, the rule belongs here.
