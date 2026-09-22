# Open Issues Log

Working log of unresolved inconsistencies and deferred repairs found while preparing analysis documents. Each entry records what the issue is, where both sides of it live, what would resolve it, and what is blocked in the meantime.

This is a working document, not a canonical one. An entry that needs canonical authority should be escalated to the open-items table in `publications/active/journal-1/evaluation-specification.md` §17.

---

## ISSUE-1 — PRIMARY/RESOLUTION spread is attributed to grid resolution in one place and left unattributed in another

**Raised:** 2026-09-21, while drafting [`experiment-report-delta-l2.md`](experiment-report-delta-l2.md)
**Status:** ✅ **RESOLVED 2026-09-21** — by common-period comparison (see Resolution below)
**Type:** Internal inconsistency between canonical documents

### The inconsistency

The PRIMARY and RESOLUTION configurations differ in **two** respects at once:

| | PRIMARY | RESOLUTION |
|---|---|---|
| Wave model | ERA5-Ocean, ~50 km | MFWAM, ~8 km |
| Record length | 5.00 yr (43,848 hr) | 3.25 yr (28,501 hr) |

Δ_L2 moves from 5.81% to 4.48% across them — a spread of roughly 1.3 percentage points. The two canonical sources disagree about what that spread may be called.

**Attributes it to grid resolution** — `docs/canonical/empirical-findings-2026-09-06.md` §0a:

> **The 1.3-point gap between the columns IS the grid-resolution sensitivity** (F-14). Report it as a robustness result, not as uncertainty about which number is true.

**Declines to attribute it** — `publications/active/ipsci-2026/submissions/v4-amict-rebuild/manuscript.md` §V.C:

> The configurations differ in both wave model and record length; this evaluation does not isolate which difference accounts for the observed spread.

### Why it matters

Calling the spread "the grid-resolution sensitivity" asserts a cause the evaluation design cannot separate. The comparison is confounded: a 1.3-point move could come from the finer wave model resolving nearshore island sheltering, from the shorter record sampling a different stretch of weather, or from both. §0a's own supporting argument — that the coarse cell averages open water the finer model resolves as sheltered — is a plausible mechanism, not an isolation of one.

The reviewer-facing risk is direct: anyone who notices that 5.00 yr ≠ 3.25 yr can ask why a difference in record length is being reported as a property of grid resolution.

### What would resolve it

Either of:

1. **Isolate the variable.** Re-run both wave models over the **common 28,501-hour overlap** so record length is held constant. The spread that survives is then attributable to wave model alone. The data for this already exists — §0a already notes both maxima fall inside the overlap window.
2. **Adopt the v4 wording as canonical.** Amend §0a to report the spread without causal attribution, and record F-14 as a confounded comparison. Cheaper, and loses only a claim that was not established.

Option 1 is the stronger result and is a bounded piece of work. Option 2 is correct immediately.

### Resolution (2026-09-21)

Option 1 was executed. Both wave models were run over the **common 28,501-hour overlap**, holding record length constant (`scripts/sensitivity/threshold_sensitivity.py`):

| Effect | Value |
|---|---|
| Wave-model / data-resolution effect, record period held constant | 6.45% − 4.48% = **+1.97 points** |
| Record-length effect, wave model held constant | 5.81% − 6.45% = **−0.64 points** |
| Combined = reported spread | 1.97 − 0.64 = **1.33 points** |

**The two effects operate in opposite directions.** The like-for-like grid-resolution sensitivity is 1.97 points; the original concern — that 1.33 points confounded two factors — is confirmed, and the magnitude was understated rather than overstated. No empirical value changed; only the interpretation of the difference.

### Current handling

- `experiment-report-delta-l2.md` §9.1 now carries the decomposition.
- `docs/canonical/empirical-findings-2026-09-06.md` §0a **corrected 2026-09-21** with the decomposition block.
- `docs/canonical/session-log-2026-09-06.md` annotated as superseded; not rewritten.
- No empirical value is affected either way. Δ_L2 = 5.81% / 4.48% stands regardless; only the interpretation of the difference between them is at issue.

### Blocks

Nothing immediately. It should be settled before the spread is described causally in any submitted document.

---

## ISSUE-2 — §3.1's observation-semantics conjunct is not supported by coded evidence

**Raised:** 2026-09-21, during the §3.2 multidimensional recoding
**Status:** OPEN — affects the wording of the gap claim
**Type:** Evidence gap

§3.1 claims that no reviewed treatment combines three things, the second being **"explicit observation-resolution and exclusion semantics"** (handling of invalid, absent, stale and unmeasured inputs).

**No source in the reviewed set has been coded for this dimension.** The per-paper extraction notes code governed object, conditioning variable, governance point, authority and participation/scope levels. None codes observation-quality or exclusion semantics. The conjunct is therefore an **absence of coding, not a coded absence** — the evidence base cannot presently support or refute it.

This is the weakest of the three conjuncts and the easiest for a reviewer to test by opening any one of the reviewed papers.

**Resolution:** either code the dimension across the existing eleven sources (bounded — the papers are already read and the notes already exist), or drop the conjunct from §3.1 and rest the claim on the two conjuncts that are coded.

---

## ISSUE-3 — §3.1 requires narrowing in light of the recoded evidence

**Raised:** 2026-09-21
**Status:** OPEN — proposed wording below, **not applied**; §3.1 is unchanged
**Type:** Claim exceeds coded evidence

The §3.2 recoding establishes that each element of the current gap claim has precedent in the reviewed set:

| Element | Already established by | On what terms |
|---|---|---|
| Advisory-type restriction by external state, human-facing | FAA (2017) | Single-component banded state; authority procedurally constrained |
| Multi-component classified state → nested admissible sets, participation and scope in one gate | Baxi (2026) | Conditioning variable is AI robustness; governed object is autonomous agent action |
| Unconditional human final authority | Kwon & Kim (2026) | Governs participation only |
| Environmental conditioning of runtime governance change | Bernabei & Costantino (2024) | Governs function allocation |
| Comprehensive governance of AI output | Shamsujjoha et al. (2025) | Content filtering, not state-conditioned category admissibility |
| Formal verification of state-conditioned advisory logic | Cleaveland et al. (2023) | Collision-freedom, not containment over an admissible set |

**Assessment: REQUIRES NARROWING.** The claim is not contradicted — no source combines the elements — but as written it implies more distance from prior work than the coding supports, and its "defined independently of the generator" and "multi-component" phrases are doing work that the word **environmental** actually does.

**Narrowest defensible alternative (proposed, not applied):**

> Within the reviewed literature, advisory-type restriction conditioned on an externally measured state is established in certified collision-avoidance avionics, and graduated admissibility over a multi-component classified state with participation and scope unified in a deterministic gate is established for AI-internal robustness conditioning. No reviewed treatment was identified that conditions **human-facing advisory-category admissibility on a classified multi-component external environmental state**, with participation and advisory scope specified as separate functions and final decision authority held unconditionally by the human.

**What actually differentiates the architecture, on current evidence:** the *conjunction* of (a) external multi-component environmental conditioning, (b) a human-facing advisory-category governed object, and (c) unconditional human authority. The formal structure, the graduated admissibility and the pre-inference application are **not** differentiators — Baxi has all three.
