---
name: scorecard
description: >-
  Account Scorecard — point a small agent team at a company and get a fast,
  one-page scorecard (Fit, Timing, Reachability + a recommended next action). Use
  when I say "score <company>", "size up <company>", "should I go after
  <company>", "scorecard for <company>", or paste a company name and ask whether
  it's worth pursuing. Runs scout → scorer and writes the scorecard to
  my-work/account-scorecard/. Fast by design — the quick read, not a deep dossier.
---

Run the Account Scorecard team on a target company and produce the scorecard — a fast,
shareable one-pager. You orchestrate two agents; they do the work. This is the quick
read: keep it tight, aim for a couple of minutes, not a deep research run.

## First — anchor to the project

The scorecard, its working folder, and the `voice.md` / `objectives.md` the run reads
all live in the builder's project. Two generations exist: the project ships inside the workspace image (usually the folder
`my-workspace`); projects made before 2026-08 were cloned and carry whatever
name the builder chose. **Assume neither — identify it by its signature.** In an SSH/cloud
container the chat may start in the project itself or in the **home folder** with the
project one level down — both are normal. Identify it by signature, not name: run `ls`; see `CLAUDE.md` and `design/` side by
side? You're in the project. If not, find it: `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`,
else `find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` in, capture the
**absolute path** with `pwd`, and use that full path throughout. Can't find it? Ask the
builder which folder their project is in.

## Setup

1. **Get the target.** A company name (plus any hint — sector, region, domain — to
   disambiguate). If it's genuinely ambiguous, ask one question before spending the run.
2. **Make the working folder.** Slugify the name → `my-work/account-scorecard/<slug>/`.
   Create it. `my-work/` is builder-owned and never overwritten.

## Run the agents, in order

Dispatch these as ordinary subagents, one at a time, waiting for each. Do not use
agent-teams tooling; this runs identically in every client.

3. **Dispatch `scout`** with the company (+ hint) and the working folder. It writes a
   quick, sourced `scan.md` (what they do and what they sell, headquarters, employees,
   estimated revenue, stage, recent signal). It's bounded to a handful of fetches — let it
   be fast. Wait for it.
4. **Dispatch `scorer`** with the same folder. It reads `scan.md` (plus `voice.md` /
   `objectives.md` from the project root if present) and writes `scorecard.md`. Wait
   for it.

## Publish the artifact — you, not the agents

5. When `scorer` finishes, read `scorecard.md` and **publish it as a Claude Artifact**
   yourself, in this conversation, following the design contract below. The agents
   write markdown only — they have no artifact publishing; the finished, shareable
   view is yours to render. If artifact publishing isn't available in my environment,
   don't block — the markdown is saved; say so and give the path.

### The artifact — design contract (follow it exactly)

A single self-contained HTML page. **CSP-safe: inline ALL CSS in one `<style>` block, no
external requests — no CDN, no web fonts, no remote images, no scripts.** It is a static
page. Print-friendly, read-only, no CTAs or buttons.

**Layout** — one centered column, `max-width: 640px`, generous whitespace:
1. **Header** — company name (serif, ~30px, heading ink); a one-line **descriptor** beneath in
   muted ink (stage + what they do, e.g. `Series B · B2B analytics SaaS for GTM teams`, from
   the scan); then a subline in muted ink: `Account Scorecard · Scored <today's date> · <N>
   sources`.
2. **Facts row** — three equal columns directly beneath the header's hairline rule:
   `HQ`, `Employees`, `Est. revenue`. Label on top in small uppercase muted ink with
   letter-spacing; value below in body ink at the base size. **All three columns always
   render**, including when the scan found nothing: an unknown value reads `Not disclosed`
   in muted ink. Never drop a column — the row's shape is what makes it scannable, and a
   visible blank is the honest answer. Where the scan marked a figure `[estimated]`, append
   a small muted `est.` after the value rather than carrying the brackets through. CSS:
   `display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px;` plus
   `@media (max-width: 460px) { grid-template-columns: 1fr; }` so it stacks on a phone.
   Hairline border below.
3. **What they do** — a labeled block (`WHAT THEY DO`, the same small uppercase muted
   label): the two-or-three-sentence summary in body ink, then a `Lines of business:` line
   beneath it with the entries separated by ` · `. If the scan named one line of business,
   print the one; don't pad it out. Hairline border below.
4. **Three dimension rows**, stacked. Each row: a small rating-colored dot + the label
   (`Fit` / `Timing` / `Reachability`, small uppercase, letter-spacing), a **rating pill**
   (`High` / `Medium` / `Low`, color-coded per the palette), and the one-line rationale
   beneath in body ink. (When Fit uses the no-objectives default, render its one-line caveat
   here in muted ink.)
5. **Why now** — a highlighted callout: cream tint background, a 3px accent-blue left
   border, the one sentence in heading ink.
6. **Recommended next step** — its own block, labeled, the concrete step in body ink.
7. **Sources** — a small "Sources" label, then the scan's source domains as a wrapped row
   of small mono chips (cream fill, hairline border), so the `<N> sources` count is visible
   and clickable-looking. Keep to the domains the scout actually used.
8. **Footer** — small muted text: `Built with BlueRock · Account Scorecard · scout + scorer`.

**Palette** (Builders "cool-paper", light-only — use these hex values directly since the
Artifact can't read the app's CSS variables):
- Page background `#F5F1EA`; card surface `#FFFFFF`; card border `#E7E0D6`, radius `14px`.
- Cream (the "cream tint" / "cream fill" above): `#F5F1EA` — the page-background value
  reused as a tint on the white card.
- Ink: heading `#1B2130`, body `#3D4658`, muted `#7B8494`.
- Accent (BlueRock blue) `#1559C4`.
- Rating pills: **High** bg `#E4F0E9` / text `#2F6B4C`; **Medium** bg `#F7ECD6` / text
  `#8A5A12`; **Low** bg `#EDEEF1` / text `#5A6272`.

**Type** (CSP-safe fallbacks, no web fonts): headings `Georgia, 'Times New Roman', serif`;
body + labels `system-ui, -apple-system, sans-serif`. Labels/pills small and uppercase with
slight letter-spacing.

## Finish

6. The **scorecard artifact** is the payoff — a clean, one-page view (company header, the
   facts row and what they do, Fit / Timing / Reachability rated High/Med/Low with
   rationales, the "why now" line, and the recommended next action). The `scorecard.md` is the source of record the
   builder keeps and can push to their repo.
7. **Report:** the scorecard path, the headline verdict (the strongest dimension and the
   why-now line), and the artifact (or the fallback note). Don't reprint the whole thing.

## Why this is the fast one

The Account Scorecard is deliberately lighter than a full dossier: two agents, a bounded
scan, a one-page output. It's the "is this worth my time, and what do I do next" read.
For the deep, multi-section dossier, that's the Account Research team (`researcher →
signal-scanner → composer`) the builder has in their own project.

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`skills/learn-meet-your-first-agent-team/SKILL.md` narrates this skill as its sales
  and operations lane**: its lane table and steps name the agents (`scout` → `scorer`),
  the folder (`my-work/account-scorecard/<company>/`), and the three dimensions (Fit,
  Timing, Reachability). Renaming any of them here strands that session's narration.
- **`agents/scout.md` owns `scan.md`'s fixed section shape** and `agents/scorer.md` reads
  it by section; this skill's artifact contract renders `scorecard.md`'s order. The
  three-outcome honesty rule on revenue and headcount (stated / `[estimated]` / `Not
  disclosed`) is stated in all three places — keep the wording in step.
- **`curriculum/manifest.json`** carries this skill's `one_liner` and **README.md
  § Account Scorecard** quotes the flow; the menu and the site read both.
