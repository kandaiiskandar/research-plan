# Adaptive Shielding via Parametric Safety Proofs

> **Source PDF:** `Adaptive Shielding via Parametric Safety Proofs.pdf` · **Pages:** 28 · Converted by `scripts/paper2md.py` from the original PDF. **Equations are extracted glyph-by-glyph and may be mangled — check the PDF before quoting any formula.**

<!-- page 1 -->

## Adaptive Shielding via Parametric Safety Proofs

YAO FENG∗, Tsinghua University, China JUN ZHU, Tsinghua University, China ANDRÉ PLATZER, Karlsruhe Institute of Technology (KIT), Germany JONATHAN LAURENT†, KIT, Germany and Carnegie Mellon University, USA

A major challenge to deploying cyber-physical systems with learning-enabled controllers is to ensure their safety, especially in the face of changing environments that necessitate runtime knowledge acquisition. Model-checking and automated reasoning have been successfully used for shielding, i.e., to monitor untrusted controllers and override potentially unsafe decisions, but only at the cost of hard tradeoffs in terms of expressivity, safety, adaptivity, precision and runtime efficiency. We propose a programming-language framework that allows experts to statically specify adaptive shields for learning-enabled agents, which enforce a safe control envelope that gets more permissive as knowledge is gathered at runtime. A shield specification provides a safety model that is parametric in the current agent’s knowledge. In addition, a nondeterministic inference strategy can be specified using a dedicated domain-specific language, enforcing that such knowledge parameters are inferred at runtime in a statistically-sound way. By leveraging language design and theorem proving, our proposed framework empowers experts to design adaptive shields with an unprecedented level of modeling flexibility, while providing rigorous, end-to-end probabilistic safety guarantees.

CCS Concepts: • Computer systems organization →Embedded and cyber-physical systems; • Software and its engineering →Formal methods; • Computing methodologies →Reinforcement learning.

Additional Key Words and Phrases: Safe Reinforcement Learning, Programming Languages, Differential Dynamic Logic, Statistical Inference, Hybrid Systems

ACM Reference Format: Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent. 2025. Adaptive Shielding via Parametric Safety Proofs. Proc. ACM Program. Lang. 9, OOPSLA1, Article 109 (April 2025), 28 pages. https://doi.org/10.1145/3720450

1 Introduction Learning-based methods such as reinforcement learning have shown great promise in the fields of autonomous driving [28, 38] and robot control [19, 37, 39]. However, their deployment in the real-world has been held back by reliability and safety concerns. The use of formal methods has been suggested to guarantee the safety of learning-enabled systems, both after and during training [10, 15, 16, 20]. Many different approaches have been proposed to do so, which share as a foundation the idea of sandboxing or shielding [2, 15, 29, 43]. In this framework, the intended actions of a learning-enabled agent are monitored at runtime and overridden by appropriate fallbacks whenever they cannot be proved safe with respect to a model of the environment.

∗Yao Feng contributed a majority of the case studies and experiments. †Jonathan Laurent contributed a majority of the theoretical framework and writing.

Authors’ Contact Information: Yao Feng, Tsinghua University, Beijing, China, y-feng23@mails.tsinghua.edu.cn; Jun Zhu, Tsinghua University, Beijing, China, dcszj@mail.tsinghua.edu.cn; André Platzer, Karlsruhe Institute of Technology (KIT), Karlsruhe, Germany, platzer@kit.edu; Jonathan Laurent, KIT, Karlsruhe, Germany and Carnegie Mellon University, Pittsburgh, USA, jonathan.laurent@kit.edu.

This work is licensed under a Creative Commons Attribution 4.0 International License. © 2025 Copyright held by the owner/author(s). ACM 2475-1421/2025/4-ART109 https://doi.org/10.1145/3720450

<!-- page 2 -->

109:2 Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent

Most existing approaches leverage automated techniques for proving safety such as reachability analysis [26, 43], LTL model-checking [2, 27] or Hamilton-Jacobi solving [13]. Such techniques can be applied offline to precompute numerical, table-based control envelopes that indicate what actions are safe in every possible state of the system. Alternatively, they can be used at runtime to analyze the safety of different actions with respect to the current state. Such online methods mostly offer only bounded-horizon guarantees and must typically make aggressive tradeoffs to regain efficiency at the cost of precision or generality. However, an advantage of online methods is that they allow the model to be updated at runtime as the agent gathers information about its environment. Indeed, in many situations, a fully-specified model of the environment is not known at design-time and using a necessarily conservative static model may lead to overly cautious behavior. In principle, adaptivity can also be offered by offline methods, by precomputing control envelopes for every possible model that may be considered at runtime. However, doing so further compounds the scalability challenges of model-checking. Finally, existing approaches to adaptive shielding, whether online or offline, are either offering limited expressivity to encode model uncertainty (e.g. bounded disturbance terms [3] or finite model families [16]) or failing to provide rigorous end-to-end guarantees under assumptions that can be easily validated (e.g. methods based on learning Gaussian processes [4, 5, 9, 13]).

This work introduces a programming-language framework for designing adaptive safety shields, leveraging a minimal yet crucial amount of human insight to target a very general class of model families, while shifting the full burden of safety analysis offline. In this framework, control envelopes are described by nondeterministic controllers, whose safety is established using differential dynamic logic [31, 32]. Environment models can be parametrized by unknown function symbols. Those function symbols are subject to parametric bounds, whose parameters are accessible to the controller and can be instantiated and refined at runtime. Updating these parameters in a way that is sound and efficient is a great challenge in itself. We address this challenge by offering experts a domain-specific language to express nondeterministic inference strategies that are sound by construction, and whose nondeterminism is resolved by an inference policy that can be programmed or learned in the same way that the control policy is.

We illustrate our framework on four case studies, demonstrating its safety and its ability to handle advanced uncertainty models that are beyond the reach of existing methods. We also showcase the possibility of having agents learn how to manage their own safety budget by learning inference policies, which – to the best of our knowledge – has no equivalent in the literature.

## 2 Overview

In this section, we motivate and illustrate our framework on a series of closely-related examples.

2.1 Extracting Shields from Verified Nondeterministic Controllers Our framework builds on the idea of extracting runtime controller monitors from provably safe, nondeterministic controllers [15, 29]. The safety of such nondeterministic controllers is established using differential dynamic logic (dL) [31, 32], which is designed specifically to verify hybrid systems with both discrete and continuous dynamics. In dL, we use hybrid programs (HPs) to model both controllers and the differential equations of the physical environments they interact with. A summary of the syntax and semantics of hybrid programs can be found in Table 1. Proving the safety of a cyber-physical system using dL typically comes down to proving a modal formula of the form Init→[(Ctrl ; Plant)∗]Safe, where Init and Safe are logical formulas while Ctrl and Plant are hybrid programs. This means that under a certain initial condition (Init), no matter how often we execute the discrete-time controller (Ctrl) and let the continuous-time system evolve to the next control cycle (Plant), the safety condition (Safe) is satisfied.

<!-- page 3 -->

Adaptive Shielding via Parametric Safety Proofs 109:3

**Table 1. Semantics of Hybrid Programs in dL**

Syntax Semantics

𝑥··=𝑒 Assign the value of 𝑒to variable 𝑥, leaving all other variables unchanged. 𝑥··= ∗ Assign variable 𝑥nondeterministically to some real value. ?𝑄 If 𝑄is true, continue running; else abort. 𝑥′ = 𝑓(𝑥) & 𝑄 Follow the system of differential equations 𝑥′ = 𝑓(𝑥) for a certain (nondeterministic) amount of time while 𝑄holds true. 𝛼∪𝛽 Nondeterministically run either HP 𝛼or 𝛽. 𝛼; 𝛽 Sequentially run 𝛽after 𝛼. 𝛼∗ Run 𝛼repeatedly for any ≥0 amount of iterations.

```math
Model ≡Init →[(Ctrl ; Plant)∗] Safe
(1)
```

Init ≡(𝐴> 0 ∧𝐵> 0 ∧𝑇> 0) ∧(𝑥+ 𝑣2/2𝐵≤𝑒)

```math
Ctrl ≡(𝑎··= −𝐵) ∪(?(𝑥+ 𝑣𝑇+ 𝐴𝑇2/2 + (𝑣+ 𝐴𝑇)2/2𝐵≤𝑒) ; 𝑎··=𝐴)
(2)
```

```math
Plant ≡𝑡··= 0 ; {𝑥′ = 𝑣, 𝑣′ = 𝑎, 𝑡′ = 1 & 𝑡≤𝑇∧𝑣≥0}
```

Safe ≡𝑥≤𝑒

**Fig. 1. A Simple dL Model of a Train Braking-Control System [33]**

For example, the dL model described in Figure 1 designates a nondeterministic train controller that must stop by the end of movement authority 𝑒located somewhere ahead of the train, as assigned by the train network scheduler [33]. Variable 𝑥models the position of the train on its tracks. At every control cycle, the driver can choose between braking with acceleration −𝐵< 0 or accelerating with acceleration 𝐴> 0. It then gives control to the environment until the next control cycle, which happens in at most 𝑇seconds. However, the option to accelerate is only acceptable when a sufficient distance remains to accelerate and then brake safely. The safety of this nondeterministic train controller can be established by proving the validity of Formula 1, using the rules and axioms of dL. This can be done interactively in a proof assistant such as KeYmaera X [14]. In particular, doing so requires finding a loop invariant Inv that holds initially, implies the safety property and is preserved by any run of hybrid program Ctrl ; Plant. Here, one can take Inv ≡Init.

Crucially, one can extract a runtime monitor from the nondeterministic controller shown in Equation 2 and use it as a shield for a learning-enabled agent [15]. For example, one could use reinforcement learning to learn a deterministic train controller that optimizes for speed, energy efficiency and passenger comfort, while guaranteeing safety by overriding acceleration whenever the distance to the end-of-movement authority is insufficient (i.e. the guard in Equation 2 is violated).

### 2.2 Adding Adaptivity via Parametric Bounds

As illustrated in the previous section, previous work [15, 29] has shown how to extract shields from nondeterministic controllers whose safety is established using differential dynamic logic. However, doing so requires an accurate model of every safety-relevant aspect of the system. In cases where only a conservative model is available, the shield may force the system into an overly cautious behavior. One contribution of this work is to allow the design of adaptive shields, whose behavior

<!-- page 4 -->

109:4 Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent

is refined at runtime as the agent gathers more information about its environment. To do so, we allow environment models to be parameterized by unknown quantities and control envelopes to be parameterized by bounds on these same quantities.

An example of such an adaptive shield is described in Figure 2. It is specified using our proposed shield specification language, which we define rigorously in Sections 4 and 5. This example is a variation of the train control system from Figure 1 with a continuous action space: instead of making a binary choice between accelerating and braking, the agent must select a commanded acceleration 𝑢∈[−𝐵,𝐴], which is expressed in dL using a nondeterministic assignment 𝑢··= ∗ followed by a test ?(−𝐵≤𝑢≤𝐴). In addition, the relationship between the commanded acceleration 𝑢and the actual acceleration 𝑎of the train is governed by an unknown linear function: 𝑎= 𝜃𝑢+ 𝜑 where 𝜃> 0 and 𝜑are unknown real parameters. At runtime, the actual acceleration of the train is measured repeatedly, allowing the agent to compute increasingly precise estimates of the systematic disturbance 𝜃and 𝜑and thus allowing the shield to be increasingly permissive.

The shield specification in Figure 2 consists of eleven sections, each of them introduced by a distinct keyword. constant introduces real quantities that are known by the agent at runtime such as the maximum commanded acceleration 𝐴. unknown introduces quantities that are not known and must be estimated at runtime, namely 𝜃and 𝜑. assume gathers global assumptions about constant and unknown symbols such as 𝐴> 0 and 𝜃> 0. Such assumptions could be encoded as system invariants instead (see invariant) but separating them from state-dependent invariants leads to greater conceptual clarity and more concise proof obligations (global assumptions are preserved by definition). The controller, plant, safe and invariant sections define a dL model similar in shape to the one already studied in Figure 1. However, the plant model can feature unknown symbols, which it does here via the 𝑣′ = 𝜃𝑢+ 𝜑differential equation. Also the controller can depend on bound parameters that constrain these unknowns and that are introduced in the bound section. Here, we introduce a lower bound ¯𝜃on 𝜃, an upper bound ¯𝜃on 𝜃, and an upper bound ¯𝜑on 𝜑. These parameters are instantiated and refined at runtime as the agent is gathering knowledge, using statistical inference. The controller is similar to Equation 2, except that it offers a continuous action space and conservatively assumes a maximum achievable braking rate of ¯𝜃𝐵−¯𝜑. Thus, the control envelope defined by the nondeterministic controller gets increasingly permissive as tighter bounds are obtained on 𝜃and 𝜑.

The invariant can depend on bound parameters but only monotonically, in the sense that it can only be made more permissive by a tightening of the bounds. This is an intuitive requirement: acquiring knowledge must never transition an agent from a state considered safe to a state considered unsafe. Here, this requirement clearly holds since the maximum guaranteed braking rate of ¯𝜃𝐵−¯𝜑 can only get larger as ¯𝜃and ¯𝜑tighten. Finally, noise and observe specify the kind of information that may become available at runtime to compute and refine such bounds. Here, we are assuming that at every control cycle, an estimate of the actual acceleration of the system may be measured, with some Gaussian noise of standard deviation 𝜎. No guarantee is offered on when and under what conditions such an observation becomes available. infer defines a family of provably-sound strategies for updating ¯𝜃, ¯𝜃and ¯𝜑based on such observations, as we discuss shortly in Section 2.4. Before we do so though, we introduce a last variant of our train control shield that illustrates how functional unknowns can be handled, using the concept of a local bound.

2.3 Handling Functional Unknowns with Local Bounds In our previous example from Figure 2, two real-valued unknowns are estimated at runtime. However, our framework can handle a more powerful and flexible form of model-uncertainty in the form of functional unknowns. Figure 3 provides an example, considering a train that evolves on tracks of unknown, varying slope. Variable 𝑥denotes the train position on an arc-length parametrization

<!-- page 5 -->

Adaptive Shielding via Parametric Safety Proofs 109:5

constant 𝐴, 𝐵,𝑇, 𝜎

unknown 𝜃,𝜑

assume 𝐴> 0, 𝐵> 0, 𝑇> 0, 𝜎> 0, 𝜃> 0

```math
bound ¯𝜃: ¯𝜃≤𝜃, ¯𝜃: ¯𝜃≥𝜃, ¯𝜑: ¯𝜑≥𝜑
```

controller

```math
𝑢··= ∗; ?(−𝐵≤𝑢≤𝐴) ; ?(𝑥+ 𝑣𝑇+ ( ¯𝜃𝑢+ ¯𝜑)𝑇2/2 + (𝑣+ ( ¯𝜃𝑢+ ¯𝜑)𝑇)2/2(¯𝜃𝐵−¯𝜑) ≤𝑒)
```

```math
plant 𝑡··= 0 ; {𝑥′ = 𝑣, 𝑣′ = 𝜃𝑢+ 𝜑,𝑡′ = 1 & 𝑡≤𝑇∧𝑣≥0}
```

safe 𝑥≤𝑒

invariant (¯𝜃𝐵−¯𝜑> 0) ∧(𝑥+ 𝑣2/2(¯𝜃𝐵−¯𝜑) ≤𝑒)

noise 𝜂∼N (0, 𝜎2)

observe 𝜔= 𝜃𝑢+ 𝜑−𝜂

infer

¯𝜃, ¯𝜃··= aggregate 𝑖, 𝑗: (𝜔𝑗−𝜔𝑖)/(𝑢𝑗−𝑢𝑖) and (𝜂𝑗−𝜂𝑖)/(𝑢𝑗−𝑢𝑖) when 𝑢𝑗> 𝑢𝑖;

¯𝜑··= aggregate 𝑖: 𝜔𝑖−¯𝜃𝑢𝑖and 𝜂𝑖when 𝑢𝑖≤0

**Fig. 2. An adaptive shield for a train control system, where the relationship between the commanded and actual train acceleration is governed by an unknown linear function.**

of the tracks. A train at position 𝑥is subject to an additional acceleration term of −𝑔· sin(𝜃𝑥) where 𝑔≈9.81 m s−2 is Earth’s gravitational acceleration and 𝜃𝑥the track angle at coordinate 𝑥. We model this influence by defining the train’s kinematics as 𝑣′ = 𝑎+ 𝑓(𝑥), with 𝑎the acceleration commanded by the controller and 𝑓an unknown function of 𝑥. In addition, 𝑓is assumed to be 𝑘-Lipschitz, globally lower-bounded by −𝐴(ensuring that the train will always move forward when instructed to accelerate at rate 𝐴) and upper-bounded by a known constant 𝐹. One could simply use this global bound to implement a conservative shield. Our challenge is to do better by estimating superior, local estimates of 𝑓based on runtime observations.

We do so by introducing the concept of a local bound. Figure 3 defines such a bound, namely ¯𝑓≥𝑓(𝑥). As opposed to the global bounds used in the previous section, this bound involves quantity 𝑓(𝑥) that is state-dependent. The guarantee that comes with such a definition is that before every control cycle, the inference module must provide a value ¯𝑓that is an upper bound on the value of 𝑓(𝑥), as evaluated in the current state. The value of ¯𝑓can be used in the controller. However, ¯𝑓cannot be mentioned in the invariant since ¯𝑓≥𝑓(𝑥) may not hold anymore as the plant executes and the train moves further on the tracks. A local bound is only guaranteed to be valid at discrete points in time, after each run of the inference module and right before the controller executes. Thus, we also maintain an upper bound y on 𝑓(𝑥) that holds throughout the plant and can therefore be used in the invariant. Variable 𝑦is updated before the controller executes with the value of ¯𝑓whenever the latter provides a tighter bound. Then, it is evolved via the differential equation 𝑦′ = 𝑘𝑣, degrading the precision of our bound at a rate proportional to the Lipschitz constant of 𝑓to ensure its preservation by the plant (d𝑓/d𝑡≤d𝑓/d𝑥· d𝑥/d𝑡≤𝑘· 𝑣).

We can now derive our invariant, from which the controller’s acceleration guard follows. Given a particular state and provided a bound 𝑦≥𝑓(𝑥), we wonder whether the train can be kept safe indefinitely from the current state by fully engaging the brakes. Given a constant, effective braking rate of 𝑏and starting with speed 𝑣, it can be shown that the distance needed for the train to brake to a full stop is Bdist𝑣(𝑏) ≡𝑣2/2𝑏. Thus, a sufficient condition for the train to be safe indefinitely is

<!-- page 6 -->

109:6 Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent

constant 𝐴, 𝐵, 𝐹,𝑘, 𝜎

unknown 𝑓(∗)

assume

𝐴> 0, 𝐵> 0, 𝑇> 0, 𝑘> 0, 𝜎> 0, 𝐹< 𝐵, 𝐴+ 𝐹> 0,

```math
(∀𝑥−𝐴≤𝑓(𝑥) ≤𝐹), (∀𝑥∀𝑦|𝑓(𝑥) −𝑓(𝑦)| ≤𝑘|𝑥−𝑦|)
```

bound ¯𝑓: 𝑓(𝑥) ≤¯𝑓

controller

𝑦··= min(𝑦, ¯𝑓) ;

((𝑎··= −𝐵) ∪

(?(𝑥+ 𝑣𝑇+ 1

## 2 (𝐴+ 𝐹)𝑇2 + Bdist𝑣+(𝐴+𝐹)𝑇(𝐵−min(𝐹, 𝑦+ 𝑘(𝑣𝑇+ 1 2 (𝐴+ 𝐹)𝑇2) +

𝑘· Bdist𝑣+(𝐴+𝐹)𝑇(𝐵−𝐹))) ≤𝑒) ; 𝑎··=𝐴)

```math
plant 𝑡··= 0 ; {𝑥′ = 𝑣, 𝑣′ = 𝑎+ 𝑓(𝑥),𝑦′ = 𝑘𝑣,𝑡′ = 1 & 𝑡≤𝑇∧𝑣≥0}
```

safe 𝑥≤𝑒

```math
invariant (𝑣≥0) ∧(𝑦≥𝑓(𝑥)) ∧(𝑥+ Bdist𝑣(𝐵−min(𝐹, 𝑦+ 𝑘·Bdist𝑣(𝐵−𝐹))) ≤𝑒)
```

noise 𝜂∼N (0, 𝜎2)

observe 𝜔= 𝑓(𝑥) −𝜂

infer ¯𝑓··= 𝐹; ¯𝑓··= best 𝑖: ¯𝑓𝑖+ 𝑘|𝑥−𝑥𝑖| ; ¯𝑓··= aggregate 𝑖: 𝜔𝑖+ 𝑘|𝑥−𝑥𝑖| and 𝜂𝑖

**Fig. 3. An adaptive shield for a train control system where the railway tracks are assumed to follow an unkown, space-varying slope function. We write Bdist𝑣(𝑏) ≡𝑣2/2𝑏. For simplicity, the train faces a binary choice between acceleration and braking (as in Figure 1 and unlike in Figure 2).**

𝑥+ Bdist𝑣(𝐵−𝐹) ≤𝑒, since we can guarantee an effective braking rate of at least 𝐵−𝐹using the global bound 𝐹on 𝑓. However, a stronger guarantee may result from combining the local bound 𝑦≥𝑓(𝑥) and the fact that 𝑓is 𝑘-Lipschitz. Indeed, since we already know from our naive estimate

that the train can stop within distance Bdist𝑣(𝐵−𝐹), we also know that the value of 𝑓along this trajectory must be upper-bounded by 𝑦+ 𝑘· Bdist𝑣(𝐵−𝐹). This gives us an effective braking rate along the stopping trajectory of 𝐵−(𝑦+ 𝑘· Bdist𝑣(𝐵−𝐹)). In turn, a new stopping distance can be computed from this estimate, yielding the invariant shown in Figure 3. The controller’s acceleration guard follows from the invariant, as it simply ensures that the invariant will still hold after executing the plant for time 𝑇.

So far, we have seen how adaptive shields can be extracted from nondeterministic, parametric controllers. Our next step is to show how inference modules can also be synthesized that are guaranteed to instantiate such parameters from runtime observations in a statistically sound way.

2.4 Inferring Statistically-Sound Bound Parameters In this section, we delve into our proposed inference strategy language, which is used to specify nondeterministic inference strategies for instantiating bound parameters at runtime. Inference strategies are introduced by the infer keyword. We consider the strategy from Figure 3 as an example (the strategy from Figure 2 is analyzed in the extended version of this paper [11, Appendix E.1]). An inference strategy consists of a sequence of inference assignments, where each assignment computes a value for a particular bound parameter and updates this parameter whenever the new value is tighter than the old one. Our language supports three forms of assignments, which are all

<!-- page 7 -->

Adaptive Shielding via Parametric Safety Proofs 109:7

represented in the strategy from Figure 3. Each assignment yields a proof obligation that establishes its soundness.

· · · ∧(∀𝑥(−𝐴≤𝑓(𝑥) ≤𝐹)) ∧· · · →𝑓(𝑥) ≤𝐹.

The validity of this obligation establishes the inequality 𝑓(𝑥) ≤𝜔𝑖+ 𝑘|𝑥−𝑥𝑖| + 𝜂𝑖for every triple

(𝑥𝑖,𝜔𝑖,𝜂𝑖) in the agent’s history. This does not directly give us a usable bound since 𝜔𝑖and 𝜂𝑖are random variables, only the first one of which is observed. However, given a tolerance-level of 𝜀, we can use the standard tail bound on Gaussians to establish a concrete upper-bound on 𝑓(𝑥) that holds with probability at least 1 −𝜀. Here, we get the upper-bound 𝑏𝑖≡𝜔𝑖+𝑘|𝑥−𝑥𝑖| +𝜎·𝑧𝜀, where 𝑧𝜀≡

√

## 2 · erf -1(1 −2𝜀) and erf -1 is the inverse of the error function [6]. Indeed:

P{𝑓(𝑥) > 𝑏𝑖} ≤P{𝜔𝑖+ 𝑘|𝑥−𝑥𝑖| + 𝜂𝑖> 𝑏𝑖} = P{𝜂𝑖> 𝜎· 𝑧𝜀} = 𝜀.

The first inequality above is a consequence of Equation 3, the middle equality holds by substituting the definition of 𝑏𝑖, and the last equality holds by definition of the error function.

∑︁

𝑏𝜆,𝜀≡

𝜆𝑖· (𝜔𝑖+ 𝑘|𝑥−𝑥𝑖|) +

𝑖

```math
The proof is similar to the one for Equation 3. We have 𝑓(𝑥) > 𝑏→𝜔𝑖+ 𝑘|𝑥−𝑥𝑖| + 𝜂𝑖> 𝑏for all 𝑖
and 𝑏. Thus, taking a convex combination, we have 𝑓(𝑥) > 𝑏→Í
```

∑︁

P{𝑓(𝑥) > 𝑏𝜆,𝜀} ≤P

𝜆𝑖(𝜔𝑖+ 𝑘|𝑥−𝑥𝑖| + 𝜂𝑖) > 𝑏𝜆,𝜀

𝑖

### √︃Í

where 𝜎′ ≡𝜎

𝑖𝜆2

𝑖𝜆𝑖𝜂𝑖, which is a zero-mean Gaussian provided that the choice of 𝜆is uninformed by – and thus independent from – the values of 𝜂𝑖and 𝜔𝑖.

𝑖is the standard deviation of Í

The first assignment ¯𝑓··= 𝐹indicates that the global bound 𝐹can always be used as a local bound on 𝑓(𝑥). Its soundness is justified by the validity of the following proof obligation, which is automatically generated by our framework and to be proved by the user:

Here, the right-hand-side of the implication is simply the definition of ¯𝑓, where ¯𝑓has been substituted into the assignment’s right-hand-side. The left-hand-side consists of the global assumptions, from which only the relevant ones are shown here. The second assignment ¯𝑓··= best 𝑖: ¯𝑓𝑖+𝑘|𝑥−𝑥𝑖| indicates that any previously established local bound ¯𝑓𝑖induces a new bound ¯𝑓𝑖+ 𝑘|𝑥−𝑥𝑖| for the current state. The associated proof obligation is:

```math
(∀𝑥∀𝑦|𝑓(𝑥) −𝑓(𝑦)| ≤𝑘|𝑥−𝑦|) ∧(𝑓(𝑥𝑖) ≤¯𝑓𝑖) →𝑓(𝑥) ≤¯𝑓𝑖+ 𝑘|𝑥−𝑥𝑖|,
```

where all irrelevant assumptions have been removed for clarity. To a first approximation, the semantics of this assignment is to compute one such bound for every element in the agent’s history and assign the tightest one to ¯𝑓if it beats its current value. The third assignment ¯𝑓··= aggregate 𝑖: 𝜔𝑖+ 𝑘|𝑥−𝑥𝑖| and 𝜂𝑖is most interesting and the one that performs statistical inference from observations. To understand it better, let us start from the associated proof obligation:

```math
(∀𝑥∀𝑦|𝑓(𝑥) −𝑓(𝑦)| ≤𝑘|𝑥−𝑦|) ∧(𝜔𝑖= 𝑓(𝑥𝑖) −𝜂𝑖) →(𝑓(𝑥) ≤𝜔𝑖+ 𝑘|𝑥−𝑥𝑖| + 𝜂𝑖).
(3)
```

Such a probabilistic bound may be acceptable in cases where measurement noise is small. However, when 𝜎is large, it may be unacceptably conservative. Fortunately, we can get tighter bounds by aggregating multiple independent observations together. More precisely, consider some nonnegative coefficients 𝜆𝑖that sum up to one. Then, one can show that the following is a bound on 𝑓(𝑥) with probability at least 1 −𝜀:

```math
√︄∑︁
```

𝜆2

```math
𝑖· 𝜎· 𝑧𝜀.
(4)
```

𝑖

𝑖𝜆𝑖(𝜔𝑖+ 𝑘|𝑥−𝑥𝑖| + 𝜂𝑖) > 𝑏for all 𝑏. As a consequence:

∑︁

```math
= 𝜀,
(5)
```

𝜆𝑖𝜂𝑖> 𝜎′𝑧𝜀

### = P

𝑖

<!-- page 8 -->

109:8 Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent

Human Expert

Verified Shield Agent

safety budget

designs

Inference module

Inference policy

inference action

how much budget to spend? how to weight observations? parameter instantiation

Shield Specification

• dL model with unknowns • parametric bounds • observation slots • inference strategy

Control policy

Controller

monitor

how to gather knowledge and maximize rewards?

action proposal

compiles to

safe?

state reward

Fallback

Proof Obligations

policy

proves

action

• invariant validity • controller totality • parameter monotonicity • inference soundness

Physical World

observations

**Fig. 4. Adaptive Shielding Overview Diagram**

The bound obtained in Equation 4 is the sum of two terms. Minimizing the first term requires putting all the weight on the closest measurement, where 𝑘|𝑥−𝑥𝑖| is smallest. On the other hand, minimizing the second term requires spreading the weights uniformly between measurements, resulting in a value of (𝜎· 𝑧𝜀)/√𝑛, where 𝑛is the number of considered measurements. Finding the right tradeoff can be subtle and situation-dependent. Similarly, the value chosen for 𝜀at every control cycle must be substracted from a global safety budget, whose proper management constitutes an important challenge. Fortunately, our framework does not force such choices on the shield designers. Rather, it enables the specification of nondeterministic inference strategies, where the choice of 𝜀and 𝜆is determined at each control cycle by a non-soundness-critical inference policy that can be learned similarly to the control policy.

The aggregate construct from our inference strategy language allows generalizing the reasoning above to a large class of bounds and distributions. Provided a symbolic bound that can be expressed as the sum of an observable component and of a noise component (syntactically separated using the and keyword), aggregate computes a weighted average of multiples instances of such bounds, using probabilistic tail inequalities to handle the aggregated noise term. More generally, a strategy written in our proposed inference languages can be compiled into one proof obligation per inference assignment, along with an inference module that integrates with an inference policy at runtime.

2.5 System Overview Figure 4 provides a diagrammatic summary of our proposed framework for designing adaptive shields. In this framework, human experts are offered a domain-specific language for specifying shields in the form of parametric dL models coupled with nondeterministic inference strategies. A specification written in this language can be automatically compiled into a shield and into a series of proof obligations that are sufficient in establishing its soundness. All obligations are dL formulas, which can be discharged automatically in many cases but also proved interactively in a proof assistant such as KeYmaera X [14]. Obligations include the following:

• The proposed invariant must be preserved when running the controller and the plant in sequence, assuming that all assumptions and bounds hold initially. • The proposed invariant and the global bounds must imply the postcondition.

<!-- page 9 -->

Adaptive Shielding via Parametric Safety Proofs 109:9

Hybrid Program: 𝛼, 𝛽::= 𝑥··=𝑒| 𝑥··= ∗| ?𝑃| 𝑥′ = 𝑓(𝑥) & 𝑄| 𝛼∪𝛽| 𝛼; 𝛽| 𝛼∗

```math
Formula:
𝑃,𝑄::= 𝜃1 ∼𝜃2 | ∀𝑥𝑃| ∃𝑥𝑃| [𝛼]𝑃| ⟨𝛼⟩𝑃| ¬𝑃| 𝑃∨𝑄| 𝑃∧𝑄| 𝑃→𝑄
```

Term: 𝜃::= 𝑟| 𝑥| 𝑓(𝜃1, . . . ,𝜃𝑛) | |𝜃| | 𝜃1 ⊙𝜃2

```math
Number literal: 𝑟∈R
Variable: 𝑥∈Var
Function symbol: 𝑓∈Symb
```

```math
Term comparison: ∼∈{=, < , ≤, ≥, >}
Arithmetic operator: ⊙∈{+, ×, min, max}
```

```math
𝑛∈N (R𝑛→R)
Interp ≡Symb →Fun
VState ≡Var →R
```

Fun ≡Ð

```math
⟦𝛼⟧: Interp →P(VState × VState)
⟦𝑃⟧: P(Interp × VState)
⟦𝜃⟧: Interp × VState →R
```

**Fig. 5. Syntax and semantics of dL. P(·) denotes the powerset operator.**

• The nondeterministic controller must be total, in the sense that at least one action should be available in any state where the invariant and bounds are true. • All inference assignments must be sound. In the particular case where no functional unknowns are used and all differential equations admit an analytical solution expressible as a multivariate polynomial, all generated proof obligations are decidable. In general, manual proof assistance may be required for certain obligations. Notably, dL has proved effective at reasoning about unsolvable differential equations [23, 35].

The generated shield consists of three components. The first one is an inference module that is extracted from the expert-defined, nondeterministic inference strategy. The other two are a controller monitor and a fallback policy, both of which are extracted from the nondeterministic dL controller. At runtime, an untrusted agent interacts with the physical world under the protection of the shield, which overrides any proposed action that is not validated by the controller monitor using its fallback policy. The inference module is tasked to instantiate the model’s bound parameters, which the controller monitor and the fallback policy depend on. The inference module is guided by the agent’s inference policy, which provides hints on how the safety budget should be spent and how observations should be weighted when building aggregates. The safety budget is initialized with the system’s tolerated probability of failure, which is typically a small value such as 10−6. In cases where not enough budget remains to honor the inference policy’s recommendation, the inference module skips the associated inference assignment.

Importantly, the inference policy must not depend on the value of the observations processed by the inference module and must only base its decisions on the availability of these observations and on features of their associated states. Intuitively, this restriction prevents the agent from 𝑝-hacking its way to unsafety [30]. Indeed, it would be unsound for the agent to make several measurements of the same quantity and then discard all measurements but the most favorable one. Another requirement enforced by the inference module is that the same observation cannot be reused across control cycles. Indeed, allowing the reuse of observations across control cycles enables an indirect form of cherry-picking since the next state after each control cycle may be influenced by the observations made during this cycle and thus carry some amount of information about it.

## 3 Background

### 3.1 Differential Dynamic Logic

Differential dynamic logic (dL) [31, 32] is designed specifically to verify hybrid systems with both discrete and continuous dynamics. The syntax and semantics of dL is summarized in Figure 5. A state is defined as a mapping from variable names to real values. An interpretation is defined as a

<!-- page 10 -->

109:10 Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent

mapping from function symbols to real functions of proper arity (possibly zero). The semantics of a hybrid program 𝛼can be defined by induction on 𝛼. For 𝐼an interpretation, ⟦𝛼⟧(𝐼) denotes the set of all pairs of states (𝑠1,𝑠2) such that 𝑠2 is reachable from 𝑠1 by executing 𝛼. We provide an intuitive summary of such semantics in Table 1 but formal definitions can be found in the literature [32]. The semantics ⟦𝑃⟧of a formula 𝑃is defined as the set of all (𝐼,𝑠) pairs such that 𝑃is true in state 𝑠and under interpretation 𝐼. It follows naturally from first-order logic. In addition, [𝛼]𝑃is true if and only if 𝑃is true after all runs of the hybrid program 𝛼and ⟨𝛼⟩𝑃is true if and only if there exists a run of the hybrid program 𝛼after which 𝑃is true. Atomic formulas consist in comparisons of terms. The semantics ⟦𝜃⟧of a term 𝜃maps a pair of an interpretation and a state to a real value. A formula 𝑃is said to be valid (written ⊨𝑃) if it is true in all states and interpretations.

3.2 Notations for Valuations Given a set of variables 𝑉, a valuation of 𝑉is defined as a function 𝜌: 𝑉→R that maps each variable in𝑉to a value. Moreover, a partial valuation of𝑉is defined as a partial function 𝜌′ : 𝑉⇀R that attributes values to a subset dom 𝜌′ of variables from 𝑉(note the special arrow symbol for partial functions). We denote {} an empty valuation. Moreover, if 𝑣and 𝑣′ are valuations of two disjoint subsets of variables 𝑉and 𝑉′, we write 𝑣∪𝑣′ the valuation of 𝑉∪𝑉′ induced by 𝑣and 𝑣′.

### 3.3 Reinforcement Learning

Reinforcement learning (RL) is about learning to make decisions in an environment in such a way to maximize rewards. Environments are typically represented using Markov Decision Processes (MDPs) [41]. An MDP is defined by a tuple ⟨𝑆,𝐴, 𝑃, 𝑅,𝛾⟩where 𝑆is the state space, 𝐴is the action space, and 𝑃: 𝑆× 𝐴→D(𝑆) is the transition function, which maps any state-action pair to a probability distribution over new states. 𝑅: 𝑆× 𝐴× 𝑆→R is the reward function, which describes the reward associated with a specific state-action pair and a specific next state. Finally, 𝛾∈(0, 1) is the factor by which future rewards are discounted at each time step. The goal of RL is to find an optimal policy 𝜋: 𝑆→D(𝐴) for the agent to maximize the expected discounted sum of future rewards: E𝜋

. In the most common model-free RL setting, 𝑃and 𝑅are unknown and the agent accesses samples of these by directly interacting with the environment.

Í∞

𝑖=0 𝛾𝑖𝑅(𝑠𝑖,𝑎𝑖)

### 3.4 Safe Reinforcement Learning via Shielding

This work builds on the Justified Speculative Control framework (JSC) [15], which leverages models written in dL to shield reinforcement learning agents by only allowing provably-safe control actions. JSC crucially relies on the ability to extract monitors [29] from nondeterministic dL controllers. To define those monitors [29], we need to bridge dL models with reinforcement learning environments. Thus, consider a dL model of the kind defined in Equation 1. Such a model induces a state space State ≡FV(Model) →R, where a state maps each free variable occuring in the model to a real value. In addition, the controller Ctrl induces an action space that can be defined inductively:

A⟦𝛼∪𝛽⟧≡A⟦𝛼⟧⊎A⟦𝛽⟧, A⟦𝛼; 𝛽⟧≡A⟦𝛼⟧× A⟦𝛽⟧, A⟦𝑥··= ∗⟧≡R, A⟦𝑥··=𝑒⟧≡A⟦?𝑄⟧≡1.

In this definition, 𝑋⊎𝑌≡{(left,𝑥) : 𝑥∈𝑋} ∪{(right,𝑦) : 𝑦∈𝑌} denotes the disjoint union of sets 𝑋and 𝑌and 1 ≡{•} denotes a set with a single element. Intuitively, an action records a sequence of choices that uniquely characterizes a run of the controller. For example, the discrete controller defined in Equation 2 has an action space A⟦Ctrl⟧= 1 ⊎(1 × 1), which is isomorphic to a 2-element set containing a braking and an accelerating action. The continuous controller used in Figure 2 has an action space A⟦Ctrl⟧= R × 1. For any state 𝑠∈State and action 𝑎∈A⟦Ctrl⟧, we write E⟦Ctrl⟧(𝑠,𝑎) for the state that results from executing Ctrl while performing the sequence of choices encoded in 𝑎. A formal definition is provided in the extended version of this paper [11,

<!-- page 11 -->

Adaptive Shielding via Parametric Safety Proofs 109:11

Appendix D.1]. From the structure of a nondeterministic controller, one can extract a controller monitor that takes as an input a state and an action and returns a Boolean value indicating whether or not the action is permissible.

Lemma 3.1 (Existence of a controller monitor and fallback policy). Let Ctrl be a nondeterministic controller in the form of a dL hybrid program that is free of loops, modalities, differential equations, quantifiers and function symbols of nonzero arity. Then, there exists a computable function M⟦Ctrl⟧: (FV(Ctrl) →R) × A⟦Ctrl⟧→{true, false} that we call controller monitor and such that for all state 𝑠and action 𝑎, M⟦Ctrl⟧(𝑠,𝑎) = true if and only if (𝑠, E⟦Ctrl⟧(𝑠,𝑎)) ∈⟦Ctrl⟧({}). In addition, given any formula Inv such that ⊨Inv →⟨Ctrl⟩true (i.e. there exists an outgoing controller transition for all states in Inv), there exists a computable function F ⟦Ctrl⟧: (FV(Ctrl) → R) →A⟦Ctrl⟧that we call fallback policy and such that for all state 𝑠such that ({},𝑠) ∈⟦Inv⟧, (𝑠, E⟦Ctrl⟧(𝑠, F ⟦Ctrl⟧(𝑠)) ∈⟦Ctrl⟧({}).

In our train example from Figure 2 (with a continuous control input), the action space A⟦Ctrl⟧is isomorphic to R. An action is a commanded acceleration𝑢and the runtime monitor M⟦Ctrl⟧simply evaluates the two tests featured in the controller definition for the selected value of 𝑢: it checks that both formula (−𝐵≤𝑢≤𝐴) and formula (𝑥+ 𝑣𝑇+ ( ¯𝜃𝑢+ ¯𝜑)𝑇2/2 + (𝑣+ ( ¯𝜃𝑢+ ¯𝜑)𝑇)2/2(¯𝜃𝐵−¯𝜑) ≤𝑒) evaluate to true in the current state and for the current values of bound parameters ¯𝜃, ¯𝜃and ¯𝜑. In our train example from Figure 3 (with a binary control input), the action space is isomorphic to {brake, accelerate}. The braking action is always allowed. To determine whether or not to allow acceleration, the monitor evaluates the test from the associated branch of the nondeterministic controller from Figure 3. In general, controller monitors can be derived from shield specifications via a simple syntactic transformation. We formalize this transformation and provide a proof of Lemma 3.1 in the extended version of this paper [11, Appendix D]. The KeYmaera X toolchain features a tool called ModelPlex [29] for extracting executable controller monitors from dL models.

The existence of a fallback policy is guaranteed by the assumption ⊨Inv→⟨Ctrl⟩true, which indicates that there exists at least one way to resolve the nondeterministic choices in Ctrl in such a way to pass all tests (i.e. not trigger any monitor alert). The corresponding action can be computed systematically by solving a decidable SMT problem, hence the existence of a decidable fallback policy (see the extended version of this paper for details [11, Appendix D.3]). However, for the sake of monitoring efficiency, tools like ModelPlex require the user to specify an explicit fallback policy on a case-by-case basis. Doing so is never a problem in practice since proving ⊨Inv→⟨Ctrl⟩true requires characterizing such a policy anyway. In particular, an explicit fallback policy can be automatically extracted from a constructive proof of this formula [7]. In our train examples, a possible fallback policy is to brake with maximal force, which corresponds to action −𝐵in the continuous case and action “brake” in the discrete case.

## 4 Adaptive Shielding

### 4.1 Shield Specifications

We define a language to specify adaptive shields via parametric safety models. Models can assume a set of parametric bounds on a number of unknown quantities. The derived runtime controller is parametric in these same bounds, which are maintained and improved at runtime by a derived inference module. Examples of shield specifications are available in Figures 2 and 3. Formally, a shield specification is defined by a tuple of the following elements:

Const: a set of constants, which are dL symbols of arity zero whose value is known at runtime. Unknown: a set of 𝑢𝑛𝑘𝑛𝑜𝑤𝑛𝑠, which are dL symbols of fixed arity, whose value is not known at

runtime and can be estimated by the inference module using observations.

<!-- page 12 -->

109:12 Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent

Assum: a set of assumptions, which are dL formulas representing global assumptions about the

constants and unknowns. Assumptions can feature symbols but no free variables. When clear from the context, we also write Assum for the conjunction of all assumptions. StateVar: a set of state variables, which are dL variables used to represent model state. In our

concrete syntax, the set of state variables is inferred as the set of all mentioned free variables that are not parameters, observation variables or noise variables (see below). Param, Dir, Bound: a set of parametric bounds. Param is a set of dL variables called bound pa-

rameters (or parameters for short). Each parameter 𝑝is mapped to a dL formula Bound𝑝 that is either monotone or anti-monotone with respect to 𝑝, depending on bound direction Dir𝑝∈{up, lo}. In our concrete syntax, the bound direction can be omitted whenever easily inferrable. For𝜃a dL term, we write Bound𝑝[𝜃] for the result of substituting𝜃for 𝑝in Bound𝑝. If Dir𝑝= up, we call Bound𝑝an upper-bound and we mandate that it is monotone, meaning that ⊨∀𝑥𝑦(𝑥≤𝑦→Bound𝑝[𝑥] →Bound𝑝[𝑦]). If Dir𝑝= lo, we call Bound𝑝a lower-bound and we mandate that it is anti-monotone: ⊨∀𝑥𝑦(𝑥≤𝑦→Bound𝑝[𝑦] →Bound𝑝[𝑥]). Bound𝑝can feature constants, unknowns and state variables. It cannot feature any parameter other than 𝑝. It is said to be local if it contains a free occurence of a state variable. Otherwise, it is said to be global. The associated parameter 𝑝is also called local or global accordingly. We write LParam the set of local parameters and GParam the set of global parameters. We write GBound ≡Ó

𝑝∈GParam Bound𝑝for the conjunction of all global bounds. Finally, when clear from the context, we use the notational shortcut Bound ≡Ó

```math
𝑝∈Param Bound𝑝for the conjunc-
tion of all bounds. For 𝑏∈Param ⇀R, we also write Bound[𝑏] ≡Ó
```

𝑝∈dom𝑏Bound𝑝[𝑏(𝑝)]. Ctrl: a controller, in the form of a (nondeterministic) dL hybrid program that is free of loops,

modalities, differential equations and quantifiers. The controller can involve constants, parameters and state variables but no unknowns. Only state variables can be modified. For 𝑐∈Const →R and 𝑏∈Param →R, we write Ctrl[𝑐,𝑏] for the result of substituting all constants and parameters in Ctrl by their value according to 𝑐and 𝑏. Thus, Ctrl[𝑐,𝑏] has no symbols and its free variables are all in StateVar. For any (𝑐,𝑏) pair, Lemma 3.1 guarantees that a controller monitor and a fallback policy can be extracted from Ctrl[𝑐,𝑏]. Plant: a dL hybrid program that represents the physical environment. As opposed to the controller,

it can feature unknowns but no parameters. Only state variables can be modified. Safe: a dL formula that represents the safety constraint under which the system must operate. It

can involve constants, unknowns and state variables but no parameters, since the safety condition cannot change over time as knowledge is gathered. Inv: an invariant, in the form of a dL formula. The invariant can feature constants, state variables

and unknowns but only global parameters. Local parameters are not allowed in the invariant. The following proof obligations are generated that involve the invariant: (1) The invariant must imply the postcondition: ⊨Assum ∧GBound ∧Inv →Safe. (2) The invariant must be preserved: ⊨Assum ∧Bound ∧Inv →[Ctrl ; Plant] Inv. (3) There always exists a safe controller action: ⊨Assum ∧Bound ∧Inv →⟨Ctrl⟩true. (4) The invariant must be monotone with respect to upper-bound parameters and anti-monotone

with respect to lower-bound parameters. NoiseVar, Noise: a set of noise variable declarations. NoiseVar is a set of dL variables that can be

used in the definition of observations and that model samples from mutually independent random variables. Each noise variable 𝜂∈NoiseVar is mapped to an expression Noise𝜂that denotes a probability distribution. NoiseVar𝜂can be either N (𝜃1,𝜃2) for a normal distribution, U(𝜃1,𝜃2) for a uniform distribution or B(𝜃1) for a Bernouilli distribution. In all cases, 𝜃1 and

<!-- page 13 -->

Adaptive Shielding via Parametric Safety Proofs 109:13

𝜃2 are dL terms that can feature constants and state variables. We write ⟦Noise⟧: (Const→ R) →NoiseVar →Distr(R) for the semantic denotation of Noise. ObsVar, Obs: a set of observations. ObsVar is a set of dL variables called observation variables. Each

observation variable 𝜔is mapped to a defining dL term Obs𝜔that may feature constants, unknowns, state variables and noise variables (but no bound parameter). Infer: an inference strategy, which defines an inference module that issues concrete values for

bound parameters at runtime, using an external inference policy for guidance. The inference strategy can be defined in a custom, domain-specific language that is explained in details in Section 5. Before we dive into this language though, we characterize the abstract requirements that an inference module must fulfill in Section 4.2. The soundness of our proposed inference strategy language can then be established against these requirements.

4.2 Symbolic Bound Instantiations An inference strategy Infer induces an action space A⟦Infer⟧for the agent’s inference policy, which is defined rigorously in Section 5. In particular, inference actions associated with a single aggregate assignment are (𝜀, 𝜆) pairs, as seen in Section 2.4. An inference strategy denotes a function ⟦Infer⟧: A⟦Infer⟧→List(Param × SBInst × [0, 1]) that maps an inference action to a list of symbolic inference assignments. A symbolic inference assignment consists of a triple (𝑝,𝑒,𝜀) of a bound parameter 𝑝, a symbolic bound instantiation 𝑒and a failure probability 𝜀.

To illustrate the concept of a symbolic bound instantiation, consider the following example statement from Section 2.4: “ ¯𝑓··= aggregate 𝑖: 𝜔𝑖+ 𝑘|𝑥−𝑥𝑖| and 𝜂𝑖”. Provided a (𝜀, 𝜆) pair and a history of states and observations, the right-hand-side of this statement can be evaluated into a concrete, numerical value proposal for ¯𝑓. This is done in two stages, the first one of which being the computation of a symbolic bound instantiation 𝑒for ¯𝑓. For example, if 𝜀= 10−8, 𝜆2 = 0.3, 𝜆5 = 0.7 and 𝜆𝑖= 0 for all 𝑖∉{2, 4}, we obtain the following symbolic bound instantiation:

```math
𝑒≡0.3 × (𝜔2 + 𝑘|𝑥−𝑥2|) + 0.7 × (𝜔5 + 𝑘|𝑥−𝑥5|) + CDF -1
```

```math
𝜂2,𝜂5∼N(0, 𝜎2) (0.3𝜂2 + 0.7𝜂5, 10−8).
(6)
```

In the expression above, the CDF -1 construct provides a symbolic representation of the inverse tail function of a probability distribution, also called its inverse complementary cumulative distribution function – hence the notation. Given a random expression and a tolerance 𝜀, CDF -1 returns the best upper-bound obtainable on this expression that is true with probability 1 −𝜀at least. For example, we have CDF -1

𝑋∼U(0,1) (𝑋+ 1,𝜀) = 2 −𝜀for all 𝜀∈[0, 1] since P𝑋∼U(0,1){𝑋+ 1 > 2 −𝜀} = 𝜀. Details on how to compute or approximate the CDF -1 operator numerically are available in the extended version of this paper [11, Appendix E.2].

Provided some values for the constant symbols, for the current state and for past states and observations from the agent’s history, the symbolic bound instantiation from Equation 6 can be in turn evaluated into a real number. There are two reasons for performing such staging. First, it makes it very clear that ⟦Infer⟧has no access to the actual observation values when building 𝑒, which is critical for soundness (as previously discussed in Section 2.4). Second, this pushes the orthogonal challenge of evaluating CDF -1 outside of the core inference machinery.

4.2.1 Formal Syntax and Semantics. A sketch of a formal syntax and semantics for symbolic bound instantiations is provided in Figure 6. A symbolic bound instantiation 𝑒can be a dL term 𝜃, the sum of two other symbolic bound instantiations, an application of the CDF -1 operator or a guarded expression (𝑒when 𝑃), where 𝑃is a quantifier-free, modality-free dL formula. Importantly, the evaluation of a symbolic bound instantiation can fail and return a special value ⊥. It does so when attempting to access the value of an undefined variable or symbol, or when evaluating (𝑒when 𝑃) while 𝑃evaluates to false. Support for ⊥is important since our framework does not mandate

<!-- page 14 -->

109:14 Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent

𝛿::= N (𝜃1,𝜃2) | U(𝜃1,𝜃2) | B(𝜃) 𝑒::= 𝜃| 𝑒1 + 𝑒2 | 𝑒when 𝑃| CDF -1

𝜂1∼𝛿1···𝜂𝑛∼𝛿𝑛(𝜃1,𝜃2)

```math
⟦𝑒⟧: (Symb →Fun) × (Var ⇀R) →R ∪{⊥}
```

⟦𝜃1⟧(𝐼, 𝑣∪(∪𝑖𝜂𝑖)) > 𝑏 ≤⟦𝜃2⟧(𝐼, 𝑣)

### ⟦CDF -1

n

o

𝑏: P𝜂𝑖∼⟦𝛿𝑖⟧(𝐼,𝑣)

𝜂1∼𝛿1···𝜂𝑛∼𝛿𝑛(𝜃1,𝜃2)⟧(𝐼, 𝑣) ∈

∪{⊥}

**Fig. 6. Syntax and semantics of symbolic bound instantiations. We only show the contract that CDF -1 must fulfill for soundness. Concrete implementations must optimize for small, real return values.**

observations to be available at each cycle, making some observation variables possibly unassigned. In addition, “ when ” is necessary for our inference strategy language to support conditionally sound bounds, which we use in the example from Figure 2 and discuss further in Section 5.

4.2.2 Indexed Variables. Finally, symbolic bound instantiations can contain special dL variables, whose name contains an integer index (i.e. 𝜔2). Semantically, there is nothing special about such variables and we can just regard them as normal variables following a naming convention. The only thing that matters is that for any 𝑥∈𝑉and 𝑖∈N, 𝑥𝑖∉𝑉where 𝑉≡StateVar ∪Param ∪ ObsVar∪NoiseVar. We also introduce some notations to ease the manipulation of indexed variables. For 𝑣a partial valuation over 𝑉and 𝑖∈N, we write 𝑣(𝑖) ≡{𝑥𝑖↦→𝑟: 𝑣(𝑥) = 𝑟} the same valuation in which all domain variables are tagged with index 𝑖. For example, if 𝑥,𝑦∈𝑉and 𝑣= {𝑥↦→0,𝑦↦→1}, then 𝑣(2) = {𝑥2 ↦→0,𝑦2 ↦→1}. In addition, for 𝑃a formula with variables in 𝑉, we write 𝑃(𝑖) the formula that results from 𝑃after tagging every free variable with index 𝑖. Finally, we also allow the use of symbolic names as indices. For example, in the inference assignment “aggregate 𝑖: 𝜔𝑖+ 𝑘|𝑥−𝑥𝑖| and 𝜂𝑖”, 𝜔𝑖is a normal dL variable whose name follows a particular

convention. We introduce a special syntactic transformation for “instantiating” symbolic indices in formulas. For example, if 𝑃≡𝑥𝑖+ 𝑥𝑗> 0, we write 𝑃[𝑖, 𝑗\2, 3] ≡𝑥2 + 𝑥3 > 0.

### 4.3 Soundness of Symbolic Inference Assignments

As mentioned in the previous section, an inference strategy denotes a function ⟦Infer⟧: A⟦Infer⟧→ List(Param×SBInst×[0, 1]) that maps an inference action to a list of symbolic inference assignments. Our proposed inference strategy language is sound in the sense that any strategy expressed with it produces sound assignments by construction. In turn, a symbolic inference assignment (𝑝,𝑒,𝜀) is sound if 𝑒evaluates to a “correct” instantiation of 𝑝with probability at least 1 −𝜀. To make this definition more precise, we need a couple of preliminary definitions:

• A state is defined as a valuation of the state variables: State ≡StateVar →R. • A bound instantiation is a partial valuation of the parameters: Inst ≡Param ⇀R. • An observation availability set is a subset of observation variables indicating what observation were made at one point in time: ObsAvail ≡P(ObsVar). We can now define the notion of soundness for symbolic inference assignments. Intuitively, (𝑝,𝑒,𝜀) is sound if and only if for any possible history of states, observations and bound instantiations and for any intepretation of the model unknowns, updating an instantiation 𝑏by assigning the value of 𝑒to 𝑝preserves the truth of Bound[𝑏] with probability at least 1 −𝜀. The challenge in formalizing this intuition is to precisely characterize what counts as a possible history. We do so in Definition 4.1, building a valuation 𝑣that stands for an arbitrary, consistent history.

Definition 4.1 (Sound inference assignment). A symbolic inference assignment (𝑝,𝑒,𝜀) is said to be sound if and only if for any 𝑐∈Const →R, 𝑢∈Unknown →Fun, 𝑛∈N, (𝑠1 . . .𝑠𝑛) ∈State𝑛, (𝑧1 . . .𝑧𝑛) ∈ObsAvail𝑛and (𝑏1 . . .𝑏𝑛) ∈Inst𝑛such that (𝑐∪𝑢,𝑠𝑖) ∈⟦Assum ∧Inv ∧Bound[𝑏𝑖]⟧

<!-- page 15 -->

Adaptive Shielding via Parametric Safety Proofs 109:15

for all 𝑖≤𝑛, we have:

```math
P {(𝑐∪𝑢,𝑠𝑛) ∉⟦Bound[𝑏𝑛[𝑝←𝑟]]⟧} ≤𝜀
```

∪Ð

where 𝑟= ⟦𝑒⟧(𝑐, 𝑣), 𝑣= 𝑠𝑛∪𝑏𝑛

### 4.4 Compatible Environments

⟨𝑆,𝐴, 𝑃, 𝑅,𝛾⟩,𝜑s,𝜑a,𝜑−1

a = id. • 𝑐: Const →R is an interpretation of the shield’s constant symbols. • 𝑢: Unknown →Fun is an interpretation of the shield’s unknown symbols. • 𝛼: 𝑆→P(ObsVar) is an observation availability function. • 𝜇: 𝑆→D(ObsVar →R) is an observation measurement function.

In addition, the following should hold:

𝑠∈𝑆and 𝑜∈ObsVar→R, then P𝜂∼⟦Noise⟧(𝑐){⟦Obs⟧(𝑐∪𝑢,𝜑s(𝑠) ∪𝜂) = 𝑜} = 𝜇(𝑠)(𝑜).

4.5 Shielded Environments and Main Safety Theorem We define our main shielding algorithm by describing how a shield acts as a wrapper around compatible environments, resulting into shielded environments that are amenable to RL themselves and in which no unsafe state is reachable by construction.

ˆ𝑆, ˆ𝐴, ˆ𝑃, ˆ𝑅,𝛾

where:

1≤𝑖≤𝑛𝑠𝑖(𝑖) ∪𝑏𝑖(𝑖) ∪𝑜𝑖(𝑖), 𝑜𝑖= {𝜔↦→⟦Obs𝜔⟧(𝑐∪𝑢,𝑠𝑖∪𝜂𝑖) : 𝜔∈Param ∩𝑧𝑖} for all 1 ≤𝑖≤𝑛, and 𝜂1 · · ·𝜂𝑛∼⟦Noise⟧(𝑐) i.i.d.

A shield acts as a buffer between an untrusted agent and a compatible environment. By compatible, we mean that the environment must conform to the assumptions made by the shield specification, without which no safety guarantee can be provided. The following definition formalizes this notion.

Definition 4.2 (Compatible environments). Consider a shield specification ⟨Const, . . . , Infer⟩. A compatible environment is a tuple

where:

a ,𝑐,𝑢, 𝛼, 𝜇

• ⟨𝑆,𝐴, 𝑃, 𝑅,𝛾⟩is a Markov Decision Process. • 𝜑s : 𝑆→State is a state mapping function that maps environment states to shield states. • 𝜑a : 𝐴→A⟦Ctrl⟧is a surjective action mapping. • 𝜑−1 a : A⟦Ctrl⟧→𝐴is a reverse action mapping such that 𝜑a ◦𝜑−1

(1) The shield’s plant correctly models the environment’s transition function: for all 𝑠,𝑠′ ∈𝑆,

𝑎∈𝐴and 𝑏∈Inst, assuming that (1) 𝑠′ ∈supp(𝑃(𝑠,𝑎)) (i.e (𝑠,𝑎,𝑠′) is a valid transition), (2) (𝑐∪𝑢,𝜑s(𝑠) ∪𝑏) ∈⟦Assum ∧Bound ∧Inv⟧, and (3) (𝜑s(𝑠) ∪𝑏,𝑠′′ ∪𝑏) ∈⟦Ctrl⟧(𝑐) where 𝑠′′ ≡E⟦Ctrl[𝑐,𝑏]⟧(𝜑s(𝑠),𝜑a(𝑎)), then we have (𝑠′′,𝜑s(𝑠′)) ∈⟦Plant⟧(𝑐∪𝑢). (2) The observation measurement function behaves consistently with Noise and Obs: for all

A compatible environment extends a standard RL environment with a formal mapping between this environment and a shield specification’s underlying model. It also defines some ground-truth values for all unknown symbols, along with two observation functions for acquiring knowledge about those. We choose to have two separate functions, where 𝛼indicates what observations are available in any given state and 𝜇performs an actual measurement of those observations. Such a separation is convenient since the inference policy is allowed to access information about observation availability but cannot access actual observation values.

Definition 4.3 (Shielded environment). Consider a shield specification ⟨Const, . . . , Infer⟩and a compatible environment ⟨⟨𝑆,𝐴, 𝑃, 𝑅,𝛾⟩, . . . , 𝜇⟩(see Definition 4.2). We define the induced shielded environment as an MDP

• A state ˆ𝑠= (𝑠,ℎ,𝑏G,𝜀rem) consists of a state 𝑠from the original environment, a history ℎ, an instantiation of global parameters 𝑏G and a remaining safety budget 𝜀rem ≥0. In turn, a history is a list of (𝑠′,𝑧,𝑏L) triples where 𝑠′ is a state, 𝑧is an observation availability set and

<!-- page 16 -->

109:16 Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent

Algorithm 1 Sampling a transition in a shielded MDP

1: procedure shielded_transition (ˆ𝑠, ˆ𝑎)

```math
2:
𝑠,ℎ,𝑏G,𝜀rem ←ˆ𝑠
⊲Decompose ˆ𝑠∈ˆ𝑆
```

3: 𝑎ctrl,𝑎inf ←ˆ𝑎 ⊲Decompose ˆ𝑎∈ˆ𝐴 4: 𝐵←⟦Infer⟧(𝑎inf) ⊲Get list of symbolic bound assignments 𝐵 5: Ω = {𝜔𝑖∈FV(𝑒) : (𝑝,𝑒,𝜀) ∈𝐵, 𝜔∈ObsVar} ⊲Determine observations to make 6: 𝑛←|ℎ| + 1 ⊲Get index of history element being built

```math
7:
𝑣←𝜑s(𝑠) ∪𝜑s(𝑠)(𝑛) ∪𝑏G ∪𝑏G(𝑛)
⊲Initialize a valuation for 𝐵
8:
for 𝑖∈{𝑖: 𝜔𝑖∈Ω} do
⊲For every relevant step 𝑖in history
9:
𝑠′,𝑧′,𝑏′
```

```math
L ←ℎ𝑖
10:
𝑜←sample 𝜇(𝑠′)
⊲Measure observations for step 𝑖
11:
𝑣←𝑣∪{𝜔𝑖↦→𝑜(𝜔) : 𝜔𝑖∈Ω, 𝜔∈𝑧′}
⊲Update 𝑣with accessible measurements
```

12: 𝑣←𝑣∪𝜑s(𝑠′)(𝑖) ∪𝑏′

```math
(𝑖)
⊲Update 𝑣with history element 𝑖
13:
ℎ←ℎ[𝑖←(𝑠′, {}, 𝑏′
```

L

L)] ⊲Ensure observations are not reused

14: for (𝑝,𝑒,𝜀) ∈𝐵do ⊲For every symbolic bound assignment in 𝐵 15: if 𝜀> 𝜀rem then ⊲If not enough budget remains 16: continue ⊲We skip the assignment

17: 𝜀rem ←𝜀rem −𝜀 ⊲Update the remaining safety budget 18: 𝑟←⟦𝑒⟧(𝑐, 𝑣) ⊲Evaluate symbolic instantiation with 𝑣 19: if 𝑟≠⊥and (𝑝∉dom𝑣or 𝑟< 𝑣(𝑝)) then ⊲Whenever a tighter value is obtained

```math
20:
𝑣←𝑣[𝑝←𝑟][𝑝(𝑛) ←𝑟]
⊲Update 𝑣with the new tighter bound
```

21: 𝑏L ←{𝑝↦→𝑣(𝑝) : 𝑝∈LParam} 22: 𝑏G ←{𝑝↦→𝑣(𝑝) : 𝑝∈GParam} 23: assert dom𝑏L = LParam ⊲Ensure that all local parameters are set 24: ℎ←ℎ· (𝑠, 𝛼(𝑠), 𝑏L) ⊲Add current state to the inference history 25: safe ←M⟦Ctrl[𝑐, 𝑏G ∪𝑏L]⟧ ⊲Instantiate the control monitor 26: fallback ←F ⟦Ctrl[𝑐, 𝑏G ∪𝑏L]⟧ ⊲Instantiate the fallback policy

27: if not safe(𝜑s(𝑠), 𝜑a(𝑎ctrl)) then ⊲When the control action is deemed unsafe 28: 𝑎ctrl ←𝜑−1

fallback(𝜑s(𝑠)) ⊲Override it with a fallback action

a

29: 𝑠←sample 𝑃(𝑠,𝑎ctrl) ⊲Perform the action in the underlying MDP 30: return (𝑠,ℎ,𝑏G,𝜀rem) ⊲Return a new value of ˆ𝑠

```math
𝑏L is a local parameter instantiation. Formally, ˆ𝑆≡𝑆× Hist × (GParam →R) × [0, 1] and
```

Hist ≡List(𝑆× P(ObsVar) × (LParam →R)). • An action ˆ𝑎= (𝑎ctrl,𝑎inf) is defined as a pair of a control action and of an inference action. Formally, ˆ𝐴≡A⟦Ctrl⟧× A⟦Infer⟧. • The transition function 𝑃: ˆ𝑆× ˆ𝐴→D( ˆ𝑆) is defined as in Algorithm 1. • The reward function is lifted from the original MDP: if ˆ𝑠= (𝑠,ℎ,𝑏G,𝜀rem), ˆ𝑎= (𝑎ctrl,𝑎inf) and ˆ𝑠′ = (𝑠′,ℎ′,𝑏′

rem), then ˆ𝑅(ˆ𝑠, ˆ𝑎, ˆ𝑠′) = 𝑅(𝑠,𝑎ctrl,𝑠′).

G,𝜀′

Note that in our definition, a state of the shielded MDP does not contain any information about past observation values. Keeping such knowledge from the agent is crucial for soundness since the agent could otherwise engage in cherry-picking. Instead, the history component of a state only indicates which past observations are available and not used already.

Algorithm 1 rigorously defines the process of sampling a transition from a shielded environment, indirectly defining the behavior of our proposed adaptive shield (see Figure 4 for a synthetic view).

<!-- page 17 -->

Adaptive Shielding via Parametric Safety Proofs 109:17

Lines 4 to 24 describe the execution of the inference module, which computes valuations 𝑏G and 𝑏L for global and local bound parameters respectively while updating the history ℎand the remaining safety budget 𝜀rem. Lines 25 to 28 instantiate the controller monitor and fallback policy using 𝑏G and 𝑏L. If the action proposed by the agent is rejected by the controller monitor, it is overriden via the fallback policy. Finally, line 29, executes the resulting action in the real environment.

Note that we rely on a formalization trick where Algorithm 1 performs observation measurements lazily (Line 10), sometimes on past states, rather than performing them eagerly and storing them. Although physically unrealistic, this formalization enables us to stay within the standard MDP framework that is dominant in RL. Concrete implementations would of course perform observations eagerly and “secretely” cache them, offering the same interface. An alternative choice would have been to define our shielding algorithm using framework of Partially-Observed Markov Decision Processes (POMDPs) [24]. However, doing so would complicate our proofs and definitions for little gain. Finally, instantiating the controller monitor (Line 25) requires every global and local parameter to be mapped to a real value. This trivially holds for global parameters, by definition of a shielded environment state (Definition 4.3). However, this does not obviously hold for local parameters, hence the assertion on Line 23. It is the inference strategy itself that must guarantee the validity of this assertion, which it does by statically enforcing that every local parameter is provided a default value that is independent from observations or other local parameters. In the example from Figure 3, the first assignment ¯𝑓··= 𝐹serves this role. We can now state our main safety theorem (a proof sketch is provided in the extended version of this paper [11, Appendix F.1]).

Theorem 4.4 (Safety of shielded environments). Consider a shield specification ⟨Const, . . . ⟩ and a compatible environment ⟨⟨𝑆, . . . ⟩, . . . , 𝜇⟩(see Definition 4.2). Let ˆ𝐸be the resulting shielded MDP (see Definition 4.3). Then, given a safety budget 𝜀∈[0, 1], an initial global bound instantiation 𝑏∈GParam→R and an initial state 𝑠∈𝑆such that (𝑐∪𝑢,𝜑s(𝑠) ∪𝑏) ∈⟦Assum ∧Bound ∧Inv⟧,

any trace in ˆ𝐸starting with state ˆ𝑠0 = (𝑠, ∅,𝑏,𝜀) is safe with probability at least 1 −𝜀, meaning that (𝑐∪𝑢,𝜑s(𝑠𝑡)) ∈⟦Safe⟧for all state ˆ𝑠𝑡= (𝑠𝑡, . . . ) in the trace.

4.6 Learning in a Shielded Environment Adaptive shields such as defined in Section 4.5 can be used to protect any agent from acting unsafely in its environment, whether or not it is capable of learning and regardless of how it is implemented. This is emphasized by our choice of formalizing shields as environment wrappers, which are agent-agnostic by construction. Still, for the sake of concreteness, it is useful to illustrate the use of Algorithm 1 and Theorem 4.4 in two typical reinforcement-learning scenarios: Learning in a fixed environment. A shielded agent is placed in a fixed, compatible environment.

It ignores the value of unknowns but those are kept constant across training. A total safety budget is defined for the inference module, which must be small enough to make crashes unlikely (as per Theorem 4.4). Initially, the parameter bounds provided by the inference module are very loose and so the shield’s action monitor is equally conservative. However, at each control cycle, the inference module spends some safety budget to improve those bounds, thereby allowing the agent to take increasingly aggressive exploratory moves. When the safety budget is fully spent, the inference module is not allowed to update parameter bounds anymore. However, the agent is still guaranteed to remain safe indefinitely, and in particular as it finishes to optimize its control policy. Section 6 demonstrates this setting by showcasing a train that learns to navigate on a fixed circuit. Meta-learning across a family of environments. In many practical scenarios, autonomous

cyber-physical systems must be capable of quickly adapting to changing environments without training a dedicated policy from scratch. It is thus useful to train an agent across a

<!-- page 18 -->

109:18 Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent

family of environments so that it can generalize across them. Such a meta-learning setting integrates particularly well with our shielding framework. Indeed, we can train a shielded agent through a series of episodes, each of which takes place in a possibly different environment that is nonetheless compatible with the agent’s shield (for possibly different values of the unknowns). At the start of each episode, the inference module is reinitialized and a fixed, per-episode safety budget is granted. In addition to the state information, the agent is given access to the current bound parameters and the remaining safety budget at all times. It must learn to gather suitable information about its environment and adapt its actions accordingly within each episode. In particular, this allows a form of active sensing, where the agent learns to act in such a way to receive useful information from the inference module. This also allows optimizing the behavior of the inference module itself by learning inference policies, as we discuss in Section 5. In the meta-learning setting, Theorem 4.4 is applied at each episode and so a global safety bound can be obtained by multiplying the per-episode safety budget by the number of training episodes. Section 6 explores this setting in three different case studies, including one with a train controller that must learn to quickly adapt to different circuits with different slope profiles.

5 The Inference Strategy Language We define the syntax and semantics of our inference strategy language in Figure 7. An inference strategy is defined as a sequence of inference assignments. Each kind of assignment defines its own action space and the action space for a whole strategy is the product of the action spaces of individual assignments. Three kinds of assignments are supported. Any assignment can be attached a when-clause that restricts its applicability, as illustrated in Figure 2 and in the extended version of this paper [11, Appendix E.1]. A direct assignment “𝑝··= 𝜃” does not require any input from the inference policy and executing it costs no budget. It yields a single symbolic bound instantiation, which is 𝜃itself. An assignment of the form “𝑝··= best 𝑖1, · · · ,𝑖𝑛: 𝜃” expects as an input a list of 𝑛-tuples of history indices and yields one bound instantiation 𝜃[𝑖1, · · · ,𝑖𝑛\ 𝑗1, · · · , 𝑗𝑛] for each tuple

(𝑗1, · · · , 𝑗𝑛). An alternate design would expect no input and consider every possible combination of indices through the current history. However, the number of such combinations may grow intractably large, which explains our current pragmatic choice.

Semantics of aggregate. An assignment of the form “𝑝··= aggregate 𝑖1, · · · ,𝑖𝑛: 𝜃1 and 𝜃2” takes as an input an (𝜀, 𝐷) pair, where 𝜀indicates how much safety budget should be spent and 𝐷is a finite distribution over all 𝑛-tuples of history indices. More precisely, 𝐷is a sequence of

(𝜆, 𝑗) pairs where 𝑗indexes a combination of measurements from history and 𝜆is a positive weight attached to it (Í

𝜆,𝑗∈𝐷𝜆= 1). It yields a single bound instantiation that performs a weighted average over all instances of the observable bound component 𝜃1, while using the CDF -1 operator to handle the noise component 𝜃2. As a requirement, 𝜃1 can contain observation variables but no noise variables, while 𝜃2 can contain noise variables but no observation variables. The semantics of aggregate generalizes our reasoning from Section 2.4 (see Equation 5). Indeed, let us assume that Bound𝑝[(𝜃1 + 𝜃2)[𝑖\𝑗]] is true for any instantiation 𝑗≡(𝑗1, . . . , 𝑗𝑛) of 𝑖≡(𝑖1, . . . ,𝑖𝑛), as guaranteed by the generated proof obligation. Also, let us assume without loss of generality that 𝑝is an upperbound. Since Bound𝑝is monotone in 𝑝and thus convex, we know that Bound𝑝[𝑏∗] is true where 𝑏∗≡Í

𝜆,𝑗∈𝐷𝜆(𝜃1 + 𝜃2)[𝑖\𝑗]. However, 𝑏∗is not known at runtime since 𝜃2 features noise variables that are not observed directly. Instead, our semantics yields instantiation 𝑏≡Í

𝜆,𝑗∈𝐷𝜆𝜃1[𝑖\𝑗] + 𝛿, where 𝛿≡CDF -1(Í

```math
𝜆,𝑗∈𝐷𝜆𝜃2[𝑖\𝑗], 𝜀). Since Bound𝑝is monotone, we have 𝑏≥𝑏∗→Bound𝑝[𝑏].
Contraposing, we get ¬Bound𝑝[𝑏] →𝑏∗> 𝑏. We can then establish the soundness of (𝑝,𝑏,𝜀) with
```

<!-- page 19 -->

Adaptive Shielding via Parametric Safety Proofs 109:19

𝜄::= 𝑝1 ··=𝑒1 ; . . . ; 𝑝𝑛··=𝑒𝑛 (𝑝1, . . . , 𝑝𝑛··= 𝑒) ≡(𝑝1 ··= 𝑒; . . . ; 𝑝𝑛··= 𝑒)

𝑒::= 𝜃when 𝐺| best 𝑖1, . . . ,𝑖𝑛: 𝜃when 𝐺| aggregate 𝑖1, . . . ,𝑖𝑛: 𝜃1 and 𝜃2 when 𝐺

```math
A⟦𝑝1 ··=𝑒1 ; . . . ; 𝑝𝑛··=𝑒𝑛⟧= A⟦𝑝1 ··=𝑒1⟧× · · · × A⟦𝑝𝑛··=𝑒𝑛⟧
```

A⟦𝑝··= 𝑒⟧= A⟦𝑒⟧

A⟦𝜃⟧= 1

A⟦best 𝑖1, . . . ,𝑖𝑛: 𝜃⟧= List(N𝑛)

A⟦aggregate 𝑖1, . . . ,𝑖𝑛: 𝜃1 and 𝜃2⟧= [0, 1] × FinDistr(N𝑛)

```math
⟦𝜄⟧: A⟦𝜄⟧→List(Param × SBInst × [0, 1])
```

⟦𝑝1 ··=𝑒1 ; . . . ; 𝑝𝑛··=𝑒𝑛⟧((𝑎1, . . . ,𝑎𝑛)) = ⟦𝑝1 ··= 𝑒1⟧(𝑎1) ⊕· · · ⊕⟦𝑝𝑛··= 𝑒𝑛⟧(𝑎𝑛)

⟦𝑝··= 𝑒⟧(𝑎) = [(𝑝,𝑒,𝜀) : (𝑒,𝜀) ∈⟦𝑒⟧(𝑎)]

⟦𝜃when 𝐺⟧(•) = [(𝜃when 𝐺, 0)]

⟦best 𝑖1, . . . ,𝑖𝑛: 𝜃when 𝐺⟧(𝐽) = [(𝜃[𝑖\𝑗] when 𝐺[𝑖\𝑗], 0) : 𝑗∈𝐽]

⟦aggregate 𝑖1, . . . ,𝑖𝑛: 𝜃1 and 𝜃2 when 𝐺⟧((𝜀, 𝐷))





∑︁

𝜆· 𝜃1[𝑖\𝑗] + CDF -1 ∑︁

when

Û

𝜆· 𝜃2[𝑖\𝑗] , 𝜀

𝐺[𝑖\𝑗] , 𝜀

=

𝜆,𝑗∈𝐷

𝜆,𝑗∈𝐷

𝜆,𝑗∈𝐷

**Fig. 7. Syntax and semantics of the inference strategy language. Without loss of generality, all bounds are assumed to be upper-bounds (otherwise, substitute some parameter 𝑝by −𝑝). All when-clauses can be omitted when 𝐺= true. We use the list concatenation operator ⊕and the list comprehension notation. FinDistr(𝑋) denotes the set of all distributions over set 𝑋with finite support: FinDistr(𝑋) ≡{[(𝜆1,𝑥1), . . . , (𝜆𝑛,𝑥𝑛)] : 𝑛∈N, 𝑥1, . . . 𝑥𝑛∈𝑋, 𝜆1, . . . , 𝜆𝑛> 0, Í**

𝑖𝜆𝑖= 1}.

the exact same reasoning that was demonstrated in Equation 5:

∑︁

P(¬Bound𝑝[𝑏]) ≤P(𝑏∗> 𝑏) = P

𝜆· 𝜃2[𝑖\𝑗] > 𝛿

≤𝜀.

𝑖,𝜆∈𝐷

Details on how to evaluate or approximate the CDF -1 operator are available in the extended version of this paper [11, Appendix E.2]. In the particular case where 𝜃2 is a linear combinations of Gaussian variables (with possibly state-dependent coefficients), closed-form solutions exist that involve the erf -1 function. Concentration inequalities (e.g. Chebyshev, Hoeffding, or Chernoff bounds) can be used to approximate it conservatively in the general case [6].

Proof obligations and soundness. An inference strategy Infer induces a proof obligation in the form of a dL formula, P⟦Infer⟧, which is defined inductively in Figure 8. Provided that this obligation is valid, our language guarantees the soundness of all resulting inferences. This is expressed in Theorem 5.1 (a proof is provided in the extended version of this paper [11, Appendix F.2].

Theorem 5.1 (Soundness of the inference strategy language). Let ⟨Const, . . . , Infer⟩a shield specification. If the formula P⟦Infer⟧is valid, then ⟦Infer⟧(𝑎) is a list of sound inference assignments for any inference action 𝑎∈A⟦Infer⟧.

<!-- page 20 -->

109:20 Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent

P⟦𝑝1 ··=𝑒1 ; . . . ; 𝑝𝑛··=𝑒𝑛⟧= P⟦𝑝1 ··=𝑒1⟧∧· · · ∧P⟦𝑝𝑛··=𝑒𝑛⟧

Û

D(FV(𝑒))

P⟦𝑝··= 𝑒⟧= Assum ∧

→P⟦𝑒⟧(𝑝)

P⟦𝜃when 𝐺⟧(𝑝) = 𝐺→Bound𝑝[𝜃]

P⟦best 𝑖1, . . . ,𝑖𝑛: 𝜃when 𝐺⟧(𝑝) = 𝐺→Bound𝑝[𝜃]

P⟦aggregate 𝑖1, . . . ,𝑖𝑛: 𝜃1 and 𝜃2 when 𝐺⟧(𝑝) = 𝐺→Bound𝑝[𝜃1 + 𝜃2]

D(𝑥𝑘) = D(𝑥)(𝑘) D(𝑝) = Bound𝑝 D(𝜔) = (𝜔= Obs𝜔) D(𝑣) = Inv

**Fig. 8. Obligation induced by an inference strategy. Per convention, 𝑝∈Param, 𝜔∈ObsVar and 𝑣∈StateVar.**

Learning inference policies. A crucial feature of our inference strategy language is its nondeterminism: an inference strategy does not fully specify the behavior of the inference module and key decisions about what measurements to aggregate, how much budget to spend and when are left to a separate inference policy. As illustrated in Section 2.4, such a policy must make subtle tradeoffs. However, it is not soundness-critical and amenable to learning. Learning an inference policy is possible within the meta-learning setting described in Section 4.6. A per-episode safety-budget is fixed and the agent must learn a way to best manage this budget within an episode, in a way that generalizes across a family of environments and allows maximizing returns. Section 6 illustrates this idea in three different case studies.

## 6 Experimental Evaluation

We evaluate our framework on a series of case studies and demonstrate the claims:

C1 Our framework allows expressing diverse types of model uncertainty in a unified way. C2 Shielded agents always remain safe. C3 Adaptive shields allow more aggressive control strategies than non-adaptive shields. C4 Inference policies can be learned that generalize across settings. C5 Control policies can be learned that actively seek information as a prerequisite for success.

All case studies are summarized in Table 2. Each case study trains a shielded reinforcement learning agent, either in a fixed environment or using the meta-learning setting described in Section 4.6. We demonstrate the qualitative claim C1 by having each case study illustrate distinct modelling concepts, all of which are listed in Table 2. Claims C2 and C3 are evaluated on all case studies. As shown in Table 3 and validating Theorem 4.4, shielded agents never encounter crashes. Unshielded agents reach unsafe states during training, but also after training in all but one environment. Furthermore, disabling the inference module leads to inferior policies in all examples. Claims C4 and C5 are relevant in the meta-learning setting, which is explored in three case studies whose results we summarize below. Full details on our experimental protocol, results, and on the shield used for each case study are available in the extended version of this paper [11, Appendix A].

Versatile Train. This case study uses the shield from Figure 3, which is inspired by published models of train control systems [23, 34], with added support for runtime track slope estimation. Our key results are summarized in Figures 9 and 10. We show how different inference policies work best for different kinds of train tracks and noise models. A policy that aggregates observations in small batches works better in a setting with irregular tracks (large 𝑘) and low sensor noise (small 𝜎), while a policy that aggregates observations in large batches works better in settings with regular tracks and high sensor noise. Importantly, inference policies can be learned that are at least competitive with the best hardcoded solution in both cases.

<!-- page 21 -->

Adaptive Shielding via Parametric Safety Proofs 109:21

**Table 2. Summary of our Experimental Evaluation. Each case study is annotated with references to the main experimental claims C𝑖that it provides evidence for. A “fixed” annotation means that learning is conducted in a fixed environment, while a“meta” annotation means that the case study involves meta-learning (as defined in Section 4.6). No shielded agent encountered an unsafe state in our experiments (Table 3).**

Case Study Property

Concepts: Fixed environment, Concentration inequalities Description: A train must go up-and-down a hill repeatedly to transport merchandise, protected by a variant of the shield from Figure 3 that assumes uniform measurement noise. Results: Enabling the inference module yields a more efficient controller. Hoeffding bounds beat Chebyshev bounds for inference.

Sisyphean Train

C1, C2, C3, fixed

Concepts: Meta-learning, Learned inference policy Description: A train is exposed to a variety of track topologies and must learn to spend its safety budget wisely in unknown terrains. Results: Different types of tracks call for different inference policies. Appropriate inference policies can be learned automatically.

Versatile Train

C1, C2, C3, C4, meta

Concepts: Mapping, Active sensing Description: A robot equipped with a lamp must cross a bridge located at an unknown position along a river, at night. The lamp sheds light within a fixed radius. Results: The robot successfully learns to approach the river, switch on its lamp and go along the river until it locates the bridge. Disabling the inference module prevents learning. A non-shielded agent frequently falls into the river, even after training.

Crossing the River

C1, C2, C3, C5, meta

Concepts: Discrete model switching, Boolean inference Description: We consider a variant of the next-generation Airborne Collision Avoidance System (ACAS X) [22]. The agent controls a plane and must learn to react to an intruder aircraft entering its airspace. Results: A provably-safe policy can be learned that attempts to infer whether or not the intruding aircraft flies in ACAS-compliant ways in order to avoid drastic maneuvers whenever possible.

Revisiting ACAS X

C1, C2, C3, C4, meta

Crossing the River. This case study illustrates the concept of active sensing and demonstrates claim C5 in a minimal setting. The goal is for a robot equipped with a lamp to cross a bridge at night. The robot must find the position of the bridge, which translates into a model where the unknown is in the safety property instead of the plant. The robot only observes the bridge when it gets close enough and its lamp is on. In addition to an inference policy, it must learn a control policy that seeks knowledge explicitly. We illustrate this learned control policy in Figure 11.

Revisiting ACASX. This case study revisits a classic of cyberphysical-system verification: the nextgeneration Airborne Collision Avoidance System (ACAS X) [22]. However, rather than assuming a known intruder trajectory or a random-walk intruder model [25], we propose a new uncertainty model where intruders are either ACAS-compliant (in which case they are also actively trying to avoid collision) or not (in which case they must be treated as adversarial). The agent must attempt to infer the compliance of the intruder so as to avoid drastic maneuvers whenever possible. We illustrate the effectiveness of our learned inference policy in Figure 12.

<!-- page 22 -->

109:22 Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent

푘/휎small

푘/휎large

10

10

Train Return

Train Return

5

5

0

0

−5

−5

## 0 2000 4000 6000 Episode

## 0 2000 4000 6000 Episode

Unshielded Adaptive Non-adaptive Aggregate-1 Aggregate-20

**Fig. 9. Returns for the versatile train case study, for two different combinations of 𝑘and 𝜎(and averaged across three random seeds, with standard deviations represented as shaded areas around the mean). The train gets rewarded for reaching the station as quickly as possible (a fixed negative reward is issued at every step before the train reaches destination) and penalized for (unsafely) overshooting its target. Training returns are shown for an unshielded agent (red), an agent using our proposed adaptive shield (green), and a nonadaptive variant where the inference module is deactivated (orange). In addition, the Aggregate-𝑖agent is a variant of the Adaptive agent that uses a hardcoded inference policy that spends a fixed budget to aggregate all available observations every 𝑖steps. Different hardcoded inference policies perform best in different settings but the learned inference policy manages to match the best one in both cases.**

푘/휎small

푘/휎large

0.2

0.2

0.0

0.0

−0.2

−0.2

Position 푥(km)

Position 푥(km)

−0.4

−0.4

−0.6

−0.6

−0.8

−0.8

−1.0

−1.0

−1.2

−1.2

## 0 10 20 30 Time 푡(s)

## 0 10 20 30 Time 푡(s)

**Fig. 10. A visualization of the learned control and inference policies for the versatile train case study, on two random tracks and for two different combinations of 𝑘and 𝜎. We show the position of the train over time using dots. The train needs to stop before 𝑥= 0 (bold black line). At each time step, a vertical segment indicates the estimated braking distance assuming that the train decides to accelerate for this time step. The segment is drawn in red if the train effectively decides to accelerate and in blue if it decides to brake. A green circle is shown whenever the inference module aggregates existing measurements to improve the local slope estimate. The resulting reduction in the shield’s estimated braking distance is plotted as a green segment. In particular, we observe as expected that the learned inference policy aggregates measurements in bigger batches when 𝑘/𝜎is small.**

<!-- page 23 -->

Adaptive Shielding via Parametric Safety Proofs 109:23

**Table 3. Return at testing time (average value of the last 100 episodes during 10,000 evaluation steps) and number of crashes during training and testing time, for different case studies and under different settings. The number of training steps and the maximum episode length for each setting are 80,000/100; 400,000/100; 400,000/100; 400,000/50; and 400,000/40 respectively. Agents are given a total safety budget of 10−3 in fixedenvironment settings (Sisyphean Train) and 10−7 per episode in meta-learning settings (all others).**

Setting Method Return Crashes during training Crashes during testing

```math
Unshielded
8.3 ± 0.1
110.7 ± 21.5
1.3 ± 0.5
Adaptive
7.0 ± 0.0
0.0 ± 0.0
0.0 ± 0.0
Non-adaptive
5.5 ± 0.0
0.0 ± 0.0
0.0 ± 0.0
```

Sisyphean Train

```math
Unshielded
10.0 ± 0.7
102.7 ± 45.0
0.0 ± 0.0
Adaptive
9.1 ± 0.3
0.0 ± 0.0
0.0 ± 0.0
Non-adaptive
5.8 ± 0.0
0.0 ± 0.0
0.0 ± 0.0
```

Versatile Train

(𝑘/𝜎large)

```math
Unshielded
9.5 ± 1.2
94.3 ± 6.2
0.7 ± 0.5
Adaptive
9.1 ± 0.2
0.0 ± 0.0
0.0 ± 0.0
Non-adaptive
5.8 ± 0.1
0.0 ± 0.0
0.0 ± 0.0
```

Versatile Train

(𝑘/𝜎small)

```math
Unshielded
3.9 ± 0.4
325.7 ± 81.8
0.7 ± 0.5
Adaptive
4.2 ± 0.7
0.0 ± 0.0
0.0 ± 0.0
Non-adaptive
−5.0 ± 0.0
0.0 ± 0.0
0.0 ± 0.0
```

Crossing the River

```math
Unshielded
6.7 ± 0.5
987.0 ± 66.4
25.0 ± 6.7
Adaptive
6.6 ± 0.2
0.0 ± 0.0
0.0 ± 0.0
Non-adaptive
4.5 ± 0.0
0.0 ± 0.0
0.0 ± 0.0
```

Revisiting ACAS X

20

20

10

10

Position 푦(m)

Position 푦(m)

0

0

−10

−10

−20

−20

−20 −10 0 10 20 Position 푥(m)

−20 −10 0 10 20 Position 푥(m)

**Fig. 11. Visualization of the learned policy for the crossing the river case study. The river is drawn as a vertical blue line at 𝑥= 0 and the bridge is drawn in brown. The range within which the agent can observe the bridge is plotted as a bold, black dashed circle. The agent’s position is marked by a point for each control cycle, which is blue if the lamp is off and red if it is on. A green circle around the current position indicates some safety budget being spent. Regardless of its starting position, the agent learns to go near the river, activate the lamp when it gets close enough and then move along the river until it observes the bridge.**

## 7 Discussion

Runtime overhead. Our framework pushes most of the burden of safety analysis offline via static proof obligations. Thus, it benefits from a small and predictable runtime overhead. This overhead results from running the inference module, monitoring the proposed control actions and executing

<!-- page 24 -->

109:24 Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent

2000

2000

1000

1000

Position ℎ(m)

Position ℎ(m)

0

0

−1000

−1000

−2000

−2000

## 0 10 20 30 40 30 20 10 0 Time 푡(s)

## 0 10 20 30 40 30 20 10 0 Time 푡(s)

**Fig. 12. Learned policy for the Revisiting ACAS X case study, in two different scenarios. The scenario on the right features an ACAS-compliant intruder while the scenario on the left involves a non-compliant intruder. In both cases, the ownship’s trajectory is shown on the left of the plot while the intruder’s trajectory is shown on the right. The estimated upper and lower bounds for the intruder’s final altitude at meeting time is shown for each time step as a dashed line. Red dots on the ownship’s trajectory indicate the observation of information that is relevant to estimating the intruder’s compliance. Green dots indicate that the intruder has been identified as compliant. When this happens, a less aggressive avoidance maneuver can be executed.**

the fallback policy when needed. The complexity of running a cycle of the inference module is linear in the size of the specification and in the size of the inference action being considered (e.g. the number of measurements being aggregated), assuming that the CDF -1 operator can be evaluated in linear time (which is true in particular in the Gaussian case or when using concentration inequalities, see details in the extended version of this paper [11, Appendix E.2]). Running the controller monitor is inexpensive since it consists in evaluating a formula whose size does not exceed the size of the shield itself. Finally, assuming that an explicit fallback policy is provided (see discussion in Section 3.4), the cost of computing fallback actions is small and predictable. In our experiments, the total overhead of shielding during training never exceeds 15% (see details in the extended version of this paper [11, Appendix A, Table 4]).

On the complexity of designing adaptive shields. There is an inherent complexity to the engineering task of designing adaptive monitors for rich, realistic model families, which typically necessitates the exploitation of domain-specific insights. Our framework allows designers to focus on this essential complexity, while eliminating the accidental complexity of enforcing end-to-end soundness guarantees that encompass statistical inference. For example, while our paper shows how tricky and error-prone statistical reasoning can be (e.g. reusing measurements is sound within an inference cycle but not across cycles), our framework exposes abstractions that fully protect users from such considerations and generates dL proof obligations that require no probabilistic reasoning. Still, specifying formal models of hybrid systems and proving properties about them using interactive theorem proving is a nontrivial skill to acquire. Doing so is eased by the increasing availability of automation in tools such as KeYmaera X [14, 40]. We show the proof obligations generated by our tool for all case studies in the extended version of this paper [11, Appendix B]. Out of 32 obligations, 27 can be discharged fully automatically or with trivial human guidance (such as providing a single term for instantiating an existential variable). The others require more effort but can be proved in under an hour by an experienced KeYmaera X user [11, Appendix C].

<!-- page 25 -->

Adaptive Shielding via Parametric Safety Proofs 109:25

## 8 Related Work

Safe reinforcement learning is widely studied [8, 17, 18], including several approaches without formal verification. Several policy-search algorithms have been proposed that take into account safety constraints specified separately from the reward signal, but do not offer any guarantee that those constraints will not be violated during training or deployment [1, 42, 44]. In contrast, this work is part of a family of approaches that are often called sandboxing or shielding-based [2, 15, 43], and where the intended actions of an RL agent are monitored at runtime and overridden by appropriate fallbacks whenever they cannot be proved safe with respect to a model of the environment.

Virtually all existing approaches to shielding aim for full-automation of the shield computation, imposing hard tradeoffs in terms of safety, adaptivity, precision, expressivity and scalability. In circumstances where they run fast enough to be used online, methods based on reachability analysis [21, 26, 43] are naturally amenable to a form of adaptivity. However, they only offer bounded-horizon guarantees and precision comes at the expense of runtime efficiency. Methods based on LTL model-checking [2, 27] or finite-MDP solving [36] can handle infinite time-horizons but require discretization of hybrid dynamics, often at a significant cost in terms of precision and safety. They also tend to scale poorly with increasing dimensionality. Methods based on Hamilton-Jacobi solving [13] face similar challenges. In contrast, our proposed framework allows leveraging human ingenuity by extracting shields from nondeterministic, symbolic controllers that are proved safe using interactive theorem proving. It builds on the Justified Speculative Control (JSC) framework [15], which it generalizes in a crucial way to support adaptivity.

Our framework offers a uniquely expressive language for modelling environment uncertainty via arbitrarily constrained function symbols. For example, reachability analysis typically uses bounded disturbance terms [3] to model environment uncertainty, which is sufficient to model the example from Figure 2 but not those from Figure 3 and from the ACASX case study. To the best of our knowledge, these last two examples cannot be accommodated by any pre-existing approach. Another standard way of representing model uncertainty for the purpose of adaptive shielding is to use Gaussian processes to model an unknown, state-dependent term added to the system’s dynamics [4, 5, 9, 13]. This approach offers a different form of modelling flexibility, where assumptions about functional unknowns are implicitly encoded into prior kernels rather than hard logical constraints. However, this also makes the resulting safety guarantees harder to interpret and fundamentally dependent on assumptions that are nearly impossible to validate experimentally.

Another approach has been proposed to extend the JSC framework with a form of adaptivity, in which an agent starts with a finite set of plausible models and then progressively discards those that are found inconsistent with observations [16]. Our framework handles a more general form of parametric model uncertainty and additionally supports noisy observations and statistical reasoning. Finally, our idea of having experts define nondeterministic inference strategies that are sound by construction and refined via learning – thereby making shielded agents in charge of their own safety budget – has, to the best of our knowledge, no equivalent in the literature.

## 9 Conclusion

Our framework gives experts full access to the power of differential dynamic logic to build adaptive shields for hybrid systems. Its unique flexibility raises the equally unique challenge of performing statistical inference soundly and efficiently. We tackle this challenge with a mix of language design and learning, introducing the concepts of an inference strategy and of an inference policy respectively. Future work may explore the integration of reachability analysis and model-checking within our framework, allowing hybrid combinations of symbolic and numerical, offline and online proving.

<!-- page 26 -->

109:26 Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent

Data-Availability Statement

An artifact that contains our framework implementation, instructions to replicate all experiments, and formal proofs for all case studies is available at https://doi.org/10.5281/zenodo.14916164 [12].

Acknowledgments This work was supported by the NSFC (Nos. 62276149, 92370124, 62350080, 92248303, U2341228, 62061136001), BNRist (BNR2022RC01006), Tsinghua Institute for Guo Qiang, and the High Performance Computing Center, Tsinghua University. J. Zhu was also supported by the XPlorer Prize. Finally, this work was supported by the Alexander von Humboldt Professorship program. We thank the anonymous reviewers for their helpful feedback.

## References

[1] Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel. 2017. Constrained Policy Optimization. In Proceedings of the 34th International Conference on Machine Learning, ICML 2017, Sydney, NSW, Australia, 6-11 August 2017 (Proceedings of Machine Learning Research, Vol. 70), Doina Precup and Yee Whye Teh (Eds.). PMLR, 22–31. http: //proceedings.mlr.press/v70/achiam17a.html

[2] Mohammed Alshiekh, Roderick Bloem, Rüdiger Ehlers, Bettina Könighofer, Scott Niekum, and Ufuk Topcu. 2018. Safe Reinforcement Learning via Shielding. In Proceedings of the Thirty-Second AAAI Conference on Artificial Intelligence, (AAAI-18), the 30th innovative Applications of Artificial Intelligence (IAAI-18), and the 8th AAAI Symposium on Educational Advances in Artificial Intelligence (EAAI-18), New Orleans, Louisiana, USA, February 2-7, 2018, Sheila A. McIlraith and Kilian Q. Weinberger (Eds.). AAAI Press, 2669–2678. doi:10.1609/AAAI.V32I1.11797

[3] Matthias Althoff and John M Dolan. 2014. Online verification of automated road vehicles using reachability analysis. IEEE Transactions on Robotics 30, 4 (2014), 903–918. doi:10.1109/TRO.2014.2312453

[4] Felix Berkenkamp and Angela P. Schoellig. 2015. Safe and robust learning control with Gaussian processes. In 14th European Control Conference, ECC 2015, Linz, Austria, July 15-17, 2015. IEEE, 2496–2501. doi:10.1109/ECC.2015.7330913

[5] Felix Berkenkamp, Matteo Turchetta, Angela P. Schoellig, and Andreas Krause. 2017. Safe Model-based Reinforcement Learning with Stability Guarantees. In Advances in Neural Information Processing Systems 30: Annual Conference on Neural Information Processing Systems 2017, December 4-9, 2017, Long Beach, CA, USA, Isabelle Guyon, Ulrike von Luxburg, Samy Bengio, Hanna M. Wallach, Rob Fergus, S. V. N. Vishwanathan, and Roman Garnett (Eds.). 908–918. https://proceedings.neurips.cc/paper/2017/hash/766ebcd59621e305170616ba3d3dac32-Abstract.html

[6] Dimitri Bertsekas and John N Tsitsiklis. 2008. Introduction to probability. Vol. 1. Athena Scientific.

[7] Brandon Bohrer and André Platzer. 2020. Constructive game logic. In Programming Languages and Systems: 29th European Symposium on Programming, ESOP 2020, Held as Part of the European Joint Conferences on Theory and Practice of Software, ETAPS 2020, Dublin, Ireland, April 25–30, 2020, Proceedings 29. Springer International Publishing, 84–111. doi:10.1007/978-3-030-44914-8_4

[8] Lukas Brunke, Melissa Greeff, Adam W Hall, Zhaocong Yuan, Siqi Zhou, Jacopo Panerati, and Angela P Schoellig.

2022. Safe learning in robotics: From learning-based control to safe reinforcement learning. Annual Review of Control, Robotics, and Autonomous Systems 5 (2022), 411–444. doi:10.1146/ANNUREV-CONTROL-042920-020211

[9] Richard Cheng, Gábor Orosz, Richard M. Murray, and Joel W. Burdick. 2019. End-to-End Safe Reinforcement Learning through Barrier Functions for Safety-Critical Continuous Control Tasks. In The Thirty-Third AAAI Conference on Artificial Intelligence, AAAI 2019, The Thirty-First Innovative Applications of Artificial Intelligence Conference, IAAI 2019, The Ninth AAAI Symposium on Educational Advances in Artificial Intelligence, EAAI 2019, Honolulu, Hawaii, USA, January 27 - February 1, 2019. AAAI Press, 3387–3395. doi:10.1609/aaai.v33i01.33013387

[10] Ingy Elsayed-Aly, Suda Bharadwaj, Christopher Amato, Rüdiger Ehlers, Ufuk Topcu, and Lu Feng. 2021. Safe Multi- Agent Reinforcement Learning via Shielding. In AAMAS ’21: 20th International Conference on Autonomous Agents and Multiagent Systems, Virtual Event, United Kingdom, May 3-7, 2021, Frank Dignum, Alessio Lomuscio, Ulle Endriss, and Ann Nowé (Eds.). ACM, 483–491. doi:10.5555/3463952.3464013

[11] Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent. 2025. Adaptive Shielding via Parametric Safety Proofs. arXiv:2502.18879 [cs.PL] https://arxiv.org/abs/2502.18879

[12] Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent. 2025. Adaptive Shielding via Parametric Safety Proofs. doi:10.5281/zenodo.14916164

[13] Jaime F. Fisac, Anayo K. Akametalu, Melanie N. Zeilinger, Shahab Kaynama, Jeremy H. Gillula, and Claire J. Tomlin.

2019. A General Safety Framework for Learning-Based Control in Uncertain Robotic Systems. IEEE Trans. Autom. Control. 64, 7 (2019), 2737–2752. doi:10.1109/TAC.2018.2876389

<!-- page 27 -->

Adaptive Shielding via Parametric Safety Proofs 109:27

[14] Nathan Fulton, Stefan Mitsch, Jan-David Quesel, Marcus Völp, and André Platzer. 2015. KeYmaera X: An Axiomatic Tactical Theorem Prover for Hybrid Systems. In Automated Deduction - CADE-25 - 25th International Conference on Automated Deduction, Berlin, Germany, August 1-7, 2015, Proceedings (LNCS, Vol. 9195), Amy P. Felty and Aart Middeldorp (Eds.). Springer, 527–538. doi:10.1007/978-3-319-21401-6_36

[15] Nathan Fulton and André Platzer. 2018. Safe Reinforcement Learning via Formal Methods: Toward Safe Control Through Proof and Learning. In 8th AAAI Symposium on Educational Advances in Artificial Intelligence (EAAI-18), New Orleans, Louisiana, USA, February 2-7, 2018, Sheila A. McIlraith and Kilian Q. Weinberger (Eds.). AAAI Press, 6485–6492. doi:10.1609/AAAI.V32I1.12107

[16] Nathan Fulton and André Platzer. 2019. Verifiably Safe Off-Model Reinforcement Learning. In Tools and Algorithms for the Construction and Analysis of Systems - 25th International Conference, TACAS 2019, Held as Part of the European Joint Conferences on Theory and Practice of Software, ETAPS 2019, Prague, Czech Republic, April 6-11, 2019, Proceedings, Part I (LNCS, Vol. 11427), Tomás Vojnar and Lijun Zhang (Eds.). Springer, 413–430. doi:10.1007/978-3-030-17462-0_28

[17] Javier García and Fernando Fernández. 2015. A comprehensive survey on safe reinforcement learning. J. Mach. Learn. Res. 16 (2015), 1437–1480. doi:10.5555/2789272.2886795

[18] Shangding Gu, Long Yang, Yali Du, Guang Chen, Florian Walter, Jun Wang, Yaodong Yang, and Alois C. Knoll.

2022. A Review of Safe Reinforcement Learning: Methods, Theory and Applications. CoRR abs/2205.10330 (2022). doi:10.48550/arXiv.2205.10330 arXiv:2205.10330

[19] Todd Hester, Michael J. Quinlan, and Peter Stone. 2012. RTMBA: A Real-Time Model-Based Reinforcement Learning Architecture for robot control. In IEEE International Conference on Robotics and Automation, ICRA 2012, 14-18 May, 2012, St. Paul, Minnesota, USA. IEEE, 85–90. doi:10.1109/ICRA.2012.6225072

[20] Nathan Hunt, Nathan Fulton, Sara Magliacane, Trong Nghia Hoang, Subhro Das, and Armando Solar-Lezama. 2021. Verifiably safe exploration for end-to-end reinforcement learning. In HSCC ’21: 24th ACM International Conference on Hybrid Systems: Computation and Control, Nashville, Tennessee, May 19-21, 2021, Sergiy Bogomolov and Raphaël M. Jungers (Eds.). ACM, 14:1–14:11. doi:10.1145/3447928.3456653

[21] Radoslav Ivanov, James Weimer, Rajeev Alur, George J Pappas, and Insup Lee. 2019. Verisig: verifying safety properties of hybrid systems with neural network controllers. In Proceedings of the 22nd ACM International Conference on Hybrid Systems: Computation and Control. 169–178. doi:10.1145/3302504.3311806

[22] Jean-Baptiste Jeannin, Khalil Ghorbal, Yanni Kouskoulas, Ryan Gardner, Aurora Schmidt, Erik Zawadzki, and André Platzer. 2015. A formally verified hybrid system for the next-generation airborne collision avoidance system. In Tools and Algorithms for the Construction and Analysis of Systems: 21st International Conference, TACAS 2015, Held as Part of the European Joint Conferences on Theory and Practice of Software, ETAPS 2015, London, UK, April 11-18, 2015, Proceedings 21. Springer, 21–36. doi:10.1007/978-3-662-46681-0_2

[23] Aditi Kabra, Stefan Mitsch, and André Platzer. 2022. Verified train controllers for the federal railroad administration train kinematics model: Balancing competing brake and track forces. IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems 41, 11 (2022), 4409–4420. doi:10.1109/TCAD.2022.3197690

[24] Mykel J Kochenderfer. 2015. Decision making under uncertainty: theory and application. MIT press.

[25] Mykel J Kochenderfer, Jessica E Holland, and James P Chryssanthacopoulos. 2012. Next generation airborne collision avoidance system. Lincoln Laboratory Journal 19, 1 (2012), 17–33.

[26] Torsten Koller, Felix Berkenkamp, Matteo Turchetta, and Andreas Krause. 2018. Learning-Based Model Predictive Control for Safe Exploration. In 57th IEEE Conference on Decision and Control, CDC 2018, Miami, FL, USA, December 17-19, 2018. IEEE, 6059–6066. doi:10.1109/CDC.2018.8619572

[27] Bettina Könighofer, Florian Lorber, Nils Jansen, and Roderick Bloem. 2020. Shield Synthesis for Reinforcement Learning. In Leveraging Applications of Formal Methods, Verification and Validation: Verification Principles - 9th International Symposium on Leveraging Applications of Formal Methods, ISoLA 2020, Rhodes, Greece, October 20-30, 2020, Proceedings, Part I (Lecture Notes in Computer Science, Vol. 12476), Tiziana Margaria and Bernhard Steffen (Eds.). Springer, 290–306. doi:10.1007/978-3-030-61362-4_16

[28] Xiaodan Liang, Tairui Wang, Luona Yang, and Eric P. Xing. 2018. CIRL: Controllable Imitative Reinforcement Learning for Vision-Based Self-driving. In Computer Vision - ECCV 2018 - 15th European Conference, Munich, Germany, September 8-14, 2018, Proceedings, Part VII (LNCS, Vol. 11211), Vittorio Ferrari, Martial Hebert, Cristian Sminchisescu, and Yair Weiss (Eds.). Springer, 604–620. doi:10.1007/978-3-030-01234-2_36

[29] Stefan Mitsch and André Platzer. 2016. ModelPlex: verified runtime validation of verified cyber-physical system models. Formal Methods Syst. Des. 49, 1-2 (2016), 33–74. doi:10.1007/s10703-016-0241-z

[30] Randall Munroe. 2011. Significant. http://xkcd.com/882/.

[31] André Platzer. 2008. Differential Dynamic Logic for Hybrid Systems. J. Autom. Reason. 41, 2 (2008), 143–189. doi:10.1007/s10817-008-9103-8

[32] André Platzer. 2017. A Complete Uniform Substitution Calculus for Differential Dynamic Logic. J. Autom. Reason. 59, 2 (2017), 219–265. doi:10.1007/s10817-016-9385-1

<!-- page 28 -->

109:28 Yao Feng, Jun Zhu, André Platzer, and Jonathan Laurent

[33] André Platzer and Jan-David Quesel. 2008. Logical Verification and Systematic Parametric Analysis in Train Control.. In HSCC (LNCS, Vol. 4981), Magnus Egerstedt and Bud Mishra (Eds.). Springer, 646–649. doi:10.1007/978-3-540-78929-1_55

[34] André Platzer and Jan-David Quesel. 2009. European Train Control System: A case study in formal verification. In International Conference on Formal Engineering Methods. Springer, 246–265. doi:10.1007/978-3-642-10373-5_13

[35] André Platzer and Yong Kiam Tan. 2018. Differential equation axiomatization: The impressive power of differential ghosts. In Proceedings of the 33rd Annual ACM/IEEE Symposium on Logic in Computer Science. 819–828. doi:10.1145/ 3209108.3209147

[36] Stefan Pranger, Bettina Könighofer, Martin Tappler, Martin Deixelberger, Nils Jansen, and Roderick Bloem. 2021. Adaptive shielding under uncertainty. In 2021 American Control Conference (ACC). IEEE, 3467–3474. doi:10.23919/ ACC50511.2021.9482889

[37] Loris Roveda, Jeyhoon Maskani, Paolo Franceschi, Arash Abdi, Francesco Braghin, Lorenzo Molinari Tosatti, and Nicola Pedrocchi. 2020. Model-Based Reinforcement Learning Variable Impedance Control for Human-Robot Collaboration. J. Intell. Robotic Syst. 100, 2 (2020), 417–433. doi:10.1007/s10846-020-01183-3

[38] Shai Shalev-Shwartz, Shaked Shammah, and Amnon Shashua. 2016. Safe, Multi-Agent, Reinforcement Learning for Autonomous Driving. CoRR abs/1610.03295 (2016). arXiv:1610.03295 http://arxiv.org/abs/1610.03295

[39] William D. Smart and Leslie Pack Kaelbling. 2002. Effective Reinforcement Learning for Mobile Robots. In Proceedings of the 2002 IEEE International Conference on Robotics and Automation, ICRA 2002, May 11-15, 2002, Washington, DC, USA. IEEE, 3404–3410. doi:10.1109/ROBOT.2002.1014237

[40] Andrew Sogokon, Stefan Mitsch, Yong Kiam Tan, Katherine Cordwell, and André Platzer. 2022. Pegasus: Sound Continuous Invariant Generation. Form. Methods Syst. Des. 58, 1 (2022), 5–41. doi:10.1007/s10703-020-00355-z Special issue for selected papers from FM’19.

[41] Richard S Sutton and Andrew G Barto. 2018. Reinforcement learning: An introduction. MIT press.

[42] Chen Tessler, Daniel J. Mankowitz, and Shie Mannor. 2019. Reward Constrained Policy Optimization. In 7th International Conference on Learning Representations, ICLR 2019, New Orleans, LA, USA, May 6-9, 2019. OpenReview.net. https: //openreview.net/forum?id=SkfrvsA9FX

[43] Jakob Thumm and Matthias Althoff. 2022. Provably Safe Deep Reinforcement Learning for Robotic Manipulation in Human Environments. In 2022 International Conference on Robotics and Automation, ICRA 2022, Philadelphia, PA, USA, May 23-27, 2022. IEEE, 6344–6350. doi:10.1109/ICRA46639.2022.9811698

[44] Qisong Yang, Thiago D. Simão, Simon H. Tindemans, and Matthijs T. J. Spaan. 2021. WCSAC: Worst-Case Soft Actor Critic for Safety-Constrained Reinforcement Learning. In Thirty-Fifth AAAI Conference on Artificial Intelligence, AAAI 2021, Thirty-Third Conference on Innovative Applications of Artificial Intelligence, IAAI 2021, The Eleventh Symposium on Educational Advances in Artificial Intelligence, EAAI 2021, Virtual Event, February 2-9, 2021. AAAI Press, 10639–10646. doi:10.1609/AAAI.V35I12.17272 Received 2024-10-16; accepted 2025-02-18
