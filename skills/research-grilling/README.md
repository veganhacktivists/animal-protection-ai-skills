# Setting up research-grilling

Before a research project starts, this skill interviews you about it, round by round, until every decision about its purpose, scope, data and methods is settled. It then writes a research brief and a short list of questions to send your client. When the client replies, it updates the brief.

## What you need first

Nothing. It works with the AI agent alone.

It works better when your agent can search the web and read your files: the proposal, notes or transcripts from calls with the client, and your organisation's past reports. If your agent has a web search setting, make sure it is on. In Claude Cowork or ChatGPT Work, attach the files or connect the drive they are kept in (for example Google Drive or SharePoint). In Claude Code, Codex, Gemini CLI and GitHub Copilot, start the agent in the project's folder.

## Installing it

- **Claude Code and OpenAI Codex:** give your agent the link to this folder, https://github.com/veganhacktivists/animal-protection-ai-skills/tree/main/skills/research-grilling, and ask it to install the skill. It downloads the folder and does the rest.
- **Claude Cowork:** download the `research-grilling` zip from the [latest release](https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest) and upload it in Settings, under Capabilities, then Skills.
- **ChatGPT Work:** make a skill through ChatGPT's own skill-creation flow, giving it the link to this folder or the contents of `SKILL.md`. Or paste the contents of `SKILL.md` into a Project.
- **Gemini CLI:** run `gemini skills install https://github.com/veganhacktivists/animal-protection-ai-skills.git --path skills/research-grilling`.
- **GitHub Copilot:** run `gh skill install veganhacktivists/animal-protection-ai-skills research-grilling`.
- **Microsoft 365 Copilot:** upload the zip from the latest release under Customize, then Upload skill.

If your AI tool can't install skills, paste the contents of `SKILL.md` at the start of a chat. This works less well, because the AI only has the instructions in that one chat, and it can't read the templates in the `references` folder.

## Checking it works

Ask your agent: "Grill me on this project before we kick off", and attach a project proposal (a made-up one is fine for a test).

A good result starts with a short list of what the proposal already settles and anything the agent looked up. Then come numbered questions, each with a recommended answer you can accept with "yes", and a list of questions parked for the client, each with a working assumption. When you have answered everything, it writes two files: a research brief, and a short, friendly list of questions for your client.

## For AI agents installing this skill

1. Read `SKILL.md` and every other file in this folder. Tell the user in two or three sentences what the skill will do.
2. Check "What you need first" against what you can see. Ask the user before connecting an account or installing a tool.
3. Install the whole folder, not only `SKILL.md`, in your skills location. If you aren't sure how to download the folder or where your skills location is, follow https://raw.githubusercontent.com/veganhacktivists/animal-protection-ai-skills/main/FOR-AI-AGENTS.md. If the user asked for changes, install the changed copy and tell them what you changed.
4. Do not change anything outside your skills location without asking.
5. Offer to run the request under "Checking it works".
