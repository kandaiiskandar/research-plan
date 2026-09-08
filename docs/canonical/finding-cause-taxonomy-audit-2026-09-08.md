# Post-migration `cause` taxonomy audit

**Date:** 2026-09-08  
**Status:** AUDIT COMPLETE — semantic correction recommended; canonical taxonomy NOT migrated.  
**Baseline:** SDR-001 APPLIED; Model B canonical, per [C-8 report](report-c8-migration-2026-09-08.md).  
**Scope:** Provenance semantics and a reviewable correction proposal. No new architecture design change, classifier change, or publication-wide cleanup.

## 1. Verdict

The two-value `cause` taxonomy is semantically inadequate. Add an explicit `policy` trigger, but do not merely insert it into the existing scalar fallback. Define SAFE behaviour and concurrent triggers as well. Recommended representation: a set of active restriction reasons, with component-level detail. This is an annotation of the existing classification, not an input to governance.

The canonical definition remains `cause : Y → {fault, hazard}` until a separate cleanup applies the proposal consistently. The OPEN issue is diagnosed, not closed by this audit.

## 2. Evidence and implementation inventory

| Location | Finding |
|---|---|
| [Appendix C](appendix-c-formalisation.md), C.2.0.8 | `fault` if any non-excluded resolved input is bottom; `hazard` otherwise. OPEN mismatch note retained. |
| Appendix C, C.1 | Already distinguishes environmental, fault and conservative-policy routes to UNSAFE. The two-value taxonomy cannot express its own explanatory framework. |
| Appendix C, C.8.2 and symbol summary | Repeats the two-value provenance contract. |
| [Project instructions](../../CLAUDE.md), formal type table | Repeats `Y → {fault, hazard}`. |
| Appendix C, C.7.2, A3 and proof | Reason-independence is explicit, although examples still enumerate only hazard/fault. |
| [Canonical time classifier](../../scripts/canonical_gt.py), `g_t` | Returns state integers only; valid night and missing solar lookup both return UNSAFE. No reason output. |
| `scripts/` search for the whole word `cause` | No matches. No implemented `cause` function or consumer found in this directory. This is a specification defect, not an observed production logging defect. |
| [C-8 report](report-c8-migration-2026-09-08.md), §23 remaining issues | Explicitly leaves the nighttime mismatch OPEN. |

Searches used `rg -n '\bcause\b' scripts` and `rg -n 'cause :|cause\(|\{fault, hazard\}' docs publications CLAUDE.md`. Historical audit and closure reports are provenance, not active definitions to overwrite.

## 3. Semantic findings

**CT-1 — valid night is mislabelled.** With valid observations, calm weather, and time outside sunrise–sunset, `g_t = UNSAFE` and the residual branch returns `hazard`. The withdrawal is an architectural time policy. The label cannot be read as evidence that an environmental threshold was exceeded. This defect predates SDR-001.

**CT-2 — SAFE also receives `hazard`.** The declared domain is all Y. All-valid, all-SAFE input has no bottom, so it returns `hazard` as well. Calling the function “provenance of a non-SAFE state” does not restrict its written domain. A correction must either declare a partial function or explicitly represent no active restriction. An empty reason set is preferable to another scalar value.

**CT-3 — concurrent reasons are lost.** Fault-first selection suppresses valid weather evidence and night policy when they coexist. A scalar `fault / hazard / policy` needs an arbitrary priority and remains incomplete as an audit record. Night plus wave UNSAFE should preserve both triggers; fault plus night should preserve both if the time inputs remain valid.

**CT-4 — time validity cannot be inferred from state.** Missing clock/date/solar lookup and valid night both return UNSAFE in `canonical_gt.py`. A future annotation must retain resolution validity and solar-lookup status. `g_t == UNSAFE` alone is insufficient to assign `policy`. Missing or invalid dependencies belong to `fault`. File-loading or parsing exceptions are a separate runtime fidelity question; this audit does not certify them as handled.

**CT-5 — the proposed contract needs explicit context.** The current predicate refers to D while its signature shows only Y. Distinguishing active weather triggers also requires vessel-dependent `g_o`, and time policy requires resolved date and solar context. A replacement must name this context or accept an already evaluated component trace, rather than repeat `Y → ...` with hidden dependencies. No redefinition of Y or the classifier is made here.

**CT-6 — `hazard` needs a bounded positive meaning.** Use “valid environmental component in a non-SAFE band”, not “physical danger established”. This includes CAUTION. The medium-vessel interpolation and other conservative threshold choices still require evidence/policy disclosure. Trigger kind and the evidential basis of a threshold are different fields: all governance responses are policy choices, but that does not make every trigger a time-policy trigger. Record the threshold source or policy rationale alongside the component. A future non-environmental policy trigger must be mapped explicitly.

## 4. Recommended semantics — proposal only

Keep the existing resolution and classification pipeline. Let q be its evaluated component trace, carrying component identity, exclusion status, validity, resulting severity, configured vessel context, and time/solar validity. This is proposed provenance data, not a new condition variable or new classifier.

Define a proposed annotation `reasons(q) ∈ P({fault, hazard, policy})`:

1. Include `fault` iff at least one required, non-excluded component or required time dependency failed resolution.
2. Include `hazard` iff at least one valid, non-excluded environmental component in `{w,r,m,o}` is CAUTION or UNSAFE.
3. Include `policy` iff valid canonical time inputs satisfy the nighttime policy, giving `g_t = UNSAFE`.
4. Otherwise the set is empty. Excluded components never contribute a trigger. Missing vessel configuration remains a startup failure and produces no classification record.

This records **all active restriction triggers**, including a lower-severity environmental trigger when another component determines UNSAFE. It is not a partition of binding causes and does not claim causal attribution. Record each component's severity so a consumer can separately identify contributors equal to the aggregate severity. Ties remain ties.

Prefer `policy` over `scheduled`: scheduled describes timing and could mislabel a missing solar lookup; policy identifies the reason for the restriction. A detail such as `nighttime_advisory_policy` makes the generic label intelligible. A fault detail should identify the failed input, and an environmental detail should identify the exceeded band and its provenance.

If the existing name `cause` must be retained, its proposed replacement would be set-valued over the evaluated trace. The exact public name can be settled during cleanup; this audit does not silently introduce a second canonical function.

## 5. Required cases

All examples assume configured v and well-formed D. “Weather” means non-excluded environmental components.

| Case | State | Proposed reason set |
|---|---|---|
| Valid daylight, all weather SAFE | SAFE | ∅ |
| Valid daylight, wave CAUTION | CAUTION | {hazard} |
| Valid daylight, wave UNSAFE | UNSAFE | {hazard} |
| Valid night, all weather SAFE | UNSAFE | {policy} |
| Valid night, wave CAUTION or UNSAFE | UNSAFE | {hazard, policy} |
| Required wave fault, valid daylight, other weather SAFE | UNSAFE | {fault} |
| Required wave fault, valid night, other weather SAFE | UNSAFE | {fault, policy} |
| Required wind fault, valid wave UNSAFE, valid night | UNSAFE | {fault, hazard, policy} |
| Clock/date/solar failure, other weather SAFE | UNSAFE | {fault}; do not infer night |
| `m ∈ D`, raw marine-warning input absent, otherwise daylight SAFE | SAFE | ∅; exclusion is separate scope metadata |
| Exact valid sunrise, weather SAFE | SAFE | ∅ |
| Exact valid sunset, weather SAFE | UNSAFE | {policy} |
| v unconfigured or `t ∈ D` | Startup refused | No classified record |

Example operator wording: “AI advisory unavailable: nighttime policy applies.” For a simultaneous wave trigger, add “Wave reading exceeds the configured band.” Neither wording claims that navigation is legally prohibited or that harm is certain.

## 6. Governance invariance and verification

For any existing resolved input and valid configuration, let `S = F_{D,τ}(obs,v)`. The annotated result is `(S, reasons(q))`. Projecting its first coordinate returns exactly the old S. Consequently `G(S)`, `A_AI(S)` and `RS(S)` are identical pointwise. Reason labels must never select rules, enable the gate, or change the admissible set.

Theorem C.3 continues to use the same three state cases under A1–A4. Fault, policy, environmental and mixed reasons all use the existing UNSAFE case when S is UNSAFE. This is a specification-level invariance argument, not proof that an unimplemented engine obeys its specification.

An abstract exhaustive check covered **12,288 cases**: 16 environmental exclusion sets × 4⁴ environmental statuses (fault/SAFE/CAUTION/UNSAFE) × 3 time statuses (fault/SAFE/UNSAFE). Exclusions were applied first; vessel effects are abstracted into component severity. Every case preserved state projection and the governance pair, had an empty reason set iff SAFE, and satisfied fault ⇒ UNSAFE. All eight subsets of the three proposed labels were exercised. Results: [audit checks](cause-taxonomy-audit-checks-2026-09-08.json).

Enumeration recipe: for each exclusion vector d and status vector x, map excluded components to 0, faults to 2, and valid severities to themselves; take max with the time severity. Derive labels by the three predicates in §4. Check the projection and the existing maps `G=(1,1,0)` and `A_AI=(R,{Go,Delay},∅)`. This checks the proposed abstract contract only; it does not exercise solar computation, raw-input resolution, sensor freshness or a production logger. The sunrise/sunset cases above follow by inspection of the canonical half-open comparison.

No canonical code, classifier thresholds, solar artefacts, prediction register or manuscript was changed. No replay rerun is needed for an audit-only addition. Headline rates remain **5.81% / 4.48%**, outcomes **15 CONFIRMED / 9 REFUTED**, with **3 of 7** flips attributable to SDR-001, as recorded in C-8.

## 7. Bounded follow-through

The next cleanup should update Appendix C C.2.0.8 first, then C.1 cross-references, C.7.2 explanatory wording, C.8.2, the symbol summary and the CLAUDE type table. Retain historical reports. Define and validate the trace contract before claiming any runtime logging behaviour. Close the OPEN taxonomy note only after those active definitions agree. A scalar display summary, if wanted, must retain the full reason set in its audit record.

Metrics must distinguish overlapping active reasons from mutually exclusive counts. Do not retrofit the current weather-driven UNSAFE metric as a `cause` partition or sum overlapping shares to 100%. Do not change registered prediction scopes or values for a provenance-only correction.

Separately queued for the user's next publication consistency audit: the conference Methods paragraph still says 23 confirmed / 1 refuted, and its prototype/Deployment Challenges text retains old hysteresis figures. The older session log still opens “nothing was migrated”; read it as historical and use C-8 for current status. These observed inconsistencies are recorded here without expanding this task into the full manuscript sweep.

**Completion boundary:** semantics audited, correction recommended and invariance checked; taxonomy implementation/migration remains outstanding. Solar citation closure, full manuscript consistency and reviewer audit remain subsequent tasks in the requested order.
