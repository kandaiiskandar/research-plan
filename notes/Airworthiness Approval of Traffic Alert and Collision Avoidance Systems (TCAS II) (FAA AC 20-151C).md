# Airworthiness Approval of Traffic Alert and Collision Avoidance Systems (TCAS II), Versions 7.0 & 7.1 and Associated Mode S Transponders (FAA AC 20-151C)

**Citation:** Federal Aviation Administration. (2017). *Airworthiness Approval of Traffic Alert and Collision Avoidance Systems (TCAS II), Versions 7.0 & 7.1 and Associated Mode S Transponders* (Advisory Circular 20-151C). U.S. Department of Transportation. https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-151C.pdf

**Short reference:** FAA AC 20-151C (2017)

**Corpus status:** Added September 2026 by the AMICT novelty-corpus validation task — authorised source for the operational precedent identified by the targeted novelty audit (matrix entry N-01).

**Source class:** `ACCEPT_AUTHORISED` · `AUTHORISED_SOURCE = TRUE` · official aviation-authority certification guidance. Pre-2023 date is admissible under the authorised-source exception; this is the current revision.

---

## 1. What the document is

An FAA Advisory Circular giving guidance for airworthiness approval of TCAS II Versions 7.0 and 7.1 and associated Mode S transponders. Issued **21 July 2017**. It **cancels AC 20-151B** (18 March 2014); AC 20-151, AC 20-151A and AC 20-151B are all recorded as cancelled in the FAA advisory-circular index.

TCAS II is a certified airborne collision-avoidance system. It issues **Traffic Advisories (TAs)**, which alert the flight crew to nearby traffic, and **Resolution Advisories (RAs)**, which recommend a vertical manoeuvre. Both are presented to a human flight crew; TCAS II does not fly the aircraft.

The AC restates the inhibition logic that the equipment must implement — the conditions under which specific advisory types must not be issued.

---

## 2. The advisory-inhibition schedule

From the AC's system-inhibits table. Heights are above ground level, from the radio altimeter.

| Advisory type | Climbing | Descending |
|---|---|---|
| Increase Descent RA | inhibited below 1650 ft | inhibited below 1450 ft |
| Descend RA | inhibited below 1200 ft | inhibited below 1000 ft |
| All RAs (system reverts to TA-only) | inhibited below 1100 ft | inhibited below 900 ft |
| TA voice messages | inhibited below 600 ft | inhibited below 400 ft |

Separately, **Climb and Increase Climb RAs may be inhibited on aircraft-performance grounds**, evaluated per aircraft type against weight, altitude, temperature, flap position and landing-gear configuration, so that the system does not command a manoeuvre outside the aircraft's safe performance envelope.

The bands are nested: as height decreases, the set of advisory types the equipment may issue contracts, and never expands. At the lowest band it is empty.

---

## 3. Mechanism coding

| Question | Finding |
|---|---|
| What is governed? | The set of advisory **types** the equipment may issue to the flight crew |
| What causes the restriction? | Radio-altimeter height AGL, banded; plus aircraft-configuration discretes and performance limits |
| Runtime or design-time? | **Runtime**, continuously, per encounter |
| External state or AI-internal? | **External** — a sensor measurement independent of the advisory logic |
| AI participation changed? | Not applicable — the advisory generator is a deterministic collision-avoidance algorithm, not an AI component. At the lowest bands the advisory function is disabled entirely |
| Advisory content changed? | Yes — an active Descend RA converts to a weaker advisory when the aircraft descends through the inhibit height |
| Recommendation **type** scope changed? | **Yes — nested and monotone in severity, contracting to empty** |
| Executable action space changed? | No. The crew's control authority is untouched |
| Human/AI authority changed? | No transfer of authority to the equipment |
| Human final authority invariant? | **Partially.** The crew flies the aircraft and may deviate, but ICAO procedures expect RA compliance, so authority is procedurally constrained rather than structurally unconditional |
| Formal verification? | No. The schedule is a certified design requirement, not a proved containment property |
| Empirical evaluation? | Extensive operational and encounter-model evidence exists, but not as a governance characterisation and with no binary-versus-graduated comparator |

---

## 4. Relevance to this research

This is the **material-equivalence finding** of the targeted novelty audit. The pattern

    externally measured state → banded classification → nested admissible advisory-type set → human decides

is instantiated in full, in certified equipment, and has been for roughly three decades. The containment runs in the same direction as `A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅`, on a five-band rather than three-state lattice.

The consequence is that **the mechanism pattern cannot be claimed as new**. The contribution is repositioned to formalisation, generalisation and empirical characterisation.

What the AC's mechanism does **not** contain, and what therefore remains available to claim within the reviewed literature:

- a multi-component environmental classifier `S = f(E)` aggregated by max severity — the AC conditions on one scalar plus configuration discretes;
- abstraction as a governance construct separating participation `G(S)` from admissible advisory scope `A_AI(S)`, applicable across domains and advisory generators;
- stated and proved totality, monotonicity and containment properties over the advisory set;
- empirical characterisation of how often an intermediate level changes the governance outcome relative to participation-only governance.

Note that the "it governs a deterministic algorithm, not AI" distinction is **weak here and must not be leaned on**: this project's own Layer 3 is a deterministic rule engine, so the governed component is of the same computational kind.

---

## 5. Claims this source supports

- Advisory-type inhibition conditioned on an externally measured runtime state has operational precedent in certified collision-avoidance avionics.
- The inhibited sets are nested and contract to empty as the measured hazard state worsens.
- The advisories are presented to a human crew, who remain the actor.

## 6. Claims this source does NOT support

- It does not establish any formal containment or monotonicity theorem.
- It does not present the inhibition logic as a general governance construct, nor abstract it beyond TCAS II.
- It does not condition on a multi-component environmental classification.
- It does not assert unconditional human authority; ICAO procedure expects RA compliance.
- It says nothing about AI systems, advisory scope governance as a research concept, or decision support outside collision avoidance.
- It must not be cited as evidence about safety outcomes, trust, or decision quality.

---

## 7. Prohibited wording when citing this source

Do not write that runtime restriction of advisory types by external state is new, unprecedented, or unaddressed in prior work. Do not write "no existing system restricts what may be recommended". Do not present the CAUTION mode as the first realisation of graduated advisory scope.

Permitted framing: *"Advisory-type inhibition conditioned on an externally measured state is established practice in certified collision-avoidance avionics, where resolution-advisory types are progressively inhibited as radio altitude decreases."*

---

## 8. Limitations and caveats

- The AC is certification guidance, not the primary standard. The inhibition logic originates in **RTCA DO-185B (TCAS II MOPS)** and **ICAO Annex 10 Volume IV**, which sit higher in the source hierarchy. Recorded as a potential primary-standard enhancement; not obtained, and not required for the bounded claim above.
- **AC 20-151A is cancelled and must not be cited as current authority.** The targeted novelty audit cited it; the figures are identical in AC 20-151C, so the finding is unchanged. See `data/amict-conference-rebuild/novelty-audit-addendum-001.md`.
- The AC covers TCAS II Versions 7.0/7.1. ACAS X is a separate, later system — see the Cleaveland, Mitsch & Platzer note.

---

## 9. Bibliographic details

- **Title:** Airworthiness Approval of Traffic Alert and Collision Avoidance Systems (TCAS II), Versions 7.0 & 7.1 and Associated Mode S Transponders
- **Document number:** Advisory Circular 20-151C
- **Issuing authority:** Federal Aviation Administration, U.S. Department of Transportation
- **Issue date:** 21 July 2017
- **Cancels:** AC 20-151B, dated 18 March 2014
- **Status:** Current revision. AC 20-151, 20-151A and 20-151B are cancelled
- **DOI:** none — official government publication
- **URL:** https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_20-151C.pdf
- **Access:** Open access
- **Source type:** Official aviation-authority certification guidance (source-quality category D)
- **Peer review:** Not applicable — authority status rather than peer review
- **Classification:** `ACCEPT_AUTHORISED` · authorised · contemporary status current, issue date 2017
