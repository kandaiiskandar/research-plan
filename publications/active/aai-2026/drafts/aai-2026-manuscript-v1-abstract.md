# Abstract

A declared risk level constrains an AI system only if it changes what the system may recommend, and its presence in a specification establishes neither that it does nor how often it binds. We take the governed object to be the admissible recommendation set, apply an operational criterion under which a declared level changes governance behaviour only if it changes that set, and measure how often it binds. Configurations were defined so that a participation-only gate and an intermediate advisory-scope configuration differ at one state only, and replayed over five years of hourly environmental records for one coastal-fisheries deployment site in Kota Kinabalu, Sabah. The intermediate restriction bound in 5.81% of evaluated departure-window hours under the PRIMARY configuration and 4.48% under RESOLUTION. The frequency is conditional: it spans a deterministic configuration range of 5.67–9.56% across externally sourced threshold settings and falls to 1.96% and 1.26% under medium- and large-vessel configurations. Ocean state accounted for 97.6% of PRIMARY CAUTION classifications. Because historical marine-warning data were unavailable, that component was held at its least-severe value, so these frequencies are lower bounds under the declared exclusion. The measurements characterise governance activation rather than safety or decision outcomes. They indicate how a declared governance level can be audited through the recommendation constraints it imposes and the conditions under which they bind.

**Index Terms—** AI governance, Responsible AI, runtime governance, decision support, advisory systems, governance measurement, coastal fisheries.

---

# Phase 6 Drafting Audit

| # | Check | Result |
|---|---|---|
| 1 | Abstract word count | **217** |
| 2 | Within 180–220 target | **YES** — near the top of the band; see the note below on the preferred 190–210 range |
| 3 | Under 230 hard ceiling | **YES** |
| 4 | One paragraph | **YES** — nine sentences, no breaks |
| 5 | No citation in Abstract | **YES** — no bracketed key, no equation, no acronym left undefined |
| 6 | Problem stated | **YES** — S1 |
| 7 | Operational criterion represented accurately | **YES** — S2, as a criterion applied, not a result proved |
| 8 | Measured object remains admissible recommendation set | **YES** — named in S2 |
| 9 | Participation-only comparator represented | **YES** — S3 |
| 10 | Historical replay represented | **YES** — S3, five years of hourly environmental records |
| 11 | One-site scope preserved | **YES** — *"one coastal-fisheries deployment site in Kota Kinabalu, Sabah"*; no Malaysia- or Sabah-level framing |
| 12 | PRIMARY 5.81% included | **YES** |
| 13 | 5.81% explicitly interpreted as binding frequency | **YES** — S2 states the study measures *how often* the change binds; S4 reports it as hours in which the restriction *bound*; S5 calls it *"the frequency"* |
| 14 | RESOLUTION 4.48% included | **YES** |
| 15 | No claim the difference is due solely to spatial resolution | **YES** — the Abstract offers no explanation of the difference at all |
| 16 | Conditionality explicit | **YES** — S5 opens *"The frequency is conditional"* |
| 17 | Sourced-threshold envelope included | **YES** — 5.67–9.56% |
| 18 | Envelope correctly labelled deterministic / configuration-based | **YES** — *"a deterministic configuration range … across externally sourced threshold settings"* |
| 19 | Controlled 2.54–14.75% perturbation omitted or distinguished | **YES — OMITTED.** It answers a different question and could not be distinguished from the envelope in the available space |
| 20 | 97.6% attribution included | **YES** |
| 21 | 97.6% correctly refers to PRIMARY CAUTION classifications | **YES** — the object is named inside the sentence: *"97.6% of PRIMARY CAUTION classifications"* |
| 22 | Vessel-class result included | **YES** — 1.96% and 1.26% |
| 23 | Lower-bound qualification included | **YES** — S7 |
| 24 | Marine-warning exclusion not overexplained | **YES** — one clause: unavailable, held at least-severe value, hence lower bounds |
| 25 | No safety improvement claim | **YES** — denied outright in S8 |
| 26 | No decision-quality claim | **YES** — same sentence |
| 27 | No generated-advice validation claim | **YES** — the Abstract speaks only of what the system *may recommend* and of admissible sets |
| 28 | No human-validation claim | **YES** — no human term appears |
| 29 | No optimality claim | **YES** |
| 30 | No generalisation claim | **YES** |
| 31 | No statistical inference introduced | **YES** — no *significant*, *p-value*, *confidence interval*; the envelope is labelled deterministic |
| 32 | No architecture novelty claim | **YES** — no architecture is described |
| 33 | No mechanism novelty claim | **YES** |
| 34 | No unscoped "first / no prior study" claim | **YES** — the literature gap sentence was omitted entirely, so no absence claim appears |
| 35 | Responsible AI implication included | **YES** — S9 |
| 36 | Responsible AI implication concerns operational auditability | **YES** — auditing through the constraints imposed and the conditions under which they bind |
| 37 | No claim of trustworthy / ethical / safe AI | **YES** |
| 38 | Index Terms count 5–7 | **YES** — 7 |
| 39 | Index Terms consistent with manuscript | **YES** |
| 40 | Human-centred AI absent from Index Terms | **YES** — also absent: trustworthy AI, explainable AI, fairness, AI safety |
| 41 | IPoSCI absent | **YES** |

**42. Unsupported statement.** None. Every numeral is locked and already reported in Sections IV–V, and every predicate has a source sentence in the body.

**43. Abstract statement stronger than the body.** None. One wording difference is recorded for transparency: S9 says *"the recommendation constraints it imposes"* where Section VI says *"the admissible recommendations it changes"*. Section V-C already licenses the auditing verb — *"A declared intermediate level can be audited through whether, and how often, it changes the admissible recommendation set"* — so the Abstract is not reaching beyond the body, but the two formulations are not word-identical.

**44. Finding carried into the Abstract without its body qualification.** None, with one deliberate omission noted. The 97.6% figure carries its object inside the sentence (*CAUTION classifications*), and S8 additionally denies safety and decision-outcome readings. The 5.81% / 4.48% pair carries the envelope, the vessel-class fall and the lower bound, which are three of the four elements the locked central claim attaches to it. The fourth — the wave CAUTION onset being the dominant threshold sensitivity — is **not** stated separately in the Abstract. The envelope sentence conveys that the figure moves materially with threshold choice, and the locked central claim in the research chain likewise does not carry a separate wave-dominance clause, so this is judged acceptable rather than a missing qualification. It is recorded here so a later pass can revisit it if space is recovered.

### Abstract ↔ body traceability

| Abstract statement | Supporting section | Status |
|---|---|---|
| A declared level constrains a system only if it changes what may be recommended; its presence establishes neither that nor how often | I-P1, I-P2 | **TRACED** |
| Governed object is the admissible recommendation set | III, opening paragraph | **TRACED** |
| Operational criterion: a declared level changes governance behaviour only if it changes that set | III, **Criterion** | **TRACED** — status preserved (*"an operational measurement rule rather than a result"*) |
| Four configurations differing at one state only; participation-only gate versus intermediate advisory scope | III, Table II and the C1/C2 isolation paragraph | **TRACED** |
| Replay over five years of hourly environmental records, one site in Kota Kinabalu, Sabah | IV, paragraphs 1–2 | **TRACED** |
| Measures how often the change binds | III, metric-consequences paragraph | **TRACED** |
| 5.81% PRIMARY | V-A, Table III, V-C | **TRACED** |
| 4.48% RESOLUTION | V-A, Table III | **TRACED** |
| Sourced-threshold envelope 5.67–9.56%, deterministic configuration range | V-B, Table III note | **TRACED** |
| Falls to 1.96% and 1.26% for medium and large vessel classes | V-C | **TRACED** |
| Ocean state 97.6% of PRIMARY CAUTION classifications | V-C | **TRACED** |
| Marine-warning unavailable, held least-severe, frequencies are lower bounds | IV final paragraphs, V-C | **TRACED** |
| Characterises governance activation rather than safety or decision outcomes | I-P6, V-C closing, VI-P2 | **TRACED** |
| A declared level can be audited through the constraints imposed and the conditions under which they bind | V-C closing, VI-P3 | **TRACED** |

### Claim-strength classification

| Sentence | Class | Check |
|---|---|---|
| S1 | BACKGROUND | States the problem; asserts no result |
| S2 | METHOD | Criterion applied and quantity defined; no truth claim about the criterion |
| S3 | METHOD | Design and data only |
| S4 | RESULT | 5.81% / 4.48% — both in Section V-A and Table III |
| S5 | RESULT + QUALIFICATION | 5.67–9.56%, 1.96%, 1.26% — all in Section V; the deterministic label is preserved |
| S6 | RESULT | 97.6% — Section V-C, object named inline |
| S7 | QUALIFICATION | Lower bound, matching Section IV's scope (*activation frequencies*, not all results) |
| S8 | QUALIFICATION | Non-claim, weaker than or equal to Section VI-P2 |
| S9 | INTERPRETATION | Auditability only; does not exceed Section V-C or VI-P3 |

No RESULT sentence contains a value absent from Sections IV–V. No INTERPRETATION sentence exceeds Sections V–VI.

### Final logical check

**A.** No. 5.81% appears as hours in which the restriction *bound*, introduced by a sentence that says the study measures how often it binds; no improvement, effectiveness or gain predicate appears.
**B.** No. The Abstract states both values and explains neither; no accuracy, quality or preference language attaches to either configuration.
**C.** No. The envelope is named *"a deterministic configuration range … across externally sourced threshold settings"*, and no inferential term appears anywhere.
**D.** No. The figure is bound to *"PRIMARY CAUTION classifications"* inside the sentence, and S8 denies safety and outcome readings.
**E.** No. {Go, Delay} is not mentioned; no admissible-set content is named or endorsed.
**F.** No. S8 is explicit, no human or advice-quality term appears, and no rate is extended beyond the evaluated site and configurations.
**G.** Yes. S2 states the measurement is *how often* the change binds, S4 reports hours in which it bound, and S5 calls it *"the frequency"*.
**H.** Yes. S5 opens *"The frequency is conditional"* and gives two independent dependencies.
**I.** Yes. S9 is operational auditability, with no ethics, trust or safety framing.

### Note on length

At **217 words** the Abstract sits inside the 180–220 target and well under the 230 ceiling, but seven words above the preferred 190–210 range. The remaining cut candidates are the deterministic-range label, the lower-bound clause and the non-claim sentence, each of which the brief protects, so the Abstract was left at 217 rather than compressed into a qualification. No sentence was trimmed to hit a number.

### Body edits

**NONE.** Sections I–VI were not modified. No body–abstract conflict was found: every Abstract statement traced to an existing sentence without requiring the body to change.

### Open tasks carried forward

| Task | Status |
|---|---|
| FIGURE DATA EXTRACTION REQUIRED | **PRE-FINAL BLOCKER** |
| MFWAM CITATION RESOLUTION | **PRE-FINAL BLOCKER** |
| [AI-GOV-SLR] AUTHOR LIST | **PRE-FINAL TASK** |
| IPoSCI PUBLICATION STATUS RECHECK | **PRE-SUBMISSION CHECK** |

None solved in Phase 6.

---

PHASE 6 STATUS: READY FOR MANUSCRIPT INSERTION
