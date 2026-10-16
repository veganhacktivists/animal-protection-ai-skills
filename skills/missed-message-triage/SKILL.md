---
name: missed-message-triage
description: "Sweeps the user's messaging apps for requests that were asked of them and never became tasks, then proposes them as a numbered list of draft tasks for the user to approve. Read-only: it never creates a task and never sends a message. It has to be wired to the user's own chats and task manager when it is installed (see README.md in this folder). Use when someone asks to check for missed requests, \"what did people ask me that I haven't done\", \"triage my messages into tasks\", \"did I miss anything in chat\", or when its scheduled run starts. Not for replying to messages or managing existing tasks."
license: MIT
metadata:
  version: "2.0.0"
  author: Richie (Thomas Manandhar-Richardson)
  author-org: Vegan Hacktivists
  last-verified: "2026-09-08"
  verified-on: "Claude Code, Claude Cowork"
---

# Missed message triage

Sweep your user's low-priority messaging apps for things that were asked of them and never got done, then propose those as draft tasks for approval. You never create a task and never send a message.

## Your user's setup

This section is filled in when the skill is installed, by following the setup guide (`README.md` in this folder). If anything below still says `<not set up yet>`, stop. Tell the user the skill needs setting up first, and offer to follow the "For AI agents installing this skill" steps in the setup guide.

- **Sources to sweep:** `<not set up yet>` (platforms and chats, plus anything to ignore)
- **The user's identity on each platform:** `<not set up yet>` (user ID, handle, display name)
- **People whose requests always surface:** `<not set up yet>`
- **Task system:** `<not set up yet>` (which is authoritative, and what kind of work belongs where if there is more than one)
- **Context files to read:** `<not set up yet>` (for example a colleagues list or a channel map, or "none")
- **Timezone:** `<not set up yet>`
- **State file:** `<not set up yet>` (its location)
- **Where the output goes:** `<not set up yet>` (chat, a notification or a file)
- **Schedule:** `<not set up yet>` (or "on demand")

## Establish the cutoff

Read the state file for the previous run's timestamp. That's the cutoff. If it's missing, fall back to the last scheduled slot, or ask what window to cover on an on-demand run, and say in the output that you fell back.

## Sweep

For each source, since the cutoff: direct mentions, DMs and group DMs, and threads the user participated in or was mentioned in. Use the user's identity on each platform to tell what was directed *at* them from what was merely near them. If context files are listed above, read them, so a request is attributed to the right person and routed to the right task system.

Prioritise, in order:

1. Explicit requests directed at the user
2. Unanswered questions
3. Review or approval requests
4. Blockers waiting on them
5. Commitments the user themselves made
6. Follow-ups with no visible response

Ignore social chatter, FYIs, and team discussion carrying no action for this specific person. **A message with too little visible context to become an actionable task is not a task.** Report it as ambiguous instead of inventing an action. Over-proposing is the main failure mode: it trains the user to skim.

## Duplicate check

Search their task system by keyword for every candidate, including future due dates. Drop anything that already exists as an incomplete task. Then check the state file's prior proposals. Don't re-propose unless still unresolved *and* still absent from the task system. Mark repeats as `(repeat)`.

## Output

A numbered list. Per item: actionable title, suggested due date, suggested priority, one or two lines of context, and the source conversation. If nothing credible surfaced, say so plainly rather than padding. Add a **Watchouts** section naming any source that couldn't be checked.

## Constraints

- Read-only. Never create, update, or complete a task.
- Never send or draft a message in any messaging app.
- Proposals only. A human approves by number.
- If a connector is unavailable, say so explicitly under Watchouts and name what went unchecked. Never silently substitute another source or imply full coverage.

## Update state

Overwrite the state file at the end of every run:

```
Last reviewed run: <ISO 8601 timestamp with offset>
Cutoff used: <the cutoff this run used>

Sources checked this run:
- <source>: <what was checked; candidates found, and why each did or didn't become a task>

Draft tasks proposed this run:
1. <title>

Do not re-propose unless still unresolved and no task exists in the task system.
```

The rejection reasoning matters as much as the proposals. It is what stops the next run re-litigating the same judgement call and re-surfacing the same dismissed item.

## Tuning notes (learned the hard way)

- **The state file is what makes it survivable.** Without it, the same three items resurface every run and it gets muted inside a fortnight.
- **Bias toward under-proposing.** A missed task costs one follow-up message. A list full of noise costs the user's trust in the whole thing, permanently.

## Privacy

This reads personal and team messages, including DMs. The state file quotes private conversations by design. Keep both wherever the user keeps private material, never in a shared repo, and never paste raw output into a shared channel.

## Requirements

Needs read access to the messaging apps where people ask the user for things, read access to their task manager (including searching tasks with future due dates), and somewhere private to keep a state file. In Claude, connect a connector for each messaging app and the task manager. In Codex, install an MCP server for each. An aggregator such as Beeper can cover several messaging apps through one connection. Running it on a schedule needs an agent that can run scheduled tasks, such as Claude Code or Codex. It must be set up once before first use: see `README.md` in this folder.
