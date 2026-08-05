# Literature Review Extraction
## Paper: Quantifying uncert-AI-nty: Testing the accuracy of LLMs' confidence judgments

---

## 1. Paper Identity

- **Full title:** Quantifying uncert-AI-nty: Testing the accuracy of LLMs' confidence judgments
- **Authors:** Trent N. Cash, Daniel M. Oppenheimer, Sara Christie, Mira Devgan
- **Affiliations:** Carnegie Mellon University (USA)
- **Year:** 2025
- **Venue:** Memory & Cognition, 54, 375–400 (Springer / Psychonomic Society)
- **DOI:** https://doi.org/10.3758/s13421-025-01755-4
- **Accepted:** 17 June 2025 | **Published online:** 22 July 2025
- **Open access:** Yes — CC BY 4.0; preregistered (AsPredicted, Studies 3–5)
- **Type:** Empirical cognitive psychology — five behavioural studies comparing LLM and human confidence judgments
- **Models tested:** ChatGPT-4, Bard/Gemini (1.5 Flash), Claude Sonnet, Claude Haiku (LLM data collected May–June 2024)
- **Domains:** Aleatory uncertainty — NFL predictions (Study 1, n=502), Oscar predictions (Study 2, n=109); epistemic uncertainty — Pictionary (Study 3, n=164), trivia (Study 4, n=110), university life questions (Study 5, n=110)
- **Extraction category:** External evidence (metacognitive limits of LLM self-assessment — not a governance corpus paper)

---

## 2. Core Contribution

- **Research problem:** LLMs readily produce confidence judgments, but their metacognitive accuracy (absolute calibration and relative discrimination) had not been systematically compared with humans across uncertainty types.
- **Key findings:**
  - **Mixed calibration, no across-the-board verdict:** accuracy varied by domain and model. Of 24 absolute-accuracy comparisons, LLMs beat humans 13 times, tied 4, lost 7. Of 28 relative-accuracy comparisons, LLMs were better 10 times, equal 14, worse 4.
  - **Systematic overconfidence:** LLMs, like humans, were largely overconfident — and may be *more consistently* overconfident than humans retrospectively.
  - **The headline metacognitive limitation — no learning from experience:** humans improved calibration after completing a task (retrospective better than prospective). ChatGPT and Gemini tended to do the opposite — retrospective errors *larger* than prospective, i.e. actively becoming less well-calibrated after performing. This insensitivity to own performance supports the hypothesis that LLMs lack access to **mnemonic cues** — internal experiential signals (fluency, effort, discomfort) that ground human metacognition. Haiku was the exception (consistently improved); Sonnet was mixed.

**Key quote (Abstract):** *"Unlike humans, LLMs—especially ChatGPT and Gemini—often fail to adjust their confidence judgments based on past performance, highlighting a key metacognitive limitation."*

**Key quote (General discussion):** LLMs' *"insensitivity to performance (i.e., lack of learning) suggests that LLMs do not have the capacity to learn from their own experience—supporting the hypothesis that LLMs do not have access to mnemonic metacognitive cues."*

---

## 3. Relevance to My Research

| Theme | Addressed? | How it relates |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | No | Behavioural study of LLM outputs only |
| Safety-critical AI decision-making | **Partial** | Not a safety domain (sports, trivia, Pictionary), but directly evidences why LLM self-assessed confidence cannot carry a safety case |
| AI governance / control mechanisms | No | No governance mechanism proposed or tested |
| Pre-generation advisory scope restriction | No | Not discussed |
| Environmental state classification | No | No state-conditioned behaviour |
| Low-resource environments | No | Not discussed |
| Decision architecture formalisation | No | Psychometric methods (calibration error, AUROC), not architecture |
| Human role in AI-assisted decision-making | **Partial** | Human–LLM comparison of confidence; relevant to why the human decision-maker must not rely on AI self-reported certainty |
| Maritime / fisheries domain | No | General prediction/knowledge tasks |

**Mid-Extraction Relevance Gate:** 0 Yes + 2 Partial → **EXTERNAL EVIDENCE** (reduced extraction; strongest of the three mechanistic external-evidence sources — peer-reviewed, preregistered, multi-model)

---

## 4. The Metacognitive Findings in Detail

- **Calibration is domain- and model-contingent.** No model was reliably well-calibrated across the five domains; the same model could be better than humans in one domain and worse in another. This unpredictability is itself the safety-relevant result: there is no domain-general guarantee that an LLM knows when it is likely wrong.
- **Overconfidence is the default direction of error.** ChatGPT, Gemini, and Haiku were prospectively overconfident in every instance tested (Studies 3–5); Sonnet was the lone underconfident exception. In a departure-decision context, overconfidence is the dangerous direction.
- **No experiential recalibration.** The prospective→retrospective comparison is the paper's sharpest instrument: having just performed the task provides humans with mnemonic cues that improve their self-assessment; ChatGPT and Gemini got *worse*. The authors attribute this to the absence of experiential internal signals in LLMs — Koriat's third cue class (mnemonic) is structurally unavailable to them.
- **Model heterogeneity.** Haiku consistently improved retrospectively and both Claude models had consistently better absolute accuracy than humans — so the limitation is not uniform across models, and claims must be model-qualified.

---

## 5. Use in the Architecture Argument — Scope and Limits

**What this paper CAN be cited for:**

- Peer-reviewed evidence that LLM self-assessed confidence is unreliable in a way that is **unpredictable across domains and models**, and biased toward **overconfidence**. A safety-critical system therefore cannot delegate risk sensitivity to the model's own uncertainty estimates — the model cannot be trusted to recognise, and flag, the conditions under which its advice should narrow.
- Evidence that LLMs (ChatGPT, Gemini) do not recalibrate from their own performance — so even repeated deployment does not converge toward trustworthy self-assessment. Caution cannot be expected to *emerge* with experience; it must be imposed.
- The third leg of the external mechanistic evidence set: Kamath et al. (2025) [[notes]](../notes/POD-Attention-%20Unlocking%20Full%20Prefill-Decode%20Overlap%20for%20Faster%20LLM%20Inference.md) — the serving pipeline is fixed and semantics-blind; Wu et al. (2025) [[notes]](../notes/LLMs%20are%20Single-threaded%20Reasoners-%20Demystifying%20the%20Working%20Mechanism%20of%20Soft%20Thinking.md) — reasoning exploration is decoding-mechanical, not risk-adaptive; Cash et al. (2025) — self-assessment of uncertainty is miscalibrated and non-learning. Together: neither the pipeline, the reasoning process, nor the model's self-knowledge provides a hook for risk-conditioned self-restriction — the structural case for an external governance pair (G(S), A_AI(S)).

**What this paper CANNOT be cited for (overreach guard):**

- It does **not** "prove that LLMs lack metacognition." The paper's own headline is more nuanced: LLM confidence judgments were *as accurate or more accurate than humans'* in a majority of comparisons. The demonstrated deficit is specific — failure to *update* calibration from task experience (and even that excepts Haiku).
- It does **not** show "the model has no internal mechanism for adjusting its output when uncertain." Verbalised confidence and output behaviour are different things; the paper measures stated confidence, not generation dynamics.
- It says nothing about **deteriorating environmental conditions** — the uncertainty domains are sports, awards, drawings, and trivia. The bridge from "poor metacognitive updating" to "cannot adapt advice to environmental risk" is *our* architectural argument; the citation supports the premise (unreliable, non-learning self-assessment), not the conclusion.
- Models tested are early-2024 vintage (ChatGPT-4, Gemini 1.5 Flash); results are model-heterogeneous (Haiku counter-trend). Avoid categorical "LLMs cannot X" phrasing — use "cannot be relied upon to X."

---

## 6. Formal Model and Mathematical Representation

- **Formal model:** Psychometric — calibration error (absolute accuracy), AUROC / Type-2 ROC (relative accuracy), prospective vs. retrospective judgment comparison. Nothing relating to governance, states, or admissible action spaces.
- **Comparison to (G(S), A_AI(S)):** No comparison possible. The paper measures a property of the AI component that the governance architecture is designed *not to depend on* — it motivates why S = f(E) is computed by a deterministic external layer rather than derived from AI self-confidence.
- **Safety Dominance Property:** Not defined, not applicable.

---

## 7. Positioning for This Research

**Positioning paragraph:** Cash et al. (2025), in five preregistered studies comparing four LLMs with human participants across aleatory and epistemic uncertainty domains, find that LLM confidence judgments are unpredictably calibrated across domains and models, biased toward overconfidence, and — for ChatGPT and Gemini — insensitive to the models' own past performance: unlike humans, these models failed to improve their calibration after completing a task, which the authors attribute to LLMs' lack of mnemonic metacognitive cues. For a safety-critical advisory architecture, the implication is that risk sensitivity cannot be delegated to the AI component's self-assessed uncertainty: the model cannot be relied upon to recognise the conditions under which its advice should narrow, and repeated operation does not make its self-assessment more trustworthy. The proposed architecture therefore derives the safety state S = f(E) from a deterministic external classification of environmental conditions, and enforces advisory scope through the governance pair (G(S), A_AI(S)) — placing the caution mechanism entirely outside the AI component whose self-knowledge this literature shows to be unreliable.

---

## 8. Overall Relevance Score

### ⭐⭐ Low–Medium (external evidence)

**Justification:** Outside the governance and fisheries literatures, but the strongest of the three external mechanistic sources: peer-reviewed, preregistered, multi-model, multi-domain, and directly on point for one architectural design decision — why S is computed by an external deterministic layer rather than inferred from AI self-confidence. Cite in `justification-ai-necessity` and the mechanistic subsection of the gap discussion, always model-qualified ("cannot be relied upon to"), never as a categorical impossibility claim. Its two Partial themes (safety-relevant self-assessment; human reliance on AI confidence) also make it usable in the RQ5 discussion of fisher trust in AI output.
