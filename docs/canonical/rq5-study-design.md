# RQ5 study design: contextual validation of the graduated governance architecture

**RQ5:** Does the two-level graduated governance architecture function as intended when real users interact with it — specifically, do fishers correctly perceive safety state, understand the CAUTION restriction, and make different decisions under CAUTION than under SAFE and UNSAFE?

**Date:** 25 April 2026

**Role of this study:** Contextual validation. RQ5 tests whether the architecture works with the population it was designed for. It does not test a theoretical proposition about trust, socio-technical alignment, or human factors in general. Results reported here confirm or disconfirm architecture-level design assumptions — particularly the CAUTION mode's interpretability and behavioural effect.

---

## 1. Scope

RQ5 answers three questions. No others.

**Q1.** Do users correctly identify which safety state the system is currently in?

**Q2.** Do users correctly understand *why* AI is restricted under CAUTION — that is, do they understand the restriction as a scope limitation (the system is allowed to say less), not merely as a change in display or tone?

**Q3.** Does CAUTION mode produce different decision behaviour than SAFE and UNSAFE?

These three questions are sufficient to confirm whether the architecture works contextually. Q1 tests perceptibility — the state must be readable to be useful. Q2 tests interpretability — a correctly perceived state that is misunderstood produces miscalibrated trust. Q3 tests behavioural effect — an understood state that produces no behavioural change adds no safety value.

**What this study does not address:**
- Deep trust calibration or longitudinal trust trajectories
- Socio-technical alignment, organisational factors, or cultural adaptation
- Long-term behavioural change or adoption intent

Introducing any of these expands the study beyond what one chapter can handle and risks reframing RQ5 as a theoretical contribution rather than a validation exercise. They are questions for future work.

---

## 2. Instrument design

Four components, administered in sequence within a single session of approximately 60–75 minutes per participant.

### 2.1 Scenario-based system display

Before any measurement, present the participant with the system interface under each of the three safety states in sequence: SAFE, then CAUTION, then UNSAFE. Each state is shown as a static display — the same information the system would show a fisher on a real departure morning. The display includes:

- The safety state indicator (colour and label)
- The AI recommendations available in that state (or absence of recommendations under UNSAFE)
- A brief system message explaining the state

Order is fixed across all participants. The display is the stimulus for all three measurement components that follow.

### 2.2 Comprehension check (per safety state)

After viewing each state display, ask the participant three questions targeting Q1 and Q2. Questions are administered verbally by the researcher and answered verbally, recorded for later coding.

**After SAFE display:**
- "In your own words, what is the system telling you right now?"
- "What kinds of advice can the system give you in this situation?"
- "Would you trust this advice to help you decide whether to go to sea today?"

**After CAUTION display:**
- "In your own words, what is the system telling you right now?"
- "What kinds of advice can the system give you in this situation, compared to the previous display?"
- "Why do you think the system is not giving you a departure time or trip duration right now?"

**After UNSAFE display:**
- "In your own words, what is the system telling you right now?"
- "Why is there no AI advice shown in this situation?"
- "What would you do next if you saw this display?"

**Coding:** Responses are coded as Correct / Partial / Incorrect against a coding rubric. For Q2, a response is Correct only if the participant identifies that the *type* of advice is restricted — not merely that the display looks different or that the system is being cautious. A response that says "it's telling me to be careful" is Partial. A response that says "it's not giving me a departure time because it's not reliable enough" is Correct.

### 2.3 Decision task (per safety state)

After the comprehension check for each state, present a brief scenario with specific E vector values and ask: "Given what the system is showing you, what would you do?" Record the response and ask one follow-up: "What information from the system influenced your decision most?"

Three decision scenarios, matched to the three states:

| Task | E = (w, r, m, o, v, t) | S | System display |
|---|---|---|---|
| DT-SAFE | 8 kn, none, none, 0.5 m, big, 08:00 | SAFE | Full advisory: Go recommended, departure window 06:30–07:30, duration up to 8 hours |
| DT-CAUTION | 18 kn, none, none, 0.5 m, big, 08:00 | CAUTION | Restricted advisory: Proceed with caution / Consider delaying. No departure time or duration shown. |
| DT-UNSAFE | 30 kn, none, none, 0.5 m, big, 08:00 | UNSAFE | No AI advisory. Safety alert: dangerous conditions. |

Decision response options presented to participant: Go now / Delay departure / Do not go. Record choice and the reasoning offered. Do not prompt for specific reasoning categories.

### 2.4 Trust scale

Administer a shortened Jian et al. (2000) Trust in Automation scale after all three scenario-display-decision cycles are complete. Use 7 items, rated 1–7:

1. The system is dependable.
2. The system's recommendations are reliable.
3. I can trust the system to give me appropriate advice.
4. The system is predictable — I can anticipate what it will do in different conditions.
5. The system is honest with me about its limitations.
6. I would feel safe relying on this system when conditions are uncertain.
7. The system behaved the way I expected it to across the three conditions I saw.

Item 7 is added to capture cross-state coherence — whether the system's graduated behaviour (more advice in SAFE, less in CAUTION, none in UNSAFE) felt logical rather than arbitrary.

**Scoring:** Mean score across 7 items (range 1–7). Report per-item scores and the overall mean. Do not reduce to a binary pass/fail — the scale is ordinal evidence, not a threshold.

### 2.5 Debrief interview

A 10–15 minute semi-structured debrief after the trust scale. Three open questions:

1. "The system gave you different amounts of advice in the three situations. In your own words, why do you think it did that?"
2. "Was there a situation where the system's behaviour surprised you or didn't make sense?"
3. "If you were going to sea regularly and this system was available on your phone, would you use it? What would make you more or less likely to use it?"

Debrief responses are not scored. They are analysed thematically to identify whether CAUTION mode is interpreted as a coherent intermediate state or as a confusing in-between. Direct quotes are used in Chapter 7 reporting.

---

## 3. Participant group

**Population:** Active fishers and fisheries officers in Terengganu and/or Penang, Malaysia.

**Minimum sample:** 12–15 participants. This is sufficient for qualitative validity — identifying whether CAUTION mode is consistently understood or consistently misunderstood — but not for statistical inference. The study is designed for pattern confirmation, not population-level frequency claims.

**Sampling approach:** Purposive. Recruit through local fisheries cooperatives and the Department of Fisheries Malaysia offices in the study sites. Prioritise participants with active sea-going experience in the past 12 months. Include at least 2–3 fisheries officers alongside fishers to test whether domain knowledge affects interpretation of the CAUTION restriction.

**Exclusion criteria:** Participants with no sea-going experience or with no familiarity with decision support tools of any kind (to avoid measuring technology familiarity rather than architecture interpretability).

**Session format:** One-on-one, in person, at a location familiar to the participant (cooperative office or equivalent). Malay-language materials throughout. If a translator is required for dialect variation, note this in the study record.

---

## 4. What success looks like

RQ5 is confirmatory, not exploratory. The study is looking for a specific pattern of results. The following criteria define whether the architecture functions contextually as designed.

### 4.1 Q1 — State perceptibility

**Success:** ≥ 70% of participants correctly identify the safety state from the display in all three conditions.

A result below 70% in any single state indicates a display design problem, not an architecture failure — the governance logic may be correct but the presentation does not communicate it. This would require interface revision before deployment.

### 4.2 Q2 — CAUTION interpretability

**Success:** ≥ 60% of participants give a Correct response to the CAUTION comprehension question — that is, they identify the restriction as a scope limitation, not merely a cautionary tone.

This is the harder criterion and the more architecturally significant one. A Partial result (majority understand *something* has changed but not *what*) suggests the CAUTION display needs more explicit explanation of why specific advice types are absent. A Correct result confirms that the Level 2 governance mechanism is legible to users without technical knowledge of the architecture.

### 4.3 Q3 — Behavioural effect

**Success:** Decision behaviour under CAUTION differs measurably from both SAFE and UNSAFE — specifically, more participants choose Delay under CAUTION than under SAFE, and more participants choose Go or Delay under CAUTION than under UNSAFE (where the expected dominant response is Do not go).

This does not require statistical significance given the sample size. The pattern — SAFE → more Go, CAUTION → more Delay, UNSAFE → more Do not go — should be directionally consistent across participants. Any reversal (e.g., more participants choosing Go under CAUTION than under SAFE) would indicate a misinterpretation of the CAUTION mode.

### 4.4 Trust coherence

**Success:** Trust scale item 7 ("The system behaved the way I expected it to across the three conditions I saw") scores ≥ 4.5 mean. This indicates that the graduated behaviour — more advice in SAFE, restricted in CAUTION, silent in UNSAFE — reads as a coherent system rather than an inconsistent one.

---

## 5. What this study confirms and does not confirm

| Claim | Confirmed by RQ5 | Not confirmed by RQ5 |
|---|---|---|
| CAUTION mode is perceptible to users | Q1 results | Whether perception degrades over repeated use |
| CAUTION restriction is interpretable without technical background | Q2 Correct coding rate | Whether interpretation transfers to novel conditions |
| CAUTION produces different decisions than SAFE and UNSAFE | Q3 decision patterns | Whether those decisions are safer in practice |
| Graduated behaviour reads as coherent | Trust scale item 7 | Long-term trust trajectory |

**The study cannot claim that using the system makes fishers safer.** That would require a longitudinal study with real departure decisions and outcome tracking. RQ5 establishes that the architecture works as designed in controlled interaction — users perceive, understand, and respond to the CAUTION mode as intended. Whether that translates to improved real-world safety behaviour is a separate question.

---

## 6. Relationship to socio-technical literature

Flehmig et al. (2025) STA variable, Rasmussen's (1997) risk homeostasis, and Zarei (2024) on socio-technical alignment are not theoretical frameworks for this study. They may appear in the Chapter 7 discussion as interpretive lenses — for example, if debrief data suggests participants adapt their own risk tolerance to the system's graduated state, Rasmussen's framework offers a way to name that pattern. But they do not appear in the methodology or the result coding schema.

The architecture makes three claims about how users should behave, and the study checks whether those claims hold. Socio-technical frameworks can explain *why* they hold or fail — that is a discussion-section question, answered after results are in hand.

---

## 7. Ethical approval requirements

An ethical approval application is required before recruitment begins. The application should cover:

- Study purpose and participant population
- Data collection methods (verbal responses, recorded session, trust scale)
- Data storage and anonymisation procedures
- Informed consent process (Malay-language consent form)
- Right to withdraw at any point without consequence
- Any risks to participants (minimal — no deception, no sensitive personal data beyond fishing experience)

The application should be submitted to the institutional review board of the supervising university. Timeline: allow 4–8 weeks for review before field recruitment begins.

Prepare consent forms and participant information sheets in both English and Malay. Offer verbal administration as an alternative to written consent for participants with limited literacy.
