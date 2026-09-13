# Diff Audit — F1–F3 / E5 Status Synchronisation Micro-Repair

**File changed:** `publications/active/journal-1/evaluation-specification.md` — **the only scientific-authority file touched**
**Hash:** `bfc6038516c998b3` → **`5a0e706a9b982e92`** · **Diff: +21 / −13 lines**

Every change below corrects a *status representation*. No fidelity criterion, metric, research question, threshold, condition, mathematical definition, evaluation-design decision or empirical value was altered, and nothing was recomputed.

---

## Changes applied — 10 loci

### §1 Purpose (OCC-01)

| | |
|---|---|
| **Before** | "**what requires empirical implementation** (implementation-fidelity criteria, awaiting Layer 3 build)" |
| **After** | "**what is implementation-fidelity evidence** (fidelity criteria measured against the built Layer 3 prototype)" |

The purpose list enumerated evidence *kinds*; one entry described its kind by what it was still waiting for. Corrected to describe the kind itself.

### §7 Implementation-fidelity criteria (OCC-02, OCC-03) — primary locus

| | |
|---|---|
| **Before** | "Three fidelity criteria test whether a **future** Layer 3 build conforms…"<br>"**Status:** all three are **OPEN — deferred to Layer 3 build**. See Section 14." |
| **After** | "Three fidelity criteria test whether **the** Layer 3 build conforms…"<br>"**Status:** all three are **CLOSED — PASS** (Batch 5, 2026-09-11)." |

Two paragraphs were added, both required for the closure to be readable without being over-read:

1. **Measured counts** — 292 primary episodes (32 SAFE, 260 CAUTION), 454 advisory records, 244 episodes with a non-empty advisory, F1 = 0, F2 = 0, F3 = 0; the 16 empty-advisory CAUTION episodes explained as admissibility rather than failure; and **162 UNSAFE gate-off cases counted separately and explicitly not part of the 292**.
2. **Bounded interpretation** — interface-contract exhaustive scope, not the retrospective replay; evaluated against the implemented rule configuration; `R-SAFE-001` DEFERRED, `RS(SAFE)` empty, all 32 SAFE episodes producing zero advisories, `Delay` the only generated type; and an explicit statement that the closure does not demonstrate fidelity of a populated SAFE rule set, does not establish that every `A_AI(SAFE)` type was exercised, and is not behavioural or real-world validation.

A dated provenance note records what the section previously said, so the supersession is legible rather than silent.

### §11 Performance evaluation (OCC-04)

| | |
|---|---|
| **Before** | "**Status:** OPEN — requires prototype benchmarking. **Blocked by Layer 3 build** for realistic end-to-end timing." |
| **After** | "**Status:** **OPEN — requires target-hardware benchmarking.**" plus the full E5 boundary set. |

**E5's OPEN status is unchanged and was never in question.** What was stale was the *blocker*: the prototype now exists, so Layer 3 cannot be what blocks E5. The real blocker — absence of representative physical hardware — is now stated, together with `E5_HARNESS = CLOSED`, `MACBOOK_REFERENCE = COMPLETE`, `MACBOOK_CLASSIFICATION = DEVELOPMENT_MACHINE_REFERENCE`, `target_hardware_evidence = false`, `E5_ANDROID_TARGET_BENCHMARK = DEFERRED_MANDATORY`, and `H3 = X ms` OPEN/UNSUPPORTED with the note that a low reference latency is not a threshold pass.

### §14 Layer 3 dependency (OCC-05, OCC-06, OCC-07)

| | |
|---|---|
| **Before** | "Layer 3 is **specified** … but **not fully implemented**."<br>"Prototype fidelity evidence — F1, F2, F3. **Blocked on Layer 3 build.**"<br>"Performance evidence — E5. Realistic timing requires the prototype; partial timing from Layer 2 alone can be reported as a lower bound." |
| **After** | "Layer 3 is **specified and implemented**" — engine, Algorithm 3 supply, `ComponentStateTrace`, `R-CAUTION-001`–`R-CAUTION-004`; `R-SAFE-001` DEFERRED; explicitly a **research prototype**, not a production deployment, operational maritime system, validated field system or complete recommendation engine.<br>"F1, F2, F3. **CLOSED — PASS** (Section 7), bounded…"<br>"E5 / RQ-J2. **OPEN.** Harness validated, development-machine reference complete, target-hardware measurement outstanding and mandatory." |

The existing instruction *"Do not write future-tense planned implementation as completed experimental evidence"* was retained and extended with its new counterpart: *"and do not read the closure as covering a populated SAFE rule set."* The old failure mode was claiming too early; the new one is claiming too broadly.

### §16 Threats and limitations (OCC-10)

"If a **future** Layer 3 build violates any of these" → "If a Layer 3 build violates any of these". A two-word change. The assumption-dependence threat is unchanged and remains valid for the current build and any successor; only the implication that no build exists was removed.

### §17 Open items (OCC-08)

`OPEN-3` (Layer 3 prototype fidelity evidence, reason "Layer 3 not yet implemented") is **struck through and annotated CLOSED 2026-09-11**, rather than deleted — it is the record of an item that was genuinely open when the specification closed, and deleting it would erase that. Its "Blocks" cell now reads "Nothing. Superseded."

A new row **OPEN-5** records the live performance dependency: the E5 target-hardware benchmark, blocked by hardware availability, affecting E5 / RQ-J2 only.

### §18 Final evaluation matrix (OCC-09)

| | |
|---|---|
| **Before** | `FIDELITY (deferred to Layer 3 build)` |
| **After** | `FIDELITY (CLOSED — PASS; interface-contract exhaustive scope, implemented rule configuration; R-SAFE-001 DEFERRED)` with per-criterion `0 violations` / `0 mismatches` |

---

## Located, inspected, deliberately not changed — 6 loci

| Locus | Why it stays |
|---|---|
| §18 paragraph on the frozen `evaluation-specification.csv` | **Already correct.** It was the one pre-existing place that stated F1–F3 were closed by Batch 5, and it correctly flags the frozen CSV as stale batch evidence. |
| §8, §11, §17 OPEN-1 — `H3 = X ms` OPEN | Genuinely open. No threshold exists and none was invented. |
| §9, §15, §17 OPEN-2 / OPEN-4 — decision-support utility, trust, RQ5 | Genuinely open and outside Journal 1's evidence base. |
| §1 "proofs deferred to Section 6"; §2 record of the earlier §12/§14 wording corrections | Cross-reference and historical record, not status assertions. |
| §13 — E3 scope `{E1, E2, E6}`, `E4_RESOLUTION = NOT_REQUIRED_BY_CURRENT_E3_DESIGN` | **Out of scope.** The E3/E4 micro-repair set this contract and it was not reopened. Verified unchanged. |
| §12 statistical treatment, §16 retrospective-window scope, all empirical values | Unrelated to implementation-fidelity status. |

---

## What the repair did not do

- No change to F1, F2 or F3 **definitions** — only to their status.
- No change to E5 **design**, and no change to its OPEN status.
- No change to the E3/E4 authority contract.
- No change to conditions, metrics, research questions, thresholds or the evaluation matrix structure.
- No new experiment, replay, citation or evidence.
- No change to the taxonomy: P1–P4 FORMAL, F1–F3 IMPLEMENTATION_FIDELITY, E1–E4/E6 EMPIRICAL_TRACE, E5 PERFORMANCE. F1–F3 were not recategorised as empirical replay evidence and were not turned back into hypotheses.
- **The Batch 8B-1 work product was not touched.** The manuscript and all eleven 8B-1 artefacts are byte-identical to their preflight hashes.
