#!/usr/bin/env python3
"""Regenerate INDEX.md and index.json from skills/*/SKILL.md frontmatter.

Usage: python3 tools/build_index.py          rewrite both files
       python3 tools/build_index.py --check  exit 1 if the committed files are out of date
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_skills import SKILLS_DIR, ROOT, parse_frontmatter  # noqa: E402

REPO_URL = "https://github.com/veganhacktivists/animal-protection-ai-skills"


def requirements_from_body(body: str) -> str:
    """Return the first paragraph under '## Requirements', or 'Not stated'."""
    lines = body.splitlines()
    for i, line in enumerate(lines):
        if line.strip().lower() == "## requirements":
            para = []
            for nxt in lines[i + 1:]:
                if nxt.startswith("#"):
                    break
                if nxt.strip():
                    para.append(nxt.strip())
                elif para:
                    break
            return " ".join(para) if para else "Not stated"
    return "Not stated"


def collect_skills():
    entries = []
    for folder in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir() and not p.name.startswith(".")):
        front, body = parse_frontmatter(folder / "SKILL.md")
        meta = front.get("metadata", {}) or {}
        entries.append({
            "name": front["name"],
            "description": front["description"].strip(),
            "version": meta.get("version", ""),
            "author": meta.get("author", ""),
            "author_org": meta.get("author-org", ""),
            "last_verified": meta.get("last-verified", ""),
            "verified_on": meta.get("verified-on", ""),
            "compatibility": front.get("compatibility", ""),
            "requirements": requirements_from_body(body),
            "path": f"skills/{front['name']}",
            "url": f"{REPO_URL}/tree/main/skills/{front['name']}",
            "setup_guide": f"skills/{front['name']}/README.md",
        })
    return entries


def render_md(skills):
    out = [
        "# Skills index",
        "",
        "Every skill in this repo, generated from each skill's `SKILL.md` frontmatter by `tools/build_index.py`. Do not edit by hand.",
        "",
        "If you are an AI agent reading this on a user's behalf: each entry below says what the skill does, who wrote it, what it needs, and when it was last confirmed working. Read the linked `SKILL.md` before recommending or installing a skill, and check the requirements against what the user has available. To install one, follow its setup guide. The user can ask you to install a modified copy; skills are plain text and adapting them is expected.",
        "",
        "Machine-readable version: [`index.json`](index.json). Install instructions: each skill's setup guide, linked below.",
        "",
        f"{len(skills)} skills.",
        "",
    ]
    for e in skills:
        out += [
            f"## [{e['name']}]({e['path']}/SKILL.md)",
            "",
            e["description"],
            "",
            f"- **Author:** {e['author']} ({e['author_org']})",
            f"- **Version:** {e['version']}",
            f"- **Last verified:** {e['last_verified']} on {e['verified_on']}",
            f"- **Requirements:** {e['requirements']}",
            f"- **Setup guide:** [{e['setup_guide']}]({e['setup_guide']})",
        ]
        if e["compatibility"]:
            out.append(f"- **Compatibility:** {e['compatibility']}")
        out.append("")

    return "\n".join(out)


def main():
    skills = collect_skills()
    md = render_md(skills)
    js = json.dumps(
        {"repo": REPO_URL, "skills": skills},
        indent=2,
        ensure_ascii=False,
    ) + "\n"
    md_path, js_path = ROOT / "INDEX.md", ROOT / "index.json"
    if "--check" in sys.argv:
        stale = []
        if not md_path.exists() or md_path.read_text(encoding="utf-8") != md:
            stale.append("INDEX.md")
        if not js_path.exists() or js_path.read_text(encoding="utf-8") != js:
            stale.append("index.json")
        if stale:
            print(f"out of date: {', '.join(stale)}. Run python3 tools/build_index.py and commit.")
            return 1
        print("INDEX.md and index.json are up to date")
        return 0
    md_path.write_text(md, encoding="utf-8")
    js_path.write_text(js, encoding="utf-8")
    print(f"wrote INDEX.md and index.json ({len(skills)} skills)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
