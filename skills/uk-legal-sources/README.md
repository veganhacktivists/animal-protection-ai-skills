# Setting up uk-legal-sources

This skill helps your AI agent research UK law and policy from the original sources instead of from memory. It knows which official site holds each kind of answer (legislation.gov.uk for Acts, Hansard for debates and written questions, Find Case Law for judgments, GOV.UK for guidance) and which way of reaching each one actually works. It comes with small programs that read Parliament's and the government's open data feeds, and it ends every answer with a list of the sources it used, so you can check them.

## What you need first

- **An agent that can run Python with internet access,** such as Claude Code, Claude Cowork or OpenAI Codex. The programs use plain Python 3 and need nothing installed.
- **Permission for your agent to reach the data feeds** in the table under "Letting your AI reach the data feeds". Claude Code and Codex on your own computer can usually reach them already. Claude Cowork only reaches websites on an approved list, so you will probably need to add them.
- **If you can't change that permission:** a web browser your agent can control, such as Claude in Chrome. Your agent then opens the same data feeds in your browser and reads them there. It is slower, but it works.

If your AI tool can't run code or control a browser, paste the contents of `PROMPT.md` at the start of a chat instead. It gives any AI the same rules about fetching and quoting sources.

## Installing it

- **Claude Code and OpenAI Codex:** give your agent the link to this folder, https://github.com/veganhacktivists/animal-protection-ai-skills/tree/main/skills/uk-legal-sources, and ask it to install the skill. It downloads the folder and does the rest.
- **Claude Cowork:** download the `uk-legal-sources` zip from the [latest release](https://github.com/veganhacktivists/animal-protection-ai-skills/releases/latest) and upload it in Settings, under Capabilities, then Skills.
- **ChatGPT Work:** make a skill through ChatGPT's own skill-creation flow, giving it the link to this folder or the contents of `SKILL.md`. Or paste the contents of `SKILL.md` into a Project.
- **Microsoft 365 Copilot:** upload the zip from the latest release under Customize, then Upload skill.

If your AI tool can't install skills, paste the contents of `SKILL.md` at the start of a chat. This works less well, because the AI only has the instructions in that one chat.

## Letting your AI reach the data feeds

The official Parliament websites block automated visits, so the skill doesn't use them. It reads Parliament's open data feeds instead, which are built for software. Your agent needs permission to reach these addresses:

| Address | What the skill uses it for |
| --- | --- |
| questions-statements-api.parliament.uk | Written questions and answers |
| hansard-api.parliament.uk | Debates in the Commons and Lords |
| members-api.parliament.uk | MPs and peers |
| committees-api.parliament.uk | Select committees and their written evidence |
| bills-api.parliament.uk | Progress of bills |
| www.legislation.gov.uk | Acts and statutory instruments, including past versions |
| caselaw.nationalarchives.gov.uk | Court judgments (Find Case Law) |
| www.gov.uk | Government guidance, consultations and ministers' meetings |

Two more are optional: api.parliament.uk for Hansard before 2005, and publications.europa.eu for the text of EU law.

**In Claude Cowork:** open Settings, then Capabilities. Turn on "Allow network egress", choose the option that allows package managers plus specific domains, and add the addresses above. The labels may differ slightly on your screen. On a Team or Enterprise plan the same setting is under Organization settings, then Capabilities, and only an organisation owner can change it. Start a new session afterwards, because the setting only applies to sessions started after the change.

**In other tools:** ask your agent where its network setting is. It can tell you for the tool it is running in.

Some sources won't work whatever you allow, because the sites block automated visits: the Commons Daily Report PDF, the normal hansard.parliament.uk and questions-statements.parliament.uk pages, and TheyWorkForYou. BAILII is left out on purpose, because its terms forbid automated access. The data feeds above carry the same Parliament material.

## If you can't change the setting

If you aren't allowed to change your network settings, or your organisation owner says no, your agent can use a web browser instead. In Claude Cowork and Claude Code, install and connect Claude in Chrome. Your agent then opens the same data feed addresses in your browser, which uses your own internet connection rather than the agent's. It reads one page at a time, so a big search takes longer.

## Checking it works

Ask your agent: "Use the uk-legal-sources skill to find written questions about animal welfare tabled in the last two weeks, with who asked, the department and the full answer."

A good result lists each question with its number, the MP or peer who asked it, the department, the full answer (or a note that it hasn't been answered yet) and a link. It ends with a section headed "Data sources I used for this answer" that says it used the written questions data feed, or your browser. If the answer only has headings or search snippets, the agent couldn't reach the feed: go back to "Letting your AI reach the data feeds".

## For AI agents installing this skill

1. Read `SKILL.md` and every other file in this folder, including the scripts. Tell the user in two or three sentences what the skill does.
2. Install the whole folder, not only `SKILL.md`, in your skills location. If you aren't sure how to download the folder or where your skills location is, follow https://raw.githubusercontent.com/veganhacktivists/animal-protection-ai-skills/main/FOR-AI-AGENTS.md. Don't change anything outside it without asking.
3. Check whether you can reach the data feeds. Run `python3 scripts/check_access.py --feeds` from the installed folder. Each line says `OK`, `BLOCKED BY YOUR NETWORK SETTINGS`, or something else.
4. If every line says `OK`, go to step 7.
5. If any line says `BLOCKED BY YOUR NETWORK SETTINGS`, or you can't run code with internet access at all, tell the user which addresses you couldn't reach and ask whether they can change your network settings. Explain that on a Team or Enterprise plan only an organisation owner may be able to.
   - **If they can:** walk them through it one step at a time for the tool you are running in. Use "Letting your AI reach the data feeds" above, and give them the full list of addresses to add so they only do it once. Tell them to start a new session or chat afterwards, then run the check in step 3 again there.
   - **If they can't, or would rather not:** go to step 6.
6. Check whether you can control a real web browser on the user's computer. If you can, open `https://questions-statements-api.parliament.uk/api/writtenquestions/questions?take=1` in it and confirm you can read the data on the page. Tell the user you will read the data feeds through their browser for this skill, and that it is slower. If you can't control a browser, tell the user they can connect one (in Claude Cowork and Claude Code, Claude in Chrome), or that you will give them each address to open and paste back.
7. Offer to run the request under "Checking it works".
