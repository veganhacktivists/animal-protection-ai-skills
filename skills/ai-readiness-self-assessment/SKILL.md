---
name: ai-readiness-self-assessment
description: Scores an organization's AI adoption against seven fixed competencies (model access and plan tier, memory and custom instructions, projects and knowledge grounding, agent skills, automations, meeting capture, and coding agent use), each rated 0 to 3 with evidence, plus a one-line verdict naming the binding constraint. Use when someone asks "how mature is our AI use", "assess our AI readiness", "score us on AI adoption", "audit our AI setup", "where are we weak on AI", or wants a structured baseline before planning training or a rollout. Needs real evidence about the organization, not general AI knowledge, so gather that first rather than guessing.
license: MIT
metadata:
  version: "1.0.0"
  author: Richie (Thomas Manandhar-Richardson)
  author-org: Vegan Hacktivists
  last-verified: "2026-09-08"
  verified-on: "Claude Code, Claude Cowork"
---

# AI Readiness Self-Assessment

A short, structured way for an organization to score its own AI adoption against a fixed set of competencies, so a leadership team or an AI lead can see where they actually stand before planning training, a rollout, or a policy. It produces one scorecard and one verdict sentence, not a full plan.

## Requirements

None. Works with the agent alone. It needs real evidence about the organization, gathered one of two ways:

- **Interview the user.** Ask what tools people use, how consistently, and for what. This works with the agent alone and no setup.
- **Read what the agent can already see.** If the agent has access to the organization's own chat history, shared drive, or saved memory of how the team works, use that as evidence instead of or alongside the interview, and say which sources you used.

Either way, evidence beats assumption. Do not score a row from general knowledge of what AI can do.

## Step 1: Gather evidence

Before scoring anything, find out, for this organization specifically:

- Which AI tools and plans people are actually on (free, individual paid, team, enterprise).
- Whether anyone has set up memory, custom instructions, or an organization-wide "who we are and how we work" document.
- Whether AI work happens in ad hoc chats or is anchored to real files, folders, and ongoing projects.
- Whether anyone has built or uses a reusable skill, template, or saved prompt for a recurring task.
- Whether anything runs on a schedule without a person starting it each time.
- How meetings get recorded, transcribed, and turned into next steps.
- Whether anyone uses a terminal-based or file-editing coding agent, even for non-coding work like bulk data cleanup.

If the person you are talking to does not know the answer for a row, say so in the assessment rather than guessing on their behalf.

## Step 2: Score the seven competencies

The seven competencies are fixed. Do not add or remove rows, so a repeat assessment stays comparable to the last one.

1. **Model access and plan tier** — which AI products and plan levels people are on. A hard gate: organization-wide skills, shared projects, and coding agents are often impossible below certain tiers, and it is usually the cheapest thing to fix.
2. **Memory and custom instructions** — whether people have configured the model to know who they are and how they work. Per-person hygiene, not something a purchase fixes on its own.
3. **Projects and knowledge grounding** — whether work is anchored to the organization's real documents, rather than done in blank chats that start from nothing every time.
4. **Agent skills** — reusable, packaged instructions for a recurring task, ideally shared across the team. The lever that turns "AI helps me write" into "AI runs our process consistently."
5. **Automations and scheduled routines** — things that run on a trigger or a schedule with nobody starting them. Distinct from a skill: a skill runs when someone invokes it; an automation runs whether or not anyone shows up.
6. **Meeting capture and synthesis** — recording, transcribing, and routing meeting outputs to wherever the actual work happens next.
7. **Coding agent or command-line use** — a terminal-based or file-editing agent that can touch files, run scripts, and take on bulk or data work, even outside a technical team.

Score each row 0 to 3, using these anchors for every row:

- **0** — nobody / not set up.
- **1** — one person, ad hoc.
- **2** — several people, inconsistent, no shared standard.
- **3** — embedded: the default way work happens, and it survives that person leaving.

Scoring rules:

- Score the organization, not individuals. Give one score per row, plus a short note on the spread: who does it, and how unevenly.
- Name specific people only for credit ("Priya set this up for the comms team"), never to single someone out for a gap. This document may circulate; a scorecard that reads as a performance review damages trust in the process.
- A range, such as 1 to 2, is fine when the evidence genuinely straddles two anchors.
- Score only on evidence gathered in Step 1. Where there is none, say so in the notes rather than inventing a middle score.
- Note what is already working for each row, not only what is missing.

## Step 3: Give the verdict

Close with one line: **"What this says in one sentence"**, naming the binding constraint rather than restating the rows. For example: "Capability is real but stays personal and manual: nothing is shared, and nothing runs unattended."

## Output format

```
## AI Readiness Scorecard for [organization]

| Competency | Score | What's already working | Evidence / notes |
|---|---|---|---|
| Model access and plan tier | 0-3 | | |
| Memory and custom instructions | 0-3 | | |
| Projects and knowledge grounding | 0-3 | | |
| Agent skills | 0-3 | | |
| Automations and scheduled routines | 0-3 | | |
| Meeting capture and synthesis | 0-3 | | |
| Coding agent or command-line use | 0-3 | | |

**What this says in one sentence:** [the binding constraint]
```

## What this deliberately does not do

This is a baseline, not a plan. It does not recommend a rollout sequence, a training curriculum, or a change-management approach, and it does not diagnose culture, burnout, or staff resistance. Those are real and important questions, but they need more than a scorecard to answer well. Once the scores exist, that is a separate follow-up conversation.
