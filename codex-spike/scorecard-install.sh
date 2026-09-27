#!/usr/bin/env bash
# Spike installer: puts the Codex form of the Account Scorecard team where Codex looks for
# user-level skills and agents. Touches nothing in the builder's project. Re-runnable.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)/scorecard"
mkdir -p "$HOME/.agents/skills" "$HOME/.codex/agents"
rm -rf "$HOME/.agents/skills/bluerock-scorecard"
cp -R "$HERE/skills/bluerock-scorecard" "$HOME/.agents/skills/"
cp "$HERE/agents/scout.toml" "$HERE/agents/scorer.toml" "$HOME/.codex/agents/"
echo "Installed:"
ls -la "$HOME/.agents/skills/bluerock-scorecard" "$HOME/.codex/agents"
