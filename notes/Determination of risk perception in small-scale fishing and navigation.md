# Paper Extraction: Atacan & Düzbastılar (2023)

## 1. Bibliographic Information

- **Title:** Determination of risk perception in small-scale fishing and navigation
- **Authors:** Can Atacan, Faik Ozan Düzbastılar
- **Year:** 2023
- **Venue:** *Ege Journal of Fisheries and Aquatic Sciences*, 40(1), 1–14
- **DOI:** https://doi.org/10.12714/egejfas.40.1.01
- **Type:** Peer-reviewed journal article (open access)

---

## 2. Early Relevance Gate

| Core Theme | Match? | Notes |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | ✗ | No AI system |
| Safety-critical AI decision-making | ✗ | No AI; but proactive risk assessment for safety-critical fishing decisions |
| AI governance and control mechanisms | ✗ | No AI governance |
| Low-resource environments | ✓ | Small-scale fisheries, small boats (4–18m), low-tech gear |
| Decision architecture formalisation | △ | Fine-Kinney risk assessment is a structured P×C×F method; no formal architecture |
| Human role in decision-making | ✓ | Fisher risk perception directly measured; go/no-go decision context |
| Socio-technical evaluation | △ | Simulator-based risk perception study with fishermen |
| Coastal fisheries / maritime domain | ✓ | Directly small-scale coastal fisheries |

**Theme matches:** 3 full + 2 partial → **Full extraction**

---

## 3. Paper Type & Methodology

- **Type:** Empirical study — simulator-based risk perception assessment
- **Participants:** 30 small-scale fishing vessel captains from two Turkish fishing ports (İskele: n=20; Çeşmealtı: n=10)
- **Method:** Fine-Kinney risk assessment (P × C × F) applied during bridge navigation simulator scenarios under six environmental conditions: calm weather/sea, current (4 knots), restricted visibility (100m), night navigation, heavy weather (5 Beaufort), and combined night + heavy weather
- **Statistical analysis:** Mann-Whitney U test, Pearson correlation, independent-samples t-test (SPSS 22.0)
- **Simulator:** ARI (Applied Research International, Version 1.0), DNV-GL classified bridge operation simulator

---

## 4. Core Contribution Summary

The paper proactively assesses how small-scale fishermen perceive the risk of navigation under different environmental conditions using a bridge simulator and the Fine-Kinney risk assessment method. Fishermen evaluated the probability and consequences of accidents under six environmental scenarios for both sea and port navigation. The key finding is a clear risk hierarchy among environmental conditions: restricted visibility is rated the highest risk factor for sea navigation accident probability, while the combination of night + heavy weather is rated highest for port navigation and for overall accident consequences. Night navigation alone is consistently rated as more dangerous than daytime navigation across all conditions. The study advocates a proactive (pre-departure) environmental risk assessment approach to prevent maritime casualties.

---

## 5. Key Findings Relevant to Dissertation

### 5a. Night navigation significantly increases perceived accident risk

**This is the paper's most important finding for the t variable.**

Fishermen consistently rated night navigation as substantially more dangerous than daytime navigation:

- **Sea navigation, accident probability (all fishermen):** Night navigation mean = 4.08 vs. calm weather/sea mean = 3.43 (Table 6)
- **Sea navigation, accident consequence (all fishermen):** Night navigation mean = 12.80 vs. calm weather/sea mean = 8.53 (Table 6)
- **Combined night + heavy weather (sea, consequence):** Mean = 37.03 — the **highest single consequence score** across all conditions (Table 6)
- **Combined night + heavy weather (port, probability):** Mean = 5.56 — the **highest single probability score** for port navigation (Table 6)
- **Significant port-level difference:** İskele fishermen rated nighttime port navigation consequences at 4.40 vs. Çeşmealtı at 1.20 (p = 0.001), suggesting port geometry interacts with nighttime risk

**Direct relevance to Appendix C.1:** This provides empirical evidence from small-scale fishing vessel captains that night navigation elevates both accident probability and consequence severity, directly justifying the classification of t ∈ [19:00, 06:00) as UNSAFE in the safety state function f(E).

### 5b. Night as an amplifier of heavy weather risk

The combined night + heavy weather condition consistently produced the highest or near-highest risk scores across both ports and both navigation types:

- Sea navigation risk score: Night-heavy weather = highest for both İskele (35%) and Çeşmealtı (25%) fishermen
- Port navigation risk score: Night-heavy weather = highest for both İskele (45%) and Çeşmealtı (46%) fishermen

This amplification effect supports the max-severity aggregation rule in the formalisation: when multiple E vector variables independently classify to elevated states, the overall S should reflect the worst case. The interaction between t (night) and w (heavy weather) producing the highest risk scores validates the conservative max-severity approach.

### 5c. Restricted visibility is the highest single risk factor for sea navigation

Across both fishing ports, restricted visibility (100m range) was rated as the most dangerous single environmental factor for accident probability in sea navigation:

- İskele fishermen: restricted visibility = 26% of total probability score
- Çeşmealtı fishermen: restricted visibility = 28% of total probability score
- All fishermen, sea accident probability mean: restricted visibility = 7.90 (highest) vs. night-heavy weather = 6.30 (second)

**Relevance to t:** Time of day governs natural visibility for small vessels without radar. The finding that restricted visibility is the single most dangerous factor for sea navigation accident probability creates a direct empirical link between the t variable and the most critical risk factor identified by fishermen themselves. The CAUTION zone (17:00–19:00, approaching darkness) maps onto the transition from full visibility to restricted visibility — the exact condition fishermen identify as most dangerous.

### 5d. Environmental risk hierarchy established by fishermen

The study produces a clear risk ordering across environmental conditions. For **sea navigation probability** (all fishermen):

1. Restricted visibility (mean = 7.90)
2. Night + heavy weather (mean = 6.30)
3. Heavy weather alone (mean = 4.48)
4. Current (mean = 4.29)
5. Night alone (mean = 4.08)
6. Calm weather/sea (mean = 3.43)

For **sea navigation consequence** (all fishermen):

1. Night + heavy weather (mean = 37.03)
2. Restricted visibility (mean = 33.06)
3. Heavy weather alone (mean = 24.83)
4. Current (mean = 13.40)
5. Night alone (mean = 12.80)
6. Calm weather/sea (mean = 8.53)

**Relevance to E vector:** The five environmental conditions tested map directly onto variables in E = {w, r, m, o, v, t}: wind/heavy weather → w; visibility → governed by t; current → o; calm conditions → baseline. This empirical risk hierarchy from small-scale fishermen provides a domain-grounded basis for how f(E) should weight input variables.

### 5e. Port navigation perceived as safer than sea navigation

Under identical environmental conditions, fishermen consistently rated port navigation as less risky than sea navigation (Table 6, all means lower for port than sea). This aligns with the intuition that proximity to shore and familiarity reduce risk — but critically, **night + heavy weather in port still produces very high risk scores** (probability mean = 5.56, consequence mean = 19.70), confirming that environmental conditions dominate even in familiar waters.

### 5f. Strong correlation between past accidents and nighttime risk perception

Fishermen who had experienced more past accidents showed significantly stronger perception of nighttime risk:

- Number of accidents ↔ port navigation accident probability with night + heavy weather: **r = 0.866, p = 0.003**
- Number of accidents ↔ port navigation accident probability with restricted visibility: **r = 0.726, p = 0.027**

This suggests that experienced fishermen — those who have faced real maritime casualties — are particularly attuned to nighttime and visibility-related risks, reinforcing the validity of these conditions as safety-critical inputs.

### 5g. Proactive vs. reactive risk assessment framing

The paper explicitly advocates a shift from reactive (post-accident) to **proactive** (pre-departure) risk assessment. The authors argue that fishermen should assess environmental conditions before leaving port, and that if precautions cannot reduce accident probability, the trip should be cancelled.

**Relevance to architecture:** This pre-departure risk assessment framing maps precisely onto the architectural pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E). The paper's proactive approach is essentially what the deterministic safety classification layer does: evaluate environmental conditions before the trip and gate the decision accordingly. The paper provides empirical justification from the fisheries domain for exactly this architectural pattern.

### 5h. Fishing activity rated more dangerous than navigation

All fishermen stated that risk perception during active fishing is higher than during navigation, because fishermen neglect lookout duties while handling gear. This is noted but is outside the scope of the architectural E vector (which governs departure and navigation decisions, not fishing activity).

---

## 6. Methodology Assessment

**Strengths:**
- Simulator-based: controlled environmental conditions, standardised scenarios across participants
- Direct elicitation from active small-scale fishing captains (not proxied through accident statistics)
- Fine-Kinney method provides structured quantitative risk scores with probability, consequence, and frequency dimensions
- Statistical tests applied appropriately (nonparametric where distributions were non-normal)

**Limitations:**
- Small sample (n=30), acknowledged by authors
- Turkish Mediterranean context — fishermen's risk thresholds may differ from Malaysian tropical coastal fishermen
- Simulator fidelity: while DNV-GL classified, fishermen may not react identically to real conditions (authors acknowledge this)
- Fishing boats in the study (LOA 18m in simulator) are at the larger end of small-scale vessels; Malaysian coastal boats may be smaller
- No time-of-day threshold analysis — night is treated as a binary condition, not graduated into twilight/darkness zones

---

## 7. Quotable / Citable Elements

- **Night + heavy weather as highest risk:** "Night-heavy weather navigation was the most important factor for both the accident probability (mean = 5.56) and consequence (mean = 19.70) for all fishermen [in port navigation]" (Table 6)
- **Restricted visibility as highest single probability factor:** "Restricted visibility (mean = 7.90) for the probability of accidents... was identified as the most dangerous factor for all fishermen in sea navigation" (Table 6)
- **Correlation between accident history and nighttime risk perception:** "There is a significant, positive, and strong association between the number of accidents experienced by fishermen and... the night-heavy weather conditions in port navigation (p = 0.003, r = 0.866)" (Table 5)
- **Proactive recommendation:** "If the risk rating is high as a result of the experimental study, fishermen should not go to sea without taking precautions... if possible precautions do not reduce the probability of accidents, the cruise should be cancelled" (Conclusion)
- **Prior work on time-of-day:** "some previous work has examined a significant association between fishing vessel accidents and... time of day" (p. 2, citing Jin et al. 2001, 2002; Roberts et al. 2010; Kim & Kang 2011)

---

## 8. Connections to Other Extracted Papers

| Paper | Connection |
|---|---|
| **Rahim et al. (2024)** | Complementary evidence: Rahim provides fisher *behaviour* data (departure timing, self-restriction); Atacan provides fisher *risk perception* data (environmental conditions rated by severity). Together they establish both that fishermen perceive night/visibility as dangerous AND that they behaviourally self-restrict in response. |
| **Dominguez-Péry et al. (2023)** | Convergent evidence from different scales: Dominguez-Péry's IMO report analysis of large commercial vessels identifies visibility as a central risk cluster (26.7% of text segments); Atacan's small-scale fisheries simulator study identifies restricted visibility as the highest single risk factor. Same conclusion, different vessel scales and methods. |
| **Duit & Galaz (2008)** | Theoretical link: Atacan's empirical risk hierarchy (calm → current → night → heavy weather → night+heavy weather) provides domain evidence for the threshold effects and non-linear risk transitions that Duit & Galaz's governance theory predicts. |

---

## 9. Relevance to Specific Architecture Components

| Architecture Component | Relevance | Notes |
|---|---|---|
| E = {w, r, m, o, v, t} | **High** | Directly tests w (heavy weather/5 Beaufort), o (current/4 knots), t (night navigation), and visibility (governed by t). Provides mean risk scores for each. |
| S = f(E) | **Moderate** | Risk hierarchy supports threshold-based classification. Night + heavy weather producing highest risk supports max-severity aggregation. No tri-state mapping provided. |
| G(S) — Level 1 governance | **Low-Moderate** | Proactive recommendation to cancel trips when risk is high is functionally equivalent to G(S) = 0 for UNSAFE states. |
| A_AI(S) — Level 2 governance | **None** | No advisory scope concept |
| Safety Dominance Property | **None** | No formal safety constraint |
| CAUTION mode | **Low** | No intermediate state, but the graduated risk scores (night alone < night+weather) suggest a continuum that could be discretised into tri-state logic |
| PS5 (socio-technical evaluation) | **Low-Moderate** | Fisher risk perception methodology could inform PS5 evaluation design — measuring whether fishermen's trust and reliance on the system varies with safety state |

---

## 10. Relevance to E Vector Variables

| E variable | Evidence from this paper | Strength |
|---|---|---|
| **w (wind)** | Heavy weather (5 Beaufort) significantly increases both probability and consequence scores vs. calm conditions | **Strong** — directly tested |
| **r (rainfall)** | Not tested | None |
| **m (marine warning)** | Not tested directly, but environmental scenarios simulate conditions that would trigger warnings | Indirect |
| **o (ocean condition)** | Current (4 knots) tested; increases risk vs. calm but less than visibility or weather | **Moderate** — directly tested |
| **v (vessel class)** | All participants used same simulated vessel (LOA 18m); no vessel variation tested. But 90% of real boats were <12m. | Low |
| **t (time of day)** | Night navigation tested as separate condition and in combination with heavy weather. Night alone increases risk; night + heavy weather produces the highest overall risk scores. | **Strong** — directly tested, highest impact in combination |

---

## 11. Follow-up Papers Flagged

From the introduction (p. 2), the following are cited for the association between fishing vessel accidents and time of day:

- **Jin et al. (2001)** — determinants of fishing vessel total losses and injuries
- **Jin et al. (2002)** — model of fishing vessel accident probability
- **Roberts et al. (2010)** — human and fishing vessel losses in UK fishing (1948–2008)
- **Jin (2014)** — determinants of fishing vessel accident severity (found night hours increase collision probability)

These could provide additional quantitative evidence for the t variable if needed. Jin (2014) in particular is cited as showing that nighttime increases collision accident frequency for fishing vessels.

---

## 12. Citation Placement Recommendations

| Section | Use | Specific claim supported |
|---|---|---|
| **Appendix C / C.1 (t variable justification)** | **Primary** | Night navigation significantly increases accident probability and consequence for small-scale fishing vessels; restricted visibility (governed by time of day) is the single highest-rated risk factor for sea navigation |
| **Appendix C / C.1 (max-severity rule)** | Supporting | Night + heavy weather interaction produces highest risk scores across all conditions, validating conservative worst-case aggregation |
| **Section 1 (Motivation)** | Supporting | Small-scale fishing is one of the most dangerous occupations; proactive environmental risk assessment can prevent casualties |
| **Section 2.1 (Domain context)** | Supporting | Empirical risk hierarchy for environmental conditions in small-scale fisheries navigation |
| **Section 2.3 (Gap / design rationale)** | Supporting | Fishermen's proactive risk assessment recommendation maps onto the E → S = f(E) pipeline — existing practice calls for exactly the kind of environmental state classification the architecture formalises |

---

## 13. Final Relevance Score

**⭐⭐⭐ (3/5)**

**Justification:** This is a peer-reviewed empirical study directly in the small-scale fisheries domain that provides quantitative risk perception data for environmental conditions matching the E vector variables. It is the strongest available evidence for justifying the time-of-day variable t, because it measures fishermen's own risk ratings under controlled nighttime conditions and finds night navigation significantly elevates both accident probability and consequence. The restricted visibility finding further strengthens the t justification via the visibility → time-of-day causal chain. However, the paper has no AI component, no governance mechanism, no formalisation, and a small sample from a different geographic context (Turkey, not Malaysia). Its value is concentrated in E vector empirical grounding and the proactive risk assessment framing.

**Tracker cluster:** Domain context / E vector empirical grounding (t variable primary evidence)

---

## Post-Extraction Commentary

### This is your strongest t justification paper, Iskandar.

Here's the argument chain you can now construct for the time-of-day note in Appendix C.1:

**Three-source justification for t ∈ E:**

1. **Atacan & Düzbastılar (2023)** — Small-scale fishing vessel captains rate night navigation as significantly more dangerous than daytime navigation (mean probability 4.08 vs. 3.43; mean consequence 12.80 vs. 8.53). Combined night + heavy weather produces the highest overall risk scores. Restricted visibility — directly governed by time of day for small vessels without radar — is the single highest-rated risk factor for sea navigation accident probability (mean = 7.90).

2. **Dominguez-Péry et al. (2023)** — IMO accident investigation reports identify external environmental factors including visibility as the most prominent risk cluster (26.7% of text segments) across a decade of maritime accidents. Time of day is captured in accident reporting metadata.

3. **Rahim et al. (2024)** — Malaysian fishers behaviourally self-restrict departure timing based on environmental conditions, with departure patterns showing sensitivity to daylight availability.

**For the CAUTION zone (17:00–19:00) specifically:** You still need a source anchoring these specific thresholds to Malaysian tropical twilight timing. Civil twilight in peninsular Malaysia ends approximately 30–40 minutes after sunset, which occurs around 19:00–19:30 year-round near the equator. A citation to Malaysian Meteorological Department data or a nautical almanac for the region would close this gap.

### Tracker update recommendation

Add to tracker under "Domain context / E vector grounding":

```
Atacan & Düzbastılar (2023) ⭐⭐⭐ — Small-scale fisheries risk perception; 
night navigation and restricted visibility as highest-rated risk factors; 
Fine-Kinney method; primary evidence for t variable in E vector
```

### Inter-paper note

The proactive risk assessment framing in this paper's conclusion — "if precautions do not reduce the probability of accidents, the cruise should be cancelled" — is essentially a natural-language description of G(S) = 0 when S = UNSAFE. You could cite this as evidence that the participation gate concept is not an artificial imposition on fishing practice but rather a formalisation of what fisheries safety experts already recommend.
