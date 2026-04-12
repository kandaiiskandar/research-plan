# Literature Search Methodology

**Dissertation**: A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Socio-Technical Evaluation in Coastal Fisheries 
**Candidate**: Iskandar 
**Date of last search**: 2026 (latest paper year found in corpus) 
**Total papers included**: 75 

---

## 1. Research Questions Driving the Search

Five research questions (RQ1–RQ5) shaped the literature search, each motivating one or more search strands:

| Research Question | Summary | Search Strands Motivated |
|---|---|---|
| **RQ1** | What two-level governance architecture simultaneously governs AI participation (Level 1: G(S)) and AI recommendation scope (Level 2: A_AI(S)), conditioned on classified environmental safety state? | Strand 1, Strand 2 |
| **RQ2** | How can environmental conditions be formally classified into discrete safety states (SAFE / CAUTION / UNSAFE) such that the Safety Dominance Property AI(E) ⊆ A_AI(S) holds across all states? | Strand 2 |
| **RQ3** | How does the proposed architecture perform in low-resource coastal fisheries environments characterised by intermittent connectivity, limited data, and continuously varying environmental risk? | Strand 3 |
| **RQ4** | Does graduated two-level governance (ungated vs binary-gated vs two-level graduated) produce better-calibrated trust and decision quality than binary governance? | Strand 4 |
| **RQ5** | How do users understand, trust, and respond to graduated governance states — in particular the novel CAUTION mode, in which AI is active but operating under recommendation scope restriction? | Strand 4 |

**Rationale for search structure**: RQ1 and RQ2 motivated broad coverage of safety governance, hybrid AI, and formal methods literature to establish what exists and where the gap lies. RQ3 motivated domain-specific search across fisheries, maritime, and low-resource AI literature. RQ4 and RQ5 motivated a second-phase search (the methodological foundation phase) targeting trust measurement, trust calibration, and levels-of-automation literature to ground the evaluation design.

---

## 2. Search Strands and Keywords

Four search strands were used, each targeting a distinct research question cluster:

**Strand 1 — AI Safety Governance and Hybrid AI Architecture** (RQ1, RQ2)

Keywords: "AI governance", "safety governance", "graduated governance", "hybrid AI", "safety-critical AI", "runtime enforcement", "AI participation", "advisory scope", "safety shield", "guardrail", "formal verification", "decision architecture", "AI control mechanisms", "supervision function", "safety monitor", "neuro-symbolic AI", "deterministic rules", "probabilistic AI", "two-level governance"

**Strand 2 — Formal Methods and Safety Properties** (RQ2)

Keywords: "formal methods", "safety properties", "Safety Dominance", "reachability analysis", "Hamilton-Jacobi reachability", "control barrier function", "verified AI", "safe reinforcement learning", "environmental state classification", "safety state", "safety filter", "shielding", "model checking", "runtime verification", "formal safety guarantee", "SMT-based verification"

**Strand 3 — Low-Resource Environments and Fisheries Domain** (RQ3)

Keywords: "fisheries AI", "maritime AI", "coastal fishing", "small-scale fisheries", "low-resource AI", "resource-constrained", "edge AI", "offline AI", "decision support fisheries", "data-deficient fisheries", "autonomous shipping", "maritime safety", "fisher decision-making", "data-efficient AI", "TinyML", "federated learning", "AI deployment developing countries"

**Strand 4 — Trust, Evaluation, and Human Factors** (RQ4, RQ5)

Keywords: "trust in automation", "trust calibration", "trust in AI", "levels of automation", "graduated automation", "human factors AI", "socio-technical evaluation", "automation mode confusion", "AI decision support evaluation", "trust measurement", "TIAS", "human-AI interaction", "over-trust", "under-trust", "dependence on AI", "user study AI", "mixed-initiative AI"

---

## 3. Databases and Sources Searched

The primary search was conducted via **Scopus**, which provided cross-database access to IEEE, ACM, Elsevier, Springer, Taylor & Francis, and other indexed publishers. arXiv was searched directly for preprints in the AI safety and governance space. Additional papers were identified through backward snowball sampling and expert recommendation (see Section 7).

The table below shows the publisher/database breakdown of the 75 included papers, reflecting the range of sources indexed within Scopus and accessed directly.

| Database / Publisher | Papers in Set | Venues Represented |
|---|---|---|
| **Scopus** (primary search interface) | 66 | Cross-database aggregator — primary corpus papers indexed or accessible via Scopus |
| *of which* **IEEE Xplore** | 11 | IEEE IECON 2024, IEEE/ACM ICSE '26, 28th Euromicro DSD (IEEE), IEEE Comms Standards Magazine, IEEE T-ITS (×2), IEEE ICSA 2025, IEEE Trans. Neural Networks & Learning Systems, IEEE Trans. Technology and Society, IEEE Access Vol. 12 (Bach, Kristiansen et al.), IEEE/SICE SII 2023 (Odriozola-Olalde et al.), IEEE PRDC 2025 (Seong, Lim & Yoon) |
| *of which* **ACM Digital Library** | 6 | Communications of the ACM, ACM Computing Surveys (×2), ACM Transactions on Autonomous and Adaptive Systems, Journal of the ACM, ACM Web Conference 2025 (WWW Companion) |
| *of which* **Elsevier / ScienceDirect** | 12 | Intelligence-Based Medicine, iScience (Cell Press), Machine Learning with Applications, SoftwareX, Information Fusion, Results in Engineering, Journal of Loss Prevention in the Process Industries, Computers in Human Behavior: Artificial Humans, One Earth (Cell Press), Procedia CIRP, Marine Policy, Aquacultural Engineering (Chandran et al.) |
| *of which* **MDPI / Frontiers** | 13 | Buildings, Information (×2), Electronics, AI, Big Data and Cognitive Computing, Informatics, Frontiers in Marine Science (×2), Frontiers in Sustainable Food Systems, Frontiers in Artificial Intelligence (×2), Frontiers in Internet of Things (Ogenyi et al.) |
| *of which* **Springer / SpringerLink** | 4 | Journal of Marine Science and Technology, Annals of Mathematics and Artificial Intelligence, EURO Journal on Decision Processes, Scientific Reports (Zhang et al.) |
| *of which* **Taylor & Francis** | 5 | International Journal of Human–Computer Interaction (×2), Reviews in Fisheries Science & Aquaculture, Journal of Decision Systems, Behaviour & Information Technology |
| *of which* **Wiley / Oxford** | 2 | ICES Journal of Marine Science (Oxford UP), Journal of International Maritime Safety, Environmental Affairs, and Shipping |
| *of which* **Other / Specialist** | 13 | International AI Safety Report 2026 (UK DSIT), Security and Safety (EDP Sciences), Environmental Science Archives (Zenodo), UNSW Law Journal, Journal of Marine and Island Cultures, Pakistan Journal of Life and Social Sciences, AAAI-25 (Hamel-De le Court et al.), OWASP Foundation (Agentic Top 10), The Science World e-Magazine (Tandel et al.), Science/AAAS (Bengio, Hinton et al.), ICML 2025/PMLR (×2: SHIELDAGENT, CRANE), Korean J. Remote Sensing (Ryu & Han) |
| **arXiv** (searched directly) | 8 | Bajcsy/Fisac, Dalrymple et al., Baxi, Bloomfield/Rushby, Pitale et al. (HySAFE-AI), Corsi et al. (Verification-Guided Shielding), Feng et al. (Levels of Autonomy), Kwon et al. (Adaptive Shielding) |
| **Institutional repositories** | 1 | M.Sc. thesis — Gao (2024), WorldFish/CGIAR open repository |
| **External evidence phase** | 8 | Papers added in targeted fifth phase to strengthen novelty gap evidence (see Section 6, Stage 6) — AAAI (Hamel-De le Court), arXiv (Kwon, Feng), Scientific Reports/Springer Nature (Zhang), Aquacultural Engineering/Elsevier (Chandran), Frontiers in Internet of Things (Ogenyi), OWASP Foundation (OWASP Agentic Top 10), The Science World e-Magazine (Tandel) |
| **Governance comparators and domain evidence phase** | 9 | Papers added in targeted fourth phase (see Section 6, Stage 5) — IEEE Access (Bach, Kristiansen et al.), Science/AAAS (Bengio, Hinton et al.), arXiv (Corsi et al.), ICML/PMLR (SHIELDAGENT; CRANE), IEEE/SICE SII (Odriozola-Olalde et al.), IEEE PRDC (Seong, Lim & Yoon), IJHCI/T&F (Tatasciore & Loft), Korean J. Remote Sensing (Ryu & Han) |

**Note**: Several papers appear in multiple discovery paths (e.g., arXiv preprints later published in ACM CS). The table groups by primary publisher/access route. Scopus was the entry point for Strands 1–3 (safety governance, formal methods, fisheries/low-resource AI). arXiv was searched directly for Strand 2 (formal methods) given the pace of preprint publication in AI safety. Taylor & Francis papers in Strand 4 (trust and evaluation) were accessed via Scopus or targeted hand-search following examiner recommendation. The 9 governance comparator and domain evidence papers (papers 59–67) were added in a targeted fourth phase — see Section 6, Stage 5. The 8 external evidence papers (papers 68–75 in the tracker) were added in a targeted fifth phase to extend gap validation across safety shields, agent governance, IoT+AI, and autonomy frameworks — see Section 6, Stage 6. The "External evidence phase" and "Governance comparators and domain evidence phase" rows are informational callouts; all 75 papers are counted within the Scopus, arXiv, and institutional rows above.

---

## 4. Inclusion Criteria

| Criterion | Specification |
|---|---|
| **Language** | English only |
| **Date range** | 2022–2026 (earliest paper: Gabriel et al. 2022; latest: multiple papers 2026) |
| **Publication type** | Peer-reviewed journal articles, peer-reviewed conference papers, arXiv preprints (where content is sufficiently rigorous), theses/reports with institutional repository identifiers |
| **Relevance** | Addresses at least one of eight core themes (T1–T8): hybrid AI, safety-critical AI, AI governance, low-resource environments, decision architecture formalisation, human role in AI-assisted decision-making, socio-technical evaluation, or coastal fisheries/maritime domain |
| **Content** | Safety-critical AI, AI governance mechanisms, hybrid AI architecture, formal decision models, low-resource AI deployment, fisheries or maritime AI, human role in AI-assisted decisions, socio-technical evaluation of AI systems, or trust in automation/AI |
| **Extraction gate** | Papers retained only if scoring ≥ Minimal on a structured relevance check (early hard stop applied for clearly out-of-scope papers) |

---

## 5. Exclusion Criteria

| Criterion | Specification |
|---|---|
| **Language** | Non-English publications excluded |
| **Duplicates** | Same paper found via multiple databases or sources — retained once only |
| **Scope** | No relation to AI governance, safety-critical systems, or any of the eight core themes (T1–T8) |
| **Accessibility** | Full text unavailable via institutional or open access routes |
| **Domain-only** | Fisheries or maritime papers with no AI, governance, or decision-support component |
| **AI-only** | AI papers with no relevance to safety, governance, human factors, low-resource deployment, or fisheries context |
| **Relevance gate** | Papers scoring ⭐ Minimal (0 Yes and ≤ 1 Partial across relevance dimensions) received an early stop — 0 papers excluded at this stage in the final corpus |

---

## 6. Screening and Extraction Process

**Stage 1 — Title and Abstract Screening**

Titles and abstracts were reviewed against the eight core themes and the inclusion/exclusion criteria above. Papers with any plausible relevance to safety-critical AI, hybrid AI, AI governance, low-resource deployment, fisheries/maritime AI, or trust in automation were retained for full-text review.

**Stage 2 — Full-Text Screening and Relevance Gate**

Full texts were reviewed using a structured extraction template. An early relevance check (hard stop) was applied at the outset of each extraction: papers failing to address any of the eight themes were excluded without further extraction. A mid-extraction relevance gate then determined extraction depth:

| Extraction level | Gate condition | Papers |
|---|---|---|
| Full extraction (17 sections) | ≥ 3 Yes ratings across theme and relevance dimensions | n = 25 |
| Reduced extraction (7 sections) | 1–2 Yes or ≥ 2 Partial ratings | n = 24 |
| Early stop (no further extraction) | 0 Yes and ≤ 1 Partial | n = 0 |
| **Total via primary search** | | **n = 49** |

Two extraction templates were used:
- `methodologies/extraction-prompt.md` — for architecture, governance, and domain papers (full and reduced extraction)
- `methodologies/extraction-prompt-methodological.md` — for trust, levels of automation, and socio-technical evaluation papers (methodological foundation phase)

**Stage 3 — Methodological Foundation Phase (second pass)**

Six additional papers (papers 50–55 in the tracker) were added in a targeted second phase using `methodologies/extraction-prompt-methodological.md`. These papers address trust measurement, trust calibration, and human-AI dependence — providing the methodological foundations for the PS4/PS5 evaluation design. This phase was initiated following feedback indicating that the evaluation methodology required explicit grounding in the human factors and trust measurement literature.

| Extraction level | Papers |
|---|---|
| Methodological foundation (targeted extraction) | n = 6 |
| **Total included** | **n = 55** |

**Stage 4 — Domain Supplement Phase (third pass)**

Three domain-grounding papers (papers 56–58 in the tracker) were added in a targeted third pass to strengthen the empirical context for the target domain: Shaffril et al. (2017) for historical baseline of Malaysian SSF environmental adaptation, Yamin et al. (2025) as the primary empirical study for Terengganu SSF, and Muhamad et al. (2024) for productivity factor validation in Malaysian SSF.

| Extraction level | Papers |
|---|---|
| Domain supplement (targeted extraction) | n = 3 |
| **Total included** | **n = 58** |

**Stage 5 — Governance Comparators and Domain Evidence Phase (fourth pass)**

Nine papers (papers 59–67 in the tracker) were added in a targeted fourth pass to deepen the comparator set and domain evidence base across five groups: (i) HAII and policy context — Bach, Kristiansen et al. (2024) [SLR of HAII in safety-critical industries, IEEE Access] and Bengio, Hinton et al. (2024) [Science policy perspective on graduated institutional governance]; (ii) shielded RL comparators — Corsi et al. (2024) [region-selective verification-guided shielding, arXiv] and Odriozola-Olalde et al. (2023) [shielded RL taxonomy, IEEE/SICE SII]; (iii) action suppression comparators — Chen, Kang & Li (2025) [SHIELDAGENT, ICML] and Seong, Lim & Yoon (2025) [CLGuard semantic suppression, IEEE PRDC]; (iv) trust methodology — Tatasciore & Loft (2025) [empirical evidence that corrective trust feedback fails, IJHCI]; and (v) formal theoretical motivation and maritime domain evidence — Banerjee et al. (2025) [CRANE formal proof that binary output constraints reduce LLM expressivity, ICML] and Ryu & Han (2025) [maritime environmental conditions as first-order determinants of sensor reliability, Korean J. Remote Sensing].

| Extraction level | Papers |
|---|---|
| Governance comparators and domain evidence (targeted) | n = 9 |
| **Total included** | **n = 67** |

**Stage 6 — External Evidence Phase (fifth pass)**

Eight additional papers (papers 68–75 in the tracker) were added in a targeted fifth phase to extend and validate the binary governance gap across four domains not fully covered in the primary corpus: safety shields (Hamel-De le Court et al. 2025, Kwon et al. 2025), agent governance frameworks (Feng et al. 2025, OWASP 2025), IoT+AI systems (Zhang et al. 2025, Ogenyi et al. 2025), and aquaculture/fisheries IoT (Chandran et al. 2025, Tandel et al. 2025). These papers were identified through targeted searches of arXiv, Google Scholar, Elsevier, Frontiers, and OWASP to test the novelty claim against the widest possible evidence base.

| Extraction level | Papers |
|---|---|
| External evidence (gap validation) | n = 8 |
| **Total included** | **n = 75** |

This review followed a semi-systematic search protocol. Exact counts at identification and screening stages are estimated retrospectively; future updates should record these prospectively.

---

## 7. Additional Search Methods

**Backward snowball sampling**

Reference lists of key papers were scanned for additional relevant works. The following citation relationships within the corpus were identified, indicating papers discovered through backward snowball from foundational works:

*Cluster 1 — Safety Governance lineage:*
- Dalrymple et al. (2024) "Guaranteed Safe AI" → cited by → Liang et al. (2025) "Safeguarded AI" (implements world-model/safety-spec/gatekeeper architecture as per-output filter)
- Dalrymple et al. (2024) → cited by → Bengio et al. (2026) "International AI Safety Report 2026" (as theoretical foundation for guaranteed safety approaches)
- Bajcsy & Fisac (2024) "Human-AI Safety" → cited by → Ramos et al. (2024) "Collaborative Intelligence" (as Fisac et al. for Bayesian prediction in collaborative intelligence)
- Perez-Cerrolaza et al. (2024) "AI Safety-Critical Survey" → shared authorship with → Abella et al. (2025) "SAFEXPLAIN" (overlapping author team)
- Perez-Cerrolaza et al. (2024) → cited by → Newcomb & Ochoa (2026) "Formal methods SLR" (in background)
- Flehmig et al. (2024) → cited by → Newcomb & Ochoa (2026) (in SLR corpus)

*Cluster 2 — Guardrails lineage:*
- Shamsujjoha et al. (2025) "Swiss Cheese Model" → cited by → Chen et al. (2025) "AI Safety LLM Landscape" (guardrail taxonomy referenced)

*Cluster 3 — Trust and evaluation methodology lineage:*
- Bach et al. (2024) "User Trust SLR" → builds into → McGrath et al. (2025) "S-TIAS" (trust measurement SLR used as foundation for instrument selection)
- McGrath et al. (2025) "S-TIAS" ↔ McGrath et al. (2025) "CHAI-T" (same lead author, complementary papers: instrument + framework)
- McGrath et al. (2025) "CHAI-T" ↔ Schrills et al. (2025) "Questioning Trust" (complementary findings on trust calibration and trust–dependence distinction)

*Cluster 4 — Fisheries lineage:*
- Wing & Woodward (2024) → Kühn et al. (2025) → Welch et al. (2024): shared co-author (Jordan T. Watson) connecting fisheries AI monitoring papers — not citation relationships per se but a dense single-community cluster indicating snowball potential within the fisheries AI literature

**Forward citation chasing**

Citing papers of core comparators were checked for relevant extensions. Specifically, citing papers of Flehmig et al. (2024), Könighofer et al. (2025), Dalrymple et al. (2024), and Baxi (2026) were reviewed for papers extending binary governance toward graduated or state-conditioned approaches. No papers implementing state-conditioned two-level governance were found — confirming the gap.

**Expert/examiner recommendation**

The six methodological foundation papers (Bach et al. 2024; McGrath et al. 2025 — CHAI-T; Aquilino et al. 2025; Atf & Lewis 2026; McGrath et al. 2025 — S-TIAS; Schrills et al. 2025) were added in response to feedback that the evaluation methodology chapters required explicit grounding in the trust and human factors literature. These papers were not identified through the primary keyword search but through targeted hand-search of the trust-in-automation literature following examiner guidance.

---

## 8. PRISMA Flow Diagram

```
╔══════════════════════════════════════════════════════════════════╗
║                         IDENTIFICATION                           ║
╠══════════════════════════════════════════════════════════════════╣
║  Records identified through database searching                   ║
║    (n = estimated — not recorded prospectively)                  ║
║                                                                  ║
║  Additional records from snowball / citation chasing             ║
║    (n = estimated ~8–12, from reference list scanning)           ║
║                                                                  ║
║  Records added via expert/examiner recommendation                ║
║    (n = 6 — methodological foundation papers 50–55)              ║
║                                                                  ║
║  Records added via domain supplement phase                       ║
║    (n = 3 — domain-grounding papers 56–58)                       ║
║                                                                  ║
║  Records added via governance comparators phase                  ║
║    (n = 9 — comparator and evidence papers 59–67)                ║
║                                                                  ║
║  Records added via external evidence phase                       ║
║    (n = 8 — gap validation papers 68–75)                         ║
╠══════════════════════════════════════════════════════════════════╣
║                           SCREENING                              ║
╠══════════════════════════════════════════════════════════════════╣
║  Records after duplicates removed                                ║
║    (n = estimated)                                               ║
║                                                                  ║
║  Records screened at title/abstract                              ║
║    (n = estimated)                                               ║
║       └─ Records excluded at title/abstract (n = estimated)      ║
╠══════════════════════════════════════════════════════════════════╣
║                          ELIGIBILITY                             ║
╠══════════════════════════════════════════════════════════════════╣
║  Full-text records assessed for eligibility                      ║
║    (n = estimated)                                               ║
║       ├─ Excluded — out of scope (n = estimated)                 ║
║       ├─ Excluded — full text inaccessible (n = estimated)       ║
║       └─ Excluded — early stop (relevance gate) (n = 0)          ║
╠══════════════════════════════════════════════════════════════════╣
║                           INCLUDED                               ║
╠══════════════════════════════════════════════════════════════════╣
║  Studies included in review (n = 75)                             ║
║       ├─ Full extraction (17 sections): n = 25                   ║
║       ├─ Reduced extraction (7 sections): n = 24                 ║
║       ├─ Methodological foundation (targeted): n = 6             ║
║       ├─ Domain supplement (targeted): n = 3                     ║
║       ├─ Governance comparators and domain evidence: n = 9       ║
║       └─ External evidence (gap validation): n = 8               ║
╚══════════════════════════════════════════════════════════════════╝
```

*Note: Counts marked "estimated" were not recorded prospectively during the search. Exact pre-screening counts should be confirmed if this review is updated or submitted for formal audit. The endpoint counts — 75 included, 25 full, 24 reduced, 6 methodological, 3 domain supplement, 9 governance comparators, 8 external evidence — are exact.*

---

## 9. Venue Distribution

The following table lists all 75 papers organised by database/publisher category, with venue details as extracted from Section 1 of each paper's notes file.

### ACM Digital Library (6 papers)

| # | Author(s) | Year | Venue |
|---|---|---|---|
| 3 | Könighofer et al. | 2025 | Communications of the ACM, Vol. 68, No. 11, pp. 80–90 |
| 22 | Perez-Cerrolaza et al. | 2024 | ACM Computing Surveys, Vol. 56, Issue 7, Article 176 |
| 14 | Chen et al. | 2025 | ACM Computing Surveys (arXiv:2408.12935v3) |
| 23 | Porter et al. | 2025 | ACM Transactions on Autonomous and Adaptive Systems, Vol. 20, Issue 3 |
| 24 | Punzi et al. | 2024 | Journal of the ACM, Vol. 1, No. 1 (arXiv:2402.06287) |
| 29 | Zhao & Yuan | 2025 | ACM Web Conference 2025 (WWW Companion), ACM |

### IEEE Xplore (11 papers)

| # | Author(s) | Year | Venue |
|---|---|---|---|
| 4 | Wang et al. | 2026 | IEEE/ACM ICSE '26 (48th Int. Conference on Software Engineering) |
| 5 | Abella et al. | 2025 | 28th Euromicro Conference on Digital System Design (DSD), IEEE |
| 10 | Flehmig et al. | 2024 | IEEE IECON 2024 (50th Annual Conference of IEEE Industrial Electronics Society) |
| 11 | Liang et al. | 2025 | IEEE Communications Standards Magazine, Dec. 2025, pp. 41–49 |
| 15 | Gyllenhammar et al. | 2025 | IEEE Transactions on Intelligent Transportation Systems, Vol. 26, No. 4 |
| 19 | Li et al. | 2026 | IEEE Transactions on Intelligent Transportation Systems (early access) |
| 27 | Shamsujjoha et al. | 2025 | IEEE 22nd International Conference on Software Architecture (ICSA) |
| 53 | Atf & Lewis | 2026 | IEEE Transactions on Technology and Society, Vol. 7, No. 1 |
| 59 | Bach, Kristiansen et al. | 2024 | IEEE Access, Vol. 12, pp. 106385–106414 |
| 63 | Odriozola-Olalde et al. | 2023 | IEEE/SICE International Symposium on System Integration (SII 2023) |
| 64 | Seong, Lim & Yoon | 2025 | IEEE PRDC 2025 (30th Int. Symposium on Pacific Rim Dependable Computing) |

### arXiv (8 papers — preprints not yet in a peer-reviewed venue at time of access)

| # | Author(s) | Year | Venue |
|---|---|---|---|
| 1 | Bajcsy & Fisac | 2024 | arXiv:2405.09794v2 |
| 2 | Dalrymple et al. | 2024 | arXiv:2405.06624v3 |
| 6 | Baxi | 2026 | arXiv:2603.15639v2 |
| 8 | Bloomfield & Rushby | 2025 | arXiv:2407.13948v3 / SRI CSL Technical Report SRI-CSL-2024-02R3 |
| 41 | Pitale et al. | 2025 | arXiv:2507.17118v1 |
| 61 | Corsi et al. | 2024 | arXiv:2406.06507v2 |
| 69 | Kwon et al. | 2025 | arXiv:2506.11033v2 |
| 71 | Feng et al. | 2025 | arXiv:2506.12469v2 / Knight First Amendment Institute, Columbia University |

### Elsevier / ScienceDirect / Cell Press (12 papers)

| # | Author(s) | Year | Venue |
|---|---|---|---|
| 13 | Bhuvaneswari et al. | 2025 | Intelligence-Based Medicine, Vol. 12, 100311 (Elsevier) |
| 12 | Mussi et al. | 2025 | iScience, 28, 113400 (Cell Press / Elsevier) |
| 17 | Katende | 2026 | Machine Learning with Applications, Vol. 23, 100796 (Elsevier) |
| 34 | Kalmykov & Kalmykov | 2025 | Information Fusion, Vol. 123, 103352 (Elsevier) |
| 37 | Longobardi et al. | 2025 | SoftwareX, Vol. 29, 102028 (Elsevier) |
| 44 | Tahsin et al. | 2025 | Results in Engineering, Vol. 25, 103825 (Elsevier) |
| 43 | Selvam et al. | 2026 | Journal of Loss Prevention in the Process Industries, Vol. 100, 105917 (Elsevier) |
| 47 | Welch et al. | 2024 | One Earth, 7, 1685–1691 (Cell Press / Elsevier) |
| 51 | McGrath et al. (CHAI-T) | 2025 | Computers in Human Behavior: Artificial Humans, 6, 100200 (Elsevier) |
| 32 | Gabriel et al. | 2022 | Procedia CIRP, 109, pp. 431–436 (Elsevier) |
| 56 | Shaffril et al. | 2017 | Marine Policy, Vol. 81, pp. 196–201 (Elsevier) |
| 72 | Chandran et al. | 2025 | Aquacultural Engineering, 111, 102584 (Elsevier) |

### MDPI / Frontiers (13 papers)

| # | Author(s) | Year | Venue |
|---|---|---|---|
| 9 | Castagnone & Nitti | 2026 | Buildings, 16(3), 534 (MDPI) |
| 16 | Haque & Al Jufaili | 2026 | Big Data and Cognitive Computing, 10(1), 19 (MDPI) |
| 25 | Ramos et al. | 2024 | Information (MDPI), Vol. 15, Issue 11, Article 728 |
| 39 | Nastoska et al. | 2025 | Electronics, 14(13), 2717 (MDPI) |
| 48 | Wen et al. | 2025 | AI, 6(8), 164 (MDPI) |
| 45 | Talpur et al. | 2025 | Information (MDPI), 16, 658 |
| 52 | Aquilino et al. | 2025 | Informatics, 12(3), 70 (MDPI) |
| 31 | Bossier et al. | 2025 | Frontiers in Marine Science, 12:1521526 (Frontiers) |
| 57 | Yamin et al. | 2025 | Frontiers in Marine Science, 12:1492131 (Frontiers) |
| 40 | Obi et al. | 2025 | Frontiers in Sustainable Food Systems, 9:1545263 (Frontiers) |
| 21 | Newcomb & Ochoa | 2026 | Frontiers in Artificial Intelligence, Vol. 9, 1749956 (Frontiers) |
| 54 | McGrath et al. (S-TIAS) | 2025 | Frontiers in Artificial Intelligence, 8:1582880 (Frontiers) |
| 74 | Ogenyi et al. | 2025 | Frontiers in the Internet of Things, 4:1658273 (Frontiers) |

### Taylor & Francis (5 papers)

| # | Author(s) | Year | Venue |
|---|---|---|---|
| 50 | Bach et al. | 2024 | International Journal of Human–Computer Interaction, 40(5), 1251–1266 |
| 35 | Kühn et al. | 2025 | Reviews in Fisheries Science & Aquaculture, Vol. 33, No. 2, pp. 334–357 |
| 26 | Saup et al. | 2026 | Journal of Decision Systems, 35(1), 2597835 |
| 55 | Schrills et al. | 2025 | Behaviour & Information Technology (online 2025) |
| 65 | Tatasciore & Loft | 2025 | International Journal of Human–Computer Interaction, 41(23), 14723–14733 |

### Wiley / Oxford University Press (2 papers)

| # | Author(s) | Year | Venue |
|---|---|---|---|
| 49 | Wing & Woodward | 2024 | ICES Journal of Marine Science, Vol. 81, Issue 10, pp. 1912–1919 (Oxford UP) |
| 20 | Madsen & Kim | 2024 | Journal of International Maritime Safety, Environmental Affairs, and Shipping, 8(1–2) |

### Springer Nature (4 papers)

| # | Author(s) | Year | Venue |
|---|---|---|---|
| 28 | Yuzui & Kaneko | 2025 | Journal of Marine Science and Technology, 30, pp. 153–176 (Springer) |
| 46 | Vermaelen & Holvoet | 2025 | Annals of Mathematics and Artificial Intelligence, 93, 541–567 (Springer) |
| 36 | Leppinen et al. | 2026 | EURO Journal on Decision Processes, 14, 100063 (Springer) |
| 73 | Zhang et al. | 2025 | Scientific Reports, 15, 29056 (Springer Nature) |

### AAAI (1 paper)

| # | Author(s) | Year | Venue |
|---|---|---|---|
| 68 | Hamel-De le Court et al. | 2025 | AAAI-25 (39th AAAI Conference on Artificial Intelligence), pp. 16091–16099 |

### Other / Specialist (13 papers)

| # | Author(s) | Year | Venue |
|---|---|---|---|
| 7 | Bengio et al. | 2026 | International AI Safety Report 2026 (UK DSIT / Crown copyright) |
| 18 | Klüver et al. | 2024 | Security and Safety, Vol. 3, 2024020 (EDP Sciences) |
| 38 | Mandal et al. | 2025 | Environmental Science Archives, Vol. IV, Issue 1, pp. 44–58 (Zenodo) |
| 33 | Gao | 2024 | Unpublished M.Sc. thesis, IMRD/Erasmus Mundus, deposited WorldFish/CGIAR repository |
| 30 | Bello y Villarino et al. | 2025 | UNSW Law Journal, 48(4), pp. 1165–1195 |
| 58 | Muhamad et al. | 2024 | Pakistan Journal of Life and Social Sciences (PJLSS), 22(2), 12024–12040 |
| 42 | Rahim et al. | 2024 | Journal of Marine and Island Cultures, v13n3 |
| 60 | Bengio, Hinton et al. | 2024 | Science, Vol. 384, Issue 6698, pp. 842–845 (DOI: 10.1126/science.adn0117) |
| 62 | Chen, Kang & Li | 2025 | ICML 2025, Proceedings of Machine Learning Research (PMLR) 267 |
| 66 | Banerjee et al. | 2025 | ICML 2025, Proceedings of Machine Learning Research (PMLR) 267 |
| 67 | Ryu & Han | 2025 | Korean Journal of Remote Sensing, 41(6), pp. 1225–1250 |
| 70 | OWASP | 2025 | OWASP Foundation — Agentic Top 10 for AI Applications (December 2025) |
| 75 | Tandel et al. | 2025 | The Science World e-Magazine, ISSN 2583-2212, Vol. 5(2), pp. 6319–6327 |

---

## 10. Date Range and Coverage

### Year Range

- **Earliest paper**: 2022 (Gabriel et al., Procedia CIRP — socio-technical AI requirements)
- **Latest papers**: 2026 (11 papers, including AgentSpec, Bengio/International AI Safety Report, Haque/Al Jufaili, Castagnone, Leppinen, Li, Saup, Selvam, Baxi, Atf & Lewis, Newcomb/Ochoa)

### Year Distribution

| Year | Count | Notes |
|---|---|---|
| 2017 | 1 | Shaffril et al. (historical contextual background for Malaysian SSF domain) |
| 2022 | 1 | Gabriel et al. (foundational socio-technical method) |
| 2023 | 1 | Odriozola-Olalde et al. (shielded RL taxonomy — comparator for binary governance confirmation) |
| 2024 | 16 | Core comparators: Bajcsy/Fisac, Dalrymple, Flehmig, Perez-Cerrolaza, Klüver, Madsen/Kim, Punzi, Rahim, Welch, Wing/Woodward, Bach, Gao, Muhamad et al.; governance comparators: Bach/Kristiansen (HAII SLR), Bengio/Hinton (Science policy), Corsi (verification-guided shielding) |
| 2025 | 45 | Largest cohort — covers governance taxonomy, formal methods SLR, fisheries reviews, trust measurement literature, external evidence (Hamel-De le Court, Kwon, Feng, Zhang, OWASP, Chandran, Ogenyi, Tandel); governance comparators (SHIELDAGENT, CLGuard, Tatasciore/Loft, CRANE, Ryu/Han); includes Yamin et al. (primary domain study) |
| 2026 | 11 | Most recent: AgentSpec, International AI Safety Report, Baxi, Castagnone, Haque, Leppinen, Li, Saup, Selvam, Atf & Lewis, Newcomb |
| **Total** | **75** | |

### Coverage Assessment

The corpus is highly contemporary: 56 of 75 papers (75%) are from 2025–2026, reflecting the rapidly evolving state of the safety governance and AI control literature. The 2022–2024 papers (17 papers, 23%) establish foundational comparators and domain context. One paper (Odriozola-Olalde et al., 2023) covers shielded RL taxonomy; one paper (Shaffril et al., 2017) is included as historical contextual background for the target domain. No other pre-2022 papers are included, reflecting a deliberate focus on current practice and the recency of the formal AI governance literature.

**Theme-specific currency**:

- **T1 (Hybrid AI) and T2 (Safety-critical AI)**: Papers span 2024–2026, with the core architectural comparators (Shields, AgentSpec, SAFEXPLAIN, Dalrymple, Bajcsy) clustering in 2024–2025. The field is active and recent.
- **T3 (AI governance)**: The most recent papers (2025–2026) reflect a governance paradigm shift post-ChatGPT. Binary governance is confirmed as universal across all surveyed frameworks through 2026. The 9 governance comparator papers (2023–2025) extend confirmation to shielded RL (Odriozola-Olalde, Corsi), action suppression (SHIELDAGENT, CLGuard), and HAII policy (Bach/Kristiansen, Bengio/Hinton). The 8 external evidence papers (2025) further extend to safety shields (Hamel-De le Court, Kwon), agent governance (Feng, OWASP), and IoT+AI (Zhang, Chandran, Ogenyi, Tandel).
- **T4 (Low-resource AI)**: Katende (2026) is the most comprehensive recent taxonomy; domain papers span 2024–2026.
- **T6 (Human role) and T7 (Socio-technical evaluation)**: The trust measurement literature (papers 50–55) was largely published 2024–2026, reflecting growing attention to rigorous trust operationalisation.
- **T8 (Fisheries/maritime)**: The fisheries AI literature reviewed includes papers through 2026 (Haque & Al Jufaili), confirming that no formal governance architecture existed in this domain at the time of search. Chandran et al. (2025) and Tandel et al. (2025) further confirm that IoT+AI systems in aquaculture/fisheries use environmental sensors as AI input but implement no governance layer.

---

## 11. Search Limitations

1. **Retrospective documentation**: This methodology document was produced retrospectively from the extracted corpus. Exact counts at the identification and pre-screening stages were not recorded prospectively and are therefore estimated in the PRISMA flow diagram. Future search updates should record these counts at the time of search.

2. **Date cutoff**: Papers published after early 2026 are not included. The safety governance field is evolving rapidly; papers appearing after the search window may address related gaps.

3. **Language bias**: Only English-language papers were included. This may systematically exclude work from Malaysia, Indonesia, the Philippines, and other small-scale fisheries nations where relevant domain expertise may be published in national languages.

4. **Grey literature scope**: arXiv preprints were included (6 papers) given the high pace of publication in AI safety. Unpublished technical reports, government documents (other than the International AI Safety Report), and workshop proceedings without DOIs were excluded. One M.Sc. thesis (Gao 2024) was included given its unique empirical contribution to domain context and its institutional repository availability.

5. **Methodological foundation papers added retrospectively**: The six trust and evaluation papers (papers 50–55) were added in a second phase following examiner feedback, not as part of the initial primary search. They represent a targeted supplementary search rather than a systematic strand, and are documented separately in Section 6 (Stage 3).

6. **Keyword sensitivity**: Search strings were optimised for governance and safety-critical system framing. Papers using alternative vocabulary — for example, "autonomy levels" rather than "AI governance", "operational design domain" rather than "environmental state", or "AI oversight" rather than "AI participation control" — may have been missed if they did not appear via snowball sampling or expert recommendation.

7. **Snowball incompleteness**: Backward snowball was limited to scanning reference lists of core papers and forward citation checking of primary comparators. A full systematic backward snowball (following all references of all included papers) was not conducted. The citation relationships documented in Section 7 represent the subset identified during extraction rather than a complete citation network analysis.

---

## USER INPUT REQUIRED

The following items could not be derived from the extracted notes and require user confirmation:

- [x] **Actual databases searched** — confirmed: Scopus (primary), arXiv (direct). Section 3 updated accordingly. If additional databases were searched but yielded 0 results (e.g., Web of Science, PubMed), add them to Section 3 with a note.

- [ ] **Actual search strings used** — if the literal query strings were recorded at the time of search, please supply them for Section 2. The keyword clusters shown are a retrospective reconstruction from the themes and paper types found; they may differ from the strings actually entered.

- [ ] **Date(s) searches were conducted** — the "Date of last search" field currently shows the latest paper year (2026) as a proxy. Please supply the actual calendar date(s) on which database searches were run.

- [ ] **Approximate number of records identified at database search stage** — required for PRISMA compliance. Even a rough estimate (e.g., "approximately 300–400 records identified across all databases") is sufficient for the PRISMA flow diagram in Section 8.

- [ ] **Approximate number excluded at title/abstract and full-text stages** — required for PRISMA flow. Estimated counts (e.g., "approximately 200 excluded at title/abstract; approximately 50–60 assessed full-text") are acceptable with "(estimated)" notation.

- [ ] **Papers added on supervisor or examiner recommendation** — please confirm which specific papers (if any beyond the 6 trust papers in the methodological foundation phase) were suggested by supervisors or examiners, for transparency in Section 7 (Expert/examiner recommendation).

- [ ] **Any additional exclusion criteria applied** — for example, minimum citation count thresholds, journal impact requirements, or any domain-specific filters not captured in the criteria listed in Section 5.
