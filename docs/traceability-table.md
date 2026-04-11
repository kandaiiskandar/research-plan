---
layout: document
---

# Cross-Document Traceability Table
**Research title:** *A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Socio-Technical Evaluation in Coastal Fisheries*
**Purpose:** Verify alignment across the Research Design Alignment Table, Architecture Diagram, and Mathematical Formalisation (Appendix C).

---

## Table 1: Formal Component Traceability

| Formal Component | Appendix C Section | Architecture Diagram Element | Alignment Table Reference |
|---|---|---|---|
| E = {w, r, m, o, v, t} where:<br>w = wind condition (speed/strength)<br>r = rainfall intensity<br>m = sea state (wave height/swell)<br>o = official marine warning level (e.g., no warning, caution, danger)<br>v = vessel category (small, medium, big)<br>t = time of day (hour, 24-hour clock) | C.1 Environmental State Representation | L1 box: "Environmental data input" with subtitle "E = {w, r, m, o, v, t}" | PS2 gap: environmental state vector mapped to safety states; O2: formally define E |
| S = f(E) | C.2 Safety State Classification Function | L2 box: "Safety state classification" with subtitle "S = f(E)" | PS2 gap: no architecture classifies environmental conditions into discrete safety states; O2: formally define S = f(E) |
| S ∈ {SAFE, CAUTION, UNSAFE} | C.2 Classification output | Three state boxes: SAFE (green), CAUTION (amber), UNSAFE (red) | PS1: graduated AI participation — enabled, restricted, disabled; O1: three-mode architecture |
| G(S) | C.3 AI Participation Gate Function | Level 1 dashed container: G(S) = 1, G(S) = 1, G(S) = 0 per state | PS1 gap: existing architectures implement binary governance; O2: formally define G(S) |
| R = {Go, Delay, DepartureTime, Duration} | C.4 Recommendation type set | Implicit in A_AI box subtitles: "Go, delay, timing, duration" | PS3 gap: domain-specific operationalisation for fisheries; O2: domain-specific operationalisation of safety thresholds |
| A_AI(SAFE) = {Go, Delay, DepartureTime, Duration} | C.4 AI-Admissible Recommendation Space | Level 2 green box: "A_AI(SAFE)" / "Go, delay, timing, duration" | O2: formally define A_AI(S); O1: full advisory scope in SAFE |
| A_AI(CAUTION) = {Go, Delay} | C.4 AI-Admissible Recommendation Space | Level 2 amber box: "A_AI(CAUTION)" / "Go, delay" | O1: restricted advisory scope in CAUTION; O5: particular attention to CAUTION state |
| A_AI(UNSAFE) = ∅ | C.4 AI-Admissible Recommendation Space | Level 2 red box: "A_AI(UNSAFE)" / "= ∅" | O1: AI disabled in UNSAFE; O4: safety compliance evaluation |
| A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ | C.4 Containment relationship | Diagram legend below Level 2 boxes | O2: formally define A_AI(S) with the property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ |
| Two-level governance: (G(S), A_AI(S)) | C.5 Two-Level Governance Structure | Two dashed containers labelled "Level 1: G(S)" and "Level 2: A_AI(S)" | PS1 gap: no intermediate participation mode; core contribution in all five objectives |
| Participation constraint: G(S) = 0 ⇒ A_AI(S) = ∅ | C.6 Governance Constraints | UNSAFE column: G(S) = 0 (Level 1) → A_AI(UNSAFE) = ∅ (Level 2) | O4: safety compliance evaluation metric |
| Advisory restriction: A_AI(CAUTION) ⊂ A_AI(SAFE) | C.6 Governance Constraints | CAUTION column drops DepartureTime, Duration relative to SAFE column | O4: comparative performance — does CAUTION restriction add value; O5: user response to restricted AI |
| Safety Dominance: AI(E) ⊆ A_AI(S) | C.7 Safety Dominance Property | Pipeline footer: E → S = f(E) → (G(S), A_AI(S)) → AI(E) | O4: does the system ever produce recommendations outside admissible space |
| Human decision authority | Architectural principle (not formalised) | L4 box: "Human decision layer" / "Final decision authority" | O5: user trust, understanding, decision behaviour |
| Pipeline: E → S = f(E) → (G(S), A_AI(S)) → AI(E) | C.5 page 6 summary | Diagram footer text | Contribution statement in alignment table traceability notes |

---

## Table 2: Research Objective → Architecture Diagram Traceability

| Objective | What it requires | Diagram elements that satisfy it | Can a binary gate satisfy this? |
|---|---|---|---|
| **O1:** Design a three-mode architecture (enabled / restricted / disabled) based on classified environmental safety state | Three distinct AI participation modes; environmental state as trigger | Three columns (SAFE → enabled, CAUTION → restricted, UNSAFE → disabled); L2 classification produces three states from E | No — binary gate has only two modes |
| **O2:** Formally define E, S = f(E), G(S), A_AI(S) with containment property | All four formal components visible; containment stated | L1 (E), L2 (S = f(E)), Level 1 boxes (G(S) values), Level 2 boxes (A_AI contents), legend (containment) | No — binary gate has no A_AI differentiation between SAFE and CAUTION |
| **O3:** Implement prototype for small-scale coastal fisheries | Domain-specific recommendation types | A_AI subtitles use fisheries-specific terms: go/no-go, delay, departure timing, trip duration | N/A (implementation objective) |
| **O4:** Evaluate against binary-gated baseline AND ungated baseline | Three-condition comparison structure must be visible | Level 1 alone = binary-gated baseline (G(S) only); removing both levels = ungated baseline; full diagram = proposed three-mode system | N/A (evaluation objective, but diagram makes comparison structure self-evident) |
| **O5:** Evaluate user understanding across three states, especially CAUTION | CAUTION must be visually distinct from both SAFE and UNSAFE | CAUTION column: G(S) = 1 (same as SAFE at Level 1) but A_AI = {Go, Delay} (different from SAFE at Level 2) — shows why CAUTION is the interesting evaluation target | No — binary gate makes CAUTION identical to SAFE |

---

## Table 3: Problem Statement → Gap → Architecture Element

| Problem Statement | Research Gap | Architecture Element That Addresses It |
|---|---|---|
| **PS1:** Existing architectures implement binary governance — AI is either fully enabled or fully blocked | No intermediate participation mode with restricted recommendation space | Three columns with three distinct A_AI sets; Level 2 governance differentiates SAFE from CAUTION |
| **PS2:** Graduated governance (Flehmig et al.) is triggered by AI performance, not environmental state | No architecture classifies environmental conditions into safety states that determine AI recommendation scope | L1 (environmental input E) → L2 (S = f(E)) → Level 1 + Level 2 governance; trigger is environmental, not performance-based |
| **PS3:** No safety governance architecture designed for low-resource fisheries | No formal safety architecture for resource-constrained fisheries deployment | Recommendation types (Go, Delay, DepartureTime, Duration) are fisheries-specific trip decisions; architecture designed for offline/limited-data contexts |
| **PS4:** No comparative evaluation of graduated vs. binary governance | Three-mode value over binary has not been tested | Level 1 alone (binary) vs. Level 1 + Level 2 (graduated) — diagram structure enables three-condition experimental design |
| **PS5:** No socio-technical evaluation of graduated AI governance, especially CAUTION | User response to restricted AI is unknown | CAUTION column is the focal evaluation point: AI active but bounded — unique user experience not present in binary systems |

---

## Consistency Checklist

| Check | Status |
|---|---|
| Every formal component in Appendix C appears in the architecture diagram | ✓ Verified in Table 1 |
| Every research objective maps to specific diagram elements | ✓ Verified in Table 2 |
| Every problem statement traces through a gap to an architectural response | ✓ Verified in Table 3 |
| A_AI notation is consistent across formalisation and diagram | ✓ Both use A_AI(S) |
| Recommendation types match between C.4 and diagram subtitles | ✓ R = {Go, Delay, DepartureTime, Duration} maps to "Go, delay, timing, duration" |
| Containment property stated identically in C.4 and diagram legend | ✓ A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ |
| Two-level governance labelled in both C.5 and diagram | ✓ Dashed containers: Level 1: G(S), Level 2: A_AI(S) |
| Pipeline expression matches between C.5 and diagram footer | ✓ E → S = f(E) → (G(S), A_AI(S)) → AI(E) |
| GoWithCaution does NOT appear anywhere | ✓ Removed from formalisation and diagram |
| No objective can be satisfied by a binary gate | ✓ Verified in Table 2 final column |
| A_H(S) does NOT appear anywhere | ✓ Correctly excluded from formalisation and diagram |
| Parameter definitions in E are consistent across Appendix C and this traceability table | ✓ Both use {w, r, m, o, v, t} with matching definitions (wind, rainfall, sea state, official warning, vessel category, time of day) |

---

*This table should be used as an internal verification tool during proposal revision. It does not need to appear in the submitted thesis but can be referenced during viva preparation.*