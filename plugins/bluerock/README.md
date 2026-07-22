# BlueRock for Builders

Say *"wrap up my session"* and it runs. Say *"research Acme Corp"* and three agents hand
you a sourced dossier. This is the plugin behind
[BlueRock for Builders](https://builders.bluerock.io) — it turns Claude Code (inside
Cursor) into a set of skills and agents that do your real work and write it back as plain
markdown you own.

You drive it in plain language, or use the commands when you'd rather be explicit. Every tool
has a full name like `/bluerock:check` (the `/bluerock:` part just says which toolkit it came
from), and you can drop that prefix and type the short form, `/check`, as long as no other
installed tool has the same name — right now none do. If a short name ever gets crowded, the
full `/bluerock:check` always works. Everything runs inside your own repo, your **AI Work Hub**, so
nothing is locked in an app: the output is your files, and they're yours with or without the plugin.

> **New here?** The [BlueRock for Builders curriculum](https://builders.bluerock.io) sets
> up your Hub and walks you through everything below — start there.

## What's in the toolkit

Everything is organized by what it's *for* — not by whether it's a skill or an agent. Say what
you want; the right one runs.

| Category | What it's for |
|---|---|
| **Set up your Hub** | Get oriented, teach your Hub who you are, stay current: `onboard`, `check`, `whats-installed` |
| **Your daily rhythm** | The loop that runs your day: `daily-brew`, `today`, `capture`, `wrap-up` |
| **Meetings** | A brief before a call, a follow-up after: `meeting-prep`, `meeting-recap` |
| **Account research** | Point a three-agent team at a company for a sourced dossier: `research` |

Say *"what can I do"* (or run `/whats-installed`) anytime and it writes this same map,
grouped and up to date, into your Hub as `your-toolkit.md`. The set grows over time — new skills
and role-specific packs land here as they ship.

## Install

In the Claude Code panel, type `/plugins` (plural) to open the plugin manager. On the
**Marketplaces** tab, enter `bluerock-io/claude-plugins` and click **Add**. On the **Plugins**
tab, find **bluerock** under Available → **Install** → choose **"Install for you"** and trust it.
Click **Restart** when prompted.

Then say *"check my workspace"* (or run `/check`) to confirm you're set. You'll want a Hub to run it in — the
[the Starter](https://github.com/bluerock-io/hub-starter) gives you one in a click.

## Account Research — point a team at a company

`/research <company>` (or *"research Acme Corp"*) runs three agents in order and hands you a sourced dossier.
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

- **`/onboard`** — teaches your Hub who you are and how you write (writes your
  `CLAUDE.md`, `voice.md`, and `objectives.md`).
- **`/capture`** + the **`scribe`** agent — drop a note any time; it gets filed.
- **`daily-brew`** agent — a morning brief that closes yesterday's loop and sets today's
  priorities.
- **`/today`** — your living to-do for the day.
- **`meeting-prep`** + **`/meeting-recap`** — a brief before a call, a follow-up
  email after.
- **`/wrap-up`** — ends the session: logs what happened, refreshes your dashboard
  (a local page that shows what your agents did), and, with your okay, commits and pushes.
- **`/whats-installed`** — say "what can I do" and it writes a browsable
  `your-toolkit.md` into your Hub, listing every skill and agent you have.

## Run them, then make them your own

The skills and agents work the moment you install. When you're ready to go further, you
build your own (the curriculum walks you through it):

- **Your own skills** live under `.claude/commands/` and run as your own commands (say,
  `/standup`).
- **Your own agents** live under `.claude/agents/`; name one after a plugin agent (like
  `daily-brew`) and yours takes over.
- A couple, `/wrap-up` and `/check`, you just run; they keep your
  dashboard correct for you.

Everything stays inside your own files — no servers, nothing reaching outside your repo
without you asking.
