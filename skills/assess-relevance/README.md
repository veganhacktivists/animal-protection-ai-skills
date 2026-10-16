# Setting up assess-relevance

Share a report, paper, policy brief, web page or file, and this skill tells you whether it is worth your time for your animal advocacy work: Highly relevant, Possibly relevant or Not relevant, with a plain-language reason. It keeps a high bar, so most things are not marked Highly relevant.

## What you need first

Nothing. It works with the AI agent alone.

It gives a sharper answer when your agent already knows about your work, for example from a memory feature, a project's custom instructions, or a `CLAUDE.md` or `AGENTS.md` file. Without that, it judges relevance for a typical animal protection worker and says so.

## Installing it

The easiest way is to give your AI agent the link to this folder and ask it to install the skill. Your agent can usually do this for you.

To install it by hand:

- **Claude Code:** run `/plugin marketplace add veganhacktivists/animal-protection-ai-skills`, then `/plugin install assess-relevance@animal-protection-ai-skills`. Or copy this folder into `~/.claude/skills/`.
- **Claude Cowork and claude.ai:** download the `assess-relevance` zip from the [latest release](https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest) and upload it in Settings, under Capabilities, then Skills.
- **OpenAI Codex:** copy this folder into `~/.agents/skills/`.
- **Gemini CLI:** run `gemini skills install https://github.com/veganhacktivists/animal-protection-ai-skills.git --path skills/assess-relevance`.
- **GitHub Copilot:** run `gh skill install veganhacktivists/animal-protection-ai-skills assess-relevance`.
- **Microsoft 365 Copilot:** upload the zip from the latest release under Customize, then Upload skill.

If your AI tool cannot install skills, such as the plain ChatGPT web app, paste the contents of `SKILL.md` into a project's instructions or at the start of a chat. This works less well: the AI only has the instructions in that one chat or project, and any scripts in this folder will not run.

## Checking it works

Ask your agent: "Is this worth my time?" and paste a link to a report.

A good result has a verdict at the top, a few plain sentences on what the document says, and a paragraph on why it does or does not matter to you. That paragraph quotes what the agent knows about your work, or says it had nothing to go on.

## For AI agents installing this skill

1. Read `SKILL.md` and every other file in this folder. Tell the user in two or three sentences what the skill will do.
2. Check "What you need first" against what you can see. Ask the user before connecting an account or installing a tool.
3. Install the whole folder, not only `SKILL.md`, in your skills location. If the user asked for changes, install the changed copy and tell them what you changed.
4. Do not change anything outside your skills location without asking.
5. Offer to run the request under "Checking it works".
