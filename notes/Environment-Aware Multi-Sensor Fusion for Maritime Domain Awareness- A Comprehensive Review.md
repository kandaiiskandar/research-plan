# Environment-Aware Multi-Sensor Fusion for Maritime Domain Awareness: A Comprehensive Review
**Ryu, S. & Han, S. (2025)**

---

## 1. Bibliographic Information

- **Title:** Environment-Aware Multi-Sensor Fusion for Maritime Domain Awareness: A Comprehensive Review
- **Authors:** Sumin Ryu, Sanghyuck Han
- **Affiliation:** Satellite Application Research Team, Korea Aerospace Research Institute (KARI), Daejeon, Republic of Korea
- **Year:** 2025
- **Venue:** Korean Journal of Remote Sensing, 41(6), 1225–1250
- **DOI:** 10.7780/kjrs.2025.41.6.21
- **Publisher:** Korean Society of Remote Sensing (Open Access, CC BY-NC)
- **Citation Quality:** ✅ Peer-reviewed journal article. Niche venue (Korean Journal of Remote Sensing) but indexed, DOI-assigned, and the content is a comprehensive 26-page review with 100+ references. Acceptable as domain evidence citation; not a flagship venue.

---

## 2. Early Relevance Gate

| Theme | Match? | Notes |
|-------|--------|-------|
| T1: AI governance architecture | ❌ No | No governance architecture proposed |
| T2: Safety-state classification | ✅ Yes | Argues environmental state should be the organising principle for sensor fusion and detection; proposes detection-chain framework: environment → surface/atmospheric state → sensor signal → detectability → decision-making |
| T3: Graduated/adaptive autonomy | ⚠️ Partial | Argues for adaptive detection thresholds and condition-dependent reliability weighting — functionally analogous to graduated system behaviour |
| T4: Low-resource / maritime / fisheries | ✅ Yes | Maritime domain; discusses small-vessel detection, coastal environments, fishing vessel monitoring |
| T5: Environmental context in AI safety | ✅ Yes | **Core thesis:** environmental conditions are not peripheral noise but fundamental determinants of sensor reliability and detection performance |
| T6: Formal safety properties | ❌ No | No formal safety properties |
| T7: Trust / human-AI interaction | ❌ No | No trust measurement |
| T8: Decision-support systems | ⚠️ Partial | Positions environment-aware MDA as supporting operational decision-making |

**Gate Decision:** 3+ theme matches → **FULL EXTRACTION**

---

## 3. Research Problem & Motivation

Current maritime surveillance systems and research remain fundamentally sensor-centric. Environmental factors are addressed only superficially, treated as incidental degradation sources rather than as variables that fundamentally shape what can be detected and how reliably. This creates systematic vulnerabilities: high sea states, strong winds, swell, cloud cover, and atmospheric ducting reduce detectability, distort signatures, and degrade AIS/RF reception. The paper argues that no existing review systematically organises maritime sensing from an environment-aware perspective that connects physical scattering, sea state, detection algorithms, and multi-sensor fusion under the unifying question of how environmental conditions control satellite sensing performance and how MDA systems should adapt.

---

## 4. Research Questions / Objectives

No explicit research questions. Four contributions claimed:
1. Synthesising SAR, optical, AIS, and RF sensing from an explicitly environment-aware perspective
2. Introducing a structured detection-chain framework: environment → surface/atmospheric state → sensor signal and clutter → detectability and reliability → operational decision-making
3. Identifying critical gaps (environment-labelled datasets, adaptive detection pipelines, MetOcean-driven dynamic fusion)
4. Discussing operational implications for the Korean EEZ

---

## 5. Methodology

- **Approach:** Comprehensive narrative review / thematic synthesis
- **Scope:** SAR, optical, AIS, and RF sensing modalities examined through the lens of environmental sensitivity
- **No primary data collection** — entirely secondary analysis of existing literature
- **Structure:** Physics of environment–sensor coupling → per-modality environmental sensitivity analysis → multi-sensor fusion frameworks → gaps and future directions

---

## 6. Key Concepts & Definitions

- **Environment-aware MDA:** Maritime surveillance architecture that treats environmental information as a central organising principle rather than a peripheral auxiliary input
- **Detection-chain framework:** Environment → surface/atmospheric state → sensor signal and clutter → detectability and reliability → operational decision-making
- **Vessel detectability as environmentally conditioned:** "vessel detectability is not an intrinsic property of the target but is strongly conditioned by the prevailing sea state"
- **Non-stationary sea clutter:** Sea clutter statistics vary substantially with wind speed, wave height, and surface turbulence; shift from near-Gaussian to heavy-tailed (K-distributions, compound models) under strong winds — this invalidates fixed-threshold detectors
- **Environmentally-driven AIS gaps:** Meteorological/oceanographic conditions degrade AIS VHF signal propagation (heavy precipitation, high waves, vessel roll/pitch, atmospheric ducting), creating data gaps independent of intentional "dark vessel" behaviour
- **Domain shift:** Gap between sea states present in training data vs. operational deployment conditions, structurally restricting DL model generalisation under extreme conditions

---

## 7. Core Framework / Architecture

**Detection-chain framework (implicit architecture):**

```
Environment (wind, wave height, swell, atmospheric state)
    → Surface/Atmospheric State (sea clutter statistics, radiometric conditions, VHF propagation)
        → Sensor Signal & Clutter (σ₀ backscatter, optical contrast, AIS reception quality, RF propagation)
            → Detectability & Reliability (PD, false alarm rate, confidence)
                → Operational Decision-Making (adaptive thresholding, sensor tasking, fusion weighting)
```

**Per-sensor environmental failure modes (from Tables 2–5 and Sections 2–3):**

| Sensor | Environmental Factor | Failure Mode |
|--------|---------------------|--------------|
| SAR (X-band) | High wind (>10–12 m/s) | Severe clutter escalation, heavy-tailed statistics, small-vessel miss |
| SAR (all bands) | High wave height with breaking | Increased σ₀ variance, non-Bragg scattering, clutter dominates |
| SAR | Long-period swell | Wake-like artefacts → false alarms |
| Optical | Cloud/fog | Binary failure — up to 70–80% of scenes partially/fully obscured |
| Optical | Aerosols/haze | Reduced contrast, small vessels indistinguishable from background |
| Optical | Sun glint | Geometry-driven failure; sensor saturation masks target–background contrast |
| AIS | High waves / vessel roll-pitch | Antenna tilt → intermittent signals, reduced reception success |
| AIS | Rainfall / sea spray | VHF signal attenuation → lower received signal strength |
| AIS | High traffic density | TDMA message collisions → packet loss, reduced update rate |
| AIS | Atmospheric ducting | Anomalous long-range reception or dropouts; requires environment-aware interpretation |
| RF | Evaporation ducts / temperature inversions | Non-geometric propagation paths → false bearings, mislocalized emitters |

---

## 8. Findings / Results

**Key findings across the review:**

1. **Environmental conditions are first-order determinants of detection performance**, not peripheral noise. Every sensing modality (SAR, optical, AIS, RF) exhibits distinct environment-dependent failure modes.

2. **Sensor confidence is environmentally conditioned.** SAR detectability (PD) is a function of wind speed, wave height, incidence angle, and vessel length (Tings et al., 2019a model). Under high-wind/high-wave conditions, PD drops sharply for small vessels; false alarm rates surge. Under calm conditions, PD remains consistently high.

3. **Fixed thresholds fail under non-stationary conditions.** Classical CFAR detectors assume homogeneous Gaussian clutter, which is invalid under strong wind/high sea states where clutter shifts to heavy-tailed K-distributions. This undermines any detection system relying on fixed confidence thresholds.

4. **AIS gaps are frequently environmental, not intentional.** Rough seas, precipitation, atmospheric conditions, and traffic congestion cause AIS reporting delays and gaps independent of deliberate "dark vessel" behaviour. Inferring illegal activity from AIS gaps alone is cautioned against as risky.

5. **DL models suffer domain shift.** Most SAR ship detection training datasets lack environmental metadata. Models trained on calm-condition imagery degrade under extreme sea states — a structural generalisation failure.

6. **Multi-sensor fusion frameworks remain structurally limited** when environmental context is not explicitly incorporated. Most SAR–AIS fusion studies treat metocean conditions only implicitly.

7. **Environment-aware fusion is identified as a structural requirement**, not an optional enhancement: "MDA systems that do not explicitly incorporate environmental awareness are inherently limited."

---

## 9. Limitations (Author-Stated)

- No primary data collected — entirely secondary analysis
- Regional focus on Korean EEZ may limit generalisability of operational recommendations
- Many gaps identified but no proposed solution architecture
- Environment-aware multi-sensor fusion with MetOcean priors remains at an early research stage

---

## 10. Limitations (Analyst-Identified)

- **No governance architecture proposed.** The paper identifies the problem (environmental conditions degrade sensor reliability) and the principle (environment should be the organising variable) but does not propose any formal mechanism for how systems should *adapt their behaviour* based on environmental state. This is precisely the gap your architecture fills.
- **No discrete state classification.** The detection-chain framework is continuous, not discrete. There is no equivalent of $S = f(E) \in \{SAFE, CAUTION, UNSAFE\}$ — no mechanism for classifying environmental conditions into governance-actionable states.
- **No AI participation governance.** The paper discusses adaptive thresholding and sensor weighting but never considers whether the AI system should *reduce its participation* or *restrict its output types* under degraded conditions. The concept of graduated autonomy restriction is entirely absent.
- **Surveillance domain, not decision-support.** The paper concerns vessel detection (surveillance), not advisory output to human decision-makers. The fisheries connection exists (IUU fishing monitoring) but the paper does not address fisher-facing decision support.

---

## 11. Relevance to Dissertation

### Rating: ⭐⭐⭐⭐ (High)

**Role:** Domain evidence for the "reliability collapse" argument (Thread 1) and empirical grounding for the environmental state vector $E$

### 11.1 Mapping to Governance Architecture

| Governance Element | Ryu & Han Implementation | Gap Relative to Dissertation |
|---|---|---|
| **E (Environmental input)** | ✅ **Extensively characterised.** Wind speed, significant wave height, swell period, atmospheric state, sea surface temperature, precipitation, traffic density, atmospheric ducting — all documented with specific failure modes per sensor | Your E = {w, r, m, o, v, t} is a subset of what this paper documents. Provides empirical validation that these variables are the right ones to include. |
| **S = f(E)** | ⚠️ **Implicit only.** Wind-speed regimes classified in Table 2 (<2 m/s, 2–8 m/s, >10–12 m/s) with distinct detection behaviours — functionally a three-state classification. But not formalised as a governance trigger. | Your S = f(E) formalises what this paper leaves as a descriptive observation. The wind-speed regime table is effectively your SAFE/CAUTION/UNSAFE mapping without the governance consequence. |
| **G(S) — Level 1 Participation** | ❌ Not addressed | No concept of AI participation governance. System is always active; only thresholds adapt. |
| **A_AI(S) — Level 2 Advisory Scope** | ❌ Not addressed | No concept of restricting advisory/output types based on environmental state. The paper concerns detection performance, not advisory scope. |
| **Safety Dominance Property** | ❌ Not addressed | No formal safety property. |
| **CAUTION mode** | ❌ Absent | No intermediate governance mode. The paper's implicit three-regime classification (calm/moderate/rough) maps naturally onto SAFE/CAUTION/UNSAFE but without governance consequences. |

### 11.2 The Three Argumentative Threads

**Thread 1 — Reliability Collapse (PRIMARY VALUE):**

This paper is the single strongest piece of domain evidence for the reliability collapse argument. Key evidence chains:

- **SAR confidence degrades with sea state.** Under high wind/waves, sea clutter shifts from Gaussian to heavy-tailed K-distributions. Fixed-threshold detectors (analogous to fixed AI confidence thresholds) produce either surging false alarms or missed detections. The paper explicitly states: "vessel detectability is not an intrinsic property of the target but is strongly conditioned by the prevailing sea state."
- **Sensor self-assessment becomes unreliable.** The domain shift finding means that DL models trained on calm-condition data produce *confidently wrong* outputs under extreme conditions — the model doesn't know what it doesn't know. This is the exact mechanism by which internal confidence scores become misleading.
- **AIS signals — the "ground truth" — are themselves environmentally degraded.** High waves cause vessel roll/pitch that intermittently blocks antenna line-of-sight. Rainfall attenuates VHF signals. Traffic congestion causes packet collisions. The data source that would be used to validate AI outputs is itself corrupted by the same environmental conditions.
- **Environmental conditions corrupt ALL sensing modalities simultaneously.** SAR, optical, AIS, and RF all degrade under adverse conditions. There is no single sensor that remains reliable as a self-referential check. This is the structural justification for externalising the governance trigger to independently sourced environmental state data (meteorological services, port authority reports, vessel monitoring systems).

**Thread 2 — Flehmig Contrast:**

The paper's finding that fixed detection thresholds fail under non-stationary sea clutter directly parallels the vulnerability of Flehmig et al.'s traffic-light degradation index. Flehmig's internal metrics (confidence scores, drift detection) are analogous to fixed CFAR thresholds — both assume stationary statistical conditions that do not hold in volatile maritime environments. This paper provides the physical mechanism explaining *why* they fail.

**Thread 3 — Action Suppression vs. Advisory Space Contraction:**

Less directly relevant to Thread 3, but the paper's detection-chain framework (environment → detectability → decision-making) provides domain validation that environmental state should condition downstream system behaviour. The paper stops at adaptive thresholding (analogous to per-action adjustment); your architecture goes further to proactive space contraction ($A_{AI}(S)$).

### 11.3 The Wind-Speed Regime Table as Empirical Precursor to S = f(E)

Table 2 in the paper classifies three wind-speed regimes with distinct detection behaviours:

| Wind Speed | Sea-Surface Characteristics | Detection Implications | **Your Mapping** |
|---|---|---|---|
| < 2 m/s | Very smooth surface | High vessel contrast, reliable detection | **→ SAFE** |
| 2–8 m/s | Developed gravity–capillary waves | Stable clutter, robust detection | **→ CAUTION** (transition zone) |
| > 10–12 m/s | Breaking waves, strong roughness | Increased variance, reduced detectability for small vessels | **→ UNSAFE** |

This is a ready-made empirical justification for discrete environmental state classification. The paper provides the physics; your architecture provides the governance consequence.

---

## 12. Key Citations to Follow

| Ref | Citation | Potential Relevance |
|-----|----------|-------------------|
| Tings et al. (2019a) | Modelling ship detectability depending on TerraSAR-X-derived metocean parameters, CEAS Space Journal | **High priority.** Quantitative PD = f(wind, wave height, incidence angle, vessel length) model. Direct empirical evidence for environment-conditioned system performance. |
| Bezerra et al. (2023) | Marine environmental impact on CFAR ship detection as measured by wave age, Remote Sensing | High. Wave-age-dependent clutter statistics shifting false alarm rates. |
| Pleskachevsky et al. (2022) | Multiparametric sea state fields from SAR for maritime situational awareness, RSE | Moderate. SAR-derived MetOcean fields as priors — analogous to your E vector sources. |
| Talpur et al. (2025) | AI in maritime security: applications, challenges, future directions, Information | Already in tracker. Cross-validates. |
| Li et al. (2022) | Deep learning for SAR ship detection: Past, present and future, Remote Sensing | Moderate. Documents the training data gap (no environmental metadata) causing domain shift. |
| Kazemi et al. (2013) | Open data for anomaly detection in maritime surveillance, ESWA | Moderate. Framework for incorporating environmental conditions and contextual factors into maritime anomaly detection. |

**Assessment:** Tings et al. (2019a) is the highest-priority follow-up — it provides the quantitative detectability model that directly supports environment-conditioned governance.

---

## 13. Quotable Passages

- "vessel detectability is not an intrinsic property of the target but is strongly conditioned by the prevailing sea state" — directly supports externalising the governance trigger
- "MDA systems that do not explicitly incorporate environmental awareness are inherently limited" — supports the structural necessity claim
- "environmental conditions are not peripheral background factors but fundamental constraints" — aligns with your core argument
- "inferring illegal or non-cooperative activities based solely on the presence of missing data segments is cautioned against as being risky" — shows how environmental degradation creates ambiguity that governance must handle

---

## 14. Methodological Concerns

- Narrative review without systematic search protocol (no PRISMA, no explicit inclusion/exclusion criteria)
- Strong Korean EEZ focus in operational recommendations may introduce regional bias
- No quantitative meta-analysis; findings are qualitative synthesis
- Some cited sources are online blog posts and product pages (WINDWARD, Kontas, Owen) rather than peer-reviewed literature

---

## 15. Inter-Paper Relationships

| Paper | Relationship |
|-------|-------------|
| **CLGuard / Seong et al. (2025)** | CLGuard's semantic validation depends on camera-based scene assessment. This paper documents how optical/visual sensing degrades under environmental conditions (cloud, fog, aerosols, glint). CLGuard's CLIP-based evaluation would suffer the same degradation mechanisms described here — direct evidence for the reliability collapse of CLGuard's approach in maritime environments. |
| **Flehmig et al. (2024)** | Flehmig's traffic-light degradation index relies on internal metrics (confidence, drift). This paper demonstrates that fixed thresholds and internally-derived confidence metrics fail under non-stationary maritime conditions. Physical mechanism for why Flehmig's approach is structurally vulnerable in your domain. |
| **Talpur et al. (2025)** | Already in tracker. Both papers identify maritime AI degradation under adverse conditions. Talpur focuses on AI applications and challenges broadly; Ryu & Han provides the physics-level explanation of *why* degradation occurs per sensor modality. |
| **Rahim et al.** | Rahim documents fisher self-restriction behaviour under extreme weather. Ryu & Han provides the sensor-physics evidence that the same weather conditions that cause fishers to self-restrict also cause AI sensing systems to degrade — convergent empirical support for CAUTION-state governance from both the human and the technical side. |
| **Könighofer et al. (2025)** | Könighofer shows intermediate shielding outperforms binary extremes. Ryu & Han's three wind-speed regimes with distinct detection behaviours provide the domain-specific empirical basis for why intermediate (CAUTION) governance is needed — calm conditions don't need it, extreme conditions may require full restriction, but the moderate/transitional regime is where graduated governance adds most value. |

---

## 16. Citation Placement in Dissertation

| Section | Role |
|---------|------|
| **Section 1: The Deployment Problem** | Domain evidence that maritime environmental conditions systematically degrade AI/sensor performance. Grounds the E vector variables (wind, wave height, swell, atmospheric state) in physical sensing mechanisms. Strengthens domain justification for why fisheries is the right application domain. |
| **Section 2/3: AI Safety Governance Mechanisms** | Evidence that fixed-threshold / fixed-confidence approaches fail under non-stationary maritime conditions. Supports the argument that internal metrics are unreliable as governance triggers. |
| **Section 4: The Level 1 / Level 2 Gap** | Does not enter the gap table directly (no governance architecture proposed). However, cited as domain evidence supporting *why* the gap matters — systems without environment-conditioned governance are "inherently limited." |
| **Formalisation Chapter** | Wind-speed regime table (Table 2) as empirical precedent for $S = f(E)$ discrete state classification. The three regimes map directly onto SAFE/CAUTION/UNSAFE with documented detection behaviour differences per regime. |

---

## 17. Tracker Entry

```
| Ryu & Han (2025) | Environment-Aware Multi-Sensor Fusion for MDA | Korean J. Remote Sensing 41(6) | ⭐⭐⭐⭐ | Domain evidence — reliability collapse | Comprehensive review: environmental conditions are first-order determinants of maritime sensor reliability. All modalities (SAR, optical, AIS, RF) exhibit distinct environment-dependent failure modes. Fixed thresholds fail under non-stationary clutter. Three wind-speed regimes with distinct detection behaviours = empirical precursor to S=f(E). No governance architecture proposed. Strongest domain evidence for externalising governance trigger. | 1, 2/3, Formalisation |
```
