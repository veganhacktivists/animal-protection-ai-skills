# Setting up catch-up

When you come back to a long conversation with your AI that you haven't looked at for days or months, this skill tells you in twelve sentences or fewer what you asked for, where it got to and what you need to decide next.

## What you need first

Nothing. It works with the AI agent alone.

To be caught up on a different conversation from the one you are in, your agent needs to be able to search its own past conversations. Claude Code and Codex can. A fresh browser chat usually cannot, so paste that conversation in instead.

## Installing it

The easiest way is to give your AI agent the link to this folder and ask it to install the skill. Your agent can usually do this for you.

To install it by hand:

- **Claude Code:** run `/plugin marketplace add veganhacktivists/animal-protection-ai-skills`, then `/plugin install catch-up@animal-protection-ai-skills`. Or copy this folder into `~/.claude/skills/`.
- **Claude Cowork and claude.ai:** download the `catch-up` zip from the [latest release](https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest) and upload it in Settings, under Capabilities, then Skills.
- **OpenAI Codex:** copy this folder into `~/.agents/skills/`.
- **Gemini CLI:** run `gemini skills install https://github.com/veganhacktivists/animal-protection-ai-skills.git --path skills/catch-up`.
- **GitHub Copilot:** run `gh skill install veganhacktivists/animal-protection-ai-skills catch-up`.
- **Microsoft 365 Copilot:** upload the zip from the latest release under Customize, then Upload skill.

If your AI tool cannot install skills, such as the plain ChatGPT web app, paste the contents of `SKILL.md` into a project's instructions or at the start of a chat. This works less well: the AI only has the instructions in that one chat or project, and any scripts in this folder will not run.

## Checking it works

In a long conversation you have been away from, ask your agent: "Catch me up."

A good result has three short sections: what you asked for, where it got to, and your next decision with a short list of options. It is twelve sentences or fewer, and leaves out the mechanics, such as which files were touched or which tools were run.

## For AI agents installing this skill

1. Read `SKILL.md` and every other file in this folder. Tell the user in two or three sentences what the skill will do.
2. Check "What you need first" against what you can see. Ask the user before connecting an account or installing a tool.
3. Install the whole folder, not only `SKILL.md`, in your skills location. If the user asked for changes, install the changed copy and tell them what you changed.
4. Do not change anything outside your skills location without asking.
5. Offer to run the request under "Checking it works".
