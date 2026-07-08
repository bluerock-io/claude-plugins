# BlueRock for Builders — Claude Code plugin

The BlueRock plugin marketplace for Claude Code. One plugin, `bluerock`, with two things in it:

- **A daily operating rhythm.** `/bluerock:onboard` learns who you are and how you write,
  `scribe` captures your day, `daily-brew` seeds a morning brief and priorities,
  `/bluerock:today` keeps the list, `meeting-prep` and `/bluerock:meeting-recap` bracket
  your meetings, and `/bluerock:wrap-up` closes the loop and refreshes your build dashboard.
- **An Account Research agent team.** `/bluerock:research <company>` runs researcher →
  signal-scanner → composer at a target and hands you a sourced dossier: overview, recent
  signals, and strategic angles in your voice.

## Install

```
/plugin marketplace add bluerock-io/claude-plugins
/plugin install bluerock@bluerock
```

Then try `/bluerock:onboard` to set up, or `/bluerock:research <company>` for a dossier.

## Safe by default

Skills, commands, and agents only: no MCP servers, no hooks, nothing that executes code on
install. The agents use Claude Code's own tools (including `WebSearch` / `WebFetch` for
research); your files stay yours, your API calls go straight to Anthropic.

## Pairs with

The **BlueRock for Builders** starter project and curriculum →
[builders.bluerock.io](https://builders.bluerock.io)

---

© BlueRock
