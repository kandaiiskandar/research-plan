# Literature Extraction: Toskov, B., & Toskova, A. (2026)  
## "AgroNova: An Autonomous IoT Platform for Greenhouse Climate Control"

---

## Section 1 — Paper Identity

- **Title:** AgroNova: An Autonomous IoT Platform for Greenhouse Climate Control  
- **Authors:** Borislav Toskov, Asya Toskova  
- **Year:** 2026  
- **Venue:** *Sensors (MDPI), Volume 26*  
- **DOI:** https://doi.org/10.3390/s26010001 *(verify exact DOI in final submission)*  
- **Type:** System design + empirical deployment study  

---

## Section 2 — Core Contribution

### Problem Addressed
The paper addresses limitations of traditional greenhouse control systems, particularly:
- reliance on **centralized cloud processing**
- vulnerability to **network disruptions**
- lack of **real-time autonomous decision-making at the edge**

---

### Proposed Solution
The authors propose **AgroNova**, a hybrid IoT platform that:
- integrates **edge-based rule-driven control**
- incorporates **LLM-based advisory reasoning**
- ensures **autonomous operation under constrained connectivity**

---

### Main Contributions (as presented in the paper)

- **Edge-based autonomous control:**  
  Real-time decisions are executed locally using deterministic rule logic.

- **Hybrid decision architecture:**  
  Combines rule-based control with server-side LLM consultation.

- **Bounded action execution:**  
  The LLM is restricted to a predefined set of actuator commands.

- **Resilient system design:**  
  The system maintains operation without reliance on cloud connectivity.

- **Empirical validation:**  
  The system is deployed for over seven months with more than 380,000 sensor readings.

---

### What is Novel (from the paper context)

The novelty lies in:
- integrating **LLM-based advisory reasoning** into an **edge-first autonomous control system**
- maintaining **deterministic control authority** while enabling **context-aware suggestions**

---

## Section 3 — Relevance to My Research

| Theme | Relevance | Notes |
|------|--------|------|
| Deterministic safety layer | Yes | Edge gateway uses rule-based logic |
| AI advisory role | Yes | LLM provides recommendations |
| AI participation control | Partial | LLM invoked conditionally but not formally defined |
| Admissible action space | Yes | Actions restricted to predefined commands |
| State-based governance | No | No explicit safety states |
| Formal guarantees | No | No formal model |
| Low-resource environment | Yes | Designed for intermittent connectivity |
| Hybrid AI architecture | Yes | Rule-based + LLM integration |

---

### Gate Decision

- Yes: 5  
- Partial: 1  

➡️ **FULL EXTRACTION**

---

## Section 4 — Decision Architecture Analysis

The system follows a layered IoT architecture:

- **Sensor Layer:** Collects environmental data (temperature, humidity)
- **Gateway Layer:** Executes deterministic rule-based decisions
- **Server Layer:** Provides LLM-based advisory suggestions
- **Actuator Layer:** Executes physical actions (e.g., ventilation)

Key observation:

> Decision authority remains at the gateway, where rule-based logic determines final actions.

---

## Section 5 — Formal Model and Mathematical Representation

- No explicit formal model is defined.
- No mathematical representation of decision logic is provided.
- The system is implemented as an engineering architecture rather than a formal framework.

---

## Section 6 — Safety State Classification

- No explicit classification into safety states.
- Environmental thresholds are used instead:
  - e.g., temperature > 30°C
  - relative humidity > 85%

These function as **implicit safety triggers**, not structured states.

---

## Section 7 — Governance Level Analysis

| Governance Aspect | Presence | Notes |
|------------------|--------|------|
| AI participation control | Partial | LLM invoked when needed |
| Action constraint | Yes | Restricted actuator commands |
| Decision authority | Yes | Gateway dominates |
| Formal governance model | No | Not defined |

---

## Section 8 — Human Role in Decision-Making

- Humans define:
  - threshold values  
  - system configuration  

- System operates autonomously during runtime.

---

## Section 9 — System Constraints and Environment

- Designed for **low-resource IoT environments**
- Handles:
  - intermittent connectivity  
  - limited actuation capability  
  - real-world environmental variability  

---

## Section 10 — Hybrid AI Taxonomy

The system can be classified as:

- **Deterministic control layer (primary)**
- **Advisory AI layer (secondary)**

This reflects a **hierarchical hybrid model**.

---

## Section 11 — Baseline Comparison and Evaluation

Evaluation includes:

- latency of local decision-making (<1 second)  
- system recovery time (~7.57 hours)  
- actuator usage (~2.3% of time)

Focus is on **operational performance**, not comparative benchmarking.

---

## Section 12 — Key Concepts and Definitions

- Edge autonomy  
- Rule-based control  
- Hybrid decision-making  
- LLM advisory integration  
- Bounded actuator actions  

---

## Section 13 — Limitations and Unsolved Problems

- No formal governance model  
- No explicit safety-state abstraction  
- No mathematical guarantees  
- Limited formal evaluation of LLM behaviour  
- AI participation not explicitly controlled  

---

## Section 14 — Methodology Notes

- Real-world deployment over 7 months  
- 5 distributed sensor nodes  
- MQTT-based communication  
- Rule-based threshold control  
- Integration with weather API  

---

## Section 15 — Quotable / Citable Points

- Deterministic control is maintained at the gateway level.  
- The LLM provides advisory input rather than direct control.  
- Actions are limited to predefined actuator operations.  
- The system operates autonomously under network failure conditions.  

---

## Section 16 — Relation to My Research and Positioning

### Alignment

This paper supports:
- hybrid AI architecture  
- deterministic-first control design  
- bounded AI behaviour  
- real-world feasibility  

---

### Gap

The system does not:
- define **formal AI participation control**
- model **state-based risk governance**
- enforce **admissible action space per state**
- provide **formal guarantees of safety**

---

### Positioning

AgroNova demonstrates a practical hybrid architecture where deterministic rule-based control is combined with an AI advisory component. However, it does not formalise how AI participation is governed or how its recommendation space should be constrained under varying risk conditions. This highlights the need for a structured governance architecture that explicitly regulates both participation and admissible actions.

---

## Section 17 — Overall Relevance Score

⭐⭐⭐⭐⭐ (5/5)

### Justification

- Strong architectural similarity  
- Real-world deployment evidence  
- Direct support for hybrid AI design  
- Clearly exposes the absence of formal governance  

---