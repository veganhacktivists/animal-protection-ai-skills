# Setting up ai-smell

This skill takes text that reads as if an AI wrote it and removes the patterns that give it away, such as em dashes, "it's not X, it's Y" sentences and words like "delve". It changes as little as possible. It is an editing pass, not a rewrite.

## What you need first

Nothing. It works with the AI agent alone.

## Installing it

The easiest way is to give your AI agent the link to this folder and ask it to install the skill. Your agent can usually do this for you.

To install it by hand:

- **Claude Code:** run `/plugin marketplace add veganhacktivists/animal-protection-ai-skills`, then `/plugin install ai-smell@animal-protection-ai-skills`. Or copy this folder into `~/.claude/skills/`.
- **Claude Cowork and claude.ai:** download the `ai-smell` zip from the [latest release](https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest) and upload it in Settings, under Capabilities, then Skills.
- **OpenAI Codex:** copy this folder into `~/.agents/skills/`.
- **Gemini CLI:** run `gemini skills install https://github.com/veganhacktivists/animal-protection-ai-skills.git --path skills/ai-smell`.
- **GitHub Copilot:** run `gh skill install veganhacktivists/animal-protection-ai-skills ai-smell`.
- **Microsoft 365 Copilot:** upload the zip from the latest release under Customize, then Upload skill.

If your AI tool cannot install skills, such as the plain ChatGPT web app, paste the contents of `SKILL.md` into a project's instructions or at the start of a chat. This works less well: the AI only has the instructions in that one chat or project, and any scripts in this folder will not run.

## Checking it works

Ask your agent: "Check this for AI smells:" and paste in a paragraph an AI wrote for you.

A good result is the same paragraph back, with the same meaning and mostly the same words, minus the giveaway patterns. There is no commentary before or after it.

## For AI agents installing this skill

1. Read `SKILL.md` and every other file in this folder. Tell the user in two or three sentences what the skill will do.
2. Check "What you need first" against what you can see. Ask the user before connecting an account or installing a tool.
3. Install the whole folder, not only `SKILL.md`, in your skills location. If the user asked for changes, install the changed copy and tell them what you changed.
4. Do not change anything outside your skills location without asking.
5. Offer to run the request under "Checking it works".
