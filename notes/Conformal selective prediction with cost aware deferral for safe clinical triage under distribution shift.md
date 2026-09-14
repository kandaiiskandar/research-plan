# Literature Review Extraction (Reduced)
## Paper: Conformal selective prediction with cost aware deferral for safe clinical triage under distribution shift

---

## 1. Paper Identity

- **Full title:** Conformal selective prediction with cost aware deferral for safe clinical triage under distribution shift
- **Authors:** Hyun Kwon, Dae-Jin Kim
- **Year:** 2026
- **Venue:** Scientific Reports
- **Publisher:** Nature Portfolio
- **Volume / article:** Vol. 16, article 10016
- **DOI:** 10.1038/s41598-026-40637-w
- **Type:** Peer-reviewed journal article, empirical + methodological
- **Peer review:** Yes
- **Extraction category:** External evidence (family A comparator for the novelty defence)
- **Source class:** `ACCEPT_CONTEMPORARY` · `SOURCE_VALIDITY = PASS` · year ≥ 2023

**Disambiguation:** this is **Kwon & Kim (2026)**, not Kwon et al. (2025) — *Runtime Safety through Adaptive Shielding* — which is a different author and a different corpus entry.

---

## 2. Core Contribution

A selective-prediction framework for clinical triage that decides, per case, whether to issue a prediction or defer the case to a clinician, and that holds up under distribution shift.

- **Deferral rule:** a certainty threshold on calibrated posterior probabilities. A case defers when the maximum class probability falls below a threshold τ.
- **How τ is set:** to minimise an explicit expected clinical cost on a held-out calibration set. The cost function encodes asymmetric harm — false negatives 10.0, false positives 1.0, deferrals 2.0.
- **Conformal component:** split conformal prediction supplies finite-sample, distribution-free coverage guarantees under exchangeability, and constructs set-valued predictions for communicating uncertainty. The deferral decision itself uses the simpler threshold rule.
- **Distribution shift:** handled by importance-weighted conformal variants that reweight calibration scores toward the target distribution.
- **Evaluation:** PhysioNet 2019 sepsis challenge data, 2,155 patients, 7.0% prevalence, temporally separated test splits. Error reduction at 80% coverage of 49.6% in-distribution and 46.7% out-of-distribution. Coverage near the nominal 90% in-distribution, 87.3–88.2% under temporal shift. Expected calibration error 0.016 in-distribution, 0.030 out-of-distribution. Mondrian conformal prediction reduced the gender coverage gap to 1.4 percentage points.

---

## 3. Relevance to My Research

This is the contemporary peer-reviewed authority establishing **what the governed quantity is in family A** — selective prediction, abstention and deferral. The answer is participation, not scope.

The paper is explicit that the system determines whether to issue a prediction or defer the case, and that it does **not vary the types of recommendation** — only the participation decision itself.

### Mechanism coding

| Question | Finding |
|---|---|
| What is governed? | **Whether the model issues a prediction at all** for a given case |
| What causes the restriction? | Calibrated posterior probability below a cost-optimised threshold; conformal machinery for coverage and shift correction |
| Runtime or design-time? | Runtime, per case; τ calibrated offline |
| External state or AI-internal? | **AI-internal.** The trigger is the model's own calibrated confidence. Distribution shift is handled by reweighting calibration, not by classifying an external environmental state |
| AI participation changed? | **Yes — this is the mechanism** |
| Prediction availability changed? | Yes, per instance |
| Advisory content changed? | Only in that a deferred case yields no prediction |
| Recommendation **type** scope changed? | **No.** Recommendation types are not a governed quantity |
| Executable action space changed? | No |
| Human/AI authority changed? | No |
| Human final authority invariant? | **Yes.** Deferred cases route to human review without automatic override; the system supplies calibrated probabilities and prediction sets to support the clinician |
| Formal verification? | Statistical rather than logical: finite-sample distribution-free coverage under exchangeability |
| Empirical evaluation? | **Yes** — 2,155 patients, temporally separated splits, in- and out-of-distribution |

---

## 4. Use in the Architecture Argument — Scope and Limits

**What this paper CAN be cited for:**

- That in contemporary peer-reviewed selective prediction, the governed quantity is prediction participation at instance level, conditioned on the model's own calibrated confidence.
- That human final decision authority is preserved in this family — deferral routes to a human rather than transferring authority.
- That distribution shift in this family is handled by recalibration, not by classifying an external environmental state.
- As peer-reviewed evidence for the family A row of the novelty-defence matrix, replacing reliance on a preprint.

**What this paper CANNOT be cited for (overreach guard):**

- It provides **no** state-conditioned restriction of recommendation types, and must not be described as advisory-scope governance.
- Its guarantees are statistical coverage properties, not containment or monotonicity over an admissible set.
- Clinical triage on retrospective sepsis data; do not generalise its performance figures to any other domain.
- It does not address governance architecture, participation gating by environmental hazard, or graduated intermediate states.
- Do not use it to argue that abstention is always all-or-nothing at the level of a whole assessment — partial, per-item withholding also occurs in this family.

---

## 5. Positioning for This Research

Kwon and Kim (2026) formalise selective prediction for clinical triage as a cost-aware deferral rule over calibrated posterior probabilities, with split-conformal coverage guarantees and importance weighting for distribution shift, evaluated on 2,155 sepsis cases across temporally separated splits. The governed quantity is whether the model predicts for a given case; the types of recommendation it may offer are not conditioned, and the trigger is the model's own confidence rather than a classification of the operating environment. Clinician authority is preserved by routing deferred cases to human review. The family therefore governs participation where this project governs admissible advisory scope, and conditions on model-internal reliability where this project conditions on an externally classified environmental state.

---

## 6. Overall Relevance Score

### ⭐⭐⭐ Medium (novelty-defence evidence)

Peer-reviewed, contemporary, mechanistically explicit, and directly on the question the novelty audit needed answered for family A. It resolves what would otherwise have been an open corpus gap resting on a preprint. Not an architecture comparator and not part of the Chapter 2 core corpus.

---

## 7. Caveats

- Retrospective evaluation on a public challenge dataset; no deployment evidence.
- The conformal guarantee holds under exchangeability, which the temporal-shift experiments themselves stress; coverage degrades to 87.3–88.2% under shift.
- The cost weights (10.0 / 1.0 / 2.0) are stipulated, not derived from a clinical source — a limitation structurally similar to threshold-provenance concerns in this project, and worth noting rather than borrowing.
- Author-name collision with the existing corpus entry Kwon et al. (2025) on adaptive shielding. Use distinct citation keys.
