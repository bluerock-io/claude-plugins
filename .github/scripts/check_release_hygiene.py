#!/usr/bin/env python3
"""Two release guards. Run in CI on every pull request, and runnable locally.

    python3 .github/scripts/check_release_hygiene.py <base-ref>
    python3 .github/scripts/check_release_hygiene.py origin/main

GUARD 1 — a change to what builders run requires a version bump.

Merge to main IS the release for this plugin. Claude Code's auto-update compares
versions, and `/bluerock:check` compares the installed version against the published
one. So a change that ships without a bump is invisible twice: auto-update sees nothing
to fetch, and the drift check tells every builder they are current.

That is not hypothetical. On 2026-09-08, PRs #19 through #23 landed five complete use
cases, and none carried a bump. All five were live in the repo at 0.11.0, the version
already installed everywhere, and reachable by nobody. `bfb-plugin-auto-update-spec.md`
§7 proposed this exact guard on 2026-08-16 as insurance against a forgotten bump. This
is that guard, three weeks and one forgotten bump later.

GUARD 2 — the JSON files must parse.

`curriculum/manifest.json` took four hand-resolved add/add conflicts in a single
afternoon during that same release. A malformed manifest would not have surfaced until
a builder's session failed to load it.

CHANGELOG.md is deliberately exempt from guard 1: fixing a typo in a release note is
not a release. Everything else under plugins/bluerock/ counts.

To ship a change under plugins/bluerock/ without a bump, label the PR `no-version-bump`.
That is a deliberate, visible act, which is the point. A guard with a silent override is
a guard that gets deleted the first time it is inconvenient.
"""

import json
import subprocess
import sys
from pathlib import Path

PLUGIN_DIR = "plugins/bluerock/"
MANIFEST = "plugins/bluerock/.claude-plugin/plugin.json"
EXEMPT = {"plugins/bluerock/CHANGELOG.md"}
JSON_FILES = [MANIFEST, "plugins/bluerock/curriculum/manifest.json"]


def git(*args):
    return subprocess.run(
        ["git", *args], capture_output=True, text=True, check=True
    ).stdout.strip()


def version_at(ref):
    """The plugin version as of a ref, or None if the file is absent there."""
    try:
        blob = git("show", f"{ref}:{MANIFEST}")
    except subprocess.CalledProcessError:
        return None
    try:
        return json.loads(blob).get("version")
    except json.JSONDecodeError:
        return None


def check_version_bump(base):
    changed = [
        f for f in git("diff", "--name-only", f"{base}...HEAD").splitlines()
        if f.startswith(PLUGIN_DIR) and f not in EXEMPT
    ]
    if not changed:
        print("GUARD 1 skipped: nothing under plugins/bluerock/ changed.")
        return True

    base_v, head_v = version_at(base), version_at("HEAD")
    print(f"GUARD 1: {len(changed)} file(s) changed under {PLUGIN_DIR}")
    print(f"         version at {base}: {base_v}")
    print(f"         version at HEAD:  {head_v}")

    if head_v is None:
        print(f"\nFAIL: cannot read a version from {MANIFEST} at HEAD.")
        return False
    if base_v == head_v:
        print(f"\nFAIL: builder-facing files changed and the version is still {head_v}.")
        print("\nWhy this fails the build, not just warns:")
        print("  Merge to main is the release. Auto-update compares versions, so it will")
        print("  fetch nothing, and /bluerock:check compares installed against published,")
        print("  so it will report every builder as current. The change ships to nobody")
        print("  and nothing says so.")
        print("\nFiles that triggered it:")
        for f in changed[:20]:
            print(f"  {f}")
        if len(changed) > 20:
            print(f"  ... and {len(changed) - 20} more")
        print(f"\nFix: bump \"version\" in {MANIFEST} and add a CHANGELOG entry under it.")
        print("     A new skill or agent is a minor. A copy or wording fix is a patch.")
        print("\nOr, if this genuinely ships nothing to builders, label the PR")
        print("  no-version-bump")
        return False

    print("\nPASS: version moved with the change.")
    return True


def check_json_parses():
    ok = True
    print("\nGUARD 2: JSON files parse")
    for rel in JSON_FILES:
        p = Path(rel)
        if not p.exists():
            print(f"  SKIP  {rel} (absent)")
            continue
        try:
            json.loads(p.read_text(encoding="utf-8"))
            print(f"  ok    {rel}")
        except json.JSONDecodeError as e:
            print(f"  FAIL  {rel}: {e}")
            ok = False
    if not ok:
        print("\nFAIL: a JSON file does not parse. This usually means a merge conflict")
        print("      was resolved by hand and left the file malformed. A builder's")
        print("      session is where that surfaces otherwise.")
    return ok


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    base = sys.argv[1]
    results = [check_version_bump(base), check_json_parses()]
    if all(results):
        print("\nAll release guards passed.")
        return 0
    print("\nRelease guards failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
