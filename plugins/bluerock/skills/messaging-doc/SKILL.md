---
name: messaging-doc
description: >-
  Core Messaging Doc — point a small agent team at a brand's website and get the
  doc every later draft leans on: positioning, voice, and the phrases the brand
  actually uses. Use when I say "build my messaging doc", "distill my messaging",
  "messaging doc for <site>", "what does our site actually say", or paste a
  website URL and ask for the brand's messaging. Runs site-reader → distiller and
  writes the doc to my-work/messaging-doc/. One URL plus anything I paste — no
  exports, no logins, no integrations.
---

Run the Messaging Doc team on a brand's website and produce the core messaging doc — a
one-page source of truth for positioning, voice, and the exact phrases the brand uses.
You orchestrate two agents; they do the work. Keep it tight: a bounded site read and a
distillation, aiming for about five minutes, not a brand audit.

## First — anchor to the project

The doc, its working folder, and the `voice.md` / `objectives.md` the run reads all
live in the builder's project (the repo they cloned from the Starter). In an SSH/cloud
container the session usually starts in the **home folder**, with the project one level
down, named by the builder (`maria-hub`, `alex-hub` — don't assume a fixed name).
Identify it by signature, not name: run `ls`; see `CLAUDE.md` and `design/` side by
side? You're in the project. If not, find it: `ls */CLAUDE.md`, then `ls ~/*/CLAUDE.md`,
else `find ~ -maxdepth 3 -path '*/design/dashboard.html'`. `cd` in, capture the
**absolute path** with `pwd`, and use that full path throughout. Can't find it? Ask
where they cloned their project.

## Setup

1. **Get the site.** One website URL — usually the builder's own brand. (It runs on any
   brand's site; pointing it at a competitor for a comparison is a trick for later.) If
   they give only a company name, confirm the domain before spending the run.
2. **Offer the paste — once, lightly.** Recent material sharpens the doc: a post or two,
   campaign copy, an email they're proud of. Optional; if they have nothing at hand,
   move on without ceremony.
3. **Make the working folder.** Slugify the brand name → `my-work/messaging-doc/<slug>/`.
   Create it. `my-work/` is builder-owned and never overwritten.
4. **Save the paste before dispatching.** If they pasted anything, write it as
   `references.md` in the working folder, labeled by what each piece is ("LinkedIn post,
   July", "campaign email"). The agents read files, not this conversation — an unsaved
   paste is invisible to them.

## Run the agents, in order

Dispatch these as ordinary subagents, one at a time, waiting for each. Do not use
agent-teams tooling; this runs identically in every client.

5. **Dispatch `site-reader`** with the URL and the working folder. It reads the homepage
   plus the two or three pages that carry the messaging and writes `signals.md` — the
   positioning lines, voice notes, and exact recurring phrases, quoted and sourced. It's
   bounded to a handful of fetches — let it be fast. Wait for it.
6. **Dispatch `distiller`** with the same folder. It reads `signals.md` (plus
   `references.md` if present, and `voice.md` / `objectives.md` from the project root),
   writes `messaging-doc.md`, and renders the one-page doc artifact.

## Finish

7. The **messaging doc artifact** is the payoff — a clean, one-page view (brand header
   with the positioning one-liner, the voice attributes with quoted examples, the
   verbatim phrase bank, any honest gaps, and the pages read). The `messaging-doc.md`
   is the source of record the builder keeps and can push to their repo. If artifact
   publishing isn't available in my environment, don't block — the markdown is saved;
   say so and give the path.
8. **Report:** the doc's path, the positioning one-liner it found (or the "assembled
   from fragments" caveat if the site never says it cleanly), and the artifact (or the
   fallback note). Don't reprint the whole thing.

## Why this doc matters

This is not a one-off report — it's the project's memory seed for everything the builder
writes from here. Later sessions wire it into the project's memory, drafting skills lean on
its phrase bank, and the same two-agent run pointed at a competitor's site gives a
side-by-side messaging comparison with this doc as the baseline. The better this doc,
the more the whole project sounds like the brand.
