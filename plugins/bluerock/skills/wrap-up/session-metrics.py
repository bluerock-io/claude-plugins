#!/usr/bin/env python3
"""
session-metrics.py — read the current Claude Code session transcript and emit
quantitative metrics (tokens, wall-clock time, turns, models) as JSON to stdout.

Why this exists: a skill (a prompt) cannot reliably know its own token usage or
session duration. The honest source is the Claude Code transcript JSONL, where
every assistant turn carries `message.usage` and a `timestamp`. This script parses
that file deterministically so /wrap-up can log real numbers (beta has no telemetry
backend — see bfb-beta-user-flow.md M7). In the BlueRock workspace, the richer,
sensor-sourced metrics supersede this; this is the safe-by-default "lite" source.

stdlib only. No dependencies. Never raises to the caller — on any problem it prints
a JSON object with "ok": false and an "error" string, so the skill can degrade.

Usage:
  python3 session-metrics.py [--transcript /path/to/session.jsonl]
If --transcript is omitted, it picks the most-recently-modified *.jsonl under
~/.claude/projects (that is the session currently being written).
"""

import sys, os, json, glob
from datetime import datetime


def find_latest_transcript():
    base = os.path.expanduser("~/.claude/projects")
    files = glob.glob(os.path.join(base, "*", "*.jsonl"))
    if not files:
        return None
    return max(files, key=os.path.getmtime)


def parse_ts(value):
    if not value:
        return None
    try:
        return datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    except ValueError:
        return None


def main():
    transcript = None
    args = sys.argv[1:]
    if "--transcript" in args:
        i = args.index("--transcript")
        if i + 1 < len(args):
            transcript = args[i + 1]
    if not transcript:
        transcript = find_latest_transcript()

    if not transcript or not os.path.exists(transcript):
        print(json.dumps({"ok": False, "error": "no transcript found"}))
        return

    tok = {"input": 0, "output": 0, "cache_read": 0, "cache_creation": 0}
    turns = 0
    models = set()
    timestamps = []

    try:
        with open(transcript, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    continue
                ts = parse_ts(entry.get("timestamp"))
                if ts:
                    timestamps.append(ts)
                msg = entry.get("message") or {}
                usage = msg.get("usage") or {}
                if usage:
                    turns += 1
                    tok["input"] += usage.get("input_tokens", 0) or 0
                    tok["output"] += usage.get("output_tokens", 0) or 0
                    tok["cache_read"] += usage.get("cache_read_input_tokens", 0) or 0
                    tok["cache_creation"] += usage.get("cache_creation_input_tokens", 0) or 0
                if msg.get("model"):
                    models.add(msg["model"])
    except OSError as e:
        print(json.dumps({"ok": False, "error": f"read failed: {e}"}))
        return

    tok["total"] = tok["input"] + tok["output"] + tok["cache_read"] + tok["cache_creation"]

    started = min(timestamps) if timestamps else None
    ended = max(timestamps) if timestamps else None
    duration_minutes = 0
    if started and ended:
        duration_minutes = round((ended - started).total_seconds() / 60, 1)

    out = {
        "ok": True,
        "session_id": os.path.splitext(os.path.basename(transcript))[0],
        "started_at": started.isoformat() if started else None,
        "ended_at": ended.isoformat() if ended else None,
        "duration_minutes": duration_minutes,
        "turns": turns,
        "tokens": tok,
        "models": sorted(models),
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
