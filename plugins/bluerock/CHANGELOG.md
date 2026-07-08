# Changelog — `bluerock` plugin

## 0.4.1 — run correctly at user scope (Hub anchoring)
- **Fixed:** the plugin installs at user scope (`~/.claude`), so its skills load from *any* folder — but in the cloud workspace the Hub is a subfolder of the container, so a skill firing from the wrong folder used to scatter files (profile, notes, dashboard data) outside the Hub, silently. Every file-touching skill (`onboard`, `today`, `capture`, `meeting-recap`, `research`, `wrap-up`) now anchors to the Hub first: it identifies the Hub by its signature (`CLAUDE.md` + `design/` together, not a fixed folder name), finds it a level down or via `find` when the session started in the home folder (the common SSH/cloud case), resolves its **absolute path** at runtime, and writes to that full path — so nothing leaks into the container home even when Claude Code is launched from outside the Hub.
- **`/bluerock:check`** now *fixes* a wrong-folder situation instead of only flagging it — it walks the builder back into their Hub (`cd`, or reopen the folder) and asks them to re-run.
- **`/bluerock:onboard`** fills `CLAUDE.md` in place and preserves the rest (the session-start greeting block), rather than overwriting the whole file.
- **Clarified** the two `.bluerock/` locations in `wrap-up`: the home `~/.bluerock/workspace.json` (Eng-provisioned facts) vs the Hub's own `.bluerock/runs.json` (run history).
- Docs: install URLs point at `bluerock-io/claude-plugins` and `bluerock-io/hub-starter`. Still skills/commands/agents only — no MCP, no hooks.

## 0.4.0 — agent-example teams (Account Research)
- **New:** the **Account Research** agent team, folded into this plugin (was the separate `bluerock-examples` plugin). `/bluerock:research <company>` runs three agents in sequence — **researcher** (company profile), **signal-scanner** (recent, dated signals), **composer** (the dossier) — and writes a sourced dossier to `my-work/account-research/<company>/<company>.md`: overview, recent signals, and strategic angles, in your voice.
- Reads `voice.md` + `objectives.md` (from `/bluerock:onboard`) so the angles and tone are yours. Public-web research via Claude Code's built-in `WebSearch` / `WebFetch` — no MCP, no hooks. Cites sources; marks gaps instead of inventing.
- **Consolidation:** one `bluerock` plugin now ships the daily rhythm **and** the agent-example teams, so every command is uniformly `/bluerock:<verb>` (incl. `/bluerock:research`). The first example team; Insights Analyzer and Comparative Research come next.

## 0.3.0 — priming (get to know your Hub)
- **New:** `/bluerock:onboard` — the get-to-know-you. Paste what ChatGPT/Claude already knows about you (via the portability prompt) plus a couple of writing samples; it interviews for gaps and writes three builder-owned files: `CLAUDE.md` (who you are + how to help), `voice.md` (how you write), and `objectives.md` (what you're working on — which `daily-brew` reads to rank your focus).
- **Why:** knowing the builder well is the highest-leverage, most-compounding setup step — every downstream skill produces output that's actually yours. The voice guide is the entry carrot.
- Paste-back, self-distill (one skill writes all three files). Single `voice.md` at beta; multi-profile reserved as a later add. Still skills/commands/agents only — no MCP, no hooks.

## 0.2.0 — the daily operating rhythm
- **New:** `/bluerock:today` (living priorities in `today.md`), `/bluerock:capture` (fast intake), and the `meeting-prep` agent (before-a-meeting brief; the before to `meeting-recap`'s after).
- **Renamed:** `follow-up-email` → `meeting-recap` (it's a recap you send; broad triggers kept).
- **Changed:** `daily-brew` now seeds `today.md` and opens by closing yesterday's loop (gained Write/Edit tools). `scribe` reframed from "end-of-day" to continuous capture. `wrap-up` tallies `today.md` (set/closed/carried) into the dashboard `priorities` block.
- **Meta from provisioning:** `wrap-up` + `daily-brew` read `.bluerock/workspace.json` (`provisioned_at` → trial countdown, plus builder / workspace / region), with an honest fallback when absent (neutral "Trial," generic name — never scrape boot/file timestamps). Provisioning contract: `bfb-workspace-facts-spec.md`.
- Motion: capture → brew → today → recap/prep → wrap. Still skills/commands/agents only (no MCP, no hooks). Dashboard `priorities` panel ships in try-bluerock (separate PR).

## 0.1.0 — initial set
- **Agents:** `daily-brew` (start-of-day brief from yesterday's notes), `scribe` (end-of-day note filer). They pair as a loop; in the curriculum the builder learns to build their own, which auto-overrides these.
- **Skills:** `/bluerock:wrap-up` (session log + build-dashboard refresh + optional commit/push + continuation prompt), `/bluerock:check` (read-only readiness check), `/bluerock:follow-up-email` (draft a follow-up from call notes).
- Skills/commands/agents only — no MCP servers, no hooks (safe-by-default install).
