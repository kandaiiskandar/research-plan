# Appendix C: Mathematical Formalisation of the Graduated Safety-State-Gated Architecture

## C.1 Environmental State Representation

Let the environmental–operational state be defined as a state vector:

E = {w, r, m, o, v, t}

Where:

- w = wind condition  
- r = rainfall intensity  
- m = marine warning level  
- o = ocean condition (wave, tide, current)  
- v = vessel class  
- t = time of day (hour, 24-hour clock)


The environmental state represents the operational context used by the deterministic safety classification layer.

### Time of Day Classification Note

t ∈ [0, 24) is classified by the threshold function g_t(t) into three safety zones:

- SAFE: 06:00–17:00 (daytime — sufficient daylight for safe operation and return)
- CAUTION: 17:00–19:00 (approaching darkness — elevated visual risk)
- UNSAFE: 19:00–06:00 (night — insufficient daylight for safe small-vessel operation)

The overall safety state S = max-severity(S_w, S_r, S_m, S_o, S_v, S_t) applies the conservative worst-case rule across all six parameters, including t. Time of day is therefore a direct input to the governance classification, not a post-hoc filter on recommendation types.

**Empirical justification for t.** The inclusion of t is grounded in two complementary empirical sources. Atacan & Düzbastılar (2023) conducted a bridge navigation simulator study with 30 small-scale fishing vessel captains and found that night navigation significantly elevates both accident probability (mean 4.08 vs. 3.43 at calm conditions) and consequence (mean 12.80 vs. 8.53). Combined night and heavy weather produced the highest consequence scores across all tested conditions (mean 37.03). Restricted visibility — the principal mechanism by which nighttime elevates risk for small vessels without radar — was rated the single most dangerous factor for sea navigation accident probability (mean 7.90, the highest across all six environmental scenarios). Dominguez-Péry et al. (2023) analysed 504 IMO maritime accident investigation reports (2011–2021) and found that external environmental factors including visibility constitute the largest single risk cluster (26.7% of text segments), with time of day captured as a standard field in IMO accident records. These findings establish that time of day is an empirically validated maritime risk factor, not an arbitrary addition to E.

---

## C.2 Safety State Classification Function

The deterministic safety layer maps the environmental state to a safety state:

S = f(E)

Where:

S ∈ {SAFE, CAUTION, UNSAFE}

An example rule-based classification:

S =
- UNSAFE if m = Warning or w > w_max
- CAUTION if w_caution < w ≤ w_max
- SAFE otherwise

This example illustrates the classification logic.  
In the full system, the function f(E) incorporates all variables in the environmental state vector E, with thresholds derived from Malaysian maritime safety data and expert elicitation during the design science research cycle.

---

## C.3 AI Participation Gate Function

The AI participation gate determines whether the Advisory AI Layer is allowed to operate:

G(S) =
- 0 if S = UNSAFE
- 1 if S ∈ {SAFE, CAUTION}

Where:

- G(S) = 0 → AI disabled  
- G(S) = 1 → AI enabled  

This gate controls AI participation, but it does not define the scope of AI recommendations.

---

## C.4 AI-Admissible Recommendation Space

To formally represent advisory governance, define the AI-admissible recommendation space:

A_AI(S)

Let the set of recommendation types be:

R = {Go, Delay, DepartureTime, Duration}

Where:

- Go = go / no-go recommendation  
- Delay = recommendation to delay departure  
- DepartureTime = recommended departure window  
- Duration = recommended safe trip duration  

The AI-admissible recommendation space is defined as:

A_AI(S) =
- {Go, Delay, DepartureTime, Duration} if S = SAFE
- {Go, Delay} if S = CAUTION
- ∅ if S = UNSAFE

This produces the containment relationship:

A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅

When S = CAUTION, the Go recommendation is automatically presented by the system with a caution qualifier (e.g., “Proceed with caution”). The recommendation type remains Go, but its presentation and explanation are modified by the safety state. This preserves set containment while allowing state-dependent advisory messaging.

This restriction means that under CAUTION conditions, the AI cannot provide timing optimisation or trip duration recommendations.

---

## C.5 Two-Level Governance Structure

The architecture implements a two-level AI governance model controlled by environmental safety state.

### Level 1 – Participation Governance

Determines whether AI is allowed to operate:

G(S)

### Level 2 – Advisory Scope Governance

Determines what the AI is allowed to recommend:

A_AI(S)

Therefore, the AI decision system is governed by the pair:

(G(S), A_AI(S))

Environmental safety state therefore governs:

1. Whether AI participates  
2. What the AI is allowed to recommend  

This two-level governance structure is the core architectural mechanism of the proposed system.

---

## C.6 Governance Constraints

The architecture must satisfy the following governance constraints.

### Participation Constraint

If the AI participation gate is closed, the AI recommendation space must be empty:

G(S) = 0 ⇒ A_AI(S) = ∅

This ensures deterministic safety constraints override AI advisory reasoning.

### Advisory Restriction Constraint

The CAUTION state must restrict AI advisory scope relative to SAFE:

S = CAUTION ⇒ A_AI(CAUTION) ⊂ A_AI(SAFE)

This ensures that CAUTION represents a restricted advisory mode rather than full AI operation.

---

## C.7 Safety Dominance Property

The Graduated Safety-State-Gated Architecture satisfies the Safety Dominance Property if deterministic safety classification always constrains AI recommendations.

Let AI(E) denote the set of recommendation types generated by the AI for environmental state E.

Then the Safety Dominance Property is defined as:

For all E, if S = f(E), then:

AI(E) ⊆ A_AI(S)

and

If S = UNSAFE, then:

AI(E) = ∅

This means the AI can only generate recommendations that belong to the admissible recommendation space defined by the safety state.

This property ensures that probabilistic AI reasoning cannot generate recommendations outside deterministic safety constraints.

---

## C.8 Formal Architecture Flow

The decision architecture can be summarised as the following formal pipeline:

E → S = f(E) → (G(S), A_AI(S)) → AI(E)

This represents the layered governance process:

1. Environmental state is observed  
2. Safety state is classified  
3. Governance rules determine AI participation and advisory scope  
4. AI generates recommendations within permitted scope  

---

## Summary of Formal Model Components

The formal architecture is defined by four core functions:

| Symbol | Meaning |
|-------|---------|
| E | Environmental state |
| S = f(E) | Safety classification |
| G(S) | AI participation gate |
| A_AI(S) | AI admissible recommendation space |

These four functions together define the Graduated Safety-State-Gated Hybrid AI Decision Architecture.

---

## Conceptual Structure of the Architecture Governance Model

The formal architecture defines the governance mechanism that controls AI participation and advisory scope using environmental safety state.

The architecture is governed by the following sequence:

E → S = f(E) → (G(S), A_AI(S)) → AI(E)

Where:

- E = Environmental–operational state
- S = Safety state
- G(S) = AI participation gate
- A_AI(S) = AI-admissible recommendation space
- AI(E) = AI-generated recommendations

In this architecture:

1. The environmental state is observed.
2. The deterministic safety layer classifies the safety state.
3. The safety state controls whether AI is allowed to operate.
4. The safety state controls what the AI is allowed to recommend.
5. The AI generates recommendations within the permitted advisory scope.
6. The human operator makes the final decision.

This structure represents a state-governed hybrid AI decision architecture where deterministic safety classification governs probabilistic AI advisory behaviour.

---

## Formal Contribution of the Architecture

The formal contribution of this research is the definition of a safety-state-governed AI decision architecture using a two-level governance mechanism.

The architecture is formally defined by the governance pair:

(G(S), A_AI(S))

Where:

- G(S) determines whether the AI is allowed to participate.
- A_AI(S) determines the set of recommendation types the AI is allowed to generate.

The architecture must satisfy the following governance properties:

1. Participation Constraint  
   If G(S) = 0, then A_AI(S) = ∅.

2. Advisory Restriction Constraint  
   A_AI(CAUTION) ⊂ A_AI(SAFE).

3. Safety Dominance Property  
   AI(E) ⊆ A_AI(S).

These properties ensure that deterministic safety classification always constrains AI participation and advisory behaviour.

Therefore, the proposed contribution is not a new AI prediction model, but a governance architecture that formally constrains how AI participates in decision-making under different safety states. The architecture ensures that AI operates within a safety-governed advisory space and cannot generate recommendations outside deterministic safety constraints.