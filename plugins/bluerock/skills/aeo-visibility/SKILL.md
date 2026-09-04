---
name: aeo-visibility
description: >-
  AEO Visibility — find out whether you show up when buyers ask an AI which product
  to use, and what to fix first. Point an agent team at your brand and the questions
  your buyers actually ask, and get an AEO Scorecard: the verdict per question (you're
  cited / a competitor is and you aren't / nobody is), and a fix queue ordered by
  impact and effort with an owner on every line. Use when I say "do we show up in
  ChatGPT", "are we cited in AI answers", "AEO check", "AEO audit", "answer engine
  optimization", "why does Perplexity recommend our competitor", "check our AI search
  visibility", "are we in AI Overviews", or ask whether buyers asking an AI would find
  us. Runs answer-sampler (once per question, up to 10, concurrently) →
  visibility-auditor, and writes to my-work/aeo-visibility/.
  Every verdict is dated: this is a read of one moment, never a rank tracker.
---

Run the AEO Visibility team and produce an **AEO Scorecard** — Answer Engine Optimization,
which is the discipline of being the source an AI answer draws on when someone asks it
what to use. The scorecard says where the builder shows up today, where a competitor owns
the answer instead, and what to fix first.

**What it replaces:** asking an AI a dozen buyer questions by hand, writing down who it
named, then trying to work out which of twenty possible site changes would actually move
any of it.
**Time saved:** about 1.5 hours by hand, estimated and not yet timed. The timed
baseline (E6-26) replaces this figure when it lands.

## The honesty rule this whole skill is built around — read it first

AI answers are **generated fresh each time and vary between runs.** The same question,
asked twice an hour apart, can name different companies and cite different pages with
nothing having changed on anyone's website. Everything this skill produces is therefore a
**dated sample of one moment**, and the wording never drifts from that:

- **Every verdict carries its sampled-on date.** In `inputs.md`, in every sample file, in
  `aeo-scorecard.md`, and on the artifact's masthead where it cannot be scrolled away from.
- **Never claim rank tracking, position, share, or trend.** There is no rank here. Two runs
  a month apart are two samples, not a before and after, and the skill says so rather than
  drawing an arrow between them.
- **Never imply reproducibility.** Do not tell the builder they can "re-run and check
  progress." Tell them a re-run is another sample.
- **The count is a count, never a grade.** "Cited in 3 of 7 questions, sampled
  2026-09-03" is a fact about one sample. A composite score out of 100 is an invention;
  never produce one, however much it would look like a scorecard.
- **A fix changes what is findable, not what an AI will say.** Fixes are stated as
  "this makes the answer retrievable from your site" — never as "this will get you cited."

**What we can and cannot reach.** This matters more here than anywhere else in the
toolkit, and the builder is told it plainly rather than discovering it later:

- The team **cannot log into ChatGPT, Perplexity, or Google AI Overviews.** There is no
  API key, no session, and inventing a transcript would be the worst possible failure for
  a tool about honesty.
- What the team **can** do is sample **the retrieval layer** — run the buyer's question as
  a real web search and read what actually comes back, which is the pool an answer engine
  draws from when it answers that question. That is a genuine, defensible proxy, and it is
  labeled as exactly that: `[retrieval sample]`.
- If the builder wants the real answer text, **they can paste it in** — the skill offers
  this at intake. A pasted answer is the strongest evidence in the run and is labeled
  `[pasted answer · <engine> · <date>]`. It is never summarized; the brands and links it
  names are captured verbatim.

## First — anchor to the project

The scorecard, its working folder, and the `voice.md` / `objectives.md` the run reads all
live in the builder's project. Two generations exist: the project ships inside the
workspace image (usually the folder `my-workspace`); projects made before 2026-08 were
cloned and carry whatever name the builder chose. **Assume neither — identify it by its
signature.** In an SSH/cloud container the chat may start in the project itself or in the
**home folder** with the project one level down — both are normal. Run `ls`; see
`CLAUDE.md` and `design/` side by side? You're in the project. If not, find it:
`ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`, else
`find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` in, capture the **absolute
path** with `pwd`, and use that full path throughout. Can't find it? Ask the builder which
folder their project is in.

## Before the questions — read what the builder already has

Check, without asking: `objectives.md` and `voice.md` at the project root, and the latest
doc under `my-work/messaging-doc/` if one exists. These sharpen the run — they are never
required for it.

- **If they're real**, use them to pre-fill the intake: the messaging doc in particular
  names the category the brand competes in and the phrases it uses, which is most of what
  step 2's proposed questions are built from.
- **If they're placeholder templates or absent**, say so once, plainly, and keep moving:
  *"Your `objectives.md` / `voice.md` are still the placeholder templates, so I'll build
  the buyer questions from your site alone. Happy to run anyway — running
  `/bluerock:onboard` would sharpen future runs."* Never make setup homework the price of
  the first scorecard.
- **If a prior run exists**, its `inputs.md` pre-fills the same way (propose, confirm,
  don't re-ask cold) — the questions especially, since asking the same questions again is
  what makes two samples comparable at all.

## Intake — one question per step, short, then confirm

Ask these one at a time. Keep each ask to a line or two; don't stack questions or explain
the whole flow up front. **Skip what they already gave you** — if the opening request
named the brand or the domain, say what you're taking as given (`Brand: Acme ·
Domain: acme.com`) so a wrong reading gets corrected early, then pick up at the first step
that's actually missing.

**Which prompt shape for which step:** use the question picker (`AskUserQuestion`) only
where the answer is genuinely a choice between a few options — steps 2 and 4. Everywhere
else the answer is free text in the builder's own words; ask in the message and let them
type. Where the picker isn't available in this client, ask in the message.

1. **Brand and domain.** "What brand are we checking, and what's the website?" One line.
   The domain is what presence is judged against, so take it exactly — apex or www, and
   note any second domain (a docs site, a separate product site) they also own.

2. **The buyer questions — you propose, they confirm.** This is the step that decides the
   whole run, so do the work before asking. **Fetch two or three pages of their site**
   (homepage, a product or solutions page, a pricing page if there is one) and read what
   they sell, to whom, and against what. Then propose **5 to 10 questions in the shape a
   buyer would actually type into an AI**, drawn across three kinds — this is the intent
   spread the method calls for, and a list that is all one kind produces a useless sample:
   - **Category questions** — the buyer knows what they want to buy.
     *"What's the best <category> for <segment>?"*, *"Top <category> tools 2026"*
   - **Problem-aware questions** — they feel the pain, not the category.
     *"How do I stop <the pain the site describes>?"*, *"Why does <symptom> happen?"*
   - **Comparison and buying questions** — they are close to a decision.
     *"<Competitor> alternatives"*, *"<Brand> vs <Competitor>"*, *"How much does
     <category> cost?"*
   Show the list numbered, say where each came from in one clause, then: *"These are what
   I'd ask on your behalf. Edit any of them, delete what's wrong, add what I missed — the
   ones your buyers actually type matter far more than the ones I guessed."* Take their
   edits **verbatim**; a question reworded into our phrasing is no longer their buyer's
   question. Cap the confirmed list at 10.

3. **Competitors — optional.** "Who should I watch for in the answers? Names are enough."
   Optional and never blocks: without names the sampler still reports every brand the
   answers name, which is often how a builder discovers a competitor they weren't
   tracking. With names, the scorecard can say *absent, and <competitor> is there instead*,
   which is the sharpest line on the whole card.

4. **A real answer, if they have one — optional, and worth offering properly.** Explain
   the trade in one breath, because it changes what the run can claim: *"I can't log into
   ChatGPT or Perplexity, so by default I sample what a search actually returns for each
   question — the pool those engines draw on. If you want the real thing in the mix, paste
   what ChatGPT or Perplexity said for any of these questions and I'll read it verbatim."*
   (options: I'll paste some answers · sample the retrieval layer, that's fine). Take
   whatever they paste, whole, and note which engine and what date each came from — an
   undated pasted answer is asked about once, because the date is the whole point.

5. **Confirm before we run.** Play back brand, domain, the numbered questions, competitors,
   and which questions have a pasted answer, then: "Good to go, or anything to edit?"
   **Carry the questions forward verbatim from here.**

**The moment the builder approves**, set the expectation for the wait in one message of
its own, then go quiet until the report: the samples run concurrently and the audit
follows, so this takes several minutes — a good moment to grab a coffee or switch tasks,
and the scorecard will be ready when they check back. No further chatter between this and
the report.

## Set up the run

6. **Make the working folder:** `my-work/aeo-visibility/<YYYY-MM-DD>-<brand-slug>/`. Dated
   on purpose — runs accumulate and are never overwritten. `my-work/` is builder-owned.
7. **Check for a previous run:** list `my-work/aeo-visibility/`. If a prior dated folder
   holds an `aeo-scorecard.md`, note its path and date for the auditor. **A previous run is
   a previous sample, not a baseline** — the auditor is told this explicitly, and the words
   "improved", "declined", "up", and "down" never appear about the pair.
8. **Write `inputs.md`** into the working folder: brand, domain, the confirmed questions
   verbatim and numbered, competitors, which pasted answers were supplied and their engine
   and date, which project files were real enough to read, and **the sampled-on date**.
   This is the record of what shaped the scorecard and the seed the next run pre-fills from.

## Run the agents

Dispatch these as ordinary subagents. Do not use agent-teams tooling; this runs
identically in every client.

9. **Dispatch one `answer-sampler` per confirmed question — all in a single message so
   they run concurrently.** Each gets: its one question **verbatim**, the brand and domain,
   the competitor names if given, any pasted answer for *that* question in full, and the
   working folder's **absolute path** in the dispatch prompt itself (a subagent starts
   wherever the session started; the path you pass is the handoff). Each writes
   `sample-<question-slug>.md`. Wait for all of them.
   - **Ten concurrent samplers is the cap** because the confirmed list is capped at 10. If
     a builder insists on more, run the first 10 and say plainly which were not sampled
     rather than silently truncating.

10. **Dispatch `visibility-auditor`** with the working folder path, the brand and domain,
    and, when step 7 found one, the previous `aeo-scorecard.md` path. It reads `inputs.md`
    and every sample, audits the builder's **own** pages against the eight-step method, and
    writes `aeo-scorecard.md`: the verdict, the per-question grid, and the fix queue.

## Publish the artifact — you, not the agents

11. When `visibility-auditor` finishes, read `aeo-scorecard.md` and **publish it as a
    Claude Artifact** yourself, in this conversation, following the design contract below.
    The agents write markdown only; the finished, shareable view is yours to render. If
    artifact publishing isn't available in my environment, don't block — the markdown is
    saved; say so and give the path.

### The artifact — design contract (follow it exactly)

**The artifact is a tool the builder works from, not a report they scroll** (product
decision, 2026-08-31). One question on screen at a time, reachable in one click; the
verdict readable by color before it is read as words. Read-only and honest: no CTAs, no
dead controls, nothing that pretends to fetch or save — a dead button in a sandboxed
artifact is worse than no button. Interactivity is navigation, never chrome.

A single self-contained HTML page. **CSP rules: exactly one external request, the Google
Fonts stylesheet below. All CSS in one `<style>` block, all JS inline (one small tab
script), no CDN scripts, no remote images.** Print-friendly: under `@media print` the tab
strip hides, `.panel[hidden] { display: block }` renders every panel in sequence, with a
page break between questions.

**Fonts** — one Google Fonts link, every face with a real fallback: `DM Sans` (display +
body; fallback `system-ui, -apple-system, sans-serif`), `Source Serif 4` (the verdict
line, the verbatim passages, the fix statements; fallback `Georgia, serif`),
`JetBrains Mono` (labels, meta, chips, dates; fallback `ui-monospace, Menlo, monospace`).

**Theme — ship both, token-structured.** Bare `:root` carries the complete light palette;
`@media (prefers-color-scheme: dark)` guarded as `:root:not([data-theme="light"])`
redefines only the tokens; `:root[data-theme="dark"]` duplicates them. Every component
rule uses `var()` — no literal color outside the three token blocks. `body` background is
`var(--paper)`.

**Tokens** (light / dark) — the toolkit's shared set, carried from the Competitive Intel
contract so the two tools look like one family:

| Token | Light | Dark |
|---|---|---|
| paper / card / card-2 | `#F5F1EA` / `#FFFFFF` / `#FAF7F1` | `#14171E` / `#1C212B` / `#222835` |
| line / line-2 | `#E7E0D6` / `#D6CDBE` | `#2E3542` / `#3D4658` |
| ink / ink-2 / ink-3 / ink-4 | `#1B2130` / `#3D4658` / `#6B7486` / `#8B93A3` | `#EDEEF2` / `#C3C9D4` / `#97A0B0` / `#7B8494` |
| accent (BlueRock blue) + soft + line | `#1559C4` / `#E8EFFB` / `#B9CDEF` | `#6E9BE8` / `#1D2A45` / `#34528C` |
| absent + soft + line | `#B4432E` / `#F9ECE8` / `#E8C7BE` | `#E0715A` / `#372220` / `#6B392F` |
| cited + soft + line | `#206E5B` / `#E7F2EE` / `#BFDCD3` | `#55B092` / `#1B2E29` / `#2F5A4B` |
| open + soft + line | `#94660F` / `#F7EFDD` / `#E5D3AC` | `#D3A24C` / `#322A19` / `#66542B` |
| neutral + soft + line | `#5A6272` / `#EEEDE9` / `#D9D3C8` | `#9AA3B2` / `#262C37` / `#414A5A` |
| chip text (on lane-colored chips) | `#FFFFFF` | `#14171E` |

**The four lanes and what each color means here** — the legend row states them in these
words:

- **cited** (green) — the brand appears in what came back for this question.
- **absent, competitor present** (red) — someone else owns this answer. The sharpest state
  on the card; name who.
- **nobody cited** (gold) — no source owns this answer yet. Open ground, not a failure.
- **fix** (accent) — an action in the queue.
- **couldn't check** (neutral) — say so; never let it read as either presence or absence.

**Structure** (max width 1000px):

1. **Sticky masthead** — uppercase display title (`AEO SCORECARD` + the brand), then a
   mono meta line carrying the facts that bound every claim below it:
   `SAMPLED <date> · <N> questions · <retrieval | + M pasted answers> · CITED IN <X> OF <N>`.
2. **The sampling caveat — sticky, directly under the masthead, on every tab.** This is the
   honesty rule made structural, and it is never demoted to the footer. Neutral-soft strip,
   mono, one or two lines: *"Sampled <date>. AI answers are generated fresh each time and
   vary between runs — the same questions tomorrow can name different sources with nothing
   changed on any site. This is a read of one moment. Not a rank, not a tracker."*
3. **Tab strip** — one `role="tab"` button per panel, `aria-selected` on the active one,
   3px accent underline; panels are `<section role="tabpanel">` toggled via the `hidden`
   attribute by the inline script (first panel visible on load, others carry `hidden` in
   markup). Order: **Verdict** · **Fix queue** · then one tab per question. **Each question
   tab carries an 8px verdict dot in its lane color before its label**, so the strip itself
   is the summary — four red dots and two green is read before a word of it is.
   Question tab labels are a short slug of the question (3 to 5 words), never "Q1".
4. **Legend row** naming the lanes with color dots, in the words above.
5. **Verdict panel** (first):
   - **The verdict** in serif, 20–24px, one sentence naming the dominant state and who owns
     the answers if anyone does. Inside an accent-soft callout with a 3px accent left rule.
   - **The count**, mono, stated as a count and never a grade:
     `CITED IN 3 OF 7 QUESTIONS · SAMPLED 2026-09-03`.
   - **The per-question grid** — one row per question: the question (serif), its lane chip,
     and who was cited instead (mono domain chips). This is the whole card in one screen.
   - **Who owns these answers today** — the auditor's source-type read (are the answers
     coming from vendor pages, listicles, review sites, communities, or analysts), because
     it decides which fixes are even available. Labeled `[my read]` where it is inference.
   - **What we couldn't check** — the auditor's list of gated pages, failed fetches,
     script-injected structured data, and every question marked `COULDN'T CHECK`, in a
     neutral-soft block. **It renders on the card, not just in the markdown**: a visibility
     tool that shows only what it managed to see is the exact failure this one is built
     against. If the list is empty, say "nothing was blocked on this run" rather than
     dropping the block — an absent section reads as a clean bill of health nobody gave.
6. **Fix queue panel** — the action surface, and the reason the tool exists:
   - Numbered fix cards, **ordered by impact then effort**, accent-colored 4px left stripe,
     mono number. Each card carries, in this order: the **fix** as an action in serif bold
     (something a person could start this afternoon); three mono chips —
     **IMPACT** (`high` / `medium` / `low`, colored by lane intensity), **EFFORT**
     (`minutes` / `hours` / `a project`), and **OWNER** (see below); **why, from the
     sample** — one line citing the sample it traces to as a mono chip
     `sample-<slug>.md · <section>`; and **what it changes**, stated honestly
     (*"makes the answer retrievable from your page"*, never *"gets you cited"*).
   - **The OWNER chip is a role, not a person**, and one of these four:
     `you, today` (wording on a page you control) · `your web person` (template, metadata,
     or schema) · `a writer` (a page that doesn't exist yet) · `someone else's site`
     (a review profile, a listicle, a directory, an analyst — you can't edit it, you can
     ask). The fourth is the honest one most tools omit, and it is never dropped just
     because it is uncomfortable.
7. **One panel per question**, sections in this order:
   - **The question, verbatim**, display 22–30px, exactly as the builder confirmed it.
   - **State banner** — the lane color, the state in words, and the sampled-on date, mono.
   - **What came back** — the ranked sources the sample actually returned: mono domain
     chip, title, and the one-line reason it answers the question. Where a pasted answer
     exists for this question, it leads, tagged `[pasted answer · <engine> · <date>]` in
     the accent color, and is visually separated from the retrieval sample below it.
   - **Who is cited** — brand chips; the builder's own brand in cited-green when present,
     competitors in absent-red, others in neutral. Absence is stated as a sentence, never
     an empty div.
   - **Passages worth owning** — the verbatim text currently answering this question, in
     serif, each behind a neutral left rule with its source domain. This is the single most
     useful thing on the panel: it shows the builder the shape of the answer that wins.
   - **Source-type read** — one line: what kind of page is winning this question.
   - **Fixes from this question** — the numbers from the fix queue that trace here, as
     accent chips. Navigation only; the fixes live in one place.
8. **Footer** — the separation-rule note (*what was sampled carries a source and a date;
   what the audit concluded is our read, and is labeled*), the line **`A dated sample, not
   a rank. Re-running gives another sample, not a trend.`**, and
   `Built with BlueRock · AEO Visibility · answer-sampler + visibility-auditor`.

**The scan test:** someone who opens this on a phone has about eight seconds — the tab
strip's verdict dots, the verdict sentence, and the first three fixes must carry the whole
card before a single paragraph is read.

## Finish

12. The **AEO Scorecard artifact** is the payoff. `aeo-scorecard.md` is the source of
    record the builder keeps and can push to their repo, and `inputs.md` beside it is what
    the next run pre-fills from — including the questions, which is what makes a later
    sample worth comparing at all.
13. **Report:** the folder path, the one line that matters (the sharpest *absent, and
    <competitor> is there instead*, or the best piece of open ground), and the artifact (or
    the fallback note). Don't reprint the scorecard.
14. **Offer the depth, after the run — never before it.** One beat, two doors, then stop:
    *"Want to see how this worked? Two agents ran it — a sampler that asked each of your
    buyer questions and wrote down what actually came back, and an auditor that read your
    pages against it. The anatomy-of-an-agent and subagent-teams sessions explain the
    pattern — say 'teach me how this works'. And if you want the questions sharper next
    time, run `/bluerock:messaging-doc` on your site — the buyer questions build themselves
    from it."*

## Honesty rules this skill carries

- **Sampled versus concluded never blur.** What came back carries a source and a date;
  what the audit concluded is our read and is labeled. The auditor enforces it; the
  artifact preserves it.
- **A dated sample, never a rank.** No positions, no share, no trend, no arrows between
  runs. Two runs are two samples.
- **We cannot reach the answer engines directly, and we say so** — `[retrieval sample]` on
  what we searched, `[pasted answer]` on what the builder supplied. A transcript is never
  invented, paraphrased into existence, or attributed to an engine nobody queried.
- **A thin question gets an honest thin panel**, not a padded one. "Nothing came back that
  answers this" is a finding, and usually the best piece of open ground on the card.
- **No composite grade.** A count out of N, dated. Never a score out of 100.
- **A fix names what it changes, and what it doesn't.** Retrievability is ours to affect;
  what a model says is not.
- **The time-saved line above ships only with a timed figure and its provenance.**

## Who depends on this skill's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`agents/answer-sampler.md` owns the sample section names** (What came back, Who is
  cited, The brand's presence, Passages worth owning, Source-type read, Gaps and open
  questions) and the sample filename shape `sample-<question-slug>.md`, which the auditor
  matches by Glob and reads by section. Every one of those six is rendered on the artifact
  except **Gaps and open questions**, which feeds the auditor's *What we couldn't check* —
  so dropping it from the sampler silently empties an honesty section two files away. Reword them in either file and the artifact loses
  sections silently.
- **`agents/visibility-auditor.md` owns the scorecard section names** (The verdict, The
  count, Per-question grid, Who owns these answers today, Fix queue, What we couldn't
  check) **and the two fixed scales**: impact (`high` / `medium` / `low`) and effort (`minutes` / `hours` /
  `a project`), plus the four owner-types (`you, today` / `your web person` / `a writer` /
  `someone else's site`). This skill's artifact contract renders all of them by name.
- **The four lane names and their colors** (cited, absent-competitor-present, nobody
  cited, couldn't check) are shared between the auditor's grid and the artifact's legend,
  tab dots, and state banners. Renaming a lane in one place strands the other two.
- **`curriculum/manifest.json`** carries this skill's `one_liner`, `artifact`,
  `time_saved`, and `team` — the menu and the site read them; keep them in step with the
  opening lines here.
- **README.md § AEO Visibility** quotes the intake shape and the scorecard sections.
- The working folder shape `my-work/aeo-visibility/<YYYY-MM-DD>-<brand-slug>/` is what
  makes run history findable; `/bluerock:wrap-up` logs runs against the agent-team label
  **AEO Visibility** with members `answer-sampler` + `visibility-auditor`.
- **`skills/messaging-doc/SKILL.md`** names this skill as a consumer of
  `my-work/messaging-doc/` — the folder shape is load-bearing beyond that skill.
- **The flow doc mirrors this skill** (content repo, private:
  `09-product/use-case-flows/aeo-visibility-flow.md`) — any change to the intake,
  dispatch, artifact, or close updates it in the same pass.
