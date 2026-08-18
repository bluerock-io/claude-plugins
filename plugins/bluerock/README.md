# BlueRock for AI Builders

Say *"score Acme Corp"* and a two-agent team hands you a one-page account scorecard. Say
*"wrap up my session"* and it logs your work and refreshes your dashboard. This is the
plugin behind [BlueRock for AI Builders](https://builders.bluerock.io) — the run-as-is core
that turns Claude Code (inside Cursor or VS Code) into tools that do your real work and write it back
as plain markdown you own.

You drive it in plain language, or use the commands when you'd rather be explicit. Plugin
tools are written with their full name — `/bluerock:check`, `/bluerock:wrap-up` — where the
`/bluerock:` part says which toolkit they came from. The skills and agents seeded in your own
project live in that project's `.claude/` folders; `/bluerock:check` can link them for new chats while
the files stay in your repo. Everything runs inside your own repo, your **agentic project**
(older docs call the same repo your AI Work Hub — same thing), so
nothing is locked in an app: the output is your files, yours with or without the plugin.

> **New here?** The [BlueRock for AI Builders learning path](https://builders.bluerock.io) sets
> up your project and walks you through everything below — start there.

## What the plugin gives you

The **run-as-is core** — you drive these; you don't edit them:

| Category | What it's for |
|---|---|
| **Set up** | Get to know you, confirm you're ready: `/bluerock:onboard`, `/bluerock:check` |
| **When you're stuck** | One diagnosis, one next step: `/bluerock:help` |
| **Your daily rhythm** | Today's priorities and the end-of-session wrap: `/bluerock:today`, `/bluerock:wrap-up` |
| **Account Scorecard** | Point a fast team at a company for a one-page scorecard: `/bluerock:scorecard` (agents `scout` + `scorer`) |
| **Messaging Doc** | Point a fast team at your website for your core messaging doc: `/bluerock:messaging-doc` (agents `site-reader` + `distiller`) |

## Account Scorecard — the fast first win

`/bluerock:scorecard <company>` (or *"score Acme Corp"*) runs two agents and hands you a one-page
scorecard:

- **`scout`** — a quick, sourced scan: what they do, size and stage, one or two recent signals.
- **`scorer`** — grades **Fit / Timing / Reachability**, calls the "why now," and recommends a
  concrete next action, in your voice and against your objectives.

Seconds, not a deep dig — the "is this worth my time, and what do I do next" read. For the
deep, multi-section dossier, that's the **Account Research team** seeded in your project (below).

## Messaging Doc — the marketing first win

`/bluerock:messaging-doc <your site>` (or *"build my messaging doc"*) runs two agents and hands
you your **core messaging doc** — positioning, voice, and the phrases your brand actually uses:

- **`site-reader`** — reads your homepage and the pages that carry the messaging, capturing
  exactly what the site says: quoted, sourced, never paraphrased.
- **`distiller`** — turns that (plus anything you paste in: a recent post, campaign copy) into
  the one-page doc, with honest gaps named.

One website address plus whatever you paste — no exports, no logins. The doc saves in your project
and becomes the baseline every later draft leans on.

## Your project comes with more — and they're yours

Your project (from [the starter kit](https://github.com/bluerock-io/my-workspace)) ships seeded
agents and skills in `.claude/` that you can open, run, **edit**, and build on:

- **Agents** (`.claude/agents/`) — `daily-brew` (a morning brief that closes yesterday's
  loop and sets today's), `scribe` (files a note any time), `meeting-prep` (a brief before
  a call), plus the **Account Research team** `researcher` / `signal-scanner` / `composer`
  for a deep dossier.
- **Skills** (`.claude/skills/`) — `meeting-recap` (a follow-up after a call), `capture`
  (drop a note), and `research` (point the research team at a company for the full dossier).

These are yours from day one: edit any of them, or build your own alongside. The learning path
walks you through it.

## Install

In the Claude Code panel, type `/plugins` (plural) to open the plugin manager. On the
**Marketplaces** tab, enter `bluerock-io/claude-plugins` and click **Add**. On the
**Plugins** tab, find **bluerock** under Available → **Install** → choose **"Install for
you"** and trust it. Then start a new chat — that is what loads the plugin. Skip the
banner's **Restart** button; it does not reliably load it.

Then say *"check my workspace"* (or run `/bluerock:check`) to confirm you're set. You'll want a project to
run it in — [the starter kit](https://github.com/bluerock-io/my-workspace) gives you one in a click.

## Run as-is vs. make it yours

- The plugin's core (`/bluerock:onboard`, `/bluerock:today`, `/bluerock:wrap-up`,
  `/bluerock:check`, `/bluerock:scorecard`) you run as-is.
  `/bluerock:wrap-up` and `/bluerock:check` especially stay plugin-owned so they keep your
  dashboard correct.
- Everything in your project's `.claude/` is yours: edit it in place, or build your own
  alongside. Name a skill of your own (`/standup`) and it just works; name an agent after a
  seeded one and yours takes over.

Everything stays inside your own files — no servers, nothing reaching outside your repo
without you asking.
