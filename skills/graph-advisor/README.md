# Setting up graph-advisor

Share a chart or graph and this skill gives you blunt, specific feedback on how well it gets its main point across, based on data visualisation good practice. It does not redraw the chart unless you ask it to.

## What you need first

Nothing. It works with the AI agent alone.

Your agent needs to see the chart, so paste in the image or the chart file. If your agent cannot view images, describe the chart in words or share the data and the code that draws it.

## Installing it

The easiest way is to give your AI agent the link to this folder and ask it to install the skill. Your agent can usually do this for you.

To install it by hand:

- **Claude Code:** run `/plugin marketplace add veganhacktivists/animal-protection-ai-skills`, then `/plugin install graph-advisor@animal-protection-ai-skills`. Or copy this folder into `~/.claude/skills/`.
- **Claude Cowork and claude.ai:** download the `graph-advisor` zip from the [latest release](https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest) and upload it in Settings, under Capabilities, then Skills.
- **OpenAI Codex:** copy this folder into `~/.agents/skills/`.
- **Gemini CLI:** run `gemini skills install https://github.com/veganhacktivists/animal-protection-ai-skills.git --path skills/graph-advisor`.
- **GitHub Copilot:** run `gh skill install veganhacktivists/animal-protection-ai-skills graph-advisor`.
- **Microsoft 365 Copilot:** upload the zip from the latest release under Customize, then Upload skill.

If your AI tool cannot install skills, such as the plain ChatGPT web app, paste the contents of `SKILL.md` into a project's instructions or at the start of a chat. This works less well: the AI only has the instructions in that one chat or project, and any scripts in this folder will not run.

## Checking it works

Ask your agent: "Critique this graph." and paste in a chart.

If you didn't say what the chart is meant to show, a good result asks you that first. Then it gives short sections such as what's working, the main takeaway, the title, the axes, colour and what to cut, each with specific suggestions. It skips sections with nothing to say and does not redraw the chart.

## For AI agents installing this skill

1. Read `SKILL.md` and every other file in this folder. Tell the user in two or three sentences what the skill will do.
2. Check "What you need first" against what you can see. Ask the user before connecting an account or installing a tool.
3. Install the whole folder, not only `SKILL.md`, in your skills location. If the user asked for changes, install the changed copy and tell them what you changed.
4. Do not change anything outside your skills location without asking.
5. Offer to run the request under "Checking it works".
