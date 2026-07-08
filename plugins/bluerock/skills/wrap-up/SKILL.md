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
- **Append the atom(s) to the run history** (keep all atoms, e.g. `.bluerock/runs.json`).
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
- `meta` (builder, workspace, region, trial) comes from the **workspace facts file** — read `~/.bluerock/workspace.json` (or `./.bluerock/workspace.json`). Compute `meta.trialDaysLeft = trial_days − (today − provisioned_at)`; take `builder` / `workspace` / `region` from the same file. **If the file is absent, degrade honestly:** omit the trial countdown (neutral "Trial," no number), generic builder name — never scrape boot time or file timestamps for the provision date (the container suspends/resumes, so those are wrong).
- `meta.outputsSince` is **singular "you," single user (not a team)**; `count` = outputs this week from `runs[]` (not a last-visit anchor); 0/unknown → greeting only, no fabricated number.
- `priorities` = `{ set, closed, carried }` for this week, counted from `today.md` (the closure loop). Derived "from your sessions," not sensors.
- `actions` = `{ total, byAgent: [{ name, count, tone, timeMin }] }` — agent actions this week from `runs[]`, grouped by `agent`. `name` = the agent's name (required — labels the bar), `count` = its action total, `tone` = a stable palette key (`coral`/`plum`/`composer`/`sage`) for the bar (omit → defaults to coral; reuse the same tone per agent across weeks), `timeMin` = wall-clock minutes for that agent this week (from `runs[].runTimeSec`, rolled up). For a multi-agent **team** (e.g. Account Research = researcher + signal-scanner + composer), emit one entry for the team plus `members: [{ name, count, timeMin }]` (members sum to the team's `count` and `timeMin`); use the same team label in `runs[]` so it reads consistently across the Actions card and section 04.
- `perf` = `{ successRate, runs:{successful,total}, avgSessionMin, avgSessionDeltaMin, outputsShipped }` — the honest set only. **No** output-quality/reader-rating and **no** cache-hit rate (dropped — no honest source / operator metric). `success` is your judgment (a run that completed without error or guardrail block); `avgSessionMin` from `session-metrics.py`; delta is neutral (shorter ≠ better).
- `resume` chapter comes from curriculum progress, not the transcript.

The source of truth for the shape + renderer is the builder's own design — the
data contract (`design/dashboard-data-contract.md`) and `dashboard.html`. Target
that contract; do not invent or restyle the dashboard.

**Then open it for me — one step, no fuss.** The Hub runs in a cloud workspace, so
`file://` won't render `design/dashboard.html` (the file is on the container, not my
machine). Serve it and hand me a link instead. Do this now, and any time I say
**"open my dashboard"**:

```bash
(cd design && nohup python3 -m http.server 8137 >/tmp/br-dashboard.log 2>&1 &) ; echo "Dashboard → http://localhost:8137/dashboard.html"
```

Cursor auto-forwards the port — tell me to click the link (or the "port forwarded"
popup) and my dashboard opens in my browser. Works the same if I'm ever fully local.
If port 8137 is busy, pick another and tell me the URL. To stop it later:
`lsof -ti:8137 | xargs kill`.

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
