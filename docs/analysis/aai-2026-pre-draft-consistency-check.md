# AAI 2026 — Final Pre-Draft Consistency Check

**Date:** 2026-09-24
**Mode:** Consistency audit only. No drafting, no discovery, no redesign. Research chain not reopened.
**Method:** mechanical verification across the patched documents (term scans, value-presence checks, scoping counts) plus logical audit of each chain transition. Findings are anchored to line-level evidence.

---

## 1. Audit status

✅ **The package is internally consistent and sufficiently locked to begin drafting.**

**Two defects found, neither a blocker under the stated blocker rule:**

| # | Defect | Class |
|---|---|---|
| D1 | Patched chain §3 prior-art table labels a row *"Pre-inference / preemptive restriction of the action set"*. **"Pre-inference" is prohibited by Citation Lock v2 §9**, and it mischaracterises Alshiekh, who restrict before **action selection**, not before inference | 🟠 Wording defect in a concession label — fix at drafting |
| D2 | Citation Lock v2 §15 pointer to *"§21 attack 16"* | 🟢 Documentation correction — non-substantive (Check J) |

**One tension requiring an explicit drafting constraint** — see §6, A4.

---

## 2. Research-chain transition audit

| Transition | Verdict |
|---|---|
| Problem → Gap B | **PASS.** The problem states that a declared level constrains behaviour only if it changes the permitted action set, and that neither that property nor its binding frequency follows from the specification. Gap B is the empirical half of exactly that. |
| Gap B → Primary RQ | **PASS** — see A1 |
| RQ → Measured object | **PASS.** RQ asks how often an intermediate advisory-scope level changes the admissible recommendation set; the measured object is `A_AI(S)`, the admissible recommendation set. |
| Measured object → Comparator | **PASS** — see A3 |
| Comparator → Metric | **PASS.** Δ_L2 = (C0↔C2) − (C0↔C1), cross-checked by direct pairwise C1↔C2 = 5.81%. |
| Metric → Evidence | **PASS.** 43,848 / 28,501 records; 9,135 / 5,935 window hours; all values verified present. |
| Evidence → Contribution | **PASS** — see A5 |
| Contribution → Central claim | **PASS** — see A6 |

### A1 — Does the RQ directly answer Gap B? **PASS**
Gap B: *"no empirical characterisation… of how often an intermediate advisory-scope governance level changes the admissible recommendation set relative to a participation-only gate."* RQ1: *"how often does an intermediate advisory-scope governance level change the admissible recommendation set relative to a participation-only gate, and how sensitive is that frequency…"* The RQ is the gap restated as a question, plus a sensitivity clause the gap does not require. The addition narrows rather than widens.

### A2 — Does Δ_L2 measure what RQ1 asks? **PASS, with the semantics stated**
Δ_L2 counts departure-window hours in which C2 admits a strictly smaller recommendation set than C1. That is literally "how often the intermediate level changes the admissible set relative to a participation-only gate." The identity in A4 explains what that count turns out to be; it does not change what is counted.

### A3 — Does C1 vs C2 isolate the intermediate contraction? **PASS**
C1 and C2 are identical at SAFE (FULL) and at UNSAFE (∅) and differ only at CAUTION (FULL vs {Go, Delay}). Any divergence is therefore attributable to that one cell. This is the strict form of "differing only at that level" required by the gap.

### A4 — Does Δ_L2 ≡ P(S = CAUTION) contradict the isolation claim? **PASS — but a drafting constraint is required**

**No contradiction.** The subtraction is a valid marginal isolation; the identity is a fact about what the isolated quantity evaluates to, given that C1 and C2 differ *totally* at CAUTION (FULL versus any strict subset). Both statements are true simultaneously.

🔴 **But there is a tension the manuscript must handle explicitly.** Because the isolated quantity equals the CAUTION base rate, it is invariant to *how much* the set contracts — only to *whether* it contracts. A reviewer may therefore ask: **if Δ_L2 ≡ P(S = CAUTION), why was the comparator ladder needed at all? Could you not simply count CAUTION hours?**

**The answer is available and must be given:** the ladder additionally yields the C0↔C1 = 42.88% and C0↔C2 = 48.69% decomposition — the Level-1-alone versus Levels-1-and-2 split — which counting CAUTION hours does not provide; and it *establishes* that the identity holds rather than assuming it.

🔒 **DRAFTING CONSTRAINT (new, from this audit):** do **not** write or imply that the comparator ladder was *necessary* to obtain 5.81%. State that the ladder yields the decomposition and establishes the identity; state that the identity then explains why the isolated value equals the intermediate-state base rate.

### A5 — Is the contribution narrower than the gap and fully supported? **PASS**
The contribution claims four things (isolation, identity interpretation, contraction-specific threshold sensitivity, component attribution), all scoped to one site, one vessel class, under a declared exclusion, as a lower bound. The gap is broader than the contribution in every dimension. Every contribution component maps to verified evidence in §§11–12 of the chain.

### A6 — Does the central claim stay inside the evidence? **PASS**
Every quantity in the claim was verified present in the patched chain: 5.81%, envelope 5.67–9.56%, 97.6% single-component attribution, 1.96% and 1.26% vessel classes, lower-bound status. The claim contains no outcome, safety, quality or optimality term.

---

## 3. Prior-art / contribution boundary audit

**Confirmed: no contribution is claimed for any of the seven established techniques.** Verified by term scan across both patched documents — every occurrence of a novelty term sits inside a prohibition list or a status label, none inside a claim.

| Technique | Where conceded |
|---|---|
| Runtime restriction | Chain §3; architecture §5 Cluster B |
| Graduated governance levels | Chain §3; Cluster D (Aarab) |
| FULL → RESTRICTED → NONE topology | Chain §13 ledger; Cluster D |
| Activation-frequency measurement *generally* | Chain §13 row 12 split; Cluster D (Kim et al.) |
| Threshold-sensitivity analysis *generally* | Chain §13 row 12 split; Cluster D |
| Comparator / ablation methodology *generally* | Chain §13 row 6 = METHOD; Cluster D (Miller) |
| Operational governance measurement *generally* | Citation Lock v2 §7 row 7 |

**Contribution-bearing assembly is represented consistently** as the four locked items across chain §13 (rows 6b, 11, 12-split, 13), Citation Lock v2 §7 (rows 4b, 5b, 8, 9, 10) and architecture §9/§14.

🔴 **One sentence flagged.** Chain §3 line 81: *"Pre-inference / preemptive restriction of the action set"*. It does not claim novelty — it concedes — but the label itself is a prohibited term and misdescribes Alshiekh. **Correct at drafting to "Preemptive restriction of the available action set (before the agent selects)".** No other sentence in either document accidentally implies generic technique novelty.

---

## 4. Near-neighbour consistency audit

Cross-checked Citation Lock v2 §§4–6, patched chain §21 row 13, and architecture §5 Cluster D.

| Paper | Required distinction | Consistent across all three? |
|---|---|---|
| **Aarab** | Graduated active contraction exists | ✅ |
| | No participation-only comparator | ✅ |
| | Directive-frequency simulation under permissive mode | ✅ — all three state it, and architecture Cluster D carries an explicit "do NOT imply" instruction |
| **Miller** | Governance-configuration ablation exists | ✅ |
| | Configurations are enforcement operators, not risk levels | ✅ |
| | No intermediate contraction-binding frequency | ✅ |
| **Kim et al.** | Gray-Zone burden + parameter sensitivity exist | ✅ |
| | Gray Zone = mandatory human review / abstention | ✅ |
| | Not active recommendation-scope contraction | ✅ |
| | No participation-only comparator | ✅ |

**No wording found that makes any distinction weaker or stronger than the verified evidence.** The Aarab limitation is stated identically in all three documents and never overstated into "Aarab measured graduated-mode frequency".

---

## 5. Gap-language audit

**PASS.** Scoping phrase *"within the reviewed literature"* appears **5 times** in the patched chain, **4 times** in the patched architecture and **6 times** in Citation Lock v2 — attached to every absence statement.

**No unscoped absence claim survives.** All hits for *novel · first study · first measurement · unique · unprecedented · never studied · no one has measured · no prior work exists* fall inside prohibition lists. The single apparent exception (chain line 113) is a **disclaimer**: *"does not claim that no one has measured anything adjacent."*

**Planned Related Work closing sentence** — *"Within the reviewed literature, these works do not combine active intermediate scope contraction, a participation-only comparator, marginal isolation, and binding-frequency measurement"* — is scoped, enumerates only the four verified elements, and does not exceed the five-source audit. ✅ **Does not exceed verified scope.**

---

## 6. Metric-semantics audit

| Requirement | Verdict | Evidence |
|---|---|---|
| 1. Appears in METHOD before results | ✅ **PASS** | Chain §19: *"MUST INCLUDE — in the method, before results"*; architecture §10 row "Method §III — the identity, before any number"; final block: *"Section III… before any numerical result"* |
| 2. Treated as metric interpretation, not empirical discovery | ✅ **PASS** | Chain §7: *"a metric-interpretation proposition stated in the method, before results… not a result, not a finding"* |
| 3. Invariance to the content of A_AI(CAUTION) explained | ✅ **PASS** | Chain §7 and §10: invariant for any strict subset of FULL |
| 4. 5.81% does not validate {Go, Delay}, correctness, optimality, safety, usefulness | ✅ **PASS** | Chain §14 non-claims; §17 matrix marks all PROHIBITED; attack row 9 makes the concession costless |
| 5. C1↔C2 measures how often the contraction binds; the identity explains why | ✅ **PASS** | Chain §10 and §9 results narrative R2–R3 |

**Overall: PASS**, subject to the A4 drafting constraint above.

---

## 7. Results-and-qualification audit

**PASS.** The architecture forces the headline to travel with its qualifications structurally, not by instruction alone: Table III is a **single two-panel float** carrying the headline and every qualification together, so they cannot be separated in layout.

| Required accompaniment | Present |
|---|---|
| Envelope 5.67–9.56% / 4.26–6.64% | ✅ MUST INCLUDE — *"the envelope, not the point figure alone"* |
| Alternative reading 9.22% | ✅ Table III footnote ‡ |
| Wave ±0.25 m → 2.54–14.75% | ✅ Table III Panel B |
| `g_o` 518/531 = 97.6% | ✅ MUST INCLUDE |
| Vessel class 1.96% / 1.26% (0.66% / 0.37%) | ✅ MUST INCLUDE — it is in the central claim |
| Daylight denominator 9.59% / 7.40% | ✅ USE IF SPACE + Table III row |
| Lower-bound status from excluded `g_m` | ✅ MUST INCLUDE |

**Role classification verified correct:**

| Item | Classification | Confirmed |
|---|---|---|
| Denominator dependence | Measurement sensitivity / robustness disclosure | ✅ chain §13 row 15 |
| Lower-bound status | Measurement qualification / limitation handling | ✅ chain §13 row 17 |
| Vessel-class dependence | Robustness disclosure | ✅ chain §13 row 14 |
| Component attribution | **Contribution-bearing evidence** | ✅ chain §13 row 13, PRIMARY |

---

## 8. Component epistemic-status audit

**PASS.** The decomposition is present in **three** places in the patched chain (§0 I-1, §12 attribution table, §17 claim matrix) and the collapsed form is explicitly forbidden.

| Component | Locked status | Verified |
|---|---|---|
| `g_o` | Empirically dominant, 518/531 = 97.6% | ✅ |
| `g_r` | Empirically binds 13/531 = 2.4% | ✅ |
| `g_w` | **Empirical negative** — 0 CAUTION binding; two activations in 43,848 h, decisive in neither | ✅ |
| `g_t` | **Definitional zero** — emits no CAUTION by construction | ✅ |
| `g_m` | **Structurally excluded** — no historical archive, D = {m} | ✅ |

🔒 The phrase *"three of five components never bind"* appears **only inside prohibitions** (chain §0 I-1 and §12): *"the paper may claim one empirical non-binding component (`g_w`), not three"* and *"Not 'three of five never bind.'"* No usable instance survives.

---

## 9. IPoSCI / originality audit

**PASS on all seven requirements.**

| Requirement | Verified |
|---|---|
| Represented as ACCEPTED, NOT CONFIRMED PUBLISHED | ✅ chain §0 I-6, §18; Citation Lock v2 §10 |
| No bibliography entry | ✅ removed; not renumbered |
| No "previously published" | ✅ only occurrence is the prohibition itself |
| No "previously reported" | ✅ chain §0: *"The figures are **not** labelled 'previously reported'"* |
| No proceedings claim | ✅ |
| 5.81% / 4.48% not claimed as newly discovered for AAI | ✅ architecture §10: reported as outputs of the evaluation described, *"no statement about when they were first computed"* |
| Substantive differentiation enforced internally | ✅ architecture §11 control, marked **PRIMARY safeguard** |
| Status rechecked before submission | ✅ logged as the single 🔴 High item |

---

## 10. Citation-control audit

| Item | Verdict |
|---|---|
| Aarab = single author | ✅ Verified from Crossref + primary text; flagged in three places |
| Miller = single author | ✅ Verified from MDPI + primary text |
| Kim et al. = seven authors | ✅ Verified from Nature + primary text |
| *"Aarab et al."* / *"Miller et al."* survive as errors? | ✅ **NO** — every occurrence is inside a prohibition |
| Alshiekh = preemptive / before the agent selects | ✅ Citation Lock v2 §9 |
| "pre-inference" never used | 🟠 **D1** — survives as a concession-table row label in chain §3. Prohibited elsewhere in all three documents |
| ASTM = title/scope only | ✅ no clause-level claim anywhere |
| NIST does not "require" our criterion | ✅ Citation Lock v2 §A.1 narrowed wording locked |
| Manski not required | ✅ removed |
| TSO-C151c dropped | ✅ |
| DSA-SafetyBench dropped | ✅ |
| A⁴-Gov optional / drop | ✅ |

**Remaining bibliographic blocker:** the **AI-governance SLR author list** (reference [1]) is still not captured. 🔎 **Checked the supplied corpus** — the note `notes/AI governance- a systematic literature review.md` exists in the project corpus, so this is resolvable from material already held; it was not resolved here because this is an audit task. **Not a blocker** under the stated rule (it is a lookup, not a repair).

---

## 11. Documentation pointer correction

**DOCUMENTATION CORRECTION — NON-SUBSTANTIVE.**

Citation Lock v2 §15 refers to *"§21 attack 16"* of the research chain. No such row existed; the chain's attack table had 12 rows. The precision patch created **attack row 13**. The intended pointer is therefore **"research-chain reviewer attack row 13"**. No substantive evidence in the lock changes. Recorded, not applied.

---

## 12. Six-page feasibility

**Feasible — but with effectively zero margin.**

| Element | Columns |
|---|---|
| Body 3,690 words @ ~480/col | 7.69 |
| Title + author block | 0.35 |
| Abstract + index terms | 0.45 |
| Tables I + II + III | 1.45 |
| Figure 1 | 0.55 |
| References (17–20, down from 22) | **0.95–1.10** |
| Heading / float whitespace | 0.40 |
| **Total** | **11.84 – 11.99 of 12.00** |

⚠️ **The reduced reference count is what makes this fit.** At 22 references the layout would exceed 12 columns. Holding to 17–20 is now a **layout requirement**, not just a discipline.

**If compression is needed, take it from one place only:**
- **Section V (Results and Discussion), ~910 words → remove ~60–80 words.** Specifically the closing-discussion second move (the practice consequence), leaving move (i) — the C3-versus-C2 contrast. Table III carries the numbers, so prose reduction there costs no evidence.

🔒 Do not compress Related Work below 520 words; Cluster D is the novelty-exposure control. Do not cut any Table III row or the Figure 1 envelope band.

---

## 13. Remaining blockers

**NONE.**

| Item | Class | Why not a blocker |
|---|---|---|
| D1 "pre-inference" concession label | Wording | Fixable in one line at drafting; concedes rather than claims |
| D2 Citation Lock pointer | Documentation | Explicitly excluded by the blocker rule |
| AI-governance SLR author list | Lookup | Source already in corpus; explicitly excluded |
| IPoSCI status recheck | Pre-submission | Explicitly excluded |
| ASTM full text unavailable | Citation scope | Only title/scope used; explicitly excluded |
| Six-page margin ~0.01–0.16 col | Layout | Feasible; compression target identified |

**No blocker condition is met:** Problem → Gap → RQ aligns; Δ_L2 answers RQ1; the contribution is narrower than the evidence; near-neighbour evidence does not invalidate Gap B (v2 audit); no experimental values conflict; the six-page architecture is feasible without deleting a required claim; the publication treatment creates no ethical or submission conflict.

---

## 14. Binding manuscript drafting contract

🔒 **Guardrail for all subsequent drafting agents. 20 items.**

### MUST DO
1. Lead with the governance-measurement problem, the criterion and the measurement — **never** with the architecture.
2. Concede all mechanisms on page 1: ASTM F3269, Alshiekh, TCAS II (AC 20-151C), Parasuraman et al. Close that paragraph with *"This paper contributes none of these mechanisms."*
3. Include Related Work **Cluster D** conceding Aarab, Miller and Kim et al., closing with the scoped residue sentence.
4. State **Δ_L2 ≡ P(S = CAUTION) in the Method, before any number**, with its invariance consequence.
5. State the criterion as a **criterion**, never as a theorem, proposition or research question.
6. Label **C1 ↔ C3 = 0.00% as entailed** by the configurations and as a conformance check.

### MUST NOT DO
7. Never present runtime restriction, graduated levels, the FULL → RESTRICTED → NONE topology, activation-frequency measurement, threshold-sensitivity analysis, comparator/ablation methodology or operational governance measurement as a contribution.
8. Never use *novel · first · unique · unprecedented · never studied · no one has measured · no prior work exists*.
9. Never write *"Aarab et al."* or *"Miller et al."* — both are single-author.
10. Never use *"pre-inference"*; use *"preemptive"* or *"before the agent selects an action"*.
11. Never imply Aarab measured graduated-mode activation frequency, that Miller's projection improves compliance (0.8317 vs 0.0333 — it is worse), or that Kim et al. share the Δ_L2 estimand.
12. 🔴 **Never imply the comparator ladder was necessary to obtain 5.81%** (A4).
13. Never write *"three of five components never bind"* without immediate epistemic decomposition.
14. Never cite the IPoSCI abstract or call anything *previously published / previously reported*.

### MUST REPORT
15. The headline **never alone**: 5.81% / 4.48% always with the 5.67–9.56% envelope, wave dominance, `g_o` 97.6%, and the vessel-class figures.
16. The component attribution decomposed by epistemic status: `g_o` dominant · `g_r` 13/531 · `g_w` empirical negative · `g_t` definitional · `g_m` excluded.

### MUST QUALIFY
17. Every absence statement with *"within the reviewed literature"*.
18. Denominator dependence and lower-bound status as **qualifications**; vessel-class dependence as a **robustness disclosure** — never as contributions.
19. Human authority in the **specification register only** (*"the architecture does not automate the departure decision"*) — never as meaningful human control, human-centred, oversight effectiveness, trust or acceptance.

### MUST CITE
20. Aarab 2026 (DOI 10.1109/ICHCAI70183.2026.11607581) · Miller 2026 (DOI 10.3390/make8050125) · Kim et al. 2026 (DOI 10.1038/s41746-026-02450-7) — all three in Cluster D, with their verified limits stated.

---

## 15. Final verdict

The chain holds end to end. Every transition passes. The contribution is narrower than the gap, the central claim sits inside verified evidence, the near-neighbours are conceded consistently across three documents, all absence claims are scoped, and every experimental value is present and unaltered. Two defects were found; both are wording or documentation matters explicitly excluded from the blocker rule, and both are recorded with their fixes.

One new drafting constraint emerged from this audit (A4) and is carried into the contract as item 12.

**PRE-DRAFT STATUS: READY FOR MANUSCRIPT DRAFTING**

---

*Consistency audit complete. No manuscript prose drafted. No document edited by this task — D1 and D2 are recorded for correction during drafting.*
