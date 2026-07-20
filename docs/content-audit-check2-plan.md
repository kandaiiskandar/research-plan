# Content Audit — Check 2: Claim Accuracy Plan

**Scope:** `ipsci-2026-paper-v5.md`  
**Against:** Notes files in `notes/` (via `docs/citation-notes-map.md`)  
**Tier 1 verification:** Completed 2026-07-20  
**Tier 2 / Tier 3:** Pending

---

## Method

For each cited paper, identify the exact claim(s) made in the paper body, then verify against the corresponding notes file. Only claims with verifiable specific content are included — general "this paper discusses X" citations are excluded.

**Priority tiers:**

- **Tier 1 — Quantitative claims** (specific numbers, statistics, percentages) — highest falsification risk
- **Tier 2 — Qualitative characterisations** of papers central to the gap argument
- **Tier 3 — Structural descriptions** (what a framework does / how it works)

---

## Tier 1 — Quantitative Claims

| Ref | Paper | Claim in paper | Status | Finding |
|---|---|---|---|---|
| [31] | Reuel et al. | "1,000 organizations across 20 industries and 19 regions"; "9% reach highest governance maturity; only 0.8% reach it operationally; none reach both" | **Confirmed** | All four numbers verified in notes §1 and §2 |
| [5] | Indykov et al. | "206 papers and 16 architectural tactics"; "AT11 → Safety = 0" | **Confirmed** | 206 papers, 16 ATs, AT11→Safety=0 all verified in notes §1 and §6 |
| [6] | Shamsujjoha et al. | "13 guardrail actions across 32 studies" | **Confirmed** | 13 action types and 32 selected studies verified in notes §1 and §4 |
| [13] | Ramos et al. | "reviewing 91 collaborative intelligence studies" | **Confirmed** | "91 articles, 2014–2023" verified in notes §1 |
| [22] | Attard-Frost & Lyons | "610 topics from expert interviews" | **Confirmed** | "610 governance-related topics across 12 analytical dimensions" verified in notes §2 |
| [36] | Batool et al. | "systematic review of 28 AI governance studies"; "only three studies address who governs, what, when, and how" | **Confirmed** | "28 primary studies" and "Only 3 of 28 studies answer all four questions" verified in notes §2 |
| [11] | Corsi et al. | "reduce overhead by 25–71%" | **Wrong — corrected** | Primary source Table 4 confirms the combined gain range is 20.5–71.1%. The 25% lower bound was taken from Seed 104 (25.1%) but the actual minimum is Seed 225 (20.5%). Paper corrected to "20–71%"; notes §2 summary corrected to "20–71% (exact 20.5–71.1%)". |
| [34] | Wang et al. (Pro2Guard) | "93.6% of unsafe tasks"; "collapses task completion to 17.54%"; "softer mode recovers 80.4%" | **Confirmed** | All three percentages verified verbatim in notes §2 |
| [27] | Ghaleb et al. | "21.6 vs. 11.5 interventions per shifted episode" | **Confirmed** | Verified verbatim in notes §11 and quoted in §15 |
| [2] | Dominguez-Péry et al. | "504 IMO reports 2011–2021"; "26.7% of text segments"; "small vessels highest mean fatality rank (p = 0.01)" | **Confirmed** | All three claims verified in notes §3 and §5 |
| [3] | Atacan & Düzbastılar | "30 small-scale fishing captains"; "mean 37.03"; bridge navigation simulator | **Confirmed** | 30 captains, mean 37.03 (Table 6), ARI/DNV-GL simulator — all verified in notes §3 and §5 |
| [1] | Yamin et al. | "89,000 registered small-scale fishers"; "vessels under 40 GRT"; "0–5 nautical miles" | **Wrong — corrected** | "Vessels below 40 GRT" and "0–5 nm" confirmed (Introduction, p. 3). "89,000 registered fishers" does NOT appear anywhere in the Yamin paper — it is a national LKIM/Department of Fisheries figure, not a Yamin finding. Wrong citation attribution. Paper corrected: "89,000 registered" removed from sentence; [1] retained for the vessel/zone/traditional-knowledge claims that Yamin does verify. Yamin-verified national stats added to notes (75.8% of registered fishers are SSF; 5,023+ in Terengganu; ~800 in study area). |
| [24] | Perez-Cerrolaza et al. | "294 references across safety-critical domains" | **Confirmed** | "294 references" verified in notes §1 ("40 pages, 294 references") |
| [26] | Sahoo | "five response levels"; "CQS levels 0.4–0.6" | **Confirmed** | Five levels (Normal/Elevated/Restricted/Minimal/Safe State) and CQS 0.4–0.6 = Restricted — verified in notes §2 and §4 |

### Tier 1 Summary

| Result | Count |
|---|---|
| Confirmed | 12 |
| Wrong — corrected | 2 |
| Needs review | 0 |

**[11] Corsi et al. "25–71%"** — primary source Table 4 confirms the actual range is 20.5–71.1%. The 25% lower bound came from Seed 104 (25.1%) while the true minimum is Seed 225 (20.5%). Fixed to "20–71%" in the paper and notes. ✓

**[1] Yamin et al. "89,000 registered fishers"** — confirmed absent from the primary source. The figure is a national LKIM/Department of Fisheries statistic, not a Yamin finding. Citation attribution was wrong. Removed from the paper sentence; [1] retained on the verified claims (vessels under 40 GRT, 0–5 nm, traditional knowledge erosion). Yamin national-scale stats added to notes (75.8% SSF share, 5,023+ in Terengganu, ~800 local). ✓

**Tier 1 complete — no open items remaining.**

---

## Tier 2 — Qualitative Gap Argument Claims

| Ref | Paper | Claim in paper | Status |
|---|---|---|---|
| [7] | Flehmig et al. | Three-level traffic-light (green/orange/red); at orange: supervisory checks intensify; at red: control → non-AI backup; AI advisory scope **identical at green and orange** | Pending |
| [7] | Flehmig et al. | Direct quote: *"To our knowledge, there is currently no existing framework or method for indexing AI degradation in safety-critical systems in such a manner"* — must match notes verbatim | Pending |
| [9] | Dalrymple et al. | "Guaranteed Safe AI, requiring formal proof certificates before AI output is deployed" | Pending |
| [25] | Kang | "Three oversight tiers via a deterministic classification model with monotonicity, fail-safety, and totality properties"; coding agent generates "full-scope, unconstrained code artifacts at every tier" | Pending |
| [26] | Sahoo | "restricts to reversible actions only" at intermediate CQS; "governs an executing military agent rather than a human-facing recommendation menu" | Pending |
| [15] | Baxi | "tiers determined by AI's own verified robustness, not by classified environmental state" | Pending |
| [32] | Engin & Hand | "dimensions defined as properties of the human-AI relationship, not of the operator's physical environment" | Pending |
| [35] | Kolt et al. | "effective governance must intervene early, at calibrated risk thresholds, on incomplete information" | Pending |

---

## Tier 3 — Structural Descriptions

| Ref | Paper | Claim in paper | Status |
|---|---|---|---|
| [16] | Vermaelen & Holvoet | "allowed(a,s) predicate" as "absolute execution toggle" | Pending |
| [34] | Wang et al. | "learns a Discrete-Time Markov Chain from execution traces" | Pending |
| [27] | Ghaleb et al. | Three regimes: Safe to proceed / Borderline / Unsafe to proceed; Borderline forces "re-observation loop capturing alternative camera viewpoints" | Pending |
| [28] | Kamath et al. | "compute-bound prefill phase" + "memory-bandwidth-bound decode phase" — two fixed phases of LLM inference | Pending |
| [29] | Wu et al. | "models collapse onto single highest-probability component at each step"; "exploration restored only by externally injected, undirected randomness" | Pending |
| [30] | Cash et al. | "five preregistered studies comparing four LLMs with human participants"; "ChatGPT and Gemini failed to improve calibration after task" | Pending |
| [33] | Mussi et al. | "function allocation and automation levels fixed at design time" | Pending |

---

## Scope Exclusions

Papers cited only for general context with no specific characterisation in the paper body — not checked:

- [8] Könighofer — cited for shields concept, no specific statistics
- [10] Bajcsy & Fisac — cited as "control-theoretic safety filter", no further claims
- [12] Abella et al. — cited as "supervision function that can switch to non-AI fallback"
- [14] Feng et al. — cited for agency/autonomy decomposition, no specific numbers
- [17]–[21] — application domain papers cited for general domain evidence; [2] and [3] cover the key statistics already in Tier 1

---

## Execution Order

1. Tier 1 in full — numbers are binary right/wrong, fastest to verify
2. Tier 2, starting with [7] Flehmig direct quote — central to the gap argument
3. Tier 3 — structural claims, verify mechanics match notes
