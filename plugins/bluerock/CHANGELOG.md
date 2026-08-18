# Changelog — `bluerock` plugin

## 0.9.6 — the backup step gets simpler, and Session 3 runs on your own day

- **Changed — `learn-save-your-work`: sign in first, then make the repo from the
  chat.** Walked live 2026-08-17. Signing in moved ahead of repo creation
  because `gh repo create` needs a signed-in workspace, and the browser
  create-form walk is gone from the path — a repo made this way is born empty,
  so the master/main divergence failure is designed out instead of warned about.
  The form survives as the recovery for anyone who makes the repo on github.com.
  **Finding 1 still stands:** `gh auth login` is not driven interactively; the
  device-code procedure is what runs, and the skill says so explicitly. Marked
  PROVISIONAL on one live run, with the 0.9.3 procedure kept as step 2's
  recovery. The v4 page shipped in lockstep.
- **Changed — `learn-anatomy-of-an-agent` (S3) runs on the builder's own day.**
  Step 1 offered a demo input about a call with Maria; a builder pasting our
  fiction cannot recognise anything in what comes back, and recognising their
  own words sorted is the whole payoff. The session now asks for one real thing
  and has them hand it over in their own words, with an honest floor for a
  genuinely empty day. Checkpoints moved with it. Also: the session's premise
  now says an agent is *configured by* a markdown file rather than *is* one, in
  lockstep with the page.
- **Fixed — the retired `hub-starter` slug gives way to `my-workspace`** in 17
  places across skills, checkpoints, and both READMEs, including four links a
  builder can click. The old slug still redirects, so nothing was broken;
  CHANGELOG history is deliberately left alone.

## 0.9.5 — the stuck-builder message stops pointing at steps that no longer exist

- **Fixed — `/bluerock:check`'s no-project message had the wrong diagnosis and the wrong
  fix.** It told a builder whose project wasn't found that they most likely "haven't created
  their project yet" and sent them to *Make your own copy of the starter kit* and *Clone your
  project into your workspace*. Neither step exists: since 2026-08-13 the starter is cloned
  into the container image and opened as the workspace root, so the project ships **with** the
  workspace and nobody copies it. A builder hitting the one case the skill calls "genuinely
  needs attention" was being sent after instructions that had been retired. The message now
  names the real cause — this chat isn't running in their workspace, usually an unfinished
  connection — routes to Get Started's connection steps by title for both tracks (the Desktop
  and Cursor tracks title that step differently, not just number it differently), and sends
  the connected-but-still-missing case to Discord instead of guessing, since that one cannot
  be fixed from inside the workspace.

## 0.9.4 — updates start reaching builders on their own

One problem, one release (product decision, 2026-08-17). Claude Code turns plugin auto-update **off**
by default for third-party marketplaces, so every builder has been silently opted out of
updates since their install — the root cause behind a real 0.6.4 → 0.9.2 stall, verified
2026-08-16. Official-marketplace listing can't fix it (invitation-only; and community
listing doesn't change the default), so the plugin now fixes it for its own builders.
Spec: the auto-update spec (content repo, private).

- **New — `/bluerock:check` 7b: turns plugin auto-update on, with consent.** A third
  consented repair alongside the load-path links and the template-remote cleanup: one
  field, `"autoUpdate": true`, in the `bluerock` entry of `~/.claude/settings.json` —
  nothing else in that file, ever. Asks first with the recommendation and the reason,
  preserves the whole file, refuses to touch a file that doesn't parse, silent when
  already on. This is the skill's first write outside the project, under a narrow
  carve-out written into the repo `CLAUDE.md` §6 the same day (the §4.1 decision).
- **Changed — `shared/version-drift.md` gets the verified way out.** The primary path is
  now two terminal commands (`/plugin marketplace update bluerock`, then
  `/plugin update bluerock@bluerock` — VERIFIED 2026-08-16, v2.1.233, no teardown, no
  re-auth, no restart); the six-step Desktop teardown stays as the PROVISIONAL fallback.
  The file also names the real root cause — a stale local marketplace clone, never a
  missed version bump — so the greyed Update button stops being read as evidence.

## 0.9.3 — the backup step ships, and the sign-in survives an agent driving it

The release that lets BlueRock team testers follow the v4 pages with a matching plugin
(product decision, 2026-08-16). Everything here is grounded in the same day's walkthroughs and
captures — the team's fresh-image forensics and GitHub walk, a screen recording, and
the five-findings doc.

- **New — `learn-save-your-work`: the standalone backup step between Sessions 6 and 7**
  (product decision, 2026-08-14). Six beats: the GitHub account, the empty
  private repo (the master/main divergence trap, with the walked create-form controls),
  the device-flow sign-in, the first backup behind two guards (secrets scan,
  shallow-history completion), the refresh-the-repo-page proof, and what changes at every
  wrap-up from now on. Fires on "back up my project" or
  `/bluerock:learn-save-your-work`. No manifest row on purpose — its completion is
  inspectable (the remote and the sign-in ARE the record), and the row is Eng-cadence.
- **Fixed — the sign-in can actually be driven.** `gh auth login` waits on an interactive
  terminal a session doesn't have and hangs silently — three attempts documented,
  including under a pseudo-terminal. The skill now drives GitHub's device endpoint
  directly, shows the builder only the code and the address, and pipes the token straight
  into `gh auth login --with-token` so it is never printed. One poller, one consumer: a
  second status check consumes the one-time token issuance and strands the poller — this
  cost a real failure on 2026-08-16 and is now written into the step.
- **Changed — the identity ask explains itself before it fires.** After a successful
  sign-in, "what name and email should your saves be recorded under?" reads as a failure
  (a real builder hit exactly this). The separating sentence comes first — signing in
  proves entry; the byline is written separately — and the privacy-preserving
  `<id>+<login>@users.noreply.github.com` form is offered, with the `user/emails` 404
  trap flagged (this sign-in's scope doesn't cover it).
- **Changed — `learn-put-an-agent-on-a-schedule` (S7) hands the backup to the step that
  owns it.** The interim first-backup teaching in Before-you-start becomes what its own
  text promised: a check and a pointer at Save your work. This also retires "walk
  whatever git asks for honestly" — the clause that sent an agent into the
  `gh auth login` hang.
- **Changed — `learn-get-started` (S1) catches up to the walked screens.** The Console's
  new Connect page (the URL lives on it directly — no "Connect now", no detail page);
  the Connector is a portable app downloaded from that same page (no installer — Mac
  unzip → Applications, Windows the download IS the app); host values copy from the
  Connect Claude dialog, copy-never-retype; and the plugin install goes chat-first
  (read the seeded `bluerock-plugins.md`, hand the address with its copy button
  in-conversation) then the walked Desktop path — + → Add plugins… → Add marketplace →
  Add from a repository, with Anthropic's trust warning named before it surprises
  anyone. Cursor/VS Code keeps its real `/plugins` panel route.


## 0.9.2 — five session skills reach the v4 standard, and the plugin stops saying "Hub" out loud

The batch release carrying the S4–S8 skill quality passes from the learn v4 rollout, plus
three mechanical fixes the concept-ledger audit routed here. Safe ahead of the page cutover:
every pass kept live-page compatibility notes deliberately (e.g. Session 6's step-1 redirect
stays for anyone on the live page until cutover retires both together).

- **Changed — `learn-give-your-agent-memory` (S4), `learn-turn-a-task-into-a-skill` (S5),
  `learn-assemble-a-team-of-agents` (S6), `learn-put-an-agent-on-a-schedule` (S7),
  `learn-run-your-system` (S8): aligned to the S2 standard.** The teach loop, inspectable
  checkpoints, honest-floor recoveries, the help ladder (recover once → `/bluerock:help` →
  Discord with the ask pre-written), rationed encouragement, and the finding-1 vocabulary
  sweep — "save a checkpoint" / "back up to GitHub"; bare git verbs never reach the builder,
  with the teacher's own commands as named silent exceptions. On S8 the skill carried six
  bare git verbs to the page's two — a page-only sweep would have looked complete. Standing
  rules added per skill so the words cannot return.
- **Changed — S7's `Before you start` does the missing GitHub step's whole job, honestly.**
  The hard block (the path's only one, with 0.8.2's template-remote guard) now walks the fix
  in builder vocabulary, creates the repo EMPTY (the master/main divergence trap — Eng,
  2026-08-15), and carries the help ladder. Hands back to the standalone "Save your work"
  step when that ships.
- **Changed — the "Hub" bridge is recognize-only, in seven skills.** The bridging clause
  ("some older docs call the same repo a Hub") stays for old folder names, but each now says:
  recognize the old name, never speak it — to the builder this is always "your project."
  Found live: a session said "The Hub is here at…" on a real builder's screen.
- **Fixed — `curriculum/manifest.json`:** `meeting-recap` is used in Session 5 and its
  `used_in_sessions` said so to nobody (`[]` → `[5]`); `wrap-up` closes every session, not
  two (`[2, 8]` → `[2..8]`); wrap-up's library one-liner said "commits" to a builder's face —
  now "saves a checkpoint."
- **Changed — `wrap-up` answers "wrap up my chat".** The trigger list gains the chat-sense
  alias alongside the verbatim "wrap up my session" (nothing removed — the two senses of
  "session" collided on screen, and the skill now answers both).

## 0.9.1 — the next step happens in this chat, and the builder's own words get kept

- **Changed — `check`'s closing:** the call to action is now the in-chat one ("Say **teach
  me Session 2** in this chat…") with the session page demoted to companion ("prefer to see
  it first?") and Discord a quieter third. Every session runs in-session; linking out at the
  ready moment broke the momentum the milestone had just created. The rule is now in the
  authoring guide: when an in-chat equivalent exists, it is the primary CTA.
- **Fixed — `onboard` keeps the samples themselves:** writing samples are saved verbatim
  into `writing-samples/`, one file each with a kind-and-byline header; `voice.md` holds the
  distilled guide and a pointer, never a full sample (it loads on every content-skill run).
  Found 2026-08-15: onboard distilled a pasted post and discarded it, leaving no file in the
  project containing a word the builder actually wrote. Pairs with the starter kit's new
  `writing-samples/` folder (my-workspace `ee9c275`).
- **Wording — `learn-anatomy-of-an-agent`:** "the progress commit rides the save habit" →
  "the progress update rides the checkpoint habit," matching wrap-up's 0.9.0 vocabulary.

## 0.9.0 — the session stops asking what it can see, and wrap-up stops proposing what will fail

Two live runs on 2026-08-15 produced the same class of finding: a skill asking a builder
for something it could have detected, or offering a builder something it had not checked
would work. A tester who ships this product hit a wall at wrap-up step 4 on a fresh
workspace with no git identity, no usable remote, and no GitHub authentication, and after
approving a purely local save still believed her files had left the workspace. Separately,
the surface question ("Desktop or Cursor?") was sent in the same message as a question
about her own work, and only the work question came back.

- **Changed — every session skill + `learn`: the surface is detected, not asked.** One
  resolution order, repeated identically in all eight places: read
  `CLAUDE_CODE_ENTRYPOINT`, map `desktop` / `cursor`, fall back to `surface` in
  `progress.json`, and only then ask, in a message of its own. A detected value always
  beats a stored one and is **never written back** — writing it back is what made the
  stored copy go stale for anyone who switched apps between sessions. `surface` survives
  in `progress.json` demoted to a last-resort fallback, documented where the template is
  defined so nobody restores its old authority. `curriculum/manifest.json` is unchanged;
  `surfaces: ["desktop", "cursor"]` stays as the vocabulary.
  **PROVISIONAL:** `CLAUDE_CODE_ENTRYPOINT=claude-desktop` was verified live; nobody has
  observed what Cursor sets. The `cursor` mapping is an assumption, and the fallback chain
  is what makes a wrong guess degrade to asking rather than to misrouting. Detection
  cannot be claimed to work on Cursor until someone running it posts
  `echo $CLAUDE_CODE_ENTRYPOINT`.
- **Changed — `learn-meet-your-first-agent-team`: the role question is asked alone.**
  **Role capture stays at first use in Session 2, asked alone — product decision, 2026-08-15.** The
  finding-5 spec recommended moving it to Session 1; capture-at-first-use wins, and the
  recommendation is overruled deliberately, not overlooked. Bundling was the actual defect:
  on the test run the role question rode along with "confirm the website you want the doc
  built from," and only the work question came back. Stored-fact questions now go in a
  message of their own, before any question about the builder's work. Session 1 asks for no
  role at all; its finding-5 change is surface detection only.
- **Fixed — `wrap-up` steps 4 and 5: check first, offer only what will succeed.** The
  skill now runs `git status`, `git remote -v`, `gh auth status`, and `git config
  user.name` / `user.email` before it proposes anything, and branches on what it finds.
  No remote means the save is local and pushing,
  backup, and GitHub are not mentioned at all, because raising them invents a problem the
  builder does not have. A remote without authentication gets the local save now and
  backup named once, as optional. A first save leads with one sentence explaining what
  saving is and where it stays. The vocabulary is **"save a checkpoint"** and **"back up
  to GitHub"**; the git words are not used as bare verbs with a builder who has not been
  taught them. A failed push, if one happens anyway, leads with what worked and must never
  be a builder's first experience of wrap-up. 0.8.2's refusal to ever push to the shared
  template is preserved inside the new branch list.
- **Fixed — `wrap-up`: an unset git identity no longer breaks the local save.** The
  fresh-init image configures no identity, so on a new workspace the very first save
  aborted with `Author identity unknown` and handed a non-developer two `git config`
  commands to run — a failure with no GitHub in it at all, at the worst possible moment.
  The state check now detects it first and repairs it with consent, in builder language
  ("What name and email should your saves be recorded under? This just labels your work in
  your own project — nothing is sent anywhere"), scoped to the project and **never
  `--global`**. Declining is fine, says plainly that saving needs a name to record it
  under, and wrap-up offers again next time. The failed commit never happens first.
- **Fixed — `learn-get-started` + `learn-meet-your-first-agent-team`: two lines that
  promised or blamed.** Session 1's close-out no longer promises "the progress commit,"
  which set up a step that would not complete; it suggests the save habit instead.
  Session 2's checkpoint 5 no longer reads a missing save as a builder skipping something
  — usually it is an authentication wall, or wrap-up correctly declining to offer what
  would fail. The checkpoint was always the log and the dashboard refresh.
- **Added — version-drift tripwires, detect-only.** `wrap-up` and `learn` each carry one
  line, **silent when clean and silent when the lookup didn't happen**; `check` carries the
  explanation and the steps out. A builder installed the plugin one day and was still on
  the previous version the next, missing everything that had shipped in between, because
  the in-app **Update** button compares against the app's *cached* copy of the marketplace:
  a greyed-out Update button does not mean up to date. The published version is read from
  the raw `plugin.json` URL (not `marketplace.json`, which carries no version field, and
  not Releases, which the repo does not publish), cached to once per day in the workspace
  folder, and **silent on any failure** — a check that goes red because GitHub was slow
  teaches builders to ignore it. Builder-facing copy names what is missing, never a version
  number. Procedure and wording live in one new file, `shared/version-drift.md`, so the
  three skills cannot drift apart.
  **PROVISIONAL:** the recovery steps (remove plugin → remove marketplace → re-add → install
  → accept "Sync automatically" → fully quit and reopen) were verified once, on Claude
  Desktop, on 2026-08-15. Order matters: reinstalling without removing the marketplace
  reads the same stale cache and reproduces the old version.
- **Added — `check`: two detect-only checks.** Unfilled profile files (`CLAUDE.md`,
  `voice.md`, `objectives.md` still bracketed, `your-toolkit.md` still `placeholder`) are
  reported as the thing that will make their output better, never as a failure, and route
  to `/bluerock:onboard`. Neither new check offers a repair, because neither can be fixed
  from inside the workspace, and `check` **never** fills a profile file in for a builder.
- **Changed — `distiller` + `messaging-doc`: Gaps is a required section.** For the
  first-win session it was the most valuable output and the one most likely to be omitted:
  a builder knows roughly what their own site says, and cannot see the distance between the
  language they use internally and the language the site carries. It now always renders,
  with an explicit "nothing inconsistent turned up" state, and the run's report and Session
  2's debrief both lead with it.
- **Fixed — `wrap-up`: two sessions wrapping up at once no longer lose runs.** Builders
  run more than one chat, and on 2026-08-15 two wrap-ups raced against one project:
  `dashboard-data.js` was rewritten mid-write and `runs.json` gained atoms from a session
  that started later. The skill now re-reads `dashboard-data.js`, `.bluerock/runs.json`,
  and `session-log.md` immediately before writing each, merges rather than overwrites,
  re-reads and reconciles again if a file moved under it, treats `session-log.md` as
  append-only, and **leaves another session's reconciliation alone when it is more
  complete** — which is exactly the judgment call that got made correctly on the day, now
  written down instead of improvised.
- **Changed — `wrap-up`: the data contract is the authority, in both directions.** The
  skill writes only the fields `design/dashboard-data-contract.md` defines, in its
  structure, with no invented fields and no format improvisation, and reads that file
  rather than working from memory. The contract now names this skill as its one consumer,
  so the dependency is recorded at both ends.
- **Changed — `wrap-up`: cost says "coming soon," never a number it cannot stand behind.**
  `cost` gains `available`, false by default. A beta workspace has no pricing table, so
  tokens cannot become dollars honestly, and the old zero rendered as `$0` with a flat
  sparkline and a "vs yesterday" pill — a real, reassuring figure standing in for a
  missing one. Rates are never estimated or carried over. (Renderer and contract ship in
  the starter kit; this is the writer half.)
- **Changed — `agents/`: em dashes stripped from all four agent specs.** They were written
  in the style they then reproduce, and two strings in `distiller.md` are mandated
  verbatim into every messaging doc every builder generates, bypassing the builder's own
  `voice.md` entirely. Those two are now style-neutral. No behavior change beyond
  punctuation.

## 0.8.2 — nothing ever pushes to the template

Earlier workspace images shipped the builder's project still pointing its `origin` at
BlueRock's shared template (`bluerock-io/my-workspace`) — so a builder's first backup was
rejected with a confusing permission error, and anyone with org write could silently land
their work on the template. Eng is fixing the image (fresh `git init`, no remote); this
release protects every existing workspace in the meantime, and stays correct after.

- **`check`:** now inspects the project's remote. No remote or their own remote: silent
  pass. The inherited template remote: explained plainly and removed **with consent**, in
  the same ask-first shape as the load-path repair. The skill's write contract widens to
  exactly these two consented repairs.
- **`wrap-up`:** never pushes to the template remote, even when the push would succeed —
  commits locally and points at `/bluerock:check` for the cleanup.
- **`learn-put-an-agent-on-a-schedule`:** a template remote counts as missing — a routine
  is never scheduled against the shared template.

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
the learning site's page data (content repo, private).

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
  Workspace**, the agreed term, and the description is marketplace-visible — it is the last
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
  "the learning path"** (product decision, 2026-08-01) and **"the Starter" → "the starter kit"**, which
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
- **Changed (naming, product decision 2026-07-27):** plugin skills are always written with the full
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
  truth in the content repo alongside the rest of the plugin.
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
- **Changed (delivery model, product decision 2026-07-22):** the plugin is now the **run-as-is core**,
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
