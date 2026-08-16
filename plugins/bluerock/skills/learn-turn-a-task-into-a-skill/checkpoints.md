# Session 5 — checkpoint verification spec

Six checkpoints. The first two verify a file the builder only **reads**; the last
four verify a file they **authored**, which changes what "pass" can mean.

**Checkpoints 5 and 6 verify SHAPE, not content.** There is no correct output
here — it's their workflow, and only they know what good looks like. Asserting
content would either fail correct work or pass anything. Check the file is in the
right place, has the right frontmatter, and actually fires. The quality of the
instructions is theirs to judge, and step 6's edit loop is where they judge it.

Run inspection commands quietly; the builder sees conclusions, not plumbing.
`<project>` is the project's absolute path.

## Checkpoint 1 — meeting-recap ran and produced a real draft

- **Observed in-conversation:** a follow-up email in the chat, in the skill's
  fixed shape (subject, opener, what was agreed, one ask, sign-off), with a
  "check before sending" note **below** the draft rather than inside it.
- **The shape is the checkpoint, not the content.** If it read yesterday's notes
  or a thin set of bullets, the draft may be thin. That passes. A generic
  template with `[placeholders]` where the meeting should be does not — that
  means it found nothing and improvised, which the skill is written not to do.
- If it declined to draft because no notes exist, that is **correct behavior, not
  a failure.** Have them paste bullets from a real call and re-run. Pass on the
  re-run.

## Checkpoint 2 — they can point at three things in the file

- **Conversational, and it's a real check — don't wave it through.** Ask them to
  find each one and wait for their answer:
  1. the **trigger phrases**, and specifically that they live *inside* the
     `description` rather than in a field of their own;
  2. the **never-do rule** (*"Do not invent a meeting."*);
  3. the **one-ask rule** (*"One ask per email, never two."*).
- **Confirm the file they opened is `.claude/skills/meeting-recap/SKILL.md`.** If
  they report not finding the file, they are probably looking in
  `.claude/commands/`, which does not exist in this starter kit — the site page
  says so wrongly. Redirect them in one line without editorializing about the
  site.
- Getting one wrong is not a fail; walk them to it. The point is that they've
  read a real skill file closely enough to build one, and skimming here shows up
  as difficulty in step 4.

## Checkpoint 3 — a named workflow, in one sentence

- **Conversational:** they finish "the skill I want to build is ___" with one
  sentence naming a real, repeated, mostly-text workflow.
- **Pass spec, and hold this line:** it must be something **they** have actually
  done more than once. "Something for emails" is not yet a workflow — push once
  for which email, in what situation. A workflow they picked off a suggestion
  list without recognizing it as theirs will produce a skill they never use, and
  step 6's "real input" will be a toy.
- If they genuinely cannot name one after their role's prompts and the two
  fallback questions (what they did last Friday afternoon; what they'd hand a new
  hire first), stop the session here honestly at `in_progress` rather than
  inventing one. Say it's worth coming back to with a week of work in view. That
  is a better outcome than a skill nobody wanted — and point them at the Discord
  on the way out, where other builders name the workflows they turned into
  skills. Watching someone else's list is often what makes their own visible.

## Checkpoint 4 — five questions asked and answered

- **Observed in-conversation:** the agent asked five sharpening questions and
  **the builder answered them.** Both halves.
- **You cannot pass this one on your own answers.** If they said "just decide
  for me," the escape valve does not apply here — their answers are the skill's
  content. Ask again, smaller: pick the two questions that most change the output
  and get those. Two real answers beat five invented ones.
- Questions that came back generic mean the workflow statement was too vague:
  have them restate it with an example of the output they want, then re-ask. Pass
  on the second round.

## Checkpoint 5 — the file exists, in the right place, in the right shape

- **Inspectable:** `.claude/skills/<name>/SKILL.md` exists under the project,
  and:
  1. it has **frontmatter** with `name` and `description`;
  2. `name` matches the directory name (this is what makes `/<name>` fire);
  3. the `description` contains **plain-language trigger phrases** — the words a
     person would actually say — not just a summary of what the skill does;
  4. there are **instructions below the frontmatter**, not an empty body.
- **Do not assert anything about the instructions' content.** Sections, length,
  and rules are theirs. A skill whose body is three sentences passes if those
  three sentences are their workflow.
- **Wrong location is the failure to catch here:** `.claude/commands/<name>/` is
  the likely miss (the site page names it). Move the file and re-verify rather
  than passing it in place.
- Extra frontmatter fields: not a fail. Trim them and say why in one line — the
  two-field shape is what they read in step 2.

## Checkpoint 6 — it fires both ways, got refined, and is saved

Three parts, all required.

- **Fires by slash:** observed in-conversation — `/<name>` ran on a **real
  input**, not a toy. A run against made-up sample data means the editor's read
  that follows it isn't real either; ask for something from this week.
- **Fires by phrase, from a new chat:** their report is the evidence, and this
  one **cannot** be verified from this conversation — the design discussion is in
  here, so a phrase said here proves nothing about the description's routing.
  Ask what they saw. If it fired without a slash, pass.
  - **Mark `{ "status": "in_progress", "checkpoint": 5 }` before they leave** for
    the new chat, so nothing is lost if they don't come straight back.
  - If it didn't fire, that's the session's most common failure and it is
    fixable: rewrite the `description` to name the exact words they'd say, and
    try again. Do not pass this on the slash alone. **If a second rewrite still
    doesn't fire, stop retrying and climb the help ladder** (`/bluerock:help`,
    then Discord with a post written for them). Leave the session
    `in_progress` at checkpoint 5 and say plainly that the file is real, saved,
    and runs by slash — the routing is the only open part.
- **Refined at least once:** the file changed after they read the real output —
  `git -C <project> diff` or the log shows an edit to their `SKILL.md` after its
  creation. A first-try-perfect skill is rare; if they insist nothing needed
  changing, ask what they'd change if they had to name one thing, and let them
  decide whether to make the edit. Their call, but the loop is the lesson.
- **Saved, and the save runs through wrap-up** (step 6), not through a separate
  ask. Verify the result, never the mechanism: `git -C <project> log -1 --stat`
  shows the new skill file. Run it quietly; the builder sees the conclusion, not
  the plumbing. Keep the builder-facing word to **"saved."**
  - **No remote is a full pass, and say nothing about it.** A local save is the
    finished state on newer workspaces. wrap-up is deliberately silent about
    pushing and backup; raising either invents a problem the builder doesn't have.
  - **An identity prompt is not a failure.** A fresh workspace has no git identity
    configured, so wrap-up asks for a name and email to label the save. Let
    wrap-up run that exchange; never pre-empt it with `git config` of your own.
  - **A blocked backup still passes** on the local save. Don't teach git here.
  - If nothing was saved at all, that fails — offer the one-line fix ("wrap up my
    session") rather than sending them away.

## Encouragement, and where it goes

Two checkpoints earn a beat, both after they verify. **Checkpoint 5** is the
first thing this builder has built rather than run — name what they made, in
their own words for it. **Checkpoint 6** is the routing working from a cold
chat — name the evidence, not the achievement. Everywhere else, confirm and move
on: six congratulations in one session trains skimming, and a checkpoint that
didn't verify gets the recovery, never the warmth.

## Marking progress

After each verified checkpoint N:
`sessions["5"] = { "status": "in_progress", "checkpoint": N }` — and on
checkpoint 6, `{ "status": "complete", "completed": "<today>", "artifact":
"/<their-skill-name>, fires by name and by phrase" }`. Write valid JSON; never
delete history. Never mark a checkpoint you didn't verify — honest state beats a
green dashboard.
