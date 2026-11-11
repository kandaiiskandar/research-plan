# AAI 2026 — Evidence Resolution, Configuration Register and Revision Log

**Date:** 2026-10-07
**Manuscript in:** `aai-2026-manuscript-v2-revised.docx`
**Manuscript out:** `aai-2026-manuscript-v3-evidence-corrected.docx` / `.pdf` — **6 pages**, validated
**Method:** repository evidence inspected first; canonical scripts instrumented and executed; manuscript changed only where evidence established the point.

---

# 1. EVIDENCE FINDINGS

## 1.1 Wave CAUTION onset — **DIRECTLY SOURCE-GROUNDED, but to a source the manuscript did not cite**

**Classification: A — directly source-grounded.** Not [16]. Not researcher-defined.

The decisive record is `docs/canonical/appendix-c-formalisation.md`, line 607:

> *small (< 10 GRT).* The **1.0 m SAFE/CAUTION boundary is Jeong & Im's own proposed restriction for vessels ≤ 10 m LOA (their Table 12)**. The **1.25 m CAUTION/UNSAFE boundary is Yaakob et al.'s (2015) operational ceiling for their 6.54 m Malaysian vessel** — the top of Sea State 3…

And line 60 of the same file:

> Jeong & Im (2023) … **propose a graduated management framework in which vessels ≤ 10 m are restricted at Hs ≥ 1.0 m** and vessels ≤ 24 m at Hs ≥ 2.0 m.

**This is a different paper from [16].** Jeong & Im (2023), *J. Mar. Sci. Eng.* 11(7):1302, DOI 10.3390/jmse11071302, was reference **[19]** in Citation & Evidence Lock v1, classified **"DROP IF SPACE"** — and it was dropped during the six-page compression. The manuscript therefore carried no source for the threshold that determines **when CAUTION occurs at all**, and so drives both Δ<sub>L2</sub> and the 97.6% ocean-state attribution.

The previous sentence — *"The ocean-state boundary for the small-vessel class follows the operational ceiling reported by [16]"* — is true of the **UNSAFE** boundary only. "Operational ceiling" names Yaakob's Sea State 3 ceiling specifically. The CAUTION onset was silently unattributed.

| Value | Class | Source | Status |
|---|---|---|---|
| **1.0 m CAUTION onset** | small | **Jeong & Im (2023), Table 12** — their own proposed restriction for vessels ≤ 10 m LOA | Directly stated by the source |
| 1.25 m UNSAFE boundary | small | Yaakob et al. (2015) — operational ceiling, top of SS3 | Directly stated |
| ~1.875 m alternative reading | small | Yaakob et al. (2015) — failure point, SS4 | Directly stated |
| 1.4 m CAUTION onset | medium | Jeong & Im Hs_KIMO across 10–15 m LOA (1.13 m at 10 m, 1.48 m at 15 m) | **Derived** |
| **2.8 m UNSAFE boundary** | medium | **Interpolated between the small and big rows.** Appendix C: *"No corpus source provides a direct medium-vessel UNSAFE threshold. This is the weakest-grounded value in the table."* | **Researcher-defined** |
| 1.5 m CAUTION onset | big | Corroborated by Jeong & Im Hs_KIMO (1.43 m at 14 m, 1.58 m at 16 m bracket 1.5 m) | Corroborated |
| 3.5 m UNSAFE boundary | big | MET Malaysia Category 1 maximum wave height | Source-grounded |

**Supporting files:** `docs/canonical/appendix-c-formalisation.md` (lines 58, 60, 562, 601, 607, 609); `notes/Proposal of Restrictions on the Departure of Korea Small Fishing Vessel according to Wave Height.md`; `notes/Stability, Seakeeping and Safety Assessment of Small Fishing Boats…md`; `papers/sources/STABILITY, SEAKEEPING AND SAFETY ASSESSMENT…pdf`.

## 1.2 Wave UNSAFE boundary — source-grounded, with a declared design decision

Appendix C line 609 is explicit:

> **Design decision:** the boundary is placed at the operational ceiling rather than the failure point. **Yaakob et al. do not themselves characterise either value as a departure prohibition**… The true limit lies between the last passing test (0.875 m) and the first failing test (1.875 m).

The manuscript already handles this correctly in §V-B — *"two defensible readings… neither is selected here as correct"* — so no change was needed.

## 1.3 Deterministic execution — confirmed by code inspection and by execution

`scripts/sensitivity/threshold_sensitivity.py` and `scripts/condition_comparison.py` contain **no** random number generator, no seed, no sampling, no model fitting. Classification is a chain of `numpy.where` threshold comparisons; Δ<sub>L2</sub> is a count divided by a count. The script's own identity check printed `IDENTITY HOLDS` for both data configurations on re-execution, and every value reproduced exactly.

**One execution per configuration is therefore sufficient.** Repetition could not produce a different number.

## 1.4 Number of distinct configurations — **established**

Determined by instrumenting `run()` in the canonical sensitivity script to log every call with its full parameter dictionary and denominator policy, then executing it.

| Measure | Value |
|---|---|
| **Actual replay executions** (sensitivity script) | **78** |
| **Unique configurations** (data configuration × threshold set × denominator) | **56** |
| Per data configuration | 38 executions, 27 unique (PRIMARY and RESOLUTION alike) |
| Common-period de-confounding runs | 2 |

The 22-execution excess is re-execution of the same configuration where sweeps overlap — the canonical baseline runs 5 times (baseline, rainfall-sweep midpoint, wind-sweep midpoint, two grid cells), and four rainfall settings and three wave pairs run twice each. **These are not additional configurations and were not counted as such**, exactly as the brief required.

Separately, `scripts/condition_comparison.py` classifies each data configuration **once** and then applies the **four** governance configurations (C0, C1, C3, C2) to that single classified record, reporting a 4×4 pairwise divergence matrix on two denominators. The governance configurations are mappings applied to a classification, not separate replays of the data.

**Supporting artefact:** instrumented execution log, 78 entries, retained at `~/instr/exec_log.json` on the device.

## 1.5 Two findings surfaced that the brief did not ask for

**(a) The withheld RESOLUTION pairwise components are produced by the canonical script.** Running `scripts/condition_comparison.py` prints, in the same table and the same run as the PRIMARY values the manuscript does report:

```
RESOLUTION, DEPARTURE WINDOW 05:00-09:00 (n = 5,935)
  C0 vs C1 = 41.08%     C0 vs C2 = 45.56%     C1 vs C3 = 0.00%
```

The manuscript states these are *"not reported because their provenance is incomplete"*. That stated reason is not supported by the scripts, which compute both configurations identically. **No change was made** — Phase 7A placed this decision outside scope — but the justification as written will not survive a reviewer who runs the artefact. See Author Verification.

**(b) An all-hours denominator does exist in the scripts**, printing n = 43,848 and n = 28,501. The manuscript reports only departure-window and daylight-only. This is why the earlier Figure 1 "All hours" bullet was not invented — but it remains correct to have removed it, because the paper reports no all-hours result.

---

# 2. CONFIGURATION REGISTER

Groups follow the actual script structure, not an assumed Cartesian product.

## Script A — `scripts/sensitivity/threshold_sensitivity.py`

| ID | Data config | Governance | Vessel class | Threshold configuration | Denominator | Purpose | Result in paper? |
|---|---|---|---|---|---|---|---|
| A1 | PRIMARY | C1 vs C2 | small | canonical (W 21.6/27.0, R 10/20, O 1.0/1.25) | departure-window | Baseline Δ<sub>L2</sub> + component attribution | **Yes** — 5.81%, 531 h, 518/13 |
| A2–A6 | PRIMARY | C1 vs C2 | small | R_C ∈ {5.0, 7.5, 10.0, 15.0, 19.9} | departure-window | Rainfall sensitivity | **Yes** — 0.48 pp |
| A7–A11 | PRIMARY | C1 vs C2 | small | W_C ∈ {18.0, 20.0, 21.6, 22.0, 25.0} | departure-window | Wind sensitivity | **Yes** — structural zero |
| A12–A17 | PRIMARY | C1 vs C2 | small/medium/big | (O_C, O_U) ∈ {(0.75,1.25), (1.0,1.25), (1.25,1.5), (1.0,1.9), (1.4,2.8), (1.5,3.5)} | departure-window | Wave readings + vessel classes | **Partly** — 9.22%, 1.96%, 1.26% reported; the ±0.25 m pair results are **removed from this paper** |
| A18 | PRIMARY | C1 vs C2 | small | canonical | **daylight-only** | Denominator policy | **Yes** — 9.59% |
| A19–A38 | PRIMARY | C1 vs C2 | small/medium/big | R_C (5) × wave (4) grid | departure-window | Sourced-threshold envelope | **Yes** — 5.67–9.56% |
| A39–A76 | RESOLUTION | — | — | identical 38-execution structure | — | Alternative environmental-data configuration | **Yes** — 4.48%, 0.78 pp, 0.66%, 0.37%, 7.40%, 4.26–6.64% |
| A77 | PRIMARY wave model, common period | C1 vs C2 | small | canonical | departure-window | De-confound wave source from record length | Indirectly — supports §V-A |
| A78 | RESOLUTION wave model, common period | C1 vs C2 | small | canonical | departure-window | Same | Indirectly |

**Executions: 78. Unique configurations: 56** (27 PRIMARY + 27 RESOLUTION + 2 common-period).

## Script B — `scripts/condition_comparison.py`

| ID | Data config | Governance | Vessel class | Threshold configuration | Denominator | Purpose | Result in paper? |
|---|---|---|---|---|---|---|---|
| B1 | PRIMARY | C0, C1, C2, C3 | small | canonical | all hours | 4×4 divergence matrix | No — all-hours not reported |
| B2 | PRIMARY | C0, C1, C2, C3 | small | canonical | departure-window | 4×4 divergence matrix | **Yes** — 42.88%, 48.69%, 5.81%, 0.00% |
| B3 | RESOLUTION | C0, C1, C2, C3 | small | canonical | all hours | 4×4 divergence matrix | No |
| B4 | RESOLUTION | C0, C1, C2, C3 | small | canonical | departure-window | 4×4 divergence matrix | **Partly** — 4.48% and 0.00% reported; 41.08% and 45.56% withheld |

**2 environmental classifications; 4 governance configurations applied to each; 4 reported matrices.**

## Script C — `scripts/canonical_figures.py`

2 data configurations × 2 vessel classes (small, big) = 4 classification computations, producing the headline figure table. Medium is not computed here; the medium results come from A14/A52.

---

# 3. REVISED MANUSCRIPT

`aai-2026-manuscript-v3-evidence-corrected.docx` — **6 pages**, XSD-validated against the original, +1 paragraph.

**Four changes. Nothing else touched.**

### 3.1 §IV provenance sentence — wave CAUTION onset attributed

> **Was:** "The ocean-state boundary for the small-vessel class follows the operational ceiling reported by [16], and the day boundary follows COLREGs Rule 20(b) [17]."
>
> **Now:** "For the small-vessel class, the ocean-state CAUTION onset follows the departure restriction proposed for vessels under 10 m by [16] and the UNSAFE boundary follows the operational ceiling reported by [17]. The day boundary follows COLREGs Rule 20(b) [18]."

### 3.2 Reference [16] added; [16]–[18] renumbered to [17]–[19]

New **[16]** Y. Jeong and N. Im, "Proposal of restrictions on the departure of Korea small fishing vessel according to wave height," *J. Mar. Sci. Eng.*, vol. 11, no. 7, art. 1302, 2023. doi: 10.3390/jmse11071302.

Metadata taken from Citation & Evidence Lock v1 entry [19], already verified there. Nothing invented. Yaakob → [17], IMO COLREGs → [18], DID → [19]; both in-text occurrences of the old [16] updated, IEEE first-appearance order preserved, 19 references cited and listed with no gaps.

### 3.3 §IV procedure paragraph — configuration count added

> **Added:** "Because the replay is deterministic, each configuration is evaluated once rather than repeated: the canonical sensitivity script evaluates 56 distinct combinations of environmental-data configuration, threshold setting and denominator policy, and the four governance configurations are applied to each classified record rather than replayed separately."

No term implying statistical replication was used — no trial, seed, repetition or confidence interval.

### 3.4 🔴 Defect I introduced earlier, now fixed — 38 stray backslashes

The reference list rendered as `\"AI governance: a systematic literature review,\"` — a literal backslash before **every** quotation mark in **all 19 entries**, 38 in total. This came from my own pandoc round-trip during the previous revision step, where markdown escaping leaked into the rebuilt document. It was present in the v2 file I delivered and it rendered in the v2 PDF.

All 38 removed. Verified zero remaining in the rendered text.

I should have caught this when I delivered v2. If you have already circulated that PDF, this is the reason to replace it.

---

# 4. CORRECTED FIGURE 1 — not produced; here is why and what to do

**The Ø → ∅ fix could not be applied to your v4 figure.** It is a raster image, and there is still no editable source for it in the repository — I searched again for `.svg`, `.drawio`, `.pptx`, `.ai`, `.fig` and `.vsdx` and found none. Text in a PNG cannot be edited; redrawing it would replace your styling for the sake of four characters.

**The fix is four character replacements in your figure source:**

| # | Location | Change |
|---|---|---|
| 1 | Governance Contract — UNSAFE row | Ø → ∅ |
| 2 | C1 — UNSAFE line | Ø → ∅ |
| 3 | C2 — UNSAFE line | Ø → ∅ |
| 4 | C3 — UNSAFE line | Ø → ∅ |

Use U+2205. If the figure's font lacks it, Cambria Math, STIX Two, Latin Modern Math and DejaVu Sans all carry it.

**Fallback supplied:** `aai-2026-figure1-v3.png` and `aai-2026-figure1-v3-nocaption.png` already use ∅ throughout and carry identical content to your v4. Use these only if you would rather not edit your source; your v4 styling is otherwise preferable.

---

# 5. REVISION LOG

| Item | Evidence found | Change made | Author verification required? |
|---|---|---|---|
| Wave CAUTION onset provenance | Appendix C line 607: Jeong & Im Table 12, vessels ≤ 10 m restricted at Hs ≥ 1.0 m | §IV sentence split; Jeong & Im added as [16] | **No** — established |
| Wave UNSAFE boundary provenance | Appendix C lines 562, 607: Yaakob operational ceiling (SS3 top) | Attributed to [17] in the revised sentence | No |
| Operational ceiling vs failure point | Appendix C line 609: explicit design decision; Yaakob characterises neither as a prohibition | None — §V-B already states both readings and selects neither | No |
| Deterministic execution | No RNG, seed or sampling in either canonical script; identity check passes on re-execution | Count sentence added to §IV | No |
| Configuration count | Instrumented execution: 78 executions, 56 unique | "56 distinct combinations" stated in §IV | No |
| Reference renumbering | — | [16]→[17], [17]→[18], [18]→[19]; both in-text [16] occurrences updated | No |
| Stray `\"` escapes | 38 literal backslashes rendering in all 19 reference entries, present in v2 | All removed | No |
| **Medium-vessel UNSAFE boundary (2.8 m)** | Appendix C: **interpolated between the small and big rows**; *"no corpus source provides a direct medium-vessel UNSAFE threshold… the weakest-grounded value in the table"* | **None** — flagged only | **YES** |
| **Withheld RESOLUTION pairwise components** | `condition_comparison.py` prints 41.08% and 45.56% in the same run as the reported PRIMARY values | **None** — out of scope per Phase 7A | **YES** |
| Figure 1 Ø → ∅ | Confirmed Ø (U+00D8) at magnification in four places | **None possible** — raster, no source | **YES** |

---

## AUTHOR VERIFICATION REQUIRED

### 1. Medium-vessel UNSAFE boundary is interpolated, and the paper does not say so

The manuscript reports the medium-vessel variant (1.96% PRIMARY, 0.66% RESOLUTION) as a deterministic configuration variant. Its CAUTION onset (1.4 m) is derived from Jeong & Im's formula, but its **UNSAFE boundary (2.8 m) is interpolated** — your own Appendix C calls it *"the weakest-grounded value in the table"* and records it as a threat to internal validity.

If a reviewer asks where 2.8 m comes from, the honest answer is "interpolated". The paper currently offers no answer at all. One clause in §V-C would close it, for example noting that the medium-vessel UNSAFE boundary is interpolated rather than sourced. **I did not add it** — it concerns a robustness-disclosure variant rather than the headline, it costs space at exactly 6 pages, and the brief asked for minimal evidence-supported edits. Your call.

### 2. The stated reason for withholding the RESOLUTION pairwise components is not supported

§V-A says they are *"not reported because their provenance is incomplete"*. `condition_comparison.py` computes and prints 41.08% and 45.56% in the same table and the same execution as the PRIMARY values the paper does report. Either report them, or restate the reason for withholding them in terms the artefact supports. **Unchanged** — Phase 7A explicitly placed this outside scope, and reversing it would touch Table III, the table note and §V-A together.

### 3. Figure 1 empty-set glyph

Four character replacements in your figure source, as listed in section 4. Cannot be done from a raster.

---

## FINAL CONSISTENCY CHECK

| Check | Result |
|---|---|
| Wave CAUTION onset provenance explicitly resolved | **PASS** — attributed to [16] Jeong & Im |
| No unsupported source claim added | **PASS** — every attribution traced to Appendix C and the project's own citation lock |
| Source-grounded and researcher-defined remain distinguishable | **PASS** — §IV's researcher-defined list is unchanged and still enumerated |
| Configuration count stated only if verified | **PASS** — 56, from instrumented execution |
| Deterministic replay not described as statistical replication | **PASS** — no trial, seed, repetition or interval language |
| No random trials or confidence intervals invented | **PASS** |
| ±0.25 m analysis remains removed | **PASS** — absent from the rendered PDF |
| 2.54–14.75% remains removed | **PASS** — absent |
| Figure 1 uses ∅ | **NOT DONE** — see section 4 |
| C0–C3 unchanged | **PASS** |
| Δ<sub>L2</sub> definition unchanged | **PASS** |
| PRIMARY and RESOLUTION results unchanged | **PASS** |
| Claim boundaries unchanged | **PASS** |
| Governance activation not read as safety effectiveness | **PASS** |
| Page count | **6** — unchanged, at the limit |
