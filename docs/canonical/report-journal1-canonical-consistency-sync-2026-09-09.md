# Journal 1 Canonical Consistency Synchronisation Report

**Date:** 2026-09-10 (branch opened under the 2026-09-09 workstream)
**Branch:** `chore/journal1-canonical-consistency-sync`
**Type:** publication synchronisation — no new science
**Appendix C:** `abee8715e842e0d9` unchanged · **Conference manuscript:** `27b33b846ae327cb` unchanged

---

## 1. Scope

Audit and synchronise all maintained Journal 1 artefacts against the canonical specification. Journal 1 was deliberately deferred from the Canonical Repository Drift Synchronisation and is the downstream publication that must describe the canonical state without becoming a competing source of truth.

## 2. Branch and protected before-state

Branch created clean. All three authorities verified **before** work began: Appendix C `abee8715e842e0d9`, conference manuscript `27b33b846ae327cb`, frozen solar artefact `057c46a19d0e8ea7…`. Prediction register, canonical scripts and raw datasets hashed alongside.

## 3. Journal 1 file classification

Eight files (`journal1-file-classification.csv`):

| File | Classification |
|---|---|
| `submissions/v1-initial-submission/manuscript.md` | **ACTIVE-MAINTAINED — the maintained target** |
| `research-design.md` | ACTIVE-MAINTAINED |
| `README.md` | ACTIVE-MAINTAINED |
| `correspondence/notes.md` | SUPPORTING |
| `section-5-plan.md`, `section-6-plan.md` | HISTORICAL (document-level supersession banners) |
| `session-log.md` | HISTORICAL (dated session records) |
| `submissions/.DS_Store` | IRRELEVANT |

**J1-R6 resolved and not triggered.** Despite the `v1-initial-submission` path, this is **not** a submission snapshot: README names it *"Current working manuscript … aligned to Appendix C"*, its own header says *"active working manuscript"*, and the project status is **research-design phase with target submission early 2027**. Nothing has been submitted, so there is no immutable record to preserve and the maintained target is unambiguous. The directory name is the only thing suggesting otherwise.

## 4. Canonical authorities

Appendix C for the formal model; canonical scripts for executable semantics and thresholds; `canonical_figures.py` / `condition_comparison.py` for empirical state; the prediction register for prediction state; the conference manuscript as a publication-consistency reference. **No authority conflict — J1-R1 not triggered.**

## 5. Known deferred drift

The prior audit deferred four items: scalar `g_r(r)`, categorical rainfall, the 22 kn `g_w` boundary, and fixed-clock `g_t`.

**Two of the four were already clean.** The maintained manuscript carries `g_w` at **21.6 / 27.0 kn** and `g_t` as **Model B** with a header banner recording SDR-001; it contains no active fixed clock and zero occurrences of *"Meeus"*. The categorical rainfall model survives only inside the two section plans, both of which carry document-level supersession banners. **Only the `g_r` drift was live in maintained prose** — and it ran deeper than the deferral note implied.

## 6. Additional drift discovered

23 findings classified (`journal1-canonical-audit.csv`): **ACTIVE-CANONICAL-DRIFT 8** (one an omission) · ACTIVE-CORRECT 10 · HISTORICAL 3 · OPEN 1 · IRRELEVANT 1.

Three were not in the deferral list:

- **The novelty overclaim.** *"Prior governance architectures implement only a participation gate G(S)"* — the same universal claim corrected in the conference manuscript, whose own TABLE II lists five graduated architectures.
- **The condition-label collision** (§16 below), which is the most consequential finding in this task.
- **A missing type declaration**: the paper used `g_r` throughout without ever declaring its input type.

## 7. Formal-model synchronisation

`g_r` was repaired at **five loci**: the Table 1 threshold row, the Section 5 `f(E)` definition, the Theorem 6.1 totality case, and both `f(E)` restatements inside the proof.

The totality case carried exactly the defect Appendix C itself had before its own synchronisation — the rate partition asserted as exhaustive over `g_r`'s domain, with the storm route bolted on as *"where available"*. It is now a two-case proof over κ ∈ {0, 1}, disjoint and covering.

## 8. Rainfall / κ synchronisation

**New Definition 5.2a** supplies what the paper never declared: `X_r = ℝ≥0 × K`, `g_r : ℝ≥0 × K → S`, and `κ = χ(c)` with `χ(c) = 1 iff c ∈ {95, 96, 99}`. It states the three properties that matter formally — **c is not the classifier input** and κ is computed rather than measured; **χ is total and never returns ⊥**, so an absent code yields κ = 0 rather than a fault, a default that is **non-escalating and explicitly not fail-safe**, with the rate remaining the required coordinate; and **κ is escalation-only**, so reported `g_r` figures are lower bounds where the feed is incomplete. κ is stated **not** to be a member of `D`.

## 9. Wind synchronisation

**No repair needed.** 21.6 / 27.0 already canonical, with MET onsets shown at source value. No *"never fires"* claim anywhere in maintained prose; the activation-versus-binding distinction is not misstated because the paper's drafted sections make no wind-frequency claim.

## 10. Time / solar synchronisation

**No repair needed.** `g_t` is Model B — SAFE iff sunrise ≤ t < sunset, no CAUTION, UNSAFE on required clock/date/solar failure — with COLREGs Rule 20(b) cited as a boundary and explicitly *"not a mandate for AI abstention"*. Solar provenance uses the bounded NOAA wording with two disclosed simplifications, the frozen table, and the canonical site configuration.

## 11. Observation / exclusion synchronisation

**No repair needed.** `Obs_i = (X_i × 𝕋) ∪ {⊥}`, `ρ_{D,τ}`, `F_{D,τ} = f ∘ ρ`, `t ∉ D`, exclusions resolved before faults, and `D = {m}` for the retrospective replay are all present and correct.

## 12. Governance / novelty synchronisation

The governance-pair paragraph now concedes that graduated governance exists and scopes the binary claim to the axis that matters: **what those architectures graduate is supervisory intensity, execution deferral or an agent's action space; on the recommendation set offered to a human decision-maker, the control reduces to a participation gate.**

Two adjacent statements were checked and **retained**: *"A binary governance architecture implements only G"* and *"A binary governance architecture, having no Level 2 mechanism, cannot express this"* are definitional statements about binary architectures, not universal claims about the field.

Safety Dominance already uses **"admissible scope"**; the phrase *"warranted scope"* does not occur. `UNSAFE` is defined as *"AI advisory participation is unavailable"*, and `A_AI(CAUTION) = {Go, Delay}` is labelled a **conservative architecture policy**.

## 13. Empirical-result synchronisation

Journal 1's drafted sections (1–6) are formal and theoretical; the empirical sections remain plans. The only canonical figure quoted is **3,661 transitions**, which is correct. **No stale headline, no stale binding rate, no stale component share.** Nothing to repair.

## 14. Prediction-state synchronisation

Journal 1 makes no prediction-state claim. Register verified unchanged at **24 · 15 CONFIRMED / 9 REFUTED**, P01 REFUTED, P16 CONFIRMED, P09 **3,661**, P20 **1,529**.

## 15. Data-provenance synchronisation

Journal 1's drafted sections do not yet state data sources, so no land-cell configuration is presented as current. Nothing to repair; the canonical path is recorded in `data-provenance-verification.json` for the empirical sections when they are written.

## 16. Reportability guidance — the most consequential finding

Journal 1's evaluation table reads **C1 Ungated · C2 Binary-gated · C3 Graduated (proposed)**. The canonical harness uses a *four*-condition scheme in which **every one of those letters means something else**:

| Canonical | Meaning | Journal 1 |
|---|---|---|
| C0 | Ungated | C1 |
| C1 | Binary-gated | C2 |
| **C2** | **Proposed architecture** | C3 |
| C3 | Flehmig traffic-light | *(absent)* |

**Canonical C2 is the proposed architecture; Journal 1's C2 is the binary baseline — a direct inversion of the single most important condition.** Journal 1 cites `evaluation-design-rq4.md` and will draw on canonical artefacts, so any figure carried across without translation inverts its meaning. This is the failure mode the branch has been chasing all along, in its most dangerous form: not a stale number or a stale instruction, but **a stale symbol that silently renames the result.**

**Repaired by mapping, not renaming.** A mapping table with canonical reference values was added to the manuscript and cross-referenced from `research-design.md`. Renaming would ripple into H1–H4 and both section plans, and would itself be an evaluation-design change.

## 17. Epistemic-boundary repairs

None required. The manuscript already distinguishes characterisation from validation: Layer 3 is *"specified as a production rule engine; runtime fidelity is not yet demonstrated"*, `A_AI(CAUTION)` is a policy rather than a derived optimum, and the COLREG/abstention boundary is explicit.

## 18. Threats-to-validity alignment

The drafted sections do not yet contain a threats section; it belongs to the planned empirical chapters. The canonical threat set — MET-versus-model measurement mismatch, absent marine-warning archive, unexercised κ route, hourly resolution, wave-resolution sensitivity, cell separation, domain-specific instantiation, Layer 3 unbuilt — is recorded in the verification artefacts for when that section is written. **Recorded, not written: writing it now would be new content, not synchronisation.**

## 19. Historical and snapshot material retained

Both section plans retained in full under their existing 2026-09-09 banners, including the categorical `g_r`, the 22 kn `g_w` row and `g_v(v)` in the superseded `f(E)`. `session-log.md` retained unchanged, including its `g_v` and 1.5 m references, as dated records of what was believed on those days. **Nothing was rewritten to achieve zero search hits.**

## 20. Files changed

Two, both mapped in `journal1-change-map.csv`:

- `submissions/v1-initial-submission/manuscript.md` — J1-01…J1-07, J1-09
- `research-design.md` — J1-08

## 21. Files intentionally unchanged

Appendix C, the conference manuscript, the prediction register, the frozen solar artefact, all raw datasets, all canonical scripts, both section plans, the session log, README and correspondence notes.

## 22–24. Invariance and protected after-state

Level 2 **5.81% / 4.48%** · `g_o` **98.71% / 97.66%** · `g_t` **86.82% / 90.19%** · `g_r` **1.48% / 2.70%** and **0.20% / 0.26%** · daylight UNSAFE **1,262 / 455**. Register **24 · 15 / 9**. Appendix C, conference manuscript and solar artefact byte-identical; **no authority changed**; no unexpected changes.

## 25. Parser verification

Three CSVs, both `csv.DictReader` and `pandas.read_csv`, strict field-count: **PASS**.

## 26. Open and deferred items

1. **No Flehmig-style C3 baseline in Journal 1's design.** The canonical C3 is what converts the novelty claim from assertion to measurement (0.00% divergence). Adding it is an evaluation-design decision — **J1-R2, recorded not made.**
2. **Threats-to-validity section unwritten** — belongs to the planned empirical chapters.
3. **Condition labels remain non-canonical**, now mapped. Renaming is a separate decision.

## 27. Stop-condition assessment

| | Condition | Triggered |
|---|---|---|
| J1-R1 | Authority conflict | **NO** |
| J1-R2 | New science required | **Recorded** — missing baseline, threats section |
| J1-R3 | Canonical empirical conflict | **NO** |
| J1-R4 | Protected publication change | **NO** |
| J1-R5 | External evidence required | **NO** — no claim needed new support |
| J1-R6 | Maintained target unresolved | **NO** — resolved from two explicit conventions |

## 28. Final decision

All closure criteria pass.

**What Journal 1 adds to the branch's pattern.** Every earlier residue was a stale *value*, *assertion* or *instruction*. Journal 1 contributed a fourth kind: **a stale symbol.** Its condition labels are individually reasonable and internally consistent — nothing in the document is false — yet placed beside canonical artefacts they invert the meaning of the paper's central comparison. That defect is invisible to any check performed within one document, which is precisely why a downstream publication has to be audited *against* the canonical state rather than for internal coherence.

---

*Artefacts:* `data/journal1-canonical-consistency-sync/` — `integrity-before.json`, `integrity-after.json`, `journal1-file-classification.csv`, `journal1-canonical-audit.csv`, `journal1-change-map.csv`, `formal-model-verification.json`, `empirical-verification.json`, `prediction-verification.json`, `data-provenance-verification.json`, `assertion-residue-verification.json`, `parser-test.json`, `closure.json`, `build.py`.
