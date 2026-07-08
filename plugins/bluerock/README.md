# BlueRock for Builders

Say *"wrap up my session"* and it runs. Say *"research Acme Corp"* and three agents hand
you a sourced dossier. This is the plugin behind
[BlueRock for Builders](https://builders.bluerock.io) — it turns Claude Code (inside
Cursor) into a set of skills and agents that do your real work and write it back as plain
markdown you own.

You drive it in plain language; the `/bluerock:` commands are there when you'd rather be
explicit. Everything runs inside your own repo — your **Hub** — so nothing is locked in an
app: the output is your files, and they're yours with or without the plugin.

> **New here?** The [BlueRock for Builders curriculum](https://builders.bluerock.io) sets
> up your Hub and walks you through everything below — start there.

## Install

In Claude Code (the panel inside Cursor):

```
/plugin marketplace add bluerock-io/claude-plugins
/plugin install bluerock@bluerock
```

Then run `/bluerock:check` to confirm you're set. You'll want a Hub to run it in — the
[starter template](https://github.com/bluerock-io/hub-starter) gives you one in a click.

## Account Research — point a team at a company

`/bluerock:research <company>` runs three agents in order and hands you a sourced dossier.
Each has one job:

- **`researcher`** — the company profile: what they do, their stage, size, and who's who.
- **`signal-scanner`** — recent, dated signals: a new VP of Sales posted last week, a $12M
  Series A this quarter, a product launch, a leadership move.
- **`composer`** — the dossier itself: overview, signals, and the strategic angles that
  matter to *you*, written in your voice.

The 20 minutes of digging before a call, in about 90 seconds. It's the first agent team in
the plugin; more come next.

## Your daily rhythm

The skills that run your day. Say what you want, or use the command:

- **`/bluerock:onboard`** — teaches your Hub who you are and how you write (writes your
  `CLAUDE.md`, `voice.md`, and `objectives.md`).
- **`/bluerock:capture`** + the **`scribe`** agent — drop a note any time; it gets filed.
- **`daily-brew`** agent — a morning brief that closes yesterday's loop and sets today's
  priorities.
- **`/bluerock:today`** — your living to-do for the day.
- **`meeting-prep`** + **`/bluerock:meeting-recap`** — a brief before a call, a follow-up
  email after.
- **`/bluerock:wrap-up`** — ends the session: logs what happened, refreshes your dashboard
  (a local page that shows what your agents did), and — with your okay — commits and pushes.

## Run them, then make them your own

The skills and agents work the moment you install. When you're ready to go further, you
build your own (the curriculum walks you through it):

- **Your own skills** live under `.claude/commands/` and run as your own commands (say,
  `/standup`).
- **Your own agents** live under `.claude/agents/`; name one after a plugin agent (like
  `daily-brew`) and yours takes over.
- A couple — `/bluerock:wrap-up` and `/bluerock:check` — you just run; they keep your
  dashboard correct for you.

Everything stays inside your own files — no servers, nothing reaching outside your repo
without you asking.
