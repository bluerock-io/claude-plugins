# Save your work — checkpoint verification spec

Half of this step happens in the builder's browser, where no command run here
can see. Two kinds of evidence, never blurred:

- **Inspectable** — a state you can check from this chat with a command. The
  only evidence that can mark a checkpoint passed on its own.
- **Reported** — a state on the builder's own screen (github.com, the consent
  window). Ask what they *see*, never "did it work?", and treat the report as
  provisional until its nearest inspectable consequence appears.

The step's shape alternates between them on purpose: browser (reported) →
workspace (inspectable) → browser (reported), and the final proof is the
builder's own eyes on the repo page — deliberately reported, because the point
of the step is that *they* watched it happen.

Run inspection commands quietly; the builder sees conclusions, not plumbing.
`<project>` is the project's absolute path.

## Checkpoint 1 — signed in on github.com

- **Reported.** Ask what the top-right corner of `github.com` shows: their
  avatar means signed in. A brand-new account passes the same way as a
  ten-year-old one.
- Do not move on while they are mid-verification on GitHub's side; the next
  checkpoint needs a signed-in account to exist.

## Checkpoint 2 — the workspace is signed in

- **Inspectable:** `gh auth status` reports logged in to github.com with
  their account. Report it in builder words ("your workspace is signed in to
  GitHub as maria-w"), never the command output.
- **The consent for the one setting is part of this checkpoint.** If they
  declined `gh auth setup-git`, the checkpoint still passes — the sign-in
  exists — but note that step 4's backup will stop at credentials, and offer
  the setting again there rather than springing it.
- The code itself is never evidence: a code typed is not a sign-in completed.
  Check the status, not the ritual.

## Checkpoint 3 — the repo exists, and it is empty

- **Inspectable.** `gh repo create` prints the new repo's address on success,
  and `gh repo view <name> --json isPrivate,isEmpty` answers both halves
  directly. Report it in builder words ("your backup home is ready, and only
  you can see it"), never the command output.
- **Made this way, empty is the default** — there is no starter-file checkbox
  to mistake, which is the whole reason the step moved into the chat. The
  divergence failure that this checkpoint used to guard against cannot happen
  on this path.
- **If they created it on github.com instead**, the spec is the old one and
  the heading is the evidence: GitHub shows the **"Quick setup"** page only
  for a repo with no starting files. A file listing (a README visible) means
  the repo is not empty — run the step's recovery, delete and recreate, before
  anything else.
- **Confirm private either way.** Public is not a failure, but it is not what
  the step promised — offer the fix (Settings → change visibility) or
  delete-and-recreate while the repo is still empty.

## Checkpoint 4 — the backup went up

- **Inspectable, both halves:** the current branch exists on the remote and
  tracks it, and nothing saved is left behind (`git -C <project> status`
  reports the branch up to date with the remote). The remote's URL is the
  builder's own repo — **never** `bluerock-io/my-workspace`; a "successful"
  push to the template is a failure of the standing rule, not a pass.
- **The guards are part of the pass, in order:** if `.git/shallow` existed,
  it no longer does (the history was completed before the push); the secrets
  scan ran and came back clean, or what it found was excluded with consent
  before anything went up.
- Do not declare the step done here. The builder has not seen anything yet,
  and the step's outcome is *watched*, not inferred.
- **Failure diagnosis, in order:**
  1. Error mentioning the remote or unpacking → shortened history still
     present. Complete it, push again.
  2. Rejected because the remote has history → the repo was not empty. Step
     2's recovery, then push again.
  3. Asked for credentials → the sign-in setting was declined or did not
     take. Offer `gh auth setup-git` again, with the same consent.
  Once each, then the ladder: `/bluerock:help`, then Slack with their post
  written for them.

## Checkpoint 5 — their own files on the repo page

**The step's real pass, and it is deliberately reported.**

- The builder refreshes the repo page and **names one file they recognize.**
  Their naming it is the checkpoint — it proves the backup is real to the one
  person the step exists for.
- If the page still says "Quick setup" after a refresh: the push did not
  land — back to checkpoint 4's diagnosis. Do not talk past this; an empty
  page after a claimed backup is the exact confusion this step exists to
  prevent.

## Marking progress

**None.** This step has no session number and writes no
`learning/progress.json` entry — the remote and the sign-in are the record,
inspectable by any later skill or chat at any time. The journal entry
(`learning/journal.md`, the builder's own words) is the only file this step's
close-out writes.
