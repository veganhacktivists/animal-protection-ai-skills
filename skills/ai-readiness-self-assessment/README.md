# Setting up ai-readiness-self-assessment

This skill scores your organisation's use of AI in seven areas, from which AI plans people are on to whether anyone uses a coding agent. Each area gets a score from 0 to 3 with the evidence behind it, and the skill ends with one sentence naming what holds you back most. It is a starting point for planning, not a plan.

## What you need first

Nothing. It works with the AI agent alone.

It does need real evidence about your organisation, so expect it to ask what tools people use, how often and for what. If your agent can already see your organisation's chat history, shared drive or saved notes on how the team works, it can use those instead of asking, or as well, and it will say which it used.

## Installing it

The easiest way is to give your AI agent the link to this folder and ask it to install the skill. Your agent can usually do this for you.

To install it by hand:

- **Claude Code:** run `/plugin marketplace add veganhacktivists/animal-protection-ai-skills`, then `/plugin install ai-readiness-self-assessment@animal-protection-ai-skills`. Or copy this folder into `~/.claude/skills/`.
- **Claude Cowork and claude.ai:** download the `ai-readiness-self-assessment` zip from the [latest release](https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest) and upload it in Settings, under Capabilities, then Skills.
- **OpenAI Codex:** copy this folder into `~/.agents/skills/`.
- **Gemini CLI:** run `gemini skills install https://github.com/veganhacktivists/animal-protection-ai-skills.git --path skills/ai-readiness-self-assessment`.
- **GitHub Copilot:** run `gh skill install veganhacktivists/animal-protection-ai-skills ai-readiness-self-assessment`.
- **Microsoft 365 Copilot:** upload the zip from the latest release under Customize, then Upload skill.

If your AI tool cannot install skills, such as the plain ChatGPT web app, paste the contents of `SKILL.md` into a project's instructions or at the start of a chat. This works less well: the AI only has the instructions in that one chat or project, and any scripts in this folder will not run.

## Checking it works

Ask your agent: "Assess our AI readiness."

A good result starts with questions about your organisation, or a note of what it has already read, before anything is scored. Then comes a table with the seven areas, each with a score from 0 to 3, what is already working and the evidence. It ends with one sentence naming the main thing holding you back. It does not score an area from general knowledge of what AI can do.

## For AI agents installing this skill

1. Read `SKILL.md` and every other file in this folder. Tell the user in two or three sentences what the skill will do.
2. Check "What you need first" against what you can see. Ask the user before connecting an account or installing a tool.
3. Install the whole folder, not only `SKILL.md`, in your skills location. If the user asked for changes, install the changed copy and tell them what you changed.
4. Do not change anything outside your skills location without asking.
5. Offer to run the request under "Checking it works".
