---
name: wrap-up
description: >-
  End-of-session ritual: log what this session did, refresh my BlueRock
  dashboard, then (with my go-ahead) commit, push, and hand me a continuation
  prompt for next time. Use when I say "wrap up", "done for today", "end
  session", "ship it", or "save my progress". Not for mid-session saves; only
  when the session is actually ending.
---

Wrap up this working session. Conversations end; the work persists. Make sure
everything this session produced survives into the next one: my dashboard
refreshed, the story logged, and — once I say so — committed and ready to pick
back up.

## Steps, in order

### 0. Anchor to the Hub

Everything below reads and writes inside the builder's Hub — the repo they cloned from
the starter: `today.md`, `session-log.md`, the Hub's `.bluerock/runs.json`, and
`design/dashboard-data.js` — and `git` runs from the Hub root. In an SSH/cloud
container the session usually starts in the **home folder**, with
the Hub one level down. The builder named it when they cloned (`maria-hub`, `alex-hub` —
don't assume a fixed name like `hub-starter`); identify it by its signature, not its
name. Confirm first: run `ls`. See `CLAUDE.md` and `design/` side by side? You're in the
Hub. If not, find it: `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`, else
`find ~ -maxdepth 3 -path '*/design/dashboard.html'`. **`cd` into that folder and stay
there for the rest of the wrap-up**, and capture its absolute path with `pwd` so every
write below targets the full path (e.g. `/home/you/maria-hub/design/dashboard-data.js`).
Skipping this writes the dashboard and log to the home folder and runs `git` against the
wrong repo (or none). Can't find it? Ask the builder where they cloned their Hub before
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
- **Append the atom(s) to the run history** — the Hub's own `.bluerock/runs.json`
  (keep all atoms). Note this is the Hub-local `.bluerock/`, distinct from the home
  `~/.bluerock/` workspace facts read below.
- **Tally today's priorities.** Read `today.md` and count Focus items: `set` (total),
  `closed` (`[x]`), `carried` (`[>]`). Offer to check off anything I finished this
  session that's still `[ ]`. This feeds the dashboard's "priorities set vs. closed."
- **Roll up the sections and overwrite the dashboard data file** so my dashboard
  repaints — match the pinned contract exactly, all keys present:
  `window.__BR_DASH__ = { meta, productivity, cost, actions, guardrail, perf, brag, priorities, runs }`
  (write it to the starter's `design/dashboard-data.js`). The renderer just paints —
  roll the sections up here, don't make the browser re-aggregate.

Provenance is a trust claim. Beta has **no BlueRock sensor pipeline**, so the label
is **"From your sessions,"** never "sensor-sourced." Specifically:
- `guardrail` = `{ wired: false, events: [] }`.
- `cost` only if a pricing table is present (tokens × price); otherwise zeros / placeholder — never a fabricated number under a trust label.
- `meta` (builder, workspace, region) comes from the **workspace facts file** — the home `~/.bluerock/workspace.json` (Eng-provisioned, workspace-level; NOT the Hub's `.bluerock/`). Take `builder` / `workspace` / `region` from it; if it's absent, degrade honestly to a generic builder name. **No trial countdown.** The trial clock is not passed into the workspace and the dashboard is a value mirror, not a conversion surface — trial timing and upgrade prompts live in the email lifecycle and Console, not here. Never scrape boot time or file timestamps to fake a provision date (the container suspends/resumes, so those are wrong).
- `meta.outputsSince` is **singular "you," single user (not a team)**; `count` = outputs this week from `runs[]` (not a last-visit anchor); 0/unknown → greeting only, no fabricated number.
- `priorities` = `{ set, closed, carried }` for this week, counted from `today.md` (the closure loop). Derived "from your sessions," not sensors.
- `actions` = `{ total, byAgent: [{ name, count, tone, timeMin }] }` — agent actions this week from `runs[]`, grouped by `agent`. `name` = the agent's name (required — labels the bar), `count` = its action total, `tone` = a stable palette key (`coral`/`plum`/`composer`/`sage`) for the bar (omit → defaults to coral; reuse the same tone per agent across weeks), `timeMin` = wall-clock minutes for that agent this week (from `runs[].runTimeSec`, rolled up). For a multi-agent **team** (e.g. Account Research = researcher + signal-scanner + composer), emit one entry for the team plus `members: [{ name, count, timeMin }]` (members sum to the team's `count` and `timeMin`); use the same team label in `runs[]` so it reads consistently across the Actions card and section 04.
- `perf` = `{ successRate, runs:{successful,total}, avgSessionMin, avgSessionDeltaMin, outputsShipped }` — the honest set only. **No** output-quality/reader-rating and **no** cache-hit rate (dropped — no honest source / operator metric). `success` is your judgment (a run that completed without error or guardrail block); `avgSessionMin` from `session-metrics.py`; delta is neutral (shorter ≠ better).
- `resume` chapter comes from curriculum progress, not the transcript.

The source of truth for the shape + renderer is the builder's own design — the
data contract (`design/dashboard-data-contract.md`) and `dashboard.html`. Target
that contract; do not invent or restyle the dashboard.

**First, show me my numbers in the panel.** Before opening the visual dashboard, print a
short, plain readout of this session so the payoff lands even if the page doesn't open:
the runs this session and what each did, session length, priorities set / closed /
carried (from `today.md`), success rate, and cost only if a pricing table was present
(else "not tracked this session" — never a guessed number). A few honest lines, "from
your sessions." This always works, with no server or port involved.

**Then render my visual dashboard as a Claude Artifact.** The Hub runs in a remote,
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
- **No CTA buttons and no trial countdown.** This is a read-only value mirror — what my
  agents did, what shipped, what it cost. No "Upgrade," no "Start trial," no
  "days left." Conversion and trial timing live in the email lifecycle and Console,
  not here. A dead button in a sandboxed artifact is worse than no button.
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

Run `git status` and show me a plain summary: which files, new or changed, and a
proposed one-line commit message that says what the session accomplished (not
"updates"). **Wait for my go-ahead before committing.** "Wrap up" starts the
ritual; it is not yet permission to commit.

### 5. Commit and push (only after I confirm)

Once I confirm: stage the files, commit with the agreed message, push. If the
push fails (usually authentication), tell me plainly what happened and what to
click. Don't retry silently.

### 6. Hand me the continuation prompt

Last, print a short prompt I can paste into my next session:

```
I'm continuing work in my Hub.

Last session (YYYY-MM-DD): [one sentence: what got done]
Next up: [what to work on]

Read session-log.md for context.
```

That's the whole point of the ritual: the next session starts already knowing
what this one knew — and my dashboard already shows the work.

## Rules

- Never commit without my explicit go-ahead in this conversation.
- Never push anything that looks like a credential or a private key; flag it.
- If nothing changed this session, say so, still refresh the dashboard and log
  the session if I want the record, and skip the git steps.
