# AAI 2026 — Figure 1 (v4) ↔ Manuscript Audit

**Figure audited:** Figure 1, version supplied 2026-10-07 (post-correction)
**Manuscript:** `aai-2026-manuscript-v2-revised.docx` / `.pdf`, unchanged since 2026-10-07 08:12
**Authority:** the manuscript, for all definitions, equations, results and claim boundaries
**Method:** every stage inspected at magnification against the manuscript text; glyphs checked by letterform

Nothing was modified.

---

# PART A — Executive verdict

## **Publication-ready after minor corrections** — now down to a single item

Six of the seven corrections are applied and verified. The **critical** issue is fixed: the denominator policy now reads "Departure-window · Daylight-only", matching the only two denominators the manuscript evaluates. Both **major** issues are fixed: the threshold heading reads "(externally sourced thresholds)" rather than "official guidelines", and stage 2 now carries provenance markers on every classifier component, including the one that matters most — "Time / daylight state (COLREGs boundary; night → UNSAFE researcher-defined)". The RESOLUTION period is restored, and the Δ*L*₂ box now carries the formal definition alongside the cross-check, closing the last semantic gap between figure and equation.

**One correction was not applied.** Every empty set in the figure is still **Ø** (U+00D8, Latin capital O with stroke), not **∅** (U+2205, empty set). I checked this at magnification rather than at a glance, because it was the one item I previously could not settle from the rendered image. It is Ø in all four places: the Governance Contract UNSAFE row, and the UNSAFE line of C1, C2 and C3. The evidence is unambiguous — the glyph is an oval with pronounced thick/thin stroke contrast, carries the italic slant of the surrounding letters, and its slash barely exits the oval. A true ∅ in a serif face is a uniform-weight circle with a long diagonal extending clearly beyond it on both ends.

This is small but not cosmetic. Ø is a Scandinavian letter. The paper's central object is a set-valued mapping *A*<sub>AI</sub>(*S*), the manuscript uses ∅ correctly in Table I, and the figure sits on the facing column. A reviewer who reads set notation for a living will see a letter where a set symbol belongs. Four character replacements in the figure source.

Two residual observations follow, neither blocking: the stage 1 header still carries PRIMARY's period only, which stage 5 now mitigates; and the manuscript — not the figure — never states where the wave CAUTION onset comes from, which is the one provenance hole the ±0.25 m removal left behind.

---

# PART B — Alignment table

| Item | Figure 1 (v4) | Manuscript | Status | Severity | Action |
|---|---|---|---|---|---|
| **Stage 1** record list | Wind speed, Rainfall, Ocean state (wave), Time (hour), Marine warning (unavailable for replay period) | §IV: wind, rainfall, marine warning, ocean state, time; no usable archive | Aligned | None | — |
| Stage 1 period header | "(2020–2024)" | PRIMARY Jan 2020–Dec 2024; RESOLUTION Oct 2021–Dec 2024 | PRIMARY only | **Minor** | Mitigated by stage 5; optionally qualify as PRIMARY |
| **Stage 2** wind | "Wind speed (sourced threshold)" | §IV: MET Malaysia strong-wind criteria [14] | Aligned | None | **Fixed** |
| Stage 2 rainfall | "Rainfall (sourced thresholds)" — plural | §IV: UNSAFE from MET [15]; CAUTION from DID [18], non-MET | Aligned; plural is correct | None | **Fixed** |
| Stage 2 ocean state | "Ocean state (sourced threshold)" | §IV: ocean-state boundary follows operational ceiling [16] | Aligned as written | **Minor** | See C-2 below |
| Stage 2 time/daylight | "(COLREGs boundary; night → UNSAFE researcher-defined)" | §IV: day boundary COLREGs [17]; non-daylight→UNSAFE policy researcher-defined | Aligned | None | **Fixed** |
| Stage 2 marine warning | "excluded; held at least-severe value" | §IV: declared exclusion, least-severe value | Aligned | None | — |
| Stage 2 output | SAFE / CAUTION / UNSAFE | §III: three states | Aligned | None | — |
| **Stage 3** governed object | *A*<sub>AI</sub>(*S*) | §III: *A*<sub>AI</sub>(*S*) | Aligned | None | — |
| Stage 3 SAFE | FULL (all recommendations) | Table I: FULL | Aligned | None | — |
| Stage 3 CAUTION | {Go, Delay} (researcher-defined strict subset) | Table I + §III | Aligned | None | — |
| Stage 3 UNSAFE | **Ø** (no participation) | Table I: **∅** | **Wrong glyph** | **Minor** | See C-1 |
| **Stage 4** C0 | FULL / FULL / FULL | §III: "C0 applies no restriction" | Aligned | None | — |
| Stage 4 C1 | FULL / FULL / **Ø** | §III: participation gating alone | Values aligned; glyph wrong | **Minor** | See C-1 |
| Stage 4 C2 | FULL / {Go, Delay} / **Ø** | §III: evaluated intermediate-scope | Values aligned; glyph wrong | **Minor** | See C-1 |
| Stage 4 C3 | FULL / FULL / **Ø** | §III: three states, no contraction at intermediate | Values aligned; glyph wrong | **Minor** | See C-1 |
| Stage 4 isolation | "Same at SAFE and UNSAFE · Different only at CAUTION" | §III, verbatim in substance | Aligned | None | — |
| **Stage 5** replay character | "Deterministic replay (on classified record)" | §IV: deterministic historical replay, no randomisation | Aligned | None | — |
| Stage 5 PRIMARY | 2020–2024; 43,848; 9,135; 05:00–09:00 | §IV, identical | Aligned | None | — |
| Stage 5 RESOLUTION | **Oct 2021–Dec 2024**; alternative environmental-data configuration; 28,501; 5,935; 05:00–09:00 | §IV, identical; §V-A "differ in both wave source and record period" | Aligned | None | **Fixed** |
| Stage 5 metric | Δ*L*₂; "binds (C₂ vs C₁)"; "Defined by: (C₀↔C₂) − (C₀↔C₁)"; "Direct cross-check: C₁↔C₂" | §III definition and cross-check; §V-A "returned the same value" | Aligned | None | **Fixed** |
| **Stage 6** threshold heading | "(externally sourced thresholds)" | §IV: four distinct provenances, one journal-sourced | Aligned | None | **Fixed** |
| Stage 6 threshold bullets | Alternative threshold sets · Rainfall · Wind · Wave UNSAFE boundary (alternative reading) | §V-B: envelope, rainfall 0.48/0.78 pp, wind structural zero, two sourced readings 5.81%/9.22% | Aligned | None | — |
| Stage 6 vessel classes | Small (baseline) · Medium · Large | §V-C: 5.81 / 1.96 / 1.26 PRIMARY | Aligned | None | — |
| Stage 6 denominator | **Departure-window · Daylight-only** | §V-C: departure-window baseline; daylight-only 9.59% / 7.40% | Aligned | None | **Fixed (was Critical)** |
| Stage 6 attribution | Wind · Rainfall · Ocean state · Time/daylight · Marine warning (excluded) | §V-C: all five, three distinct zeros | Aligned | None | — |
| Removed analyses | No ±0.25 m, no 2.54–14.75%, no "wave CAUTION onset" | Deleted from manuscript | Aligned | None | — |
| Bottom band | Data and Classification · Governance Design · Evaluation · Robustness Analysis | — | Unchanged | None | — |
| Caption | "Fig. 1. Evaluation framework for measuring the operational effect of the intermediate governance restriction." | — | Unchanged | None | — |

---

# PART C — Issues requiring correction

## CRITICAL

**None.** The previous critical issue — the "All hours" denominator — is resolved.

## MAJOR

**None.** Both previous major issues — the "official guidelines" heading and the unmarked researcher-defined choices in stage 2 — are resolved.

## MINOR

### C-1. Every empty set in the figure is Ø, not ∅ — *the one outstanding correction*

**Issue.** All four empty-set symbols use **Ø** (U+00D8, Latin capital O with stroke) where the manuscript uses **∅** (U+2205, empty set).

**Determination.** Checked at magnification, not inferred. The glyph shows: an oval letterform with clear thick/thin stroke modulation (heavy on the left and right, light at top and bottom), the italic slant of the adjacent bold-italic text, and a slash that terminates just outside the oval. U+2205 in a serif face renders as a geometrically even circle with a long diagonal extending well past the circle at both ends. The figure's glyph is the letter.

**Why it matters.** Ø is a Danish and Norwegian letter. This paper's governed object is a set-valued mapping, Table I in the facing column prints ∅ correctly, and §III defines participation gating as "the special case in which the admissible set is empty". Using a letter for the empty set in the figure that illustrates that mapping is the kind of slip a set-literate reviewer registers immediately. It costs nothing to fix and nothing to leave, except credibility on exactly the point the figure exists to make.

**Manuscript location.** Table I, UNSAFE row.
**Figure location.** Four places — Governance Contract UNSAFE row; C1, C2, C3 UNSAFE lines.
**Correction.** Replace all four with ∅ (U+2205). If the drawing tool's font lacks it, Cambria Math, STIX Two, Latin Modern Math and DejaVu Sans all carry it.

### C-2. The manuscript never states the provenance of the wave CAUTION onset

**Issue.** §IV reads: *"The ocean-state boundary for the small-vessel class follows the operational ceiling reported by [16]."* Singular, and "operational ceiling" names the **UNSAFE** boundary specifically. The classifier uses two wave boundaries — a CAUTION onset and an UNSAFE boundary. The CAUTION onset appears in neither §IV's sourced list nor its researcher-defined list.

**Why it matters.** Before the revision this was partly masked, because §V-B's ±0.25 m analysis was about the wave CAUTION onset and gave it visible standing. That analysis has been removed on your instruction, and the consequence is that the paper now never says where the onset comes from. Since the supervisor's question is precisely "which values are sourced and which are yours", a reviewer tracing the one parameter that most moves the result finds a gap in the provenance list.

The figure is **not** at fault here — "Ocean state (sourced threshold)" is consistent with the manuscript as written. This is a manuscript gap the figure's new precision happens to expose.

**Manuscript location.** §IV, threshold-provenance paragraph.
**Correction, if you want it closed.** One clause, for example: *"The ocean-state boundaries for each vessel class follow the operational ceiling and the corresponding onset reported by [16]"* — but only if [16] does in fact supply the onset. See Author Verification Required.

### C-3. Stage 1 header still carries PRIMARY's period only

"(2020–2024)" sits in the stage 1 title while RESOLUTION covers Oct 2021–Dec 2024. Stage 5 now states both periods explicitly, so the risk of misreading is much reduced. Optional: qualify the header as PRIMARY, or drop the dates from stage 1 and let stage 5 carry them.

---

# PART D — Confidence assessment

| | v3 audit | **v4** | Explanation |
|---|---|---|---|
| **A. Figure ↔ manuscript alignment** | 72% | **94%** | The critical denominator error and both major provenance issues are gone; every number, configuration, category and label now reconciles. The deduction is C-1, a wrong symbol in four places, plus the residual stage 1 header. Nothing semantic remains. |
| **B. Methodological clarity** | 88% | **93%** | Stage 2's provenance markers carry the sourced/researcher-defined distinction into the figure, so a reader working from the diagram alone now gets the same picture as a reader of §IV. Held under 95% only because the figure necessarily compresses four distinct provenances into two labels. |
| **C. Threshold / design-choice traceability** | 76% | **90%** | Both figure-side defects fixed. The remaining gap is C-2 — the wave CAUTION onset's provenance is stated nowhere in the paper. That is one clause away from closed, and it is the only place the provenance chain still breaks. |
| **D. Experimental reproducibility** | 80% | **80%** | Unchanged, and now the lowest score. §IV establishes determinism well — nothing estimated, nothing randomised, identical input reproduces identical output. But the manuscript still never states **how many distinct configurations were evaluated**, which is the literal form of the question that prompted this whole revision. |
| **E. Numerical consistency** | 97% | **99%** | Every figure number matches: 43,848 / 9,135 / 28,501 / 5,935, both periods, the window on both configurations, and all stage-6 categories. The RESOLUTION period that was missing is now present. No orphan or unsupported number. |
| **F. Claim discipline** | 95% | **96%** | Δ*L*₂ reads as binding frequency everywhere. No safety, accuracy, oversight or optimality claim. {Go, Delay} is marked researcher-defined in the figure as well as the text, and the figure now explicitly marks the night→UNSAFE policy the same way. |
| **G. Overall publication readiness** | 82% | **93%** | The manuscript is submission-quality and the figure now tells the same story. Four character replacements and, if you choose, one clause on the wave onset. |

---

# AUTHOR VERIFICATION REQUIRED

### 1. Number of evaluated configurations — still open, still the substantive gap

Unchanged from the previous audit, and now the single largest remaining weakness in the paper rather than in the figure.

§IV answers *why repeated runs are unnecessary*: the replay is deterministic, nothing is estimated from the data, nothing is randomised, and an identical record under an identical configuration reproduces an identical result. That is the right answer to the spirit of "how many times did you run the test?"

It does not answer the count. The manuscript names C0–C3, two environmental-data configurations, three vessel classes, two denominator policies and several threshold settings, but never multiplies them out. Figure 1 does not either.

Keep the two senses apart when you answer:
- **Repeated runs of one identical configuration:** one is sufficient, and the manuscript now says why.
- **Distinct configurations evaluated:** a real count exists and is not stated anywhere in the supplied materials.

**No number has been inserted.** If you want one in the paper, count it from the canonical sensitivity script rather than reconstructing it from the text, and treat it as new information entering the manuscript.

### 2. Does [16] supply the wave CAUTION onset as well as the operational ceiling?

Needed to resolve C-2. If Yaakob et al. provide the per-vessel-class onset alongside the ceiling, one clause in §IV closes the gap. If the onset is a researcher-defined value derived from that source rather than reported by it, it belongs in §IV's researcher-defined list instead. Only you can say which.

---

**Resolved and no longer requiring verification:** the Ø / ∅ question. It is determined — the figure uses Ø, and it needs changing.
