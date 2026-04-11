## Literature Review Extraction — GAP-FOCUSED
### OWASP (2025) — Top 10 for Agentic Applications 2026

---

### 1. Paper Identity

- **Title:** OWASP Top 10 for Agentic Applications 2026
- **Authors:** OWASP GenAI Security Project — Agentic Security Initiative. Leads: John Sotiropoulos (ASI Co-lead, Agentic Top 10 Chair), Keren Katz (Agentic Top 10 Lead, ASI Core Team), Ron F. Del Rosario (ASI Co-lead)
- **Year:** Version 2026, published December 2025
- **Venue:** OWASP (Open Worldwide Application Security Project) — genai.owasp.org
- **Type:** Industry standard / consensus security framework
- **License:** Creative Commons CC BY-SA 4.0
- **Citation Quality:** **Authoritative industry standard.** Produced by dozens of security experts from industry, academia, and government via open collaboration, peer review, and evidence from research, exploits, incidents, and real-world deployments. Maps to OWASP LLM Top 10 (2025), Agentic AI Threats & Mitigations taxonomy, OWASP AIVSS scoring framework, and CycloneDX standard.

---

### 2. Core Contribution

- **Problem:** Agentic AI systems (agents that plan, decide, and act across multiple steps autonomously) pose novel security risks that go beyond single-model LLM vulnerabilities.
- **Proposed solution:** A taxonomy of the 10 highest-impact threats to agentic AI systems, with descriptions, vulnerability examples, real-world attack scenarios, and actionable mitigations for each.
- **The 10 threats:**
  1. **ASI01: Agent Goal Hijack** — manipulating agent objectives via prompt injection, deceptive tool outputs, or poisoned data
  2. **ASI02: Tool Misuse and Exploitation** — agents misusing legitimate tools via over-privilege, chaining, or unvalidated input forwarding
  3. **ASI03: Identity and Privilege Abuse** — exploiting delegation chains, credential inheritance, and cross-agent trust
  4. **ASI04: Agentic Supply Chain Vulnerabilities** — compromised MCP servers, agent cards, tool descriptors, poisoned dependencies
  5. **ASI05: Unexpected Code Execution (RCE)** — agents executing arbitrary code from untrusted model output
  6. **ASI06: Memory & Context Poisoning** — persistent corruption of stored context or long-term memory
  7. **ASI07: Insecure Inter-Agent Communication** — exploiting multi-agent messaging, delegation, and routing
  8. **ASI08: Cascading Failures** — single faults propagating across agents, tools, and workflows
  9. **ASI09: Human-Agent Trust Exploitation** — manipulating human trust via anthropomorphism, fake explainability, and automation bias
  10. **ASI10: Rogue Agents** — agents deviating from intended function, acting deceptively or parasitically

---

### 3. Governance Mechanism Analysis

| Property | Assessment |
|---|---|
| **Governance type** | **Binary across all 10 entries.** Every mitigation strategy operates as permit/block, allow/deny, approve/reject, or execute/quarantine. No mitigation proposes graduated or intermediate governance modes. |
| **Trigger** | Agent action, tool invocation, identity/credential, message content, or behavioral deviation — never classified environmental state |
| **Intermediate mode?** | **No.** Despite 10 vulnerability categories covering hundreds of attack surfaces, no mitigation introduces a "reduced scope" or "restricted advisory" mode. Actions are either permitted or blocked. |
| **Environmental conditioning?** | **No.** No mitigation conditions governance on external environmental state (weather, ocean conditions, time of day, etc.). Governance is triggered by agent behavior, identity, or policy rules — not by the environment the agent operates in. |
| **Advisory scope restriction?** | **No.** Mitigations restrict whether an agent *may perform an action*, not what *types of recommendations* the agent may generate. No equivalent to A_AI(S) restricting advisory categories. |
| **Runtime adaptation?** | Partial — ASI09 mitigation #5 "Adaptive Trust Calibration" adjusts human oversight level based on contextual risk scoring. This is the closest to graduated governance in the document (see Section 5 below). |

**Key mitigations surveyed (all binary):**

- **ASI01 mitigation #4:** "Pause or block execution on any unexpected goal shift" — binary pause/block
- **ASI02 mitigation #1:** "Least Agency and Least Privilege for Tools" — per-tool allow/deny profiles
- **ASI02 mitigation #4:** "Policy Enforcement Middleware ('Intent Gate')" — PEP/PDP validates or rejects, binary enforcement
- **ASI03 mitigation #3:** "Mandate Per-Action Authorization" — centralized policy engine permits or denies each privileged step
- **ASI08 mitigation #4:** "Independent policy enforcement" — external policy engine blocks or permits
- **ASI10 mitigation #4:** "Containment & Response" — kill-switches, credential revocation, quarantine — all binary emergency stops

---

### 4. Governance Level Analysis

| Level | Question | Implemented? | How? |
|---|---|---|---|
| **Level 1 — Participation governance** | Does AI act at all? (G(S)) | **Yes (binary)** | Per-action allow/deny across all 10 entries. Policy enforcement middleware (ASI02), per-action authorization (ASI03), kill-switches (ASI10). |
| **Level 2 — Advisory scope governance** | What may AI recommend? (A_AI(S)) | **No** | No mitigation restricts what types of recommendations an agent may generate. All governance operates on actions/tool calls, not advisory content scope. |
| **Levels 1 + 2 unified, state-conditioned** | Both levels governed by classified environmental state? | **No** | No mention of environmental state classification. Governance is conditioned on agent identity, action type, policy rules, and behavioral baselines — not on the external environment in which the agent operates. |

---

### 5. Gap Evidence for Novelty Argument

**Key finding:** The OWASP Top 10 for Agentic Applications represents the global security community's consensus threat model and mitigation framework for agentic AI as of December 2025. Produced by dozens of experts from industry, academia, and government. Despite comprehensive coverage of 10 threat categories, hundreds of mitigations, and cross-mapping to 4 other OWASP frameworks, **every single governance mechanism is binary**.

**The near-miss — ASI09 "Adaptive Trust Calibration" (p.35, mitigation #5):**

> "Continuously adjust the level of agent autonomy and required human oversight based on contextual risk scoring. Implement confidence weighted cues (e.g., 'low-certainty' or 'unverified source') that visually prompt users to question high-impact actions, reducing automation bias and blind approval."

This is the closest any OWASP mitigation comes to graduated governance. The rebuttal is precise:

1. **Continuous adjustment ≠ discrete governance modes.** The trust calibration adjusts a continuous risk score, not a classified environmental state with categorically different governance properties (SAFE/CAUTION/UNSAFE).
2. **Human oversight, not AI scope restriction.** The calibration adjusts how much *human oversight* is required. It does not restrict what *types of recommendations* the AI may generate. This is a human-side control, not AI-side governance.
3. **No environmental state classification.** The "contextual risk scoring" is based on agent behavior and output confidence — not on external environmental conditions (wind, waves, time of day, marine warnings).
4. **No containment property.** There is no A_AI(SAFE) ⊃ A_AI(CAUTION) ⊃ A_AI(UNSAFE) = ∅ structure. The recommendation scope doesn't narrow as risk increases — only the human approval requirement changes.

**Why this source is powerful for the novelty argument:**

1. **Consensus authority.** Not one company's opinion but the global OWASP community's agreed standard.
2. **Comprehensiveness.** 10 threat categories, hundreds of attack scenarios and mitigations — if graduated governance were standard practice, it would appear here.
3. **Recency.** Published December 2025, covering threats up to and including MCP server attacks, Agent2Agent protocol abuse, and multi-agent cascading failures.
4. **Cross-framework mapping.** Appendix A maps all 10 entries to OWASP LLM Top 10, Agentic AI Threats & Mitigations (T1–T17), and AIVSS Core Risks — none of which include graduated governance.
5. **Architecture diagram (p.8).** The canonical agentic architecture shows "Policy & Governance" as a single binary gateway between inputs and agent processing, with a human-in-the-loop connection. No state classifier, no graduated modes.

**Critical distinction from proposed architecture:** OWASP's governance paradigm asks "should this action be permitted?" The proposed architecture asks "given the current environmental state, what *type* of governance applies and what *scope* of advisory is the AI allowed to provide?" OWASP assumes governance type is fixed (always binary); the proposed architecture dynamically selects governance type based on classified environmental state.

**Use in justification:** Cite alongside the Microsoft Agent Governance Toolkit (which explicitly implements OWASP's Top 10) to show that both the *standard* and its leading *implementation* are binary. Together they form the strongest possible evidence that binary governance is the industry consensus — not by accident or oversight, but by the global security community's deliberate and comprehensive framework design.

---

### 6. Theme Relevance

| Theme | Match? | Notes |
|---|---|---|
| T1: Hybrid AI | ⚠️ Partial | Architecture diagram shows policy engine + LLM agent, but not hybrid in the proposed architecture's sense |
| T2: Safety-critical AI | ✅ Yes | Core focus — security threats and mitigations for autonomous AI agents |
| T3: AI governance | ✅ Yes | Definitive industry governance framework for agentic AI — all binary |
| T4: Low-resource environments | ❌ No | Enterprise/cloud deployment context throughout |
| T5: Decision architecture formalisation | ⚠️ Partial | AIVSS scoring framework provides structured risk assessment, but no mathematical formalisation |
| T6: Human role | ✅ Yes | ASI09 (Human-Agent Trust Exploitation) directly addresses human factors, automation bias, anthropomorphism |
| T7: Socio-technical evaluation | ⚠️ Partial | References real-world exploits and incidents (Appendix D), but no systematic socio-technical evaluation framework |
| T8: Coastal fisheries / maritime | ❌ No | General-purpose agentic AI security |

---

### 7. Overall Relevance Score

**⭐⭐⭐⭐⭐ Very High** (Verified from full text — PDF uploaded and read in its entirety)

The single most authoritative evidence that binary governance is the global industry consensus for agentic AI security. While the Microsoft Agent Governance Toolkit shows the *implementation* is binary, OWASP shows the *standard itself* is binary. Together they prove that binary governance is not just current practice but the deliberate, expert-reviewed, consensus design choice of the global AI security community — making the proposed architecture's graduated, environment-state-conditioned governance a clear and well-evidenced contribution.
