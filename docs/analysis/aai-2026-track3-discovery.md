# AAI 2026 Track 3 Discovery Report

**Date:** 2026-09-23
**Task:** Discovery only. No manuscript drafted. No research reframed. No novelty invented.
**Authoritative source:** `experiment-report-delta-l2.md`, read in full (§§1–13).
**Critically checked, not inherited:** `aai-2026-track1-discovery.md`. §4.4 identifies where that report was wrong about Track 3.
**Candidate:** Track 3 — Robotics, Autonomous & Human-Centred Intelligent Systems · *Responsible, Ethical & Human-Centred AI*

---

## 1. Executive finding

**Track 3 is the better of the two tracks, but the margin is narrower than the Track 1 discovery claimed, and the Responsible AI connection is not the one that report assumed.**

Three findings drive this.

**(i) The obvious Responsible AI framing does not survive.** "AI participation and advisory scope are restricted according to assessed risk, and a human retains authority" is **not** by itself a Responsible AI research contribution. Every mechanism in it is established safety engineering: ASTM F3269 is an industry standard for *"Methods to Safely Bound Behavior of Aircraft Systems Containing Complex Functions Using Run-Time Assurance"*, and Simplex, shielding and supervisory switching all predate it. Responsible AI reviewers will recognise this immediately. A paper claiming "we built a Responsible AI architecture" is a runtime-assurance paper with a fashionable label.

**(ii) There is a genuine Responsible AI connection, and it is a different one.** Responsible AI has a well-documented **principles-to-practice gap** — governance commitments that are stated but never shown to do anything operationally. This work contains a clean, uncomfortable demonstration of exactly that failure mode: **a governance design can declare three risk states, look graduated in every diagram and policy document, and be behaviourally identical to a binary on/off gate.** C3 is not a strawman — §7.2 of the report states it ports Flehmig et al.'s governance *topology* onto an environmental conditioning variable — and it diverges from a binary gate in **0.00%** of hours, while C2, which actually contracts the admissible set, diverges in **5.81%**. The contribution is therefore **a measurement discipline for governance controls**, not a governance mechanism. That maps onto the NIST AI RMF **MEASURE** function rather than onto any architecture claim.

**(iii) The structural result is definitionally true and the recommended title overstated it.** C1 ≡ C3 because their admissible sets are identical at every state; this is entailed, not discovered, and the report says so — the 0.00% "follows from the comparator definitions rather than from the data" and P21 "functions as a regression lock on the encoding rather than as a test." The underlying principle is also **already implicit** in the levels-of-automation literature, where Parasuraman, Sheridan & Wickens define levels by function allocation rather than by label count. **"Adding a State Is Not Adding Governance" therefore promises a discovery that the evidence delivers as a definition.** See §7 and §11.

**What remains, and it is real but modest:** an explicitly auditable criterion for when a graduated governance design is graduated in behaviour rather than in name, a method for testing it (the C0–C3 ladder), and a measurement showing the criterion is non-vacuous at one site — reported with its full sensitivity envelope and its negative findings.

**Recommendation: Track 3, on the measurement framing, not the architecture framing.** Confidence is moderate, not high. §19 gives the anonymous-submission test, whose answer is that *neither* track is the natural home — the natural home is runtime assurance.

---

## 2. What the existing evidence actually establishes

Read from the authoritative report in full. Every row is evidenced; nothing is inferred.

| # | Established | Evidence | Note |
|---|---|---|---|
| 1 | The intermediate state is **non-vacuous** at this site | Δ_L2 = 5.81% PRIMARY / 4.48% RESOLUTION; non-vacuous across every sourced small-vessel configuration | The control is exercised, not decorative |
| 2 | Level 2's contribution is **isolable** | C0↔C1 = 42.88%; C0↔C2 = 48.69%; difference 5.81%; independent pairwise cross-check 5.81% | The ladder works |
| 3 | A three-state topology **without scope contraction** is governance-identical to a binary gate | C1 ≡ C3 by construction; 0.00% on any trace | **Entailed, not measured** |
| 4 | The activation measure identifies the **CAUTION base rate**, not restriction quality | Δ_L2 ≡ P(S=CAUTION), verified <1e-9 | Invariant to A_AI(CAUTION) content |
| 5 | The headline is **not a stable site property** | Envelope 5.67–9.56% PRIMARY (4.26–6.64% RESOLUTION); wave ±0.25 m → 2.54–14.75% | Report: *"a point on a steep gradient"* |
| 6 | Wave onset **dominates**; rainfall is minimal | `g_o` ≈ −1.4 pts per 0.05 m; `g_r` moves 0.48 pts | |
| 7 | The five-component state is **not empirically warranted** at this site | `g_o` binds 518/531 = **97.6%**; `g_r` 2.4%; `g_w`, `g_t`, `g_m` never bind; wind a structural zero | §10: part of the **primary** contribution |
| 8 | The headline is **vessel-class specific**, near-vacuous for larger classes | Medium **1.96%**, large **1.26%** (0.66% / 0.37% RESOLUTION) | |
| 9 | The headline is **denominator-policy dependent** | Daylight-only → **9.59% / 7.40%** | `night ⇒ UNSAFE` is researcher-defined |
| 10 | Classification stays **total** under a declared exclusion; figures are **lower bounds** | P1; D = {m}; g(⊥) = UNSAFE; `g_m` can only raise severity | Standard partial identification |
| 11 | Implementation **conforms** to its governance contract | P1–P3; prototype fidelity criteria | Not new theory (report's own words) |
| 12 | **Threshold provenance is traced and gaps are documented** | Four boundaries to named authorities; three load-bearing choices declared researcher-defined; MET publishes nothing below 20 mm/hr | Genuine transparency artefact |
| 13 | **Pre-registration was used** | P01–P24; P21–P24 registered before the comparison ran; 15 CONFIRMED / 9 REFUTED | Unusual; currently unused in any paper |
| 14 | The headline **moved five times**, each with a recorded cause | §12: 12.4% → 8.3% → 6.1% → 7.84%/6.15% → 7.72%/5.98% → 5.81%/4.48% | Supports a documentation claim, not a result claim |

**Not established anywhere:** any property of generated advice (limitation 7 — "the replay does not compare the *content* of generated advice"), any human outcome, any safety outcome, any statistical inference (limitation 8 — a deterministic census, "no p-values, confidence intervals or significance tests apply").

---

## 3. Responsible AI literature landscape

| Concept | Closest primary source | Relationship | Correspondence | Terminology risk |
|---|---|---|---|---|
| **Run-time assurance** | **ASTM F3269** — *Methods to Safely Bound Behavior of Aircraft Systems Containing Complex Functions Using Run-Time Assurance*; AIAA SciTech 2021 overview | The architecture **is** an RTA pattern: a simple verified monitor bounding a complex function | **EXACT** | None if cited as prior art. 🔴 Fatal if the paper claims the pattern |
| **Simplex architecture** | Sha, *The Simplex Architecture for Safe On-Line Control System Upgrades* | Supervisory switching to a safe controller on envelope exit | **EXACT (pattern)** | Same |
| **Shielding** | Alshiekh et al., AAAI 2018 — preemptive vs post-posed | Preemptive shield "provides a list of safe actions" before the agent decides | **EXACT** for pre-inference restriction | 🔴 Must be conceded |
| **Advisory inhibition by external state** | FAA AC 20-151C (TCAS II); TSO-C151c §5.6 | The mechanism, in certified avionics | **EXACT** | Already conceded in the report |
| **Selective prediction / reject option** | Chow (reject option); Geifman & El-Yaniv, *SelectiveNet*; JMLR, *Optimal Strategies for Reject Option Classifiers* | Abstention as a first-class system behaviour | **ANALOGOUS ONLY** — abstention there is driven by the model's **own confidence**; here by an **external environmental state**. The AI's competence is never consulted | ⚠️ Usable only with that distinction stated |
| **Levels of automation** | Parasuraman, Sheridan & Wickens (2000), *IEEE Trans. SMC-A* 30(3):286–297 | Levels defined by **function allocation across stages**, not by label count | **PARTIAL — and it pre-empts the structural finding** | See §7 |
| **Meaningful human control** | Santoni de Sio & van den Hoven (2018), *Frontiers in Robotics and AI*; TU Delft | Requires **tracking** (responsiveness to human reasons) and **tracing** (traceability to human understanding) | **UNSUPPORTED** — neither condition is evidenced | 🔴 **Do not use** |
| **Human oversight (regulatory)** | **EU AI Act Article 14** | Requires oversight *measures* for high-risk systems | **PARTIAL** — the architecture is a plausible oversight measure; no evidence it is effective, and applicability is unestablished | ⚠️ Cite only as context |
| **AI risk management / measurement** | **NIST AI RMF** (GOVERN · MAP · **MEASURE** · MANAGE); ISO/IEC 23894; ISO/IEC 42001 | **MEASURE** is where "does this control actually do anything in deployment" lives | **PARTIAL–GOOD** — the best available anchor for this paper | ✅ Lowest-risk framing |
| **AI governance / principles-to-practice gap** | *AI governance: a systematic literature review* (AI & Ethics, 2024); *Responsible AI governance: a review and research framework* (2024) | Documented gap between stated governance and operational effect | **GOOD** — the paper is an instance of closing it by measurement | ✅ The strongest honest hook |

### The consequence

**Every mechanism corresponds exactly to established prior art. Nothing mechanistic survives.** The only concepts where the work is *not* fully anticipated are (a) NIST AI RMF's MEASURE function, which is a framework rather than a result and therefore anchors rather than competes, and (b) the AI-governance principles-to-practice literature, which describes the gap this paper measures rather than measuring it.

**This is the Responsible AI connection, and it is the only defensible one.**

---

## 4. Track 3 fit analysis

### 4.1 Is this actually Responsible AI? — the ten properties classified

Classification: **A** genuine Responsible AI property · **B** general software/safety engineering · **C** governance but not AI-specific · **D** insufficient to justify an RAI contribution.

| Property | Class | Reasoning |
|---|---|---|
| Deterministic external governance | **B** | This is runtime assurance (ASTM F3269). Nothing about it is AI-specific — the governed function could be any complex component |
| Human final authority | **C** | A governance/architectural property. Necessary for RAI, nowhere near sufficient, and asserted rather than evaluated. See §5 |
| **AI abstention under UNSAFE** | **A** | Abstention is a recognised first-class behaviour in RAI and in the selective-prediction literature. ⚠️ But here abstention is triggered by **external state, never by the AI's own competence** — the opposite of selective prediction. This must be stated, and it is interesting |
| **Restricted capability under intermediate risk** | **A** | Risk-proportionate capability is a genuine RAI idea and the closest thing to an RAI mechanism here. Also the thing C3 shows can be faked |
| Containment of recommendation scope | **B** | "True by definition of A_AI" (report, P2). A specification property |
| **Explicit researcher-defined policy choices** | **A** | Declaring which choices are designer decisions rather than derived is a real RAI transparency norm — NIST AI RMF, ISO/IEC 42001. §5.1 does this unusually well: three load-bearing choices named |
| **Declared unavailable components** | **A** | Documenting a structurally missing input (`D = {m}`) instead of imputing it, and carrying the consequence as a lower bound, is genuine RAI data-limitation transparency |
| Fail-safe resolution | **B** | Classical safety engineering |
| **Explicit non-claims** | **A** | Overclaiming is a named RAI failure mode. A paper that states what its evidence does *not* establish is practising the discipline it studies |
| **Transparent threshold provenance** | **A** | Four boundaries traced to named authorities, the MET gap documented rather than filled, five superseded headline figures with recorded causes. A real traceability artefact |

**Tally: 5 A · 3 B · 2 C · 0 D.**

**But the tally misleads if read as a score.** The five **A** properties are all *transparency and disclosure* properties, not mechanism properties. None of them is a contribution in itself — every competent paper should disclose its design choices. They make the paper *respectable* Responsible AI work; they do not make it a Responsible AI *contribution*.

**The contribution has to come from elsewhere, and it does:** from showing that a governance control's stated graduation and its behavioural graduation can diverge completely, and that only measurement distinguishes them.

### 4.2 Does the subtopic fit?

**"Responsible, Ethical & Human-Centred AI" is a three-part subtopic and this work reaches only the first part.**

- **Responsible** — yes, on the measurement framing. ✅
- **Ethical** — no. No ethical analysis, no value trade-off, no stakeholder ethics, no normative argument. ❌
- **Human-Centred** — **no**, and §5 forbids claiming it. ❌

A submission must therefore sit squarely in *Responsible* and make no attempt at the other two.

### 4.3 The reviewer-population risk the Track 1 discovery did not consider

Track 3's Responsible AI reviewers are drawn substantially from **fairness, bias, explainability and sociotechnical evaluation of learned models**. Presented with a paper containing **no model, no training data, no protected attributes, no users and no explanation mechanism**, such a reviewer may conclude the work is outside their area — structurally the same failure as Track 1's *"where is the learning?"*.

The mitigating asymmetry is real but smaller than previously claimed: Responsible AI **does** recognise governance and oversight *mechanisms* as objects of study in a way that Knowledge Representation does not recognise lookup tables. So the risk is lower — not absent.

### 4.4 🔴 Where the Track 1 discovery was wrong about Track 3

The Track 1 report asserted, **with no literature verification**, that:

> *"Responsible-AI reviewers are the audience most likely to accept the honest non-claims… reviewers there recognise governance mechanisms as legitimate objects of study, expect neither a model nor an inference procedure, and treat disciplined non-claims as a virtue rather than a missing result."*

**Three defects.**

1. **It was an unverified claim about reviewer psychology**, made in a report whose entire method was refusing unverified claims. The literature review above partially supports it — the principles-to-practice gap is real, disclosure is a genuine RAI norm — but it was asserted before it was checked.
2. **It ignored the counter-risk in §4.3.** "Expect neither a model nor an inference procedure" is wrong for a substantial part of the RAI community, which works almost exclusively on models.
3. **It treated Track 3 as a home for the *architecture*.** That framing is now shown to be the weakest available one, because the architecture is textbook runtime assurance (ASTM F3269). Track 3 is a home for the **measurement**, which is a different paper.

**Net effect: the conclusion ("Track 3 is better") survives; the reasoning did not.** The recommendation now rests on the principles-to-practice measurement anchor rather than on assumptions about who will review it.

---

## 5. Human-centred claim audit

**Mandatory section. No contextual validation with fishers has been conducted.**

| Term | Verdict | Basis |
|---|---|---|
| **Human final authority** | ✅ **SAFE TO USE — as an architectural property only** | A checkable specification fact: the architecture emits advice, never a binding instruction, and `A_AI(UNSAFE) = ∅`. Phrase as *"the architecture does not automate the departure decision"*, never as *"humans retain control"* |
| **Human decision support** | ✅ **SAFE TO USE** | A system-category description, not a claim |
| **AI abstention** | ✅ **SAFE TO USE** | Literally what `G(UNSAFE) = 0` does |
| **Human oversight** | ⚠️ **USE WITH QUALIFICATION** | EU AI Act Art. 14 means oversight *measures*. The architecture plausibly provides one; there is no evidence any oversight is *effective*, and the Act's applicability is unestablished. Use only as *"an oversight measure in the Art. 14 sense"*, with citation |
| **Human-in-the-loop** | ⚠️ **USE WITH QUALIFICATION** | Descriptively true — the human decides. Carries connotations of a studied interaction. Use once, descriptively, or not at all |
| **Human agency** | ⚠️ **USE WITH QUALIFICATION** | Only as "the architecture does not remove the decision from the human." Never as a demonstrated property |
| **Human-centred AI** | 🔴 **AVOID** | Requires user involvement in design or evaluation. None occurred. The term names the thing the work has not done |
| **Meaningful human control** | 🔴 **AVOID** | Santoni de Sio & van den Hoven require **tracking** (responsiveness to human moral reasons) and **tracing** (outcomes traceable to human understanding). Neither is evidenced. This is a **specific, checkable overclaim** and an RAI reviewer will know the conditions |
| **Trusted / accepted / usable by fishers** | 🔴 **AVOID** | Explicit non-claims |
| **Preserves fisher autonomy** | 🔴 **AVOID** | Normative claim with no evidence |

### The question asked directly

> *Can "human final authority" be described as a governance property without claiming human-centred validation?*

**Yes — and this is the single most important line to get right in the paper.**

The architecture **specifies** that no AI output is binding and that under UNSAFE no output exists. That is a property of the specification, verifiable by reading it, and it requires no user study. What requires a user study is whether that authority is *meaningful* in practice — whether fishers understand the states, whether advice anchors them, whether restriction is read as a warning or as a malfunction.

**The discipline:** state human authority in the **specification** register (*"the architecture does not automate the decision"*) and never in the **effect** register (*"the human remains in control"*). The first is a fact about the design. The second is an empirical claim about people, and the work has no people in it.

> ⚠️ The task brief warns: *do not assume the work is "human-centred" merely because a human makes the final decision.* The audit confirms the warning is correct. **A human receiving advice is a system topology, not a human-centred property.** Reviewers of a subtopic named *Human-Centred AI* are precisely the people who will make that distinction.

---

## 6. Terminology audit

**Category 1 — supported; safe**
Runtime assurance · run-time bounding of a complex function · advisory-scope restriction · admissible recommendation set · state-conditioned restriction · abstention · fail-safe resolution · totality of classification · declared exclusion · lower bound under partial identification · governance activation frequency · comparator ladder · conformance · threshold provenance · risk-proportionate capability restriction.

**Category 2 — qualify explicitly**
*Shielding* (agent literature; concede Alshiekh) · *selective abstention* (external-state-triggered, not confidence-triggered) · *human oversight* (Art. 14 measure sense only) · *graduated governance* (conceded to Flehmig, Shamsujjoha) · *safety envelope* (control connotation) · *Responsible AI* (use for the measurement problem, not for the architecture) · *structural equivalence* (definitional — see §7).

**Category 3 — avoid**
Human-centred AI · meaningful human control · ethical AI · trustworthy AI (a term of art with its own criteria) · novel/first/new mechanism · safe/safer/risk-reducing · optimal/validated/correct · trusted/accepted/usable · *"Responsible AI architecture"* (claims the architecture is the contribution — it is ASTM F3269) · any framing that makes coastal fisheries the contribution rather than the setting.

---

## 7. Structural finding analysis

The seven questions, answered directly.

**1. Is the statement formally correct?**
**Yes, and trivially so.** C1 and C3 assign identical admissible sets at all three states, so they are the same function A_AI. Any divergence metric between them is identically zero on every input. Nothing is measured.

**2. Is it trivial?**
**Mathematically, yes.** The report says so plainly: the 0.00% "follows from the comparator definitions rather than from the data", it is "not independent empirical evidence", and P21 "functions as a regression lock on the encoding rather than as a test of the site data."

**What is not trivial** is that C3 is a *published framework's topology*. §7.2 states C3 ports **Flehmig et al.'s** governance topology onto an environmental conditioning variable — with the explicit fairness qualification that Flehmig conditions on AI degradation, not environmental state, and that C3 "is not a reproduction of their system… not a claim that their framework is deficient." So the honest statement is not "prior frameworks are hollow" but the much narrower **"a three-level topology of this published shape, ported to this conditioning variable, contributes nothing unless the intermediate level contracts the admissible set."**

**3. Already established in prior literature?**
**The principle, largely yes.** Parasuraman, Sheridan & Wickens (2000) define levels of automation by *function allocation across stages* — precisely because a level is meaningless unless it changes what the automation does. SAE J3016 does the same for driving automation. The insight that levels must be individuated behaviourally is decades old.

**Not found:** an explicit statement of it as an **auditable criterion for AI governance designs**, paired with a worked demonstration and an activation measurement. That gap is narrow and real.

**4. Useful as a Responsible AI design observation?**
**Yes — this is its strongest property.** It converts into a one-line audit question: *does each risk level change the set of things the system may do?* If not, the level is documentation. That is checkable, transferable, and directly addresses the principles-to-practice gap.

**5. Can it be the centre of a 4–6 page paper?**
**Not alone.** It is one paragraph and a table row. It can be the *framing* if the paper's body is the empirical activation measurement, the sensitivity envelope and the negative component findings.

**6. What generality is permitted from one instantiated design?**
**Very little.** One site, one vessel class, one ported topology, one conditioning variable. Permitted: *"we exhibit a design where this occurs, and give a criterion for detecting it."* Not permitted: any claim about governance designs in general, or about Flehmig et al.'s framework in its own setting.

**7. What should it be called?**

| Candidate | Verdict |
|---|---|
| Structural result | ❌ "Result" implies discovery |
| Negative result | ❌ Implies an experiment that could have gone otherwise; it could not |
| Comparator result | ❌ Same problem |
| Structural equivalence | ⚠️ Accurate but reads as a finding |
| Governance property | ⚠️ Close |
| **Specification-level criterion** / **auditable design criterion** | ✅ **Recommended.** Honest about its definitional status while keeping its usefulness |

> **Consequence for §11.** *"Adding a State Is Not Adding Governance"* announces a discovery. The evidence supplies a definition plus a demonstration. The title **overstates**, and the Track 1 discovery recommended it partly on the strength of an argument (threshold-invariance) that is true but does not make a definitional claim empirical. **Do not preserve that title unexamined.**

---

## 8. Empirical activation analysis

**Is measuring governance activation frequency a legitimate contribution?** Tested, not assumed.

**Yes, with a specific anchor.** NIST AI RMF's **MEASURE** function exists because stated controls must be shown to function in deployment, and the AI-governance literature documents a persistent principles-to-practice gap. A governance control that never activates is decorative; one that activates constantly is a different design problem. **"How often does this control change what the system may do?" is a well-formed question in that frame**, and no prior characterisation of it was located for advisory-scope governance (Gap B).

**What survives the Δ_L2 ≡ P(S=CAUTION) concession:**

- ✅ The control is **non-vacuous** — exercised in every sourced small-vessel configuration. This is the real finding and it could have been zero.
- ✅ The intermediate level's contribution is **isolable** from the participation gate (42.88% → 48.69%).
- ✅ The measure's **own semantics are characterised** — it identifies the intermediate base rate, not restriction quality. Reporting what your metric cannot see is itself a MEASURE-function contribution.
- ❌ **Not** survived: any claim that 5.81% is a stable property, that {Go, Delay} is right, or that activation implies benefit.

**The honest framing:** the paper reports **a lower-bounded, threshold-sensitive, class-specific activation rate**, disclosed with its 5.67–9.56% envelope, its 97.6% single-component dependence, and its near-vacuity at 1.96% / 1.26% for larger vessel classes. That combination is unusual to see published and is the paper's credibility.

> **The sharpest available sentence:** across four governance configurations, the one that looks most different on an architecture diagram (C3, three states) behaves identically to the simplest (C1, binary), while the one that differs in a single table cell (C2) is the only one that changes anything. **Diagrams do not show governance; admissible sets do.**

---

## 9. Candidate scientific centres

*No numerical scoring. No forced winner.*

### A — Structural adequacy of graduated AI governance
**Question.** When is a graduated governance design graduated in behaviour rather than in name?
**Contribution.** An auditable criterion. **Novelty:** low — implicit in levels-of-automation (Parasuraman et al. 2000). **Evidence:** complete but definitional. **Missing:** any second design. **Track 3 fit:** good — it is a governance-audit question. **IPoSCI overlap:** none. **Reviewer risk:** "trivially true." **Six pages:** as framing only, not as body.

### B — Empirical activation frequency of advisory-scope governance
**Question.** How often does the intermediate level change the admissible set, and how robust is that?
**Contribution.** Gap B — a characterisation that could have returned null. **Novelty:** genuine, modest. **Evidence:** complete, including the envelope and negatives. **Missing:** nothing for the question as posed. **Track 3 fit:** moderate — anchors to NIST MEASURE. **IPoSCI overlap:** 🟠 the two headline numbers are already published. **Reviewer risk:** "it's just P(CAUTION)" — answerable. **Six pages:** yes, comfortably.

### C — Risk-dependent restriction of AI advisory capability
**Question.** Should AI capability contract as assessed risk rises?
**Contribution.** None that is new — this is ASTM F3269, Simplex, TCAS II. **Novelty:** 🔴 **none.** **Track 3 fit:** superficially excellent, which is the danger. **IPoSCI overlap:** 🔴 high. **Reviewer risk:** 🔴 fatal — a reviewer who knows RTA will reject. **Verdict: exclude.**

### D — Comparator-based evaluation of governance layers
**Question.** How can one governance level's marginal contribution be isolated?
**Contribution.** The C0–C3 ladder as an evaluation instrument. **Novelty:** moderate, under-argued. **Evidence:** complete for one application. **Missing:** a second design — so it is an instrument exhibited, not a method established. **Track 3 fit:** good under MEASURE. **IPoSCI overlap:** none. **Six pages:** yes.

### E — Runtime governance under incomplete environmental information
**Question.** Can governance stay total and bounded when a required input is structurally absent?
**Contribution.** P1 + D = {m} + fail-safe + lower bound. **Novelty:** low — totality is runtime verification, bounding is Manski. **Evidence:** complete. **Track 3 fit:** moderate — data-limitation transparency is a genuine RAI norm. **IPoSCI overlap:** none. **Six pages:** as a subsection.

### F — Responsible-AI operationalisation in a low-resource environment
**Question.** How is AI governance operationalised where inputs and institutions are thin?
**Contribution.** The domain operationalisation. **Novelty:** low as CS. **Track 3 fit:** apparently good. **IPoSCI overlap:** 🔴 **highest — this is the IPoSCI paper.** **Reviewer risk:** "domain application." **Verdict: exclude as centre; retain as setting.**

### G — Structural equivalence between binary gating and a three-state topology without scope restriction
As A, stated as the specific instance. Same profile; sharper. **Reviewer risk:** "true by construction" — must be conceded up front, not defended.

### H — *(identified here)* Measuring whether a declared governance control does anything ⭐
**Question.** Governance designs declare risk levels; how do you tell whether a declared level changes system behaviour, and how often does it?
**Contribution.** A criterion (A/G), an instrument (D), and a measurement with full disclosure (B, E).
**Novelty.** The **composition** is the novelty; no component is novel. Honest and defensible.
**Literature support.** NIST AI RMF MEASURE; AI-governance principles-to-practice literature.
**Evidence.** Complete — every element exists and is reproduced from canonical scripts.
**Missing.** A second governance design for generality; nothing for the claim as scoped.
**Track 3 fit.** **Best available** — it makes the paper about governance *assurance* rather than about an architecture or a domain.
**IPoSCI overlap.** Low — the abstract has neither the criterion, the ladder, nor the disclosure apparatus.
**Reviewer risk.** "Is a measurement study enough for a paper?" Real, and mitigated by six pages being a short format.
**Six pages.** Yes — it is exactly a six-page paper.

> **Centre H is the recommendation.** It subsumes A/G as framing, B as body, D as instrument, E as a subsection, and excludes C and F, which are respectively prior art and the IPoSCI paper.

---

## 10. Candidate research questions

### RQ-1 — Activation and disclosure ✅ fully answerable
> Over a multi-year environmental record, how often does an intermediate advisory-scope level change the admissible recommendation set relative to a participation-only gate, and how sensitive is that frequency to defensible threshold, vessel-class and denominator configurations?

**Method.** C0–C3 replay; subtraction; one-at-a-time and grid sensitivity; class and denominator variants.
**Evidence.** 43,848 / 28,501 records; 9,135 / 5,935 window hours; 5.81% / 4.48%; envelope 5.67–9.56%; classes 1.96% / 1.26%; daylight-only 9.59% / 7.40%.
**Result.** Non-vacuous in every sourced small-vessel configuration; wave-dominated; near-vacuous for larger classes.
**Claim permitted.** A lower-bounded, disclosed, site- and class-specific activation characterisation.
**Claim NOT permitted.** Stability, robustness, generalisation, benefit, correctness of {Go, Delay}.

### RQ-2 — The audit criterion ✅ answerable, definitional
> Under what condition does adding an intermediate risk level to a governance design change system behaviour rather than only its description?

**Method.** Specification comparison of C1, C2, C3.
**Evidence.** C1 ≡ C3 (0.00%, entailed); C1 ↔ C2 = 5.81%.
**Result.** Only contraction of the admissible set changes behaviour; state count alone does not.
**Claim permitted.** An auditable criterion, demonstrated on one ported topology.
**Claim NOT permitted.** 🔴 That this is discovered, measured, or general; any judgement of Flehmig et al. in their own setting.

### RQ-3 — What the metric identifies ✅ fully answerable
> What property of a graduated governance design does an activation-rate measure identify?

**Evidence.** Δ_L2 ≡ P(S=CAUTION), verified <1e-9; component attribution `g_o` 97.6%.
**Result.** The intermediate base rate — invariant to restriction content, and at this site largely a single component's base rate.
**Claim permitted.** A methodological caution for governance evaluation.
**Claim NOT permitted.** That the metric evaluates restriction quality.

### RQ-4 — Totality under declared exclusion ✅ answerable, supporting
> Can governance remain total and containment-preserving when a required component is structurally unavailable, and what follows interpretively?

**Evidence.** P1, P2; D = {m}; g(⊥) = UNSAFE.
**Result.** Total; containment preserved; all figures lower bounds.
**Claim permitted.** Conformance and a directional bound. **NOT permitted:** new theory.

### RQ-5 — Component warrant ✅ answerable, negative
> Does the evaluated record warrant the multi-component structure of the classifier?

**Evidence.** `g_o` 518/531 = 97.6%; `g_r` 2.4%; `g_w`/`g_t`/`g_m` never bind; wind a structural zero across 18–25 kn.
**Result.** **No** — not at this site. The specification remains defensible as transferable; the record does not warrant equal component importance.
**Claim permitted.** A negative finding, named in §10 of the report as part of the primary contribution.
**Claim NOT permitted.** That the components are wrong in general.

### 🔴 Flagged — RQs requiring evidence that does not exist
- Any RQ about **generated advice** — limitation 7: the replay does not compare advice content.
- Any RQ about **fisher comprehension, trust, usability or decision quality** — no validation conducted.
- Any RQ about **safety outcomes** — no incident record exists for the site (limitation 5).
- Any RQ about **another site or vessel class as a positive claim** — explicit non-claims.
- Any RQ requiring **statistical inference** — limitation 8: a deterministic census; no p-values or CIs apply.

**None of these is necessary for RQ-1 through RQ-5.**

---

## 11. Candidate titles

| # | Title | Promises | Delivered? | Reviewer expectation | IPoSCI risk | Terminology risk |
|---|---|---|---|---|---|---|
| 1 | **Does Declaring a Risk Level Change What an AI May Do? Measuring Advisory-Scope Governance** ⭐ | A measurement answering an audit question | ✅ Fully | A disclosure-heavy empirical study | 🟢 None | 🟢 Low |
| 2 | **Measuring Whether Graduated AI Governance Is Graduated in Behaviour** ⭐ | Criterion + measurement | ✅ Fully | Governance assurance | 🟢 None | 🟢 Low |
| 3 | **Activation Frequency of Advisory-Scope Restriction: A Comparator Study Under Declared Data Exclusion** | Exactly what was measured | ✅ Fully | A careful, dry empirical paper | 🟢 Low | 🟢 None |
| 4 | Adding a State Is Not Adding Governance: Structural Equivalence of Three-State and Binary Advisory Gating | A discovered structural result | ⚠️ **Over-promises** — see below | A finding | 🟢 None | 🟠 "Governance" broad; "equivalence" reads as discovery |
| 5 | When Risk Levels Do Not Restrict: An Auditable Criterion for Graduated AI Governance | A criterion | ✅ | A short conceptual + empirical paper | 🟢 None | 🟢 Low |
| 6 | Runtime Governance of Advisory Scope Under Incomplete Environmental Information | RTA contribution | 🔴 **No** — that is ASTM F3269 | A runtime-assurance advance | 🟢 Low | 🔴 High |
| 7 | Responsible AI Governance for Coastal Fisheries Decision Support | An RAI architecture for a domain | 🔴 **No** | Architecture + domain | 🔴 **This is the IPoSCI paper** | 🔴 High |
| 8 | A Graduated Advisory-Scope Architecture with Formal Guarantees | Architecture + theory | 🔴 **No** — P1–P4 disclaimed as non-novel | Formal methods | 🔴 High | 🔴 High |
| 9 | What an Activation-Rate Metric Identifies in Graduated AI Governance | Methodological clarification | ✅ Fully | Short, sharp analysis | 🟢 None | 🟢 Low |
| 10 | Governance Activation Under Structurally Unavailable Inputs: A Lower-Bound Characterisation | Bounded measurement | ✅ | Partial-identification-aware empirical work | 🟢 None | 🟢 Low |
| 11 | Human Authority and Graduated AI Restriction in Low-Resource Decision Support | Human-centred contribution | 🔴 **No** — no users studied | Human factors evidence | 🟠 Moderate | 🔴 **Fatal** |
| 12 | From Declared Risk Levels to Admissible Actions: Measuring the Operational Effect of AI Governance | Principles-to-practice measurement | ✅ Fully | RAI governance assurance | 🟢 None | 🟢 Low |

### Explicit test of the existing candidate (#4)

| Question | Answer |
|---|---|
| Is "governance" too broad? | ⚠️ **Yes.** The paper governs *advisory scope in one advisory system*, not governance generally. "Advisory-scope governance" is the honest scope |
| Is "structural equivalence" justified? | ✅ **Technically yes** — C1 and C3 are the same function. But it reads as a *discovered* equivalence when it is definitional |
| Is "binary advisory gating" precise? | ✅ **Yes** — C1 is exactly a binary participation gate over advisory output |
| Does the title overstate? | 🔴 **Yes.** "Adding a state is not adding governance" states a general law. The evidence gives one ported topology at one site, and the principle is already implicit in levels-of-automation work |
| Should "Responsible AI" appear? | ⚠️ **Not in the title.** It sets an expectation of ethics/fairness content the paper lacks. Put the RAI framing in the abstract and introduction via NIST MEASURE |
| Should "coastal fisheries" appear? | 🔴 **No.** It converts the paper into a domain application and moves it toward the IPoSCI framing |

**Verdict on #4: do not carry it forward as-is.** It was recommended in the Track 1 discovery partly on a threshold-invariance argument that is true but does not convert a definition into a finding.

**The three most accurate: #1, #2, #12.** Each promises a measurement of whether governance does anything — which is precisely what the evidence supports.

---

## 12. Evidence map

| Claim | Evidence | Status |
|---|---|---|
| Intermediate level activates 5.81% / 4.48% | Replay, 9,135 / 5,935 window hours | ✅ Complete |
| Level 2 isolable from Level 1 | 48.69% − 42.88%; pairwise cross-check | ✅ Complete |
| Three-state without contraction ≡ binary | P4; 0.00% | ✅ Complete — **entailed, not measured** |
| Metric identifies the CAUTION base rate | Δ_L2 ≡ P(S=CAUTION), <1e-9 | ✅ Complete |
| Sensitivity envelope 5.67–9.56% | Threshold sensitivity | ✅ Complete — supports **disclosure**, not robustness |
| Wave onset dominant (≈ −1.4 pts / 0.05 m) | Sensitivity | ✅ Complete |
| `g_o` binds 97.6% of CAUTION hours | Component attribution, 531 hours | ✅ Complete |
| Multi-component structure unwarranted at this site | Three of five never bind; wind structural zero | ✅ Complete — negative result |
| Near-vacuity for larger vessel classes | 1.96% / 1.26% (0.66% / 0.37%) | ✅ Complete |
| Denominator policy moves headline | Daylight-only 9.59% / 7.40% | ✅ Complete |
| Totality under D = {m}; lower bounds | P1; fail-safe; Manski | ✅ Complete |
| Conformance to contract | P1–P3 | ✅ Complete — not new theory |
| Threshold provenance traced; gaps documented | §5.1; four sourced, three researcher-defined | ✅ Complete |
| Pre-registration used | P01–P24; 15 CONFIRMED / 9 REFUTED | ✅ Complete — unused so far |
| Wave-model vs record-length attribution | +1.97 / −0.64 pts | ✅ Complete |
| **Anything about generated advice** | — | 🔴 Absent (limitation 7) |
| **Human oversight is effective** | — | 🔴 Absent |
| **Meaningful human control (tracking/tracing)** | — | 🔴 Absent |
| **Comparator ladder as a general method** | One application | ⚠️ Partial |
| **Criterion generalises beyond one ported topology** | One instance | ⚠️ Partial |
| Safety / decision quality / accuracy / optimality | — | 🔴 Non-claims |

---

## 13. Reviewer attack / falsification

Hostile but fair Track 3 reviewer. No manufactured defences.

**1. "This is ordinary safety engineering, not Responsible AI."**
⚠️ **PARTIAL.** Largely correct about the *architecture* — ASTM F3269 standardises exactly this pattern, and the paper must concede it on page 1. The defensible reply is that the contribution is not the mechanism but **the measurement of whether a declared governance level has operational effect**, which sits in NIST AI RMF's MEASURE function and addresses the documented principles-to-practice gap. If the paper leads with the architecture this objection is fatal; if it leads with the measurement it is answerable.

**2. "There is no AI in the experiment."**
⚠️ **PARTIAL.** True. The replay exercises a deterministic classifier and a governance layer; no model is invoked. The reply is that the object of study is the governance layer, whose behaviour is well-defined independently of what it governs — and that this is a *limitation of scope*, not a defect, already stated in limitation 7. It remains a genuine disadvantage.

**3. "You evaluate an environmental classifier, not AI governance."**
⚠️ **PARTIAL — the sharpest version of 1 and 2.** Δ_L2 is a property of f(E), and at this site 97.6% a property of `g_o`. Honest reply: the measured quantity is the **activation rate of the governance control**, which is necessarily a function of the classifier driving it; that is why the paper reports the component attribution and the sensitivity envelope rather than the headline alone. The reviewer is substantially right and the paper's credibility rests on conceding it.

**4. "Human-centred claims are unsupported."**
✅ **SUPPORTED — by making no such claims.** See §5. Human authority is stated only as a specification property. "Human-centred" and "meaningful human control" do not appear.

**5. "5.81% is just P(CAUTION)."**
✅ **SUPPORTED.** Derived, verified to <1e-9, and stated before the result. Reframed as a finding about what activation metrics identify (RQ-3). **Contingent on disclosure order.**

**6. "The CAUTION advisory set is researcher-defined."**
✅ **SUPPORTED.** Conceded in §5.2 with its domain rationale explicitly labelled as not constituting validation. The identity makes it costless — **the headline is invariant to that choice.**

**7. "The structural equivalence is trivial by construction."**
✅ **SUPPORTED — by agreeing.** It is definitional; the report says so. Its value is as an **auditable criterion**, not a discovery. 🔴 Requires that the paper never presents it as a measured result. See §7.

**8. "Why does three-state vs binary matter?"**
⚠️ **PARTIAL.** Because governance designs are commonly *described* by their state count, and C3 shows description and behaviour can diverge completely. Weakened by the fact that levels-of-automation work already individuates levels behaviourally. The reply is that the criterion is stated explicitly and measured, not that it is new.

**9. "Dominated by one wave threshold."**
⚠️ **PARTIAL — volunteer it.** ≈ −1.4 pts per 0.05 m; envelope 5.67–9.56%; ±0.25 m → 2.54–14.75%. The paper must report the envelope, not the point, and must not describe the headline as stable.

**10. "97.6% of CAUTION comes from one component."**
⚠️ **PARTIAL — and it is a finding.** `g_o` 518/531; three of five never bind. §10 of the report names this among the **primary** contributions. State first; a reviewer who derives it unaided reads the five-component framing as padding.

**11. "The result nearly disappears for other vessel classes."**
⚠️ **PARTIAL.** 1.96% and 1.26% (0.66% / 0.37% RESOLUTION) — the report's own word is "approaching vacuity." Scoped to <10 GRT, with class generalisation an explicit non-claim. A reviewer may still find the finding's interest limited.

**12. "The denominator policy materially changes the headline."**
⚠️ **PARTIAL.** Daylight-only gives 9.59% / 7.40%. `night ⇒ UNSAFE` is a declared researcher-defined policy, conservative and disclosed — but the headline is not denominator-invariant and both must be reported.

**13. "No evidence of improved safety."**
✅ **SUPPORTED.** Explicit non-claim. No incident record exists for the site (limitation 5). The paper claims the architecture *would have* restricted scope in those hours, not that restriction was correct.

**14. "No evidence of improved decision quality."**
✅ **SUPPORTED.** Explicit non-claim; no validation conducted.

**15. "What is new beyond IPoSCI?"**
✅ **SUPPORTED.** The criterion, the C0–C3 ladder, the 42.88%/48.69% decomposition, C1≡C3, the identity, the sensitivity envelope, component attribution, class and denominator variants, the lower-bound argument, P1–P4. See §14. **Requires disclosure.**

**16. "What is new beyond prior AI governance / runtime assurance literature?"**
🔴 **UNRESOLVED as a mechanism claim — and it must not be made.** Nothing. RTA, Simplex, shielding, TCAS II and graduated governance all predate this. What is not anticipated: the **explicit audit criterion plus its activation measurement**, which is a composition and a modest one. A reviewer who wants mechanism novelty will not be satisfied, correctly.

**17. "Why should Responsible AI reviewers care?"**
⚠️ **PARTIAL — the decisive question.** The honest answer: because governance controls are routinely specified and rarely measured, and this paper shows a control that looks graduated and is not, gives a criterion for detecting it, and reports an activation rate with unusually complete disclosure of its sensitivity and negatives. **Whether that interests a reviewer working on fairness in learned models is genuinely uncertain** (§4.3). This is the reviewer-population risk and it is not resolvable by better writing.

**Tally: 6 supported · 10 partial · 1 unresolved.** No objection is fatal *if* the paper leads with measurement and concedes mechanism on page 1. Several become fatal if it leads with the architecture.

---

## 14. IPoSCI overlap audit

| Category | Items |
|---|---|
| **ALREADY IN IPoSCI** | Four-layer architecture · SAFE/CAUTION/UNSAFE · S = f(E), E = {w,r,m,o,v,t} · the governance table · the graduated-gating concept · Δ = (N_restricted/N_eval)×100% · **5.81% / 4.48%** |
| **SUBSTANTIVE EXTENSION** | C0–C3 comparator design · C0↔C1 = 42.88% and C0↔C2 = 48.69% decomposition · threshold sensitivity and the 5.67–9.56% envelope · component attribution (`g_o` 97.6%) · vessel-class comparison · daylight-only denominator variant · common-period attribution (+1.97 / −0.64) · declared-exclusion lower-bound argument · P1–P4 |
| **NEW INTERPRETATION OF EXISTING RESULT** | Δ_L2 ≡ P(S=CAUTION) and its consequence that the headline is invariant to A_AI(CAUTION) · the reframing of 5.81% as a *lower-bounded, threshold-sensitive, class-specific* activation rate rather than a site property |
| **NEW ANALYSIS** | C1 ≡ C3 as an **auditable criterion** · the negative finding that the five-component structure is unwarranted at this site |
| **SUPPORTING MATERIAL ONLY** | Threshold provenance table · pre-registration record · provenance history of the five superseded figures · reproduction instructions |

### Is the proposed paper sufficiently distinct to justify separate publication?

**Yes — conditionally, and the condition is structural, not cosmetic.**

The overlap is confined to the object of study (the architecture and its table), the measure definition, and the two headline numbers. **All three must be retained unchanged**, because altering them would mean altering results. What makes the paper distinct is that it asks a **different question about the same object**: IPoSCI asked *"what is this architecture and what does it do?"*; the proposed paper asks *"does a declared governance level do anything, how would you tell, and how often does it here?"*

**The condition:** the paper must **lead with the criterion and the measurement**, and must present the architecture as recap with explicit citation of the extended abstract. If it leads with the architecture, it is the IPoSCI paper with extra tables, and the answer becomes **no**.

🔴 **Unresolved dependency.** AAI is not one of IPoSCI's three publication routes. If the extended abstract defaults to the IPoSCI e-Proceedings it becomes **published prior work** and this paper must be submitted as a disclosed extension. See `aai-2026-track-fit-analysis.md` §0.

---

## 15. Six-page content strategy

| Item | Verdict | Why |
|---|---|---|
| E definition | **USE IF SPACE** | One line naming six components. Not load-bearing |
| Threshold table | **USE IF SPACE — wave onset MUST appear** | `g_o` drives 97.6% and ≈1.4 pts per 0.05 m. The full table is optional; the wave boundary and its source are not |
| SAFE/CAUTION/UNSAFE contract | **MUST INCLUDE** | The object of study. Small table |
| G(S) | **USE IF SPACE** | ⚠️ `G(S) = 1 ⟺ A_AI(S) ≠ ∅`, so G adds nothing to A_AI. Mention once; do not build on it |
| A_AI(S) | **MUST INCLUDE** | The actual object |
| P1 Totality | **USE IF SPACE** | One sentence; supports the lower bound |
| P2 Containment | **USE IF SPACE** | "True by definition." State, do not prove |
| P3 Safety Dominance | **OMIT** from body | Conformance. One clause in evaluation |
| **P4 (C1≡C3)** | **MUST INCLUDE — as a criterion, not a result** | Carries RQ-2 |
| **C0–C3** | **MUST INCLUDE** | The instrument. Nothing is interpretable without it |
| 43,848-record description | **MUST INCLUDE — compressed** | Site, period, source, denominator. Four lines |
| PRIMARY/RESOLUTION | **MUST INCLUDE** | Second configuration |
| **5.81% / 4.48%** | **MUST INCLUDE** | The measurement |
| **C1↔C3 = 0.00%** | **MUST INCLUDE — labelled entailed** | 🔴 Never as a measured result |
| **Δ_L2 ≡ P(S=CAUTION)** | **MUST INCLUDE — before the result** | RQ-3; pre-empts attack 5 |
| **Sensitivity envelope 5.67–9.56%** | **MUST INCLUDE — the envelope, not the point** | Attack 9. Reporting only the 0.48-pt rainfall figure would imply a robustness the evidence contradicts |
| **Wave-threshold dominance** | **MUST INCLUDE** | Attack 9 |
| **Component attribution (`g_o` 97.6%)** | **MUST INCLUDE** | Attack 10; part of the report's primary contribution |
| Vessel-class comparison | **USE IF SPACE** | Attack 11. One table row |
| Daylight-only denominator | **USE IF SPACE** | Attack 12. One sentence |
| Lower-bound argument | **USE IF SPACE** | Two sentences: D = {m}, fail-safe, therefore lower bound |
| Provenance history | **OMIT** | Repo record. Not a paper contribution |
| **Architecture figure** | **OMIT** | 🔴 Highest IPoSCI overlap; lowest information density |
| Responsible AI framework mapping | **USE IF SPACE — at most two sentences** | One NIST AI RMF MEASURE anchor. A framework-mapping table would consume half a page and contribute nothing |

**Budget:** Intro + the governance-measurement problem 0.75 · Related work and concessions (RTA/F3269, shielding, LOA, TCAS II) 0.75 · Contract and criterion 0.75 · Comparator instrument 0.75 · Results with identity, envelope, attribution 1.5 · Discussion, limitations, non-claims 0.75 · References 0.75.

> **The concessions paragraph is mandatory and belongs on page 1.** ASTM F3269, Alshiekh et al., TCAS II/TSO-C151c, Parasuraman et al. A reviewer who finds F3269 *after* reading an unqualified runtime-governance claim rejects. One who sees it conceded first reads everything after as disciplined.

---

## 16. Figure/table strategy

**Recommended: 1 figure, 3 tables.**

| # | Item | Claim supported |
|---|---|---|
| **T1** | Governance contract — states × G(S) × A_AI(S) | Defines the object. Irreplaceable, tiny |
| **T2** | Comparator design — C0–C3 × admissible set at each state | **The highest-value item in the paper.** A reader sees C1 and C3 are identical *by inspection*, so the criterion lands before any number appears. Also makes "C2 differs in one cell" visible |
| **T3** | Combined results — configuration × records × window hours × C0↔C1 · C0↔C2 · Δ_L2 · C1↔C3, plus rows for the sensitivity envelope, `g_o` share, vessel classes, daylight-only denominator | Every number the paper claims, including all four disclosure rows that answer attacks 9–12 |
| **F1** | Sensitivity — Δ_L2 against wave CAUTION onset across the sourced range, both configurations, envelope band marked | The only genuinely visual content. Directly answers "dominated by one threshold" and makes the steep gradient visible rather than asserted |

**Rejected:** architecture diagram (IPoSCI overlap; low density) · structural-equivalence illustration (T2 already shows it; a figure would over-dramatise a definitional point) · separate component-attribution figure (a T3 row suffices) · Responsible AI framework mapping diagram (decorative).

---

## 17. Evidence gaps

| Gap | Blocks | Resolvable before 19 Oct? |
|---|---|---|
| No inference performed; advice content never compared | Any reasoning or pre-inference claim | ⚠️ Partially — §18 |
| G and A_AI never vary independently | Any "two independent controls" claim | ❌ No |
| Criterion demonstrated on one ported topology | Generality of RQ-2 | ❌ No |
| Ladder applied to one design | "General method" claim | ❌ No |
| No users studied | Every human-centred term | ❌ No — and not needed |
| No incident record at the site | Any safety-outcome claim | ❌ No — none exists |
| Single site, single class positive claim | Generalisation | ❌ No — explicit non-claim |
| `age_i` freshness parameter OPEN | Specification completeness | ❌ Do not invent |
| `RESOLUTION_PAIRWISE_C0_C1_C0_C2 = PROVENANCE_INCOMPLETE` | RESOLUTION pairwise reporting | ❌ Withheld — do not invent |

---

## 18. Minimal additional analysis, if necessary

**Finding: none is necessary for the recommended paper identity.** Centre H is fully evidenced by material already produced and reproduced from canonical scripts on 2026-09-21.

One optional candidate, recorded for completeness and **not recommended for this paper**:

**Admissibility-conformance contrast over a stub advisory layer.**
*Question:* does restriction applied before generation differ observably from filtering after? *Data:* none new — existing state sequence plus a trivial stub. *Effort:* small. *Value:* would convert attacks 2 and 3 from partial toward supported.
🔴 **Why not recommended here:** the recommended paper makes **no pre-inference claim**, so the analysis resolves an objection the paper does not raise. With a deterministic stub the outcome is entailed by the architecture, making it a demonstration rather than an experiment. Adding it would consume roughly half a page of a six-page budget to defend a claim better simply not made.

**Explicitly not recommended:** fisher validation (the paper makes no human-centred claim, so it is not required), a second site, a second governance design, any outcome or accuracy measurement, any attempt to evidence the G/A_AI separation.

---

## 19. Track 1 versus Track 3 comparison

| Dimension | Track 1 — KR, Reasoning & Decision Intelligence | Track 3 — Responsible, Ethical & Human-Centred AI |
|---|---|---|
| Object actually studied | A three-row state→set map. **Textbook `A(s)`** | A governance control and whether it has operational effect |
| Literature community | KR, reasoning, ML, agentic systems | AI governance, assurance, RAI — **plus** fairness/XAI, a poor match (§4.3) |
| Experiment alignment | 🔴 **None** — no inference is performed | ⚠️ **Partial** — governance behaviour is measured; no AI is exercised |
| Contribution alignment | 🔴 No representational or inferential contribution exists | ✅ Measurement of a declared control maps to NIST AI RMF MEASURE |
| Reviewer expectations | Representation language, inference procedure, complexity or expressiveness result | Governance effect, disclosure, oversight, limitations |
| Missing evidence | Reasoning evaluation, independent G/A_AI variation | Users, outcomes, generality |
| Terminology risk | 🔴 High — "knowledge representation" is indefensible | 🟠 Moderate — manageable if "human-centred" and "meaningful human control" are excluded |
| IPoSCI differentiation | Good | Good |
| Six-page feasibility | Yes | Yes |
| Unresolved objections | **4, all track-specific** | **1**, plus 10 partial |

### The anonymous-submission test

> *If this paper were submitted with no track label, which community would most naturally recognise the research question as theirs?*

**Honest answer: neither. The natural home is runtime assurance and safety-critical systems** — the ASTM F3269 / Simplex / supervisory-control community. That community would recognise the object immediately, would not ask where the AI is, and would treat "how often does the monitor bound the function" as a normal question. AAI 2026 offers no such track; Track 3's *Intelligent Control & Automation* is the nearest neighbour but sits under a robotics-oriented heading.

**Between the two offered, Track 3 — because of what the research question asks about.** The question is *"does a declared governance level change what the system may do, and how often?"* That is a question about **governance efficacy**, which the AI-governance and assurance literature owns. Track 1's subtopic would require the question to be about how knowledge is represented or how inference is constrained, and it is neither — the representation is a lookup table and no inference occurs.

**Track 3 wins on the object, not on the audience.** The audience risk in §4.3 is real and unresolved.

---

## 20. Recommended paper identity

**Centre H** — measuring whether a declared governance control has operational effect.

**Shape.** Governance designs declare risk levels; whether a level changes system behaviour is an empirical question, not a design claim. Here is an auditable criterion (a level must contract the admissible set), an instrument for testing it (the C0–C3 ladder), and a measurement at one site: the level that adds a state without contracting scope diverges from a binary gate in 0.00% of hours; the level that contracts one table cell diverges in 5.81% — a figure that is a lower bound, spans 5.67–9.56% across sourced thresholds, is 97.6% attributable to one component, and approaches vacuity for larger vessel classes. All mechanisms conceded to runtime-assurance prior art on page 1.

**Title:** #2 *Measuring Whether Graduated AI Governance Is Graduated in Behaviour*, with #1 and #12 as alternates. **Not #4.**

**Track:** Track 3, subtopic *Responsible, Ethical & Human-Centred AI*, positioned strictly under **Responsible**, with no ethical analysis and no human-centred claim.

**Confidence: moderate.** The paper is sound, honest and distinct from IPoSCI. Its risk is not soundness but audience — §4.3 and attack 17 are unresolved and not fixable by writing.

---

THE PAPER IS ABOUT: whether a declared intermediate risk level in an AI governance design actually changes what the system is permitted to recommend, how that can be audited, and how often it does so at one evaluated site.

THE PAPER IS NOT ABOUT: a new governance mechanism, a runtime-assurance advance, a knowledge representation, a human-centred evaluation, or an AI decision-support system for coastal fisheries.

THE RESPONSIBLE AI CONNECTION IS: the documented principles-to-practice gap — governance controls are routinely declared and rarely measured — which this paper addresses by supplying a criterion and an activation measurement in the sense of the NIST AI RMF MEASURE function.

THE HUMAN-CENTRED CLAIM IS LIMITED TO: the specification-level fact that the architecture does not automate the departure decision and issues no binding recommendation, with no claim whatsoever about human oversight effectiveness, comprehension, trust, or meaningful human control.

THE STRONGEST STRUCTURAL RESULT IS: a three-state governance topology whose intermediate state preserves the permissive admissible set is behaviourally identical to a binary gate — entailed by the specifications rather than discovered, and therefore best presented as an auditable design criterion.

THE STRONGEST EMPIRICAL RESULT IS: the intermediate advisory-scope restriction is non-vacuous at the evaluated site, activating in 5.81% of departure-window hours as a lower bound, within a sourced-threshold envelope of 5.67–9.56% that is 97.6% attributable to the wave component alone.

EXISTING EVIDENCE IS SUFFICIENT FOR: the activation measurement and its full disclosure envelope, the isolation of the intermediate level via the C0–C3 ladder, the audit criterion, the identity Δ_L2 ≡ P(S=CAUTION), the negative finding that the five-component structure is unwarranted at this site, and conformance under a declared component exclusion.

EXISTING EVIDENCE IS NOT SUFFICIENT FOR: any human-centred, oversight-effectiveness, safety, decision-quality or optimality claim; any claim that the headline is a stable site property; any claim that the criterion or the ladder generalises beyond the single design instantiated here.

THE CLEAREST CONTRIBUTION BEYOND IPoSCI IS: the reframing of the already-published 5.81% from a headline figure into a disclosed, lower-bounded, wave-dominated, class-specific activation measurement, set against a comparator that shows a three-state topology can contribute exactly nothing.

TRACK 1 FIT: Weak — the representation is textbook `A(s)`, no inference is performed anywhere in the evaluation, and four reviewer objections are unresolved, all of them specific to that track.

TRACK 3 FIT: Moderate and conditional — good on the object of study and on the NIST MEASURE anchor, poor on the "Ethical" and "Human-Centred" halves of the subtopic, with an unresolved risk that reviewers drawn from fairness and explainability work will not recognise a model-free governance measurement as theirs.

RECOMMENDED AAI TRACK: **Track 3 — Robotics, Autonomous & Human-Centred Intelligent Systems, subtopic *Responsible, Ethical & Human-Centred AI*** — positioned strictly under *Responsible*.

WHY: The research question the evidence can actually answer is whether a declared governance level has operational effect, which is a governance-efficacy question owned by the AI-governance and assurance literature and anchored to the NIST AI RMF MEASURE function; Track 1 would require a representational or inferential contribution that does not exist, since `A_AI(S)` is the standard state-dependent action set and no inference is performed anywhere in the experiment. The recommendation is nonetheless qualified: every mechanism in the architecture is established runtime assurance and must be conceded on page 1, the structural finding is definitional rather than discovered, the human-centred half of the subtopic must be left entirely unclaimed, and a substantial part of the Responsible AI reviewer population works on learned models and may not recognise a model-free governance measurement as belonging to their area — a risk that is real, unresolved, and not fixable by better writing.

---

*Discovery complete. No manuscript drafted. No research reframed. Literature verified against primary and authoritative sources on 2026-09-23. `experiment-report-delta-l2.md` read in full; `aai-2026-track1-discovery.md` critically checked, with its Track 3 reasoning corrected in §4.4.*
