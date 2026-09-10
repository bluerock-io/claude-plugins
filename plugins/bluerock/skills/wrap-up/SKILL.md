---
name: wrap-up
description: >-
  End-of-session ritual: log what this session did, refresh my BlueRock
  dashboard, then (with my go-ahead) save a checkpoint of my project and hand me
  a continuation prompt for next time. Use when I say "wrap up", "wrap up my
  chat", "wrap up my session", "done for today", "end session", "ship it", or
  "save my progress". Not for mid-session saves; only when the chat is actually
  ending.
---

Wrap up this working session. Conversations end; the work persists. Make sure
everything this session produced survives into the next one: my dashboard
refreshed, the story logged, and — once I say so — committed and ready to pick
back up.

## Steps, in order

### 0. Anchor to the project

Everything below reads and writes inside the builder's project: `today.md`,
`session-log.md`, the project's `.bluerock/runs.json`, and `design/dashboard-data.js` —
and `git` runs from the project root. Two generations exist: the project ships inside the workspace image (usually the folder
`my-workspace`); projects made before 2026-08 were cloned and carry whatever
name the builder chose. **Assume neither — identify it by its signature.** In an
SSH/cloud container the chat may start in the project itself or in the **home folder**
with the project one level down — both are normal. Confirm first: run `ls`. See `CLAUDE.md` and `design/` side by side? You're in the
project. If not, find it: `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`, else
`find ~ -maxdepth 3 -path '*/design/dashboard.html'`. **`cd` into that folder and stay
there for the rest of the wrap-up**, and capture its absolute path with `pwd` so every
write below targets the full path (e.g. `/home/you/maria-hub/design/dashboard-data.js`).
Skipping this writes the dashboard and log to the home folder and runs `git` against the
wrong repo (or none). Can't find it? Ask the builder which folder their project is in
before wrapping up. (`session-metrics.py` below is the one exception — it's read via
`${CLAUDE_PLUGIN_ROOT}`, so it runs correctly from anywhere.)

### 1. Review the session

Look back over this conversation and identify what got done (finished things,
not attempts), which files were created or changed, any decision I made that
future sessions should know about, and what's unfinished. Don't ask me to
summarize — you were here.

### 2. Refresh my dashboard

Real numbers, not guesses. First read this session's tokens + time honestly from
the Claude Code transcript:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/wrap-up/session-metrics.py"
```

(If it returns `{"ok": false}`, continue with zeros and note "metrics unavailable
this session.") Then:

- **Build this session's run atom(s)** — one per agentic run, contract shape:
  `{ ts, sessionId, agent, target, outputFile, runTimeSec, success, tokens,
  toolsCalled, filesRead, model, costUsd, guardrailEvents }`. Quantitative fields
  from the script; qualitative (agent, target, output) from the session. `model`
  = the canonical undated alias from the usage payload (e.g. `claude-sonnet-4-6`).
- **Append the atom(s) to the run history** — the project's own `.bluerock/runs.json`
  (keep all atoms). Note this is the project-local `.bluerock/`, distinct from the home
  `~/.bluerock/` workspace facts read below.
- **Tally today's priorities.** Read `today.md` and count Focus items: `set` (total),
  `closed` (`[x]`), `carried` (`[>]`). Offer to check off anything I finished this
  session that's still `[ ]`. This feeds the dashboard's "priorities set vs. closed."
- **Tally time saved, and say what it is made of.** The rule for attributing an atom to a
  use case, and for counting runs, is in `${CLAUDE_PLUGIN_ROOT}/shared/use-case-catalog.md`;
  read it rather than working from memory. Across the whole run history in
  `.bluerock/runs.json` (not only this session), count runs per use case, multiply each by
  its estimate, and sum. The estimate is **the builder's own number** when they have given
  one (next bullet), otherwise the manifest's `time_saved_minutes` for that use case. A use
  case with no estimate is left out and said to be left out, never counted as zero. Atoms
  that attribute to no use case (the builder's own skills and agents) are not in the tally;
  if there were any this session, say so in a clause. **The label states what the number
  is: a count of runs times an estimate per run, and whose estimate.** Two labels exist and
  no line blurs them: *from what you told us* for a use case the builder priced, *our
  estimate* for one they have not. Never "measured," never "baseline runs": no run of any
  use case has ever been timed, and the note claims no measurement we have not made. Round
  to the half hour. Example of the readout line:

  > Time saved so far, estimated: about 6 hours across 3 runs. That is a count of your runs
  > times an estimate per run: yours for the Account Scorecard (1.5 hours each, from what
  > you told us), ours for the Brand Messaging Doc (4 hours).

  The tally lives in the plain readout below. **The dashboard contract carries no
  time-saved field today**, so it does not go on the dashboard artifact and no field is
  added to `design/dashboard-data.js` for it (the contract rule further down). It goes on
  the dashboard the day `design/dashboard-data-contract.md` in the builder's project defines
  a field for it, with this label.
- **Ask the baseline question once per use case, after their first run of it, in its own
  message.** Before the readout, for each use case run this session that has no entry in the
  project's `.bluerock/baselines.json`, ask, alone, nothing else in the message:

  > One quick question before your numbers: how long did an Account Scorecard like this used
  > to take you by hand? A rough number is fine, or say skip.

  Record the answer, merged into `.bluerock/baselines.json` (create it if absent; never
  remove another entry): `{ "<use-case id>": { "minutes": <number or null>, "asked":
  "YYYY-MM-DD", "skipped": <true or false>, "said": "<their words>" } }`. **Never re-ask,
  whether they answered or skipped**, and never bundle it with a question about their work;
  a stored-fact question sent beside a work question does not get answered. It is a
  baseline question, not a value question: "how long did this used to take you" is a number
  they can defend, and it is what grounds every later estimate. Their number drives their
  tally from then on, and the label says so. The file is the builder's, in their project;
  the manifest never learns it. Two new use cases in one session means two messages, one
  each, which is rare and fine.
- **Roll up the sections and overwrite the dashboard data file** so my dashboard
  repaints — match the pinned contract exactly, all keys present:
  `window.__BR_DASH__ = { meta, productivity, cost, actions, guardrail, perf, brag, priorities, runs }`
  (write it to the starter kit's `design/dashboard-data.js`). The renderer just paints —
  roll the sections up here, don't make the browser re-aggregate.
- **Never carry `sample: true` forward.** The seeded file ships with it, and it renders one
  line telling the builder the numbers are a demo. The moment you write real rollups that
  line is false, so drop the flag (or write `sample: false`). This is the one key you
  remove rather than update.

Provenance is a trust claim. Beta has **no BlueRock sensor pipeline**, so the label
is **"From your sessions,"** never "sensor-sourced." Specifically:
- `guardrail` = `{ wired: false, events: [] }`.
- `cost` = `{ available, today, deltaPct, series }`. **`available: true` only when a real pricing table is present in the workspace and you read it** (tokens × price). Otherwise write `available: false` and leave the rest as they are: the card renders **"Coming soon"** and no number. Never estimate a rate, never carry one over from elsewhere, and never write a zero — a zero is a claim about spend, and "not tracked" is not "$0.00." Say it in one line in the plain readout too: cost isn't tracked in this workspace yet, which is a missing source rather than a free session.
- `meta` (builder, workspace, region) comes from the **workspace facts file** — the home `~/.bluerock/workspace.json` (Eng-provisioned, workspace-level; NOT the project's `.bluerock/`). Take `builder` / `workspace` / `region` from it; if it's absent, degrade honestly to a generic builder name. **No trial countdown.** The trial clock is not passed into the workspace and the dashboard is a value mirror, not a conversion surface — trial timing and upgrade prompts live in the email lifecycle and Console, not here. Never scrape boot time or file timestamps to fake a provision date (the container suspends/resumes, so those are wrong).
- `meta.outputsSince` is **singular "you," single user (not a team)**; `count` = outputs this week from `runs[]` (not a last-visit anchor); 0/unknown → greeting only, no fabricated number.
- `priorities` = `{ set, closed, carried }` for this week, counted from `today.md` (the closure loop). Derived "from your sessions," not sensors.
- `actions` = `{ total, byAgent: [{ name, count, tone, timeMin }] }` — agent actions this week from `runs[]`, grouped by `agent`. `name` = the agent's name (required — labels the bar), `count` = its action total, `tone` = a stable palette key (`coral`/`plum`/`composer`/`sage`) for the bar (omit → defaults to coral; reuse the same tone per agent across weeks), `timeMin` = wall-clock minutes for that agent this week (from `runs[].runTimeSec`, rolled up). For a multi-agent **team** (e.g. Account Research = researcher + signal-scanner + composer), emit one entry for the team plus `members: [{ name, count, timeMin }]` (members sum to the team's `count` and `timeMin`); use the same team label in `runs[]` so it reads consistently across the Actions card and section 04.
- `perf` = `{ successRate, runs:{successful,total}, avgSessionMin, avgSessionDeltaMin, outputsShipped }` — the honest set only. **No** output-quality/reader-rating and **no** cache-hit rate (dropped — no honest source / operator metric). `success` is your judgment (a run that completed without error or guardrail block); `avgSessionMin` from `session-metrics.py`; delta is neutral (shorter ≠ better).
- `resume` chapter comes from learning-path progress, not the transcript.

**`design/dashboard-data-contract.md` is the single authority on the shape, and this skill
is its one consumer.** Write only the fields it defines, in the structure it defines:
no invented fields, no improvised formats, no restyling, no "helpful" extras. Where a
value has no honest source, write the empty state that file specifies rather than a
plausible number. Read it before you write, not from memory — it is a file in the
builder's own project and it can be ahead of you. `dashboard.html` is the renderer that
paints what you write; if the contract and the renderer disagree, that is a bug to
report, not a gap to fill with a guess.

### Writing when another session is also wrapping up

Builders run more than one chat at once, and two wrap-ups against one project will race.
This happened on 2026-08-15: `design/dashboard-data.js` was rewritten mid-write and
`.bluerock/runs.json` gained two atoms from a session that had started after this one.

**Immediately before you write `design/dashboard-data.js`, `.bluerock/runs.json`, or
`session-log.md`, re-read each one.** Not the copy you read at the start of the wrap-up —
the file as it is now.

- **Merge, never overwrite.** Append your atoms to what is there. Entries you did not
  write are not yours to remove, reorder, or "clean up," and a run history that silently
  loses runs is worse than one that is briefly untidy.
- **If a file changed between your read and your write, re-read and reconcile again.**
  Repeat until your write lands on the version you actually read.
- **`session-log.md` is append-only, always.** Add your entry; never rewrite the file.
- **If another session's reconciliation is more complete than yours, leave it alone.**
  On 2026-08-15 the other session had already restored all four run atoms with better
  notes on the token overlap than this one was about to write, and leaving its work in
  place was the right call. Correct only what is yours.
- **Say so in one line** when you find another session's work: which files moved, what you
  merged, what you left. The builder is the only one who can see both chats.

**First, show me my numbers in the panel.** Before opening the visual dashboard, print a
short, plain readout of this session so the payoff lands even if the page doesn't open:
the runs this session and what each did, session length, priorities set / closed /
carried (from `today.md`), success rate, **time saved so far with its label** (the tally
above), and cost only if a pricing table was present
(else "not tracked this session" — never a guessed number). A few honest lines, "from
your sessions." This always works, with no server or port involved.

**Then render my visual dashboard as a Claude Artifact.** The project runs in a remote,
headless cloud workspace — there's no browser on the container and no forwarded port,
so a served page (`localhost:...`) never reaches my machine. Instead, publish the
dashboard as a **Claude Artifact**: it's hosted for me and opens right here, no port,
no browser on the container, nothing to install. Do this now, and any time I say
**"open my dashboard"**.

Build a **single, self-contained HTML page** from the rolled-up data above and hand it
to me as an artifact. The static `design/dashboard.html` is your visual reference (the
cool-paper look — light theme, Source Serif / DM Sans / JetBrains Mono headings, the
card layout), but the artifact must be self-contained, so:

- **Inline everything** — all CSS and all data in one file. Read the rolled-up values
  out of `design/dashboard-data.js` and write them directly into the page as literal
  values (or an inline `<script>` that sets them); do **not** `fetch()` or load an
  external `dashboard-data.js`, and do not use ES-module imports.
- **No external requests of any kind** — no CDN scripts, no external stylesheets, no
  web fonts, no remote images. Artifacts run under a strict CSP that blocks them.
  Use system-font fallbacks (`Georgia, serif` for the serif headings;
  `system-ui, sans-serif` for body; `ui-monospace, monospace` for numerals) so it
  still reads like the design without the web fonts.
- **Embed the logo as a `data:` URI.** The BlueRock for AI Builders logo must be inlined as a
  base64 `data:` URI built from the project's `design/builders-logo-light.svg` (the design-system
  logo, alongside `dashboard.html`) — never an `<img src>` that points at that file. The same
  CSP that blocks remote images blocks a file reference too, so it fails silently and every
  builder's dashboard ships with a broken logo. Read the SVG, base64-encode it, and set
  `src="data:image/svg+xml;base64,…"`. If the file isn't present, omit the logo rather than
  reference it externally.
- **No CTA buttons and no trial countdown.** This is a read-only value mirror — what my
  agents did, what shipped, what it cost. No "Upgrade," no "Start trial," no
  "days left." Conversion and trial timing live in the email lifecycle and Console,
  not here. A dead button in a sandboxed artifact is worse than no button.
- **Topbar is the logo only.** No account chrome in the header — no builder name, no
  workspace id, no avatar. The dashboard is a read-only value mirror, not a logged-in
  console, so the top bar carries the logo and nothing else.
- Keep the **"From your sessions"** provenance label and the honest-data rules above —
  omit any section you don't have honest data for rather than faking it.

Also **overwrite `design/dashboard-data.js`** as specified above regardless — it's the
data of record (and the source for the future hosted render), even though the artifact
inlines its own copy.

If publishing an artifact isn't available in my environment for any reason, don't
block: the plain in-panel readout above is the always-works fallback, and the data
file is saved — just tell me the artifact couldn't be created and show me the numbers.

### 3. Update the session log

Append an entry to `session-log.md` at the project root (create it with a one-line
title if it doesn't exist). Newest at the bottom, short — a trail, not a diary:

```markdown
## YYYY-MM-DD — [what this session was about, in a few words]

**Did:** [1-3 lines]
**Files:** [paths created or changed]
**Decided:** [only if a real decision was made; otherwise omit]
**Next:** [what the next session should pick up]
```

### 4. Show me what's about to be saved

First, check what is actually possible. Run `git status`, `git remote -v`,
`gh auth status`, and `git config user.name` / `git config user.email`. What you offer
depends on what you find:

- **No identity configured** (either is empty) → **fix this before anything else, and
  never by letting the save fail first.** On a fresh workspace nothing is configured, so
  this is every new builder's first wrap-up, and it breaks the purely local save that has
  nothing to do with GitHub. Don't show them the raw git error, and don't ask them to run
  `git config` themselves. Ask once, plainly, and say what it is for:

  > "What name and email should your saves be recorded under? This just labels your work
  > in your own project — nothing is sent anywhere."

  Then set it **scoped to this project** — `git config user.name` and
  `git config user.email` inside the project, **never `--global`**; their workspace is
  theirs and this skill has no business setting a machine-wide identity. If they'd rather
  not answer, say plainly that saving needs a name to record the save under, that nothing
  leaves their workspace either way, and that wrap-up will offer again next time. Then
  skip the save and carry on with the rest of the wrap-up — the log and the dashboard
  don't depend on it.
- **No remote** → the save is local only. Do not mention pushing, backup, or GitHub.
  There is nothing to push to, and raising it invents a problem the builder does not
  have.
- **The remote is BlueRock's template** (`bluerock-io/my-workspace` in its URL) → treat
  it as no backup at all, because it is the shared template every builder starts from,
  not theirs; earlier workspace images left it pointed there. Never offer to back up to
  it, even if the push would succeed. The save is local only, and one line covers it:
  "your project still points at BlueRock's template rather than a backup of your own;
  `/bluerock:check` can clean that up."
- **Remote, but not authenticated** → offer the local save now. Mention backup once, as
  an optional thing they can set up later. Never propose a push you already know will
  fail.
- **Remote and authenticated** → offer the save and the backup together.

Then show a plain summary: which files are new, which changed, and a proposed one-line
description of what the session accomplished (not "updates").

**If this is their first save in this project** (fewer than three commits, or none
authored by them), lead with one sentence before the file list:

> Saving takes a snapshot of your project as it is right now, with a note about what
> changed. It stays in this workspace. You can look back at it later, or undo it.

Do not use "stage," "commit," or "push" as bare verbs with a builder who has not seen
them. Say "save a checkpoint" and "back up to GitHub." Use the git words only after you
have said what they mean, or if the builder uses them first.

**Wait for my go-ahead.** "Wrap up" starts the ritual; it is not permission to save.

### 5. Save (only after I confirm)

Stage and commit with the agreed message. Identity must already be configured by step 4
— a commit that aborts with `Author identity unknown` in front of a builder is the exact
failure the state check exists to prevent. Push only if the remote exists, is the
builder's own, authentication is present, and they said yes to backup.

If a push fails anyway, lead with what worked: the local save succeeded, the backup is
the part that did not go through. One next step, not a diagnosis. A failed push must
never be a builder's first experience of wrap-up.

### 6. Hand me the continuation prompt

Then print a short prompt I can paste into my next session:

```
I'm continuing work in my project.

Last session (YYYY-MM-DD): [one sentence: what got done]
Next up: [unfinished work, if any; then the next use case, by title and command]
When you want the how: [the concept pointer, one line, only when a use case ran]

Read session-log.md for context.
```

**Next up carries the next use case** (product decision, 2026-09-09: a substitution in the
slot that already exists, never a new block; the habit and community lines below are
untouched). Fill it in this order: anything this session left unfinished, in a few words;
then the next use case by the rule in `${CLAUDE_PLUGIN_ROOT}/shared/use-case-catalog.md`,
which is the first in its order the builder has not run (read from `.bluerock/runs.json`),
or, when they ran one this session, the one that follows it. Name it by `title` and full
command, aimed at something concrete from their work when that is obvious:

> Next up: finish the Ramp follow-up note; then run the Competitor Battlecards
> (`/bluerock:competitive-intel`) on the two names from today's scorecard.

If all seven have run, Next up carries the unfinished work alone. Never a time figure
here, and never a use case named from memory.

**The third line is the concept pointer, and it appears only when a use case ran this
session.** Resolve it by the rule in the same shared file: the use case's `concept`, the
session that teaches it, and the earliest of that session's prerequisites not yet
`complete` in `learning/progress.json`. Frame it as depth available when they want it,
never as progress:

> When you want the how: Session 6, Assemble a team of agents, explains the agent team that
> ran today.

or, when prerequisites are unmet:

> When you want the how: Session 3, Anatomy of an agent, is where the explanation of today's
> agent team starts.

If the concept's own session is already complete, omit the line. No "3 of 8," no count of
sessions left.

That's the whole point of the ritual: the next session starts already knowing
what this one knew — and my dashboard already shows the work.

Then, in one line, the habit this closes: one task per chat. Start a fresh chat
for the next thing, and wrap up again when it's done.

And close with the room, one line: the BlueRock Builders Slack is where builders
ask questions and compare notes between sessions —
https://builders.bluerock.io/community. One sentence, no pitch, after the habit
line — never instead of the continuation prompt.

### 7. A quiet check on my setup

Last, run the shared version-drift procedure in
`${CLAUDE_PLUGIN_ROOT}/shared/version-drift.md`. **Silent when clean** — and silent when
the lookup didn't happen. When it finds drift, say the one tripwire line that file gives
you and nothing else: don't diagnose it, don't repair it, don't turn the end of my
session into a support ticket. `/bluerock:check` is where that conversation belongs.

## Rules

- Never commit without my explicit go-ahead in this conversation.
- Never propose a git action you have already determined will fail. Nothing in the
  curriculum teaches committing, pushing, or authenticating, so assume the builder is
  meeting all three here for the first time.
- Never push anything that looks like a credential or a private key; flag it.
- If nothing changed this session, say so, still refresh the dashboard and log
  the session if I want the record, and skip the git steps.

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`design/dashboard-data-contract.md` in the builder's project owns the dashboard's
  shape, and this skill is the only thing that writes to it.** That file names this skill
  in return. A field added here without a contract change is a field the renderer will not
  paint; a contract change without a skill change is a field nothing ever writes.
- **The identity repair is this skill's only write outside the builder's own files**, and
  it is consented, scoped to their project, and asked in builder language. It is never
  `--global`, and it is never inferred from something you happen to know about them. If
  that ever needs to widen, it is a deliberate decision recorded here, at the prompt.
- **Steps 4 and 5 decide what a builder is offered at the end of every session, and
  nothing in the eight sessions teaches committing, pushing, or authenticating.** The
  shape is deliberate: check first, then offer only what will succeed. A live tester who
  ships this product still believed a local commit had sent her files somewhere, which is
  why the vocabulary is "save a checkpoint" and "back up to GitHub" and why the first-save
  sentence exists. Don't reintroduce the git words as bare verbs.
- **Session 2's checkpoint 5 depends on this skill's *absence* of a save step being
  normal.** `skills/learn-meet-your-first-agent-team/checkpoints.md` passes on the log and
  the dashboard refresh alone, precisely because this skill may correctly never offer a
  save. Change what step 4 offers and that checkpoint needs rereading.
- **Session 1 routes builders here on day one**
  (`skills/learn-get-started/SKILL.md`, close-the-loop step 5), when there is usually no
  remote and no authentication. That is the first impression these two steps were written
  for.
- **The tripwire wording lives in `shared/version-drift.md`**, shared with
  `/bluerock:check` and `/bluerock:learn`. Reword it there, not here.
- **The use-case order, titles, run attribution, and the concept pointer live in
  `shared/use-case-catalog.md`**, shared with `/bluerock:check` and `/bluerock:onboard`.
  Step 2's tally and step 6's Next up both read it. Reword the rule there, not here.
- **`.bluerock/baselines.json` is this skill's file**, in the builder's project beside
  `runs.json`. It holds one entry per use case: the builder's own by-hand estimate, or the
  fact that they were asked and skipped. Nothing else writes it, and nothing reads it but
  step 2. If the Console ever reads it, the shape here is the contract.
- **The time-saved tally is in the plain readout and not on the dashboard, on purpose.**
  `design/dashboard-data-contract.md` defines no field for it, and this skill writes only
  the fields that contract defines. When `my-workspace` adds the field (and its renderer
  paints the label, a count times an estimate and whose), the tally moves onto the artifact
  and this note goes. Until then a tally on the dashboard would be an invented field.
- **The baseline question is a new prompt a builder sees at the end of Session 2**, since
  Session 2 runs a use case and closes with this skill. That is behavior-visible: the
  Session 2 page and `skills/learn-meet-your-first-agent-team/` describe wrap-up as logging
  the session and refreshing the dashboard, and checkpoint 5 passes on those two alone. The
  question is skippable and does not gate the checkpoint, so the checkpoint holds; the page
  diff is the one line that says wrap-up may ask one question about the work it just did.
- **learn.bluerock.io's session pages describe what wrap-up does at the end of a
  session.** Behavior-visible changes here need the page diff against the session's live
  page and the session's copy doc before finishing.
- **The one-task-per-chat line in step 6 is said in three places and must stay one
  habit** (Linda, 2026-08-19). Here, at the moment it applies; in
  `skills/learn-meet-your-first-agent-team/SKILL.md` step 5, which is where a builder
  first hears it ("a fresh chat per task, do the work, wrap up before moving on"); and in
  `skills/help/SKILL.md`'s wrap-up bullet. Session 2's live page carries the matching
  learner-facing version in its Learn more, under "Should I keep one chat going, or start
  a new one?". Reword one and the other three are the diff to check. It is deliberately
  NOT justified by the context window: Session 3 owns that concept, and this line reaches
  builders who have not reached Session 3, plus builders long past the path.
