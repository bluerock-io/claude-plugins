# Version drift — the shared check

Not a skill. Three skills read this file so the procedure and the wording live in one
place: `/bluerock:wrap-up` and `/bluerock:learn` carry the tripwire, `/bluerock:check`
carries the explanation, and the manual route for anyone who asks.

**Why this exists.** A builder installed the plugin one day and was still on the version
from the day before, missing sessions that had shipped in between. Nothing told them. The
in-app **Update** button compares against the app's *cached* copy of the marketplace, so
a stale cache disables the button: a greyed-out Update button does not mean up to date.

**The original root cause** (verified 2026-08-16, against a genuine 0.6.4 → 0.9.2 stall): the
plugin comes from a third-party marketplace, and Claude Code turns auto-refresh of the
local marketplace clone **off** by default for those. The clone stays pinned; every
reinstall faithfully re-resolves the old version from it. It was never a missed version
bump. This is also why a greyed Update button proves nothing either way — it can mean
genuinely current or a stale clone, and only the fetch in this file's procedure can tell
them apart.

**What changed, and it changes what a builder should be told** (verified 2026-09-08, in a
provisioned workspace): **auto-update ships on.** The workspace image sets it, `check` 7b
sets it for anyone the image missed, and a workspace was observed reaching the current
published version on its own. So drift is now normally **temporary**: Claude Code refreshes
the marketplace and its installed plugins in the background shortly after a session starts,
and the newer version loads on the next one. Reporting drift as something a builder must go
and fix overstates it. Report it as something that catches up, with one action for anyone
who would rather not wait.

## The procedure

Run it quietly. The builder sees nothing unless there is something to say.

1. **Read the installed version** from `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`.
2. **Read the cache** at `~/.bluerock/plugin-version-check.json`, shaped
   `{ "checked": "YYYY-MM-DD", "published": "<version>" }`. If `checked` is today's date,
   use the cached `published` and make no network call.
3. **Otherwise fetch once**, with a short timeout:

   ```bash
   curl -sfL --max-time 5 https://raw.githubusercontent.com/bluerock-io/claude-plugins/main/plugins/bluerock/.claude-plugin/plugin.json
   ```

   That raw URL is the source of truth. Not `marketplace.json`, which carries no version
   field, and not GitHub Releases, which the repo does not publish. On success, write the
   cache with today's date. **On any failure, stop and say nothing** — no error, no line
   in the report, no retry. A check that goes red because GitHub was slow teaches builders
   to ignore it.
4. **Compare.** Equal, or the fetch was skipped or failed: silent. Installed version lower
   than published: drift, reported per the skill you are in.

The cache is the only thing this procedure writes, it lives in the workspace folder, and
it never touches the builder's project.

## What the builder hears

**Never a version number.** Builder-facing copy carries none, so name what is missing
instead. And never claim an all-clear on a lookup that did not happen: if the fetch was
skipped or failed, the version is simply not part of this run's report.

- **`wrap-up` — the tripwire, one line, nothing more.** It does not diagnose and it does
  not repair:

  > Something in your setup needs attention. Run `/bluerock:check` when you have a minute.

- **`learn` — the same tripwire, worded for the one thing a builder loses by being
  behind**, since a session that runs in the chat may only exist in the newer version:

  > Your BlueRock tools are behind the published ones, and updating can add sessions that
  > run right here in the chat. `/bluerock:check` explains it.

  Never name which sessions, or how many. That is the manifest's job, and the manifest
  you can read is the installed one.

- **`check` — name what is missing, offer to walk it, promise nothing.**

  > Your BlueRock tools are behind the published ones, so some newer skills have not
  > reached you yet. Ask me to update them and I will walk you through it, it takes a
  > minute.

  **This line is deliberately written so it is true either way**, because whether a
  workspace catches up on its own is **unresolved** (see below). Two rules make it that way:

  - **Do not promise it resolves itself.** Auto-update ships on and a terminal session was
    seen reaching the current version, but the workspace's own marketplace clone sat frozen
    for three weeks with the flag true the whole time. Until one surface is watched going
    from behind to current unaided, "it will sort itself out" is a guess.
  - **Do not put `/plugin` in this line.** `check` speaks in the chat panel and **`/plugin`
    does not run there**: it answers *"/plugin isn't available in this environment."* Naming
    a command that fails in the surface the builder is reading it in is worse than naming
    nothing. Offer to walk them, then use the route below.

  Never a version number. `check` 7b is also **near-inert on the current image**: the flag
  already ships true, so 7b passes and never asks. Keep it for builders whose switch was
  never set, but do not count on it doing anything.

## Forcing an update, only if the builder asks

**The surface comes first, because the command is surface-bound.** `/plugin` runs in an
interactive Claude Code terminal. It does **not** run in the Claude Desktop chat panel, which
answers *"/plugin isn't available in this environment"* (observed 2026-09-08). So never hand a
builder `/plugin` without first telling them where to type it.

**Open a terminal first.** In Claude Desktop that is the **`>_` icon at the top right, or
**⌘J** (VERIFIED 2026-09-08: `/plugin` opens there and showed the bluerock marketplace with
auto-update enabled). Walk the builder to the terminal before naming any command.

- **The panel:** run `/plugin`, go to **Marketplaces**, select **bluerock**, choose **Update
  marketplace**. It also shows when it last updated and whether auto-update is on, which is
  the honest "am I current?" the **Update** button never gave.
- **Or two commands** (VERIFIED 2026-08-16, v2.1.233): `/plugin marketplace update bluerock`,
  then `/plugin update bluerock@bluerock`.

**If the builder is in the chat panel and does not want to move, the answer is to wait.**
Auto-update carries them, and that is the truthful answer rather than a consolation. This is
the common case, which is why the standing report says exactly that and stops.

**Do not walk a builder through removing and re-adding the marketplace.** That six-step
teardown used to live here as the Desktop fallback; it re-authorizes GitHub, it was only ever
verified once on an older build, and the Terminal pane covers the case it existed for. Removed
2026-09-08.

**UNRESOLVED, and the standing report is worded around it:** does a builder's chat-panel
session reach the current version on its own? Both of these were observed on 2026-09-08 in the
same workspace. The **terminal** session ran the current published version. The workspace's own
marketplace clone showed **no fetch in three weeks**, with `autoUpdate: true` whose mtime
matches the image provisioning second, so the flag shipped on and was never flipped by a
`check` run. Those coexist only if the terminal and the chat panel read different plugin state.
**The test:** a fresh workspace nobody else is working in, note the chat panel's loaded version,
leave it some days, look again. Do not soften the report copy until that is watched.

## Who depends on this file's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`skills/wrap-up/SKILL.md`** and **`skills/learn/SKILL.md`** quote the tripwire lines
  above; **`skills/check/SKILL.md`** quotes the explanation. Change the
  wording here and all three move together, which is the reason this file exists.
- **The manual route is the only copy of it, and it is deliberately not in the standing
  report.** `/plugin` is surface-bound and fails in the chat panel where `check` speaks, so
  the report says "nothing for you to do" and the route is offered only on request. The
  Desktop menu teardown was removed 2026-09-08; do not reintroduce it without walking it on
  a current build first.
- **The learn tripwire names no session numbers, deliberately.** `skills/learn/SKILL.md`
  derives everything about sessions from `curriculum/manifest.json`; a number written into
  the tripwire would be the same regression that file guards against.
