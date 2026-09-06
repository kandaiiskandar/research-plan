# Formal Model and Evaluation Realignment — Work Plan

**Date:** 2026-09-06
**Trigger:** IPSci 2026 rejection (Review 3: "lacks technical and empirical evidence to establish novelty, effectiveness, and safety claims") + audit of `evaluation-design-rq4.md` against canonical definitions.

**Scope:** Resolve two formal-model inconsistencies, rewrite the RQ4 evaluation design, propagate changes to both papers, then execute the evaluation.

**Governing rule:** Per CLAUDE.md Formal Model Consistency Rule — `docs/canonical/appendix-c-formalisation.md` is updated FIRST. No downstream document changes before that.

---

## Findings that triggered this plan

| # | Finding | Severity | Status |
|---|---------|----------|--------|
| F1 | **Revised during analysis.** Initially framed as "SAFE unreachable for small vessels." The sharper defect: a constant term in a max is a floor, not a threshold shift, so `g_v` had **zero effect on the CAUTION/UNSAFE boundary** — all vessel sizes classified UNSAFE at identical thresholds, under-classifying small-vessel risk across the 1.5–3.5 m band. SAFE-unreachability is a secondary consequence. | **Critical** | ✅ Fixed |
| F2 | CLAUDE.md defines `o ∈ ℝ≥0 × ℝ≥0`; downstream treats it as scalar. **Downgraded on verification** — appendix-c is internally consistent (documents wave height as governing component, swell period deferred). Only the explainer is loose. | ~~High~~ **Low** | ✅ Documented in C.9.3 |
| F3 | Conference paper Fig. 4 panel 1 shows `v = small` classified as SAFE — impossible under current `g_v`. | **High** |
| F4 | All 20 evaluation scenarios use `v = big`. Vessel dimension never exercised; deployment population never tested. | **High** |
| F5 | No scenario tests the fail-safe rule (`xᵢ = ⊥ → UNSAFE`), despite Theorem 1 and the offline-first deployment claim depending on it. | **High** |
| F6 | No temporal scenarios; hysteresis / mode-chattering claimed in both papers but never evaluated. | **Medium** |
| F7 | C0/C1/C2 are all self-ablations. No external baseline. Likely driver of Review 3's novelty objection. | **High** |
| F8 | Ablation plan (supervisor Point 6) overlaps C0/C1/C2 — "remove A_AI" *is* C1. Two inconsistent experimental plans. | **Medium** |
| F9 | SC-20 note incorrect: claims "no other parameter is SAFE" but `r=moderate`, `v=big`, `t=08:00` are all SAFE. | **Low** |
| F10 | Category E labelled "Adversarial" — no adversary present; these are non-compensation tests. | **Low** |
| F11 | "Decision consistency" listed as a metric; trivially satisfied by a deterministic engine. | **Low** |
| F12 | No timing measurements to support TABLE IV O(1)/O(n) claims or "CAUTION cheaper than SAFE". | **Medium** |
| F13 | No scenario → theorem traceability mapping. | **Medium** |

### Findings discovered during propagation (not in the original audit)

Not visible from `evaluation-design-rq4.md` alone. All predate this work.

| # | Finding | Where | Severity | Status |
|---|---------|-------|----------|--------|
| F14 | **`m` and `o` swapped** relative to Appendix C — `m` defined as sea state, `o` as marine warning level. Found in **two** documents | `canonical/traceability-table.md`, `justification/formal-model.md` | **Critical** | ✅ |
| F15 | **Consistency checklist certified its own error** — the row verifying E-parameter consistency listed the definitions in the swapped order and marked itself ✓ | `canonical/traceability-table.md` | **Critical** | ✅ |
| F16 | **Six misclassifications** in the worked day-scenarios: `w=18→CAUTION` (SAFE), `r=moderate→CAUTION` (SAFE), `r=heavy→UNSAFE` (CAUTION), a nonexistent "15 kn threshold", plus two wave readings correct only for small vessels | `canonical/architecture-illustration.md` | **High** | ✅ |
| F17 | **Three mutually inconsistent wind threshold sets** — 25/22, 25/35, 13/22 kn; none matched canonical 22/27. Three *viva one-liners* among the affected lines | `justification/viva-formalisation-architecture.md` | **Critical** | ✅ |
| F18 | **Thresholds misattributed to MMEA** (7 occurrences). They derive from MET Malaysia; MMEA is the enforcement agency and publishes no such criteria | `viva-formalisation-architecture.md` +2 | **High** | ✅ |
| F19 | **`v` described as "vessel condition / operational readiness"** with invented pre-departure-checklist thresholds. `v` is vessel *category* (size) | `viva-formalisation-architecture.md`, `safety-state-design.md` | **High** | ✅ |
| F20 | **Malformed example vectors** — rainfall as an integer, `v = GOOD`, ocean state as an ordinal label; does not typecheck against Definition C.1 | `viva-formalisation-architecture.md` EC-7 | Medium | ✅ |
| F21 | **Fail-safe misdescribed** as a per-variable HIGH default flowing through max-severity rather than a guard before any gᵢ. The distinction is what Theorem C.1's totality extension rests on | `viva-formalisation-architecture.md` | Medium | ✅ |
| F22 | **Rainfall thresholds wrong** — moderate classified CAUTION; canonical has moderate in the SAFE set. Also used mm/hr bands absent from the canonical categorical definition | `justification/safety-state-design.md` | **High** | ✅ |
| F23 | **Superseded `g_v` was itself inconsistently specified** — `safety-state-design.md` had SAFE={medium,big}/CAUTION={small}; appendix-c had SAFE={big}/CAUTION={small,medium} | `justification/safety-state-design.md` | Medium | ✅ |
| F24 | **Worked examples mis-annotated** independent of the swap — "triggered by wind" at w=20 kn (SAFE); "marine warning + vessel category + time" where only the warning contributes | `justification/formal-model.md` | Medium | ✅ |
| F25 | **Stale paths** — `docs/appendix-c-formalisation.md`, `docs/justification-layer3-enforcement.md`, `docs/rq5-study-design.md`, `docs/evaluation-design-rq4.md`; all live in `docs/canonical/`. CLAUDE.md's Formal Model Consistency Rule pointed at a nonexistent file | `CLAUDE.md`, `canonical/traceability-table.md` | Medium | ✅ |
| F26 | **Vessel-blind label logic would mislabel training data.** The Go/Delay/AI-off label table specified wave bands with no vessel reference — "waves 1.5–3.5 m → CAUTION" holds for a big vessel but a small vessel is UNSAFE above 1.9 m. Since these rows generate the advisory AI's training labels, the error would have trained the model on wrong labels for the deployment population | `implementation/dataset-label-derivation.md` | **Critical** | ✅ |
| F27 | **Tide conflated with `o`.** Gao's factor ratings annotated "Tide (**ocean state, o**): 4.55 — highest rated". Tide is lunar/solar-forced tidal height; `o` is wind- and swell-driven wave height. Distinct phenomena. **Tide is not in E at all** — so the highest-rated decision factor in the only study that ranked factors is unmodelled | `implementation/dataset-label-derivation.md` | **High** | ✅ Fixed + logged in C.9.3 |
| F28 | **Internal contradiction in source data** — Rahim East season described as "vigorous winds ... (~5 knots wind)". 5 kn is Beaufort 2 and would classify SAFE, contradicting the restricted-operations behaviour it is cited to justify | `implementation/dataset-label-derivation.md` | Medium | ✅ **Resolved** — East season is CAUTION via `g_r(heavy)`, not wind. See below |
| F29 | **Appendix-c cross-reference inaccurate** — C.2 pointed to `dataset-label-derivation.md` "for full derivation" of thresholds. That document derives *training labels for Layer 3*; it consumes the thresholds rather than deriving them | `canonical/appendix-c-formalisation.md` | Low | ✅ |
| F30 | **Two scenario rows wrong under the old model too.** "1.0–1.5 m → SAFE" was CAUTION under the old thresholds once the upper-bound rule is applied; "Ribut petir → CAUTION" contradicts the same document's own table listing Ribut Petir as the storm-tier UNSAFE trigger | `implementation/data-source-met-malaysia.md` | **High** | ✅ |
| F31 | **Wind band annotated "UNSAFE for small vessels"** at 22–27 kn. `g_w` is not vessel-conditional; 22–27 kn is CAUTION for every vessel. MET's "dangerous to small craft" is advisory language, not a state assignment | `implementation/data-source-met-malaysia.md` | Medium | ✅ |

### F28 resolution — East season maps via rainfall, not wind

Checking `notes/Survival Decisions and Adaptation Strategies...md` against the label derivation: Rahim reports wind spanning **5–40 kn across all three seasons**, West at 30–40 kn. The 5 kn East-season figure sits at the bottom of that range and is not obviously mis-transcribed. Reading the seasons together:

| Season | Wind | Precipitation | Seas | Classifies as |
|---|---|---|---|---|
| Fishing | low | **moderate** | mild swells | SAFE — `g_r(moderate)` = SAFE |
| East | ~5 kn (SAFE) | **heavy** | calm | **CAUTION via `g_r(heavy)`** |
| West | 30–40 kn | heavy | > 2 m | UNSAFE via `g_w` |

The Fishing/East distinction is exactly `g_r`'s SAFE/CAUTION boundary — moderate vs. heavy. The East season → Delay evidence holds; it underwrites the **rainfall-driven** CAUTION row, not a wind-driven one. §4 of the label document amended: East season no longer cited for the 22–27 kn row.

**Source verified against the original paper (2026-09-06).** The contradiction is in Rahim et al. itself, not in the corpus notes — the paper states "vigorous winds" and "the wind velocity is 5 knots per hour" in consecutive sentences. Three further findings from that check:

| # | Finding | Consequence |
|---|---|---|
| F32 | **West season figures are gusts, not sustained wind** — "wind **gusts** of 30 to 40 knots per hour". `w` is defined as sustained; 30–40 kn gusts ≈ 19–31 kn sustained, straddling the 27 kn boundary | `appendix-c` C.2 cited this as empirical support for the `g_w` UNSAFE threshold. **Citation removed.** The threshold stands on MET Malaysia Category 2 onset; West season's UNSAFE classification rests on wave height (> 2 m → UNSAFE for small vessels), not wind. Note added to `g_w` requiring future empirical corroboration to state whether values are sustained or gust |
| F33 | **East and Fishing seasons overlap** — both March–June, both low wind. Distinguished only by precipitation (substantial vs. moderate) | Reinforces the F28 resolution: the seasons separate on `g_r`'s SAFE/CAUTION boundary |
| F34 | **Measured vs. perceived risk divergence** — the paper appears to combine meteorological data (5 kn, plausibly BMKG) with interview language ("vigorous"). Fishers describing 5 kn sustained as vigorous is a perception/measurement gap | Relevant to **RQ5**, which tests whether operators interpret governance states as intended. Carried into the RQ5 discussion rather than treated as a data defect |

### Verification pass — 2026-09-06, after Tiers 1–3

Ran a systematic grep over all 43 files in `docs/canonical/`, `docs/justification/`, `docs/implementation/`, `docs/reference/` and `CLAUDE.md`. **Three misses found and fixed**, which is why the pass was worth doing:

| # | Miss | Where | Cause |
|---|---|---|---|
| F35 | **`v` still called "vessel condition"** with pre-departure-checklist framing in a timescale list and two data-source tables | `safety-state-design.md` ×2, `low-resource-environments.md` ×1 | During the Tier 2 pass, grep output truncated long lines as "[Omitted long matching line]"; only the visible hits were fixed |
| F36 | **F27 (tide/`o` conflation) is in FOUR files, not one.** Two state it explicitly — "tide (4.55/5 — **captured in o as ocean state**)" and "tide (4.55/5, **captured in o**)"; one implies the governance layer formalises tide; one overclaims that the architecture formalises the "dominant inputs" | `formal-model.md`, `safety-state-design.md`, `low-resource-environments.md`, `environmental-state-governance.md` | F27 was found in `dataset-label-derivation.md` and assumed local. Not re-checked repo-wide |
| F37 | **`environmental-state-governance.md` was never triaged.** It contains no `g_v`, no `max-severity`, and no threshold values, so it matched none of the triage patterns — yet it carries the Gao factor ratings and an "formalises existing practice" claim | `justification/environmental-state-governance.md` | Triage keyed on formal-model tokens; documents that discuss the model without using its notation were invisible to it |

**Methodological lesson.** Two of the three misses trace to grep-based triage: truncated output (F35) and pattern coverage (F37). A document can be wrong about the model without containing any of the model's symbols. Any future consistency sweep should include at least one content-based pass over `docs/justification/` rather than relying on token matching alone.

**Post-fix verification — all clean:**

| Check | Result |
|---|---|
| Six-term aggregation | clean |
| `m`/`o` swap | clean |
| "vessel condition" | clean |
| MMEA as threshold source | only inside the viva-doc revision notice |
| "captured in o" | only inside correction notes quoting the old text |
| Rainfall moderate → CAUTION | only inside correction notes |
| Vessel-blind `g_o` row | only `evaluation-design-rq4.md` (deferred to Stage 2) and the explainer's *big-vessel* row, which is correct |

**Pattern.** Every document audited so far contained errors predating this work. Three of five had errors in *worked examples* — the parts an examiner reads most closely. Two defined `m` and `o` backwards. One verification instrument certified its own error. The superseded `g_v` was specified inconsistently across documents even before removal.

**Process implication:** the Formal Model Consistency Rule in CLAUDE.md exists precisely to prevent F14/F22/F23, and did not. Worth considering whether the checklist in `traceability-table.md` should be re-run as a deliberate step rather than a static ✓ table — see the new "worked scenarios classify correctly" row added there.

---

## Stage 0 — Decisions ✅ RESOLVED 2026-09-06

- [x] **D1. Read `appendix-c-formalisation.md` C.2.** **Resolved:** `o` is canonically a tuple (wave height, swell period) and the file is internally consistent — line 149 already stated that wave height is the governing component with swell period deferred to domain instantiation. CLAUDE.md was correct; the explainer was loose. **F2 downgraded High → Low.**
- [x] **D2. `o` representation.** **Decision: keep the tuple.** `g_o` classifies on the wave height component only. Swell period retained in the state representation, non-use documented in new section C.9.3.
- [x] **D3. `g_v` role.** **Decision: Option 2 — drop `g_v`, parameterise `g_o(o, v)`.**

  Reasoning recorded during analysis:
  - A constant term in a max is a *floor*, not a *threshold shift*. Under the old model vessel category had **zero** effect on the CAUTION/UNSAFE boundary — a 5 m boat and a 20 m boat both classified UNSAFE at exactly 3.5 m and 27 kn.
  - Yaakob's 6.54 m vessel exceeds NORDFORSK operability limits at Hs ≈ 1.875 m — 1.9× below where the old model would call it UNSAFE. The model **under-classified risk across the 1.5–3.5 m band**, precisely where CAUTION is meant to operate.
  - The "correlated parameters will catch it" defence fails empirically: Jeong & Im report **82% of 2017–2022 capsizings occurred on days with no weather warning**.
  - Secondary: `g_v(small) = CAUTION` unconditionally made SAFE unreachable below 25 GRT. Since the deployment population is < 40 GRT, the three-state architecture collapsed to two reachable states for real users — making `A_AI(SAFE) ⊃ A_AI(CAUTION)`, the principal claim, **unobservable in-domain**. This also broke RQ4 Category A and made RQ5 unrunnable as designed.

  *Rejected:* Option 1 (keep as-is) — requires defending a classifier where the domain's defining parameter has no effect on the stop condition. Option 2b (keep `g_v` as a floor *and* parameterise) — considered after the Yaakob notes §4.2 endorsement surfaced; rejected because the "never SAFE" property is the note-writer's architectural inference, not a claim of the source, and it is what makes the contribution unobservable.

- [x] **D4. Vessel-conditional thresholds fixed.** Note: the draft numbers in the original version of this plan were **wrong** — they extrapolated Hs_KIMO below its validated 10 m LOA floor. Adopted table, grounded in what the sources actually state:

  | v (GRT) | SAFE | CAUTION | UNSAFE | Grounding |
  |---|---|---|---|---|
  | small (< 10) | o < 1.0 | 1.0 ≤ o ≤ 1.9 | o > 1.9 | Jeong & Im Table 12 (≤10 m → 1.0 m); Yaakob 6.54 m operational limit 1.25 m; SS4 = 1.875 m failure |
  | medium (10–25) | o < 1.4 | 1.4 ≤ o ≤ 2.8 | o > 2.8 | Hs_KIMO 10–15 m LOA = 1.13–1.48 m; **UNSAFE interpolated — weakest value** |
  | big (> 25) | o < 1.5 | 1.5 ≤ o ≤ 3.5 | o > 3.5 | **Unchanged** — MET Malaysia Cat 1; Hs_KIMO 16 m = 1.58 m |

  Categories keyed to **GRT, not LOA** — the Yunus (2007) LOA bands overlap (a 12 m vessel is both medium and large); tonnage bands are disjoint.

  Two values flagged in-text as explicit design decisions: small UNSAFE 1.9 m (reads NORDFORSK operability failure as UNSAFE — an interpretation, not Yaakob's claim) and medium UNSAFE 2.8 m (interpolated, no direct source).

---

## Stage 1 — Formal model (canonical first)

- [x] **T1.1** `appendix-c-formalisation.md` C.2 — `g_o` now two-argument with 3×3 threshold table; per-row empirical basis; `g_v` section replaced with a "there is no g_v" superseded note recording what changed and why. ✅ 2026-09-06
- [x] **T1.2** `appendix-c-formalisation.md` C.1 — `v` defined by GRT with Yunus (2007) table; new "Role of v in classification" paragraph; Vessel Category Classification Note fully rewritten with four evidence strands; both aggregation notes updated to five terms. ✅ 2026-09-06
- [x] **T1.3** Theorem C.1 — five-case verification; `g_o` case proves totality over the product domain in two steps (per-row partition of ℝ≥0, then finite exhaustion of v, noting independence from swell period). ✅ 2026-09-06
- [x] **T1.4** Verified: Theorems C.2 and C.3 unaffected. C.2 operates only on `A_AI(S)` set definitions; C.3's A1–A4 concern the rule engine and `RS(S)` supply, and its case analysis requires `f` total but not any particular internals. **Both load-bearing safety theorems untouched.** ✅ 2026-09-06
- [x] **T1.4b** *(added, not in original plan)* New section **C.9 Known Limitations** — threshold grounding (4 items), parameters not vessel-conditioned (wind flagged as most significant remaining gap), scope boundaries (vessel compliance deliberately excluded; swell period unused). Referenced from two places in C.2. ✅ 2026-09-06
- [x] **T1.5** CLAUDE.md — `o` and `v` rows updated; new "Classification structure (amended 2026-09-06)" block with the five-term `f(E)`, the 3×3 `g_o` table, and an explicit **"Do not reintroduce `g_v`"** warning pointing at the rationale. Also fixed two stale path references (`docs/appendix-c-formalisation.md` → `docs/canonical/...`). ✅ 2026-09-06
- [x] **T1.6** `explainer-per-component-classification-functions.md` rewritten. Five functions not six; `g_o` presented as a family of three threshold rows selected by `v`; "special case g_v" section replaced with a structural explanation of why a constant in a max is a floor and cannot shift a threshold. Worked examples expanded from two to five, chosen to demonstrate the fix: **A** small vessel reaching SAFE (impossible under the old model), **B** CAUTION, **C** UNSAFE by wave height alone with no wind and no warning — the Jeong & Im 82% scenario the old model missed, **D** same 2.5 m sea classifying UNSAFE/CAUTION/CAUTION across the three vessel classes, **E** non-compensation. Section 7 records what changed and flags the Yaakob notes as historical. `[[notes]]` links added per the Citation Reference Rule. ✅ 2026-09-06
- [x] **T1.7** `notes/Stability, Seakeeping...md` revised. Scope was wider than §4.2 — the `g_v` rationale ran through §4.1, §4.2, §4.3, §4.4 and §5. Added a partial revision notice at the top stating explicitly that §§1, 2, 3, 5, 6 (the paper's actual findings) are unaffected and only §4's architectural inferences changed. All superseded reasoning retained in blockquote with the counter-argument attached, rather than deleted. Also corrected a factual conflation running through the old text: 0.875 m and 1.875 m are the sea states at which the boats *fail*; the operational limits are ≈0.5 m (Boat B) and ≈1.25 m (Boat A). ✅ 2026-09-06

### Stage 1 complete

All formal model changes applied and cross-referenced. `g_v` no longer exists in any live document; every remaining occurrence is inside an explicitly marked superseded block.

### Verification performed

- Grepped `appendix-c-formalisation.md` for `g_v`, `S_v`, "six components/parameters" — only intentional occurrences in the superseded note remain. One false positive at line 42 ("six environmental scenarios" refers to Atacan & Düzbastılar's study design, not E components).
- Grepped all four `max-severity(...)` occurrences — consistent five-term form throughout.

---

## Stage 2 — Evaluation design rewrite

Blocked by: Stage 1.

Target file: `docs/canonical/evaluation-design-rq4.md` (rewrite, not patch).

### 2A. Conditions

- [ ] **T2.1** Add **C3 — Flehmig-style precedent**: three states, graduated *oversight* intensity, full advisory scope at intermediate level. This is the external baseline. *(Highest-value single change for answering Review 3.)*
- [ ] **T2.2** Document explicitly that C1 *is* the "remove `A_AI`" ablation, resolving F8.
- [ ] **T2.3** Restate the remaining distinct ablations: hysteresis removal (needs Category G), `max_≻` → mean/majority (needs Categories D and E).

### 2B. Scenario set

- [ ] **T2.4** Re-derive Categories A–C under the resolved model. Primary vessel class = `small` (deployment population); `big` as contrast set.
- [ ] **T2.5** Category D — add vessel-boundary cases: same `o` value classifying differently across vessel classes.
- [ ] **T2.6** Rename Category E "Adversarial" → **"Non-compensation"** (F10).
- [ ] **T2.7** Fix SC-20 note (F9).
- [ ] **T2.8** **New Category F — Fail-safe**: six scenarios, one per component set to ⊥, each verifying `f(E) = UNSAFE` (F5).
- [ ] **T2.9** **New Category G — Temporal sequences**: 3–4 multi-timestep sequences crossing a threshold repeatedly; verify hysteresis suppresses chattering (F6).

### 2C. Metrics

- [ ] **T2.10** Demote "decision consistency" from metric to implementation smoke test (F11).
- [ ] **T2.11** Add execution-timing measurement per condition to substantiate TABLE IV and the "CAUTION cheaper than SAFE" claim (F12).
- [ ] **T2.12** Keep Safety Dominance compliance as primary, per-scenario, non-statistical. *(Current framing is correct — preserve it.)*

### 2D. Traceability

- [ ] **T2.13** Add scenario → theorem matrix (F13):

  | Theorem | Scenarios |
  |---|---|
  | 1 (Totality) | All, plus Category F for the ⊥ extension |
  | 2 (Monotonicity) | A vs. B vs. C under C2 — output sets strictly contract |
  | 3 (Safety Dominance) | All scenarios under C2, row by row |

---

## Stage 3 — Propagate

Blocked by: Stage 1 (formal changes) — can run parallel with Stage 2.

> **Scope corrected 2026-09-06 after repo-wide triage.** The original plan listed only the two manuscripts. A grep for `g_v` / `S_v` / aggregation forms / threshold values found **20 affected files**. Revised order runs canonical → justification → implementation → papers, because the canonical and justification layers currently contradict `appendix-c`, and CLAUDE.md names the justification files as mandatory checks on any variable change.

### Triage results

| Tier | File | Issue | Status |
|---|---|---|---|
| **1 Canonical** | `canonical/architecture-illustration.md` | Six-term formula; 5 worked scenarios with `S_v`; **6 pre-existing misclassifications** (see below) | ✅ 2026-09-06 |
| | `canonical/evaluation-design-rq4.md` | Threshold refs — covered by Stage 2 rewrite | ☐ deferred |
| | `canonical/traceability-table.md` | **Not a false positive.** `m` and `o` swapped vs. Appendix C; consistency checklist certified the mismatch as verified; 4 stale paths | ✅ 2026-09-06 |
| **2 Justification** | `justification/formal-model.md` | **`m`/`o` swapped** (2nd occurrence); six-term formula; 2 of 3 worked examples had wrong trigger attributions | ✅ 2026-09-06 |
| | `justification/safety-state-design.md` | `v` as "vessel condition"; six-term formula; **rainfall thresholds wrong** (moderate → CAUTION); `g_v` row disagreed with then-canonical appendix-c | ✅ 2026-09-06 |
| | `justification/viva-formalisation-architecture.md` | **Worst file found.** 3 mutually inconsistent wind threshold sets; source misattributed to MMEA throughout; `v` called "vessel condition" with invented thresholds; {LOW,MEDIUM,HIGH} vocabulary; malformed example vectors; six-term aggregation | ✅ 2026-09-06 |
| | `justification/ai-necessity.md` | Essentially clean — threshold-looking numbers are hypothetical illustrations of rule-based alternatives, not canonical claims. One boundary nit fixed | ✅ 2026-09-06 |
| | `justification/low-resource-environments.md` | One error — "max-severity across six component classifications" | ✅ 2026-09-06 |
| **3 Implementation** | `implementation/dataset-label-derivation.md` | Vessel-blind label logic would have **mislabelled training data** for the deployment population; **tide conflated with `o`**; unresolved wind-value contradiction; appendix-c cross-reference inaccurate | ✅ 2026-09-06 |
| | `implementation/data-source-met-malaysia.md` | Rainfall thresholds wrong (2nd occurrence); vessel-blind wave bands; **2 scenario rows wrong under the old model too**, one internally inconsistent with the document's own Ribut Petir definition | ✅ 2026-09-06 |
| **4 Papers** | `journal-1/.../manuscript.md` | §5.2 `v` role + GRT; §5.3 Def 5.4 Table 1 + new Table 1b; Three-Tier paragraph restructured per tier; **`g_v` justification paragraph replaced with parameterisation rationale**; Def 5.5 five terms; §5.7 symbol table; §6.2 Theorem 6.1 five cases with product-domain argument | ✅ 2026-09-06 |
| | `journal-1/section-5-plan.md` | 4 `g_v`; `max-severity(s1..s6)` pseudo-code | ☐ |
| | `journal-1/section-6-plan.md` | Numbering adaptation table | ☐ |
| | `ipsci-2026/.../manuscript-v3.md` | **Forked ✅ 2026-09-06.** v2.5 frozen with a provenance header; v3 carries a lineage + pending-work header. 4 `g_v` refs incl. Algorithm 1 still to fix | ☐ content |
| | `ipsci-2026/supervisor-feedback-response.md` | 2 refs in the algorithm block | ☐ |
| **5 Historical** | `docs/MASTER_LOG.md` | Records of past changes — **append, do not rewrite** | ☐ |
| | `journal-1/session-log.md` | Historical — leave; note supersession in next entry | ☐ |
| | `ipsci-2026/submissions/archive/*` | Archived versions — leave untouched | — |
| | `scripts/README.md`, root `README.md` | 1 threshold ref each — likely cosmetic, verify | ☐ |

### Notable finding — `architecture-illustration.md` was internally inconsistent, and corroborates the new thresholds

On inspection the walkthrough contained **six** misclassifications, not two. Its scenarios used a threshold set matching neither its own §5.2 table nor `appendix-c`:

| Scenario | Doc said | Correct under current model |
|---|---|---|
| 13:00 | `w = 18 kn → CAUTION` | **SAFE** — CAUTION starts above 22 kn |
| 13:00 | `r = moderate → CAUTION` | **SAFE** — moderate is in the SAFE set |
| 16:30 | `r = heavy → UNSAFE` | **CAUTION** — only storm is UNSAFE |
| 18:30 | `w = 12 kn → SAFE (below 15 kn threshold)` | SAFE, but **no 15 kn threshold exists** — it is 22 kn |
| 13:00 | `o = 1.3 m → CAUTION` | SAFE for big; **CAUTION for small** ✓ |
| 16:30 | `o = 2.5 m → UNSAFE` | CAUTION for big; **UNSAFE for small** ✓ |

The first four are straightforward errors, likely predating the MET Malaysia threshold anchoring.

The last two are the interesting ones. Both were **wrong under the vessel-blind model in force when written** and are **correct under the new small-vessel row**. All four wave heights in the document (0.5, 0.8, 1.3, 2.5) classify correctly under the small-vessel thresholds. Whoever wrote those scenarios was reasoning with small-vessel intuitions the formal model did not support — independent corroboration of the 1.0 / 1.9 boundaries, arrived at before this analysis existed.

**Applied:** all scenarios recomputed with `v = small` (the domain-typical case), `S_v` lines removed, five-term aggregation, and a correction notice at the head of §7 recording what changed. The 06:15 scenario now carries a note that a small vessel reaching SAFE was impossible under the superseded model.

### Second finding — `traceability-table.md` had `m` and `o` swapped, and certified it as verified

Table 1 defined `m = sea state (wave height/swell)` and `o = official marine warning level`. Appendix C.1 defines the opposite: `m` = marine warning level, `o` = ocean state. Canonical order is confirmed by the mnemonic (**m**arine, **o**cean), by every `g_o` threshold in the corpus being a wave height, and by `docs/analysis/content-audit-check3-analysis.md`, which records the correct pairing.

Worse, the Consistency Checklist contained this row:

> *"Parameter definitions in E are consistent across Appendix C and this traceability table | ✓ Both use {w, r, m, o, v, t} with matching definitions (wind, rainfall, **sea state, official warning**, vessel category, time of day)"*

The check listed the definitions **in the swapped order** and passed itself. A verification instrument certifying its own error — arguably more dangerous than the error, since it would deter anyone from re-checking.

Verified the swap did not propagate: a repo-wide grep found it only in this file.

**Applied:** Table 1 row 1 corrected with full canonical definitions; row 2 updated to the five-term form showing `g_o(o, v)`; the false checklist row rewritten to record what it previously certified; three new checklist rows added (no `g_v`; `g_o` rows match across canonical docs; illustration scenarios classify correctly — the check whose absence let six misclassifications survive); four stale paths fixed (`docs/justification-layer3-enforcement.md`, `docs/rq5-study-design.md`, `docs/evaluation-design-rq4.md` → `docs/canonical/...`); the C0/C1/C2 row marked ⚠ pending re-verification after the Stage 2 rewrite.

### Third finding — `viva-formalisation-architecture.md` carried three different wind threshold sets

The viva defence document had more errors than the three canonical documents combined. Most consequential, because these are answers intended to be delivered verbally under examination:

| Location | Stated | Canonical |
|---|---|---|
| HR-5 (hysteresis example) | CAUTION at 25 kn, return below 22 | CAUTION at 22 kn |
| HR-10 (threshold errors) | `w > 25 → CAUTION`, `w > 35 → UNSAFE` | `22 < w ≤ 27 → CAUTION`, `w > 27 → UNSAFE` |
| PD-1 (calibration) | Force 4 (>13 kn) CAUTION, Force 6 (>22 kn) UNSAFE | as above |

Three mutually inconsistent sets, none matching C.2. An examiner cross-checking any answer against the appendix would find a different number each time.

Further errors:

- **Source misattributed to MMEA throughout** (7 occurrences). The thresholds derive from **MET Malaysia** — the meteorological department, not the enforcement agency. MMEA does not publish these criteria.
- **`v` described as "vessel condition"** with thresholds "derived from pre-departure checklist standards in Malaysian maritime regulations." `v` is vessel *category* (size) and has no thresholds of its own.
- **Severity vocabulary** {LOW, MEDIUM, HIGH} in EC-1, EC-3, EC-4, PD-2, AD-6 — canonical is {SAFE, CAUTION, UNSAFE}.
- **Malformed example vectors** in EC-7: `{w=20, r=15, m=ADVISORY, o=MODERATE, v=GOOD, t=DAY}` — rainfall as an integer, ocean state as an ordinal label, `v = GOOD`. Does not typecheck against Definition C.1.
- **Fail-safe mechanism misdescribed** — presented as a per-variable HIGH default flowing through max-severity, rather than a guard applied before any gᵢ evaluation. The distinction matters for Theorem C.1.
- **Six-term aggregation** in HR-6 and EC-5.

**Applied:** canonical threshold table and source attribution added to the header; revision notice listing every corrected error; all three wind threshold sets reconciled; MMEA → MET Malaysia throughout; `v` role corrected in PD-1, HR-7, EC-5; severity vocabulary normalised; EC-7 vectors rebuilt as well-typed examples; fail-safe rewritten as a pre-condition guard in EC-1, EC-4, PD-2, PD-4, AD-6; HR-6 given a dedicated note on why `v` parameterises rather than votes. Three *viva one-liners* were among the corrected lines.

### Fourth finding — the `m`/`o` swap was NOT isolated

`justification/formal-model.md` carried the same swap as the traceability table: `m ∈ ℝ≥0 × ℝ≥0 — sea state`, `o ∈ {none, advisory, warning, alert} — official marine warning level`.

An earlier note in this plan claimed the swap had been verified as isolated. **That verification was wrong** — the grep pattern used (`m = sea state`) matched only the equals-sign form and missed this file's `m ∈ ... — sea state` phrasing. Corrected with a broader pattern.

The same file's three worked CAUTION examples also carried wrong trigger attributions independent of the swap:
- E₁ annotated "triggered by wind" at w = 20 kn — 20 kn is SAFE; the actual trigger was wave height
- E₃ annotated "marine warning + vessel category + time" — only the marine warning contributes; t = 6.0 is SAFE and `v` does not vote

A fourth example was added to exercise the vessel parameterisation, which none of the originals did.

**Broader scope note:** 68 files reference the E vector, mostly notes and archived drafts. A full audit of all of them is out of scope for this plan; the active canonical, justification, implementation, and paper layers are the priority. Recommend a follow-up pass over `docs/obsolete/`, `docs/chapters/archive/`, and `publications/**/archive/` only if those are ever revived.

### Fifth finding — `safety-state-design.md` rainfall thresholds were wrong

Independent of the vessel work: the reference threshold table classified **moderate rainfall as CAUTION**. Canonical is SAFE = {none, light, moderate}, CAUTION = {heavy}, UNSAFE = {storm}. The table also used mm/hr bands (< 5, 5–20, > 20) that do not appear in the canonical categorical definition.

Its `v` row (SAFE = {medium, big}, CAUTION = {small}) additionally disagreed with the *then-canonical* appendix-c (SAFE = {big}, CAUTION = {small, medium}) — so the superseded `g_v` was itself specified inconsistently across documents before removal.

### Journal 1 — `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md`

- [ ] **T3.1** §5.2 Definition 5.1 — `E` vector if `v` role changed.
- [ ] **T3.2** §5.3 Definition 5.4 (`gᵢ`) — `g_o` parameterisation; remove or restate `g_v`.
- [ ] **T3.3** §5.3 Definition 5.5 (`f(E)`) — aggregation set if `g_v` removed from the max.
- [ ] **T3.4** §5.3 Table 1 — threshold table.
- [ ] **T3.5** §5.3.2 — empirical support paragraph for `g_o` (Yaakob et al. now supports vessel-conditional thresholds directly, a stronger claim than before).
- [ ] **T3.6** §5.7 Table 4 — symbol table.
- [ ] **T3.7** §6.2 Theorem 6.1 — per-component totality verification for parameterised `g_o`.
- [ ] **T3.8** Verify §6.3 and §6.4 unaffected.

### Conference paper — `publications/active/ipsci-2026/submissions/v2-post-review/manuscript-v2.5-submitted.md`

**Note:** fork to `v3-revision/` before editing further — v2.5 is the submitted record and has already been edited this session.

- [ ] **T3.9** Fork current file to `submissions/v3-revision/manuscript-v3.md`.
- [ ] **T3.10** **Fix Fig. 4 panel 1** (F3) — `v = small` cannot be SAFE under current model; recheck all three panels under the revised model.
- [ ] **T3.11** Domain Instantiation — `E` definition.
- [ ] **T3.12** Formal Properties — Theorem 1 proof sketch if `g_o` parameterised.
- [ ] **T3.13** Algorithm Specification — Algorithm 1 inline threshold comments.
- [ ] **T3.14** Threats to Validity — internal validity paragraph now cites vessel-conditional thresholds; strengthen.
- [ ] **T3.15** Fix TABLE II reference numbers per `revision-notes.md` (six wrong citations — Review 1's "check the comparative table").
- [ ] **T3.16** Replace acknowledgment placeholder ("Will be add later!").

---

## Stage 4 — Execute

Blocked by: Stages 1–3.

- [ ] **T4.1** Implement the classifier `f(E)` and the four conditions C0–C3.
- [ ] **T4.2** Implement `RS(SAFE)` and `RS(CAUTION)` rule sets.
- [ ] **T4.3** Run all scenarios × 4 conditions; record per the verification protocol.
- [ ] **T4.4** Run ablations (hysteresis removal, `max_≻` replacement).
- [ ] **T4.5** Collect timing data (T2.11).
- [ ] **T4.6** Verify: 100% Safety Dominance compliance under C2, every scenario individually.
- [ ] **T4.7** Verify: C2 ≠ C1 in every CAUTION scenario (the discriminator).
- [ ] **T4.8** Verify: C3 produces full scope under CAUTION (the novelty demonstration).

---

## Stage 5 — Integrate results

Blocked by: Stage 4.

- [ ] **T5.1** Journal 1 §10 — evaluation design writeup.
- [ ] **T5.2** Journal 1 §11 — results tables.
- [ ] **T5.3** Journal 1 §12 — ablation results.
- [ ] **T5.4** Conference v3 — compressed results section; update Conclusion future-work paragraph to past tense for completed items.
- [ ] **T5.5** Update Threats to Validity in both papers — "prototype fidelity" claim can now cite actual compliance figures.

---

## Deferred / not in scope

| Item | Reason |
|---|---|
| Point 11 — redraw Figs 3 and 4 as vector graphics | Do after Fig. 4 content is corrected (T3.10); no point rendering a figure that's wrong |
| Point 12 — expand LR methodology | Only if a reviewer requests; text already exists in `2026-07-16-ipsci-paper-v4-revision.md` §3.1–3.3 |
| RQ5 user study | Separate track; design in `rq5-study-design.md` |
| Venue decision for conference paper | Revisit after Stage 4 — results change what venues are viable |

---

> ## ⚠️ Superseded in part — see `docs/canonical/decision-record-empirical-first.md`
>
> This plan was written before the classifier was run against site data. Stage 2 (evaluation redesign) assumed the 20-scenario design would be patched. The 2026-09-06 historical replay changed that: **`g_w` never fires in five years**, and the superseded vessel-blind `g_o` never produced UNSAFE at all.
>
> **Stages 0, 1 and 3 (Tiers 1–3) stand as executed and verified.** Stage 2 is superseded — the evaluation is now built on historical replay over 43,848 hourly records rather than 20 constructed scenarios, and the classifier specification itself is open pending diagnostic analysis. See the decision record for open questions Q1–Q5.

## Status at a glance

| Stage | Scope | State |
|---|---|---|
| **0 — Decisions** | D1–D4 | ✅ Complete |
| **1 — Formal model** | T1.1–T1.7 | ✅ Complete |
| **3 — Propagate: Tier 1 canonical** | 3 files | ✅ 2 done, 1 deferred to Stage 2 |
| **3 — Propagate: Tier 2 justification** | 5 files | ✅ Complete |
| **3 — Propagate: Tier 3 implementation** | 2 files | ☐ **NEXT** |
| **3 — Propagate: Tier 4 papers** | 5 files | ☐ Blocked on T3.9 (fork conference paper) |
| **3 — Propagate: Tier 5 historical** | 4 files | ☐ Append-only |
| **2 — Evaluation redesign** | T2.1–T2.13 | ☐ Recommended before Tier 4 |
| **4 — Execute** | T4.1–T4.8 | ☐ |
| **5 — Integrate results** | T5.1–T5.5 | ☐ |

**Findings:** 13 from the original audit (F1–F13) + 12 discovered during propagation (F14–F25). All F14–F25 are fixed; F3–F13 are Stage 2/3 work.

## Critical path

```
D1 → D2/D3/D4 → T1.1–T1.7 → Tier 1 → Tier 2 → Tier 3 → T2.4 → Tier 4 → T4.* → T5.*
       ✅          ✅          ✅       ✅       ▓░░     ░░░      ░░░
```

Rationale for the ordering: canonical and justification layers first, because they were contradicting `appendix-c` and CLAUDE.md names the justification files as mandatory checks. Evaluation scenario re-derivation (T2.4) is recommended **before** Tier 4 papers, so the new thresholds are tested against concrete cases before being written into manuscripts.

---

## Progress log

### 2026-09-06 — Session 1

**Analysis phase.** Audited `evaluation-design-rq4.md` against canonical definitions; found 13 issues (F1–F13). Investigation of F1 escalated into a formal model defect requiring resolution before any evaluation work.

**Key analytical corrections made during the session** — recorded because two intermediate positions were wrong and should not be re-derived:

1. **Invalid extrapolation.** Hs_KIMO was initially evaluated at 5.03 m and 6.54 m LOA, producing 0.66 m and 0.82 m. Jeong & Im's Table 11 runs from **10 m upward**; the formula was not validated below that and the authors do not apply it there. Their actual recommendation for ≤10 m vessels is 1.0 m (Table 12). Proposed thresholds were corrected accordingly.

2. **Misquoted Yaakob limits.** The figures 0.875 m and 1.875 m are the sea states at which the boats *fail*. The **operational limits** are Hs ≈ 0.5 m (5.03 m vessel, SS2 ceiling) and Hs ≈ 1.25 m (6.54 m vessel, SS3 ceiling).

3. **Notes file endorsed the old design.** `notes/Stability, Seakeeping...md` §4.2 explicitly argues for `g_v(small) = CAUTION always`, stating these vessels "should never receive full-scope AI advisory output in any sea state." This prompted an intermediate recommendation (Option 2b: keep `g_v` as a floor, parameterise only the UNSAFE boundary). Ultimately rejected — the "never SAFE" property is the note-writer's architectural inference rather than a claim of Yaakob et al., and it is precisely what renders the contribution unobservable in-domain. **T1.7 exists to mark this note as superseded.**

**Implementation phase.** T1.1–T1.4 applied to `appendix-c-formalisation.md`, plus new section C.9. Verified by grep that no stale `g_v` / six-component references remain and that all `max-severity` occurrences are consistent.

**Files modified:** `docs/canonical/appendix-c-formalisation.md`, `CLAUDE.md`, `docs/reference/explainer-per-component-classification-functions.md`, `notes/Stability, Seakeeping and Safety Assessment...md`, this plan.

**Stage 1 complete.** `g_v` removed from the formal model and every downstream reference resolved. Two load-bearing theorems (C.2 Monotonicity, C.3 Safety Dominance) verified unaffected; only C.1 Totality required amendment.

---

### 2026-09-06 — Session 2: Triage and propagation (Tiers 1–2)

**Triage.** Repo-wide grep found 20 affected files, against the 2 the original plan listed. Reordered Stage 3 into five tiers, canonical first.

**Tier 1 — canonical.** `architecture-illustration.md` (F16) and `traceability-table.md` (F14, F15, F25) corrected. `evaluation-design-rq4.md` deferred to the Stage 2 rewrite.

**Tier 2 — justification.** All five files audited; four required changes. `viva-formalisation-architecture.md` was the worst single file in the repo (F17–F21).

**Corrections to earlier claims in this plan** — recorded so they are not trusted on re-reading:

1. An earlier entry stated the `m`/`o` swap had been "verified as isolated" to `traceability-table.md`. **That verification was faulty.** The grep pattern (`m = sea state`) matched only the equals-sign form and missed `formal-model.md`'s `m ∈ ℝ≥0 × ℝ≥0 — sea state`. Re-run with a broader pattern; two occurrences total.

2. The `architecture-illustration.md` finding was initially reported as **two** misclassifications. On full inspection there were **six** — four of them unrelated to the vessel work and predating the MET Malaysia threshold anchoring.

**Scope decision.** 68 files reference the E vector, mostly notes and archived drafts. Full audit judged out of scope: the active canonical, justification, implementation and paper layers are the priority. Recommend a pass over `docs/obsolete/`, `docs/chapters/archive/` and `publications/**/archive/` only if those are revived.

**Files modified this session:** `canonical/architecture-illustration.md`, `canonical/traceability-table.md`, `justification/viva-formalisation-architecture.md`, `justification/formal-model.md`, `justification/safety-state-design.md`, `justification/ai-necessity.md`, `justification/low-resource-environments.md`, this plan.

**Next:** Tier 3 — `implementation/dataset-label-derivation.md` (cited by appendix-c as the threshold derivation source, so effectively canonical) and `implementation/data-source-met-malaysia.md`. Then T2.4 scenario re-derivation before Tier 4 papers. Tier 4 remains blocked on **T3.9 — fork the conference paper to `v3-revision/`**, since `manuscript-v2.5-submitted.md` was edited during the supervisor-feedback session and no longer matches the submitted record.
