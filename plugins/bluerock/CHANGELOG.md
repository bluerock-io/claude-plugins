# Changelog — `bluerock` plugin

## 0.8.1 — the baked-image transition stops breaking flows that assumed a clone

The workspace image now ships with the project baked in (hub-starter: "no template, no
clone, project is the root"), and no GitHub remote exists until the builder connects
one. Three skills assumed the old flow; each now checks state instead of assuming it.

- **Fixed — `learn-get-started`:** step 5 now checks the workspace by signature before
  instructing the template + clone flow. If the project is already baked in, it says
  so, skips steps 5–6, creates `learning/` + `progress.json`, and continues at step 7.
  (The full rewrite of steps 5–6 for the baked image is pending a walkthrough — this
  guard stops the shipped skill from walking a builder into a wall today.)
- **Fixed — `wrap-up`:** step 5 checks `git remote` before pushing. No remote is
  normal pre–Save-your-work: commit locally, skip the push without calling it a
  failure, and say where backup starts later.
- **Fixed — `learn-put-an-agent-on-a-schedule`:** Before-you-start now verifies the
  GitHub remote exists and the branch is pushed — the one prerequisite that genuinely
  blocks, since Routines run in Anthropic's cloud against the builder's repo. If
  missing, it helps connect one before anything gets scheduled.
- **Added — repo `CLAUDE.md`:** the skill authoring guide (facilitation standard) —
  the teach loop, capture discipline, session-skill shape, voice, environment honesty,
  and hard rules, distilled from the Session 2 exemplar. Auto-loads for every session
  working in this repo.

## 0.8.0 — the learning path runs in-session, all eight sessions

Phase 1 of `bluerock-in-session-curriculum-build-spec.md` is complete. 0.6.0 shipped
the router, `progress.json`, `learn-status`, and Sessions 1–2; this adds the
remaining six, built against the site's session specs in
`marketing-hub/workbench/app/learn/_data/`.

- **Added — six session skills**, each with `checkpoints.md` and
  `examples/roles.md`, following the Session 2 template and its "How to teach"
  contract:
  - `learn-anatomy-of-an-agent` (3) — runs the seeded `scribe`, names the five
    parts against the real file, then adds one line to it. Its checkpoint is a
    **git diff**, and the diff being *small* is a pass condition: a large one
    means Claude rewrote the spec instead of adding to it, which is the failure
    the approval habit exists to catch.
  - `learn-give-your-agent-memory` (4) — orchestrates `/bluerock:onboard` rather
    than reimplementing the interview.
  - `learn-turn-a-task-into-a-skill` (5) — the builder authors their own skill, so
    the checkpoints verify **shape, not content**.
  - `learn-assemble-a-team-of-agents` (6) — the 60–90 minute one; says so up front
    and splits into two sittings at the part boundary.
  - `learn-put-an-agent-on-a-schedule` (7) — see the honesty notes below.
  - `learn-run-your-system` (8) — see the capstone decision below.
- **Changed (`learn`, the router) — it no longer names which sessions run
  in-session.** It hardcoded *"Sessions 1 and 2 run fully in-session today;
  Sessions 3–8 still live on learn.bluerock.io"*, which landing Session 3 would
  have made false **inside the one skill whose job is telling a builder where they
  are.** Availability, handoff paths, and "what's left" now all derive from
  `curriculum/manifest.json`, which ships in the same release as the skills and so
  cannot drift from them. Adding a session now requires no edit to the router at
  all. If the manifest claims a skill the release doesn't contain, the router
  trusts the filesystem and degrades to the web link.
- **Changed (`curriculum/manifest.json`):** sessions 3–8 gain their `skill` names,
  `delivery: "in-session"`, and real `checkpoints` counts (3, 4, 6, 5, 5, 5), plus
  outcomes written at the same grain as Sessions 1–2 instead of the site's
  four-word summaries.
- **Added — the dependency-note convention, applied everywhere.** Every session
  skill and the router now end with a **"Who depends on this skill's wording"**
  section, the pattern 0.6.4 introduced in `check` after the learn workstream
  found that class of coupling downstream and invisibly. Each block names its site
  page, the starter-kit files it quotes, and the neighboring sessions that depend
  on its close-out. Six new skills would otherwise have created six new instances
  of the same silent-staleness bug.
- **`learn-status` unchanged** — it was already manifest-driven and already
  handled web-versus-in-session generically.

### Three site-copy bugs found while porting, and how this release handles them

Content was ported from the site specs, not invented. Three claims did not survive
verification against `bluerock-io/hub-starter` `main`. **The skills use the
verified facts and record the divergence**; the site pages still need fixing.

- **Session 5's skills path is wrong on the site.** The page says
  `.claude/commands/meeting-recap/SKILL.md` and tells builders to create their own
  skill at `.claude/commands/<name>/SKILL.md`. The starter kit has **no
  `.claude/commands/` directory at all** — seeded skills are at
  `.claude/skills/`, which the starter kit's own README documents. As written, the
  page sends a builder to a file that does not exist and has them file their first
  skill where nothing will find it beside the others.
- **Session 6's dispatch command is wrong on the site.** The page says
  `/bluerock:research`. `research` is a **builder-owned** skill shipped in the
  starter kit, so it fires bare: `/research`. There is no `research` skill in this
  plugin, so the prefixed form resolves to nothing. Cause is recorded in the page's
  own provenance comment: the 2026-07-22 `/bluerock:` convention was applied to it,
  but that convention covers **plugin** skills only — exactly what the Session 5
  page says. The two pages contradict each other on the same rule.
- **Session 7 calls `daily-brew` read-only.** Its tools line is
  `Read, Write, Edit, Grep, Glob` and it seeds `today.md`. The *principle* the note
  is making — you don't loosen a specialist's tools line because the trigger
  changed — is correct and is ported; the false claim is not.

### Two sessions needed a design decision before code

- **Session 7 teaches a surface BlueRock does not own, and says so.** `/schedule`
  is a native Claude Code command; Routines run in **Anthropic's cloud** against
  the builder's GitHub repo, not in the BlueRock workspace. The skill attributes
  that plainly, keeps the site's "the buttons may move" honesty line, and treats
  the one-time GitHub grant as a consent moment the skill **explains but cannot
  complete or confirm**. Its checkpoints separate **reported** from
  **inspectable** evidence (the Session 1 model): a routine's existence is not
  inspectable from the project, so the session's real checkpoint is the file a
  **manual fire** produces. Hence the ported discipline: never let 7am be the
  first test. `progress.json` cannot reach `complete` on a routine that has never
  produced a file.
- **Session 8 is a reflection and wrap, not a taught session** — option 1 of the
  three in `bfb-sessions-3-8-in-session-scope.md` §2, the only one where
  `progress.json` can honestly reach `complete`. The site's capstone is *present
  one workflow live*, which no skill can verify. This one **reads the real project**
  (splitting what the builder built from what the starter kit seeded), names it
  back with counts, then does with them what the audience would have done: finds
  the gap. The presentation stays as a strongly-offered exercise with an
  explicitly **unverifiable** checkpoint that never blocks completion. Making the
  capstone presentation-gated later is a product decision, not a copy fix — it
  changes what finishing the path means.

### Not done

- **None of the six has had a real run in a real workspace**, which the scope
  doc sets as the bar for calling a session done ("reading one proves nothing").
  These are instructions to a model, and the two shipped sessions took real
  iteration. Treat this release as unproven until Sessions 4 and 3 have each been
  run end to end in a workspace.
- Out of scope, per the spec: the `learning-coach` subagent (Phase 2 — coach
  behavior stays embedded in each session skill), the dynamic manifest, and
  telemetry.

## 0.7.0 — the load-path links pin you to one project, and now something says so

Found live: a builder cloned a second project, ran `daily brew` in it, and got the *first*
project's agent — an older copy, with retired vocabulary and no anchoring. Nothing was broken;
the wrong files were loading, and the symptom pointed nowhere near the cause.

- **The mechanism.** `/bluerock:check` links `~/.claude/skills` and `~/.claude/agents` to the
  project it was first run in. Claude Code loads user-scope skills and agents from those paths,
  and in the workspace a session starts at the home folder — so a second project's own
  `.claude/` is never consulted. The builder is sitting in project B running project A's tools,
  and everything appears to work.
- **Changed (`check`):** the repoint branch already asked before repointing, but framed it as
  housekeeping. It now names the cost: which project's tools they are actually getting, that
  this project's own are not loading yet, and that a stale copy behaves like an older version
  of itself. The "no" path repeats which project's tools they will keep.
- **Changed (`help`):** added the diagnosis, because `help` is what a stuck builder actually
  runs. Its look-before-you-ask ladder now compares where the links resolve against the project
  it just found, and the shapes-of-stuck table carries a row for "behaved like an older version
  of itself, or like another project's" routing to `/bluerock:check` in the intended project.

Minor rather than patch: `help` gains a diagnostic step and a routing row, which changes what
it does rather than only what it says.

## 0.6.4 — record who depends on this skill's wording

- **Added (`check`, maintainer note):** the consent prompt's wording is quoted by
  learn.bluerock.io — Session 1 tells builders *"say yes, it explains itself when it asks"*,
  which is only true while this prompt does. Nothing links the two at build time, so rewording
  here silently falsifies the page. The skill now says so at the prompt and carries a
  "who depends on this skill's wording" section naming the files and the handoff. Flagged by
  the learn workstream after applying the page change: the dependency was documented
  downstream and invisible from here.
- Also recorded there: the report names Session 1's steps by title rather than number (the two
  tracks number differently), and the tracks diverge on purpose — a Cursor builder has met no
  permission prompt before reaching this skill, a Desktop builder has.
- No builder-facing string changed.

## 0.6.3 — say it without `git status`

- **Changed (`check`):** the consent prompt's reassurance said the links "won't show up in
  `git status`." Watching 0.6.2 run live, the model rendered that as **"won't show up as a
  change to your project"** on its own — plainer, and truer to the audience: a builder has met
  `repo` and `clone` by this point in Session 1, but not `git status`. Folded the model's
  wording back into the skill so it is the instruction rather than a lucky paraphrase.

## 0.6.2 — `check` recommends the one decision it asks you to make

- **Changed (`check`):** the load-path consent question was neutral plumbing: *"I can link
  `~/.claude/skills` and `~/.claude/agents` to your project... Do you want me to do that?"*
  No recommendation, no reason, and the mechanism first. To a builder who is not a developer
  that reads like something to ask IT about, and it lands at the milestone moment at the end
  of Session 1. A no is not neutral: Claude Code resolves `.claude/` from where a chat
  **starts**, which in the workspace is one level above the project, so without the links the
  project's own skills and agents silently do not load in new chats — and every agent and
  skill the builder goes on to build lives in exactly that folder. They would build it and it
  would not be there, with no error pointing at the cause.
- Now it leads with the recommendation, gives the reason in the builder's terms (what breaks,
  not where the symlink goes), and closes the ownership question before they think to ask it
  — nothing moves, the files stay in their project, it will not show in `git status`.
- **Changed (`check`, the no path):** saying no now states plainly what it costs and that
  rerunning `/bluerock:check` offers again, instead of a bare "nothing changed." A builder who
  declines should know what they declined and that it is one command to undo.
- Consent itself is unchanged: still asked, never assumed, and still refuses to touch a real
  directory at either path.

## 0.6.1 — `check` was still naming the workspace by a retired name

- **Fixed (`check`):** the skill description and its opening line said the project is live in
  "your secure workspace." That name was superseded on 2026-08-01 by **your Cloud AI
  Workspace**, David's term, and the description is marketplace-visible — it is the last
  thing a builder reads before installing. Shipped in 0.6.0 because the sweep that release
  carried was scoped to the project noun and "the curriculum", and this is a different slot.
  Found by auditing all three surfaces (learn, plugin, starter) against the vocabulary tokens
  rather than against each other.

## 0.6.0 — the learning path runs in-session, and a way out when you're stuck

The first release where the plugin *teaches*, not just works. Sessions 1 and 2 run inside the
conversation instead of only on the web, and a stuck builder has somewhere to go that isn't
Discord.

- **New:** `/bluerock:learn`, the front door. Reads where the builder is, greets them
  honestly, and hands off to the right session skill. It only runs when asked; it never
  surfaces mid-task. `/bluerock:learn-status` is its read-only companion: sessions done, what
  was built, what's next and how long it takes. It changes nothing, ever.
- **New:** `/bluerock:learn-get-started` runs Session 1 in-session, on both surfaces. Its twist
  is that the builder can only be talking to you because *some* of the setup already worked,
  so it orients before it teaches and never walks anyone through a step they have done.
- **New:** `/bluerock:learn-meet-your-first-agent-team` runs Session 2, the first win, now
  **two-lane**: marketing builds a core messaging doc for their own brand, sales and
  operations get the account scorecard. Same lesson, a first output each role would actually
  send someone.
- **New:** `/bluerock:messaging-doc` and the two agents behind it, `site-reader` → `distiller`.
  Point them at your website and get back positioning, voice, and the phrases you actually
  use. This is the doc every later draft leans on, which is what makes it a first win rather
  than a demo.
- **New:** `/bluerock:help`, triage for a stuck builder. One diagnosis and **one** next step,
  in plain language: it looks before it asks, matches to a single shape of stuck, and routes.
  It is explicitly not a manual, a menu, or an audit: a wall of green checks reads as
  "everything is fine" to someone whose thing is not working. What it is really teaching is
  that plain language works, so a good run of it makes the next one less necessary.
- **New:** `curriculum/manifest.json`, a machine-readable index of sessions and Library
  records (numbers, titles, outcomes, times, prerequisites, and which sessions run in-session
  vs. on the web), so skills stop improvising session names and times.
- **Changed:** session outcomes are **role-aware**: a default `outcome` plus an optional
  per-role `outcomes` map, used only where the lanes genuinely differ (today, Session 2). The
  canonical role list is three values: **sales · marketing · operations**.
- **Changed (`scorecard`):** the finished scorecard is now **published as a Claude Artifact**
  by the skill itself, against a fixed design contract (self-contained, CSP-safe, print-
  friendly, Builders "cool-paper" palette). The agents write markdown only; rendering the
  shareable view is the orchestrating skill's job. If artifact publishing isn't available it
  degrades honestly to the saved path rather than blocking. `scorer` slimmed accordingly.
- **Changed:** the **"Hub" / "AI Work Hub" noun is retired plugin-wide**. The builder's owned
  repo is **your agentic project**, then "your project". Every skill keeps a bridging line
  telling the model that older docs call the same repo a Hub and never to rename a builder's
  folder, so nobody with a `my-hub` directory gets churned.
- **Changed:** two more retired nouns swept out of builder-facing copy: **"the curriculum" →
  "the learning path"** (Linda, 2026-08-01) and **"the Starter" → "the starter kit"**, which
  is what Session 1 actually titles the step. The repo-root `README.md`, which sits outside
  `plugins/bluerock/` and had been missed by the earlier sweep, is included.
- **Changed:** the listing takes the **"BlueRock for AI Builders"** rename, deferred on
  2026-07-30 to the next functional release precisely so it would ride one for free. The
  community identity stays "BlueRock Builders".
- **Fixed (`check`):** the no-project message told the builder to "do steps 6 and 7." The two
  tracks number differently. Claude Desktop has eight steps and copy/clone are 5 and 6;
  Cursor has nine and they are 6 and 7, so the numbers were wrong for the default client, in
  the one message a builder reads when they are already stuck. It now names both steps by
  their real titles, which is correct on either track.

## 0.5.4 — Hub-seeded skills load from the workspace root

- **Fixed (`check`):** Hub-seeded skills and agents did not load in the sandbox because Claude Code
  starts at `/home/ubuntu` and resolves `.claude/` from there, not downward into the builder's Hub.
  `/bluerock:check` now finds the Hub by the same signature as `/bluerock:onboard`, asks before
  creating `~/.claude/skills` and `~/.claude/agents` symlinks, and points those links at the Hub's
  editable `.claude/` folders. The files stay in the builder's Hub repo; the links live outside it
  and do not appear in `git status`.
- **Changed (`check` contract):** the install-pane description and body no longer promise a purely
  inspection-only check. The new contract is stricter where it matters: never change anything without
  asking, never seed a stale Hub, never clobber a real `~/.claude/skills` or `~/.claude/agents`
  directory, and silently no-op when the links already point at this Hub.
- **Changed (`check` receipt):** the plugin line now says the BlueRock plugin is ready instead of
  claiming the Hub set is ready before the Hub load path has been verified. If links
  were just added, the report tells the builder to open a new Claude Code chat because plugins,
  skills, and agents load when a session starts. The Session 2 label is now "Meet your first
  agents."
- **Changed (`scorecard`, Starter `research`):** model-facing orchestration now says to dispatch
  ordinary subagents sequentially and not use agent-teams tooling. Human-facing "team" language
  stays intact; the mechanism is the only thing clarified.

## 0.5.3 — install-listing copy and metadata

Copy-only. No skill, agent, or behavior changes.

- **Changed (install pane):** `plugin.json`'s description opened with "The plugin behind
  BlueRock for Builders" and the internal phrase "the run-as-is core," a distinction that only
  lands once you already know the Hub seeds editable agents too. That sentence was the last
  thing a builder read before clicking Install. It now places the plugin inside the program,
  names the Hub prerequisite plainly, and leads with the Account Scorecard.
- **Changed (browse row):** the marketplace entry's description ran 465 characters against an
  official-marketplace median of 176, so the row truncated before it said anything. Cut to 210,
  with the brand and the Hub context inside the first 100.
- **Added:** `displayName: "BlueRock Builder Toolkit"` on both the plugin manifest and the
  marketplace entry. The Discover row and install pane header were rendering the raw `bluerock`
  slug. This does not affect namespacing — `/bluerock:check` is unchanged.
- **Added:** `author`, `homepage`, `category`, and `keywords` on the marketplace entry, plus
  `repository` and `keywords` on the manifest. The install screen asks builders to trust the
  source, and none of the provenance fields were set.

## 0.5.2 — `/bluerock:check` reports a receipt and hands off to Session 2
- **Fixed (`check`):** the report said the Hub was **"alive."** The locked word is **"live"**
  (decision 2026-07-23) — it shipped on the learn site but never reached the plugin, so the
  curriculum promised one word and the product said another at the payoff moment. Now "live"
  everywhere, including the skill description.
- **Fixed (`check`):** the report's optional tip invited the builder to open their Hub folder
  via `File → Open Folder` for "a focused file tree and the welcome greeting." In the cloud
  workspace that **reloads the window over the SSH connection and drops the attach** — the same
  failure Session 1 step 7 warns about — and the greeting it promised can't fire from the
  workspace root anyway. The tip is gone, and the skill is now explicitly barred from ever
  suggesting the builder open the Hub folder. The Hub sitting one level below the workspace
  root is the intended shape, not a problem to fix.
- **Changed (`check`):** the all-clear is a **four-line ✅ receipt** under the milestone
  headline (Claude Code · your Hub · the plugin · under the hood), not a single flat line.
  0.4.11 collapsed the checks to one sentence to avoid a "parts inventory," but Claude Code
  renders every tool call anyway, so the collapse hid nothing and cost the builder the visible
  proof. A single failure marks that one line ❌ and shows one fix; it never becomes a report
  about everything that could be wrong.
- **Changed (`check`):** the report now **links** where it points. It named Session 2 without a
  URL, leaving the builder to go find learn.bluerock.io from inside an editor panel at the
  highest-momentum moment in setup. It now carries the Session 2 link as the call to action and
  a quieter BlueRock Builders Discord line beneath it. The no-Hub path likewise links back to
  Session 1 instead of naming a step that no longer exists by that name.
- **Changed (naming, Linda 2026-07-27):** plugin skills are always written with the full
  `/bluerock:` prefix; skills and agents seeded in the builder's Hub stay bare (`/capture`,
  `daily-brew`). Written into `check` as a standing rule and applied across the plugin README,
  which still taught builders to drop the prefix.
- **Vocab:** "your cloud workspace" → **"your secure workspace"**; "the template" → **"the
  Starter project"**; the no-Hub path points at Session 1 steps 6–7 by their real titles.
- **Fixed (public copy, was two releases stale):** the marketplace catalog description and the
  repo's root README both still led with the Account Research dossier as the plugin's marquee
  feature — that moved to the Hub seed in 0.5.0 and is no longer in the plugin — and neither
  mentioned the Account Scorecard, which is the actual first win. The root README also still
  taught builders to drop the `/bluerock:` prefix. Both rewritten: Scorecard first, the
  run-as-is vs. make-it-yours split made explicit, and a note that custom marketplaces don't
  auto-update. The root README had drifted because nothing synced it — it now has a source of
  truth in `marketing-hub` alongside the rest of the plugin.
- **Fixed:** the plugin README said Claude Code runs "inside Cursor." The workspace serves
  **Cursor or VS Code**.

## 0.5.1 — scorer: honest Fit default + richer scorecard artifact
- **Fixed (`scorer`):** when `objectives.md` is absent, Fit is now scored against a **general
  business profile** with a required one-line caveat ("set your objectives to score against
  what you actually sell"), and must **not** reward the account for being AI-focused/buzzy —
  that's the builder's ICP to define, not ours. Validated against a real run (Cognition, no
  objectives.md) where the old "score against a sensible default" wording let the scorer
  invent an AI-favoring ICP. Timing/Reachability still score from scan facts; only Fit carries
  the default caveat. Strengthens the priming payoff (Fit sharpens after `/bluerock:onboard`).
- **Changed (`scorer` artifact):** the scorecard artifact now renders a company **descriptor
  line**, a rating-colored dot per dimension, a **Sources** chip row (paying off the "N
  sources" count), and the footer `Built with BlueRock · Account Scorecard · scout + scorer` —
  so the real output matches the builders.bluerock.io landing mockup. Header subline carries
  the scored date.

## 0.5.0 — plugin = run-as-is core; editable agents + skills move to the Hub
- **Changed (delivery model, Linda 2026-07-22):** the plugin is now the **run-as-is core**,
  and everything meant to be **edited and owned** ships seeded in the builder's Hub (`.claude/`)
  instead of the plugin. Rationale: the lesson is "edit agents and create more," and a plugin's
  agents live read-only in a cache (you must fork to edit). Project-scope `.claude/agents/` and
  `.claude/skills/` are directly editable, committed, and **outrank** the plugin (project > user >
  plugin), so seeding in the Hub is clean and gives one editable home. Keeping `wrap-up` + `check`
  plugin-owned is deliberate — it protects the dashboard schema.
- **Plugin now ships:** skills `onboard`, `today`, `wrap-up`, `check`, and the new **`scorecard`**
  team; agents `scout` + `scorer`. That's it.
- **New — Account Scorecard (`/bluerock:scorecard <company>`, "score Acme Corp"):** a fast,
  tight two-agent team (`scout` scans, `scorer` grades **Fit / Timing / Reachability** + a "why
  now" + a recommended next action) that renders a one-page scorecard Claude Artifact. Built as
  the Session-2 first win — seconds, not the minutes the deep dossier takes.
- **Moved to the Hub (seeded, editable):** agents `daily-brew`, `scribe`, `meeting-prep`, and the
  Account Research team `researcher` / `signal-scanner` / `composer`; skills `meeting-recap`,
  `capture`, and `research` (now `.claude/skills/research/`, invoked bare `/research`; it dispatches
  the seeded trio). These are what a builder reads, edits, and builds on.
- **Retired:** `whats-installed` and the `toolkit/` mirror. With the editable agents and skills
  now living visibly in the Hub's `.claude/`, "make the invisible plugin visible" is moot.
  `/onboard` no longer writes the mirror; `/check` no longer points to it.

## 0.4.12 — `/check` reads as a "signs of life" milestone, not a parts inventory
- **Changed:** `/check` now reports the milestone instead of a parts-inventory checklist. The
  builder is non-dev (GTM / RevOps / ops), so the readiness report no longer lists Claude Code,
  Python, Git, and the plugin as separate green/amber line items. It **leads with the payoff**
  ("Your AI Work Hub is alive."), rolls the plumbing checks into **one** reassurance ("Your tools
  are ready."), and **surfaces a specific item only if something is actually wrong**. All the same
  read-only checks still run behind the scenes; only the framing changed.
- **Changed:** the closing line now **points to the first win** — "say hello to your first agent
  team in Session 2" — instead of sending the builder to "the curriculum" generically.
- **Changed:** the skill `description` and the no-Hub-yet pointer are reframed to the milestone
  ("came alive in your cloud workspace," *"Get the Starter → your AI Work Hub"*), matching the
  learn.bluerock.io Get Started Session 1 language. Hub-found-as-subfolder is still a PASS; a Hub
  that doesn't exist yet is still the one "needs attention" case.

## 0.4.11 — align messaging to "your AI Work Hub"
- **Changed:** builder-facing copy now names the owned repo **"your AI Work Hub"** (introduced
  once per surface, then "your Hub") to match the learn.bluerock.io curriculum and Get Started.
  `/check` now reports "Your AI Work Hub is here," points a builder without one to *"Create your
  AI Work Hub from the Starter,"* and its description says "your secure workspace" (not "BlueRock
  workspace") and "your AI Work Hub (from the Starter)" (not "starter project"). `/onboard` and
  the plugin README introduce "your AI Work Hub" at first mention and call the template **the
  Starter**. The plugin description leads with "Your AI Work Hub."
- **Changed:** `daily-brew` curriculum references renumbered to the 8-session model
  (M5 → Session 7, M2–M4 → Sessions 4–6).

## 0.4.10 — lead with the short command form (`/check`, not `/bluerock:check`)
- **Changed:** builder-facing instructions and generated output now lead with the **short
  command form** — `/check`, `/wrap-up`, `/today` — instead of the verbose `/bluerock:check`.
  Claude Code lets you drop the `/bluerock:` prefix and type the short form as long as no other
  installed tool has the same name (right now none do); the full `/bluerock:<verb>` name still
  always works and is documented as the fallback for when a short name is ever taken. The plain
  phrase ("check my workspace") stays the primary, most beginner-friendly path.
- **Changed:** `/check` now refers to the other tools by their short form in its readiness
  report, and `/whats-installed` writes `your-toolkit.md` teaching the short form (with the
  `/bluerock:` full name as the fallback), so the builder's own toolkit map models the convention.
- **Note:** naming is unchanged — this is a documentation/phrasing change only. The canonical
  namespaced name (`/bluerock:check`) is unchanged and remains valid everywhere.
- **Fixed (dashboard artifact):** `/wrap-up` now embeds the BlueRock for Builders logo as a
  base64 `data:` URI (from the Hub's `design/builders-logo-light.svg`) instead of an external
  `<img src>` — the artifact CSP blocks external images, so a file reference failed silently and
  shipped a broken logo. And the artifact topbar is now the **logo only** — no builder name,
  workspace id, or avatar. The dashboard is a read-only value mirror, not a logged-in console.

## 0.4.9 — the toolkit is organized by what it's for
- **Changed:** `/bluerock:whats-installed` now groups `your-toolkit.md` by **what each thing is for** — Set up your Hub · Your daily rhythm · Meetings · Account research — instead of a flat skills-vs-agents split. A builder thinks "I'm prepping a meeting," not "I need an agent," so the map now reads that way. Each item keeps a small `(run)` / `(specialist)` tag so the distinction survives, and anything installed that doesn't match a known category lands in a "More in your toolkit" catch-all — never dropped, never misfiled — so the map stays honest as new skills and role-specific packs ship. Because `/bluerock:onboard` delegates the summary layout to this skill, the toolkit a builder sees on first open is organized the same way, with no duplicated logic.
- **Changed:** the plugin `README.md` now leads with a scannable "What's in the toolkit" category table (same four categories), so the marketplace listing reads as an organized catalog rather than a prose list.

## 0.4.8 — dashboard + dossier delivered as Claude Artifacts (no port, no browser)
- **Changed:** `/bluerock:wrap-up` no longer serves the dashboard on a workspace port (`python3 -m http.server 8137`). The beta workspace is a remote, headless container and the Connector doesn't forward ports, so `localhost` was never reachable from the builder's machine. wrap-up now publishes the dashboard as a **Claude Artifact** — hosted, opens in-panel, zero port / zero browser / zero install. It builds a single self-contained, CSP-safe HTML page from the rolled-up data (inline CSS + data, no external requests, system-font fallbacks in the cool-paper look). The in-panel numbers readout stays the always-works fallback, and `design/dashboard-data.js` is still written as the data of record.
- **Changed:** the artifact dashboard is a **read-only value mirror** — **CTA buttons and the trial countdown are removed**. The trial clock isn't passed into the workspace, and conversion + trial timing belong in the email lifecycle and Console, not the dashboard. (A dead button in a sandboxed artifact is worse than no button.)
- **New:** `/bluerock:research` now also renders the Account Research **dossier as a polished Claude Artifact** (clean report page, citations carried through, CSP-safe) in addition to the markdown file. Seeing a finished, shareable work product is the aha; the markdown stays the source of record + the thing pushed to the repo.
- **Note:** both artifact steps degrade honestly — if artifact publishing isn't available in the builder's environment, the skill says so and falls back to the in-panel readout / saved file rather than blocking.
- **Changed:** `/bluerock:onboard` now generates the visible `toolkit/` mirror as part of first-time setup (the same read-only copies `/bluerock:whats-installed` writes), so a builder's skills and agents are browsable in their own file tree from the very first session. Previously the toolkit only appeared once the builder knew to run `whats-installed`, so a freshly provisioned workspace looked empty of BlueRock tools — confusing, and hard to review or fork. This is the product-layer fix for user-scope invisibility; the plugin stays account-scoped (run-anywhere + updatable) and is preloaded on the workspace image — no project-scoped `.claude/` skills baked in (which would shadow the plugin and can't auto-update).
- **Changed:** `/bluerock:check` now confirms the visible `toolkit/` folder is present (in addition to the version-currency check), with a soft, optional invitation to generate it if absent — never a "needs attention."

## 0.4.7 — see the actual skill/agent files (`toolkit/` mirror)
- **Changed:** `/bluerock:whats-installed` now also writes read-only copies of the **actual** skill and agent files into a visible `toolkit/` folder at the Hub root (`toolkit/skills/<name>.md`, `toolkit/agents/<name>.md`, plus a `toolkit/README.md`), in addition to the `your-toolkit.md` summary. The plugin installs at user scope, so its files live in an opaque plugin cache (`~/.claude/plugins/marketplaces/<hash>/…`) the builder can't browse from the Cursor file tree; the mirror puts openable copies in their own workspace so they can read how any skill or agent actually works. Each copy is verbatim and carries a "reference copy — editing does nothing, copy into `.claude/` to make it yours" note (the fork-to-own path). The folder is overwritten each run, so it tracks plugin updates. Live/updatable source stays the plugin — this is a browsable window onto it, not a second copy that can drift silently.

## 0.4.6 — toolkit freshness: seed placeholder + `/check` drift nudge
- **Changed:** `/bluerock:whats-installed` now writes a machine-readable marker as the first line of `your-toolkit.md` (`<!-- bluerock-toolkit-version: X.Y.Z -->`, the real installed version), so freshness is detectable.
- **New:** `/bluerock:check` reads that marker and, when the toolkit list is missing, still the seeded placeholder, or an older version than what's installed, adds one **soft, optional** line inviting the builder to say "what can I do" to (re)generate it. It never marks this "needs attention" and never nags when it can't read a version. This closes the gap where a plugin update left a builder's toolkit list silently stale — the plugin updates at account scope, but nothing told them to refresh their in-Hub map.
- **Note (hub-starter):** the starter template now ships a placeholder `your-toolkit.md` so the file exists on first open and points the builder to "what can I do." The placeholder is intentionally not a list of skills (a static list in the template would go stale after clone and can't be updated); the live list is always generated by `/bluerock:whats-installed` from the installed plugin.

## 0.4.5 — `/check`: a Hub found as a subfolder is a PASS
- **Fixed:** `/bluerock:check` used to mark the Hub line amber ("Your Hub — needs attention") and tell the builder to open the `my-hub` folder and re-run to "turn green" whenever the session started one level above the Hub (the normal cloud/SSH case, and exactly what the Cancel-the-clone-popup flow produces on purpose). That contradicted our own design: the plugin installs at user scope so tools run from anywhere, and every skill self-heals into the Hub, so being a level above it is fine — the builder does not need to open the Hub to be ready. Now, a Hub found right here **or** as a subfolder nearby (e.g. `my-hub`) is a **PASS**. Opening the folder is offered only as an optional nicety (a focused file tree + the CLAUDE.md welcome greeting), never a required step. "Needs attention" on the Hub line is now reserved for the one real case: the Hub hasn't been created yet.

## 0.4.4 — see what's installed (`/bluerock:whats-installed`)
- **New:** `/bluerock:whats-installed` (say "what can I do" / "what's installed" / "show my toolkit"). The plugin installs at user scope, so its skills and agents don't appear as files in the builder's Hub — they can't browse what they have. This skill reads the actually-installed plugin (skills + agents + version) and writes a friendly, browsable `your-toolkit.md` into the Hub, so there's an in-Hub map of what the builder can do. Re-run anytime to refresh after an update. Read-only against the plugin; the only thing it writes is `your-toolkit.md`. `/bluerock:check` now points to it.

## 0.4.3 — wrap-up shows your numbers in the panel first
- **Changed:** `/bluerock:wrap-up` now prints a short, honest readout of the session (runs + what each did, session length, priorities set/closed/carried, success rate, cost-if-known) **in the panel first**, so the payoff lands with no server or port involved. It then still serves + offers to open the visual `design/dashboard.html`. Rationale: in the VS Code/Cursor extension over remote SSH, the served `localhost` port is not always reachable from the client (Connector port-forwarding gap), so the visual open can fail; the in-panel numbers degrade gracefully. The visual-open step is intentionally unchanged for now (we want the port issue surfaced until the Connector forwards ports — see `bfb-beta-onboarding-friction-report.md`).

## 0.4.2 — `/check` stops gracefully when there's no Hub yet
- **Fixed:** `/bluerock:check`, when run before the builder has created their Hub (common — they test the check early), used to widen the search and spider the home folder looking for a Hub that doesn't exist. It now takes one quick look (`ls */CLAUDE.md`, `ls ~/*/CLAUDE.md`), and if nothing turns up, stops and says plainly "you haven't created your Hub yet — do the Create-your-Hub step," treating it as a normal post-setup state rather than an error. No more spidering.

## 0.4.1 — run correctly at user scope (Hub anchoring)
- **Fixed:** the plugin installs at user scope (`~/.claude`), so its skills load from *any* folder — but in the cloud workspace the Hub is a subfolder of the container, so a skill firing from the wrong folder used to scatter files (profile, notes, dashboard data) outside the Hub, silently. Every file-touching skill (`onboard`, `today`, `capture`, `meeting-recap`, `research`, `wrap-up`) now anchors to the Hub first: it identifies the Hub by its signature (`CLAUDE.md` + `design/` together, not a fixed folder name), finds it a level down or via `find` when the session started in the home folder (the common SSH/cloud case), resolves its **absolute path** at runtime, and writes to that full path — so nothing leaks into the container home even when Claude Code is launched from outside the Hub.
- **`/bluerock:check`** now *fixes* a wrong-folder situation instead of only flagging it — it walks the builder back into their Hub (`cd`, or reopen the folder) and asks them to re-run.
- **`/bluerock:onboard`** fills `CLAUDE.md` in place and preserves the rest (the session-start greeting block), rather than overwriting the whole file.
- **Clarified** the two `.bluerock/` locations in `wrap-up`: the home `~/.bluerock/workspace.json` (Eng-provisioned facts) vs the Hub's own `.bluerock/runs.json` (run history).
- Docs: install URLs point at `bluerock-io/claude-plugins` and `bluerock-io/hub-starter`. Still skills/commands/agents only — no MCP, no hooks.

## 0.4.0 — agent-example teams (Account Research)
- **New:** the **Account Research** agent team, folded into this plugin (was the separate `bluerock-examples` plugin). `/bluerock:research <company>` runs three agents in sequence — **researcher** (company profile), **signal-scanner** (recent, dated signals), **composer** (the dossier) — and writes a sourced dossier to `my-work/account-research/<company>/<company>.md`: overview, recent signals, and strategic angles, in your voice.
- Reads `voice.md` + `objectives.md` (from `/bluerock:onboard`) so the angles and tone are yours. Public-web research via Claude Code's built-in `WebSearch` / `WebFetch` — no MCP, no hooks. Cites sources; marks gaps instead of inventing.
- **Consolidation:** one `bluerock` plugin now ships the daily rhythm **and** the agent-example teams, so every command is uniformly `/bluerock:<verb>` (incl. `/bluerock:research`). The first example team; Insights Analyzer and Comparative Research come next.

## 0.3.0 — priming (get to know your Hub)
- **New:** `/bluerock:onboard` — the get-to-know-you. Paste what ChatGPT/Claude already knows about you (via the portability prompt) plus a couple of writing samples; it interviews for gaps and writes three builder-owned files: `CLAUDE.md` (who you are + how to help), `voice.md` (how you write), and `objectives.md` (what you're working on — which `daily-brew` reads to rank your focus).
- **Why:** knowing the builder well is the highest-leverage, most-compounding setup step — every downstream skill produces output that's actually yours. The voice guide is the entry carrot.
- Paste-back, self-distill (one skill writes all three files). Single `voice.md` at beta; multi-profile reserved as a later add. Still skills/commands/agents only — no MCP, no hooks.

## 0.2.0 — the daily operating rhythm
- **New:** `/bluerock:today` (living priorities in `today.md`), `/bluerock:capture` (fast intake), and the `meeting-prep` agent (before-a-meeting brief; the before to `meeting-recap`'s after).
- **Renamed:** `follow-up-email` → `meeting-recap` (it's a recap you send; broad triggers kept).
- **Changed:** `daily-brew` now seeds `today.md` and opens by closing yesterday's loop (gained Write/Edit tools). `scribe` reframed from "end-of-day" to continuous capture. `wrap-up` tallies `today.md` (set/closed/carried) into the dashboard `priorities` block.
- **Meta from provisioning:** `wrap-up` + `daily-brew` read `.bluerock/workspace.json` (`provisioned_at` → trial countdown, plus builder / workspace / region), with an honest fallback when absent (neutral "Trial," generic name — never scrape boot/file timestamps). Provisioning contract: `bfb-workspace-facts-spec.md`.
- Motion: capture → brew → today → recap/prep → wrap. Still skills/commands/agents only (no MCP, no hooks). Dashboard `priorities` panel ships in try-bluerock (separate PR).

## 0.1.0 — initial set
- **Agents:** `daily-brew` (start-of-day brief from yesterday's notes), `scribe` (end-of-day note filer). They pair as a loop; in the curriculum the builder learns to build their own, which auto-overrides these.
- **Skills:** `/bluerock:wrap-up` (session log + build-dashboard refresh + optional commit/push + continuation prompt), `/bluerock:check` (read-only readiness check), `/bluerock:follow-up-email` (draft a follow-up from call notes).
- Skills/commands/agents only — no MCP servers, no hooks (safe-by-default install).
