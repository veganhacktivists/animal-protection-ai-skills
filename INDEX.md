# Skills index

Every skill in this repo, generated from each skill's `SKILL.md` frontmatter by `tools/build_index.py`. Do not edit by hand.

If you are an AI agent reading this on a user's behalf: each entry below says what the skill does, who wrote it, what it needs, and when it was last confirmed working. Read the linked `SKILL.md` before recommending or installing a skill, and check the requirements against what the user has available. To install one, follow its setup guide. The user can ask you to install a modified copy; skills are plain text and adapting them is expected.

Machine-readable version: [`index.json`](index.json). Install instructions: each skill's setup guide, linked below.

6 skills.

## [ai-readiness-self-assessment](skills/ai-readiness-self-assessment/SKILL.md)

Scores an organization's AI adoption against seven fixed competencies (model access and plan tier, memory and custom instructions, projects and knowledge grounding, agent skills, automations, meeting capture, and coding agent use), each rated 0 to 3 with evidence, plus a one-line verdict naming the binding constraint. Use when someone asks "how mature is our AI use", "assess our AI readiness", "score us on AI adoption", "audit our AI setup", "where are we weak on AI", or wants a structured baseline before planning training or a rollout. Needs real evidence about the organization, not general AI knowledge, so gather that first rather than guessing.

- **Author:** Richie (Thomas Manandhar-Richardson) (Vegan Hacktivists)
- **Version:** 1.0.0
- **Last verified:** 2026-09-08 on Claude Code, Claude Cowork
- **Requirements:** None. Works with the agent alone. It needs real evidence about the organization, gathered one of two ways:
- **Setup guide:** [skills/ai-readiness-self-assessment/README.md](skills/ai-readiness-self-assessment/README.md)

## [ai-smell](skills/ai-smell/SKILL.md)

Removes AI smells (AI writing tells) from text with minimal changes, keeping the original wording and structure intact. Not a rewrite tool. Use when someone pastes AI-generated or AI-assisted text and says "fix this", "check this for AI smells", "make this sound human", "de-AI this", "strip the AI tells", or "this reads like ChatGPT wrote it". Do NOT trigger for general editing or proofreading requests that don't mention AI voice.

- **Author:** Richie (Thomas Manandhar-Richardson) (Vegan Hacktivists)
- **Version:** 2.1.0
- **Last verified:** 2026-10-08 on Claude Code, Claude Cowork
- **Requirements:** None. Works with the agent alone.
- **Setup guide:** [skills/ai-smell/README.md](skills/ai-smell/README.md)

## [assess-relevance](skills/assess-relevance/SKILL.md)

Reads a report, blog post, paper, policy brief, announcement, web page, or file and gives a clear verdict on whether it is relevant to the user's day-to-day work in animal advocacy — Highly relevant, Possibly relevant, or Not relevant — with a plain-language explanation of why. Use this whenever the user shares a URL or file and asks anything like "is this relevant to me?", "should I read this?", "is this worth my time?", "does this matter for my work?", "triage this report", "assess relevance", or "/assess-relevance" — even if they just paste a link and say "worth reading?". Also use it when the user shares several links or files and wants to know which ones to prioritise.

- **Author:** Richie (Thomas Manandhar-Richardson) (Vegan Hacktivists)
- **Version:** 1.0.0
- **Last verified:** 2026-09-08 on Claude Code, Claude Cowork
- **Requirements:** None. Works with the agent alone. Gives a sharper answer when the agent has some saved context about the user's work (a memory feature, a project's custom instructions, or a `CLAUDE.md`/`AGENTS.md` file) — without that, it falls back to a best-effort verdict for a typical animal protection worker and says so.
- **Setup guide:** [skills/assess-relevance/README.md](skills/assess-relevance/README.md)

## [catch-up](skills/catch-up/SKILL.md)

Catch the user up on a long-running conversation they have not looked at in days or months. Produces exactly three short sections: what they originally asked for, a high-level summary of where things got to, and what the next decision is for them (with a short list of recommended options), in no more than twelve sentences total. Use whenever the user says 'catch me up', '/catch-up', 'catch up', 'where were we', 'where did we get to', 'what were we doing here', 'remind me what this is', 'what's the state of this', 'recap this', 'summarise this thread/conversation', or reopens an old session and asks what it was about. Also use when they name another conversation to be caught up on ('catch me up on the grant application one'). Do NOT use for catching up on messages, email, or the day ahead.

- **Author:** Richie (Thomas Manandhar-Richardson) (Vegan Hacktivists)
- **Version:** 1.0.0
- **Last verified:** 2026-09-07 on Claude Code, Claude Cowork
- **Requirements:** None. Works with the agent alone. Catching up on a *different* conversation needs an agent that can search its own past sessions (Claude Code and Codex can; a fresh browser chat usually cannot). Without that, the user pastes the conversation in.
- **Setup guide:** [skills/catch-up/README.md](skills/catch-up/README.md)

## [graph-advisor](skills/graph-advisor/SKILL.md)

Critiques data visualisations and suggests improvements to communicate their goal clearly and engagingly. Use this skill whenever the user shares a chart, graph, or visualisation and asks for feedback, a review, editing notes, or critique, even if they just paste an image and say "what do you think?", "how is this?", or "any improvements?". Also trigger for requests like "critique this graph", "review this chart", "is this viz any good", "graph feedback", "make this chart better", or "/graph-advisor". If the user uploads a chart image with minimal framing, default to using this skill rather than just describing the graph. Do NOT rewrite or regenerate the graph unless the user explicitly asks; give structured bullet-point critique only.

- **Author:** Richie (Thomas Manandhar-Richardson) (Vegan Hacktivists)
- **Version:** 1.0.0
- **Last verified:** 2026-09-07 on Claude Code, Claude Cowork
- **Requirements:** None. Works with the agent alone. The agent needs to be able to see the chart, so paste the image or the chart file into the conversation. If the agent cannot view images, describe the chart in words or share the data and the plotting code.
- **Setup guide:** [skills/graph-advisor/README.md](skills/graph-advisor/README.md)

## [missed-message-triage](skills/missed-message-triage/SKILL.md)

Sweeps the user's messaging apps for requests that were asked of them and never became tasks, then proposes them as a numbered list of draft tasks for the user to approve. Read-only: it never creates a task and never sends a message. It has to be wired to the user's own chats and task manager when it is installed (see README.md in this folder). Use when someone asks to check for missed requests, "what did people ask me that I haven't done", "triage my messages into tasks", "did I miss anything in chat", or when its scheduled run starts. Not for replying to messages or managing existing tasks.

- **Author:** Richie (Thomas Manandhar-Richardson) (Vegan Hacktivists)
- **Version:** 2.0.0
- **Last verified:** 2026-09-08 on Claude Code, Claude Cowork
- **Requirements:** Needs read access to the messaging apps where people ask the user for things, read access to their task manager (including searching tasks with future due dates), and somewhere private to keep a state file. In Claude, connect a connector for each messaging app and the task manager. In Codex, install an MCP server for each. An aggregator such as Beeper can cover several messaging apps through one connection. Running it on a schedule needs an agent that can run scheduled tasks, such as Claude Code or Codex. It must be set up once before first use: see `README.md` in this folder.
- **Setup guide:** [skills/missed-message-triage/README.md](skills/missed-message-triage/README.md)
