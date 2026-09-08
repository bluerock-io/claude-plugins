# Version drift — the shared check

Not a skill. Three skills read this file so the procedure and the wording live in one
place: `/bluerock:wrap-up` and `/bluerock:learn` carry the tripwire, `/bluerock:check`
carries the explanation and the one action.

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

- **`check` — the explanation and the one action.** Auto-update ships on, so lead with the
  fact that it catches up on its own, then offer the single action for a builder who does
  not want to wait. Something close to:

  > Your BlueRock tools are behind the published ones, so some newer skills have not
  > reached you yet. They update themselves in the background, so this usually sorts
  > itself out the next time you start a session. If you would rather have them now, open
  > `/plugin`, go to **Marketplaces**, pick **bluerock**, and choose **Update marketplace**.

  Never a version number. And `check` 7b still matters: it flips auto-update on for a
  builder whose switch was never set, which is what makes the first sentence true for them.

## The one step out

**The panel, and it works anywhere `/plugin` opens** — a Claude Code terminal chat, including
the terminal inside Claude Desktop (VERIFIED 2026-09-08): open `/plugin`, go to
**Marketplaces**, select **bluerock**, and choose **Update marketplace**. The panel also shows
when it last updated and states whether auto-update is on, which is the honest answer to "am I
current?" that the **Update** button never gave.

**The same thing as two commands** (VERIFIED 2026-08-16, v2.1.233), for a builder who would
rather type than navigate:

1. `/plugin marketplace update bluerock` — refreshes the local catalog to current.
2. `/plugin update bluerock@bluerock` — applies the newest version from it.

**If neither is reachable, the honest answer is to wait.** Auto-update carries them, and
saying so is better copy than a procedure. **Do not walk a builder through removing and
re-adding the marketplace.** That six-step teardown used to live here as the Desktop fallback;
it re-authorizes GitHub, it was only ever verified once on an older build, and it is
unnecessary now that `/plugin` opens in the Desktop terminal. It was removed on 2026-09-08
rather than left as a tempting dead end.

## Who depends on this file's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`skills/wrap-up/SKILL.md`** and **`skills/learn/SKILL.md`** quote the tripwire lines
  above; **`skills/check/SKILL.md`** quotes the explanation and the one action. Change the
  wording here and all three move together, which is the reason this file exists.
- **The step out is the only copy of it**, and it is deliberately one step now. If a second
  path ever earns its way back in, it belongs here and nowhere else. The Desktop menu
  teardown was removed 2026-09-08; do not reintroduce it without walking it on a current
  build first.
- **The learn tripwire names no session numbers, deliberately.** `skills/learn/SKILL.md`
  derives everything about sessions from `curriculum/manifest.json`; a number written into
  the tripwire would be the same regression that file guards against.
