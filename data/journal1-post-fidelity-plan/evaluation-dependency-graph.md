# Journal 1 Evaluation Dependency Graph

**Date:** 2026-09-11  
**Branch:** `design/journal1-post-fidelity-evaluation-plan`  
**Batch context:** Post-Batch-5 (F1=F2=F3=PASS, 2026-09-11)

---

## 1. Node Legend

| Symbol | Status | Meaning |
|---|---|---|
| [CLOSED] | CLOSED | Required evidence exists; claim can be supported |
| [READY] | READY | Scientific authority established; execution feasible without new assumptions |
| [OPEN] | OPEN | Unresolved scientific/design issue |
| [BLOCKED] | BLOCKED | Cannot execute due to explicit unresolved dependency |

---

## 2. Authority Chain

```
docs/canonical/appendix-c-formalisation.md                 [AUTHORITY — read-only]
publications/active/journal-1/algorithm-specification.md    [AUTHORITY — read-only]
publications/active/journal-1/evaluation-specification.md   [AUTHORITY — read-only]
publications/active/journal-1/layer3-prototype-specification.md  [AUTHORITY — read-only]
```

---

## 3. Formal Architecture → P1–P4

All four formal claims are proved, not tested. No experimental evidence is needed or admissible.

```
appendix-c-formalisation.md (C.1, C.1b, C.2, C.3, C.6, C.7.2)
algorithm-specification.md (Algorithms 1–4; §15 B21–B24; §22 Safety-Dominance chain)
evaluation-specification.md (§6 Formal propositions)
        │
        ├── P1 — Totality [CLOSED]
        │   Theorem C.1 + C.1b; Algorithm 1 Q1 postcondition
        │   No further action required
        │
        ├── P2 — Monotonicity [CLOSED]
        │   Theorem C.2; Corollary C.2; Algorithm 2 B21–B24 verification
        │   No further action required
        │
        ├── P3 — Safety Dominance [CLOSED]
        │   Theorem C.3 by construction (RS(S) supply); A1–A4 stated explicitly
        │   F1–F3 test implementation conformance to A1–A4 — separate evidence chain
        │   No further action required
        │
        └── P4 — C1 ≡ C3 (J1-P1) [CLOSED]
            One-line proof from mapping literals; 0.00% trace confirmation (E6)
            Travels with Flehmig fairness qualification in every occurrence
            No further action required
```

**Key distinction:** P1–P4 are proved by construction or finite-mapping comparison. Do not create experiments to re-prove formal properties.

---

## 4. Implementation → F1–F3

All three fidelity claims were evaluated in Batch 5 (2026-09-11). Status CLOSED.

```
governance/ module (8 files confirmed UNCHANGED, Batch 5 integrity.json)
scripts/journal1_layer3_fidelity_evaluation.py
        │
        ├── F1 — Advisory Admissibility Fidelity [CLOSED]
        │   F1 PASS: violations = 0 / 292 primary episodes / 454 advisory records
        │   Evidence: batch5-fidelity-evaluation/report.md §13; fidelity-results.json
        │   No further action required
        │
        ├── F2 — Safety Dominance Violation Count [CLOSED]
        │   F2 PASS: violation_count = 0 / 244 advisory-producing episodes
        │   Evidence: batch5-fidelity-evaluation/report.md §14; fidelity-results.json
        │   No further action required
        │
        └── F3 — RS(S) Switching Correctness [CLOSED]
            F3 PASS: mismatches = 0 / 292 episodes
            Evidence: batch5-fidelity-evaluation/report.md §15; fidelity-results.json
            No further action required
```

**Bounded claim for F1–F3:** These are implementation-fidelity results, not re-proofs of P3. They confirm that the frozen implementation conforms to the assumptions A1–A4 on which Theorem C.3 rests. They do not replace the formal proof.

---

## 5. Empirical Trace Evaluations → E1–E4, E6

All five empirical-trace evaluations are CLOSED. Canonical values exist from the retrospective replay.

```
scripts/condition_comparison.py     (E1, E2, E6)
scripts/canonical_figures.py        (E3 — dual-configuration values)
scripts/hysteresis_analysis.py      (E4)
docs/canonical/empirical-findings-2026-09-06.md §0a  (authoritative figure list)
        │
        ├── E1 — Pairwise Admissible-Set Divergence [CLOSED]
        │   PRIMARY: C0↔C1 = 42.88%; C0↔C2 = 48.69%
        │   C1↔C2 = Δ_L2 = 5.81% (PRIMARY)
        │   Report under both PRIMARY and RESOLUTION
        │
        ├── E2 — Isolated Level 2 Contribution Δ_L2 [CLOSED]
        │   PRIMARY: Δ_L2 = 5.81% (48.69 − 42.88)
        │   RESOLUTION: Δ_L2 = 4.48%
        │   Load-bearing empirical result for RQ-J4
        │
        ├── E3 — Resolution Sensitivity [CLOSED]
        │   All empirical figures report both PRIMARY and RESOLUTION
        │   Spread is resolution-sensitivity — NOT a confidence interval
        │   Do not write "5.81 ± something"
        │
        ├── E4 — Transition and Hysteresis Characterisation [CLOSED]
        │   3,661 transitions / 26 genuine oscillations (5.2/yr) / 10.36% reduction
        │   Provenance chain: 5416 (pre-amendment) → 5220 (threshold) →
        │   5201 (data) → 3661 (g_t migration SDR-001)
        │   Frame as low-cost precaution — NOT mitigation for observed instability
        │
        └── E6 — C1 ↔ C3 Divergence [CLOSED]
            0.00% over 43,848 hours (PRIMARY and RESOLUTION)
            Implementation-consistency confirmation of J1-P1 — NOT a discovery
            Travels with Flehmig fairness qualification
```

**Independence:** E1–E4 and E6 are mutually independent — they can be reported in any order. They do not depend on F1–F3 or on each other (except E3 which is the dual-configuration reporting of E1/E2/E4/E6 values).

---

## 6. Performance Evaluation → E5

E5 is the only remaining evaluation that has not been executed.

```
governance/ module (Layer 2 pipeline: classification + gate + admissible-set + RS supply)
Target deployment hardware (low-resource coastal fisheries device, manuscript §9)
evaluation-specification.md §11 (measurement design)
        │
        └── E5 — Governance Latency and Computational Overhead [READY]
            Measurement: mean, max, p95, p99 wall-clock latency for one Layer 2 pass
            Resource: peak memory and CPU
            Hardware: target low-resource deployment hardware (manuscript §9)
            Status: READY — prototype exists (Batch 5 confirmed); measurement design
                    established; no new assumptions needed
            Note: latency acceptance threshold H3 = X ms remains OPEN-B1-6
                  (no externally justified value). Report as descriptive measurement only.
            Blocker: none scientific — requires scheduling of benchmarking run on
                     target hardware
```

**E5 is independent of E1–E4, E6.** It can run immediately without waiting for any other evaluation. It does not depend on F1–F3 results. It is the ONLY remaining unexecuted evaluation in Journal 1's evidence base.

---

## 7. Full Dependency Matrix

```
         P1  P2  P3  P4  F1  F2  F3  E1  E2  E3  E4  E5  E6
P1       --  --  --  --  --  --  --  --  --  --  --  --  --
P2       --  --  --  --  --  --  --  --  --  --  --  --  --
P3       --  --  --  --  --  --  --  --  --  --  --  --  --
P4       --  --  --  --  --  --  --  --  --  --  --  --  E6*
F1       --  --  --  --  --  --  --  --  --  --  --  --  --
F2       --  --  --  --  --  --  --  --  --  --  --  --  --
F3       --  --  --  --  --  --  --  --  --  --  --  --  --
E1       --  --  --  --  --  --  --  --  --  --  --  --  --
E2       --  --  --  --  --  --  --  E1* --  --  --  --  --
E3       --  --  --  --  --  --  --  E1* E2* --  E4* --  E6*
E4       --  --  --  --  --  --  --  --  --  --  --  --  --
E5       --  --  --  --  --  --  --  --  --  --  --  --  --
E6       --  --  --  --  --  --  --  --  --  --  --  --  --

* = reporting dependency only (E3 reports dual-config values for E1, E2, E4, E6)
    E2 references E1 values for the subtraction Δ_L2 = div(C0,C2) − div(C0,C1)
    P4 is analytically prior to E6; E6 is the trace-confirmation of P4
    These are not execution dependencies — all relevant values are already canonical.
```

**No claim depends on any other claim for its execution.** All dependencies are reporting dependencies (citing related values) rather than execution prerequisites. Every claim that is CLOSED or READY can proceed independently.

---

## 8. Status Summary

| Status | Claims | Count |
|---|---|---|
| CLOSED | P1, P2, P3, P4, F1, F2, F3, E1, E2, E3, E4, E6 | 12 |
| READY | E5 | 1 |
| BLOCKED | (none) | 0 |
| OPEN | (none in primary claim structure) | 0 |
| NOT_REQUIRED | (none in primary claim structure) | 0 |

---

## 9. What Should Happen Next — and Why

**The evaluation that should happen next is E5 (governance latency benchmarking).**

Rationale:

1. **It is the only remaining unexecuted evaluation.** All 12 other claims (P1–P4, F1–F3, E1–E4, E6) are CLOSED with canonical evidence. E5 is the sole READY claim awaiting execution.

2. **Its execution is no longer blocked.** The previous blocker cited in the evaluation specification was "Layer 3 build for realistic end-to-end timing." Batch 5 confirmed the governance/ module (8 files) is frozen and the full reasoning pipeline executes. The technical blocker is resolved.

3. **It is independent of all other evaluations.** E5 does not depend on F1–F3 results or empirical-trace values. It can run immediately on the target hardware.

4. **The measurement design is fully specified.** evaluation-specification.md §11 defines exactly what to measure (mean, max, p95, p99 wall-clock latency; peak memory and CPU), on what hardware, and how to report it. No new assumptions are needed.

5. **The acceptance threshold constraint is bounded and does not block execution.** H3 = X ms is OPEN (OPEN-B1-6 — no externally justified threshold exists). This means E5 is reported as a descriptive measurement only, not as a pass/fail test. This is sufficient for Journal 1's RQ-J2, which asks "what runtime latency does Layer 2 introduce?" — a descriptive question.

**E5 execution protocol (from evaluation-specification.md §11):**
- Deploy governance/ module on the target low-resource hardware documented in manuscript §9
- Instrument one full Layer 2 pass (classification → gate → admissible-set selection → RS supply)
- Measure: mean latency, maximum latency, p95, p99, peak memory, peak CPU
- Report: descriptive values with hardware specification and instrumentation method
- Do NOT invent an acceptance threshold
- Do NOT treat algorithmic complexity bounds (O(1) per decision) as performance evidence

---

*Author: iskandar · Date: 2026-09-11 · Batch 6 Task 1*
