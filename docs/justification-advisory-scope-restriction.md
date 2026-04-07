# Why Advisory Scope Restriction? Justification for the CAUTION Mode

**Document type**: Theoretical justification / argumentation note  
**For**: Chapter 2 (Literature Review) and Chapter 3 (Architecture Design)  
**Question addressed**: Why does the CAUTION mode restrict AI advisory scope rather than (a) blocking AI entirely, or (b) reducing autonomy level?

---

## 1. The Central Claim

In the CAUTION state, the proposed architecture does not block AI participation. It does not hand decision authority back to the human. Instead, it **narrows the set of recommendation types the AI is permitted to make** — from the full advisory scope in SAFE (go/no-go + departure time + trip duration + fishing area + route) to a restricted scope in CAUTION (go/no-go + delay guidance only).

Formally: A_AI(CAUTION) ⊂ A_AI(SAFE), where both are non-empty.

This is architecturally distinct from both blocking (A_AI = ∅) and authority reduction (same A_AI, smaller human override probability). The question is: why?

---

## 2. Why Not Simply Block AI?

### 2.1 Blocking Violates ALARP

The foundational principle of risk management — ALARP (As Low As Reasonably Practicable) — requires that risk be reduced to the lowest level that is *reasonably practicable*, not to the lowest level that is *technically possible*. Total AI blocking under CAUTION conditions is not ALARP-compliant if a less restrictive measure (scope restriction) achieves the same safety outcome.

The hierarchy of risk controls in safety engineering is:

```
Eliminate → Substitute → Isolate → Control → Reduce → Accept
```

Total AI blocking is an *isolation* measure. Advisory scope restriction is a *control* measure. Control is preferred over isolation when it achieves equivalent safety — because isolation removes value as well as risk. In the CAUTION mode, go/no-go guidance remains reliable and valuable. Blocking AI removes this reliable value along with the unreliable detailed recommendations.

Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) note directly that binary blocking creates its own hazards: "excessive false alarms could lead to new system-level hazards (e.g., cascade errors in systems with multiple safety functions) and should also consider human cognitive limitations (e.g., cognitive overload, oversight and reaction time limitations)." This observation — derived from the cross-domain survey of safety-critical AI in automotive, avionics, railway, and industrial systems — confirms that binary blocking is not always the appropriate risk control; it can itself introduce harms that proportionate controls avoid.

### 2.2 Blocking Creates a False Dilemma

Binary governance (block or allow) forces a structural false dilemma between two costly failure modes:

- **Over-restriction**: Blocking AI entirely under moderate risk removes a scarce decision support resource at precisely the moment when the human faces elevated environmental complexity. In low-resource settings, the fisher may have no alternative information source. The cost of over-restriction is not zero — a fisher making a go/no-go decision without any AI guidance under CAUTION conditions may make a worse decision than one receiving restricted but reliable guidance.

- **Under-restriction**: Allowing full AI participation under elevated risk exposes the user to recommendations (precise departure times, trip durations) whose underlying data assumptions are violated under CAUTION conditions. The cost is not the AI being wrong by a small margin — it is false precision that the human may anchor on and trust.

The empirical record of small-scale fisher behaviour under marginal conditions reinforces why neither extreme is adequate. Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) document that Indonesian coastal fishers routinely override binary "do not sail" warnings issued by the Ministry of Maritime Affairs because these all-or-nothing advisories do not align with the adaptive scope restriction behaviour fishers actually employ: during marginal weather, fishers shift to near-shore areas, reduce trip duration from 7–10 hours to 3–5 hours, and cut trip frequency from 5–6 to 2–3 per week. They do not stop; they restrict scope. A governance model that blocks AI entirely replicates the bluntness of these binary warnings — which the empirical record shows are systematically ignored.

The CAUTION mode resolves this dilemma by occupying the middle ground that binary governance cannot reach: AI remains active, providing value where it can, and falls silent where it cannot.

Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md), reviewing 91 papers on collaborative intelligence for safety-critical industries, confirm that this middle ground is entirely absent from the existing literature: across all 91 papers, governance mechanisms are binary — AI operates or is overridden/blocked. No reviewed paper implements graduated governance where AI participates with restricted recommendation scope under intermediate risk conditions.

### 2.3 Not All Recommendations Degrade Equally

Binary blocking treats all AI recommendations as a single undifferentiated output. This is wrong. Different recommendation types have different **reliability profiles** under elevated environmental conditions:

| Recommendation type | SAFE reliability | CAUTION reliability | Why degradation differs |
|---|---|---|---|
| Go/no-go directional | High | **Still high** | Depends on threshold crossing, not precise estimation |
| Delay guidance (wait, depart tomorrow) | High | **Still high** | Depends on trend direction, not precise timing |
| Departure time (depart at 06:15) | High | **Low** | Requires precise sea-state estimation — degrades under uncertainty |
| Trip duration estimate | High | **Low** | Requires reliable current/wind modelling — degrades under CAUTION |
| Fishing area recommendation | High | **Low** | Requires good environmental prediction — unreliable under CAUTION |
| Route optimisation | High | **Low** | Requires stable conditions — invalid under variable CAUTION state |

Blocking AI because precise recommendations are unreliable also blocks go/no-go guidance that remains reliable. This is the wrong unit of governance. The correct unit is the **recommendation type**, not the AI system as a whole.

The cross-domain evidence from Madsen & Kim (2024) [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md), reviewing AI decision transparency for autonomous shipping, confirms this differentiation is already implicitly recognised in adjacent domains: colour-coded risk classification schemes in maritime collision avoidance (green/amber/red, based on TCPA/CPA values) are used to display risk information at different levels of granularity. However, Madsen & Kim (2024) [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md) identify a critical gap — the risk classification conditions only the *display* to the human, not the *AI's permitted output types*: "none of the studies identified in this review evaluated how proposed strategies, visualization, or technology affect systems' or individual operators' [situational awareness]." Advisory scope restriction fills this gap by making the same principle operational: it is not enough to tell the human the risk level; the AI's output space must itself be conditioned on that level.

### 2.4 The Safety Envelope Is Recommendation-Type-Specific

Safety envelope theory in control systems defines the boundary beyond which a system cannot operate safely. Different system functions have different safety envelopes — the envelope for one function is not the envelope for all.

In fly-by-wire aviation (Airbus flight envelope protection), the system does not block the pilot when the aircraft approaches a structural limit — it restricts the specific control inputs that would violate the envelope, while continuing to assist with all other inputs. This is not a reduction in autonomy; it is scope restriction. The pilot retains full decision authority; the automation restricts what it will assist with.

Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) review this pattern in automated driving systems, where the Operational Design Domain (ODD) defines the boundary conditions for system operation, with Restricted Operational Domains (RODs) providing intermediate states between full operation and the Minimal Risk Condition (MRC). Critically, they identify that "the safe, warning and catastrophic states" partition for monitoring purposes exists in the automotive literature — but note that no reviewed method connects this partitioning to a discrete mechanism governing what types of recommendations AI may produce. Advisory scope restriction applies the same envelope principle to AI decision support: the AI's "flight envelope" for precise recommendations narrows under CAUTION, while its envelope for directional recommendations remains wide.

Similarly, Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) show through their architectural taxonomy of guarded AI systems that the nuclear power "ladder of protection" — operational control → limitation system → shutdown system — implicitly recognises the value of an intermediate limitation mode. Their analysis of Architecture 8 (the most sophisticated guarded configuration) confirms, however, that even this advanced pattern implements only binary permit/override control at each guard layer, with no intermediate mode restricting AI advisory scope. Advisory scope restriction formalises the limitation layer that nuclear safety practice acknowledges but that guarded AI architectures have not yet implemented.

---

## 3. Why Not Just Reduce Autonomy?

### 3.1 What Autonomy Reduction Actually Means

"Reducing autonomy" means shifting the locus of decision authority from AI to human — for example, moving from "AI decides, human monitors" to "AI recommends, human decides." Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) classify this across 91 collaborative intelligence papers: supervisor controllers, shared control arbitration, and simplex switching all implement authority redistribution between human and AI without changing the content of what the AI produces. Porter et al. (2025 — INSYTE) formalise this as two orthogonal classification dimensions: Dimension 7 (intervention independence — can AI act without human approval?) and Dimension 8 (oversight independence — can AI operate without human monitoring?). Both dimensions govern authority; neither governs recommendation content.

This is a governance action on the **decision authority** dimension, not the **recommendation content** dimension. The AI still produces the same recommendations — the difference is the weight the human places on them, and whether the human must explicitly confirm.

### 3.2 Autonomy Reduction Without Scope Restriction Exposes Humans to Unreliable Information

Reducing autonomy under CAUTION — for example, requiring the human to confirm all AI recommendations — does not solve the core problem. The AI is still generating precise departure times, trip duration estimates, and route recommendations under conditions where these are unreliable. The human receives this information, must evaluate it, and must decide whether to follow it.

This creates several human factors problems:

**Anchoring bias**: The human sees "recommended departure: 06:15, estimated trip duration: 8 hours" and anchors on these values even while attempting to evaluate them critically. Schrills et al. (2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) demonstrate empirically that communicated system reliability — not the human's own assessment of the information — is the dominant driver of reliance behaviour: participants anchored their dependence on the instructed reliability level even under conditions where they had independent grounds to doubt it. A precise AI recommendation communicates high reliability implicitly, irrespective of whether that precision is warranted under current conditions.

**Automation bias**: Humans systematically over-rely on automated recommendations, particularly when under cognitive load. Under CAUTION conditions — elevated environmental stress, time pressure, safety concerns — the human is at maximum susceptibility to automation bias. Presenting unreliable precise recommendations under these conditions is actively harmful. Wen et al. (2025) provide cross-domain empirical evidence for the severity of this problem: analysing 60 real-world accident reports across process control and autonomous vehicle domains, they find that over-reliance on automation contributed to failures in 20% of process control cases and 30% of autonomous vehicle cases, with human intervention proving ineffective in 83.3% and 66.7% of cases respectively. The implication is direct: in safety-critical systems, reducing autonomy without removing unreliable content does not reliably protect against automation bias, because humans fail to exercise effective override even when authority nominally rests with them.

**Cognitive overload**: Evaluating whether an AI recommendation is trustworthy under elevated conditions requires the human to perform a meta-cognitive assessment on top of the already elevated primary task. This is cognitive work the human cannot spare. Scope restriction performs this meta-cognitive assessment systematically and reliably at the architecture level, removing it from the human's cognitive burden. Mussi et al. (2025), reviewing human-AI interaction across power grid, railway, and air traffic management domains, propose "progressive disclosure" — delivering explanatory information in phases to avoid cognitive overload — as a design principle. Advisory scope restriction operationalises this principle at the output level: in CAUTION, the AI discloses only what the human can usefully process under elevated conditions.

**False precision effect**: A recommendation of "depart at 06:15" implies a level of precision that the underlying model cannot support under CAUTION conditions. Even if the human reduces the weight they give this recommendation, the presence of a precise number creates an implicit confidence signal that misrepresents the model's actual reliability. Atf & Lewis (2026) [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md) provide meta-analytic evidence that even the provision of explanations (which is a weaker transparency mechanism than precision suppression) has only a weak positive correlation with appropriate trust (r = 0.194 across 90 studies), accounting for approximately 3.8% of variance in trust. This finding underscores that providing unreliable precise information and then explaining its limitations is insufficient: "explanations can lead to 'over-reliance on incorrect information if not carefully managed'" (Atf & Lewis, 2026 [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md), citing Ayoub et al., 2021). Suppressing false-precision outputs removes the problem at source.

### 3.3 Autonomy Reduction Changes Who Decides; Scope Restriction Changes What Is Decided

This distinction is fundamental:

| Governance action | Changes decision authority | Changes recommendation content | Protects against anchoring | Removes false precision |
|---|---|---|---|---|
| Reduce autonomy | Yes — human decides | No — AI still recommends everything | No | No |
| Block AI | Yes — AI removed | Yes — no recommendation | Yes | Yes (by absence) |
| **Advisory scope restriction** | **No — AI still advisory** | **Yes — only reliable types** | **Yes** | **Yes** |

Advisory scope restriction achieves what autonomy reduction cannot: it removes the *unreliable content* from the AI output while maintaining AI participation. This is not a weaker version of blocking — it is a structurally different governance action operating on a different dimension.

---

## 4. Theoretical Foundations for Advisory Scope Restriction

### 4.1 Risk Management: Information Quality as a Safety Property

Risk management frameworks (ISO 31000, IEC 61508) treat information quality as a safety-relevant property. An information source that provides systematically unreliable outputs under specific conditions is a *hazard*, not merely a suboptimal tool. The hazard is not the information being wrong — it is the human trusting information that is wrong.

Advisory scope restriction is a **risk control** applied to the information quality hazard:
- **Hazard**: AI provides precise departure time under CAUTION conditions where sea-state prediction is unreliable
- **Risk**: Fisher anchors on this recommendation and departs at a dangerous time
- **Control**: Remove departure time recommendations from A_AI(CAUTION)

This frames scope restriction as a standard risk engineering measure, not an architectural novelty. Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) confirm this framing within the safety-critical AI literature: safety bags and safety envelopes — the canonical risk control mechanisms for AI in certified systems — function by enforcing boundaries on AI outputs, not by blocking the AI system entirely. Advisory scope restriction is a recommendation-type-specific safety envelope: the AI's output space is bounded by what can be reliably supported under current environmental conditions.

### 4.2 Bounded Rationality: Less Information of Higher Quality

Herbert Simon's bounded rationality (1955) establishes that human decision-making is limited by cognitive capacity and information processing constraints. Under elevated environmental conditions, the fisher's cognitive capacity is already partially consumed by heightened vigilance and situation assessment.

**Gerd Gigerenzer's ecological rationality** extends this: in many real-world decision environments, *less information* processed by *simpler heuristics* produces better decisions than more information processed by complex analysis. The CAUTION mode implements this insight: by restricting advisory scope to go/no-go and delay guidance, it provides the information that supports the critical decision (whether to fish today) without the additional information that would overwhelm the decision-maker's bounded capacity under elevated conditions.

This is not dumbing down the AI — it is ecologically rational governance: match the AI's information output to the human's processing capacity under current conditions. Mussi et al. (2025) arrive at the same design principle from the infrastructure domain, arguing that AI systems in safety-critical operations must "optimis[e] the degree of decision support" rather than maximise information provision, and that "progressive disclosure" — phased rather than comprehensive information delivery — reduces cognitive overload in high-stakes environments.

### 4.3 Decision Theory: Value of Information Under Uncertainty

In decision theory, the **Value of Information (VOI)** is the difference in expected utility between a decision made with information and a decision made without it. VOI is positive when information improves expected outcomes and negative when it degrades them (by misleading the decision-maker).

Under CAUTION conditions:

- **VOI(go/no-go guidance)** = positive — even under elevated conditions, the AI's directional assessment (go or no-go) is more reliable than the fisher's unaided estimate under weather uncertainty. This information improves expected outcomes.

- **VOI(precise departure time)** = negative — the AI's precise timing recommendation is derived from models that assume reliable sea-state data. Under CAUTION, this assumption is violated. The recommendation conveys false precision. A fisher who ignores it is no worse off; a fisher who anchors on it may be worse off than if no recommendation had been made.

Advisory scope restriction is the operational implementation of VOI management: provide information when VOI > 0, suppress it when VOI < 0 or ≈ 0.

Atf & Lewis (2026) [[notes]](../notes/Is%20Trust%20Correlated%20With%20Explainability%20in%20AI%3F%20A%20Meta-Analysis.md) provide quantitative support for this framing: their meta-analysis establishes that the provision of information (in the form of explanations) has only a weak positive effect on trust (r = 0.194), and that "interpretable models can 'engender distrust' as well as trust" — that is, transparency about limitations can reduce trust below appropriate calibration. This is precisely the VOI argument: when information has negative or near-zero value (it misleads or overwhelms), withholding it is the rational governance action.

### 4.4 Human Factors: Trust Calibration and Mode Awareness

**Trust calibration** (McGrath et al., 2025 [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md) — CHAI-T; Bach et al., 2024) requires that user trust in an AI system matches the system's actual reliability. If an AI provides precise recommendations under conditions where precision is unjustified, the user cannot distinguish reliable from unreliable outputs — trust cannot be calibrated.

McGrath et al. (2025 [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md) — CHAI-T) state this directly: "Trust in a machine system is considered to have reached its optimal level and, consequently, best facilitate performance outcomes, when the human trustor's expectations are aligned with the capabilities of system. When optimal levels of trust are exceeded... the resulting overreliance and lack of monitoring can have catastrophic outcomes." This is precisely the failure mode that scope restriction prevents: by restricting AI output to recommendation types whose reliability can be guaranteed under CAUTION conditions, the architecture ensures that user trust in those recommendations is appropriate — they can be depended upon fully within the restricted scope.

The same framework confirms the risks of the alternative: "A failure to reach optimal levels of trust, on the other hand, can result in disuse of technological systems, representing a waste of time and resources" (McGrath et al., 2025 [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md) — CHAI-T). This justifies why full AI blocking is also suboptimal: it creates undertrust for the go/no-go and delay guidance that remains reliable, leading to disuse of valuable and trustworthy advice.

Advisory scope restriction enforces calibration at the architectural level:
- In SAFE: full scope → user can trust all recommendation types
- In CAUTION: restricted scope → user knows only go/no-go and delay are being provided; can trust these fully
- In UNSAFE: no AI → user knows AI is unavailable; no trust misplacement possible

This is a **trust calibration mechanism**: the architecture prevents the user from over-trusting unreliable recommendations by not making them. Schrills et al. (2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) distinguish trust (attitude) from dependence (behaviour) and demonstrate empirically that "instructed reliability appears to be more influential in determining behaviour compared to assessed trust... participants complied with system recommendations depending on the instructed reliability of the system across various conditions." This finding is directly applicable: the CAUTION mode's restricted scope functions as a communicated reliability signal — by providing only go/no-go and delay guidance, the architecture communicates to the user that these are the reliable recommendation types under current conditions, anchoring their dependence appropriately. Schrills et al.'s (2025) [[notes]](../notes/Questioning%20Trust%20in%20AI%20Research-%20Exploring%20the%20Influence%20of%20Trust%20Assessment%20on%20Dependence%20in%20AI-Assisted%20Decision-Making.md) finding that users engage in "probability matching" — calibrating their reliance to the communicated system capability — predicts that users will appropriately reduce their dependence on restricted AI output, achieving exactly the trust calibration the architecture is designed to produce.

**Mode awareness** refers to the human operator's understanding of what automated systems are currently doing and what their capabilities are. Wen et al. (2025) document the consequences of poor mode awareness empirically: across 60 real-world accident reports in process control and autonomous vehicle domains, a recurring failure pattern is operators misunderstanding automation state — treating a system as active when it is in a degraded or limited mode, or vice versa. They find human interventions were ineffective in 83.3% of process control incidents and 66.7% of AV incidents, attributing this partly to mode confusion that delayed or misdirected operator response.

Advisory scope restriction addresses mode awareness directly: the CAUTION mode makes explicit to the user what the AI *is not* doing. The restricted scope is a clear signal of the AI's current capability boundary. Compared to a system that continues providing all recommendation types at varying (but undisclosed) confidence levels, scope restriction makes the AI's current state fully legible. This addresses a gap identified by Bach et al. (2024): reviewing 23 empirical studies on user trust in AI systems, they find that "a mismatch between user expectations and system behaviour" is a primary risk to trust, and that "expectation mismatch between user expectations and system capabilities" is a recurring source of failure. Advisory scope restriction prevents this mismatch by ensuring the AI's output space is precisely aligned with what the system can reliably deliver under current environmental conditions.

### 4.5 Safety Envelope Theory: Recommendation-Space Envelopes

The **operational envelope** (or safety envelope) defines the range of conditions under which a system can operate safely. Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) review this principle extensively in automated driving: fly-by-wire aircraft and ADS both employ envelope protection — restricting control inputs or system actions that would exceed safe operational boundaries — without blocking the human or system entirely. The pilot retains full authority; the automation restricts what it will assist with near structural limits.

The analogy to advisory scope restriction:

| Aviation | Proposed architecture |
|---|---|
| Flight envelope (structural limits) | Advisory envelope (reliability limits per recommendation type) |
| Envelope protection restricts control inputs near structural limits | Scope restriction removes recommendation types beyond their reliability envelope |
| Pilot retains full decision authority | Fisher retains full decision authority |
| Aircraft continues to fly; some inputs become unavailable | AI continues to advise; some recommendation types become unavailable |
| Not a loss of autonomy — a restriction of automation assistance | Not a loss of AI — a restriction of AI advisory scope |

This is not a novel concept — it is the application of an established aviation safety principle to the AI advisory layer. Gyllenhammar et al. (2025) [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md) confirm that the ODD → ROD → MRC hierarchy in automated driving systems implements the same principle architecturally: as operational conditions worsen, the system's admissible operational scope contracts. The key difference is that their ROD is triggered by system degradation (internal faults), not by environmental safety state classification — the gap this architecture fills by conditioning scope restriction on S = f(E).

Bloomfield & Rushby (2025) [[notes]](../notes/Assurance%20of%20AI%20Systems%20From%20a%20Dependability%20Perspective.md) observe that the nuclear power limitation system (sitting between operational control and emergency shutdown) is the closest conceptual analogue in certified safety practice. Their work confirms, however, that this limitation concept has not been formalised as a restriction on AI *recommendation types* in any existing guarded architecture. Advisory scope restriction provides this formalisation.

### 4.6 Maritime Safety Practice: Informal Scope Restriction Already Exists

Yamin et al. (2025) [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md), in a primary survey of 136 small-scale fishers in central Terengganu, Malaysia (*Frontiers in Marine Science*, Q1), provide the strongest current empirical grounding for why advisory scope restriction — and specifically the CAUTION mode — is architecturally necessary. Three findings are directly relevant.

First, the binary status quo is confirmed by primary data: the empirical knowledge item "I know if it's suddenly windy/change of weather, I can't go fishing" documents that under elevated environmental conditions, the only documented decision is binary cessation. No intermediate advisory scope is reported.

Second, flexibility is the weakest adaptive capacity domain in this population (Figure 9, Yamin et al., 2025 [[notes]](../notes/Interplay%20of%20traditional%20knowledge%20and%20adaptive%20capacity%20in%20climate%20change%20adaptation%20of%20small-scale%20fishers%20in%20central%20Terengganu%2C%20Malaysia%20.md)): only 58% of fishers are willing to consider alternative livelihoods; 67.6% rely solely on fishing for income. This means fishers lack the *operational flexibility* to self-restrict scope under intermediate risk without structured support — making advisory scope restriction not merely a governance design choice but an active capacity-building mechanism.

Third, traditional weather prediction ability is declining. Fishers increasingly rely on weather apps (Windy, Windfinder) for raw data but have no system that translates environmental data into scope-restricted decisions. This creates the precise decision support vacuum that the CAUTION mode fills: the AI provides what the apps do not — an actionable, scope-limited recommendation (go/no-go + delay guidance) rather than raw data that the user must interpret alone under elevated stress.

Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) documents that Penang fishers implement informal scope restriction in their *cautious-go* decision:

- **Go**: full fishing trip, normal scope — depart on schedule, fish planned area, return as planned
- **Cautious-go**: restricted scope — depart later, fish closer inshore, return earlier, avoid exposed areas
- **Don't-go**: no trip

The *cautious-go* is not a reduction in the fisher's decision authority — the fisher is still making all decisions. It is a restriction of the *scope of the fishing operation* under elevated conditions. The fisher is still participating, but with reduced operational scope. Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) further establishes the empirical validity of this tripartite classification by demonstrating that fishers' informal state assessment is driven by exactly the environmental variables the proposed architecture formalises: tide (importance 4.55), fishing resources (4.45), weather (3.75), and safety concern (3.40). The architecture's S = f(E) → {SAFE, CAUTION, UNSAFE} formalises what fishers do intuitively.

Advisory scope restriction in the proposed architecture formalises this at the AI recommendation layer: in CAUTION, the AI recommends the *scope-restricted* information that supports the cautious-go decision (should I go? should I wait?) without providing the *full-scope* information that assumes normal operating conditions (when exactly, for how long, where specifically).

Earlier background work — Shaffril et al. (2017) [[notes]](../notes/Adapting%20towards%20climate%20change%20impacts-%20Strategies%20for%20small-scale%20fishermen%20in%20Malaysia%20.md), studying Malaysian small-scale fishermen — documented that fishermen operating vessels ≤22 feet within <5 nautical miles of shore responded to elevated environmental risk with binary cessation: operating days were reduced by up to 90% during the north-east monsoon, with no intermediate operational scope restriction recorded for this population. While nearly a decade has passed since this study and the Malaysian fishing sector has evolved, it provides historical context supporting the claim that the *cautious-go* advisory scope the proposed CAUTION mode formalises had no formal decision support analogue for Malaysian fishers at the time — informal intermediate practice, while documented in Penang (Gao, 2024) and Indonesia (Rahim et al., 2024), had not been formalised or supported by any advisory system in the Malaysian context. The population profile documented by Shaffril et al. (2017) [[notes]](../notes/Adapting%20towards%20climate%20change%20impacts-%20Strategies%20for%20small-scale%20fishermen%20in%20Malaysia%20.md) — MCE-or-lower education, aged >40, mobile phone users — provides background context for why environmental-state-based governance ("CAUTION: winds elevated, fishing scope restricted") is the appropriate governance trigger for this user group rather than confidence-based or uncertainty-based alternatives. More current domain characterisation would be required to confirm whether these socio-technical constraints remain unchanged; Shaffril et al. (2017) [[notes]](../notes/Adapting%20towards%20climate%20change%20impacts-%20Strategies%20for%20small-scale%20fishermen%20in%20Malaysia%20.md) is cited here for historical contextual grounding, not as primary evidence of present-day practice.

Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) independently confirm the empirical validity of this intermediate state from a different coastal fisheries context (coastal Makassar, Indonesia): during marginal conditions (East season — high precipitation but calm seas), fishers neither fully cease operations nor operate at full scope, but shift to near-shore areas, reduce trip duration, and reduce frequency. This behaviourally documented intermediate state — neither full operation nor cessation — is the empirical foundation for the CAUTION mode's design.

COLREGS Rule 8 (*Action to Avoid Collision*) requires that under elevated risk, navigational actions be simple, clear, and readily apparent. This principle — simplify decision support under elevated risk — is operationally analogous to scope restriction: under CAUTION, provide the decision support that is clear and reliable, not the full range of decision support whose reliability is conditional on conditions that no longer hold. Madsen & Kim (2024) [[notes]](../notes/A%20state-of-the-art%20review%20of%20AI%20decision%20transparency%20for%20autonomous%20shipping.md) note that maritime autonomous ship research already implements this principle at the display level — simplifying what operators see as risk increases — but confirm that no reviewed system restricts what the AI itself may recommend. Advisory scope restriction closes this gap.

---

## 5. The Structural Argument: What Scope Restriction Is

Advisory scope restriction is best understood as **information quality-conditioned output control**: the architecture conditions *which types of recommendations* the AI produces on the *reliability of those recommendation types* under current environmental conditions.

It is not:
- A reduction in AI capability (the AI model is unchanged)
- A transfer of decision authority (the human was always the decision-maker)
- A degraded mode (it is a different mode, designed for elevated conditions)

It is:
- A runtime filter on AI output types, conditioned on S = f(E)
- An application of VOI management (only provide information where VOI > 0)
- An implementation of envelope protection for AI recommendations
- A formalisation of the *cautious-go* decision pattern already present in domain practice (Gao, 2024 [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md); Rahim et al., 2024 [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md))

The formal structure — A_AI(CAUTION) ⊂ A_AI(SAFE) with the containment property A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ — captures this precisely: as environmental conditions worsen, the set of recommendation types the AI is permitted to make shrinks, but each remaining type is reliably supported by the AI's capabilities under those conditions.

---

## 6. Why This Has Not Been Done Before

The gap is not conceptual — the constituent ideas (VOI management, envelope protection, ALARP, bounded rationality) are all established. The gap is architectural: no prior system implements state-conditioned restriction of AI *recommendation types* as a formal runtime governance mechanism.

The closest approaches and why they fall short:

| Approach | What it does | Why it falls short |
|---|---|---|
| Flehmig et al. (2024) [[notes]](../notes/Implementing%20Artificial%20Intelligence%20in%20Safety-Critical%20Systems%20during%20Operation-%20Challenges%20and%20Extended%20Framework%20for%20a%20Quality%20Assurance%20Process.md) traffic-light | 3-level governance, triggers at Level 3 | Level 2 (CAUTION equivalent) changes monitoring intensity, not recommendation scope: "AI stays as safety function" at both Level 1 and Level 2 with identical unrestricted output |
| Baxi (2026) [[notes]](../notes/The%20Comprehension-Gated%20Agent%20Economy-%20A%20Robustness-First%20Architecture%20for%20AI%20Economic%20Agency.md) CGAE | K-tier nested permission sets with containment | Conditions on agent robustness, not environment; economic domain not physical safety; formal structure is parallel but conditioning variable is orthogonal |
| Shields / Könighofer et al. (2025) [[notes]](../notes/Shields%20for%20Safe%20Reinforcement%20Learning.md) | Per-state safe action sets | Filters individual actions, not recommendation *types*; continuous not discrete modes; confirmed by Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) who survey 46 formal methods papers and find all operate with binary safety boundaries |
| Shamsujjoha et al. (2025) [[notes]](../notes/Swiss%20Cheese%20Model%20for%20AI%20Safety-%20A%20Taxonomy%20and%20Reference%20Architecture%20for%20Multi-Layered%20Guardrails%20of%20Foundation%20Model%20Based%20Agents.md) Swiss Cheese | 13 guardrail action types across 14 targets | Static configuration, not conditioned on environmental safety state: "context-dependent rules" adjust per data context, not per classified environmental safety state |
| Autonomy level frameworks | Change decision authority allocation | Change who decides, not what the AI recommends |

The universality of binary governance across prior approaches is confirmed by multiple systematic reviews. Ramos et al. (2024) [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md) review 91 papers on collaborative intelligence for safety-critical industries and find that every safety governance mechanism is binary — AI operates or is overridden. Newcomb & Ochoa (2026) [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md) review 46 papers on formal methods for safety-critical ML and find that "every formal method for safety-critical ML — shielding, runtime verification, CBFs, reachability analysis, model checking, SMT-based verification — operates with binary safety boundaries." Perez-Cerrolaza et al. (2024) [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md) survey AI safety in industrial and transportation domains across automotive, avionics, railway, and industrial robotics contexts and confirm binary governance is universal: "AI outputs are either permitted (within safety envelope) or blocked (safe state activated)."

None of these apply state-conditioned advisory type restriction in a physical safety-critical environment. The proposed architecture is the first to do so — not because the idea is unprecedented in theory, but because no prior work has integrated it into a formal, runtime, environment-conditioned governance architecture.

---

## 7. One-Paragraph Summary (for use in Chapter 2 or 3)

> The CAUTION mode restricts AI advisory scope rather than blocking AI or reducing autonomy for three interlocking reasons. First, blocking AI violates ALARP: go/no-go directional guidance remains reliable under CAUTION conditions, so removing all AI assistance fails to meet the proportionality requirement of risk engineering — a less restrictive measure achieves adequate safety (Perez-Cerrolaza et al., 2024 [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md)). Moreover, binary blocking replicates the failure of real-world binary warnings, which Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) document are routinely overridden by small-scale fishers who adaptively self-restrict operational scope rather than cease fishing entirely. Second, reducing autonomy without scope restriction exposes the human to unreliable precise recommendations (departure times, trip durations) whose VOI under CAUTION conditions is negative — they mislead rather than inform — while anchoring bias and automation bias ensure these recommendations affect the decision regardless of stated confidence; Wen et al. (2025) find that human intervention was ineffective in 66.7–83.3% of real-world safety-critical incidents, confirming that authority reduction alone does not reliably protect against automation bias. Third, different recommendation types have different reliability envelopes: directional guidance (go/no-go, delay) degrades slowly under elevated conditions while precise operational recommendations (exact timing, routing) degrade rapidly. Scope restriction — A_AI(CAUTION) ⊂ A_AI(SAFE) — is information quality-conditioned output control: it confines the AI's advisory output to recommendation types whose reliability can be guaranteed under current environmental conditions. This formalises the *cautious-go* decision pattern empirically documented by Gao (2024) [[notes]](../notes/Mapping%20the%20decision-making%20factors%20of%20small-scale%20fishers-%20a%20case%20study%20of%20Penang.md) among Penang fishers and independently confirmed by Rahim et al. (2024) [[notes]](../notes/Survival%20Decisions%20and%20Adaptation%20Strategies%20of%20Small-scale%20Fishers%20in%20the%20Face%20of%20Extreme%20Weather%20Impacts%20in%20Coastal%20Areas.md) in coastal Indonesia, applies the VOI principle from decision theory, implements ecological rationality under bounded cognitive capacity, and achieves trust calibration by preventing the user from depending on recommendation types the AI cannot reliably support — operationalising the CHAI-T principle that "optimal levels of trust" require user expectations to be "aligned with the capabilities of system" (McGrath et al., 2025 [[notes]](../notes/Collaborative%20Human-AI%20Trust%20(CHAI-T)-%20A%20Process%20Framework%20for%20Active%20Management%20of%20Trust%20in%20Human-AI%20Collaboration.md)). The systematic absence of this approach from all prior safety-critical AI governance literature — confirmed across 91 collaborative intelligence papers (Ramos et al., 2024 [[notes]](../notes/Collaborative%20Intelligence%20for%20Safety-Critical%20Industries-%20A%20Literature%20Review.md)), 46 formal methods papers (Newcomb & Ochoa, 2026 [[notes]](../notes/Formal%20methods%20for%20safety-critical%20machine%20learning%3A%20a%20systematic%20literature%20review.md)), and cross-domain automotive and avionics surveys (Gyllenhammar et al., 2025 [[notes]](../notes/The%20Road%20to%20Safe%20Automated%20Driving%20Systems-%20A%20Review%20of%20Methods%20Providing%20Safety%20Evidence.md); Perez-Cerrolaza et al., 2024 [[notes]](../notes/Artificial%20Intelligence%20for%20Safety-Critical%20Systems%20in%20Industrial%20and%20Transportation%20Domains-%20A%20Survey.md)) — establishes that state-conditioned advisory scope restriction is a genuine architectural contribution, not a refinement of existing approaches.
