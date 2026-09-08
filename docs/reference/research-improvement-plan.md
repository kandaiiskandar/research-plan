# Research Improvement Plan

**Date:** 25 April 2026
**Purpose:** Step-by-step strategic guidance to strengthen the thesis from its current state to examination readiness.
**Scope:** Covers all five RQs, thesis structure, title, and the critical path item blocking RQ3 and RQ4.

---

## Current State Assessment

The research is in strong shape for its stage. The core formal model (Appendix C) is well-specified with strong empirical justification for every design decision. The architecture illustration is detailed, layered, and includes a scenario walkthrough and honest limitations section. The four-layer gap argument (problem → Indykov → Dalrymple → Flehmig) is forensically precise and multi-sourced. Chapter 2 (Sections 2.1–2.9) is substantively complete. The research alignment table provides full RQ → Objective → Methodology traceability.

**What is strong:**
- Formal pipeline E → S = f(E) → (G(S), A_AI(S)) → AI(E) is clearly defined
- Three-state governance table (SAFE, CAUTION, UNSAFE) is concrete and defensible
- Empirical justification for E vector components is thorough and well-cited
- Worst-case aggregation rule is justified from five independent sources
- Flehmig et al. (2024) comparison table is the sharpest differentiator from existing work
- Limitations section (L1–L6) demonstrates intellectual maturity
- Indykov et al. AT11 → Safety = 0 is a striking and citable gap confirmation

**What needs work:**
- Layer 3 AI component and enforcement mechanism is unspecified (critical path)
- Title signals socio-technical co-contribution it should not
- RQ4 evaluation design is too vague for examination
- RQ5 is over-scoped relative to its role as contextual validation
- Chapter 2 needs a closing bridge paragraph to Chapter 3

---

## Step 1 — Resolve the Layer 3 Enforcement Mechanism (CRITICAL PATH)

**Why this is first.** Everything in RQ3 and RQ4 depends on this. The Safety Dominance Property (AI(E) ⊆ A_AI(S)) is stated as a formal guarantee, but the mechanism enforcing it is not yet specified. Until it is, the property holds only by design intent, not by implementation. A CS examiner will find this immediately.

**The question to answer:** What is the AI advisory component in Layer 3?

### Three options and their trade-offs

| Option | Description | Enforcement mechanism | Proof approach | Low-resource suitability |
|---|---|---|---|---|
| **A — Rule-based** | Explicit if-then rules per safety state | Trivial — CAUTION rule set excludes DepartureTime and Duration by configuration | Proof by construction — the rule set IS the constraint | Excellent — deterministic, O(1), no GPU |
| **B — ML classifier with constrained output** | Learned model with output head restricted to permitted recommendation types | Output layer configuration per safety state — only permitted types are decodable | Architecture-level enforcement — output space is physically restricted | Good — lightweight model, constrained head |
| **C — LLM with output grammar** | Language model constrained by output grammar per safety state (cf. Banerjee et al. CRANE) | Grammar G_A(S) intersected with model output distribution at decoding | Formal via grammar containment — A_AI(CAUTION) grammar ⊂ A_AI(SAFE) grammar | Poor — too heavy for low-resource deployment |

**Recommendation:** Option A (rule-based) for the prototype. It makes the Safety Dominance Property provable by construction, is maximally suitable for low-resource deployment, and aligns with the architecture's deterministic governance philosophy. The AI advisory layer becomes a rule engine that is reconfigured by the governance layer per safety state — no filtering after the fact, because the CAUTION rule set literally does not contain DepartureTime or Duration rules.

**Action items:**
1. Decide on Option A, B, or C and document the decision with justification in `docs/justification-layer3-enforcement.md`
2. Update `docs/architecture-illustration.md` Section 2 (Layer 3) to specify the chosen component
3. State the enforcement mechanism precisely: how does (G(S), A_AI(S)) configure Layer 3 before it generates recommendations?
4. Add a proof or proof sketch of the Safety Dominance Property based on the chosen mechanism
5. Update `docs/appendix-c-formalisation.md` Section C.7 to reference the enforcement mechanism

**Completion test:** A CS examiner asks "how do you guarantee AI(E) ⊆ A_AI(S) in your implementation?" You can answer in two sentences with a concrete mechanism.

---

## Step 2 — Revise the Title

**Current title:**
*"A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Socio-Technical Evaluation in Coastal Fisheries"*

**Problem:** "Socio-Technical Evaluation" signals a socio-technical research strand as a named co-contribution. It elevates RQ5 above its proper role as contextual validation and will cause framing drift throughout the examination.

**Recommended title:**
*"A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Environments: Design and Comparative Evaluation in Coastal Fisheries"*

**Why "Comparative Evaluation":**
- Accurately describes what RQ4 does — three-condition comparative analysis (ungated vs. binary-gated vs. two-level graduated)
- Covers RQ5 accurately — user study across three safety states is also comparative
- Signals CS evaluation methodology without specifying socio-technical framing
- Removes the word "Socio-Technical" from the title entirely

**Action items:**
1. Update the title in the thesis document
2. Update the title in `CLAUDE.md` Research Context section
3. Update the title in `docs/research-alignment-table.md`
4. Update any other document that carries the full title

---

## Step 3 — Sharpen the RQ4 Evaluation Design

**Current state:** RQ4 methodology is described as "scenario-based testing; three-condition comparative analysis." This is too vague. A CS examiner will ask for specifics.

**What RQ4 must demonstrate:**
1. The Safety Dominance Property holds in the two-level graduated architecture across all test scenarios
2. The graduated architecture produces safer, more consistent outcomes than the binary-gated baseline
3. The binary-gated baseline performs better than the ungated baseline
4. The CAUTION mode specifically adds value beyond Level 1 governance alone

### Evaluation design specification

**Three conditions:**

| Condition | Description | What it tests |
|---|---|---|
| Ungated | No governance — AI outputs full recommendation set regardless of S | Baseline: no safety architecture |
| Binary-gated | Level 1 only — G(S) gates AI participation but A_AI is always full scope when G = 1 | Tests whether Level 1 alone is sufficient |
| Two-level graduated | Full proposed architecture — (G(S), A_AI(S)) both active | Tests the primary contribution |

**Scenario design requirements:**
- Minimum 15–20 scenarios covering all three safety states (at least 5 per state)
- At least 3 boundary scenarios — conditions sitting at the SAFE/CAUTION threshold and the CAUTION/UNSAFE threshold
- At least 3 adversarial scenarios — multiple parameters in conflict (e.g., wind UNSAFE but all others SAFE)
- Scenarios should be derived from real Malaysian maritime safety data where possible

**Primary metric — Safety Dominance Property compliance:**
For each scenario under the two-level graduated architecture: does AI(E) ⊆ A_AI(S)?
This must hold for 100% of scenarios. Any violation is a formal failure of the architecture.

**Secondary metrics:**
- Recommendation type accuracy: does the system produce the correct recommendation types per state?
- Decision consistency: does the same environmental input produce the same governance output on repeated runs?
- Boundary behaviour: does the system correctly classify boundary conditions without ambiguity?

**Comparison metrics:**
- Under CAUTION, does the ungated system produce DepartureTime or Duration recommendations? (It should — this is the gap being filled)
- Under CAUTION, does the binary-gated system produce DepartureTime or Duration recommendations? (It should — this confirms Level 1 alone is insufficient)
- Under CAUTION, does the two-level graduated system produce only {Go, Delay}? (It must — this is the contribution)

**Action items:**
1. Design 15–20 test scenarios with specific E vector values for each
2. Define evaluation metrics formally in the methodology chapter
3. Implement all three conditions in the prototype (Step 1 must be done first)
4. Run the comparison and record results per scenario per condition
5. Document the Safety Dominance Property verification explicitly — not as a general claim but as a per-scenario check

---

## Step 4 — Scope RQ5 Appropriately

**Current state:** RQ5 asks how users understand, trust, and make decisions across three safety states, and whether the CAUTION mode produces distinct interaction patterns. This is broad and risks expanding into a socio-technical research program.

**The right scope for RQ5:** A contextual validation study that answers whether the architecture works as intended when real users interact with it. Three questions only:

1. Do users correctly identify which safety state the system is in?
2. Do users correctly understand why AI is restricted in CAUTION (i.e., do they understand the scope restriction, not just that something has changed)?
3. Does the CAUTION mode produce different decision behaviour than SAFE and UNSAFE?

**What RQ5 should NOT try to answer:**
- Deep trust calibration theory
- Socio-technical alignment (STA variable from Flehmig et al. 2025)
- Organisational or cultural factors
- Long-term adoption or behavioural change

**Instrument design:**
- Validated trust-in-automation scale (e.g., Jian et al.) — keep it short, 7–10 items
- Targeted comprehension check per safety state — can the user correctly describe what the system is allowed to say in each state?
- Scenario-based decision tasks — given the system display, what would you do? (Record response per state)
- Short debrief interview — what did CAUTION mean to you? Did the restriction make sense?

**Participant group:** Fishers and fisheries officers in Terengganu and/or Penang. Minimum sample for qualitative validity — 12–15 participants across three safety state scenarios each.

**RQ5 reporting scope:** One chapter, not two. Results reported per safety state across the three questions above. Socio-technical literature (Flehmig et al. 2025 STA, Rasmussen 1997) may appear only in the discussion section as an interpretive lens — not in the methodology.

**Action items:**
1. Reduce the RQ5 research questions to the three stated above
2. Design the instrument: trust scale + comprehension check + decision tasks + debrief
3. Draft the ethical approval application
4. Define what "success" looks like for RQ5 — what pattern of results would confirm the architecture works contextually?

---

## Step 5 — Complete Chapter 2

**Current state:** Sections 2.1–2.9 are substantively complete. The comparative analysis in Section 2.9 is the strongest closing argument. One element is missing.

**What is needed:** A closing paragraph at the end of Section 2.9 that names the gap precisely in terms of the formal contribution and bridges directly to Chapter 3. This paragraph should:

1. State the gap in one sentence using formal notation — no existing architecture formally defines a governance pair (G(S), A_AI(S)) where both levels are conditioned on classified environmental safety state S = f(E)
2. State what the proposed architecture contributes — the two-level governance pair with the formal property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅
3. State what the rest of the thesis does — Chapter 3 presents the research design; Chapter 4 presents the formal architecture; Chapters 5 and 6 implement and evaluate it

**Action items:**
1. Write the closing bridge paragraph for Section 2.9
2. Review all [[notes]] links are present for every cited paper
3. Check that no section introduces socio-technical theory as a primary framework

---

## Step 6 — Confirm Thesis Chapter Structure

The following chapter structure reflects the CS-first positioning with evaluation components in their proper supporting role.

| Chapter | Content | Primary RQ |
|---|---|---|
| 1 | Introduction — problem, gap, research questions, thesis structure | — |
| 2 | Literature review — CS architecture framing, fisheries as domain context | — |
| 3 | Research methodology — DSR framework, five RQs and their methods | — |
| 4 | Architecture design and formal model — the two-level governance architecture | RQ1, RQ2 |
| 5 | Prototype implementation — low-resource coastal fisheries deployment | RQ3 |
| 6 | Technical evaluation — three-condition comparative analysis | RQ4 |
| 7 | User study — contextual validation across three safety states | RQ5 |
| 8 | Discussion and conclusion — contribution, limitations, future work | — |
| Appendix C | Mathematical formalisation — canonical formal model | RQ2 |

**Chapters 4 and 6 are the examination-critical chapters.** Chapter 4 is where the CS contribution is made. Chapter 6 is where it is proven. All other chapters frame, implement, or validate them.

**Action items:**
1. Confirm this structure with supervisor
2. Ensure Chapter 4 covers both RQ1 (architecture design) and RQ2 (formal specification) — these are the two primary contributions and should not be split across chapters
3. Ensure Chapter 8 discussion explicitly names the two-level governance architecture as the primary contribution before mentioning evaluation findings

---

## Priority Order Summary

| Priority | Step | Blocking? |
|---|---|---|
| 1 — Immediate | Step 1: Resolve Layer 3 enforcement mechanism | Yes — blocks RQ3, RQ4, and the formal proof |
| 2 — Soon | Step 2: Revise the title | No — but do it before sharing any documents externally |
| 3 — Concurrent with Step 1 | Step 5: Complete Chapter 2 bridge paragraph | No — can be done in parallel |
| 4 — After Step 1 | Step 3: Sharpen RQ4 evaluation design | Yes — requires Layer 3 decision first |
| 5 — After Step 3 | Step 6: Confirm thesis chapter structure | No — but confirms before writing new chapters |
| 6 — After Steps 3–5 | Step 4: Scope RQ5 | No — but before designing the instrument |

---

## What a CS Examiner Will Look For

At the viva, a CS examiner will focus on three things in order:

**1. The formal contribution.** Can you state precisely what (G(S), A_AI(S)) is, why it is novel, and what formal properties it satisfies? This is answered by Chapter 4 and Appendix C.

**2. The enforcement proof.** How do you guarantee AI(E) ⊆ A_AI(S) in your implementation? This is answered by Step 1 above.

**3. The comparative evidence.** Does your evaluation show that the two-level architecture outperforms the binary-gated baseline in CAUTION conditions specifically? This is answered by Chapter 6.

Everything else — the fisheries domain, the user study, the literature review — is supporting material. The examination will be won or lost on these three.
