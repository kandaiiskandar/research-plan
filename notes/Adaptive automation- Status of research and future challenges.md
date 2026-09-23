# Literature Review Extraction (Reduced)
## Paper: Adaptive automation: Status of research and future challenges

---

## 1. Paper Identity

- **Full title:** Adaptive automation: Status of research and future challenges
- **Authors:** Margherita Bernabei, Francesco Costantino
- **Year:** 2024
- **Venue:** Robotics and Computer-Integrated Manufacturing
- **Publisher:** Elsevier
- **Volume / article:** Vol. 88, article 102724
- **DOI:** 10.1016/j.rcim.2024.102724
- **ISSN:** 0736-5845
- **Type:** Peer-reviewed systematic literature review
- **Peer review:** Yes
- **Scope:** 344 contributions retrieved from Scopus; 181 documents reviewed in full, plus 10 by snowball sampling; coverage spans the 1950s to 2022; multidisciplinary (engineering, management, psychology, social sciences, neuroscience)
- **Extraction category:** External evidence (family D comparator for the novelty defence)
- **Source class:** `ACCEPT_CONTEMPORARY` · `SOURCE_VALIDITY = PASS` · year ≥ 2023

**Metadata provenance:** verified against the Crossref DOI record for 10.1016/j.rcim.2024.102724.

---

## 2. Core Contribution

A systematic review of adaptive automation (AA): systems that dynamically reallocate functions between human and machine according to contextual conditions, rather than fixing the allocation at design time.

**The review's trigger taxonomy — seven invocation categories, not mutually exclusive and often hybridised:**

1. Operator-based — direct operator activation, or systematic evaluation of operator status
2. System-based — current or predicted system states
3. Task/mission-based — task or mission status
4. **Environmental-based — environmental parameters activating changes**
5. Spatiotemporal-based — time and position criteria
6. Performance-based — flexibility, quality, productivity metrics
7. Psychophysiological-based — EEG, fNIRS, ECG, eye tracking

**A terminological distinction the review makes explicit, and which matters here:**

> "The authority belongs to the human operator, the dynamic allocation is called adaptable automation. If the authority belongs to the machine, it is referred to as adaptive automation."

The review reports that adaptable automation — human authority — showed greater operator acceptance and more appropriate levels of trust.

**Stated future challenges:** moving from simulation to real-world validation; generalising across contexts; determining the optimal frequency of function reallocation; human–machine intention alignment; mitigating automation surprises through HMI design; evaluating situation awareness and genuine trust; balancing operator well-being against system performance.

---

## 3. Relevance to My Research

This is the contemporary peer-reviewed authority for what family D — adaptive automation and adjustable autonomy — actually governs.

### Mechanism coding

| Question | Finding |
|---|---|
| What is governed? | The **allocation of functions** between human and machine, and the level of automation |
| What causes the change? | Any of the seven trigger categories above |
| Runtime or design-time? | **Runtime** — this is the defining feature of AA relative to static allocation |
| External state or AI-internal? | Both occur. Environmental-based triggers exist as one of seven categories |
| AI participation changed? | Yes, in the sense that function allocation shifts between human and machine |
| Advisory content changed? | Not as a governed quantity. The review discusses HMI adaptation at interaction, perception and cognition levels |
| Recommendation **type** scope changed? | **No.** The review does not describe systems that restrict the set or types of recommendations presented to a human on the basis of an externally classified environmental state |
| Executable action space changed? | Indirectly, through reallocation of who performs a function |
| Human/AI authority changed? | **Yes — this is the point of the mechanism.** Authority location is what distinguishes adaptive from adaptable automation |
| Human final authority invariant? | **No.** Under adaptive automation the authority belongs to the machine; invariant human authority corresponds to the *adaptable* case |
| Formal verification? | No |
| Empirical evaluation? | The reviewed literature is largely simulation-based; real-world validation is named as an open challenge |

**Two findings do real work for the novelty defence.**

First, **environmental triggering of automation change already exists** — it is one of seven recognised invocation categories. So conditioning a governance change on environmental parameters is not itself novel. What the reviewed AA literature does with that trigger is reallocate functions and adjust automation level, not contract an admissible recommendation-type set.

Second, **the adaptive/adaptable distinction is a precision point the manuscript should adopt.** In this literature "adaptive automation" denotes machine authority. The architecture here holds human authority unconditionally, which places it on the *adaptable* side of the review's own terminology while retaining runtime state-conditioning. Using "adaptive" loosely would misdescribe the architecture in the vocabulary of the field it is being compared against.

---

## 4. Use in the Architecture Argument — Scope and Limits

**What this paper CAN be cited for:**

- That adaptive automation switches governance at runtime, across seven recognised trigger categories including environmental parameters.
- That what is governed is function allocation and automation level, not the admissible set of recommendation types.
- The adaptive (machine authority) versus adaptable (human authority) distinction.
- That real-world validation, not mechanism invention, is the field's stated open challenge.

**What this paper CANNOT be cited for (overreach guard):**

- It must **not** be cited for advisory-scope restriction. The review describes no such mechanism.
- It is a manufacturing-oriented review; do not generalise its acceptance and trust findings to maritime decision support.
- It provides no formal model and no safety property.
- Do not cite it as evidence that *no* system restricts recommendation types — its silence is about the AA literature, not about avionics.

---

## 5. Positioning for This Research

Bernabei and Costantino (2024) review 181 documents on adaptive automation and identify seven categories of invocation trigger, including environmental parameters, confirming that runtime, environmentally conditioned governance change is established in human-factors engineering. What the reviewed systems reallocate is function and level of automation; none restricts the set of recommendation types presented to a human on the basis of a classified environmental state. The review also fixes the field's terminology in a way this project must respect: dynamic allocation with authority retained by the human operator is *adaptable* automation, while *adaptive* automation places authority with the machine. The architecture proposed here is runtime state-conditioned but holds human authority unconditionally, and governs a quantity — admissible advisory scope — that the review's taxonomy does not contain.

---

## 6. Overall Relevance Score

### ⭐⭐⭐ Medium (novelty-defence evidence)

Contemporary, peer-reviewed, large-scope, and mechanistically precise about what the family governs. It replaces the USAARL technical report as the primary family D source. Not a governance-architecture comparator and not part of the Chapter 2 core corpus; its value is bounding what family D can and cannot be said to have done.

---

## 7. Caveats

- Coverage ends at 2022 despite the 2024 publication date; the review is a status-of-research synthesis, not a source of recent primary systems.
- Manufacturing and industrial focus; aviation and maritime cases appear but are not the centre of gravity.
- Its negative finding about recommendation-type restriction is a finding about the AA literature it reviewed, and should be reported with that scope.
