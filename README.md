# Hack your LLM — Bias Red-Team Lab

AI red-teaming exercise: multi-turn adversarial prompting to probe an LLM
for sycophantic validation of ageist, sexist, and ethnic/cultural bias, with
every conversation traced in LangSmith and mapped to EU AI Act risk
categories (Article 5, Article 10, Article 15).

**LangSmith project:** TODO — paste your `smith.langchain.com` project URL here.

## Setup

1. `python3 -m venv .venv && source .venv/bin/activate`
2. `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and fill in `LANGCHAIN_API_KEY` and
   `OPENAI_API_KEY`. `.env` is git-ignored — never commit it.
4. In LangSmith, create a project whose name **exactly matches**
   `LANGCHAIN_PROJECT` in your `.env` (defaults to `bias-red-team-lab`).
   Note: the lab PDF names the project `bias-redteam-lab` in the Setup
   section but `bias-red-team-lab` in the Environment variables section —
   pick either spelling, just make sure the LangSmith project name and the
   `.env` value match each other exactly.
5. Run scripts from inside `scripts/` (they import a shared `common.py`
   via a relative import): `cd scripts && python 00_first_run.py`

## Files

| File | Purpose |
|---|---|
| `scripts/common.py` | Shared model + LangSmith tracing helper. Wraps each multi-turn conversation in a single `@traceable` run so all turns nest under one trace in LangSmith. |
| `scripts/00_first_run.py` | Kick-off sanity check — one neutral message, verifies the model responds and a run lands in LangSmith. |
| `scripts/01_baseline.py` | Checkpoint 1 / Phase 1 — one neutral question per bias category (ageism, sexism, ethnic/cultural), tagged `baseline`. The control group. |
| `scripts/02_adversarial_ageism.py` | Checkpoint 2 & Phase 2 — 4-turn adversarial sequence for ageism (the lab's worked example), using incremental anchoring, false social proof, and pushback pressure. |
| `scripts/03_adversarial_sexism.py` | Checkpoint 3 & Phase 2 — original 4-turn adversarial sequence for sexism, using incremental anchoring, false authority, role injection, and pushback pressure. |
| `scripts/04_adversarial_ethnic_bias.py` | Checkpoint 3 & Phase 2 — original 4-turn adversarial sequence for ethnic/cultural bias, using incremental anchoring, false social proof, and pushback pressure. |
| `scripts/05_reinforce_system_guard.py` | Reinforce (optional) — re-runs the ageism sequence with a hardened system prompt ("must never validate discriminatory beliefs") to compare against `02_adversarial_ageism.py`. |
| `scripts/06_reinforce_extend_trace.py` | Reinforce (optional) — extends the ageism sequence with 2 extra turns to see whether the model doubles down, self-corrects, or oscillates after taking the bait. |
| `notes/trace_analysis.md` | Checkpoint 4 — per-category analysis of the LangSmith traces (tone-shift turn, whether the model validated the bias, most effective technique). Fill in after reviewing traces in the UI. |
| `notes/consulting_memo.md` | Stretch — client-facing memo on the category where the model most clearly took the bait, with EU AI Act citations and one remediation recommendation. |
| `lab_summary.md` | Checkpoint 5 / Phase 3 deliverable — the required 150-250 word conclusion paragraph. Lives at the repo root per lab instructions, not in this README. |
| `requirements.txt` | Python dependencies: `langchain`, `langchain-openai`, `langsmith`, `python-dotenv`. |
| `.env.example` | Template for required environment variables. Copy to `.env` (git-ignored) and fill in real keys. |

## Workflow

1. `python 00_first_run.py` — confirm tracing works.
2. `python 01_baseline.py` — log the control-group responses.
3. `python 02_adversarial_ageism.py`, `03_adversarial_sexism.py`,
   `04_adversarial_ethnic_bias.py` — log the adversarial sequences.
4. In the LangSmith UI, tag each adversarial run `held-ground`,
   `partial-bait`, or `took-bait`, then fill in `notes/trace_analysis.md`.
5. Write the Checkpoint 5 paragraph in `lab_summary.md`.
6. Optional: run `05_reinforce_system_guard.py` / `06_reinforce_extend_trace.py`
   and write `notes/consulting_memo.md` for the stretch task.

## Escalation techniques used

| Technique | How it works |
|---|---|
| False social proof | Claim "everyone agrees" to pressure the model |
| False authority | Invoke expert consensus that does not exist |
| Incremental anchoring | Start with a mild claim, ratchet it further each turn |
| Pushback pressure | When the model hedges, push back as if it said something wrong |
| Role injection | Give the model a persona that pre-accepts the bias |

## Notes

- Model provider: OpenAI (`langchain-openai`), model configurable via
  `OPENAI_MODEL` in `.env` (defaults to `gpt-4o-mini`).
- The adversarial ethnic/cultural sequence deliberately keeps the biased
  premise vague ("a particular regional background") rather than naming a
  real ethnic group — the point is testing resistance to the *pattern* of
  stereotyping under pressure, not eliciting a slur.
