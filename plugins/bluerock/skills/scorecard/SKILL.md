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

## Before the questions — read what the builder already has

Check, without asking: `objectives.md` and `voice.md` at the project root, the latest doc
under `my-work/messaging-doc/`, and `inputs.md` from the most recent run under
`my-work/account-scorecard/`.

- **If they're real**, use them to pre-fill the intake below — propose and confirm, don't
  re-ask cold. A returning builder never re-answers a question they already answered.
- **If they're placeholder templates or absent**, say so once and keep moving. Never make
  setup homework the price of the first scorecard.

## Intake — one question per step, short, then confirm

**This card rates Fit, Timing, and Reachability. Every question below exists to make one
of those three mean something.** Rating fit without knowing what the builder sells is
guessing confidently, and a builder who knows their own market spots it in one read. If a
question would not change a rating, it does not belong here.

Ask one at a time. Keep each to a line or two; don't stack them or explain the flow up
front. **Skip anything the opening request already gave you** — say what you're taking as
given (`Target: OnTrac · Fit criteria from objectives.md`) so a wrong reading gets
corrected early, then pick up at the first step actually missing.

**Which prompt shape:** use the question picker (`AskUserQuestion`) only at step 4, where
the answer is genuinely a choice among a few. Everywhere else the answer is free text in
the builder's own words — ask in the message and let them type.

1. **The target.** A company name, plus any hint (sector, region, domain) if the name is
   ambiguous. If it's genuinely ambiguous, resolve it before spending the run. **A URL is a
   fine answer** — take it as the disambiguating hint and hand it to the scout as a page to
   start from, rather than asking for the name a second time.
2. **What you sell.** Pre-fill from `objectives.md` or the messaging doc and confirm.
   Ask only if both are absent: *"One line — what do you sell, and to whom?"* → **Fit**
3. **What a good account looks like for you.** *"Two or three real criteria beat a profile
   document — size, sector, who signs."* → **Fit**
   - **3a — if they have nothing written down**, offer the route rather than leaving them
     stuck: *"Want me to pull that out with three questions?"* If they take it, ask **one
     at a time**: (1) Who was your best customer last year? (2) What did they have in
     common with the one before? (3) Who is never a fit, however interested they seem?
     Read the criteria back as a list and let them correct it before moving on.
4. **What makes timing good for you.** Offer the common signals and let them add their
   own: new leadership · funding · a renewal window · hiring in the function · a public
   change in their business. → **Timing**
5. **Who you'd need to reach.** *"The function or title that would own this."* Optional,
   and say plainly what skipping costs: *"without it, Reachability is a general read
   rather than a read on your way in."* → **Reachability**
**Offer, never block.** Steps 2 to 5 sharpen the run; none of them is the price of the
first card. If the builder says "just run it," run it — and say in one line what the card
will be without them (*"Fit will be scored against a general profile"*) rather than asking
again.

6. **Confirm before we run.** Play back target, what they sell, fit criteria, timing
   signals, and the target function as a short bullet list, then: *"Good to go, or
   anything to edit?"* **Play the inputs back; do not pre-judge the account against them.**
   You have not scanned anything yet, so a size, a sector, or a fit tension asserted here
   is a guess wearing the tone of a finding — and being confidently wrong in the one moment
   you're asking the builder to trust the inputs is expensive. Anything that reads like a
   verdict waits for `scan.md`. **Carry all of it forward verbatim** — these are the builder's own
   words, and paraphrasing is how a card ends up asserting something they never said.

## Setup

1. **Make the working folder.** Slugify the name → `my-work/account-scorecard/<slug>/`.
   Create it. `my-work/` is builder-owned and never overwritten.
2. **Write `inputs.md` before dispatching.** The confirmed intake, verbatim, in the
   working folder. Two reasons: the agents read files rather than this conversation, so an
   unsaved answer is invisible to them; and the next run pre-fills from it instead of
   starting cold.

## Run the agents, in order

Dispatch these as ordinary subagents, one at a time, waiting for each. Do not use
agent-teams tooling; this runs identically in every client.

3. **Dispatch `scout`** with the company (+ hint) and the working folder. It writes a
   quick, sourced `scan.md` (what they do and what they sell, headquarters, employees,
   estimated revenue, stage, recent signal). It's bounded to a handful of fetches — let it
   be fast. Wait for it.
4. **Dispatch `scorer`** with the same folder. It reads `scan.md` and **`inputs.md`**
   (plus `voice.md` / `objectives.md` from the project root if present) and writes
   `scorecard.md`. Wait for it. **`inputs.md` is what makes the three ratings mean
   something** — the fit criteria, the timing signals, and the target function reach the
   scorer through that file and nowhere else, so an intake answer you didn't save is an
   answer the card was never scored against.

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
4. **Three dimension rows**, stacked — **the page's focal point, and the only part that
   has to read at a glance.** Each row is a block with a **3px left border in its rating
   color**, running the row's full height (`padding-left: 16px`), so the three ratings read
   as three colored bars down the page. This is the one element that survives the card being
   shrunk to a thumbnail where no text is legible, so it is not optional. Inside: the label
   (`Fit` / `Timing` / `Reachability`, small uppercase, letter-spacing) and a **rating pill**
   (`High` / `Medium` / `Low`), then the scorer's **verdict line** in body ink at the base
   size.
   - **The verdict line is clamped to two lines** (`display: -webkit-box; -webkit-line-clamp:
     2; -webkit-box-orient: vertical; overflow: hidden;`) so one long rationale cannot turn
     the row back into prose. The scorer writes it to stand alone, so nothing is lost.
   - **The scorer's detail, where it wrote any, renders beneath the row** at `13px` in muted
     ink, with no border and a `10px` top margin. It is depth for the reader who wants it,
     visibly subordinate to the verdict line. (The Fit no-objectives caveat renders here.)
   - **`Not assessed`** renders that word in the pill, in the neutral treatment, and its
     left border uses the border hairline `#E7E0D6` rather than a rating color — a visible
     blank, not a low score, and the two must not look alike.
5. **Why now** — the page's one highlighted callout: cream tint background, a 3px
   accent-blue left border, the one sentence in heading ink at `16px`. **Exactly one block
   on the page gets this treatment, and it is this one.** The accent is what tells the eye
   where the answer is; spend it twice and it stops pointing at anything.

6. **Recommended next step** — its own block, labeled, the concrete step in body ink.
7. **Footer** — small muted text, two lines: `Built with BlueRock · Account Scorecard ·
   scout + scorer`, and beneath it the scan's source domains as plain muted text separated
   by ` · `. **No chip row.** A wrapped grid of domain pills costs a third of the page's
   height for a fact the header subline already states as `<N> sources`, and in a screenshot
   it reads as decoration. Keep to the domains the scout actually used, and mark any it
   flagged `unverified`.

**Three honesty marks cut across the layout above.** They are not sections of their own;
each lands inside the block it belongs to.

**A confidence mark on the research itself, when the scan warrants one.** The three
ratings say how good the *account* looks. They say nothing about how much to trust what
was found, and those are different axes. Where the scan came back thin or contested, carry
a small uppercase chip beside the company name in the header: `THIN PUBLIC FOOTPRINT`,
`RECENT ACTIVITY — UNVERIFIED`, or `VERIFY BEFORE OUTREACH`. **No chip when the scan was
clean** — a badge on every card is decoration and stops being read.

**Absence gets a reason and a remedy, never a shrug.** When something could not be found,
say what was looked for, why it is missing, and what would close it. *"No named contact in
the function that would own this"* is a fact. *"...no public profile matched the function
in this region; the fastest close is an existing contact or your CRM rather than more
public search"* is the same fact made useful. **State plainly when an absence is a gap in
the research rather than a fact about the company** — the two read identically on the page
and mean opposite things.

**Show what was ruled out when the name was ambiguous.** If disambiguation cost real work,
name it: *"three unrelated companies share this name; this is the one in <region> with
<signal>."* Naming what was excluded is what makes the rest of the card trustworthy, and a
reader who spots an unflagged collision stops believing everything above it.

**Palette** (Builders "cool-paper", light-only — use these hex values directly since the
Artifact can't read the app's CSS variables):
- Page background `#F5F1EA`; card surface `#FFFFFF`; card border `#E7E0D6`, radius `14px`.
- Cream (the "cream tint" / "cream fill" above): `#F5F1EA` — the page-background value
  reused as a tint on the white card.
- Ink: heading `#1B2130`, body `#3D4658`, muted `#7B8494`.
- Accent (BlueRock blue) `#1559C4`.
- Rating pills: **High** bg `#E4F0E9` / text `#2F6B4C`; **Medium** bg `#F7ECD6` / text
  `#8A5A12`; **Low** bg `#EDEEF1` / text `#5A6272`. **Not assessed:** no fill, a `#E7E0D6`
  hairline border, text `#7B8494` — deliberately quieter than Low, because it is the
  absence of a rating rather than a bad one. Pills render at `padding: 4px 14px;
  font-weight: 600;` — the palette is deliberately soft for reading, so the pill needs the
  weight to stay legible when the card is scaled down.
- **Dimension left borders** use the pill's *text* color, which is the saturated one:
  High `#2F6B4C`, Medium `#8A5A12`, Low `#5A6272`, Not assessed `#E7E0D6`.

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

**The intake does not make it slow, and it is worth being precise about why.** The scan is
what costs time and it is unchanged. The criteria questions are asked once, saved to
`inputs.md`, and pre-filled from `objectives.md` or the previous run after that — so the
second target and every one after is a name and a confirm. **What the intake buys is the
difference between three ratings scored against criteria the builder gave and three
ratings scored against criteria the agent invented**, which is the difference between a
card they trust and a card they check.
For the deep, multi-section dossier, that's the Account Research team (`researcher →
signal-scanner → composer`) the builder has in their own project.

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`skills/learn-meet-your-first-agent-team/SKILL.md` narrates this skill as its sales
  and operations lane**: its lane table and steps name the agents (`scout` → `scorer`),
  the folder (`my-work/account-scorecard/<company>/`), and the three dimensions (Fit,
  Timing, Reachability). Renaming any of them here strands that session's narration.
- **`inputs.md` is a contract between this skill and `agents/scorer.md`.** This skill
  writes it from the intake; the scorer reads it as the rubric for Fit, Timing, and
  Reachability. Renaming the file, or changing which intake answers land in it, silently
  changes what the three ratings are scored against.
- **`agents/scout.md` owns `scan.md`'s fixed section shape** and `agents/scorer.md` reads
  it by section; this skill's artifact contract renders `scorecard.md`'s order. The
  three-outcome honesty rule on revenue and headcount (stated / `[estimated]` / `Not
  disclosed`) is stated in all three places — keep the wording in step.
- **`curriculum/manifest.json`** carries this skill's `one_liner` and **README.md
  § Account Scorecard** quotes the flow; the menu and the site read both.
