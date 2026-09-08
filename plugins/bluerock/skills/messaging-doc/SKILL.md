---
name: messaging-doc
description: >-
  Core Messaging Doc — point a small agent team at a brand's website and get the
  doc every later draft leans on: positioning, voice, and the phrases the brand
  actually uses. Use when I say "build my messaging doc", "distill my messaging",
  "messaging doc for <site>", "what does our site actually say", or paste a
  website URL and ask for the brand's messaging. Runs site-reader → distiller and
  writes the doc to my-work/messaging-doc/. A short guided intake, one URL, and
  anything I paste — no exports, no logins, no integrations.
---

Run the Messaging Doc team on a brand's website and produce the core messaging doc — a
one-page source of truth for positioning, voice, and the exact phrases the brand uses.
You orchestrate two agents; they do the work. Keep it tight: a bounded site read and a
distillation, aiming for about five minutes, not a brand audit.

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
- **If they're placeholder templates or absent**, say so once and keep moving. Never make
  setup homework the price of the first doc.

## Intake — one question per step, short, then confirm

**A URL alone can only produce a summary of the site.** Everything the agents can see is
already on the page, so without the builder's own view the doc is a well-organised mirror
of the homepage — which is the difference between a source of truth and a restatement.
**The questions below exist to make it a comparison rather than a summary:** what the site
says, what the builder says, and where those two have come apart.

Ask one at a time, a line or two each. **Skip anything the opening request already gave.**

1. **The site.** One website URL — usually the builder's own brand. (It runs on any
   brand's site; pointing it at a competitor for a comparison is a trick for later.) If
   they give only a company name, confirm the domain before spending the run.
2. **Who you sell to.** Pre-fill from `objectives.md` and confirm; ask only if absent.
   The voice section is judged against a reader, and without this it is judged against
   nobody.
3. **What you want people to understand about you.** *"Two or three lines, your words —
   the thing you'd want them to walk away with."*
   - **3a — if they have nothing written down**, offer the route: *"Want me to pull it out
     with three questions?"* If they take it, ask **one at a time**: (1) What do people
     most often misunderstand about what you do? (2) What do you say in a first call that
     the site doesn't say? (3) If they remember one thing, what should it be? Read the
     answers back and let them correct before moving on.
4. **Where the site is out of date, or wrong.** *"Anything on there you wouldn't say any
   more? A product that moved on, a claim you've retired, an audience you no longer
   chase?"* **This is the question the agents can never answer for themselves**, and it is
   what turns the output from *here is what your site says* into *here is what your site
   says, here is what you say, and here is the gap.* Optional, and worth asking properly.
5. **The paste — once, lightly.** Recent material that sounds like you *now*: a post or
   two, campaign copy, an email you were proud of. Optional; if they have nothing at hand,
   move on without ceremony.
   - **A URL is a fine answer here, and often a better one.** Builders reach for a link
     before they reach for the clipboard. Take it: **hand extra URLs to the site reader as
     additional pages to read** rather than asking them to paste the text instead. Say in
     one line that that is what you are doing, so they know the link was used and not
     filed. Pasted text still goes to `references.md`; a URL goes to the reader.
**Offer, never block.** Steps 2 to 5 sharpen the run; none of them is the price of the
first doc. If the builder says "just run it," run it — and say in one line what the doc
will be without them (*"it'll be a read of the site, not a comparison"*) rather than asking
again.

6. **Confirm before we run.** Play back the site, the audience, the intended message, and
   anything they flagged as stale, then: *"Good to go, or anything to edit?"* **Play the
   inputs back; do not pre-judge the site against them.** You have not read a page yet, so
   a guess about what the site says is a guess wearing the tone of a finding. The reading
   is the run's job. **Carry it
   forward verbatim** — the builder's own words are the half of this doc the site cannot
   supply, and paraphrasing them collapses the comparison back into a summary.

## Setup

1. **Make the working folder.** Slugify the brand name → `my-work/messaging-doc/<slug>/`.
   Create it. `my-work/` is builder-owned and never overwritten.
2. **Save the paste before dispatching.** If they pasted anything, write it as
   `references.md` in the working folder, labeled by what each piece is ("LinkedIn post,
   July", "campaign email"). The agents read files, not this conversation — an unsaved
   paste is invisible to them. **If step 5 produced URLs instead**, they are not references;
   carry them into the site reader's dispatch as extra pages and record them in `inputs.md`
   as what they are, so a rerun reads the same set. **Note in `inputs.md` which arrived as
   a paste and which as a link** — the two travel different routes, and a rerun that mixes
   them up reads a different site than the first run did.
3. **Write `inputs.md` before dispatching.** The confirmed intake, verbatim. The agents
   read files rather than this conversation, and the next run pre-fills from it rather
   than starting cold.

**One rule the intake creates downstream, and it is the same separation rule the
battlecard runs on:** what the site claims and what the builder claims are both carried,
neither is dressed up as the other, and **the difference between them is the finding.**
Where they disagree, say so plainly rather than smoothing it into one voice.

## Run the agents, in order

Dispatch these as ordinary subagents, one at a time, waiting for each. Do not use
agent-teams tooling; this runs identically in every client.

5. **Dispatch `site-reader`** with the URL and the working folder. It reads the homepage
   plus the two or three pages that carry the messaging and writes `signals.md` — the
   positioning lines, voice notes, and exact recurring phrases, quoted and sourced, plus a
   read-quality note. It's bounded to a handful of fetches, and may spend one more to
   verify a term that looks off-pattern rather than hedge on it — let it be fast. Wait for it.
6. **Dispatch `distiller`** with the same folder. It reads `signals.md` and **`inputs.md`**
   (plus `references.md` if present, and `voice.md` / `objectives.md` from the project
   root) and writes `messaging-doc.md`. Wait for it. **`inputs.md` is the half of the doc
   the site cannot supply** — the intended positioning and the stale-copy flags reach the
   distiller through that file and nowhere else, so an intake answer you didn't save is an
   answer the comparison was never made against.

## Publish the artifact — you, not the agents

7. When `distiller` finishes, read `messaging-doc.md` and **publish it as a Claude
   Artifact** yourself, in this conversation, following the design contract below. The
   agents write markdown only — they have no artifact publishing; the finished,
   shareable view is yours to render. If artifact publishing isn't available in my
   environment, don't block — the markdown is saved; say so and give the path.

### The artifact — design contract (follow it exactly)

A single self-contained HTML page. **CSP-safe: inline ALL CSS in one `<style>` block, no
external requests — no CDN, no web fonts, no remote images, no scripts.** It is a static
page. Print-friendly, read-only, no CTAs or buttons.

**Layout** — one centered column, `max-width: 640px`, generous whitespace:
1. **Header** — brand name (serif, ~30px, heading ink); the positioning one-liner beneath
   in muted ink; then a subline in muted ink: `Core Messaging Doc · Distilled <today's
   date> · <N> pages read`. **The doc's Read quality line does not go here** — it renders
   at the foot beside the sources. It is provenance, and provenance in the header spends
   the reader's confidence before they have read a finding. When Positioning carries the "assembled from fragments"
   caveat, the one-liner slot uses the doc's **first positioning sentence** as written,
   with the caveat rendered beneath in muted ink — never invent a cleaner line than the
   doc has.
2. **Positioning** — a small uppercase section label (letter-spacing), then the two-to-
   three-sentence positioning in body ink. If it carries the "assembled from fragments"
   caveat, render the caveat beneath in muted ink. **When the doc carries the builder's own
   intended positioning as well, render it beneath the site's in the same block**, in body
   ink, under a small muted label that keeps the two apart (`WHAT THE SITE SAYS` /
   `WHAT YOU SAY`). Two blocks, never merged into one paragraph: the whole value of the
   section is that the reader can see the distance.
3. **Voice** — the same section label treatment, then each attribute as a row: the
   attribute name in heading ink, its quoted example beneath in body ink with a hairline
   left border.
4. **The phrases you actually use** — section label, then the verbatim phrases. **The chip
   shape only holds a term, not a sentence.** Anything **40 characters or under** renders as
   a small mono chip (cream fill, hairline border), wrapped into a row: product names,
   capitalized terms, signature constructions. **Anything longer renders as a quoted line
   instead** — serif, `15px`, a hairline left border and `16px` of left padding, one per
   row, no pill shape. A fifteen-word tagline stuffed into a rounded pill reads as broken
   layout, not as a phrase bank. Exact words either way. Lead with the load-bearing few the
   distiller put first; keep the tail short.
5. **Gaps** — always present, because the doc always has the section. **Only the first
   gap gets the highlighted callout**: cream tint background, a 3px accent-blue left border,
   the note in heading ink at `16px`. It is the one the skill already leads the chat report
   with, and it is the sharpest thing the run found. **Every gap after it renders plain** —
   white background, no left border, a hairline rule above, the note in body ink. Four
   identical blue callouts stacked is four things shouting, which reads as none. When the
   distiller found nothing inconsistent, render its one line as the callout; an
   empty-handed Gaps section is a real result and reads as one. Render only what the
   distiller put in Gaps.
6. **What to do about it** — the doc's last content block and the reason it is a document
   rather than an audit: the section label, then the distiller's one-or-two-sentence
   recommendation in heading ink at `16px`, on white with a hairline rule above. **Give it
   the weight of an ending.** If the distiller found no change worth making, render that
   line as written rather than dropping the section.
7. **Footer** — small muted text, three lines: `Built with BlueRock · Messaging Doc ·
   site-reader + distiller`; beneath it the pages read (and "pasted references" if used) as
   plain muted text separated by ` · `, **not chips**; and beneath that the **Read quality**
   line if the doc carries one, in the same muted ink. Provenance belongs together, and it
   belongs last.

**Palette** (Builders "cool-paper", light-only — use these hex values directly since the
Artifact can't read the app's CSS variables):
- Page background `#F5F1EA`; card surface `#FFFFFF`; card border `#E7E0D6`, radius `14px`.
- Cream (the "cream tint" / "cream fill" above): `#F5F1EA` — the page-background value
  reused as a tint on the white card.
- Ink: heading `#1B2130`, body `#3D4658`, muted `#7B8494`.
- Accent (BlueRock blue) `#1559C4`.

**Type** (CSP-safe fallbacks, no web fonts): headings `Georgia, 'Times New Roman', serif`;
body + labels `system-ui, -apple-system, sans-serif`. Labels small and uppercase with
slight letter-spacing; chips in `ui-monospace, monospace`.

## Finish

8. The **messaging doc artifact** is the payoff — a clean, one-page view (brand header
   with the positioning one-liner, the site's claims beside the builder's, the voice
   attributes with quoted examples, the phrase bank, the gaps, and the one recommendation
   it ends on). The `messaging-doc.md` is the source of record the builder keeps and can
   push to their repo.
9. **Report, gaps first.** Lead with the sharpest thing in Gaps, in one sentence, before
   anything else: it is the part they could not have written themselves, and it is what
   makes the run feel like the tool saw something they didn't. ("Nothing in your internal
   vocabulary shows up on the site" beats "here's your messaging doc.") If the distiller
   found nothing inconsistent, say that plainly and move on. Then the doc's path, the
   positioning one-liner it found (or the "assembled from fragments" caveat if the site
   never says it cleanly), **the one thing the doc recommends doing about it**, and the
   artifact (or the fallback note). Don't reprint the whole thing.

## Why this doc matters

This is not a one-off report — it's the project's memory seed for everything the builder
writes from here. Later sessions wire it into the project's memory, drafting skills lean on
its phrase bank, and the same two-agent run pointed at a competitor's site gives a
side-by-side messaging comparison with this doc as the baseline. The better this doc,
the more the whole project sounds like the brand.

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **This skill matches on `agents/distiller.md`'s exact phrase "assembled from
  fragments"** to decide how the artifact renders its header and Positioning block.
  Rewording the phrase in either file silently changes the artifact. The distiller's own
  dependency notes name this coupling in return.
- **`inputs.md` is a contract between this skill and `agents/distiller.md`.** This skill
  writes it from the intake; the distiller reads it as the builder's half of the
  comparison — the intended positioning it renders beside the site's, and the stale-copy
  flags it checks `signals.md` against. Renaming the file, or changing which intake
  answers land in it, collapses the doc back into a summary of the site.
- **`skills/learn-meet-your-first-agent-team/SKILL.md` narrates this skill as its
  marketing lane**: its lane table and steps name the agents (`site-reader` →
  `distiller`) and the folder (`my-work/messaging-doc/<brand>/`).
- **`curriculum/manifest.json`** carries this skill's `one_liner` and **README.md
  § Messaging Doc** quotes the flow; the menu and the site read both.
- **Four use cases read the latest doc under `my-work/messaging-doc/`** — the folder shape is
  load-bearing well beyond this skill. `/bluerock:competitive-intel` reads it to pre-fill a
  builder's differentiators; `/bluerock:aeo-visibility` reads it to build the buyer questions
  it proposes; `/bluerock:outreach-prep` reads it to pre-fill what the builder sells; and
  `/bluerock:signal-monitor` reads it to aim the "why it matters" line on every signal card.
  Change the folder shape and all four go quiet rather than failing loudly, since each is
  written to degrade honestly when it is absent.
