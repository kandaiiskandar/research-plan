# Batch 8B-1 — New-Prose Audit

Sections authored: **9, 10, 11, 12**. Sections 1–4, 13–15, the Abstract, Keywords and References are out of scope for this sub-batch and remain undrafted, carrying their Batch 8A markers.

---

## Section 9 — Prototype Implementation

**Authoring status:** AUTHORED (7 subsections; 3 tables).

**Authoritative sources used**

- `publications/active/journal-1/layer3-prototype-specification.md` §§3, 5–13, 16–26 — module boundaries, `ComponentStateTrace`, rule representation, predicate semantics, rule register, evidence hierarchy
- `data/journal1-layer3-prototype/batch5-fidelity-evaluation/` — `fidelity-results.json`, `rule-activation-summary.csv`, `state-space-manifest.json`, `evaluation-design.json`, `reporting-repair.json`
- `docs/canonical/appendix-c-formalisation.md` C.2.0.5, C.2.0.6 — exclusion and startup-precondition semantics
- `docs/canonical/empirical-findings-2026-09-06.md` F-6 and mode-chattering block — hysteresis framing
- `CLAUDE.md` canonical `g_t` block — frozen solar artefact

**New quantitative claims:** Q-01 – Q-18, Q-57, Q-59 (fidelity counts, rule activation, oscillation and hysteresis figures). All provenanced in `quantitative-provenance.csv`.

**Interpretive claims:** prototype-versus-deployed-system distinction; offline-first as a structural rather than performance property; permission ≠ warrant; hysteresis as precaution rather than mitigation; site-specific instantiation.

**Limitations introduced**

1. **`R-SAFE-001 = DEFERRED`; `RS(SAFE)` is empty.** All 32 SAFE episodes generated zero advisories, the only generated conclusion type is `Delay`, and F1/F2 therefore do **not** demonstrate fidelity of a populated SAFE rule set. Stated in §9.3 and again in §9.5.
2. Interface-contract exhaustive scope is not historical, environmental, deployment or real-world exhaustive.
3. The 244 figure is conclusion-type evaluations, not distinct conclusion types.
4. The 162 gate-off cases are separate from the 292 primary episodes.
5. Hysteresis findings bounded at hourly resolution.
6. `DepartureTime` and `Duration` have no repository authority for payload content.

**Open dependencies:** E5 (§11.7). The SAFE-rule limitation must reappear in §14 during 8B-2.

---

## Section 10 — Experimental Design

**Authoring status:** AUTHORED (5 subsections; Table 7 plus three condition tables).

**Authoritative sources used**

- `publications/active/journal-1/evaluation-specification.md` §§3–6, 9–13, 15–18 — conditions, comparator, RQs, metrics, statistical treatment, PRIMARY/RESOLUTION contract, human-validation boundary
- `data/journal1-e5-benchmark/` — `benchmark-protocol.md`, `workload-manifest.json`, `execution-path-audit.md`, `latency-results.json`
- `data/c8/canonical-results-post-migration.txt` — replay scope and record counts
- E3/E4 authority micro-repair (`data/journal1-e3-e4-authority-repair/`) — E3 scope `{E1, E2, E6}`

**New quantitative claims:** Q-19 – Q-22, Q-67 – Q-69 (replay scope, benchmark parameters, hardware profile, target-hardware flag).

**Interpretive claims:** the four evidence classes and why they must not substitute for one another; C1/C2 differing in exactly one cell is what makes the comparison informative; the C3 fairness qualification and its modelling premise; `D = {m}` producing lower bounds; PRIMARY/RESOLUTION as two measurements rather than two draws.

**Limitations introduced**

1. Decision-support utility has no operational definition on replay data and is not closed.
2. Trust, calibrated reliance and real-world outcomes are outside the evidence base entirely.
3. E5 OPEN; `H3 = X ms` OPEN and unsupported; RQ-J2 unanswered.
4. `D = {m}` lower-bound consequence.
5. The C3 result is bounded by the modelling premise `A_C3(CAUTION) = FULL`.

**Open dependencies:** E5 / RQ-J2.

**Retired hypotheses not restored:** H1, H2 and H4 do not appear. H3 appears only as OPEN/UNSUPPORTED.

---

## Section 11 — Results

**Authoring status:** AUTHORED (7 subsections; Tables 8–12 plus a state-distribution table).

**Authoritative sources used**

- `data/c8/canonical-results-post-migration.txt` — divergence matrices, state distributions, transition counts, hysteresis comparison, C1↔C3 both configurations
- `data/prediction-register.csv` P21–P24, P04 — full-precision cross-checks (`45.5602`, `41.0783`, `4.4819`, `0.0000`, `5.8128078817733995`)
- `data/c7/baseline-provenance.csv` P09 row — the `5416 → 5220 → 5201 → 3661` vintage chain
- `data/journal1-e5-benchmark/latency-results.json` — Table 12 and resource semantics
- `docs/canonical/empirical-findings-2026-09-06.md` §0a — canonical figure authority
- Batch 5 evidence — §11.2 status summary

**New quantitative claims:** Q-23 – Q-66. Every value cross-checked against at least one artefact; four arithmetic identities (Q-43 – Q-46) re-derived from the state distributions and confirmed against the register.

**Interpretive claims:** what divergence counts are and are not; `Δ_L2` as additional advisory-scope governance; the 1.3-point gap as the sensitivity result; transitions dominated by scheduled solar boundaries; E6 as confirmation rather than discovery; the development-machine reference as reference only.

**Limitations introduced**

1. E4 is PRIMARY-only by scope, with no resolution-insensitivity claim.
2. The `5416 → 3661` change is not attributable to `g_t` alone.
3. Hysteresis findings bounded at hourly resolution.
4. E6 bounded by the C3 modelling premise.
5. E5 OPEN; reference measurements carry no threshold and no extrapolation.
6. All severity figures are lower bounds under `D = {m}`.

**Open dependencies:** E5 target-hardware measurement (Batch 7B, deferred for want of physical hardware).

**Deliberate departure from the original brief's recommended structure:** the brief suggested §11.2 carry the implementation-fidelity results in full. The manuscript's own §11 instruction — repaired in Batch 8A — directs F1–F3 to §9 because they are implementation-fidelity rather than empirical-trace evidence. §11.2 therefore states the status and cross-references §9.5 rather than duplicating it. Repository authority was followed over the prompt; no scientific content is lost or duplicated.

---

## Section 12 — Ablation Study

**Authoring status:** AUTHORED (5 subsections; Table 13). **Existing title retained** per Decision 4.

**Authoritative sources used**

- `publications/active/journal-1/evaluation-specification.md` §10 — ablation design
- §11 results of this manuscript (no new computation)
- `docs/canonical/evaluation-design-rq4.md` SC-16–SC-20 — inspected and found to be specified against superseded thresholds

**New quantitative claims:** Q-50 and restatements of Q-23, Q-24, Q-27, Q-28, Q-47, Q-48, Q-49, Q-51 – Q-59. No new value is introduced.

**Interpretive claims:** ablation removes a mapping rather than estimating an effect; the Level 1 / Level 2 magnitude difference is structural, not a statement of relative value; hysteresis retained on cost rather than necessity grounds; the C1/C3 ablation is degenerate by construction and that degeneracy is the finding.

**Limitations introduced**

1. Descriptive differences are not causal effects.
2. **Worst-case-aggregation ablation not performed** — the specified boundary scenarios use superseded threshold and time-classifier values and have not been executed under the canonical configuration. Labelled future work.
3. **Component ablation not performed** — the site binding profile characterises which component decides the state; it is not an ablation.
4. No RESOLUTION hysteresis counterpart.

**Open dependencies:** §12.5 forward-references §14 for the ablation-scope limitations. §14 is drafted in 8B-2 and **must carry them**; this is recorded as a required 8B-2 item.

---

## Cross-cutting observations recorded, not acted on

Three pre-existing inconsistencies were found in material this sub-batch is not authorised to modify. None is a contradiction between closed *evidence* sources, so none triggered a stop condition; all three are carried forward.

1. **`evaluation-specification.md` carries stale F1–F3 and E5 status wording.** §7 ("all three are OPEN — deferred to Layer 3 build"), §14 ("Layer 3 is specified but not fully implemented") and §17 OPEN-3 predate Batch 5. The document's own §18 acknowledges the supersession and states that Batch 5 closed all three PASS. The manuscript was authored against the CLOSED status, which is the frozen status in the batch brief and in Batch 8A. **The specification was not modified.** A separate authority-synchronisation repair is warranted.
2. **Theorem numbering is inconsistent inside the protected §§5–8.** §5 states Theorem 5.1 (Totality); §6 restates the same results as Theorems 6.1–6.3; §7 refers back to Theorems 5.1–5.3. §§9–12 use the §6 numbering throughout, matching `evaluation-specification.md` §6. Protected prose was not edited.
3. **Frozen historical artefacts contain superseded values** — for example the `22 kn` wind threshold in the narrative text of `data/c8/canonical-results-post-migration.txt` and the fixed-clock description in its hysteresis method block. These are records of what was computed then. No figure was taken from them; only the canonical result tables in the same file were used.
