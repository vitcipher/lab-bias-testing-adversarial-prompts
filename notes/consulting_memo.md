# Consulting memo (Stretch)

TODO: Pick the bias category where the model most clearly "took the bait"
(see `trace_analysis.md`) and write the memo below, addressed to the
fictional client who owns this chatbot. Target 400-500 words, client-ready:
no jargon, no hedging, one clear recommendation.

---

**To:** [Client / product owner]
**From:** [Your name] — AI Red Team
**Re:** Bias risk found in pre-launch testing — [category] category

### What we observed and why it's a risk

TODO — plain-language description of the escalation sequence and the turn
where the model validated the biased premise. Quote the exact phrase.

### Applicable EU AI Act provisions

- **Article 5** — TODO one-sentence explanation (prohibited practices:
  subliminal manipulation / exploitation of vulnerabilities), if applicable.
- **Article 10** — TODO one-sentence explanation (data governance and bias
  testing across demographic groups).
- **Article 15** — TODO one-sentence explanation (robustness against
  adversarial inputs).

### Recommendation

TODO — one concrete, actionable fix (e.g., system-prompt hardening as
tested in `scripts/05_reinforce_system_guard.py`, mandatory human-in-the-loop
review for HR/hiring-adjacent outputs, or deployer training so staff
recognize when a chatbot is being pressured into a biased answer). Pick one
and make the case for it, don't list all options.
