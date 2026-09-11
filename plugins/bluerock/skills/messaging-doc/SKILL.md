---
name: messaging-doc
description: >-
  Brand Messaging Doc — answer a few short questions about what your brand should
  say, and a small agent team writes your core messaging doc (positioning, voice, and
  the phrases you actually use) from your answers, then checks your website against
  it. Use when I say "build my messaging doc", "distill my messaging", "messaging doc
  for <site>", "what does our site actually say", or paste a website URL and ask for
  the brand's messaging. Runs site-reader → distiller and writes the doc and a
  Messaging Assessment to my-work/messaging-doc/. A short guided intake, one URL, and
  anything I paste — no exports, no logins, no integrations.
---

Run the Messaging Doc team and produce two things from one run: the **Brand Messaging
Doc**, a one-page source of truth for positioning, voice, and the exact phrases the brand
uses, written from what the builder means to say; and the **Messaging Assessment**, what
the website says today set beside that doc, with the gaps named and one thing to fix
first. You orchestrate two agents; they do the work. Keep it tight: a short intake, a
bounded site read and a distillation, aiming for about fifteen minutes end to end, not a
brand audit.

**Which way round this runs, and why (0.15.0, Linda, 2026-09-11).** Earlier versions
read the site first and set the builder's words beside it, which made the doc a
well-organised mirror of the homepage. A messaging doc is a statement of intent; the
website is one of its outputs. So the builder's answers are the source, the site is the
evidence that gets checked against them, and the two are never dressed up as each other.
A run with a URL and no answers produces the assessment only, and says so.

## First — anchor to the project

The doc, its working folder, and the `voice.md` / `objectives.md` the run reads all
live in the builder's project. Two generations exist: the project ships inside the workspace image (usually the folder
`my-workspace`); projects made before 2026-08 were cloned and carry whatever
name the builder chose. **Assume neither — identify it by its signature.** In an SSH/cloud
container the chat may start in the project itself or in the **home folder** with the
project one level down — both are normal. Identify it by signature, not name: run `ls`; see `CLAUDE.md` and `design/` side by
side? You're in the project. If not, find it: `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`,
else `find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` in, capture the
**absolute path** with `pwd`, and use that full path throughout. Can't find it? Ask the
builder which folder their project is in.

## Before the questions — read what the builder already has

Check, without asking: `objectives.md` and `voice.md` at the project root, and `inputs.md`
from the most recent run under `my-work/messaging-doc/`.

- **If they're real**, pre-fill the intake below — propose and confirm, don't re-ask cold.
  A rerun should feel like reading your own answers back, not starting over.
- **If they're placeholder templates or absent**, say so once and keep moving. Never make
  setup homework the price of the first doc.

## Intake — one question per step, short, then confirm

**The answers are the doc.** Everything the agents can see on the site is already on the
site, so a run with only a URL can only describe the site. The questions below are where
the doc comes from: they take a couple of minutes, and the site read then shows where the
website agrees with them and where it says something else.

Ask one at a time, a line or two each. **Skip anything the opening request already gave.**
**Pre-fill from `objectives.md`, `voice.md`, and the last `inputs.md` wherever they hold a
real answer**, and confirm instead of asking.

**Rate each answer as you go, once, in a word: clear, vague, or missing.** *Clear* means a
stranger could act on it. *Vague* gets exactly one follow-up, then you take what you have.
*Missing* is a real answer too: the doc marks that section open rather than filling it in.
Say the rating plainly and move on; never lecture.

1. **The site.** One website URL, usually the builder's own brand. If the opening request
   gave it, don't ask. If they give only a company name, confirm the domain before spending
   the run. (Pointing it at a competitor is a trick for later; the doc is for their brand.)
2. **Who you sell to, and what is happening when they come looking.** *"Not the job title:
   the situation. What has just gone wrong, or changed, when someone reaches for you?"*
   Pre-fill from `objectives.md` if it names an audience, and confirm. If the answer is a
   title alone, the one follow-up is: *"What's going on for that person the week they
   start looking?"*
3. **What it is, in plain language.** *"One line, the way you'd say it to someone outside
   your industry."*
4. **What they do today instead.** *"Before you, what do these people use or do? Name it
   the way they'd name it, including 'a spreadsheet' or 'nothing'."* This is the question
   a run can never answer from the site, and the one most messaging skips.
5. **Why yours is better than that.** *"Against what they do today, what's actually
   different? Two or three plain bullets."* Then **one push-back, once**: *"A competitor
   could say most of that too. Which part couldn't they say?"* Take their answer as the
   differentiation; keep the rest as claims. Never invent a differentiator.
6. **The one thing to remember.** *"If they remember one sentence about you, what should
   it be? Your words."* This is the line the doc carries beside the site's, verbatim.
7. **Where the site is out of date, or wrong.** *"Anything on there you wouldn't say any
   more? A product that moved on, a claim you've retired, an audience you no longer sell
   to?"* Optional, and the sharpest thing the assessment can find: it is the finding the
   agents can never reach on their own.
8. **The paste — once, lightly.** Recent material that sounds like you *now*: a post or
   two, campaign copy, an email you were proud of. Optional. **This is the voice sample the
   doc reads first**, ahead of the site, because it is copy the builder already judged
   good. A URL is a fine answer and often a better one: **hand extra URLs to the site
   reader as additional pages to read** rather than asking for the text, and say in one
   line that that is what you are doing. Pasted text goes to `references.md`; a URL goes to
   the reader.

**Offer, never block.** If the builder says "just run it" with a URL and no answers, run
it, and say in one line what they will get: *"With just the site, this is a Messaging
Assessment: what your site says today and where it disagrees with itself. Answer the
questions any time and the run writes the doc too."* Do not ask again.

9. **Confirm before we run.** Play back the answers in order, each with its one-word
   rating, plus the site and anything flagged as stale, then: *"Good to go, or anything to
   edit?"* **Play the inputs back; do not pre-judge the site against them.** You have not
   read a page yet, so a guess about what the site says is a guess wearing the tone of a
   finding. **Carry the answers forward verbatim.** The builder's own words are the doc;
   paraphrasing them is how it turns back into a summary.

## Setup

1. **Make the working folder.** Slugify the brand name → `my-work/messaging-doc/<slug>/`.
   Create it. `my-work/` is builder-owned and never overwritten.
2. **Keep the last run.** If the folder already holds `messaging-doc.md` or
   `messaging-assessment.md`, move them into `previous/` inside the folder before anything
   is written. The distiller reads them to say what changed since last time.
3. **Save the paste before dispatching.** If they pasted anything, write it as
   `references.md` in the working folder, labeled by what each piece is ("LinkedIn post,
   July", "campaign email"). The agents read files, not this conversation — an unsaved
   paste is invisible to them. **If step 8 produced URLs instead**, they are not references;
   carry them into the site reader's dispatch as extra pages and record them in `inputs.md`
   as what they are. **Note in `inputs.md` which arrived as a paste and which as a link.**
4. **Write `inputs.md` before dispatching.** The confirmed intake, verbatim, one labelled
   line per answer, each with its rating, in this order and with these labels (the
   distiller and the artifact both read them by label):
   `Site` · `Who you sell to` · `What it is` · `What they do today instead` · `Why yours is
   better` (with the push-back answer marked *"what a competitor couldn't say:"*) · `The one
   thing to remember` · `Where the site is out of date, or wrong` · `Paste`. A question the
   builder didn't answer is written as `missing`, never left out.

**One rule the intake creates downstream, and it is the same separation rule the
battlecard runs on:** what the builder says and what the site says are both carried,
neither is dressed up as the other, and **the difference between them is the finding.**

## Run the agents, in order

Dispatch these as ordinary subagents, one at a time, waiting for each. Do not use
agent-teams tooling; this runs identically in every client.

5. **Dispatch `site-reader`** with the URL, any extra URLs, and the working folder. It reads
   the homepage plus the two or three pages that carry the messaging and writes
   `signals.md` — the positioning lines, voice notes, and exact recurring phrases, quoted
   and sourced, plus a read-quality note. It also checks every term `inputs.md` marks as
   retired against the pages it read. Bounded to a handful of fetches; let it be fast. Wait
   for it.
6. **Dispatch `distiller`** with the same folder. It reads **`inputs.md`** first, then
   `signals.md`, `references.md` if present, `previous/` if present, and `voice.md` /
   `objectives.md` from the project root. It writes `messaging-doc.md` when the intake
   holds answers, and `messaging-assessment.md` always. Wait for it. **`inputs.md` is the
   doc**: an answer you didn't save is a section the doc will mark open.

## Publish the artifact — you, not the agents

7. When `distiller` finishes, read what it wrote and **publish it as a Claude Artifact**
   yourself, in this conversation, following the design contract below. The agents write
   markdown only — they have no artifact publishing; the finished, shareable view is
   yours to render. If artifact publishing isn't available in my environment, don't
   block — the markdown is saved; say so and give the paths.

### The artifact — design contract (follow it exactly)

A single self-contained HTML page. **CSP-safe: inline ALL CSS in one `<style>` block, no
external requests — no CDN, no web fonts, no remote images, no scripts.** It is a static
page. Print-friendly, read-only, no CTAs or buttons.

**Layout** — one centered column, `max-width: 640px`, generous whitespace. The page has two
parts, the doc and then the assessment, separated by one labelled divider. **When the run
produced only the assessment** (no answers), the page is the assessment alone under its own
header (`Messaging Assessment`), with one muted line under the header: *"Answer the
questions on a rerun and this becomes your Brand Messaging Doc."*

1. **Header** — brand name (serif, ~30px, heading ink); beneath it **the one thing to
   remember**, verbatim from `inputs.md`, in muted ink (when missing, the doc's umbrella
   statement; when there is no doc, the site's positioning one-liner); then a subline in
   muted ink: `Brand Messaging Doc · Generated <today's date> · <N> pages read`. Read
   quality does not go here; it renders at the foot.
1b. **At a glance** — directly beneath the header, two blocks side by side
   (`grid-template-columns: 1fr 1fr; gap: 12px;`, stacking under 460px). **WHAT YOU SAY**
   first, white with a 3px accent-blue left border, carrying the one thing to remember
   verbatim as a serif quote; **WHAT THE SITE SAYS** second, cream fill, carrying the
   site's positioning one-liner as a serif quote (when the assessment carries the
   "assembled from fragments" caveat, the first positioning sentence as written, caveat
   beneath in muted ink). Labels small uppercase muted. **When `inputs.md` carries no
   intended line, render the site block alone at full width and never invent the other
   half.** Beneath the two, pill counters in small sans: `N gaps found` (accent border and
   text; the count of entries in the assessment's Gaps), `N stale name(s), confirmed live`
   (medium amber fill; **only when the site reader verified a retired term still live**,
   otherwise absent), `N pillars, M open` (hairline; from the doc's Pillars section; absent
   when there is no doc), and `N phrases you run on` (hairline). Counts are read from the
   sections, never typed. **Read by**: under the counters, a small uppercase `READ BY`
   label followed by one accent-soft pill per use case that reads the latest messaging
   doc, by its manifest `title`: read them from
   `${CLAUDE_PLUGIN_ROOT}/curriculum/manifest.json` as the use-case records whose skill
   reads `my-work/messaging-doc/` (today Competitor Battlecards, Answer Engine Visibility,
   Sales Outreach Prep, Weekly Signal Digest). Pills name deliverables, never commands, and
   name only use cases present in the installed manifest.

**Part one — the Brand Messaging Doc.** Each section: a small uppercase label
(letter-spacing), then the content in body ink. **An open section renders as a dashed
hairline box** with the label, the word `Open` in muted ink, and the distiller's one-line
note of what would fill it. Never fill an open section with anything.

2. **Who it's for** — the builder's line, verbatim.
3. **What it is** — the builder's line, verbatim.
4. **Instead of** — what they do today, the builder's line, verbatim.
5. **Why you** — the differentiation, with the part a competitor couldn't say rendered
   first in heading ink, the rest in body ink beneath.
6. **Pillars** — up to three, as tinted blocks in a row (`1fr 1fr 1fr`, stacking under
   460px): the pillar in heading ink, its proof beneath in body ink with the source in
   muted ink (a page URL or "you said"). A pillar with no proof renders with a dashed
   border and `Proof: open` in muted ink. Never more than three.
7. **Positioning statement** — the distiller's one-sentence draft as a serif quote at
   `18px`, with `Drafted from your answers; edit it until it's yours.` beneath in muted ink.
8. **Voice** — each attribute as a row: the attribute name in heading ink, its quoted
   example beneath in body ink with a hairline left border and its source in muted ink.
9. **The phrases you actually use** — the verbatim phrases. **The chip shape only holds a
   term, not a sentence.** Anything **40 characters or under** renders as a small mono chip
   (cream fill, hairline border), wrapped into a row. **Anything longer renders as a quoted
   line instead**: serif, `15px`, a hairline left border and `16px` of left padding, one
   per row. Exact words either way. Lead with the load-bearing few the distiller put first.

**Divider** — a hairline rule with a small uppercase label centred on it:
`MESSAGING ASSESSMENT · WHAT YOUR SITE SAYS TODAY`.

**Part two — the Messaging Assessment.**

10. **Site positioning** — the site's positioning in two or three sentences, with the
    "assembled from fragments" caveat beneath in muted ink when it carries one.
11. **Where the site agrees, and where it differs** — one row per doc section the
    assessment compared (who it's for, what it is, instead of, why you, the one thing):
    the section label, then `Agrees` in a small green-tinted pill or `Differs` in a small
    amber-tinted pill, then the distiller's one line with the page quoted.
12. **Gaps** — always present. **Only the first gap gets the highlighted callout**: cream
    tint background, a 3px accent-blue left border, the note in heading ink at `16px`.
    **Every gap after it renders plain**: white, no left border, a hairline rule above,
    body ink. When nothing inconsistent was found, render the distiller's one line as the
    callout. Render only what the distiller put in Gaps.
13. **Since last run** — only when `previous/` existed: the distiller's lines on which
    gaps closed and which remain, plain rows with a hairline rule above.
14. **What to fix first** — the closing content block: the section label, then the
    recommendation in heading ink at `16px`, on white with a hairline rule above. **Give
    it the weight of an ending.** If the distiller found no change worth making, render
    that line as written.
15. **Footer** — small muted text, three lines: `Built with BlueRock · Brand Messaging Doc
    · site-reader + distiller`; beneath it the pages read (and "pasted references" if
    used) as plain muted text separated by ` · `, **not chips**; and beneath that the
    **Read quality** line if the assessment carries one. Provenance belongs together, and
    it belongs last.

**Palette** (Builders "cool-paper", light-only — use these hex values directly since the
Artifact can't read the app's CSS variables):
- Page background `#F5F1EA`; card surface `#FFFFFF`; card border `#E7E0D6`, radius `14px`.
- Cream (the "cream tint" / "cream fill" above): `#F5F1EA`.
- Ink: heading `#1B2130`, body `#3D4658`, muted `#7B8494`.
- Accent (BlueRock blue) `#1559C4`. Agree tint `#E6F1EA` with ink `#2F6B45`; differ tint
  `#FBEFD9` with ink `#8A5A12`; the stale pill uses the differ tint.

**Type** (CSP-safe fallbacks, no web fonts): headings `Georgia, 'Times New Roman', serif`;
body + labels `system-ui, -apple-system, sans-serif`. Labels small and uppercase with
slight letter-spacing; chips in `ui-monospace, monospace`.

## Finish

8. The **artifact** is the payoff: the doc in the builder's words with the site checked
   against it beneath. `messaging-doc.md` is the source of record the builder keeps and
   that four other use cases read; `messaging-assessment.md` is the check, and it is the
   file to rerun when the site changes.
9. **Report, sharpest finding first.** Lead with the sharpest thing in Gaps, in one
   sentence, before anything else: it is the part they could not have written themselves.
   (*"Your site never says who it's for; you did, in one line."* beats *"here's your
   messaging doc."*) If nothing was inconsistent, say that plainly. Then: the paths, any
   sections the doc left open and the one question that would fill each, **the one thing
   to fix first**, and the artifact (or the fallback note). Don't reprint the whole thing.
10. **Say what it's for on Monday.** One line: this is the page to hand an agency at
    kickoff, a new writer on day one, or whoever keeps rewriting the homepage, and it is
    what Competitor Battlecards, Sales Outreach Prep, Answer Engine Visibility and the
    Weekly Signal Digest start from.

## Why this doc matters

This is not a one-off report — it's the project's memory seed for everything the builder
writes from here. Later sessions wire it into the project's memory, drafting skills lean on
its phrase bank, and four use cases read it to pre-fill what the builder sells and to whom.
The better this doc, the more the whole project sounds like the brand. The assessment is
what keeps it honest: rerun it when the site changes and see whether the site still says
what the builder means.

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **This skill matches on `agents/distiller.md`'s exact phrase "assembled from
  fragments"** to decide how the artifact renders the site's positioning. Rewording the
  phrase in either file silently changes the artifact.
- **`inputs.md` is a contract between this skill and `agents/distiller.md`**, by the eight
  labels listed under Setup. This skill writes it from the intake; the distiller builds the
  doc from it and checks `signals.md` against it; the artifact reads `The one thing to
  remember` from it. Renaming a label or dropping an answer collapses the doc back into a
  summary of the site.
- **`previous/` inside the working folder** is what makes "since last run" possible. The
  skill moves the last run's files there; the distiller reads them.
- **`skills/learn-meet-your-first-agent-team/SKILL.md` narrates this skill as its
  marketing lane**: its lane table and steps name the agents (`site-reader` →
  `distiller`) and the folder (`my-work/messaging-doc/<brand>/`).
- **`curriculum/manifest.json`** carries this skill's `one_liner` and **README.md
  § Messaging Doc** quotes the flow; the menu and the site read both.
- **Four use cases read the latest `messaging-doc.md` under `my-work/messaging-doc/`** — the
  folder shape and the filename are load-bearing well beyond this skill.
  `/bluerock:competitive-intel` reads *Why you* to pre-fill a builder's differentiators;
  `/bluerock:aeo-visibility` reads *What it is* and the phrases to build the buyer questions
  it proposes; `/bluerock:outreach-prep` reads *What it is* and *Why you* to pre-fill what
  the builder sells; and `/bluerock:signal-monitor` reads the positioning to aim the "why it
  matters" line on every signal card. An assessment-only run writes no `messaging-doc.md`,
  so all four keep degrading honestly rather than reading the site's words as the builder's.
