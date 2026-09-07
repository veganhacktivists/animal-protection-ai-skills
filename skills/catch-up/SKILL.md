---
name: catch-up
description: "Catch the user up on a long-running conversation they have not looked at in days or months. Produces exactly three short sections: what they originally asked for, a high-level summary of where things got to, and what the next decision is for them (with a short list of recommended options), in no more than twelve sentences total. Use whenever the user says 'catch me up', '/catch-up', 'catch up', 'where were we', 'where did we get to', 'what were we doing here', 'remind me what this is', 'what's the state of this', 'recap this', 'summarise this thread/conversation', or reopens an old session and asks what it was about. Also use when they name another conversation to be caught up on ('catch me up on the grant application one'). Do NOT use for catching up on messages, email, or the day ahead."
license: MIT
metadata:
  version: "1.0.0"
  author: Richie Manandhar-Richardson
  author-org: Vegan Hacktivists
  last-verified: "2026-09-07"
  verified-on: "Claude Code, Claude Cowork"
---

# Catch Up

The user has come back to a conversation they may not have touched in months. They need to re-enter it in about fifteen seconds. Your job is to give them the smallest possible amount of information that lets them pick up where they left off.

## Which conversation

**Default: the current one.** If the user asks to be caught up with no target, they mean the conversation they are sitting in. It is already in your context. Do not go looking for it anywhere else.

**If they name a different one** ("catch me up on the volunteer onboarding thing"), find it first:

- If your agent can search or list past conversations or sessions, use that. Search by the topic, file name, or error they mentioned; browse by title and recency when the name is vague.
- If your agent cannot see past conversations, say so in one sentence and ask the user to paste the conversation or its export.
- If more than one conversation plausibly matches, ask which one rather than guessing. One short question, then stop.

**Do not read the whole transcript.** For a long conversation you only need two things: the opening user message (for section 1) and the last stretch of exchange (for sections 2 and 3). The middle is almost entirely mechanics you are going to throw away anyway.

## The output

Exactly three sections, in this order, with these headings:

**What you asked for**: one sentence, the original ask in the user's terms, not the shape it later mutated into. If it genuinely changed direction mid-way, say so in the same sentence ("...though it turned into X").

**Where we got to**: two to five bullets, one line each. Outcomes and conclusions only.

**Your next decision**: one sentence, phrased as an actual choice the user has to make, then a numbered list of the recommended options: as few as possible, never more than five. If there is genuinely nothing to decide and it is just waiting on them to say go, say that instead. If the work is finished, say that.

**Hard limit: 12 sentences across the whole response.** Bullets and numbered options count as sentences. If it does not fit, you are including too much.

## What to leave out

Everything mechanical. The user does not want to know about:

- Git operations, branches, merges, pull requests, commits.
- Which files were touched, or how many edits were made. If they asked for a set of specific edits, that is one bullet: "made the edits you listed", not a list of them.
- Debugging detours, things that broke and got fixed, tools you ran, searches you did.
- Your reasoning, your process, or anything you offered and they declined.
- Preamble ("Here's your catch-up!"), sign-off, or an offer to continue.

Collapse all of it. The test for every line: if the user would already have forgotten it existed, it does not go in.

## Shape

```
**What you asked for**
<one sentence>

**Where we got to**
- <outcome>
- <outcome>
- <outcome>

**Your next decision**
<one sentence naming the choice, or a clear "waiting on you to X">
1. <option>
2. <option>
```

## Good vs bad

Bad, because it is mechanical, too long, and has no decision:

> You asked me to help with the donor thank-you emails. We started by pulling the donor list from the spreadsheet, then found the export was missing the gift dates, so we switched to the CRM export. I drafted three versions of the email, ran them past the style guide, fixed two typos, then saved them to the shared drive. Let me know if you want me to keep going!

Good:

> **What you asked for**
> Personalised thank-you emails for everyone who gave over £100 in the spring appeal.
>
> **Where we got to**
> - Switched to the CRM export after the spreadsheet turned out to be missing gift dates.
> - Three email drafts are written and saved to the shared drive, one per donor tier.
> - Nothing has been sent yet.
>
> **Your next decision**
> Whether to send the drafts as they are or have the fundraising lead review them first.
> 1. Send now.
> 2. Send to the fundraising lead for a quick review, then send.

## After the catch-up

Stop. Do not start work, re-run anything, or re-open files to check state. The user asked to be caught up, not to be continued. They will tell you what is next.

## Requirements

None. Works with the agent alone. Catching up on a *different* conversation needs an agent that can search its own past sessions (Claude Code and Codex can; a fresh browser chat usually cannot). Without that, the user pastes the conversation in.
