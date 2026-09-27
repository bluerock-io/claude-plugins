#!/usr/bin/env python3
"""Spike: build a Codex form of the Account Scorecard agent team from the plugin source.

Reads plugins/bluerock/{skills/scorecard/SKILL.md, agents/scout.md, agents/scorer.md} and
writes codex-spike/scorecard/. Every edit asserts its anchor, so a source change fails loud
instead of shipping a half-converted file. Prototype for the generator; not a release.
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "plugins" / "bluerock"
OUT = ROOT / "codex-spike" / "scorecard"


def swap(text, old, new, label):
    if text.count(old) != 1:
        sys.exit(f"anchor not found exactly once: {label}")
    return text.replace(old, new)


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit("no frontmatter")
    return m.group(1), text[m.end():]


def common(text):
    # Codex skill names are flat: /bluerock:<name> becomes $bluerock-<name> (decision 2026-09-26).
    return text.replace("/bluerock:", "$bluerock-")


def build_skill():
    text = (SRC / "skills/scorecard/SKILL.md").read_text()
    text = swap(text, "name: scorecard\n", "name: bluerock-scorecard\n", "skill name")
    text = swap(
        text,
        "**Which prompt shape:** use the question picker (`AskUserQuestion`) only at step 4, where\n"
        "the answer is genuinely a choice among a few. Everywhere else the answer is free text in\n"
        "the builder's own words — ask in the message and let them type.",
        "**Which prompt shape:** every question is asked in plain chat. At step 4, where the answer\n"
        "is genuinely a choice among a few, list the options as a short numbered list the builder\n"
        "can answer by number or in their own words. Everywhere else, ask and let them type.",
        "prompt shape",
    )
    text = swap(
        text,
        "Dispatch these as ordinary subagents, one at a time, waiting for each. Do not use\n"
        "agent-teams tooling; this runs identically in every client.",
        "Delegate to these two subagents, `scout` and `scorer` (defined in `~/.codex/agents/`),\n"
        "one at a time, waiting for each. Give each one the working folder's **absolute path** in\n"
        "its task: a subagent reads files, not this conversation.",
        "dispatch",
    )
    text = swap(text, "## Publish the artifact — you, not the agents",
                "## Render the page — you, not the agents", "publish heading")
    text = swap(
        text,
        "5. When `scorer` finishes, read `scorecard.md` and **publish it as a Claude Artifact**\n"
        "   yourself, in this conversation, following the design contract below. The agents\n"
        "   write markdown only — they have no artifact publishing; the finished, shareable\n"
        "   view is yours to render. If artifact publishing isn't available in my environment,\n"
        "   don't block — the markdown is saved; say so and give the path.",
        "5. When `scorer` finishes, read `scorecard.md` and **write the page as `scorecard.html`**\n"
        "   in the working folder yourself, following the design contract below. The agents\n"
        "   write markdown only; the finished, shareable page is yours to render. Then give the\n"
        "   builder the file's full path so they can open it.",
        "publish step",
    )
    text = swap(text, "since the\nArtifact can't read", "since the\npage can't read", "palette note")
    text = swap(text, "and the artifact (or the fallback note)",
                "and the full path to `scorecard.html`", "report step")
    # Maintainer notes point at plugin paths that do not exist in the Codex form.
    i = text.index("## Who depends on this skill's wording")
    text = text[:i].rstrip() + "\n"
    out = OUT / "skills" / "bluerock-scorecard" / "SKILL.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(common(text))


def build_agent(name, edits=()):
    text = (SRC / f"agents/{name}.md").read_text()
    fm, body = split_frontmatter(text)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M).group(1).strip()
    for old, new, label in edits:
        body = swap(body, old, new, label)
    body, desc = common(body).strip(), common(desc)
    if "'''" in body:
        sys.exit(f"{name}: body contains ''' and cannot be a TOML literal string")
    toml = (
        f'name = "{name}"\n'
        f'description = "{desc.replace(chr(92), chr(92) * 2).replace(chr(34), chr(92) + chr(34))}"\n'
        f"developer_instructions = '''\n{body}\n'''\n"
    )
    out = OUT / "agents" / f"{name}.toml"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(toml)


build_skill()
build_agent("scout", [(
    "- `WebSearch` for the company site and recent coverage; `WebFetch` the pages that actually\n"
    "  answer the questions above.",
    "- Search the web for the company site and recent coverage, then open the pages that\n"
    "  actually answer the questions above. If your web tool cannot open a page, `curl -sL <url>`\n"
    "  in the shell will.",
    "scout web tools",
)])
build_agent("scorer")
print("built", *sorted(p.relative_to(ROOT) for p in OUT.rglob("*") if p.is_file()), sep="\n  ")
