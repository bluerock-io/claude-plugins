---
name: competitive-intel
description: >-
  Competitive Intel — point an agent team at the competitors you face and get a
  battlecard per competitor: sourced kill points, your differentiators aimed, where
  they're genuinely better, their likely attack and the answer, and one question to
  ask. Use when I say "battlecard for <competitor>", "competitive intel on <A> and
  <B>", "who are we up against", "prep me for a competitive deal", or name
  competitors before a meeting. Runs competitor-scanner (once per competitor, up to
  4) → analyst, and writes to my-work/competitive-intel/. Research-grade on purpose
  — minutes, not seconds.
---

Run the Competitive Intel team and produce **battlecards** — one card per competitor,
ready for the room. You orchestrate the agents; they do the work. This is the deep read
of the pair: the Account Scorecard is seconds on one account, this is minutes across up
to four competitors, because the answers that survive a deal live in docs and pricing
pages, not homepages.

**What it replaces:** building or refreshing battlecards by hand — the research, the
comparison, and the meeting prep.
**Time saved:** [PLACEHOLDER — DO NOT MERGE: fill from the timed manual baseline
(E6-26), with its provenance, e.g. "about N minutes, timed once by one person". Never a
bare "saves an hour".]

## First — anchor to the project

The battlecards, their working folder, and the `voice.md` / `objectives.md` the run reads
all live in the builder's project. Two generations exist: the project ships inside the workspace image (usually the folder
`my-workspace`); projects made before 2026-08 were cloned and carry whatever
name the builder chose. **Assume neither — identify it by its signature.** In an SSH/cloud
container the chat may start in the project itself or in the **home folder** with the
project one level down — both are normal. Identify it by signature, not name: run `ls`; see `CLAUDE.md` and `design/` side by
side? You're in the project. If not, find it: `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`,
else `find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` in, capture the
**absolute path** with `pwd`, and use that full path throughout. Can't find it? Ask the
builder which folder their project is in.

## Before the questions — read what the builder already has

Check, without asking: `objectives.md` and `voice.md` at the project root, and the latest
doc under `my-work/messaging-doc/` if one exists. These sharpen the run — they are never
required for it.

- **If they're real**, use them to pre-fill the intake below (propose, confirm, don't
  re-ask cold).
- **If they're placeholder templates or absent**, say so once, plainly, and keep moving:
  *"Your `objectives.md` / `voice.md` are still the placeholder templates, so I can't tune
  these cards to your voice or goals yet. Happy to run anyway — running
  `/bluerock:onboard` would sharpen future runs."* Never make setup homework the price of
  the first battlecard.
- **If the builder has their own positioning or SWOT doc**, they can name or paste it at
  any step — it feeds the same slot as the differentiators.

## Intake — one question per step, short, then confirm

Ask these one at a time. Keep each ask to a line or two; don't stack questions or explain
the whole flow up front.

1. **Industry / market context.** "What category are we competing in?"
2. **Competitors.** "Who are we up against? Names are enough — add a domain for anything
   with a common name (cap is 4 per run)."
3. **Your differentiators.** "What do you win on? Two or three bullets in your own words."
   (Pre-fill from the messaging doc or objectives when they exist and confirm instead.)
4. **Personas.** "Who are these cards for — who's in the room or in the deal?"
5. **Other notes.** "Anything else that should shape these? A deal that's stuck, pricing
   pressure, a loss you want to understand, a compliance constraint, a claim we're not
   allowed to make, a phrase to avoid. Optional — say 'nothing' if there isn't anything."
6. **Confirm before we run.** Play back industry, competitors, differentiators, personas,
   and notes as a short bullet list, then: "Good to go, or anything to edit?"

## Set up the run

7. **Make the working folder:** `my-work/competitive-intel/<YYYY-MM-DD>-<slug>/`, where
   the slug names the deal or the lead competitor. Dated on purpose — runs accumulate and
   are never overwritten; the history is what makes "what changed" possible later.
   `my-work/` is builder-owned and never overwritten.
8. **Check for a previous run:** list `my-work/competitive-intel/`. If a prior dated
   folder holds a `battlecard.md`, note its path and date — the analyst will report what
   changed since it.
9. **Write `inputs.md`** into the working folder: the confirmed intake (industry,
   competitors, differentiators, personas, notes) and which project files were real
   enough to read. This is the record of what shaped the cards, and the seed the next
   run pre-fills from.

## Run the agents, in order

Dispatch these as ordinary subagents, one at a time, waiting for each. Do not use
agent-teams tooling; this runs identically in every client.

10. **Dispatch `competitor-scanner` once per competitor**, each with: the competitor
    (name + domain if given), the industry, and the working folder's absolute path. Each
    writes a sourced `scan-<competitor-slug>.md`, docs-deep and bounded to 6 to 8 fetches.
    Wait for each before dispatching the next, and tell the builder which competitor is
    being scanned as you go — four scans take a few minutes and silence reads as a hang.
11. **Dispatch `analyst`** with the working folder path and, when step 8 found one, the
    previous `battlecard.md` path. It reads `inputs.md` and every scan — **no web tools,
    no new research** — and writes `battlecard.md`: one card per competitor, plus what
    changed since the previous run.

## Publish the artifact — you, not the agents

12. When `analyst` finishes, read `battlecard.md` and **publish it as a Claude Artifact**
    yourself, in this conversation, following the design contract below. The agents write
    markdown only; the finished, shareable view is yours to render. If artifact publishing
    isn't available in my environment, don't block — the markdown is saved; say so and
    give the path.

### The artifact — design contract (follow it exactly)

A single self-contained HTML page. **CSP-safe: inline ALL CSS in one `<style>` block, no
external requests — no CDN, no web fonts, no remote images, no scripts.** It is a static
page. Print-friendly, read-only, no CTAs or buttons.

**Layout** — one centered column, `max-width: 720px`, generous whitespace:

1. **Header** — the industry (serif, ~30px, heading ink); beneath it in muted ink:
   `Competitive Intel · Battlecards · <today's date> · <N> competitors · <M> sources`;
   then a `For:` line naming the personas. Hairline rule below.
2. **A competitor strip** — the competitor names as a wrapped row of small chips (cream
   fill, hairline border), doubling as a table of contents for the stacked cards.
3. **"Since your last run" strip** — only when a previous run existed: a cream-tint
   callout with a 3px accent-blue left border, dated, listing the analyst's "Since" items
   (or its "no material change" line). Omit the block entirely on a first run.
4. **One card per competitor**, stacked, each a white card (hairline border, radius 14px)
   carrying the analyst's sections in order: **The 30-second read** (with the scope note
   in muted ink) · **Kill points** (each with its small source chip; section subtitle in
   muted ink: `Sourced. Use in the room.`) · **Silver bullets** (subtitle: `Your
   differentiators, aimed.` — or the honest one-liner when differentiators were missing)
   · **Where they're genuinely better** (subtitle: `Don't take the fight here.`) ·
   **Their attack on us** (each attack line followed by its answer in body ink) ·
   **Head to head** (a two-column them/ours table, hairline row rules) · **One question
   to ask** (cream-tint callout, the question in heading ink). Section labels small,
   uppercase, muted, letter-spaced. Carry every `[their claim]` / `[unverified]` marker
   as a small muted superscript tag — never silently drop one.
5. **Sources** — a small "Sources" label, then the scans' source domains as a wrapped row
   of small mono chips. Keep to the domains the scanners actually used.
6. **Footer** — small muted text: `Built with BlueRock · Competitive Intel ·
   competitor-scanner + analyst`.

**Palette** (Builders "cool-paper", light-only — use these hex values directly since the
Artifact can't read the app's CSS variables):
- Page background `#F5F1EA`; card surface `#FFFFFF`; card border `#E7E0D6`, radius `14px`.
- Cream (the "cream tint" / "cream fill" above): `#F5F1EA` — the page-background value
  reused as a tint on the white card.
- Ink: heading `#1B2130`, body `#3D4658`, muted `#7B8494`.
- Accent (BlueRock blue) `#1559C4`.

**Type** (CSP-safe fallbacks, no web fonts): headings `Georgia, 'Times New Roman', serif`;
body + labels `system-ui, -apple-system, sans-serif`. Labels small and uppercase with
slight letter-spacing.

## Finish

13. The **battlecard artifact** is the payoff. The `battlecard.md` is the source of record
    the builder keeps and can push to their repo, and `inputs.md` beside it is what the
    next run pre-fills from.
14. **Report:** the folder path, the one line that matters (the sharpest sourced kill
    point, or the biggest "don't take the fight here" warning), and the artifact (or the
    fallback note). Don't reprint the cards.
15. **Offer the depth, after the run — never before it.** One beat, two doors, then stop:
    *"Want to see how this worked? Two agents ran it — a scanner that read their docs and
    an analyst that aimed your differentiators. The anatomy-of-an-agent and subagent-teams
    sessions explain the pattern — say 'teach me how this works'. And if you want future
    cards tuned to your own positioning, run `/bluerock:messaging-doc` on your site — the
    silver bullets aim themselves from it."*

## Honesty rules this skill carries

- **Sourced versus supplied never blur.** Kill points trace to scans and carry sources;
  silver bullets are the builder's own claims, aimed but labeled ours. The analyst
  enforces it; the artifact preserves it.
- **A thin competitor gets an honest short card**, not a padded one.
- **The time-saved line above ships only with a timed figure and its provenance.**

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`agents/analyst.md` owns the seven card section names** (The 30-second read, Kill
  points, Silver bullets, Where they're genuinely better, Their attack on us, Head to
  head, One question to ask) and this skill's artifact contract renders them by name and
  order. Reword them in either file and the artifact loses sections silently.
- **`agents/competitor-scanner.md` owns the scan section names**; the analyst reads
  scans by section. The scan filename shape `scan-<competitor-slug>.md` is matched by the
  analyst's Glob.
- **`curriculum/manifest.json`** carries this skill's `one_liner`, `artifact`,
  `time_saved`, and `team` — the menu and the site read them; keep them in step with the
  opening lines here.
- **README.md § Competitive Intel** quotes the intake shape and the card sections.
- The working folder shape `my-work/competitive-intel/<YYYY-MM-DD>-<slug>/` is what makes
  run history findable; `/bluerock:wrap-up` logs runs against the agent-team label
  **Competitive Intel** with members `competitor-scanner` + `analyst` (the Account
  Research roll-up shape).
