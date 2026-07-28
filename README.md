# BlueRock for Builders — Claude Code plugin

The BlueRock plugin marketplace for Claude Code. One plugin, `bluerock`: the run-as-is core
for your **AI Work Hub**.

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
- **A readiness check.** `/bluerock:check` confirms your Hub is live and points you at
  what's next.

Plugin tools are written with their full name — `/bluerock:check`, `/bluerock:wrap-up` —
where the `/bluerock:` part says which toolkit they came from. You can also just say what you
want in plain language.

## Run as-is vs. make it yours

The plugin is the part you **run**. The part you **edit** ships seeded in your own Hub, in
`.claude/` — agents like `daily-brew`, `scribe`, and `meeting-prep`, and skills like
`/capture` and `/research`. Those are yours: change them in place, or write your own
alongside. Hub skills and agents stay bare (no `/bluerock:` prefix), and a Hub agent named
after a seeded one takes over from it.

`/bluerock:wrap-up` and `/bluerock:check` stay plugin-owned so your dashboard keeps working.

## Install

In the Claude Code panel, type `/plugins` (plural) to open the plugin manager. On the
**Marketplaces** tab, add `bluerock-io/claude-plugins`. On the **Plugins** tab, install
**bluerock** ("Install for you"), trust it, and **Restart**.

Then say *"check my workspace"* (or run `/bluerock:check`) to confirm you're set. You'll want
a Hub to run it in — [the Starter](https://github.com/bluerock-io/hub-starter) gives you one
in a click.

Already installed? Custom marketplaces don't auto-update — run `/plugins`, open
**Marketplaces**, and refresh `bluerock` to pick up a new release.

## Safe by default

Skills, commands, and agents only: no MCP servers, no hooks, nothing that executes code on
install. The agents use Claude Code's own tools (including `WebSearch` / `WebFetch` for
research); your files stay yours, your API calls go straight to Anthropic.

## Pairs with

The **BlueRock for Builders** starter project and curriculum →
[builders.bluerock.io](https://builders.bluerock.io)

---

© BlueRock
