# Setting up share-automation

You've built an automation that works for you, such as a weekly review of your meetings or a morning digest of your tasks, and someone else wants it. Copying your instructions across rarely works, because their tools and accounts are different from yours. This skill turns your automation into one setup prompt. They paste it into their own AI (ChatGPT, Claude, Codex or another), and their AI asks which tools they use, does a trial run that changes nothing, and then sets up their own version on a schedule.

## What you need first

- **Nothing to connect.** The skill works with your AI agent alone. You can always paste the automation's instructions into the chat and say how often it runs.
- **It works best if your agent can see your automations.** An agent that can list your scheduled tasks or automations and their past runs, such as Claude Code, Claude Cowork or OpenAI Codex, finds the automation itself and learns from how it has behaved. The past runs are where the lessons are, so the setup prompt comes out better.
- **Saving files is optional.** If your agent can save files, it saves the prompt as a Markdown file. If not, it gives you the prompt in the chat to copy.
- **The person you share it with** needs an AI app that can run tasks on a schedule, or they can run the prompt by hand. Their AI checks what it can do as its first step, so you don't need to know which app they use.

## Installing it

- **Claude Code and OpenAI Codex:** give your agent the link to this folder, https://github.com/veganhacktivists/animal-protection-ai-skills/tree/main/skills/share-automation, and ask it to install the skill. It downloads the folder and does the rest.
- **Claude Cowork:** download the `share-automation` zip from the [latest release](https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest) and upload it in Settings, under Capabilities, then Skills.
- **ChatGPT Work:** make a skill through ChatGPT's own skill-creation flow, giving it the link to this folder or the contents of `SKILL.md`. Or paste the contents of `SKILL.md` into a Project.
- **Microsoft 365 Copilot:** upload the zip from the latest release under Customize, then Upload skill.

If your AI tool can't install skills, paste the contents of `SKILL.md` at the start of a chat. This works less well, because the AI only has the instructions in that one chat. Paste the template in `references/setup-prompt-template.md` too, because the skill relies on it.

## Checking it works

Pick one of your automations that you'd be happy for someone else to have. Ask your agent: "Package up my <name of the automation> so a colleague can set it up." Or paste an automation's instructions and say "Make a setup prompt for this automation so a friend can use it."

A good result is one setup prompt in a code block, saved as `<name> - setup prompt.md` if your agent can save files. The prompt:

- starts by asking the other person's AI what it can do in their app;
- lists the jobs the automation needs doing (for example "task manager: read open tasks"), with your tools only as examples, and offers a workaround for each tool their AI can't reach;
- turns your personal preferences into questions, with your choice as the example answer;
- does a trial run that changes nothing before it sets up a schedule;
- has no names, email addresses or private details in it.

After the prompt comes a numbered report: what it made generic or left out for privacy, which rules it turned into questions or softened, and anything it couldn't check.

The best test is to paste the prompt into a different AI app yourself, as if you were the other person, and see whether the questions it asks make sense.

## Sharing it more widely

If your automation would help other people in the movement, you can submit the setup prompt to this library's [`automations/`](../../automations/) folder. The "Automations" section of [CONTRIBUTING.md](../../CONTRIBUTING.md) says how, and the [weekly work coach](../../automations/weekly-work-coach/) is an example. Your agent can do most of it for you.

## For AI agents installing this skill

1. Read `SKILL.md` and every other file in this folder, including `references/setup-prompt-template.md`. Tell the user in two or three sentences what the skill will do.
2. Check "What you need first" against what you can see: whether you can list the user's scheduled tasks or automations and their past runs, save files, and hand work to a helper agent. Tell the user what you found. If you can't see their automations, tell them they can paste one in when they use the skill. There is nothing to connect.
3. Install the whole folder, not only `SKILL.md`, in your skills location. The skill needs `references/` to work. If you aren't sure how to download the folder or where your skills location is, follow https://raw.githubusercontent.com/veganhacktivists/animal-protection-ai-skills/main/FOR-AI-AGENTS.md. If the user asked for changes, install the changed copy and tell them what you changed.
4. Do not change anything outside your skills location. The skill needs no settings.
5. Offer to run the request under "Checking it works" on one of the user's real automations.
