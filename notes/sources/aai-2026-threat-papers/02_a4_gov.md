# A⁴-Gov: A Governance Architecture for AI Service Systems

> Source PDF: `mathrmA4_-Gov_A_Governance_Architecture_for_AI_Service_Systems(1).pdf`

> Extraction note: Text extracted from the uploaded PDF using Poppler `pdftotext -layout`. Page boundaries are preserved below. Formatting, equations, tables, and multi-column reading order may not perfectly match the original PDF. Use the original PDF for authoritative visual/layout verification.


---

## PDF Page 1

```text
2026 IEEE/ACIS 24th International Conference on Software Engineering Research, Management and Applications (SERA) | 979-8-3195-0657-3/26/$31.00 ©2026 IEEE | DOI: 10.1109/SERA69989.2026.11618631




                                                                                                                                                                                                     A⁴-Gov: A Governance Architecture for AI Service
                                                                                                                                                                                                                       Systems

                                                                                                                                                                                                                                Min Seon Ahn                                                       Yong Ik Yoon(*Corresponding Author)

                                                                                                                                                                                                               Graduate School, Department of IT Engineering,                                  Graduate School, Department of IT Engineering,
                                                                                                                                                                                                                    Sookmyung Women's University                                                    Sookmyung Women's University
                                                                                                                                                                                                                                 Seoul, South Korea                                                              Seoul, South Korea
                                                                                                                                                                                                                        msahn@sookmyung.ac.kr                                                           yiyoon@sookmyung.ac.kr


                                                                                                                                                                                                                                                                                      field by articulating normative principles, legal duties,
                                                                                                                                                                                                                                                                                      organizational controls, and audit mechanisms [1]-[8]. Yet
                                                                                                                                                                                                        Abstract—Public AI services often undergo ex ante review                      much of this literature still focuses on what should be governed
                                                                                                                                                                                                    before deployment, but the resulting risk decision must still be
                                                                                                                                                                                                                                                                                      rather than on how policy state, review conditions, and
                                                                                                                                                                                                    carried into operation through concrete controls, review triggers,
                                                                                                                                                                                                                                                                                      accountability records should function inside the decision loop
                                                                                                                                                                                                    and evidence records. This paper defines A⁴-Gov as a runtime
                                                                                                                                                                                                    governance architecture for AI service systems that performs that
                                                                                                                                                                                                                                                                                      of an AI-enabled service system.
                                                                                                                                                                                                    operational role. The architecture assumes that review or risk                        The software-engineering literature on self-adaptive
                                                                                                                                                                                                    grading has already determined the control level required for the                 systems helps frame that gap more precisely. Feedback loops,
                                                                                                                                                                                                    service or case. A ⁴ -Gov then carries that decision into four                    architecture-based self-adaptation, and autonomic computing
                                                                                                                                                                                                    runtime functions: Awareness, which derives the active baseline
                                                                                                                                                                                                                                                                                      have shown how systems can observe state, analyze deviation,
                                                                                                                                                                                                    from policy and service context; Assessment, which identifies
                                                                                                                                                                                                    governance-relevant deviation from that baseline; Adaptability,
                                                                                                                                                                                                                                                                                      select responses, and execute change under explicit control
                                                                                                                                                                                                    which selects bounded intervention and triggers human review                      structures [13], [14], [16]. However, those architectures are
                                                                                                                                                                                                    when required; and Accountability, which preserves policy state,                  typically optimized for performance, resilience, or quality-of-
                                                                                                                                                                                                    intervention rationale, and audit-ready evidence. The paper                       service objectives. They do not directly explain how policy
                                                                                                                                                                                                    positions the architecture against AI governance frameworks and                   baselines, rights-sensitive thresholds, human escalation, and
                                                                                                                                                                                                    self-adaptive software architectures, then examines it through a                  accountability traces should be modeled as first-class
                                                                                                                                                                                                    public-service walk-through and a failure-oriented analytical                     governance objects in public-service AI.
                                                                                                                                                                                                    check. The contribution is architectural: it specifies how review
                                                                                                                                                                                                    decisions, bounded intervention, and accountability logging                           A⁴-Gov is introduced here as the runtime governance
                                                                                                                                                                                                    remain connected during operation.                                                layer that follows review and risk-grading decisions. Once a
                                                                                                                                                                                                        Keywords - AI governance, AI service systems, public-service AI,              service or case has been assigned a control level, the
                                                                                                                                                                                                    software architecture, self-adaptive systems, auditability, human                 architecture carries that decision into operation through
                                                                                                                                                                                                    escalation, accountability                                                        baseline formation, deviation interpretation, bounded
                                                                                                                                                                                                                                                                                      intervention, human escalation, and accountability logging. A
                                                                                                                                                                                                                                                                                      ⁴-Gov is therefore not a separate ethics framework; it is the
                                                                                                                                                                                                       I.         Introduction                                                        operational mechanism that preserves control requirements
                                                                                                                                                                                                        Artificial intelligence is increasingly used to structure                     after deployment begins.
                                                                                                                                                                                                    operational decisions in service environments. Public-service                         This paper makes three concrete contributions. It defines A
                                                                                                                                                                                                    settings provide a useful example because questions of safety,                    ⁴ -Gov as a runtime governance architecture with explicit
                                                                                                                                                                                                    fairness, rights, and administrative responsibility become                        control objects, state variables, escalation conditions, and audit
                                                                                                                                                                                                    visible quickly. As these systems become more deeply                              artifacts. It locates the architecture after review and risk-
                                                                                                                                                                                                    embedded in service workflows, their quality cannot be                            grading decisions by showing how policy state is carried into
                                                                                                                                                                                                    assessed only in terms of predictive accuracy or throughput.                      baseline formation, bounded response, and evidence logging
                                                                                                                                                                                                    Their behavior must also remain governable, reviewable, and                       during operation. It then examines the architecture through a
                                                                                                                                                                                                    accountable during operation.                                                     public-service walk-through and a failure-oriented check that
                                                                                                                                                                                                       This challenge has intensified recent work on AI                               test explicit policy state, governance-relevant deviation,
                                                                                                                                                                                                    governance across ethics, regulation, public administration,                      bounded intervention, and review-ready evidence.
                                                                                                                                                                                                    and standards. Prior studies have significantly advanced the




                                                                                                                                                                                                    979-8-3195-0657-3/26/$31.00 ©2026 IEEE                                        641
                                                                                                                                                                                                    SERAAuthorized
                                                                                                                                                                                                          2026, Maylicensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:22:13 UTC from IEEE Xplore. Restrictions apply.
                                                                                                                                                                                                                      27-29, 2026, Towson, USA
```

---

## PDF Page 2

```text
    The remainder of the paper is organized as follows. Section                   execution. Their dominant level of analysis remains the
2 reviews related work. Section 3 clarifies the conceptual                        institution, the lifecycle process, or the compliance regime
distinction between A⁴-Gov and existing governance                                rather than the operating control loop of an AI service.
frameworks. Section 4 defines the architecture and its design
constraints. Section 5 reads the stages through a public-service
example and failure-oriented check. Section 6 discusses                               III.       Accountability,        Auditability,      and      Adaptive
implications and limitations. Section 7 concludes.                                               Governance
                                                                                      The third stream addresses mechanisms such as
                                                                                  documentation, explainability, auditing, and adaptive
   II.        RELATED WORK                                                        governance. Mokander and Floridi show that operationalizing
    Four research streams frame the proposed architecture:                        AI governance through ethics-based auditing requires concrete
principle-centered AI governance, institutional and standards-                    integration with organizational evidence flows rather than
based governance frameworks, operational accountability                           ethical declarations alone [8]. Taeihagh argues that rapidly
mechanisms, and self-adaptive software architectures.                             evolving AI capability requires adaptive governance [9]. Reuel
                                                                                  and Undheim make a similar claim in the narrower context of
                                                                                  generative AI, where governance frameworks must support
         A. Principle-Centered AI Governance                                      continuous revision under changing capability profiles [10].
    The first stream focuses on the normative foundations of AI                   Koenig and Wenzelburger add a public-sector perspective,
governance, including fairness, accountability, transparency,                     showing that algorithmic decision-making can produce a
responsibility, and non-maleficence. This literature has been                     legitimacy gap when administrative action becomes detached
essential for clarifying why AI deployment must remain                            from accountable public reasoning [11]. Model cards improve
aligned with social and legal values, especially in high-stakes                   structured reporting and downstream review, but they remain
domains [1]-[3]. However, principle-centered work often                           primarily documentation mechanisms rather than internal
leaves unresolved the engineering question of how such                            control structures [12].
principles become executable constraints in real-time operation.
    This limitation is visible in the literature on AI ethics                           A. Self-Adaptive Architectures
guidelines. Jobin, Ienca, and Vayena show that AI ethics
                                                                                       The fourth stream comes from software engineering rather
guidelines converge around recurring principles but diverge in
                                                                                  than AI governance. Kephart and Chess introduced autonomic
implementation [1]. Hagendorff likewise argues that ethics
                                                                                  computing as a vision of systems that monitor, analyze, plan,
guidelines are normatively valuable but often weak in
                                                                                  and execute adaptation under shared knowledge [13]. Cheng et
enforcement [2]. Mittelstadt et al. further show that the debate
                                                                                  al. and Brun et al. argue that control loops should become first-
around algorithmic ethics becomes most consequential when
                                                                                  class entities in the engineering of self-adaptive software [14],
algorithmic systems shape institutional outcomes, yet the
                                                                                  [15]. Garlan, Schmerl, and Cheng show how architecture-based
connection between normative expectation and concrete
                                                                                  self-adaptation can use system models, evaluation logic, and
system behavior often remains underspecified [3].
                                                                                  adaptation managers to maintain system goals under changing
                                                                                  conditions [16].
         B.   Institutional and Standards-Based Governance                             This lineage is directly relevant to the present paper because
              Frameworks                                                          it provides the architectural vocabulary for observation, control,
    The second stream emphasizes organizational and                               and adaptation during operation. At the same time, these works
regulatory governance. The NIST AI Risk Management                                do not primarily address governance-specific concerns such as
Framework defines organization-level risk functions and                           rights-sensitive escalation, immutable policy constraints, or
governance processes [4]. The NIST Generative AI Profile                          audit-ready accountability traces. A ⁴ -Gov draws on the
extends that logic to risks that are more specific to generative-                 software-architecture logic of adaptation while shifting the
AI systems [5]. The EU AI Act specifies regulatory obligations                    adaptation target from generic quality optimization to policy-
for providers and deployers [6], while IEEE 7000 defines a                        aware governance.
process for addressing ethical concerns during system design
[7]. These frameworks are highly valuable because they
identify governance responsibilities, risk categories,
compliance expectations, and oversight structures.
    These frameworks establish what responsible governance
should cover. They help organizations govern AI systems, but
they do not fully specify how policy-aligned operating
standards should be represented and enforced during system




979-8-3195-0657-3/26/$31.00 ©2026 IEEE                                        642
SERAAuthorized
      2026, Maylicensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:22:13 UTC from IEEE Xplore. Restrictions apply.
                  27-29, 2026, Towson, USA
```

---

## PDF Page 3

```text
   Table 1. Comparative positioning of A⁴-Gov against existing governance and adaptive-control frameworks


     Framework                  Analytical level             Governance or control object              Operational timing            Primary evidence


                                                                                                        pre-deployment and
                                 organization and                                                                                   risk documentation,
   NIST AI RMF                                                  risk processes and controls                   ongoing
                              lifecycle governance                                                                                     control artifacts
                                                                                                            management


                                                                                                                                         conformity
                              legal and regulatory             compliance obligations and
     EU AI Act                                                                                         lifecycle compliance          evidence, technical
                                  governance                        provider duties
                                                                                                                                       documentation

                                                                                                                                        deviation logs,
                                                                policy baseline, deviation,
                                                                                                                                         action traces,
         A⁴-Gov             governance architecture             bounded action, escalation,            continuous operation
                                                                                                                                      revised baselines,
                                                                      accountability
                                                                                                                                      escalation records


     B. Research Gap                                                              conditions, intervention limits, and review obligations that
    Taken together, the literature provides strong guidance on                    remain inspectable during execution [4]-[8].
what should be governed and how governance responsibilities                           A⁴-Gov is also related to feedback-loop and self-adaptive
should be organized. What remains underdeveloped is the                           architectures [13], [14], [16], but the target of control is
operational layer that follows review and risk-assignment                         different. Existing adaptive architectures provide monitoring
decisions. Governance frameworks define responsibilities and
                                                                                  and response logic. A⁴-Gov adds a governance-specific chain
control expectations, but they do not specify how a running AI
                                                                                  from policy context to deviation interpretation, bounded
service should preserve policy state, enforce bounded
                                                                                  intervention, human escalation, and review-ready evidence.
intervention, or write review-ready evidence once deployment
begins. A⁴-Gov addresses that narrower problem. It functions
as the runtime governance layer that carries control
requirements into operation. Table 1 therefore contrasts                              V.         A⁴-Gov Architecture
lifecycle governance frameworks with the runtime control                              This section defines A⁴-Gov as the runtime layer that
objects preserved by A⁴-Gov.                                                      executes governance requirements after review and control
                                                                                  conditions have been set. The architectural task is to preserve
The central distinction is not simply internal versus external                    policy state during operation, detect governance-relevant
governance. It is that A⁴-Gov links policy state, deviation,                      deviation, select bounded action, and retain review-ready
bounded action, escalation, and evidence as runtime objects                       evidence.
after review decisions have already been made.

                                                                                        A. Components and State Ownership
   IV.        Conceptual Distinction from Existing Governance
              Frameworks                                                              A ⁴ -Gov can be represented as eight cooperating
                                                                                  architectural components: a Policy Registry, a Context
    Existing governance frameworks are typically designed                         Normalizer, a Baseline Generator, a State Monitor, a Deviation
around oversight, compliance, risk management, and                                Analyzer, a Decision Manager, an Escalation Manager, and an
institutional accountability. A⁴-Gov operates at a different                      Audit Logger. The Policy Registry owns the current policy
layer. It begins after review obligations and control                             snapshot and the distinction between immutable constraints
requirements have been specified and turns those requirements                     and adjustable thresholds. The Baseline Generator owns the
into runtime state, bounded actions, review triggers, and                         active baseline Bₜ. The Deviation Analyzer owns the deviation
evidence records within an AI service system.                                     record Dₜ. The Decision Manager proposes aₜ*, while the
                                                                                  Escalation Manager governs Hₜ and determines whether
   This distinction matters because the architecture does not
                                                                                  automated continuation is allowed. The Audit Logger writes Lₜ
compete with lifecycle governance frameworks. It carries their
                                                                                  as the durable review artifact.
control expectations into operation. In A ⁴ -Gov, policy
requirements enter the loop as active policy state, baseline



979-8-3195-0657-3/26/$31.00 ©2026 IEEE                                        643
SERAAuthorized
      2026, Maylicensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:22:13 UTC from IEEE Xplore. Restrictions apply.
                  27-29, 2026, Towson, USA
```

---

## PDF Page 4

```text
    The architecture assumes that upstream review, service
approval, or risk grading has already assigned a control profile
                                                                                         E. A3 Adaptability and Human Escalation
to the service or case. That control profile enters the loop
through the Policy Registry together with the active policy                           Adaptability selects a response when the observed system
snapshot. The runtime task is then to preserve those                              state deviates from the governance baseline. Because
requirements during baseline generation, deviation analysis,                      governance objectives may conflict, this stage uses weighted
bounded response selection, human escalation, and                                 priorities to determine which deviations should be minimized
accountability logging. Each stage leaves an inspectable                          first:
artifact: Θₜ, Xₜ, Bₜ, Pₜ, Dₜ, aₜ*, Hₜ, and Lₜ.
                                                                                               𝒂∗𝒕 = 𝒂𝒓𝒈 𝒎𝒊𝒏 ∑ 𝒘(𝒊,𝒕) 𝒅𝒊 (𝒂)                          (3)
                                                                                                              𝒂
                                                                                                                    𝒊

     B. Notation and Design Constraints                                              where wᵢ,ₜ represents the priority assigned to governance
   The following notation is used as a formal shorthand to                        objective i at time t, and dᵢ(a) represents the residual deviation
identify state variables and their dependencies, not as a                         associated with candidate action a.
complete computational specification.
    The architecture uses the following state variables: Xₜ, Θₜ,                     The architecture does not permit unrestricted self-
Bₜ, Pₜ, Dₜ, Wₜ, aₜ*, Hₜ, Bₜ₊₁, and Lₜ.                                            redefinition. Recalibration is bounded:
    In A⁴-Gov, the baseline is not a purely statistical reference                                𝑩(𝒕+𝟏) = 𝒉(𝑩𝒕 , 𝑫𝒕 , 𝑾𝒕 , 𝒂∗𝒕 )                      (4)
point. It is a policy-aligned operating standard derived from
service rules, fairness thresholds, safety constraints, and                           The function h may update tunable operating thresholds,
procedural requirements. The architecture separates immutable                     routing rules, or monitoring sensitivity, but it may not alter
governance constraints from tunable operational baselines.                        immutable legal or safety constraints held by the Policy
Legal prohibitions, mandatory safety caps, and rights-sensitive                   Registry. Human approval is mandatory when baseline revision
review rules are immutable during system operation. Service-                      would change rights-sensitive handling, reduce safety margins,
level thresholds, monitoring sensitivity, and batch-level routing                 or resolve unresolved policy conflict.
rules may be revised only within bounded policy authority.                            Human escalation is therefore a first-class subsystem rather
This distinction prevents the recalibration loop from                             than an afterthought. In A⁴-Gov, Hₜ becomes active when at
normalizing unsafe or unlawful drift.                                             least one of three conditions holds: the deviation exceeds a
                                                                                  predefined safety or fairness threshold; the case affects rights-
                                                                                  sensitive or vulnerable populations; or the proposed
     C. A1 Awareness                                                              recalibration crosses a policy authority boundary. When Hₜ is
   Awareness identifies the policy baseline relevant to the                       active, the Escalation Manager pauses automatic continuation
current operational context. It interprets the normalized input                   for the affected case or batch, routes the case to the authorized
together with the active policy state:                                            office, records the reviewer identity and decision, and writes
                                                                                  the approved action back into the loop as part of Lₜ. This design
                   𝑩𝒕 = 𝒇(𝒂𝒘) (𝑿𝒕 , 𝜣𝒕 )                           (1)            is consistent with work on meaningful human control, which
                                                                                  emphasizes that responsibility must remain aligned with human
                                                                                  ability and authority to intervene [17].
    The role of this stage is not yet to judge observed
performance. Its task is to determine what should count as an
acceptable state under the active governance context. The                              F. A4 Accountability
output of Awareness is therefore a policy-aligned baseline that
                                                                                      Accountability records the rationale for decisions, the basis
serves as the reference point for later evaluation.
                                                                                  of weighting, the presence or absence of human escalation, and
                                                                                  the sequence of operational Adaptability:
     D. A2 Assessment                                                                       𝑳𝒕 = {𝑿𝒕 , 𝜣𝒕 , 𝑩𝒕 , 𝑫𝒕 , 𝒂∗𝒕 , 𝑯𝒕 , 𝑩(𝒕+𝟏) }              (5)
    Assessment evaluates the difference between the observed                          For review and audit in public-service settings, the most
system state and the policy-aligned baseline:                                     important artifacts are the input context, the active policy
                    𝑫𝒕 = 𝒈(𝒂𝒔) (𝑷𝒕 , 𝑩𝒕 )                            (2)          standard, the measured deviation, the selected adaptability or
                                                                                  escalation decision, and the revised baseline with its rationale.
    Here, Dₜ encodes governance-relevant properties such as                       These records form the evidence core of A⁴-Gov: they carry
severity, persistence, fairness impact, and procedural breach,                    review requirements into operational traces that can later
rather than functioning as a generic error score. Once the gap is                 support explanation, institutional review, and accountability.
explicit, governance becomes a concrete basis for intervention
and review.



979-8-3195-0657-3/26/$31.00 ©2026 IEEE                                        644
SERAAuthorized
      2026, Maylicensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:22:13 UTC from IEEE Xplore. Restrictions apply.
                  27-29, 2026, Towson, USA
```

---

## PDF Page 5

```text
   Table 2 summarizes the example as review-ready evidence.
    Artifact            Example value and validation role
                          public_safety, high-risk location,
       Xₜ                  vulnerable area; establishes the
                                 operational context
                      P1 safety rule, fairness guard, 2h cap,
       Θₜ            mandatory review rule; establishes active
                                   policy state
                          priority = P1, max_response = 2h,
       Bₜ             fairness_guard = enabled; shows policy-
                              aligned baseline formation
                     priority = P3, estimated_response = 18h,
        Pₜ           no fairness alert; shows observed system
                                      behavior
                     critical safety gap, persistent fairness gap;
       Dₜ
                        shows governance-relevant deviation
                     override to P1, open batch review, require
       aₜ*            supervisor confirmation; shows bounded
                                                                                      Figure 1. A⁴-Gov as a runtime governance loop with bounded
                                    intervention                                  recalibration and accountability logging
                        true, municipal safety office review
       Hₜ
                      required; shows human escalation logic
                                                                                      VI.        READING THE STAGES THROUGH A PUBLIC-
                         tighter clustering alert threshold,                                     SERVICE EXAMPLE
       Bₜ₊₁          unchanged statutory cap; shows bounded                           This section provides an analytical walk-through of the
                                    recalibration                                 architecture in a public-service setting. The question is whether
                                                                                  the design preserves four required properties: explicit policy
                       case id, policy snapshot id, baseline                      state, governance-relevant deviation, bounded intervention,
       Lₜ              version, reviewer id, rationale code;                      and review-ready evidence.
                    shows audit-ready accountability evidence
                                                                                      The discussion is analytical rather than comparative. It tests
                                                                                  whether the defined components and state variables are
                                                                                  sufficient to preserve those four properties in the example.

     G. Architectural Summary
                                                                                        A. Architecture Evaluation Design
    Together, these four functions form the operational
governance layer that follows review and risk-assignment                              We examine four questions. EQ1 asks whether policy state
decisions. Figure 1 shows the runtime loop; Figures 2 and 3 can                   remains explicit in the operating loop. EQ2 asks whether the
be read together through the evidence core preserved in Lₜ.                       architecture turns observation into governance-relevant
Policy state enters through Θₜ and Bₜ, bounded intervention                       deviation rather than generic anomaly scoring. EQ3 asks
passes through aₜ* and Hₜ, and accountability is closed through                   whether bounded intervention and human escalation remain
the recorded trail. This is the architectural basis for treating A                tied to explicit authority limits. EQ4 asks whether the log
⁴-Gov as more than a general operating concept.                                   preserves enough state for retrospective review and
                                                                                  institutional accountability.
                                                                                      These questions are checked against observable artifacts.
                                                                                  EQ1 depends on Θₜ, Bₜ, and baseline versioning; EQ2 on Pₜ and
                                                                                  Dₜ; EQ3 on aₜ*, constraint flags, and Hₜ; and EQ4 on Lₜ,
                                                                                  reviewer identity, rationale codes, and revision records.




979-8-3195-0657-3/26/$31.00 ©2026 IEEE                                        645
SERAAuthorized
      2026, Maylicensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:22:13 UTC from IEEE Xplore. Restrictions apply.
                  27-29, 2026, Towson, USA
```

---

## PDF Page 6

```text
      B. Illustrative Public-Service Example                                      rationale, reviewer authority, and revised baseline as structured
    Consider a municipal AI-assisted public-service triage                        evidence.
system that processes citizen complaints, welfare requests, and                       The comparator clarifies the role of A⁴-Gov. A static-
safety-related reports. A specific case arrives at time t: an                     threshold design might flag the low-priority assignment, but it
urgent public-safety-related request from a vulnerable district                   would not preserve the policy snapshot, the fairness rationale,
that has already been reported more than once. The normalized                     or the authority boundary that triggered review. An external-
operational input Xₜ includes service_type = public_safety,                       audit-only design could inspect the incident later, but it would
location_risk = high, vulnerable_area = true, and                                 not intervene while the rights-sensitive prioritization was
reported_delay = repeated.
                                                                                  unfolding. A ⁴ -Gov joins runtime control with post-
    The active policy context Θₜ contains four relevant rules:                    deployment evidence.
urgent safety-related requests should receive priority level P1;
requests affecting vulnerable districts must not be assigned
lower priority solely because of historically lower response                           D. Failure-Oriented Check
rates; any predicted response window above two hours for a P1                        The same example can be stressed with a failure condition.
case is a procedural breach; and any batch-level fairness                         Suppose the system detects the deviation but revises the future
deviation involving a vulnerable district requires human review                   baseline by lowering the safety alert threshold for that district
by the responsible municipal office.                                              in order to reduce apparent false positives. If immutable
    From this context, A1 derives the baseline Bₜ:                                constraints and approval boundaries are not separated, the
required_priority = P1, max_response_window = 2h,                                 architecture would normalize harmful drift instead of
fairness_guard             =             enabled,             and                 correcting it. A⁴-Gov treats this as a governance failure. The
mandatory_review_if_batch_bias = true. The observed system                        recalibration is rejected, Hₜ remains active, and the Audit
state Pₜ, however, shows that the model assigned the case P3,                     Logger records that the proposed revision exceeded operating
estimated a response window of 18 hours, and did not raise a                      authority. In that sense, the escalation path serves as an
fairness alert because the model treated district-level under-                    assurance mechanism: it prevents unsafe continuation while
service as historical normality rather than active deviation.                     preserving a bounded fallback path for review [18].
    A2 therefore generates a deviation record Dₜ with                                 This stress case clarifies the paper's narrower adequacy
safety_gap = critical, response_window_breach = true, and                         claim. A governance-oriented loop must expose the active
district_fairness_gap = persistent. The priority vector Wₜ for                    policy baseline, interpret deviation in governance terms,
this service window weights safety at 0.50, fairness at 0.30, and                 constrain recalibration, and preserve enough trace data for
procedural regularity at 0.20. Under these weights, A3                            institutional review.
proposes the bounded action aₜ* = {override priority to P1, open
batch review for similar district cases, require supervisor
confirmation}. Because the proposed action concerns both a                            VII.       DISCUSSION
rights-sensitive service context and a persistent district-level
                                                                                      A⁴-Gov is best read as an operational governance layer
fairness pattern, the Escalation Manager activates Hₜ = true and
routes the case batch to the municipal safety office.                             rather than as a separate ethics framework. Governance failures
                                                                                  in public AI services often appear after deployment, when
    The crucial architectural point is that Bₜ₊₁ does not rewrite                 changing conditions, undocumented overrides, or conflicting
the governing law. The revised baseline tightens the monitoring                   priorities separate formal policy from actual system behavior.
threshold for clustered safety complaints from vulnerable                         The architecture addresses that gap by keeping policy state,
districts and adds a mandatory fairness alert for the next batch,                 intervention limits, review triggers, and evidence records inside
but it does not alter the immutable P1 requirement or the                         the runtime loop.
statutory response cap. A4 writes Lₜ with the case identifier,
                                                                                     This is particularly important in public-service settings,
timestamp, policy snapshot id, baseline version, deviation
                                                                                  where institutions must justify not only outputs but also
category, selected action, escalation status, reviewer office, and
                                                                                  changes in risk, priority, and policy interpretation over time.
rationale code.
                                                                                  The combination of baseline formation, deviation analysis,
                                                                                  bounded intervention, human review, and accountability
                                                                                  logging provides a concrete operating mechanism for that task.
      C. Structural Findings and Comparator
    The example preserves the required properties as follows.                         The scope remains bounded. The paper does not compare
Policy state remains explicit through Θₜ and Bₜ. Governance-                      performance against alternative control models, and the
relevant deviation appears in Dₜ rather than as a generic                         notation is descriptive rather than control-theoretic proof. What
anomaly flag. The intervention path remains bounded because                       it provides is a design that later work can instrument with
aₜ* and Hₜ are conditioned by policy limits and review authority.                 explicit grading rules, domain thresholds, and real operational
The resulting log retains the baseline, deviation, action                         logs.




979-8-3195-0657-3/26/$31.00 ©2026 IEEE                                        646
SERAAuthorized
      2026, Maylicensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:22:13 UTC from IEEE Xplore. Restrictions apply.
                  27-29, 2026, Towson, USA
```

---

## PDF Page 7

```text
                                                                                  [4] E. Tabassi, Artificial Intelligence Risk Management Framework (AI RMF
                                                                                  1.0), NIST AI 100-1. Gaithersburg, MD, USA: National Institute of Standards
    VIII.      CONCLUSION                                                         and Technology, 2023, doi: 10.6028/NIST.AI.100-1.
                                                                                  [5] C. Autio, R. Schwartz, J. Dunietz, S. Jain, M. Stanley, E. Tabassi, P. Hall,
    A⁴-Gov is presented in this paper as a runtime governance                     and K. Roberts, Artificial Intelligence Risk Management Framework:
architecture for AI service systems. Its role is not to replace                   Generative Artificial Intelligence Profile, NIST AI 600-1. Gaithersburg, MD,
lifecycle governance frameworks but to carry their control                        USA: National Institute of Standards and Technology, 2024, doi:
                                                                                  10.6028/NIST.AI.600-1.
requirements into operation through four linked functions:
                                                                                  [6] European Parliament and Council, Regulation (EU) 2024/1689 of 13 June
Awareness, Assessment, Adaptability, and Accountability.                          2024 laying down harmonised rules on artificial intelligence (Artificial
Within that loop, policy state, deviation, bounded intervention,                  Intelligence Act), Official Journal of the European Union, OJ L 2024/1689, 12
human escalation, and evidence logging are treated as explicit                    Jul. 2024.
design objects.                                                                   [7] IEEE Standards Association, IEEE Std 7000-2021: IEEE Standard Model
                                                                                  Process for Addressing Ethical Concerns during System Design. New York,
    The public-service walk-through shows the intended use of                     NY, USA: IEEE, 2021, doi: 10.1109/IEEESTD.2021.9536679.
the architecture. Once review conditions and risk grades have                     [8] J. Mokander and L. Floridi, "Operationalising AI governance through
been assigned, A⁴-Gov preserves them during operation and                         ethics-based auditing: an industry case study," AI and Ethics, vol. 3, no. 2, pp.
                                                                                  451-468, 2023, doi: 10.1007/s43681-022-00171-7.
records the resulting decision trail. That linkage between policy
                                                                                  [9] A. Taeihagh, "Governance of Generative AI," Policy and Society, vol. 44,
state, bounded response, and evidence is the paper's main claim.                  no. 1, pp. 1-22, 2025, doi: 10.1093/polsoc/puaf001.
Future work can extend the architecture with explicit grading                     [10] A. Reuel and T. A. Undheim, "Generative AI Needs Adaptive
functions, domain-specific thresholds, and empirical testing                      Governance," arXiv:2406.04554, 2024, doi: 10.48550/arXiv.2406.04554.
with real service logs.                                                           [11] P. D. Koenig and G. Wenzelburger, "The legitimacy gap of algorithmic
                                                                                  decision-making in the public sector: Why it arises and how to address it,"
                                                                                  Technology in Society, vol. 67, Art. no. 101688, 2021, doi:
                                                                                  10.1016/j.techsoc.2021.101688.
    Acknowledgment
                                                                                  [12] M. Mitchell et al., "Model Cards for Model Reporting," in Proc. Conf.
    This work was supported by the Institute of Information &                     Fairness, Accountability, and Transparency (FAT* '19), Atlanta, GA, USA,
                                                                                  2019, pp. 220-229, doi: 10.1145/3287560.3287596.
Communications Technology Planning & Evaluation (IITP)-
                                                                                  [13] J. O. Kephart and D. M. Chess, "The vision of autonomic computing,"
ICAN (ICT Challenge and Advanced Network of HRD) grant                            Computer, vol. 36, no. 1, pp. 41-50, 2003, doi: 10.1109/MC.2003.1160055.
funded by the Korea government (Ministry of Science and ICT)                      [14] B. H. C. Cheng et al., "Software Engineering for Self-Adaptive Systems:
(IITP-2026-RS-2022-00156299).         The     figures    were                     A Research Roadmap," in Software Engineering for Self-Adaptive Systems,
conceptually designed by the authors.                                             Berlin, Germany: Springer, 2009, pp. 1-26, doi: 10.1007/978-3-642-02161-9_1.
                                                                                  [15] Y. Brun et al., "Engineering Self-Adaptive Systems through Feedback
    ChatGPT was used only to improve the visual presentation                      Loops," in Software Engineering for Self-Adaptive Systems, Berlin, Germany:
of the final figure images. All technical content, figure labels,                 Springer, 2009, pp. 48-70, doi: 10.1007/978-3-642-02161-9_3.
captions, and final revisions were reviewed and approved by                       [16] D. Garlan, B. Schmerl, and S.-W. Cheng, "Software Architecture-Based
the authors.                                                                      Self-Adaptation," in Autonomic Computing and Networking, New York, NY,
                                                                                  USA: Springer, 2009, pp. 31-55, doi: 10.1007/978-0-387-89828-5_2.
                                                                                  [17] L. C. Siebert et al., "Meaningful human control: actionable properties for
                                                                                  AI system development," AI and Ethics, vol. 3, no. 1, pp. 241-255, 2023, doi:
                                                                                  10.1007/s43681-022-00167-3.
                                                                                  [18] A. Desai, S. Ghosh, S. A. Seshia, N. Shankar, and A. Tiwari, "SOTER: A
                                                                                  Runtime Assurance Framework for Programming Safe Robotics Systems," in
                                                                                  Proc. 49th Annual IEEE/IFIP Int. Conf. Dependable Systems and Networks
                                                                                  (DSN), 2019, pp. 138-150, doi: 10.1109/DSN.2019.00027.




    References
[1] A. Jobin, M. Ienca, and E. Vayena, "The global landscape of AI ethics
guidelines," Nature Machine Intelligence, vol. 1, pp. 389-399, 2019, doi:
10.1038/s42256-019-0088-2.
[2] T. Hagendorff, "The Ethics of AI Ethics: An Evaluation of Guidelines,"
Minds and Machines, vol. 30, pp. 99-120, 2020, doi: 10.1007/s11023-020-
09517-8.
[3] B. D. Mittelstadt, P. Allo, M. Taddeo, S. Wachter, and L. Floridi, "The
ethics of algorithms: Mapping the debate," Big Data and Society, vol. 3, no. 2,
2016, doi: 10.1177/2053951716679679.




979-8-3195-0657-3/26/$31.00 ©2026 IEEE                                        647
SERAAuthorized
      2026, Maylicensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:22:13 UTC from IEEE Xplore. Restrictions apply.
                  27-29, 2026, Towson, USA
```
