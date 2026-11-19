# Path B — RQ / Evidence Map

**Prepared:** 17 November 2026 · **Author:** Claude (Cowork session) · **Status:** audit of completed evidence. **Frozen RQ1–RQ3 preserved verbatim; no canonical artefact modified; no experiment run; no new RQ introduced.**

---

## 1. Frozen RQ1–RQ3 — exact wording

Quoted verbatim from `docs/analysis/final-research-chain-lock.md` §E. **These are the research questions. Nothing below replaces or paraphrases them.**

> **RQ1 — Operational specification.** Can AI participation and admissible advisory scope be specified as two separate state-conditioned functions over a classified multi-component environmental state such that classification remains total and the containment property is preserved when some conceptually required components are structurally unavailable — and which elements of that specification must be decided by the designer rather than derived from published sources?

> **RQ2 — Empirical characterisation and robustness.** Over a multi-year historical environmental record for the deployment site, how frequently does the intermediate safety state produce a stricter admissible recommendation set than a participation-only gate, and how sensitive is that frequency to defensible environmental-threshold and data configurations?

> **RQ3 — Structural warrant of the multi-component classifier.** Which components of the environmental state actually determine the intermediate classification at the deployment site, and is the multi-component structure warranted by the evaluated record?

**Not reintroduced** (lock §E, verbatim): *prototype implementation as an RQ; contextual fisher validation as a completed RQ; target-hardware latency as an RQ; Safety Dominance as an independent thesis-level RQ.*

---

## 2. Mathematical consequences versus empirical findings

This separation is the most consequential part of the audit, because the thesis's headline number sits on the boundary.

### 2.1 Mathematical consequences of the governance design — **not empirical findings**

| | Statement | Why it is a consequence, not a finding | Source |
|---|---|---|---|
| **M1** | **Δ_L2 ≡ P(S = CAUTION)** | `A_AI["C1"]` and `A_AI["C2"]` are identical at SAFE (FULL = FULL) and at UNSAFE (∅ = ∅), and differ only at CAUTION. Divergence is counted elementwise, so an hour contributes **iff** its state is CAUTION. Verified from the implementation, not the documentation, and re-verified on every configuration: *"IDENTITY HOLDS (difference < 1e-9)"* | lock §H; `threshold-sensitivity-analysis.md` §B |
| **M2** | Containment `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅` | Lock §N: *"Design property — true by definition of `A_AI`"* | lock §N |
| **M3** | **C1 ≡ C3** (participation-only ≡ Flehmig-style traffic light) | The two admissible-set tables are identical literals. Lock §N: *"the 0.00% replay value is harness consistency, not discovery"* | lock §N |
| **M4** | Totality under structural unavailability (P1) | Lock §N: *"Formalisation of an established mechanism"* | lock §N |
| **M5** | Safety Dominance `AI(E) ⊆ A_AI(S)` (P3) | Lock §N: *"Implementation / contract-conformance property under A1–A4"* | lock §N |
| **M6** | `g_t` contributes **0%** of CAUTION attribution | Lock §K: *"emits no CAUTION by construction"*. Definitional, not measured | lock §K |
| **M7** | `g_m` contributes **0%** | Structurally excluded by the declared exclusion `D = {m}` | lock §K |
| **M8** | The `Go`/`Delay` recommendation is identical under C1 and C2 at every hour | `RESTRICTED = {Go, Delay}` contains both, so the CAUTION filter removes only `DepartureTime` and `Duration`. Measured at 1.000000 in an exploratory run, but it follows from the mapping alone | `architecture-illustration.md` §209; exploratory `results-causal-replication.json` |

**The consequence that matters most for contribution framing: M1.** Because Δ_L2 is identically the CAUTION activation rate, **the headline number is a count of CAUTION states**. It is an empirical measurement of a frequency, but it is not a measurement of a *comparative* effect, and §6 of the companion assessment turns on this.

**M6 and M7 also matter**, because two of the five "0%" entries in the component-attribution table are definitional. The attribution result is therefore a finding about **three** components (`g_o`, `g_r`, `g_w`), not five.

### 2.2 Empirical findings — genuinely measured over the record

| | Finding | Value | RQ |
|---|---|---|---|
| **E1** | Intermediate-state activation rate in the departure window | **5.81%** PRIMARY (531/9,135) · **4.48%** RESOLUTION (266/5,935) | RQ2 |
| **E2** | State distribution | SAFE/CAUTION/UNSAFE = 51.31 / 5.81 / 42.88 (PRIMARY); 54.44 / 4.48 / 41.08 (RESOLUTION) | RQ2 |
| **E3** | **Sourced-threshold robustness envelope** | **5.67% – 9.56%** PRIMARY · 4.26% – 6.64% RESOLUTION | RQ2 |
| **E4** | **Wind is a structural zero** | Δ_L2 unchanged to 2 d.p. across `W_C` 18–25 kn; only two departure-window observations within ±2 kn of 21.6; max 21.80 kn PRIMARY / 19.30 kn RESOLUTION; binds in **zero** CAUTION hours | RQ2, RQ3 |
| **E5** | **Rainfall influence is minimal** | `R_C` 5.0 → 19.9 mm/hr moves Δ_L2 by **0.48 pts** PRIMARY / 0.78 RESOLUTION | RQ2 |
| **E6** | **Wave onset is dominant** | `O_C` is the principal determinant; `O_U` ≈ +0.2 pp per 0.05 m below 1.6 m, saturating above ~1.9 m. **The gradient figure is disputed across documents — see `path-b-essential-gaps.md` G1** | RQ2, RQ3 |
| **E7** | **Component attribution (negative result)** | `g_o` **518/531 = 97.6%** · `g_r` **13/531 = 2.4%** · `g_w` **0** (activates twice in 43,848 hours, decisive in neither) · zero ties. RESOLUTION: `g_o` 253, `g_r` 13 of 266 | **RQ3** |
| **E8** | **PRIMARY/RESOLUTION decomposition** | Wave-model effect **+1.97 pts** (period held constant); record-length effect **−0.64 pts** (model held constant); combined **1.33 pts**. **The two act in opposite directions** | RQ2 |
| **E9** | Configuration count | `threshold_sensitivity.py`: **78 executions over 56 unique configurations** | RQ2 |
| **E10** | *(Exploratory, this session — not canonical)* Independent-event clustering | 531 CAUTION hours → 201 distinct days → **85–123 independent weather events** over five years, at >3 d / >1 d separation | bounds RQ2's precision |
| **E11** | *(Exploratory, this session — not canonical)* Advisory-type reachability | Under concurrent-information procedures, `DepartureTime` produced at 0.00% and `Duration` as a deterministic function of the present observation, over 7,305 episodes | bears on RQ1's specification |

---

## 3. Experiment-to-RQ mapping

The lock's own §Q map is reproduced first, then audited.

### 3.1 The lock's map, verbatim

| RQ | Evidence | Result | Contribution | Limitation |
|---|---|---|---|---|
| **RQ1** | `appendix-c-formalisation.md`; P1–P3; `D = {m}` with lower-bound consequence; threshold provenance table | Totality and containment hold jointly under structural unavailability. Four boundaries sourced; three load-bearing choices researcher-defined | Operational specification (secondary) | **Answered by construction and proof, not measurement** |
| **RQ2** | Replay + `scripts/sensitivity/threshold_sensitivity.py` | Δ_L2 = 5.81% / 4.48%; envelope 5.67–9.56%; `O_C` dominant; wind structural zero; rainfall < 0.5 pp | **Empirical characterisation (primary)** | Single site; invariant to `A_AI(CAUTION)` content; no incident data |
| **RQ3** | Component attribution over the same replay | `g_o` 97.6%, `g_r` 2.4%, three components never bind | **Empirical characterisation (primary, negative)** | Site-specific; does not refute transferability |

Lock §Q also asserts: *"No RQ lacks evidence. No completed experiment lacks an RQ."*

### 3.2 Audit of that map

| | Audit point | Finding |
|---|---|---|
| **A1** | **RQ1 is answered without measurement, and the lock says so.** Every item in RQ1's evidence column is M2, M4 or M5 — design properties or formalisations of established mechanisms — plus the provenance table | **Confirmed.** RQ1 therefore contributes no empirical weight. Its substantive content is the *inventory of what had to be designer-decided*: four boundaries sourced, **three load-bearing choices researcher-defined** |
| **A2** | **RQ2's headline is M1, so the "comparative" framing overstates it.** RQ2 asks how often the intermediate state produces a *stricter set than a participation-only gate*. By M1 that question has a closed-form answer — `P(CAUTION)` — for *any* strict subset of FULL | **The measurement is of the classifier's state frequency, not of a governance effect.** Lock §I already concedes the result is *"invariant to `A_AI(CAUTION)` content"* |
| **A3** | **RQ2's robustness clause carries the weight the headline cannot.** E3, E4, E5, E8, E9 all answer *"how sensitive is that frequency"* and none is a restatement of M1 | **This is where RQ2's empirical substance actually sits** |
| **A4** | **RQ3 is the only RQ answered by a result that is neither definitional nor a frequency count** — and its answer is negative | **Confirmed**, with the correction from M6/M7: the finding concerns three non-definitional components, not five |
| **A5** | Does any completed analysis lack an RQ? | **One.** E8's common-period decomposition answers RQ2's data-configuration clause, and the lock maps it there — but it also *corrects a previously published interpretation* (lock §L: *"Do not repeat: 'the 1.33-point difference is the grid-resolution effect'"*). That corrective function is a methodological contribution with no RQ slot |
| **A6** | Does any RQ lack evidence? | **No**, as the lock states — provided RQ1 is accepted as answered by construction |

---

## 4. Completed analyses by category (Task 4)

| Category | Completed analyses | Status |
|---|---|---|
| **Intermediate-state activation** | Four-condition comparison C0/C1/C3/C2 over the departure window; state distributions; the Δ_L2 identity check at <1e-9 | **Complete.** Identity verified from implementation on every configuration |
| **Threshold sensitivity** | `threshold_sensitivity.py`: 78 executions, 56 unique configurations; per-component sweeps for `W_C` (18–25 kn), `R_C` (5.0–19.9 mm/hr), `O_C`/`O_U` across four vessel-class readings of Yaakob; sourced-threshold envelope | **Complete.** One figure disputed (G1) |
| **Component attribution** | `g_o` / `g_r` / `g_w` / `g_t` / `g_m` binding counts in CAUTION hours, both configurations, ties counted (zero) | **Complete.** Two of five entries definitional (M6, M7) |
| **Data resolution** | Common-period comparison over the shared 28,501 hours; two-way decomposition into wave-model and record-length effects | **Complete**, and corrective |
| **Robustness / provenance** | Threshold provenance table distinguishing externally supported, superseded-project, and researcher-defined perturbation values; vessel-class and time-policy limits (lock §M); prediction register with pre-registered predictions and refutations | **Complete** |
| **Formal conformance** | P1 totality, P2 containment, P3 Safety Dominance, P4 C1 ≡ C3 | **Complete**, and lock §N states *"None is presented as novel theory"* |

**Nothing in this inventory requires repetition.** No validity defect identified in `path-b-essential-gaps.md` is of a kind that re-running an experiment would fix; both are documentation defects.
