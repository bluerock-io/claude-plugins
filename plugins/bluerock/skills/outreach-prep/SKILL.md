---
name: outreach-prep
description: >-
  Personalized Outreach — point an agent team at the people you want to reach and get an
  outreach kit: one panel per prospect with who they are and why now (sourced), the angle,
  a draft in your voice, and follow-up beats. Use when I say "research these prospects",
  "prep me for outreach to <name>", "who is <name> at <company>", "write a cold email to
  <name>", "draft outreach for these four", "personalize this outreach", or name people I
  want to write to. Runs prospect-scanner (once per prospect, up to 4, concurrently) →
  outreach-writer, and writes to my-work/outreach-prep/. Nothing is ever sent — the kit is
  yours to edit and send yourself.
---

Run the Personalized Outreach team and produce an **outreach kit** — one panel per
prospect, ready to edit and send. You orchestrate the agents; they do the work.

The job this replaces is the one nobody has time for: researching one prospect properly
takes longer than writing to them, so most outreach ships generic. This run does the
reading — up to four people at once, sourced — and hands back drafts that could only have
been written by someone who did it.

**What it replaces:** researching prospects one at a time before writing to them, and
writing the message generically when the research doesn't happen.
**Time saved:** about 1 hour by hand, estimated and not yet timed. The timed
baseline (E6-26) replaces this figure when it lands.

**This tool never sends anything.** It researches and drafts. Every message in the kit is
a draft waiting for the builder to read it, change it, and send it from their own account.
There is no send step, no sequence, and no CRM write — say so plainly if asked, and see
§ Honesty rules.

## First — anchor to the project

The kit, its working folder, and the `voice.md` / `objectives.md` the run reads all live
in the builder's project. Two generations exist: the project ships inside the workspace
image (usually the folder `my-workspace`); projects made before 2026-08 were cloned and
carry whatever name the builder chose. **Assume neither — identify it by its signature.**
In an SSH/cloud container the chat may start in the project itself or in the **home
folder** with the project one level down — both are normal. Identify it by signature, not
name: run `ls`; see `CLAUDE.md` and `design/` side by side? You're in the project. If not,
find it: `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`, else
`find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` in, capture the **absolute
path** with `pwd`, and use that full path throughout. Can't find it? Ask the builder which
folder their project is in.

## Before the questions — read what the builder already has

Check, without asking: `objectives.md` and `voice.md` at the project root, whether
`writing-samples/` holds anything, and the latest doc under `my-work/messaging-doc/` if
one exists. These sharpen the run — they are never required for it.

- **If they're real**, use them to pre-fill the intake below (propose, confirm, don't
  re-ask cold).
- **`voice.md` matters more here than on any other use case**, because this run writes
  something the builder puts their name on. If it's a placeholder or absent, say so once,
  plainly, and keep moving: *"Your `voice.md` is still the placeholder template, so these
  drafts will be neutral rather than yours — you'll be rewriting them more than you'd
  like. Happy to run anyway; `/bluerock:onboard` fixes it for every future run."* Never
  make setup homework the price of the first kit.
- **If the builder has their own positioning, a one-pager, or a pitch doc**, they can name
  or paste it at any step — it feeds the same slot as what they're selling.

## Intake — one question per step, short, then confirm

Ask these one at a time. Keep each ask to a line or two; don't stack questions or explain
the whole flow up front.

**Skip what they already gave you.** If the opening request named the people or the
company, don't re-ask — say what you're taking as given (`Prospects: Dana Okafor, Priya
Raman · Company: Acme`) so a wrong reading gets corrected early, then pick up at the first
step that's actually missing. A returning builder never re-answers a question they already
answered; a prior run's `inputs.md` pre-fills the same way (propose, confirm, don't re-ask
cold).

**Which prompt shape for which step:** use the question picker (`AskUserQuestion`) only
where the answer is genuinely a choice between a few options — steps 2a and 3. Everywhere
else the answer is free text in the builder's own words, and a four-option picker is the
wrong shape for it: ask in the message and let them type. Where the picker isn't available
in this client, ask in the message.

1. **Who you're writing to.** "Who are we reaching? Names plus their company — a LinkedIn
   URL is better if you have one, because it removes the guessing on common names. Cap is
   4 per run." Four is deliberate: the reading is the expensive part, and a run that
   researches twelve people shallowly is the generic outreach this replaces.
2. **What you're selling.** "What are you offering them? A couple of real sentences in
   your own words beat a polished paragraph." (Pre-fill from the messaging doc or
   `objectives.md` when they exist and confirm instead.) The angle is built **only** from
   here — never fabricate an offer.
   - **2a — if they have nothing written down**, offer the route rather than leaving them
     stuck: *"Want me to pull it out with three questions?"* (options: yes, ask me the
     three · I'll write it myself · skip it — the panels will say the angle was built
     without it). If they take the three, ask **one at a time**:
     1. What problem do you solve, in the words a customer uses for it?
     2. Who has that problem worst, and how would I recognize them?
     3. What happens to them if they do nothing?
     Then read their answers back as a short offer description and let them correct it
     before moving on.
3. **The channel.** Ask it as a picker, because the draft's whole shape depends on it and
   there are four real answers: email · LinkedIn message · LinkedIn connection note ·
   call opener. One channel per run — a message written for an inbox is not a message
   written for a connection request, and a kit that hedges across both is a kit the
   builder rewrites.
4. **Anything shaping this.** "Anything else I should know? A warm intro or a mutual
   contact, an event you both attended, a past conversation, a claim you're not allowed to
   make, a phrase to avoid, a competitor already in there. Optional — say 'nothing' if
   there isn't anything." A warm intro is the highest-value thing in this box and most
   builders won't think to mention it, so name it first in the ask.
5. **Confirm before we run.** Play back the prospects, what they're selling, the channel,
   and the notes as a short bullet list, then: "Good to go, or anything to edit?" **Carry
   all four inputs forward verbatim from here** — what they sell and their notes are the
   builder's own words, and paraphrasing either is how a draft ends up claiming something
   they never said.

**The moment the builder approves**, set the expectation for the wait in one message of
its own, then go quiet until the report: the scans run concurrently and take several
minutes, so say so plainly — this is a good moment to grab a coffee or switch tasks, and
the kit will be ready when they check back. No further chatter between this and the
report.

## Set up the run

6. **Make the working folder:** `my-work/outreach-prep/<YYYY-MM-DD>-<slug>/`, where the
   slug names the account or the lead prospect. Dated on purpose — runs accumulate and are
   never overwritten; the history is what stops a second kit reusing an opener the builder
   already sent. `my-work/` is builder-owned and never overwritten.
7. **Check for a previous run:** list `my-work/outreach-prep/`. If a prior dated folder
   holds an `outreach-kit.md`, note its path and date — the writer will report what changed
   and will not repeat an opener already used on the same person.
8. **Write `inputs.md`** into the working folder: the confirmed intake (prospects, what
   they're selling, the channel, notes) and which project files were real enough to read.
   This is the record of what shaped the kit, and the seed the next run pre-fills from.

## Run the agents

Dispatch these as ordinary subagents. Do not use agent-teams tooling; this runs
identically in every client.

9. **Dispatch one `prospect-scanner` per prospect — all in a single message so they run
   concurrently.** Each gets: its one prospect (name, LinkedIn URL if given, their
   company), what the builder sells (so it can spend its fetches where the relevance is),
   and the working folder's **absolute path** in the dispatch prompt itself (a subagent
   starts wherever the session started; the path you pass is the handoff). Each writes a
   sourced `scan-<prospect-slug>.md`, bounded to 6 to 8 fetches, public professional
   footprint only. Wait for all of them.
   - **If the builder's notes mention a specific person** — a warm intro, a past
     conversation, something they heard — pass it to *that* prospect's scanner as
     context the builder supplied. A warm intro is a fact from the builder and stands as
     one; anything they merely heard comes back sourced or comes back `[not found]`.
     Never laundered into the scan as established.
10. **Dispatch `outreach-writer`** with the working folder path and, when step 7 found one,
    the previous `outreach-kit.md` path. It reads `inputs.md`, every scan, `voice.md`, and
    a specimen from `writing-samples/` — **no web tools, no new research** — and writes
    `outreach-kit.md`: one panel per prospect; on a multi-prospect run the **Who to write
    first** synthesis; and what changed since the previous kit. What the builder sells and
    their notes reach it through `inputs.md` **verbatim** — that file carries their words,
    never a paraphrase.

## Publish the artifact — you, not the agents

11. When `outreach-writer` finishes, read `outreach-kit.md` and **publish it as a Claude
    Artifact** yourself, in this conversation, following the design contract below. The
    agents write markdown only; the finished, shareable view is yours to render. If
    artifact publishing isn't available in my environment, don't block — the markdown is
    saved; say so and give the path.

### The artifact — design contract (follow it exactly)

**The artifact is a tool the builder operates while they send, not a report they scroll**
(product decision, 2026-08-31). One prospect on screen at a time, reachable in one click;
sections scannable by color before they are read. This contract is
`skills/competitive-intel/SKILL.md` § the artifact with this use case's lanes substituted —
**same palette values, same type system, same structure rules.** Copy it; don't re-derive it.

**Read-only is absolute, and it bites hardest here.** No CTAs, no dead controls, nothing
that pretends to fetch, save, or send. **Specifically: no copy-to-clipboard button on the
drafts, and no send control of any kind.** The draft is selectable text in a bordered
block — that is enough, and a send-shaped button on a kit whose whole promise is "nothing
is sent" is the worst possible control to ship. Interactivity is navigation, never chrome.

A single self-contained HTML page. **CSP rules: exactly one external request, the Google
Fonts stylesheet below. All CSS in one `<style>` block, all JS inline (one small tab
script), no CDN scripts, no remote images.** Print-friendly: under `@media print` the tab
strip hides, `.panel[hidden] { display: block }` renders every prospect in sequence, with
a page break between prospects — a printed kit is a call-prep sheet.

**Fonts** — one Google Fonts link, every face with a real fallback: `DM Sans` (display +
body; fallback `system-ui, -apple-system, sans-serif`), `Source Serif 4` (the read block,
the angle, the drafts, the first question; fallback `Georgia, serif`), `JetBrains Mono`
(labels, meta, dates, chips; fallback `ui-monospace, Menlo, monospace`).

**Theme — ship both, token-structured.** Bare `:root` carries the complete light palette;
`@media (prefers-color-scheme: dark)` guarded as `:root:not([data-theme="light"])`
redefines only the tokens; `:root[data-theme="dark"]` duplicates them. Every component
rule uses `var()` — no literal color outside the three token blocks. `body` background is
`var(--paper)`.

**Tokens** (light / dark) — the Builders palette, with the lane families named for this
use case's four lanes:

| Token | Light | Dark |
|---|---|---|
| paper / card / card-2 | `#F5F1EA` / `#FFFFFF` / `#FAF7F1` | `#14171E` / `#1C212B` / `#222835` |
| line / line-2 | `#E7E0D6` / `#D6CDBE` | `#2E3542` / `#3D4658` |
| ink / ink-2 / ink-3 / ink-4 | `#1B2130` / `#3D4658` / `#6B7486` / `#8B93A3` | `#EDEEF2` / `#C3C9D4` / `#97A0B0` / `#7B8494` |
| accent (BlueRock blue — structural, and the **angle** lane) + soft + line | `#1559C4` / `#E8EFFB` / `#B9CDEF` | `#6E9BE8` / `#1D2A45` / `#34528C` |
| fact (the **sourced** lane) + soft + line | `#206E5B` / `#E7F2EE` / `#BFDCD3` | `#55B092` / `#1B2E29` / `#2F5A4B` |
| draft (the **drafts** lane) + soft + line | `#94660F` / `#F7EFDD` / `#E5D3AC` | `#D3A24C` / `#322A19` / `#66542B` |
| gap (the **what we couldn't find** lane) + soft + line | `#B4432E` / `#F9ECE8` / `#E8C7BE` | `#E0715A` / `#372220` / `#6B392F` |
| neutral + soft + line | `#5A6272` / `#EEEDE9` / `#D9D3C8` | `#9AA3B2` / `#262C37` / `#414A5A` |
| chip text (on lane-colored chips) | `#FFFFFF` | `#14171E` |

**Structure** (max width 1000px):

1. **Sticky masthead** — uppercase display title (`<account or campaign> · Outreach kit`
   shape), mono meta line (`<date> · SELLING: <offer in four words> · CHANNEL: <channel> ·
   <first run or run N> · <N> source domains`), then the **tab strip**: one `role="tab"`
   button per prospect, `aria-selected` on the active one, 3px accent underline; panels are
   `<section role="tabpanel">` toggled via the `hidden` attribute by the inline script
   (first panel visible on load, others carry `hidden` in markup).
2. **Legend row** naming the four lanes with color dots: sourced, dated · the angle (yours,
   aimed) · drafts — not sent · what we couldn't find. **Four lanes carry three kinds of
   statement:** the gap lane is the sourced lane's honest other half (what the record does
   not say), which is why it gets its own color rather than hiding inside the first. The
   legend is where the separation becomes visible before a word is read, so it is not
   optional.
3. **"Since your last kit" strip** — only when a previous run existed: an accent-soft
   callout, dated, listing the writer's "Since" items (or its "no material change" line),
   and any opener it deliberately avoided reusing. Omit the block entirely on a first run.
4. **On a multi-prospect run, one synthesis view** reachable from the tab strip alongside
   the prospects: **Who to write first** — the writer's table (prospect × why-now ×
   strength × angle) inside a bordered `overflow-x: auto` container, the strength column
   rendered as a lane-colored chip (`strong` fact, `fair` neutral, `cold — fit only` gap),
   and the two-line order read beneath it carrying its `[my read]` tag.
5. **One panel per prospect**, sections in this order:
   - **Name** (display, 28–40px, weight 800) + mono scope subline carried from the scan:
     `<role> · <company> · footprint: <substantial|moderate|thin>`.
   - **Who they are** — bordered block with a dark bar header (`background: var(--ink)`,
     `color: var(--paper)`), labeled grid rows (`128px + 1fr`; mono uppercase labels, serif
     values): what they own, tenure, the company. Then a highlighted **THE READ** row on
     accent-soft: the one sentence that frames this approach.
   - **Why now** — fact-colored chip + note `Sourced. Dated.`; numbered item-cards (mono
     number, fact-colored 4px left stripe) each carrying the signal as the bold lead, its
     **date** as a mono chip, and its source chip `scan-<slug>.md · <section>`. Carry every
     `[their claim]` / `[unverified]` / `[my read]` marker as a small gap-colored mono tag —
     never silently drop one. **When the writer found no dated signal**, render its honest
     line as a single full-width fact-lane card, not an empty section and not a hidden one.
   - **The angle** — accent chip + note `Yours, aimed. Not a finding about them.`; the
     angle sentence in serif italic behind an accent-colored 3px left rule, with the
     one line beneath naming what it rests on. `[my read]` markers stay visible.
   - **The draft** — draft-colored chip reading `DRAFT · <channel> · not sent`; the message
     in a card on `--draft-soft` with a 3px draft-colored left border, body face at a
     comfortable measure, `white-space: pre-wrap` so the writer's line breaks survive. Where
     the channel has a subject line, it sits above the body as a mono uppercase `SUBJECT`
     label row. Beneath the card, the **why this opener** line in small mono with its source
     chip. Selectable text only — no copy button, per the read-only rule above.
   - **Follow-up beats** — draft-colored chip + note `Also drafts. You decide if they go.`;
     WHEN/WHAT rows (mono uppercase `WHEN` label carrying the trigger, the line in ink, the
     pre-written text in the draft card treatment where the writer supplied one).
   - **The gap** — gap-colored chip + note `What we couldn't find.`; one card, hairline-
     separated list, then the **first question** in serif italic inside a gap-soft callout
     with a 3px gap left border. **Required — never omitted.** On a thin prospect this
     section renders full-width and directly under Who they are, because it is the most
     useful thing on the panel; it reads as the finding it is, never as an apology.
   - **Panel sources** — mono chips of the domains that prospect's scan actually used.
6. **Footer** — the three-lane separation note (sourced lines carry a scan citation; the
   angle is yours to say, never dressed up as a finding; drafts are drafts), the line
   **`Drafts only — nothing here has been sent, and this tool cannot send`**, the line
   **`Public professional information only`**, and `Built with BlueRock · Personalized
   Outreach · prospect-scanner + outreach-writer`.

**The scan test:** someone opening this between two calls has about eight seconds — the
lane colors, the name, the why-now dates, and the draft block must carry the panel before
a single sentence is read.

## Finish

12. The **outreach kit artifact** is the payoff. The `outreach-kit.md` is the source of
    record the builder keeps and can push to their repo, and `inputs.md` beside it is what
    the next run pre-fills from.
13. **Report:** the folder path, the one line that matters (the sharpest sourced why-now,
    or — when a prospect came back thin — the first question that gap became), and the
    artifact (or the fallback note). Say once that the drafts are drafts and nothing has
    been sent. Don't reprint the kit.
14. **Offer the depth, after the run — never before it.** One beat, two doors, then stop:
    *"Want to see how this worked? Two agents ran it — a scanner that read each person's
    public record and a writer that aimed your offer and drafted in your voice. The
    anatomy-of-an-agent and give-your-agent-memory sessions explain the pattern — say
    'teach me how this works'. And if these drafts didn't sound like you, that's
    `voice.md`: run `/bluerock:onboard` and the next kit writes the way you write."*

## Honesty rules this skill carries

- **The tool never sends anything, ever.** No send, no sequence, no scheduling, no CRM
  write. If a builder asks for it, say plainly that this run stops at drafts by design and
  that sending stays theirs — don't improvise a workaround with another tool.
- **Three lanes, never blurred.** Facts about a person trace to a scan and carry sources;
  the angle is the builder's own claim, aimed but labeled theirs; drafts are labeled
  drafts. The writer enforces it; the artifact preserves it.
- **A thin prospect gets a short honest panel**, not a padded one, and the gap becomes the
  first discovery question. This is the designed outcome, not a degraded one — a builder
  who opens with a genuine question does better than one who opens with a press release
  they mistook for insight.
- **Public professional footprint only.** No contact details found, guessed, or inferred;
  nothing behind a login; nothing personal. The scanner carries the hard version of this
  rule and it is not negotiable at this layer either.
- **Would this survive the prospect reading it?** Panels get forwarded and drafts get
  screenshotted. Nothing in a kit should embarrass the builder if it happens.
- **Refresh, don't rot.** A why-now goes stale in weeks, not quarters — a funding round is
  news for about a month. Every run is dated; when the previous run in
  `my-work/outreach-prep/` is more than a month old, say so in the report rather than
  treating the diff as a refresh.
- **The time-saved line above ships only with a timed figure and its provenance.**

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`agents/outreach-writer.md` owns the panel section names** (Who they are, Why now, The
  angle, The draft, Follow-up beats, The gap) **and the synthesis name on multi-prospect
  runs (Who to write first)**; this skill's artifact contract renders all of them by name
  and order. Reword them in either file and the artifact loses sections silently. The
  draft's two-part shape (the message, then the **why this opener** line with its source)
  is likewise shared between the writer's panel spec and the artifact's draft rendering.
- **`agents/prospect-scanner.md` owns the scan section names**; the writer reads scans by
  section, and the artifact's subline carries the scan's `Footprint:` rating verbatim
  (`substantial` / `moderate` / `thin`) — the three words are matched, not paraphrased.
  The scan filename shape `scan-<prospect-slug>.md` is matched by the writer's Glob.
- **The four channel shapes** (email, LinkedIn message, LinkedIn connection note, call
  opener) are named identically in this skill's intake step 3 and the writer's § Channel
  shapes; the artifact prints the chosen one in the masthead meta and the draft chip.
  Adding or renaming a channel is a change in three places.
- **`skills/onboard/SKILL.md` owns `voice.md` and `writing-samples/`**, which the writer
  reads and this skill's close names as the fix for drafts that don't sound like the
  builder. Renaming either strands both.
- **`curriculum/manifest.json`** carries this skill's `one_liner`, `artifact`,
  `time_saved`, and `team` — the menu and the site read them; keep them in step with the
  opening lines here.
- **README.md § Personalized Outreach** quotes the intake shape and the panel sections.
- The working folder shape `my-work/outreach-prep/<YYYY-MM-DD>-<slug>/` is what makes run
  history findable, and the history is what stops a rerun reusing a sent opener;
  `/bluerock:wrap-up` logs runs against the agent-team label **Personalized Outreach**
  with members `prospect-scanner` + `outreach-writer` (the Account Research roll-up shape).
- **The flow doc mirrors this skill** (content repo, private:
  `09-product/use-case-flows/personalized-outreach-flow.md`) — any change to the intake,
  dispatch, artifact, or close updates it in the same pass.
