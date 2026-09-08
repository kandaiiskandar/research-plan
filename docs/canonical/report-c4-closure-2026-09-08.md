# Report: SDR-001 Execution Condition C-4 — Model B Design Consequences

**Date:** 2026-09-08
**SDR-001 status:** **APPROVED — NOT YET APPLIED** (unchanged) · **Model B: SELECTED — NOT YET CANONICAL** (unchanged)
**Scope:** C-4 only. C-5 through C-8 not executed. Canonical `g_t` unchanged. No replay, hysteresis, prediction re-resolution or figure generation.

---

# RESULT

# **C-4 CLOSED — MODEL B DESIGN CONSEQUENCES DOCUMENTED**

All ten closure criteria satisfied. **Four files modified, all documentation.** No classifier changed, no sensitivity result promoted to canonical status.

---

## 1. Files inspected

| File | Purpose |
|---|---|
| `docs/canonical/appendix-c-formalisation.md` | Canonical formal source — `gᵢ` type declaration, all theorems, `g_t` table, C.9 |
| `docs/justification/formal-model.md` | The one `f`-surjectivity claim in the project (L287) |
| `docs/reference/explainer-per-component-classification-functions.md` | Component descriptions ("Dusk"/three-state language) |
| `publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md` | Active conference paper — Threats to Validity |
| `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md` | Journal 1 Threats to Validity (§14) |
| `docs/canonical/finding-gt-evidence-closure.md` | SDR-001, execution-condition table |
| `docs/canonical/finding-sdr-001-readiness-audit.md` · `finding-unsafe-semantics-audit.md` | Prior audits — read only, deliberately not rewritten |
| `docs/canonical/architecture-illustration.md` · `evaluation-design-rq4.md` · `CLAUDE.md` | Three-state / graduation language |
| 8 canonical script `g_t` sites | Integrity verification only |

**Precondition verified before editing:** canonical `g_t` = incumbent fixed clock, all three rows present verbatim in Appendix C.

---

## 2. Component-surjectivity finding

**Project-wide search for `surject`, "all three states", "onto {SAFE", "three zones":**

> **No theorem, type declaration, proof, definition or constraint in `appendix-c-formalisation.md` requires any `gᵢ` to be surjective.** The property was always true; it had simply never been written down.

**The risk was presentational, not formal.** Appendix C presents `g_t` as a three-row table beside `g_o` and `g_r`, and the C.1 note described "three governance zones". Neither is a formal dependency, but a reader meeting a two-valued component beside three-valued ones would reasonably read it as an omission. That is why the readiness audit and the evidence closure both called for an explicit statement — **and it is what C-4 required.**

---

## 3. Exact formal statement added

Added to `appendix-c-formalisation.md` **C.2**, immediately after the `gᵢ` type declaration, as a subsection **"Component classifiers are not required to be surjective"**:

> **The declaration `gᵢ : Xᵢ ∪ {⊥} → 𝒮` states a *codomain*, not an image.** It fixes the set from which gᵢ draws its values. It does **not** assert
>
> **Im(gᵢ) = 𝒮**
>
> and no result in this appendix requires that. A component classifier may therefore satisfy
>
> **|Im(gᵢ)| < |𝒮|**
>
> while remaining **well typed and total**. Totality is a requirement on the *domain* — every input receives exactly one output — and is independent of how many distinct outputs are actually produced. **Totality ≠ surjectivity**, and it is totality that Theorem C.1 and Theorem C.1b establish.

Accompanied by a per-result verification table (§10 below) and the statement that **no proof obligation changes if a component's image shrinks**, so no proof required re-verification.

A clearly-labelled subsection records the approved design:

> **Approved replacement design, pending canonical migration — `g_t` under Model B**
> **This subsection describes a design decision that is APPROVED but NOT YET CANONICAL. The canonical `g_t` is the incumbent fixed-clock classifier defined below (06:00 / 17:00 / 19:00) and is unchanged.**
> … **Im(g_t) = {SAFE, UNSAFE}** and **CAUTION ∉ Im(g_t)** — **by deliberate design, not by oversight.**

**The canonical `g_t` definition itself was not touched.**

---

## 4. `f` surjectivity finding and resolution

**Finding.** Exactly one surjectivity claim exists in the project, in **non-canonical prose**: `docs/justification/formal-model.md` L287 —

> *"The classification function f: D_E → {SAFE, CAUTION, UNSAFE} is **surjective** and many-to-one."*

**Scope analysis.** The claim is legitimate only as an *empirical* statement about the deployed configuration:

| | Status |
|---|---|
| **Codomain** `{SAFE, CAUTION, UNSAFE}` | ✅ Unconditional — what the signature states |
| **Empirical image at `D = {m}`** (the configuration actually run) | ✅ All three states occur — but this is a property of the site and exclusion set, not a structural guarantee |
| **Structural surjectivity over every admissible `D`** | ❌ **Not claimed and not required.** Lemma C.1c permits `D = {w, r, m, o}`, where the classifier reduces to a time curfew; under the approved two-valued `g_t` that configuration leaves CAUTION unreachable and `f` non-surjective — while remaining total and theorem-compliant |

**Resolution.** The sentence was **qualified, not deleted**. "Surjective" was removed from the unconditional assertion; "many-to-one" — which is true unconditionally — was retained. A dated three-row table now separates codomain, empirical image, and the absence of any theorem requiring surjectivity, closing with: *"Totality is the property the architecture requires; surjectivity is not."*

**No theorem was altered**, because no theorem contained the claim.

---

## 5. System-level graduation verification

**Documented in Appendix C C.2 under "Where graduation lives":**

> "Graduated" is a **system-level governance property**, not a requirement that each component independently realise every state. It holds because
>
> **A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅**  (C.4, Corollary C.2)
>
> and because CAUTION is reachable in 𝒮 — at this site principally through `g_o` and `g_r` (F-7). **Whether any single `gᵢ` realises CAUTION is a property of that component and its evidence, not of the architecture.**

The global state space `𝒮 = {SAFE, CAUTION, UNSAFE}` is unchanged, and the containment property is untouched.

---

## 6. The 2,091-hour CAUTION interpretation

**Labelled everywhere it appears as approved-design evidence, never as a canonical result:**

> "in the approved **Model B sensitivity result** (approved-design evidence, **not** a canonical figure) **2,091 of 43,848 PRIMARY hours — 4.77% — remain globally CAUTION, all weather-driven**. **The canonical figures remain 7.72% (PRIMARY) / 5.98% (RESOLUTION).**"

**What it establishes:** CAUTION is not marginal under the approved design. 2,091 hours over five years, every one produced by `g_o` or `g_r` — the two components that already produced essentially all of it (`g_o` alone accounts for 98.66% of daylight CAUTION under the incumbent).

**What it does not establish:** any canonical figure. It is a counterfactual computed by non-canonical analysis code, and the canonical binding rates are unchanged.

---

## 7. Exact step-cost disclosure

Recorded in a new **Appendix C §C.9.5, "Accepted transition cost of the approved `g_t` replacement design"**, with the figures stated without softening:

| | Incumbent (canonical) | Approved design (sensitivity) |
|---|---|---|
| **Direct SAFE→UNSAFE transitions** | **2** | **1,536** |
| **`g_t`-driven SAFE→CAUTION transitions** | **1,545** | **0** |

**Framing — as required, an accepted design trade-off:**

- **Not described as a defect.** No formal property is violated; the step is monotone under Theorem C.2 and no theorem constrains transition paths.
- **Not described as harmless.** *"The tension is real and is between this component's behaviour and the architecture's graduated-governance narrative."*
- **Not described as physically discontinuous.** *"Nothing physical, meteorological or physiological is claimed to be discontinuous there. What changes discontinuously is the governance response."*
- **Recorded as a disclosure obligation:** *"This cost is a disclosure obligation, not a defect to be argued away."*

The section is explicitly scoped: *"Applies to the approved replacement design, which is NOT YET CANONICAL."*

---

## 8. Threats to Validity — wording and location

**Location:** `publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md`, §Threats to Validity, inserted as a fifth threat between Internal and External validity — the paragraph a reader reaches immediately after the threshold-provenance discussion and before the domain-transfer discussion.

**Why this document, and only this one.** C-4 requires the disclosure to exist in Threats to Validity; the instruction requires modifying the minimum necessary. `manuscript-v3.md` is the **active** conference submission and the document where the graduated-governance claim is most prominently made. **Journal 1's §14 was inspected and deliberately not modified** — it is a v1 initial submission, and propagating the disclosure across manuscripts is **C-8**, recorded there rather than pre-empted here.

**All six required elements present:**

| Element | Wording |
|---|---|
| **Boundary step** | *"That classifier transitions directly between SAFE and UNSAFE, with no intermediate value."* |
| **Magnitude** | *"direct SAFE→UNSAFE transitions rise from **2 to 1,536**, while time-driven SAFE→CAUTION transitions fall from **1,545 to 0**."* |
| **Interpretation** | *"follows from removing an intermediate time band for which no evidence was found … not from any claim that conditions change discontinuously at sunset; nothing physical, meteorological or physiological is asserted to be discontinuous there."* |
| **Architectural consequence** | *"the discontinuity is confined to the time component: the architecture remains globally three-state, with CAUTION reached through the wave and rainfall classifiers in 2,091 of 43,848 hours (4.77%) … all weather-driven, and the containment property … untouched."* |
| **Usability concern** | *"predictable withdrawal of advisory support at sunset may warrant anticipatory interface support, which is a notification concern separate from the safety-state classifier."* |
| **Evidence limitation** | *"three reviews located no source supporting a twilight CAUTION state"* and *"deliberately not addressed by inventing an intermediate state to smooth the transition."* |

**Canonical/sensitivity separation stated in the paragraph itself:** *"The figures in this paragraph are counterfactual sensitivity results for the approved design; the classifier characterised elsewhere in this paper is the incumbent fixed-clock one, and the reported binding rates (7.72% / 5.98%) are computed under it."*

The paragraph also opens by acknowledging the tension directly — *"The architecture's central argument is that graduated governance is preferable to a binary step, and under this design the most predictable transition of the day becomes a step"* — rather than burying it.

---

## 9. Anticipatory-notification separation

Recorded in a new **Appendix C §C.9.6, "Anticipatory notification is not a safety state"**:

> **current governance state ≠ future-state notification**

A deterministic pre-event notice — *"AI advisory will become unavailable at [sunset time]"* — **may be investigated later**. If adopted it would be: deterministic, computed from the stored solar timestamps (C-3 artefact); **not** AI-generated reasoning, so it cannot violate Theorem C.3; **not** a safety-state classification; **not** CAUTION; **not** part of SDR-001's classifier semantics.

**No warning interval was specified.** Explicitly recorded:

> *"No value — 15 minutes, 30 minutes, an hour — has any independent justification in this project, and inventing one would repeat the error the `g_t` provenance audit was opened to correct. **No new threshold is introduced.**"*

**No UI behaviour was implemented.**

---

## 10. Theorem compatibility verification

**Targeted verification, not a new formal audit.** Each result checked for a dependency on component surjectivity:

| Result | Requires component surjectivity? | Reason |
|---|---|---|
| **Definition C.1** (severity order) | ❌ No | An order on the three-element set 𝒮 — fixed by |𝒮|, not by any component's image |
| **Theorem C.1** (ideal totality) | ❌ No | Requires each `gᵢ` **total** and each partition **exhaustive**. A two-interval partition of [0, 24) satisfies this identically |
| **Theorem C.1b** (operational totality) | ❌ No | Totality plus `gᵢ(⊥) = UNSAFE` |
| **Corollary C.1b.1** (fail-safe) | ❌ No | Only `gᵢ(⊥) = UNSAFE` and ≻-maximality of UNSAFE |
| **Lemma C.1c** (monotone degradation) | ❌ No | Only the ⪯ ordering under `D ⊆ D′` |
| **Theorem C.2** (monotonicity of A_AI) | ❌ No | Quantifies over `S₁, S₂ ∈ 𝒮`; never mentions `gᵢ` |
| **Theorem C.3** (Safety Dominance) | ❌ No | *"depends only on the value of S, never on how S was reached"* (C.7.2) |
| **`G(S)`** | ❌ No | Defined on `S` alone, after aggregation |
| **`A_AI(S)`** | ❌ No | Defined on `S` alone |
| **max-severity** | ❌ No | Only the total order ≻ on 𝒮 |
| **(D1) `t ∉ D`** | ❌ No | Independent of `Im(g_t)` |

> **No proof obligation changes. No proof was rewritten.** The reasons are the three the condition anticipated: totality ≠ surjectivity; governance properties quantify over global `S`; Safety Dominance depends on the state reached, not on the path or the component image.

---

## 11. Documents modified — 4

| File | Change |
|---|---|
| `docs/canonical/appendix-c-formalisation.md` | **C.2:** non-surjectivity subsection, "Where graduation lives", labelled approved-design subsection, "Aggregation" heading restored. **New C.9.5:** accepted transition cost. **New C.9.6:** anticipatory notification separation |
| `docs/justification/formal-model.md` | L287 `f` surjectivity claim qualified — codomain / empirical image / no theorem requirement |
| `publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md` | Threats to Validity — new fifth threat, six required elements |
| `docs/canonical/finding-gt-evidence-closure.md` | C-4 row marked CLOSED in the execution-conditions table |

Plus this report. **No script, dataset, artefact or register entry touched.**

---

## 12. Historical artefacts deliberately not rewritten

**No earlier audit was edited to appear to have known the final design from the beginning.** All were read-only inputs:

| Document | Left unchanged because |
|---|---|
| `finding-gt-provenance-audit.md` | Records that the incumbent values have no source — the origin of the sequence |
| `finding-gt-operational-semantics.md` | Records that evidence supports two states, not three |
| `finding-gt-sensitivity-analysis.md` | Produced the 2 → 1,536 and 2,091 figures being disclosed here |
| `finding-unsafe-semantics-audit.md` | Identified the `f` surjectivity claim; its diagnosis is now acted on, but its text stands |
| `finding-sdr-001-readiness-audit.md` | Called for the non-surjectivity statement; already carries dated status annotations |
| `cleanup-report-*`, `approval-report-*`, `report-c1-c2-c3-*`, `report-c2-closure-*` | Sequential records of each step |

**The preserved sequence:** provenance audit → semantics audit → readiness audit → C-0 → approval → C-1/C-2/C-3 → **C-4**.

---

## 13. Canonical / sensitivity distinction

**Every Model B figure introduced in this task carries an explicit label.**

| Figure | Status as recorded |
|---|---|
| **7.72% (PRIMARY), 5.98% (RESOLUTION)** | ✅ **CANONICAL** — authoritative, unchanged, restated in Appendix C C.2 and in the manuscript paragraph |
| 2 → 1,536 · 1,545 → 0 | **Model B sensitivity / approved-design evidence** |
| 2,091 CAUTION hours (4.77%) | **Model B sensitivity result — "not a canonical figure"** |
| 5.81% / 4.48% | Not introduced anywhere in this task |

**`empirical-findings-2026-09-06.md` §0a was not touched.** Verified: 7.72% appears 8×, 5.98% appears 5×, unchanged.

---

## 14–17. Condition status

| | Condition | Status |
|---|---|---|
| **C-1** | Pin solar implementation and reproducibility parameters | ✅ **CLOSED** — unaffected; `solar-spec-v1`, 116.01, `solar-v1`, hash all preserved |
| **C-2** | Complete 28-row USNO validation artefact | ✅ **CLOSED** — unaffected; artefact unchanged (`da14a8dc…`); `V_historical` / `V_reconstructed` untouched |
| **C-3** | Daily solar-event artefact | ✅ **CLOSED** — unaffected; artefact unchanged (`057c46a1…`) |
| **C-4** | Document Model B design consequences | ✅ **CLOSED** — see below |

### C-4 closure test — all ten criteria

| # | Criterion | Met |
|---|---|---|
| 1 | Binary `g_t` documented as an approved design position | ✅ Appendix C C.2, labelled "approved replacement design, pending canonical migration" |
| 2 | Component classifiers explicitly not required to be surjective | ✅ C.2 formal statement + 10-row verification table |
| 3 | Global three-state graduation shown intact | ✅ "Where graduation lives"; containment property; 2,091 CAUTION hours |
| 4 | `f` surjectivity prose correctly scoped | ✅ `formal-model.md` L287 qualified into three distinct claims |
| 5 | 2 → 1,536 recorded as accepted design cost | ✅ C.9.5 + manuscript Threats to Validity |
| 6 | 1,545 → 0 recorded | ✅ C.9.5 + manuscript Threats to Validity |
| 7 | Threats to Validity contains the disclosure | ✅ `manuscript-v3.md`, six required elements |
| 8 | Anticipatory notification separated from CAUTION | ✅ C.9.6; no interval invented |
| 9 | No canonical classifier changed | ✅ Incumbent `g_t` intact in Appendix C and all 8 script sites |
| 10 | No sensitivity result presented as canonical | ✅ Every figure labelled; §0a untouched |

**All ten satisfied.**

---

## 18. C-5 through C-8 — confirmed OPEN

| | Condition | Status |
|---|---|---|
| **C-5** | Three-stage hysteretic re-run for P12 | 🔴 **OPEN — not executed.** `classify_hysteretic()` not run; hysteresis not ported to v2; P12 not computed |
| **C-6** | Re-resolve affected predictions | 🔴 **OPEN — not executed.** No prediction re-resolved |
| **C-7** | Reconcile baseline discrepancies | 🔴 **OPEN — not executed.** P07 87.58/88.23, P10 230/227, P11 37/70, P12 7.83/6.17 all untouched |
| **C-8** | Execute the propagation list | 🔴 **OPEN — not executed.** No canonical `g_t` conversion; 8 scripts and remaining documents untouched. **Journal 1 Threats to Validity disclosure recorded here as a C-8 item** |

Verified: 4 conditions remain marked OPEN in the SDR.

---

## 19. Prediction-register integrity

> ### **BYTE-FOR-BYTE UNCHANGED — `sha256 538808b6d82249fa…`**
> Matches the integrity anchor exactly. **24 entries · 22 CONFIRMED / 2 REFUTED.** No record altered.

---

## 20. Canonical `g_t` integrity

> **`g_t^canonical` = `g_t^incumbent`**
> SAFE 06:00 ≤ t < 17:00 · CAUTION 17:00 ≤ t < 19:00 · UNSAFE 19:00 ≤ t < 24:00 or 00:00 ≤ t < 06:00

All three rows verbatim in Appendix C.

**All 8 canonical script `g_t` implementations unchanged, verified by hash:**

`canonical_figures.py` `5af9eaf7…` · `condition_comparison.py` `1f0f4e9c…` · `diagnostic_binding.py` `69bc2bd6…` · `hysteresis_analysis.py` `73015d88…` · `historical_replay.py` `dd6a6c3f…` · `compare_v1_v2.py` `8e977c90…` · `threshold_decision.py` `d051cac4…` · `threshold_comparison.py` `7e799b5f…`

**Also unchanged:** `solar.py` `3b7dc371…` · solar artefacts `da14a8dc…` / `057c46a1…` · wind `21.6/27.0` · rainfall `10.0/20.0` · wave `{small:(1.0,1.25), medium:(1.4,2.8), big:(1.5,3.5)}` · `cause : Y → {fault, hazard}` · `G(S)` · `A_AI(S)` · canonical figures 7.72% / 5.98%.

**SDR-001 remains APPROVED — NOT YET APPLIED. Model B remains SELECTED — NOT YET CANONICAL.**

---

## 21. Assessment

C-4 asked for documentation, and the substantive work was deciding **what could honestly be claimed**.

The non-surjectivity property was true all along; writing it down cost nothing formally and removes a misreading a reviewer would otherwise reach for. The `f` surjectivity sentence was the opposite case — a claim that was *true in the deployed configuration and false in a permitted one*, and the right repair was to scope it into three separate statements rather than delete it or leave it.

**The step cost is the part that matters.** 2 → 1,536 sits in direct tension with the paper's central argument, and the disclosure says so in its first sentence rather than after three qualifications. What the qualifications do is bound the claim correctly: the discontinuity is in the *governance response*, not in the world; it is confined to one component; and the alternative — inventing a twilight CAUTION band — was rejected because no evidence supports it, which is the same discipline that produced the `g_t` audit in the first place.

**The temptation C-4 exists to resist** is smoothing the step by adding a state. That would have made the architecture look more consistent and would have been unsupported. Keeping the step and disclosing it is the honest outcome, and C.9.6 records why the usability concern belongs to notification logic rather than to the classifier.

---

# **C-4 CLOSED — MODEL B DESIGN CONSEQUENCES DOCUMENTED**

**C-1 CLOSED · C-2 CLOSED · C-3 CLOSED · C-4 CLOSED · C-5 through C-8 REMAIN OPEN.**
**SDR-001 remains APPROVED — NOT YET APPLIED. Canonical migration has not begun.**
