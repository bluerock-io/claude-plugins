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

GUARD 3 — every library record carries a tier, ships_from matches the tree, and the
use-case records carry what the discovery surfaces read (title, concept, and a
recommended_after that forms one chain).

`tier` is the single predicate a discovery surface reads to decide what a builder may
be offered. Before it existed the question was answered by the presence of optional
fields, so `scorecard` and `messaging-doc` — the two use cases a builder meets first —
silently failed the test for months, because they predate the convention that filled
`artifact` and `team`. An optional marker is not a marker, which is why this guard
requires the classification rather than hoping for it.

`ships_from` is derivable from the tree, so the guard re-derives it instead of trusting
what is typed. The repo rule is generate facts, never type them.

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

LIBRARY_MANIFEST = "plugins/bluerock/curriculum/manifest.json"

# tier answers exactly one question: may a discovery surface offer this record?
# It carries no meaning about where a record ships from — that is ships_from,
# and keeping the two apart is what makes reclassifying one record cheap.
TIERS = {
    "use-case",    # offered as a thing to run. The predicate every surface reads
    "held",        # use-case-shaped, deliberately not offered (today: research)
    "system",      # housekeeping: today, wrap-up, onboard, check, help
    "utility",     # findable conveniences, never headline
    "team-member",  # runs inside a use-case team, never offered alone
    "concept",     # reading material
}

REQUIRED_ON_USE_CASE = ("title", "team", "artifact", "roles", "one_liner",
                        "time_saved", "time_saved_minutes", "concept")

# title and concept landed 2026-09-10 with the discovery surfaces (0.14.0). `title` is
# the builder-facing name every surface prints, the same seven the catalog page on
# learn.bluerock.io prints, so one order has two readers and neither improvises. `concept`
# names the concept record (and so the session) that explains what a use case just ran;
# wrap-up's continuation prompt points at it. `recommended_after` is required to form one
# chain: the authored order, not a model. Checked below.

# time_saved was deliberately NOT required when tier landed on 2026-09-08: the
# figures were labelled estimates and copy led on compounding, so requiring the
# field would have forced two estimates to be invented for numbers nobody could
# speak. That reasoning ended on 2026-09-09, when time saved was elevated to a
# use-case value driver and became a tally on the builder's own dashboard. A use
# case with no estimate now contributes nothing to that tally and looks broken,
# so the field must exist before the use case ships.


def derive_ships_from(rid, rtype):
    """Where a record actually lives, read off the tree. None for a topic."""
    if rtype == "skill":
        path = Path(PLUGIN_DIR) / "skills" / rid / "SKILL.md"
    elif rtype == "agent":
        path = Path(PLUGIN_DIR) / "agents" / f"{rid}.md"
    else:
        return None
    return "toolkit" if path.exists() else "project"



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


def check_library_shape():
    """GUARD 3 — every library record is classified, and ships_from is re-derived.

    `tier` is the one predicate a discovery surface reads to decide what a builder
    may be offered. Before it existed, "is this a use case" was answered by the
    presence of optional fields, so `scorecard` and `messaging-doc` — the two use
    cases a builder meets first — silently failed the test for months because they
    predate the convention. An optional marker is not a marker.

    `ships_from` is derivable from the tree, so it is re-derived here rather than
    trusted. A hand-typed derivable fact is the shape that put nine wrong numbers
    in bfb-what-is-built.md.

    Required-field rule: require what must be true, never require what we have
    decided not to say. `time_saved` is deliberately absent from REQUIRED — the
    figures are labelled estimates and copy leads on compounding, so requiring the
    field would force two estimates to be invented for numbers nobody may speak.
    """
    print("\nGUARD 3: library records are classified")
    p = Path(LIBRARY_MANIFEST)
    if not p.exists():
        print(f"  SKIP  {LIBRARY_MANIFEST} (absent)")
        return True
    try:
        records = json.loads(p.read_text(encoding="utf-8")).get("library", [])
    except json.JSONDecodeError:
        print("  SKIP  manifest does not parse (GUARD 2 reports it)")
        return True

    problems = []
    for e in records:
        rid, rtype, tier = e.get("id", "?"), e.get("type"), e.get("tier")

        if tier not in TIERS:
            problems.append(f"{rid}: tier is {tier!r}, not one of {sorted(TIERS)}")
            continue

        if tier == "use-case":
            # presence, not truthiness: a time_saved_minutes of 0 is present and
            # wrong, and reporting it as "missing" sends the reader to the wrong fix
            missing = [f for f in REQUIRED_ON_USE_CASE if f not in e or e[f] in ("", None, [])]
            if missing:
                problems.append(f"{rid}: tier use-case is missing {', '.join(missing)}")
            mins = e.get("time_saved_minutes")
            if mins is not None and not (isinstance(mins, int) and mins > 0):
                problems.append(
                    f"{rid}: time_saved_minutes is {mins!r}; it is summed into a "
                    f"builder-visible tally, so it must be a positive whole number "
                    f"of minutes per run, not prose"
                )
            if e.get("ships_from") != "toolkit":
                problems.append(
                    f"{rid}: tier use-case must ship in the toolkit, not "
                    f"{e.get('ships_from')!r} — a use case a builder cannot run is "
                    f"a menu item that fails when clicked"
                )

        if tier == "use-case":
            concept_tiers = {r.get("id"): r.get("tier") for r in records}
            c = e.get("concept")
            if c is not None and concept_tiers.get(c) != "concept":
                problems.append(
                    f"{rid}: concept is {c!r}, which is not the id of a concept record; "
                    f"wrap-up points a builder at the session that teaches it"
                )
            for after in e.get("recommended_after", []):
                if concept_tiers.get(after) != "use-case":
                    problems.append(
                        f"{rid}: recommended_after names {after!r}, which is not a use case"
                    )

        actual = derive_ships_from(rid, rtype)
        declared = e.get("ships_from")
        if actual is None:
            if declared is not None:
                problems.append(f"{rid}: type {rtype} has no file, so it takes no ships_from")
        elif declared != actual:
            problems.append(
                f"{rid}: ships_from says {declared!r}, the tree says {actual!r}"
            )

    # recommended_after is one chain over the use cases: exactly one root, every other
    # use case follows exactly one, and walking from the root reaches all of them. The
    # three discovery surfaces walk this chain to list the use cases in order, so a fork
    # or a cycle would list them differently in different skills.
    use_cases = [e for e in records if e.get("tier") == "use-case"]
    roots = [e["id"] for e in use_cases if not e.get("recommended_after")]
    if len(use_cases) > 1:
        if len(roots) != 1:
            problems.append(
                f"recommended_after: expected exactly one use case with an empty list "
                f"(the first in order); found {len(roots)}: {roots}"
            )
        followers = {}
        for e in use_cases:
            for after in e.get("recommended_after", []):
                followers.setdefault(after, []).append(e["id"])
        forks = {k: v for k, v in followers.items() if len(v) > 1}
        if forks:
            problems.append(f"recommended_after: more than one use case follows {forks}")
        multi = [e["id"] for e in use_cases if len(e.get("recommended_after", [])) > 1]
        if multi:
            problems.append(f"recommended_after: {multi} name more than one predecessor")
        if len(roots) == 1 and not forks and not multi:
            seen, cur = [], roots[0]
            while cur and cur not in seen:
                seen.append(cur)
                nxt = followers.get(cur, [])
                cur = nxt[0] if nxt else None
            missing = sorted({e["id"] for e in use_cases} - set(seen))
            if missing:
                problems.append(
                    f"recommended_after: walking from {roots[0]!r} never reaches {missing}"
                )

    if problems:
        print(f"  {len(problems)} problem(s):")
        for line in problems:
            print(f"    {line}")
        print("\nFAIL: the library is what every discovery surface reads to decide what")
        print("      a builder may be offered. An unclassified record is offered by")
        print("      nothing, or named by everything, and neither failure is visible")
        print("      until a builder types a command that does not work.")
        return False

    counts = {}
    for e in records:
        counts[e["tier"]] = counts.get(e["tier"], 0) + 1
    print(f"  ok    {len(records)} records: " +
          ", ".join(f"{k} {v}" for k, v in sorted(counts.items())))
    return True


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    base = sys.argv[1]
    results = [check_version_bump(base), check_json_parses(),
               check_library_shape()]
    if all(results):
        print("\nAll release guards passed.")
        return 0
    print("\nRelease guards failed.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
