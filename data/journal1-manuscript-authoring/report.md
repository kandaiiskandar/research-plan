# Journal 1 — Batch 8B-1: Evidence-Dense Core Authoring

**Date:** 2026-09-13 · **Branch:** `docs/journal1-manuscript-evidence-sync` · **HEAD:** `34b7b00`
**Manuscript:** `c1ef469e98101233` → **`a91ede5ff8518e46`** (928 → 1,246 lines)
**Sections authored:** 9, 10, 11, 12 · **Verification:** 76 PASS · 0 FAIL · 0 OPEN

---

## 1. Objective and scope as executed

Batch 8B was split on instruction; this sub-batch authored the four evidence-dense sections whose content derives directly from closed artefacts, and deferred everything requiring framing, interpretation or literature to 8B-2.

**Authored:** §9 Prototype Implementation, §10 Experimental Design, §11 Results (with Tables 8–12), §12 Ablation Study (Table 13), plus the quantitative-provenance, claim-evidence, E5-boundary and new-prose audits for those sections.

**Not authored, as instructed:** Abstract, Keywords, §§1–4, §§13–15, References. All retain their Batch 8A markers; eight remain in the file, which is exactly the count expected.

**Not performed:** no experiment, no replay, no re-run of any script, no scientific code change, no new citation, no closure of E5.

---

## 2. Baseline and authorities

The manuscript at `HEAD` hashed `c1ef469e98101233`, matching Batch 8A's closure exactly — no drift between batches. Authorities read in full before any prose was written: the evaluation specification, algorithm specification, Layer 3 prototype specification, research design, Appendix C, Batch 5 fidelity evidence, Batch 7A E5 evidence, the E3/E4 micro-repair, the canonical figure artefact, the prediction register, and all Batch 8A outputs.

**Every figure the task brief asserted was checked against repository authority rather than trusted.** All matched. Two were pursued further because they could not be found on first search: the RESOLUTION divergences `41.08%` and `45.56%` appear in neither the evaluation specification (which carries placeholders in that row) nor the manuscript. They were located in `data/c8/canonical-results-post-migration.txt` and independently corroborated at full precision in the prediction register — P24 = `41.0783`, P23 = `45.5602`, P22 = `4.4819`, P21 = `0.0000` — with `45.5602 − 41.0783 = 4.4819` reproducing exactly. Both are authoritative; nothing was taken from the prompt.

---

## 3. What was authored

### §9 Prototype Implementation

Seven subsections covering layer boundaries, the `ComponentStateTrace` interface, rule-set content, predicate semantics, the fidelity evaluation, hysteresis and deployment context. Tables 4 (rule register), 5 (F1–F3 results) and 6 (rule activation).

The section opens by separating what the theorems establish from what the fidelity evaluation establishes, and states plainly that the prototype has never been deployed, used by a fisher, or acted on by anyone.

### §10 Experimental Design

Table 7 presents the full evaluation matrix — P1–P4 FORMAL, F1–F3 IMPLEMENTATION_FIDELITY, E1–E4/E6 EMPIRICAL_TRACE, E5 PERFORMANCE and OPEN. Subsections cover conditions and comparator, replay protocol, fidelity protocol, performance protocol and statistical treatment. H1, H2 and H4 are not restored; H3 appears only as OPEN/UNSUPPORTED.

### §11 Results

Seven subsections in evidence-class order. Tables 8 and 9 give pairwise divergence for departure window and all hours under both configurations; a state-distribution table supports them; Table 10 gives `Δ_L2`; Table 11 gives the transition and hysteresis characterisation; Table 12 gives the development-machine reference benchmark.

Two structural identities were re-derived and hold exactly: `div(C1,C2)` equals the CAUTION rate (531/9,135 = 5.8128%; 266/5,935 = 4.4819%) and `div(C0,C1)` equals the UNSAFE rate (3,917/9,135 = 42.88%; 2,438/5,935 = 41.08%). These are reported as harness-consistency checks, not as findings.

### §12 Ablation Study

Title retained per Decision 4. Table 13 gives governance-level contributions. §12.5 states explicitly which ablations were **not** performed and why.

---

## 4. The four decisions, as applied

**Decision 1 — References.** No reference list was compiled in this sub-batch, and none was needed: §§9–12 introduce no numbered citation and no `[CITATION SUPPORT REQUIRED]` marker. Every attribution is to an in-repository artefact. Compilation remains authorised for 8B-2.

**Decision 2 — Section 3 standards.** Not engaged; §3 is out of scope for 8B-1.

**Decision 3 — R-SAFE-001.** Applied in full, and it materially changed what §§9 and 11 say.

> `R-SAFE-001 = DEFERRED`. `RS(SAFE)` is empty. All 32 SAFE episodes generated zero advisories. The only generated conclusion type is `Delay`. F1/F2 exercise a populated CAUTION rule set and the gate-off path, but **do not demonstrate fidelity of a populated SAFE rule set**, and the manuscript does not imply that `A_AI(SAFE) = {Go, Delay, DepartureTime, Duration}` was exercised.

This appears in §9.3 (Table 4 and the two numbered consequences), §9.5 (episode composition and Table 6), the claim-evidence audit (C8B1-06, C8B1-13) and the verification check `SAFE_rule_set_not_overclaimed`, which **PASSES** and which a negative-control mutation confirms would fail if the statement were removed. The §14 requirement is carried to 8B-2.

**Decision 4 — Structural mismatches.** Manuscript structure treated as authority: §12 keeps the title *Ablation Study*, no *Research Design* section was created, and `research-design.md` was used as source material for §10 only.

---

## 5. Evidence treatment

| Item | Treatment |
|---|---|
| **P1–P4** | Restated as formal results in §11.1 with an explicit statement that no empirical result proves them and that they establish nothing about physical safety or optimality |
| **F1–F3** | Reported in full in §9.5 with the interface-contract scope, the 244-count semantics, the 162/292 separation and the empty `RS(SAFE)`; §11.2 carries the status and cross-references |
| **E1** | Tables 8–9, both configurations, departure window and all hours, with state distributions and two structural identities |
| **E2** | Table 10; `Δ_L2` named the load-bearing result; explicitly not a safety, risk or accuracy claim |
| **E3** | Scope `{E1, E2, E6}`; the 1.3-point spread reported as the sensitivity result, not an interval |
| **E4** | Table 11, PRIMARY only; provenance chain `5416 → 5220 → 5201 → 3661` with the attribution warning; no resolution-insensitivity claim |
| **E5** | **OPEN.** §11.7 reports the development-machine reference in a separated subsection labelled reference-only at point of use |
| **E6** | Confirmation of an established structural equivalence, bounded by the disclosed modelling premise |
| **MacBook reference** | Reported; never called deployment, target-hardware, mobile, Android, real-time or production performance |
| **Android** | One occurrence, inside the sentence prohibiting the reading. `DEFERRED_MANDATORY` |
| **H3** | Two occurrences, both `H3 = X ms`, OPEN/UNSUPPORTED. No numeric substitution |

---

## 6. Audits

- **Quantitative provenance** — 69 quantities, each mapped to claim, metric, value, configuration, source artefact, source field, status and manuscript location. No orphan number.
- **Claim-evidence audit** — 39 material claims across §§9–12, each with authority, evidence status, allowed scope and prohibited interpretation.
- **E5 boundary audit** — every performance-adjacent term occurrence classified. 100% ALLOWED; 0 REVISED; 0 REMOVED. All five success criteria PASS.
- **Local overclaim audit** — the prohibited-phrase scan returns six hits (`risk reduction`, `safer`, `confidence interval`, `error bar`, `p-value`, `significance test`). **Every one sits inside a sentence that forbids the reading.** A sentence-level negation test was written for the inferential-statistics terms and passes with zero unnegated occurrences.
- **Parser test** — both CSVs parse identically under `csv.DictReader` and `pandas.read_csv`, with matching field lists and no empty required cells.

---

## 7. Verification — 76 PASS, 0 FAIL, 0 OPEN

**Four checks were rewritten during this batch because they asserted rather than tested.** `no_new_replay`, `no_scientific_code_change` and `only_manuscript_and_new_artefacts_changed` were hardcoded `True`; they now parse `git status` and fail on any change under `scripts/`, `governance/` or the frozen data directories. `no_p_values_invented` and `no_real_time_claim` short-circuited on an `or`; they now split the text into sentences and require every occurrence of the term to carry a negation.

Rewriting `only_manuscript_and_new_artefacts_changed` exposed a real defect in my own tooling twice over: a fixed-offset slice `l[3:]` on porcelain output ate the first character of the path, and stripping `stdout` removed the leading status column of the first line, yielding the phantom path `ublications/...`. Both were fixed in the parser rather than worked around in the assertion.

**Negative control.** Four prohibited mutations were injected into the manuscript in turn — overclaiming SAFE-episode coverage, substituting a numeric H3 threshold, asserting E4 resolution-insensitivity, and attributing Android performance — and the corresponding checks failed on each. The harness discriminates; it is not vacuously passing. The manuscript was restored and re-hashed to `a91ede5ff8518e46` afterwards.

**Integrity.** Batch 8B-1 changed exactly one existing file: the manuscript. Every protected file is hash-identical, verified against the hashes Batch 5 independently recorded rather than against a baseline taken by this batch. `evaluation-specification.md` is at `bfc6038516c998b3`, the post-micro-repair state, and is excluded from the Batch 5 comparison because Batch 5 recorded its pre-repair hash.

---

## 8. Findings recorded, not acted on

Three pre-existing inconsistencies were found in material this sub-batch may not modify. None is a disagreement between closed *evidence* sources, so no stop condition triggered.

1. **`evaluation-specification.md` carries stale F1–F3 and E5 status wording.** §7 still reads "all three are OPEN — deferred to Layer 3 build", §14 still says Layer 3 is "not fully implemented", and §17 OPEN-3 still lists fidelity evidence as blocked. All three predate Batch 5, which closed F1–F3 PASS — and the document's own §18 says so. The manuscript was authored against the CLOSED status. **A targeted authority-synchronisation repair is warranted and is the recommended next task.**
2. **Theorem numbering is inconsistent inside the protected §§5–8.** §5 states Theorem 5.1; §6 restates the same results as Theorems 6.1–6.3; §7 refers back to 5.1–5.3. §§9–12 use the §6 numbering throughout. Protected prose was not edited.
3. **Frozen historical artefacts contain superseded values** — the `22 kn` threshold in the narrative text of the c8 artefact, and its fixed-clock hysteresis description. No figure was drawn from those passages; only the canonical result tables in the same file were used.

Two forward obligations for 8B-2: §12.5 forward-references §14 for the ablation-scope limitations, and the SAFE-rule limitation must appear in §14 per Decision 3.

---

## 9. Status

```
SECTIONS_9_12 = AUTHORED
R_SAFE_001 = DEFERRED
P1–P4 = CLOSED
F1–F3 = CLOSED
E1–E4 = CLOSED · E6 = CLOSED
E3_SCOPE = {E1, E2, E6}
E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN
E5 = OPEN · E5_HARNESS = CLOSED · MACBOOK_REFERENCE = COMPLETE
E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY
H3 = OPEN/UNSUPPORTED
MANUSCRIPT_STATUS = SECTIONS_9_12_DRAFTED_WITH_OPEN_E5_DEPENDENCY
FINAL_REVIEWER_READY = false
```

**Closure:**

```
JOURNAL 1 MANUSCRIPT BATCH 8B-1 CLOSED —
EVIDENCE-DENSE IMPLEMENTATION, EVALUATION AND RESULTS SECTIONS AUTHORED
WITH E5 AND SAFE-RULE LIMITATIONS PRESERVED
```
