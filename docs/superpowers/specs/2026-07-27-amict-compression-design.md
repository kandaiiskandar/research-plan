# Compression Design: ipsci-2026-paper-v7.md → 6 IEEE Pages

**Date:** 2026-07-27  
**Target:** AMICT conference, hard 6-page limit (references included)  
**Current state:** ~9 pages including references  
**Goal:** ~3 pages recovered through restructuring, not wordsmithing

---

## Guiding Principle

Every paragraph should either establish the gap or explain the contribution. If a paragraph only elaborates on a point already established, it is a compression candidate.

The architecture section is the contribution. It must be protected. All compression comes from the literature survey and the introduction.

---

## Target Page Allocation

| Section               | Target        |
|-----------------------|---------------|
| Introduction          | 0.6–0.7 page  |
| Methodology           | 0.4–0.5 page  |
| Literature Review     | 1.8–2.0 pages |
| Proposed Architecture | 1.8–2.0 pages |
| Conclusion            | 0.5 page      |
| References            | 0.8–1.0 page  |
| **Total**             | **~6 pages**  |

---

## Section-by-Section Specification

---

### 1. Introduction → ~350–400 words (0.6–0.7 page)

**Keep:**
- Opening sentence establishing AI decision support in safety-critical settings
- Governance maturity gap (Reuel et al. [31]) — one sentence only, not a paragraph
- Fisheries motivation — two sentences (not one; provides concrete deployment context)
- Fig. 1 (three governance dimensions) — earns its space as the visual gap statement
- Two-contributions paragraph — condense to ~60 words

**Move to Proposed Architecture section:**
- The five-concept terminology block (AI decision support system, safety-critical system, runtime governance, advisory scope, environmental safety state) — relocate as a ~100-word definitional preamble immediately before the Formal Structure subsection, where these terms are first used precisely

**Cut entirely:**
- The paragraph beginning "Runtime governance frameworks determine whether AI may participate..." — Fig. 1 communicates this distinction visually; prose is redundant

**Result:** Introduction structure becomes: problem → gap → contribution. No definitions. Reviewers reach the literature in under a page.

---

### 2. Methodology → ~60–80 words + Table I (0.4–0.5 page)

**Keep:**
- Table I (four coding dimensions) — unchanged; load-bearing for Table II legibility
- One paragraph: databases (Scopus, IEEE Xplore, Web of Science, ACM DL), 72 papers, three large-scale systematic reviews (532 references), four coding dimensions, three paradigms + application domain

**Cut:**
- All three subsection headers (Search Strategy, Screening and Inclusion, Theme Development)
- Two-stage screening description
- Citation tracing detail
- Theme development prose

---

### 3. Literature Review → 1.8–2.0 pages

#### 3a. Overview paragraph (~60 words)
One sentence per paradigm naming its governance topology, one sentence naming the common absence, one sentence pointing to Fig. 2. No subsection header needed — runs as the opening of the Literature Review section.

#### 3b. Deterministic Safety Constraints (~70 words)
One paragraph. Shields, Guaranteed Safe AI, safety filter share the same binary topology. Advisory content not governed. [8][9][10] cited together. Cut references to [11] Corsi and [12] Abella — same point, redundant.

#### 3c. Authority Allocation (~70 words)
One paragraph. Ramos, Feng, Mussi — advisory scope fixed at design time regardless of conditions. [13][14] cited. [33] Mussi: retain only if the paragraph still feels well-supported without it; if cutting weakens the cross-domain claim, keep one sentence with the citation.

#### 3d. Adaptive Risk-Based Systems (~250 words) — longest subsection, retained in most detail
One paragraph per closest precedent. Three-paradigm taxonomy (oversight intensification, execution deferral, action-class restriction) preserved in prose, subheadings dropped.
- Flehmig et al. [7]: ~50 words — three-level degradation index, intermediate level governs human supervisory behaviour not AI output
- Kang GAIE [25]: ~40 words — graduated tiers, coding agent generates full-scope output at every tier
- Ghaleb et al. [27]: ~40 words — three-regime safety gate, output capability uncontracted at Borderline
- Sahoo AMAGF [26]: ~50 words — genuine graduated contraction but governs execution of acting agent, conditioned on control quality not environmental state
- Baxi K-tier [15]: ~30 words — permission sets vary by tier, conditioned on AI robustness not environmental state
- Brief closing sentence: across all three paradigms, graduated operational posture is feasible; the gap is where graduation is applied

#### 3e. Synthesis (~200 words)
Table II carries the comparison; prose states what the table proves.

Must include this bridge sentence explicitly:
> "Across all reviewed paradigms, the object of governance differs, but none conditions AI advisory scope on classified environmental safety state."

Four independent literature streams compressed to four sentences (Indykov, Shamsujjoha, adaptive risk-based body, fisheries/low-resource). The conditioning-variable misalignment (all gate on internal AI properties, not environmental state) preserved in ~2 sentences — the sharpest analytical point in the paper.

**Fisheries and Low-Resource Deployment:** folded into Synthesis as two sentences. "The pattern extends to the application domain: no fisheries AI system implements formal advisory scope restriction conditioned on environmental state [17]; the only external advisory available to coastal fishers is a binary government warning [18]; and safety governance has not been designed from the deployment floor [19]."

#### 3f. Mechanistic Basis (~130 words)
One paragraph, no subheadings. Three limitations named and cited: (1) fixed inference pipeline — no hook for semantic content conditioning [28]; (2) reasoning breadth is a property of decoding not input risk [29]; (3) self-assessed confidence poorly calibrated and non-learning [30]. Framing sentence on Symbolic AI Reasoning Engine preserved. Closing sentence: internal governance cannot be relied upon; the gap requires an external architectural layer.

#### 3g. Objectives of This Study — cut entirely
Saves ~150 words and one subsection header. The Synthesis establishes the gap; the Architecture section opens with a one-sentence transition.

#### Table II — 5 columns, all 9 rows
**Drop columns:** "Intermediate mode variable" and "AI status at max risk"  
**Keep columns:** Framework | Governance target | Conditioning variable | Runtime adaptation | Output restriction  
**Keep all 9 rows** — each is evidence, not background  
Do not reduce further; the five remaining columns allow reviewers to reconstruct the comparison independently.

---

### 4. Proposed Architecture → 1.8–2.0 pages (protected)

**Add at top:** Five-concept terminology block, condensed to ~100 words, as definitional preamble before Formal Structure. (Moved from Introduction.)

**Keep intact and do not cut:**
- Formal Structure
- Safety Dominance Property
- Table III
- CAUTION mode explanation (the novel contribution)
- Domain Instantiation paragraph
- Illustrative scenario
- Fig. 3, Fig. 4

**Minor trim only:** CAUTION Mode operational case — remove ~100 words from the Ghaleb/Pro2Guard trade-off numbers (21.6 vs. 11.5 interventions; 93.6% / 17.54% / 80.4%). Keep the conclusion ("all-or-nothing gating destroys utility precisely where bounded operation could preserve it"), cut the specific numbers.

**Opening transition sentence:** "The review establishes the gap; the following section proposes the architecture it implies." (Replaces the now-cut Objectives of This Study.)

---

### 5. Conclusion → ~300 words (0.5 page)

**Keep intact:** Final paragraph beginning "The graduated safety-state-gated architecture proposed here..." — this is the strongest closing in the paper.

**Compress:** Opening summary of Shamsujjoha and Indykov (~80 words at current length) → two sentences. These points are already established in the Synthesis; the Conclusion should remind, not re-prove.

---

### 6. References — remove five

| Reference | Reason for removal |
|-----------|-------------------|
| [11] Corsi — verification-guided shielding | Same point as [8] Könighofer; redundant |
| [12] Abella — SAFEXPLAIN | Same point as [8] Könighofer; redundant |
| [22] Attard-Frost/Lyons | Cited once in Synthesis; point covered by [31] Reuel and [5] Indykov |
| [33] Mussi | Remove if authority-allocation paragraph remains well-supported without it; retain if not |
| [36] Batool | Cited once; point absorbed into Indykov [5] reference |

Renumber all remaining references sequentially after removal.

---

## What is Not Changing

- All formal notation: E, S = f(E), G(S), A_AI(S), Safety Dominance Property
- All figures: Fig. 1, Fig. 2, Fig. 3, Fig. 4
- Table III (governance pair configurations)
- The CAUTION mode as the novel contribution
- The containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅
- The proof-by-construction basis for the Safety Dominance Property
- The domain instantiation (E = {w, r, m, o, v, t})

---

## Summary of Savings

| Decision | Estimated saving |
|----------|-----------------|
| Introduction compression + terminology move | ~300 words |
| Methodology subsections cut | ~200 words |
| Objectives of This Study cut | ~150 words |
| Fisheries section folded into Synthesis | ~180 words |
| Mechanistic Basis compressed to one paragraph | ~250 words |
| Synthesis compressed | ~200 words |
| Each paradigm section compressed | ~200 words total |
| Conclusion opening compressed | ~60 words |
| Table II two columns dropped | ~½ column width |
| Five references removed | ~15 lines |
| **Total** | **~1,500+ words** |

At IEEE double-column format (~500 words per column), ~1,500 words ≈ 3 columns ≈ 1.5 pages. Combined with the reference and table savings, this targets the 3-page reduction required.
