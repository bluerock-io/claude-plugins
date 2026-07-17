# BlueRock for Builders — Claude Code plugin

The BlueRock plugin marketplace for Claude Code. One plugin, `bluerock`, with two things in it:

- **A daily operating rhythm.** `/onboard` learns who you are and how you write,
  `scribe` captures your day, `daily-brew` seeds a morning brief and priorities,
  `/today` keeps the list, `meeting-prep` and `/meeting-recap` bracket
  your meetings, and `/wrap-up` closes the loop and refreshes your build dashboard.
- **An Account Research agent team.** `/research <company>` runs researcher →
  signal-scanner → composer at a target and hands you a sourced dossier: overview, recent
  signals, and strategic angles in your voice.

You drive it in plain language ("wrap up my session") or with commands. Each tool has a full
name like `/bluerock:check` — you can drop the `/bluerock:` prefix and type the short form,
`/check`, as long as no other installed tool has the same name (right now none do); the full
`/bluerock:check` always works if a short one is ever taken.

## Install

In the Claude Code panel, type `/plugins` (plural) to open the plugin manager. On the
**Marketplaces** tab, add `bluerock-io/claude-plugins`. On the **Plugins** tab, install
**bluerock** ("Install for you"), trust it, and **Restart**.

Then try `/onboard` (or say "onboard me") to set up, or `/research <company>` for a dossier.

## Safe by default

Skills, commands, and agents only: no MCP servers, no hooks, nothing that executes code on
install. The agents use Claude Code's own tools (including `WebSearch` / `WebFetch` for
research); your files stay yours, your API calls go straight to Anthropic.

## Pairs with

The **BlueRock for Builders** starter project and curriculum →
[builders.bluerock.io](https://builders.bluerock.io)

---

© BlueRock
