# Controlled Agentic AI Systems: A Governance-Driven Architecture for Auditable and Reproducible Decision Pipelines

> Source PDF: `Controlled Agentic AI Systems- A Governance-Driven Architecture for Auditable and Reproducible Decision Pipelines(1).pdf`

> Extraction note: Text extracted from the uploaded PDF using Poppler `pdftotext -layout`. Page boundaries are preserved below. Formatting, equations, tables, and multi-column reading order may not perfectly match the original PDF. Use the original PDF for authoritative visual/layout verification.


---

## PDF Page 1

```text
Article

Controlled Agentic AI Systems: A Governance-Driven Architecture
for Auditable and Reproducible Decision Pipelines
Tymoteusz Miller 1,2

                                         1   Institute of Marine and Environmental Sciences, University of Szczecin, Waska
                                                                                                                        ˛    13, 71-415 Szczecin, Poland;
                                             tymoteusz.miller@usz.edu.pl
                                         2   Faculty of Data Science and Information, INTI International University, Nilai 71800, Malaysia


                                         Abstract
                                         Artificial intelligence systems deployed in safety-critical and regulated environments re-
                                         quire not only predictive performance, but also strict adherence to operational constraints,
                                         auditability, and reproducibility. However, in most contemporary architectures, governance
                                         is treated as an external or post hoc mechanism, limiting the ability to ensure consistent
                                         and verifiable decision execution. This paper introduces Controlled Agentic AI Systems
                                         (CAIS), a formal architectural framework in which governance is embedded directly into
                                         the decision pipeline as a deterministic operator. The proposed formulation integrates a
                                         decision model, a constraint specification, and a governance operator that transforms pro-
                                         posed actions into admissible executed actions. The framework further defines audit trace
                                         semantics and replayability conditions, enabling deterministic reconstruction of decision
                                         trajectories. Theoretical analysis demonstrates that, under standard regularity assumptions,
                                         governance can be modeled as a non-expansive projection that enforces constraint-aware
                                         decision transformation while inducing bounded decision drift. This provides formal
                                         guarantees that governance does not destabilize system dynamics under perturbations.
                                         To evaluate these properties, we implement a reference CAIS architecture and conduct
                                         controlled experiments in multi-agent and federated simulation environments. The re-
                                         sults show that embedding governance significantly reduces the frequency and severity
                                         of constraint violations across a range of scenarios. Projection-based repair consistently
                                         outperforms approval-only strategies, achieving near-complete compliance in structured
                                         regimes while maintaining bounded intervention costs. Importantly, governance does not
                                         degrade stability or convergence in federated settings and, in some cases, reduces action-
                                         level variance induced by distributed training. While strict feasibility cannot be guaranteed
                                         in all practical settings due to approximation and solver limitations, the empirical findings
                                         confirm that governance acts as a stabilizing transformation that consistently improves
                                         compliance without introducing destabilizing effects. The CAIS framework establishes
                                         governance as a first-class architectural component of agentic AI systems, providing a
                                         unified foundation for designing constraint-aware, auditable, and reproducible decision
Academic Editor: Francesco Flammini      pipelines in regulated environments.
Received: 19 March 2026
Revised: 29 April 2026                   Keywords: controlled AI systems; governance operator; constraint-aware AI; agentic
Accepted: 4 May 2026                     systems; auditable AI; reproducible AI; federated learning governance; decision pipeline
Published: 8 May 2026                    architecture; safety-critical AI; regulatory AI systems
Copyright: © 2026 by the author.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license.




Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                            https://doi.org/10.3390/make8050125
```

---

## PDF Page 2

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                             2 of 31



                                         1. Introduction
                                               Artificial intelligence systems are increasingly deployed in environments where de-
                                         cisions have legal, economic, or safety-critical consequences [1,2]. Maritime navigation,
                                         energy grids, healthcare systems, financial infrastructures, and autonomous mobility all
                                         share a common requirement: decisions generated by machine learning models must
                                         not only be accurate but also compliant, auditable, and reproducible [3,4]. Despite rapid
                                         advances in deep learning, reinforcement learning, and multi-agent systems, the majority
                                         of AI architectures continue to treat governance as an external layer imposed after model
                                         inference rather than as an intrinsic component of the decision pipeline.
                                               In most contemporary AI systems, regulatory validation, audit logging, and constraint
                                         checking are implemented as post hoc filters or supervisory wrappers [5]. Such approaches
                                         assume that model-generated actions can be evaluated and possibly corrected after in-
                                         ference without fundamentally altering system dynamics. However, in safety-critical or
                                         regulated environments, this separation between decision generation and decision admissi-
                                         bility introduces structural fragility [6]. The decision policy operates in an unconstrained
                                         space, while regulatory logic acts as a secondary correction mechanism. This architec-
                                         tural decoupling creates ambiguities in responsibility attribution, weakens reproducibility
                                         mechanisms and complicates formal reasoning about system stability [5,7].
                                               Agent-based AI systems exacerbate this challenge. In multi-agent environments,
                                         decisions propagate through interaction loops, leading to emergent dynamics that are
                                         sensitive to even minor perturbations [8,9]. When governance constraints are applied
                                         externally, they may introduce discontinuities in agent behavior that are neither formally
                                         characterized nor dynamically analyzed. Similarly, in federated settings where models
                                         are trained across distributed nodes, governance policies are often inconsistently enforced
                                         across participants, resulting in heterogeneous compliance mechanisms. The absence of a
                                         unified formal model integrating decision policies and regulatory constraints remains a
                                         fundamental gap in current AI system design [10–12].
                                               Artificial intelligence systems deployed in safety-critical and regulated environments
                                         must satisfy multiple, partially overlapping requirements related to reliability, transparency,
                                         and accountability. In this context, the notions of trustworthy AI, explainable AI, and
                                         responsible AI are often used interchangeably, despite addressing different aspects of
                                         system behavior, e.g., [13,14].
                                               Trustworthy AI refers to the ability of a system to operate reliably under defined con-
                                         straints, including robustness to perturbations, compliance mechanisms, and compliance
                                         with regulatory requirements. Explainable AI, in contrast, focuses on the interpretability
                                         and transparency of model decisions, aiming to provide human-understandable justifica-
                                         tions for system outputs. Responsible AI extends these concepts to encompass broader
                                         ethical and societal considerations, including fairness, accountability, and governance
                                         processes [1,2,15,16].
                                               While these paradigms provide important guidance for the evaluation and deployment
                                         of AI systems, they typically operate at the level of post hoc analysis, monitoring, or policy
                                         definition. They do not, however, provide direct mechanisms for enforcing constraints at
                                         the moment of decision execution. This limitation motivates the need for architectures in
                                         which governance is not external to the system but embedded directly within the decision
                                         pipeline [1,2,13–16].
                                               This paper introduces the concept of Controlled Agentic AI Systems (CAIS), a class of
                                         AI systems in which governance is not an auxiliary mechanism but a first-class operator
                                         within the decision pipeline. A CAIS integrates a decision model Mθ , a constraint set C,
                                         and a governance projection operator G that deterministically transforms proposed actions
                                         into an admissible action space. The central premise is that the executed action at time



                                                                                                      https://doi.org/10.3390/make8050125
```

---

## PDF Page 3

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                             3 of 31



                                         t is not simply the output of the policy πθ , but the result of a structured transformation
                                         at = G (πθ ( xt ), C, st ), where governance constraints are mathematically embedded into the
                                         decision process.
                                               By formalizing governance as a projection operator over the action space, we enable
                                         several properties that are difficult to guarantee in conventional architectures. First, con-
                                         straint satisfaction becomes structurally enforced rather than probabilistically encouraged.
                                         Second, audit traces can be generated as deterministic mappings between input states,
                                         proposed decisions, constraint evaluations, and executed actions. Third, system behavior
                                         becomes replayable under identical seeds and constraint configurations, allowing full re-
                                         producibility of decision trajectories. These properties are particularly relevant in high-risk
                                         domains where regulatory compliance and traceability are not optional requirements but
                                         operational necessities.
                                               The contribution of this work is threefold. We provide a formal definition of Controlled
                                         Agentic AI Systems and characterize the governance operator as a decision-space projection
                                         with constraint-preserving properties. We analyze theoretical implications of embedding
                                         governance within the decision transformation, including bounded decision drift and
                                         stability under constraint enforcement. Finally, we implement a reference architecture and
                                         conduct controlled simulation experiments to evaluate the empirical impact of governance
                                         projection on constraint violations, adversarial robustness, and system dynamics.
                                               The central research hypothesis investigated in this study is that embedding a de-
                                         terministic governance operator within the decision pipeline reduces the frequency of
                                         inadmissible system states without inducing destabilizing effects on agentic system dy-
                                         namics. By integrating formal reasoning with experimental validation, this work aims to
                                         establish a principled architectural foundation for auditable, reproducible, and regulation-
                                         aware AI systems.

                                         Related Works
                                               In reinforcement learning, safety has been addressed through constrained optimization
                                         and safe exploration techniques. Methods such as Constrained Policy Optimization and
                                         Lyapunov-based approaches enforce safety conditions during training [17,18], while other
                                         works introduce safety layers or shielding mechanisms that restrict unsafe actions at
                                         execution time [19,20]. Although effective, these approaches typically operate either at
                                         the optimization level or as external filters, rather than as intrinsic components of the
                                         decision pipeline.
                                               Control-theoretic approaches provide formal enables for constraint satisfaction using
                                         tools such as control barrier functions and predictive safety filters [21–23]. These methods
                                         are closely related to projection-based governance, as they enforce admissibility through
                                         structured transformations of control inputs. However, they are primarily designed for
                                         continuous control systems and do not directly address auditability or reproducibility in
                                         AI decision pipelines.
                                               The literature on trustworthy and explainable AI has emphasized transparency, inter-
                                         pretability, and accountability [24–27]. While these approaches improve understanding of
                                         model behavior, they are largely post hoc and do not provide mechanisms on constraint
                                         satisfaction during execution.
                                               Federated learning introduces additional challenges related to stability, heterogeneity,
                                         and adversarial robustness [28,29]. Existing methods focus on improving convergence
                                         and mitigating parameter divergence, including proximal and variance-reduction tech-
                                         niques [30,31]. However, these approaches primarily operate in parameter space and do
                                         not directly address action-level stability.




                                                                                                      https://doi.org/10.3390/make8050125
```

---

## PDF Page 4

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                       4 of 31



                                               In multi-agent systems, interactions between agents can amplify instability and lead to
                                         emergent unsafe behaviors [32–34]. While coordination and learning stability in multi-agent
                                         systems have been extensively studied, including approaches such as Multi-Agent Deep
                                         Deterministic Policy Gradient (MADDPG), experience replay stabilization techniques, and
                                         comprehensive surveys of multi-agent reinforcement learning, these works focus primarily
                                         on convergence and coordination rather than constraint compliance and execution-level
                                         safety [35,36].
                                               Federated learning constitutes an important class of distributed learning paradigms
                                         in which multiple clients collaboratively train a shared model without exchanging raw
                                         data [29]. While this approach improves data privacy and scalability, it introduces sig-
                                         nificant challenges related to statistical heterogeneity, communication constraints, and
                                         training instability [37]. Differences in local data distributions and asynchronous updates
                                         can lead to divergence of model parameters and inconsistent decision behavior across
                                         clients. Although methods such as FedProx and variance-reduction techniques have been
                                         proposed to mitigate these effects, they primarily address convergence in parameter space
                                         rather than stability of executed actions [38]. This distinction is critical in safety-critical
                                         systems, where consistency of decisions is often more important than convergence of model
                                         parameters [35].
                                               A significant body of work has addressed safety in reinforcement learning and con-
                                         trol systems. Constraint-aware reinforcement learning methods incorporate safety con-
                                         ditions into the optimization objective, often through reward shaping or constrained
                                         policy updates. Similarly, control-theoretic approaches, including control barrier func-
                                         tions and predictive safety filters, enforce admissibility through state-space constraints or
                                         optimization-based filtering.
                                               In parallel, execution-level safety mechanisms such as shielding and runtime safety
                                         layers have been proposed to prevent unsafe actions by modifying or rejecting model
                                         outputs. While these approaches provide practical mechanisms for constraint enforcement,
                                         they are typically implemented as external components that operate outside the core
                                         decision transformation.
                                               In contrast, the CAIS framework introduces governance as an intrinsic part of the
                                         decision pipeline. Rather than modifying the training process or applying post hoc cor-
                                         rections, governance is formalized as a deterministic operator that transforms proposed
                                         actions into admissible actions prior to execution. This architectural perspective enables
                                         unified reasoning about constraint compliance, auditability, and reproducibility, which are
                                         usually treated as separate concerns in existing literature.

                                         2. Preliminaries: State Space, Action Space, and the Governance Operator
                                              Let’s consider an agentic AI system evolving over discrete time steps t ∈ N. The
                                         system is defined over an environment state space S , an observation space X , an action
                                         space A, and a (possibly stochastic) transition kernel T .

                                         2.1. State, Observation, and Transition Model
                                              Let st ∈ S denote the environment state at time t. The state may include both physical
                                         variables (e.g., kinematic state, positions, velocities) and contextual variables (e.g., traffic
                                         situation, risk level, communication delays), as well as internal system variables relevant
                                         to governance (e.g., active regulatory mode, safety margin). The environment evolves
                                         according to a transition kernel

                                                                              s t +1 ∼ T ( s t , a t , ξ t ),




                                                                                                                https://doi.org/10.3390/make8050125
```

---

## PDF Page 5

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                         5 of 31



                                         where at ∈ A is the executed action and ξ t is an exogenous disturbance capturing noise,
                                         unobserved factors, and stochasticity in the environment.
                                             Agents typically do not observe st directly. Instead, an observation xt ∈ X is generated
                                         by an observation mapping
                                                                               x t = Ω ( s t , ηt ),

                                         where ηt denotes sensing noise. In practical systems, xt may correspond to fused sensor
                                         outputs, perception embeddings, or a structured feature vector after preprocessing and
                                         sensor fusion. We emphasize that the CAIS formulation is agnostic to whether xt is a
                                         raw sensor representation, a latent embedding, or a symbolic state estimate; the only
                                         requirement is that xt is the input used by the decision model.
                                              A decision model (policy) πθ , parameterized by θ, produces a proposed decision dt
                                         (also called a candidate action):

                                                                                   dt = πθ ( xt ) ∈ D .

                                              Here, D denotes the proposal space, which may coincide with A (if the model outputs
                                         directly executable actions), or may be a richer space such as trajectories, waypoints, control
                                         vectors, or symbolic intents.

                                         2.2. Constraints and the Admissible Action Set
                                              A regulated environment imposes a set of constraints that define which actions are ad-
                                         missible in a given context. Let C denote the constraint specification. In general, constraints
                                         may depend on the current state st , the observation xt , time t, and internal governance
                                         mode mt . We therefore model admissibility via a state-dependent feasible action set:

                                                                                      A C ( s t ) ⊆ A.

                                             We define AC (st ) as the set of all actions that satisfy every constraint in the specification
                                         C under state st . A convenient and general representation is via a set of constraint functions

                                                                             gi (st , a) ≤ 0, i = 1, . . . , k,

                                         so that

                                                                       A C ( s t ) = { a ∈ A | gi ( s t , a ) ≤ 0 ∀ i }

                                              This form encompasses hard safety constraints (collision avoidance, exclusion zones),
                                         regulatory constraints (right-of-way rules, speed limits), resource constraints (energy bud-
                                         gets, communication limits), and system constraints (actuator bounds).
                                              In addition, some constraints may be soft, providing graded penalties rather than
                                         hard rejection. We denote soft constraints by functions h j (st , a), and treat them as part of
                                         a preference model used in action repair or selection. Importantly, the CAIS framework
                                         does not require all constraints to be hard; rather, it distinguishes between constraints that
                                         define feasibility and constraints that define optimality within the feasible set.
                                              To provide an intuitive overview of the proposed architecture, Figure 1 illustrates the
                                         structure of the CAIS and the interaction between its main components.




                                                                                                                  https://doi.org/10.3390/make8050125
```

---

## PDF Page 6

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                     6 of 31




                                         Figure 1. Architecture of the CAIS. The decision pipeline transforms observations into proposed
                                         actions using a policy model, which are subsequently processed by a governance operator to produce
                                         admissible actions under a defined constraint set. The executed actions influence the environment
                                         through state transitions. The system incorporates audit trace semantics (Φ), capturing decision-
                                         relevant variables for full traceability, and a replay mechanism (Ψ) enabling deterministic repro-
                                         duction of decision sequences. The architecture supports federated learning through distributed
                                         parameter updates across multiple clients.

                                         2.3. Formal Definition of the Governance Operator G
                                              The central mechanism of CAIS is the governance operator G, which deterministically
                                         maps the proposed decision dt into an admissible executed action at . We define G as
                                         a function
                                                                          G : D×S ×C → A

                                         where C denotes the space of constraint specifications (policy sets). The executed action is

                                                                                 a t = G ( d t , s t , C ).

                                              A governance operator is required to satisfy the following admissibility condition:

                                         Definition 1 (Constraint-preserving governance). A governance operator G is constraint-
                                         preserving with respect to C if for all states s ∈ S and all proposals d ∈ D ,

                                                                               G (d, s, C ) ∈ AC (s).

                                             While the governance operator is defined as constraint-preserving in the idealized
                                         formulation, this property depends on the structure of the admissible action space and



                                                                                                              https://doi.org/10.3390/make8050125
```

---

## PDF Page 7

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                       7 of 31



                                         the implementation of the projection mechanism. In practical settings, constraint sets may
                                         be non-convex, coupled across agents, or only approximately represented. Additionally,
                                         numerical solvers used for projection may introduce approximation errors. As a result, the
                                         operator may only approximate the feasible set, potentially leading to residual constraint
                                         violations. This distinction between theoretical enables and practical implementation is
                                         explicitly examined in the experimental evaluation.
                                              This is the structural core of CAIS: feasibility is enforced by construction, not by post
                                         hoc evaluation. If D = A, G can be interpreted as a projection onto the feasible action set.
                                         If D is a richer space, G can be interpreted as a projection composed with a decoding map
                                         into A.
                                              To make this notion operational, we define G in terms of three sub-mechanisms that cor-
                                         respond to common governance behaviors in real systems: approval, repair, and fallback.
                                              Approval map. Let IC (s, a) denote an indicator of admissibility:
                                                                                         (
                                                                                             1,   a ∈ AC (s )
                                                                           IC (s, a) =
                                                                                             0,   otherwise.

                                              When the proposal is already admissible, G should preserve it (identity on feasible
                                         actions), yielding a minimal-intervention property:

                                                                    if d ∈ AC (s) and D = A, G (d, s, C ) = d.

                                              This property supports that governance does not distort correct decisions unnecessarily.
                                              Repair map. When the proposal is inadmissible, governance must produce a corrected
                                         action. We define an action repair operator

                                                                            R : D × S × C → A C ( s ),

                                         and write a = R(d, s, C ) as the repaired action. A canonical choice is to define R as a
                                         projection that minimizes deviation from the proposal under a cost metric ∆(·, ·):

                                                                       R(d, s, C ) = arg min ∆( a, ρ(d)),
                                                                                             a∈AC (s)


                                         where ρ : D → A maps proposals to action space when D ̸= A. The metric ∆ can encode
                                         domain-specific notions of minimal intervention (e.g., smallest steering correction, minimal
                                         speed change, smallest trajectory deviation).
                                              Fallback map. In some states, the feasible set may be empty or numerically intractable
                                         due to conflicting constraints, uncertain state estimates, or tight safety margins. We there-
                                         fore define a safe fallback action a⋆ (s, C ), e.g., a stop, loiter, or conservative maneuver, and
                                         require that
                                                                                  
                                                                                   ρ ( d ),
                                                                                                   ρ (d ) ∈ AC (s )
                                                                    G (d, s, C ) = R(d, s, C ),      AC (s ) ̸ = ∅
                                                                                   a⋆ (s, C ),      AC (s) = ∅.
                                                                                  

                                              This decomposition captures the practical structure of governance in regulated systems
                                         while maintaining a mathematically explicit definition. It also supports implementation-
                                         level separation between constraint evaluation, repair optimization, and fallback logic.

                                         2.4. Governance-Induced Decision Drift and Minimal Intervention
                                              A key architectural question is whether governance introduces destabilizing distor-
                                         tions. We define governance-induced decision drift as the magnitude of deviation between
                                         the proposed and executed actions:


                                                                                                                https://doi.org/10.3390/make8050125
```

---

## PDF Page 8

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                                  8 of 31




                                                                                      δt = ∆( at , ρ(dt )).

                                               A governance operator exhibits minimal intervention if, whenever feasible, it selects
                                         actions with minimal drift. In the projection-based repair definition above, minimal inter-
                                         vention is ensured by construction, provided ∆ is well-defined and the argmin is unique or
                                         a stable selection rule is used.
                                               In regulated domains, the objective is not to eliminate drift—because governance must
                                         correct inadmissible actions—but to ensure drift is bounded and predictable. This notion
                                         will later support the analysis of stability and robustness under perturbations, as well as
                                         the empirical evaluation of overhead and correction frequency.

                                         2.5. Audit Trace Semantics
                                              In regulated and safety-critical environments, constraint preservation alone is insuffi-
                                         cient to guarantee accountability. Beyond admissible decision execution, the system must
                                         provide a formally defined and verifiable trace of the decision transformation process. In
                                         the CAIS framework, this requirement is addressed through the definition of audit trace
                                         semantics, which explicitly encode the transformation from observation and proposed
                                         decision to executed action under governance constraints.
                                              Let st ∈ S denote the system state at time t, xt ∈ X the observation, dt ∈ D the pro-
                                         posed decision generated by the policy πθ , and at ∈ A the executed action obtained through
                                         the governance operator G. We define the audit trace mapping as a deterministic function

                                                                           Φ : S × X × D × A × C → Z,

                                         where C is the constraint specification space and Z is the space of structured audit records.
                                             For each decision step, the audit trace element is given by

                                                                                  z t = Φ ( s t , x t , d t , a t , C ).

                                              The audit trace zt must encode sufficient information to reconstruct the ndecision trans-
                                         formation. This includes the proposal dt , the constraint evaluation results gi (st , at )}ik=1 ,
                                         the governance mode (approval, repair, fallback), and identifiers of the model parameters θ
                                         and constraint specification C. Formally, we require that Φ is information-complete with
                                         respect to the governance transformation, in the sense that if

                                                                      Φ(st , xt , dt , at , C ) = Φ s′t , xt′ , d′t , a′t , C ′ ,
                                                                                                                               


                                         then the underlying decision transformations are semantically equivalent under the same
                                         model and constraint configuration. This condition supports that the audit trace uniquely
                                         characterizes the admissible action selection process.
                                              We further define trace consistency as the property that, for every recorded step,

                                                                                       a t = G ( d t , s t , C ),

                                         and that all hard constraints are satisfied,

                                                                                        gi (st , at ) ≤ 0∀i.

                                              Under trace consistency, the audit sequence
                                                                                 n
                                                                             ZT = Φ(st , xt , dt , at , C )}tT=0




                                                                                                                           https://doi.org/10.3390/make8050125
```

---

## PDF Page 9

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                  9 of 31



                                         constitutes a verifiable record of governance-compliant execution. The audit trace is
                                         therefore not merely a log, but a formal representation of the governance-induced deci-
                                         sion transformation.
                                              To ensure that audit traces support reproducibility, we additionally require trace
                                         determinism. The mapping Φ must depend exclusively on explicitly recorded system
                                         variables and controlled sources of randomness. Hidden stochastic processes, unlogged
                                         hyperparameters, or non-deterministic governance routines invalidate deterministic replay
                                         and undermine regulatory auditability.

                                         2.6. Replayability Conditions
                                              Reproducibility in CAIS is defined as the ability to reconstruct the complete decision
                                         trajectory of the system under identical initial conditions and configuration parameters.
                                         Let the system be initialized at state s0 , with model parameters θ, constraint specification C,
                                         and a controlled randomness configuration Ξ, which encapsulates all seeds and stochastic
                                         drivers in both the policy and environment.
                                              We define the replay operator

                                                                              Ψ : (s0 , θ, C, Ξ) → τT ,

                                         where τT = (st , dt , at )}tT=0 denotes the resulting trajectory over horizon T.
                                                    

                                             The system satisfies replayability if, for any two executions with identical inputs,

                                                                         Ψ(s0 , θ, C, Ξ) = Ψ′ (s0 , θ, C, Ξ),

                                         implying equality of the generated action sequence { at } and corresponding audit trace ZT .
                                         This definition assumes that the environment transition kernel is either deterministic or
                                         driven by controlled stochastic seeds included in Ξ.
                                               We distinguish between strong and weak replayability. Strong replayability requires
                                         exact equality of state and action trajectories. This is achievable when all components—
                                         including the governance operator G, constraint evaluation, and transition dynamics—
                                         are deterministic under fixed seeds. Weak replayability allows for bounded numerical
                                         deviations in continuous state spaces, provided that the sequence of executed actions and
                                         constraint satisfaction outcomes remains invariant.
                                               Replayability in CAIS is structurally dependent on three conditions: determinism of
                                         the governance operator G, completeness of the audit trace mapping Φ, and explicit control
                                         of all stochastic processes via Ξ. When these conditions hold, the tuple ( G, Φ, Ψ) defines a
                                         controlled and reproducible decision architecture.
                                               This triadic structure distinguishes CAIS from conventional AI systems in which
                                         governance is implemented as an external validation layer and trace logging is decoupled
                                         from decision semantics. In CAIS, governance, traceability, and replayability are not
                                         implementation artifacts but formal properties of the system definition.

                                         2.7. Multi-Agent Controlled Agentic AI Systems
                                               Many real-world regulated environments are inherently multi-agent. Autonomous
                                         vessels, distributed grid nodes, financial trading agents, and edge devices in federated
                                         learning ecosystems interact within shared state spaces and influence each other’s trajecto-
                                         ries. In such settings, governance must operate not only at the individual decision level but
                                         also at the system level to ensure global constraint preservation.
                                               Let there be N agents indexed by i ∈ {1, . . . , N }. Each agent i possesses a local
                                         observation xti ∈ X i , generates a proposed decision




                                                                                                           https://doi.org/10.3390/make8050125
```

---

## PDF Page 10

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                           10 of 31




                                                                                                
                                                                                    dit = πθi i xti ∈ D i ,

                                         and produces an executed action
                                                                                                        
                                                                                    ait = Gi dit , st , C ,

                                         where Gi is the local governance operator for agent i, and st ∈ S denotes the global
                                         system state.
                                              The joint action vector is
                                                                                      
                                                                 at = a1t , . . . , atN ∈ A1 × · · · × A N = A.

                                              The system evolves according to a joint transition function

                                                                                    s t +1 ∼ T ( s t , at , ξ t ),

                                         which captures interaction effects among agents.
                                             Local and Global Constraints
                                             In multi-agent environments, constraints may be:
                                         1.   Local, affecting individual agent actions independently.
                                         2.   Coupled, constraining combinations of actions across agents.
                                              We define the admissible joint action set as

                                                                                         A C ( s t ) ⊆ A,

                                         where
                                                                   AC (st ) = {a ∈ A | gk (st , a) ≤ 0, ∀k}.

                                              Coupled constraints are common in collision avoidance, resource allocation, and
                                         distributed energy balancing, where admissibility depends on relative configurations
                                         rather than independent agent actions.
                                              Global Governance Operator
                                              To enforce global admissibility, we introduce a global governance operator

                                                                   Gglobal : D 1 × · · · × D N × S × C → A.

                                              The executed joint action is
                                                                                                             
                                                                       at = Gglobal d1t , . . . , dtN , st , C .

                                              The operator must satisfy:
                                                                                         at ∈ A C ( s t ).

                                            Two structural realizations are possible.
                                            In a decentralized CAIS, each agent applies a local governance operator Gi , and global
                                         admissibility is guaranteed if

                                                                              N
                                                                             ∏ Gi (dit , st , C) ∈ AC (st ).
                                                                             i =1




                                                                                                                     https://doi.org/10.3390/make8050125
```

---

## PDF Page 11

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                       11 of 31



                                            In a centralized CAIS, local proposals are collected and jointly projected into the
                                         admissible joint action space:

                                                                         at = arg       min       ∆(a, ρ(dt )),
                                                                                     a∈AC (st )


                                         where ρ maps proposals to joint action space and ∆ is a joint deviation metric.
                                              The centralized projection enables global constraint preservation even when individual
                                         local projections would violate coupled constraints.
                                              Multi-Agent Audit Trace
                                              The audit trace mapping generalizes naturally:

                                                                 Φmulti : S × D 1 × · · · × D N × A × C → Z .

                                              For each time step,
                                                                            zt = Φmulti (st , dt , at , C ).

                                              The trace must encode:
                                         1.   all proposals dit ;
                                         2.   constraint evaluations on joint action;
                                         3.   the applied governance mode;
                                         4.   any inter-agent correction applied.
                                              Replayability conditions extend analogously, requiring deterministic global projection
                                         and controlled stochasticity.
                                              This formalization establishes that CAIS extends naturally to interacting agent pop-
                                         ulations and provides a principled mechanism for enforcing coupled safety constraints
                                         without sacrificing architectural clarity.

                                         2.8. Bounded Decision Drift Induced by Governance
                                              We now analyze the extent to which embedding governance into the decision pipeline
                                         perturbs system dynamics. This directly supports the central hypothesis that governance
                                         reduces inadmissible states without inducing destabilizing effects.
                                              Let the proposed decision at time t be dt , and let the executed action be

                                                                                 a t = G ( d t , s t , C ).

                                              We define decision drift as
                                                                                δt = ∆( at , ρ(dt )),

                                         where ∆ is a metric on the action space and ρ maps proposals to executable actions
                                         when necessary.
                                             Projection-Based Governance
                                             Assume that G is defined as a projection onto the feasible set:

                                                                    G (dt , st , C ) = arg     min        ∆( a, ρ(dt )).
                                                                                             a∈AC (st )


                                              If AC (st ) is non-empty, closed, and convex, and if ∆ is induced by a norm, then the
                                         projection operator is non-expansive:

                                                             ∥ G (d1 , s, C ) − G (d2 , s, C ) ∥ ≤ ∥ ρ(d1 ) − ρ(d2 ) ∥ .

                                              This implies that governance does not amplify perturbations in the proposal space.
                                              Bounded Drift Theorem



                                                                                                                 https://doi.org/10.3390/make8050125
```

---

## PDF Page 12

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                     12 of 31



                                              Assume:
                                         1.   The feasible set AC (st ) is non-empty and compact.
                                         2.   The proposal mapping ρ ◦ πθ is Lipschitz continuous with constant Lπ .
                                         3.   The projection operator G is non-expansive.
                                              Then for any perturbation ϵ in observation space,

                                                                        ∥ at − a′t ∥ ≤ Lπ ∥ xt − xt′ ∥ .

                                              Moreover, for infeasible proposals,

                                                                          δt ≤ dist (ρ(dt ), AC (st )),

                                         which is bounded by the diameter of the action space.
                                             Stability Implication
                                             Consider a deterministic transition function

                                                                                s t +1 = f ( s t , a t ).

                                              If f is Lipschitz continuous in at with constant L f , then the governance-induced
                                         perturbation in state transition satisfies

                                                                                    ungoverned
                                                                       ∥ s t +1 − s t +1             ∥ ≤ L f δt .

                                              Hence, as long as drift is bounded and the system dynamics are stable under bounded
                                         input perturbations, embedding governance into the decision pipeline does not introduce
                                         unbounded divergence.
                                              Interpretation Relative to H1
                                              The bounded decision drift result establishes that governance projection reduces
                                         infeasible actions while preserving Lipschitz continuity of the overall decision process.
                                         Therefore, governance acts as a constraint-preserving, non-expansive transformation rather
                                         than a destabilizing correction layer.
                                              This formally supports the research hypothesis that embedding a deterministic
                                         governance operator reduces inadmissible system states without inducing destabiliz-
                                         ing dynamics.

                                         2.9. Governance-Induced Drift in Federated Multi-Agent Learning
                                               In federated agentic systems, model parameters are not fixed but evolve over dis-
                                         tributed training rounds. Governance is therefore applied to decisions generated by locally
                                         trained models whose parameters are periodically aggregated. It is necessary to analyze
                                         whether embedding a governance operator G interferes with convergence properties of
                                         federated optimization or amplifies parameter-induced decision instability.
                                               Federated Setting
                                               Consider N agents participating in federated training. Each agent i maintains local
                                         parameters θir at round r. During a training round, each agent performs local updates on
                                         its private dataset Di , yielding

                                                                            θir+1 = θir − η ∇ℓi (θir ),

                                         where ℓi is the local loss function and η is the learning rate.
                                             After local updates, a global aggregation operator A produces updated global parameters:
                                                                                                        
                                                                         θ r+1 = A θ1r+1 , . . . , θ rN+1 .


                                                                                                               https://doi.org/10.3390/make8050125
```

---

## PDF Page 13

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                                        13 of 31



                                              In standard FedAvg,
                                                                                                  N
                                                                                      θ r+1 = ∑ wi θir+1 ,
                                                                                                 i =1

                                         with weights wi ≥ 0, ∑ i wi = 1.
                                             The decision model used at inference time is πθr+1 , and governance is applied post-inference:

                                                                                a t = G ( π θ r +1 ( x t ) , s t , C ) .

                                             Decision Sensitivity to Parameter Perturbations
                                             Let us define decision sensitivity with respect to model parameters. Assume the
                                         proposal mapping ρ ◦ πθ is Lipschitz continuous in parameters:
                                                                                             
                                                                 ∥ ρ π θ1 ( x ) − ρ π θ2 ( x ) ∥ ≤ L θ ∥ θ 1 − θ 2 ∥ .

                                              This is a standard smoothness assumption for neural networks under bounded inputs.
                                              Without governance, parameter perturbations directly translate into action perturbations:

                                                           (1)    (2)
                                                       ∥ at − at        ∥ = ∥ ρ(πθ1 ( xt )) − ρ(πθ2 ( xt )) ∥ ≤ Lθ ∥ θ1 − θ2 ∥ .

                                              With governance projection, executed actions are

                                                                               (k)
                                                                              at     = G (ρ(πθk ( xt )), st , C ).

                                              If G is non-expansive with respect to its action argument, then

                                                                      (1)     (2)
                                                                 ∥ at − at           ∥ ≤ ∥ ρ(πθ1 ( xt )) − ρ(πθ2 ( xt )) ∥ .

                                              Combining the inequalities yields

                                                                               (1)       (2)
                                                                            ∥ at − at          ∥ ≤ L θ ∥ θ1 − θ2 ∥ .

                                              Thus, governance does not increase sensitivity of actions to parameter perturbations.
                                              Governance and Federated Convergence
                                              Let θ ⋆ denote the optimal federated solution under standard assumptions of convex-
                                         ity or smooth non-convex optimization. The presence of governance does not alter the
                                         optimization objective during training if governance is applied only at inference time.
                                              However, in safety-critical federated systems, governance may also constrain local
                                                                                                                                                  ∼
                                         training by rejecting unsafe exploratory actions or filtering data samples. Let ℓ i denote the
                                         effective loss under governance-constrained data:
                                                                  ∼                    h                             i
                                                                   ℓ i (θ ) = E(x,y)∼Di ℓ(θ; x, y) · 1admissible(x,y) .

                                              Provided that admissibility filtering preserves bounded gradients and Lipschitz con-
                                         tinuity, standard federated convergence enables extend with modified constants. The
                                         aggregation operator remains contractive under typical assumptions of bounded gradi-
                                         ent variance.
                                              Federated Drift Decomposition
                                              We decompose total action deviation between rounds into two components:

                                               ∥ art +1 − art ∥ ≤ ∥ G (ρ(πθ r+1 ( xt ))) − G (ρ(πθ r ( xt ))) ∥ +                          δt             .
                                                                  |                    {z                     }                           |{z}
                                                                              parameter−induced drift                           constraint projection drift




                                                                                                                           https://doi.org/10.3390/make8050125
```

---

## PDF Page 14

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                 14 of 31



                                             The first term is bounded by parameter smoothness and aggregation stability. The second
                                         term is bounded by the distance from proposal to feasible set, as previously established:

                                                                       δt ≤ dist (ρ(πθ r ( xt )), AC (st )).

                                              Thus, total drift is bounded by a sum of:
                                         1.   Federated parameter deviation.
                                         2.   Governance projection correction.
                                             Since governance is non-expansive and projection-based, it does not amplify
                                         parameter-induced variation. Instead, it may reduce action variance by projecting multiple
                                         nearby proposals into the same admissible region.
                                             Stability Implication in Federated CAIS
                                             Consider the closed-loop system

                                                                               s t +1 = f ( s t , a t ).

                                              Under Lipschitz continuity of f , bounded parameter drift and bounded projection
                                         drift imply bounded state deviation between consecutive rounds. Therefore, federated
                                         updates do not induce destabilizing oscillations through governance projection.
                                              Moreover, governance may improve robustness in federated settings by mitigating
                                         the effect of poisoned or adversarial shifted local models. If a malicious client produces
                                         parameter updates leading to infeasible or unsafe proposals, the governance projection
                                         restricts execution to admissible actions, preventing unbounded divergence at the system
                                         level even if parameter space temporarily deviates.
                                              Implication for the Research Hypothesis
                                              The federated extension confirms that embedding governance as a projection oper-
                                         ator does not degrade convergence properties under standard smoothness assumptions.
                                         Instead, governance acts as a stabilizing transformation that promotes admissibility while
                                         preserving Lipschitz continuity of the decision mapping.
                                              This strengthens the central hypothesis that deterministic governance reduces inad-
                                         missible states without introducing destabilizing effects, even in distributed federated
                                         multi-agent environments.

                                         3. Experimental Design
                                               This section specifies the experimental protocol used to empirically evaluate CAIS.
                                         The design is constructed to test the central hypothesis that embedding a deterministic
                                         governance operator within the decision pipeline reduces inadmissible system states with-
                                         out inducing destabilizing effects on agentic dynamics. The experiments are defined to be
                                         reproducible by construction, with all stochastic components controlled via explicit seeds
                                         and trace-based provenance.
                                               To ensure full transparency and independent verification, the complete experimental
                                         framework—including source code, configuration files, and generated results—has been
                                         made publicly available in an open repository (https://github.com/TyMill/CAIS-pub,
                                         access date: 19 March 2026). The repository contains the full implementation of the CAIS
                                         architecture, experiment runners, statistical evaluation modules, and all artifacts required
                                         to reproduce the reported results.
                                               A versioned snapshot of the repository corresponding to the experiments reported in
                                         this study was created at the time of submission (version v0.1) and archived on Zenodo
                                         (19 March 2026) with a persistent DOI (10.5281/zenodo.19110441). This snapshot includes
                                         the exact experimental configuration, fixed random seeds, and output artifacts used to



                                                                                                           https://doi.org/10.3390/make8050125
```

---

## PDF Page 15

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                              15 of 31



                                         generate all reported results. As such, the experiments can be reproduced under identical
                                         conditions, ensuring full traceability and long-term verifiability of the findings.

                                         3.1. Experimental Objectives and Hypotheses
                                              The experimental program operationalizes two core claims. The first claim concerns
                                         compliance: governance projection should reduce the frequency and severity of constraint
                                         violations. The second claim concerns stability: the correction introduced by governance
                                         should remain bounded and should not amplify perturbations or induce unstable closed-
                                         loop dynamics.
                                              Accordingly, we evaluate the following testable hypothesis.

                                         H1 (Governance compliance–stability hypothesis). Embedding a deterministic governance
                                         operator G into the decision pipeline decreases the probability of inadmissible executed actions
                                         and reduces the incidence of unsafe system states, while maintaining bounded decision drift and
                                         preserving stable system dynamics under perturbations.

                                              In addition to H1, we evaluate the federated extension implied by the theoreti-
                                         cal analysis.

                                         H2 (Federated stability hypothesis). In federated multi-agent training, governance projection
                                         does not amplify action variance across rounds and does not degrade convergence stability; under
                                         adversarial or heterogeneous clients, governance reduces executed-action instability by projecting
                                         proposals into admissible action sets.

                                               The two hypotheses are complementary and jointly address the central research
                                         question of this study: whether governance can ensure both safety and stability in AI
                                         decision systems. H1 evaluates constraint compliance and bounded intervention at the level
                                         of individual decision execution, while H2 extends this analysis to distributed and federated
                                         settings, assessing whether governance preserves stability under parameter variability and
                                         decentralized learning dynamics. Together, they provide a unified evaluation of governance
                                         across centralized and distributed architectures.

                                         3.2. Environments, State Representation, and Sensorization
                                              Experiments are conducted in a discrete-time, agent-based simulation environment
                                         with global state st ∈ S . The environment supports multi-agent interaction and coupled
                                         constraints. While the motivating application domain is maritime autonomy, the environ-
                                         ment is defined abstractly to maintain generality, with maritime-specific instantiations used
                                         as controlled case studies.
                                              The global state st includes agent kinematics and interaction context and is used to
                                         evaluate constraints and compute admissible sets AC (st ). Each agent i receives an observa-
                                         tion xti = Ωi st , ηti , potentially corrupted by sensing noise. To avoid conflating governance
                                                               

                                         effects with perception failures, the baseline experiments use structured observations with
                                         controlled noise distributions; extended experiments introduce sensor corruption regimes
                                         representative of harsh operating conditions.
                                              The simulation is initialized from a distribution over initial conditions s0 ∼ P0 de-
                                         signed to produce a mixture of nominal and high-risk encounters, thereby ensuring that
                                         constraint violations are plausible under ungoverned execution.

                                         3.3. Decision Models and Training Regimes
                                              Each agent employs a policy πθi producing proposals dit ∈ D i . To isolate architectural
                                                                             i
                                         effects, we consider two model families.



                                                                                                        https://doi.org/10.3390/make8050125
```

---

## PDF Page 16

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                               16 of 31



                                              In the first family, policies are supervised models trained to imitate admissible actions
                                         under nominal conditions. This setting provides a controlled baseline where constraint
                                         violations occur primarily under distribution shift and noise.
                                              In the second family, policies are learned through reinforcement learning, where explo-
                                         ration can generate inadmissible proposals. This setting is used to stress-test governance
                                         under aggressive policy outputs and to evaluate whether governance induces destabilizing
                                         oscillations in closed-loop dynamics.
                                              In federated experiments, each agent trains locally using its private data or experience
                                         buffer and participates in periodic aggregation rounds. The aggregation schedule and com-
                                         munication delays are explicitly parameterized to emulate realistic distributed conditions.
                                         Model updates are aggregated using FedAvg as the baseline, with an optional proximal
                                         variant to improve stability under heterogeneity.

                                         3.4. Governance Operator Configurations
                                               Governance is applied as an intrinsic stage in the decision pipeline. We evaluate
                                         three governance configurations, each corresponding to a distinct interpretation of G and
                                         enabling a systematic ablation study.
                                               The first configuration is the ungoverned baseline, in which proposed decisions are
                                         executed directly: at = ρ(dt ). This setting establishes the raw violation rate and stability
                                         characteristics of the policy without any constraint enforcement.
                                               The second configuration is approval-only gating, in which admissible proposals are
                                         executed unchanged but inadmissible proposals trigger a conservative fallback a⋆ . This
                                         setting isolates the effect of rejection-based governance without optimization-based repair.
                                               The third configuration is projection-based repair, in which inadmissible proposals are
                                         transformed into admissible actions via a minimal-intervention projection onto AC (st ). This
                                         setting corresponds to the formal CAIS definition and represents the target architecture.
                                               In multi-agent scenarios, we evaluate both decentralized governance, where each
                                         agent applies a local operator Gi , and centralized governance, where a global operator
                                         Gglobal projects joint proposals into the admissible joint action space. This allows direct
                                         measurement of the impact of coupled constraints and inter-agent correction.

                                         3.5. Constraints and Admissibility Regimes
                                              Constraint specifications C are defined as a mix of hard and soft constraints. Hard
                                         constraints define the feasible action sets AC (st ), while soft constraints encode preferences
                                         among feasible actions and serve as secondary objectives in the repair operator.
                                              Hard constraints include collision avoidance, exclusion zones, and actuator bounds.
                                         Coupled constraints include separation constraints and shared-resource constraints. Soft
                                         constraints include smoothness penalties and conservative maneuver preferences intended
                                         to minimize unnecessary corrections.
                                              To evaluate generalization across regulatory complexity, experiments are conducted
                                         under progressively richer constraint sets. This enables a sensitivity analysis of governance
                                         performance as the feasible set becomes smaller or more fragmented.

                                         3.6. Metrics: Compliance, Drift, Stability, and Convergence
                                              We measure outcomes at both the decision level and the trajectory level.
                                              Compliance is quantified as the empirical violation rate, defined as the fraction of
                                         time steps in which executed actions violate at least one hard constraint. In addition, we
                                         record the distribution of violation severity, measured by the magnitude of constraint
                                         residuals maxi gi (st , at ). For coupled constraints, violations are evaluated on the joint action
                                         at (Table 1).




                                                                                                         https://doi.org/10.3390/make8050125
```

---

## PDF Page 17

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                 17 of 31



                                         Table 1. Definition of evaluation metrics used in the study.

                                                   Metric                     Formal Definition                      Interpretation
                                                                        Fraction of time steps where
                                               Violation rate          executed action violates at least         Measures compliance
                                                                               one constraint
                                                 Mean drift                       E[∆( at , dt )]             Measures intervention cost
                                                                           Upper quantiles of drift                Captures extreme
                                              Drift quantiles
                                                                               distribution                          corrections
                                                                        Variance of executed actions
                                              Action variance                                                      Measures stability
                                                                         across runs or FL rounds
                                                                         Evolution of model norm or                Measures learning
                                               Convergence
                                                                               validation loss                        dynamics
                                                                        Time required for decision             Measures computational
                                                  Latency
                                                                      execution (model + governance)                 overhead


                                               Decision drift is quantified as δt = ∆( at , ρ(dt )), capturing the minimal-intervention
                                         cost imposed by governance. We evaluate mean drift, tail drift quantiles, and drift autocor-
                                         relation to detect oscillatory corrections.
                                               Closed-loop stability is assessed through trajectory-level metrics. We measure diver-
                                         gence between governed and ungoverned trajectories under matched initial conditions
                                         and identical stochastic seeds. In addition, we measure encounter safety outcomes such
                                         as collision rate and deadlock frequency in multi-agent interaction regimes. Stability un-
                                         der perturbation is assessed by applying controlled noise to observations and evaluating
                                         whether the resulting trajectory deviation remains bounded.
                                               In federated experiments, convergence is evaluated using standard learning metrics,
                                         including validation loss and policy performance, but the primary focus is action-level
                                         stability across rounds. We measure cross-round action variance at fixed benchmark states,
                                         and we quantify whether governance reduces the variance induced by parameter updates.
                                         Communication cost is recorded to contextualize stability outcomes.
                                               Finally, computational overhead is measured as end-to-end decision latency, separat-
                                         ing the inference time of πθ from the evaluation and repair time of G. This is crucial for
                                         high-frequency control regimes.

                                         3.7. Adversarial and Distribution-Shift Stress Tests
                                              To test robustness, we introduce two stress regimes.
                                              The first regime injects adversarial perturbations into observations, representing sens-
                                         ing corruption and spoofing. Perturbations are parameterized by strength and frequency,
                                         and are applied under controlled seeds.
                                              The second regime introduces federated poisoning by simulating a subset of malicious
                                         clients that submit biased local updates designed to increase constraint violations. This
                                         tests the claim that governance projection limits executed-action instability even when
                                         parameter space deviates due to adversarial updates.

                                         3.8. Reproducibility Protocol and Trace-Based Provenance
                                              All experiments are executed under explicit reproducibility controls. Each run records
                                         the complete configuration tuple (s0 , θ, C, Ξ) and generates an audit trace sequence ZT
                                         under the trace semantics Φ. The trace includes model version identifiers, constraint
                                         specification versions, seeds, and governance modes. A run is considered replayable if
                                         the sequence of executed actions and constraint satisfaction outcomes are identical under



                                                                                                           https://doi.org/10.3390/make8050125
```

---

## PDF Page 18

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                 18 of 31



                                         re-execution with the recorded configuration. Weak replayability is evaluated by verifying
                                         invariance of decision sequences and bounded numerical deviation of continuous states.
                                              This protocol supports that the reported results can be independently reproduced
                                         and audited, and that any observed differences between governed and ungoverned sys-
                                         tems are attributable to governance projection rather than uncontrolled randomness or
                                         implementation artifacts.

                                         3.9. Implementation Details and Reproducibility Configuration
                                             This section specifies the implementation-level configuration of the experimental
                                         framework to ensure transparency, auditability, and reproducibility in accordance with the
                                         CAIS formalism.

                                         3.9.1. Software Architecture and Determinism
                                              The experimental framework is implemented in Python 3.11 using a modular ar-
                                         chitecture consistent with the formal CAIS definition. The decision pipeline is explicitly
                                         structured as:
                                                                      xt → πθ → dt → G → at → T .

                                              The governance operator G is implemented as a deterministic projection module. All
                                         constraint evaluations are pure functions of (st , a), and no hidden stochastic elements are
                                         permitted inside the governance layer. Repair-based governance uses convex optimization
                                         solvers where applicable; in non-convex cases, deterministic tie-breaking and fixed solver
                                         seeds are enforced.
                                              All randomness in the system—including model initialization, data shuffling, envi-
                                         ronment noise, and adversarial perturbations—is controlled through a centralized seed
                                         registry Ξ. Seeds are logged as part of the audit trace and injected explicitly into:
                                         1.   NumPy (v2.4.0) random generators,
                                         2.   PyTorch (v2.10.0)/TensorFlow (v2.16.1) backends (where applicable),
                                         3.   environment transition noise,
                                         4.   adversarial perturbation modules.
                                              Floating-point determinism is enforced using fixed precision and deterministic back-
                                         end flags when supported. While bitwise determinism cannot always be guaranteed across
                                         hardware platforms, weak replayability is ensured via bounded tolerance thresholds.

                                         3.9.2. Simulation Environment
                                              The simulation operates in discrete time with fixed time step ∆t. The transition function

                                                                                s t +1 = f ( s t , a t )

                                         is implemented as a deterministic kinematic update with optional bounded disturbance
                                         term ξ t drawn from a controlled seed.
                                              For multi-agent scenarios, the joint state includes all agent positions, velocities, and
                                         interaction variables. Collision detection and separation constraints are computed using
                                         deterministic geometric routines.
                                              Initial states s0 are sampled from predefined distributions with fixed seeds. Each
                                         experiment consists of multiple runs across a grid of initial conditions to ensure statisti-
                                         cal validity.

                                         3.9.3. Policy Models
                                              Two policy families are implemented.




                                                                                                           https://doi.org/10.3390/make8050125
```

---

## PDF Page 19

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                  19 of 31



                                              In supervised experiments, policies are multi-layer feedforward networks with ReLU
                                         activations. Network depth and width are fixed across experiments to isolate governance
                                         effects. Model parameters are initialized with fixed seeds and trained using Adam with
                                         deterministic update order.
                                              In reinforcement learning experiments, policies are trained using a stable actor–critic
                                         architecture. Exploration noise is generated using seed-controlled Gaussian processes.
                                         During evaluation, exploration noise is disabled to ensure that executed proposals are
                                         deterministic functions of xt .
                                              In federated experiments, each agent trains locally for E epochs per round. Gradients
                                         are clipped to ensure bounded updates. Aggregation is implemented using weighted
                                         averaging with explicit logging of client weights and update norms.

                                         3.9.4. Governance Operator Implementation
                                              The governance operator G supports three execution modes corresponding to the
                                         experimental configurations.
                                              In approval-only mode, admissibility is evaluated and infeasible proposals are
                                         replaced by a predefined safe fallback action a⋆ (st , C ). This fallback is deterministic
                                         and state-dependent.
                                              In projection-based repair mode, infeasible proposals are mapped to the feasible set
                                         via constrained optimization:

                                                                      at = arg     min        ∥ a − ρ(dt ) ∥22 .
                                                                                 a∈AC (st )


                                              For convex feasible sets, closed-form projections are used where possible. For general
                                         constraint sets, a deterministic quadratic programming solver is applied with fixed solver
                                         tolerances and seeds.
                                              Constraint evaluation routines are vectorized and benchmarked independently to
                                         ensure that governance latency remains within acceptable bounds relative to model infer-
                                         ence time.

                                         3.9.5. Federated Training Configuration
                                              Federated experiments simulate communication rounds with synchronous aggrega-
                                         tion unless otherwise specified. Each round consists of:
                                         1.   Local training on private datasets.
                                         2.   Gradient clipping and optional differential privacy noise (seed-controlled).
                                         3.   Transmission of model updates.
                                         4.   Global aggregation.
                                              To isolate governance effects from federated instability, baseline convergence curves
                                         are computed without governance. Governance is then activated during inference-only
                                         evaluation to measure executed-action stability.
                                              In adversarial experiments, a subset of clients is designated as malicious. These
                                         clients apply gradient perturbations or label-flipping strategies during local training. The
                                         proportion of adversarial clients is parameterized and logged.

                                         3.9.6. Audit Trace Storage and Verification
                                              For each decision step, the audit mapping

                                                                           zt = Φ(st , xt , dt , at , C )




                                                                                                            https://doi.org/10.3390/make8050125
```

---

## PDF Page 20

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                           20 of 31



                                         is serialized as structured JSON with cryptographic hash chaining between consecu-
                                         tive records:
                                                                         ht = Hash(zt ∥ ht−1 ).

                                              This produces a tamper-evident audit chain.
                                              Each experiment produces:
                                         1.   full decision trajectory τT ;
                                         2.   audit trace sequence ZT ;
                                         3.   configuration metadata including model version, constraint version, seed registry,
                                              and solver parameters.
                                              Replay validation is performed by re-executing the experiment using recorded meta-
                                         data and verifying equality of executed actions at and constraint satisfaction outcomes.
                                         For weak replayability, numerical deviations in continuous states are compared against
                                         tolerance ϵ.

                                         3.9.7. Hardware and Runtime Configuration
                                              Experiments are executed on a controlled computing environment with fixed
                                         CPU/GPU configuration. For neural models, GPU acceleration is enabled with deter-
                                         ministic backend flags. All runtime libraries and dependency versions are recorded via an
                                         environment snapshot.
                                              Latency measurements are performed using high-resolution timers. Governance
                                         latency is reported separately from model inference latency to isolate architectural overhead.

                                         3.9.8. Reproducibility Guarantee
                                              An experiment is considered reproducible if the following conditions are satisfied:
                                         1.   Identical configuration tuple (s0 , θ, C, Ξ).
                                              Identical executed action sequence at }tT=0 .
                                                                                     
                                         2.
                                         3.   Identical hard-constraint satisfaction outcomes.
                                         4.   Consistent audit hash chain {ht }.
                                              All experiments reported in this study satisfy at least weak replayability; strong
                                         replayability is achieved in deterministic settings without stochastic disturbance.

                                         4. Results
                                               This section presents the empirical evaluation of CAIS under the experimental pro-
                                         tocol defined in Section 3. The results are structured to directly assess the governance
                                         compliance–stability hypothesis (H1) by analyzing constraint violations, decision drift, and
                                         their interaction.
                                               Although the CAIS formulation assumes constraint-preserving behavior in the ide-
                                         alized setting, practical implementations operate under approximation and solver limita-
                                         tions; therefore, results should be interpreted in terms of violation reduction rather than
                                         strict feasibility.

                                         4.1. Constraint Compliance
                                              The empirical violation rate exhibits a clear and statistically significant separation
                                         between governance configurations (Figure 2).
                                              The ungoverned baseline produces a violation rate of 1.0 with zero variance, indi-
                                         cating that constraint violations occur at every time step under unconstrained execution.
                                         Approval-based gating achieves near-perfect compliance, reducing the violation rate to
                                         0.033 (95% CI: [0.000, 0.100]).




                                                                                                     https://doi.org/10.3390/make8050125
```

---

## PDF Page 21

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                  21 of 31




                                         Figure 2. Comparison of constraint violation rates across governance configurations. Projection-based
                                         governance significantly reduces violation rates relative to the ungoverned baseline, but does not
                                         achieve the near-complete compliance observed under approval-based gating.

                                              Projection-based governance reduces the violation rate to 0.832 (95% CI: [0.815, 0.847]);
                                         however, a non-negligible level of residual violations remains due to approximation effects
                                         and constraint complexity, indicating that strict feasibility is not achieved in practice.
                                              Statistical analysis using the Mann–Whitney U test confirms that all pairwise differ-
                                         ences between governance modes are highly significant (p < 10−10 ), with large effect sizes
                                         (|Cliff’s δ| > 0.93). These results establish that governance materially alters the safety
                                         properties of the system (Tables 2 and 3).

                                         Table 2. Violation rate summary statistics across governance modes.

                                              Mode               n             Mean               Std             ci95_lo         ci95_hi
                                          gate_fallback         30             0.0333            0.1826           0.0000           0.1000
                                              none              30             1.0000            0.0000           1.0000           1.0000
                                            project             30             0.8317            0.0465           0.8150           0.8472

                                         Table 3. Pairwise Mann–Whitney U tests for violation rate.

                                             Group_a              Group_b               u_Stat              p_Value          Cliffs_Delta
                                           gate_fallback              none               15               1.165 × 10−13         −0.9667
                                           gate_fallback             project             30               4.483 × 10−11         −0.9333
                                               none                  project             900              1.187 × 10−12            1

                                         4.2. Decision Drift
                                              Decision drift analysis reveals the cost of governance intervention and its dependence
                                         on the selected control strategy (Figure 3).


                                                                                                            https://doi.org/10.3390/make8050125
```

---

## PDF Page 22

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                  22 of 31




                                         Figure 3. Decision drift across governance modes.

                                              The ungoverned baseline yields zero drift, as no modification is applied to policy
                                         outputs. In contrast, both governance mechanisms introduce substantial intervention.
                                              Approval-based gating produces a mean drift of 10.37 (95% CI: [9.34, 11.37]), reflecting
                                         the discrete replacement of inadmissible actions with fallback controls. Projection-based
                                         governance yields a higher mean drift of 12.74 (95% CI: [11.61, 13.77]), indicating that
                                         continuous correction of infeasible proposals can lead to larger cumulative deviations
                                         (Table 4).

                                         Table 4. Decision drift summary statistics across governance modes.

                                             Mode               n             Mean                Std             ci95_lo         ci95_hi
                                          gate_fallback         30            10.3659            2.7783           9.3446          11.3662
                                              none              30             0.0000            0.0000           0.0000          0.0000
                                            project             30            12.7434            3.0639          11.6141          13.7731


                                              All pairwise differences are statistically significant (p < 0.01). The difference between
                                         projection and gating is moderate but consistent (p ≈ 0.005, Cliff’s δ ≈ −0.42), indicating
                                         that projection induces systematically greater intervention (Table 5).

                                         Table 5. Pairwise Mann–Whitney U tests for decision drift.

                                             Group_a             Group_b                u_Stat              p_Value          Cliffs_Delta
                                           gate_fallback             none                900              1.212 × 10−12            1
                                           gate_fallback            project              260                 0.005084           −0.4222
                                               none                 project               0               1.212 × 10−12           −1




                                                                                                            https://doi.org/10.3390/make8050125
```

---

## PDF Page 23

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                            23 of 31



                                              This result highlights a structural distinction between governance mechanisms: gating
                                         concentrates intervention into discrete events, whereas projection distributes intervention
                                         across time steps through continuous correction.

                                         4.3. Behavioural Differences Between Governance Strategies
                                               The joint analysis of compliance and drift reveals a fundamental trade-off between
                                         safety and intervention cost.
                                               Approval-based gating achieves near-complete elimination of violations at the expense
                                         of large, discrete deviations from the policy output. Projection-based governance provides a
                                         smoother control mechanism, reducing violations relative to the baseline while preserving
                                         continuity of actions, but at the cost of incomplete constraint enforcement and higher
                                         cumulative drift.
                                               These results define a Pareto frontier between safety and intervention, where dif-
                                         ferent governance strategies occupy distinct operating points. The ungoverned baseline
                                         minimizes intervention but is entirely unsafe, while gating maximizes safety with ag-
                                         gressive intervention, and projection offers an intermediate regime balancing safety and
                                         control smoothness.

                                         4.4. Implications for Governance Design
                                               The results confirm that embedding a deterministic governance operator fundamen-
                                         tally reshapes the behavior of agentic systems.
                                               First, governance significantly reduces the probability of inadmissible executed actions,
                                         validating the compliance component of H1. Second, governance introduces bounded
                                         intervention, as evidenced by stable drift distributions and the absence of divergence or
                                         oscillatory behavior in the evaluated trajectories.
                                               Importantly, projection-based governance does not guarantee strict feasibility in all
                                         cases, highlighting the practical limitations of optimization-based repair under complex
                                         and coupled constraints. This suggests that, in safety-critical applications, hybrid strate-
                                         gies combining projection with fallback mechanisms may be required to achieve both
                                         smoothness and strict compliance.

                                         4.5. Summary of H1
                                              Taken together, the results provide strong empirical support for the governance
                                         compliance–stability hypothesis.
                                              Governance operators reduce constraint violations by a statistically significant margin
                                         while introducing controlled and bounded intervention. No evidence of destabilizing
                                         dynamics or unbounded drift is observed. Instead, governance induces a structured trade-
                                         off between safety and intervention cost, consistent with the theoretical characterization of
                                         the operator G.

                                         4.6. Federated Stability and Action Consistency
                                              To evaluate the federated extension of the governance framework (H2), we analyze
                                         convergence dynamics, action variance across rounds, and safety properties under dis-
                                         tributed training (Figure 4).
                                              The evolution of the global model norm across communication rounds exhibits stable
                                         convergence. The norm decreases from 0.341 in the initial round to approximately 0.011
                                         after 20 rounds, with no evidence of divergence or high-amplitude oscillations. This
                                         indicates that the inclusion of governance in the decision pipeline does not destabilize
                                         federated optimization.




                                                                                                      https://doi.org/10.3390/make8050125
```

---

## PDF Page 24

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                24 of 31




                                         Figure 4. Federated convergence across communication rounds.

                                              At convergence, action-level stability is quantified using benchmark states. The mean
                                         action variance across rounds is 0.0123, indicating low variability in executed actions
                                         despite ongoing parameter updates. This confirms that governance projection stabilizes the
                                         action space even when the underlying model parameters evolve during training (Table 6).

                                         Table 6. Federated benchmark stability metrics at convergence.

                                                             Metric                                             Value
                                                      violations_on_bench                                         0.0
                                                        action_var_mean                                        0.01230
                                                           mean_drift                                          0.03323


                                               Importantly, no constraint violations are observed on the benchmark set, demon-
                                         strating that governance preserves safety under federated learning conditions. The mean
                                         decision drift at convergence is 0.033, indicating that only minimal intervention is required
                                         once the system stabilizes.
                                               These results support the federated stability hypothesis (H2). Governance projection
                                         does not amplify action variance across rounds and does not degrade convergence. Instead,
                                         it induces a stabilizing effect on executed actions, effectively decoupling parameter-space
                                         variability from behavior-space stability.

                                         5. Discussion
                                              The primary contribution of this work lies in redefining governance as an intrinsic
                                         architectural component of AI decision systems. Unlike prior approaches that enforce
                                         safety through training constraints or external filtering mechanisms, the CAIS framework
                                         embeds governance directly within the decision transformation. This enables unified
                                         reasoning about compliance, stability, auditability, and reproducibility within a single
                                         formal structure. As a result, governance is not treated as an auxiliary mechanism, but as a
                                         fundamental property of system execution. This study is based on controlled simulation


                                                                                                          https://doi.org/10.3390/make8050125
```

---

## PDF Page 25

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                             25 of 31



                                         experiments; therefore, the findings should be interpreted as validation under synthetic
                                         but reproducible conditions.

                                         5.1. Governance as a Structural Control Layer
                                               A central finding of this work is that governance acts as a control layer that reshapes
                                         the mapping from policy outputs to executed actions. Rather than treating constraint
                                         enforcement as an external correction mechanism, the CAIS architecture integrates gov-
                                         ernance directly into the decision pipeline, thereby redefining the effective behavior of
                                         the system.
                                               This integration yields two key properties. First, governance promotes admissibility at
                                         the level of executed actions, ensuring that constraint violations are significantly reduced,
                                         although not fully eliminated in all practical settings. Second, governance introduces
                                         a bounded transformation of policy outputs, preserving the continuity and structure of
                                         decision-making while preventing unsafe deviations.
                                               Importantly, this reframes the role of learned policies: instead of being required to
                                         satisfy all constraints intrinsically, policies can operate in an unconstrained proposal space,
                                         with governance providing a deterministic projection into the admissible domain.

                                         5.2. Safety–Intervention Trade-Off
                                               The experimental results reveal a clear trade-off between safety and intervention cost.
                                         Approval-based gating achieves near-perfect compliance by replacing infeasible actions
                                         with conservative fallbacks, but at the cost of large and discrete deviations from the original
                                         policy output. In contrast, projection-based governance produces smoother behavior but
                                         does not guarantee strict feasibility in all cases.
                                               This trade-off can be interpreted as a Pareto frontier between safety and intervention.
                                         Systems can be configured to prioritize strict compliance or minimal intervention, depend-
                                         ing on application requirements. In safety-critical domains, gating may be preferable due
                                         to its strong enables, whereas projection-based approaches may be better suited for systems
                                         requiring smoother control and higher performance [39].
                                               The existence of this trade-off suggests that governance should not be treated as a
                                         binary mechanism but rather as a tunable component of system design.
                                               The observed trade-off between safety and intervention cost aligns with prior find-
                                         ings in safe reinforcement learning, where stricter constraint enforcement often leads to
                                         increased policy modification [40,41]. However, unlike training-based approaches, the
                                         governance operator introduced in this work operates at execution time, providing deter-
                                         ministic enables independent of the learning process.
                                               Similarly, the stabilization effect observed in federated settings is consistent with prior
                                         work highlighting the challenges of parameter divergence and client heterogeneity [20,22].
                                         The results suggest that governance acts as a behavioral regularizer, constraining the space
                                         of admissible actions even when underlying model parameters vary.

                                         5.3. Bounded Intervention and Stability
                                              A key concern when introducing corrective mechanisms into decision pipelines is the
                                         risk of destabilizing feedback loops [42]. The results show no evidence of such behavior.
                                         Decision drift remains bounded, and trajectory-level deviations do not exhibit divergence
                                         or oscillatory amplification.
                                              This supports the interpretation of governance operators as non-expansive transfor-
                                         mations in the action space, consistent with projection-based formulations [43]. In practice,
                                         this means that governance introduces controlled and predictable modifications to system
                                         behavior, rather than amplifying perturbations.




                                                                                                       https://doi.org/10.3390/make8050125
```

---

## PDF Page 26

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                              26 of 31



                                             The absence of instability is particularly important in closed-loop settings, where
                                         repeated corrections could otherwise accumulate and degrade performance [44].

                                         5.4. Federated Learning and Behavioral Stabilization
                                              In federated settings, governance exhibits an additional and previously underexplored
                                         role: stabilization of executed actions under parameter variability [45]. While federated
                                         training inherently introduces heterogeneity and potential instability in model updates,
                                         governance supports that the resulting actions remain consistent and admissible [46].
                                              The empirical results show low action variance across rounds and zero constraint viola-
                                         tions on benchmark states, even as model parameters evolve. This indicates that governance
                                         effectively decouples parameter-space dynamics from behavior-space outcomes [47,48].
                                              This decoupling is a significant property for distributed AI systems, where enables
                                         on model convergence do not necessarily translate into enables on executed behavior.
                                         Governance provides a mechanism for enforcing behavioral consistency independently of
                                         training dynamics [48].
                                              These findings provide empirical support for both H1 and H2. The reduction in
                                         constraint violations under governance confirms the compliance–stability hypothesis at
                                         the single-agent level (H1), while the observed stabilization of executed actions under
                                         federated training conditions supports the federated stability hypothesis (H2).

                                         5.5. Limitations of Projection-Based Governance
                                               While projection-based governance improves safety relative to the baseline, it does
                                         not guarantee strict feasibility in all scenarios. This limitation arises from multiple factors,
                                         including solver approximations, the presence of coupled constraints, and the potential
                                         non-convexity of the admissible action space [49].
                                               The discrepancy between the theoretical definition of governance as a constraint-
                                         preserving operator and the empirical violation rate (0.8317) is a central finding of this
                                         study. This mismatch reflects the distinction between idealized projection and its numerical
                                         realization in complex constraint settings. In practice, constraint sets are often non-convex,
                                         coupled across agents, and only partially observable, while projection operators rely
                                         on approximate solvers. As a result, governance behaves as an approximate feasibility
                                         operator rather than a strict constraint enforcer. This observation refines the original
                                         theoretical claim: CAIS does not guarantee absolute constraint satisfaction in practical
                                         settings but provides a structured and bounded mechanism for reducing violations under
                                         realistic conditions.
                                               Additionally, the observed higher drift under projection suggests that minimal inter-
                                         vention in a local sense does not necessarily translate into minimal cumulative deviation
                                         over time.
                                               The empirical results indicate that projection-based governance, while reducing con-
                                         straint violations relative to the baseline, does not achieve strict feasibility, with an observed
                                         violation rate of 0.8317. This highlights a critical distinction between the theoretical formu-
                                         lation of governance as a constraint-preserving operator and its practical implementation
                                         under complex constraint structures

                                         5.6. Implications for Safe AI System Design
                                              The results have broader implications for the design of safe and auditable AI systems.
                                         The CAIS architecture demonstrates that safety can be enforced at the execution level
                                         without requiring policies to internalize all constraints during training.
                                              This separation of concerns enables more flexible and scalable system design. Policies
                                         can be optimized for performance, while governance ensures compliance and safety. Fur-




                                                                                                        https://doi.org/10.3390/make8050125
```

---

## PDF Page 27

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                          27 of 31



                                         thermore, the integration of audit trace semantics provides a foundation for reproducibility
                                         and accountability, which are essential in regulated domains.
                                               Overall, governance emerges as a principled mechanism for achieving safe deploy-
                                         ment of agentic AI systems, particularly in environments characterized by uncertainty,
                                         distribution shift, and decentralized learning.
                                               The empirical evaluation presented in this work is based on controlled simulation
                                         environments, which allow precise isolation of governance effects and ensure full re-
                                         producibility. However, this also limits direct generalization to real-world systems. In
                                         practical deployments, additional factors such as sensor noise, partial observability, dy-
                                         namic constraints, and environmental uncertainty may influence performance. Therefore,
                                         the reported results should be interpreted as foundational evidence supporting the CAIS
                                         architecture, rather than definitive validation in operational settings.
                                               Compared to existing approaches such as constrained reinforcement learning, safety
                                         filtering, and shielding mechanisms, the CAIS framework introduces a distinct architectural
                                         perspective in which governance is embedded directly within the decision transformation.
                                         This enables simultaneous reasoning about compliance, stability, auditability, and repro-
                                         ducibility, which are typically addressed separately in prior work. As such, the proposed
                                         approach extends beyond optimization-based or filtering-based safety mechanisms by
                                         providing a unified and formally grounded framework for controlled AI systems.

                                         5.7. Positioning Relative to Safety Mechanisms
                                              To position CAIS within the broader landscape of safe AI methodologies, it is impor-
                                         tant to distinguish it from related approaches such as constrained reinforcement learning,
                                         shielding, safety filters, and runtime safety layers.
                                              Constrained reinforcement learning methods enforce safety during training by modi-
                                         fying the optimization objective, typically through reward shaping or constraint penalties.
                                         In contrast, CAIS operates at execution time and does not require policies to internal-
                                         ize constraints.
                                              Shielding and runtime safety layers act as external mechanisms that override unsafe
                                         actions after policy inference. While similar in function, they are typically implemented
                                         as add-on modules. CAIS differs by embedding governance directly into the decision
                                         transformation, making constraint enforcement an intrinsic property of the system.
                                              Safety filters and control-theoretic approaches, such as control barrier functions, en-
                                         force admissibility through optimization-based correction. CAIS generalizes this idea
                                         beyond continuous control systems by integrating projection-based governance with au-
                                         ditability and reproducibility semantics.
                                              Thus, CAIS can be interpreted as a unifying architectural abstraction that incorporates
                                         elements of filtering, projection, and constraint enforcement into a single deterministic
                                         operator within the decision pipeline.
                                              The findings of this study naturally suggest several concrete directions for further
                                         investigation. First, the observed discrepancy between theoretical constraint preservation
                                         and empirical feasibility highlights the need for more robust governance operators capa-
                                         ble of handling non-convex and coupled constraint spaces. Future work should explore
                                         hybrid governance mechanisms that combine projection-based repair with fallback strate-
                                         gies, as well as more advanced optimization techniques that improve feasibility under
                                         complex constraints.
                                              Second, the current formulation treats governance as an execution-time transforma-
                                         tion applied after policy inference. An important extension is to integrate governance
                                         directly into the learning process, enabling co-adaptation between policy optimization and




                                                                                                    https://doi.org/10.3390/make8050125
```

---

## PDF Page 28

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                         28 of 31



                                         constraint enforcement. This would allow the model to internalize constraint structure,
                                         potentially reducing intervention cost while maintaining compliance.
                                               Third, the federated experiments indicate that governance can stabilize behavior
                                         despite parameter variability, suggesting a promising direction for studying the inter-
                                         action between governance and distributed learning. Future research should investi-
                                         gate asynchronous federated settings, adversarial client behavior, and communication-
                                         constrained environments to better understand the role of governance in large-scale decen-
                                         tralized systems.
                                               Finally, while the current evaluation is based on controlled simulation, the ultimate
                                         validation of the CAIS framework requires deployment in real-world environments. This
                                         includes applications such as autonomous maritime navigation and distributed energy
                                         systems, where governance must operate under partial observability, noisy sensing, and
                                         dynamic regulatory constraints. Such studies would provide critical insight into the
                                         scalability and robustness of governance-driven AI architectures.

                                         6. Conclusions
                                              This work introduces Controlled Agentic AI Systems (CAIS) as a principled architec-
                                         tural framework for integrating governance directly into the decision-making process of
                                         AI systems. By formalizing governance as a deterministic operator acting on proposed
                                         decisions, the framework unifies constraint enforcement, auditability, and reproducibility
                                         within a single, mathematically grounded design.
                                              The theoretical analysis demonstrates that governance can be interpreted as a projec-
                                         tion onto an admissible action space, ensuring constraint-aware execution while preserving
                                         stability through bounded decision drift. Under standard smoothness assumptions, the
                                         governance operator is shown to be non-expansive, providing formal justification that
                                         embedding constraint enforcement into the decision pipeline does not introduce destabiliz-
                                         ing behavior.
                                              The empirical evaluation, conducted in controlled multi-agent and federated sim-
                                         ulation environments, supports these theoretical findings. Across all tested scenarios,
                                         governance consistently reduces constraint violations and improves system-level safety
                                         properties. Projection-based repair mechanisms achieve the most favorable trade-off be-
                                         tween compliance and intervention cost, while approval-based strategies provide a robust
                                         baseline. Importantly, governance does not degrade learning dynamics in federated settings
                                         and can reduce action-level variability induced by parameter heterogeneity.
                                              At the same time, the results highlight a fundamental practical distinction between
                                         theoretical guarantees and real-world implementations. While the CAIS formulation
                                         assumes ideal constraint-preserving behavior, empirical outcomes indicate that governance
                                         primarily achieves substantial reduction in violations rather than absolute elimination,
                                         particularly in the presence of non-convex constraint sets and numerical approximation.
                                         This observation is consistent with the underlying optimization and projection limitations
                                         and underscores the importance of realistic evaluation.
                                              A key limitation of the present study is that validation is performed in a controlled
                                         simulation environment. Although the experimental design incorporates multi-agent
                                         interactions, adversarial perturbations, and federated learning dynamics, real-world de-
                                         ployment may introduce additional sources of uncertainty, including imperfect sensing,
                                         model misspecification, and non-stationary environments. Future work will focus on
                                         extending the framework to high-fidelity simulators and real-world datasets, particularly
                                         in safety-critical domains such as maritime systems and distributed energy networks.




                                                                                                   https://doi.org/10.3390/make8050125
```

---

## PDF Page 29

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                  29 of 31



                                               Overall, the results indicate that governance, when treated as an intrinsic component
                                         of the decision pipeline, can act as a stabilizing and compliance-enhancing transforma-
                                         tion. The CAIS framework therefore provides a robust foundation for the development of
                                         next-generation AI systems that must operate under strict regulatory, safety, and auditabil-
                                         ity requirements.

                                         Funding: This research received no external funding.

                                         Data Availability Statement: All data, figures, and code used in this study are openly available
                                         and have been deposited in the public GitHub repository: https://github.com/TyMill/CAIS-pub—
                                         CAIS v1.0 release (access date: 19 March 2026). In addition, a permanent, citable version of the
                                         repository, including experimental results and materials, is archived on Zenodo under the following
                                         DOI: https://doi.org/10.5281/zenodo.19110441 (access date: 19 March 2026).

                                         Conflicts of Interest: The author declares no conflicts of interest.

References
1.    Pillay, N.; Nyathi, T.; Venayagamoorthy, G.K. Artificial Intelligence for Critical Infrastructure Systems: Past, Present and Future.
      In Proceedings of the International Joint Conference on Neural Networks (IJCNN), Rome, Italy, 30 June–5 July 2025; pp. 1–9.
      [CrossRef]
2.    Agarwal, A.; Nene, M.J. Addressing AI Risks in Critical Infrastructure: Formalising the AI Incident Reporting Process. In
      Proceedings of the IEEE International Conference on Electronics, Computing and Communication Technologies (CONECCT),
      Bangalore, India, 12–14 July 2024; pp. 1–6. [CrossRef]
3.    Chen, S.Y.-C.; Chen, K.-C. Quantum Artificial Intelligence for Critical Infrastructure: A Survey and Vision. In Proceedings of the
      International Joint Conference on Neural Networks (IJCNN), Rome, Italy, 30 June–5 July 2025; pp. 1–8. [CrossRef]
4.    Ali, S.M.; Razzaque, A.; Yousaf, M.; Shan, R.U. An Automated Compliance Framework for Critical Infrastructure Security through
      Artificial Intelligence. IEEE Access 2025, 13, 4436–4459. [CrossRef]
5.    Kollipara, Y.V.P. Assured, Explainable, and Auditable AI for High-Stakes Decisions: A Survey of Trustworthy Machine Learning
      in Mission-Critical Systems. J. Int. Crisis Risk Commun. Res. 2025, 8, 554–566. [CrossRef]
6.    Jaziri, W.; Sassi, N. Explainable by Design: Enhancing Trustworthiness in AI-Driven Control Systems. Mathematics 2025, 13, 3805.
      [CrossRef]
7.    Singh, Y.; Hathaway, Q.A.; Keishing, V.; Salehi, S.; Wei, Y.; Horvat, N.; Vera-Garcia, D.V.; Choudhary, A.; Mula Kh, A.; Quaia, E.;
      et al. Beyond Post hoc Explanations: A Comprehensive Framework for Accountable AI in Medical Imaging. Bioengineering 2025,
      12, 879. [CrossRef]
8.    Adabara, I.; Olaniyi, S.B.; Nuhu, S.A.; Ibrahim, D.Y.; Maninti, V. Trustworthy Agentic AI Systems: A Cross-Layer Review of
      Architectures, Threat Models, and Governance Strategies. F1000Research 2025, 14, 905. [CrossRef]
9.    Biswas, B.; Sarkar, S. Responsible Agentic Artificial Intelligence Governance: Risk, Safety, and Ethical Challenges. Int. J. Appl.
      Resil. Sustain. 2026, 2, 142–167. [CrossRef]
10.   de Witt, C.S. Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents. arXiv 2025,
      arXiv:2505.02077. [CrossRef]
11.   Hashi, A.I.; Hashi, A.M.; Jama, O.A. Trustworthy AI Governance Framework for Autonomous Systems. Int. J. Comput. Trends
      Technol. 2026, 74, 12–27. [CrossRef]
12.   Eden, R.; Chukwudi, I.; Bain, C.; Barbieri, S.; Callaway, L.; de Jersey, S.; George, Y.; Gorse, A.-D.; Lawley, M.; Marendy, P.; et al.
      Governance of Federated Learning in Healthcare: A Scoping Review. npj Digit. Med. 2025, 8, 427. [CrossRef]
13.   Matta, S.S.; Bolli, M. Trustworthy AI: Explainability and Fairness in Large-Scale Decision Systems. Rev. Appl. Sci. Technol. 2023, 2,
      54–93. [CrossRef]
14.   Basir, O.A. The Social Responsibility Stack: A Control-Theoretic Architecture for Governing Socio-Technical AI. arXiv 2025,
      arXiv:2512.16873.
15.   Butt, T.A.; Iqbal, M.; Arshad, N. From Policy to Pipeline: A Governance Framework for AI Development and Operations Pipelines.
      IEEE Access 2026, 14, 1373–1397. [CrossRef]
16.   Muhammad, A.E.; Yow, K.-C. Risk-Based AI Assurance Framework. Information 2026, 17, 263. [CrossRef]
17.   Achiam, J.; Held, D.; Tamar, A.; Abbeel, P. Constrained Policy Optimization. Proc. Mach. Learn. Res. 2017, 70, 22–31.
18.   Chow, Y.; Nachum, O.; Duenez-Guzman, E.; Ghavamzadeh, M. A Lyapunov-Based Approach to Safe Reinforcement Learn-
      ing. In Proceedings of the 32nd Conference on Neural Information Processing Systems (NeurIPS 2018), Montreal, Canada,
      2–8 December 2018; p. 31.



                                                                                                            https://doi.org/10.3390/make8050125
```

---

## PDF Page 30

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                                  30 of 31



19.   Tearle, B.; Wabersich, K.P.; Carron, A.; Zeilinger, M.N. A Predictive Safety Filter for Learning-Based Racing Control. IEEE Robot.
      Autom. Lett. 2021, 6, 7635–7642. [CrossRef]
20.   Alshiekh, M.; Bloem, R.; Ehlers, R.; Könighofer, B.; Niekum, S.; Topcu, U. Safe Reinforcement Learning via Shielding. Proc. AAAI
      Conf. Artif. Intell. 2018, 32, 2669–2678. [CrossRef]
21.   Ames, A.D.; Xu, X.; Grizzle, J.W.; Tabuada, P. Control Barrier Function Based Quadratic Programs for Safety Critical Systems.
      IEEE Trans. Autom. Control 2017, 62, 3861–3876. [CrossRef]
22.   Xiao, W.; Belta, C. Control Barrier Functions for Systems with High Relative Degree. In Proceedings of the IEEE Conference on
      Decision and Control (CDC), Nice, France, 11–13 December 2019; pp. 474–479. [CrossRef]
23.   Cheng, R.; Orosz, G.; Murray, R.M.; Burdick, J.W. End-to-End Safe Reinforcement Learning through Barrier Functions. In
      Proceedings of the AAAI Conference on Artificial Intelligence, Honolulu, HI, USA, 27 January–1 February 2019; pp. 3387–3395.
24.   Doshi-Velez, F.; Kim, B. Towards a Rigorous Science of Interpretable Machine Learning. arXiv 2017, arXiv:1702.08608. [CrossRef]
25.   Cannarsa, M. Ethics Guidelines for Trustworthy AI. In The Cambridge Handbook of Lawyering in the Digital Age; Cambridge
      University Press: Cambridge, UK, 2021; pp. 97–283.
26.   Floridi, L.; Cowls, J.; Beltrametti, M.; Chatila, R.; Chazerand, P.; Dignum, V.; Luetge, C.; Madelin, R.; Pagallo, U.; Rossi, F.; et al.
      AI4People—An Ethical Framework for a Good AI Society. Minds Mach. 2018, 28, 689–707. [CrossRef]
27.   Arrieta, A.B.; Díaz-Rodríguez, N.; Del Ser, J.; Bennetot, A.; Tabik, S.; Barbado, A.; Garcia, S.; Gil-Lopez, S.; Molina, D.; Benjamins,
      R.; et al. Explainable Artificial Intelligence (XAI): Concepts and Challenges. Inf. Fusion 2020, 58, 82–115. [CrossRef]
28.   McMahan, B.; Moore, E.; Ramage, D.; Hampson, S.; Arcas, B.A.Y. Communication-Efficient Learning of Deep Networks from
      Decentralized Data. Proc. Mach. Learn. Res. 2017, 54, 1273–1282.
29.   Kairouz, P.; McMahan, H.B. Advances and Open Problems in Federated Learning. Found. Trends Mach. Learn. 2021, 14, 1–210.
      [CrossRef]
30.   Li, T.; Sahu, A.K.; Zaheer, M.; Sanjabi, M.; Talwalkar, A.; Smith, V. Federated Optimization in Heterogeneous Networks. Proc.
      Mach. Learn. Syst. 2020, 2, 429–450.
31.   Karimireddy, S.P.; Kale, S.; Mohri, M.; Reddi, S.; Stich, S.; Suresh, A.T. SCAFFOLD: Stochastic Controlled Averaging for Federated
      Learning. arXiv 2020, arXiv:1910.06378. [CrossRef]
32.   Lowe, R.; Wu, Y.I.; Tamar, A.; Harb, J.; Abbeel, P.; Mordatch, I. Multi-Agent Actor-Critic for Mixed Environments. In Proceedings
      of the 31st Conference on Neural Information Processing Systems (NIPS 2017), Long Beach, CA, USA, 4–9 December 2017; p. 30.
33.   Zhang, K.; Yang, Z.; Başar, T. Multi-Agent Reinforcement Learning: A Selective Overview. In Handbook of Reinforcement Learning
      and Control; Springer: Berlin/Heidelberg, Germany, 2021; pp. 321–384. [CrossRef]
34.   Busoniu, L.; Babuska, R.; De Schutter, B. A Comprehensive Survey of Multiagent Reinforcement Learning. IEEE Trans. Syst. Man
      Cybern. C 2008, 38, 156–172. [CrossRef]
35.   Gu, S.; Kuba, J.G.; Wen, M.; Chen, R.; Wang, Z.; Tian, Z.; Yang, Y. Multi-Agent Constrained Policy Optimisation. arXiv 2021,
      arXiv:2110.02793.
36.   Sheebaelhamd, Z.; Zisis, K.; Nisioti, A.; Gkouletsos, D.; Pavllo, D.; Kohler, J. Safe Deep Reinforcement Learning for Multi-Agent
      Systems with Continuous Action Spaces. arXiv 2021, arXiv:2108.03952. [CrossRef]
37.   Li, T.; Sahu, A.K.; Talwalkar, A.; Smith, V. Federated Learning: Challenges, Methods, and Future Directions. IEEE Signal Process.
      Mag. 2020, 37, 50–60. [CrossRef]
38.   Zhao, Y.; Li, M.; Lai, L.; Suda, N.; Civin, D.; Chandra, V. Federated Learning with Non-IID Data. arXiv 2018, arXiv:1806.00582.
      [CrossRef]
39.   Hung, W.; Sun, S.H.; Hsieh, P.C. Efficient Action-Constrained Reinforcement Learning. arXiv 2025, arXiv:2503.12932. [CrossRef]
40.   Tessler, C.; Mankowitz, D.J.; Mannor, S. Reward Constrained Policy Optimization. arXiv 2018, arXiv:1805.11074. [CrossRef]
41.   Dalal, G.; Dvijotham, K.; Vecerik, M.; Hester, T.; Paduraru, C.; Tassa, Y. Safe Exploration in Continuous Action Spaces. arXiv 2018,
      arXiv:1801.08757. [CrossRef]
42.   Kilian, K.A. Structural Risk Dynamics of Artificial Intelligence. AI Soc. 2026, 41, 23–42. [CrossRef]
43.   Ferrari, L.; Frosini, P.; Quercioli, N.; Tombari, F. A Topological Model for Partial Equivariance. Front. Artif. Intell. 2023, 6, 1272619.
      [CrossRef] [PubMed]
44.   Tao, Y. The Decision Path to Control AI Risks Completely. arXiv 2025, arXiv:2512.04489. [CrossRef]
45.   Konakanchi, M.S.K. Aegis: AI-Driven Governance Framework for Micro-Frontend Architectures. J. Adv. Dev. Res. IJAIDR
      2025, 17.
46.   Garro, R.J.; Wibowo, S.; Wilson, C.S.; Pordomingo, A.J. A Federated Learning Architecture with Weighted Aggregation for Feed
      Intake Analysis in Precision Livestock Systems. In Proceedings of the 2025 8th International Conference on Informatics and
      Computational Sciences (ICICoS), Semarang, Indonesia, 29–30 October 2025; pp. 340–345. [CrossRef]
47.   Jiang, Y.; Wang, F.; Pang, X. Parameter Decoupling Approach in Personalized Federated Learning for Gastric Cancer Pathology
      Classification. In Proceedings of the 2024 10th International Conference on Computer and Communications (ICCC), Chengdu,
      China, 13–16 December 2024; pp. 771–775. [CrossRef]



                                                                                                         https://doi.org/10.3390/make8050125
```

---

## PDF Page 31

```text
Mach. Learn. Knowl. Extr. 2026, 8, 125                                                                                          31 of 31



48.   Wei, W.; Liu, L. Trustworthy Distributed AI Systems: Robustness, Privacy, and Governance. ACM Comput. Surv. 2025, 57, 1–42.
      [CrossRef]
49.   Li, F.; Li, M.; Li, S.; Wu, Y.; Song, Y.; Li, H. Rational-Safe Reinforcement Learning for Energy Management. In Proceedings of the
      IECON, Madrid, Spain, 14–17 October 2025; pp. 1–6. [CrossRef]


Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.




                                                                                                    https://doi.org/10.3390/make8050125
```
