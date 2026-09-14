# AMICT RQ Redesign and Narrative Freeze — Task Readiness Analysis

**Date:** 2026-09-14
**Analyses:** `docs/tasks/AMICT RQ REDESIGN AND CONFERENCE NARRATIVE FREEZE.md`
**Status:** PRE-EXECUTION ANALYSIS ONLY. No freeze performed. `rq-narrative-freeze.md` and `rq-evidence-map.csv` do not exist. No manuscript touched.
**Companions:** [readiness](amict-conference-rebuild-readiness-analysis.md) · [source validation](amict-source-validation-readiness-analysis.md) · [contribution freeze](amict-contribution-freeze-v2-readiness-analysis.md)

---

## 1. What the task is

The last gate before drafting. It converts the frozen contributions into three RQs, an evidence map, a narrative, a gap statement, a novelty-positioning sentence and a section-level plan. Everything it freezes becomes the drafting brief.

It is mostly well-specified and mostly low-risk. Seven of its nine stop conditions are already discharged by the preceding gates. **One is genuinely live, and it is the one the task names last.**

---

## 2. Stop condition 9 is the real constraint — and the arithmetic is tight

> *"the six-page story cannot accommodate both frozen contributions without dropping required limitations."*

### 2.1 Where v3 actually stands

Measured directly from `manuscript-v3.md`:

| Section | Body words |
|---|---|
| Introduction | 684 |
| Methodology | 237 |
| Literature Review (six subsections) | ~1,408 |
| Proposed Architecture + Formal Structure + Properties | 1,793 |
| Algorithm Specification + Complexity | 1,065 |
| CAUTION Mode + Domain Instantiation | 902 |
| **Empirical Characterisation** | **2,088** |
| Generalisation | 371 |
| Deployment Challenges and Limitations | 743 |
| Threats to Validity | 1,648 |
| Conclusion (includes the ~40-entry reference list) | 2,051 |
| **Total** | **~12,990** |

Discounting roughly 1,400 words of references, the body is **≈ 11,600 words ≈ 13 IEEE two-column pages**.

A six-page paper at ~875 words per page is ~5,250 words total; with references at 0.8–1.0 page, the **body budget is ≈ 4,400 words**. That is a **62% cut** — and the new structure *adds* material v3 does not contain.

### 2.2 The 2026-07 compression spec is obsolete and must not be reused

`docs/superpowers/specs/2026-07-27-amict-compression-design.md` allocates: Introduction 0.6–0.7, Methodology 0.4–0.5, Literature Review 1.8–2.0, Proposed Architecture 1.8–2.0, Conclusion 0.5, References 0.8–1.0.

**It allocates zero pages to Evaluation and Results**, because when it was written v3 had no empirical section. The task says to assume the historical six-page budget "for narrative planning only" — correct — but §12's allocation must be **designed against current content**, not inherited. Reusing that table would silently starve the contribution the paper now leads on.

### 2.3 A budget that actually balances

Estimating against the frozen content, with figures and tables costing roughly 200–300 words of column space each:

| Section | Prose | Notes |
|---|---|---|
| I. Introduction | ~450 | TCAS acknowledgement, scoped gap, two contributions |
| II. Related Work | ~700 | Seven precedent families — carried by **one comparison table**, not prose |
| III. Operational Governance Formalisation | ~900 | `G`/`A_AI`, `S = f(E)`, `F_{D,τ} = f ∘ ρ_{D,τ}`, four ⊥ responses, declared exclusion, pre-reasoning `RS(S)` with no post-filter, properties stated not proved |
| — executable conformance subsection | ~150 | Fidelity, inside III |
| IV. Evaluation Method | ~400 | Four comparators, two configurations, replay scale |
| V. Results | ~500 | ΔL2 both configurations, C1↔C3 both, one results table |
| VI. Discussion and Limitations | ~600 | The mandatory disclosures (§2.4) |
| VII. Conclusion | ~200 | |
| **Prose subtotal** | **~3,900** | |
| Figures and tables | ~900 | 1 architecture figure + 3 tables |
| **Total body** | **~4,800** | against a ~4,400 budget |

**Roughly 8–10% over.** Survivable, but only with deliberate cuts: hysteresis omitted entirely (already decided in the freeze), Related Work carried by a table rather than prose, limitations compressed into one dense paragraph plus a table column, and **one of the two optional figures dropped**.

### 2.4 The mandatory-disclosure load is the reason it is tight

Fourteen items cannot be dropped, because prior gates made them binding:

R-SAFE-001 deferred and the empty SAFE rule set · `Delay`-only advisories and the restrictive-side-only limitation · 454 records not 454 types · `D = {m}` lower bounds · κ = 0 lower bounds · `g_w` two activations / zero bindings · `ageᵢ` unparameterised · `reasons` unimplemented · re-instantiation not demonstrated · PRIMARY/RESOLUTION are alternative configurations not uncertainty bounds · C1↔C3 bounded to the evaluated comparator definitions · the TCAS precedent acknowledgement · the 72 versus targeted-post-review distinction · E5/H3 open and no human study.

At even 25–40 words apiece that is 350–550 words — **roughly one eighth of the entire body budget spent on disclosure**. This is the honest cost of the claim discipline the project has imposed on itself, and it is correct, but it has to be budgeted rather than discovered during drafting.

**Recommendation:** §12 should allocate the disclosure load explicitly as a line item rather than assuming Discussion absorbs it.

---

## 3. The evidence-hierarchy question the task raises but does not settle

§11 proposes C2 empirical as PRIMARY and C1 formal as SECONDARY, then asks whether this is optimal given the prior rejection for insufficient empirical evidence.

**It is right for evidence priority**, and it matches the contribution freeze's own finding that C2 is the stronger of the two — no source in the validated comparison set empirically characterises how often an intermediate governance level changes the outcome.

**But it creates a numbering mismatch.** C1 is numbered first, is the formalisation the paper is titled around, and is what the operational-semantics block exists to deliver; C2 carries the burden of answering Review 3. Left unresolved, a drafter will not know whether Section III or Section V is the centre of the paper.

**Recommended resolution, worth freezing explicitly:** keep contribution numbering as C1/C2 for continuity with the freeze, but let **page allocation and Results prominence follow the evidence hierarchy** — Results plus Evaluation Method together should exceed the Formalisation section. The §2.3 budget above already reflects this (900 + 150 for III against 400 + 500 for IV–V).

---

## 4. RQ-level observations

### 4.1 RQ1 is answerable, with one presentational risk

The task's redesign direction is sound and does not require restoring mechanism novelty — **stop condition 4 does not fire**. A "how can X be specified operationally" question is answered by exhibiting the specification.

The risk is presentational: in a paper titled *Evaluating…*, an RQ answered by construction sits slightly oddly beside two empirical RQs. The mitigation is already available — the executable conformance evidence gives RQ1 a verifiable component, so RQ1 can be framed as *specify and verify* rather than *specify*. Worth deciding deliberately rather than inheriting.

### 4.2 RQ3's verb

The task asks whether *change*, *differ* or *vary* is most accurate. **"Differ" is the most defensible.** "Change" implies a process acting on a single quantity over time; "vary" carries a whiff of variance. The two configurations are alternative computations over different records, so the quantities *differ between* configurations. A formulation such as *"How does the measured governance-outcome divergence differ under the alternative environmental-data configuration?"* is accurate and carries no statistical implicature.

### 4.3 C1↔C3 answers RQ2 primarily, and contributes to RQ3

It has values under both configurations (0.00% / 0.00%), and E6 sits inside E3's mandatory dual-configuration scope `{E1, E2, E6}`.

Its function is a **control on the RQ2 claim** — it shows the measured ΔL2 is tied to advisory-scope differentiation rather than to the presence of a third labelled state. That is an RQ2 role. Its RESOLUTION value is then reported under RQ3 alongside ΔL2.

**Recommendation:** primary attribution RQ2, secondary reporting under RQ3. Not "supports both" without attribution, which would leave the drafter free to place it anywhere.

---

## 5. Stop-condition pre-assessment

| # | Condition | Assessment |
|---|---|---|
| 1 | An RQ requires new experiments | **Does not fire** — all three rest on closed evidence |
| 2 | An RQ depends on E5/H3 | **Does not fire** — excluded by design |
| 3 | An RQ requires human-study evidence | **Does not fire** |
| 4 | RQ1 phraseable only by restoring mechanism novelty | **Does not fire** (§4.1) |
| 5 | RQ2/RQ3 require a safety/effectiveness reading | **Does not fire** — "governance-outcome divergence" states it without one |
| 6 | Narrative cannot distinguish contribution from TCAS/ACAS X | **Does not fire** — discharged by the contribution freeze's scoped-combination test |
| 7 | Narrative requires changing frozen C1 or C2 | **Does not fire** |
| 8 | Numerical contradiction | **Does not fire** — none known across the frozen authorities |
| 9 | Six-page story cannot carry both contributions plus required limitations | **LIVE.** Tight but survivable (§2) — the binding constraint on this task |

---

## 6. Points to settle during execution

1. **Design the §12 allocation from current content**, not from the 2026-07 spec (§2.2), and budget the disclosure load as an explicit line item (§2.4).
2. **Resolve the contribution-numbering versus evidence-priority tension** (§3) — recommend keeping C1/C2 numbering while letting space follow evidence.
3. **Decide whether RQ1 is *specify* or *specify and verify*** (§4.1).
4. **Attribute C1↔C3 to RQ2 with secondary reporting under RQ3** (§4.3).
5. **Decide the figure budget** — the architecture figure is required by the earlier rebuild spec; the optional divergence figure is the cheapest thing to cut after hysteresis.

---

## 7. Verdict

**Executable.** Eight of nine stop conditions are discharged; the ninth is a page-budget constraint that is tight rather than fatal.

The work concentrates in §12, and the honest framing is that the six-page story is **over budget by roughly 8–10% before drafting begins**. That is a planning problem to solve now, with a designed allocation and an explicit disclosure budget, rather than a drafting problem to discover later — which is how a paper ends up quietly shedding the limitations that the whole claim-discipline apparatus exists to protect.

Everything else — the three RQs, the gap statement, the novelty-positioning sentence, the evidence map, the title reconfirmation — follows cleanly from the frozen contributions.

---

## 8. Files inspected

Read-only. Nothing modified; no task artefact created.

- `docs/tasks/AMICT RQ REDESIGN AND CONFERENCE NARRATIVE FREEZE.md`
- `data/amict-conference-rebuild/` — all six existing artefacts
- `publications/active/ipsci-2026/submissions/v3-revision/manuscript-v3.md` (section word counts)
- `docs/superpowers/specs/2026-07-27-amict-compression-design.md`
- `publications/active/journal-1/evaluation-specification.md`, `algorithm-specification.md`
- `docs/canonical/appendix-c-formalisation.md`
