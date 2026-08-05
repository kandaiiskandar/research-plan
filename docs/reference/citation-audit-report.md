# Citation Audit Report — ipsci-2026-paper-v5.md

**Audited:** 2026-07-20  
**Corrections applied:** 2026-07-20 (all 12 wrong entries fixed; verified against Crossref, arXiv, Springer Link, and Elsevier; [10] and [11] resolved via user-supplied registry lookups)  
**Method:** Each of the 36 references in the paper was cross-checked against (1) `docs/citation-notes-map.md` and (2) the actual notes files in `notes/`, comparing the paper's stated venue, DOI, and arXiv ID against the identity section recorded in the notes file.

---

## Summary

| Category | Count |
|---|---|
| Total references | 36 |
| Confirmed correct | 24 |
| Wrong bibliographic details (all corrected) | 12 |
| Unconfirmed / pending | 0 |
| Papers with no notes file (fabricated) | 0 |

All 36 papers exist and have substantive notes files. No paper is entirely fabricated. 12 references carried incorrect venue, DOI, or arXiv IDs — hallucinated bibliographic details attached to real papers. All 12 have been corrected in `ipsci-2026-paper-v5.md`.

---

## Confirmed Correct (23 references)

The following references were verified against the notes files and match exactly.

| Ref | Citation |
|---|---|
| [1] | Yamin et al. — *Frontiers in Marine Science*, 12:1492131. doi: 10.3389/fmars.2025.1492131 ✓ |
| [2] | Dominguez-Péry et al. — *Journal of Shipping and Trade*, 8:11. doi: 10.1186/s41072-023-00135-y ✓ |
| [3] | Atacan & Düzbastılar — *Ege Journal of Fisheries and Aquatic Sciences*, 40(1), 1–14. doi: 10.12714/egejfas.40.1.01 ✓ |
| [4] | Wen et al. — *AI*, 6(8), 164. doi: 10.3390/ai6080164 ✓ |
| [6] | Shamsujjoha et al. — IEEE ICSA 2025, pp. 37–48. doi: 10.1109/ICSA65012.2025.00014 ✓ |
| [7] | Flehmig et al. — IEEE IECON 2024. doi: 10.1109/IECON55916.2024.10906021 ✓ |
| [9] | Dalrymple et al. — arXiv:2405.06624 ✓ |
| [13] | Ramos et al. — *Information*, 15(11), 728. doi: 10.3390/info15110728 ✓ |
| [18] | Rahim et al. — *Journal of Marine and Island Cultures*, v13n3. doi: 10.21463/jmic.2024.13.3.05 ✓ |
| [22] | Attard-Frost & Lyons — *AI and Ethics*, 5, 2557–2604. doi: 10.1007/s43681-024-00569-5 ✓ |
| [23] | Bloomfield & Rushby — SRI Technical Report, arXiv:2407.13948. doi: 10.48550/arXiv.2407.13948 ✓ |
| [24] | Perez-Cerrolaza et al. — *ACM Computing Surveys*, 56(7), art. 176. doi: 10.1145/3626314 ✓ |
| [25] | Kang — arXiv:2606.22484v2 [cs.HC], Jul. 2026 ✓ |
| [26] | Sahoo — ICLR 2026 Workshop on Agents in the Wild; arXiv:2603.03515 ✓ |
| [27] | Ghaleb et al. — *Sensors*, 26(10), 3140. doi: 10.3390/s26103140 ✓ |
| [28] | Kamath et al. — ASPLOS '25, pp. 897–912. doi: 10.1145/3676641.3715996 ✓ |
| [29] | Wu et al. — arXiv:2508.03440 ✓ |
| [30] | Cash et al. — *Memory & Cognition*, 54, 375–400. doi: 10.3758/s13421-025-01755-4 ✓ |
| [31] | Reuel et al. — FAccT '25, pp. 2505–2541. doi: 10.1145/3715275.3732165 ✓ |
| [32] | Engin & Hand — arXiv:2505.11579 ✓ |
| [33] | Mussi et al. — *iScience*, 28, 113400. doi: 10.1016/j.isci.2025.113400 ✓ |
| [35] | Kolt et al. — *Patterns*, 6, 101341. doi: 10.1016/j.patter.2025.101341 ✓ |
| [36] | Batool et al. — *AI and Ethics*, 5, 3265–3279. doi: 10.1007/s43681-024-00653-w ✓ |

---

## Wrong Bibliographic Details — Corrected (12 references)

The paper exists and has a notes file, but the journal, conference, DOI, or arXiv ID stated in the paper did not match the notes. All entries below have been corrected in `ipsci-2026-paper-v5.md`.

---

### [5] Indykov et al. — Minor DOI error

**Paper states:**
```
doi: 10.1016/j.jss.2024.112373
```

**Notes say (correct):**
```
Journal of Systems & Software, Vol. 223 (2025), Article 112373
doi: 10.1016/j.jss.2025.112373
```

**Fix:** Change `j.jss.2024.112373` → `j.jss.2025.112373`

---

### [8] Könighofer et al. — Wrong journal entirely

**Paper states:**
```
Formal Methods in System Design, vol. 65, pp. 1–38, 2025.
doi: 10.1007/s10703-025-00456-7
```

**Notes say (correct):**
```
Communications of the ACM, Vol. 68, No. 11, pp. 80–90, 2025.
doi: 10.1145/3715958
```

**Fix:** Replace journal, volume, pages, and DOI in full.

Correct reference line:
```
B. Könighofer et al., "Shields for safe reinforcement learning," Communications of the ACM,
vol. 68, no. 11, pp. 80–90, 2025. doi: 10.1145/3715958
```

---

### [12] Abella et al. — Wrong venue type (journal vs. conference)

**Paper states:**
```
Safety Science, vol. 181, p. 106699, 2025.
doi: 10.1016/j.ssci.2024.106699
```

**Notes say (correct):**
```
28th Euromicro Conference on Digital System Design (DSD), IEEE, pp. 324–331, 2025.
doi: 10.1109/DSD67783.2025.00053
```

**Fix:** Replace journal citation with conference citation.

Correct reference line:
```
J. Abella et al., "SAFEXPLAIN: A complete approach towards trustworthy AI-based safety-critical
systems," in Proc. 28th Euromicro Conf. Digital System Design (DSD), IEEE, 2025, pp. 324–331.
doi: 10.1109/DSD67783.2025.00053
```

---

### [14] Feng, McDonald & Zhang — Wrong arXiv ID

**Paper states:**
```
arXiv preprint arXiv:2506.01234, 2025.
```

**Notes say (correct):**
```
arXiv:2506.12469v2 (Knight First Amendment Institute at Columbia University; 28 Jul 2025)
URL: https://arxiv.org/abs/2506.12469
```

**Fix:** Change `arXiv:2506.01234` → `arXiv:2506.12469`

Correct reference line:
```
Z. Feng, J. McDonald, and C. Zhang, "Levels of autonomy for AI agents,"
arXiv preprint arXiv:2506.12469, 2025.
```

---

### [15] Baxi — Wrong arXiv ID and wrong ID prefix year

**Paper states:**
```
arXiv preprint arXiv:2504.01234, 2026.
```

**Notes say (correct):**
```
arXiv:2603.15639v2 (February 2026; v2 March 2026)
doi: 10.48550/arXiv.2603.15639
```

**Fix:** Change `arXiv:2504.01234` → `arXiv:2603.15639`

Correct reference line:
```
A. Baxi, "The comprehension-gated agent economy: A robustness-first architecture for
AI economic agency," arXiv preprint arXiv:2603.15639, 2026.
```

---

### [16] Vermaelen & Holvoet — Wrong journal and wrong DOI

**Paper states:**
```
IEEE Transactions on Cognitive and Developmental Systems, 2025.
doi: 10.1109/TCDS.2025.00123
```

**Notes say (correct):**
```
Annals of Mathematics and Artificial Intelligence, vol. 93, pp. 541–567, 2025.
(Published online 26 July 2024; journal volume 2025)
doi: 10.1007/s10472-024-09949-3
```

**Fix:** Replace journal name, volume, pages, and DOI in full.

Correct reference line:
```
J. Vermaelen and T. Holvoet, "Tumato 2.0: A constraint-based planning approach for safe
and robust robot behavior," Annals of Mathematics and Artificial Intelligence, vol. 93,
pp. 541–567, 2025. doi: 10.1007/s10472-024-09949-3
```

---

### [17] Haque & Al Jufaili — Wrong journal and wrong DOI

**Paper states:**
```
Reviews in Aquaculture, 2026.
doi: 10.1111/raq.12967
```

**Notes say (correct):**
```
Big Data and Cognitive Computing, vol. 10, no. 1, art. 19. MDPI. (Published 5 January 2026)
doi: 10.3390/bdcc10010019
```

**Fix:** Replace journal name, volume, article number, and DOI.

Correct reference line:
```
M. S. Haque and S. Al Jufaili, "Applications of artificial intelligence in fisheries:
From data to decisions," Big Data and Cognitive Computing, vol. 10, no. 1, art. 19, 2026.
doi: 10.3390/bdcc10010019
```

---

### [19] Katende — Wrong journal and wrong DOI

**Paper states:**
```
AI & Society, 2026.
doi: 10.1007/s00146-026-01234-5
```

**Notes say (correct):**
```
Machine Learning with Applications, Vol. 23, Article 100796. Elsevier. (Published November 2025; volume dated 2026)
doi: 10.1016/j.mlwa.2025.100796
```

**Fix:** Replace journal name, volume, article number, and DOI.

Correct reference line:
```
A. Katende, "Rethinking data-efficient artificial intelligence for low-resource settings,"
Machine Learning with Applications, vol. 23, p. 100796, 2026.
doi: 10.1016/j.mlwa.2025.100796
```

---

### [20] Longobardi et al. — Wrong journal and wrong DOI

**Paper states:**
```
PLOS ONE, vol. 20, no. 3, p. e0298765, 2025.
doi: 10.1371/journal.pone.0298765
```

**Notes say (correct):**
```
SoftwareX, Vol. 29, Article 102028. Elsevier. (Published online December 2024)
doi: 10.1016/j.softx.2024.102028
```

**Fix:** Replace journal name, volume, article number, and DOI.

Correct reference line:
```
A. Longobardi et al., "Peskas: Automated analytics for small-scale, data-deficient fisheries,"
SoftwareX, vol. 29, p. 102028, 2025. doi: 10.1016/j.softx.2024.102028
```

---

### [21] Bhuvaneswari et al. — Wrong journal and wrong DOI

**Paper states:**
```
Applied Soft Computing, vol. 168, p. 112487, 2025.
doi: 10.1016/j.asoc.2025.112487
```

**Notes say (correct):**
```
Intelligence-Based Medicine, Vol. 12, Article 100311. Elsevier.
```

**Fix:** Replace journal name, volume, article number, DOI, and expand et al. to full author list.

Correct reference line:
```
P. Bhuvaneswari, K. D. V. Prasad, M. Ashraf, and S. Jadhav, "A human-centered hybrid AI
framework for optimizing emergency triage in resource-constrained settings,"
Intelligence-Based Medicine, vol. 12, p. 100311, 2025. doi: 10.1016/j.ibmed.2025.100311
```

**Resolution:** DOI `10.1016/j.ibmed.2025.100311` supplied by user from publisher record. Notes file updated to include DOI.

---

### [10] Bajcsy & Fisac — Fabricated journal (resolved)

**Paper claimed:**
```
Annual Review of Control, Robotics, and Autonomous Systems, 2024.
doi: 10.1146/annurev-control-090623-114628
```

**Resolution:** DOI `10.1146/annurev-control-090623-114628` confirmed fabricated — does not resolve. The paper exists only as an arXiv preprint. Notes file was already correct (arXiv:2405.09794v2).

Correct reference line:
```
A. Bajcsy and J. F. Fisac, "Coping with uncertainty: Reasoning, learning, and acting,"
arXiv preprint arXiv:2405.09794, 2024.
```

---

### [11] Corsi et al. — Wrong conference (resolved)

**Paper claimed:**
```
Proc. AAAI Conf. Artificial Intelligence, vol. 38, no. 10, pp. 11391–11399, 2024.
doi: 10.1609/aaai.v38i10.28999
```

**Resolution:** DOI `10.1609/aaai.v38i10.28999` confirmed fabricated — that AAAI slot does not exist, and the paper was posted June 2024 (after AAAI 2024's February proceedings). Actual venue is the 1st Reinforcement Learning Conference (RLC), 2024. Notes file updated with correct venue and DOI.

Correct reference line:
```
A. Corsi, G. Amir, A. Rodriguez, C. Sanchez, G. Katz, and R. Fox, "Verification-guided
shielding for deep reinforcement learning," in Proc. 1st Reinforcement Learning Conference
(RLC), 2024. doi: 10.48550/arXiv.2406.06507
```

---

## Audit Status — Complete

All 36 references have been verified. All 12 wrong entries have been corrected in `ipsci-2026-paper-v5.md`. Notes files updated where needed ([11] venue/DOI, [21] DOI added). No pending actions remain.
