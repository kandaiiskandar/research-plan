# Literature Review Plan

**Date**: 2026-04-05
**Papers analysed**: 55 (25 full extraction, 24 reduced extraction, 6 methodological foundation, 0 early stop)

---

## 1. Theme Gap Analysis

### Theme Coverage Summary

| Theme | Code | Yes | Partial | No | Coverage |
|-------|------|-----|---------|-----|----------|
| Hybrid AI (rule-based + probabilistic) | T1 | 14 | 21 | 20 | Well-Covered |
| Safety-critical AI decision systems | T2 | 27 | 15 | 13 | Well-Covered |
| AI governance (Level 1 + Level 2) | T3 | 23 | 17 | 15 | Well-Covered |
| Low-resource environments | T4 | 5 | 13 | 37 | Partially Covered |
| Decision architecture formalisation | T5 | 7 | 22 | 26 | Partially Covered |
| Human role in AI-assisted decision-making | T6 | 24 | 25 | 6 | Well-Covered |
| Socio-technical evaluation | T7 | 13 | 21 | 21 | Partially Covered |
| Coastal fisheries / maritime domain | T8 | 11 | 4 | 40 | Partially Covered |

### T1: Hybrid AI — Well-Covered

**Key papers (Yes)**: SYNAPSE (Castagnone), Bhuvaneswari, Punzi, AgentSpec (Wang), Perez-Cerrolaza, Bloomfield/Rushby, Mussi, Flehmig, SAFEXPLAIN (Abella), Shields (Könighofer), Gyllenhammar, Dalrymple, Kalmykov, Yuzui/Kaneko

**Key papers (Partial)**: Klüver, Madsen/Kim, Chen, Leppinen, Haque, Bello, Ramos, Talpur, Saup, Pitale, Porter, Bajcsy, Bengio, Wen, Liang, Li, Baxi, Newcomb, Shamsujjoha, Vermaelen, Katende

**Assessment**: Strong coverage across neuro-symbolic, supervisory control, and governance-based hybrid architectures. Sufficient to establish that hybrid AI is well-studied but none implement two-level governance.

### T2: Safety-critical AI — Well-Covered

**Key papers (Yes)**: Shields, AgentSpec, Dalrymple, Bajcsy/Fisac, SAFEXPLAIN, Bloomfield, Perez-Cerrolaza, Newcomb, Flehmig, Mussi, Baxi, Shamsujjoha, Klüver, Madsen/Kim, Chen, Ramos, Saup, Liang, Bengio, Wen, Gyllenhammar, Bhuvaneswari, Pitale, Abella, Vermaelen, Selvam, Leppinen

**Assessment**: Extensive coverage. The strongest theme in the set. Establishes binary governance as the universal paradigm.

### T3: AI Governance — Well-Covered

**Key papers (Yes)**: AgentSpec, Shields, Dalrymple, Bajcsy, SAFEXPLAIN, Bloomfield, Perez-Cerrolaza, Newcomb, Flehmig, Baxi, Shamsujjoha, Chen, Mussi, Intl AI Safety Report (Bengio), Bello, Selvam, Saup, Klüver, INSYTE (Porter), SYNAPSE (Castagnone), Gyllenhammar, Vermaelen, Liang

**Assessment**: Strong coverage — but critically, ALL implement Level 1 only or static Level 2. No paper implements state-conditioned two-level governance. This theme is well-covered precisely because it establishes the gap.

### T4: Low-resource environments — Partially Covered

**Key papers (Yes)**: Bhuvaneswari, Zhao/Yuan, Peskas (Longobardi), Katende, Tahsin
**Key papers (Partial)**: Haque/Al Jufaili, Stage-Gate (Leppinen), Talpur, Wing/Woodward, Bossier, Gao, Obi, Rahim, Kühn, Bloomfield, Perez-Cerrolaza, Gyllenhammar, Bengio

**Assessment**: 5 Yes papers cover healthcare, fisheries data platforms, and general low-resource AI. But no paper combines low-resource deployment with formal safety governance. Gap exists between the low-resource AI literature and the safety governance literature.

**Search suggestions**:
- "AI deployment resource-constrained safety-critical" in healthcare, disaster response
- "Edge AI safety governance" or "offline-capable decision support systems"
- Maritime/fisheries AI with explicit resource constraint discussion

### T5: Decision architecture formalisation — Partially Covered

**Key papers (Yes)**: AgentSpec, Shields, Dalrymple, Bajcsy/Fisac, Newcomb, Baxi, Vermaelen
**Key papers (Partial)**: 22 papers with partial formalisation including Castagnone, Leppinen, Bhuvaneswari, Klüver, Madsen/Kim, Chen, Punzi, Bloomfield, Ramos, Saup, Mussi, Porter, Flehmig, Bengio, Gao, Abella, Liang, Li, Shamsujjoha, Gyllenhammar, Dalrymple, Kalmykov

**Assessment**: 7 Yes papers provide strong formal models but all use binary safety boundaries. No formal model implements tripartite state classification (SAFE/CAUTION/UNSAFE) with graduated recommendation scope. Baxi is closest (K-tier graduated permissions with containment) but conditioned on robustness, not environmental state.

### T6: Human role — Well-Covered

**Key papers (Yes)**: 24 papers including Punzi (hybrid decision-making taxonomy), Gabriel (socio-technical requirements), Bloomfield, Perez-Cerrolaza, Mussi, Bhuvaneswari, Flehmig, INSYTE, Saup, Zhao/Yuan, Gao, McGrath S-TIAS, McGrath CHAI-T, Bach, Aquilino, Atf & Lewis, Schrills, Ramos, Madsen/Kim, AgentSpec, Bengio, Wen, Newcomb (partial... excluded)

**Assessment**: Well-covered. Establishes that human-AI decision support is the dominant paradigm. No paper evaluates user response to a system with three distinct governance states.

### T7: Socio-technical evaluation — Partially Covered

**Key papers (Yes)**: Bloomfield, Madsen/Kim, Zhao/Yuan, Gabriel, Saup, INSYTE, Intl AI Safety Report (Bengio), Bach, Aquilino, Atf & Lewis, Schrills, McGrath S-TIAS, McGrath CHAI-T

**Assessment**: Several papers address socio-technical considerations but few conduct empirical socio-technical evaluation of AI governance architectures. No paper evaluates user understanding of graduated AI participation modes, particularly the CAUTION state.

**Search suggestions**:
- "Trust in AI decision support" with empirical user studies
- "User perception AI automation levels" in safety-critical domains
- "Socio-technical evaluation AI governance" empirical studies

### T8: Coastal fisheries / maritime — Partially Covered

**Key papers (Yes)**: Haque/Al Jufaili, Wing/Woodward, Yuzui/Kaneko, Welch, Bossier, Peskas (Longobardi), Mandal, Obi, Rahim, Gao, Kühn
**Key papers (Partial)**: Madsen/Kim, Ramos, Talpur

**Assessment**: 11 fisheries/maritime papers but NONE implement any AI governance mechanism. The domain is established as a context lacking formal AI safety governance — which is exactly the motivation needed for PS3.

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
| Shields (Könighofer) | Comparator | Per-state safe action sets but no discrete governance modes or recommendation-type restriction |
| AgentSpec (Wang) | Comparator | Per-action binary enforcement; no global state classification |
| Dalrymple | Comparator | Policy-level binary verification; no graduated modes |
| Bajcsy/Fisac | Comparator | Binary permit/override via safety filter; most rigorous but no CAUTION mode |
| Flehmig | **Primary comparator** | Three-level traffic-light model — closest prior art. But governs monitoring intensity, not AI recommendation scope; triggered by AI performance, not environmental state |
| Baxi | Comparator | K-tier graduated permissions with containment — structurally parallel but conditioned on robustness, not environmental state |
| Perez-Cerrolaza | Establishes gap | Survey of all industrial/transport domains — binary governance universal |
| Newcomb | Establishes gap | SLR of 46 formal methods papers — all binary safety boundaries |
| Ramos | Establishes gap | SLR of 91 collaborative intelligence papers — all binary |
| Intl AI Safety Report (Bengio) | Establishes gap | All 11 Frontier AI Safety Frameworks implement binary participation control |

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
| Peskas (Longobardi) | Establishes gap | Demonstrates feasibility of automated fisheries data in low-resource settings but no decision support or governance |
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
| Shields (Könighofer) | Yes | Partial | Partial | Binary per-state |
| AgentSpec (Wang) | Partial | No | No | Per-action binary |
| Dalrymple | Yes | Partial | No | Binary policy-level |
| Bajcsy/Fisac | Yes | Partial | Partial | Binary (permit/override) |
| SAFEXPLAIN (Abella) | Yes | Partial | No | Binary runtime; graduated design-time |
| Liang | Partial | No | No | Binary per-output |
| Shamsujjoha (Swiss Cheese) | Partial | Yes | No | Binary per-artifact; comprehensive L2 taxonomy |
| Flehmig | Yes | No | Partial | Binary; traffic-light governs monitoring only |
| Baxi (Comprehension-Gated) | Yes | Yes | Yes* | Graduated K-tier (*robustness-conditioned, not environment) |
| Bloomfield/Rushby | Yes | No | No | Binary (permit/override) |
| Perez-Cerrolaza | Yes | No | No | Binary across all domains |
| Newcomb | Yes | No | No | Binary (46 studies) |
| Mussi | Partial | Partial | No | Design-time graduated |
| INSYTE (Porter) | Partial | No | No | Classification only |
| Intl AI Safety Report (Bengio) | Yes | No | No | Binary (all 11 frameworks) |
| Chen (AI Safety LLM) | Yes | Partial | No | Binary (guardrail system) |
| Gyllenhammar | Yes | Partial | No | Binary (simplex switching) |
| Selvam | Partial | Partial | No | Design-time static autonomy levels |
| Tumato (Vermaelen) | Yes | No | No | Binary per-action |
| Klüver | Partial | No | No | Binary (design-time SIL) |
| Saup | Partial | Partial | No | Organisational; post-generation |
| Castagnone (SYNAPSE) | Partial | Partial | No | Binary output gating |
| Gao | Yes* | Partial* | Partial* | Informal only — empirical, not architecture |

### Summary

- **Level 1 only (binary gate)**: ~15 papers implement clear binary participation control
- **Any form of Level 2**: ~12 papers restrict AI output scope in some form
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
**Papers**: Perez-Cerrolaza (cross-domain survey), Intl AI Safety Report/Bengio (global assessment), Bloomfield/Rushby (dependability perspective)
**PS mapping**: Background
**Transition**: *"But AI in safety-critical contexts creates a governance problem: when should AI be allowed to participate, and what should it be allowed to recommend?"*

### Link 2: Hybrid AI combines deterministic rules with probabilistic reasoning
**Papers**: SYNAPSE/Castagnone (neuro-symbolic), Punzi (hybrid taxonomy), Shields (rule-filtered RL), Bhuvaneswari (hybrid triage), Kalmykov (XXAI), Yuzui/Kaneko (hybrid risk analysis)
**PS mapping**: Background
**Transition**: *"But the boundary between deterministic safety control and probabilistic AI reasoning must itself be governed — raising the question of how AI participation is controlled."*

### Link 3: Existing governance is binary — AI on/off (Level 1 participation governance)
**Papers**: Shields (winning region gate), Dalrymple (verifier gate), Bajcsy (safety filter), SAFEXPLAIN (supervision function), Bloomfield (backup guard), AgentSpec (per-action enforcement), Perez-Cerrolaza (binary across all domains), Newcomb (binary in all 46 studies), Ramos (binary in all 91 studies), Intl AI Safety Report/Bengio (binary in all 11 frameworks), Tumato/Vermaelen (binary allowed predicate)
**PS mapping**: PS1
**Transition**: *"Level 1 governance — whether AI operates at all — is well-established. But controlling what AI may recommend (Level 2) is a separate governance question."*

### Link 4: Some systems restrict AI output scope (Level 2), but statically
**Papers**: Shamsujjoha (13 guardrail action types — most comprehensive Level 2 taxonomy), Chen (guardrail system architecture), AgentSpec (per-action rules), Selvam (four autonomy levels — design-time), SAFEXPLAIN (DL usage levels — design-time), Mussi (hierarchical action constraints — design-time)
**PS mapping**: PS1, PS2
**Transition**: *"Level 2 governance exists — but it is applied per-action or configured at design-time, not conditioned on classified environmental safety state. No architecture dynamically adjusts AI advisory scope based on operational conditions."*

### Link 5: No architecture unifies both levels conditioned on environmental safety state
**Papers**: Flehmig (closest — traffic-light but governs monitoring intensity, not recommendation scope; triggered by AI performance, not environmental state), Baxi (graduated tiers with containment but robustness-conditioned, not environment-conditioned), Shields (per-state safe actions but continuous, not discrete governance modes)
**PS mapping**: PS1, PS2
**Transition**: *"Flehmig et al. is the closest prior art: a three-level traffic-light governance model. But it is triggered by AI performance degradation, governs monitoring intensity rather than recommendation scope, and operates at a single governance level. No architecture implements both participation governance G(S) and advisory scope governance A_AI(S) as a unified pair conditioned on environmental safety state."*

### Link 6: No formal Safety Dominance Property for graduated governance
**Papers**: Bajcsy (Theorem 1 — binary), Shields (safety guarantee — binary), Newcomb (CBFs, reachability — binary), Baxi (bounded exposure — robustness-conditioned), Tumato/Vermaelen (soundness — binary)
**PS mapping**: PS2
**Transition**: *"Formal safety properties exist for binary governance (shields, safety filters, CBFs), but none defines a Safety Dominance Property for graduated governance where AI outputs must fall within a state-dependent recommendation space that narrows as risk increases."*

### Link 7: This gap matters in low-resource, safety-critical domains
**Papers**: Katende (low-resource AI constraints), Bhuvaneswari (healthcare in resource-constrained settings), Haque/Al Jufaili (fisheries AI — no governance), Peskas/Longobardi (feasibility of fisheries data platforms), Gao (fisher decision-making in Penang), Rahim (fisher survival decisions under extreme weather)
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
    ├── cited by → Intl AI Safety Report/Bengio (2026) (references as theoretical foundation)
    └── gap: binary verifier; no state-conditioned graduated governance
         └── USER'S CONTRIBUTION: state-conditioned two-level governance pair

Könighofer (2025) "Shields"
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

Flehmig (2024) "Implementing AI in SCS"
    ├── cited by → Newcomb (2026) (in SLR)
    └── gap: traffic-light governs monitoring, not recommendation scope
         └── USER'S CONTRIBUTION: traffic-light governs recommendation scope via A_AI(S)
```

### Cluster 4: Trust & Evaluation Methodology

```
McGrath et al. (2025) — S-TIAS
    ├── builds on → Bach et al. (2024) (trust measurement SLR)
    ├── complemented by → McGrath et al. (2025) — CHAI-T (trust calibration framework)
    └── Schrills et al. (2025) — Questioning Trust (trust vs dependence distinction)
         └── triad: S-TIAS + CHAI-T + Schrills = evaluation methodology for PS4/PS5

Atf & Lewis (2026) — Explainability Meta-analysis
    └── provides baseline: r = 0.194 (explainability–trust correlation)
         └── PS4 benchmark: can graduated governance exceed this baseline?

Aquilino et al. (2025) — Decoding Trust
    └── cognitive vs affective framework → mode-specific instrument selection for PS5
```

### Cluster 5: Fisheries/Maritime

```
Haque/Al Jufaili (2026) → Wing/Woodward (2024) → Kühn (2025)
    (isolated cluster — no cross-citations with safety governance literature)
    └── gap: entire fisheries AI domain lacks governance architecture
         └── USER'S CONTRIBUTION: first formal governance architecture for fisheries

Welch (2024) + Kühn (2025) → shared Watson co-authorship
    └── small fisheries AI research community

Gao (2024) "Penang fisher decisions"
    └── empirical basis: documents go/cautious-go/don't-go → maps to SAFE/CAUTION/UNSAFE
```

### Cluster 6: International Governance & Policy

```
Bengio et al. (2026) — International AI Safety Report
    ├── references → Dalrymple et al. as theoretical foundation
    ├── documents: 11 Frontier AI Safety Frameworks — all binary
    └── gap: no graduated governance in any international framework
```

### Citation Chain Summary

- **Foundational papers** (cited by others in set): Dalrymple (2), Bajcsy/Fisac (1), Perez-Cerrolaza/SAFEXPLAIN (shared authorship + 1 citation)
- **Recent extensions** (cite others in set): Liang, Intl AI Safety Report/Bengio, Chen, Newcomb, Ramos
- **Isolated** (no citation links): Most fisheries papers, most low-resource papers, HySAFE/Pitale, Stage-Gate/Leppinen, SYNAPSE/Castagnone
- **Entry points for user's contribution**: The safety governance cluster (Dalrymple → Liang lineage) breaks where binary governance is implemented — user's work extends this lineage with graduated governance. The fisheries cluster has no connection to safety governance — user's work bridges these two disconnected bodies of literature.

---

## 7. Literature Review Outline

### Suggested Section Structure (Chapter 2 — 9 sections)

*Aligned with `improvement-plan/literature_review_improvement_plan-2.md`. The logical flow builds step-by-step toward the research gap: AI is used for decision support → safety constraints exist but govern actions not advisory scope → human-AI authority is contested → some systems adapt autonomy to risk but without formal advisory containment → governance and guardrails operate at policy level not runtime → hybrid AI focuses on accuracy not governance → low-resource environments add constraints → fisheries is the right domain → evaluation methodology is established → therefore a graduated safety-state-gated architecture is needed.*

---

#### Section 2.1: AI Decision Support in Safety-Critical Systems (Link 1)
**Purpose**: Establish that AI is increasingly used for decision support in safety-critical systems and that incorrect AI recommendations can have serious consequences.

| Paper | Role |
|-------|------|
| Perez-Cerrolaza | Fills background — cross-domain AI safety survey establishing scope |
| Intl AI Safety Report (Bengio) | Fills background — current global assessment of AI in critical systems |
| Bloomfield/Rushby | Fills background — dependability and assurance perspective |
| Gabriel | Fills background — socio-technical requirements for AI systems |
| Newcomb | Fills background — systematic review of 46 formal methods papers (scope of field) |
| Ramos | Fills background — systematic review of 91 collaborative intelligence papers |
| Selvam | Fills background — process safety AI in industrial context |

**Key conclusion**: AI decision support improves decision quality but incorrect or poorly governed AI recommendations in safety-critical environments can lead to serious consequences. This motivates the need for formal governance of when and how AI participates.

**Transition**: *"AI decision support improves decision quality — but as AI moves into safety-critical environments, the question of how to constrain AI behaviour becomes critical. The first response in the literature has been deterministic safety constraints."*

---

#### Section 2.2: Deterministic Safety Constraints and Rule-Based Safety Systems (Links 2–3)
**Purpose**: Show how safety rules and constraints are used to prevent unsafe actions — and identify the key limitation: these systems block unsafe actions but do not restrict AI advisory reasoning scope.

| Paper | Role |
|-------|------|
| Shields (Könighofer) | **Primary comparator** — formal binary shield, inductive winning region |
| AgentSpec (Wang) | **Primary comparator** — per-action enforcement with soundness theorem |
| Dalrymple | **Comparator** — guaranteed safe AI via world model + binary verifier |
| Bajcsy/Fisac | **Comparator** — Hamilton-Jacobi safety filter, binary permit/override |
| SAFEXPLAIN (Abella) | **Comparator** — supervision function, design-time DL usage levels |
| Liang | Fills background — per-output guardrail for LLM safety |
| Bloomfield/Rushby | Fills background — safety case and assurance argument |
| Tumato (Vermaelen) | **Comparator** — soundness by construction, binary allowed predicate |
| Newcomb | Establishes gap — all 46 formal methods papers implement binary gate |

**Citation cluster**: Safety governance cluster (Dalrymple → Liang → Intl AI Safety)

**Key limitation**: These systems block unsafe actions at the participation level (Level 1 — AI on/off). They do not restrict AI advisory reasoning scope (Level 2 — what AI is allowed to recommend). Governance is binary: AI participates fully or not at all.

**Transition**: *"Safety constraints govern whether AI acts — but they do not govern what AI is allowed to recommend, or when AI should participate based on conditions. This raises a deeper question: how should decision authority be allocated between human and AI?"*

---

#### Section 2.3: Human–AI Decision Authority and Decision Support Systems (Link 3 continued)
**Purpose**: Discuss how decision authority is allocated between human and AI — and identify the limitation that these systems do not define when AI should participate based on safety conditions.

| Paper | Role |
|-------|------|
| Saup | Fills background — socio-technical governance lens for decision authority |
| Ramos | Fills background — collaborative intelligence taxonomy (91 papers) |
| INSYTE (Porter) | Fills background — AI system classification including governance dimensions |
| Leppinen | Fills background — stage-gate decision support in project contexts |
| Zhao/Yuan | Motivates — ethical question of varying governance by severity |
| Madsen/Kim | Motivates — maritime AI transparency (risk display ≠ risk governance) |

**Key limitation**: Human-in-the-loop and supervisory control frameworks define who decides, but do not specify when AI should participate based on environmental safety conditions. Decision authority is allocated at design time, not adapted to runtime risk.

**Transition**: *"If static authority allocation is insufficient, the natural next step is systems that adapt the level of autonomy or AI participation based on the risk or context at runtime."*

---

#### Section 2.4: Risk-Adaptive and Graduated Autonomy Systems (Links 4–5)
**Purpose**: Review systems that change autonomy level based on risk or context. This section contains the closest literature to the proposed architecture. Identify the key limitations: autonomy level changes but advisory scope is not formally restricted, no containment relationship between advisory capabilities, and governance functions are not formally defined.

| Paper | Role |
|-------|------|
| Flehmig | **Primary comparator** — traffic-light graduated governance (3-level), triggered by AI performance, governs monitoring intensity not recommendation scope |
| Baxi | **Structural comparator** — graduated K-tier permissions with formal containment (E(T_k) ⊂ E(T_{k+1})), but conditioned on agent robustness not environmental state |
| Shields (Könighofer) | **Formal comparator** — per-state safe action sets, but continuous MDP states not discrete governance modes |
| Gyllenhammar | Fills background — operational design domains and authority switching in automotive |
| Li | Fills background — risk-adaptive autonomy in intelligent transport |
| Klüver | Highlights gap — design-time SIL assessment, not runtime graduated governance |

**Key limitations (why this section does not resolve the gap)**:
- Autonomy level changes exist (Flehmig: 3-level; Baxi: K-tier) — but advisory scope is not formally restricted
- No containment relationship between advisory capabilities across governance modes (A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ ∅ does not appear in any paper)
- Governance functions are not formally defined as a unified pair (G(S), A_AI(S))
- No architecture conditions both levels on classified environmental safety state simultaneously

**First-principles argument — why binary governance is structurally inadequate**:

Binary governance (Level 1 only) forces a false dilemma:
- **Over-restriction**: Disabling AI entirely under elevated but manageable conditions wastes a scarce resource — particularly costly in low-resource settings.
- **Under-restriction**: Permitting full AI participation under elevated risk exposes users to recommendations that assume conditions the system cannot reliably assess.

The CAUTION mode resolves this: AI remains active but advisory scope narrows to recommendation types that remain reliable under elevated conditions. This is a structurally distinct governance solution that binary governance cannot provide.

**Comparator summary** — key architectures across governance dimensions:

| Architecture | Governance trigger | Level | Mode | Runtime | Formal property |
|---|---|---|---|---|---|
| Shields (Könighofer) | MDP state | L1 + partial L2 | Binary per-state | Yes | Inductive winning region |
| Dalrymple | World model | L1 only | Binary | Yes | Verifier pass/fail |
| Bajcsy/Fisac | System state z | L1 only | Binary | Yes | Theorem 1 (HJ reachability) |
| Flehmig | AI performance | L1 only | Graduated (3-level) | Yes | Weighted index threshold |
| Baxi | Agent robustness | L1 + L2 | Graduated (K-tier) | Design-time | Bounded exposure theorem |
| Shamsujjoha | Per-artifact | Partial L1 + L2 | Binary per-layer | Yes | None (defence-in-depth) |
| AgentSpec | Per-action rule | L1 + partial L2 | Binary per-action | Yes | Soundness theorem |
| **Proposed** | **Environmental state** | **L1 + L2 unified** | **Graduated (3-mode)** | **Yes** | **Safety Dominance Property** |

**Baxi differentiator — why conditioning variable matters architecturally**:

| Dimension | Environmental state (proposed) | Agent robustness (Baxi) |
|---|---|---|
| **Observation mechanism** | Real-time sensor inputs (weather, sea state, visibility) | Offline evaluation / benchmark testing |
| **Update frequency** | Continuous — reclassification occurs during operation | Static — tier assigned at deployment |
| **Governance response** | Immediate scope adjustment as conditions change | Tier persists; no real-time response |
| **Failure mode** | Wrong governance mode applied in real-time | Overestimation of robustness persists |
| **Applicability** | Dynamic environments with varying external risk | Controlled environments with stable agent properties |

**Forward reference**:
> *"The gap established above — no architecture implements both participation governance G(S) and advisory scope governance A_AI(S) as a unified pair conditioned on classified environmental safety state — motivates the two-level governance architecture proposed in this research. The formal pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E) addresses this gap by classifying environmental conditions into discrete safety states that simultaneously determine whether AI may operate and what it may recommend."*

**Transition**: *"The graduated autonomy literature reveals the architectural gap clearly: systems change autonomy level but never formally restrict what AI is allowed to recommend, and no governance pair (G(S), A_AI(S)) is conditioned on classified environmental safety state. Before examining the domain and evaluation dimensions of this gap, two further bodies of literature require review: AI governance at the policy level, and hybrid AI as the enabling architecture."*

---

#### Section 2.5: AI Governance, Guardrails, and Safety Architectures (Link 3 continued)
**Purpose**: Introduce AI governance and guardrail concepts — and identify the limitation that most governance operates at policy or system level, not runtime decision architecture level.

| Paper | Role |
|-------|------|
| Shamsujjoha | Fills background — most comprehensive guardrail taxonomy (Swiss cheese model) |
| Chen | Fills background — AI safety LLM landscape and guardrail architecture |
| Bello | Fills background — legal and regulatory AI governance frameworks |
| Intl AI Safety Report (Bengio) | Establishes gap — 11 frontier safety frameworks, all binary |
| Abella (SAFEXPLAIN) | Highlights gap — supervision function defined at design-time only |
| Klüver | Highlights gap — SIL assessment at design time, not runtime |

**Citation cluster**: Guardrails cluster (Shamsujjoha → Chen)

**Key limitation**: AI governance frameworks operate at policy level (what AI should be allowed to do in principle) or at design-time (what DL usage level is permitted). None implement runtime governance conditioned on classified environmental safety state.

**Transition**: *"Governance frameworks define what AI should be permitted to do — but the mechanism by which AI combines deterministic rules with probabilistic inference (the hybrid architecture) determines what is technically possible to govern."*

---

#### Section 2.6: Hybrid AI and Neuro-Symbolic Systems (Links 1–2)
**Purpose**: Review hybrid AI approaches combining deterministic rules and machine learning — and establish that most hybrid AI research focuses on improving prediction accuracy and explainability, not on governing whether AI is allowed to participate and what AI is allowed to recommend.

| Paper | Role |
|-------|------|
| SYNAPSE (Castagnone) | Fills background — neuro-symbolic hybrid for building management |
| Punzi | Fills background — hybrid decision-making taxonomy |
| Mussi | Highlights gap — hierarchical rule + ML constraints, but not state-conditioned governance |
| Kalmykov | Fills background — information fusion with rule-based and probabilistic components |
| Pitale (HySAFE-AI) | Fills background — hybrid safety AI architecture |
| Vermaelen (Tumato) | **Comparator** — hybrid temporal logic + ML, soundness by construction |
| Bhuvaneswari | Analog — hybrid AI in resource-constrained healthcare |
| Yuzui/Kaneko | Fills background — hybrid risk analysis in maritime |

**Key positioning**: Most hybrid AI research focuses on combining rules and ML to improve accuracy and explainability. The governance question — whether AI is allowed to participate and what AI is allowed to recommend — is not addressed.

**Transition**: *"Hybrid AI is the enabling architecture. The deployment context determines the constraints. In low-resource environments, those constraints are particularly severe."*

---

#### Section 2.7: AI Systems in Low-Resource Environments (Link 7)
**Purpose**: Justify the low-resource environment context in the research title — and establish the additional constraints that AI systems must satisfy in these contexts.

| Paper | Role |
|-------|------|
| Katende | Fills background — comprehensive low-resource AI constraint taxonomy |
| Haque/Al Jufaili | Establishes gap — fisheries AI has no formal governance; low-resource context |
| Bhuvaneswari | Analog comparator — hybrid AI in resource-constrained healthcare (cross-domain) |
| Talpur | Fills background — ICT adoption in developing region fisheries |
| Mandal | Fills background — environmental AI in low-data contexts |
| Nastoska | Fills background — edge AI deployment constraints |
| Tahsin | Fills background — AI in resource-limited industrial settings |
| Wen | Fills background — AI deployment in data-deficient environments |

**Key idea**: AI systems in low-resource environments must operate with limited connectivity, limited compute, and users with varying digital literacy. Binary governance is particularly costly in this context — disabling AI entirely under moderate risk wastes a scarce resource when partial AI assistance would be safe and valuable.

**Transition**: *"Within the class of low-resource, safety-critical environments, coastal fisheries is the domain that most directly motivates and empirically validates the proposed architecture."*

---

#### Section 2.8: Technology and Decision Support in Small-Scale Fisheries (Link 7 continued)
**Purpose**: Justify the case study domain — and establish that no formal safety governance architecture exists in fisheries AI.

**Centrepiece**: Gao (2024) — *"Fisher Decision-Making in Penang"*

Gao's empirical finding is the cornerstone of the domain justification: Penang fishers already make tripartite decisions — *go*, *cautious-go*, and *don't-go* — based on weather and sea conditions. This maps directly to SAFE/CAUTION/UNSAFE. The proposed architecture formalises a decision structure that practitioners already use informally.

**Three pillars of domain argument**:
1. **Environmental variability as first-class concern** — fisheries face continuously varying conditions (weather, sea state, visibility, tidal patterns) that directly determine operational safety, making environment-state-conditioned governance natural.
2. **Existing informal tripartite decision-making** — Gao (2024) documents go / cautious-go / don't-go; Rahim (2024) documents survival decisions under extreme weather. SAFE/CAUTION/UNSAFE formalises existing practice, not an imposed abstraction.
3. **Resource constraints make binary governance costly** — in low-resource settings, a binary gate that disables AI under moderate risk wastes the resource precisely when partial assistance would be most valuable.

| Paper | Role |
|-------|------|
| **Gao** | **Centrepiece** — empirical tripartite fisher decision-making validates SAFE/CAUTION/UNSAFE |
| Rahim | Supports centrepiece — survival decisions under extreme weather validate CAUTION concept |
| Haque/Al Jufaili | Establishes gap — no formal governance in fisheries AI |
| Wing/Woodward | Fills background — fisheries AI ecosystem needs and data gaps |
| Welch | Fills background — fisheries AI monitoring technology |
| Kühn | Fills background — fisheries AI state of the art review |
| Bossier | Fills background — marine AI decision support |
| Obi | Fills background — Malaysian small-scale fisheries sector |
| Peskas (Longobardi) | Fills background — fisheries data platform in low-resource settings |
| Madsen/Kim | Fills background — maritime AI transparency and safety (adjacent domain) |

**Citation cluster**: Fisheries/maritime cluster (isolated from safety governance cluster — proposed work bridges these two disconnected bodies of literature)

**Transition**: *"The fisheries domain validates and motivates the proposed architecture — but the architecture must also be evaluated. The following section establishes the methodological foundations for that evaluation."*

---

#### Section 2.9: Trust Measurement and Evaluation Methodology (Links 8–9)
**Purpose**: Ground the evaluation methodology (PS4/PS5) in the human factors and trust literature — establishing that while no prior work evaluates graduated AI governance specifically, validated instruments and frameworks exist that can be extended to this context.

| Paper | Role |
|-------|------|
| McGrath et al. (S-TIAS) | **Methodological foundation** — validated 3-item trust instrument (S-TIAS) for PS5; trust calibration framework |
| McGrath et al. (CHAI-T) | **Methodological foundation** — trust calibration as evaluation criterion; temporal trust dynamics across governance mode transitions |
| Bach et al. | **Methodological foundation** — trust measurement SLR; instrument catalogue; sample size guidance for PS5 design |
| Schrills et al. | **Methodological foundation** — trust ≠ dependence; behavioural dependence metric; dual-measurement design for PS4 |
| Aquilino et al. | **Methodological foundation** — cognitive vs affective trust; mode-specific instrument selection |
| Atf & Lewis | **Methodological foundation** — explainability–trust baseline (r = 0.194); trustworthiness vs trust distinction |
| Saup | Fills background — socio-technical governance framework for evaluation design |
| Gabriel | Fills background — socio-technical requirements methodology |
| Zhao/Yuan | Motivates — ethical question of governance varying by severity (PS5 context) |
| Madsen/Kim | Motivates — maritime AI transparency gap (no governance display) |

**Citation cluster**: Trust & evaluation methodology cluster (Bach → McGrath S-TIAS ↔ McGrath CHAI-T ↔ Schrills)

**Evaluation gaps established**:
- **PS4 gap**: No study compares graduated two-level governance (ungated vs binary-gated vs two-level graduated) — methodological foundations established but not yet applied to governance architectures
- **PS5 gap**: No user study addresses the CAUTION mode specifically — AI active but operating under recommendation scope restriction is a novel governance state with no precedent in the automation trust literature

**Transition**: *"The human factors literature provides validated instruments and frameworks for measuring trust, calibration, and behavioural dependence. What remains is their application to graduated governance states — particularly the CAUTION mode — which no prior study has examined."*

---

#### Section 2.10: Literature Summary and Research Gap
**Purpose**: Synthesise limitations across all sections and state the research gap.

**Literature Summary Table**:

| Area | What Exists | Limitation |
|------|-------------|------------|
| Safety constraints (§2.2) | Block unsafe actions — binary gate | Do not control AI advisory scope |
| Human-AI authority (§2.3) | Supervisory control, automation levels | Do not define participation based on safety conditions |
| Adaptive autonomy (§2.4) | Change authority level based on risk | Advisory scope not formally restricted; no containment relationship; governance not formally defined |
| AI governance (§2.5) | Policy-level and design-time governance | Not runtime decision architecture conditioned on environmental state |
| Hybrid AI (§2.6) | Combine rules and ML | Focus on accuracy and explainability, not governance |
| Low-resource AI (§2.7) | Focus on deployment constraints | Not safety-gated decision architecture |
| Fisheries AI (§2.8) | Decision support and monitoring tools | No formal safety governance |
| Evaluation methodology (§2.9) | Validated trust instruments and frameworks | Not applied to graduated governance states |

**Research Gap Statement**:

Existing studies implement safety constraints, decision support systems, adaptive autonomy, AI governance frameworks, and hybrid AI approaches independently. However, the literature does not present an architectural model in which environmental safety state simultaneously governs both AI participation and AI advisory recommendation scope as a unified governance mechanism. Specifically, no architecture defines both G(S) (participation gate) and A_AI(S) (admissible recommendation space) as a formally unified pair conditioned on classified environmental safety state S ∈ {SAFE, CAUTION, UNSAFE}, with the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ and the Safety Dominance Property AI(E) ⊆ A_AI(S). Furthermore, no evaluation study compares graduated two-level governance against binary governance (PS4), and no socio-technical study examines user response to the CAUTION mode — a novel governance state in which AI participates under recommendation scope restriction (PS5).

Therefore, there is a lack of a formally defined graduated safety-state-gated architecture for AI decision support in safety-critical and low-resource environments, and a corresponding gap in the evaluation methodology for assessing its comparative performance and user acceptance.

---

### Positioning Summary

The literature establishes that: (1) hybrid AI is well-studied in safety-critical domains; (2) Level 1 participation governance (binary AI on/off) is universally implemented via shields, safety filters, and supervision functions, confirmed across 46 formal methods papers (Newcomb), 91 collaborative intelligence papers (Ramos), and 11 international safety frameworks (Bengio); (3) Level 2 advisory scope governance exists in the form of guardrails and runtime enforcement but is applied statically or per-action, never conditioned on classified environmental safety state; (4) risk-adaptive systems change autonomy level but do not formally restrict advisory scope or define containment relationships between governance modes.

Binary governance is structurally inadequate because it forces a false dilemma: over-restriction (disabling AI entirely when partial assistance would be safe and valuable) or under-restriction (permitting full AI participation under elevated risk). The CAUTION mode resolves this dilemma — AI remains active but advisory scope narrows to recommendation types that remain reliable under elevated conditions.

The closest prior art — Flehmig et al.'s traffic-light model — governs monitoring intensity triggered by AI performance, not recommendation scope triggered by environmental state. Baxi's comprehension-gated architecture implements the closest formal structure (graduated tiers with containment) but conditions on agent robustness — a static, offline-assessed property — rather than environmental state, which is dynamic and continuously observable. These conditioning strategies demand fundamentally different observation mechanisms, update dynamics, and failure handling — constituting architecturally distinct approaches.

The fisheries domain is not merely a convenient application context: it is the domain where environmental-state-conditioned governance is most natural (continuous environmental variability), most empirically motivated (Gao 2024 documents existing tripartite informal decision-making — go / cautious-go / don't-go), and most valuable (binary governance wastes scarce AI resources under moderate risk in low-resource settings). The proposed architecture bridges the safety governance literature and the fisheries AI literature, which have no prior citation connection.

The evaluation methodology is grounded in the human factors literature on trust in automation — validated instruments (S-TIAS), trust calibration frameworks (CHAI-T), and dual-measurement designs distinguishing attitudinal trust from behavioural dependence (Schrills et al. 2025) — extended to the novel context of graduated governance states and the CAUTION mode specifically.

The proposed two-level governance pair (G(S), A_AI(S)), conditioned on classified environmental safety state with the Safety Dominance Property AI(E) ⊆ A_AI(S), fills a gap confirmed across multiple independent bodies of literature. The evaluation gaps (PS4, PS5) extend this contribution: no prior work provides comparative evidence for graduated vs binary governance, and no prior user study examines AI participation under recommendation scope restriction as a distinct governance state.

---

## 8. Coverage Summary Tables

### Theme Coverage

| Theme | Code | Yes | Partial | No | Coverage |
|-------|------|-----|---------|-----|----------|
| Hybrid AI | T1 | 14 | 21 | 20 | Well-Covered |
| Safety-critical AI | T2 | 27 | 15 | 13 | Well-Covered |
| AI governance | T3 | 23 | 17 | 15 | Well-Covered |
| Low-resource | T4 | 5 | 13 | 37 | Partially Covered |
| Formalisation | T5 | 7 | 22 | 26 | Partially Covered |
| Human role | T6 | 24 | 25 | 6 | Well-Covered |
| Socio-technical | T7 | 13 | 21 | 21 | Partially Covered |
| Fisheries/maritime | T8 | 11 | 4 | 40 | Partially Covered |

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
| Any form of Level 2 | ~12 papers |
| Level 2 state-conditioned | 2 papers (Shields: continuous; Baxi: robustness) |
| Unified two-level, environment-state-conditioned | **0 papers** |
