# Literature Extraction: Di Paco et al. (2026)  
## "AISAFETY: An AI-based smart system for enhancing operator safety in production processes"

---

## Section 1 — Paper Identity

- Title: AISAFETY: An AI-based smart system for enhancing operator safety in production processes  
- Authors: Francesco Di Paco, Luca Burattini, Roberto Gabbrielli, Luca Landi, Francesco Marcelloni, Leonardo Marrazzini, Marco Palumbo, Marco Pirozzi  
- Year: 2026  
- Venue: Safety Science, Volume 199  
- DOI: https://doi.org/10.1016/j.ssci.2026.107201  
- Type: System design + experimental prototype + case study  

---

## Section 2 — Core Contribution

### Problem Addressed

The paper addresses operator safety in industrial human–machine collaborative environments. The challenge is ensuring real-time safety monitoring and intervention under dynamic working conditions.

### Proposed Solution

A multilayer AI-based supervision system integrating:

- RFID for operator tracking  
- Computer Vision (YOLOv8) for monitoring  
- Machine control system  
- Rule-based expert system  

### Main Contributions

- A layered safety supervision architecture  
- A rule-based AI module using IF–THEN logic  
- A closed-loop system capable of triggering safety actions  

### What is Novel

- Integration of heterogeneous sensing technologies  
- Combination of AI perception (CV) with rule-based reasoning  
- Alignment with EU Machinery Regulation requirements  

---

## Section 3 — Relevance to My Research

| Theme | Relevance | Explanation |
|------|----------|------------|
| Safety-critical AI | Yes | Focus on operator safety |
| Rule-based reasoning | Yes | Expert system used |
| Deterministic control | Yes | IF–THEN rule execution |
| Hybrid AI | Partial | CV + rule-based |
| Governance of AI | Partial | Controls actions but not AI space |
| State-based control | No | No SAFE/CAUTION/UNSAFE |
| Action space restriction | No | No A_AI(S) concept |
| Human-in-the-loop | Partial | Alerts but no structured decision layer |

### Gate Decision

- Yes: 3  
- Partial: 3  

Result: FULL extraction

---

## Section 4 — Decision Architecture Analysis

Architecture flow:

Sensors (RFID + CV)  
→ AI Module (Rule-based Expert System)  
→ Machine Control System  
→ Operator Interface  

Key characteristics:

- Event-driven  
- Reactive decision-making  
- Closed-loop control  

---

## Section 5 — Formal Model and Mathematical Representation

The system uses symbolic logic:

IF condition THEN action  

Example:

IF lathe.power = ON AND door_guard = OPEN  
THEN door_guard.is_tampered = TRUE  

No formal mathematical model is provided.

---

## Section 6 — Safety State Classification

No explicit safety states are defined.

Safety is:

- scenario-based  
- rule-specific  
- not globally classified  

No abstraction such as SAFE / CAUTION / UNSAFE exists.

---

## Section 7 — Governance Level Analysis

Governance exists at rule level:

- hazard detection  
- automatic safety action  

Example:

IF unsafe condition → trigger stop  

Properties:

- reactive  
- local  
- event-based  

Not:

- state-based  
- global  
- structured governance  

---

## Section 8 — Human Role in Decision-Making

Human role:

- receives alarms  
- supervises system  

The system can act autonomously:

- triggers machine stop  
- notifies operator  

No formal human decision layer exists.

---

## Section 9 — System Constraints and Environment

Environment:

- industrial setting (CNC + cobot)  

Constraints:

- CV affected by visibility  
- RFID accuracy limitations  
- environmental variability  

---

## Section 10 — Hybrid AI Taxonomy

System components:

- Computer Vision → statistical AI  
- RFID → sensing system  
- Rule-based module → symbolic AI  

Hybrid structure:

Perception (ML) + Reasoning (rules)

---

## Section 11 — Baseline Comparison and Evaluation

Evaluation method:

- use-case scenarios  
- hazard simulations  
- experimental validation  

Example cases:

- guard tampering  
- unauthorized access  
- machine malfunction  

---

## Section 12 — Key Concepts and Definitions

- Rule-Based Expert System  
- IF–THEN logic  
- Ontology-based knowledge  
- Sensor fusion  
- Closed-loop safety system  

---

## Section 13 — Limitations and Unsolved Problems

- Depends on predefined scenarios  
- Limited adaptability  
- CV sensitivity to environment  
- Requires manual rule design  

Key limitation:

System works only if risks are anticipated.

---

## Section 14 — Methodology Notes

- Risk assessment (ISO 12100)  
- Use-case driven design  
- Ontology modelling  
- Rule engineering  

---

## Section 15 — Quotable / Citable Points

- "The AI module was developed as a Rule-Based Expert System… IF condition THEN action."  
- "The system integrates CV, RFID, and a machine control layer governed by a rule-based expert system."  
- "The system can autonomously trigger safety-related actions rather than only issuing warnings."  
- "AI enables proactive safety management by detecting hazardous conditions."  

---

## Section 16 — Relation to My Research and Positioning

### Alignment

- Uses rule-based reasoning in safety-critical systems  
- Demonstrates real-world applicability  
- Confirms importance of deterministic logic  

### Gap

The system:

- detects hazards  
- reacts to events  

But does not:

- define safety states  
- control AI participation  
- restrict recommendation space  
- provide formal guarantees  

### Positioning

This paper demonstrates the effectiveness of rule-based systems for safety monitoring. However, it operates at a reactive level. This research extends the approach to a governance architecture that explicitly constrains AI behaviour based on safety states.

---

## Section 17 — Overall Relevance Score

⭐⭐⭐⭐☆ (4/5)

### Justification

- Strong support for rule-based safety systems  
- Real-world implementation  
- Lacks governance architecture and formal model  

---