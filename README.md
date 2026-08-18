# BlueRock for AI Builders — Claude Code plugin

The BlueRock plugin marketplace for Claude Code. One plugin, `bluerock`: the run-as-is core
for your **agentic project**.

Say *"score Acme Corp"* and a two-agent team hands you a one-page account scorecard — Fit,
Timing, Reachability, why now, and the recommended next step. Say *"wrap up my session"* and
it logs what you did and refreshes your dashboard. Everything it produces is plain markdown
in your own repo.

## What's in it

- **Account Scorecard.** `/bluerock:scorecard <company>` runs `scout` → `scorer` and returns
  a one-page scorecard you can act on. This is the fast first win.
- **Your daily rhythm.** `/bluerock:onboard` learns who you are and how you write,
  `/bluerock:today` keeps your priorities, and `/bluerock:wrap-up` closes the day and
  refreshes your dashboard.
- **A readiness check.** `/bluerock:check` confirms your project is live and points you at
  what's next.

Plugin tools are written with their full name — `/bluerock:check`, `/bluerock:wrap-up` —
where the `/bluerock:` part says which toolkit they came from. You can also just say what you
want in plain language.

## Run as-is vs. make it yours

The plugin is the part you **run**. The part you **edit** ships seeded in your own project, in
`.claude/` — agents like `daily-brew`, `scribe`, and `meeting-prep`, and skills like
`/capture` and `/research`. Those are yours: change them in place, or write your own
alongside. Ask for them in plain language rather than as slash commands, and an agent in
your project named after a seeded one takes over from it.

`/bluerock:wrap-up` and `/bluerock:check` stay plugin-owned so your dashboard keeps working.

## Install

In the Claude Code panel, type `/plugins` (plural) to open the plugin manager. On the
**Marketplaces** tab, add `bluerock-io/claude-plugins`. On the **Plugins** tab, install
**bluerock** ("Install for you") and trust it. Then start a new chat — that is what loads
the plugin. Skip the banner's **Restart** button; it does not reliably load it.

Then say *"check my workspace"* (or run `/bluerock:check`) to confirm you're set. You'll want
a project to run it in — [the starter kit](https://github.com/bluerock-io/my-workspace) gives you one
in a click.

Already installed? Custom marketplaces don't auto-update — run `/plugins`, open
**Marketplaces**, and refresh `bluerock` to pick up a new release.

## Safe by default

Skills, commands, and agents only: no MCP servers, no hooks, nothing that executes code on
install. The agents use Claude Code's own tools (including `WebSearch` / `WebFetch` for
research); your files stay yours, your API calls go straight to Anthropic.

## Pairs with

The **BlueRock for AI Builders** starter kit and Learning Paths →
[builders.bluerock.io](https://builders.bluerock.io)

---

© 2026 BlueRock Security, Inc. All rights reserved. Licensed under the Apache License 2.0 —
see [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE). "BlueRock" and "BlueRock for AI Builders"
are trademarks of BlueRock Security, Inc.; the license grants no rights to the marks.
