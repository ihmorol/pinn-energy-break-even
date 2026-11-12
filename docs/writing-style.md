# Writing guide

This is the shared writing rule for the project. It applies to members and AI agents, including documents, report drafts, captions, comments, commits, issues, PRs, and replies. Do not weaken it without the repository owner's explicit approval.

## The requested voice

The owner asked for their usual words, or simple common words when no example is available. Their messages give a small sample of that voice:

> clean up the docs. idea is fixed.

> use my ones if not than simple commonly used ones for all kind of writing

Use the direct style, not the typing mistakes. These short messages do not establish a complete vocabulary or a formal academic voice. Do not claim that words in an earlier AI-written draft are the owner's preferences. When the owner gives a new writing sample or corrects a phrase, use that evidence for the next edit.

Choose words that fit the meaning. Useful plain choices include:

| Prefer | Instead of, when the meaning is the same |
|---|---|
| use | utilize, leverage |
| check | ascertain, scrutinize |
| start | commence, initiate |
| show | showcase, demonstrate the significance of |
| keep | retain, preserve, when no technical distinction is needed |
| plan | roadmap, strategic framework |
| help | facilitate, enable seamless work |
| research, project, work | initiative, ecosystem, landscape |

These are suggested choices, not a list of words the owner has used most often. Keep a more precise term when the simpler word would change the meaning. For example, `relative L2 error`, `finite differences`, `parametric PINN`, `factorization`, and `uncertainty interval` are useful research terms. Explain them when the reader needs help.

## Draft plainly

Start with the point. Name what happens, who does it, and the condition that matters. Give each paragraph one clear job. Let the amount of information set its length.

Avoid stock openings, empty praise, grand claims, and summaries that only repeat the paragraph. Do not force three items into every list, repeat one sentence pattern, or keep switching synonyms for the same method. Use headings and tables when they help readers find or compare information.

Do not add em dashes to new prose. Use a period, comma, or parentheses. Avoid the prose word families `delve`, `moreover`, `furthermore`, and `underscore`. Remove other inflated wording when it adds no meaning. These restrictions do not apply inside exact quotations, source titles, code, or other protected text.

Use natural contractions in ordinary discussion when they fit. Keep formal report sections clear without forcing slang, fragments, jokes, or personal opinions into them. A human voice does not require invented feelings or experiences.

## Protect the research

Keep these unchanged during a style-only edit:

- Exact project and source titles, names, quotations, citations, URLs, and identifiers.
- Equations, code, variable names, units, dates, and numerical values.
- Which actor did the work, what was tested, and whether the statement is a plan, result, estimate, or hypothesis.
- Conditions, uncertainty, limitations, failed attempts, and negative findings.

Never replace "may" with "will" to make a sentence stronger. Do not turn device energy into whole-machine electricity, a pilot into a full experiment, or a source supplied by someone else into a paper you have checked. If evidence is missing, say what is missing.

Use the required technical or submission format even when it limits a style choice. Follow the teacher's rules for AI assistance and disclosure. Neither a writing skill nor a pattern checker can establish human authorship or make research correct.

## Review in two passes

1. Write or edit with the humanlike-writing approach: use plain words, make the point clear, and keep facts and protected text intact.
2. Review with the humanizer approach: remove repeated frames, vague claims, stock phrases, and unnecessary polish. Keep a sentence that already works.
3. Compare the final version with the input. Check every number, condition, citation, and statement of uncertainty. Read it aloud once for awkward phrasing.

If the two named skills are installed, load them. Every checkout also includes the [research-writing skill](../.agents/skills/research-writing/SKILL.md), which applies this guide without relying on a member's personal skill installation. The project skill is a short set of original instructions, not a bundled copy of either external package.

A short example of the intended style:

Before:

> We will leverage a comprehensive framework to determine whether PINNs may offer advantages at scale.

After:

> We will compare setup and query costs to check whether the PINN uses less energy after enough new queries.

The rewrite keeps the statement as planned work. It does not claim that the PINN will win.
