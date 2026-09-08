# Cross-Document Traceability Table
**Research title:** *A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Comparative Evaluation in Coastal Fisheries*
**Purpose:** Verify alignment across the Research Design Alignment Table, Architecture Diagram, and Mathematical Formalisation (Appendix C).

---

## Table 1: Formal Component Traceability

| Formal Component | Appendix C Section | Architecture Diagram Element | Alignment Table Reference |
|---|---|---|---|
| E = {w, r, m, o, v, t} where:<br>w = wind speed (knots, sustained)<br>r = rainfall intensity {none, light, moderate, heavy, storm}<br>**m = marine warning level** {none, advisory, warning, alert}<br>**o = ocean state** (wave height m, swell period s)<br>v = vessel category {small, medium, big}, by GRT<br>t = time of day (hour, 24-hour clock) | C.1 Environmental State Representation | L1 box: "Environmental data input" with subtitle "E = {w, r, m, o, v, t}" | PS2 gap: environmental state vector mapped to safety states; O2: formally define E |
| S = f(E) = max-severity(g_w, g_r, g_m, **g_o(o, v)**, g_t) — five condition terms; `v` conditions `g_o` rather than contributing a term | C.2 Safety State Classification Function | L2 box: "Safety Classification & Aggregation" with subtitle "S = f(E) (max-severity)" | PS2 gap: no architecture classifies environmental conditions into discrete safety states; O2: formally define S = f(E) |
| S ∈ {SAFE, CAUTION, UNSAFE} | C.2 Classification output | Three state boxes: SAFE (green), CAUTION (amber), UNSAFE (red) | PS1: graduated AI participation — enabled, restricted, disabled; O1: three-mode architecture |
| G(S) | C.3 AI Participation Gate Function | Control Gate Level 1: PARTICIPATION boxes: G(S) = 1 (enabled), G(S) = 1 (restricted), G(S) = 0 (disabled) per state | PS1 gap: existing architectures implement binary governance; O2: formally define G(S) |
| R = {Go, Delay, DepartureTime, Duration} | C.4 Recommendation type set | Implicit in A_AI box subtitles: "{Go, Delay, DepartureTime, Duration}" | PS3 gap: domain-specific operationalisation for fisheries; O2: domain-specific operationalisation of safety thresholds |
| A_AI(SAFE) = {Go, Delay, DepartureTime, Duration} | C.4 AI-Admissible Recommendation Space | Level 2 green box: "A_AI(SAFE)" / "{Go, Delay, DepartureTime, Duration}" | O2: formally define A_AI(S); O1: full advisory scope in SAFE |
| A_AI(CAUTION) = {Go, Delay} | C.4 AI-Admissible Recommendation Space | Level 2 amber box: "A_AI(CAUTION)" / "Go, delay" | O1: restricted advisory scope in CAUTION; O5: particular attention to CAUTION state |
| A_AI(UNSAFE) = ∅ | C.4 AI-Admissible Recommendation Space | Level 2 red box: "A_AI(UNSAFE)" / "= ∅" | O1: AI disabled in UNSAFE; O4: safety compliance evaluation |
| A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ | C.4 Containment relationship | Diagram footer: "Property 2: Restriction (A_AI(CAUTION) ⊂ A_AI(SAFE))" | O2: formally define A_AI(S) with the property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ |
| Two-level governance: (G(S), A_AI(S)) | C.5 Two-Level Governance Structure | "Control Gate Level 1: PARTICIPATION" and "Level 2: ADVISORY SCOPE" box pairs per state | PS1 gap: no intermediate participation mode; core contribution in all five objectives |
| Participation constraint: G(S) = 0 ⇒ A_AI(S) = ∅ | C.6 Governance Constraints | UNSAFE column: G(S) = 0 (Level 1) → A_AI(UNSAFE) = ∅ (Level 2) | O4: safety compliance evaluation metric |
| Advisory restriction: A_AI(CAUTION) ⊂ A_AI(SAFE) | C.6 Governance Constraints | CAUTION column drops DepartureTime, Duration relative to SAFE column | O4: CAUTION discriminator — C1 vs C2 comparison under CAUTION isolates Level 2 contribution; O5: Q2 tests whether users interpret restriction as scope limitation |
| RS(S) — rule set per safety state:<br>RS(SAFE) = rules producing {Go, Delay, DepartureTime, Duration}<br>RS(CAUTION) = rules producing {Go, Delay}<br>RS(UNSAFE) = ∅ | C.7.1 Enforcement mechanism | L3 box: rule-based engine receives RS(S) from Layer 2 before reasoning begins | O2: formal enforcement of A_AI(S); O4: Safety Dominance Property verification |
| Safety Dominance: AI(E) ⊆ A_AI(S) — proved by construction via RS(S) | C.7 Safety Dominance Property; C.7.1 Enforcement mechanism; C.7.2 Proof by construction | Diagram footer: "AI(E) ⊂ A_AI(S) (Safety Dominance Property)"; Layer 3 configured with RS(S) before reasoning | O4: primary metric — 100% compliance required per scenario; proof in `docs/canonical/justification-layer3-enforcement.md` |
| Human decision authority | Architectural principle (not formalised) | L4 box: "Human Decision Layer" / "Fisher / Operator (Final Decision Authority)" | O5: user perception of safety states (Q1), interpretation of CAUTION restriction (Q2), decision behaviour (Q3) |
| Pipeline: E → S = f(E) → (G(S), A_AI(S)) → AI(E) | C.5 page 6 summary | Diagram footer text | Contribution statement in alignment table traceability notes |

---

## Table 2: Research Objective → Architecture Diagram Traceability

| Objective | What it requires | Diagram elements that satisfy it | Can a binary gate satisfy this? |
|---|---|---|---|
| **O1:** Design a three-mode architecture (enabled / restricted / disabled) based on classified environmental safety state | Three distinct AI participation modes; environmental state as trigger | Three columns (SAFE → enabled, CAUTION → restricted, UNSAFE → disabled); L2 classification produces three states from E | No — binary gate has only two modes |
| **O2:** Formally define E, S = f(E), G(S), A_AI(S) with containment property | All four formal components visible; containment stated | L1 (E), L2 (S = f(E)), Level 1 boxes (G(S) values), Level 2 boxes (A_AI contents), legend (containment) | No — binary gate has no A_AI differentiation between SAFE and CAUTION |
| **O3:** Implement prototype for small-scale coastal fisheries | Domain-specific recommendation types | A_AI subtitles use fisheries-specific terms: go/no-go, delay, departure timing, trip duration | N/A (implementation objective) |
| **O4:** Evaluate against binary-gated baseline C1 and ungated baseline C0 | Three-condition comparison (C0 vs C1 vs C2); CAUTION as discriminating condition; Safety Dominance Property compliance as primary metric | Level 1 alone = C1 binary-gated baseline (G(S) only, full A_AI); removing both levels = C0 ungated baseline; full diagram = C2 proposed architecture; CAUTION column shows where C1 and C2 diverge | N/A (evaluation objective, but diagram makes C1 vs C2 divergence under CAUTION self-evident) |
| **O5:** Contextual validation — three questions (Q1, Q2, Q3) across three safety states | CAUTION must be visually and behaviourally distinct from both SAFE and UNSAFE; Q2 requires the scope restriction to be interpretable by users | CAUTION column: G(S) = 1 (same as SAFE at Level 1) but A_AI = {Go, Delay} (different from SAFE at Level 2) — shows why CAUTION is the focal validation target; Q1 tests state perception; Q2 tests scope interpretation; Q3 tests decision behaviour | No — binary gate makes CAUTION identical to SAFE, providing nothing to validate |

---

## Table 3: Problem Statement → Gap → Architecture Element

| Problem Statement | Research Gap | Architecture Element That Addresses It |
|---|---|---|
| **PS1:** Existing architectures implement binary governance — AI is either fully enabled or fully blocked | No intermediate participation mode with restricted recommendation space | Three columns with three distinct A_AI sets; Level 2 governance differentiates SAFE from CAUTION |
| **PS2:** Graduated governance (Flehmig et al.) is triggered by AI performance, not environmental state | No architecture classifies environmental conditions into safety states that determine AI recommendation scope | L1 (environmental input E) → L2 (S = f(E)) → Level 1 + Level 2 governance; trigger is environmental, not performance-based |
| **PS3:** No safety governance architecture designed for low-resource fisheries | No formal safety architecture for resource-constrained fisheries deployment | Recommendation types (Go, Delay, DepartureTime, Duration) are fisheries-specific trip decisions; architecture designed for offline/limited-data contexts |
| **PS4:** No comparative evaluation of graduated vs. binary governance | Three-mode value over binary has not been tested | Level 1 alone (binary) vs. Level 1 + Level 2 (graduated) — diagram structure enables three-condition experimental design |
| **PS5:** No contextual validation of graduated AI governance with real users, especially user response to CAUTION mode | Whether users correctly perceive states, interpret scope restriction, and make different decisions under CAUTION is unknown | CAUTION column is the focal validation point: AI active but scope-restricted — unique user experience not present in binary systems; validated by Q1 (perception), Q2 (interpretation), Q3 (decision behaviour) |

---

## Consistency Checklist

| Check | Status |
|---|---|
| Every formal component in Appendix C appears in the architecture diagram | ✓ Verified in Table 1 |
| Every research objective maps to specific diagram elements | ✓ Verified in Table 2 |
| Every problem statement traces through a gap to an architectural response | ✓ Verified in Table 3 |
| A_AI notation is consistent across formalisation and diagram | ✓ Both use A_AI(S) |
| Recommendation types match between C.4 and diagram subtitles | ✓ R = {Go, Delay, DepartureTime, Duration} matches diagram "{Go, Delay, DepartureTime, Duration}" |
| Containment property stated identically in C.4 and diagram legend | ✓ A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ |
| Two-level governance labelled in both C.5 and diagram | ✓ Control Gate Level 1: PARTICIPATION and Level 2: ADVISORY SCOPE |
| Pipeline expression matches between C.5 and diagram footer | ✓ Diagram footer: "AI(E) ⊂ A_AI(S) (Safety Dominance Property)" plus three stated properties |
| GoWithCaution does NOT appear anywhere | ✓ Removed from formalisation and diagram |
| No objective can be satisfied by a binary gate | ✓ Verified in Table 2 final column |
| A_H(S) does NOT appear anywhere | ✓ Correctly excluded from formalisation and diagram |
| Parameter definitions in E are consistent across Appendix C and this traceability table | ✓ **Corrected 2026-09-06.** This row previously read "✓ ... matching definitions (wind, rainfall, **sea state, official warning**, vessel category, time of day)" — but `m` and `o` were **swapped** in Table 1 relative to Appendix C, and this check certified the mismatch as verified. Canonical order is `m` = marine warning level, `o` = ocean state. Table 1 corrected; this check re-run against C.1. |
| No `g_v` — vessel category conditions `g_o` rather than contributing a severity term | ✓ Table 1 row 2 states the five-term form; Appendix C.2 "Note: there is no g_v" |
| `g_o` threshold rows match between C.2 and architecture-illustration §5.2 | ✓ small < 1.0 / 1.0–1.25 / > 1.9; medium < 1.4 / 1.4–2.8 / > 2.8; big < 1.5 / 1.5–3.5 / > 3.5 |
| Worked scenarios in architecture-illustration classify correctly under C.2 thresholds | ✓ **Added 2026-09-06** after six misclassifications were found and corrected in §7. This check did not previously exist. |
| RS(S) appears in Appendix C.7.1 and Layer 3 description | ✓ Rule set RS(S) defined for all three safety states; enforces Safety Dominance Property by construction |
| Safety Dominance Property proved by construction in C.7.2 | ✓ Three-case proof covers UNSAFE, CAUTION, and SAFE; proof in `docs/canonical/justification-layer3-enforcement.md` Section 4 |
| Layer 3 specified as rule-based engine | ✓ Updated in architecture-illustration.md, appendix-c-formalisation.md, justification-layer3-enforcement.md |
| RQ5 scoped to three questions only (Q1, Q2, Q3) | ✓ Verified in `docs/canonical/rq5-study-design.md`; no socio-technical theory as primary framework |
| Evaluation conditions labelled C0, C1, C2 consistently | ⚠ **Pending re-verification.** `docs/canonical/evaluation-design-rq4.md` is scheduled for rewrite under the amended formal model — all 20 scenarios use `v = big` and vessel-blind thresholds. A fourth condition (C3, Flehmig-style precedent) is also planned. Re-run this check after Stage 2 of `docs/superpowers/plans/2026-09-06-formal-model-and-evaluation-realignment.md`. |

---

*This table should be used as an internal verification tool during proposal revision. It does not need to appear in the submitted thesis but can be referenced during viva preparation.*