# Finding: `⊥` Conflates Four Conditions, and Two of Them Break the Evaluation

**Date:** 2026-09-08
**Status:** **Source of truth** for the semantics of absent, invalid, stale and unmeasured observations. Written **before** the operational-totality extension, because that extension cannot be specified correctly until this is settled.
**Trigger:** an audit of `⊥` semantics requested prior to implementation, following the observation that Theorem C.1 is total over ideal domains only.

---

## 1. The headline problem

**The fail-safe rule, as currently stated in the project's own documents, would make `f(E) = UNSAFE` for 100% of the empirical record.**

`docs/justification/viva-formalisation-architecture.md` states the rule and its rationale explicitly:

> *"The marine warning variable m makes the rationale clearest: if the broadcast channel is unavailable, m is ⊥ rather than `none`, because communication failure cannot be interpreted as confirmation that no warning is in force. Reading silence as safety is precisely the failure mode the fail-safe exists to prevent."*

Every historical replay in this project holds **`m = none` for all 43,848 hours**, because no marine warning archive exists for the site (Q2, F-11 standing caveat). That is exactly the case the document says must be `⊥`.

Applied literally: `g_m(⊥) = UNSAFE`, aggregation is by maximum, therefore `f(E) = UNSAFE` at every hour, and **the 7.72% Level 2 binding rate — the headline result of the thesis — would be meaningless.**

The resolution exists but is written nowhere:

| Setting | `m` unavailable means | Correct response |
|---|---|---|
| **Deployed system**, live broadcast channel | The channel failed *now*. A warning may be in force and we cannot see it | `⊥` → UNSAFE. Silence is not safety |
| **Retrospective replay**, no archive ever existed | The variable was never observable for this study | A **declared scope exclusion**: pin at lowest severity, state that all figures are lower bounds |

Two different settings, two different correct answers, one symbol. The contradiction has been invisible because **appendix-c — the canonical source — contains no `⊥`, no fail-safe rule, and no treatment of undefined input at all.** The rule lives only in the manuscript (asserted twice as an architectural property), the viva document (numbered "EC-1" as though specified), and an explainer.

---

## 2. The second breaking case: `o` is a tuple

`o = (wave height, swell period)`. No collected data file contains a usable swell period:

| File | Columns |
|---|---|
| `raw_marine.csv` (v1) | `swell_wave_period (undefined)` — present but empty |
| `raw_marine_era5_sea.csv` | no swell column at all |
| `raw_marine_mfwam.csv` | no swell column at all |

Under a naive **per-variable** `⊥` rule, `o = ⊥` for the entire record, and again everything classifies UNSAFE.

This forces a decision the specification has never made: **is `⊥` a property of the variable, or of the inputs the classifier actually reads?** `g_o` uses the wave height component only (C.9.3). If `⊥` attaches to what `g_o` reads, `o` is fine; if it attaches to the declared variable, `o` is permanently undefined.

**Related stale caveat, found during this audit.** The standing-caveats table in `empirical-findings-2026-09-06.md` reads *"Swell period columns are entirely NaN."* That is true of the *swell* columns but misleading: `wave_period` is **fully populated** — 43,848/43,848 in ERA5-sea and 28,477/28,512 in MFWAM. F-12 already recorded this ("`wave_period` IS fully populated and unused") and the caveat table was never updated.

---

## 3. The four conditions currently collapsed into one symbol

| # | Condition | Detectable from `xᵢ` alone? | Warrants UNSAFE? | Currently |
|---|---|---|---|---|
| **A** | **Invalid** — outside physical range (−5 kn, 500 kn) | **Yes** | **Yes** — the reading is known wrong | `⊥` |
| **B** | **Absent** — sensor offline, provider unreachable now | **Yes** | **Yes** — no information about a variable that normally has some | `⊥` |
| **C** | **Stale** — last reading is 6 hours old | **No.** Requires an observation timestamp and a freshness policy | Arguable, and policy-dependent | `⊥` |
| **D** | **Unmeasured** — the variable was never observable in this deployment (`m`) | **No.** A property of the deployment, not of any reading | **No** — this is a permanent scope limitation, not a runtime fault | `⊥` |

**A and B are the genuine fail-safe cases** and are well served by `⊥`.

**C cannot be expressed in the signature `gᵢ : Xᵢ ∪ {⊥} → {SAFE, CAUTION, UNSAFE}`.** Staleness is not a property of a value; it is a relation between a value, its observation time, and a policy. A classifier that takes only `xᵢ` cannot decide it.

**D is not a fault at all.** Treating a permanently unavailable variable as a runtime failure is precisely what produces the 100%-UNSAFE result in §1. A deployment that structurally lacks a data source is operating within a *reduced* specification, not in a continuous state of failure.

---

## 4. Three further defects

**`v` cannot be `⊥` in the same sense.** Vessel category is supplied by the operator at configuration time; it is not sampled. Its failure mode is "not configured", and the correct response is to refuse to start, not to classify UNSAFE. `v` is already distinguished in C.1 as a conditioning parameter rather than a condition variable; the `⊥` treatment must respect that distinction.

**`⊥`-driven UNSAFE is indistinguishable from hazard-driven UNSAFE.** Governance-wise this is correct — `G(S) = 0` either way, which is the point of the fail-safe. But two consequences follow that the current specification does not address. An operator told *"conditions are unsafe"* when the truth is *"the wave feed is down"* has been misinformed about the world. And the audit trail cannot separate the two, so a deployment could sit in `⊥`-UNSAFE for weeks and the logs would show only sustained bad weather. **The state should carry a reason alongside it.**

**Empirical figures conflate the same two things today.** `canonical_figures.py` reports a "weather-driven share of UNSAFE" computed as the share where `g_o`, `g_r` or `g_w` is at the maximum. Under an implemented `⊥` rule a third category appears — fault-driven UNSAFE — and that metric would need a third row rather than silently absorbing faults into "weather".

---

## 5. Recommended semantics — split the concept, do not extend it

### 5.1 `⊥` — runtime fault, cases A and B only

```
gᵢ : Xᵢ ∪ {⊥} → {SAFE, CAUTION, UNSAFE}        for xᵢ ∈ {w, r, m, o, t}
gᵢ(⊥) = UNSAFE
```

Clean, provable, and sufficient to make Theorem C.1 **operationally total** — total over the input space a deployed system actually faces, not merely over the ideal domains. This is the extension worth formalising, and it is what turns the manuscript's asserted fail-safe rule into a theorem.

### 5.2 Staleness — a freshness predicate, evaluated before classification

Staleness is resolved *upstream* of `gᵢ`, by a predicate over (value, observation time, maximum permitted age) that maps an over-age reading to `⊥`. This keeps the classifier signature honest: `gᵢ` still takes a value, and the temporal judgement lives where the timestamp is available.

The maximum permitted age is a **specified parameter per variable**, not a constant. Wave height at hourly resolution tolerates a different staleness budget from a marine warning broadcast. No value is proposed here; each needs its own justification, and an unsourced number would repeat the 7.5 mm/hr error.

### 5.3 Unmeasured variables — a declared scope exclusion, not `⊥`

A variable with no data source in a given deployment is **declared excluded**, with three obligations:

1. The exclusion is stated in the specification, not left as an unwritten convention.
2. The component is pinned at its **lowest severity** — the value that cannot raise `f(E)`.
3. The consequence is stated wherever figures are reported: **every severity figure is a lower bound.**

This is exactly what the replay already does for `m`. It has simply never been specified, which is why it silently contradicts the `⊥` rule.

**Why lowest severity rather than highest.** Pinning high would make the system unusable (§1). Pinning low is the honest choice *provided* the lower-bound consequence travels with every figure — which is already project practice. The residual risk is that a reader takes a lower bound for an estimate, and the mitigation is disclosure, not a different pin.

### 5.4 `v` unconfigured — a startup precondition

Not a classification outcome. The system does not start without a vessel category.

---

## 6. What this changes

| Item | Before | After |
|---|---|---|
| `⊥` meanings | 4 conflated | 1 (runtime fault) |
| Staleness | undefined, and inexpressible in the signature | freshness predicate upstream of `gᵢ` |
| Unmeasured `m` | contradicts the fail-safe rule | declared scope exclusion with lower-bound disclosure |
| `o` tuple | permanently `⊥` under a naive rule | `⊥` attaches to the components `g_o` reads |
| `v` | undefined | startup precondition |
| Theorem C.1 | total over ideal domains | **operationally total** over `Xᵢ ∪ {⊥}` |
| UNSAFE reason | not carried | fault-driven vs hazard-driven distinguished |

**No empirical figure changes.** This is a specification correction: it makes explicit what the replay already does, and removes a contradiction that would otherwise invalidate the headline the moment a reader applied the stated rule.

---

## 7. Why this is a contribution, not housekeeping

The distinction between **mathematical totality** — `f` defined over its specified domains — and **operational totality** — `f` defined over the input space a deployed system actually faces — is real, and the gap between them is exactly where a low-resource deployment lives. Missing, stale and permanently unavailable observations are the normal case in the target context, not the exception.

The thesis already claims an offline-first architecture for a low-resource environment. Formalising the input space that environment actually produces is a stronger version of that claim than asserting a fail-safe rule in prose and proving totality over the ideal case.

**It also has an audit finding attached, which is worth stating in the paper rather than hiding:** the project's own specification, applied literally to its own data, would have produced a 100% UNSAFE classification. That is a concrete demonstration that mathematical totality does not imply operational totality — found in this system, not hypothesised.

---

## 8. Related

| Document | Relationship |
|---|---|
| `appendix-c-formalisation.md` C.2, Theorem C.1, C.9.4 | Where the extension must be applied. **Currently contains no `⊥` at all** |
| `docs/justification/viva-formalisation-architecture.md` §EC-1, Q-lines 588–596 | States the rule and the `m = ⊥` rationale that §1 shows to be in conflict with the replay |
| `publications/.../manuscript-v3.md` Algorithm 1, Deployment Challenges | Asserts the fail-safe rule twice as an architectural property |
| `docs/reference/explainer-per-component-classification-functions.md` | Third statement of the rule |
| `empirical-findings-2026-09-06.md` §0 caveats, F-11 | `m = none` throughout; stale swell-period caveat (§2 above) |
| `decision-record-empirical-first.md` Q2 | The marine warning archive question — the source of the `m` exclusion |
