# Literature Review Extraction (Reduced)
## Paper: Formally Verified Next-Generation Airborne Collision Avoidance Games in ACAS X

---

## 1. Paper Identity

- **Full title:** Formally Verified Next-Generation Airborne Collision Avoidance Games in ACAS X
- **Authors:** Rachel Cleaveland, Stefan Mitsch, André Platzer
- **Year:** 2023 (print issue; published online 29 October 2022)
- **Venue:** ACM Transactions on Embedded Computing Systems (TECS)
- **Publisher:** Association for Computing Machinery
- **Volume / issue / article / pages:** Vol. 22, Issue 1, Article 10, pp. 1–30
- **DOI:** 10.1145/3544970
- **ISSN:** 1539-9087 (print), 1558-3465 (electronic)
- **Preprint:** arXiv:2106.02030 — superseded for citation purposes by the ACM record
- **Type:** Peer-reviewed journal article, formal methods
- **Peer review:** Yes — ACM journal
- **Extraction category:** External evidence (novelty-defence comparator; not a governance-architecture comparator)
- **Source class:** `ACCEPT_CONTEMPORARY` · `SOURCE_VALIDITY = PASS` · year ≥ 2023

**Metadata provenance:** verified against the Crossref DOI record for 10.1145/3544970 and the authors' institutional publication list. **Author spelling is Cleaveland, not Cleveland.**

---

## 2. Core Contribution

Formal verification of collision-avoidance advisory logic for ACAS X, the next-generation airborne collision avoidance system, under adversarial assumptions about the intruder aircraft.

- **Problem:** existing collision-avoidance systems have been analysed assuming severe restrictions on the intruder's manoeuvres, which limits the reach of their safety guarantees in encounters where the intruder may change course.
- **Method:** the encounter is modelled as a game and analysed in **differential game logic**, proving the existence of winning strategies for the resulting Adversarial ACAS X.
- **Result:** collision-freedom is established for rich encounters in which ownship and intruder make independent decisions along differential equations for flight paths with evolving vertical and horizontal velocities.
- The work distinguishes several classes of model, including multi-advisory models.

---

## 3. Relevance to My Research

Its role in the novelty defence is narrow and specific: it establishes that **formal verification of state-conditioned advisory logic has precedent**. Combined with FAA AC 20-151C, it removes two things from the set of claimable novelties — the mechanism of state-conditioned advisory restriction, and the formal treatment of advisory admissibility.

### Mechanism coding

| Question | Finding |
|---|---|
| What is governed? | Advisory selection in a collision-avoidance system |
| What causes the restriction? | The encounter state — relative geometry, velocities, and the adversarial intruder's available manoeuvres |
| Runtime or design-time? | Runtime advisory selection; verification is performed offline on the logic |
| External state or AI-internal? | External — the physical encounter state, not a model-confidence estimate |
| AI participation changed? | Not applicable — no AI component; the advisory logic is algorithmic |
| Advisory content changed? | Yes — which advisory is safe depends on the encounter state |
| Recommendation **type** scope changed? | Yes, in the sense that the safe advisory set is state-dependent. The paper's object is collision-freedom of manoeuvre advisories, not an abstracted admissible-type set |
| Executable action space changed? | No — advisories are issued to a crew |
| Human/AI authority changed? | Not addressed as a governance property |
| Human final authority invariant? | Not established by the paper. Pilot reaction appears as a source of unpredictability rather than as a preserved invariant |
| Formal verification? | **Yes** — differential game logic; winning-strategy existence; collision-freedom |
| Empirical evaluation? | Not the paper's mode; verification rather than measurement |

---

## 4. Use in the Architecture Argument — Scope and Limits

**What this paper CAN be cited for:**

- That formal verification of state-conditioned advisory logic has precedent in airborne collision avoidance.
- That the safety of an advisory can be established by proof rather than by testing — a point this project also makes about Safety Dominance.
- As the contemporary peer-reviewed authority for ACAS X verification, preferred over earlier hybrid-systems verification work for manuscript-facing citation.

**What this paper CANNOT be cited for (overreach guard):**

- It does **not** prove the same general governance theorem as this project. It establishes collision-freedom for an adversarial encounter game; it does not state totality, monotonicity over a severity order, or containment of an advisory set within a state-indexed admissible set.
- It does **not** define a governance pair separating participation from advisory scope, and does not abstract advisory admissibility beyond collision avoidance.
- It does **not** establish that human final decision authority is invariant.
- It contains no AI component, so it must not be cited as evidence about governing AI advisory output.
- Do not cite it as evidence that this project's formal properties are unoriginal in content — only that formal verification of advisory logic is not itself new.

---

## 5. Positioning for This Research

Cleaveland, Mitsch and Platzer (2023) verify ACAS X advisory logic in differential game logic, proving collision-freedom against an adversarial intruder whose manoeuvres are not restricted in advance. Together with the TCAS II inhibition schedule, the paper bounds what this project may claim: neither the runtime restriction of advisory types by an externally measured state, nor its formal verification, is new. What the collision-avoidance line does not supply — and what remains available within the reviewed literature — is the abstraction of that pattern into a domain-independent governance construct with totality, monotonicity and containment proved over an admissible recommendation-type set, and an empirical characterisation of how often the intermediate level changes the governance outcome.

---

## 6. Overall Relevance Score

### ⭐⭐⭐⭐ High (novelty-defence evidence)

Not an architecture comparator and not part of the Chapter 2 governance corpus. Its importance is entirely in the novelty defence, where it is one of the two sources that force the repositioning from mechanism invention to formalisation and generalisation. Peer-reviewed ACM journal provenance makes it safely citable as load-bearing for the bounded claim in §4.

---

## 7. Caveats

- The verified property is collision-freedom in an encounter game. Do not paraphrase it as "advisory containment" or map it onto Theorem 6.3 without qualification.
- Full-text mechanism detail in this note is drawn from the abstract and the authors' summary; the ACM full text was not accessible during validation. Claims in §4 are confined to what those sources establish.
- ACAS X is a different system from the TCAS II covered by FAA AC 20-151C.
