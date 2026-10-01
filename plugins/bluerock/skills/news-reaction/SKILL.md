---
name: news-reaction
description: >-
  Verified News Reaction — point an agent team at a news story or announcement
  and get a reaction kit: the claims in it checked against independent sources,
  what was dropped and why, your angle on it, and drafted posts in your voice
  that only say what checked out. Use when I say "react to this", "should I post
  about this", "draft a post on this story", "is this true", "fact-check this
  before I share it", "write a take on this announcement", or paste a news link
  and ask what to say about it. Runs fact-checker → reaction-writer and writes to
  my-work/news-reaction/. Holds the drafts when the story is not confirmed yet.
---

Run the Verified News Reaction team on one story and produce a **reaction kit**: the facts
checked, the drafts written from only the facts that held. You orchestrate two agents; they
do the work. The order is the point. The fact-checker runs first and can stop the
reaction-writer, because a post that repeats a wrong claim costs the builder more than no
post.

**What it replaces:** reading a story, checking whether it is true, finding what it means for
what you sell, and drafting the post, by hand.
**Time saved:** about 45 minutes by hand, estimated and not yet timed. The timed baseline
(E6-26) replaces this figure when it lands.

## First — anchor to the project

The kit, its working folder, and the `voice.md` / `objectives.md` the run reads all live in
the builder's project. Two generations exist: the project ships inside the workspace image
(usually the folder `my-workspace`); projects made before 2026-08 were cloned and carry
whatever name the builder chose. **Assume neither — identify it by its signature.** In an
SSH/cloud container the chat may start in the project itself or in the **home folder** with
the project one level down — both are normal. Identify it by signature, not name: run `ls`;
see `CLAUDE.md` and `design/` side by side? You're in the project. If not, find it:
`ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`, else `find ~ -maxdepth 3 -path
'*/design/dashboard.html'`. `cd` in, capture the **absolute path** with `pwd`, and use that
full path throughout. Can't find it? Ask the builder which folder their project is in.

## Before the questions — read what the builder already has

Check, without asking: `objectives.md` and `voice.md` at the project root, the latest doc
under `my-work/messaging-doc/`, and `inputs.md` from the most recent run under
`my-work/news-reaction/`. These sharpen the run; they are never required for it. Here they do
one job each: the positioning decides what the story means *for this builder*, and the voice
decides whether the drafts sound like them.

- **If they're real**, use them to pre-fill the intake below (propose, confirm, don't re-ask
  cold).
- **If they're placeholder templates or absent**, say so once, plainly, and keep moving:
  *"Your `objectives.md` / `voice.md` are still the placeholder templates, so the facts will
  be checked but the angle and the voice will be generic. Happy to run anyway; running
  `/bluerock:onboard` would sharpen future kits."* Never make setup homework the price of the
  first kit.

## Intake — one question per step, short, then confirm

Ask these one at a time. Keep each ask to a line or two; don't stack questions or explain the
whole flow up front.

**Skip what they already gave you.** If the opening request carried a link or pasted text,
don't re-ask: say what you're taking as given (`Story: theverge.com/… · posting to LinkedIn`)
so a wrong reading gets corrected early, then pick up at the first step that's actually
missing. A returning builder never re-answers what a prior run's `inputs.md` already holds.

**Which prompt shape for which step:** use the question picker (`AskUserQuestion`) only at
step 3, where the answer is genuinely a choice among a few. Everywhere else the answer is free
text in the builder's own words; ask in the message and let them type. Where the picker isn't
available in this client, ask in the message.

1. **The story.** "Paste the link, or the text if it's behind a paywall." A link is best,
   because the fact-checker reads the original. **A headline alone is not enough**: ask for the
   link or the text rather than searching for it and reacting to whatever turns up.
2. **What you sell, and to whom.** Pre-fill from the messaging doc or `objectives.md` and
   confirm. Ask only if both are absent: *"One line: what do you sell, and to whom?"* This is
   what relevance is scored against and what the angle is built on. If they skip it, the kit
   says relevance was not assessed rather than inventing a market for them.
3. **Where you'll post it.** Genuinely a choice; use the picker, more than one allowed:
   *LinkedIn post* · *X post* · *Note to customers or prospects* · *Note to my team*. Default
   to LinkedIn if they say "whatever".
4. **Anything that should shape it.** "A view you already hold on this, a claim you can't
   make, a competitor not to name, a phrase to avoid. Optional; say 'nothing' if there isn't
   anything."
5. **Confirm before we run.** Play back the story, the positioning line, the channels, and the
   notes as a short bullet list, then: *"Good to go, or anything to edit?"* **Play the inputs
   back; do not pre-judge the story.** Nothing has been checked yet, so "this looks big" or
   "this seems shaky" here is a guess in the tone of a finding. **Carry all four inputs forward
   verbatim**; the positioning and notes are the builder's own words.

**The moment the builder approves**, say in one line that the fact-checker reads the story
first and checks the claims before anything gets drafted, so it takes a few minutes. Then go
quiet until the report.

## Set up the run

6. **Make the working folder:** `my-work/news-reaction/<YYYY-MM-DD>-<slug>/`, where the slug
   names the story in three or four words. Dated on purpose: runs accumulate and are never
   overwritten. `my-work/` is builder-owned and never overwritten.
7. **Check for an earlier reaction to the same story.** Read the `inputs.md` of every prior
   folder under `my-work/news-reaction/` and compare the link. If one matches, tell the builder
   before running: *"You reacted to this on <date>. Run again for what's changed since, or
   stop here?"* On a re-run, record the earlier folder in `inputs.md` as `Prior runs:` so the
   fact-checker reports what is new.
8. **Write `inputs.md`** into the working folder: the confirmed intake (link or "pasted",
   positioning, channels, notes, verbatim), which project files were real enough to read, and
   any `Prior runs:` line. **If the builder pasted text, save it verbatim as `source.md`**
   beside it. The agents read files, not this conversation; an answer you did not save is an
   answer they never saw.

## Run the agents, in order

Dispatch these as ordinary subagents, one at a time, waiting for each. Do not use agent-teams
tooling; this runs identically in every client. Pass the working folder's **absolute path** in
each dispatch prompt (a subagent starts wherever the session started; the path you pass is
the handoff).

9. **Dispatch `fact-checker`** with the working folder. It reads `inputs.md` (and `source.md`
   if present), classifies the source, checks the claims, scores relevance, and writes
   `check.md`, bounded to 6 to 8 fetches. Wait for it.
   - **If `check.md` says `Could not read the item`**, stop. Ask the builder to paste the text,
     save it as `source.md`, and dispatch the fact-checker again. Do not continue to the
     writer on a story nobody has read.
10. **Dispatch `reaction-writer`** with the same folder. It reads `check.md`, `inputs.md`, and
    the project's `voice.md` / `objectives.md` / messaging doc if present, and writes
    `reaction-kit.md`. It does no research. **On a Hold verdict it writes the kit without
    drafts, and that is the run working, not failing.**

## Publish the artifact — you, not the agents

11. When `reaction-writer` finishes, read `reaction-kit.md` and **publish it as a Claude
    Artifact** yourself, in this conversation, following the design contract below. The agents
    write markdown only; the finished, shareable view is yours to render. If artifact
    publishing isn't available in my environment, don't block: the markdown is saved; say so
    and give the path.

### The artifact — design contract (follow it exactly)

**The artifact is a tool the builder uses at the moment of posting, not a report they
scroll** (product decision, 2026-08-31). One view on screen at a time, reachable in one
click; claim status readable by color before it is read. Read-only and honest: no CTAs, no
dead controls, no copy or post buttons, nothing that pretends to fetch or save.

A single self-contained HTML page. **CSP rules: exactly one external request, the Google Fonts
stylesheet below. All CSS in one `<style>` block, all JS inline (one small tab script), no CDN
scripts, no remote images.** Print-friendly: under `@media print` the tab strip hides and
`.panel[hidden] { display: block }` renders every view in sequence.

**Fonts** — one Google Fonts link, every face with a real fallback: `DM Sans` (display + body;
fallback `system-ui, -apple-system, sans-serif`), `Source Serif 4` (the drafts and the angle;
fallback `Georgia, serif`), `JetBrains Mono` (labels, meta, chips, character counts; fallback
`ui-monospace, Menlo, monospace`).

**Theme — ship both, token-structured.** Bare `:root` carries the complete light palette;
`@media (prefers-color-scheme: dark)` guarded as `:root:not([data-theme="light"])` redefines
only the tokens; `:root[data-theme="dark"]` duplicates them. Every component rule uses `var()`
— no literal color outside the three token blocks. `body` background is `var(--paper)`.

**Tokens** (light / dark), the same table as Competitive Intel:

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
| chip text (on status-colored chips) | `#FFFFFF` | `#14171E` |

**What the colors mean here.** One meaning per color, on every view:

| Color | Claim status | Verdict | Timing | Relevance | Dropped and corrected | Source type |
|---|---|---|---|---|---|---|
| `bullet` | Confirmed | Draft | React today | High | — | Primary, Established outlet |
| `mine` | Single source | Draft with caveats | This week | Medium | Corrected, Attributed only | — |
| `kill` | Contradicted, Not confirmed | Hold | Wait for confirmation | — | Dropped | — |
| `neutral` | — | — | Let it pass | Low, Not assessed | — | Secondary, Not read |

A relevance qualifier the fact-checker added ("High (if true)") keeps its color and prints its
words.

**Structure** (max width 880px):

1. **Sticky masthead** — the title is `reaction-kit.md`'s H1 without ` — reaction kit`
   (display, 24–32px, weight 800); a mono meta line `<outlet> · <source type> · published
   <date> · checked <run date>`, the run date being the date in the working folder's name;
   then the **verdict strip**: three chips in one row, Verdict · Timing · Relevance, each in
   its color from the table above. **Directly beneath the strip, the Verdict section's caveat
   line, when there is one**, in a mine-soft block; it is the line a builder most needs before
   copying a draft. Beneath it, the Verdict section's relevance sentence in ink-2, because
   that line is the builder's positioning applied to the story. The voice fallback line, when the kit carries it, sits under the meta line
   in small ink-3 italic. Then the **tab strip**: `Drafts` · `Facts checked` · `Sources`, `role="tab"` buttons
   with `aria-selected`, 3px accent underline; panels are `<section role="tabpanel">` toggled
   via `hidden` (Drafts visible on load). The whole masthead is sticky at desktop width;
   under 600px only the tab strip sticks, so the header never fills a phone screen.
2. **Drafts** panel:
   - **Your angle** — accent-soft callout, 3px accent left border, a mono `YOUR ANGLE` label
     inside it and the one sentence in serif; no separate heading above it. Exactly one block
     on the page gets this treatment.
   - **One card per draft**, labeled with the channel and a mono `DRAFT` tag; X drafts carry
     their character count in mono. The draft text in serif, `white-space: pre-wrap`, inside a
     card-2 block so it reads as text to copy by hand. The `Link to add` line beneath in mono.
   - **On Hold**: no draft cards. The panel carries **Why there are no drafts yet** in a
     kill-soft block, and the tab label reads `Drafts (held)`. Never render an empty card.
   - **Before you post** — the checklist as plain list items with an empty square glyph, not
     form controls (no dead checkboxes).
3. **Facts checked** panel:
   - **The story** — the two sentences and the kit's Source line, then one numbered item-card
     per row of **Facts you can use**: a 4px left stripe and a chip in its status color, the
     fact, the `Line in the item` in serif italic inside quotation marks, one mono chip per
     confirming source (the `Source` column split on ` · `), and the `Note`, when present, in
     small ink-3 beneath.
   - **Dropped and corrected** — section note `What changed before drafting.`; one row per
     item, its chip (Dropped, Corrected, or Attributed only) in its color from the table
     above, then what the story said → what the better source says. When nothing was dropped,
     one quiet neutral line: `Nothing dropped. Every claim the drafts lean on checked out.`
   - **Claim trace** — the trace table inside a bordered `overflow-x: auto` container.
4. **Sources** panel — one row per URL in `check.md`'s Sources: the domain in mono, the
   source type as a chip in its color from the table above (a fetch that failed is `Not
   read`), the full URL as plain text, and the fact-checker's note on it in ink-3. Web
   searches with no URL are not rows.
5. **Footer** — `Drafts only. Nothing here has been posted.` and `Built with BlueRock ·
   Verified News Reaction · fact-checker + reaction-writer`.

**The scan test:** a builder about to post has about five seconds. The verdict strip and the
claim colors must tell them whether it is safe to post before they read a sentence.

## Finish

12. The **reaction kit artifact** is the payoff. `reaction-kit.md` is the source of record the
    builder keeps; `check.md` beside it is the evidence; `inputs.md` is what the next run
    pre-fills from.
13. **Report:** the folder path, the verdict and timing in one line, the one claim that was
    dropped or corrected if there was one (that is usually the line worth reading), and the
    artifact (or the fallback note). Don't reprint the drafts.
14. **Offer the depth, after the run, never before it.** One beat, then stop: *"Want to see
    how this worked? Two agents ran it: a fact-checker that read the story and checked each
    claim, and a writer that could only use what checked out. The subagent-teams session
    explains the pattern; say 'teach me how this works'."*

## Honesty rules this skill carries

- **Checked before drafted, every time.** The writer never runs before `check.md` exists, and
  never runs on a story nobody could read.
- **A Hold is a result.** Say it plainly in the report. A builder who did not post something
  wrong got what this use case is for.
- **The builder's positioning, never ours.** Relevance and the angle come from what they sell.
  With no positioning on file, relevance is `Not assessed`; it is never filled with a guess.
- **Drafts only.** Nothing is posted, sent, or scheduled. The kit says so.
- **The time-saved line above ships only with a timed figure and its provenance.**

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`agents/fact-checker.md` owns `check.md`'s section names** (Source, Claims, Dropped and
  corrected, Relevance, Verdict, Sources), **the four claim statuses** (Confirmed, Single
  source, Contradicted, Not confirmed), **the three verdicts** (Draft, Draft with caveats,
  Hold), **the four timings**, and the `Could not read the item` line this skill stops on.
  `agents/reaction-writer.md` reads all of them by name, and this skill's color map renders
  them. Rename one in any file and it changes in all three.
- **`agents/reaction-writer.md` owns `reaction-kit.md`'s section names** (The story, Verdict,
  Your angle, Drafts, Facts you can use, Dropped and corrected, Claim trace, Before you post,
  and Why there are no drafts yet on Hold); this skill's artifact contract renders them by
  name, and owns the three Dropped-and-corrected labels (Dropped, Corrected, Attributed only)
  that the color table renders. The four channel names are shared between the intake's picker (step 3) and the
  writer's draft list.
- **`inputs.md` is the contract between this skill and both agents.** The positioning line is
  what relevance is scored against; the notes are hard rules for the writer. The `Prior runs:`
  line is how a re-run reports what changed.
- **`curriculum/manifest.json`** carries this skill's `title`, `one_liner`, `artifact`,
  `time_saved`, and `team`; the menu and the site read them. Keep them in step with the
  opening lines here.
- The working folder shape `my-work/news-reaction/<YYYY-MM-DD>-<slug>/` is what step 7's
  same-story check reads; `/bluerock:wrap-up` logs runs against the agent-team label
  **Verified News Reaction** with members `fact-checker` + `reaction-writer`.
- **Generalized from two BlueRock-internal skills** (`industry-intel` for relevance scoring
  against positioning and the same-story check, `industry-pov` for the source gate, the
  mechanism check, and the dropped-claims log). Those stay BlueRock's; nothing here reads them.
