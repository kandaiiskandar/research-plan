## Literature Review Extraction — GAP-FOCUSED
### Feng, McDonald & Zhang (2025) — Levels of Autonomy for AI Agents

---

### 1. Paper Identity

- **Title:** Levels of Autonomy for AI Agents
- **Authors:** K. J. Kevin Feng, David W. McDonald, Amy X. Zhang
- **Affiliation:** University of Washington
- **Year:** 2025 (arXiv v2: 28 Jul 2025)
- **Venue:** Knight First Amendment Institute at Columbia University; arXiv:2506.12469v2
- **Type:** Working paper / essay (described as "PDF accompaniment to the web publication by the Knight 1st Amendment Institute")
- **URL:** https://arxiv.org/abs/2506.12469
- **Citation Quality:** Prominent institutional publication (Knight Institute at Columbia), University of Washington HCI researchers. Acknowledged by participants of Knight Institute's *Artificial Intelligence and Democratic Freedoms* workshop and MINT Lab's Sociotechnical AI Safety Retreat. Not yet peer-reviewed journal publication.

---

### 2. Core Contribution

- **Problem:** AI agent autonomy is a double-edged sword — transformative but risky. Developers need a framework for calibrating the appropriate level of autonomy. The paper argues: "rather than treating autonomy as an inevitable consequence of increasing agent capability, autonomy can instead be a deliberate design decision made by agent developers" (p.2).
- **Key conceptual move — agency ≠ autonomy (Section 2.2):** Agency is "the capacity to formulate an intention for an action and carry out that action." Autonomy is "the extent to which an AI agent is designed to operate without user involvement." These are distinct levers: an agent with high agency (many tools) can still have low autonomy (must ask user before acting), and vice versa.
- **Proposed solution:** Five levels of escalating agent autonomy, characterised by the user's role (Figure 1, Table 1):
  1. **Level 1 — User as Operator:** "User directs and makes decisions, agent acts." User is in charge at all times; agent provides contextual assistance on-demand (copilot metaphor). User owns all long-term planning.
  2. **Level 2 — User as Collaborator:** "User and agent collaboratively plan, delegate, and execute." Back-and-forth communication is most frequent here. User can take control of the agent's work at any time.
  3. **Level 3 — User as Consultant:** "Agent takes lead but consults user for expertise/preferences." Agent drives task planning and execution; user provides directional guidance, feedback, and higher-level preferences. Unlike L2, user cannot directly take control — only provides input via indirect means.
  4. **Level 4 — User as Approver:** "Agent engages user only in risky or pre-specified scenarios." User is passive except when the agent encounters blockers (failure states, credentials needed, consequential actions). Pre-selected a report format without consulting user (unlike L3 which would ask).
  5. **Level 5 — User as Observer:** "Agent operates with full autonomy under user monitoring." No means for user involvement. Only control mechanism: "an emergency off-switch that shuts off all agent activity" (p.8). User monitors via activity logs.
- **Autonomy certificates (Section 4):** Digital documents issued by a third-party governing body (government agencies, nonprofits like METR, or companies) that prescribe "the maximum level of autonomy at which an agent can operate given 1) some set of technical specifications... and 2) its operational environment" (p.9). Analogous to safety cases [5, 15, 21]. Certificate renewal required when technical specifications or operational environment change.
- **Assisted evaluations (Section 5):** A method for evaluating autonomy (not capability) by measuring "the minimum level of user involvement needed for the agent to exceed a certain accuracy or pass rate threshold" T. Start at L5 (no user), iteratively increase involvement until task completion, then classify.

---

### 3. Governance Mechanism Analysis

| Property | Assessment |
|---|---|
| **Governance type** | **Graduated** — five discrete levels with different governance properties at each level |
| **Trigger** | **Design-time decision** — "given a fixed set of capabilities and a fixed operational environment, developers can make intentional choices about the level of autonomy" (p.4). The level is a deliberate design choice, not conditioned on runtime state. |
| **Intermediate mode?** | **Yes** — Levels 2, 3, 4 are intermediate between full human control (L1) and full agent autonomy (L5), each with qualitatively different user roles |
| **Environmental conditioning?** | **No** — the paper explicitly models the environment as a *fixed constant*, not a variable: "We show how agent developers may vary the autonomy of the agent even when these factors for model capability and agency are held constant" (p.4). The autonomy certificate is issued for a specific operational environment; if the environment changes, the certificate must be *renewed*, not dynamically adjusted. |
| **Advisory scope restriction?** | **No** — the levels define the *human role* (operator → observer), not the *scope of what the agent may recommend*. At any level, the agent's recommendation content is unrestricted. An L3 Consultant agent can recommend anything — the user just provides directional guidance. |
| **Runtime adaptation?** | **No** — the autonomy certificate prescribes a *maximum* level. "Changes to either [technical specifications or operational environment] can alter the agent's interactive behaviors and thus invalidate the certificate" (p.10). Level changes require certificate renewal through a governing body, not runtime switching. |

---

### 4. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI act at all? (G(S)) | **Partial** | At L1 (Operator), the agent only provides information — effectively restricted participation. But this is a fixed design choice, not a runtime state-conditioned switch. |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No** | The framework does not restrict what the agent may recommend — only how much autonomy it has in executing actions. An L3 (Consultant) agent can recommend anything; the user just provides input when asked. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | Neither level is conditioned on environmental state. Both are fixed at design/deployment time. |

---

### 5. Gap Evidence for Novelty Argument

**Key finding:** This paper is the closest existing work to graduated AI governance and the strongest "near-miss" comparator. It defines five discrete levels with different governance properties — structurally parallel to the proposed three-state architecture. An examiner might argue: "Feng et al. already implemented graduated governance."

**The rebuttal has three precise points:**

1. **Design-time vs. runtime.** Feng et al.'s levels are fixed at deployment. The paper explicitly models the environment as a constant: "given a fixed set of capabilities and a fixed operational environment, developers can make intentional choices about the level of autonomy" (p.4). The proposed architecture's governance modes change dynamically at runtime based on S = f(E). The same agent, in the same deployment, shifts between SAFE, CAUTION, and UNSAFE as environmental conditions change. Feng et al.'s agent stays at its certificated level regardless of what happens in the environment. If the environment changes, it requires *certificate renewal through a governing body* (p.10), not automatic runtime switching.

2. **Human role vs. advisory scope.** Feng et al.'s levels define *how much the human is involved* (operator → observer). The proposed architecture defines *what the AI may recommend* (full scope → restricted types → nothing). These are orthogonal governance dimensions. An L3 (Consultant) agent in Feng et al. can recommend anything — it merely "consults user for expertise/preferences" (Figure 1). In the proposed architecture, a CAUTION-mode agent can only recommend conservative, near-shore activities regardless of the human's role.

3. **No environmental trigger.** The framework treats the operational environment as a fixed deployment context ("a computer running a popular operating system," p.4), not a variable that triggers governance changes. The proposed architecture makes the operational environment — specifically, the environmental state vector E = {w, r, m, o, v, t} — the *sole trigger* for governance mode. This is the fundamental architectural difference.

4. **Agency-autonomy distinction supports the gap.** Feng et al.'s important insight that agency (what tools the agent can use) and autonomy (how much user involvement is required) are "two distinct levers for agent governance" (p.3) actually highlights the absence of a *third* lever that the proposed architecture introduces: **advisory scope** (what types of recommendations the agent may generate). The proposed A_AI(S) restricts recommendation categories — neither agency nor autonomy in Feng et al.'s terminology.

**Use in justification:** Cite as the strongest near-miss comparator for graduated governance. Its five levels demonstrate that the AI governance community recognises the value of graduated approaches — but applies them only to the human-role dimension at design time, not to the advisory-scope dimension at runtime. The proposed architecture fills the specific gap Feng et al. leave open: runtime, environment-state-conditioned, advisory-scope governance. The paper's own agency/autonomy distinction inadvertently reveals the missing third governance dimension.

---

### 6. Theme Relevance

| Theme | Match? | Notes |
|---|---|---|
| T1: Hybrid AI | ❌ No | Framework/essay paper, not a technical architecture |
| T2: Safety-critical AI | ⚠️ Partial | Autonomy certificates reference safety cases [5, 15, 21] and Anthropic's RSP [2] |
| T3: AI governance | ✅ Yes | Core focus — agent autonomy governance framework with certificates |
| T4: Low-resource environments | ❌ No | General-purpose framework; running example is a computer-using frontier model |
| T5: Decision architecture formalisation | ⚠️ Partial | Conceptual framework with evaluation methodology, no mathematical formalisation |
| T6: Human role | ✅ Yes | Central contribution — five human roles defining autonomy levels (operator → observer) |
| T7: Socio-technical evaluation | ⚠️ Partial | Proposes assisted evaluations; references Collaborative Gym [36] and user studies |
| T8: Coastal fisheries / maritime | ❌ No | General AI agent domain |

---

### 7. Overall Relevance Score

**⭐⭐⭐⭐⭐ Very High** (Verified from full text — PDF uploaded and read in its entirety, 15 pages + references)

The single most important comparator for the novelty argument regarding graduated governance. Feng et al. prove the AI governance community recognises the value of graduated approaches (5 discrete levels) but applies them only to the human-role dimension at design time, not to the advisory-scope dimension at runtime. The paper's own agency/autonomy distinction inadvertently reveals the missing third governance dimension (advisory scope) that the proposed architecture introduces. The precise differences — design-time vs. runtime, human-role vs. advisory-scope, environment as constant vs. environment as trigger — define the exact contribution of the proposed architecture.
