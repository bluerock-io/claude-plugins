---
name: signal-monitor
description: >-
  Signal Monitor — drop in your account list and get a signal digest: an
  act-this-week lane first, then worth-knowing, then the accounts that were checked
  and are genuinely quiet. Every signal dated, sourced, and framed against what you
  sell, with a suggested next touch. Use when I say "what's happening with my
  accounts", "check my account list", "any signals this week", "what moved on my
  accounts", "monitor these accounts", "did anything happen at <account>", "run my
  signal digest", or drop a list of accounts and ask what's new. Runs account-scanner
  (one per batch of 8, concurrently) → signal-analyst, and writes to
  my-work/signal-monitor/.
---

Run the Signal Monitor team and produce a **signal digest** — a board of what moved on the
builder's accounts, ranked so the first thing they read is the thing to do this week. You
orchestrate the agents; they do the work.

This is the wide read of the set: dozens of accounts, swept shallowly, because the question
is *"which of my accounts moved"* — not *"tell me everything about this account"*. When one
account turns out to matter, `/bluerock:scorecard` and `/bluerock:competitive-intel` are the
deep reads waiting for it.

**What it replaces:** checking each account by hand, one search at a time, and finding out
about the ones you missed from someone else.
**Time saved:** [PLACEHOLDER — DO NOT MERGE: fill from the timed manual baseline
(E6-26), with its provenance, e.g. "about N minutes, timed once by one person". Never a
bare "saves an hour".]

## First — anchor to the project

The digests, their working folder, and the `voice.md` / `objectives.md` the run reads all
live in the builder's project. Two generations exist: the project ships inside the workspace
image (usually the folder `my-workspace`); projects made before 2026-08 were cloned and carry
whatever name the builder chose. **Assume neither — identify it by its signature.** In an
SSH/cloud container the chat may start in the project itself or in the **home folder** with
the project one level down — both are normal. Identify it by signature, not name: run `ls`;
see `CLAUDE.md` and `design/` side by side? You're in the project. If not, find it:
`ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`, else `find ~ -maxdepth 3 -path
'*/design/dashboard.html'`. `cd` in, capture the **absolute path** with `pwd`, and use that
full path throughout. Can't find it? Ask the builder which folder their project is in.

## Before the questions — read what the builder already has

Check, without asking: `objectives.md` and `voice.md` at the project root, and the latest doc
under `my-work/messaging-doc/` if one exists. These sharpen the run — they are never required
for it. Here they do one specific job: the **why it matters** line on every card is the
builder's positioning applied to a fact, so a real messaging doc is the difference between
"they raised a Series B" and "they raised a Series B, and the team that would own this is the
one that grows first after a raise."

- **If they're real**, use them to pre-fill the intake below (propose, confirm, don't re-ask
  cold).
- **If they're placeholder templates or absent**, say so once, plainly, and keep moving:
  *"Your `objectives.md` / `voice.md` are still the placeholder templates, so I can rank these
  signals but I can't aim them at what you sell. Happy to run anyway — running
  `/bluerock:messaging-doc` on your site would sharpen future digests."* Never make setup
  homework the price of the first digest.

## Intake — one question per step, short, then confirm

Ask these one at a time. Keep each ask to a line or two; don't stack questions or explain the
whole flow up front.

**Skip what they already gave you.** If the opening request named a file or the accounts,
don't re-ask — say what you're taking as given (`List: target-accounts.csv · 34 accounts`) so
a wrong reading gets corrected early, then pick up at the first step that's actually missing.
A returning builder never re-answers a question they already answered; a prior run's
`inputs.md` pre-fills the same way (propose, confirm, don't re-ask cold).

**Which prompt shape for which step:** use the question picker (`AskUserQuestion`) only where
the answer is genuinely a choice between a few options — step 3. Everywhere else the answer is
free text in the builder's own words, and a four-option picker is the wrong shape for it: ask
in the message and let them type. Where the picker isn't available in this client, ask in the
message.

1. **The account list.** "Drop in your account list — a file is easiest. Names or domains both
   work, and dozens is fine." Accept a file path, a pasted list, or a file they attach; a CSV,
   a spreadsheet export, a markdown list, or plain lines all parse. **Read it and play back
   what you found**: the count, and the first few names, so a mis-parsed column is caught
   before it costs a scan. If the file has several columns, say which one you took as the
   account and offer to switch. **Domains beat names** — say so once here, because it is the
   single thing that reduces the skipped-entry list next run.
   - **Cap: 40 accounts per run.** If the list is longer, say so plainly and ask what they
     want: the first 40, or a subset they name. Don't silently truncate, and don't quietly
     run 200.
2. **What counts as a signal — in their words.** "What would make you want to reach out?
   Funding, hiring, a launch, a leadership change, pricing — or something specific to how you
   sell." **Take their answer verbatim and do not translate it into our categories.** If they
   say "anything about their support team", that is the definition, and a funding round is not
   a signal for them. Read it back in their words before moving on. This is the one input that
   decides what the whole run looks at.
3. **How far back.** Genuinely a choice — use the picker: *last 30 days (the default; matches
   "what did I miss")* · *last 90 days (a quarter, for a first run on a new list)* · *since my
   last digest (only when a previous run exists — offer this first when it does)*.
4. **What you sell, and to whom.** Pre-fill from the messaging doc or `objectives.md` when
   they're real and ask them to confirm rather than type it again. This is what the "why it
   matters" line is aimed with. If there's nothing on file and they'd rather not type it, take
   the skip — the digest says so on every card rather than inventing a positioning.
5. **Anything else that should shape this.** "A rep who owns some of these, an account you're
   already in a deal with, someone we shouldn't contact, a phrase to avoid. Optional — say
   'nothing' if there isn't anything."
6. **Confirm before we run.** Play back the list name and count, their signal definition in
   their words, the window, the positioning line, and notes as a short bullet list, then: "Good
   to go, or anything to edit?" **Carry all five inputs forward verbatim from here** — the
   signal definition and the notes are the builder's own words, and paraphrasing either is how
   a digest ends up ranking against a category they never named.

**The moment the builder approves**, set the expectation for the wait in one message of its
own, then go quiet until the report: the scans run concurrently across batches and take
several minutes on a list of this size, so say so plainly — this is a good moment to grab a
coffee or switch tasks, and the digest will be ready when they check back. No further chatter
between this and the report.

## Set up the run

7. **Make the working folder:** `my-work/signal-monitor/<YYYY-MM-DD>-<slug>/`, where the slug
   names the list (`target-accounts`, `q4-pipeline`). Dated on purpose — runs accumulate and
   are never overwritten; the history is what makes "what changed" and the quiet-two-runs-in-a-row
   finding possible. `my-work/` is builder-owned and never overwritten.
8. **Check for a previous run:** list `my-work/signal-monitor/`. If a prior dated folder holds
   a `signal-digest.md`, note its path and date — the analyst will dedupe against it and report
   what moved.
9. **Write `inputs.md`** into the working folder: the confirmed intake (the parsed account list,
   their signal definition **verbatim**, the window, the positioning line, notes) and which
   project files were real enough to read. This is the record of what shaped the digest, and the
   seed the next run pre-fills from.

## Run the agents

Dispatch these as ordinary subagents. Do not use agent-teams tooling; this runs identically in
every client.

10. **Split the accounts into batches of 8 and dispatch one `account-scanner` per batch — all
    in a single message so they run concurrently.** Thirty-four accounts is five scanners, not
    thirty-four; a subagent per account is what makes a dropped list unaffordable, and the whole
    design of this use case is that it stays cheap enough to run weekly. Each scanner gets: its
    batch of accounts, the builder's signal definition **verbatim**, the window, its batch
    number, and the working folder's **absolute path** in the dispatch prompt itself (a subagent
    starts wherever the session started; the path you pass is the handoff). Each writes a
    sourced `scan-batch-<n>.md`, bounded to **2 to 3 fetches per account**. Wait for all of them.
    - **The fetch bound is a promise the digest repeats.** Don't raise it to chase a thin run,
      and don't let a scanner quietly exceed it — the artifact's meta line states the bound to
      the builder, and a run that broke it makes that statement false.
    - **If the builder's notes mention a specific account** — a deal in flight, a rumour they
      heard, a rep who owns it — pass it to *that* account's scanner as an **unverified lead
      from the builder**, to come back sourced or come back unconfirmed. Never as a fact.
11. **Dispatch `signal-analyst`** with the working folder path and, when step 8 found one, the
    previous `signal-digest.md` path. It reads `inputs.md` and every scan — **no web tools, no
    new research** — and writes `signal-digest.md`: the four lanes in order, one card per signal
    (what happened, why it matters, next touch), the quiet accounts named, the unresolved entries
    named, and what changed since the previous run. The builder's signal definition, positioning,
    and notes reach it through `inputs.md` **verbatim** — that file carries their words, never a
    paraphrase.

## Publish the artifact — you, not the agents

12. When `signal-analyst` finishes, read `signal-digest.md` and **publish it as a Claude
    Artifact** yourself, in this conversation, following the design contract below. The agents
    write markdown only; the finished, shareable view is yours to render. If artifact publishing
    isn't available in my environment, don't block — the markdown is saved; say so and give the
    path.

### The artifact — design contract (follow it exactly)

**The artifact is a tool the builder operates on Monday morning, not a report they scroll**
(product decision, 2026-08-31). The act-this-week lane is on screen first; any account is
reachable in one click; lanes are scannable by color before they are read. Still read-only and
honest: no CTAs, no dead controls, nothing that pretends to fetch, send, or save — a dead
button in a sandboxed artifact is worse than no button. Interactivity is filtering, never
chrome.

**Filter chips, not tabs.** Competitive Intel gives each competitor a tab because four
competitors are four deep reads. A dropped account list can be dozens, and dozens of tabs is a
filing cabinet. The board is the default view; the chips narrow it.

A single self-contained HTML page. **CSP rules: exactly one external request, the Google Fonts
stylesheet below. All CSS in one `<style>` block, all JS inline (one small filter script), no
CDN scripts, no remote images.** Print-friendly: under `@media print` the chip row hides, every
card and every lane renders regardless of filter state, and a page break falls between lanes.

**Fonts** — one Google Fonts link, every face with a real fallback: `DM Sans` (display + body;
fallback `system-ui, -apple-system, sans-serif`), `Source Serif 4` (the "why it matters" and
next-touch lines; fallback `Georgia, serif`), `JetBrains Mono` (labels, meta, chips, dates;
fallback `ui-monospace, Menlo, monospace`).

**Theme — ship both, token-structured.** Bare `:root` carries the complete light palette;
`@media (prefers-color-scheme: dark)` guarded as `:root:not([data-theme="light"])` redefines
only the tokens; `:root[data-theme="dark"]` duplicates them. Every component rule uses `var()`
— no literal color outside the three token blocks. `body` background is `var(--paper)`.

**Tokens** (light / dark) — the same set as the battlecard, unchanged, so the two use cases
look like one product:

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

**The lane-to-token mapping is fixed**, and it carries the same semantic logic as the
battlecard — sourced facts and our own judgment never share a color:

| Lane / element | Token | Why |
|---|---|---|
| **Act this week** | `kill` | The urgent lane, warm and first |
| **Worth knowing** | `accent` | Informational, calm |
| **Quiet accounts** | `neutral` | A result, deliberately quiet on the page too |
| **Could not check** | `mine` | Same amber the battlecard uses for handle-with-care |
| **Next touch** (and it alone) | `bullet` | Ours to say — the same token the battlecard gives silver bullets |
| **Tier / `[unconfirmed]` markers** | `mine` mono tag | Same treatment as `[their claim]` |

**Structure** (max width 1000px):

1. **Sticky masthead** — uppercase display title (`SIGNAL DIGEST · <LIST NAME>` shape), mono
   meta line (`<date> · <N> accounts checked · <window> · 2–3 fetches per account · <first run
   or run N>`), then the **filter chip row**: an `All accounts` chip plus **one chip per checked
   account**, each carrying a small lane-colored dot for its state (act / worth / quiet).
   Buttons with `aria-pressed`, exactly one active at a time, `All accounts` active on load; the
   inline script toggles the `hidden` attribute on cards and lane sections. The chip row **is**
   the account list — that a builder can see all thirty of their accounts in one glance, colored
   by whether anything happened, is the point of chips over tabs.
   - Selecting an account shows that account's cards. **If the account is quiet, selecting it
     shows its quiet state in words** (`Checked <date>. Nothing in the window.`) — never an
     empty screen, because an empty screen reads as a bug where the finding is that there is
     nothing.
2. **Legend row** naming the four lanes with color dots: act this week · worth knowing · quiet
   (checked, nothing found) · could not check (not scanned).
3. **"Since your last run" strip** — only when a previous run existed: an accent-soft callout,
   dated, listing the analyst's "Since" items (or its "no account changed lane" line). Omit the
   block entirely on a first run.
4. **Act this week** — lane header with a kill-colored chip and the count, then the cards.
   **This lane renders first and is never collapsed**, including when it holds one card. When it
   holds none, it renders as a stated finding — `Nothing on this list needs action this week.` —
   never as a missing section.
5. **Worth knowing** — accent-chipped lane header and count, same card shape.
6. **Quiet accounts** — neutral-chipped header and count, then a compact multi-column grid of
   account names, each with `checked <date>`. **Never a bare number, never collapsed by
   default.** A one-line note above it states the finding plainly: `<N> of <M> accounts were
   checked and had nothing in the window.`
7. **Could not check** — mine-chipped header and count, one row per unresolved entry: the entry
   exactly as the builder wrote it, the candidates seen, and what would fix it (`add a domain`).
   Omit the whole section only when the scanners resolved everything.
8. **Coverage note + sources** — the analyst's coverage line (how many weak signals were
   dropped, anything that blocked a scan) and mono chips of the domains the scans actually used.
9. **Footer** — the separation-rule note (**what happened is sourced and dated; why it matters
   and the next touch are yours to say, not findings about the account**), the line **`Internal
   account material — not for circulation to customers or prospects`**, and `Built with BlueRock
   · Signal Monitor · account-scanner + signal-analyst`.

**The card**, in the two signal lanes:

- **Account name** (display, 20–26px, weight 800) + the builder's own signal category as a mono
  tag, + a lane-colored 4px left stripe on the card.
- **WHAT HAPPENED** — mono uppercase label; the dated finding in ink, with the date as a mono
  chip, the source as a mono chip (`<domain>`), and the tier as a small mine-colored mono tag.
  Carry every `[unconfirmed]` marker through — **never silently drop one.**
- **WHY IT MATTERS** — mono uppercase label; serif, in ink-2. Carries `[my read]` markers where
  the analyst set them. When the builder gave no positioning, this row carries the analyst's
  honest one-liner instead, and it is not styled to look like a finding.
- **NEXT TOUCH** — mono uppercase label; behind a bullet-colored left rule, the opening line in
  serif italic. Visually distinct from the two rows above it, because it is the one part of the
  card that is a suggestion rather than a fact.

**The scan test:** someone opening this on a phone with coffee in the other hand has about eight
seconds — the lane colors, the act-this-week count, and the account names must carry the board
before a single sentence is read.

## Finish

13. The **signal digest artifact** is the payoff. The `signal-digest.md` is the source of record
    the builder keeps and can push to their repo, and `inputs.md` beside it is what the next run
    pre-fills from.
14. **Report:** the folder path, the one line that matters (the single strongest act-this-week
    signal, or — when the lane is empty — the honest headline that nothing on the list needs
    action this week), and the artifact (or the fallback note). Don't reprint the digest.
15. **Offer the depth, after the run — never before it.** One beat, two doors, then stop:
    *"Want to see how this worked? Two agents ran it — a scanner that swept your accounts a few
    sources at a time and an analyst that ranked what it found against what you sell. The
    anatomy-of-an-agent and subagent-teams sessions explain the pattern — say 'teach me how this
    works'. And when one of these accounts is worth a proper look, `/bluerock:scorecard` is the
    deep read on a single company."*

## Honesty rules this skill carries

- **Sourced versus ours never blur.** What happened traces to a scan and carries a source and a
  date; why it matters and the next touch are the builder's positioning applied, labeled as
  ours. The analyst enforces it; the artifact preserves it in a different color.
- **A quiet account is a finding, and it ships as one.** Checked-with-nothing-found is the most
  common honest outcome on a real list, and hiding it would let the digest imply the run found
  more than it did.
- **Checked-and-quiet is never merged with could-not-check.** One was looked at; the other never
  was. Merging them is the one change to this tool that would make it lie about its coverage.
- **An entry that can't be disambiguated is named and skipped, never guessed.** A confident,
  sourced signal filed against the wrong company is worse than no signal at all.
- **The fetch bound is stated because it is a real limit.** This is a wide, shallow sweep. It
  will miss things a deep read would find, and the artifact says the bound out loud so the
  builder can calibrate rather than over-trust it.
- **Nothing unconfirmed reaches the act-this-week lane** — any Tier 3 item, and anything marked
  `[unconfirmed]` at any tier. The marker governs, not the tier number, and a high rank never
  overrides it; the item lands in worth-knowing with its marker intact and a next touch that
  finds out rather than acts.
- **Refresh, don't rot.** Signals go stale in weeks, not quarters. Every run is dated; when the
  previous run in `my-work/signal-monitor/` is more than a month old, say so in the report rather
  than treating the diff as a fresh picture.
- **The time-saved line above ships only with a timed figure and its provenance.**

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`agents/signal-analyst.md` owns the lane names** (Act this week, Worth knowing, Quiet
  accounts, Could not check) **and the three card part names** (What happened, Why it matters,
  Next touch); this skill's artifact contract renders all of them by name and order. Reword them
  in either file and the artifact loses sections silently.
- **`agents/account-scanner.md` owns the scan section names** (Signals, Context, Could not
  resolve, Coverage note); the analyst reads scans by section, and its **Could not check** lane
  is built from **Could not resolve** specifically — the one cross-file hook where the two files
  use different words for the same thing on purpose (the scanner reports what it could not
  resolve; the digest reports what the builder could not have checked). The scan filename shape
  `scan-batch-<n>.md` is matched by the analyst's Glob. **The 2–3 fetches per account bound is
  stated in three places** — the scanner, this skill's step 10, and the artifact meta line — and
  changing it means changing all three or shipping a false statement to the builder.
- **The batch size of 8 is shared** between step 10 and the scanner's "up to 8" contract. It is
  what keeps a 40-account list to five subagents.
- **`curriculum/manifest.json`** carries this skill's `one_liner`, `artifact`, `time_saved`, and
  `team` — the menu and the site read them; keep them in step with the opening lines here.
- **README.md § Signal Monitor** quotes the intake shape and the lane names.
- The working folder shape `my-work/signal-monitor/<YYYY-MM-DD>-<slug>/` is what makes run
  history findable, and the dedupe in the analyst depends on it; `/bluerock:wrap-up` logs runs
  against the agent-team label **Signal Monitor** with members `account-scanner` +
  `signal-analyst` (the Account Research roll-up shape).
- **The flow doc mirrors this skill** (content repo, private:
  `09-product/use-case-flows/signal-monitor-flow.md`) — any change to the intake, dispatch,
  artifact, or close updates it in the same pass.
