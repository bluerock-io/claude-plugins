# Version drift — the shared check

Not a skill. Three skills read this file so the procedure and the wording live in one
place: `/bluerock:wrap-up` and `/bluerock:learn` carry the tripwire, `/bluerock:check`
carries the explanation and the steps out.

**Why this exists.** A builder installed the plugin one day and was still on the version
from the day before, missing sessions that had shipped in between. Nothing told them. The
in-app **Update** button compares against the app's *cached* copy of the marketplace, so
a stale cache disables the button: a greyed-out Update button does not mean up to date.

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
  > run right here in the chat. `/bluerock:check` has the steps.

  Never name which sessions, or how many. That is the manifest's job, and the manifest
  you can read is the installed one.

- **`check` — the explanation and the steps out.** Detect-only: nothing inside the
  workspace can update the plugin, because it lives in the builder's Claude account and
  is mirrored in at connect time. Detect-but-cannot-fix is still worth reporting, as long
  as the steps are exact.

## The steps out (PROVISIONAL)

⚠️ **These are menu steps and they ship PROVISIONAL** until walked on a current build.
They were verified once, on 2026-08-15, on Claude Desktop. **Order matters:** reinstalling
without removing the marketplace reads the same stale cache and reproduces the old version.

1. Remove the **BlueRock Builder Toolkit** plugin.
2. Remove the marketplace.
3. Add the marketplace again: `https://github.com/bluerock-io/claude-plugins`
4. Install **BlueRock Builder Toolkit**.
5. Accept **"Sync automatically"** when offered. It opens a separate GitHub authorization
   window, which is a normal part of keeping the plugin current, and it is a different
   thing from signing in to BlueRock.
6. Quit the app fully and reopen it.

The ⋮ menu offers only Cursor / Show in folder / Remove. There is no refresh, and the
**Update** button is not a reliable signal.

## Who depends on this file's wording

Not part of a run. Read this before rewording anything a builder sees.

- **`skills/wrap-up/SKILL.md`** and **`skills/learn/SKILL.md`** quote the tripwire lines
  above; **`skills/check/SKILL.md`** quotes the explanation and the steps out. Change the
  wording here and all three move together, which is the reason this file exists.
- **The steps out are the only copy of them.** When someone walks the menus on a current
  build, clear the PROVISIONAL marker here and nowhere else.
- **The learn tripwire names no session numbers, deliberately.** `skills/learn/SKILL.md`
  derives everything about sessions from `curriculum/manifest.json`; a number written into
  the tripwire would be the same regression that file guards against.
