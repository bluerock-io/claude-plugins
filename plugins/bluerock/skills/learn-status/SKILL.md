---
name: learn-status
description: >-
  Where I am in the BlueRock for AI Builders curriculum, in plain language —
  sessions done, what I built, and what's next with its time. Read-only; run via
  /bluerock:learn-status.
disable-model-invocation: true
---

Render the builder's curriculum progress as a short, plain-language summary.
Read-only: this skill changes nothing, ever. If something needs fixing or
resuming, point at `/bluerock:learn` — don't do it here.

## Find the state

Progress lives in the builder's agentic project (the repo cloned from the
starter kit), at `learning/progress.json`. Find the project by its signature,
not its name: run `ls` and look for `CLAUDE.md` and `design/` side by side; if
not here, `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`, else
`find ~ -maxdepth 3 -path '*/design/dashboard.html'`. Use the absolute path.

Session titles and times come from
`${CLAUDE_PLUGIN_ROOT}/curriculum/manifest.json` — read it alongside so the
summary names sessions correctly.

## Report

A few honest lines, shaped like this:

```
**Your course so far: 2 of 8 sessions complete.**

Done: Session 1 (project set up and live) · Session 2 (account scorecard on Ramp)
Next: Session 3 — Anatomy of an agent, ~20 min

Say "continue the course" (or run /bluerock:learn) when you're ready.
```

- Count `complete` sessions; name each with its recorded `artifact` when one
  was captured, so progress reads as things built, not boxes ticked.
- If a session is `in_progress`, say where it stands ("Session 2, paused at
  step 3 of 5") and that "continue the course" resumes exactly there.
- Name the next session with its title and time from the manifest. If it runs
  on the web rather than in-session, include its link.
- Never inflate: report exactly what `progress.json` says, nothing rounder.

## Edge cases, handled plainly

- **No `learning/progress.json`:** they haven't started — say so warmly and
  point at `/bluerock:learn` to begin (Session 1 gets their project running).
- **No project found:** same answer — Session 1 is where the project comes
  from. Don't keep hunting past the bounded checks above.
- **Invalid JSON:** say the progress file looks hand-edited or damaged, show
  nothing invented, and point at `/bluerock:learn`, which can rebuild it from
  the journal and the project itself.
