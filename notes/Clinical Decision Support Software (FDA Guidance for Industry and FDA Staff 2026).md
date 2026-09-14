# Clinical Decision Support Software — Guidance for Industry and Food and Drug Administration Staff (January 2026)

**Citation:** U.S. Food and Drug Administration. (2026). *Clinical Decision Support Software: Guidance for Industry and Food and Drug Administration Staff* (29 January 2026). Center for Devices and Radiological Health; Center for Biologics Evaluation and Research; Center for Drug Evaluation and Research; Office of Combination Products. Docket FDA-2017-D-6569. https://www.fda.gov/media/109618/download

**Short reference:** FDA CDS Guidance (2026)

**Corpus status:** Added September 2026 by the AMICT novelty-corpus validation task — authorised regulatory source for novelty-defence matrix entry N-13.

**Source class:** `ACCEPT_AUTHORISED` · `AUTHORISED_REGULATORY_SOURCE` · contemporary (2026).

---

## 1. What the document is

FDA final guidance interpreting section 520(o)(1)(E) of the Federal Food, Drug, and Cosmetic Act, which excludes certain clinical decision support software functions from the statutory definition of a device. The guidance sets out four criteria that a software function must meet to be **non-device CDS**.

**Version history matters here.** The guidance was published **6 January 2026** and **reissued 29 January 2026**; the January 2026 guidance **supersedes the September 2022 final guidance** on CDS. The targeted novelty audit cited the 2022 version. This note records the current document.

---

## 2. The four criteria and Criterion 3

The four criteria, as numbered in the guidance:

1. Not intended to acquire, process, or analyse a medical image, a signal from an in vitro diagnostic device, or a pattern/signal from a signal acquisition system.
2. Intended for the purpose of displaying, analysing, or printing medical information about a patient or other medical information.
3. Intended for the purpose of supporting or providing recommendations to a health care professional about prevention, diagnosis, or treatment of a disease or condition.
4. Intended for the purpose of enabling an HCP to independently review the basis for the recommendations that the software presents, so that the HCP does not rely primarily on any of those recommendations.

**Criterion 3 turns on output type.** Permissible outputs, quoted from the guidance:

> "Software functions that provide the following outputs may also be considered 'supporting or providing recommendations to an HCP' and would meet Criterion 3, as long as they were not intended to replace or direct the HCP's judgment:
> 1. List of preventive, diagnostic or treatment options;
> 2. Prioritized list of preventive, diagnostic or treatment options; or
> 3. List of follow-up or next-step options for consideration."

Impermissible:

> "Cases where a software function provides a specific preventive, diagnostic or treatment output or directive, the software function fails Criterion 3 because it is not intended for the purpose of supporting or providing recommendations."

**New in the 2026 revision:** an enforcement-discretion policy —

> "If only one option is clinically appropriate and the software function otherwise meets all criteria under section 520(o)(1)(E), FDA intends to exercise enforcement discretion (meaning that FDA does not intend to enforce requirements under the FD&C Act) for such functions."

---

## 3. Mechanism coding

| Question | Finding |
|---|---|
| What is governed? | The permissible **form** of the software's output: a list or prioritised list of options, versus a specific directive |
| What causes the restriction? | The software function's **intended purpose**, assessed by the regulator |
| Runtime or design-time? | **Design-time.** A determination about the software function, fixed regardless of clinical context |
| External state or AI-internal? | Neither. There is no state variable |
| AI participation changed? | No |
| Advisory content changed? | No — the guidance classifies software, it does not modulate output at runtime |
| Recommendation **type** scope changed? | **Yes in kind, no in mechanism.** Recommendation type is the operative regulatory variable, but it is set once, not conditioned |
| Executable action space changed? | Not applicable |
| Human/AI authority changed? | No |
| Human final authority invariant? | **Yes** — Criterion 4 requires the HCP to be able to review the basis independently and not rely primarily on the recommendation |
| Formal verification? | No |
| Empirical evaluation? | No |

---

## 4. Relevance to this research

Supportive, not threatening. The guidance corroborates that **which type of recommendation a system offers is a meaningful safety-governance variable**, treated as regulatorily load-bearing in a major jurisdiction, with an explicit distinction between offering options and issuing a directive. That independently motivates treating recommendation type as a governed quantity in the architecture.

The distinction is applied **once, to the software's intended purpose**, and does not vary with clinical context. The architecture's move is to make an analogous type-level distinction **runtime and state-conditioned**.

The 2026 revision strengthens rather than weakens this reading: the list-versus-directive distinction survived a deregulatory revision intact, with the change confined to enforcement discretion for the single-clinically-appropriate-option case.

Criterion 4 is a second useful point of contact: it is a regulatory statement of the same principle the architecture asserts structurally — the professional must remain able to decide independently, not defer to the system.

---

## 5. Claims this source supports

- Recommendation/output type is already treated as a meaningful governance and regulatory variable.
- Regulatory practice distinguishes a list or prioritised list of options from a specific preventive, diagnostic or treatment directive, and attaches different consequences to each.
- Preserving the professional's ability to review the basis independently, and not rely primarily on the recommendation, is a stated regulatory requirement.

## 6. Claims this source does NOT support

- It is **not** evidence of a runtime advisory-scope mechanism. The classification is design-time and context-independent.
- It does not condition on any environmental or risk state.
- It provides no formal property, no architecture, and no empirical evaluation.
- It must not be cited as an architectural precedent, nor as evidence that graduated advisory-scope governance exists in regulation.
- It is U.S.-specific and concerns device classification, not safety outcomes.

---

## 7. Limitations and caveats

- **Supportive only. N-13 must not become load-bearing.** The material-equivalence finding rests on TCAS II, not on this guidance.
- Guidance documents represent FDA's current thinking and are not legally binding; they are revised. This document has been revised twice within January 2026 alone.
- The media URL `fda.gov/media/109618/download` now serves the January 2026 version; the same URL previously served the September 2022 version. Always check the date printed on the document.
- Secondary accounts of the 2026 revision are dominated by law-firm advisories and compliance blogs. These are **not** acceptable bibliographic authority; cite the FDA document.

---

## 8. Bibliographic details

- **Title:** Clinical Decision Support Software: Guidance for Industry and Food and Drug Administration Staff
- **Issuing authority:** U.S. Food and Drug Administration — CDRH, CBER, CDER, Office of Combination Products
- **Date on document:** 29 January 2026 (first published 6 January 2026, reissued 29 January 2026)
- **Supersedes:** the September 2022 CDS final guidance; the 6 January 2026 version
- **Docket number:** FDA-2017-D-6569
- **Status:** Final guidance
- **DOI:** none — official government publication
- **URL:** https://www.fda.gov/media/109618/download
- **Guidance landing page:** https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software
- **Access:** Open access
- **Source type:** Official government/regulatory publication (source-quality category C)
- **Peer review:** Not applicable — authority status
- **Classification:** `ACCEPT_AUTHORISED` · `AUTHORISED_REGULATORY_SOURCE` · contemporary (2026)
