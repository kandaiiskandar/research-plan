# Path B — Contribution Assessment

**Prepared:** 17 November 2026 · **Author:** Claude (Cowork session) · **Status:** assessment of completed evidence. **Frozen RQ1–RQ3 preserved; no canonical artefact modified; no new RQ introduced; no new algorithm proposed.**

**Companion:** `path-b-rq-evidence-map.md` (E- and M- codes below refer to its tables).

---

## 1. The six new literature summaries — triage

**All six are Scopus AI syntheses over abstracts, not primary sources.** The project's own standing rule applies: *"No Scopus AI summary is treated as primary evidence anywhere."* They are leads. **None can support a novelty claim**, and §1.4 explains why the one that looks like it could, cannot.

### 1.1 Directly relevant — one

**`comparing Intermediate or Action-Specific AI Restrictions.md`.** Its central claim is exactly the thesis's comparative territory:

> *"No direct comparison between intermediate/action-specific restrictions and binary gating for safety outcomes is reported. Most studies focus on general AI safety or specific applications without contrasting these restriction types."*

and it adds a methodological observation that lands close to M1:

> *"Existing evaluations often treat outcomes under different AI access conditions as comparable, even when they answer different questions."*

**Why it is relevant:** it is an independent (if weak) statement that the comparison the thesis performs is not reported elsewhere, and its methodological caution is the same one the Δ_L2 identity forces on this project.

**Why it cannot carry a novelty claim** — four reasons, all from the document itself: it self-rates *"Confidence Level: Moderate"*; it concedes *"none directly compare"*, i.e. the absence is inferred from abstracts that are off-topic rather than from a search designed to find such comparisons; it is abstract-level with no full-text verification; and **its nine references are almost all unrelated to the claim** — unpredictability of smarter-than-human agents, a Japanese pharmacist licensing examination, text-to-image dataset safety, China–US governance cooperation, diabetes RCTs, primary-care triage equity. **The claim is relevant; the evidence base behind the claim is not.**

### 1.2 Indirectly relevant — four

The four safety–utility summaries (`Evaluating Safety-Utility Trade-offs…`, `Impact of Evaluation Frameworks…`, `Several methodologies…`, `peer-reviewed-research-on-safety–utility-trade-offs.md`) supply **methodological context, not contribution support.** Two statements in them are worth citing because they bear on *why a disclosed sensitivity envelope matters*:

- *"There is rarely a quantified trade-off between coverage and risk, making it hard to assess the effectiveness of selective prediction strategies in practice."*
- *"Lack of standardized, publicly available datasets and common evaluation protocols makes it difficult to compare algorithms across studies and conditions."*

**One individual reference is worth chasing to full text**, and it is the only one in all six summaries that is close to a completed analysis of this project: **Alshamlan (2026), "Uncertainty-Aware Selective Prediction in Brain-Tumour MRI Classification: Selective Risk Reduction and Component-Wise Reliability Findings", *Bioengineering***. It appears in two of the six summaries, and *component-wise reliability* is the nearest published analogue to this project's component attribution (E7). **Unverified — abstract-level record only.**

**A caution these summaries create rather than resolve.** They frame everything as a *safety–utility trade-off*. This project **cannot** use that frame: it has no independent utility outcome and no independent safety outcome, so a trade-off claim is unavailable. Adopting the summaries' vocabulary would import a claim the evidence cannot support, and the constraint on this audit forbids it.

### 1.3 Insufficient for any claim — one

**`Probabilistic Shielding on Safety-Critical AI.md`** states its own inadequacy: *"There is **limited direct information** in the provided abstracts about the specific impact of research gaps in probabilistic shielding… However, several abstracts discuss related challenges… which allow us to **infer** some key impacts."* A synthesis that proceeds by inference from off-topic abstracts cannot support anything.

### 1.4 An integrity flag on the reference lists

**Two references carry 2027 dates** — Brorholt et al., *"Adaptive Probabilistic Shielding by Learning MDPs for Safe Reinforcement Learning"*, LNCS **2027**; and Stathis et al., *"How Can We Make AI Understand Safety?"*, SpringerBriefs **2027**. These are forward-dated catalogue records. **Neither may be cited without verifying its actual publication status**, and the first is directly on-topic for the architecture's shielding comparison, so it should be verified rather than ignored.

---

## 2. Is the completed evidence substantive beyond counting CAUTION states?

**Yes — but not where the thesis currently puts its emphasis.** The honest division:

### 2.1 What *is* a count of CAUTION states

**The headline is.** By M1, `Δ_L2 ≡ P(S = CAUTION)`, verified from the implementation at <1e-9 on every configuration. Two consequences the lock already concedes:

- The result is **invariant to the content of `A_AI(CAUTION)`** (lock §I) — *any* strict subset of FULL yields the same number, so the measurement says nothing about whether `{Go, Delay}` is the right restriction.
- Lock §R permits 5.81% only as *"Activation rate of the intermediate state"* and **prohibits** *"effectiveness, safety, accuracy, or threshold-independent"*.

Add M8: because `RESTRICTED = {Go, Delay}` retains both, **the restriction never alters the departure recommendation** — it removes timing and duration detail only. So the count is a count of hours in which *advisory detail* was withheld.

### 2.2 What is **not** a count — three results that carry the contribution

| | Result | Why it is not counting | Evidence |
|---|---|---|---|
| **S1** | **Wind is a structural zero.** Δ_L2 unchanged to two decimal places across a 7-knot range of `W_C`; `g_w` binds in zero CAUTION hours; only two departure-window observations fall within ±2 kn of the threshold, maximum 21.80 kn | This is a **demonstration that one classifier input cannot change the count at all**, established by varying it rather than by tallying states. It falsifies the relevance of a component the design treats as co-equal | E4 |
| **S2** | **The weakest provenance element is shown not to drive the result.** `R_C` — the single non-MET, JPS/DID-derived boundary, and the most contestable number in the specification — moves Δ_L2 by **0.48 pts** across its full defensible range (5.0 → 19.9 mm/hr) | This is a **methodological result**: it converts a known provenance weakness into a *bounded* one. That is a different kind of statement from an activation frequency, and it is the clearest defence of the specification available | E5 |
| **S3** | **Component attribution, and it is negative.** `g_o` 518/531 = 97.6%; `g_r` 13/531 = 2.4%; `g_w` 0. After removing the two definitional zeros (M6 `g_t`, M7 `g_m`), the finding is that **one of three non-definitional components accounts for 97.6% of intermediate-state activation** | This answers frozen RQ3 directly and **in the negative**: the evaluated record does not warrant equal importance of the five-component structure at this site. A negative structural result about the design is substantive in a way a frequency is not | E7 |

**And one methodological correction with no RQ slot:** E8's decomposition shows the PRIMARY/RESOLUTION spread is **not** a grid-resolution effect — it is **+1.97 pts** of wave-model effect against **−0.64 pts** of record-length effect, acting in **opposite directions** and partially cancelling. The lock explicitly instructs: *"Do not repeat: 'the 1.33-point difference is the grid-resolution effect.'"* Catching and correcting a published misattribution of one's own result is a reproducibility contribution.

### 2.3 What bounds all of it

**E10 (exploratory):** 531 CAUTION hours cluster into **85–123 independent weather events** over five years. Statistical precision is bounded by roughly 100 events, **not** by 9,135 hours. The envelope must therefore never be read as a confidence interval — which lock §R already prohibits: *"Never a confidence interval; never '±'."*

**And the envelope is wide.** 5.67–9.56% means the upper bound is **1.65×** the headline. Lock §I classifies this honestly as *"sensitive but still informative"* and requires that 5.81% *"must not appear without the envelope."*

---

## 3. Proposed contribution statement

Written to be defensible against every constraint in this audit. **Each clause is traceable to an E- or S- code and claims nothing beyond it.**

> This thesis provides an **empirical characterisation of intermediate advisory-scope activation** for a graduated, risk-gated advisory architecture, over a five-year hourly environmental record for a single small-vessel deployment site.
>
> It establishes that the intermediate state activates in **5.81%** of departure-window hours (PRIMARY) and **4.48%** (RESOLUTION), that this quantity is **identically the intermediate-state activation rate** and therefore invariant to which strict subset of the advisory space the intermediate state admits, and that it lies within a **sourced-threshold envelope of 5.67–9.56%** — a deterministic sensitivity range, not a confidence interval.
>
> Its substantive findings are three, and two are negative. **First**, the activation rate is governed almost entirely by one environmental component: the wave CAUTION onset determines **97.6%** of intermediate-state activations, while the wind component binds in **none** and is invariant across a seven-knot range of its threshold. The evaluated record therefore **does not warrant** equal treatment of the specified multi-component structure at this site, although it does not refute the structure's transferability. **Second**, the specification's least externally grounded boundary — the non-MET rainfall threshold — moves the result by at most **0.48 percentage points** across its full defensible range, bounding a known provenance weakness. **Third**, the difference between data configurations decomposes into a **+1.97**-point wave-model effect and a **−0.64**-point record-length effect acting in opposite directions, correcting an earlier attribution of that difference to grid resolution alone.
>
> The architecture's totality, containment and contract-conformance properties are established by construction and proof, and are presented as formalisations of established mechanisms rather than as novel theory.

**What that statement deliberately does not say**, each because the evidence forbids it: that activation implies improved safety; that a safety–utility trade-off was measured; that the thresholds are optimal; that the result generalises beyond this site or vessel class; that any mechanism is novel.

---

## 4. Proposed limitations statement

> **Activation is not effectiveness.** The reported rate measures how often the intermediate state is reached, not whether reaching it improves any outcome. No accident, incident or casualty data exists for this site, so no safety claim is made or available.
>
> **No safety–utility trade-off is claimed**, because neither an independent utility outcome nor an independent safety outcome was measured. The contribution is a characterisation of activation and its sensitivity, not of a trade-off.
>
> **The headline quantity is definitionally the intermediate-state activation rate.** Because the participation-only and graduated comparators differ only at the intermediate state, the divergence between them equals that state's frequency exactly. The measurement is consequently invariant to the content of the intermediate admissible set, and — because both `Go` and `Delay` are retained at the intermediate state — the restriction withholds advisory detail without altering the departure recommendation.
>
> **The result is sensitive.** The sourced-threshold envelope spans 5.67–9.56%, an upper bound 1.65 times the headline. It is a deterministic range over defensible configurations and must never be reported as a confidence interval.
>
> **Statistical precision is bounded by independent events, not hours.** The 531 intermediate-state hours fall within an estimated 85–123 independent weather events over five years.
>
> **Single site, single vessel class, no operational availability.** Findings are specific to one location and to vessels under 10 GRT. The environmental record is reanalysis, produced after the fact, so no element of it was available at the decision instant it describes — a limitation that applies to the activation rate itself and belongs in the abstract rather than here alone.
>
> **Two of five component-attribution zeros are definitional**, not measured: the daylight component emits no intermediate state by construction, and the fifth component is structurally excluded by a declared exclusion, which also makes every severity figure a lower bound.

---

## 5. Thesis chapter alignment

Mapped to the frozen RQ set only. **No chapter is created for a question the frozen set does not contain.**

| Chapter | Content | Frozen RQ | Evidence | Status |
|---|---|---|---|---|
| **Specification** | The governance pair `(G(S), A_AI(S))`; totality under structural unavailability; containment; the declared exclusion `D = {m}` and its lower-bound consequence; **the provenance inventory — four boundaries externally sourced, three load-bearing choices researcher-defined** | **RQ1** | M2, M4, M5; provenance table | Complete. Answered by construction; carries no empirical weight, and the chapter should say so |
| **Empirical characterisation** | Activation rates; the identity `Δ_L2 ≡ P(CAUTION)` stated **at the front of the chapter, not in its limitations**; state distributions | **RQ2** | E1, E2, M1 | Complete |
| **Robustness** | The sourced-threshold envelope; per-component sensitivity including the wind structural zero and the bounded rainfall influence; the 56-configuration design; the PRIMARY/RESOLUTION decomposition and the attribution it corrects | **RQ2** | E3, E4, E5, E6, E8, E9 | Complete, pending G1 |
| **Structural warrant** | Component attribution; the negative finding on the multi-component structure; the definitional-zero correction | **RQ3** | E7, M6, M7 | Complete. **This is the strongest chapter and should be positioned as such** |
| **Limitations and threats** | §4 in full; independent-event clustering; operational availability; invariance to `A_AI(CAUTION)` content | — | E10, E11 | Complete |

**The ordering recommendation, which is the practical consequence of this audit.** The lock's contribution hierarchy places empirical characterisation first and warns that *"architecture composition must not be promoted above empirical characterisation."* That holds. But **within** the empirical contribution, the robustness and structural-warrant chapters carry more weight than the activation chapter, because the activation figure is a count whose comparative interpretation the identity forecloses. Presenting 5.81% as the thesis's central result invites the examiner's first question — *what does this number compare?* — and the answer is uncomfortable. Presenting the robustness envelope and the negative attribution result as central, with 5.81% as the quantity they characterise, is both more defensible and a better account of what was actually established.
