# Changelog — `bluerock` plugin

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
