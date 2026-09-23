# AMICT Source Corpus Validation — Task Readiness Analysis

**Date:** 2026-09-14
**Analyses:** `docs/tasks/AMICT NOVELTY CORPUS VALIDATION AND SOURCE INTEGRATION.md`
**Status:** PRE-EXECUTION ANALYSIS ONLY. No task artefact created. `source-validation-report.md` does not exist. No note written, no `citation-notes-map.md` entry added, no audit artefact touched.
**Companion:** [`amict-conference-rebuild-readiness-analysis.md`](amict-conference-rebuild-readiness-analysis.md)

---

## 1. What the task is

A **source-hygiene gate** between the completed novelty audit and the contribution freeze. It validates the six external works the audit relied on, replaces weak ones, and integrates the survivors into the existing `notes/` system so that manuscript-facing citations resolve through `[[notes]]` like every other corpus reference.

It is correctly sequenced. The novelty audit reached `STOP_MATERIAL_EQUIVALENCE_FOUND` on the strength of six sources that were **fetched but never validated** — no publication-status check, no DOI verification, no test of whether the documents were current. Freezing contributions on that basis would put the paper's central repositioning on unverified ground. This task closes that exposure before anything is frozen.

The task also does something the audit did not: it imposes a **2023+ preference** on manuscript-facing research literature, with explicit escape hatches for foundational and authorised sources. That is a stricter standard than the audit worked to, and it is the right one for a Related Work section that a reviewer will scan for currency.

---

## 2. Pre-validation of the four decisive items

Four checks were run against issuing authorities before writing this analysis, because each could have changed the task's shape.

### 2.1 AC 20-151A is CANCELLED — and the finding survives anyway

The FAA advisory-circular index labels **AC 20-151, AC 20-151A and AC 20-151B all as "(Cancelled)"**. The current revision is **AC 20-151C, issued 21 July 2017**, which cancels AC 20-151B dated 18 March 2014.

The novelty audit cited the cancelled 20-151A. That is a real defect and exactly what Source Area 1 exists to catch.

**But the mechanism claim survives intact.** AC 20-151C Table 2 (System Inhibits) carries the identical schedule:

| Advisory type | Climbing | Descending |
|---|---|---|
| Increase Descent RA | inhibited below 1650 ft AGL | inhibited below 1450 ft AGL |
| Descend RA | inhibited below 1200 ft AGL | inhibited below 1000 ft AGL |
| All RAs (reverts to TA-only) | inhibited below 1100 ft AGL | inhibited below 900 ft AGL |
| TA voice messages | inhibited below 600 ft AGL | inhibited below 400 ft AGL |

Plus performance-based inhibition of Climb and Increase Climb RAs, evaluated per aircraft against weight, altitude, temperature, flap and gear configuration.

Every figure quoted in `novelty-audit-report.md` §2 is confirmed by the current document. **Stop condition 1 does not fire.** The action is a citation swap, not a re-examination of the finding — and §16.I ("the TCAS precedent has not been weakened or hidden merely to restore novelty") passes trivially, since validation strengthened it.

One upgrade worth considering beyond the task's ask: the inhibition logic originates in **RTCA DO-185B (TCAS II MOPS)** and **ICAO Annex 10 Volume IV**, which sit higher in the task's own source hierarchy as standards/certification material. AC 20-151C is the accessible authority; the standards are the primary one.

**Classification:** AC 20-151C → `ACCEPT_AUTHORISED`, `AUTHORISED_SOURCE = TRUE`. The 2017 date is not a problem — the date rule exempts authorised sources. AC 20-151A should be recorded as superseded and not cited.

### 2.2 ACAS X — the source exists, the author's name in the task is misspelled

**Confirmed:** *Formally Verified Next-Generation Airborne Collision Avoidance Games in ACAS X*, **Cleaveland, Mitsch & Platzer**, *ACM Transactions on Embedded Computing Systems*, vol. 22, **DOI 10.1145/3544970**. Peer-reviewed ACM journal record. arXiv:2106.02030 is the 2021 preprint of the same work; the ACM version is the citable one.

**The task writes "Cleveland". The correct spelling is "Cleaveland."** Worth fixing before it propagates into a note filename and a reference list.

Two items to verify against the ACM record during execution: the exact issue and article number, and whether the publication year is 2023 as the task states (dblp places the volume in 2023; the DOI record settles it).

This is a genuine improvement on the audit, which cited Jeannin et al.'s earlier STTT work. **Stop condition 3 does not fire.** The narrower comparison the task specifies — *formal verification of state-conditioned advisory logic has precedent* — is exactly what this source supports, and no more.

### 2.3 Bernabei & Costantino (2024) — confirmed and well-chosen

**Confirmed:** *Adaptive automation: Status of research and future challenges*, **Robotics and Computer-Integrated Manufacturing**, vol. 88, article **102724**, 2024, **DOI 10.1016/j.rcim.2024.102724**. Peer-reviewed Elsevier journal. Satisfies `PEER_REVIEWED_2023_PLUS`.

The mechanism check the task demands still has to be done on the text: the source must establish what adaptive automation actually governs (level of automation, task allocation, operator state) and must **not** be cited for advisory-scope restriction. Based on the title and venue this is a status-of-research review, which is the right shape for the claim — but the claim must come from the paper, not from the title.

It would replace the USAARL technical report as the primary Area 4 source, with the report retained as supplementary if useful. That matches the task's stated preference.

### 2.4 FDA CDS guidance was revised in January 2026 — this is the live risk

The audit cited the **September 2022** final guidance. That is no longer current: **the FDA revised the Clinical Decision Support Software guidance in January 2026**, in a deregulatory direction.

This matters because the audit's N-13 entry rests specifically on **Criterion 3** — the distinction between software offering "a list of options" and software offering "a specific preventive, diagnostic or treatment output or directive". If the revision narrowed, restructured or removed that distinction, the corroborating point weakens.

The exposure is bounded: N-13 is **supportive, not load-bearing**. It corroborates that recommendation *type* is treated as a governance-relevant variable; it is not evidence for the TCAS material equivalence and does not carry the repositioning. But it must be re-read rather than assumed, and if Criterion 3 changed, §10 requires an addendum to the audit rather than a silent edit.

The task's source rules bite hard here: every secondary account of this revision found so far is a **law-firm advisory or compliance blog**, all of which §3 explicitly bars as bibliographic authority. The revised FDA document itself must be located on fda.gov and read directly.

**This is the item most likely to consume time and the one most likely to produce a finding.**

---

## 3. Structural observations

### 3.1 The date rule is satisfiable, and bites where it should

Three of six areas are inherently non-2023, and all three have a clean route through the rule:

| Area | Source | Year | Route |
|---|---|---|---|
| 1 | AC 20-151C | 2017 | `AUTHORISED_SOURCE = TRUE` |
| 3 | Parasuraman, Sheridan & Wickens | 2000 | `FOUNDATIONAL_HISTORICAL` — the historical claim belongs to the original; §5 correctly forbids substituting a paper that merely cites it |
| 6 | FDA CDS guidance | 2022 → 2026 | `AUTHORISED_REGULATORY_SOURCE`; the revision makes it contemporary anyway |

The rule's real force lands on Areas 2, 4 and 5, where contemporary peer-reviewed alternatives genuinely exist — and for 2 and 4 they have now been located. The requirement is achievable without straining.

For Area 3 the task additionally asks for a 2023+ synthesis to provide modern context alongside the foundational source. That is a discretionary addition and should not delay closure if nothing mechanistically apt is found.

### 3.2 Area 5 is the likely OPEN gap — and that is acceptable

The clinical selective-prediction study is arXiv-only, so under §4 it cannot be load-bearing. Finding a 2023+ peer-reviewed replacement that is *mechanistically* relevant is harder than it sounds: the task rightly refuses keyword matches, and most learning-to-defer literature governs **prediction participation**, which is the wrong mechanism. The corpus's own family-A anchor (Punzi et al. 2024, J. ACM) already establishes that canonical form.

Expected outcome: `SELECTIVE_PREDICTION_CORPUS_GAP = OPEN`, preprint retained as `SUPPLEMENTARY`, task closing at **`CLOSED_WITH_OPEN_SUPPLEMENTARY_GAP`**. That is a sound landing. Family A is not load-bearing for the novelty finding — TCAS is — so an open gap here does not block the contribution freeze.

### 3.3 The notes schema is under-determined — resolve it before writing

§8 requires following "the existing note filename convention, structure, metadata convention, citation convention, extraction style". There is no single such structure. At least four are in active use:

| Pattern | Example | Shape |
|---|---|---|
| Full extraction | `CRANE- Reasoning with Constrained LLM Generation.md` | 17 numbered sections |
| Reduced extraction | `Towards Adaptive Categories- Dimensional Governance for Agentic AI.md` | 6 sections, relevance gate recorded |
| GAP-FOCUSED | `OWASP Top 10 for Agentic Applications 2026.md`, `Levels of Autonomy for AI Agents.md` | condensed, gap-oriented |
| Document/standards form | `Artificial Intelligence Risk Management Framework (AI RMF 1.0).md` | *What the document is · Relevance · Accurate citation text · Bibliographic details* |

`papers/review-plan.md` records the governing tiers — full extraction, reduced extraction, methodological foundation, external evidence, early stop — so style follows tier, not house format.

**Recommendation:** FAA AC 20-151C and the FDA guidance follow the **AI RMF document/standards pattern**, which is the existing precedent for a non-research authority document and already carries an "Accurate citation text" and "Bibliographic details" section. Cleaveland et al., Bernabei & Costantino and Parasuraman et al. follow the **reduced-extraction pattern** as external evidence. Both routes accommodate §9's sixteen required fields without inventing a schema, satisfying §9's instruction that the repository format wins where the two differ.

### 3.4 A downstream effect the task does not mention: corpus counts

`docs/canonical/review-protocol.md` §Corpus reconciliation (resolved 2026-09-07) fixes four numbers at distinct scopes: **72** manuscript-facing, **111** active corpus, **112** files in `notes/`, and **63** as a superseded historical figure. It states that 72 "remains the reviewer-facing figure… Do not change unless the manuscript is resubmitted with a new methodology."

Adding six sources moves the active corpus to ~117 and the file count to ~118. More consequentially, **the AMICT rebuild *is* a resubmission**, and these six works are being added specifically to strengthen Related Work — which puts the 72 figure in play for the rebuilt paper's review claim (v3 line 103: *"from 72 papers, complemented by three large-scale systematic reviews involving 532 primary references"*).

This is not a blocker for source validation, but it is a decision the contribution-freeze task must take explicitly rather than inherit. Flagging it now so it is not discovered during drafting.

### 3.5 A gap in the completed novelty audit

`notes/Governed AI-Assisted Engineering- Graduated Human Oversight for Agentic Code Generation in Regulated Domains.md` — **Kang (2026), GAIE** — was **not coded** in `novelty-defence-matrix.md`.

It should have been. It is a three-tier graduated governance framework built on a deterministic **total** classifier `OCM : T → {Tier1, Tier2, Tier3}` over a four-dimensional risk vector, with **monotonicity, fail-safety and totality established by construction** — structurally the closest thing in the corpus to Theorems 6.1 and 6.2, and it explicitly grounds itself in the graduated-autonomy tradition the audit examined.

It **reinforces** the finding rather than threatening it: the graduated variable is human oversight intensity and evidence requirements, and the AI's generative scope is identical at every tier. It is also an arXiv preprint by a single industry author and cannot be load-bearing.

So **stop condition 2 does not fire** — no material finding changes. But under §10 this warrants an **addendum entry** to the defence matrix rather than a silent edit, and it strengthens the gap argument by adding a second independent formally-specified three-level framework alongside Flehmig whose intermediate level governs oversight rather than advisory scope.

---

## 4. Stop-condition pre-assessment

| # | Condition | Pre-assessment |
|---|---|---|
| 1 | TCAS material equivalence unsupportable | **Does not fire.** AC 20-151C confirms every figure; finding strengthened |
| 2 | Newer source materially changes the audit conclusion | **Does not fire on current evidence.** Kang (2026) reinforces; addendum, not rewrite |
| 3 | ACAS X precedent unverifiable | **Does not fire.** Cleaveland et al., ACM TECS, DOI 10.1145/3544970 |
| 4 | Load-bearing claim rests on an unsuitable source | **Open.** Depends on the revised FDA guidance — but N-13 is supportive, not load-bearing |
| 5 | Undiscovered prior work also performing the formalisation/generalisation/characterisation | **Unresolved until validation runs.** The residual risk; nothing seen so far |
| 6 | Validation contradicts the two-contribution direction | **Does not fire on current evidence.** Every validated source governs oversight, actions, or participation — none formalises advisory-scope governance as a general construct with empirical characterisation |

---

## 5. Expected outcome and effort

Most likely landing:

    SOURCE_CORPUS_VALIDATION = CLOSED_WITH_OPEN_SUPPLEMENTARY_GAP

with Area 5 open, Areas 1–4 and 6 resolved, six to eight notes created, and one addendum to the novelty audit covering the AC 20-151A → 20-151C correction, the Jeannin → Cleaveland upgrade, and the Kang (2026) matrix entry.

Effort is concentrated in three places, in this order:

1. **Locate and read the revised FDA CDS guidance on fda.gov** — the only item that can change a finding, and the one where secondary sources are barred.
2. **Write the notes** — six sources in an established schema, with §9's sixteen fields each, plus `citation-notes-map.md` registration. This is the bulk of the work and is mechanical once §3.3 is settled.
3. **Area 5 search** — bounded, likely to end in a documented gap rather than a source.

Areas 1, 2 and 4 are largely pre-validated by this analysis; execution there is confirmation, metadata capture and note authoring.

---

## 6. Points to settle before execution

1. **Notes schema per source type** — §3.3 recommendation, or an alternative.
2. **Whether to pursue RTCA DO-185B / ICAO Annex 10 Vol IV** as the primary standards authority for the inhibition logic, or rest on AC 20-151C as the accessible official source.
3. **Whether the Area 3 contemporary synthesis is required for closure** or discretionary.
4. **Acknowledgement that the corpus-count question (§3.4) transfers to the contribution-freeze task** rather than being resolved here.

None of these blocks starting. All four are cheaper to decide now than to unpick later.

---

## 7. Verdict

The task is **well-formed, correctly sequenced, and executable**. Its six source areas are real, four of the decisive items have been pre-verified against issuing authorities, and no stop condition is currently firing.

Two corrections to the task text itself: the ACAS X first author is **Cleaveland**, not Cleveland; and Source Area 1's premise is confirmed — **AC 20-151A is cancelled**, with AC 20-151C the current revision carrying identical inhibition figures.

One finding the task did not anticipate: the **FDA CDS guidance was revised in January 2026**, so Area 6 is a re-read rather than a confirmation, and the acceptable authority is the FDA document alone.

One correction owed to the previous task: **Kang (2026) was missed** by the novelty audit and needs an addendum entry.

---

## 8. Files inspected

Read-only. Nothing in this analysis modified any existing file, and no task artefact was created.

- `docs/tasks/AMICT NOVELTY CORPUS VALIDATION AND SOURCE INTEGRATION.md`
- `data/amict-conference-rebuild/novelty-defence-matrix.md`, `novelty-audit-report.md`
- `docs/canonical/citation-notes-map.md`, `docs/canonical/review-protocol.md`
- `papers/review-plan.md`, `papers/comparison-table.md`
- `notes/` — schema survey plus `Governed AI-Assisted Engineering…`, `Artificial Intelligence Risk Management Framework (AI RMF 1.0)`, `CRANE…`, `Towards Adaptive Categories…`, `OWASP Top 10…`
- External, verified against issuing authority: FAA AC index and AC 20-151C; ACM Digital Library record 10.1145/3544970; Elsevier record 10.1016/j.rcim.2024.102724
