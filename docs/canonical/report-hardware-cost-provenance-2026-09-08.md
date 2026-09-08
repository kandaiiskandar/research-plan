# Hardware-Cost Provenance Resolution Report

**Date:** 2026-09-08  
**Outcome:** **C — unsupported number.**  
**Scope:** Resolve the hardware-cost SC-3 only. No Publication Consistency Audit resumption, Solar Citation Closure or architectural work.

## 1. Claim and locations

The claim investigated was “The target deployment hardware is commodity smartphones or low-cost single-board computers (under USD 50).”

| Location before cleanup | Role | Disposition |
|---|---|---|
| Conference v3, Deployment Challenges, line 504 | Active working manuscript | Remove numerical parenthesis only |
| `supervisor-feedback-response.md`, Point 7, line 204 | Supporting response text still used to prepare revisions | Remove numerical parenthesis only |
| Conference v2.5 submitted, line 378 | Historical submission | Preserve unchanged |
| Previous Publication Consistency Audit report/evidence | Historical record of the stop | Preserve unchanged; this report records resolution prospectively |

## 2. Search and Git provenance

The repository search covered tracked textual canonical/supporting documents, publication notes, research notes, planning/implementation files, historical manuscripts, scripts and data, including synonyms for hardware and budget. No grant/budget decision, bill of materials, priced configuration, cost citation or hardware test establishing USD 50 was located. Search hits and exact search terms are stored in [repository-search.json](../../data/hardware-cost-provenance/repository-search.json). Binary PDF contents were not separately searched; the imported response PDF is preserved, with its Markdown source and history inspected. No retail shopping or new external evidence was used.

`git log --all -S` searches for `USD 50` and `$50`, broader `-G` inspection, commit inspection and blame traced the statement to:

| Commit | Author / authored date | Finding |
|---|---|---|
| `8ddf83d924b7ea8cd760239c5b44632daa816f0f` | iskandar, 2026-09-02 09:16:08 +08:00 | Earliest located Git introduction: adds both the submitted v2.5 Markdown and supervisor response containing the price claim. Neither passage has a cost citation or documented budget rationale. |
| `2a0e32f3766a055a714d07166ee566326ab13d5e` | iskandar, 2026-09-06 09:00:23 +08:00 | The claim appears in the conference v3 working manuscript. No new cost evidence establishes it. |

The imported response says Point 7 was completed **2026-08-20**. That is an internal document date, not an earlier located Git introduction. Both relevant texts arrived in the same located commit, so their exact copying direction and original authoring event cannot be reconstructed from that import. Git author metadata identifies the committer/author record, not who scientifically chose the figure. Repetitions establish propagation, not independent validity.

Exact command outputs and the original response text are stored in [git-provenance.json](../../data/hardware-cost-provenance/git-provenance.json). Earliest *located* introduction is deliberately distinguished from the unknowable first drafting event.

## 3. Classification and scientific justification

**Selected outcome: C only.** No device/configuration, dated source, currency-inclusive bill of materials or empirical price result supports Outcome A. No prior explicit affordability-budget decision, inclusions/exclusions or rationale supports Outcome B. The number must not be retroactively turned into a researcher-chosen budget assumption.

The USD 50 precision adds no identified requirement, experiment parameter or theoretical constraint. Removing it preserves the intended qualitative deployment discussion without substituting another arbitrary number. This is a publication provenance repair; it does not prove hardware suitability or affordability.

## 4. Smartphones, SBCs and architecture scope

[Low-resource justification](../justification/low-resource-environments.md) §§1.1–1.2 describes constrained data, connectivity, compute, institutional capacity and finance, alongside existing mobile-device use. That supports a qualitative device context, not a USD 50 budget. It does not establish that every participant already owns a suitable phone or that incremental phone deployment costs are zero.

A phone already owned by a participant and a newly purchased SBC have different acquisition-cost implications. No documented total-cost accounting covers storage, power, enclosure, sensors, peripherals, connectivity or maintenance. This report does not invent inclusions/exclusions.

Appendix C's governance definitions are hardware-independent and contain no mandatory SBC purchase or cost ceiling. The SBC is an implementation possibility in deployment prose, not a formal architecture requirement. No canonical Android-only or mobile-first requirement was located; those possibilities are not asserted as established choices here. The minimal edit retains device classes without claiming tested hardware or a cost cap.

## 5. Scientific-impact questions

| Question | Evidence-based answer |
|---|---|
| 1. Is USD 50 part of the architecture? | No such dependency occurs in the inspected formal specification. It appears in descriptive deployment prose. |
| 2. Is it a formal requirement? | No canonical cost requirement or prior explicit budget decision located. |
| 3. Is it an evaluated hypothesis? | No. Register entries and research-design hypotheses do not establish a USD 50 hardware test. |
| 4. Was a prototype tested on sub-USD-50 hardware? | No such test record was located. The working manuscript discloses the unimplemented reasoning engine; costed hardware fidelity is not established. |
| 5. Does an experiment depend on the figure? | No identified experiment or calculation reads the cost value. The empirical scripts classify environmental records. |
| 6. Do empirical results change if it is removed? | No; calculation artefacts/scripts and findings are byte-identical. |
| 7. Do theorems change? | No; formal definitions and proofs are byte-identical. |
| 8. Does novelty change? | No; the governance pair and admissible-scope claim have no identified dependence on a purchase-price ceiling. |
| 9. Is low-resource operationalised elsewhere measurably? | The justification supplies five qualitative constraint dimensions; design plans include measurable latency/overhead aims (one bound remains `[X ms]`) and analytical complexity. No unified measured hardware affordability cut-off or completed sub-USD-50 feasibility validation was located. Those concepts are not interchangeable with a dollar budget. |

## 6. Exact active edits

Conference v3:

- **Before:** “The target deployment hardware is commodity smartphones or low-cost single-board computers (under USD 50).”
- **After:** “The target deployment hardware is commodity smartphones or low-cost single-board computers.”

Supervisor response:

- **Before:** “Target deployment: commodity smartphones or low-cost single-board computers (< $50).”
- **After:** “Target deployment: commodity smartphones or low-cost single-board computers.”

Only the two numerical parentheses were removed. Other sentences, including stale values awaiting the resumed audit, were not corrected. Historical response completion dates were not rewritten. The historical submitted manuscript and imported PDF remain provenance copies, not updated working exports.

## 7. Integrity and files

Existing source files modified: the two active texts listed above only. New evidence: `data/hardware-cost-provenance/{integrity-before.json,integrity-after.json,git-provenance.json,repository-search.json,resolution.json}` and this report.

The snapshot contains 483 tracked files; **481 are unchanged**. It includes all tracked classifier scripts, solar artefacts, Appendix C, CLAUDE, empirical findings, prediction register, prior audit table and numeric queue. Pre-existing user changes to `data/.DS_Store` and `docs/.DS_Store` were preserved and excluded from commits, not reset.

| Frozen item | SHA-256 before | SHA-256 after |
|---|---|---|
| `data/prediction-register.csv` | `5574b88ea65168b6ef5e308629f3eb14fb70f8688a592fde279103ea4b37eae6` | `5574b88ea65168b6ef5e308629f3eb14fb70f8688a592fde279103ea4b37eae6` |
| `scripts/canonical_gt.py` | `b330bf9f94e848aad282a71d226c85c7e73f4ec8c0f2f8c88bfd7112b6e9a577` | `b330bf9f94e848aad282a71d226c85c7e73f4ec8c0f2f8c88bfd7112b6e9a577` |
| `data/solar/solar-events-daily.csv` | `057c46a19d0e8ea7956cdc38ae3d7615cf43cf800e7bc33ab286dfdc20ce1894` | `057c46a19d0e8ea7956cdc38ae3d7615cf43cf800e7bc33ab286dfdc20ce1894` |
| `docs/canonical/appendix-c-formalisation.md` | `03e80802a46404df90c3e36960feab298e9036396f3f3a5d64e956a5b3c6cfb4` | `03e80802a46404df90c3e36960feab298e9036396f3f3a5d64e956a5b3c6cfb4` |
| `docs/canonical/empirical-findings-2026-09-06.md` | `667161e288d5e403ac068edab31b21c86c8694ca6fa6b35288ae2096f685b556` | `667161e288d5e403ac068edab31b21c86c8694ca6fa6b35288ae2096f685b556` |

Full manifests: [before](../../data/hardware-cost-provenance/integrity-before.json), [after](../../data/hardware-cost-provenance/integrity-after.json). [Resolution record](../../data/hardware-cost-provenance/resolution.json) names the authorised two-file delta.

The register remains **24 entries — 15 CONFIRMED / 9 REFUTED**. Canonical figures remain **PRIMARY 5.81% / RESOLUTION 4.48%**. No replay, prediction revision, threshold change, formal governance edit or solar calculation occurred.

## 8. Stop conditions and audit handoff

HC-1: no conflicting authoritative budgets located. HC-2: no material research requirement depending on the number located; removal is descriptive only. HC-3: no tied cost experiment located. HC-4: no deployment redesign required. None is triggered.

**Publication Consistency Audit SC-3 is cleared for this hardware-cost claim.** The other audit findings remain unresolved; this is not closure of the Publication Consistency Audit.

The audit evidence was first committed on `chore/publication-consistency-audit` (`8adf9b0`). Resolution was prepared on `chore/resolve-hardware-cost-provenance`; retain both branches and integrate the resolution into the audit branch. The previous report and finding table describe the pre-resolution state and remain unchanged. When the audit resumes, use its existing finding table and quantitative coverage queue, accounting for the approved delta in this resolution record. The old audit integrity builder intentionally checks the pre-edit baseline, so do not mistake its expected detection of these authorised edits for new evidence corruption.

Per the attached subtask's explicit stop instruction, the full audit is **not resumed within this task**. Solar Citation Closure and Full Reviewer Audit remain unstarted.

# `HARDWARE-COST PROVENANCE RESOLVED — SC-3 CLEARED`
