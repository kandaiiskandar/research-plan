# Source Validation and Corpus Integration Report — AMICT Conference Rebuild

**Date:** 2026-09-14
**Task:** `docs/tasks/AMICT NOVELTY CORPUS VALIDATION AND SOURCE INTEGRATION.md`
**Companion artefacts:** [`novelty-defence-matrix.md`](novelty-defence-matrix.md) · [`novelty-audit-report.md`](novelty-audit-report.md) · [`novelty-audit-addendum-001.md`](novelty-audit-addendum-001.md)

---

## 1. Executive verdict

    SOURCE_CORPUS_VALIDATION = CLOSED

All six source areas resolved. Every load-bearing source validates against its issuing authority or publisher record. The anticipated open gap in Area 5 **did not materialise** — a peer-reviewed 2026 replacement was found, so no preprint is load-bearing anywhere in the corpus.

Three findings of substance:

1. **FAA AC 20-151A is cancelled.** The audit cited it. The current revision, **AC 20-151C** (21 July 2017), carries the identical inhibition schedule, so the material-equivalence finding is unchanged and now rests on current authority.
2. **The FDA CDS guidance was revised twice in January 2026**, superseding the September 2022 version the audit cited. Criterion 3's list-versus-directive distinction is **preserved verbatim**; N-13's bounded proposition survives.
3. **Area 5 resolved on peer-reviewed ground.** Kwon & Kim (2026) in *Scientific Reports* states explicitly that the governed quantity is prediction participation, not recommendation type — the exact clarification the task specified. The arXiv preprint the audit used is no longer needed.

No stop condition fired. The repositioned two-contribution direction remains defensible.

---

## 2. Validation table — six source areas

| Area | Original candidate | Result | Accepted source | Year | Type | Status |
|---|---|---|---|---|---|---|
| 1 — TCAS II advisory inhibition | FAA AC 20-151A | **REPLACE** — cancelled | FAA AC 20-151C | 2017 | Aviation-authority certification guidance | `ACCEPT_AUTHORISED` |
| 2 — ACAS X formal verification | Jeannin et al., STTT | **REPLACE** — contemporary peer-reviewed available | Cleaveland, Mitsch & Platzer | 2023 | Peer-reviewed ACM journal | `ACCEPT_CONTEMPORARY` |
| 3 — Levels of automation | Parasuraman, Sheridan & Wickens (2000) | **RETAIN** — historical claim belongs to the original | Parasuraman, Sheridan & Wickens | 2000 | Peer-reviewed IEEE journal | `FOUNDATIONAL_HISTORICAL` |
| 3b — contemporary synthesis | *(none identified by audit)* | **CANDIDATE, NOT ACCEPTED** | Richardson, Fidock & Gunawan | 2025 | Peer-reviewed T&F journal | `MECHANISM_UNVERIFIED` — see §4.4 |
| 4 — Adaptive automation | USAARL-TECH-TR-2025-09 | **REPLACE** — peer-reviewed preferred over technical report | Bernabei & Costantino | 2024 | Peer-reviewed Elsevier journal | `ACCEPT_CONTEMPORARY` |
| 5 — Selective prediction / deferral | arXiv:2508.07617 | **REPLACE** — preprint superseded | Kwon & Kim | 2026 | Peer-reviewed Nature Portfolio journal | `ACCEPT_CONTEMPORARY` |
| 6 — FDA CDS guidance | FDA CDS guidance, Sept 2022 | **REPLACE** — superseded | FDA CDS guidance, 29 Jan 2026 | 2026 | Official regulatory publication | `ACCEPT_AUTHORISED` |

---

## 3. Per-candidate detail

### 3.1 Area 1 — TCAS II advisory inhibition

- **Original:** FAA AC 20-151A
- **Validation result:** **CANCELLED.** The FAA advisory-circular index records AC 20-151, AC 20-151A and AC 20-151B as cancelled.
- **Accepted source:** FAA AC 20-151C, *Airworthiness Approval of Traffic Alert and Collision Avoidance Systems (TCAS II), Versions 7.0 & 7.1 and Associated Mode S Transponders*, issued 21 July 2017, cancelling AC 20-151B (18 March 2014)
- **Source type:** Official aviation-authority certification guidance (category D)
- **Authority status:** Authorised. No DOI — official government publication
- **Official identifier:** Advisory Circular 20-151C · https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-151C.pdf
- **Status:** `ACCEPT_AUTHORISED` · `AUTHORISED_SOURCE = TRUE` · `SOURCE_VALIDITY = PASS`
- **Rationale:** the current document preserves the inhibition schedule in full. Verified figures: Increase Descent RA inhibited below 1650 ft AGL climbing / 1450 ft descending; Descend RA below 1200 / 1000; all RAs (TA-only) below 1100 / 900; TA voice below 600 / 400; plus performance-based Climb and Increase Climb inhibition against weight, altitude, temperature, flap and gear configuration. Every figure quoted in the novelty audit is confirmed.
- **Recorded:** `AC_20_151A = SUPERSEDED`, `AC_20_151C = ACCEPT_AUTHORISED`
- **Primary-standard enhancement:** RTCA DO-185B (TCAS II MOPS) and ICAO Annex 10 Volume IV sit higher in the source hierarchy and are recorded as optional enhancements. **Not obtained and not required** — AC 20-151C authoritatively supports the exact manuscript-facing claim. Per the execution decision, no disproportionate effort was spent pursuing them.

### 3.2 Area 2 — ACAS X formal verification

- **Original:** Jeannin et al., earlier STTT hybrid-systems verification
- **Validation result:** **REPLACED** by the contemporary peer-reviewed source the task named
- **Accepted source:** Cleaveland, R., Mitsch, S., & Platzer, A. (2023). *Formally Verified Next-Generation Airborne Collision Avoidance Games in ACAS X.* ACM Transactions on Embedded Computing Systems, 22(1), Article 10, 1–30
- **Source type:** Peer-reviewed journal article (category A)
- **Peer review:** Yes — ACM journal
- **DOI:** 10.1145/3544970 · ISSN 1539-9087 / 1558-3465
- **Status:** `ACCEPT_CONTEMPORARY` · `SOURCE_VALIDITY = PASS` · year ≥ 2023
- **Rationale:** metadata verified against the **Crossref DOI record** — online 29 October 2022, print issue 31 January 2023, publisher ACM. The arXiv preprint (2106.02030) is superseded for citation. **The task text spelled the first author "Cleveland"; the correct spelling is "Cleaveland"** and has been used throughout.
- **Formal property established:** collision-freedom for rich encounters with an adversarial intruder, proved via winning-strategy existence in **differential game logic**. Recorded in the note that this is *not* the same general governance theorem as this project's, and must not be represented as such. The supported comparison is narrower and exactly as the task specified: formal verification of state-conditioned advisory logic has precedent.

### 3.3 Area 3 — Levels of automation

- **Original:** Parasuraman, Sheridan & Wickens (2000)
- **Validation result:** **RETAINED** as foundational
- **Accepted source:** Parasuraman, R., Sheridan, T. B., & Wickens, C. D. (2000). *A model for types and levels of human interaction with automation.* IEEE Transactions on Systems, Man, and Cybernetics — Part A: Systems and Humans, 30(3), 286–297
- **Source type:** Peer-reviewed journal article (category A)
- **DOI:** 10.1109/3468.844354 · ISSN 1083-4427 — verified against the Crossref DOI record
- **Status:** `FOUNDATIONAL_HISTORICAL` · `SOURCE_VALIDITY = PASS`
- **Necessity justification (exception A — original/foundational source of a concept):** the claim being sourced is that graduated narrowing of the options presented to a human is long established, and that its canonical formulation assigns levels at design time per function. That claim is *about* this paper. A 2023+ review citing the model can attest to continued influence but cannot source the model's own wording — Level 2 "offers a complete set of decision/action alternatives", Level 3 "narrows the selection down to a few", Level 4 "suggests one alternative" — nor the design-time character of the original formulation. Substituting a later citing paper would misattribute the historical position and weaken the honesty of the comparison.
- **Required distinction recorded in the note:** design-time narrowing of the *number of alternatives* within a decision ≠ runtime environmental-state-conditioned restriction of admissible *recommendation types*.

### 3.4 Area 3b — contemporary levels-of-automation synthesis

- **Candidate identified:** Richardson, L. S., Fidock, J., & Gunawan, I. (2025). *Systematic Literature Review of Levels of Automation (Autonomy) Taxonomy: Critiques and Recommendations.* International Journal of Human–Computer Interaction, 41(24), 15824–15843. DOI 10.1080/10447318.2025.2502978. Peer-reviewed, Informa UK / Taylor & Francis.
- **Metadata:** verified against the Crossref DOI record.
- **Status:** **NOT ACCEPTED** — `MECHANISM_UNVERIFIED`
- **Rationale:** full text is paywalled and could not be obtained during validation. The task's mechanism-first rule forbids inferring relevance from terminology, and the repository's note convention requires an extraction, not a metadata stub. Creating a note from title and venue alone would risk a later citation resting on an unverified mechanism.
- **Disposition:** recorded here as a verified-metadata candidate for a future pass. `AREA_3_CONTEMPORARY_SYNTHESIS = PREFERRED_NOT_BLOCKING` per the execution decision, so this does not affect closure. **No note was created and no citation-map row was added.**

### 3.5 Area 4 — Adaptive automation / adjustable autonomy

- **Original:** USAARL-TECH-TR-2025-09 (authorised technical report)
- **Validation result:** **REPLACED** — peer-reviewed 2023+ source preferred over technical-report-only evidence
- **Accepted source:** Bernabei, M., & Costantino, F. (2024). *Adaptive automation: Status of research and future challenges.* Robotics and Computer-Integrated Manufacturing, 88, 102724
- **Source type:** Peer-reviewed systematic literature review (category A)
- **DOI:** 10.1016/j.rcim.2024.102724 · ISSN 0736-5845 — verified against the Crossref DOI record
- **Status:** `ACCEPT_CONTEMPORARY` · `SOURCE_VALIDITY = PASS` · `PEER_REVIEWED_2023_PLUS`
- **Mechanism verification (not accepted on title):** full text obtained from the University of Rome institutional repository and read. Scope: 344 contributions retrieved, 181 reviewed in full plus 10 by snowball, covering the 1950s to 2022. The review governs **function allocation and level of automation**, and identifies **seven invocation-trigger categories**: operator-based, system-based, task/mission-based, **environmental-based**, spatiotemporal-based, performance-based, psychophysiological-based. It describes **no** system that restricts the set or types of recommendations presented to a human on the basis of an externally classified environmental state.
- **Two findings that do real work:** (i) environmental triggering of automation change already exists as a recognised category, so conditioning governance on environmental parameters is not itself novel — what the literature does with that trigger is reallocate function, not contract an admissible recommendation-type set; (ii) the review fixes the field's terminology — *adaptable* automation is dynamic allocation with authority retained by the human operator, *adaptive* automation places authority with the machine. The architecture here is runtime state-conditioned but holds human authority unconditionally, so using "adaptive" loosely would misdescribe it in the vocabulary of the field it is compared against. Recorded in the note as a precision requirement for the manuscript.
- **USAARL report:** superseded as primary Area 4 source. Not integrated; no note created.

### 3.6 Area 5 — Selective prediction / abstention / deferral

- **Original:** *On the Limits of Selective AI Prediction: A Case Study in Clinical Decision Making*, arXiv:2508.07617 — preprint, therefore barred from load-bearing use
- **Validation result:** **REPLACED** by a peer-reviewed 2026 source
- **Accepted source:** Kwon, H., & Kim, D.-J. (2026). *Conformal selective prediction with cost aware deferral for safe clinical triage under distribution shift.* Scientific Reports, 16, article 10016
- **Source type:** Peer-reviewed journal article, Nature Portfolio (category A)
- **DOI:** 10.1038/s41598-026-40637-w
- **Status:** `ACCEPT_CONTEMPORARY` · `SOURCE_VALIDITY = PASS` · year ≥ 2023
- **Mechanism verification (not accepted on keyword):** the paper states that the system determines **whether to issue a prediction or defer the case**, and **does not vary the types of recommendation** — only the participation decision. Deferral is triggered by a certainty threshold on calibrated posterior probabilities, with the threshold selected to minimise expected clinical cost (false negatives 10.0, false positives 1.0, deferrals 2.0). Distribution shift is handled by importance-weighted conformal variants that reweight calibration, **not** by classifying an external environmental state. Split conformal prediction supplies finite-sample distribution-free coverage under exchangeability. Clinician authority is invariant — deferred cases route to human review without automatic override. Evaluated on PhysioNet 2019 sepsis data, 2,155 patients, temporally separated splits; error reduction at 80% coverage of 49.6% in-distribution and 46.7% out-of-distribution.
- **Why this is the right source:** the task asked for a source that clarifies whether the governed quantity is prediction participation rather than recommendation-type scope conditioned on external environment. This paper answers that question explicitly, on peer-reviewed ground, and therefore **resolves rather than defers** the family A row.
- **Disposition of the preprint:** no longer required. Not integrated; no note created. It may be cited in future as supplementary evidence that human response to scope restriction is not benign, but that is a Limitations point outside this task.
- **Disambiguation recorded:** Kwon & Kim (2026) is a different author from the existing corpus entry Kwon et al. (2025) on adaptive shielding. Distinct citation keys are in use.

    SELECTIVE_PREDICTION_CORPUS_GAP = CLOSED

### 3.7 Area 6 — FDA Clinical Decision Support guidance

- **Original:** FDA CDS final guidance, September 2022
- **Validation result:** **SUPERSEDED.** Published 6 January 2026, reissued 29 January 2026
- **Accepted source:** U.S. Food and Drug Administration (2026). *Clinical Decision Support Software: Guidance for Industry and Food and Drug Administration Staff*, 29 January 2026. CDRH, CBER, CDER, Office of Combination Products
- **Source type:** Official government/regulatory publication (category C)
- **Official identifier:** Docket FDA-2017-D-6569 · https://www.fda.gov/media/109618/download
- **Status:** `ACCEPT_AUTHORISED` · `AUTHORISED_REGULATORY_SOURCE` · contemporary (2026) · `SOURCE_VALIDITY = PASS`
- **Verification method:** read directly from the FDA document and cross-checked against the FDA guidance landing page. **No law-firm advisory or compliance blog was used as authority**, per §3 of the task; all such secondary accounts encountered were disregarded.
- **Criterion 3 — the coded distinction survives.** Permissible outputs are still enumerated as (1) a list of preventive, diagnostic or treatment options; (2) a prioritised list of such options; (3) a list of follow-up or next-step options for consideration — "as long as they were not intended to replace or direct the HCP's judgment". A software function that "provides a specific preventive, diagnostic or treatment output or directive" still fails Criterion 3. Criterion 4's independent-review requirement is unchanged.
- **What changed:** an enforcement-discretion policy is added — where only one option is clinically appropriate and the function otherwise meets all criteria, FDA does not intend to enforce.
- **Effect on N-13:** the bounded proposition — *recommendation/output type is already treated as a meaningful governance and regulatory variable* — **still holds**, mildly strengthened by having survived a deregulatory revision. **N-13 remains `SUPPORTIVE` and does not become load-bearing.** Recorded in `novelty-audit-addendum-001.md` §B.3.
- **Caveat recorded in the note:** the media URL previously served the 2022 version; always check the date printed on the document.

---

## 4. Contemporary literature coverage

| Category | Count | Sources |
|---|---|---|
| Accepted 2023+ peer-reviewed research sources | **3** | Cleaveland, Mitsch & Platzer (2023); Bernabei & Costantino (2024); Kwon & Kim (2026) |
| Accepted authorised official sources | **2** | FAA AC 20-151C; FDA CDS guidance (2026) |
| Foundational historical sources | **1** | Parasuraman, Sheridan & Wickens (2000) |
| Supplementary / preprint sources integrated | **0** | — |
| Preprints load-bearing anywhere | **0** | — |
| Unresolved corpus gaps | **0 load-bearing** | one non-blocking item, §3.4 |

Five of six manuscript-facing sources are either 2023+ or authorised. The single pre-2023 research source is explicitly classified `FOUNDATIONAL_HISTORICAL` with its necessity justified in §3.3. The one authorised source carrying a pre-2023 issue date (AC 20-151C, 2017) is the **current** revision of a live certification document, admitted under the authorised-source exception.

---

## 5. Notes created

Six, all in `notes/`, following existing repository schema by source type. No second notes directory, no conference-specific folder, no new reference system.

**Document/standards pattern** — structural precedent `Artificial Intelligence Risk Management Framework (AI RMF 1.0).md`:

1. `Airworthiness Approval of Traffic Alert and Collision Avoidance Systems (TCAS II) (FAA AC 20-151C).md`
2. `Clinical Decision Support Software (FDA Guidance for Industry and FDA Staff 2026).md`

**Reduced-extraction / external-evidence pattern** — structural precedent `Towards Adaptive Categories- Dimensional Governance for Agentic AI.md`:

3. `Formally Verified Next-Generation Airborne Collision Avoidance Games in ACAS X.md`
4. `Adaptive automation- Status of research and future challenges.md`
5. `A model for types and levels of human interaction with automation.md`
6. `Conformal selective prediction with cost aware deferral for safe clinical triage under distribution shift.md`

Every note carries: full title, authors, year, venue, publisher, volume/issue/pages or document number, DOI or official identifier, source type, peer-review or authority status, contemporary/historical classification, a twelve-row mechanism-coding table, the claims the source supports, the claims it does **not** support, relevance to the novelty defence, relationship to graduated advisory-scope governance, and limitations.

Duplicate check performed before creation: none of the six existed in `notes/`. `notes/` moved from 112 to 118 `.md` files.

## 6. Existing notes updated

**None.** No existing note required modification. Existing content was preserved untouched.

One observation for a future pass, not acted on here: `notes/Artificial Intelligence Risk Management Framework (AI RMF 1.0).md` §4.1 refers to "Totality (Theorem 5.1)", which predates the theorem-numbering repair. This is a stale cross-reference in an existing note, outside this task's scope, and is recorded rather than edited.

## 7. citation-notes-map entries

Six rows appended to `docs/canonical/citation-notes-map.md`, following the append-only convention used for recent additions, with bracketed descriptors and URL-encoded quick links:

- `FAA (2017) [AC 20-151C, TCAS II advisory inhibition, authorised source]`
- `FDA (2026) [Clinical Decision Support Software guidance, authorised regulatory source]`
- `Cleaveland, Mitsch & Platzer (2023) [ACAS X formal verification, novelty-defence evidence]`
- `Bernabei & Costantino (2024) [adaptive automation SLR, novelty-defence evidence]`
- `Parasuraman, Sheridan & Wickens (2000) [levels of automation, foundational historical]`
- `Kwon & Kim (2026) [conformal selective prediction, novelty-defence evidence]`

Mapped rows: 111 → 117, reconciling with the `review-protocol.md` active-corpus convention. (A naive `grep` for `notes/` returns 119 because the file header contains two further lines mentioning that path.) A pre-existing missing trailing newline caused the first appended row to concatenate onto the final Yaakob et al. row; this was detected and repaired, and the Yaakob row is intact.

## 8. Rejected and replaced sources

| Source | Disposition | Reason |
|---|---|---|
| FAA AC 20-151A | `REPLACE` → AC 20-151C | Cancelled. Must not be cited as current authority |
| Jeannin et al., STTT ACAS X verification | `REPLACE` → Cleaveland et al. (2023) | Contemporary peer-reviewed source available and preferred |
| USAARL-TECH-TR-2025-09 | `REPLACE` → Bernabei & Costantino (2024) | Peer-reviewed journal preferred over technical-report-only evidence |
| arXiv:2508.07617, selective AI prediction | `REPLACE` → Kwon & Kim (2026) | Preprint; peer-reviewed alternative found, so it cannot be load-bearing |
| FDA CDS guidance, September 2022 | `REPLACE` → 29 January 2026 version | Superseded |
| Richardson, Fidock & Gunawan (2025) | `NOT ACCEPTED` (candidate retained) | Full text paywalled; mechanism unverified. Non-blocking |
| Law-firm advisories and compliance blogs on the FDA revision | `REJECT` | Barred as bibliographic authority under §3 |

## 9. Does the TCAS material-equivalence finding survive validation?

**Yes — intact, and now better evidenced.**

The finding rested on a cancelled advisory circular. Validation moved it onto the current one and confirmed every quoted figure. Nothing was softened, narrowed or hidden: the nested, monotone, externally-conditioned advisory-type inhibition schedule is reproduced in full in the accepted note, together with the explicit statement that the "it governs a deterministic algorithm, not AI" distinction is **weak** and must not be leaned on, since this project's Layer 3 is itself a deterministic rule engine.

`MATERIAL_EQUIVALENCE_FINDING = UNCHANGED`

## 10. Does the ACAS X formal-verification precedent survive validation?

**Yes**, and on stronger footing. The precedent now rests on a peer-reviewed ACM journal article with a verified DOI rather than on older work. The bounded claim is unchanged: formal verification of state-conditioned advisory logic has precedent.

The note explicitly records what the paper does **not** establish — it proves collision-freedom in an adversarial encounter game, not totality, monotonicity over a severity order, or containment of an advisory set within a state-indexed admissible set — so the precedent cannot be overread into equivalence with this project's formal properties.

## 11. Does the repositioned contribution direction remain defensible?

**Yes.**

    CONTRIBUTION_DIRECTION_CONTRADICTION = FALSE

Checked against every validated source:

| Source | Governs | Conditions on | Formalises advisory-scope governance as a general construct? | Empirically characterises it against participation-only governance? |
|---|---|---|---|---|
| FAA AC 20-151C | Advisory types | External scalar + configuration | No — device-specific certified table | No |
| Cleaveland et al. (2023) | Advisory selection | Encounter state | No — collision-freedom for one system | No |
| Parasuraman et al. (2000) | Automation degree per stage | Design decision | No | No |
| Bernabei & Costantino (2024) | Function allocation, LOA | Seven trigger categories | No | No |
| Kwon & Kim (2026) | Prediction participation | Model confidence + cost | No | No |
| FDA CDS (2026) | Permissible output form | Intended purpose (design-time) | No | No |
| Kang (2026), addendum N-16 | Oversight intensity, evidence | Task metadata | No | No |

No validated source performs the claimed **generalisation + formalisation + empirical characterisation** combination. **Stop condition 5 does not fire.** C1 and C2 as stated in the task remain supportable.

Two wording consequences carried forward to the contribution freeze:

- The claim that *graduated governance with properties established by construction* is new is prohibited on the strength of Baxi (2026) and independently confirmed by Kang (2026).
- The claim that graduated frameworks govern only supervisory intensity must stay scoped to the frameworks reviewed — TCAS II is a counterexample inside the audit's own evidence base.

## 12. Open corpus gaps

| Item | Status | Blocking? |
|---|---|---|
| Area 3b contemporary LOA synthesis — Richardson et al. (2025) | Metadata verified, full text paywalled, mechanism unverified | **No** — `PREFERRED_NOT_BLOCKING` |
| RTCA DO-185B / ICAO Annex 10 Vol IV as primary standards | Recorded as optional enhancement; not obtained | **No** — AC 20-151C supports the claim |
| `CORPUS_COUNT_RECONCILIATION` | `DEFERRED_TO_CONTRIBUTION_FREEZE` | **No** — see §13 |

No load-bearing gap remains.

## 13. Deferred downstream item

    CORPUS_COUNT_RECONCILIATION = DEFERRED_TO_CONTRIBUTION_FREEZE

Per the execution decision, the figures **72** (manuscript-facing), **111** (active corpus), **112** (notes files) and **63** (historical/superseded) were **not modified**, and no methodology statement was rewritten. Adding six validated notes mechanically changes repository file counts — `notes/` is now 118 `.md` files and `citation-notes-map.md` now maps 117 rows — 117 mapped plus the one archived stub that `review-protocol.md` records as deliberately unmapped — but the manuscript-facing review count has not been reinterpreted.

**The Contribution Freeze task must decide** whether the rebuilt conference paper can continue to describe its review as based on 72 manuscript-facing papers after adding external novelty-defence sources, or whether those sources must be described separately as targeted post-review additions. That methodological question is explicitly **not** resolved here.

## 14. Changed files

**Created — notes (6):**

- `notes/Airworthiness Approval of Traffic Alert and Collision Avoidance Systems (TCAS II) (FAA AC 20-151C).md`
- `notes/Clinical Decision Support Software (FDA Guidance for Industry and FDA Staff 2026).md`
- `notes/Formally Verified Next-Generation Airborne Collision Avoidance Games in ACAS X.md`
- `notes/Adaptive automation- Status of research and future challenges.md`
- `notes/A model for types and levels of human interaction with automation.md`
- `notes/Conformal selective prediction with cost aware deferral for safe clinical triage under distribution shift.md`

**Created — evidence area (2):**

- `data/amict-conference-rebuild/source-validation-report.md` (this file)
- `data/amict-conference-rebuild/novelty-audit-addendum-001.md`

**Modified (1):**

- `docs/canonical/citation-notes-map.md` — six rows appended; one pre-existing missing-newline defect repaired

**Untouched, as required:**

- `data/amict-conference-rebuild/novelty-defence-matrix.md` and `novelty-audit-report.md` — audit records, amended by addendum only
- all existing `notes/` files
- `docs/canonical/review-protocol.md` and all corpus-count figures
- the conference manuscript line, all empirical artefacts, all CLOSED workstreams

---

## 15. Verification summary

| # | Check | Result |
|---|---|---|
| A | Every accepted citation resolves to an existing note | **PASS** — 6/6 |
| B | No duplicate source note created | **PASS** — pre-creation check found none of the six present |
| C | Every new manuscript-facing research source is 2023+ or justified `FOUNDATIONAL_HISTORICAL` | **PASS** — 3 contemporary, 1 foundational with justification, 2 authorised |
| D | Every official source verified against its issuing authority | **PASS** — FAA index and AC 20-151C from faa.gov; FDA guidance and landing page from fda.gov |
| E | Every DOI verified | **PASS** — 10.1145/3544970, 10.1016/j.rcim.2024.102724, 10.1109/3468.844354 verified against Crossref DOI records; 10.1038/s41598-026-40637-w verified against the publisher record; official documents carry no DOI |
| F | Every claimed peer-reviewed publication is actually peer reviewed | **PASS** — ACM TECS, Elsevier RCIM, IEEE T-SMC-A, Nature Portfolio Scientific Reports |
| G | No ResearchGate, blog or generic website used as bibliographic authority | **PASS** — institutional repository used once, to obtain a readable copy of an Elsevier article, not for metadata |
| H | No preprint load-bearing where a peer-reviewed alternative exists | **PASS** — zero preprints integrated |
| I | TCAS precedent not weakened or hidden to restore novelty | **PASS** — strengthened; full schedule and the weakness of the "not AI" distinction recorded in the note |
| J | Distinction between mechanism precedent and formalisation/generalisation contribution remains explicit | **PASS** — stated in every note's scope-and-limits section and in §11 |
| K | No scientific experiment run | **PASS** |
| L | No frozen empirical figure recomputed | **PASS** |
| M | No manuscript drafted | **PASS** — no `manuscript.md`, `.docx`, `.pdf` or `.tex` created or modified |

**Counts:** 13 PASS · 0 FAIL · 0 OPEN load-bearing · 1 OPEN non-blocking (§3.4)

**Integrity note.** A filesystem scan showed post-midnight modification timestamps across many `data/` and `publications/` files. These are an artefact of the folder mount, not edits. The Journal 1 manuscript was checked directly and is byte-identical to its pre-task state (MD5 `9c64ab80c025c14b24dc1a043a6adf88`, 1,661 lines, zero `Theorem 5.x` occurrences). The only files written by this task are the eleven listed in §14.

**Link-encoding check.** The six appended citation-map rows were verified to parse as valid Markdown links with their targets resolving on disk. Parentheses in the two document/standards filenames are percent-encoded (`%28`/`%29`), so the links do not terminate early. All 117 mapped rows in the file were re-checked: 0 unparseable, 0 missing targets.

---

    SOURCE_CORPUS_VALIDATION = CLOSED
    MECHANISM_NOVELTY = WITHDRAWN
    REPOSITIONING_DECISION = ACCEPTED
    CONTRIBUTION_FREEZE = NOT_STARTED
    CONFERENCE_MANUSCRIPT = NOT_DRAFTED
