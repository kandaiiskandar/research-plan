# Supervisor Feedback Response — IPSci 2026 Conference Paper

**Date:** 2026-08-12  
**Status:** Paper under review. This document tracks the response to each supervisor comment for use when revisions are requested.  
**Key source:** Much of the content needed for points 2–9 is already drafted in the journal paper at `publications/active/journal-1/submissions/v1-initial-submission/manuscript.md`. Adapt from there rather than rewriting from scratch.

---

## Point 1 — Clearly emphasise the novelty and contribution

**Status:** ✅ Done — 2026-08-20. Novelty paragraph inserted in Introduction after Fig. 1 reference in `manuscript-v2.5-submitted.md`. Opens with "The contribution is the second dimension — advisory scope — which existing architectures leave entirely unaddressed." Separates G(S) (participation) from A_AI(S) (advisory scope) and closes with "CAUTION is not a softer version of SAFE; it is a formally distinct governance position that binary architectures cannot express."

**Answer:**  
The core novelty is the governance pair **(G(S), A_AI(S))** as a two-level mechanism — specifically the CAUTION mode, which no reviewed architecture implements. The sharpest way to state it:

> Existing governance architectures conflate two distinct governance dimensions into a single binary variable: whether the AI participates. This paper separates them. G(S) governs participation. A_AI(S) governs advisory scope. Under CAUTION — the novel intermediate state — G(S) = 1 (AI active) but A_AI(CAUTION) = {Go, Delay} ⊊ A_AI(SAFE). A binary architecture, having no A_AI mechanism, cannot express this: for any state where G = 1, the full recommendation set is available. CAUTION is not a softer version of SAFE; it is a formally distinct governance position that binary architectures have no vocabulary to name.

**Where content already exists:**  
- Journal manuscript Section 5.1 — architecture overview with explicit "prior architecture" contrast  
- Journal manuscript Section 5.4.4 — governance pair table, CAUTION explanation  
- Conference paper Fig. 1 — three governance dimensions (good visual anchor)

**What to add for revision:**  
Move the three-governance-dimensions framing (Fig. 1) earlier in the Introduction and add a single crisp sentence: *"The contribution is the second dimension — advisory scope — which existing architectures leave entirely unaddressed."* This can be done in one paragraph without restructuring the paper.

---

## Point 2 — Add formal theoretical analysis or proofs

**Status:** ✅ Done — 2026-08-20. Formal Properties subsection added to `manuscript-v2.5-submitted.md` after the Formal Structure subsection. Contains Theorem 1 (Totality), Theorem 2 (Monotonicity) with case table, and Theorem 3 (Safety Dominance Property) with constructive proof sketch. All three use conference-paper numbering (1–3, not 6.1–6.3).

**Answer:**  
Three formal properties, all proved:

**Theorem 1 — Totality of f.** For all E in its domain, f(E) is defined and returns exactly one element of {SAFE, CAUTION, UNSAFE}. Proved by showing each per-component function gᵢ partitions its domain exhaustively and max_≻ over a finite totally ordered set is always defined and unique.

**Theorem 2 — Monotonicity of A_AI.** For all S₁, S₂ ∈ {SAFE, CAUTION, UNSAFE}, if S₁ ≻ S₂ then A_AI(S₁) ⊆ A_AI(S₂). Proved by exhaustive case analysis over the three ordered pairs. Corollary: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ — strict monotonicity.

**Theorem 3 — Safety Dominance Property.** For all E, AI(E) ⊆ A_AI(f(E)). Proved by construction: Layer 2 supplies RS(S) to Layer 3 before any reasoning begins; RS(CAUTION) contains only rules producing {Go, Delay}; the engine cannot produce types outside its active rule set.

**Where content already exists:**  
- Journal manuscript Section 6 — full proofs of all three theorems with case analysis  
- `docs/canonical/appendix-c-formalisation.md` — Theorems C.1, C.2, C.3 with full proofs  
- `docs/canonical/justification-layer3-enforcement.md` — enforcement mechanism and construction proof

**What to add for revision:**  
Extract the three theorem statements and proofs from the journal Section 6 and compress them into a "Formal Properties" subsection within the Proposed Architecture section. Full proofs can be referenced as supplementary material to stay within page limits.

---

## Point 3 — Include pseudocode or an algorithm describing the architecture workflow

**Status:** ✅ Done — 2026-08-20. Algorithm Specification subsection added to `manuscript-v2.5-submitted.md` after Formal Properties. Contains Algorithms 1–3 with inline comments. Closing paragraph explains that Step 3 of Algorithm 3 is the enforcement point and Step 6 is a construction invariant, not a runtime check.

**Answer — four algorithms:**

```
Algorithm 1: Safety Classification S = f(E)
Input:  E = (w, r, m, o, v, t)
Output: S ∈ {SAFE, CAUTION, UNSAFE}

1.  If any xᵢ ∈ E is undefined or corrupted: return UNSAFE  [fail-safe]
2.  Compute per-component states:
    S_w ← g_w(w)     // SAFE if w≤22, CAUTION if 22<w≤27, UNSAFE if w>27
    S_r ← g_r(r)     // SAFE if r∈{none,light,moderate}, CAUTION if heavy, UNSAFE if storm
    S_m ← g_m(m)     // SAFE if none, CAUTION if advisory, UNSAFE if warning/alert
    S_o ← g_o(o)     // SAFE if o<1.5m, CAUTION if 1.5≤o≤3.5m, UNSAFE if o>3.5m
    S_v ← g_v(v)     // SAFE if big, CAUTION if small/medium
    S_t ← g_t(t)     // SAFE if 6≤t<17, CAUTION if 17≤t<19, UNSAFE if 19≤t<6
3.  return max_≻ {S_w, S_r, S_m, S_o, S_v, S_t}
    // max_≻: UNSAFE > CAUTION > SAFE (worst-case dominates)

Algorithm 2: Governance Gate Evaluation
Input:  S ∈ {SAFE, CAUTION, UNSAFE}
Output: G(S) ∈ {0,1}, A_AI(S) ⊆ R

1.  If S = UNSAFE:
      G(S) ← 0
      A_AI(S) ← ∅
2.  If S = CAUTION:
      G(S) ← 1
      A_AI(S) ← {Go, Delay}
3.  If S = SAFE:
      G(S) ← 1
      A_AI(S) ← {Go, Delay, DepartureTime, Duration}
4.  return G(S), A_AI(S)

Algorithm 3: RS(S) Supply and Advisory Generation
Input:  E, S, G(S), A_AI(S)
Output: AI(E) ⊆ A_AI(S)

1.  If G(S) = 0: return ∅  [AI disabled]
2.  Select RS(S):
      If S = SAFE:    RS ← RS(SAFE)    // rules producing R = {Go,Delay,DepartureTime,Duration}
      If S = CAUTION: RS ← RS(CAUTION) // rules producing {Go,Delay} only
3.  Load RS into reasoning engine
4.  Execute reasoning engine against E with active rule set RS
5.  AI(E) ← set of recommendation types fired by the engine
6.  Assert AI(E) ⊆ A_AI(S)  [invariant — holds by construction]
7.  return AI(E)
```

**Where content already exists:**  
- Journal manuscript Section 7 — placeholder, lists the four algorithms to write  
- Journal manuscript Section 5.6.2 — RS(S) supply mechanism in prose  
- `docs/canonical/justification-layer3-enforcement.md` Section 3 — enforcement in pseudocode-style prose

**What to add for revision:**  
Write the three algorithms above into a new "Algorithm" subsection in the Proposed Architecture section. Algorithm 3 is the critical one to include — it directly demonstrates the Safety Dominance Property by showing where the RS(S) supply happens relative to inference.

---

## Point 4 — Discuss computational complexity and runtime efficiency

**Status:** ✅ Done — 2026-08-20. Computational Complexity subsection added to `manuscript-v2.5-submitted.md` after Algorithm Specification. Contains TABLE IV (six-row complexity table) and three-point narrative: O(1) governance layer, CAUTION cheaper than SAFE, latency dominated by data acquisition not governance computation. Closes with Katende [17] low-resource deployment requirement.

**Answer:**

| Component | Complexity | Notes |
|---|---|---|
| Safety classifier f(E) | O(1) time, O(1) space | Six independent threshold comparisons, no iteration |
| Governance gate G(S), A_AI(S) | O(1) time | Direct lookup on three-state enum |
| RS(S) selection | O(1) time | Pre-built rule sets, atomic swap on state change |
| Rule engine execution | O(n) time, O(n) space | n = number of rules in active RS(S); finite and bounded |
| Full governance pipeline | O(n) time | Dominated by rule engine; classifier and gate are O(1) |
| State transition (hysteresis check) | O(1) time | Dual-threshold comparison at boundary |

**Key points for the paper:**
- The governance layer (Layers 1–2) runs in O(1) — six threshold comparisons and a maximum. No iteration, no learned inference, no GPU.
- Layer 3 runtime is O(n) in the rule set size. RS(CAUTION) is a strict subset of RS(SAFE), so governance restriction actually reduces runtime under CAUTION — the more restrictive state is also the faster one.
- Worst-case decision latency: the governance overhead is deterministic and bounded. The full pipeline latency is dominated by external API calls for environmental data (w, r, m, o), not by the governance computation.
- This meets the Katende (2026) hard requirement for AI deployed on constrained devices: bounded-time inference with no dependency on GPU or cloud compute.

**Where content already exists:**  
- Journal manuscript Section 8 — placeholder listing the questions to answer  
- `docs/canonical/justification-layer3-enforcement.md` Section 2a — O(1) / O(n) characterisation mentioned  
- `docs/canonical/justification-layer3-enforcement.md` Section 2 — comparison table noting "O(1)" for production rule engine

**What to add for revision:**  
Write a short paragraph (or small table) in the Proposed Architecture section covering O(1) classifier, O(n) rule engine, and the note that CAUTION is cheaper than SAFE. No formal complexity proof needed — a worked characterisation is sufficient for a conference paper.

---

## Point 5 — Validate through experiments or simulations

**Status:** Evaluation design is fully specified in `docs/canonical/evaluation-design-rq4.md`. Experiments not yet run — this is thesis work (RQ4).

**Answer:**  
The evaluation runs 20 scenarios across five categories under three conditions:

| Condition | Description |
|---|---|
| C0 — Ungated | No governance; AI outputs full R at all states |
| C1 — Binary-gated | Level 1 only: G(S) gates participation, full scope when active |
| C2 — Graduated | Full proposed architecture: both G(S) and A_AI(S) active |

**Primary metric:** Safety Dominance Property compliance — for each scenario under C2, verify AI(E) ⊆ A_AI(f(E)). Requirement: 100%.

**Discriminating result:** Under CAUTION, C0 and C1 both produce DepartureTime and Duration; C2 does not. This is the direct empirical evidence that Level 2 governance adds capability that Level 1 alone cannot.

**Scenario categories:** Pure SAFE (5), Pure CAUTION (5), Pure UNSAFE (5), Boundary (3), Adversarial (2).

**Where content already exists:**  
- `docs/canonical/evaluation-design-rq4.md` — full evaluation design: 20 scenarios, E vectors, expected classifications, per-metric verification protocol  
- Journal manuscript Section 10 — three-condition comparison outline  
- Journal manuscript Section 11 — placeholder for results

**What to add for revision:**  
Run the 20 scenarios (simulation, not user study), record the AI(E) outputs under each condition, and tabulate the results. The evaluation design is complete — execution is what's needed. Present a results table showing C0/C1/C2 output types per scenario category, especially the CAUTION rows.

---

## Point 6 — Include an ablation study

**Status:** Already designed in journal manuscript Section 12. Needs execution.

**Answer — four ablation conditions:**

| Ablation | What is removed | What it measures |
|---|---|---|
| Remove A_AI restriction | A_AI(S) = full set at all states | Reduces to binary gate; confirms Level 2 adds value |
| Remove G(S) gate | G(S) = 1 always | Removes participation control; measures value of Level 1 |
| Remove hysteresis smoothing | Hard state transitions at boundaries | Measures mode-chattering frequency near SAFE/CAUTION boundary |
| Remove worst-case aggregation | Replace max_≻ with mean or majority vote | Measures misclassification rate at boundary scenarios |

The first ablation (remove A_AI) is the most important — it directly isolates the Level 2 contribution, which is the paper's primary claim.

**Where content already exists:**  
- Journal manuscript Section 12 — ablation plan with all four conditions listed

**What to add for revision:**  
Run the first two ablation conditions against the 20 evaluation scenarios (same input, different governance logic). Results table: scenario ID, expected S, AI(E) under full architecture vs. each ablation. One paragraph interpreting the difference.

---

## Point 7 — Expand discussion on deployment challenges and limitations

**Status:** ✅ Done — 2026-08-20. Deployment Challenges and Limitations subsection added to `manuscript-v2.5-submitted.md` as the final subsection of Proposed Architecture, before Conclusion. Two paragraphs: (1) four challenges in bold inline headings — connectivity/fail-safe, hardware, threshold maintenance, mode-chattering; (2) three limitations — domain-specific R, rule set correctness vs. Safety Dominance, human override unconditional.

**Answer — key deployment challenges:**

**Connectivity.** The architecture is designed offline-first: the governance classifier f(E) and rule engine RS(S) must operate without real-time API access. Environmental data (w, r, m, o) may be pre-cached or sourced from local sensors. The fail-safe rule (if any xᵢ = ⊥, return UNSAFE) ensures graceful degradation when data feeds are unavailable.

**Hardware constraints.** Target deployment: commodity smartphones or low-cost single-board computers (< $50). O(1) governance layer and O(n) rule engine both execute without GPU. Storage footprint for RS(SAFE) and RS(CAUTION) is minimal.

**Threshold maintenance.** Classification thresholds (g_w, g_o, etc.) are anchored to MET Malaysia published criteria. As climate patterns shift or MET Malaysia revises criteria, thresholds must be recalibrated and RS(S) must be updated to preserve A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅.

**Mode-chattering.** At classification boundaries (e.g., wind near 22 kn), rapid S oscillation would produce unstable advisory output. Mitigated by dual-threshold hysteresis: state transitions require sustained condition change before reclassification. Empirical validation of hysteresis parameters is part of the prototype work.

**Limitations:**
- The current recommendation type space R = {Go, Delay, DepartureTime, Duration} is domain-specific. Extension to other domains requires instantiating a new A_AI(S) and RS(S) for that domain's recommendation vocabulary.
- The rule sets RS(SAFE) and RS(CAUTION) require domain expert validation. Errors in rule encoding do not violate the Safety Dominance Property (construction holds regardless) but can produce incorrect advisory output within the permitted scope.
- The architecture governs advisory scope — not final decisions. Human override is unconditional. User study evidence (RQ5) is needed to assess whether CAUTION mode actually reduces over-reliance in practice.

**Where content already exists:**  
- Journal manuscript Section 13 — deployment challenges listed as bullet points  
- `docs/canonical/justification-layer3-enforcement.md` Section 6 — limitations of rule-based choice  
- Journal manuscript Section 5.6.3 — low-resource deployment rationale  
- Journal manuscript Section 5.2 — fail-safe rule for missing inputs

**What to add for revision:**  
Write a "Deployment Challenges and Limitations" subsection in the Discussion or at the end of the Proposed Architecture section. Approximately 3–4 paragraphs covering: connectivity/fail-safe, hardware, threshold maintenance, mode-chattering, and the three limitations above.

---

## Point 8 — Explain generalisation to other safety-critical domains

**Status:** ✅ Done — 2026-08-20. Generalisation subsection added to `manuscript-v2.5-submitted.md` before Deployment Challenges. Contains: three-step recipe (define E, define f(E), define R and A_AI(S)); formal properties transfer statement; TABLE V with two domain examples (Bhuvaneswari et al. [19] healthcare, Perez-Cerrolaza et al. [21] industrial/transportation); closing caveat that domain-specific empirical validation is still required.

**Answer:**  
The architecture is domain-independent at the structural level. The three steps that must be instantiated for a new domain are:

1. **Define E** — the observable parameters relevant to that domain's risk classification
2. **Define S = f(E)** — per-component threshold functions and worst-case aggregation
3. **Define R and A_AI(S)** — the recommendation type space and the admissible subsets per state

The formal properties (Totality, Monotonicity, Safety Dominance) transfer automatically to any correct instantiation — they are proved from the structure, not from the fisheries-specific values.

**Example generalisations:**

| Domain | E components | CAUTION mode restriction (example) |
|---|---|---|
| Emergency triage (Bhuvaneswari et al., 2025) | Patient acuity score, resource availability, staffing level | Restrict to {Triage, Refer} — withhold specific treatment protocols under resource scarcity |
| Industrial process safety (AISAFETY, Di Paco et al.) | Equipment state, worker proximity, ambient hazard | Restrict to {Stop, Alert} — withhold specific procedural steps under elevated hazard |
| Autonomous driving (marginal weather) | Weather severity, road condition, traffic density | Restrict to {Slow, Stop} — withhold specific route and manoeuvre recommendations under poor visibility |

In each case: the participation gate (G(S)) and advisory gate (A_AI(S)) remain the two-level governance mechanism. Only E, f(E), and A_AI(S) are re-instantiated.

**Where content already exists:**  
- Journal manuscript Section 13 — "Generalisation: which aspects are domain-independent" listed as content to include  
- `docs/canonical/architecture-illustration.md` — domain-independent pipeline statement

**What to add for revision:**  
One paragraph in the Discussion with the three-step generalisation recipe and one or two concrete domain examples from the literature already in the corpus (Bhuvaneswari et al. for healthcare, AISAFETY for industrial safety). Approximately 200 words.

---

## Point 9 — Include a Threats to Validity section

**Status:** ✅ Done — 2026-08-20. Threats to Validity added as a standalone section between Proposed Architecture and Conclusion in `manuscript-v2.5-submitted.md`. Four paragraphs covering internal (threshold selection + rule set completeness + prototype fidelity), external (single domain + engine type), construct (compliance rate ≠ quality + simulation fidelity), and conclusion validity (20-scenario set vs. construction proof).

**Answer — four categories:**

**Internal validity:**
- *Threshold selection:* Are SAFE/CAUTION/UNSAFE boundaries principled? Yes — anchored to MET Malaysia published criteria and three independent empirical sources (Jeong & Im 2023 for wave height; Atacan & Düzbastılar 2023 for time of day; Rahim et al. 2024 for wind/weather). Threat level: low.
- *Rule set completeness:* Do RS(SAFE) and RS(CAUTION) cover all deployment scenarios? Partial threat — rules are constructed for the fisheries domain and may not handle novel condition combinations. Mitigated by fail-safe rule (undefined input → UNSAFE).
- *Prototype fidelity:* Does the implementation faithfully realise the formal specification? Verified through the 20-scenario evaluation — 100% Safety Dominance compliance is the fidelity check.

**External validity:**
- *Generalisability:* Results are demonstrated in one domain (Malaysian coastal fisheries, Kota Kinabalu). The formal properties transfer by construction to any correct instantiation, but whether the three-state governance structure is practically appropriate in other domains has not been empirically validated.
- *Non-symbolic engines:* The Safety Dominance proof requires a rule-based Layer 3. Applicability to ML or LLM advisory components would require a different enforcement argument.

**Construct validity:**
- *Advisory scope compliance rate:* The metric P(AI(E) ⊆ A_AI(S)) measures structural compliance, not advisory quality. A system could comply formally while producing unhelpful advice within the permitted scope. Addressed by the secondary metric (decision support utility).
- *Simulation vs. deployment:* Historical weather replay and constructed scenarios are a proxy for real deployment. Fishers making real departure decisions may encounter conditions or interaction patterns not covered by the 20-scenario set.

**Conclusion validity:**
- *Small scenario set:* 20 scenarios may not be sufficient to conclude that the formal guarantee holds universally. Mitigated by the construction proof — the guarantee holds for all E by proof, not by testing.

**Where content already exists:**  
- Journal manuscript Section 14 — all four validity categories outlined with specific threats listed

**What to add for revision:**  
Write Section 14 as a 4–5 paragraph section using the content above. Each threat can be stated and immediately addressed (mitigation strategy). Approximately 400 words.

---

## Point 10 — Strengthen the conclusion

**Status:** ✅ Done — 2026-08-20. Conclusion fully rewritten in `manuscript-v2.5-submitted.md` with four-paragraph structure: (1) gap + mechanistic basis + consequence [4][7][23][24][25][26][27]; (2) two contributions — gap confirmation + governance pair with CAUTION mode + Safety Dominance by construction; (3) formal guarantees — Theorems 1–3 with completeness/consistency/effectiveness characterisation; (4) future work — C0/C1/C2 evaluation, RQ5 user study, domain generalisation, IEC 61508 certification pathway, ML extension caveat.

**Answer — suggested conclusion structure:**

**Paragraph 1 — The gap and its consequences.**  
Existing AI governance in safety-critical decision support is binary. Operators in marginal conditions receive full-scope tactical advice at the moment the underlying data can no longer support it. No existing architecture restricts advisory scope as a function of classified environmental risk.

**Paragraph 2 — The contribution.**  
This paper contributes two things. First, a structured review of 72 papers plus three large-scale systematic reviews confirms the binary governance gap from four independent bodies of literature. Second, the graduated safety-state-gated architecture closes the gap through a formally specified governance pair (G(S), A_AI(S)) that produces a CAUTION mode — a formally distinct intermediate governance position that no reviewed architecture implements. The Safety Dominance Property (AI(E) ⊆ A_AI(S)) holds by construction, not by runtime monitoring.

**Paragraph 3 — Formal guarantees (if proofs are added).**  
Three formal properties are proved: Totality of f (the classifier has no undefined states), Monotonicity of A_AI (advisory scope never expands as conditions worsen), and the Safety Dominance Property (AI output is bounded within the admissible scope at every state, by construction). Together they characterise a governance mechanism with no formally identifiable path by which AI recommendations can exceed their warranted scope.

**Paragraph 4 — Future work.**  
Immediate next steps: (1) prototype implementation and experimental validation against the three-condition comparative evaluation (C0/C1/C2); (2) user study with small-scale fishers across the three safety states (RQ5); (3) generalisation to at least one additional safety-critical domain to validate domain independence. Longer-term: formal certification pathway (IEC 61508, maritime safety standards), and extension of R to cover recommendation types that require learned inference rather than rule-based reasoning.

**Where content already exists:**  
- Conference paper conclusion — good final two paragraphs on the governance pair and future work  
- Journal manuscript Section 15 — contribution structure listed

**What to add for revision:**  
Replace or substantially expand the current conclusion with the four-paragraph structure above. Add formal guarantee references if proofs are included (Point 2). Explicitly name future work items.

---

## Point 11 — Improve figures with clearer labels, colour coding, and illustrative examples

**Status:** Conference paper figures are embedded images in the submitted .docx. The .md version uses ASCII art for Figs 3 and 4.

**Answer — figure-by-figure improvement plan:**

**Fig. 1 — Three governance dimensions:**  
Add colour coding: Dimension 2 (this paper's contribution) in a distinct colour (e.g., blue highlight). Label each dimension with the type of mechanism that addresses it. Add a "gap" marker between Dimensions 1 and 2.

**Fig. 2 — Review process:**  
Straightforward flowchart. Improve by labelling the number of papers at each stage. Add a box explicitly labelling "Gap identified" at the synthesis step.

**Fig. 3 — Architecture flow:**  
The most important figure. Improvements: colour-code by governance layer (Layer 1 neutral, Layer 2 governance in one colour, Layer 3 AI in another). Label the two decision points explicitly: "Level 1: G(S)" and "Level 2: A_AI(S)". Add the mathematical notation (G(S) = 0 / G(S) = 1) on the branching arrows. Make the CAUTION branch visually distinct.

**Fig. 4 — State transitions (illustrative scenario):**  
Replace or supplement the ASCII table with a proper state transition diagram showing SAFE → CAUTION → UNSAFE with the advisory scope at each state labelled. Add input vector values as annotations. Colour-code each state (green/amber/red is the natural choice, consistent with Flehmig et al.'s traffic-light metaphor that appears in the literature review).

**Where content already exists:**  
- Conference paper .docx has embedded versions of all four figures  
- ASCII art versions in `manuscript-v2.5-submitted.md` for Figs 3 and 4

**What to add for revision:**  
Redraw Figs 3 and 4 using a diagram tool (draw.io, Inkscape, or similar). Apply consistent colour coding: green = SAFE, amber = CAUTION, red = UNSAFE. Ensure all text in figures is readable at single-column width.

---

## Point 12 — Provide more details on the literature review methodology and selection process

**Status:** Already addressed in the conference paper Methodology section. May need expansion.

**Answer:**  
The current Methodology section covers: structured (not systematic) scope, four databases (Scopus, IEEE Xplore, Web of Science, ACM DL), search strings, three large-scale systematic reviews as secondary evidence, 72 papers to full review, and four-dimension coding. The PRISMA-style process is captured in Fig. 2.

**If reviewer asks for more detail, add:**
- Explicit inclusion/exclusion criteria (inclusion: mechanisms constraining AI behaviour at runtime in safety-critical/human-in-the-loop contexts; exclusion: training-time or static-configuration approaches only)
- Saturation statement: papers were added iteratively through citation tracing until no new governance mechanisms emerged
- Inter-rater reliability: the four-dimension coding was performed by the author; limitations of single-coder coding should be acknowledged in Threats to Validity

**Where content already exists:**  
- Conference paper Methodology section — covers all the above at current level  
- `docs/superpowers/plans/2026-07-16-ipsci-paper-v4-revision.md` Task 4 — full expanded methodology text (Section 3.1, 3.2, 3.3) that was drafted for v5

**What to add for revision:**  
If the reviewer specifically requests more detail, restore the three-subsection expanded methodology from the v4 revision plan (3.1 Search Strategy, 3.2 Screening and Coding, 3.3 Theme Development). This is already fully written — it was removed to fit page limits.

---

## Point 13 — Include references to established AI governance standards and frameworks

**Status:** ✅ Done — 2026-08-20. Three sentences added to Proposed Architecture section (before Formal Structure subsection) in `manuscript-v2.5-submitted.md`. Covers: NIST AI RMF [35] runtime tier mapping; IEC 61508/ISO 26262 as graduated constraint precedent; Bloomfield & Rushby [20] deterministic guard principle at advisory scope level. NIST AI RMF added as reference [35] (replaces placeholder).

**Answer — relevant standards in the corpus:**

| Standard / Framework | Relevance to this architecture |
|---|---|
| NIST AI RMF 1.0 (NIST 2023) | Risk-tiered governance framework; the three safety states map to risk tiers | 
| IEC 61508 (SIL levels) | Safety Integrity Levels — graduated safety classification principle; analogue for the three-state architecture |
| ISO 26262 (ASIL levels) | Automotive safety; graduated safety levels analogous to SAFE/CAUTION/UNSAFE; enforces by-construction constraints |
| SOLAS / COLREGS | Maritime safety conventions; establish the regulatory context for the fisheries domain |
| Dalrymple et al. (2024) — Guaranteed Safe AI | Already cited as [9]; the architecture is a domain-specific, state-conditioned GS instantiation |
| Bloomfield & Rushby (2025) — Assurance from Dependability Perspective | Already cited as [20]; provides the deterministic guard principle |
| Perez-Cerrolaza et al. (2024) — AI Safety-Critical Survey | Already cited as [21]; establishes that safety mechanisms in automotive/avionics/railway are calibrated to err toward restriction |
| Engin & Hand (2025) — Dimensional Governance | Already cited as [29]; proposed explicit thresholds over monitored dimensions — the architecture realises their proposal with enforcement |

**NIST AI RMF:** The NIST AI Risk Management Framework (2023) defines risk tiers for AI systems in safety-critical applications. The SAFE/CAUTION/UNSAFE classification in this architecture operationalises the NIST tiered approach at runtime — UNSAFE maps to the highest risk tier where AI participation is suspended; CAUTION maps to an intermediate tier where advisory scope is formally bounded.

**IEC 61508 / ISO 26262:** Both standards use graduated safety levels (SIL 1–4, ASIL A–D) where higher levels impose stricter design and verification requirements. The A_AI(S) contraction from SAFE to CAUTION directly mirrors this graduated restriction principle — as risk level increases, the permitted action space contracts. The Safety Dominance Property proved in this paper is the runtime analogue of the by-construction requirements in these standards.

**Where content already exists:**  
- `notes/NIST AI RMF 1.0` — notes file exists in corpus  
- Journal manuscript Section 3 — "Relevant standards: IEC 61508 SIL levels, ISO 26262 ASIL, maritime safety regulations (SOLAS, COLREGS)" listed as content to include

**What to add for revision:**  
Add 2–3 sentences in the Introduction or Related Work section situating the proposed architecture within established governance standards. Cite NIST AI RMF, reference IEC 61508/ISO 26262 as precedent for graduated safety constraints, and note that the architecture operationalises the deterministic guard principle of Bloomfield & Rushby (2025) at the advisory scope level. These citations are already in the corpus — no new literature search required.

---

## Summary Status Table

| Point | Status | Source for content | Action required |
|---|---|---|---|
| 1. Novelty emphasis | ✅ Done | manuscript-v2.5-submitted.md §Introduction | — |
| 2. Formal proofs | ✅ Done | manuscript-v2.5-submitted.md §Formal Properties | — |
| 3. Pseudocode | ✅ Done | manuscript-v2.5-submitted.md §Algorithm Specification | — |
| 4. Complexity | ✅ Done | manuscript-v2.5-submitted.md §Computational Complexity | — |
| 5. Experiments | Design exists, not run | evaluation-design-rq4.md, Journal §10 | Run 20 scenarios, tabulate results |
| 6. Ablation | Design exists, not run | Journal §12 | Run ablation on 4 conditions |
| 7. Deployment challenges | ✅ Done | manuscript-v2.5-submitted.md §Deployment Challenges and Limitations | — |
| 8. Generalisation | ✅ Done | manuscript-v2.5-submitted.md §Generalisation | — |
| 9. Threats to Validity | ✅ Done | manuscript-v2.5-submitted.md §Threats to Validity | — |
| 10. Conclusion | ✅ Done | manuscript-v2.5-submitted.md §Conclusion | — |
| 11. Figure improvements | Images in .docx | ASCII art in .md | Redraw Figs 3 and 4 with colour |
| 12. LR methodology | Already in paper | Conference paper §Methodology, v4 plan | Expand if reviewer requests |
| 13. Governance standards | ✅ Done | manuscript-v2.5-submitted.md §Proposed Architecture | — |
