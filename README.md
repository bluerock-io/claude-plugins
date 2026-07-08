# BlueRock for Builders — Claude Code plugins

The BlueRock plugin marketplace for Claude Code. Two plugins:

- **`bluerock`** — a daily operating rhythm: `/onboard` learns who you are and how
  you write, `scribe` captures your day, `daily-brew` seeds a morning brief +
  priorities, `/today` keeps the list, `meeting-prep` + `meeting-recap` bracket your
  meetings, and `/wrap-up` closes the loop and refreshes your build dashboard.
- **`bluerock-examples`** — agent-example teams. **Account Research**: point an agent
  team at a target company and get a sourced dossier — overview, recent signals, and
  strategic angles in your voice — with `/bluerock:research <company>`.

## Install

```
/plugin marketplace add bluerock-io/claude-plugins
/plugin install bluerock@bluerock
/plugin install bluerock-examples@bluerock
```

Then try `/bluerock:onboard` to set up, or `/bluerock:research <company>` for a dossier.

## Safe by default

Skills, commands, and agents only — **no MCP servers, no hooks, nothing that
executes code on install**. The agents use Claude Code's own tools (including
`WebSearch` / `WebFetch` for research); your files stay yours, your API calls go
straight to Anthropic.

## Pairs with

The **BlueRock for Builders** starter project and curriculum →
[builders.bluerock.io](https://builders.bluerock.io)

---

© BlueRock
