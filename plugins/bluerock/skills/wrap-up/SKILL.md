---
name: wrap-up
description: >-
  End-of-session ritual: log what this session did, refresh my BlueRock
  dashboard, then (with my go-ahead) save a checkpoint of my project and hand me
  a continuation prompt for next time. Use when I say "wrap up", "done for
  today", "end session", "ship it", or "save my progress". Not for mid-session
  saves; only when the session is actually ending.
---

Wrap up this working session. Conversations end; the work persists. Make sure
everything this session produced survives into the next one: my dashboard
refreshed, the story logged, and — once I say so — committed and ready to pick
back up.

## Steps, in order

### 0. Anchor to the project

Everything below reads and writes inside the builder's project — the repo they cloned from
the starter kit: `today.md`, `session-log.md`, the project's `.bluerock/runs.json`, and
`design/dashboard-data.js` — and `git` runs from the project root. In an SSH/cloud
container the session usually starts in the **home folder**, with
the project one level down. The builder named it when they cloned (`maria-hub`, `alex-hub` —
don't assume a fixed name like `hub-starter`); identify it by its signature, not its
name. Confirm first: run `ls`. See `CLAUDE.md` and `design/` side by side? You're in the
project. If not, find it: `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`, else
`find ~ -maxdepth 3 -path '*/design/dashboard.html'`. **`cd` into that folder and stay
there for the rest of the wrap-up**, and capture its absolute path with `pwd` so every
write below targets the full path (e.g. `/home/you/maria-hub/design/dashboard-data.js`).
Skipping this writes the dashboard and log to the home folder and runs `git` against the
wrong repo (or none). Can't find it? Ask the builder where they cloned their project before
wrapping up. (`session-metrics.py` below is the one exception — it's read via
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
carried (from `today.md`), success rate, and cost only if a pricing table was present
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
Next up: [what to work on]

Read session-log.md for context.
```

That's the whole point of the ritual: the next session starts already knowing
what this one knew — and my dashboard already shows the work.

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
- **learn.bluerock.io's session pages describe what wrap-up does at the end of a
  session.** Behavior-visible changes here need the page diff against the session's live
  page and its `learn-s<N>-copy-v4.md` before finishing.
