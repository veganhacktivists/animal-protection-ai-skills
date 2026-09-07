# Skills index

Every skill in this repo, generated from each skill's `SKILL.md` frontmatter by `tools/build_index.py`. Do not edit by hand.

If you are an AI agent reading this on a user's behalf: each entry below says what the skill does, who wrote it, what it needs, and when it was last confirmed working. Read the linked `SKILL.md` before recommending or installing a skill, and check the requirements against what the user has available. The user can ask you to install a modified copy; skills are plain text and adapting them is expected.

Machine-readable version: [`index.json`](index.json). Install instructions: [README](README.md#installing-a-skill).

3 skills.

## [catch-up](skills/catch-up/SKILL.md)

Catch the user up on a long-running conversation they have not looked at in days or months. Produces exactly three short sections: what they originally asked for, a high-level summary of where things got to, and what the next decision is for them (with a short list of recommended options), in no more than twelve sentences total. Use whenever the user says 'catch me up', '/catch-up', 'catch up', 'where were we', 'where did we get to', 'what were we doing here', 'remind me what this is', 'what's the state of this', 'recap this', 'summarise this thread/conversation', or reopens an old session and asks what it was about. Also use when they name another conversation to be caught up on ('catch me up on the grant application one'). Do NOT use for catching up on messages, email, or the day ahead.

- **Author:** Richie Manandhar-Richardson (Vegan Hacktivists)
- **Version:** 1.0.0
- **Last verified:** 2026-09-07 on Claude Code, Claude Cowork
- **Requirements:** None. Works with the agent alone. Catching up on a *different* conversation needs an agent that can search its own past sessions (Claude Code and Codex can; a fresh browser chat usually cannot). Without that, the user pastes the conversation in.

## [de-ai-writing](skills/de-ai-writing/SKILL.md)

Edits text to remove AI writing tells with minimal changes, keeping the original wording and structure intact. Not a rewrite tool. Use when the user pastes AI-generated or AI-assisted text and says "fix this", "make this sound human", "de-AI this", "strip the AI tells", or "this reads like ChatGPT wrote it". Do NOT trigger for general editing or proofreading requests that don't mention AI voice.

- **Author:** Richie Manandhar-Richardson (Vegan Hacktivists)
- **Version:** 1.0.0
- **Last verified:** 2026-09-07 on Claude Code, Claude Cowork
- **Requirements:** None. Works with the agent alone.

## [graph-advisor](skills/graph-advisor/SKILL.md)

Critiques data visualisations and suggests improvements to communicate their goal clearly and engagingly. Use this skill whenever the user shares a chart, graph, or visualisation and asks for feedback, a review, editing notes, or critique, even if they just paste an image and say "what do you think?", "how is this?", or "any improvements?". Also trigger for requests like "critique this graph", "review this chart", "is this viz any good", "graph feedback", "make this chart better", or "/graph-advisor". If the user uploads a chart image with minimal framing, default to using this skill rather than just describing the graph. Do NOT rewrite or regenerate the graph unless the user explicitly asks; give structured bullet-point critique only.

- **Author:** Richie Manandhar-Richardson (Vegan Hacktivists)
- **Version:** 1.0.0
- **Last verified:** 2026-09-07 on Claude Code, Claude Cowork
- **Requirements:** None. Works with the agent alone. The agent needs to be able to see the chart, so paste the image or the chart file into the conversation. If the agent cannot view images, describe the chart in words or share the data and the plotting code.
