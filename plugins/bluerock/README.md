# BlueRock for AI Builders

Say *"score Acme Corp"* and a two-agent team hands you a one-page account scorecard. Say
*"wrap up my session"* and it logs your work and refreshes your dashboard. This is the
plugin behind [BlueRock for AI Builders](https://builders.bluerock.io) — the run-as-is core
that turns Claude Code (inside Cursor or VS Code) into tools that do your real work and write it back
as plain markdown you own.

You drive it in plain language, or use the commands when you'd rather be explicit. Plugin
tools are written with their full name — `/bluerock:check`, `/bluerock:wrap-up` — where the
`/bluerock:` part says which toolkit they came from. The skills and agents seeded in your own
project live in that project's `.claude/` folders; `/bluerock:check` can link them for new chats while
the files stay in your repo. Everything runs inside your own repo, your **agentic project**
(older docs call the same repo your AI Work Hub — same thing), so
nothing is locked in an app: the output is your files, yours with or without the plugin.

> **New here?** The [BlueRock for AI Builders learning path](https://builders.bluerock.io) sets
> up your project and walks you through everything below — start there.

## What the plugin gives you

The **run-as-is core** — you drive these; you don't edit them:

| Category | What it's for |
|---|---|
| **Set up** | Get to know you, confirm you're ready: `/bluerock:onboard`, `/bluerock:check` |
| **When you're stuck** | One diagnosis, one next step: `/bluerock:help` |
| **Your daily rhythm** | Today's priorities and the end-of-session wrap: `/bluerock:today`, `/bluerock:wrap-up` |
| **Account Scorecard** | Point a fast team at a company for a one-page scorecard: `/bluerock:scorecard` (agents `scout` + `scorer`) |
| **Messaging Doc** | Point a fast team at your website for your core messaging doc: `/bluerock:messaging-doc` (agents `site-reader` + `distiller`) |
| **Competitive Intel** | Battlecards for the competitors you face: `/bluerock:competitive-intel` (agents `competitor-scanner` + `analyst`) |
| **AEO Visibility** | Whether you show up when buyers ask an AI: `/bluerock:aeo-visibility` (agents `answer-sampler` + `visibility-auditor`) |
| **Personalized Outreach** | Prep and drafts for the people you want to reach: `/bluerock:outreach-prep` (agents `prospect-scanner` + `outreach-writer`) |
| **Process to Skill** | Turn a process that lives in your head into a skill you can run and a runbook you can hand over: `/bluerock:process-to-skill` (agent `understudy`) |

## Account Scorecard — the fast first win

`/bluerock:scorecard <company>` (or *"score Acme Corp"*) runs two agents and hands you a one-page
scorecard:

- **`scout`** — a quick, sourced scan: what they do and sell, headquarters, headcount,
  estimated revenue and stage, one or two recent signals.
- **`scorer`** — carries that snapshot onto the page, grades **Fit / Timing / Reachability**,
  calls the "why now," and recommends a concrete next action, in your voice and against your
  objectives.

Revenue and headcount follow one rule: a stated figure with its source, an outside estimate
marked `est.`, or `Not disclosed`. Nothing is inferred — a blank you can see is what makes the
rest of the page safe to forward.

Seconds, not a deep dig — the "is this worth my time, and what do I do next" read. For the
deep, multi-section dossier, that's the **Account Research team** seeded in your project (below).

## Messaging Doc — the marketing first win

`/bluerock:messaging-doc <your site>` (or *"build my messaging doc"*) runs two agents and hands
you your **core messaging doc** — positioning, voice, and the phrases your brand actually uses:

- **`site-reader`** — reads your homepage and the pages that carry the messaging, capturing
  exactly what the site says: quoted, sourced, never paraphrased.
- **`distiller`** — turns that (plus anything you paste in: a recent post, campaign copy) into
  the one-page doc, with honest gaps named.

One website address plus whatever you paste — no exports, no logins. The doc saves in your project
and becomes the baseline every later draft leans on.

## Competitive Intel — the deal-room win

`/bluerock:competitive-intel` (or *"battlecard for Acme"*, *"who are we up against"*) asks
you five short questions — category, competitors (up to 4), what you win on, who the cards
are for, anything shaping the deal — confirms, then runs two agents:

- **`competitor-scanner`** — one docs-deep, sourced scan per competitor: what the product
  actually does (from their docs, not their homepage), pricing posture, traction, their own
  pitch, and where they're genuinely strong. Their unverified claims stay marked.
- **`analyst`** — one battlecard per competitor: sourced kill points, your differentiators
  aimed, the fights not to pick, their likely attack with the answer, a head-to-head, and
  one question to ask.

Two kinds of statement never blur on the card: claims about the competitor carry sources;
your own differentiators are aimed but labeled yours. Runs save to dated folders in
`my-work/competitive-intel/`, so a rerun before the next meeting tells you what changed.
This is the deep read of the pair — minutes, not seconds; the Account Scorecard stays the
fast one.

## AEO Visibility — do you show up when a buyer asks an AI?

`/bluerock:aeo-visibility` (or *"do we show up in ChatGPT"*, *"why does Perplexity
recommend our competitor"*) answers the question behind all of those: buyers ask an AI
which product to use, and you have no idea whether you're in the answer.

Give it your brand and your website. It reads your site and **proposes the 5 to 10
questions your buyers actually ask** — category, problem, and comparison — for you to edit
until they're right. Then two agents run:

- **`answer-sampler`** — one per question, concurrently: asks it, and writes down what
  actually came back. The sources, every brand named, whether you're among them, and the
  verbatim passages currently answering the question.
- **`visibility-auditor`** — reads the samples, looks at your own pages against the
  answer-engine method, and writes the **AEO Scorecard**: the verdict on each question
  (you're cited / a competitor is and you aren't / nobody is), a dated count, and a **fix
  queue ordered by impact and effort** with an owner on every line.

That owner line is the honest part. Some fixes are yours today, some belong to whoever
owns your site's templates, some need a page that doesn't exist yet — and some are on
**someone else's site**, because a listicle or a review profile owns that answer and no
amount of work on your own pages will win it.

**Two things this tool will not do.** It can't log into ChatGPT or Perplexity, so by
default it samples what a search actually returns — the pool those engines draw on — and
labels it as exactly that. Paste a real answer in and it reads that verbatim instead. And
it is **a dated sample, never a rank tracker**: AI answers are generated fresh each time
and vary between runs, so two runs are two samples, not a before and after. Every verdict
on the card carries the day it was taken.

## Personalized Outreach — the reading you never have time for

`/bluerock:outreach-prep` (or *"prep me for outreach to Dana"*, *"research these four
prospects"*) asks you four short questions — who you're writing to (up to 4), what you're
selling, which channel, anything shaping it — confirms, then runs two agents:

- **`prospect-scanner`** — one bounded, sourced scan per person: what they actually own,
  the dated reasons this is the moment, and what they've said in public, in their own
  words. Public professional footprint only, and it never collects contact details.
- **`outreach-writer`** — one panel per prospect: who they are and why now with sources,
  the angle (your offer aimed at this person), a draft in your voice, follow-up beats, and
  the thing it couldn't find turned into your first question.

Three kinds of statement never blur: facts about them carry sources, the angle is yours to
say, and every draft is labeled a draft. **Nothing is ever sent** — this tool has no send
step, no sequences, and no CRM write; you edit and send from your own account. A prospect
with a thin public record gets a short honest panel rather than a padded one, because
opening with a real question beats opening with a press release. Runs save to dated folders
in `my-work/outreach-prep/`, so the next kit won't reuse an opener you already sent.

## Process to Skill — the one that points at you

The other three point agents at the outside world. This one points at you, because the thing
it needs isn't on the internet: it's the process you run every week that nobody wrote down.

`/bluerock:process-to-skill` (or *"turn my Monday pipeline review into a skill"*, *"nobody
else can do this when I'm out"*) interviews you one question at a time — what starts it, the
steps, where you have to decide something, what done looks like, what goes wrong — and asks
you to paste one or two real examples. Then it writes two things:

- **A skill in your own project**, at `.claude/skills/<your-name>/SKILL.md`, that runs the
  process. It's yours: it fires bare (`/weekly-pipeline-review`), you can open it, and when
  the process changes you edit the file.
- **A runbook** in `my-work/process-to-skill/` — the printable half, with the steps, the
  inputs, your decision rules, the edge cases, and who covers when you're out.

In between, one agent earns its place: **`understudy`** reads your new skill file cold, with
no memory of the conversation that produced it, tries to follow it against your real example,
and reports every place it had to guess. That's the actual test of "could someone else run
this" — and the gaps it finds get closed before you ever run it.

**What the generated skill will not do:** send, post, submit, update a system of record, or
write anywhere outside your project. It drafts and stops, and the runbook says so out loud.
Anything that goes outward gets your eyes first.

Then you run it, on something real. That's the point of the whole thing: a tool that didn't
exist an hour ago, that you now own.

## Your project comes with more — and they're yours

Your project (from [the starter kit](https://github.com/bluerock-io/my-workspace)) ships seeded
agents and skills in `.claude/` that you can open, run, **edit**, and build on:

- **Agents** (`.claude/agents/`) — `daily-brew` (a morning brief that closes yesterday's
  loop and sets today's), `scribe` (files a note any time), `meeting-prep` (a brief before
  a call), plus the **Account Research team** `researcher` / `signal-scanner` / `composer`
  for a deep dossier.
- **Skills** (`.claude/skills/`) — `meeting-recap` (a follow-up after a call), `capture`
  (drop a note), and `research` (point the research team at a company for the full dossier).

These are yours from day one: edit any of them, or build your own alongside. The learning path
walks you through it.

## Install

In the Claude Code panel, type `/plugins` (plural) to open the plugin manager. On the
**Marketplaces** tab, enter `bluerock-io/claude-plugins` and click **Add**. On the
**Plugins** tab, find **bluerock** under Available → **Install** → choose **"Install for
you"** and trust it. Then start a new chat — that is what loads the plugin. Skip the
banner's **Restart** button; it does not reliably load it.

Then say *"check my workspace"* (or run `/bluerock:check`) to confirm you're set. You'll want a project to
run it in — [the starter kit](https://github.com/bluerock-io/my-workspace) gives you one in a click.

## Run as-is vs. make it yours

- The plugin's core (`/bluerock:onboard`, `/bluerock:today`, `/bluerock:wrap-up`,
  `/bluerock:check`, `/bluerock:scorecard`, `/bluerock:messaging-doc`,
  `/bluerock:competitive-intel`, `/bluerock:aeo-visibility`, `/bluerock:outreach-prep`,
  `/bluerock:process-to-skill`) you run as-is — though `/bluerock:process-to-skill` is the
  one whose *output* is yours to edit: the skill it writes lands in your project alongside
  your own.
  `/bluerock:wrap-up` and `/bluerock:check` especially stay plugin-owned so they keep your
  dashboard correct.
- Everything in your project's `.claude/` is yours: edit it in place, or build your own
  alongside. Name a skill of your own (`/standup`) and it just works; name an agent after a
  seeded one and yours takes over.

Everything stays inside your own files — no servers, nothing reaching outside your repo
without you asking.
