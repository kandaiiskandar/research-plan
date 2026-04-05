# Literature Review Plan

**Date**: 2026-04-05
**Papers analysed**: 55 (25 full extraction, 24 reduced extraction, 6 methodological foundation, 0 early stop, 0 skipped)

---

## 1. Theme Gap Analysis

### Theme Coverage Summary

| Theme | Code | Yes | Partial | No | Coverage |
|-------|------|-----|---------|-----|----------|
| Hybrid AI (rule-based + probabilistic) | T1 | 14 | 20 | 15 | Well-Covered |
| Safety-critical AI decision systems | T2 | 30 | 10 | 9 | Well-Covered |
| AI governance (Level 1 + Level 2) | T3 | 22 | 15 | 12 | Well-Covered |
| Low-resource environments | T4 | 4 | 13 | 32 | Partially Covered |
| Decision architecture formalisation | T5 | 7 | 21 | 21 | Partially Covered |
| Human role in AI-assisted decision-making | T6 | 21 | 20 | 8 | Well-Covered |
| Socio-technical evaluation | T7 | 8 | 19 | 22 | Partially Covered |
| Coastal fisheries / maritime domain | T8 | 8 | 5 | 36 | Partially Covered |

### T1: Hybrid AI — Well-Covered

**Key papers (Yes)**: SYNAPSE (Castagnone), Bhuvaneswari, Punzi, AgentSpec (Wang), Perez-Cerrolaza, Bloomfield/Rushby, Mussi, Flehmig/Flehmig, SAFEXPLAIN (Abella), Shields (Konighofer), Gyllenhammar, Dalrymple, Kalmykov, Yuzui/Kaneko

**Assessment**: Strong coverage across neuro-symbolic, supervisory control, and governance-based hybrid architectures. Sufficient to establish that hybrid AI is well-studied but none implement two-level governance.

### T2: Safety-critical AI — Well-Covered

**Key papers (Yes)**: Shields, AgentSpec, Dalrymple, Bajcsy/Fisac, SAFEXPLAIN, Bloomfield, Perez-Cerrolaza, Newcomb, Flehmig, Mussi, Baxi, Shamsujjoha, plus 18 others

**Assessment**: Extensive coverage. The strongest theme in the set. Establishes binary governance as the universal paradigm.

### T3: AI Governance — Well-Covered

**Key papers (Yes)**: AgentSpec, Shields, Dalrymple, Bajcsy, SAFEXPLAIN, Bloomfield, Perez-Cerrolaza, Newcomb, Flehmig, Baxi, Shamsujjoha, Chen, Mussi, Intl AI Safety Report, Bello, Selvam, Saup, Kluever, INSYTE, SYNAPSE, Gyllenhammar, Tumato

**Assessment**: Strong coverage — but critically, ALL implement Level 1 only or static Level 2. No paper implements state-conditioned two-level governance. This theme is well-covered precisely because it establishes the gap.

### T4: Low-resource environments — Partially Covered

**Key papers (Yes)**: Bhuvaneswari, Zhao/Yuan, Peskas, Katende, Tahsin
**Key papers (Partial)**: Haque/Al Jufaili, Stage-Gate, Talpur, Wing/Woodward, Bossier, Gao, Obi, Rahim, Kühn, Bloomfield, Perez-Cerrolaza, Gyllenhammar, Intl AI Safety

**Assessment**: 4 Yes papers cover healthcare, fisheries data platforms, and general low-resource AI. But no paper combines low-resource deployment with formal safety governance. Gap exists between the low-resource AI literature and the safety governance literature.

**Search suggestions**:
- "AI deployment resource-constrained safety-critical" in healthcare, disaster response
- "Edge AI safety governance" or "offline-capable decision support systems"
- Maritime/fisheries AI with explicit resource constraint discussion

### T5: Decision architecture formalisation — Partially Covered

**Key papers (Yes)**: AgentSpec, Shields, Dalrymple, Bajcsy/Fisac, Newcomb, Baxi, Tumato
**Key papers (Partial)**: 21 papers with partial formalisation

**Assessment**: 7 Yes papers provide strong formal models but all use binary safety boundaries. No formal model implements tripartite state classification (SAFE/CAUTION/UNSAFE) with graduated recommendation scope. Baxi is closest (K-tier graduated permissions with containment) but conditioned on robustness, not environmental state.

### T6: Human role — Well-Covered

**Key papers (Yes)**: 21 papers including Punzi (hybrid decision-making taxonomy), Gabriel (socio-technical requirements), Bloomfield, Perez-Cerrolaza, Mussi, Bhuvaneswari, Flehmig, INSYTE, Saup, Gabriel, Zhao/Yuan, Gao

**Assessment**: Well-covered. Establishes that human-AI decision support is the dominant paradigm. No paper evaluates user response to a system with three distinct governance states.

### T7: Socio-technical evaluation — Partially Covered

**Key papers (Yes)**: Bloomfield, Madsen/Kim, Zhao/Yuan, Gabriel, Saup, INSYTE, Intl AI Safety Report, Gyllenhammar (wait - N)

**Assessment**: Several papers address socio-technical considerations but few conduct empirical socio-technical evaluation of AI governance architectures. No paper evaluates user understanding of graduated AI participation modes, particularly the CAUTION state.

**Search suggestions**:
- "Trust in AI decision support" with empirical user studies
- "User perception AI automation levels" in safety-critical domains
- "Socio-technical evaluation AI governance" empirical studies

### T8: Coastal fisheries / maritime — Partially Covered

**Key papers (Yes)**: Haque/Al Jufaili, Wing/Woodward, Yuzui/Kaneko, Welch, Bossier, Peskas, Mandal, Obi, Rahim, Gao (some overlap with Partial)
**Key papers with fisheries focus**: Haque, Wing, Kühn, Mandal, Peskas, Welch, Obi, Gao, Rahim, Bossier

**Assessment**: 10 fisheries/maritime papers but NONE implement any AI governance mechanism. The domain is established as a context lacking formal AI safety governance — which is exactly the motivation needed for PS3.

---

## 2. Problem Statement Coverage

| Problem Statement | Coverage | Key comparators found | Key gaps |
|---|---|---|---|
| PS1: No intermediate AI participation mode | Well-Supported | Shields, AgentSpec, Dalrymple, Bajcsy, Flehmig, Baxi | Flehmig is named comparator — present in set |
| PS2: No environment-state-conditioned (G(S), A_AI(S)) | Well-Supported | Shields, Bajcsy, Baxi, Shamsujjoha, AgentSpec | All implement binary or differently-conditioned governance |
| PS3: No safety governance for low-resource fisheries | Partially Supported | Bhuvaneswari (healthcare analog), Peskas, Haque | No paper combines governance + fisheries |
| PS4: No graduated vs binary comparative evaluation | Partially Supported | McGrath S-TIAS, Schrills, CHAI-T, Bach, Aquilino, Atf & Lewis | No direct evaluation of graduated vs binary governance — methodological foundation established |
| PS5: No socio-technical evaluation of CAUTION mode | Partially Supported | McGrath S-TIAS, Schrills, CHAI-T, Bach, Aquilino, Atf & Lewis | No user study of intermediate governance mode — validated instruments and trust frameworks now in set |

### PS1: No architecture formally defines an intermediate AI participation mode with restricted recommendation space

**Coverage: Well-Supported**

| Paper | Role | How it relates |
|-------|------|----------------|
| Shields (Konighofer) | Comparator | Per-state safe action sets but no discrete governance modes or recommendation-type restriction |
| AgentSpec (Wang) | Comparator | Per-action binary enforcement; no global state classification |
| Dalrymple | Comparator | Policy-level binary verification; no graduated modes |
| Bajcsy/Fisac | Comparator | Binary permit/override via safety filter; most rigorous but no CAUTION mode |
| Flehmig/Flehmig | **Primary comparator** | Three-level traffic-light model — closest prior art. But governs monitoring intensity, not AI recommendation scope; triggered by AI performance, not environmental state |
| Baxi | Comparator | K-tier graduated permissions with containment — structurally parallel but conditioned on robustness, not environmental state |
| Perez-Cerrolaza | Establishes gap | Survey of all industrial/transport domains — binary governance universal |
| Newcomb | Establishes gap | SLR of 46 formal methods papers — all binary safety boundaries |
| Ramos | Establishes gap | SLR of 91 collaborative intelligence papers — all binary |
| Intl AI Safety Report | Establishes gap | All 11 Frontier AI Safety Frameworks implement binary participation control |

**Assessment**: Strong. The gap is convincingly demonstrated across multiple surveys and the primary comparator (Flehmig) is in the set.

### PS2: No architecture classifies environmental conditions into safety states that determine AI recommendation scope via (G(S), A_AI(S))

**Coverage: Well-Supported**

| Paper | Role | How it relates |
|-------|------|----------------|
| Shields | Comparator | Per-state safe action sets via MDP — closest to A_AI(S) but not discrete modes |
| Bajcsy/Fisac | Comparator | Continuous safety value function V(z^AI), not discrete environmental state classification |
| Baxi | Comparator | Discrete robustness tiers with nested permissions — formally closest but conditioned on agent properties, not environment |
| Dalrymple | Comparator | World model captures environment but verifier produces binary pass/fail, not tripartite classification |
| Shamsujjoha | Comparator | Most comprehensive Level 2 taxonomy (13 guardrail actions) but not state-conditioned |
| AgentSpec | Comparator | Per-action rule enforcement; no global environmental state classifier |
| Madsen/Kim | Motivates | Maritime AI already classifies risk into discrete levels for display — but not for governance |

**Assessment**: Strong. Multiple comparators show individual components exist (state classification, action restriction, gate functions) but none unifies them in a state-conditioned governance pair.

### PS3: No safety governance architecture designed for low-resource fisheries environments

**Coverage: Partially Supported**

| Paper | Role | How it relates |
|-------|------|----------------|
| Bhuvaneswari | Analog comparator | Hybrid AI for resource-constrained healthcare — closest domain analog but no governance architecture |
| Haque/Al Jufaili | Establishes gap | Surveys fisheries AI — no governance, no safety architecture |
| Peskas | Establishes gap | Demonstrates feasibility of automated fisheries data in low-resource settings but no decision support or governance |
| Katende | Fills background | Strongest characterisation of low-resource AI constraints |
| Gao | Motivates | Documents fisher decision-making in Penang — informal go/cautious-go/don't-go maps to SAFE/CAUTION/UNSAFE |
| Rahim | Motivates | Fisher survival decisions under extreme weather — validates CAUTION concept |
| Obi | Fills background | Malaysian fisheries sector overview |
| Wing/Woodward | Fills background | Fisheries AI ecosystem needs |

**Assessment**: Partial. Domain background is well-covered. The gap (no formal governance in fisheries) is easy to argue. But there are no close architectural comparators within fisheries — the argument relies on cross-domain comparison (safety governance from other domains + fisheries deployment context).

### PS4: No comparative evaluation of graduated two-level governance vs binary governance

**Coverage: Partially Supported (updated — 6 methodological foundation papers added)**

No paper directly compares graduated vs binary governance. However, 6 new methodological foundation papers now provide the theoretical and empirical grounding for the evaluation design:

| Paper | Role | What it provides |
|-------|------|-----------------|
| McGrath et al. (2025) — S-TIAS | Primary instrument | Validated 3-item trust scale (S-TIAS) directly adoptable as primary trust measure across all three PS4 conditions; provides trust calibration framework defining "better" as expectation–capability alignment |
| Schrills et al. (2025) — Questioning Trust | Methodological design | Demonstrates trust and behavioural dependence are distinct constructs; provides behavioural dependence metric (Cohen's Kappa); establishes dual-measurement design (attitudinal + behavioural); sample size benchmark: N=150 for 80% power |
| McGrath et al. (2025) — CHAI-T | Evaluation criterion | Trust calibration as the evaluative criterion — graduated governance should produce better calibration than binary; defines overtrust/undertrust as calibration failures, providing PS4's dependent variable vocabulary |
| Bach et al. (2024) — User Trust SLR | Instrument guidance | Recommends validated cross-context instruments (Jian et al. 2000; Gulati et al. 2019) over custom questionnaires; sample size guidance (M=326.80 across 23 studies) |
| Aquilino et al. (2025) — Decoding Trust | Instrument selection | Cognitive vs affective trust framework; predicts cognitive trust dominates low-anthropomorphism decision support — supports S-TIAS selection |
| Atf & Lewis (2026) — Explainability Meta-analysis | Benchmark | r = 0.194 explainability–trust correlation as baseline; PS4 can test whether graduated governance exceeds this baseline |

**What's still missing**: No paper compares graduated vs binary governance specifically. The three-condition design (ungated vs binary-gated vs two-level graduated) remains novel. But the evaluation methodology is now grounded rather than invented from scratch.

**Status rationale**: Moved from "Unsupported" to "Partially Supported" — methodological foundations established; direct evaluation precedent still absent.

### PS5: No socio-technical evaluation of graduated AI governance, particularly user response to CAUTION mode

**Coverage: Partially Supported (updated — 6 methodological foundation papers added)**

No paper evaluates user response to graduated AI participation modes. However, 6 new papers now provide the conceptual and instrumental foundations:

| Paper | Role | What it provides |
|-------|------|-----------------|
| McGrath et al. (2025) — S-TIAS | Primary instrument | Validated S-TIAS for measuring trust across governance states; highlights that performance-lens perception of restriction (CAUTION mode as "unreliability" vs "governance") is a key PS5 measurement challenge |
| Schrills et al. (2025) — Questioning Trust | Critical warning | Self-reported trust has only moderate correlation with behavioural dependence (r = 0.42–0.45); instructed reliability (i.e., communicated governance state) strongly shapes behaviour; PS5 must measure both attitudinal trust and behavioural reliance independently |
| McGrath et al. (2025) — CHAI-T | Trust dynamics framework | Temporal trust dynamics across collaboration episodes; predicts trust from SAFE mode episodes will be miscalibrated for CAUTION mode — a testable PS5 hypothesis; tripartite antecedents (human, technology, context) structure PS5's evaluation dimensions |
| Bach et al. (2024) — User Trust SLR | Measurement catalogue | Three-factor taxonomy (socio-ethical, technical/design, user characteristics); recommends validated instruments (HCTS, TiA scale) over custom questionnaires; Malaysia context addresses geographic concentration gap |
| Aquilino et al. (2025) — Decoding Trust | Mode-specific trust prediction | CAUTION mode restriction changes system profile → shifts trust from mixed cognitive–affective to primarily cognitive; warns against using purely cognitive instrument in SAFE condition |
| Atf & Lewis (2026) — Explainability Meta-analysis | Design risk | Interpretable models can engender distrust as well as trust; making CAUTION restriction transparent may produce appropriate caution OR inappropriate distrust — PS5 must distinguish these outcomes |

**What's still missing**: No paper evaluates user response to an *intermediate* governance mode ("AI active but restricted"). The CAUTION mode remains unmapped territory. PS5 is methodologically grounded but its specific contribution — evaluating the novel intermediate state — has no direct precedent.

**Status rationale**: Moved from "Unsupported" to "Partially Supported" — validated instruments and trust dynamics frameworks established; evaluation of intermediate governance mode remains novel.

---

## 3. Governance Level Analysis

### Governance Level Distribution

| Paper | L1 (G(S)) | L2 (A_AI(S)) | Unified State-cond. | Type |
|-------|-----------|-------------|---------------------|------|
| Shields (Konighofer) | Yes | Partial | Partial | Binary per-state |
| AgentSpec (Wang) | Partial | No | No | Per-action binary |
| Dalrymple | Yes | Partial | No | Binary policy-level |
| Bajcsy/Fisac | Yes | Partial | Partial | Binary (permit/override) |
| SAFEXPLAIN (Abella) | Yes | Partial | No | Binary runtime; graduated design-time |
| Liang | Partial | No | No | Binary per-output |
| Shamsujjoha (Swiss Cheese) | Partial | Yes | No | Binary per-artifact; comprehensive L2 taxonomy |
| Flehmig/Flehmig | Yes | No | Partial | Binary; traffic-light governs monitoring only |
| Baxi (Comprehension-Gated) | Yes | Yes | Yes* | Graduated K-tier (*robustness-conditioned, not environment) |
| Bloomfield/Rushby | Yes | No | No | Binary (permit/override) |
| Perez-Cerrolaza | Yes | No | No | Binary across all domains |
| Newcomb/Ochoa | Yes | No | No | Binary (46 studies) |
| Mussi | Partial | Partial | No | Design-time graduated |
| INSYTE (Porter) | Partial | No | No | Classification only |
| Intl AI Safety Report | Yes | No | No | Binary (all 11 frameworks) |
| Chen (AI Safety LLM) | Yes | Partial | No | Binary (guardrail system) |
| Gyllenhammar | Yes | Partial | No | Binary (simplex switching) |
| Selvam | Partial | Partial | No | Design-time static autonomy levels |
| Tumato (Vermaelen) | Yes | No | No | Binary per-action |
| Kluever | Partial | No | No | Binary (design-time SIL) |
| Saup | Partial | Partial | No | Organisational; post-generation |

### Summary

- **Level 1 only (binary gate)**: ~15 papers implement clear binary participation control
- **Any form of Level 2**: ~10 papers restrict AI output scope in some form
- **Level 2 state-conditioned**: 2 papers — Shields (per-state action sets, continuous), Baxi (robustness-state tiers)
- **Unified two-level, environment-state-conditioned**: **0 papers**

**Gap confirmed**: No paper in the set implements both levels in a unified governance pair conditioned on classified environmental safety state. Baxi is structurally closest (graduated tiers with containment) but conditions on agent robustness, not environmental state. Shields is formally closest (per-state safe action sets) but does not define discrete governance modes or recommendation-type restriction.

---

## 4. Formal Component Coverage

| Formal Component | Papers that address it | Papers that come close | Gap? |
|---|---|---|---|
| Environmental state vector E | Bajcsy (z), AgentSpec (S, Omega), Dalrymple (world model), Shields (MDP state), Tumato (state vars) | Bhuvaneswari (X_t input vector) | No — concept exists but not as E = {w,r,m,o,v,t} |
| Safety state classification S = f(E) | None (tripartite) | Shields (safe/dangerous/unsafe partition), Bajcsy (V(z^AI) continuous), Flehmig (traffic-light) | **Yes** — no discrete tripartite classification of environmental state |
| Participation gate G(S) | Shields (winning region), Bajcsy (safety filter), Dalrymple (verifier), Tumato (allowed predicate), Bloomfield (backup guard) | AgentSpec (per-action), Liang (per-output) | No — binary gate concept well-established |
| AI-admissible recommendation space A_AI(S) | None (state-conditioned) | Shields (per-state safe action sets — closest), Baxi (nested permission tiers), Shamsujjoha (guardrail taxonomy) | **Yes** — no state-conditioned recommendation-type restriction |
| Containment: A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅ | None | Baxi (E(T_k) ⊂ E(T_{k+1}) — structurally identical property), Shields (inductive winning region) | **Yes** — no tripartite containment for recommendation types |
| Two-level governance pair (G(S), A_AI(S)) | None | Baxi (f(R), E(T_k)) — closest structural analog | **Yes** — core novel contribution |
| Safety Dominance Property: AI(E) ⊆ A_AI(S) | None (graduated) | Bajcsy (Theorem 1 — binary), Shields (never visit unsafe states — binary), Baxi (bounded exposure — robustness-conditioned), Tumato (soundness), Newcomb (CBFs — binary) | **Yes** — safety dominance for graduated governance is novel |

### Assessment

**Components with precedent (not novel)**:
- Environmental state representation (E) — well-established in multiple formalisms
- Participation gate (G(S)) — binary gate is universal

**Components with structural analogs but no direct precedent (partially novel)**:
- Safety state classification (S = f(E)) — Flehmig's traffic-light and Shields' state partition come closest but neither classifies environmental state into discrete governance-triggering modes

**Components with no precedent (novel contributions)**:
- State-conditioned recommendation space A_AI(S) with recommendation-type restriction
- Tripartite containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅
- Unified two-level governance pair (G(S), A_AI(S))
- Safety Dominance Property for graduated (non-binary) governance

---

## 5. Argumentative Chain

### Link 1: Safety-critical systems increasingly use AI
**Papers**: Perez-Cerrolaza (cross-domain survey), Intl AI Safety Report (global assessment), Bloomfield/Rushby (dependability perspective)
**PS mapping**: Background
**Transition**: *"But AI in safety-critical contexts creates a governance problem: when should AI be allowed to participate, and what should it be allowed to recommend?"*

### Link 2: Hybrid AI combines deterministic rules with probabilistic reasoning
**Papers**: SYNAPSE (neuro-symbolic), Punzi (hybrid taxonomy), Shields (rule-filtered RL), Bhuvaneswari (hybrid triage), Kalmykov (XXAI), Yuzui/Kaneko (hybrid risk analysis)
**PS mapping**: Background
**Transition**: *"But the boundary between deterministic safety control and probabilistic AI reasoning must itself be governed — raising the question of how AI participation is controlled."*

### Link 3: Existing governance is binary — AI on/off (Level 1 participation governance)
**Papers**: Shields (winning region gate), Dalrymple (verifier gate), Bajcsy (safety filter), SAFEXPLAIN (supervision function), Bloomfield (backup guard), AgentSpec (per-action enforcement), Perez-Cerrolaza (binary across all domains), Newcomb (binary in all 46 studies), Ramos (binary in all 91 studies), Intl AI Safety Report (binary in all 11 frameworks), Tumato (binary allowed predicate)
**PS mapping**: PS1
**Transition**: *"Level 1 governance — whether AI operates at all — is well-established. But controlling what AI may recommend (Level 2) is a separate governance question."*

### Link 4: Some systems restrict AI output scope (Level 2), but statically
**Papers**: Shamsujjoha (13 guardrail action types — most comprehensive Level 2 taxonomy), Chen (guardrail system architecture), AgentSpec (per-action rules), Selvam (four autonomy levels — design-time), SAFEXPLAIN (DL usage levels — design-time), Mussi (hierarchical action constraints — design-time)
**PS mapping**: PS1, PS2
**Transition**: *"Level 2 governance exists — but it is applied per-action or configured at design-time, not conditioned on classified environmental safety state. No architecture dynamically adjusts AI advisory scope based on operational conditions."*

### Link 5: No architecture unifies both levels conditioned on environmental safety state
**Papers**: Flehmig/Flehmig (closest — traffic-light but governs monitoring intensity, not recommendation scope), Baxi (graduated tiers with containment but robustness-conditioned, not environment-conditioned), Shields (per-state safe actions but continuous, not discrete governance modes)
**PS mapping**: PS1, PS2
**Transition**: *"Flehmig et al. is the closest prior art: a three-level traffic-light governance model. But it is triggered by AI performance degradation, governs monitoring intensity rather than recommendation scope, and operates at a single governance level. No architecture implements both participation governance G(S) and advisory scope governance A_AI(S) as a unified pair conditioned on environmental safety state."*

### Link 6: No formal Safety Dominance Property for graduated governance
**Papers**: Bajcsy (Theorem 1 — binary), Shields (safety guarantee — binary), Newcomb (CBFs, reachability — binary), Baxi (bounded exposure — robustness-conditioned), Tumato (soundness — binary)
**PS mapping**: PS2
**Transition**: *"Formal safety properties exist for binary governance (shields, safety filters, CBFs), but none defines a Safety Dominance Property for graduated governance where AI outputs must fall within a state-dependent recommendation space that narrows as risk increases."*

### Link 7: This gap matters in low-resource, safety-critical domains
**Papers**: Katende (low-resource AI constraints), Bhuvaneswari (healthcare in resource-constrained settings), Haque/Al Jufaili (fisheries AI — no governance), Peskas (feasibility of fisheries data platforms), Gao (fisher decision-making in Penang), Rahim (fisher survival decisions under extreme weather)
**PS mapping**: PS3
**Transition**: *"Small-scale coastal fisheries represent a safety-critical, low-resource domain where AI must operate under intermittent connectivity, limited data, and varying environmental risk — yet no formal safety governance architecture exists for this context."*

### Link 8: No evaluation compares graduated vs binary governance
**Papers**: (Gap — no paper directly addresses this)
**PS mapping**: PS4
**Transition**: *"Existing evaluations compare gated versus ungated AI (does governance help at all?), but none isolates the contribution of Level 2 advisory scope governance beyond Level 1 participation governance — does the CAUTION mode add value beyond a binary gate?"*

### Link 9: No socio-technical evaluation of user response to CAUTION mode
**Papers**: (Gap — no paper directly addresses this)
**PS mapping**: PS5
**Transition**: *"Users have interacted with AI that is fully on or fully off, but never with a system that communicates 'AI is active but operating under restriction.' How users understand, trust, and respond to this intermediate state is unknown."*

---

## 6. Citation Chain

### Cluster 1: Safety Governance

```
Dalrymple (2024) "Guaranteed Safe AI"
    ├── cited by → Liang (2025) "Safeguarded AI" (implements as per-output gatekeeper)
    ├── cited by → Intl AI Safety Report (2026) (references as theoretical foundation)
    └── gap: binary verifier; no state-conditioned graduated governance
         └── USER'S CONTRIBUTION: state-conditioned two-level governance pair

Konighofer (2025) "Shields"
    └── gap: per-state safe action sets but no discrete modes or recommendation-type restriction
         └── USER'S CONTRIBUTION: discrete safety modes with recommendation-type restriction

Bajcsy/Fisac (2024) "Human-AI Safety"
    ├── cited by → Ramos (2024) (as Fisac et al. for Bayesian prediction)
    └── gap: binary permit/override; no CAUTION mode
         └── USER'S CONTRIBUTION: graduated governance with CAUTION mode
```

### Cluster 2: Guardrails & Runtime Enforcement

```
Shamsujjoha (2025) "Swiss Cheese Model"
    ├── cited by → Chen (2025) (references guardrail taxonomy)
    └── gap: comprehensive L2 taxonomy but no state-conditioned activation
         └── USER'S CONTRIBUTION: state-conditioned activation of L2 governance

AgentSpec (Wang 2026)
    └── gap: per-action binary enforcement; no global environmental state classifier
         └── USER'S CONTRIBUTION: global state classification layer
```

### Cluster 3: Safety-Critical AI Architecture

```
Perez-Cerrolaza (2024) "AI Safety-Critical Survey"
    ├── shares authors with → SAFEXPLAIN (Abella 2025)
    ├── cited by → Newcomb (2026) (in SLR)
    └── gap: binary governance universal across all industrial/transport domains

Flehmig/Flehmig (2024) "Implementing AI in SCS"
    ├── cited by → Newcomb (2026) (in SLR)
    └── gap: traffic-light governs monitoring, not recommendation scope
         └── USER'S CONTRIBUTION: traffic-light governs recommendation scope via A_AI(S)
```

### Cluster 4: Fisheries/Maritime

```
Haque/Al Jufaili (2026) → Wing/Woodward (2024) → Kühn (2025)
    (isolated cluster — no cross-citations with safety governance literature)
    └── gap: entire fisheries AI domain lacks governance architecture
         └── USER'S CONTRIBUTION: first formal governance architecture for fisheries

Gao (2024) "Penang fisher decisions"
    └── empirical basis: documents go/cautious-go/don't-go → maps to SAFE/CAUTION/UNSAFE
```

### Citation Chain Summary

- **Foundational papers** (cited by others in set): Dalrymple (2), Bajcsy/Fisac (1), Perez-Cerrolaza/SAFEXPLAIN (shared authorship + 1 citation)
- **Recent extensions** (cite others in set): Liang, Intl AI Safety Report, Chen, Newcomb, Ramos
- **Isolated** (no citation links): Most fisheries papers, most low-resource papers, HySAFE, Stage-Gate, SYNAPSE
- **Entry points for user's contribution**: The safety governance cluster (Dalrymple → Liang lineage) breaks where binary governance is implemented — user's work extends this lineage with graduated governance. The fisheries cluster has no connection to safety governance — user's work bridges these clusters.

---

## 7. Literature Review Outline

### Suggested Section Structure

#### Section 1: AI in Safety-Critical Systems (Links 1-2)
**Purpose**: Establish that AI is increasingly deployed in safety-critical domains and that hybrid architectures are the dominant approach.

| Paper | Role |
|-------|------|
| Perez-Cerrolaza | Fills background — cross-domain survey establishing scope |
| Intl AI Safety Report | Fills background — current global assessment |
| Bloomfield/Rushby | Fills background — dependability perspective |
| SYNAPSE | Fills background — neuro-symbolic example |
| Punzi | Fills background — hybrid decision-making taxonomy |
| Yuzui/Kaneko | Fills background — maritime hybrid risk analysis |

**Transition**: *"While hybrid AI architectures are well-studied, the critical question of how to govern AI participation — not just whether AI works, but when and how it should be allowed to contribute — requires formal governance mechanisms."*

#### Section 2: AI Governance — Level 1 Participation Control (Link 3)
**Purpose**: Establish that binary AI governance (on/off) is the universal paradigm.

| Paper | Role |
|-------|------|
| Shields (Konighofer) | Represents baseline — formal binary shield |
| Dalrymple | Represents baseline — guaranteed safe AI framework |
| Bajcsy/Fisac | Represents baseline — formal safety filter |
| SAFEXPLAIN | Represents baseline — supervision function |
| AgentSpec | Represents baseline — per-action enforcement |
| Newcomb | Establishes gap — all 46 formal methods implement binary |
| Ramos | Establishes gap — all 91 collaborative intelligence papers implement binary |

**Citation cluster**: Safety governance cluster (Dalrymple → Liang → Intl AI Safety)

**Transition**: *"Level 1 governance — whether AI operates at all — is well-established across all domains. However, a second governance question remains: even when AI is permitted to operate, should the scope of its recommendations be restricted under elevated risk?"*

#### Section 3: AI Governance — Level 2 Advisory Scope Control (Link 4)
**Purpose**: Show that output-scope restriction exists but is static, not state-conditioned.

| Paper | Role |
|-------|------|
| Shamsujjoha | Represents baseline — most comprehensive Level 2 taxonomy |
| Chen | Fills background — guardrail system architecture |
| AgentSpec | Represents baseline — per-action rule enforcement |
| Selvam | Highlights gap — design-time autonomy levels, not runtime |
| SAFEXPLAIN | Highlights gap — DL usage levels at design-time only |
| Mussi | Highlights gap — hierarchical constraints but not state-conditioned |

**Citation cluster**: Guardrails cluster (Shamsujjoha → Chen)

**Transition**: *"Level 2 governance mechanisms exist — guardrails, runtime enforcement, output filtering — but they are applied per-action or configured at design-time. No architecture dynamically adjusts the set of permissible AI recommendation types based on classified environmental conditions."*

#### Section 4: The Two-Level Governance Gap (Link 5)
**Purpose**: Establish that no architecture unifies Level 1 + Level 2 conditioned on environmental safety state.

| Paper | Role |
|-------|------|
| Flehmig/Flehmig | **Primary comparator** — closest prior art (PS1, PS2) |
| Baxi | **Structural comparator** — graduated governance with containment, but robustness-conditioned |
| Shields | **Formal comparator** — per-state action sets, but continuous, not discrete modes |
| INSYTE | Fills background — AI system classification dimensions including governance |
| Kluever | Highlights gap — design-time SIL assessment, not runtime governance |

**Citation cluster**: Safety-critical architecture cluster (Perez-Cerrolaza → Newcomb → Flehmig)

**Transition**: *"Flehmig et al.'s traffic-light model is the closest prior art — but it governs monitoring intensity triggered by AI performance degradation, not AI recommendation scope triggered by environmental safety state. Baxi's comprehension-gated architecture implements graduated governance with formal containment, but conditions on agent robustness properties, not environmental state. The two-level governance pair (G(S), A_AI(S)) conditioned on environmental safety state remains unimplemented."*

#### Section 5: Formal Safety Properties for Graduated Governance (Link 6)
**Purpose**: Show that formal safety properties exist for binary governance but not for graduated governance.

| Paper | Role |
|-------|------|
| Bajcsy/Fisac | Represents baseline — Theorem 1, binary safety guarantee |
| Shields | Represents baseline — inductive safety, binary |
| Baxi | Structural comparator — bounded exposure theorem, graduated but robustness-conditioned |
| Newcomb | Establishes gap — all formal methods SLR operates binary |
| Tumato | Represents baseline — soundness by construction, binary |

**Transition**: *"The Safety Dominance Property — AI(E) ⊆ A_AI(S) — extends the concept of formal safety guarantees from binary to graduated governance, ensuring that AI outputs are always bounded by the state-dependent recommendation space."*

#### Section 6: Low-Resource Deployment and Domain Context (Link 7)
**Purpose**: Ground the architecture in the fisheries domain and low-resource deployment constraints.

| Paper | Role |
|-------|------|
| Katende | Fills background — low-resource AI constraint taxonomy |
| Bhuvaneswari | Analog comparator — hybrid AI in resource-constrained healthcare |
| Haque/Al Jufaili | Establishes gap — fisheries AI has no governance |
| Gao | Motivates — Penang fisher decisions map to SAFE/CAUTION/UNSAFE |
| Rahim | Motivates — fisher survival decisions validate CAUTION concept |
| Peskas | Fills background — fisheries data platform feasibility |
| Obi | Fills background — Malaysian fisheries sector |
| Wing/Woodward | Fills background — fisheries AI ecosystem needs |

**Citation cluster**: Fisheries/maritime cluster (isolated from safety governance — user's work bridges)

**Transition**: *"Small-scale coastal fisheries represent a domain where AI must navigate varying environmental risk under severe resource constraints — yet the entire fisheries AI literature operates without formal safety governance. This domain provides both the motivation and the test case for the proposed two-level governance architecture."*

#### Section 7: Evaluation and Socio-Technical Gaps (Links 8-9)
**Purpose**: Establish that no evaluation framework exists for graduated vs binary governance, and no user study addresses the CAUTION mode — while grounding the evaluation methodology in established human factors literature.

| Paper | Role |
|-------|------|
| Saup | Fills background — socio-technical governance lens |
| Gabriel | Fills background — socio-technical requirements for AI |
| Madsen/Kim | Motivates — maritime AI transparency (risk display ≠ risk governance) |
| Zhao/Yuan | Motivates — ethical question of varying governance by severity |
| McGrath et al. (S-TIAS) | **Methodological foundation** — validated trust instrument (S-TIAS) for PS4/PS5; trust calibration framework defining evaluation criterion |
| Schrills et al. | **Methodological foundation** — demonstrates trust ≠ dependence; behavioural dependence metric; dual-measurement design for PS4 |
| McGrath et al. (CHAI-T) | **Methodological foundation** — trust calibration as evaluation criterion; temporal trust dynamics across governance mode transitions |
| Bach et al. | **Methodological foundation** — trust measurement catalogue; instrument recommendations; sample size guidance |
| Aquilino et al. | **Methodological foundation** — cognitive vs affective trust framework; mode-specific instrument selection guidance |
| Atf & Lewis | **Methodological foundation** — explainability–trust baseline (r = 0.194); trustworthiness vs trust distinction |

**Citation cluster**: Trust & evaluation methodology cluster (McGrath S-TIAS → McGrath CHAI-T → Bach SLR)

**Transition**: *"While no prior work evaluates graduated AI governance specifically, the human factors literature on trust in automation provides the methodological foundations — validated instruments (S-TIAS, Jian et al. 2000 TiA scale), trust calibration frameworks (CHAI-T), and dual-measurement designs distinguishing attitudinal trust from behavioural dependence. The proposed research extends this foundation to the novel context of graduated governance states — particularly the CAUTION mode, where AI participates under restriction, a state that has no precedent in the automation trust literature."*

### Positioning Summary

The literature establishes that (1) hybrid AI is well-studied in safety-critical domains, (2) Level 1 participation governance (binary AI on/off) is universally implemented via shields, safety filters, and supervision functions, and (3) Level 2 advisory scope governance exists in the form of guardrails and runtime enforcement but is applied statically or per-action, never conditioned on classified environmental safety state. The closest prior art — Flehmig et al.'s traffic-light model — governs monitoring intensity triggered by AI performance, not recommendation scope triggered by environmental state. Baxi's comprehension-gated architecture implements the closest formal structure (graduated tiers with containment) but conditions on agent robustness rather than environmental state. The fisheries/maritime literature confirms that no formal safety governance architecture exists for the target domain. The proposed two-level governance pair (G(S), A_AI(S)), conditioned on classified environmental safety state with the Safety Dominance Property AI(E) ⊆ A_AI(S), fills a gap that is consistently demonstrated across the literature — from formal methods surveys (Newcomb: 46 papers, all binary), to collaborative intelligence reviews (Ramos: 91 papers, all binary), to international safety frameworks (Bengio: 11 frameworks, all binary).

---

## 8. Coverage Summary Tables

### Theme Coverage

| Theme | Code | Yes | Partial | No | Coverage |
|-------|------|-----|---------|-----|----------|
| Hybrid AI | T1 | 14 | 20 | 15 | Well-Covered |
| Safety-critical AI | T2 | 30 | 10 | 9 | Well-Covered |
| AI governance | T3 | 22 | 15 | 12 | Well-Covered |
| Low-resource | T4 | 4 | 13 | 32 | Partially Covered |
| Formalisation | T5 | 7 | 21 | 21 | Partially Covered |
| Human role | T6 | 27 | 20 | 8 | Well-Covered |
| Socio-technical | T7 | 14 | 19 | 22 | Well-Covered |
| Fisheries/maritime | T8 | 8 | 5 | 36 | Partially Covered |

### Problem Statement Coverage

| PS | Coverage | Comparators / foundations found | Key gaps |
|---|---|---|---|
| PS1 | Well-Supported | Flehmig, Shields, AgentSpec, Dalrymple, Bajcsy, Baxi | None — gap well-argued |
| PS2 | Well-Supported | Shields, Bajcsy, Baxi, Shamsujjoha, AgentSpec | None — gap well-argued |
| PS3 | Partially Supported | Bhuvaneswari (analog), Peskas, Haque, Gao | No architectural comparator within fisheries |
| PS4 | **Partially Supported** | McGrath S-TIAS, Schrills, CHAI-T, Bach, Aquilino, Atf & Lewis | No direct evaluation of graduated vs binary governance |
| PS5 | **Partially Supported** | McGrath S-TIAS, Schrills, CHAI-T, Bach, Aquilino, Atf & Lewis | No user study of intermediate governance mode (CAUTION) specifically |

### Governance Level Distribution

| Category | Count |
|----------|-------|
| Level 1 only (binary gate) | ~15 papers |
| Any form of Level 2 | ~10 papers |
| Level 2 state-conditioned | 2 papers (Shields: continuous; Baxi: robustness) |
| Unified two-level, environment-state-conditioned | **0 papers** |
