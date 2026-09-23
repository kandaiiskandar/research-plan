# AMICT Conference Manuscript V4 — Task Readiness Analysis

**Date:** 2026-09-14
**Analyses:** `docs/tasks/AMICT CONFERENCE MANUSCRIPT V4 — EVIDENCE-LED SIX-PAGE DRAFT.md`
**Status:** PRE-EXECUTION ANALYSIS ONLY. No manuscript drafted. `v4-amict-rebuild/` does not exist. Nothing modified.
**Companions:** [readiness](amict-conference-rebuild-readiness-analysis.md) · [source validation](amict-source-validation-readiness-analysis.md) · [contribution freeze](amict-contribution-freeze-v2-readiness-analysis.md) · [RQ freeze](amict-rq-narrative-freeze-readiness-analysis.md)

---

## 1. What the task is

The drafting task. Everything scientific is frozen; this executes it. The task is unusually well-specified — title, RQs, gap statement and novelty sentence are given verbatim, the section allocation is the lower bound from the narrative freeze, and forty numbered constraints govern the rest.

Most stop conditions are already discharged by the preceding gates. **Two are live, and both are about space.**

---

## 2. The budget does not close as specified

The narrative freeze costed *prose plus visuals*. The V4 task adds two components that were not in that arithmetic: **an abstract** (§33) and a **reference list** (§35). Both consume column space.

### 2.1 Full accounting

Six pages at ~900 words per page ≈ **5,400 words of column space**.

| Component | Words |
|---|---|
| Title, abstract (~200), keywords | ~225 |
| Body prose (§25 lower bound) | 3,880 |
| Visuals (§26, three) | ~630 |
| References | *variable* |

**v3's reference list is 40 entries / 1,205 words.**

| References | Visuals | Total | vs 5,400 |
|---|---|---|---|
| 40 (v3 as-is) | 3 | 5,940 | **over by 540** |
| 40 (v3 as-is) | 2 | 5,790 | over by 390 |
| 30 | 3 | 5,635 | over by 235 |
| 30 | 2 | 5,485 | over by 85 |
| 25 | 3 | 5,485 | over by 85 |
| **25** | **2** | **5,335** | **FITS** (~65 words slack) |

**Only one configuration fits.** Drafting to §25's word targets while inheriting v3's reference list overruns by roughly half a page.

### 2.2 The uncosted lever: reference-list pruning

§35 governs reference *style* — numbered brackets, validated metadata, AC 20-151C not 20-151A, Cleaveland not Cleveland. It says nothing about reference *count*.

But the count is a first-class compression lever. v3's 40 references support six literature-review subsections that §22 deletes. A table-led Related Work across seven families needs roughly 10–12 precedent citations, plus threshold and domain sources, plus governance framing, plus provenance citations — realistically **25–30 entries**. Pruning 40 → 25 recovers **~450 words**, more than any single prose cut available.

**Recommendation:** treat the reference list as a budgeted section with a target of ~25 entries, and have the drafting report record the count. Every dropped reference should be one whose only anchor was a deleted subsection.

### 2.3 The visual trade-off is sharper than §26 implies

§26 caps visuals at three and ranks them: Related Work table, Results table, architecture figure — dropping the architecture figure first when tight.

In the only fitting configuration there are **two** visuals, so the architecture figure is gone. That leaves no slot for a compact operational-semantics table — and Section III is where the compression pressure is worst (§3).

Two defensible options:

- **(a) Two visuals** — Related Work table + Results table. Fits with ~65 words slack. Section III carries all operational semantics in prose.
- **(b) Three visuals**, substituting a compact operational-semantics table for the architecture figure. Over by 85 words, recoverable from Conclusion (180 → 160) and Introduction (450 → 420).

**Recommend (b).** A four-row table of ⊥ condition × response carries the invalid/absent/stale/unmeasured semantics in ~120 words of column space where prose needs ~250, so the net is favourable and the content is clearer. It is also consistent with §26's own ranking — the architecture figure is the one marked expendable, and two figure assets already exist on disk (`graphic_architecture.png`, `proposed_diagram.png`) if it is ever restored for the journal version.

---

## 3. Section III is the hardest constraint in the task

§25 allocates Section III **750 words**. §13 places the implementation-fidelity block **inside** Section III. At ~150 words for the fidelity block plus its mandatory disclosures, formalisation proper gets **~600 words**.

§11 requires, concisely, in those 600 words:

- five notation objects — `S = f(E)`, `(G(S), A_AI(S))`, `Obs_i = (X_i × 𝕋) ∪ {⊥}`, `ρ_{D,τ}`, `F_{D,τ} = f ∘ ρ_{D,τ}`
- thirteen operational-semantic requirements — three fault routes, declared exclusion, exclusion-before-fault, `D` fixed and declared, `t ∉ D`, excluded component pinned SAFE, lower bounds when `D ≠ ∅`, operational totality, ideal-versus-deployed distinction, pre-reasoning `RS(S)`, no post-generation filter
- four formal properties stated compactly

That is **~22 distinct technical items in ~600 words — roughly 27 words each.** Achievable only with a table doing part of the work, which is the argument for option (b) in §2.3.

**This is also where §32's failure condition bites.** Results is 900, Section III is 750: only **150 words of margin** before `DRAFT_STRUCTURE = FAIL`. Given how much Section III must carry, overrun there is the single most likely way to trip that check.

**Recommendation:** draft Section V (Results) first, fix its length, then draft Section III against the remaining ceiling. Drafting III first invites it to expand into the space Results needs.

---

## 4. Smaller findings

**No v4 exists.** The convention is `vN-<label>` (`v1-initial-submission`, `v2-post-review`, `v3-revision`), so `v4-amict-rebuild/` fits cleanly. §2's conditional resolves to "create it".

**v3 has no abstract.** §33's abstract is entirely new content with no reusable source. The original rebuild task's template constraints — no symbols, special characters, footnotes or mathematics in title or abstract — still apply, so plain-text forms are required: *multi-component environmental state*, *participation gating*, *advisory-scope restriction*, never `A_AI(S)` or `F_{D,τ}`.

**Double-blind is a standing constraint the V4 task does not restate.** The original rebuild task §12 requires that author identities not appear in the text body. The drafting report should confirm it explicitly alongside the other checks in §38.

**The AMICT template is still absent** — flagged in the first readiness analysis and never resolved. §2 forbids `.docx`/`.tex`, so it does not block drafting, but it means the six-page claim remains a **word-budget proxy, not a measurement**. The drafting report should say so rather than assert a six-page fit.

**Compression scale.** v3 carries seven tables and four figures. V4 carries two or three visuals. That is a reduction from eleven to two or three, on top of the 62% prose cut — worth stating plainly so the drafter treats this as rebuilding, not trimming.

---

## 5. Stop-condition pre-assessment

| # | Condition | Assessment |
|---|---|---|
| 1 | Frozen C1/C2 must change for coherence | **Does not fire** |
| 2 | An RQ requires new evidence | **Does not fire** — all three rest on closed evidence |
| 3 | Lower-bound structure cannot fit without deleting a protected disclosure | **LIVE but manageable** — fits only at ~25 references with two visuals, or three visuals with ~85 words recovered from prose (§2). No disclosure need be cut |
| 4 | Results cannot remain the largest prose section | **LIVE** — only 150 words of margin over Section III (§3). Mitigated by drafting Results first |
| 5 | A required citation lacks validated support | **Does not fire** — all six load-bearing sources are registered in `citation-notes-map.md` and resolve to notes |
| 6 | Draft requires E5/H3 | **Does not fire** |
| 7 | Novelty only achievable by omitting the avionics precedent | **Does not fire** — the gap statement and novelty sentence are given verbatim and both name the precedent |
| 8 | Numerical conflict | **Does not fire** |
| 9 | Draft requires the provenance-incomplete RESOLUTION pairwise values | **Does not fire** — RQ3 rests on ΔL2 RESOLUTION 4.48% and C1↔C3 RESOLUTION 0.00%, both provenanced |
| 10 | Post-review literature indistinguishable from the 72-paper review | **Does not fire** — the reporting rule is frozen |

---

## 6. Points to settle before drafting

1. **Reference target.** Adopt ~25 entries as a budgeted figure and record the count in the drafting report (§2.2).
2. **Visual configuration.** Option (a) two visuals, or option (b) three with an operational-semantics table replacing the architecture figure — recommend (b), with ~85 words recovered from Conclusion and Introduction (§2.3).
3. **Drafting order.** Results before Formalisation, to protect §32 (§3).
4. **Confirm double-blind** in the drafting report alongside §38's other checks (§4).
5. **State the page-count caveat** — word budget as proxy, template still absent (§4).

---

## 7. Verdict

**Executable.** Eight of ten stop conditions are discharged; the two live ones are both space constraints with identified mitigations that cost no protected content.

The task's own §25 targets are correct but incomplete: they cost prose and assume the rest follows. Adding the abstract and a realistic reference list, **the six-page envelope closes in exactly one configuration** — around 25 references with two visuals, or three visuals with ~85 words recovered. Deciding that before drafting, rather than discovering it at the end, is what keeps the protected disclosures intact.

Section III is the hardest writing problem in the task: roughly 22 technical items in ~600 words, under a 150-word margin against the section that must stay larger.

---

## 8. Files inspected

Read-only. Nothing modified; no manuscript or task artefact created.

- `docs/tasks/AMICT CONFERENCE MANUSCRIPT V4 — EVIDENCE-LED SIX-PAGE DRAFT.md`
- `data/amict-conference-rebuild/` — all eight artefacts
- `publications/active/ipsci-2026/submissions/` — version naming; `v3-revision/manuscript-v3.md` reference and visual inventory
- `docs/canonical/citation-notes-map.md` — load-bearing source registration
- `docs/tasks/AMICT CONFERENCE PAPER REBUILD — ARCHITECTURE TO EMPIRICAL EVALUATION.md` — template and double-blind constraints
- `docs/images/architecture/` — existing figure assets
