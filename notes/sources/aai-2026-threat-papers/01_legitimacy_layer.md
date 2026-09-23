# The Legitimacy Layer: A Runtime Governance Architecture for Human Oversight in AI-Assisted Critical Decision Systems

> Source PDF: `The_Legitimacy_Layer_A_Runtime_Governance_Architecture_for_Human_Oversight_in_AI-Assisted_Critical_Decision_Systems(1).pdf`

> Extraction note: Text extracted from the uploaded PDF using Poppler `pdftotext -layout`. Page boundaries are preserved below. Formatting, equations, tables, and multi-column reading order may not perfectly match the original PDF. Use the original PDF for authoritative visual/layout verification.


---

## PDF Page 1

```text
                                                                                                                                                                         The Legitimacy Layer: A Runtime Governance Architecture for Human Oversight in
                                                                                                                                                                                               AI-Assisted Critical Decision Systems
                                                                                                                                                                                                                                         Hamza Aarab(0009-0006-0061-3888)
                                                                                                                                                                                                                                           Independent Researcher
                                                                                                                                                                                                                                             Geneva, Switzerland
                                                                                                                                                                                                                                          m.hamzaaarab@gmail.com

                                                                                                                                                                        Abstract - Artificial intelligence systems increasingly support operational decision-making in safety-critical environments, yet existing governance
                                                                                                                                                                        frameworks primarily regulate AI before deployment and after incidents, leaving the runtime execution interval structurally unaddressed. This
                                                                                                                                                                        interval - the legitimacy gap - is the period in which AI-generated decisions may proceed to operational effect without active oversight,
2026 1st International Conference on Human Centric Artificial Intelligence (ICHCAI) | 979-8-3315-5118-6/26/$31.00 ©2026 IEEE | DOI: 10.1109/ICHCAI70183.2026.11607581




                                                                                                                                                                        contestability, or escalation control. This paper introduces the Legitimacy Layer, a runtime governance architecture that addresses the legitimacy
                                                                                                                                                                        gap by operating as model-agnostic middleware between the AI decision system and the operational environment. The architecture evaluates four
                                                                                                                                                                        governance signals (uncertainty, impact, reversibility, and contestation) and routes each decision through a legitimacy controller to one of four
                                                                                                                                                                        execution directives (execute, execute_async, escalate, or halt), regulated by a four-state autonomy model (Normal, Reduced, Human Oversight
                                                                                                                                                                        Required, Safe Halt). By specifying the architectural conditions under which human oversight, contestation, and escalation become structurally
                                                                                                                                                                        enforceable at runtime, the Legitimacy Layer positions human inclusion as an architectural property of the execution pipeline rather than an
                                                                                                                                                                        external assumption. The architecture is analytically validated through logical trace across four adversarial governance conditions and
                                                                                                                                                                        demonstrated through a reproducible prototype implementation publicly available for independent verification, proposing that runtime governance
                                                                                                                                                                        for AI-assisted critical decisions can be formally specified as model-agnostic middleware prior to empirical deployment validation.
                                                                                                                                                                        Keywords - Runtime AI governance, Human oversight, Contestability, Legitimacy gap, Governance middleware, Decision autonomy control

                                                                                                                                                                                                                                                           execution during which no governance mechanism evaluates
                                                                                                                                                                                              I. INTRODUCTION
                                                                                                                                                                                                                                                           whether the decision should proceed, be escalated, or be
                                                                                                                                                                        Artificial intelligence systems are increasingly embedded in                       contested, producing governance failures that are invisible until
                                                                                                                                                                        operational environments where decisions carry direct real-                        their consequences have already materialised.
                                                                                                                                                                        world consequences. Across operational environments
                                                                                                                                                                                                                                                           The contributions of this paper are as follows. Runtime
                                                                                                                                                                        characterised by time pressure, consequence asymmetry,
                                                                                                                                                                                                                                                           governance problem definition: formalisation of the legitimacy
                                                                                                                                                                        accountability requirements, and operator dependency
                                                                                                                                                                                                                                                           gap as a structural absence in current AI governance
                                                                                                                                                                        ( including energy grid management, transport control systems,
                                                                                                                                                                                                                                                           frameworks. Legitimacy Layer architecture: specification of a
                                                                                                                                                                        financial operations, and healthcare decision support), AI
                                                                                                                                                                                                                                                           model-agnostic runtime governance middleware comprising
                                                                                                                                                                        outputs no longer function solely as advisory analytics but may
                                                                                                                                                                                                                                                           eight components, decision intake interface, governance signal
                                                                                                                                                                        directly influence actions affecting infrastructure stability,
                                                                                                                                                                                                                                                           evaluator, governance mode manager, legitimacy controller,
                                                                                                                                                                        economic activity, and public welfare [1], [2]. As AI systems
                                                                                                                                                                                                                                                           contestability interface, governance policy store, execution
                                                                                                                                                                        move closer to operational control, ensuring that their decision
                                                                                                                                                                                                                                                           router, and audit log module. Controller routing mechanism:
                                                                                                                                                                        processes remain governable within institutional structures
                                                                                                                                                                                                                                                           design of a deterministic legitimacy controller that routes
                                                                                                                                                                        becomes a critical engineering challenge.
                                                                                                                                                                                                                                                           decisions across four execution directives according to
                                                                                                                                                                        In high-consequence environments, technical accuracy alone is                      governance signals and current autonomy state. Governance
                                                                                                                                                                        insufficient to guarantee institutional trust. Human operators                     mode state machine: definition of a four-state autonomy control
                                                                                                                                                                        bring contextual judgment, accountability, and the capacity for                    model: Normal Autonomy, Reduced Autonomy, Human
                                                                                                                                                                        reasoned intervention that automated systems cannot replicate                      Oversight Required, and Safe Halt, with formally specified
                                                                                                                                                                        in situations involving competing values or unanticipated                          entry conditions, transition logic, and exit conditions.
                                                                                                                                                                        circumstances [3], [4], [5], [6]. Trust in AI-assisted decision                    Evaluation methodology: development of a scenario-based
                                                                                                                                                                        systems depends not only on predictive accuracy but on the                         stress testing framework evaluated across four adversarial
                                                                                                                                                                        structural assurance that a human can intervene, contest, or                       governance conditions with defined pass and fail criteria.
                                                                                                                                                                        override a decision when conditions warrant. This assurance                        Prototype implementation: a publicly available reference
                                                                                                                                                                        cannot be assumed, it must be architecturally supported.                           implementation demonstrating the executability of Algorithm 1
                                                                                                                                                                        Existing AI governance frameworks are predominantly                                and the governance mode state machine, with a reproducible
                                                                                                                                                                        structured around two phases: pre-deployment validation,                           1,000-decision simulation reproducing Table IV [31].
                                                                                                                                                                        including risk assessment, model testing, and regulatory                           To our knowledge, no prior work integrates runtime governance
                                                                                                                                                                        compliance; and post-incident accountability, including                            signal evaluation, deterministic decision routing, graduated
                                                                                                                                                                        auditing and corrective review [7], [8]. While these                               autonomy control, and pre-execution contestability as a unified
                                                                                                                                                                        mechanisms serve important functions, neither operates during                      model-agnostic middleware architecture positioned between an
                                                                                                                                                                        decision execution itself. The runtime interval, in which AI-                      AI decision system and its operational environment. The
                                                                                                                                                                        generated decisions transition from model output to operational                    Legitimacy Layer specifies this combination as a concrete,
                                                                                                                                                                        effect remains structurally unaddressed.                                           formally defined system contribution.
                                                                                                                                                                        This creates what this paper terms the legitimacy gap: the                         The remainder of this paper is organised as follows. Section II
                                                                                                                                                                        interval between AI decision generation and operational                            reviews related work. Section III defines key concepts and the

                                                                                                                                                                        979-8-3315-5118-6/26/$31.00 ©2026 IEEE



                                                                                                                                                                              Authorized licensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:21:26 UTC from IEEE Xplore. Restrictions apply.
```

---

## PDF Page 2

```text
problem structure. Section IV presents the architecture. Section                  influence routing logic before execution completes. The timing
V describes the evaluation. Section VI discusses limitations and                  problem is structurally unresolved: by the time contestation is
future work. Section VII concludes. A note on scope. The                          possible under existing frameworks, the decision has already
Legitimacy Layer addresses human-centric AI at the                                produced operational consequences.
architectural level: it specifies the runtime conditions under                    C. Runtime Monitoring and Safety
which human operators and affected stakeholders are
                                                                                  Runtime monitoring has been an active area of research in
structurally included in consequential AI decisions (through
                                                                                  autonomous systems, safety-critical software engineering, and
escalation, contestation, and graduated autonomy) rather than
                                                                                  machine learning operations. Anomaly detection methods
assumed to be present by default. The architecture does not
                                                                                  identify deviations from expected system behaviour during
model human cognition, decision quality under load, or
                                                                                  operation, flagging inputs or outputs that fall outside learned or
interface usability; these are human-factors concerns requiring
                                                                                  specified distributions [18]. Out-of-distribution detection
empirical human-in-the-loop validation, identified as declared
                                                                                  research addresses the specific challenge of identifying when a
follow-on work (Section VI).
                                                                                  deployed model encounters inputs that differ significantly from
                      II. RELATED WORK                                            its training distribution, a condition associated with degraded
A. Human Oversight in AI                                                          predictive reliability. Uncertainty quantification methods
                                                                                  provide probabilistic estimates of model confidence at
Human oversight in AI-assisted decision systems has been
                                                                                  inference time, enabling downstream systems to assess the
widely studied across human-computer interaction, supervisory
                                                                                  reliability of individual predictions before acting on them [19],
control, and human factors research. Human-in-the-loop
                                                                                  [20]. Collectively, these methods provide the signal detection
models position human judgment as an active component
                                                                                  capability that runtime governance requires; they identify
within the decision pipeline, requiring human input before
                                                                                  conditions under which autonomous execution may be
consequential actions are taken [3], [4]. Human-on-the-loop
                                                                                  inappropriate. However, runtime monitoring literature
models adopt a monitoring posture, in which humans observe
                                                                                  addresses signal detection but not governance routing logic:
automated system behaviour and retain the capacity to
                                                                                  what the system should do when a signal crosses a threshold
intervene when anomalies are detected. Supervisory control
                                                                                  remains outside the scope of monitoring frameworks.
frameworks formalise the conditions under which operators
assume authority from automated systems, drawing on decades                       D. AI Governance Frameworks
of research in aviation, process control, and military command                    AI governance has developed as a multidisciplinary field
systems [9], [6]. This body of work establishes that meaningful                   addressing the responsible development, deployment, and
human oversight requires structured intervention pathways,                        oversight of AI systems across their operational lifecycle.
clearly defined authority boundaries, and mechanisms for                          Lifecycle governance models structure oversight across phases
transferring decision control under specified conditions [10],                    from design and development through deployment and
[11]. However, these frameworks establish the desirability of                     decommissioning, establishing accountability responsibilities
oversight without specifying the architectural mechanisms                         at each stage [21], [22]. Pre-deployment compliance
through which it is triggered, routed, or enforced during                         mechanisms, including conformity assessments, algorithmic
execution.                                                                        impact assessments, and certification processes, evaluate
B. Contestability in Algorithmic Systems                                          systems against technical and ethical requirements before they
                                                                                  enter operational use. Risk-based governance approaches
Contestability has emerged as a significant concern in the
                                                                                  classify AI systems by potential harm severity and apply
algorithmic accountability literature, reflecting the recognised
                                                                                  proportionate       oversight    requirements        accordingly,
need for individuals and institutions to challenge automated
                                                                                  concentrating regulatory attention on high-risk applications [7],
decisions that affect their interests. The right to explanation
                                                                                  [17], [23]. Post-incident accountability mechanisms provide
establishes that affected parties should be able to understand
                                                                                  structured processes for investigating failures, assigning
and dispute the basis of automated decisions [12], [13].
                                                                                  responsibility, and implementing corrective measures
Procedural fairness frameworks extend this principle by
                                                                                  following identified harms [8], [24]. While these frameworks
requiring that appeals and review mechanisms be accessible,
                                                                                  collectively     constitute    a   sophisticated      governance
timely, and capable of producing meaningful redress.
                                                                                  infrastructure, they bracket the runtime execution interval
Contestability has also been examined as a design property,
                                                                                  without addressing it. Compliance operates before deployment,
with proposals for interface mechanisms that allow users to
                                                                                  establishing the conditions under which a system is permitted
query, dispute, or request review of algorithmic outputs [14],
                                                                                  to operate. Accountability operates after incidents, establishing
[15], [16]. Despite this progress, existing contestability
                                                                                  what went wrong and who is responsible. The execution
mechanisms are predominantly oriented toward post-hoc or
                                                                                  interval, as the period during which AI-generated decisions are
legal processes, they provide channels through which decisions
                                                                                  actively transitioning to operational effect, lies between these
can be challenged after they have taken effect, through
                                                                                  phases and is left ungoverned by current lifecycle frameworks
administrative review, judicial appeal, or regulatory complaint.
                                                                                  [25].
They do not provide operational interfaces through which
contestation signals submitted by affected stakeholders can




     Authorized licensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:21:26 UTC from IEEE Xplore. Restrictions apply.
```

---

## PDF Page 3

```text
Recent work has begun to propose model-agnostic runtime                           As a concrete illustration: a clinical decision-support system
enforcement layers, control-plane governance architectures,                       recommending discontinuation of anticoagulation in a post-
and policy-driven orchestration mechanisms for agentic and                        stroke patient, with the upstream model reporting an uncertainty
enterprise AI systems. Gaurav et al. [26] introduce Governance-                   score of 0.65, the decision classed HIGH impact, non-reversible
as-a-Service, a modular policy-driven enforcement layer                           within a 6-hour governance window, and no active contestation
governing agent outputs at runtime with allow, warn, block, and                   signal, would be routed by Algorithm 1 through Rule 5 (HIGH
escalate outcomes. However, it does not specify the internal                      impact with uncertainty above the 0.6 high threshold) to
routing logic determining which outcome applies under which                       ESCALATE, transferring the decision to an attending clinician
signal conditions, does not define a system-level autonomy                        for review before execution.
state machine constraining controller behaviour across                            B. The Runtime Legitimacy Gap
operational modes, and does not provide a pre-execution
                                                                                  The central problem this paper addresses is formally defined as
contestability mechanism. The Legitimacy Layer addresses
                                                                                  follows. The legitimacy gap is the interval between the
each of these gaps directly. Goyal et al. [27] propose a unified
                                                                                  generation of an AI decision and its execution in the operational
AI orchestration platform with explicit control-plane and data-
                                                                                  environment during which no active governance mechanism
plane separation, incorporating policy engines, sandboxed
                                                                                  evaluates the decision's legitimacy or risk.
execution environments, and governance lifecycle management
across enterprise deployments. Recent preprints [28], [29], [30]                  The consequences of this absence are characterised by three
address related runtime and agentic governance concerns in                        distinct failure modes. The first is silent execution failure, in
adjacent problem spaces.                                                          which a decision executes outside acceptable governance
                                                                                  boundaries without triggering any oversight response. The
                 III. PROBLEM DEFINITION                                          system produces and applies a decision that would, under any
A. Critical Decision Environments                                                 reasonable governance evaluation, have required escalation or
The Legitimacy Layer targets a class of operational                               deferral but because no runtime evaluation occurs, the failure is
environments characterised by four structural properties that                     invisible until its operational effects materialise. The second
collectively distinguish it from general-purpose AI application                   failure mode is uncontestable execution, in which a decision
contexts. First, decisions must be made within operational                        produces operational effects before affected parties have any
windows that preclude extended deliberation, the temporal                         opportunity to challenge it. Even where contestability
structure of the environment compresses the interval available                    mechanisms exist in principle, their post-hoc orientation means
for evaluation, routing, and intervention. Second, errors                         that by the time a challenge can be submitted, the decision has
produce consequences that are difficult or impossible to                          already committed its consequences. The third failure mode is
reverse, the asymmetry between the cost of incorrect action and                   escalation collapse, in which conditions arise during execution
the cost of delayed action creates conditions in which                            that genuinely require human judgment, elevated uncertainty,
governance failures propagate before they can be detected or                      high-impact irreversible action, ambiguous accountability
corrected. Third, decisions must be traceable, explainable, and                   boundaries but no escalation pathway is available, operable, or
attributable to responsible parties, accountability requirements                  sufficiently specified to route the decision to a human operator
impose structural constraints on how decisions are recorded,                      within the available window.
communicated, and reviewed. Fourth, human operators are                           These failure modes are observable in current AI-assisted
present but may be overloaded, unavailable, or operating under                    pipelines across healthcare, financial, and infrastructure
incomplete information and the assumption of continuous,                          contexts, where the execution interval proceeds without active
attentive human oversight cannot be relied upon as a                              governance evaluation, the structural gap the Legitimacy Layer
governance mechanism in its own right.                                            is designed to close.
These four characteristics (time pressure, consequence                            C. Design Requirements
asymmetry, accountability requirements, and operator                              The problem analysis in Sections III-A and III-B yields five
dependency) are not incidental features of specific deployment                    design requirements that any runtime governance architecture
domains. A runtime governance architecture for these                              for critical AI decision systems must satisfy.
environments must function under time constraints, must
                                                                                  R1 - Runtime governance signal evaluation. The architecture
handle the possibility of operator unavailability, must produce
                                                                                  must evaluate governance-relevant signals during the execution
auditable records, and must be capable of restricting
                                                                                  interval, not only before deployment or after incidents. Signals
autonomous execution without requiring continuous human
                                                                                  including decision uncertainty, impact severity, reversibility,
attention. Deployment across specific domains will require
                                                                                  and stakeholder contestation must be assessed at the point of
domain-specific threshold calibration, illustratively, a clinical
                                                                                  execution.
decision support deployment might configure uncertainty
thresholds against ensemble disagreement metrics, impact                          R2 - Deterministic routing logic. The architecture must route
classes against clinical harm severity taxonomies, and                            decisions through a deterministic governance controller that
reversibility windows against the time horizon within which a                     produces consistent, auditable routing decisions based on
proposed intervention can be safely withdrawn.                                    defined signal thresholds. Routing logic must be transparent,
                                                                                  reproducible, and traceable in the audit record.




     Authorized licensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:21:26 UTC from IEEE Xplore. Restrictions apply.
```

---

## PDF Page 4

```text
R3 - Graduated autonomy control. The architecture must
support graduated reduction of AI autonomy in response to
elevated risk conditions, without requiring binary human-
machine switching. A governance architecture capable only of
full autonomy or full human control is operationally impractical
in time-pressured environments.
R4 - Operational contestability. The architecture must provide
a mechanism through which contestation signals submitted
during the execution window can influence routing decisions
before effects become irreversible.
R5 - Model-agnostic deployment. The architecture must
operate without modifying the upstream AI decision system,
enabling deployment as middleware compatible with existing
operational systems.
The Legitimacy Layer is designed to satisfy all five
requirements. Section IV presents its full architectural
specification, including component definitions, controller                          Fig. 1. Legitimacy Layer architecture showing decision flow from the AI
                                                                                  decision system via the governance pipeline to execution or human oversight.
routing logic, and governance mode transition conditions.
                                                                                  B. Component Architecture
These requirements assume governance signals are trusted
inputs supplied by the upstream system or operator-configured                     The Legitimacy Layer is implemented as a set of coordinated
policy layer. Signal trustworthiness and threshold calibration                    runtime components that collectively regulate the execution of
are deployment-time concerns identified as priorities for future                  AI-generated decisions, transforming model outputs into
work.                                                                             governance-aware execution directives.
                                                                                  The Decision Intake Interface serves as the entry point to the
   IV. THE LEGITIMACY LAYER ARCHITECTURE
                                                                                  Legitimacy Layer. It transforms raw AI model outputs into
A. Architecture Overview                                                          standardised decision records suitable for governance
The Legitimacy Layer is a runtime governance architecture                         evaluation, enabling the architecture to operate independently
designed to regulate how AI-generated decisions are executed                      of specific model implementations.
within operational systems. Rather than modifying the internal                    The Governance Signal Evaluator collects and validates the
logic of the upstream AI model, the architecture operates as                      four governance signals associated with each decision record
model-agnostic middleware positioned between the AI decision                      ( uncertainty score, decision impact class, reversibility flag, and
system and the operational execution environment, directly                        contestation signal) normalises them against policy-defined
satisfying the model-agnostic deployment requirement                              formats, and forwards the validated signal set to the Legitimacy
established in Section III (R5).                                                  Controller and Governance Mode Manager.
As illustrated in Fig. 1, the Decision Intake Interface captures                  The Governance Mode Manager maintains the system's current
AI system outputs and converts them into structured decision                      autonomy state across four governance modes: Normal
records. Four runtime governance signals (uncertainty score,                      Autonomy, Reduced Autonomy, Human Oversight Required,
decision impact class, reversibility flag, and contestation signal)               and Safe Halt. Rather than treating autonomy as a binary
are then evaluated at the point of execution, satisfying R1.                      condition, it dynamically constrains which routing directives
Routing directives are issued to the Execution Router, which                      the Legitimacy Controller may issue under prevailing
directs the decision toward autonomous execution, deferred                        operational conditions.
asynchronous execution, escalation, or operational halt. The                      The Legitimacy Controller is the core routing mechanism of the
eight internal components implementing this pipeline are                          architecture. It receives validated governance signals and the
specified in Section IV-B.                                                        current governance mode, evaluates them against deterministic
                                                                                  policy rules supplied by the Governance Policy Store, and
                                                                                  issues one of four routing directives (execute, execute_async,
                                                                                  escalate, or halt).
                                                                                  The Contestability Interface enables affected stakeholders to
                                                                                  submit contestation signals challenging an AI-generated
                                                                                  decision during the execution window before its effects become
                                                                                  irreversible. Contestation signals are forwarded to the
                                                                                  Governance Signal Evaluator and become active inputs to the
                                                                                  controller's routing evaluation.




     Authorized licensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:21:26 UTC from IEEE Xplore. Restrictions apply.
```

---

## PDF Page 5

```text
The Governance Policy Store maintains policy thresholds and                            6: end if

routing rules that parameterise the controller, enabling                               7: if signals.contestation_signal = TRUE then
governance parameters to be updated without modifying                                  8:    return ESCALATE
controller logic. The Execution Router implements directives                           9: end if
by directing decisions toward autonomous execution, reversible                         10: if signals.impact_class = CRITICAL then
asynchronous execution, escalation, or halt with queue                                 11:    return ESCALATE
preservation. The Audit Log Module records all governance                              12: end if
events in an append-only tamper-evident record operating                               13: if signals.impact_class = HIGH and
independently of the controller. The deterministic routing logic                             signals.uncertainty_score > high_threshold then
is specified in Section IV-C.                                                          14:    return ESCALATE
C. Runtime Legitimacy Controller                                                       15: end if

The Legitimacy Controller is the deterministic routing                                 16: if signals.reversibility_flag = TRUE and signals.impact_class = LOW and
                                                                                       signals.uncertainty_score ≤ high_threshold then
mechanism at the core of the Legitimacy Layer. Its function is
                                                                                       17:    return EXECUTE_ASYNC
to evaluate governance conditions at the moment a decision
                                                                                       18: end if
transitions toward operational execution and determine which
                                                                                       19: if signals.impact_class = LOW and
execution directive is permissible under the current runtime
                                                                                             signals.uncertainty_score < low_threshold then
context. Routing is deterministic as identical signal inputs under
                                                                                       20:    return EXECUTE
the same governance mode always produce the same directive
directly satisfying the deterministic routing logic requirement                        21: end if

(R2) and enabling full post-hoc audit verification.                                    22: return ESCALATE ▷ Default: fail toward human oversight

The controller evaluates four governance signals. The                             The routing logic applies a strict priority ordering. Governance
uncertainty score represents the predictive confidence of the                     mode is evaluated first because it represents a system-level
upstream AI model and serves as an indicator of potential                         constraint that overrides all signal-level evaluation,a system in
reliability degradation. The decision impact class reflects the                   Safe Halt or Human Oversight Required mode cannot be
severity of potential operational consequences, distinguishing                    returned to autonomous execution by a favourable signal
routine actions from those capable of producing irreversible or                   combination on a single decision. Contestation signal is
system-critical effects. The reversibility flag indicates whether                 evaluated before impact class and uncertainty because it
operational effects can be withdrawn within a defined execution                   represents an external governance claim that cannot be
window. The contestation signal represents an external                            overridden by system-generated signals alone. The default
challenge submitted by an affected stakeholder indicating that                    case escalates rather than executes, embedding a conservative
the decision's legitimacy requires re-evaluation before                           failure posture: when no condition is matched, the architecture
execution proceeds.                                                               fails toward human oversight rather than autonomous action.
While the architecture treats these signals as validated inputs                   Safety constraints override contestation signals, contestation
supplied by the upstream AI system or operator-configured                         overrides impact classification, and both override uncertainty-
policy layer, their practical production is domain-specific. In a                 based routing conditions.
clinical decision support context, for example, the uncertainty                   The rule set is deliberately non-exhaustive over the joint
score may be derived from ensemble disagreement across                            (impact × uncertainty × reversibility) signal space. HIGH-
model predictions or from conformal prediction intervals at                       impact decisions with uncertainty at or below the high
inference time. The decision impact class may be configured by                    threshold, and LOW-impact decisions that fail either the
clinical governance teams against established harm severity                       reversibility precondition for EXECUTE_ASYNC or the low-
taxonomies, distinguishing routine advisory outputs from                          uncertainty precondition for EXECUTE, are not matched by
recommendations capable of producing irreversible patient                         any preceding rule and therefore route through the default.
consequences. The reversibility flag reflects whether a                           This is consistent with the conservative failure posture: signal
proposed clinical action (such as a medication adjustment                         combinations not explicitly authorised for autonomous or
versus a surgical referral) can be withdrawn within a defined                     asynchronous execution are routed to human oversight rather
governance window. Specific configurations are governance                         than resolved by a permissive default.
policy inputs subject to domain-specific derivation rather than                   The asynchronous execution pathway introduced by the
architectural constants.                                                          EXECUTE_ASYNC directive is described in Section IV-D.
    Algorithm 1: route_decision(signals, governance_mode)
                                                                                  D. Asynchronous Governance
    ────────────────────────────────────────
    1: if governance_mode = SAFE_HALT then
                                                                                  Requiring human approval before every moderate-risk decision
    2:   return HALT
                                                                                  is operationally impractical. The EXECUTE_ASYNC directive
    3: end if
                                                                                  addresses this by targeting decisions that cannot safely proceed
                                                                                  under unrestricted autonomy yet do not require immediate
    4: if governance_mode = HUMAN_OVERSIGHT_REQUIRED then
                                                                                  escalation, providing a bounded execution pathway that
    5:   return ESCALATE
                                                                                  maintains operational continuity while preserving governance




     Authorized licensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:21:26 UTC from IEEE Xplore. Restrictions apply.
```

---

## PDF Page 6

```text
intervention capability. This intermediate state implements the                   Mode transitions follow two directional paths, as illustrated in
graduated autonomy control requirement (R3), positioning                          Fig. 2. The escalation path progresses from Normal Autonomy
asynchronous governance between the execute and escalate                          through Reduced Autonomy and Human Oversight Required
directives established in Section IV-C.                                           toward Safe Halt as signal thresholds are crossed or integrity
When the Legitimacy Controller issues EXECUTE_ASYNC                               conditions are violated. Any mode may transition directly to
(triggered when the reversibility flag is TRUE, uncertainty                       Safe Halt on system integrity failure. Recovery transitions
remains within acceptable bounds, and no contestation signal is                   follow the reverse path but require explicit operator clearance
active) the decision executes immediately but enters a                            at each stage, as the system does not return automatically to
reversible execution window defined by governance policy.                         Normal Autonomy, ensuring that a human operator has
This window functions as a temporal buffer between execution                      confirmed that the conditions warranting reduced autonomy no
initiation and final commitment of the decision's effects. The                    longer apply. The evaluation of this state machine under
Contestability Interface remains active throughout: contestation                  adversarial conditions is presented in Section V.
signals submitted by affected stakeholders are processed by the
controller, which responds by issuing ESCALATE and
initiating reversal. If the window expires without contestation,
the decision is committed and can no longer be reversed
through the governance layer. All window events are recorded
by the Audit Log Module.
Asynchronous governance is subject to strict constraints: it
cannot be applied to decisions with a reversibility flag of
FALSE, nor under governance modes that prohibit autonomous
execution, Human Oversight Required or Safe Halt. The
reversibility window is the primary operational interval in
which contestability produces real governance effect. Once
commitment occurs, runtime reversal is no longer possible
through the architecture, making window integrity critical. The
governance mode conditions governing all execution pathways
are specified in Section IV-E.
E. Governance Mode State Machine
The Legitimacy Layer regulates system autonomy through a
four-state governance mode model that constrains controller                         Fig. 2. Governance mode state machine showing escalation and recovery
                                                                                               transition paths between the four autonomy states.
routing based on the broader operational condition of the
system, not only on individual decision signals. This prevents                                  V. SPECIFICATION VALIDATION
favourable signal combinations on a single decision from re-                      A. Evaluation Approach
enabling autonomous execution under elevated risk conditions.                     The architecture is evaluated using scenario-based analytical
The Governance Mode Manager evaluates current mode as the                         trace: governance logic is subjected to controlled adversarial
first routing priority before any signal-level condition is                       runtime conditions and its outputs assessed against predefined
assessed.                                                                         pass and fail criteria. Scenarios are derived from the three
The architecture defines four governance modes. In Normal                         runtime failure modes defined in Section III-B (silent execution
Autonomy, the system operates under standard conditions and                       failure, uncontestable execution, escalation collapse) in a
the controller may issue execute or execute_async for decisions                   manner analogous to hazard-based systems-safety analysis
meeting signal thresholds, full routing capability is available. In               [32], with each scenario targeting one failure mode under
Reduced Autonomy, the execute directive is restricted to low-                     adversarial signal injection; routing behaviour is then checked
impact decisions, asynchronous execution remains available for                    against predefined expected outcomes in the spirit of trace- and
reversible decisions, and escalation is triggered when individual                 comparison-based validation in simulation modelling [33]. The
signal thresholds are met as the system continues operating                       approach is appropriate for pre-deployment specifications,
under tighter governance constraints. In Human Oversight                          evaluating correctness of governance signal interpretation,
Required, both execute and execute_async are suppressed and                       routing behaviour, and mode transitions without requiring a
all decisions are routed through escalate, transferring decision                  deployed implementation.
authority to a human operator. In Safe Halt, all execution is                     B. Evaluation Procedure
suspended, pending decisions are queued without processing,
and only halt is permitted, activated by system integrity failures,               Each scenario initialises the system in Normal Autonomy
audit log unavailability, governance policy store unavailability,                 mode, injects scenario-specific governance signal conditions,
or operator timeout on an unresolved escalation.                                  records the resulting controller directive and mode transition,
                                                                                  and compares observed behaviour against predefined pass and
                                                                                  fail conditions.




     Authorized licensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:21:26 UTC from IEEE Xplore. Restrictions apply.
```

---

## PDF Page 7

```text
C. Evaluation Scenarios                                                           decision executes during Safe Halt; system returns directly to
Each scenario is designed to stress-test the architecture's                       Normal Autonomy without passing through Human Oversight
response to one of the three failure modes identified in Section                  Required. Primary metric: operator workload.
III-B: Scenarios 1 and 2 address silent execution failure,                        TABLE I. Analytical Logical Trace Results Across Evaluation Scenarios
Scenario 3 addresses uncontestable execution, and Scenario 4                                             Injected                                                Mode
                                                                                     Scenario                                      Observed Directive                            Pass/Fail
addresses                   escalation                   collapse.                                      Condition                                              Transition

Scenario 1 - Uncertainty Spike. Injected signal: uncertainty                                            uncertainty
                                                                                                                              ESCALATE at threshold
                                                                                                                                                               Normal
                                                                                       1-                                             crossing;
score elevated progressively from below high-uncertainty                            Uncertainty
                                                                                                       progressively
                                                                                                          exceeds
                                                                                                                              EXECUTE_ASYNC for
                                                                                                                                                              Autonomy
                                                                                                                                                              → Reduced
                                                                                                                                                                                   Pass
                                                                                      Spike                                    reversible LOW below
threshold through to halt threshold across sequential decision                                        high_threshold
                                                                                                                                      threshold
                                                                                                                                                              Autonomy

records. Expected result: system transitions from Normal                                              uncertainty held         ESCALATE for HIGH-
                                                                                                                                                                Reduced
                                                                                                                                                               Autonomy
Autonomy to Reduced Autonomy; if halt threshold is reached,                         2 - Sustained
                                                                                     Uncertainty
                                                                                                           above
                                                                                                       high_threshold
                                                                                                                                       impact;
                                                                                                                                 EXECUTE_ASYNC
                                                                                                                                                               → Human             Pass
controller issues escalate; reversible decisions may route                                             across window           blocked above threshold
                                                                                                                                                               Oversight
                                                                                                                                                               Required
through execute_async under Reduced Autonomy. Pass                                       3-
                                                                                                    contestation_signal
                                                                                                                                 ESCALATE issued;               Human
                                                                                                          = TRUE,
condition: mode transition to Reduced Autonomy occurs at                            Contestation
                                                                                                        reversibility
                                                                                                                               reversal initiated before       Oversight           Pass
                                                                                    (in-window)                                        commit                  Required
correct threshold; escalate issued before any halt-threshold                             3-
                                                                                                      window active
                                                                                                    contestation_signal            Signal logged; no
decision routes to execute; all events recorded in audit log. Fail                  Contestation     = TRUE, window           intervention on committed       No transition        Pass
                                                                                   (post-commit)           expired                      decision
condition: controller issues execute for any decision at or above                                                                HALT issued; queue
                                                                                                                                                                Human
high-uncertainty threshold; mode transition does not fire                           4 - Operator    escalation timeout
                                                                                                                                  preserved; recovery
                                                                                                                              requires Human Oversight
                                                                                                                                                               Oversight
                                                                                                                                                                                   Pass
correctly. Primary metric: escalation latency.                                      Unavailable         exceeded
                                                                                                                                 Required not Normal
                                                                                                                                                               Required
                                                                                                                                                              → Safe Halt
                                                                                                                                      Autonomy
Scenario 2 - Sustained Uncertainty. Injected signal: uncertainty                  D. Evaluation Metrics
score held persistently above high-uncertainty threshold across
a sustained sequence of decisions within a policy-defined                         Four metrics provide observable, architecture-specific
observation window. Expected result: system remains in                            indicators of governance correctness across the evaluation
Reduced Autonomy; transitions to Human Oversight Required                         scenarios.
if escalation-triggering conditions accumulate; high-impact                         TABLE II. Evaluation Metrics - Observable Governance Correctness
decisions must not route to autonomous execution. Pass                                                         Indicators
condition: Reduced Autonomy entered and maintained                                    Metric                Definition                   Unit           Good Result
                                                                                                                                                                               Failure
                                                                                                                                                                              Condition
correctly; Human Oversight Required triggered when                                                  Time between detection of                                                 Exceeds
accumulation conditions met; autonomous execution restricted                         Escalation          threshold-crossing
                                                                                                                                       Seconds
                                                                                                                                                      Within policy-       policy-defined
                                                                                      latency       condition and issuance of                         defined bound            bound
for elevated-risk decisions. Fail condition: system returns                                               escalate directive
prematurely to Normal Autonomy; high-impact decisions                                                 Proportion of decisions
                                                                                      Missed             meeting escalation
routed through execute during sustained abnormal uncertainty.                        escalation         conditions routed to          Percentage
                                                                                                                                                        Zero missed
                                                                                                                                                        escalations
                                                                                                                                                                            Any non-zero
                                                                                                                                                                               value
                                                                                        rate        execute or execute_async
Primary metric: missed escalation rate.                                                              instead of escalate or halt
                                                                                    Contestation    Time between contestation                            Resolved           Not resolved
Scenario 3 - Stakeholder Contestation. Injected signal:                              resolution           receipt and final            Seconds        before window            before
contestation signal submitted against (i) a decision within an                          time          governance disposition                               closes           commitment
                                                                                                       Number of escalation                           Within policy-          Exceeds
active reversibility window and (ii) a decision post-commit.                         Operator
                                                                                     workload
                                                                                                      directives generated per
                                                                                                                                       Escalation
                                                                                                                                      per window
                                                                                                                                                         defined           policy-defined
Expected result: sub-scenario (i): controller issues escalate and                                         decision window                                 bounds               bounds

initiates reversible execution intervention; sub-scenario (ii):                   The operator workload metric warrants additional
signal logged, committed execution pathway unaltered. Pass                        consideration given its practical significance for deployment
condition: sub-scenario (i): escalate issued and intervention                     viability. As an illustrative estimate, if the system processes D
initiated before window closes; all events logged; sub-scenario                   decisions per hour and the simulation-derived escalation rate
(ii): post-commit contestation recorded, no intervention                          under balanced signal conditions is 82.9%, the expected
attempted on committed decision. Fail condition: sub-scenario                     operator load approaches D × 0.829 escalations per hour under
(i): escalate not triggered within window; sub-scenario (ii):
                                                                                  those conditions. In practice, this rate would be substantially
system attempts intervention on committed decision. Primary
                                                                                  lower under operationally representative parameter
metric: contestation resolution time.
                                                                                  configurations, as characterised analytically in Section V-G
Scenario 4 - Operator Unavailable. Injected signal: escalation
                                                                                  and Table V; operational deployments would configure
directive active; operator response withheld beyond policy-
                                                                                  contestation frequency and impact class distributions to reflect
defined escalation timeout. Expected result: system transitions
from Human Oversight Required to Safe Halt; pending                               domain-specific decision volumes and risk profiles. Research
decisions queued; no further execution directives permitted                       on human interaction with automation establishes that systems
until recovery conditions satisfied. Pass condition: system                       generating excessive escalation rates risk operator
enters Safe Halt at policy-defined timeout; all pending                           complacency and disuse: when automation interrupts too
execution blocked; system re-enters Human Oversight                               frequently, operators reduce their monitoring attention or
Required (not Normal Autonomy) following operator re-                             disengage from escalation pathways entirely, undermining the
authorisation; all events recorded in audit log. Fail condition:                  governance function the architecture is designed to provide




     Authorized licensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:21:26 UTC from IEEE Xplore. Restrictions apply.
```

---

## PDF Page 8

```text
[6]. This workload estimate is illustrative and not derived from                                     Halt                       0                  0.0%
empirical deployment conditions; its validation requires
human-in-the-loop testing identified as a priority item for
future work.                                                                              Among high-impact and critical-impact instances, 529 of 529
                                                                                          (100%) were routed to escalate, confirming that the architecture
E. Scenario Coverage Matrix                                                               maintains a conservative governance posture across varied
TABLE III. Scenario Coverage Matrix - Primary and Secondary Metric                        signal conditions. The 82.9% escalation rate decomposes
                           Applicability                                                  analytically across four routing sources: active contestation
            Metric               Scenario 1        Scenario 2   Scenario 3   Scenario 4   signals (20.0 points), CRITICAL impact decisions (16.0
                                                                                          points), HIGH impact combined with uncertainty above the
      Escalation latency          Primary          Secondary    Secondary    Secondary    high threshold (9.6 points), and the default fallthrough (36.4
                                                                                          points). The default fallthrough is the largest single contributor
    Missed escalation rate       Secondary          Primary         -        Secondary    and reflects two classes of unmatched signal combinations:
                                                                                          HIGH-impact decisions with uncertainty at or below the high
  Contestation resolution time       -                 -         Primary         -        threshold (14.4 points), which no preceding rule handles, and
                                                                                          LOW-impact decisions that fail either the reversibility
      Operator workload          Secondary         Secondary    Secondary     Primary     precondition for EXECUTE_ASYNC or the low-uncertainty
                                                                                          precondition for EXECUTE (22.0 points). The rate is therefore
F. Evaluation Scope and Limits                                                            not primarily driven by contestation but by the architecture's
This evaluation validates correctness of governance signal                                conservative failure posture specified in Section IV-C, which
interpretation, routing logic, governance mode transitions, and                           routes unmatched decisions toward human oversight rather than
architectural robustness under runtime governance disruptions.                            autonomous action.
It cannot validate real-world deployment performance,
statistical performance of the upstream AI model, operator                                To characterise how the escalation rate depends on input
usability under workload, organisational adoption, or threshold                           regime, Table V reports the analytical prediction of the total
calibration for specific domains.                                                         ESCALATE rate across a 2×2 grid of configurations, varying
Four limitations constrain the conclusions: reliance on                                   the uncertainty distribution and the contestation probability
simulated signal injection rather than deployed execution;                                while holding the impact mix, reversibility probability, and
scenarios modelled as isolated rather than compound                                       controller thresholds constant. The values are derived in closed
conditions; configurable rather than empirically derived                                  form from Algorithm 1's priority-ordered rules under the stated
thresholds; and operator workload treated as a design-constraint                          signal distributions. A verification run of the simulator at each
indicator rather than measured human-factors evidence. All                                grid cell (N=1000, averaged over 20 seeds) agrees with the
four are revisited as future work in SectionVI-B.                                         analytical prediction within ±1.5 percentage points, confirming
                                                                                          that the implementation faithfully realises the specified routing
G. Minimal Routing Simulation
                                                                                          logic. The 82.9% result reported in Table IV corresponds to the
To demonstrate the executability of the controller routing
                                                                                          top-left cell and agrees with its analytical value of 82.0%.
logic, a minimal simulation of 1,000 decision instances was
conducted under Normal Autonomy mode assumptions.                                            TABLE V. Total ESCALATE rate across input regimes (analytical
Governance signals were sampled across the full parameter                                            prediction; simulation agrees within ±1.5 pp)
space relevant to routing behaviour: uncertainty ∈ [0,1],                                  Uncertainty distribution   p_contestation = 0.20   p_contestation = 0.02
impact ∈ {low, high, critical} with probabilities of 0.5, 0.3,
and 0.2 respectively, reversibility ∈ {true, false}, and
                                                                                                 Uniform[0,1]                82.0%                   78.0%
contestation ∈ {true, false} with a 0.2 probability of active
contestation. Algorithm 1 was applied deterministically to
                                                                                                  Beta(2,5)                  69.2%                   62.3%
each instance. Routing outcomes are summarised in Table IV.

TABLE IV. Routing Distribution Across 1,000 Simulated Decision Instce
                                                                                          (Impact mix LOW/HIGH/CRITICAL = 0.5/0.3/0.2, reversibility probability 0.5,
                                                                                          thresholds            low=0.3                /                 high=0.6.)
           Directive                     Count                  Percentage                The grid shows that the escalation rate is a controllable function
                                                                                          of input regime rather than a fixed architectural property: lower
                                                                                          contestation probability reduces the contestation component by
            Execute                           53                   5.3%
                                                                                          the corresponding amount, and a left-shifted uncertainty
       Execute_Async                         118                   11.8%
                                                                                          distribution reduces Rule 5 escalations while increasing HIGH-
                                                                                          impact fallthroughs under the current rule set. These four
            Escalate                         829                   82.9%
                                                                                          configurations are illustrative of the parameter surface and do
                                                                                          not identify a privileged operational rate; domain-specific rates
                                                                                          depend on calibration of impact class distributions, uncertainty




       Authorized licensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:21:26 UTC from IEEE Xplore. Restrictions apply.
```

---

## PDF Page 9

```text
distributions, contestation frequencies, and thresholds against                      pressure [5] shows that escalation does not guarantee a better
operational data, identified as a deployment-time concern in                         outcome than autonomous execution in all conditions. Future
Section III-C and as future work in Section VI-B.                                    work should examine the conditions under which human
                                                                                     intervention improves governance outcomes and integrate
Halt directives were not produced under Normal Autonomy                              human-factors evidence into escalation threshold calibration.
mode, consistent with the specification in Section IV-E, which                       B. Limitations and Future Work
restricts halt to Safe Halt mode transitions rather than signal-
                                                                                     A reference prototype implementation has been developed and
level routing alone. All routing decisions were consistent with
                                                                                     is publicly available [31]. The evaluation confirms architectural
the deterministic policy rules specified in Section IV-C, with no
                                                                                     coherence under simulated signal injection but cannot capture
instance producing an unexpected directive. The prototype
                                                                                     failure modes that emerge only at runtime in real systems.
implementation and simulation code are publicly available to
                                                                                     Future work should evaluate the prototype's behaviour against
support                    reproducibility                    [31].
                                                                                     real decision streams in a controlled operational context.
To illustrate dynamic governance mode behaviour, Table VI
                                                                                     The contestability interface assumes that affected stakeholders
presents a manually constructed decision sequence designed to
                                                                                     are identifiable, reachable, and capable of submitting
traverse all four governance states. Signal values are illustrative
                                                                                     contestation signals within the reversibility window. This
examples consistent with the architecture's transition logic;
                                                                                     assumption does not hold uniformly across deployment
operational threshold values are governance policy inputs
                                                                                     contexts — in emergency response or infrastructure control
subject to domain-specific calibration, as noted in Section III-
                                                                                     environments, affected parties may not be known at execution
C.
                                                                                     time or may be unable to act within compressed operational
            TABLE VI. Deterministic Mode Transition Sequence
                                                                                     windows. Addressing this gap requires domain-specific
                                                                                     stakeholder identification protocols and accessible interface
 Step    Unc.     Impact             Cont.                    Mode     Mode
                             Rev.              Directive                             designs, identified as prerequisites for deployment in contexts
                                                              Before   After
                                                                                     where real-time contestability cannot be structurally
  1       0.3      Low       True    False      Execute        NA       NA           guaranteed.
                                                                                     The scenario-based evaluation validates routing correctness and
  2       0.5      Low       True    False   Execute_Async     NA       NA           mode transition behaviour but does not measure real-world
                                                                                     latency, resilience under infrastructure load, or integration
  3       0.7      High      False   False      Escalate       NA       RA           effects in complex deployments.
                                                                                     The routing and mode-transition rules depend on configurable
  4       0.8      High      False   False      Escalate       RA       RA           parameters (uncertainty thresholds, escalation conditions, and
                                                                                     reversibility windows)treated here as governance policy inputs
  5       0.9     Critical   False   False      Escalate       RA      HOR           rather than empirically validated constants. Future work should
                                                                                     develop domain-specific threshold calibration methodologies
  6       0.9     Critical   False   False      Escalate      HOR      HOR           and evaluate governance sensitivity to threshold variation.
                                                                                     Governance thresholds, impact class taxonomies, and
  7        -         -         -       -     Halt (timeout)   HOR       SH           contestation interface design are themselves value-laden
                                                                                     decisions that redistribute risk between autonomous execution,
(Unc. = Uncertainty, Rev. = Reversibility, Cont. = Contestation, NA = Normal
Autonomy, RA = Reduced Autonomy, HOR = Human Oversight Required, SH                  operator workload, and affected stakeholder access; their
                               = Safe Halt.)                                         domain-specific calibration therefore requires ethical review
The sequence confirms that the governance mode state machine                         alongside technical calibration and is not a neutral engineering
transitions correctly under escalating risk conditions. This                         task.
minimal simulation does not constitute empirical validation but                      The operator workload metric and the design requirements
demonstrates that the routing logic specified in Algorithm 1 is                      themselves require human-in-the-loop validation beyond the
directly executable under concrete runtime conditions, and that                      scope of this paper, including requirements elicitation from
the governance mode state machine behaves consistently with                          domain operators in the target deployment contexts. Real
its formal specification.                                                            operational environments may also produce compound signal
                                                                                     interactions (simultaneous uncertainty spikes, contestation
                VI. DISCUSSION AND LIMITATIONS
                                                                                     events, and operator constraints) that exceed what the four
A. Discussion                                                                        isolated scenarios model, and should be addressed in future
An important boundary condition of this contribution should be                       evaluation. The rule set of Algorithm 1 is specified to be non-
noted. The architecture governs whether human operators are                          exhaustive over the joint signal space, routing unmatched
included in the decision process but does not address the quality                    combinations to the default (Section IV-C); whether to replace
of human judgment under the conditions in which escalation                           this implicit default with explicit rules for currently-unmatched
occurs. Research on automation-induced complacency [10],                             signal combinations is a design choice identified for future
mode confusion [11], and operator performance under time                             work.




        Authorized licensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:21:26 UTC from IEEE Xplore. Restrictions apply.
```

---

## PDF Page 10

```text
                     VII. CONCLUSION                                                             [12] S. Wachter, B. Mittelstadt, and L. Floridi, "Why a right to explanation of automated
                                                                                                        decision-making does not exist in the General Data Protection Regulation," Int. Data
Existing AI governance frameworks leave the runtime                                                     Privacy Law, vol. 7, no. 2, pp. 76–99, 2017, doi: 10.1093/idpl/ipx005.
execution interval between decision generation and operational                                   [13] B. Goodman and S. Flaxman, "European Union regulations on algorithmic decision-
                                                                                                        making and a right to explanation," AI Mag., vol. 38, no. 3, pp. 50–57, 2017, doi:
effect structurally unaddressed. To address this problem, the                                           10.1609/aimag.v38i3.2741.
paper introduced the Legitimacy Layer, a runtime governance                                      [14] T. Hirsch, K. Merced, S. Narayanan, Z. E. Imel, and D. C. Atkins, "Designing
architecture designed as model-agnostic middleware positioned                                           contestability: Interaction design, machine learning, and mental health," in Proc.
                                                                                                        2017 Conf. Designing Interactive Syst. (DIS), Edinburgh, U.K., 2017, pp. 95–99,
between an AI decision system and the operational                                                       doi: 10.1145/3064663.3064703.
environment. The architecture shows how governance can be                                        [15] D. K. Mulligan, D. N. Kluttz, and N. Kohli, "Shaping our tools: Contestability as a
embedded directly into the execution pipeline through                                                   means to promote responsible algorithmic decision making in the professions,"
                                                                                                        SSRN Electron. J., 2019, doi: 10.2139/ssrn.3311894.
governance signal evaluation, deterministic routing logic,                                       [16] M. Almada, "Human intervention in automated decision-making: Toward the
graduated autonomy control, and operational contestability. By                                          construction of contestable systems," in Proc. 17th Int. Conf. Artif. Intell. Law
                                                                                                        (ICAIL), Montreal, QC, Canada, 2019, pp. 1–10, doi: 10.1145/3322640.3326699.
routing decisions through bounded directives (autonomous
                                                                                                 [17] D. Amodei et al., "Concrete problems in AI safety," arXiv:1606.06565 [cs.AI], Jun.
execution, reversible asynchronous execution, escalation, and                                           2016.
halt)the Legitimacy Layer proposes that legitimacy can be                                        [18] D. Hendrycks and K. Gimpel, "A baseline for detecting misclassified and out-of-
treated as an operational control problem rather than only as a                                         distribution examples in neural networks," arXiv:1610.02136, 2016, doi:
                                                                                                        10.48550/arXiv.1610.02136.
normative or regulatory concern. Future work should extend                                       [19] Y. Gal and Z. Ghahramani, "Dropout as a Bayesian approximation: Representing
this contribution through operational deployment testing,                                               model uncertainty in deep learning," in Proc. 33rd Int. Conf. Mach. Learn. (ICML),
domain-specific threshold calibration, and human-in-the-loop                                            vol. 48, 2016, pp. 1050–1059.
                                                                                                 [20] B. Lakshminarayanan, A. Pritzel, and C. Blundell, "Simple and scalable predictive
validation of escalation and oversight processes. Beyond these                                          uncertainty estimation using deep ensembles," in Adv. Neural Inf. Process. Syst.
directions, the broader significance of this work lies in what it                                       (NeurIPS), vol. 30, 2017, pp. 6402–6413.
establishes for human-centric AI: that the moment a decision                                     [21] A. Dafoe, "AI governance: A research agenda," Future of Humanity Inst., Univ. of
                                                                                                        Oxford, Oxford, U.K., Tech. Rep., 2018.
acts upon the world is not beyond governance, and that the
                                                                                                 [22] A. Batool, D. Zowghi, and M. Bano, "AI governance: A systematic literature review,"
systems entrusted with consequential decisions in critical                                              AI Ethics, vol. 5, pp. 3265–3279, 2025, doi: 10.1007/s43681-024-00653-w.
environments can be held accountable not only before they are                                    [23] C. Novelli, F. Casolari, A. Rotolo, M. Taddeo, and L. Floridi, "AI risk assessment: A
deployed or after they fail, but at the precise moment they act.                                        scenario-based, proportional methodology for the AI Act," Digit. Soc., 2024, doi:
                                                                                                        10.1007/s44206-024-00095-1.
                           ACKNOWLEDGMENT                                                        [24] C. Novelli, M. Taddeo, and L. Floridi, "Accountability in artificial intelligence: What
                                                                                                        it is and how it works," AI Soc., vol. 39, no. 4, pp. 1871–1882, 2024, doi:
AI-assisted tools (including ChatGPT and Grammarly) were used for language                              10.1007/s00146-023-01635-y.
editing and formatting. All scientific content, analysis, and conclusions are                    [25] J. Schuett, "Frontier AI developers need an internal audit function," Risk Anal., vol.
solely the author’s responsibility.                                                                     44, no. 11, Oct. 2024, doi: 10.1111/risa.17665.
                                                                                                 [26] S. Gaurav, J. Heikkonen, and J. Chaudhary, "Governance-as-a-Service: A Multi-
                                  REFERENCES                                                            Agent Framework for AI System Compliance and Policy Enforcement,"
                                                                                                        arXiv:2508.18765 [cs.LG], Aug. 2025, doi: 10.48550/arXiv.2508.18765.
[1] J. Perez-Cerrolaza, J. Abella, F. J. Cazorla, C. Hernandez, R. Vargas, A. Batiz, P. Trigo,
        and A. Zuepke, "Artificial intelligence for safety-critical systems in industrial and    [27] I. Goyal, G. Patil, and A. Shaikh, "Unified Multi-Channel AI Orchestration Platform
        transportation domains: A survey," ACM Comput. Surv., vol. 56, no. 7, Art. no. 176,             Architecture," J. Comput. Sci. Technol. Stud., vol. 7, no. 10, pp. 400–425, Oct. 2025,
        2024, doi: 10.1145/3626314.                                                                     doi: 10.32996/jcsts.2025.7.10.42.
[2] W. Wang and C. Chung, "Artificial intelligence in safety-critical systems: A systematic      [28] C. L. Wang et al., "MI9: An integrated runtime governance framework for agentic
        review," Ind. Manage. Data Syst., vol. 122, no. 2, pp. 442–470, 2021, doi:                      AI," arXiv:2508.03858 [cs.AI], Aug. 2025.
        10.1108/IMDS-07-2021-0419.                                                               [29] O. A. Basir, "The social responsibility stack: A control-theoretic architecture for
[3] T. A. Bach, J. K. Kristiansen, A. Babić, and A. Jacovi, "Unpacking human-AI                         governing socio-technical AI," arXiv:2512.16873 [cs.AI], Dec. 2025.
        interaction in safety-critical industries: A systematic literature review," IEEE         [30] E. Calboreanu, "LATTICE: A governance-first architecture for authorized
        Access, vol. 12, pp. 106385–106414, 2024, doi: 10.1109/ACCESS.2024.3437190.                     autonomous       AI     operations,"    Zenodo,      Tech.      Rep.,   2026,     doi:
[4] E. Veitch and O. A. Alsos, "A systematic review of human-AI interaction in                          10.5281/zenodo.18419923.
        autonomous ship systems," Safety Sci., vol. 152, Art. no. 105778, 2022, doi:             [31] H. Aarab, "Legitimacy Layer Prototype," GitHub, 2026, v1.1. [Online]. Available:
        10.1016/j.ssci.2022.105778.                                                                     https://github.com/MrHamzaAb/legitimacy-layer-prototype
[5] T. B. Sheridan, Humans and Automation: System Design and Research Issues.                    [32] N. G. Leveson, Engineering a Safer World: Systems Thinking Applied to Safety.
        Hoboken, NJ, USA: Wiley, 2002.                                                                  Cambridge, MA, USA: MIT Press, 2011.
[6] R. Parasuraman, T. B. Sheridan, and C. D. Wickens, "A model for types and levels of          [33] R. G. Sargent, "Verification and validation of simulation models," J. Simul., vol. 7,
        human interaction with automation," IEEE Trans. Syst., Man, Cybern. A, Syst.                    no. 1, pp. 12–24, 2013, doi: 10.1057/jos.2012.20.
        Humans, vol. 30, no. 3, pp. 286–297, 2000, doi: 10.1109/3468.844354.
[7] B. W. Wirtz, J. C. Weyerer, and I. Kehl, "Governance of artificial intelligence: A risk
        and guideline-based integrative framework," Gov. Inf. Q., vol. 39, no. 4, Art. no.
        101685, 2022, doi: 10.1016/j.giq.2022.101685.
[8] I. D. Raji et al., "Closing the AI accountability gap: Defining an end-to-end framework
        for internal algorithmic auditing," in Proc. 2020 Conf. Fairness, Accountability,
        Transparency (FAT*), Barcelona, Spain, 2020, pp. 33–44, doi:
        10.1145/3351095.3372873.
[9] T. B. Sheridan, Telerobotics, Automation, and Human Supervisory Control.
        Cambridge, MA, USA: MIT Press, 1992.
[10] L. Bainbridge, "Ironies of automation," Automatica, vol. 19, no. 6, pp. 775–779, 1983,
        doi: 10.1016/0005-1098(83)90046-8.
[11] M. R. Endsley, "From here to autonomy: Lessons learned from human-automation
        research," Hum. Factors, vol. 59, no. 1, pp. 5–27, 2017, doi:
        10.1177/0018720816681350.




        Authorized licensed use limited to: Universiti Malaysia Sabah. Downloaded on September 23,2026 at 15:21:26 UTC from IEEE Xplore. Restrictions apply.
```
