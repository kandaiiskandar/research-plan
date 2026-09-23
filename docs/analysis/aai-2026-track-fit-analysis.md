# AAI 2026 — Track Fit Analysis for the v5 Paper

**Date:** 2026-09-23
**Status:** ANALYSIS ONLY. No planning performed. No manuscript written. No research framing changed.
**Authority:** `final-research-chain-lock.md` wins on all research framing. Nothing here overrides it.

---

## 0. READ THIS FIRST — AAI 2026 is NOT AMICT 2026

Every prior planning document in this repository (`v5-amict-discovery.md`, the v4 manuscript header, the IPoSCI correspondence record) targets **AMICT 2026**. This analysis targets **AAI 2026**, which is a **different conference at a different university**.

| | AMICT 2026 | **AAI 2026** |
|---|---|---|
| Host | UMS — the same body that ran IPoSCI | **UniMAP** (Universiti Malaysia Perlis) |
| Relationship to IPoSCI | **One of the three offered publication routes** | **Unrelated.** Not an IPoSCI option |
| Dates | — | **21–23 December 2026** |
| Venue | — | **Langkawi, Kedah** |

### ⚠️ Consequence the planner must not miss

The IPoSCI acceptance email offered exactly three publication routes: **e-Proceedings, AMICT, or IJMIC**. **AAI is not among them.**

So publishing the full paper at AAI does **not** consume the IPoSCI publication choice. The extended abstract still needs a route, and if nothing is elected it presumably defaults to the **IPoSCI e-Proceedings** — meaning **the extended abstract gets published**.

That **reactivates the prior-publication and similarity exposure** that §13 of `v5-amict-discovery.md` had provisionally set aside. The §13 relief was conditional on electing AMICT so the abstract would *not* appear in the e-Proceedings. **Choosing AAI instead removes that relief.**

**This is now the single most consequential open item.** Under an AAI route the v5 paper must be written as a disclosed, substantially extended version of a *published* extended abstract — not as a first publication.

---

## 1. Verified AAI 2026 facts

Retrieved from the official site on 2026-09-23. **The track descriptions supplied in the task prompt match the official site exactly** — no newer or divergent version was found.

| Item | Value |
|---|---|
| Full name | International Conference on Advances in Artificial Intelligence (AAI 2026) |
| Theme | *"Accelerating AI through Mathematical Foundations and Sustainable Computing for Green Energy Innovations"* |
| Dates / venue | 21–23 December 2026, Langkawi, Kedah, Malaysia |
| Submission deadline | ~~21 September 2026~~ → **extended to 19 October 2026** |
| Notification | 12 October 2026 |
| Camera-ready | 2 November 2026 |
| **Length** | **4–6 pages A4, all content included. Over 6 pages is rejected** |
| **Template** | **IEEE Conference Proceedings template**, two-column, English |
| Submission | **EDAS** — https://edas.info/N34957 |
| PDF | IEEE PDF eXpress, Conference ID **71745X** |
| Indexing | IEEE Conference Proceedings, **Scopus indexed** |

### Three things to confirm with the organisers

1. 🔴 **The dates are internally inconsistent.** Notification is listed as **12 October**, which is *before* the extended submission deadline of **19 October**. One of the two is stale. Confirm before planning a schedule around either.
2. 🔴 **Review appears NON-BLIND.** Manuscript preparation requires the first page to carry *"paper title, author(s), affiliations, and corresponding author's email."* No blind-review instruction appears anywhere. **This contradicts v4**, whose header states it was written double-blind with all identifying material stripped. If confirmed non-blind, v5 must be **de-anonymised** — authors, affiliations and the Yayasan Sabah acknowledgement restored.
3. 🟠 **No similarity threshold and no prior-publication policy are published.** Given the IPoSCI abstract will likely be in the e-Proceedings, the absence of a stated policy is *not* permission. Ask directly.

### Timing

**26 days to the extended deadline.** Materially more room than the ~5 days that remained under the AMICT assumption. The 4–6 page limit also matches v4's existing six-page word budget, so the page envelope is not a rebuild.

---

## 2. What the research actually is — the fixed input to every track assessment

Restated from the locked chain, because every judgement below depends on it.

**Contribution as locked:**
- The governance pair **(G(S), A_AI(S))** — participation gating and admissible advisory scope as **two separate mappings** over a classified environmental state
- **S = f(E)**, E = {w, r, m, o, v, t}, S ∈ {SAFE, CAUTION, UNSAFE}
- Admissible sets supplied to the reasoning layer **before inference**, not filtered after
- Formal properties **P1 Totality**, **P2 Advisory-Scope Containment**, **P3 Safety Dominance** (under A1–A4), **P4 C1≡C3 equivalence**
- Declared exclusion set **D = {m}**, fail-safe **g(⊥) = UNSAFE**, lower-bound consequence
- Comparator ladder **C0 / C1 / C2 / C3** isolating the Level-2 contribution
- **Δ_L2 = 5.81%** (PRIMARY) / **4.48%** (resolution configuration); **C1≡C3 diverges 0.00%**
- Threshold sensitivity analysis; rainfall threshold moves the headline by only **0.48 pts**

**`MECHANISM_NOVELTY = WITHDRAWN.`** The work claims *formalisation, scoped generalisation and empirical characterisation* of an existing mechanism pattern. It does **not** claim invention of state-gating, fail-safe, totality or advisory inhibition.

**Non-claims — inviolable.** No accident reduction, no improved safety, no decision quality, no classification accuracy, no optimal thresholds, no optimal state count, no optimal {Go, Delay}, no generalisation beyond Sabah or vessel class, no AI prediction accuracy, no causal effectiveness.

**Not yet run:** contextual validation with fishers. **`age_i` freshness parameter remains OPEN.**

**What IPoSCI already published:** the architecture, Table 1, S = f(E), the four layers, Δ = (N_restricted/N_eval)×100%, and **both headline numbers**.
**What IPoSCI does NOT contain:** any formal property or theorem, the C0–C3 ladder, the C1≡C3 0.00% result, the sensitivity analysis, the declared-exclusion lower-bound argument, partial identification, bounded executable conformance, or the **Δ_L2 ≡ P(S = CAUTION)** identity.

> **That last list is the entire answer to "what is beyond IPoSCI."** It already exists. No new experiment is needed to clear the bar — see §9.

---

## 3. Track 1 — Artificial Intelligence & Agentic Systems

*Topics: Machine Learning & Deep Learning · Agentic AI & Multi-Agent Systems · Generative AI & Foundation Models · Computational Intelligence & AI-Based Optimization · **Knowledge Representation, Reasoning & Decision Intelligence***

**1. What fits.** Exactly one topic, but it fits properly: **Knowledge Representation, Reasoning & Decision Intelligence**. A_AI(S) is a formal specification of *admissible action sets indexed by a classified state*, handed to the reasoning layer **before** inference. Restricting an advisory agent's action space ex ante rather than filtering its outputs ex post is a real KR&R position, and P1–P3 give it formal backing.

**2. What does not fit.** Four of five topics, completely. There is **no machine learning, no deep learning, no generative model, no foundation model, no multi-agent system, and no optimisation** anywhere in this work. The classifier is deterministic and threshold-based by design.

**3. Required central contribution.** A formal treatment of pre-inference admissible-action-set restriction as a knowledge-representation construct, with the containment lattice A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ and the totality/dominance properties as the technical core.

**4. Natural RQ.** *How can admissible advisory action sets be represented and constrained as a function of a classified operating state, such that restriction is guaranteed prior to inference rather than enforced by output filtering?*

**5. Supporting evidence.** P1 (Theorem C.1, C.1b, Corollary C.1b.1), P2 (Theorem C.2, Corollary C.2), P3 (Theorem C.3 under A1–A4), bounded executable conformance, the C0–C3 ladder.

**6. Additional work required.** None empirically. Would need the formal section expanded relative to v4, which is hard inside 6 pages.

**7. IPoSCI overlap.** **LOW.** None of the formal apparatus appears in the abstract.

**8. CS contribution or domain?** **Core CS.** Fisheries becomes an instantiation, not the subject. This is the framing that most thoroughly escapes the "application paper" trap.

> **Risk — reviewer mismatch.** The track is dominated by ML, generative and agentic topics. A deterministic rule-based governance paper risks reviewers whose first question is *"where is the learning?"*. The "agentic" hook is tempting and should be **resisted**: this system has no autonomy, no tool use and no planning loop. Calling it agentic would be exactly the superficial repositioning to avoid.

---

## 4. Track 2 — Data Analytics, Modelling & Computational Sciences

*Topics: Data Science, Statistics & Advanced Analytics · Big Data, Data Mining & Data Engineering · Modelling & Computational Methods · Operation Research & Optimization · Distributed, Parallel & High-Performance Computing*

**1. What fits.** Thinly. The retrospective replay over 43,848 hourly ERA5 records, the one-at-a-time and combined-grid threshold sensitivity analysis, and the partial-identification framing (Manski) are genuine analytical work that could sit under *Modelling & Computational Methods*.

**2. What does not fit.** 43,848 records is **not big data**. There is no data mining, no optimisation, no distributed or high-performance computing, and no new statistical method is developed — existing partial-identification results are *applied*, not extended.

**3. Required central contribution.** A measurement-methodology paper: how to isolate and quantify the marginal contribution of one governance level using a comparator ladder under declared data exclusions.

**4. Natural RQ.** *How can the isolated contribution of an intermediate governance level be identified from retrospective environmental traces under incomplete input availability?*

**5. Supporting evidence.** The C0–C3 ladder, Δ_L2 ≡ P(S=CAUTION), sensitivity analysis, the D = {m} lower-bound argument.

**6. Additional work required.** To be competitive here the paper would need a genuine methodological advance — formal identification bounds, or an uncertainty treatment the work deliberately does not currently claim. **That is a real research programme, not a reframing.**

**7. IPoSCI overlap.** LOW.

**8. CS contribution or domain?** Core, but the *wrong* core. It elevates the measurement apparatus over the governance contribution that the PhD is actually about.

> **Verdict: poor home.** Rewards the supporting analysis and buries the reason the work exists.

---

## 5. Track 3 — Robotics, Autonomous & Human-Centred Intelligent Systems

*Topics: Robotics & Autonomous Systems · Intelligent Control & Automation · Human-Machine & Human-Robot Interaction · Affective, Cognitive & Behavioral Computing · **Responsible, Ethical & Human-Centred AI***

**1. What fits.** Strongly, on two topics.
- **Responsible, Ethical & Human-Centred AI** — the entire contribution is an operational governance mechanism that graduates AI advisory scope by assessed risk state and preserves human decision authority throughout. This is responsible AI expressed as an *architecture with formal properties*, not as principles.
- **Intelligent Control & Automation** — state-gated supervisory restriction is a control pattern, and the acknowledged precedents (TCAS II advisory inhibition, TAWS) come from certified avionics control systems.

**2. What does not fit.** No robot, no physical autonomy, no human-robot interaction, no affective or cognitive computing. Critically: **no human-subject work has been done**, so the *"Human-Centred"* half of the track title is not earned.

**3. Required central contribution.** Graduated advisory-scope governance as a **formally specified, empirically characterised responsible-AI mechanism** — with the honest boundary that it governs system behaviour and makes no claim about human or safety outcomes.

**4. Natural RQ.** *How can responsible-AI restriction be specified as an operational contract that separates participation from advisory scope, and how often does the intermediate restriction bind under real environmental conditions?*

**5. Supporting evidence.** All of it. P1–P3, the fail-safe, D = {m} and the lower-bound consequence, the C0–C3 ladder, Δ_L2 = 5.81%/4.48%, C1≡C3 = 0.00%, sensitivity, bounded executable conformance.

**6. Additional work required.** **None.** Everything needed is already produced and locked.

**7. IPoSCI overlap.** **LOW** — provided the paper leads with the formal properties and comparator evaluation rather than re-presenting the architecture.

**8. CS contribution or domain?** **Core CS.** Responsible AI is a computing subfield; fisheries is the evaluation setting.

> **The decisive advantage — and this is the central finding of this analysis.** Responsible-AI reviewers are the audience *most likely to accept the honest non-claims*. "We characterise governance behaviour and do not claim safety outcomes" reads as methodological discipline in this community. In an applied track the same sentence reads as a missing result. **The non-claims are an asset here and a liability in Track 5.**

> **Danger.** Do **not** let "Human-Centred" pull the paper toward claims about fisher comprehension or decision quality. That validation has not been run and is an explicit non-claim. Position under *Responsible/Ethical*, cite the planned validation as future work only.

---

## 6. Track 4 — Connected, Smart & Sustainable Technologies

*Topics: IoT & Cyber-Physical Systems · Smart Cities & Intelligent Infrastructure · Intelligent Transportation & Smart Mobility · Smart Energy & Sustainable Technologies · Edge, Cloud & Next-Generation Connectivity*

**1. What fits.** Weakly. *Cyber-Physical Systems* is the only honest hook — a governance layer mediating between environmental state and human action in a physical setting. The domain is superficially adjacent to the conference **theme** ("Sustainable Computing", "Green Energy").

**2. What does not fit.** Almost everything. **No IoT deployment, no sensor network, no edge or cloud architecture, no connectivity contribution, no physical actuation, no deployed system.** Environmental state comes from **ERA5 reanalysis**, not instrumentation — the paper would be visibly missing the hardware the track expects.

**3. Required central contribution.** Would have to be a deployed sensing-and-governance CPS. **That system does not exist.**

**4. Natural RQ.** Would require a deployment the research has not performed.

**5. Supporting evidence.** Insufficient.

**6. Additional work required.** A full instrumented deployment — **out of scope and impossible before 19 October.**

**7. IPoSCI overlap.** Moderate, on the architecture.

**8. CS contribution or domain?** **Domain and theme only.** The fit is to the sustainability *topic* and the conference theme, not to any CPS contribution.

> **Verdict: exclude.** Theme-chasing. Would invite reviewers to ask for a deployment that does not exist.

---

## 7. Track 5 — Applied AI & Intelligent Technologies

*Topics: Healthcare & Biomedical Intelligence · Education & Human Development · Industrial & Manufacturing Intelligence · **Agriculture, Environment & Sustainable Applications** · **Intelligent Decision Support & Emerging Applications***

**1. What fits.** The strongest **surface** fit of any track. Two topics land directly: the system *is* intelligent decision support, and coastal fisheries *is* an environment/sustainability application. The conference theme reinforces it.

**2. What does not fit.** **There is no deployed application, no user, no field trial, and no demonstrated benefit.** An applied paper is normally judged on what the application achieved.

**3. Required central contribution.** A decision-support system for coastal fisheries, evidenced by deployment or user outcomes.

**4. Natural RQ.** *How can AI decision support be delivered safely to small-scale coastal fishers under variable environmental conditions?*

**5. Supporting evidence.** The architecture, the historical replay, the domain-informed thresholds — but **no outcome evidence of any kind**.

**6. Additional work required.** Deployment or contextual validation with fishers. **Not available before the deadline.**

**7. IPoSCI overlap.** **🔴 HIGHEST OF ALL FIVE TRACKS.** This is *precisely* the framing the extended abstract already uses — same domain, same architecture, same numbers, same applied posture. A Track 5 paper is the version of v5 that most closely duplicates a work that will likely be published in the IPoSCI e-Proceedings.

**8. CS contribution or domain?** **Domain.** The contribution would be read as "AI applied to fisheries", making the formal governance work supporting material.

> **The trap, stated plainly.** Track 5 looks like the obvious home and is the worst available choice. It maximises IPoSCI overlap, demotes the contribution to an application, and — most damaging — **sets the paper against reviewer expectations it has deliberately refused to meet.** Applied reviewers reward demonstrated benefit; this work's integrity rests on *not* claiming benefit. Every honest non-claim becomes a visible hole.

---

## 8. Track ranking

| Rank | Track | Fit basis | IPoSCI overlap | New work needed | Verdict |
|---|---|---|---|---|---|
| **1** | **T3 — Responsible, Ethical & Human-Centred AI** | **Core CS** | LOW | **None** | ✅ **Recommended** |
| **2** | **T1 — KR, Reasoning & Decision Intelligence** | **Core CS** | LOW | None empirically | ✅ Viable; reviewer-mismatch risk |
| 3 | T5 — Intelligent Decision Support | Domain | 🔴 **HIGHEST** | Deployment/validation | ⚠️ Avoid as primary |
| 4 | T2 — Modelling & Computational Methods | Core, wrong core | LOW | Genuine method advance | ❌ Poor home |
| 5 | T4 — Connected, Smart & Sustainable | Theme only | Moderate | Full deployment | ❌ Exclude |

**The ranking is driven by one asymmetry.** Tracks 3 and 1 judge the paper on what it *has* — formal properties, a comparator ladder, a measured governance effect. Tracks 5 and 4 judge it on what it *deliberately does not claim* — deployment, benefit, outcomes. Same paper, opposite reception.

---

## 9. Contribution types A–F, assessed against the locked evidence

| | Contribution | Evidence today | Beyond IPoSCI? | Verdict |
|---|---|---|---|---|
| **A** | Architecture | Full | 🔴 **No — already published** | ⚠️ Cannot be primary |
| **B** | **AI governance / safety mechanism** | **Full + formal** | ✅ **Yes** | ✅ **PRIMARY** |
| **C** | Decision intelligence | Full | ✅ Yes | ✅ Supporting |
| **D** | **Comparator-based evaluation** | **Full** | ✅ **Yes — strongest delta** | ✅ **CO-PRIMARY** |
| **E** | Human-centred AI | 🔴 **None** | — | ❌ **Excluded — not run** |
| **F** | Applied coastal fisheries | Partial | 🔴 No | ⚠️ Setting, not contribution |

### A — Architecture contribution
Fully evidenced, but **this is what IPoSCI already reports**: the four layers, Table 1, the state set, the containment relation. `MECHANISM_NOVELTY = WITHDRAWN` also forbids claiming invention. Leading with A produces the highest-overlap, lowest-novelty version of v5. **Keep it as necessary exposition; never as the claim.**

### B — AI governance / safety mechanism ← primary
The separation of **participation** from **advisory scope** as two distinct mappings, formalised as an operational contract with P1 Totality, P2 Containment, P3 Safety Dominance (A1–A4), a declared exclusion set with an explicit lower-bound consequence, and a fail-safe. **None of this is in the extended abstract.** It is fully proved in Appendix C and survived the adversarial falsification and external stress-test. This is the locked contribution and the strongest thing the work has.

### C — Decision-intelligence contribution ← supporting
The underexploited idea: admissible recommendation types are supplied to the reasoning layer **before inference**, so restriction is structural rather than a post-hoc filter on outputs. This is a genuine decision-intelligence position and it is what makes Track 1 a real option rather than a stretch. Currently under-argued in v4.

### D — Comparator-based experimental evaluation ← co-primary
**The single clearest empirical advance over IPoSCI.** The abstract reports two numbers against an informal binary baseline. v5 has a four-rung ladder (C0 ungated, C1 participation-only, C2 proposed, C3 traffic-light) that *isolates* the Level-2 contribution, plus two results the abstract does not contain:

- **C1 ≡ C3 structurally, confirmed empirically at 0.00% divergence** — a comparator that looks different and provably is not
- **Δ_L2 ≡ P(S = CAUTION)** — the headline is identically the CAUTION base rate, so it is *invariant to the content of* A_AI(CAUTION)

plus the threshold sensitivity analysis showing the non-MET rainfall boundary moves the headline by only **0.48 pts**, which pre-empts the most probable reviewer attack.

> **The identity is a double-edged result and must be presented, not buried.** It is intellectually honest and it is a genuine finding — but it also means the headline measures a property of the *classifier*, not of the governance design's most researcher-dependent choice. Stating it first, as v5 already does in §7.3 of the canonical report, converts a latent vulnerability into a demonstration of rigour. Concealing it would be the kind of thing an adversarial reviewer finds.

### E — Human-centred AI ← excluded
**No supporting evidence exists.** The contextual validation with fishers has not been run; `age_i` is still OPEN. Decision quality and comprehension are explicit non-claims. Any human-centred framing would promise what the work cannot deliver. **Cite as future work only.**

### F — Applied coastal-fisheries ← setting, not contribution
Supportable as *context*. As a *contribution* it duplicates IPoSCI, demotes the CS work, and exposes every non-claim. Fisheries should be where the architecture is instantiated and measured — not what the paper is about.

---

## 10. Recommendation

**Track 3 — Responsible, Ethical & Human-Centred AI**, positioned under *Responsible/Ethical*, with **B + D as the paired contribution** and **C** as the framing that connects them. **A** is exposition. **F** is the setting. **E** is future work.

**Working thesis for the planner:**

> Graduated advisory-scope governance, specified as an operational contract that separates participation from advisory scope, proved total, containing and safety-dominant, and empirically characterised by a comparator ladder that isolates the intermediate level's contribution at 5.81% / 4.48% while showing a structurally equivalent traffic-light comparator contributes 0.00%.

**Why this satisfies the "clearly identifiable contribution beyond IPoSCI" requirement without manufacturing difference:**

| | IPoSCI extended abstract | v5 at AAI |
|---|---|---|
| Architecture | ✅ reported | exposition only |
| Formal properties & proofs | ❌ absent | ✅ **core** |
| Comparator ladder C0–C3 | ❌ absent | ✅ **core** |
| C1≡C3 at 0.00% | ❌ absent | ✅ **new result** |
| Δ_L2 ≡ P(S=CAUTION) | ❌ absent | ✅ **new result** |
| Threshold sensitivity | ❌ absent | ✅ **new analysis** |
| Declared exclusions / lower bound | ❌ absent | ✅ **new argument** |
| Bounded executable conformance | ❌ absent | ✅ present |
| 5.81% / 4.48% | ✅ reported | ✅ **same — and must stay the same** |

**The results do not change, the terminology does not change, and nothing is renamed.** The extension is real: formal results, a comparator design, two analytical findings and a sensitivity study that the abstract does not contain. That is a normal full-paper extension of a presented abstract — and it is what makes disclosure safe rather than risky.

### Second choice
**Track 1**, if the planner judges the KR&R framing stronger for this reviewer pool. Same contribution set, weight shifted from B toward C, with the pre-inference admissible-set argument as the lead. Accept the reviewer-mismatch risk. **Do not reach for the "agentic" label to improve fit.**

---

## 11. Open items for the planner

| # | Item | Why it blocks |
|---|---|---|
| 1 | 🔴 **Resolve the IPoSCI publication route** | AAI is *not* an IPoSCI option. If the abstract defaults to the e-Proceedings it becomes a **published** prior work and v5 must be written and disclosed as an extension |
| 2 | 🔴 **Confirm blind vs non-blind** | v4 is written double-blind; AAI appears to require author identification on page 1 |
| 3 | 🔴 **Resolve the date inconsistency** | Notification (12 Oct) precedes the extended deadline (19 Oct) |
| 4 | 🟠 **Ask AAI for its similarity threshold and prior-publication policy** | Neither is published; silence is not permission |
| 5 | 🟠 **Recover the IPoSCI reviewer comments** | May contain criticism that bears on v5's framing |
| 6 | 🟢 Confirm the 4–6 page limit against v4's word budget | v4 was built to a six-page envelope — likely compatible |

**Unchanged:** `age_i` remains OPEN. `RESOLUTION_PAIRWISE_C0_C1_C0_C2 = PROVENANCE_INCOMPLETE` remains withheld. Do not run `{m,w}`. The non-claims in §2 are inviolable.

---

*Analysis complete. All five tracks assessed. No planning performed, no manuscript drafted, no research framing altered. Track descriptions verified against the official AAI 2026 site on 2026-09-23 and found identical to those supplied in the task.*

**Source:** https://aai.unimap.edu.my/index.php/event/call-for-paper
