# A18.2 → Next Phase: Reference Readiness

**From `M1dQ-A18.2-CFB-v0.1`, 21 November 2026.** What the next phase needs, and what it does not get from here.
**No new safety claim is made in this document.**

---

## 1. What A18.2 settled

Incremental intermediate binding factorises exactly:

```
I_CF = P(S = CAUTION)  ×  P(proposal is DepartureTime or Duration | S = CAUTION)
```

The **first** factor is the gate's own quantity and is already measured: 531/9,135. The **second** is a property of the advisor, bounded in [0, 1], and the conference experiment never observed it. A18.2 shows the whole range is reachable: 0 for an always-Go/Delay advisor, 1 for an always-timing/duration advisor, 0.4275 for one plausible simulated rule.

**So the open scientific question is now specific and bounded**: what is `P(timing-or-duration | CAUTION)` for an advisor anyone would defend? Everything else in the identity is known.

---

## 2. R1 — issue-time forecast inputs

**Need.** Archived **issue-time** marine forecast products for Kota Kinabalu, 2020–2024, at a lead short enough to inform an 05:00–09:00 departure decision.

**Why it is required.** Every feature in A18.2, gate and advisor alike, is retrospective reanalysis. `decision_time_availability` is UNKNOWN for 100% of cases (Step 2 D-08). Until issue-time products exist, **no advisor evaluated on this data can be described as one a fisher could have run**, however plausible its rule.

**Gap.** No such archive is present locally. Earlier work in this project assessed availability, licensing and sample size as the principal obstacles. **This is not closable from local artefacts.**

**Deadline consideration.** The conference presentation is 23 December 2026. R1 cannot plausibly be resolved before it, and nothing in A18.2 requires it to be — A18.2 is explicitly a hindsight replay.

---

## 3. R2 — expert action semantics and labels

**Need.** For each of `Go`, `Delay`, `DepartureTime`, `Duration`, an operational definition that a Sabah small-vessel skipper or fisheries officer would recognise, and then per-case judgements of whether a proposal was appropriate.

**Why it is required.** A18.2 counts exclusions. It cannot say whether **any** exclusion was correct, because **no protective-action truth exists for any of the four types**. Without R2 the direction of every exclusion is undefined: a withheld `DepartureTime` might have been the safe advice or the unsafe one.

**Gap.** No expert labels, no action catalogue mapping, no adjudication protocol. The conference types are **not** the later A1/A2/A3 fisheries action catalogue and must not be substituted for it.

**Constraint carried from this session.** Recruitment and external requests require explicit authorisation and have not been sought.

---

## 4. What a defensible B2 successor needs

A18.2's B2 is **SIMULATED**: three features, three arbitrary thresholds, no source. Its ordering against the constants is robust; its level is not. A successor needs, in order of difficulty:

1. **A sourced rule.** Any published or practitioner-stated mapping from observable conditions to a departure-timing or trip-duration recommendation for small vessels. The recently converted corpus is the obvious place to look — in particular the operational risk awareness tool for small fishing vessels, which builds a Bayesian network over wave height, swell, wind and current, and the Peninsular Malaysia seakeeping study, which gives sea-state-indexed pass/fail for sub-10-GRT boats.
2. **A pre-registered threshold set**, frozen before any binding number is computed, as A18.2 did.
3. **Coverage below 1.** A real advisor will abstain. A18.2's coverage of 1.0000 is an artefact of PRIMARY having no nulls in the whitelist.

## 5. Device and data gaps

| Gap | Status |
|---|---|
| Issue-time forecast archive | **absent** — blocks any operational-availability claim, permanently from local data |
| Expert action semantics / R2 labels | **absent** — blocks every appropriateness and direction-of-error claim |
| Marine warning archive | **absent** — `g_m` pinned SAFE, so all counts are lower bounds (D-05) |
| Independent safety or utility outcome | **absent** — no safety–utility trade-off is statable |
| Co-located wind field per wave cell | **absent** — needed to separate wave product from co-location (D-12) |
| Sourced advisor rule | **absent** — the specific, bounded gap A18.2 isolates |
| Certified vessel thresholds | **absent** — the band is a length-to-tonnage transfer (A-03) |

## 6. Optional cheap replication

RESOLUTION can be run as exploratory replication with the frozen B2. Two differences to expect and report: n = 5,935, and **coverage below 1.0000** because `wave_period` has 35 nulls there, so ABSTAIN will fire. **Populations must not be pooled**, and no pure-resolution interpretation is admissible (D-12).

## 7. Statements the next phase must not make

No maritime safety improvement. No harm reduction. No effect on actual departure decisions. No decision quality. No human trust. No certified thresholds. No algorithmic novelty. No claim that any excluded proposal should have been excluded. No IID interval over serially dependent grid-hours.
