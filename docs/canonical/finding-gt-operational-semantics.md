# Finding: `g_t` Operational Semantics — What the Time Component Should Represent

**Date:** 2026-09-08
**Status:** **Evidence review only. Nothing modified.** `g_t`, Appendix C, the scripts, thresholds, figures, predictions and the register are unchanged. No replacement thresholds are proposed.
**Predecessor:** `finding-gt-provenance-audit.md` established that 06:00 / 17:00 / 19:00 have no source. This review asks the prior question: **what should `t` mean?**

---

## 1. Headline

**An authoritative maritime boundary definition exists, and the project has not been using it.**

**COLREGs Rule 20(b)** — the International Regulations for Preventing Collisions at Sea — requires navigation lights to be exhibited **"from sunset to sunrise."** This is a binding international standard, it applies to the vessels in question, and it defines the operative day/night transition as a **solar event pair, not a clock time**.

Three further results follow, each of which changes how the component should be framed:

1. **COLREGs and the cited study independently treat *darkness* and *restricted visibility* as separate hazards.** Appendix C conflates them — see §3.
2. **The evidence supports a two-state distinction, not three.** No source in the corpus or in the standards establishes an intermediate time-based band — see §6.
3. **A third citation link in the current justification is unsupported.** See §3.3.

---

## 2. Evidence search — what was found at each priority tier

| Tier | Source | Risk evidence? | **Boundary evidence?** |
|---|---|---|---|
| 1. METMalaysia | Wind/sea, thunderstorm, continuous-rain criteria | — | **None.** MET publishes no time-of-day operating criterion. Consistent with `finding-met-lower-boundary-gap.md`: MET issues hazard warnings, not operating-hours rules |
| 2. Malaysian maritime / fisheries | Fisheries Act 1985; Fisheries (Maritime) (Licensing of Local Fishing Vessel) Regulations 1985; DoF Malaysia licensing/zoning (Zones A, B, C…) | — | **None found.** The licensing regime is spatial (zones by distance from shore) and gear-based. **No night-operation restriction or operating-hours rule for Zone A small vessels was located.** Recorded as a negative search result, not proof of absence |
| 3. **International maritime standards** | **COLREGs Rule 20(b)** | Implicitly — the rule exists because darkness raises collision risk | ✅ **YES — "from sunset to sunrise."** The only authoritative boundary definition found at any tier |
| 4. Peer-reviewed, small-vessel | Atacan & Düzbastılar (2023); Dominguez-Péry et al. (2023); Jeong & Im (2023); Gao (2024); Rahim et al. (2024); Yamin et al. (2025) | ✅ Strong for P1 | **None.** See §3 |
| 5. Astronomical / almanac | timeanddate, Gaisma (verified in the provenance audit) | — | Supplies *values* for whichever solar event is chosen; **cannot supply the choice of event** |

**The two evidence questions come apart cleanly.** Risk evidence is abundant and consistent. Boundary evidence exists in exactly one place — COLREGs — and it names sunset/sunrise.

---

## 3. What "night" means in the existing evidence

### 3.1 Atacan & Düzbastılar: a rendered simulator condition

The study applied Fine-Kinney risk assessment across **six bridge-simulator scenarios**:

> calm weather/sea · current (4 knots) · **restricted visibility (100 m)** · **night navigation** · heavy weather (5 Beaufort) · **night + heavy weather**

**"Night navigation" is a scenario label, not a measurement.** It is:

| Candidate meaning | Supported? |
|---|---|
| Astronomical night | ❌ Not stated |
| Absence of daylight | ❌ Not defined; implied by the rendering only |
| **A simulator scenario** | ✅ **This is what it is** — one of six rendered conditions |
| A clock-time interval | ❌ **The paper contains no clock times** |
| A solar-referenced condition | ❌ Not stated |

**No clock boundary can be inferred, and none should be.** The paper compares named conditions; it does not partition a day.

### 3.2 The conflation in Appendix C

Note that **`restricted visibility (100 m)` and `night navigation` were *separate* conditions** in the design. The study therefore treats darkness and restricted visibility as **distinct hazards**.

Appendix C's justification for `t` reads:

> *"Restricted visibility — the principal mechanism by which nighttime elevates risk for small vessels without radar — was rated the single most dangerous factor for sea navigation accident probability (mean 7.90…)"*

**The 7.90 is the score for the *restricted visibility* scenario, not the *night* scenario.** Night navigation scored 4.08 (probability) / 12.80 (consequence). Appendix C borrows the highest-scoring condition in the study to justify a *different* variable, on the argument that visibility is the mechanism of night risk — but the study's own design treats them as separate, and so does COLREGs (§3.4). **This is an evidential conflation and should be corrected regardless of what happens to the thresholds.**

The `r` variable, not `t`, is where rain-driven visibility restriction enters the model; fog and haze are in no component at all.

### 3.3 A third unsupported link, found during this review

The Atacan extraction note lists as supporting evidence:

> *"Rahim et al. (2024) — Malaysian fishers behaviourally self-restrict departure timing based on environmental conditions, with departure patterns showing sensitivity to daylight availability."*

**The Rahim et al. extraction notes contain no such content.** A full-term sweep of that file returns **zero** occurrences of *daylight*, *night*, *dawn*, *dusk*, *departure timing*, *morning* or *evening*; the single "hour" match is unrelated. Rahim et al. concerns **survival decisions under extreme weather and economic compulsion**, not diurnal departure patterns.

**Status: unsupported claim.** It is not cited in Appendix C itself, but it appears in the notes as corroboration for the time variable and should be struck.

### 3.4 What the corpus does *not* contain

**No corpus paper provides an accident-by-time-of-day distribution.** Dominguez-Péry et al. state explicitly that the paper *"does not isolate time of day as a standalone statistical variable"* — time appears only as an IMO metadata field. Jeong & Im's 66 capsizings carry no time-of-day data. Gao and Yamin have none.

**Consequence:** there is no empirical basis anywhere in the corpus for locating a risk transition at any particular time, solar or clock. The evidence establishes *that* night is riskier, never *when* the risk changes.

---

## 4. Geographical applicability

Established in the provenance audit and unchanged here: at Kota Kinabalu (5.98° N, 116.07° E) sunrise ranges **06:01–06:34** and sunset **17:57–18:35**.

**If a solar semantics is adopted, it must be computed from (date, latitude, longitude), not fixed.** Three reasons:

1. **Sunset moves 38 minutes across the year** at this site — wider than any plausible tolerance for a boundary intended to mark darkness.
2. **Longitude within the time zone matters more than latitude here.** Kota Kinabalu sits ~13° east of Kuala Lumpur in the same UTC+8 zone, so its solar day runs ~50–70 minutes earlier. A threshold calibrated on peninsular Malaysia is wrong for Sabah by more than the annual variation — which is exactly the error the provenance audit found in the extraction note.
3. **Transferability.** The architecture claims domain-independence. A solar-referenced `g_t` transfers to any site by construction; a fixed-clock `g_t` requires re-derivation per deployment and silently fails if that step is skipped.

**No solar event is selected here.** Sunset/sunrise, civil twilight and nautical twilight all remain open; §7 records what would decide between them.

---

## 5. Evidence class of each candidate boundary

| Candidate | Boundary | Class |
|---|---|---|
| **A** Fixed clock policy | 06:00 / 17:00 / 19:00 | **Policy-defined** — *if and only if* presented as a governance design choice. **Currently presented as empirically derived, which is unsupported** |
| **B** Sunrise / sunset | sunrise, sunset | **Regulation-derived** — COLREGs Rule 20(b), "from sunset to sunrise" |
| **C** Civil twilight | civil dawn / dusk | **Proxy-derived** — a defensible proxy for usable natural light; no maritime standard located that adopts it as an operating boundary |
| **D** Nautical twilight | nautical dawn / dusk | **Proxy-derived** — the horizon-visibility definition, relevant to celestial navigation rather than small-vessel operation; no source located applying it to this population |
| **E** Other maritime definition | — | **None found.** Searched tiers 1–5; only COLREGs supplies an operating boundary |

**Only one candidate is regulation-derived.** A is acceptable but requires the justification to be rewritten as policy. C and D are proxies that would need their own justification for preferring them over the regulated boundary.

---

## 6. Do three states survive the evidence?

**Assessed separately, as instructed:**

| Proposition | Evidence |
|---|---|
| daylight = SAFE | ✅ Supported. Both the study's baseline condition and COLREGs' implicit "no lights required" period |
| **transition / twilight = CAUTION** | ❌ **No source found.** Atacan & Düzbastılar tested no twilight condition. COLREGs has no intermediate state — lights are required or they are not. No corpus paper reports a graded risk profile across dusk |
| night = UNSAFE | ✅ Supported as *elevated risk*. Whether it warrants full AI withdrawal is an architecture decision, not an evidence finding |

**The evidence supports a two-state distinction — daylight versus night — not three.**

This is a real finding and it cuts against the model's structure. Two readings are available and they are not equivalent:

- **The intermediate band is a governance design choice.** The architecture's contribution *is* a graduated middle state; applying it to time is consistent with that thesis. But then the CAUTION band is **policy-defined**, and must be labelled so.
- **The intermediate band is unsupported for time specifically.** `g_t` could be two-state (SAFE / UNSAFE) while `g_o` and `g_r` remain three-state. Nothing in the architecture requires every component to have three levels — max-severity aggregates over `{SAFE, CAUTION, UNSAFE}` regardless of each component's range.

**The second reading is worth stating plainly because it is uncomfortable:** the component that produces 87.63% of non-SAFE classifications may not need its middle state at all, and no evidence has ever been offered for it.

---

## 7. Candidate semantics — comparison

| Candidate | Meaning of `t` | Evidence strength | Local applicability | Supports 3 states? | Main limitation |
|---|---|---|---|---|---|
| **A. Fixed clock policy** | Permitted vs restricted operating period | **Policy only.** No source supports the values | ❌ Poor — 06:00 precedes sunrise year-round; 17:00 is ~1–1.5 h before sunset | Only as policy | Must be relabelled as a design choice; currently misdescribed as empirical |
| **B. Sunrise / sunset** | Daylight vs night | **Strongest — regulation-derived.** COLREGs Rule 20(b) | ✅ Computed from (date, lat, lon); transfers to any site | ❌ Two states natively | No intermediate band; requires a solar computation in the pipeline |
| **C. Civil twilight** | Usable natural light | **Proxy.** Astronomically well-defined; no maritime standard located adopting it | ✅ Same computation | ⚠️ Could support 3 (sunset→civil dusk as CAUTION) — **but that band would be proxy-derived, not evidenced** | Chosen for convenience of yielding a middle band, which is the wrong reason |
| **D. Nautical twilight** | Horizon still discernible | **Weak for this population.** Celestial-navigation concept; no source applying it to small coastal vessels | ✅ Same computation | ⚠️ As C | Least appropriate to the population; no supporting evidence located |
| **E. Other** | — | **None found** | — | — | Tiers 1–5 searched; only COLREGs supplies a boundary |

### Recommended for quantitative sensitivity testing

**B and C, tested against the current A.** Reasons:

- **B is the only regulation-derived option** and is the natural null: it is what the governing international standard already requires vessels to observe.
- **C is the only candidate that could support a three-state `g_t` on a principled basis** — the sunset→civil-dusk interval is a real, computable transition period. **It must be tested, not assumed**, and if adopted the CAUTION band is proxy-derived and must be labelled so.
- **A should be retained in the comparison as the incumbent**, so the effect of any change is measurable against the published figures.
- **D is not recommended for testing** — no evidence links nautical twilight to this population, and including it would be testing an option nothing supports.

**Sensitivity testing is not a threshold decision.** It would quantify how §0a moves under B and C, which the provenance audit identified as the missing analysis. The decision on semantics should follow the numbers, not precede them.

---

## 8. What this review did not do

No threshold proposed. No solar event selected. `g_t` unchanged, Appendix C unchanged, scripts unchanged, replay not re-run, figures unchanged (7.72% / 5.98%), predictions unchanged (22 confirmed / 2 refuted), register untouched.

**Two corrections are warranted independently of any `g_t` decision**, because they are misattributions rather than threshold questions:

1. **The 7.90 restricted-visibility score should stop being cited as evidence for `t`** (§3.2). It is the score for a different scenario, and both the study and COLREGs treat visibility and darkness as separate hazards.
2. **The Rahim et al. daylight claim in the Atacan extraction note should be struck** (§3.3). The cited notes contain no such content.

Neither requires touching a threshold.

---

## 9. Sources

| Source | Tier | Establishes |
|---|---|---|
| [COLREGs Rule 20 — Application](https://www.cultofsea.com/colregs/part-c-lights-and-shapes-rules-20-31/rule-20-application/) · [eColRegs Rule 20](https://ecolregs.com/index.php?option=com_k2&view=item&layout=item&id=60&Itemid=393&lang=en) | 3 | **"From sunset to sunrise"** — the only authoritative operating boundary found. Also: restricted visibility is a **separate** trigger, applying "from sunrise to sunset" |
| [DoF Malaysia — Licensing FAQ](https://www.dof.gov.my/en/frequently-asked-questions/licensing-faq/) · [Fisheries (Maritime) (Licensing of Local Fishing Vessel) Regulations 1985](https://www.ecolex.org/details/legislation/fisheries-maritime-licensing-of-local-fishing-vessel-regulations-1985-lex-faoc001878/) · [Fisheries Act 1985](https://faolex.fao.org/docs/pdf/mal1869.pdf) | 2 | Zoning and licensing are **spatial and gear-based**; no night-operation or operating-hours rule located |
| [SEAFDEC — Fisheries Country Profile: Malaysia 2025](https://www.seafdec.org/fisheries-country-profile-malaysia/) | 2 | Corroborates the zoning structure; no time-of-day provision |
| Atacan & Düzbastılar (2023) [[notes]](../../notes/Determination%20of%20risk%20perception%20in%20small-scale%20fishing%20and%20navigation.md) | 4 | Night riskier than day (P1). **"Night navigation" is a simulator scenario. No clock times. Restricted visibility is a separate condition scoring 7.90** |
| Dominguez-Péry et al. (2023) [[notes]](../../notes/A%20holistic%20view%20of%20maritime%20navigation%20accidents%20and%20risk%20indicators-%20examining%20IMO%20reports%20from%202011%20to%202021.md) | 4 | Visibility is the largest risk cluster. **Explicitly does not isolate time of day as a variable** |
| timeanddate / Gaisma (verified in the provenance audit) | 5 | Kota Kinabalu sunrise 06:01–06:34, sunset 17:57–18:35 |

---

## 10. Related

| Document | Relationship |
|---|---|
| `finding-gt-provenance-audit.md` | Establishes that the current values have no source; this review asks what should replace the *semantics*, not the numbers |
| `finding-met-lower-boundary-gap.md` | Same provenance discipline. MET's silence on operating hours is consistent with its role: it issues hazard warnings, not operating rules |
| `appendix-c-formalisation.md` C.1 time-of-day note, C.2 `g_t`, C.9.1 | Where the conflation in §3.2 sits and where any correction would land |
| `notes/Determination of risk perception…md` | Contains the unsupported Rahim claim (§3.3) and the peninsular-Malaysia twilight error identified in the provenance audit |
