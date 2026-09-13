# E5 Execution Path Audit

**Batch:** 7A — Journal 1 E5 Benchmark Harness  
**Task:** 1 — Execution Path Audit + Hardware Profile  
**Date:** 2026-09-13  
**Status:** ALL STAGES HAVE EXECUTABLE IMPLEMENTATIONS — proceed to Task 2

---

## E5 Timed Region

E5 measures the full pass from classification through to rule-set supply and reasoning. Per the established ruling in the Task 1 brief, the timed region covers two top-level operations:

1. Component classifier calls → S (using functions from `historical_replay.py` / `canonical_gt.py`)
2. `execute_episode(state, repository, context)` → AI(E)

No existing classifier logic is duplicated in the harness.

---

## Stage 1 — Classification: f(E) / F_{D,τ}

**Determines S from environmental inputs.**

| Field | Value |
|---|---|
| **stage** | Classification |
| **authoritative specification** | `docs/canonical/appendix-c-formalisation.md` C.2 (component classifiers and max-severity aggregation); `CLAUDE.md` Classification structure section (thresholds) |
| **implementation file (component classifiers)** | `scripts/historical_replay.py` (g_w, g_r, g_o); `scripts/canonical_gt.py` (g_t, canonical) |
| **implementation functions** | `g_w(w_kn)` — wind speed (historical_replay.py line 74); `g_r(precip_mm_hr, wmo_code)` — rainfall + thunderstorm indicator (line 79); `g_o(wave_m, vessel)` — ocean state, vessel-conditioned (line 102); `g_t(times, hours)` — canonical solar-event classifier (canonical_gt.py line 82) |
| **aggregation** | `f(E) = max_≻(g_w(w), g_r(r,κ), g_m(m), g_o(o,v), g_t(t,date))` — five terms; `g_m` is excluded in replay (D = {m}) |
| **input** | w (wind speed, kn), r (precip rate mm/hr, WMO code → κ), m (marine warning level; pinned SAFE in replay: D={m}), o (wave height m), t (datetime), v (vessel category ∈ {small, medium, big}) |
| **output** | S encoded as int (0=SAFE, 1=CAUTION, 2=UNSAFE); maps to string via STATE dict in historical_replay.py |
| **included_in_E5** | yes |
| **reason** | Classification is the entry point of the timed region. The harness supplies pre-resolved component inputs and calls g_w, g_r, g_o, and g_t to produce S. These are the authoritative implementations; no duplication is introduced. |

### Component function detail

| Function | File | Lines | Input | Output | Notes |
|---|---|---|---|---|---|
| `g_w(w_kn)` | `scripts/historical_replay.py` | 74–76 | wind speed (knots) | 0/1/2 | Thresholds: 21.6 kn (CAUTION), 27.0 kn (UNSAFE) — MET Cat 1/2 onsets |
| `g_r(precip_mm_hr, wmo_code)` | `scripts/historical_replay.py` | 79–94 | precip rate (mm/hr), WMO code | 0/1/2 | Thresholds: 10.0 (CAUTION), 20.0 (UNSAFE); WMO 95/96/99 → UNSAFE directly |
| `g_o(wave_m, vessel)` | `scripts/historical_replay.py` | 102–105 | wave height (m), vessel category | 0/1/2 | Vessel-conditioned via VESSEL_THRESHOLDS dict; small (1.0/1.25 m), medium (1.4/2.8 m), big (1.5/3.5 m) |
| `g_t(times, hours)` | `scripts/canonical_gt.py` | 82–106 | pandas datetime Series (or array), optional hours | int array SAFE/UNSAFE | CANONICAL — SDR-001 applied; reads frozen solar artefact; never returns CAUTION; g_t(⊥)=UNSAFE |
| `g_m(m)` | (replay: excluded) | — | marine warning level | pinned SAFE in replay | D={m}: no marine warning archive exists for study site; all figures are lower bounds |

### Thresholds in effect (canonical, 2026-09-08)

| Classifier | SAFE | CAUTION | UNSAFE | Source |
|---|---|---|---|---|
| g_w | ≤ 21.6 kn | 21.6–27.0 kn | > 27.0 kn | MET Cat 1/Cat 2 onsets |
| g_r | ≤ 10.0 mm/hr | 10.0–20.0 mm/hr | > 20.0 mm/hr | JPS/DID Light limit / MET Ribut Petir |
| g_t | sunrise ≤ t < sunset | (none — g_t emits no CAUTION) | otherwise; g_t(⊥)=UNSAFE | COLREGs Rule 20(b) — SDR-001 |
| g_o (small) | < 1.0 m | 1.0–1.25 m | > 1.25 m | Yaakob et al. 2015 |
| g_o (medium) | < 1.4 m | 1.4–2.8 m | > 2.8 m | Yaakob et al. 2015 |
| g_o (big) | < 1.5 m | 1.5–3.5 m | > 3.5 m | Yaakob et al. 2015 |

---

## Stage 2 — G(S): Participation Gate

**Determines whether AI participates for the classified state.**

| Field | Value |
|---|---|
| **stage** | G(S) — Participation gate |
| **authoritative specification** | `docs/canonical/appendix-c-formalisation.md` C.3; `governance/rule_set_provider.py` module docstring and GOVERNANCE_MAP (lines 35–48) |
| **implementation file** | `governance/rule_set_provider.py` |
| **implementation function/class** | `get_governance_config(state: str) -> GovernanceConfig` (line 146); `.G` attribute of returned `GovernanceConfig` dataclass (line 29) |
| **input** | state: str ∈ {"SAFE", "CAUTION", "UNSAFE"} |
| **output** | GovernanceConfig.G ∈ {0, 1} — 0 means AI does not participate (UNSAFE); 1 means AI participates |
| **included_in_E5** | yes |
| **reason** | G(S) is resolved as part of execute_episode Step 1. The lookup is a dict access (GOVERNANCE_MAP) — negligible cost but logically part of the timed pass. Included for completeness of the full pipeline path. |

### GOVERNANCE_MAP (canonical values)

| State | G | A_AI |
|---|---|---|
| SAFE | 1 | {Go, Delay, DepartureTime, Duration} |
| CAUTION | 1 | {Go, Delay} |
| UNSAFE | 0 | ∅ |

---

## Stage 3 — A_AI(S): Admissible Set Selection

**Determines which recommendation types are admissible for the classified state.**

| Field | Value |
|---|---|
| **stage** | A_AI(S) — Admissible set selection |
| **authoritative specification** | `docs/canonical/appendix-c-formalisation.md` C.4; `governance/rule_set_provider.py` GOVERNANCE_MAP and GovernanceConfig docstring |
| **implementation file** | `governance/rule_set_provider.py` |
| **implementation function/class** | `get_governance_config(state: str) -> GovernanceConfig` (line 146); `.A_AI` attribute (line 30) — `frozenset` of admissible conclusion types |
| **input** | state: str ∈ {"SAFE", "CAUTION", "UNSAFE"} (same call as Stage 2) |
| **output** | GovernanceConfig.A_AI: frozenset ⊆ {"Go", "Delay", "DepartureTime", "Duration"}. SAFE → full set; CAUTION → {"Go","Delay"}; UNSAFE → ∅ |
| **included_in_E5** | yes |
| **reason** | A_AI(S) is resolved in the same `get_governance_config(state)` call as G(S) at execute_episode Step 1. A_AI is then passed to validate_rule_set (Step 4) to enforce containment: ConclusionTypes(RS(S)) ⊆ A_AI(S). This is the core architectural constraint and must be in the timed region. |

### Containment property (implemented in validate_rule_set)

`validate_rule_set` checks `ConclusionTypes(candidate) ⊆ A_AI(state)` before any reasoning begins. Violation raises `ConfigurationError(failure_type="A_AI_CONTAINMENT")`. This check is at `governance/rule_set_provider.py` lines 206–216.

---

## Stage 4 — RS(S) Supply + Reasoning

**Selects, validates, and supplies the rule set, then runs the reasoning engine to produce AI(E).**

| Field | Value |
|---|---|
| **stage** | RS(S) supply + reasoning |
| **authoritative specification** | `layer3-prototype-specification.md §8–§9`; `algorithm-specification.md §17–§20`; `governance/reasoning_episode.py` module docstring (ten-step orchestration) |
| **implementation file** | `governance/rule_set_provider.py` (select_rule_set, validate_rule_set); `governance/reasoning_episode.py` (execute_episode); `governance/canonical_rules.py` (build_canonical_repository) |
| **implementation functions** | `select_rule_set(repository, state)` (rule_set_provider.py line 160); `validate_rule_set(candidate, state, episode_id)` (line 181); `execute_episode(state, repository, context)` (reasoning_episode.py line 152) |
| **input** | state: str, repository: RuleRepository, context: DecisionContext |
| **output** | EpisodeResult (advisories: list[Advisory] = AI(E); trace: FidelityTrace; error: Optional[Exception]) |
| **included_in_E5** | yes |
| **reason** | This is the second top-level operation in the timed region per the E5 ruling. It includes rule-set selection, A_AI containment + structural validation (V1–V4), and engine reasoning. The full EpisodeResult constitutes AI(E). |

### Sub-function detail

| Function | File | Lines | Role |
|---|---|---|---|
| `build_canonical_repository()` | `governance/canonical_rules.py` | 61–213 | Initialises the RuleRepository with R-CAUTION-001 through R-CAUTION-004. Called once before the timed loop, not inside it. |
| `select_rule_set(repository, state)` | `governance/rule_set_provider.py` | 160–178 | Extracts enabled rules for the given state. RS(UNSAFE)=∅ immediately. |
| `validate_rule_set(candidate, state, episode_id)` | `governance/rule_set_provider.py` | 181–341 | A_AI containment check + V1 (variable exists in schema) + V2 (type compatible) + V3 (operator valid) + V4 (domain value in declared set). Raises ConfigurationError on first violation. |
| `execute_episode(state, repository, context)` | `governance/reasoning_episode.py` | 152–330 | Orchestrates ten-step pipeline: G(S) lookup → UNSAFE gate-off → consistency check → RS selection → validation → RS supply → reasoning → AI(E) → FidelityTrace → EpisodeResult. |

### execute_episode ten-step orchestration (from reasoning_episode.py docstring)

| Step | Action |
|---|---|
| 1 | Establish governance configuration from state |
| 2 | If G(S)==0 (UNSAFE): return empty set with trace — no reasoning |
| 2.5 | Check S/ComponentStateTrace consistency |
| 3 | Select RS_candidate(S) from repository |
| 4 | Validate RS_candidate (A_AI containment + V1–V4) |
| 5 | Supply RS(S) |
| 6 | engine.reason(context, RS(S)) |
| 7 | Produce AI(E) |
| 8 | Emit fidelity trace |
| 9 | Return EpisodeResult |

### Rule repository (canonical, build_canonical_repository)

| Rule ID | Applicable state | Condition | Conclusion type | Notes |
|---|---|---|---|---|
| R-CAUTION-001 | CAUTION | resolved_m == "advisory" | Delay | 0 activations expected in replay (D={m}); structurally correct |
| R-CAUTION-002 | CAUTION | component_o_state == "CAUTION" | Delay | Ocean state CAUTION — primary binding driver (98.71%/97.66% of daylight CAUTION) |
| R-CAUTION-003 | CAUTION | component_r_state == "CAUTION" | Delay | Rainfall CAUTION |
| R-CAUTION-004 | CAUTION | component_w_state == "CAUTION" | Delay | Wind CAUTION (2 activations in 5 yr, 0 bindings) |
| R-SAFE-001 | SAFE | (deferred) | Go | DEFERRED — STATE_RESTATEMENT (Batch 4A) |

Note: No SAFE-state rules are loaded (R-SAFE-001 is deferred). OPEN items: no DepartureTime or Duration rules (OPEN-L3-1C, OPEN-L3-1D); no Go rule under CAUTION (GAP-03).

---

## canonical_rules.build_canonical_repository() — Rule Repository Initialisation

| Field | Value |
|---|---|
| **function** | `build_canonical_repository()` |
| **file** | `governance/canonical_rules.py` |
| **lines** | 61–213 |
| **authority** | `layer3-prototype-specification.md §24`; `data/journal1-layer3-prototype/closure-batch2.json` |
| **input** | None (no parameters) |
| **output** | `RuleRepository` instance loaded with R-CAUTION-001 through R-CAUTION-004 |
| **role in E5** | Called once before the benchmark loop begins. Repository is constructed once and passed to each `execute_episode` call. Not included in the timed region for individual episodes. |

---

## Blocking Check

Per brief instructions: if any E5 stage has NO executable implementation, report `E5_HARNESS_BLOCKED`.

| Stage | Implementation status |
|---|---|
| Classification (f(E)) | IMPLEMENTED — g_w, g_r, g_o in historical_replay.py; g_t in canonical_gt.py |
| G(S) participation gate | IMPLEMENTED — get_governance_config(state).G in rule_set_provider.py |
| A_AI(S) admissible set | IMPLEMENTED — get_governance_config(state).A_AI in rule_set_provider.py |
| RS(S) supply + reasoning | IMPLEMENTED — select_rule_set, validate_rule_set, execute_episode |

**Result: NO BLOCK. All four E5 stages have executable implementations. Proceed to Task 2.**

---

## Key Constraints for Task 2

1. **Do not duplicate classifier logic.** Call g_w, g_r, g_o from `scripts/historical_replay.py` and g_t / is_daylight from `scripts/canonical_gt.py` directly.
2. **Do not duplicate governance logic.** Call `get_governance_config`, `select_rule_set`, `validate_rule_set`, `execute_episode` from their respective modules.
3. **build_canonical_repository() is called once** before the timed loop — repository construction is not part of the per-episode timed region.
4. **E5 is DESCRIPTIVE** — no pass/fail threshold (H3 is OPEN/UNSUPPORTED). Record wall-clock times only; do not assert a latency bound.
5. **L3_RETROSPECTIVE_REPLAY = NOT_REQUIRED** — the harness drives individual episodes, not a full historical replay.
