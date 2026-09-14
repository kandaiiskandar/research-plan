# Literature Review Extraction (Reduced)
## Paper: A model for types and levels of human interaction with automation

---

## 1. Paper Identity

- **Full title:** A model for types and levels of human interaction with automation
- **Authors:** Raja Parasuraman, Thomas B. Sheridan, Christopher D. Wickens
- **Year:** 2000
- **Venue:** IEEE Transactions on Systems, Man, and Cybernetics — Part A: Systems and Humans
- **Publisher:** Institute of Electrical and Electronics Engineers
- **Volume / issue / pages:** Vol. 30, Issue 3, pp. 286–297
- **DOI:** 10.1109/3468.844354
- **ISSN:** 1083-4427
- **Type:** Peer-reviewed journal article, conceptual model
- **Peer review:** Yes
- **Extraction category:** Methodological foundation / external evidence
- **Source class:** `FOUNDATIONAL_HISTORICAL` · `SOURCE_VALIDITY = PASS` · pre-2023, retention justified in §7

**Metadata provenance:** verified against the Crossref DOI record for 10.1109/3468.844354.

---

## 2. Core Contribution

The canonical model of automation design in human factors. Two ideas carry it.

**Types (stages).** Automation is not one thing. It applies to four stages of human information processing, and a system may be automated to a different degree at each:

1. Information acquisition
2. Information analysis
3. Decision and action selection
4. Action implementation

The paper is explicit that a system cannot have a single overall level of automation; a level is always stated relative to a specific function.

**Levels.** Within a stage, automation occupies a point on a ten-level continuum from fully manual to fully autonomous. The lower levels concern what is offered to the human:

- Level 2: the computer "offers a complete set of decision/action alternatives"
- Level 3: the computer "narrows the selection down to a few"
- Level 4: the computer "suggests one alternative"

Higher levels progressively transfer execution and the right to veto from human to computer.

---

## 3. Relevance to My Research

Levels 2–4 are the sharpest historical precedent for graduated restriction of what an automated system presents to a human. This is why the source is retained despite its age: the claim belongs to the original.

### Mechanism coding

| Question | Finding |
|---|---|
| What is governed? | The degree of automation applied to each of four stages |
| What causes the level to be set? | A design decision. The paper offers evaluative criteria — human performance consequences, automation reliability, cost of action outcomes — applied during design |
| Runtime or design-time? | **Design-time.** The model is a taxonomy for assigning levels per function; it does not prescribe runtime switching conditioned on environmental state |
| External state or AI-internal? | Neither — there is no state variable |
| AI participation changed? | Not as a runtime quantity |
| Advisory content changed? | At levels 2–4, what the human sees differs by level |
| Recommendation **type** scope changed? | **Partially.** Level 3 narrows the *number of alternatives within a single decision*. It does not restrict which *types* of recommendation are admissible |
| Executable action space changed? | Yes at the higher levels, where the computer executes |
| Human/AI authority changed? | **Yes** — that is what the level scale encodes |
| Human final authority invariant? | Only at the lower levels. Levels 6–10 progressively remove it |
| Formal verification? | No |
| Empirical evaluation? | Not in this paper; the model has since been the subject of meta-analytic work on stages and levels |

---

## 4. Use in the Architecture Argument — Scope and Limits

**What this paper CAN be cited for:**

- That graduated restriction of the options presented to a human operator is long established in human-factors models of automation.
- That the degree of automation is properly stated per function rather than for a system as a whole — a distinction the governance pair `(G(S), A_AI(S))` also observes, separating participation from advisory scope.
- Level 3's exact wording, "narrows the selection down to a few", as the historical precedent for option-set narrowing.

**What this paper CANNOT be cited for (overreach guard):**

- It is a **design-time taxonomy**. It must not be cited as a runtime state-conditioned mechanism.
- Level 3 narrows the *number of alternatives*; it does not condition an admissible *recommendation-type* set. Do not conflate the two.
- There is no environmental classifier, no enforcement mechanism, no containment property, and no proof.
- Human authority is not invariant across the scale, so it must not be cited as a precedent for unconditional human authority.
- Do not cite it for empirical claims about automation effects; that evidence lives in the later meta-analytic literature.

---

## 5. Positioning for This Research

Parasuraman, Sheridan and Wickens (2000) established that automation should be characterised per processing stage rather than as a single system property, and placed each stage on a ten-level scale whose lower levels differ precisely in what is presented to the human: a complete set of alternatives at level 2, a narrowed selection at level 3, a single suggestion at level 4. Graduated restriction of the presented option space is therefore not new, and the architecture proposed here must not claim it. The distinction that survives is one of object and timing: the level scale narrows the number of alternatives within a decision and is assigned at design time per function, whereas the governance pair conditions the admissible set of *recommendation types* on a classified environmental state that is evaluated at runtime.

---

## 6. Overall Relevance Score

### ⭐⭐⭐ Medium (foundational evidence)

No architecture, no formalism, no runtime mechanism, and no empirical content, but it is the origin of the concept the novelty claim must be defended against. Cite in Related Work for the historical position and for the required distinction; do not cite it as a contemporary account of the field.

---

## 7. FOUNDATIONAL_HISTORICAL justification

**Why a modern replacement is insufficient for this specific claim.**

The claim being sourced is that graduated narrowing of the options presented to a human is a long-standing design concept, and that its canonical formulation assigns levels at design time per function. That claim is *about* this paper. A 2023+ review that cites the model can attest to its continued influence, but cannot serve as the source for the model's own wording or for the design-time character of the original formulation. Substituting a later citing paper would misattribute the historical position and would weaken rather than strengthen the honesty of the comparison.

Retention is therefore justified under exception A — the original/foundational source of a concept. Contemporary context for the levels-of-automation literature is provided separately; see `data/amict-conference-rebuild/source-validation-report.md` §Area 3.
