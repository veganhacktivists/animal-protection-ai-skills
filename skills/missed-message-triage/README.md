# Setting up missed-message-triage

This skill checks your messaging apps for things people asked you to do that never became tasks, and gives you a numbered list of draft tasks to approve. It only reads. It never creates a task or sends a message.

Unlike most skills, it has to be wired to your own chats and task manager before it works. When you install it, your agent looks at what it can already reach, asks you a few questions and writes your answers into its copy of the skill.

## What you need first

- **Your messaging apps.** Your agent needs to read the apps where people ask you for things. In Claude, connect a connector for each one. In Codex, install an MCP server for each. An aggregator such as Beeper can cover WhatsApp, Discord, iMessage, Signal, LinkedIn and more through one connection.
- **Your task manager.** Your agent needs to search it, including tasks with future due dates, for example Todoist, Asana, Monday, Linear, Things, Notion or a plain markdown file. Connect it the same way.
- **A private place for a state file.** The skill keeps notes between runs, and they quote private conversations. Keep the file wherever you keep private material, never in a shared folder or repository.
- **Optional, a scheduler.** To run it automatically, use an agent that can run scheduled tasks, such as Claude Code or Codex. Otherwise, ask for it when you want it.

## Installing it

The easiest way is to give your AI agent the link to this folder and ask it to install the skill. Your agent can usually do this for you, and it will then ask you the setup questions.

To install it by hand:

- **Claude Code:** run `/plugin marketplace add veganhacktivists/animal-protection-ai-skills`, then `/plugin install missed-message-triage@animal-protection-ai-skills`. Or copy this folder into `~/.claude/skills/`.
- **Claude Cowork and claude.ai:** download the `missed-message-triage` zip from the [latest release](https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest) and upload it in Settings, under Capabilities, then Skills.
- **OpenAI Codex:** copy this folder into `~/.agents/skills/`.
- **Gemini CLI:** run `gemini skills install https://github.com/veganhacktivists/animal-protection-ai-skills.git --path skills/missed-message-triage`.
- **GitHub Copilot:** run `gh skill install veganhacktivists/animal-protection-ai-skills missed-message-triage`.
- **Microsoft 365 Copilot:** upload the zip from the latest release under Customize, then Upload skill.

If your AI tool cannot install skills, such as the plain ChatGPT web app, paste the contents of `SKILL.md` into a project's instructions or at the start of a chat. This works less well: the AI only has the instructions in that one chat or project, and any scripts in this folder will not run.

After installing it by hand, ask your agent to "set up missed-message-triage", so it can ask you the setup questions.

## Checking it works

Ask your agent: "Check my messages from the last two days for anything I was asked to do that isn't in my task list."

A good result is a short numbered list of draft tasks, each with a title, a suggested due date and priority, a line or two of context and the conversation it came from. It ends with a Watchouts section naming any source it couldn't check. If nothing credible came up, it says so instead of padding the list. Nothing is added to your task manager by the skill.

## For AI agents installing this skill

1. Read `SKILL.md` and every other file in this folder. Tell the user in two or three sentences what the skill will do.
2. Check "What you need first" against what you can see. Ask the user before connecting an account or installing a tool.
3. Install the whole folder, not only `SKILL.md`, in your skills location. If the user asked for changes, install the changed copy and tell them what you changed.
4. Do not change anything outside your skills location without asking. The scheduled task in step 8 is the one exception, and only once the user has asked for it.
5. **Look before you ask.** Work these out yourself first, then report what you found:
   - Where skills and scheduled tasks live in your agent. Claude Code uses `~/.claude/skills/` and `~/.claude/scheduled-tasks/<id>/SKILL.md`. Codex uses `~/.agents/skills/` or `~/.codex/skills/`, and `~/.codex/automations/<id>/automation.toml`.
   - Which messaging connectors you have. Enumerate your tools. Do not ask "do you use Slack?" when you can see whether a Slack tool exists. Ask instead about the ones you *can* reach.
   - Whether there is an aggregator such as Beeper. If there is, list its connected accounts. That answers most of the platform question outright.
   - Which task managers you can reach. There may be more than one, split by area of life.
   - Which scheduled tasks already exist, so you don't stack another heavy job onto a slot that's already busy.
   - Whether the user keeps context files you should read, such as a colleagues list, a channel routing map or a workspace `AGENTS.md`. These make the difference between "someone called Sam asked for something" and a correctly attributed, correctly routed task.
   - The user's own identity on each platform: their user ID, handle and display name. Without this the skill cannot tell what was directed *at* them from what was merely near them. This is the most common reason a first run returns garbage.
6. **Ask.** Cover these, adapting the wording but keeping the intent:
   - Scope: which of the platforms you can reach carry work requests to them? Sweep everything, or only work chats, and if only some, is there a rule or a channel map? Anyone whose requests should always surface, even when phrased casually? Anything to ignore, such as a busy channel, a personal chat or a bot?
   - Task system: where do their tasks live? If there is more than one, which is authoritative, and does certain work belong in a specific one? Confirm you can search it, including tasks due in the future.
   - Timing: scheduled or on demand? If scheduled, how often and at what time? Recommend every other day: daily produces too many empty runs and the output stops being read. Offset it from their other morning automations, because two agents hitting the same message and task connectors at once causes contention and a pile-up of permission prompts. What timezone should it use?
   - Output and state: where should the state file live? Default it next to the skill or scheduled task, somewhere they treat as private. Do they want the output in chat, as a notification or in a file?

   Do not ask about the read-only rule or the state file format. Those are not preferences. They are already built into the skill.
7. Fill in every line of "Your user's setup" in your installed copy of `SKILL.md` with their answers.
8. If they want it scheduled, create a scheduled task in your agent that runs this skill at the time they chose.
9. Offer to run the request under "Checking it works".
