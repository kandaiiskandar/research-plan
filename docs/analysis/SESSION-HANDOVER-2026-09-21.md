# Agent Handover — PhD Research Status

**Date:** 2026-09-21
**Purpose:** Session checkpoint before pausing. Authored by the researcher; recorded here so it survives the session.
**Read this first when work resumes.**

---

## Status

| | |
|---|---|
| Research chain | **LOCKED** |
| Experiment set | **SUFFICIENT** |
| Canonical revision | **COMPLETE — consistent with the final research chain** |
| New experiment required | **NO** |
| Next major task | **JOURNAL 1 MANUSCRIPT V2** |

Do not reopen the research framing, novelty search, experiment design or RQs without new evidence, supervisor feedback, reviewer feedback, or an identified contradiction.

---

## Frozen position

**Mechanism novelty is conceded.** Prior work establishes state-conditioned advisory restriction, advisory-category inhibition, nested admissible sets, deterministic gating, graduated governance, multi-component runtime state, human final authority, fail-safe/degraded operation, totality over incomplete observations, conservative handling of unusable observations, and directional bounds from unmeasured variables. **Do not claim mechanism-level architecture novelty.**

**Contribution hierarchy.** Primary: empirical characterisation of graduated advisory-scope governance under multi-year environmental replay. Secondary: domain operationalisation for small-scale Malaysian coastal fisheries; operational specification separating `G(S)` from `A_AI(S)`. Supporting: formal contract-conformance analysis; reproducibility/provenance methodology. **Architecture composition must not be promoted above the empirical contribution.**

**Gap A (operationalisation, modest)** — established mechanisms from different domains were not found composed into one operational specification with `G(S)` and `A_AI(S)` separately specified over a classified multi-component environmental state for this human-facing low-resource DSS setting. Not a major architecture gap.

**Gap B (empirical, stronger)** — no characterisation identified of how often an intermediate advisory-scope state changes the admissible recommendation set relative to a participation-only gate over a multi-year environmental record. Supports the primary contribution.

---

## Research questions

**RQ1 — Operational specification.** Can AI participation and admissible advisory scope be specified as two separate state-conditioned functions over a classified multi-component environmental state such that classification remains total and the containment property is preserved when some conceptually required components are structurally unavailable — and which elements of that specification must be decided by the designer rather than derived from published sources?

**RQ2 — Empirical characterisation and robustness.** Over a multi-year historical environmental record for the deployment site, how frequently does the intermediate safety state produce a stricter admissible recommendation set than a participation-only gate, and how sensitive is that frequency to defensible environmental-threshold and data configurations?

**RQ3 — Structural warrant of the multi-component classifier.** Which components of the environmental state actually determine the intermediate classification at the deployment site, and is the multi-component structure warranted by the evaluated record?

**Removed / demoted — do not reintroduce.** RQ-J2 target-hardware latency → deferred deployment/prototype evaluation, not required for the contribution; do not run E5 merely because it was in the old plan. Old RQ5 fisher validation → future socio-technical validation, **not conducted**; never imply otherwise. RQ-J1 Safety Dominance → supporting formal contract-conformance property.

---

## The identity that governs all interpretation

$$\Delta_{L2} = P(S = \text{CAUTION})$$

C1 and C2 are identical at SAFE and UNSAFE and differ only at CAUTION. The experiment measures **how frequently the intermediate restriction is activated**. It does **not** measure whether `{Go, Delay}` is the correct restriction — any strict subset of FULL at CAUTION gives the same value. **This limitation must never be lost in future writing.**

---

## Results

| | PRIMARY | RESOLUTION |
|---|---|---|
| Records | 43,848 | 28,501 |
| Departure-window denominator | 9,135 | 5,935 |
| Δ_L2 | **5.81%** | **4.48%** |
| Sourced-threshold envelope, small vessel | **5.67 – 9.56%** | 4.26 – 6.64% |

Describe as **sensitive but still informative**. Never present 5.81% as a universal or stable site property.

**Sensitivity.** Wind: structural zero. Rainfall: minimal — the non-MET 10 mm/hr boundary is **not** driving the headline. Wave: dominant, `O_C` ≈ **−1.4 pp per 0.05 m**, descriptive not causal.

**Component attribution** (PRIMARY, 531 CAUTION hours): `g_o` 518/531 = **97.6%**; `g_r` 13/531 = 2.4%; `g_w`, `g_t` zero binding; `g_m` structurally excluded; zero ties. *The five-component state remains defensible as a transferable specification, but the evaluated record does not empirically warrant equal importance of all five components at this site.* Negative result — do not hide it. F-7 (binding across all states) and this table (CAUTION-specific, departure window) do **not** contradict each other.

**PRIMARY vs RESOLUTION.** Not purely grid resolution. Wave-model effect +1.97 pts (period held constant); record-length effect −0.64 pts; net 1.33 pts. Opposite directions. ISSUE-1 **RESOLVED**.

**Vessel class.** Medium 1.96%, large 1.26% (PRIMARY). Approaching vacuity for larger classes. Do not generalise beyond small vessels (< 10 GRT).

**Time policy.** `night ⇒ UNSAFE` is researcher-defined. COLREGs Rule 20(b) supports the sunrise/sunset navigation-light boundary, not a claim that night fishing is unsafe. Daylight-only denominator gives 9.59% / 7.40%.

**Governance contract.** `A_AI(CAUTION) = {Go, Delay}` is researcher-defined with a domain rationale from Gao (2024) and Rahim et al. (2024). **Not** empirically validated, optimal, safer, or shown to improve decisions.

**Formal properties.** Totality = formalisation of an established mechanism. Containment = design property. Safety Dominance = implementation/contract-conformance. C1 ≡ C3 = supporting structural proof. **None is novel theory.**

---

## Explicit non-claims

Accident reduction · improved safety outcomes · improved fisher decision quality · classification accuracy · optimal thresholds · optimal number of states · optimal `{Go, Delay}` · generalisation across Sabah · generalisation across vessel classes · AI prediction accuracy · causal effectiveness · novel fail-safe mechanism · novel state-gating mechanism · novel totality mechanism · novel advisory-inhibition mechanism.

---

## Open items — none blocking

| Item | Status |
|---|---|
| `RESOLUTION_PAIRWISE_C0_C1_C0_C2` | PROVENANCE_INCOMPLETE — withhold; do not invent |
| Exclusion sensitivity `D ∈ {{m},{m,r},{m,o}}` | STRENGTHENING only. **Do not run `{m,w}`** — `g_w` never binds |
| Advisory-content ablation | FUTURE WORK — current metric cannot evaluate `{Go, Delay}`; needs Layer 3 and an outcome metric |
| `ageᵢ` freshness parameter | OPEN — do not invent a value |
| Journal 1 v1 submitted manuscript | Retains the old PRIMARY/RESOLUTION interpretation **by design**. Correct in v2; never edit the submitted artefact |

---

## Next task — Journal 1 Manuscript V2

Do not start without researcher approval. Do not patch isolated paragraphs — the paper must tell one coherent story.

Sequence: read the lock, the revision report and the revised canonical report → compare against submitted v1 → create a **new** revision (v1 untouched) → replace architecture-novelty framing → install Gap A/B, RQ1–RQ3, the Δ_L2 identity, threshold sensitivity, component attribution → correct PRIMARY vs RESOLUTION → add vessel-class and time-policy limitations → update the contribution hierarchy → preserve the explicit non-claims → keep every statement inside the available evidence.

**After v2:** structure the thesis on the same locked chain — Ch1 introduction/gaps/RQs/contributions · Ch2 literature, concession-first · Ch3 methodology and evaluation design · Ch4 architecture/operational specification · Ch5 formalisation and implementation · Ch6 replay, sensitivity, attribution, results · Ch7 discussion, limitations, contributions, future work. Adjust later to UMS requirements.

---

## Authority order when resuming

1. `docs/analysis/final-research-chain-lock.md` — **wins on research framing**
2. `docs/analysis/canonical-revision-report.md`
3. `docs/analysis/experiment-report-delta-l2.md` — **wins on current canonical wording**
4. `docs/analysis/rq-finalisation.md`
5. `docs/analysis/threshold-sensitivity-analysis.md`

For historical traceability, preserve the historical document rather than silently rewriting it.

**On restart:** report locked status, last completed task, remaining non-blocking open items, and the proposed next task. Wait for approval before beginning a large revision.
