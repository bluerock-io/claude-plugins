# bluerock-examples — agent-example teams

> Review copy of the second BlueRock for Builders plugin: agent-example **teams**
> that show off what multi-agent work looks like, distinct from the daily rhythm
> in the `bluerock` plugin. Lives in the same `bluerock` marketplace.

## Install

```
/plugin marketplace add bluerock-io/claude-plugins
/plugin install bluerock-examples@bluerock
```

(The rhythm plugin is `bluerock@bluerock`; install both for the full set. The beta
workspace pre-installs both.)

## What's here

```
plugins/bluerock-examples/
├── .claude-plugin/plugin.json   # name: bluerock-examples, version 0.1.0
├── CHANGELOG.md
├── agents/
│   ├── researcher.md            # company profile — what they do, stage, size, who's who
│   ├── signal-scanner.md        # recent signals — hiring, funding, launches, moves (sourced)
│   └── composer.md              # the dossier — synthesis + strategic angles, in your voice
└── skills/
    └── research/SKILL.md        # /bluerock:research <company> — runs the team, writes the dossier
```

## Account Research — the first team

`/bluerock:research <company>` orchestrates the three agents:

```
researcher      → my-work/account-research/<slug>/profile.md   (who they are)
signal-scanner  → my-work/account-research/<slug>/signals.md    (what's new)
composer        → my-work/account-research/<slug>/<slug>.md     (the dossier you share)
```

The **dossier** is the artifact: company overview → recent signals → strategic angles
with fit scores, tuned to your `objectives.md` and written in your `voice.md`. It's a
high-value deliverable for marketing, sales, founders, and job-seekers.

## Honest scope (beta)

- **Public-web research** via Claude Code's built-in `WebSearch` / `WebFetch` — not a
  paid data API. The agents **cite their sources** and **mark gaps** rather than invent.
- **Agents only — no MCP servers, no hooks** (safe-by-default, consistent with the
  `bluerock` plugin's D2 rule).
- Outputs land in `my-work/` (builder-owned, never overwritten).
