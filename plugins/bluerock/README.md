# BlueRock for Builders

Say *"score Acme Corp"* and a two-agent team hands you a one-page account scorecard. Say
*"wrap up my session"* and it logs your work and refreshes your dashboard. This is the
plugin behind [BlueRock for Builders](https://builders.bluerock.io) — the run-as-is core
that turns Claude Code (inside Cursor) into tools that do your real work and write it back
as plain markdown you own.

You drive it in plain language, or use the commands when you'd rather be explicit. Every
tool has a full name like `/bluerock:check` (the `/bluerock:` part just says which toolkit
it came from), and you can drop the prefix and type the short form, `/check`, as long as no
other installed tool has the same name. Everything runs inside your own repo, your **AI Work
Hub**, so nothing is locked in an app: the output is your files, yours with or without the
plugin.

> **New here?** The [BlueRock for Builders curriculum](https://builders.bluerock.io) sets
> up your Hub and walks you through everything below — start there.

## What the plugin gives you

The **run-as-is core** — you drive these; you don't edit them:

| Category | What it's for |
|---|---|
| **Set up** | Get to know you, confirm you're ready: `onboard`, `check` |
| **Your daily rhythm** | Today's priorities and the end-of-session wrap: `today`, `wrap-up` |
| **Account Scorecard** | Point a fast team at a company for a one-page scorecard: `scorecard` (agents `scout` + `scorer`) |

## Account Scorecard — the fast first win

`/scorecard <company>` (or *"score Acme Corp"*) runs two agents and hands you a one-page
scorecard:

- **`scout`** — a quick, sourced scan: what they do, size and stage, one or two recent signals.
- **`scorer`** — grades **Fit / Timing / Reachability**, calls the "why now," and recommends a
  concrete next action, in your voice and against your objectives.

Seconds, not a deep dig — the "is this worth my time, and what do I do next" read. For the
deep, multi-section dossier, that's the **Account Research team** seeded in your Hub (below).

## Your Hub comes with more — and they're yours

Your Hub (from [the Starter](https://github.com/bluerock-io/hub-starter)) ships seeded
agents and skills in `.claude/` that you can open, run, **edit**, and build on:

- **Agents** (`.claude/agents/`) — `daily-brew` (a morning brief that closes yesterday's
  loop and sets today's), `scribe` (files a note any time), `meeting-prep` (a brief before
  a call), plus the **Account Research team** `researcher` / `signal-scanner` / `composer`
  for a deep dossier.
- **Skills** (`.claude/skills/`) — `meeting-recap` (a follow-up after a call), `capture`
  (drop a note), and `research` (point the research team at a company for the full dossier).

These are yours from day one: edit any of them, or build your own alongside. The curriculum
walks you through it.

## Install

In the Claude Code panel, type `/plugins` (plural) to open the plugin manager. On the
**Marketplaces** tab, enter `bluerock-io/claude-plugins` and click **Add**. On the
**Plugins** tab, find **bluerock** under Available → **Install** → choose **"Install for
you"** and trust it. Click **Restart** when prompted.

Then say *"check my workspace"* (or run `/check`) to confirm you're set. You'll want a Hub to
run it in — [the Starter](https://github.com/bluerock-io/hub-starter) gives you one in a click.

## Run as-is vs. make it yours

- The plugin's core (`onboard`, `today`, `wrap-up`, `check`, `scorecard`) you run as-is.
  `/wrap-up` and `/check` especially stay plugin-owned so they keep your dashboard correct.
- Everything in your Hub's `.claude/` is yours: edit it in place, or build your own
  alongside. Name a skill of your own (`/standup`) and it just works; name an agent after a
  seeded one and yours takes over.

Everything stays inside your own files — no servers, nothing reaching outside your repo
without you asking.
