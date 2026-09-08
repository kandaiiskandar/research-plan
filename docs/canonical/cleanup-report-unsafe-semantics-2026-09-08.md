# Cleanup Report: Pre-Adoption `UNSAFE` Semantic Correction

**Date:** 2026-09-08
**Basis:** `finding-unsafe-semantics-audit.md` — **Outcome B, compatible only with clarification**
**Scope:** Semantic and prose correction only. **Model B not adopted. Canonical `g_t` unchanged. `cause` unchanged. No theorem re-proved.**

The audit found the formal apparatus already correct (uniformly governance-semantic) and the contradictions confined to prose. This cleanup closes that gap. Every edit below changes what a document *says* `UNSAFE` means; none changes what the system *does*.

---

## 1. Files changed — 4

| File | Edits | Canonical? |
|---|---|---|
| `docs/canonical/appendix-c-formalisation.md` | 5 | ✅ Canonical — single source of truth |
| `docs/canonical/architecture-illustration.md` | 3 | ✅ Canonical |
| `docs/canonical/rq5-study-design.md` | 1 | ✅ Canonical |
| `docs/justification/viva-formalisation-architecture.md` | 1 | Non-canonical (viva prep) |

**No script, dataset, figure, replay output or register entry was touched.** Verified: `find scripts data -newermt` returns empty (§8).

---

## 2. Exact semantic changes

### 2.1 The definitional move

**Before:** `UNSAFE` was defined by a **conjunction** — an envelope claim about the world *and* a governance consequence. Envelope exceedance was constitutive.

**After:** `UNSAFE` is defined **solely** by its governance consequence. Envelope exceedance is demoted to *one of three routes* by which the state is reached.

```
BEFORE   UNSAFE  ≜  (departure outside demonstrated operating envelope)
                    ∧ (no AI advisory output permissible)

AFTER    UNSAFE  ≜  the governance state in which AI advisory participation
                    is not admissible:  G(S) = 0  ∧  A_AI(S) = ∅

         reached by ─┬─ route 1: observation outside a supported operating envelope
                     ├─ route 2: fail-safe on a required observation (yᵢ = ⊥)
                     └─ route 3: an explicitly defined conservative governance condition
```

**Route 2 is what makes the old definition untenable, independently of Model B.** A failed wave feed produces `UNSAFE` while the sea is flat. Under the old wording that state *asserted* envelope exceedance, which was simply false.

### 2.2 All three states redefined for symmetry

Defining only `UNSAFE` by governance would have left `SAFE` and `CAUTION` defined by conditions — a new inconsistency. Definition C.1 now carries a table defining all three by their `(G(S), A_AI(S))` configuration.

### 2.3 New: evidence/policy separation (Definition C.1)

A subsection now states that two questions must not be collapsed:

- **Where does the risk boundary fall?** — empirical or regulatory. Sources can settle it.
- **Should AI advisory participation be withdrawn there?** — **architectural governance policy.** It does not follow from the first.

Recorded explicitly: **no source in the corpus establishes `elevated risk ⇒ AI advisory must be suppressed`, for any component.** The architecture's conservative over-approximation principle (C.1 Worst-Case Aggregation Note) makes the withdrawal defensible *as policy* — and it must be labelled as policy where a component's boundary rests on it.

### 2.4 C.9.4 reconciled

C.9.4 previously read "UNSAFE denotes conditions outside the demonstrated operating envelope" — **overstating in the opposite direction from L4**, and directly contradicting the new Definition C.1. Rescoped to constrain what the *envelope route* may claim, which is what the seakeeping evidence actually supports. **The "operating envelopes, not survivability" distinction is preserved verbatim.**

### 2.5 `cause` — pointer added, definition untouched

A marked **OPEN** note added under C.2.0.8 referencing the audit's §7 mismatch. It states the mismatch is pre-existing, provenance-only, requires no theorem re-proof, and is deferred to a separate workstream.

**Confirmed not done:** no `policy` value, no `scheduled` value, no rename of `hazard`, no signature change. Signature verified intact at line 295: `cause : Y → {fault, hazard}`.

---

## 3. Before / after — L1 to L4

### L4 — Definition C.1 (`appendix-c-formalisation.md`) — *canonical, most consequential*

> **BEFORE:** "The ordering reflects increasing operational risk: UNSAFE represents conditions in which **departure lies outside the demonstrated operating envelope for the vessel category and** no AI advisory output is permissible; CAUTION represents marginal conditions…; SAFE represents conditions in which all environmental parameters are within acceptable bounds…"

> **AFTER:** A three-row table —
> **SAFE** — "The governance state in which **full AI advisory participation is admissible**: G(S) = 1 and A_AI(S) = R"
> **CAUTION** — "The governance state in which **AI advisory participation is admissible but restricted**: G(S) = 1 and A_AI(S) ⊊ R"
> **UNSAFE** — "The governance state in which **AI advisory participation is not admissible**: G(S) = 0 and A_AI(S) = ∅"
> — followed by *How UNSAFE is reached* (3 routes), *What UNSAFE does not assert*, and *Evidence and policy are separate claims*.

Explicit non-assertion added: *"It does not assert that operation is physically impossible, prohibited, or unsafe for every operator and vessel."*

### L1 — `architecture-illustration.md` §"What happens under UNSAFE"

> **BEFORE:** `"Dangerous conditions — return to shore"`

> **AFTER:** `"UNSAFE governance state — AI advisory unavailable. Triggered by: wave height 4.0 m (above the configured limit for this vessel). Final decision remains with the operator."`

Carries all four required elements: state · advisory unavailable · reason · retained authority.

### L2 — `architecture-illustration.md` §L1 "Loss of planning capability"

> **BEFORE:** `"dangerous conditions — do not depart"` — the closest thing in the project to an instruction not to depart.

> **AFTER:** `"UNSAFE governance state — AI advisory unavailable. Triggered by: [component and reading]. Final decision remains with the operator."`

Consequential fix in the same section: *"The fisher **knows conditions are dangerous (the system tells them so)**"* → *"The fisher **can see which component triggered the state and what it read**"*. Also *"which A_AI(UNSAFE) = {} **prohibits**"* → *"**excludes**"* — `A_AI` bounds the AI, it does not prohibit anything of the human.

### L3 — `viva-formalisation-architecture.md`

> **BEFORE:** "Only under UNSAFE does the AI go silent, and **in that state no maritime authority recommends fishing activity**."

> **AFTER:** "Only under UNSAFE does the AI go silent, and there **the architecture withdraws advisory participation entirely under its predefined governance policy**."

**Not replaced with another universal claim**, as instructed. The rationale note records that `UNSAFE` is reachable by routes no authority speaks to at all.

### Two further operator-facing hits found by the sweep and fixed

Neither appears in the audit's L-list; both are the same defect class and were caught by the post-edit sweep.

| Location | Before | After |
|---|---|---|
| `architecture-illustration.md` 09:00 scenario | "UNSAFE — AI advisory withdrawn. **Dangerous conditions**: high wind (28 kn)… **Return to shore immediately.**" | "UNSAFE governance state — AI advisory unavailable. Triggered by: wind 28 kn, heavy rain, 2.5 m seas, marine warning active… Final decision remains with the operator." |
| `rq5-study-design.md` DT-UNSAFE | "No AI advisory. **Safety alert: dangerous conditions.**" | "No AI advisory. State notice: *'UNSAFE governance state — AI advisory unavailable. Triggered by: wind 30 kn. Final decision remains with the operator.'*" |

**The RQ5 fix matters more than its size suggests.** That string is the *stimulus participants respond to*. A message asserting danger or instructing the participant would confound the very measurement RQ5 exists to make — whether graduated governance changes reliance behaviour. The old wording risked measuring compliance with an instruction.

In the 09:00 scenario the readings genuinely *do* exceed the envelope, so the trigger is still reported. Only the imperative was removed.

---

## 4. Treatment of "insufficient daylight"

**Determination: yes, an unsupported physical-safety claim. Rewritten.**

The evidence (Atacan & Düzbastılar 2023) establishes night navigation carries **elevated** accident probability (4.08 vs 3.43) and consequence (12.80 vs 8.53). It does not establish that operation is unsafe or infeasible — and small-scale fishers demonstrably operate at night, so the claim was also false on its face.

**Two locations, both corrected. Thresholds untouched.**

| | Before | After |
|---|---|---|
| **C.1 note, SAFE** | "daytime — sufficient daylight for safe operation and return" | "daytime operating condition — full AI advisory scope admissible" |
| **C.1 note, CAUTION** | "approaching darkness — elevated visual risk" | "transition to darkness — elevated visual risk; restricted AI advisory scope" |
| **C.1 note, UNSAFE** | "night — **insufficient daylight for safe small-vessel operation**" | "night-time operating condition — AI advisory participation withdrawn" |
| **C.2 `g_t` table, SAFE** | "Daytime — sufficient daylight for safe operation and return to port" | "Daytime operating condition — the baseline against which Atacan & Düzbastılar measure elevated night-time risk" |
| **C.2 `g_t` table, UNSAFE** | "Night — restricted visibility; …highest accident probability and consequence scores" | "Night-time operating condition — …elevated accident probability (4.08 vs 3.43) and consequence (12.80 vs 8.53) **relative to the daytime baseline**" |

Also changed: "three **safety** zones" → "three **governance** zones".

**The distinction now drawn:** *night-time operating condition* (what the classifier reads) versus *physically unsafe operation* (what no source establishes). Each row names the operating condition and the governance response.

**Two further improvements in the `g_t` table:**

1. The bare figures replace "highest scores", so what the source establishes — **elevated risk relative to a baseline** — is visible rather than compressed.
2. **"restricted visibility" dropped** from the UNSAFE row. Per `finding-gt-operational-semantics.md` §3.2 the 7.90 score belongs to the study's *restricted visibility* scenario, not its *night* scenario; the study and COLREGs treat them as separate hazards. Recorded as an open item in a warning block, not silently resolved.

A warning block on that table now records both open provenance items and points to draft **SDR-001**, flagged **DRAFT — not approved, not applied**.

**No solar terms introduced.** `grep -ci "sunrise|sunset|USNO|Meeus"` on `appendix-c-formalisation.md` → **0**.

---

## 5. Human authority — unconditional, verified after editing

| Location | Status |
|---|---|
| `appendix-c` C.8.2 step 6 | ✅ Intact: "Human decision. **Unconditional**; the operator may act contrary to any recommendation" |
| `architecture-illustration.md` §"Why the fisher always decides" | ✅ Intact and untouched: "The governance layer constrains the AI, not the human" |
| `journal-1` manuscript L327 | ✅ Untouched |
| `manuscript-v3` L506 | ✅ Untouched |
| `supervisor-feedback-response` L213 | ✅ Untouched |

**Strengthened, not merely preserved.** Every operator-facing message now *states* retained authority ("Final decision remains with the operator"). Previously the commitment lived only in specification prose while the displayed messages contradicted it.

**Sweep for override restrictions: zero hits.** No edit implies `S = UNSAFE ⇒ human operation prohibited`. The two surviving "cannot override" strings both constrain the **AI** (`architecture-illustration.md` L35; `paper_extraction_prompt.md` L51), which is correct.

---

## 6. Formal governance behaviour — unchanged

| Invariant | Verified |
|---|---|
| `G(UNSAFE) = 0` | ✅ C.3 unedited — "0 if S = UNSAFE"; "G(S) = 0 → AI disabled" |
| `A_AI(UNSAFE) = ∅` | ✅ C.4 unedited — line 626 |
| Containment `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅` | ✅ 2 occurrences, both intact |
| `G(S) = 0 ⇒ A_AI(S) = ∅` (C.6) | ✅ Unedited |
| **Theorem C.3 / Safety Dominance** | ✅ Statement, A1–A4 and all three proof cases unedited (lines 750–801) |
| **A1–A4** | ✅ Verbatim |
| **Theorem C.1** (ideal totality) | ✅ Unedited |
| **Theorem C.1b** (operational totality) | ✅ Unedited |
| **Corollary C.1b.1** (fail-safe) | ✅ Unedited |
| **Theorem C.2** (monotonicity) | ✅ Unedited |
| **Max-severity aggregation** | ✅ 2 occurrences, both intact |
| Severity order `UNSAFE ≻ CAUTION ≻ SAFE` | ✅ Unedited |
| Canonical pipeline C.8 | ✅ Unedited |

**No theorem requires re-proof.** The reasoning: every theorem quantifies over the *value* of `S`, never over what `S` means. C.7.2 says so in the document's own words — *"The proof depends only on the value of S, never on how S was reached."* Redescribing what the label denotes cannot disturb a proof that never read the label's description.

**Definition C.1's operative content is unchanged.** Its formal role is to fix the strict total order `≻` for max-severity and Theorem C.2. That order is byte-identical. What changed is the *gloss* on each state.

---

## 7. Remaining contradictions after cleanup

### 7.1 Unresolved — 0

**No unresolved contradiction remains within the scope of this task.** All four audit findings (L1–L4) are closed, plus two further instances found by the sweep.

### 7.2 Valid — design-rationale prose, correctly retained

Sweep hits for "dangerous conditions" in `big-questions.md`, `unified-governance.md`, `safety-state-design.md`, `binary-governance-external-evidence.md`, `ai-necessity.md`, `README.md`, `index.md`, `plan-chapter-1-introduction.md`.

**These are valid and were deliberately left alone.** They describe the *class of conditions the architecture is designed for* ("AI should be disabled under dangerous conditions") — a statement about design intent, not a claim that `S = UNSAFE` proves danger in any particular instance. Editing them would be scope creep and would flatten a legitimate distinction.

### 7.3 Historical — correctly located, no action

`docs/obsolete/`, `docs/chapters/archive/`, `v1`/`v2` submissions. Untouched by policy.

### 7.4 Non-canonical, pre-existing, out of scope — reported not fixed

| Location | Issue |
|---|---|
| `viva-formalisation-architecture.md` L335/337/345 | Fail-safe still described as a **pre-condition guard**; superseded by Corollary C.1b.1. The document's own header L28 already carries the correction; the body was never updated |
| `viva-formalisation-architecture.md` L181 | `22 < w ≤ 27` — superseded by 21.6 |
| `justification/formal-model.md` L287 | `f` asserted **surjective** (audit §3.1). Survives at `D = {m}`; would fail under Model B at `D = {w,r,m,o}` |
| `justification/formal-model.md` L29 | Repeats the old 06:00/17:00/19:00 gloss and the 7.90 restricted-visibility conflation |
| `reference/explainer-per-component…md` L28/45/72 | "Daytime / Dusk / Nighttime" |
| `evaluation-design-rq4.md` SC-07/SC-18, SC-16/SC-17 | Categorical `r`; "22 kn" labels |

**All predate this task and none is a `UNSAFE`-semantics contradiction.** Left for their own workstreams — this task was a semantic correction, not a general staleness sweep.

### 7.5 Deferred by instruction

The `cause` taxonomy mismatch (audit §7). Recorded as an OPEN note under C.2.0.8; **not modified**.

---

## 8. Integrity check

| Item | Status | Evidence |
|---|---|---|
| **Canonical `g_t`** | ✅ **UNCHANGED** | `06:00 ≤ t < 17:00` / `17:00 ≤ t < 19:00` / `19:00 ≤ t < 24:00 or 00:00 ≤ t < 06:00` — all three present, values identical |
| **06:00 / 17:00 / 19:00** | ✅ **UNCHANGED** | Only the *basis* column prose was edited |
| **Wind thresholds** | ✅ **UNCHANGED** | `W_CAUTION, W_UNSAFE = 21.6, 27.0` |
| **Rainfall thresholds** | ✅ **UNCHANGED** | `R_CAUTION, R_UNSAFE = 10.0, 20.0` |
| **Wave thresholds** | ✅ **UNCHANGED** | `TH = {"small": (1.0, 1.25), "medium": (1.4, 2.8), "big": (1.5, 3.5)}` |
| **`cause`** | ✅ **UNCHANGED** | `cause : Y → {fault, hazard}` intact, line 295. No value added, nothing renamed |
| **Canonical pipeline (C.8)** | ✅ **UNCHANGED** | Not edited |
| **Scripts** | ✅ **UNCHANGED** | `find scripts data -newermt` → **empty**. `g_t` logic identical in `canonical_figures.py` L121–122 and `condition_comparison.py` L155–156 |
| **Replay outputs** | ✅ **UNCHANGED** | Nothing executed |
| **Sensitivity outputs** | ✅ **UNCHANGED** | Not re-run |
| **Figures** | ✅ **UNCHANGED** | Not regenerated |
| **7.72% / 5.98%** | ✅ **UNCHANGED** | 8 occurrences of 7.72% intact in §0a |
| **Prediction outcomes** | ✅ **UNCHANGED** | Not re-resolved |
| **Prediction register** | ✅ **UNCHANGED** | 24 predictions, 22 CONFIRMED / 2 REFUTED |
| **SDR-001** | ✅ **DRAFT — NOT APPROVED — NOT APPLIED** | "Status: DRAFT. Not applied. Requires approval." |
| **Model B** | ✅ **NOT ADOPTED** | 0 occurrences of sunrise/sunset/USNO/Meeus in `appendix-c-formalisation.md` |
| **Files modified** | 4 `.md` files, listed §1 | `find -newermt` confirms no others |

---

## 9. What this cleanup did and did not accomplish

**Did:** removed every statement in the active project asserting that `S = UNSAFE` proves physical danger or that it instructs the operator; made the canonical definition consistent with C.9.4 and with the five documents asserting unconditional human authority; separated evidence from policy at the point where the definition is given.

**Did not:** change any governance behaviour, threshold, figure, prediction, or the classifier. Nothing here decides SDR-001.

**Effect on the SDR-001 decision.** The audit's Outcome B stated Model B is formally compatible but requires clarification first. **That clarification is now complete** — so the outcome for Model B, if it were reassessed today, would be Outcome A. This does not approve it. It removes semantic clarity as a blocker, leaving the three approval conditions in `finding-gt-evidence-closure.md` Part 6 exactly as they stand: the SAFE→UNSAFE step cost, the pinned solar implementation, and the re-resolution protocol.

Worth stating plainly: **the corrections here were needed regardless of Model B.** L1 and L2 were false at 19:00 on a calm night under the *incumbent* classifier, and route 2 (fail-safe UNSAFE on a flat sea) breaks the old definition with no reference to time at all.

---

## 10. Sources

`docs/canonical/finding-unsafe-semantics-audit.md` (§1, §2, §4, §5, §7, §10, §12) · `docs/canonical/appendix-c-formalisation.md` (Definition C.1, C.1 time-of-day note, C.2 `g_t` table, C.2.0.8, C.3, C.4, C.6, C.7.2, C.8.2, C.9.1, C.9.4) · `docs/canonical/architecture-illustration.md` · `docs/canonical/rq5-study-design.md` · `docs/justification/viva-formalisation-architecture.md` · `docs/canonical/finding-gt-provenance-audit.md` · `docs/canonical/finding-gt-operational-semantics.md` §3.2 · `docs/canonical/finding-gt-evidence-closure.md` (SDR-001, DRAFT)
