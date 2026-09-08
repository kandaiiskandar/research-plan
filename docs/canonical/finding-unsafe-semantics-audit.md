# Finding: `UNSAFE` Semantics and `cause` Provenance — Read-Only Consistency Audit

**Date:** 2026-09-08
**Type:** Read-only formal consistency audit. **Nothing modified.**
**Question:** Is the proposed solar-triggered `g_t` (Model B) compatible with the architecture *as it currently exists*?
**Predecessors:** `finding-gt-provenance-audit.md` · `finding-gt-operational-semantics.md` · `finding-gt-sensitivity-analysis.md` · `finding-gt-evidence-closure.md` (draft SDR-001)

**Model B was not assumed correct.** Where the audit found the specification pointing away from Model B, that is recorded rather than reconciled. Section 13 states the integrity check.

**Epistemic labels used throughout:**
**[PROVES]** what the formal specification establishes · **[EVIDENCE]** what an empirical source supports · **[POLICY]** an architectural design choice · **[INTERPRETATION]** my reading, not the project's text.

---

## 1. Canonical definition of `UNSAFE`

**Result: Interpretation U3 — mixed — but with a strong and important asymmetry. The formal apparatus is uniformly U2 (governance). The prose is mixed, and the mixing is already a known, partially-corrected defect.**

### 1.1 What the formal layer says — uniformly U2

`UNSAFE` is never given a standalone definition. It is defined **only** by its position in an order and by what the governance functions do with it.

| Location | Text | Reading |
|---|---|---|
| `appendix-c-formalisation.md` **Definition C.1**, line 91–93 | `UNSAFE ≻ CAUTION ≻ SAFE` — a total strict order on a three-element set | Purely ordinal. No semantic content at all |
| **C.2**, line 117 | `S ∈ {SAFE, CAUTION, UNSAFE}` | An element of a codomain |
| **C.3**, line 548–554 | `G(S) = 0 if S = UNSAFE`; `G(S) = 0 → AI disabled` | **U2** |
| **C.4**, line 581 | `A_AI(S) = ∅ if S = UNSAFE` | **U2** |
| **C.2.0.8**, line 258 | "Governance treats them identically — `G(UNSAFE) = 0` either way" | **U2** |

**[PROVES]** In the formal model `UNSAFE` is a *label on a governance configuration*. Nothing in C.1–C.8 attaches a physical claim to it. The three states are distinguished formally **only** by `(G(S), A_AI(S))` and by their position under `≻`.

### 1.2 The one canonical statement that settles it

`appendix-c-formalisation.md` **C.9.4**, line 873:

> **The severity ordering reflects operating envelopes, not survivability.** UNSAFE denotes conditions outside the demonstrated operating envelope for the vessel category. The seakeeping sources characterise their limits as the sea state at which criteria are breached or heavy manual work becomes unsafe; **none characterises any threshold as a survivability boundary, and this document does not claim one.**

**This is canonical, current, and was added deliberately on 2026-09-08 by the claim sweep.** It is the project's own explicit repudiation of U1 in its strong form.

### 1.3 Where the mixing actually is

Definition C.1 itself, line 95, is the hinge:

> "UNSAFE represents conditions in which **departure lies outside the demonstrated operating envelope** for the vessel category **and** no AI advisory output is permissible"

This is a **conjunction of a world claim and a governance claim**. It is the single most authoritative sentence about what `UNSAFE` means, and it asserts both. **[INTERPRETATION]** The world-claim half is deliberately weakened relative to U1 — "outside the demonstrated operating envelope" is an epistemic statement about the limits of the evidence, not a claim that operation is unsafe. But it is still a claim about the world, and it is stated as *co-constitutive* of `UNSAFE` rather than as a typical cause of it.

**This matters for Model B specifically**, because Model B introduces an `UNSAFE` whose world-claim half would be **empty**: night is not "outside the demonstrated operating envelope for the vessel category" in the sense C.1 means (a wave-height/wind envelope from seakeeping analysis). See §5.

### 1.4 Verdict

| | |
|---|---|
| **U1 — physical claim** | **Explicitly disclaimed** in its strong form (C.9.4 line 873). Present in weakened form in Definition C.1 line 95 and in three prose sites (§10) |
| **U2 — governance claim** | **The whole of the formal apparatus.** C.3, C.4, C.6, C.7, C.8.2, C.2.0.8 |
| **U3 — mixed** | **Accurate as a description of the document set**, but the mixing is *asymmetric*: formalism U2 throughout, prose partially U1, and the project has already begun correcting toward U2 |

**[PROVES]** The formal specification supports **U2 only**. **[INTERPRETATION]** U1 survives in prose as residue, not as specification.

---

## 2. Operational consequence of `S = UNSAFE`

**Traced through the canonical pipeline, C.8.2, lines 795–820:**

```
obs ──ρ_{D,τ}──▶ y ──f(·,v)──▶ S ──▶ ( G(S), A_AI(S) ) ──▶ AI ──▶ Human Decision
```

### 2.1 The two guarantees

| Guarantee | Status | Location |
|---|---|---|
| `G(UNSAFE) = 0` | ✅ **By definition, not derivation** | C.3, line 549 |
| `A_AI(UNSAFE) = ∅` | ✅ **By definition, not derivation** | C.4, line 581 |
| `G(S) = 0 ⇒ A_AI(S) = ∅` | ✅ Constraint, satisfied trivially by the two definitions | C.6 Participation Constraint, line 624 |
| `AI = ∅` when `S = UNSAFE` | ✅ **Theorem C.3, Case 1** — derived from (A3) | C.7.2, lines 736–741 |

Both are **stipulated definitions**, not theorems. Theorem C.3 Case 1 is the derived part: it shows the *rule engine's output* is empty, given the gate.

### 2.2 The five-way test

| Does `S = UNSAFE` … | Answer | Support |
|---|---|---|
| **1. Suppress AI advisory only?** | ✅ **Yes — this is the entire effect** | C.3 + C.4 + Theorem C.3 Case 1 |
| **2. Prohibit the human from operating?** | ❌ **No.** Nothing in C.1–C.8 constrains the human | C.8.2 step 6, line 818 |
| **3. Block human override?** | ❌ **No — explicitly the opposite** | C.8.2 step 6: *"Human decision. **Unconditional**; the operator may act contrary to any recommendation."* |
| **4. Make a physical safety claim?** | ⚠️ **Not in the formalism.** Partially, in prose | C.9.4 line 873 disclaims it; Definition C.1 line 95 half-asserts it |
| **5. Other effect?** | ⚠️ **One, and it is outside the formal model** | See §2.4 |

### 2.3 Human override — corroborated across five documents

| Location | Text |
|---|---|
| `appendix-c-formalisation.md` C.8.2 step 6, line 818 | "Human decision. **Unconditional**; the operator may act contrary to any recommendation" |
| `architecture-illustration.md` line 141 | "The human operator retains final decision authority **in all three states**… **The governance layer constrains the AI, not the human**" |
| `journal-1/.../manuscript.md` line 327 | "Layer 4 represents human authority, which is unconditional… The governance pair constrains what the AI **can say**; it does not constrain what the human **can decide**" |
| `ipsci-2026/.../manuscript-v3.md` line 506 | "the architecture governs advisory scope, not final decisions. **Human override is unconditional**" |
| `supervisor-feedback-response.md` line 213 | "The architecture governs advisory scope — not final decisions. Human override is unconditional" |

**[PROVES] Human override is unconditional in every state including UNSAFE, stated consistently in five documents with no contradicting instance found.** This is the single most robust semantic commitment in the project, and it is the one that does the work in §5.

### 2.4 The one effect outside the formal model

`architecture-illustration.md` line 143 and line 546 describe a **deterministic Layer-2 alert** that fires under `UNSAFE` — *"Dangerous conditions — return to shore"*, *"dangerous conditions — do not depart"*. The document is careful that this preserves `A_AI(UNSAFE) = ∅` because the message originates in the governance layer, not `AI(E)`.

**[PROVES]** Formally sound — the containment guarantee is untouched.
**[INTERPRETATION]** Semantically this is the *only* place in the architecture where `S = UNSAFE` produces something that reads as a claim about the world, and it is where Model B does real damage. See §10.

---

## 3. Model B — formal compatibility (Q3A)

**Result: fully compatible. No formal obstacle of any kind.**

| Requirement | Does a binary `g_t : X_t → {SAFE, UNSAFE}` satisfy it? |
|---|---|
| **Type** `gᵢ : Xᵢ ∪ {⊥} → {SAFE, CAUTION, UNSAFE}` (C.2, line 274) | ✅ A codomain declaration, not an image declaration. A function into a three-element set need not hit all three |
| **Totality** (Theorem C.1, line 480–494) | ✅ Requires each `gᵢ` **total**, not surjective. The `g_t` case (line 470) argues only that its intervals partition `[0, 24)` exhaustively. Two intervals partition it identically |
| **Operational totality** (Theorem C.1b, line 502–526) | ✅ Unaffected. Depends on `gᵢ(⊥) = UNSAFE` and on `max-severity` totality |
| **Fail-safe** (Corollary C.1b.1, line 530) | ✅ Requires `g_t(⊥) = UNSAFE`, which is the uniform ⊥ rule, independent of the value branches |
| **`max-severity`** (Definition C.1, line 91) | ✅ Depends only on the order `≻`, not on any component's range |
| **`G(S)`, `A_AI(S)`** (C.3, C.4) | ✅ Defined on `S`, reached only after aggregation. Blind to component structure |
| **Theorem C.2 Monotonicity** (line 641) | ✅ Quantifies over `S₁, S₂ ∈ S`. No reference to `gᵢ` |
| **Theorem C.3 Safety Dominance** (line 705) | ✅ "**The proof depends only on the value of S, never on how S was reached**" (line 734) |
| **`t ∉ D` (D1)** (C.2.0.5, line 209) | ✅ Preserved — a solar `g_t` still reads the device clock |

**[PROVES] No theorem, type declaration, proof or constraint in Appendix C requires any `gᵢ` to be surjective.**

### 3.1 One surjectivity claim exists — and it survives

The previous evidence closure reported zero surjectivity hits. **That search was scoped to Appendix C and missed one instance.**

`docs/justification/formal-model.md` line 287:

> "The classification function `f: D_E → {SAFE, CAUTION, UNSAFE}` is **surjective** and many-to-one."

**Classification:** non-canonical explanatory prose, about **`f`**, not about any `gᵢ`.

**It survives Model B** — `CAUTION` remains reachable through `g_o` (98.66% / 97.41% of daylight CAUTION) and `g_r`. Model B removes time-driven CAUTION, not CAUTION.

**[INTERPRETATION]** But it is now a load-bearing claim in a way it was not before, and it interacts with **Lemma C.1c** (C.9.4 line 881): at `D = {w, r, m, o}` the classifier reduces to a night curfew. Under Model B that degenerate configuration would make `f` **non-surjective**, falsifying this sentence. It is false-in-a-corner today too (that configuration yields only SAFE/UNSAFE under the current `g_t` as well, since `g_t`'s CAUTION band would be the sole CAUTION source and *is* present — so today it survives, and under Model B it would not). **Reported, not fixed.**

---

## 4. Evidence versus governance policy (Q4)

**This is the load-bearing distinction in the audit.**

### 4.1 What the sources establish

| Proposition | Established? | Source |
|---|---|---|
| Night navigation carries **elevated** accident probability and consequence | ✅ **[EVIDENCE]** | Atacan & Düzbastılar 2023: 4.08 vs 3.43 probability; 12.80 vs 8.53 consequence (`appendix-c` line 43) |
| Sunset↔sunrise is an authoritative **maritime operating boundary** | ✅ **[EVIDENCE]** | COLREGs Rule 20(b), navigation lights "from sunset to sunrise" (`finding-gt-operational-semantics.md` line 13, 29) |
| Night navigation is **physically unsafe / impossible** | ❌ **Not established, and contradicted by practice** | Atacan & Düzbastılar establish elevated risk, not impossibility; fishers demonstrably operate at night |
| **Night ⇒ AI advisory must be suppressed** | ❌ **No source establishes this** | See below |

### 4.2 The implication has no source — and the project already says so

`finding-gt-operational-semantics.md` line 123, in the project's own words:

> "night = UNSAFE — ✅ Supported as *elevated risk*. **Whether it warrants full AI withdrawal is an architecture decision, not an evidence finding.**"

**[PROVES-by-exhaustion]** Three prior reviews searched five priority tiers. COLREGs regulates **navigation lights**, not decision support. Atacan & Düzbastılar studied **accident risk perception**, not advisory systems. No corpus paper conditions AI advisory scope on time of day — indeed the entire gap argument (Chapter 2, line 129) rests on *no system anywhere* conditioning advisory scope on environmental state.

**Therefore: `night ⇒ suppress AI advisory` is an architectural governance policy choice. It is not an evidence-derived safety fact.** This holds for Model B and — worth stating — **equally for the incumbent fixed-clock `g_t`**. Model B does not introduce the policy character; it inherits it. The incumbent's boundaries are, if anything, *worse* off, being neither evidence-derived nor regulation-derived (`finding-gt-provenance-audit.md`).

### 4.3 Does the specification permit policy-defined conservative rules?

**Yes, and abundantly. Four independent precedents, all canonical:**

1. **Conservative over-approximation is the stated design principle.** `appendix-c` line 77 (Corsi et al.; Newcomb & Ochoa): the classifier "may over-classify (producing false CAUTION or false UNSAFE)" and this is the standard safety guarantee.
2. **Conservative bias is stated as accepted practice.** `appendix-c` line 79 (Perez-Cerrolaza et al.): safety mechanisms "calibrated to err on the side of restriction".
3. **A threshold is already labelled an interpretation rather than a source claim.** C.9.1 line 838: the 1.25 m small-vessel boundary — "Yaakob et al. do not characterise either value as a departure prohibition; **treating the operational ceiling as the gate is an interpretation**".
4. **A threshold is already labelled a design decision.** C.9.1 line 840: the 2.8 m medium-vessel boundary is "**Interpolated**… No corpus source provides a medium-vessel UNSAFE threshold."

**[PROVES]** The architecture already contains `UNSAFE` boundaries that are policy-defined and labelled as such. **A policy-defined `g_t` would be consistent with existing practice, not a departure from it — provided it is labelled the same way.** That proviso is the whole of the requirement.

---

## 5. Model B — semantic compatibility (Q3B)

**Result: the formal model is silent; the surrounding prose currently communicates the wrong one of the three claims.**

### 5.1 The three claims, separated

| # | Claim | Status |
|---|---|---|
| **1** | "Night navigation presents **elevated operational risk**." | ✅ **[EVIDENCE]** Atacan & Düzbastılar |
| **2** | "Night navigation is **physically unsafe**." | ❌ **False.** Not supported by any source; contradicted by fisher practice |
| **3** | "The architecture **conservatively abstains from AI advisory participation** during night operation." | ✅ **[POLICY]** — an available and defensible design position (§4.3) |

### 5.2 Which does the model actually communicate?

**Split, and the split is the finding.**

**The formal model communicates claim 3 and nothing else.** `S = UNSAFE` sets `G(S) = 0`, `A_AI(S) = ∅`, `AI = ∅`, and leaves the human unconstrained (§2). That *is* conservative abstention, stated formally. **[PROVES]**

**The prose currently communicates claim 2.** Under Model B, at 18:30 on a flat-calm evening, a fisher would be shown:

- *"Dangerous conditions — return to shore"* — `architecture-illustration.md` line 143
- *"dangerous conditions — do not depart"* — `architecture-illustration.md` line 546

**These are false statements about the world in that scenario.** The sea is calm, the wind is 8 knots, and it is 18:30. The architecture has not detected danger; it has detected sunset.

The incumbent `g_t` blunts this only by accident — its 19:00 boundary means the message fires an hour later, when it is genuinely dark. **The defect exists today; Model B enlarges it and makes it structural** (time-driven UNSAFE rises from 41.2% to 100% of the night interval's non-SAFE hours, and time-driven CAUTION → 0, so *every* evening transition becomes a direct SAFE→UNSAFE step: 2 → 1,536, per `finding-gt-sensitivity-analysis.md`).

### 5.3 Does Model B make a claim stronger than the evidence supports?

**The architecture does not. Three documents do.**

**[INTERPRETATION]** This is a prose defect with a formal system underneath it that is already correct. The distinction matters because it determines the remedy: nothing in Appendix C's theorems needs changing, but the operator-facing message and two explanatory passages state something the model does not.

---

## 6. Current `cause` taxonomy

**Canonical signature — `appendix-c-formalisation.md` C.2.0.8, line 262:**

> **`cause : Y → {fault, hazard}`**, with **`cause(y) = fault`** if `yᵢ = ⊥` for any `i ∉ D`, and **`hazard`** otherwise

**Confirmed:** the prompt's stated form matches the project. Two values, no more.

**Complete inventory of `cause` in the project** (searched `cause :`, `cause(`, `cause(y)`, `cause(E)`, `{fault, hazard}`):

| Location | Role |
|---|---|
| `appendix-c` C.2.0.8, lines 260–266 | **Canonical definition** |
| `appendix-c` C.8.2, line 820 | Canonical pipeline restatement — "provenance only, with no effect on `G(S)` or `A_AI(S)`" |
| `appendix-c` Summary table, line 898 | Symbol index |
| `CLAUDE.md` line 194 | Type table |
| `finding-gt-evidence-closure.md` lines 137, 154 | Prior report of the mismatch |

**`cause` appears in no script.** It is specified and unimplemented. **[PROVES]** — grep across `scripts/` returns zero hits.

**Definitional structure worth naming:** `hazard` is **the residual category**, defined as "otherwise". It is not defined positively as "an environmental hazard was detected". This is doing real work in §7 Case C.

---

## 7. Cases A / B / C

### Case A — Environmental hazard
`g_o = UNSAFE` because wave height exceeds the supported operating envelope. All observations valid, `D = {m}`.

**`cause(y) = hazard`** — no `yᵢ = ⊥` for `i ∉ D`.
**Verdict: ✅ Compatible.** This is the paradigm case the taxonomy was written for.

### Case B — Runtime data fault
`o = ⊥ ⇒ g_o(⊥) = UNSAFE` (C.2, line 274; Corollary C.1b.1, line 530).

**`cause(y) = fault`** — `o ∉ D` and `y_o = ⊥`.
**Verdict: ✅ Compatible.** This case is *why* `cause` exists — C.2.0.8 line 258 states the motivating scenario: an operator told *"conditions are unsafe"* when the truth is *"the wave feed is down"* has been misinformed.

### Case C — Nighttime under Model B
All environmental observations valid and non-UNSAFE; `t ≥ sunset ⇒ g_t = UNSAFE`.

**What the taxonomy assigns: `hazard`** — no component is `⊥`, so the "otherwise" branch fires.

**Is `hazard` semantically correct? No.**

| Property | Environmental hazard (Case A) | Sunset (Case C) |
|---|---|---|
| Predictable years ahead | ❌ | ✅ To the minute, from `(date, lat, lon)` |
| Stochastic | ✅ | ❌ Deterministic astronomy |
| Could have been otherwise tonight | ✅ | ❌ |
| Resolves by waiting a **known** interval | ❌ | ✅ Sunrise, computable now |
| Detected by a sensor | ✅ | ❌ Computed from a clock and an ephemeris |
| Indicates something has **gone wrong** | ✅ | ❌ Nothing has gone wrong |

**Classification: genuine semantic mismatch.**

**Why — precisely.** The `fault`/`hazard` partition is built on **one distinction: did the measurement apparatus fail?** It has no place for a third thing that is neither an apparatus failure nor a detected environmental condition: a **scheduled, deterministic, policy-triggered** state change. Sunset is that third thing. Assigning it `hazard` is not a rounding error; it is a category error, and it produces an operator log reading *"UNSAFE — hazard"* every single evening at sunset, 1,536 times over the replay period, when nothing hazardous has occurred and nothing was detected.

**Not "awkward but defensible"**, because the resulting record is *actively misleading in exactly the way C.2.0.8 was written to prevent*. The document's own stated rationale — that an operator "has been misinformed about the world" — applies verbatim.

**No new category is proposed here.** Per instruction, this is reported. **[INTERPRETATION]** The mismatch is a genuine defect but a *small and self-contained* one; §12 sizes it.

### 7.1 The mismatch is not created by Model B

Under the incumbent `g_t`, 19:00 already produces `cause = hazard` on a calm night — the same category error, 1,536 times a year. **Model B does not introduce the defect. It removes the last cover for it**, because under Model B the boundary is *explicitly* an astronomical event rather than a clock number that could be loosely narrated as "when it gets dark and rough". **This is a pre-existing defect that Model B makes undeniable.**

---

## 8. Does `cause` affect governance?

**Result: provenance only. Verified three ways, no counter-instance.**

| Check | Result |
|---|---|
| Stated directly | C.2.0.8 line 264: "**`cause` has no effect on `G(S)` or `A_AI(S)`** — it is provenance, not governance, and **the formal properties are untouched by it**" |
| Stated again in the canonical pipeline | C.8.2 line 820: "provenance only, with no effect on `G(S)` or `A_AI(S)`" |
| **`G(S)` signature** | C.3, line 548: `G` takes `S` alone. `cause` is not an argument |
| **`A_AI(S)` signature** | C.4, line 578: `A_AI` takes `S` alone |
| **Theorem C.3 proof** | Line 734: "The proof depends only on the value of `S`, never on how `S` was reached… **`cause` is provenance and does not enter the case analysis**" |
| **Implementation** | `cause` appears in zero scripts |

### 8.1 Consequence of the Case C mismatch — scoped, not overstated

| Domain | Affected? |
|---|---|
| **Safety behaviour** | ❌ **No.** `G(UNSAFE) = 0` and `A_AI(UNSAFE) = ∅` fire identically. The gate closes correctly |
| **Formal theorem validity** | ❌ **No.** C.1, C.1b, C.1b.1, C.2, C.3 are all independent of `cause`. C.3's proof says so explicitly |
| **Empirical figures** | ❌ **No.** `cause` is unimplemented; 7.72% / 5.98% do not depend on it |
| **Explainability / provenance / operator record** | ✅ **Yes — and this alone** |

**[PROVES] The mismatch is confined entirely to explainability and the audit record. It has no safety consequence and invalidates no theorem.**

**[INTERPRETATION]** That said, "explainability only" is not "cosmetic" in *this* thesis. The architecture's claim is that graduated governance communicates something to the operator that binary governance cannot (`architecture-illustration.md` line 141; Chapter 2 line 131). A provenance field that says `hazard` when the truth is `sunset` undercuts precisely the communicative function the contribution rests on. The consequence is bounded, and within its bounds it is not trivial.

---

## 9. Compatibility of `cause` with Model B

`cause` requires no change for Model B to function. It would, however, be **wrong more often and more visibly**: from an evening-transition frequency of roughly 365/yr under the incumbent to the same frequency under Model B but with an explicitly astronomical trigger, and with the SAFE→UNSAFE step count rising 2 → 1,536 (`finding-gt-sensitivity-analysis.md`), every one of them logged as `hazard`.

---

## 10. Legacy contradiction sweep

Searched: `must not depart`, `should not depart`, `not survivable`, `survivab`, `cannot operate`, `prohibit`, `no human override`, `override`, `AI determines whether… safe`, `nighttime… unsafe`, `do not depart`, `too dangerous`, `conditions are unsafe`, `insufficient daylight`. Across `docs/`, `publications/`, `scripts/`, `papers/`, `CLAUDE.md`. **Nothing fixed.**

### 10.1 Genuine remaining contradictions — 4

| # | Location | Text | Why it contradicts |
|---|---|---|---|
| **L1** | `architecture-illustration.md` **line 143** | *"the governance layer… may still display a deterministic safety alert (e.g., **'Dangerous conditions — return to shore'**)"* | Asserts danger. Under Model B, false on a calm evening. **Under the incumbent it is already false at 19:00 on a calm night** |
| **L2** | `architecture-illustration.md` **line 546** | *"pre-defined safety alerts (e.g., **'dangerous conditions — do not depart'**)"* | Same defect, and this one is imperative — the closest thing in the project to "the fisher must not depart", against unconditional override in five documents (§2.3) |
| **L3** | `viva-formalisation-architecture.md` **line 241** | *"Only under UNSAFE does the AI go silent, and in that state **no maritime authority recommends fishing activity**"* | An empirical claim about maritime authorities. **False for night**: no Malaysian or international authority prohibits night fishing, and COLREGs Rule 20(b) *presupposes* night operation by mandating lights for it. Already shaky under the incumbent; Model B makes it plainly false |
| **L4** | `appendix-c-formalisation.md` **Definition C.1, line 95** | *"UNSAFE represents conditions in which **departure lies outside the demonstrated operating envelope** for the vessel category and no AI advisory output is permissible"* | **Canonical and current.** Conjoins a world claim with the governance claim. Under Model B the world-claim half is vacuous for the time component — night is not an envelope exceedance |

**L4 is the most consequential**, being the canonical definition. **L1 and L2 are the most visible**, being operator-facing.

### 10.2 Already corrected — 2

| Location | Status |
|---|---|
| `appendix-c` **C.9.4 line 873** — "operating envelopes, not survivability" | ✅ **The correction.** Added 2026-09-08 by the claim sweep. **Directly contradicts L4 within the same document**, and is the later and more considered statement |
| `appendix-c` **C.9.1 lines 838, 840** | ✅ Threshold interpretations labelled as interpretations |

### 10.3 Historical / stale — 3 (`g_t`-adjacent, not `g_t`-caused)

| Location | Status |
|---|---|
| `viva-formalisation-architecture.md` lines **335, 337, 345** | **Stale.** State the fail-safe as "a **pre-condition** evaluated before any classification function runs" / "a guard applied before any `gᵢ`". Superseded by Corollary C.1b.1 (derived, not stipulated). **The document's own header line 28 already carries the correction; the body was not updated** |
| `viva-formalisation-architecture.md` line **181** | **Stale.** `22 < w ≤ 27` — superseded by 21.6 |
| `docs/obsolete/`, `docs/chapters/archive/`, `v1`/`v2` submissions | **Historical.** Correctly located; no action |

### 10.4 Non-canonical explanatory prose — 3

| Location | Note |
|---|---|
| `justification/formal-model.md` line 287 | `f` surjective — §3.1 |
| `justification/formal-model.md` line 29 | Repeats the 06:00/17:00/19:00 bands and the 7.90 restricted-visibility conflation |
| `reference/explainer-per-component…md` lines 28, 45, 72 | "Daytime / Dusk / Nighttime" — three-state `g_t` |

### 10.5 Claims **not** found — the sweep's negative result

**Searched for and absent from the entire project:**

- ❌ "UNSAFE means departure is not survivable" — **zero hits.** C.9.4 line 873 explicitly disclaims it
- ❌ "fisher must not depart" / "should not depart" (as a system claim) — **zero hits**
- ❌ "AI determines whether fishing is safe" — **zero hits**
- ❌ "no human override" / any override restriction — **zero hits.** Five documents assert the opposite

**[PROVES] The strongest U1 formulations do not exist in this project.** What survives is the weaker envelope language of L4 and the operator-facing alert text of L1/L2.

### 10.6 Incidental, unrelated to `g_t` — reported not fixed

`docs/canonical/evaluation-design-rq4.md`: **SC-07** and **SC-18** use categorical `r` (`heavy`, `moderate`), superseded by the 2026-09-08 numeric redefinition; **SC-16/SC-17** label the wind boundary "22 kn", superseded by 21.6 (both scenario *outcomes* still hold at 21.6). Pre-existing, independent of this audit.

---

## 11. Final outcome

# **Outcome B — Compatible only with clarification**

**Not Outcome A.** Model B is formally compatible without any semantic change (§3), but Outcome A would require that no clarification is needed. Four sites currently communicate physical unsafety (§10.1), and under Model B two of them become plainly false statements shown to an operator on a calm evening. Selecting A would mean shipping a system whose displayed message contradicts its own specification.

**Not Outcome C.** Model B requires **no change to the formal meaning of `UNSAFE`**. The formalism already means exactly "governance abstention" (§1.1, §2), and C.9.4 line 873 already disclaims the survivability reading. The clarifications needed are to **prose that was already wrong** — L1 and L2 are false at 19:00 on a calm night under the *incumbent* `g_t`. Model B exposes an existing defect; it does not create a new semantic requirement.

**Not Outcome D.** No material conflict exists. The gate closes correctly, every theorem holds unchanged, human override is preserved, and §4.3 shows the architecture already contains policy-defined `UNSAFE` boundaries labelled as such. The `cause` mismatch (§7) is real but confined to provenance (§8) and is pre-existing (§7.1).

### 11.1 The decisive reasoning

**[PROVES]** The formal architecture *already* supports governance abstention — that is all `S = UNSAFE` has ever done in the formalism. **[PROVES]** Human override is unconditional in all three states, asserted in five documents with no counter-instance. Together these mean Model B asks the architecture for nothing it does not already provide.

**[INTERPRETATION]** The gap is entirely between what the formal model means and what the prose says it means. That gap predates Model B. Model B is what makes it impossible to keep ignoring.

### 11.2 Stated against interest

Two findings in this audit **do not favour Model B**, and are recorded as found:

1. **Definition C.1 line 95 (L4) is the canonical definition of the severity order, and its world-claim half is vacuous under Model B.** A reviewer could reasonably press on this. The answer is that C.9.4 line 873 already narrows it — but that answer requires the reader to prefer a limitations section over a definition, which is not automatic.
2. **The `cause` mismatch (§7) is genuine, not cosmetic within its scope**, and Model B increases its visibility. It is bounded to provenance, but the thesis's contribution claim is partly communicative (§8.1).

Neither is disqualifying. Both belong in the record.

---

## 12. Exact changes required if Model B were later approved

**Scoped to `UNSAFE` semantics and `cause`.** For thresholds, scripts, figures, predictions and the full document list, see `finding-gt-evidence-closure.md` Part 8 — this section does **not** duplicate it.

### 12.1 Required — the clarification that Outcome B names

| # | Location | Change |
|---|---|---|
| **1** | `appendix-c` **Definition C.1, line 95** (L4) | Separate the governance claim from the world claim. `UNSAFE` = the state in which AI advisory participation is not admissible. Envelope exceedance is a *typical cause*, not the definition. **This is the single required formal-document edit** |
| **2** | `appendix-c` **C.2 / C.9.4** | Add: component classifiers need not be surjective; `g_t` is deliberately binary; `CAUTION` remains reachable via `g_o` and `g_r`. Prevents a reviewer reading a two-row `g_t` table as an omission (`finding-gt-evidence-closure.md` Part 4.1) |
| **3** | `architecture-illustration.md` **lines 143, 546** (L1, L2) | Replace *"Dangerous conditions — return to shore"* / *"dangerous conditions — do not depart"* with state-reporting text that does not assert danger and does not instruct. **Required regardless of Model B** — false today at 19:00 on a calm night |
| **4** | `viva-formalisation-architecture.md` **line 241** (L3) | Strike or restrict *"no maritime authority recommends fishing activity"*. False for night under either `g_t` |

### 12.2 Consequential

| # | Location | Change |
|---|---|---|
| **5** | `appendix-c` **C.1 line 39** | "insufficient daylight for safe small-vessel operation" — an unsourced physical claim, and the sharpest U1 residue in the canonical document |
| **6** | `appendix-c` **C.1 line 35** | "three safety zones" → two |
| **7** | `appendix-c` **C.2 `g_t` table, lines 464–470** | Two rows; partition argument restated over two intervals |
| **8** | `evaluation-design-rq4.md` **SC-10** (line 131) | **Not in the Part 8 list.** Its *only* CAUTION trigger is `g_t` at 18:00. Under Model B its expected outcome becomes date-dependent (KK sunset 17:57–18:35), so the scenario needs a date or a different trigger. **SC-15 (22:00 → UNSAFE) is unaffected** |
| **9** | `reference/explainer-per-component…md` lines 28, 45, 72 | "Dusk (CAUTION)" removed |
| **10** | `justification/formal-model.md` line 287 | The `f` surjectivity claim — survives at `D = {m}` but fails at `D = {w,r,m,o}` under Model B (§3.1) |
| **11** | Manuscript **Threats to Validity** | The SAFE→UNSAFE step (2 → 1,536) against the architecture's own graduated-governance thesis. Already flagged in the draft SDR |

### 12.3 Explicitly **not** required

| | |
|---|---|
| **Any theorem** | C.1, C.1b, C.1b.1, C.2, C.3 all hold unchanged (§3) |
| **`G(S)`, `A_AI(S)`, `RS(S)`, A1–A4** | Untouched (§2) |
| **The canonical pipeline (C.8)** | Untouched |
| **The formal meaning of `UNSAFE`** | **Unchanged — this is what makes the outcome B and not C** |
| **A new `cause` value** | Not required for Model B to function (§9). The mismatch is pre-existing (§7.1) and should be sequenced **separately, after** the `g_t` decision — bundling would make one decision carry two rationales |

---

## 13. Integrity check

**This was a read-only audit. No file was created other than this finding, and no file was modified.**

| Item | Status | Verification |
|---|---|---|
| Canonical `g_t` | ✅ **UNCHANGED** | `17:00 ≤ t < 19:00` — 1 occurrence in `appendix-c-formalisation.md` |
| Appendix C | ✅ **UNCHANGED** | Read only |
| Canonical pipeline (C.8) | ✅ **UNCHANGED** | Read only |
| Scripts | ✅ **UNCHANGED** | `canonical_figures.py` lines 121–122 still `hour >= 6 / < 17 / < 19` |
| Replay outputs | ✅ **UNCHANGED** | Not executed |
| **7.72% / 5.98%** | ✅ **UNCHANGED** | `empirical-findings-2026-09-06.md` §0a line 24 |
| Sensitivity outputs | ✅ **UNCHANGED** | Not re-run |
| Figures | ✅ **UNCHANGED** | Not regenerated |
| Prediction outcomes | ✅ **UNCHANGED** | P07, P09, P16 all CONFIRMED |
| Prediction register | ✅ **UNCHANGED** | 24 predictions, 22 CONFIRMED / 2 REFUTED |
| **SDR-001 status** | ✅ **STILL DRAFT — NOT APPLIED, NOT APPROVED** | `finding-gt-evidence-closure.md` line 164 |
| `cause` | ✅ **UNCHANGED** | No `policy`/`scheduled` value introduced |
| Model B | ✅ **NOT ADOPTED** | |
| Contradictions L1–L4 | ✅ **REPORTED, NOT FIXED** | |

---

## 14. Sources

**Canonical, this project:** `docs/canonical/appendix-c-formalisation.md` (C.1, Definition C.1, C.2, C.2.0.5–8, C.3–C.8, Theorems C.1/C.1b/C.2/C.3, Corollary C.1b.1, C.9.1/C.9.3/C.9.4) · `docs/canonical/architecture-illustration.md` · `docs/canonical/evaluation-design-rq4.md` · `docs/canonical/finding-gt-provenance-audit.md` · `docs/canonical/finding-gt-operational-semantics.md` · `docs/canonical/finding-gt-sensitivity-analysis.md` · `docs/canonical/finding-gt-evidence-closure.md` · `docs/canonical/empirical-findings-2026-09-06.md` · `CLAUDE.md`

**Non-canonical, this project:** `docs/justification/formal-model.md` · `docs/justification/viva-formalisation-architecture.md` · `docs/reference/explainer-per-component-classification-functions.md` · `docs/implementation/dataset-label-derivation.md` · `publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md` · `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md`

**External, as cited within the project:** Atacan & Düzbastılar (2023) · COLREGs Rule 20(b) · Corsi et al. (2024) · Newcomb & Ochoa (2026) · Perez-Cerrolaza et al. (2024) · Yaakob et al. (2015)
