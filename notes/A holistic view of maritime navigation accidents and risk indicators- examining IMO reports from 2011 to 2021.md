# Paper Extraction: Dominguez-Péry et al. (2023)

## 1. Bibliographic Information

- **Title:** A holistic view of maritime navigation accidents and risk indicators: examining IMO reports from 2011 to 2021
- **Authors:** Carine Dominguez-Péry, Rana Tassabehji, Franck Corset, Zainab Chreim
- **Year:** 2023
- **Venue:** *Journal of Shipping and Trade*, 8:11
- **DOI:** https://doi.org/10.1186/s41072-023-00135-y
- **Type:** Peer-reviewed journal article (Open Access, CC BY 4.0)

---

## 2. Early Relevance Gate

| Core Theme | Match? | Notes |
|---|---|---|
| Hybrid AI (rule-based + probabilistic) | ✗ | No AI system involved |
| Safety-critical AI decision-making | ✗ | Human decision-making only |
| AI governance and control mechanisms | ✗ | No AI governance |
| Low-resource environments | △ | Small vessels identified as highest-risk category; indirect relevance |
| Decision architecture formalisation | ✗ | No formal decision architecture |
| Human role in decision-making | △ | Human error analysis; human-centric accident reporting critique |
| Socio-technical evaluation | △ | AME ecosystem framework is socio-technical |
| Coastal fisheries / maritime domain | ✓ | Maritime domain (large commercial shipping primarily, but includes all vessel types) |

**Theme matches:** 1 full + 3 partial → **Reduced extraction** (Sections 4–7, 12–13)

---

## 3. Paper Type & Methodology

- **Type:** Empirical study — mixed methods (statistical analysis + text mining)
- **Data:** 504 IMO maritime accident investigation reports (2011–2021)
- **Methods:** Descriptive statistics, ANOVA (Kruskal-Wallis), IRAMUTEQ text mining (similarity analysis, descending hierarchical classification, correspondence factor analysis)
- **Framework output:** Accident Maritime Ecosystem (AME) framework — five nested layers of risk actors

---

## 4. Core Contribution Summary

The paper challenges the dominant human-error-centric framing of maritime accident causes. Using a decade of IMO accident reports, the authors apply statistical and text mining techniques to identify five clusters of risk factors. Three clusters (75.5% of text segments) relate to what the authors term "fate risk factors" — individual human error, technical failures, and external environmental factors. Two clusters (24.5%) reveal under-reported organisational and ecosystem-level actors. The paper proposes the Accident Maritime Ecosystem (AME) framework with five nested layers: individual, ship organisation, ship internal ecosystem, ship external ecosystem, and global maritime ecosystem.

---

## 5. Key Findings Relevant to Dissertation

### 5a. External environmental factors as a major risk cluster

Cluster 5 (26.7% of all text segments) describes **external factors during navigation**: wind, vessel speed, bad weather, and poor visibility. This is the largest single cluster in the analysis, confirming that environmental conditions are among the most prominently reported risk factors in maritime accident investigation.

**Relevance to E vector:** Directly supports the inclusion of wind (w), ocean conditions (o), and — critically — visibility-affecting variables in the environmental state vector. Time of day (t) governs visibility in small-vessel operations; the prominence of visibility as an accident factor in this dataset provides empirical grounding for treating t as a safety-relevant input to f(E).

### 5b. Small vessels have the highest fatality rate

ANOVA results (p = 0.01) found a significant difference in deaths by vessel size. Small vessels (≤2,000 GT) had the **highest mean rank for deaths (3.67)**, compared to large vessels (1.02) and medium vessels (0.85). This is despite small vessels comprising only 58 of 504 accidents in the dataset.

**Relevance to dissertation:** Malaysian coastal fishing vessels are small craft. This finding provides empirical evidence that small-vessel operations carry disproportionate fatality risk, strengthening the case for a safety governance architecture specifically targeting this vessel class.

### 5c. Vessel age as a significant risk factor

Older vessels (>20 years) had the highest mean death rank (2.13), followed by young vessels (≤10 years, 1.21), with middle-aged vessels lowest (0.64). Significant at p = 0.009.

**Relevance to E vector (vessel class, v):** Supports treating vessel characteristics as safety-relevant. In the Malaysian coastal fisheries context, many vessels are aged and may lack modern safety equipment, which maps onto the vessel class variable v in the state vector.

### 5d. Inconsistency in vessel-characteristic-based risk prediction

The paper documents contradictory findings across the literature regarding how vessel age, size, and flag state relate to accident severity. The authors argue this inconsistency means vessel characteristics alone are unreliable risk predictors and that a broader ecosystem lens is needed.

**Relevance to architecture:** This supports the multi-variable approach of E = {w, r, m, o, v, t} — no single variable is a reliable predictor; the classification function f(E) must integrate multiple environmental and operational parameters.

### 5e. Time of day in accident data

The IMO reporting structure captures **date and time of accident** as standard fields (exemplified in the Costa Concordia entry: "AccDT_13-01-2012At21h00" — 9:00 PM, i.e., nighttime). The dendrogram sub-analysis of Cluster 5 includes navigational context terms such as "weather," "wind," "visibility," and temporal/positional terms. Time of day is embedded in the accident reporting structure as a contextual factor.

**Relevance to t variable:** While the paper does not isolate time of day as a standalone statistical variable, its inclusion in IMO reporting structure and its indirect presence through the visibility/external factors cluster supports treating time of day as a legitimate environmental input. The Costa Concordia example (accident at 21:00) and the prominence of visibility in Cluster 5 provide circumstantial evidence that nighttime operations elevate risk — consistent with the UNSAFE classification for t ∈ [19:00, 06:00) in the formalisation.

### 5f. Weather and wind as central risk terms

In the similarity analysis of the 143 most frequent terms, "weather" and "wind" appear directly in the "vessel" universe of words, connected to general navigational information. In the dendrogram (Cluster 5), "wind" is the highest-weighted term, followed by "speed," "weather," "swell," and "position."

**Relevance to E vector:** Directly validates w (wind) and o (ocean condition, including swell) as core variables. Confirms that these are among the most frequently reported contextual factors in real maritime accident investigations.

---

## 6. Limitations and Gaps (from dissertation perspective)

1. **Commercial shipping focus:** The dataset covers IMO-reported accidents, which are predominantly large commercial vessels. Small-scale coastal fisheries are almost entirely absent from IMO reporting — Malaysian fishing vessels would not appear in this dataset.

2. **No AI component:** The paper contains no discussion of AI, decision support systems, or automated governance. It is purely an accident analysis study.

3. **Time of day not statistically analysed:** While time is captured in the data, the authors did not include it as an independent variable in the ANOVA. The evidence for t is therefore indirect (via visibility cluster and accident timestamps).

4. **No graduated risk classification:** External factors are treated as a single cluster, not graduated into severity levels. There is no analogue to the tri-state SAFE/CAUTION/UNSAFE classification.

5. **Western/international bias:** IMO reports are submitted by national administrations, predominantly from developed maritime nations. Malaysian small-craft accident data would not be captured.

---

## 7. Quotable / Citable Elements

- **Small vessel fatality finding:** "Small-sized vessels (less than 2KGT) reported the highest number of deaths" (p. 13) — citable as empirical evidence for elevated risk in small-vessel operations.
- **External factors cluster size:** Cluster 5 (external factors including wind, weather, visibility) represents 26.7% of all text segments — the largest single cluster.
- **Inconsistency argument:** The paper documents contradictory findings across studies regarding vessel characteristics and accident severity, supporting multi-variable environmental state classification.

---

## 12. Relevance to Specific Architecture Components

| Architecture Component | Relevance | Notes |
|---|---|---|
| E = {w, r, m, o, v, t} | **Moderate** | Validates w, o, v as empirically grounded risk variables. Indirect support for t via visibility cluster. |
| S = f(E) | **Low** | No classification function; no graduated risk states |
| G(S) — Level 1 governance | **None** | No AI participation mechanism |
| A_AI(S) — Level 2 governance | **None** | No advisory scope mechanism |
| Safety Dominance Property | **None** | No formal safety constraint |
| CAUTION mode | **None** | No intermediate state concept |
| PS4 (graduated vs. binary) | **None** | No governance comparison |
| PS5 (socio-technical evaluation) | **Low** | AME ecosystem framework is a socio-technical lens, but for accident analysis not AI trust |

---

## 13. Citation Placement Recommendations

| Section | Use | Specific claim supported |
|---|---|---|
| **Section 1 (Motivation)** | Supporting | Small vessels face disproportionate fatality risk — motivates the need for safety governance in coastal fisheries |
| **Section 2.1 (Domain context)** | Supporting | External environmental factors (wind, weather, visibility) are the most prominently reported risk category in maritime accident investigation |
| **Appendix C / C.1 (E vector justification)** | **Primary use** | Empirical evidence that wind, ocean conditions, vessel characteristics, and visibility-related factors (time of day proxy) are documented risk indicators in maritime accident investigation reports |
| **Appendix C / C.1 (Time of day note)** | Supporting | IMO accident reporting captures time of day; visibility appears as a central term in the largest risk cluster; nighttime accident examples (Costa Concordia at 21:00) provide circumstantial support for t as safety-relevant |

---

## Final Relevance Score

**⭐⭐ (2/5)**

**Justification:** The paper is a peer-reviewed maritime domain study with a robust dataset (504 IMO reports over a decade) and validated statistical findings. However, it has no AI component, no governance mechanism, no formal risk classification, and focuses on large commercial shipping rather than coastal fisheries. Its value to the dissertation is narrow but real: it provides empirical evidence from maritime accident investigation that external environmental factors — particularly wind, weather, visibility, and vessel characteristics — are among the most prominent risk indicators, supporting the composition of the environmental state vector E and providing circumstantial justification for the time-of-day variable t.

**Tracker cluster:** Domain context / E vector empirical grounding

---

## Post-Extraction Commentary

### Strategic value for the time-of-day justification

Iskandar, this paper provides **partial but not standalone** support for including t in the E vector. Here's what it gives you:

1. **Visibility is prominent:** Cluster 5 (26.7% of text segments) centres on external navigational factors, with visibility explicitly named. Since time of day is the primary determinant of natural visibility for small vessels without radar, this creates a logical chain: *visibility is an empirically validated maritime risk factor → time of day governs visibility → therefore t is a legitimate input to f(E)*.

2. **Accident timestamps confirm nighttime risk:** The Costa Concordia (21:00) and other accidents have timestamps captured in the data, though the authors didn't analyse time as a variable. This is circumstantial but citable.

3. **Small-vessel finding is a bonus:** The p = 0.01 finding that small vessels have the highest fatality rate is independently valuable for Section 1 motivation — it anchors the "why coastal fisheries?" question in quantitative maritime safety evidence.

### What this paper does NOT give you for t

It does not provide a statistical analysis of time-of-day as an independent variable, nor does it establish threshold values for daylight-related risk transitions. For that, you need **Rahim et al. (2024)** (fisher departure timing behaviour) and potentially the **Utne/Johansen** maritime risk supervision papers for threshold-based operational safety zones. You could also look for IMO or Malaysian Maritime Enforcement Agency (MMEA) data on accident timing distributions to find a direct statistical relationship.

### Recommendation

Cite Dominguez-Péry et al. (2023) in the Appendix C time-of-day note as one element of a multi-source justification: *"External environmental factors including visibility are among the most prominently reported risk indicators in maritime accident investigation (Dominguez-Péry et al., 2023), and time of day is the primary determinant of natural visibility for small-vessel operations without electronic navigation aids."* Then pair it with Rahim et al. (2024) for fisher-specific departure timing evidence and any available MMEA/IMO temporal distribution data.
