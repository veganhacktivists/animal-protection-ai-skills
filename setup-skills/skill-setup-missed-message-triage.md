---
title: "Skill setup — Missed message task triage"
description: "Interviews the user and builds them a personalised, read-only agent that periodically sweeps their messaging apps for requests that never became tasks, then proposes those as draft tasks for approval. There is no installable skill to copy: it only works wired to the specific channels, chats, and task manager the user actually has. Use when someone wants to stop losing requests that arrive as chat messages rather than tasks."
license: MIT
metadata:
  version: "1.0.0"
  author: Richie (Thomas Manandhar-Richardson)
  author-org: Vegan Hacktivists
  last-verified: "2026-09-08"
  verified-on: "Claude Code, Claude Cowork"
---

# Skill setup — Missed message task triage

**This document is written to be read by an AI agent.** If you are an agent
reading this, your job is not to follow these steps yourself — it is to **build a
personalised version of this skill for your user**, interviewing them as you go.

There is deliberately no installable skill to copy. This one only works when it
is wired to the specific channels, chats, and task manager your user actually
uses. 

## What you are building

A read-only agent that periodically sweeps your user's low-priority messaging apps for things
that were asked of them and never got done — then proposes those as draft tasks
for approval. It never creates a task and never sends a message.

Three artifacts, depending on their answers:

1. **The skill** — instructions, written to wherever your agent keeps skills.
2. **A state file** — how it remembers across runs. Not optional; see
   [Tuning](#tuning-notes-learned-the-hard-way).
3. **A scheduled task** — only if they want it recurring.

---

## Step 1 — Look before you ask

Work these out yourself first. 

- **What agent am I, and where do skills and scheduled tasks live here?**
  Claude Code uses `~/.claude/skills/` and `~/.claude/scheduled-tasks/<id>/SKILL.md`;
  Codex uses `~/.codex/skills/` and `~/.codex/automations/<id>/automation.toml`.
- **Which messaging connectors do I actually have?** Enumerate your available
  tools. Do not ask "do you use Slack?" when you can see whether a Slack tool
  exists. Ask instead about the ones you *can* reach.
- **Is there an aggregator?** Something like Beeper can front WhatsApp, Discord,
  iMessage, Signal, LinkedIn and more through one connector. If you have one,
  list its connected accounts — that answers most of the platform question
  outright.
- **Which task manager can I reach?** Todoist, Asana, Monday, Linear, Things,
  Notion, plain markdown. There may be more than one, split by life area.
- **What scheduled tasks already exist?** You need this to avoid stacking
  another heavy job onto a slot that's already busy — see
  [Tuning](#tuning-notes-learned-the-hard-way).
- **Does the user keep context files you should read?** A colleagues list, a
  channel routing map, a workspace `AGENTS.md`. These make the difference
  between "someone called Kate asked for something" and a correctly attributed,
  correctly routed task. If they exist, the skill should reference them.
- **Resolve the user's own identity in each platform.** Their user ID, handle,
  display name. Without this the skill cannot tell what was directed *at* them
  versus merely near them. This is the single most common reason a first run
  returns garbage.

Report what you found before moving on. 

## Step 2 — Ask

Cover these. Adapt the wording; keep the intent.

**Scope**

- Which of these platforms actually carry work requests to you? (List only what
  you can reach.) 
- Should it sweep everything, or only work-relevant chats? If a subset — which,
  and is there a rule for deciding, or should it check a channel map?
- Anyone whose requests should always surface, even when phrased casually?
- Anything to explicitly ignore — a firehose channel, a personal chat, a bot?

**Task system**

- Where do your tasks live? If more than one, which is authoritative, and do
  certain kinds of work belong to a specific one?
- The duplicate check searches this before proposing. Confirm you can search it,
  including tasks due in the future.

**Cadence**

- Do you want this scheduled, or run on demand when you ask for it?
- If scheduled: how often, and what time? Recommend against daily —
  see [Tuning](#tuning-notes-learned-the-hard-way).
- What timezone should it reason in?

**Output and state**

- Where should the state file live? Default it next to the skill or scheduled
  task; it must be somewhere they treat as private.
- How do they want the output — straight into chat, a notification, a file?

Do not ask about the read-only constraint or the memory format. Those are not
preferences; build them in.

## Step 3 — Build

Write the skill with the logic below. Adapt names and tools to their setup, but
keep the shape.

### Establish the cutoff

Read the state file for the previous run's timestamp. That's the cutoff. If it's
missing, fall back to the last scheduled slot, or ask what window to cover on an
on-demand run — and say in the output that you fell back.

### Sweep

For each source, since the cutoff: direct mentions, DMs and group DMs, and
threads the user participated in or was mentioned in.

Prioritise, in order:

1. Explicit requests directed at the user
2. Unanswered questions
3. Review or approval requests
4. Blockers waiting on them
5. Commitments the user themselves made
6. Follow-ups with no visible response

Ignore social chatter, FYIs, and team discussion carrying no action for this
specific person. **A message with too little visible context to become an
actionable task is not a task** — report it as ambiguous instead of inventing an
action. Over-proposing is the main failure mode; it trains the user to skim.

### Duplicate check

Search their task system by keyword for every candidate, including future due
dates. Drop anything that already exists as an incomplete task. Then check the
state file's prior proposals — don't re-propose unless still unresolved *and*
still absent from the task system. Mark repeats as `(repeat)`.

### Output

A numbered list. Per item: actionable title, suggested due date, suggested
priority, one or two lines of context, and the source conversation. If nothing
credible surfaced, say so plainly rather than padding. Add a **Watchouts**
section naming any source that couldn't be checked.

### Constraints

- Read-only. Never create, update, or complete a task.
- Never send or draft a message in any messaging app.
- Proposals only; a human approves by number.
- If a connector is unavailable, say so explicitly under Watchouts and name what
  went unchecked. Never silently substitute another source or imply full
  coverage.

### Update state

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

The rejection reasoning matters as much as the proposals. It is what stops the
next run re-litigating the same judgement call and re-surfacing the same
dismissed item.

## Tuning notes (learned the hard way)

- **Every other day beats daily.** Daily produces too many empty runs and the
  output stops being read.
- **Offset it from their other morning automations.** Two agents hitting the
  same message and task connectors at once causes contention and permission
  prompts piling up.
- **The state file is what makes it survivable.** Without it, the same three
  items resurface every run and it gets muted inside a fortnight.
- **Bias toward under-proposing.** A missed task costs one follow-up message. A
  list full of noise costs the user's trust in the whole thing, permanently.

## Privacy

This reads personal and team messages, including DMs. The state file quotes
private conversations by design. Keep both wherever the user keeps private
material, never in a shared repo, and never paste raw output into a shared
channel.
