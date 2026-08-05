# Introduction — IPSCI 2026
## A Graduated Safety-State-Gated Architecture for AI Decision Support in Low-Resource Coastal Fisheries

---

> **Structure:** 5-step problem statement framework
> 1. Background — who, what, where
> 2. General problem statement — overall issue and consequences
> 3. Scholarly support — the literature already sees it
> 4. Specific problem statement — the precise gap
> 5. Concluding commentary — who is affected, why it matters, what if unsolved

---

## DRAFT

---

### Step 1 — Background

Every morning along Malaysia's Zone A coastline — the 0 to 5 nautical mile band where small-scale fishers are legally permitted to operate — fishers make a decision that is both economically and physically consequential: whether to go to sea. They assess the same set of conditions their fathers assessed: wind strength, wave height, rainfall, the marine warning status on the radio, the size and condition of their vessel, and the time of day. For 67.6% of them, the income from that decision is the household's only source of livelihood [9]. For most, the vessel is a traditional craft under 40 GRT, with no electronic navigation system, no institutional safety backup, and no access to cloud-based tools at sea [9].

This population already uses an informal three-part decision structure — go, cautious-go, don't go — that mirrors how professional maritime risk classification is designed to work [6]. Under marginal conditions, Penang fishers shorten trips and stay closer to shore rather than cancelling entirely. But this informal graduated response is under pressure. Yamin et al. [9], surveying 136 fishers in Terengganu, found that 95% reported stronger monsoonal winds and larger waves over the preceding decade, and 91% reported more intense weather and more erratic rainfall. Traditional weather prediction — the primary tool fishers use to classify conditions — is declining in reliability as climate patterns become less predictable. Fishers are turning to weather apps like Windy and Windfinder, which provide raw wind and wave data but no decision logic: the app shows the wind speed, but it does not tell the fisher what that wind speed means for whether to leave port.

---

### Step 2 — General Problem Statement

This is the gap that AI decision support is supposed to fill. An AI system for the departure decision could translate environmental readings into actionable advice — go, delay, suggested departure time, recommended trip duration — calibrated to the fisher's vessel class, the current conditions, and the marine warning status. Versions of such systems are beginning to appear across fisheries and maritime domains.

The problem is that existing AI governance architectures are not designed to handle intermediate-risk conditions. Every reviewed architecture treats AI participation as binary: either the AI generates its full recommendation set or it is blocked entirely [1]. When conditions are clearly safe, the AI advises fully. When conditions are clearly dangerous, the AI shuts down. When conditions are somewhere in between — wind elevated but below the warning threshold, advisory in effect but no formal danger signal — the system has no third option. It continues generating departure-time and trip-duration recommendations built on environmental data that is no longer reliable enough to support them, or it goes silent and offers nothing.

Both outcomes are wrong. A fisher who receives confident AI departure-time advice under marginal conditions may treat that recommendation as an accurate assessment of a situation the AI is no longer equipped to evaluate. A fisher who receives nothing loses the one source of structured decision support that could help them navigate a condition that traditional knowledge alone can no longer reliably classify.

---

### Step 3 — Scholarly Support

The absence of an intermediate governance mode is consistent across the ML architecture literature, the broader guardrail literature, cross-domain safety-critical AI surveys, the nearest structural precedent, the fisheries application domain, and the maritime accident record.

**Architecture and governance literature.** Indykov et al. [1], reviewing 206 papers and cataloguing 16 architectural tactics for machine-learning-enabled systems, found no tactic demonstrating a formal impact on safety through advisory scope restriction. Shamsujjoha et al. [10], deriving a taxonomy from 32 studies on runtime guardrails for foundation model-based agents, identify 13 distinct governance actions — block, filter, flag, modify, validate, retry, fall back, human intervention, defer, isolate, redundancy, evaluate, parallel calls. None of the 13 actions condition advisory scope on a classified environmental safety state. Perez-Cerrolaza et al. [11], surveying AI safety mechanisms across automotive, avionics, railway, and industrial domains across 294 references, document safety bags, safety monitors, and safety envelopes as the primary runtime governance mechanisms. All operate as binary constraints: the AI either functions within a defined safety boundary or is blocked. No reviewed mechanism varies the AI's admissible output categories based on classified environmental conditions.

**Theoretical framework.** Dalrymple et al. [7] propose Guaranteed Safe AI as a unifying framework for verifiably safe AI systems. Safety verification in that framework is binary: a system either satisfies its specification or fails it. There is no intermediate mode where the AI participates within a formally restricted advisory scope.

**Closest structural precedent.** Flehmig et al. [2] proposed a three-level traffic-light degradation index for AI in safety-critical industrial systems — green, orange, and red — that maps structurally onto the intuition of safe, cautious, and unsafe states. At Level 3 (red), the AI is blocked. At Level 2 (orange), the AI remains active and supervisory activity is heightened. But the AI's advisory scope is identical at Level 1 and Level 2. The three-level classification governs what the human supervisor does; it does not change what the AI may say. The intermediate level's governance potential for AI scope restriction remains unrealised.

**Fisheries domain.** Haque and Al Jufaili [3] reviewed AI across four fisheries application domains and found no system implementing formal participation governance or advisory scope restriction conditioned on environmental safety state. Yamin et al. [9] confirm through primary survey data from 136 Malaysian fishers that the current decision pattern is binary — "if it's suddenly windy or the weather changes, I can't go fishing" — with no documented intermediate response. Flexibility was the weakest of the five adaptive capacity domains assessed, with only 58% of fishers willing to consider alternative responses under stress.

**Maritime accident record.** The domain-level safety stakes are empirically grounded. Dominguez-Péry et al. [12], analysing 504 IMO maritime accident investigation reports (2011–2021), found that external environmental factors — wind, weather, visibility — constitute the largest single risk cluster (26.7% of text segments). Small vessels (≤2,000 GT) recorded the highest mean fatality rank (3.67) despite representing only 58 of 504 accidents, a difference statistically significant at p = 0.01. Atacan and Düzbastılar [13], in a simulator study with 30 small-scale fishing vessel captains, found that the combination of night navigation and heavy weather produced the highest accident consequence scores across all tested conditions (mean 37.03) — substantially higher than either factor alone. Rahim et al. [14] document that during extreme weather events, fisher income drops from IDR 656,000 to 213,000 per trip and trip frequency halves from 5–6 to 2–3 per week. The only external override available is a binary government advisory with no graduated response — a binary-only architecture at the institutional level that mirrors the binary-only architecture in the AI governance literature.

---

### Step 4 — Specific Problem Statement

No architecture identified in this review formally defines an intermediate governance mode in which AI participation is permitted but advisory scope is restricted to the recommendation types that the current environmental safety state can reliably support. Stated precisely: no existing architecture specifies an AI-admissible recommendation space A_AI(S) that varies by classified safety state S — a construct that would allow a system under intermediate-risk conditions to continue advising on go/no-go and delay decisions while formally withholding departure-time and trip-duration recommendations that depend on environmental data now outside their reliable operating range.

This study addresses that gap. The proposed architecture introduces a two-level governance pair (G(S), A_AI(S)) conditioned on a classified environmental safety state S = f(E), where E is a six-parameter environmental state vector capturing wind speed, rainfall intensity, marine warning level, ocean state, vessel category, and time of day. The result is three formally specified governance modes: SAFE (full advisory scope), CAUTION (go/no-go and delay only), and UNSAFE (AI silent). The intermediate CAUTION mode — AI active, scope formally restricted — is the contribution that no reviewed architecture implements.

---

### Step 5 — Concluding Commentary

The population this gap affects is not abstract. Malaysian small-scale fishers operate without institutional safety infrastructure, without access to professional maritime safety services, and — increasingly — without the traditional knowledge that generations of coastal communities used to assess conditions their instruments cannot measure [9]. For 67.6% of them, a wrong departure decision is not a financial setback; it is an existential one [9].

The governance architecture matters beyond this domain. Wen et al. [8], analysing 60 real-world accident reports across process control and autonomous vehicle domains, found that human intervention was ineffective in 83.3% of process control incidents where the AI was acting autonomously and the human was expected to override. A binary AI governance model — one that stays fully active until it shuts down — creates exactly this condition: the human receives confident-looking recommendations right up to the boundary of the AI's reliable operating range, with no signal that the advisory scope has become questionable. A graduated architecture that formally restricts what the AI says before conditions reach that boundary gives the human something no binary system can provide: a structured intermediate state where the system's reduced scope communicates, in the architecture itself, that conditions are no longer suitable for full AI advisory confidence.

If this problem remains unsolved, the gap does not close on its own. Traditional knowledge erosion continues. Weather apps fill the vacuum with raw data and no governance. AI adoption in fisheries will grow regardless of whether the governance architecture is adequate for intermediate-risk conditions. The question is whether that architecture is designed for the full range of conditions fishers actually face — or only for the two ends.

---

## REFERENCES

[1] V. Indykov, D. Strüber, and R. Wohlrab, "Architectural tactics to achieve quality attributes of machine-learning-enabled systems: A systematic literature review," *Journal of Systems and Software*, vol. 223, p. 112373, 2025.

[2] N. Flehmig, M. A. Lundteigen, and S. Yin, "Implementing artificial intelligence in safety-critical systems during operation: Challenges and extended framework for a quality assurance process," in *Proc. IEEE IECON 2024*, 2024, DOI: 10.1109/IECON55916.2024.10906021.

[3] M. S. Haque and S. Al Jufaili, "Applications of artificial intelligence in fisheries: From data to decisions," *Reviews in Aquaculture*, 2026.

[6] P. K. Gao, "Mapping the decision-making factors of small-scale fishers: A case study of Penang," M.Sc. thesis, Univ. Pisa / WorldFish, 2024. [Online]. Available: https://hdl.handle.net/10568/152289

[7] D. Dalrymple et al., "Towards guaranteed safe AI: A framework for ensuring robust and reliable AI systems," *arXiv preprint arXiv:2405.06624*, 2024.

[8] H. Wen, Z. Sajid, and R. Arunthavanathan, "Risk perception in complex systems: A comparative analysis of process control and autonomous vehicle failures," *AI*, vol. 6, no. 8, p. 164, 2025, DOI: 10.3390/ai6080164.

[9] L. Yamin, T.-C. Kuo, and N. Aziz, "Interplay of traditional knowledge and adaptive capacity in climate change adaptation of small-scale fishers in central Terengganu, Malaysia," *Frontiers in Marine Science*, vol. 12, p. 1492131, 2025, DOI: 10.3389/fmars.2025.1492131.

[10] Md. Shamsujjoha, Q. Lu, D. Zhao, and L. Zhu, "Swiss cheese model for AI safety: A taxonomy and reference architecture for multi-layered guardrails of foundation model based agents," in *Proc. IEEE 22nd International Conference on Software Architecture (ICSA)*, 2025, pp. 37–48, DOI: 10.1109/ICSA65012.2025.00014.

[11] J. Perez-Cerrolaza et al., "Artificial intelligence for safety-critical systems in industrial and transportation domains: A survey," *ACM Computing Surveys*, vol. 56, no. 7, Article 176, 2024, DOI: 10.1145/3626314.

[12] C. Dominguez-Péry, R. Tassabehji, F. Corset, and Z. Chreim, "A holistic view of maritime navigation accidents and risk indicators: examining IMO reports from 2011 to 2021," *Journal of Shipping and Trade*, vol. 8, p. 11, 2023, DOI: 10.1186/s41072-023-00135-y.

[13] C. Atacan and F. O. Düzbastılar, "Determination of risk perception in small-scale fishing and navigation," *Ege Journal of Fisheries and Aquatic Sciences*, vol. 40, no. 1, pp. 1–14, 2023, DOI: 10.12714/egejfas.40.1.01.

[14] Abd. Rahim et al., "Survival decisions and adaptation strategies of small-scale fishers in the face of extreme weather impacts in coastal areas," *Journal of Marine and Island Cultures*, vol. 13, no. 3, 2024, DOI: 10.21463/jmic.2024.13.3.05.
