# Changelog — `bluerock-examples` plugin

## 0.1.0 — Account Research
- **New:** the Account Research agent team. `/bluerock:research <company>` runs
  three agents in sequence — **researcher** (company profile), **signal-scanner**
  (recent signals), **composer** (the dossier) — and writes a sourced dossier to
  `my-work/account-research/<company>/<company>.md`: overview, recent signals, and
  strategic angles, in your voice.
- Reads `voice.md` + `objectives.md` (from `/bluerock:onboard`) so the angles and
  tone are yours.
- Public-web research via Claude Code's built-in `WebSearch` / `WebFetch` — no MCP
  servers, no hooks (safe-by-default). Cites sources; marks gaps instead of inventing.
- The first agent-example team; Insights Analyzer and Comparative Research come next.
