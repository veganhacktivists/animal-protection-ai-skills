---
name: de-ai-writing
description: "Edits text to remove AI writing tells with minimal changes, keeping the original wording and structure intact. Not a rewrite tool. Use when the user pastes AI-generated or AI-assisted text and says \"fix this\", \"make this sound human\", \"de-AI this\", \"strip the AI tells\", or \"this reads like ChatGPT wrote it\". Do NOT trigger for general editing or proofreading requests that don't mention AI voice."
license: MIT
metadata:
  version: "1.0.0"
  author: Richie (Thomas Manandhar-Richardson)
  author-org: Vegan Hacktivists
  last-verified: "2026-09-07"
  verified-on: "Claude Code, Claude Cowork"
---

# De-AI Writing

You are editing text to strip out the patterns that make readers think "AI wrote this." Your goal is the same text, minus the tells: as close to the original wording as possible, but reading like a competent human wrote it. Not a human pretending to be quirky. Not a human trying too hard. Just normal, clear writing.

## Philosophy

AI tells are not just about vocabulary. They exist on five layers, from surface to deep:

1. **Vocabulary** (the words themselves)
2. **Punctuation habits**
3. **Sentence structure and syntax**
4. **Paragraph and document architecture**
5. **Rhythm and cadence**

Most people only address layer 1 (swapping out "delve" for "explore") and wonder why it still sounds like AI. That is because layers 3-5 are where the real tells live. This skill works through all five.

## Process

When you receive text to de-AI:

1. Read the full text first. Understand what it is actually trying to say.
2. Go through it and identify every AI tell listed below.
3. Fix each tell with the smallest edit that removes it: swap a word, cut a filler phrase, split a sentence, restructure the one offending sentence.
4. Leave everything else alone. Sentences that contain no tells should survive verbatim.

This is an editing pass, not a rewrite. Do not paraphrase text that was fine, do not reorganise the document, and do not add content. The author's voice, wording, and structure stay unless they are the problem.

## Layer 1: Vocabulary

### Banned words and phrases

Never use these in your rewrite. They are the most widely recognised AI tells. If the original uses them, replace with plain language or cut entirely.

**Verbs:** delve, leverage, utilize, harness, streamline, underscore, illuminate, elucidate, foster, embark, navigate (as metaphor), unravel, bolster, spearhead, catalyse, facilitate, encompass, captivate, showcase, exemplify, embody, epitomise

**Banned adverb pattern: "quietly" personifying AI or a system.** "AI quietly does X", "the system quietly handles Y". This softens and humanises the tool doing mechanical work, a common AI tell. State what it does without the adverb, or use a plain one ("in the background", "automatically") only if genuinely needed.

**Adjectives/adverbs:** pivotal, cutting-edge, groundbreaking, transformative, holistic, multifaceted, meticulous, dynamic, bustling, paramount, invaluable, fundamentally, intricately, meticulously

**Nouns:** tapestry, landscape (as metaphor), realm, journey (as metaphor), synergy, paradigm, testament, beacon, cornerstone, underpinning, bedrock, nexus, interplay, confluence, gamut, spectrum (when vague)

**Phrases:** "It's important to note that", "In today's [adjective] world/age", "Let's dive in", "Here's the thing", "At its core", "When it comes to", "From X to Y" (as sweeping range), "a testament to", "serves as a reminder", "the ever-evolving landscape of", "rich tapestry of", "stands as a beacon of", "at the intersection of", "paving the way for", "the art and science of", "not just X, but Y", "a deep understanding of", "plays a crucial role", "it is worth noting", "worth naming", "this is where X comes in", "the beauty of X lies in", "X is more than just Y", "X matters" (as a standalone closer, e.g. "This matters.", "Why this matters:"), "the whole point" (any variant: "that's the whole point," "it's the whole point," "that is the whole point of X"), "X is the win", "X is the unlock", "X is the tell", "X is the moat", "X becomes the trap", "X is the real cost" (see "X is the win" in Layer 3)

### What to use instead

Use ordinary, concrete language. If the original says "leverage AI to streamline workflows," write "use AI to speed up the work." Prefer short, common words. A good test: would you say this out loud to a colleague? If not, simplify.

## Layer 2: Punctuation

### Em dashes

This is the single most discussed AI tell. Don't use them ever.

- If the original is full of em dashes, replace them with: periods (split into two sentences), commas, parentheses, colons, or just cut the aside.
- **Never use double hyphens (--) as a substitute.** That is the same tell in a different costume.

### Semicolons

AI overuses semicolons to glue simple sentences together. Use them only where both clauses are genuinely interdependent and a period would lose something. In most cases, use a period and start a new sentence.

### Colons

Fine when genuinely introducing something. Not fine as a dramatic pause substitute.

### Leading zeros on single-digit numbers

Padding the numbers 1 to 9 with a leading zero in a numbered list or numbered table of contents ("01.", "02.", "03.") is an AI tell. Write plain "1.", "2.", "3." instead. Only keep zero-padding where it is functionally required (e.g. dates, IDs, or filenames that need fixed-width sorting).

## Layer 3: Sentence structure

This is where most "cleaned up" AI text still fails. The structures below are used at 2-5x the human rate in AI text. Avoid or severely limit all of them.

### An -ing or -ed phrase tacked on after a comma

AI pattern: "The system analyses the data, revealing key insights."
This structure (main clause, comma, then a verb phrase that modifies it) is the single most statistically overrepresented construction in AI text.

It comes in two forms, and both count:

- **The -ing form:** "The system analyses the data, revealing key insights." "It ships in March, giving the team time to test."
- **The -ed form:** "Eleven workflows, grouped under the weeks they extend." "The report went out on Friday, signed off by the whole team." The verb here is a past participle rather than an -ing word, so it is easy to miss, but it is the same shape doing the same job.

Rules:

- **Maximum one per 500 words, counting both forms together.** Zero is fine.
- Replace with: a new sentence ("The system analyses the data. This reveals..."), a conjunction ("The system analyses the data and reveals..."), a plain relative clause ("Eleven workflows that extend the weeks below"), or restructure entirely.

### "It's not X, it's Y" / "It's not just X, it's Y"

This contrastive negation pattern is one of the most recognised AI structures. **Never use it.** Find another way to make the point. State the positive claim directly. If the contrast matters, set it up across two sentences.

### Rule of three (tricolon)

AI groups things in threes constantly: "fast, reliable, and scalable." Three-part lists with neat parallel structure are a strong AI signal, especially when the items are abstract or corporate-sounding.

- **Break the pattern.** Use two items, or four, or five. Not always three.
- If you genuinely have three things to list, make sure they are concrete and not interchangeable buzzwords.
- Vary the rhythm. Not every list needs parallel grammatical structure.

### Manufactured-significance closers

AI likes to end a paragraph, section, or demo beat with a short standalone sentence that asserts importance instead of demonstrating it: "This matters." "Why this matters:" "That's the whole point." "That is the whole point of X." These add no information. If the preceding sentences already showed why something matters, the closer is dead weight. If they didn't, the closer papers over the gap instead of closing it.

- **Never use "X matters" or "that's the whole point" as a standalone closing sentence.** Cut it. If the original text already contains the concrete reason (a number, a consequence, a specific stake), let that stand as the closer; do not invent a new one.
- Watch for this at the end of paragraphs and sections especially. It is a tell that shows up disproportionately as a scene-closer or section-closer, the written equivalent of a mic drop that has no joke behind it.
- If you're tempted to write it, ask what the actual payoff is and say that instead. "Every hour this saves is an hour back for the campaign" beats "and that's the whole point" because it is a claim, not an assertion of importance.

### The self-disclaiming closer ("..., and we do not claim it")

AI names an alternative result and then formally disavows it in the same breath: "Scaling by hours would have given $1,600 to $2,400, and we do not claim it." "Matching on length alone would have given $1,950 to $2,900, and we do not claim it." "One reading puts the figure at 40%, though we make no such claim."

The disavowal does no work. If the paragraph already explained why the alternative was rejected, the reader knows it is not being claimed. The tacked-on disclaimer reads as procedural throat-clearing, and slightly defensive, as though the writer expects to be accused of something. It also has a stiff legal register that clashes with everything around it.

- **Cut the disclaimer and keep the number.** "Scaling by hours would have given $1,600 to $2,400." The figure is informative on its own.
- Catches the variants: "and we do not claim it", "we make no such claim", "this is not our claim", "we do not assert this", "though we do not rely on it", "we mention it only for completeness".
- If the rejection genuinely needs stating, give the reason instead of the disavowal: "Scaling by hours would have given $1,600 to $2,400, but hours and price are unrelated here."
- Watch for it in analytical and evidence-heavy writing especially, where it clusters at the end of paragraphs that consider and reject an approach.

### "X is the win" / "X is the unlock" / "X becomes the trap"

An ordinary noun gets "the" put in front of it and is handed over as a verdict: "Doing it live is the win." "Shared context is the unlock." "Efficiency becomes the trap." Other nouns that get used this way: the tell, the moat, the lever, the play, the move, the ask, the real cost, the whole game.

The definite article is doing all the work. "The win" asserts that this one thing is the thing that counts, without saying what follows from it. The reader gets a label where the claim should be. It sounds like a conclusion someone reached, but nothing was actually concluded.

- **Never use it.** Say what happens instead. "Doing the demo live is the unlock" becomes "When they watch it happen live, they go and try it themselves that afternoon."
- Catches the "becomes" and "is the real" variants too: "X becomes the trap", "X is the real cost", "that's the tell".
- Watch the ends of paragraphs and sections hardest. Like the closers above, this shape is most often used to land a beat.
- Test it: swap the noun phrase for a specific consequence, number, or stake. If you cannot, there was no claim there to begin with.
- Sibling of the "X matters" and "that's the whole point" closers above. Same job, dressed as a noun rather than a sentence.

### Manufactured-significance prefaces ("I want to be X about Y, because Z")

AI often announces a virtue before displaying it: "I want to be clear about this, because I've thought about it carefully." "I want to be precise about the claim, because precision is the whole spirit of this post." The "because" clause rarely gives a concrete reason, it usually just restates the virtue (precise because precision matters) instead of tying it to a real stake or consequence. A person making a hard point usually just makes it, without prefacing that they're about to be honest, clear, or precise.

- **Never use "I want to be [clear/honest/precise/fair] about X, because Y" where Y just restates the virtue instead of giving a concrete reason.**
- Flag repeated use even more than a single instance. This template showing up twice or more in one document is a stronger tell than any single occurrence.
- Sibling pattern: "There's a pattern worth naming here..." / "There's a second pattern worth naming..." Announcing that something significant is coming instead of just saying it. Cut the announcement; state the thing.
- Sibling pattern: "My honest take:", "My honest recommendation:", "Honestly,", "If I'm being honest," — labelling an opinion as honest before giving it. The honesty label adds nothing; a person just gives the take. **Cut the preface and state the take or recommendation directly.**

### The bolted-on "because" clause (Clause 1, because Clause 2)

The section above is the narrow case. The general shape is any clause, a comma, then "because" plus something that occupies the position of a reason without being one:

- "We do this on screen, together, because of what comes next."
- "I am putting it this way because it matters."
- "We start with the audit, because that is the whole point."

A real "because" clause tells you something you did not already know: a consequence, a constraint, a number, a stake. These do not. "Because of what comes next" points forward at something unstated and asks the reader to accept that it is important. The others just restate the first clause in different words.

- **Cut the clause, or replace it with the actual reason.** "We do this on screen, together, because of what comes next" becomes "We do this on screen together, so that the next exercise builds on what they just made."
- Watch for the forward-pointing kind especially ("because of what comes next", "because of what follows", "because of where this goes"). Withholding the reason is not the same as having one.
- Test it: can you put a specific consequence, number, or stake in place of the because-clause? If not, delete it. The first clause almost always stands fine alone.

### The drumroll "and" (setup clause, comma, and, reveal)

AI joins a flat setup clause to a second clause that reverses, escalates, or undercuts it, using "and" as a drum roll rather than as a connector:

- "There are two obvious ways to try to clear that bar, and both fail."
- "Foundations registration is open, and the public page doesn't say so."
- "Three vendor links had rotted, and one rotted dangerously."
- "The 2025 materials are public, and I'd missed them."

The tell is that the two halves are not two facts of equal weight being joined. The first exists only to make the second land. Swapping the comma for an em dash does not fix it: the shape is the tell, not the punctuation.

- **Maximum one per 800 words.** Zero is fine. Two in the same section is a strong tell on its own, and so is one used to close a paragraph.
- Watch for the escalating-echo variant, where the second clause repeats a word from the first and adds a twist ("had rotted... rotted dangerously"), and the self-implicating variant, where the reveal is the writer's own failure ("and I'd missed them").
- Fix by cutting the setup and keeping the fact that carries the weight ("The public page doesn't say Foundations registration is open"), by splitting into two sentences, or by using "but" where the contrast is real rather than staged.
- "I think X is true, and I want to be clear about why" is this pattern crossed with the manufactured-significance preface above. Cut the second clause and give the reason.

### Correlative conjunctions overuse

"Not only X but also Y" - These are fine in moderation. AI uses them in nearly every paragraph. Limit to one per 400 words.

### Hedging and throat-clearing

"It's worth noting that...", "It goes without saying...", "Generally speaking...", "Interestingly enough...", "To be sure..."

- **Cut all of them.** Just state the point.

### Over-explanation and "mansplaining"

AI tells you that Tokyo is the capital of Japan before telling you something about Tokyo. It defines terms the reader obviously knows.

- **Trust the reader.** If the audience for this text would already know something, do not explain it.

## Layer 4: Paragraph and document architecture

### Uniform paragraph length

AI paragraphs tend to be almost identical in length (4-6 sentences each, neat topic-sentence-then-support structure). This creates a metronomic feel.

- **Vary paragraph length by splitting and merging what is already there.** Break a key sentence out into its own one-line paragraph. Join two short related paragraphs. Do not write new material to pad or fill.

### Rigid topic-sentence structure

AI almost always opens a paragraph with its topic sentence, then supports it, then wraps it up. Every paragraph. Like clockwork.

- **Where every paragraph follows this template, reorder within a few of them.** Move an example or detail that is already in the paragraph up to the front. Do not invent new openings, questions, or concessions to break the pattern.

### Headers as filler

AI loves to use headers like "The Power of X" or "Why X Matters" or "Understanding X." These are generic and add nothing.

- If headers are appropriate for the format, make them specific and concrete. "How the 2024 supply chain crisis hit small farms" not "Understanding Supply Chain Challenges."
- If headers are not appropriate (e.g. a short blog post, a LinkedIn post, an email), do not add them.

### Eyebrow text above headers

Placing a small line of text directly above a header (a kicker or "eyebrow" — a short label, category, or teaser sitting above the main heading) is an AI tell. Do not add eyebrow text above a header. If one exists in the original and adds nothing, cut it or fold it into the header itself.

## Layer 5: Rhythm and cadence

Researchers call the variance in sentence structure and length "burstiness." AI has low burstiness; human writing has high burstiness. Aim for deliberate, controlled unevenness, not sloppiness.

### Sentence length uniformity

AI sentences cluster around 15-25 words. Human writing has much higher variance, mixing 5-word sentences with 35-word sentences.

- **Vary sentence length by splitting and merging.** Break a long sentence into a long one and a short one. Join two same-length sentences where it reads naturally. Read it aloud in your head: does it have a pulse, or does it drone?

### Predictable cadence

AI prose has a lulling, even beat. Each sentence carries roughly the same weight and lands the same way.

- **Break the rhythm with what is already on the page.** Split a sentence so its key clause stands alone as a fragment. Turn a "however" into a sentence starting with "But." Front-load important information sometimes, back-load it other times. Do not add new one-liners for effect.

## What NOT to do

- **Do not add fake "human" quirks.** Deliberate typos, random slang, forced humour, or "um, so, like" insertions are just a different kind of fake.
- **Do not make the text worse to make it sound human.** The goal is writing that is both good and human, not writing that is bad in a charming way.
- **Do not flag what you changed.** Just return the rewritten text. If the user wants a before/after analysis, they will ask.
- **Do not lose information.** Every factual claim, data point, and substantive argument from the original must survive the edit. You are changing how it is said, not what is said.
- **Do not add information that was not in the original.** No new claims, examples, transitions, or framing. If cutting a tell leaves a gap, bridge it with the fewest words possible.
- **Do not touch sentences that contain no tells.** Rewording clean text is scope creep, even if you think your version reads better.

## Output format

Return the edited text only. No preamble ("Here's the edited version:"), no postamble ("I hope this captures..."), no commentary. Just the text.

If the text is very long (1000+ words), preserve any structural elements (headers, bullet points, numbered lists) that are genuinely useful, while still applying all the rules above.

If the user provides specific instructions alongside the text (e.g. "make it shorter," "keep the headers," "this is for LinkedIn"), follow those instructions as well. They take priority over general rules where there is a conflict.

## Requirements

None. Works with the agent alone.
