# Animal Protection Skills

A trusted, human-reviewed collection of AI agent skills for people working in animal protection.

Maintained by the [Vegan Hacktivists](https://veganhacktivists.org/) AI Services team. Skills come from our team and from organisations across the movement. Every skill in this repo has been read line by line by a member of our team before it was merged.

## What a skill is

A skill is a folder containing a `SKILL.md` file. That file is a set of instructions an AI agent reads when it decides the skill is relevant to what you have asked. Skills teach an agent how to do a specific job the way an experienced person would do it: critique a chart, strip AI tells out of a draft, catch you up on an old conversation.

The format is the open [Agent Skills standard](https://agentskills.io/), so the same folder works in Claude (Code, Cowork and claude.ai), OpenAI Codex, Gemini CLI, GitHub Copilot and Microsoft 365 Copilot. See [Installing a skill](#installing-a-skill) for the details per agent.

## How to use this repo

You do not need to read the skills yourself. The intended way to use this repo is to point your AI agent at it and talk to it.

Paste the repo link into your agent and try things like:

- "Read the skills index in this repo and tell me which skills would be useful for my job. I do fundraising for a farmed animal charity."
- "Read the `graph-advisor` skill and tell me whether it would help me. What does it need set up first?"
- "Install the `de-ai-writing` skill from this repo for me."
- "Install `catch-up`, but change it so the summary is aimed at my manager rather than at me."

That last one is the point. A skill is plain text. Your agent can read it, discuss it with you, adapt it to your organisation and install the adapted copy. You are not stuck with our version.

Start with [`INDEX.md`](INDEX.md). It lists every skill with a one-line description, who wrote it, what it needs, and when we last checked it works.

## Installing a skill

Every skill lives at `skills/<skill-name>/`. Your agent can usually do this for you if you ask. If you would rather do it yourself:

**Claude Code**

```
/plugin marketplace add veganhacktivists/animal-protection-ai-skills
/plugin install de-ai-writing@animal-protection-ai-skills
```

Or copy the skill folder into `~/.claude/skills/` (all projects) or `.claude/skills/` (one project).

**Claude Cowork and claude.ai**

Download the skill folder as a zip (each release on the [Releases page](../../releases) has one zip per skill) and upload it in Settings under Capabilities, then Skills.

**OpenAI Codex**

Copy the skill folder into `~/.agents/skills/` (all projects) or `.agents/skills/` in your repo. The ChatGPT web app cannot install custom skills, so this route is for the Codex desktop app, command line tool and IDE extension.

**Gemini CLI**

```
gemini skills install https://github.com/veganhacktivists/animal-protection-ai-skills.git --path skills/de-ai-writing
```

**GitHub Copilot**

```
gh skill install veganhacktivists/animal-protection-ai-skills de-ai-writing
```

**Microsoft 365 Copilot**

Upload the skill's zip from the [Releases page](../../releases) under Customize, then Upload skill.

**Any agent, one command**

The community [`skills` installer](https://skills.sh) knows the install path for most agents:

```
npx skills add veganhacktivists/animal-protection-ai-skills
```

## Submitting a skill

We want skills from across the movement, and the author is credited in the skill itself and in the index.

Two ways to submit:

1. **Open a pull request.** Read [CONTRIBUTING.md](CONTRIBUTING.md) for the folder layout and the required fields. Your agent can do most of this for you: "Read CONTRIBUTING.md in this repo and prepare my skill for submission."
2. **Email us** at hello@veganhacktivists.org with the skill folder attached, or a link to it. Put "Skill submission" in the subject line. We will do the pull request for you and credit you as the author.

Every submission is read in full by a member of the Vegan Hacktivists AI Services team before it is merged. We check that it does what it says, that it does not do anything else, and that it works on at least one agent. We may suggest edits. We will say no to skills that are not useful to animal protection work, or that we cannot review with confidence.

## What "trusted" means here

A skill is a set of instructions your agent will follow, so a bad one could tell your agent to do something you did not ask for. That is why nothing goes into this repo without a human reading every line.

What we check for is written down in [CONTRIBUTING.md](CONTRIBUTING.md#review-checklist). In short: no instructions fetched from elsewhere at run time, no hidden or encoded text, no scripts we have not read, no requests for credentials, nothing that sends data anywhere the user did not ask for.

We still recommend you read a skill, or have your agent summarise it for you, before installing it. Trust, then check.

## Versions and dates

Each `SKILL.md` carries a `version` and a `last-verified` date in its frontmatter. The version changes when the skill changes. The date is the last time one of us ran the skill and confirmed it still works. Repo releases are tagged so you can install from a known point.

## Licence

Everything here is [MIT licensed](LICENSE). Copy it, change it, use it inside your organisation, no permission needed.

## Related

- [Vegan Hacktivists AI Resource Library](https://github.com/veganhacktivists/ai-resource-library) for guides, templates and other AI resources that are not skills.
- [Agent Skills specification](https://agentskills.io/specification) for the file format.
