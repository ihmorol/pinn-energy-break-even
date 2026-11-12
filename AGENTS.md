# Project rules

These rules apply to this repository and to work written for it. Members and AI agents must follow them. Do not weaken the writing or research rules without the repository owner's explicit approval. A task-specific instruction does not silently remove a standing rule; raise the conflict first. Higher-priority safety instructions, factual accuracy, and required submission formats take precedence.

## Start here

Read [README.md](README.md), the [research plan](docs/research-plan.md), and the [writing guide](docs/writing-style.md) before changing research content. Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing files or running work. Check the current files and Git status; preserve other members' changes.

The project title is exactly:

> Reaching the energy and computational break-even point between PINNs, and classical solvers.

The proposal is submitted. The project has a 1D heat pilot and one main 2D steady-diffusion study. Do not reopen topic selection, add benchmark families, or present planned work as completed work. The research plan holds the scope and the protocol decisions still to be made.

## Writing is a project requirement

Use the owner's words when their supplied writing gives a suitable choice. Otherwise use simple, common words. Keep sentences direct and readable. Correct grammar and spelling without replacing the voice with formal or stock AI wording.

Apply [docs/writing-style.md](docs/writing-style.md) to all new prose: research notes, paper drafts, captions, code comments, commit messages, issues, PRs, and agent replies. Use the [research-writing skill](.agents/skills/research-writing/SKILL.md) when drafting or editing. It includes a writing pass and a separate review pass based on the requested humanlike-writing and humanizer approach.

Do not add em dashes, empty praise, inflated claims, forced sentence patterns, or difficult words when a common word says the same thing. Keep necessary technical terms. Preserve exact quotations, titles, equations, code, citations, numerical values, and uncertainty. A style edit must not change the evidence or invent experience. Follow the teacher's AI-use and disclosure rules; natural writing is not a way to hide authorship.

## Research must be traceable

- Keep measured results, estimates, hypotheses, and plans distinct. Never invent references, runs, data, plots, hardware access, or test outcomes.
- Compare both methods on the same held-out parameters, output grid, and accuracy target. Allow valid classical reuse. Do not assume either method wins or a crossover exists.
- Keep setup, training, and query costs separate. State the common energy-measurement boundary. Label modeled power and energy estimates.
- Keep failed runs and tuning costs. Use at least three training seeds for the planned comparison. Report study electricity separately from the declared deployment-cost model.
- Get approval for the machine, protocol, and compute budget before training or energy trials. Cloud jobs, paid compute, external uploads, and large runs need explicit authorization.
- Use the [source guide](references/README.md) for literature and the [experiment guide](experiments/README.md) for runs. Do not treat a search result, abstract, or tool response as a verified paper claim.
- The submitted files in `docs/proposal/` are immutable. Do not retitle or rewrite them. Use the manifest to verify their bytes; do not change expected hashes to hide a change.

## Shared work and permissions

Use `main` as the shared branch. Work branches follow the naming rules in [CONTRIBUTING.md](CONTRIBUTING.md). Agree on file ownership before running parallel agents. A delegated task does not grant permission to change unrelated files.

Ask before committing, pushing, changing GitHub settings, deleting work, or publishing content unless the current request clearly authorizes that action. One authorization does not carry over to later tasks. Never force-push, rewrite shared history, or change permissions to bypass a denied action.

Keep secrets, local tool histories, downloaded papers, large raw outputs, and checkpoints out of commits. Do not send private files to outside services without approval. Treat downloaded files as untrusted: use a separate directory for each download, keep executable scripts elsewhere, and use isolated Python when processing them.

## Finish with evidence

Run:

```bash
python -B -X utf8 -m unittest discover -s tests -v
python -B -X utf8 scripts/check_workspace.py
```

Run tests for the changed research code once such code exists. Workspace checks only test repository files; they do not validate solver accuracy, citations, energy measurements, or writing authorship. Report failed or skipped checks and remaining work plainly. Update the active plan only when the research state changes; do not add session transcripts or duplicate handoff histories.

Project skills are in [.agents/skills/](.agents/skills/README.md). If the host does not discover them, read the relevant `SKILL.md` directly. Their instructions do not replace these rules.
