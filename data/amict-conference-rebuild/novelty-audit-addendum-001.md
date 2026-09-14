# Novelty Audit — Addendum 001

**Date:** 2026-09-14
**Raised by:** AMICT novelty corpus validation and source integration task
**Amends:** [`novelty-defence-matrix.md`](novelty-defence-matrix.md) and [`novelty-audit-report.md`](novelty-audit-report.md) — **by addition only.** Neither artefact has been edited. They stand as the record of the audit as conducted on 2026-09-14.

    NOVELTY_AUDIT_VERDICT_CHANGE = NO

The verdict remains `STOP_MATERIAL_EQUIVALENCE_FOUND`. Nothing in this addendum reverses, weakens or restores any part of it.

---

## Part A — Omitted corpus entry: Kang (2026), GAIE

### A.1 What was missed

`notes/Governed AI-Assisted Engineering- Graduated Human Oversight for Agentic Code Generation in Regulated Domains.md` — **Kang, R. (2026), Governed AI-Assisted Engineering: Graduated Human Oversight for Agentic Code Generation in Regulated Domains**, arXiv:2606.22484v2 [cs.HC] — was in the corpus at the time of the audit and was not coded in the novelty-defence matrix.

### A.2 Why it should have been included

It is a family E entry that satisfies several of the audit's coding criteria simultaneously, and it is the **second** formally specified three-level graduated governance framework in the corpus after Flehmig et al. (2024). Omitting it left the family E row thinner than the corpus supported.

The audit's search proceeded by family keyword over the corpus. Kang's note uses the vocabulary of *oversight*, *tiers* and *regulatory impact* rather than the family terms the search enumerated, so it did not surface. This is a search-coverage defect, not a coding error: had it surfaced, it would have been coded, and the coding would have reinforced the finding.

### A.3 Mechanism coding — entry N-16

- **Prior work:** Kang (2026), Governed AI-Assisted Engineering (GAIE)
- **Prior-work family:** E — graduated runtime governance
- **Governed object:** **human oversight intensity and per-tier evidence/auditability requirements** for agentic code generation. Three pathways: Tier 1 Human-in-the-Loop (agent halts via `RETURN_CONTROL`; human approves the approach before generation and signs deployment); Tier 2 Human-over-the-Loop (agent generates and tests autonomously; human approves deployment only); Tier 3 Automated with Monitoring (fully autonomous pipeline with post-deployment monitoring and exception escalation).
- **Runtime state source:** an Oversight Classification Model `OCM : T → {Tier1, Tier2, Tier3}`, a **deterministic total function** over a four-dimensional risk vector `φ(t) = (RI, CP, RV, DS)` — regulatory impact, customer proximity, reversibility, data sensitivity. The vector is task metadata, not an external environmental measurement.
- **AI participation changed?** No. No tier disables the AI.
- **Prediction availability changed?** No.
- **Executable action space changed?** Indirectly — what the agent may deploy without human sign-off differs by tier — but the generative action space itself is not restricted.
- **Human authority changed?** Yes, by design: the tier determines how much human approval is required and at which point.
- **Recommendation-type scope changed?** **No. The AI's generative scope is identical at every tier.** This is the decisive coding.
- **Human final authority invariant?** Yes at Tier 1 and Tier 2; Tier 3 removes pre-deployment human approval, so authority is tier-dependent rather than invariant.
- **Formal guarantee:** three properties established **by construction** — **monotonicity**, **fail-safety** under correct or uncertain metadata, and **totality**. Structurally the closest analogue in the corpus to Theorem 6.1 (Totality) and Theorem 6.2 (Monotonicity).
- **Empirical evaluation:** none. Analytical productivity model only (84–97% velocity preservation, central estimate 91%, against 45–65% under uniform HITL). Expert validation with 5–8 practitioners is stated as pending (limitation L4). Regulatory mappings are the author's own analysis and are explicitly not validated by any regulator.
- **Mechanism overlap:** a deterministic total classifier producing discrete governance levels with monotone, fail-safe properties proved by construction — the same *shape* of formal apparatus this project uses.
- **Key distinction:** the governed object is oversight intensity and evidence requirements, not admissible advisory scope; the conditioning vector is task metadata, not a classified environmental state; the AI's output scope is constant across all three tiers.
- **Novelty threat:** **MEDIUM** — as with Baxi (2026), it constrains what may be claimed about graduated governance with properties-by-construction, while leaving the advisory-scope claim untouched.
- **Source status:** `SUPPLEMENTARY` — arXiv preprint, single industry author, no empirical validation, regulatory mappings unvalidated. **Must not be load-bearing.** Cite as "Kang, 2026, preprint".

### A.4 Why this reinforces rather than reverses the verdict

Kang (2026) is a **contrast case, not a counterexample**. The audit's finding is that the mechanism pattern `external state → nested admissible advisory-type set → human decides` has operational precedent, and that what remains available to claim is its abstraction, generalisation, proved containment and empirical characterisation. Kang governs a different object — how closely a human supervises, and what evidence is retained — while leaving the AI's generative scope constant across every tier.

It therefore extends the advisory-scope gap's confirmed footprint into a third domain: industrial safety-critical operation (Flehmig et al. 2024), embodied runtime assurance (Ghaleb et al. 2026), and now regulated software engineering. A 2026 framework that formalises graduation end-to-end, and explicitly grounds itself in the graduated-autonomy tradition, still does not condition what the AI may produce on the classified level.

Two consequences for wording discipline, both additive to the report's §7 prohibition list:

- The claim "graduated governance with properties established by construction is new" was already prohibited on the strength of Baxi (2026). Kang (2026) independently confirms that prohibition. Do not restate it.
- The claim that graduated frameworks govern only supervisory intensity must stay scoped to the frameworks reviewed. TCAS II is a counterexample within the audit's own evidence base.

### A.5 Effect on artefacts

`novelty-defence-matrix.md` should be read as carrying entry **N-16** as specified in §A.3 above. The matrix file itself is unchanged.

---

## Part B — Source corrections arising from validation

Three sources cited in the audit have been superseded or improved. **None changes a coded finding.** Recorded here so the audit record and the manuscript-facing corpus do not diverge.

### B.1 N-01 — FAA AC 20-151A is cancelled

The audit cited **FAA AC 20-151A**. The FAA advisory-circular index records AC 20-151, AC 20-151A and AC 20-151B as **cancelled**. The current revision is **AC 20-151C**, issued 21 July 2017, which cancels AC 20-151B (18 March 2014).

**The inhibition schedule is identical in the current document:**

| Advisory type | Climbing | Descending |
|---|---|---|
| Increase Descent RA | below 1650 ft AGL | below 1450 ft AGL |
| Descend RA | below 1200 ft AGL | below 1000 ft AGL |
| All RAs (TA-only) | below 1100 ft AGL | below 900 ft AGL |
| TA voice messages | below 600 ft AGL | below 400 ft AGL |

Every figure quoted in `novelty-audit-report.md` §2 is confirmed against AC 20-151C. The material-equivalence finding is **unchanged and, if anything, better evidenced** — it now rests on current rather than cancelled authority.

    AC_20_151A = SUPERSEDED
    AC_20_151C = ACCEPT_AUTHORISED

Manuscript-facing citation is AC 20-151C. AC 20-151A must not be cited as current authority.

RTCA DO-185B (TCAS II MOPS) and ICAO Annex 10 Volume IV are recorded as potential primary-standard enhancements. Not obtained; not required, since AC 20-151C authoritatively supports the bounded claim.

### B.2 N-02 — ACAS X citation upgraded

The audit cited Jeannin et al.'s earlier STTT hybrid-systems verification of ACAS X. The contemporary peer-reviewed source is:

**Cleaveland, R., Mitsch, S., & Platzer, A. (2023).** *Formally Verified Next-Generation Airborne Collision Avoidance Games in ACAS X.* ACM Transactions on Embedded Computing Systems, 22(1), Article 10, 1–30. DOI 10.1145/3544970.

Note the spelling: **Cleaveland**, not Cleveland. Metadata verified against the Crossref DOI record.

The coded finding is unchanged: formal verification of state-conditioned advisory logic has precedent. The 2023 paper establishes collision-freedom in differential game logic against an adversarial intruder, which supports the bounded claim at least as well as the earlier work and satisfies the contemporary-source preference.

### B.3 N-13 — FDA CDS guidance revised, coded proposition survives

The audit cited the **September 2022** FDA CDS final guidance. That version has been superseded: the guidance was published **6 January 2026** and reissued **29 January 2026** (docket FDA-2017-D-6569).

The revision was read directly from the FDA document. **Criterion 3's list-versus-directive distinction is preserved verbatim**, with permissible outputs still enumerated as a list of options, a prioritised list of options, or a list of follow-up or next-step options, and a specific preventive, diagnostic or treatment output or directive still failing the criterion. Criterion 4's independent-review requirement is unchanged.

The revision adds an **enforcement-discretion policy**: where only one option is clinically appropriate and the function otherwise meets all criteria, FDA does not intend to enforce.

N-13's bounded proposition — *recommendation/output type is already treated as a meaningful governance and regulatory variable* — **still holds**, and is mildly strengthened by having survived a deregulatory revision. N-13 remains `SUPPORTIVE` and must not become load-bearing.

---

## Part C — Status

    NOVELTY_AUDIT_VERDICT_CHANGE = NO
    MATERIAL_EQUIVALENCE_FINDING = UNCHANGED
    MECHANISM_NOVELTY = WITHDRAWN
    REPOSITIONING_DECISION = ACCEPTED
    ADDENDUM_ENTRIES_ADDED = N-16 (Kang 2026)
    SOURCE_CORRECTIONS = 3 (N-01 authority, N-02 citation, N-13 revision)
    KANG_2026_LOAD_BEARING = NO

No empirical figure was recomputed. No CLOSED workstream was reopened. No manuscript was drafted.
