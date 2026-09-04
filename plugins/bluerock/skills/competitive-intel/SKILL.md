---
name: competitive-intel
description: >-
  Competitive Intel — point an agent team at the competitors you face and get a
  battlecard per competitor: sourced kill points, your differentiators aimed, where
  they're genuinely better, their likely attack and the answer, and one question to
  ask. Use when I say "battlecard for <competitor>", "competitive intel on <A> and
  <B>", "who are we up against", "how do I beat <competitor>", "kill points against
  <competitor>", "compare us to <X> and <Y>", "prep me for a competitive deal", or
  name competitors before a meeting. Runs competitor-scanner (once per competitor,
  up to 4, concurrently) → analyst, and writes to my-work/competitive-intel/.
  Research-grade on purpose — minutes, not seconds.
---

Run the Competitive Intel team and produce **battlecards** — one card per competitor,
ready for the room. You orchestrate the agents; they do the work. This is the deep read
of the pair: the Account Scorecard is seconds on one account, this is minutes across up
to four competitors, because the answers that survive a deal live in docs and pricing
pages, not homepages.

**What it replaces:** building or refreshing battlecards by hand — the research, the
comparison, and the meeting prep.
**Time saved:** about 1 hour by hand, estimated and not yet timed. The timed
baseline (E6-26) replaces this figure when it lands.

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

**Skip what they already gave you.** If the opening request named the industry or the
competitors, don't re-ask — say what you're taking as given (`Industry: AI runtime
security · Competitors: Straiker, Zenity`) so a wrong reading gets corrected early, then
pick up at the first step that's actually missing. A returning builder never re-answers a
question they already answered; a prior run's `inputs.md` pre-fills the same way (propose,
confirm, don't re-ask cold).

**Which prompt shape for which step:** use the question picker (`AskUserQuestion`) only
where the answer is genuinely a choice between a few options — steps 3a and 4. Everywhere
else the answer is free text in the builder's own words, and a four-option picker is the
wrong shape for it: ask in the message and let them type. Where the picker isn't available
in this client, ask in the message.

1. **Industry / market context.** "What category are we competing in?"
2. **Competitors.** "Who are we up against? Names are enough — add a domain for anything
   with a common name (cap is 4 per run)."
3. **Your differentiators.** "What do you win on? Two or three real bullets in your own
   words beat ten aspirational ones." (Pre-fill from the messaging doc or objectives when
   they exist and confirm instead.) Kill points come from the scans; **silver bullets come
   only from here** — never fabricate a differentiator.
   - **3a — if they have nothing written down**, offer the route rather than leaving them
     stuck: *"Want me to pull them out with three questions?"* (options: yes, ask me the
     three · I'll write them myself · skip it — the cards will say the silver-bullets
     section was built without them). If they take the three, ask **one at a time**:
     1. What do you win on when you win?
     2. What do you hear in a won deal that you never hear anywhere else?
     3. What can you do on day one that a competitor needs a services project for?
     Then read their answers back as a differentiator list and let them correct it before
     moving on.
4. **Personas.** Offer it explicitly — it changes the cards materially — but **never block
   the run on it**: *"Tailor these to the person in the room?"* (yes — give me title, what
   they own, seniority · no — keep it general). More than one person is normal and fine: a
   card carries a lane each (a CISO and a CIO want different openings). Take them all.
5. **Other notes.** "Anything else that should shape these? A deal that's stuck, pricing
   pressure, a loss you want to understand, a compliance constraint, a claim we're not
   allowed to make, a phrase to avoid. Optional — say 'nothing' if there isn't anything."
6. **Confirm before we run.** Play back industry, competitors, differentiators, personas,
   and notes as a short bullet list, then: "Good to go, or anything to edit?" **Carry all
   five inputs forward verbatim from here** — notes and differentiators are the builder's
   own words, and paraphrasing either is how a card ends up asserting something they never
   said.

**The moment the builder approves**, set the expectation for the wait in one message of
its own, then go quiet until the report: the scans run concurrently and take several
minutes, so say so plainly — this is a good moment to grab a coffee or switch tasks, and
the battlecards will be ready when they check back. No further chatter between this and
the report.

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

## Run the agents

Dispatch these as ordinary subagents. Do not use agent-teams tooling; this runs
identically in every client.

10. **Dispatch one `competitor-scanner` per competitor — all in a single message so they
    run concurrently.** Each gets: its one competitor (name + domain if given), the
    industry, and the working folder's **absolute path** in the dispatch prompt itself (a
    subagent starts wherever the session started; the path you pass is the handoff). Each
    writes a sourced `scan-<competitor-slug>.md`, docs-deep and bounded to 6 to 8 fetches.
    Wait for all of them.
    - **If the builder's notes mention a specific competitor** — a loss to them, a claim
      they made in a deal, a rumour worth checking — pass it to *that* competitor's scanner
      as an **unverified lead from the builder**, to come back sourced or come back
      `[not found]`. Never as a fact.
11. **Dispatch `analyst`** with the working folder path and, when step 8 found one, the
    previous `battlecard.md` path. It reads `inputs.md` and every scan — **no web tools,
    no new research** — and writes `battlecard.md`: one card per competitor; on a
    multi-competitor run, the two field-level syntheses (**The field** and the
    **Capability chart**); and what changed since the previous run. The builder's
    differentiators, personas, and notes reach it through `inputs.md` **verbatim** — that
    file carries their words, never a paraphrase.

## Publish the artifact — you, not the agents

12. When `analyst` finishes, read `battlecard.md` and **publish it as a Claude Artifact**
    yourself, in this conversation, following the design contract below. The agents write
    markdown only; the finished, shareable view is yours to render. If artifact publishing
    isn't available in my environment, don't block — the markdown is saved; say so and
    give the path.

### The artifact — design contract (follow it exactly)

**The artifact is a tool the builder operates in the room, not a report they scroll**
(product decision, 2026-08-31). One competitor on screen at a time, reachable in one
click; sections scannable by color before they are read. Still read-only and honest:
no CTAs, no dead controls, nothing that pretends to fetch or save — a dead button in a
sandboxed artifact is worse than no button. Interactivity is navigation, never chrome.

A single self-contained HTML page. **CSP rules: exactly one external request, the Google
Fonts stylesheet below. All CSS in one `<style>` block, all JS inline (one small tab
script), no CDN scripts, no remote images.** Print-friendly: under `@media print` the tab
strip hides, `.panel[hidden] { display: block }` renders every competitor in sequence,
with a page break between competitors.

**Fonts** — one Google Fonts link, every face with a real fallback: `DM Sans` (display +
body; fallback `system-ui, -apple-system, sans-serif`), `Source Serif 4` (the 30-second
read, "say it" lines, the closing question; fallback `Georgia, serif`), `JetBrains Mono`
(labels, meta, chips; fallback `ui-monospace, Menlo, monospace`).

**Theme — ship both, token-structured.** Bare `:root` carries the complete light palette;
`@media (prefers-color-scheme: dark)` guarded as `:root:not([data-theme="light"])`
redefines only the tokens; `:root[data-theme="dark"]` duplicates them. Every component
rule uses `var()` — no literal color outside the three token blocks. `body` background is
`var(--paper)`.

**Tokens** (light / dark):

| Token | Light | Dark |
|---|---|---|
| paper / card / card-2 | `#F5F1EA` / `#FFFFFF` / `#FAF7F1` | `#14171E` / `#1C212B` / `#222835` |
| line / line-2 | `#E7E0D6` / `#D6CDBE` | `#2E3542` / `#3D4658` |
| ink / ink-2 / ink-3 / ink-4 | `#1B2130` / `#3D4658` / `#6B7486` / `#8B93A3` | `#EDEEF2` / `#C3C9D4` / `#97A0B0` / `#7B8494` |
| accent (BlueRock blue) + soft + line | `#1559C4` / `#E8EFFB` / `#B9CDEF` | `#6E9BE8` / `#1D2A45` / `#34528C` |
| kill + soft + line | `#B4432E` / `#F9ECE8` / `#E8C7BE` | `#E0715A` / `#372220` / `#6B392F` |
| bullet + soft + line | `#206E5B` / `#E7F2EE` / `#BFDCD3` | `#55B092` / `#1B2E29` / `#2F5A4B` |
| mine + soft + line | `#94660F` / `#F7EFDD` / `#E5D3AC` | `#D3A24C` / `#322A19` / `#66542B` |
| neutral + soft + line | `#5A6272` / `#EEEDE9` / `#D9D3C8` | `#9AA3B2` / `#262C37` / `#414A5A` |
| chip text (on lane-colored chips) | `#FFFFFF` | `#14171E` |

**Structure** (max width 1000px):

1. **Sticky masthead** — uppercase display title (`AI <industry> · Battlecards` shape),
   mono meta line (`<date> · FOR: <personas> · <first run or run N> · <N> source
   domains`), then the **tab strip**: one `role="tab"` button per competitor,
   `aria-selected` on the active one, 3px accent underline; panels are
   `<section role="tabpanel">` toggled via the `hidden` attribute by the inline script
   (first panel visible on load, others carry `hidden` in markup).
2. **Legend row** naming the four lanes with color dots: kill points (sourced, use in the
   room) · silver bullets (our claims, aimed) · don't take the fight here · their attack,
   our answer.
3. **"Since your last run" strip** — only when a previous run existed: an accent-soft
   callout, dated, listing the analyst's "Since" items (or its "no material change"
   line). Omit the block entirely on a first run.
4. **On a multi-competitor run, two field-level views** reachable from the tab strip
   alongside the competitors: **The field** (the analyst's cross-competitor table plus its
   "who's actually the threat" read) and the **Capability chart** — render the Harvey-ball
   grid as an actual grid of the five symbols (never a bar chart or a numeric score), each
   cell's one-line rationale directly beneath its row. The symbols are the point.
5. **One panel per competitor**, sections in this order:
   - **Name** (display, 28–40px, weight 800) + mono scope subline carried from the scan.
   - **The 30-second read** — bordered block with a dark bar header (`background:
     var(--ink)`, `color: var(--paper)`), labeled grid rows (`128px + 1fr`; mono
     uppercase labels, serif values): what they are, the tell or how they move, and a
     highlighted **THE FIGHT** row on accent-soft.
   - **Kill points** — kill-colored chip + note `Sourced. Use in the room.`; numbered
     item-cards (mono number, kill-colored 4px left stripe) each carrying the four lines:
     the **point** as the bold lead, the **proof** with its mono source chip
     `scan-<slug>.md · <section>`, the **ask** (labeled `ASK`, the question that lets the
     buyer discover it), and **they'll say** (labeled, their rebuttal and the one-line
     counter). Carry every `[their claim]` / `[unverified]` marker as a small mine-colored
     mono tag — never silently drop one.
   - **Silver bullets** — bullet-colored chip + note `Your differentiators, aimed.`;
     numbered cards with the "say it" line in serif italic behind a bullet-colored left
     rule. When differentiators were missing, this section carries the honest one-liner
     instead.
   - **Where they're genuinely better** — mine-colored chip + note `Don't take the fight
     here.`; one card, hairline-separated list. Never empty when the scans found
     strengths.
   - **Their attack on us** — neutral chip + note `What they'll open with, and the
     answer.`; THEM/US volley rows (mono uppercase speaker labels, their line italic,
     our answer in ink) with the persona target as an accent mono tag (`→ CISO`).
   - **Head to head** — ink-colored chip; a them/ours table inside a bordered
     `overflow-x: auto` container (`min-width: 560px` on the table), their column headed
     `(sourced)`, ours `(ours)` in bullet color. Only rows where both sides are known.
   - **One question to ask** — accent chip + note `Worded so the prospect asks them.`;
     the question in serif italic inside an accent-soft callout with a 3px accent left
     border.
   - **Persona lane — for <title>** (only when a persona was given; one lane per person):
     accent-topped card with what they're measured on, the lead-with silver bullet in
     their vocabulary, the kill points re-ranked for them, the don't-say line, and their
     three discovery questions. `[my read]` markers stay visible.
   - **Panel sources** — mono chips of the domains that competitor's scan actually used.
6. **Footer** — the separation-rule note (sourced lines carry a scan citation; silver
   bullets are ours to say, never dressed up as findings), the line **`Internal
   competitive material — not for circulation to customers or prospects`**, and
   `Built with BlueRock · Competitive Intel · competitor-scanner + analyst`.

**The scan test:** someone reading this on a phone in a lobby has about eight seconds —
the lane colors, the 30-second read, and the numbered points must carry the card before a
single sentence is read.

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
- **No FUD, no disparagement.** Attack the capability gap, never the company or its
  people. These cards should read like they would survive being forwarded to the wrong
  person.
- **Refresh, don't rot.** Competitive intel goes stale in about a quarter. Every run is
  dated; when the previous run in `my-work/competitive-intel/` is more than a quarter old,
  say so in the report rather than treating the diff as a refresh.
- **The time-saved line above ships only with a timed figure and its provenance.**

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`agents/analyst.md` owns the card section names** (The 30-second read, Kill points,
  Silver bullets, Where they're genuinely better, Their attack on us, Head to head, One
  question to ask, and the conditional Persona lane) **and the two field-level synthesis
  names on multi-competitor runs (The field, Capability chart)**; this skill's artifact
  contract renders all of them by name and order. Reword them in either file and the
  artifact loses sections silently. The kill-point four-line shape (point, proof, ask,
  they'll say) is likewise shared between the analyst's card spec and the artifact's
  kill-point rendering.
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
- **The flow doc mirrors this skill** (content repo, private:
  `09-product/use-case-flows/competitive-intel-flow.md`) — any change to the intake,
  dispatch, artifact, or close updates it in the same pass.
