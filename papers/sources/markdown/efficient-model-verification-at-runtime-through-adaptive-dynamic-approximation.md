# Efficient Model Verification at Runtime through Adaptive Dynamic Approximation

> **Source PDF:** `Efficient Model Verification at Runtime through Adaptive Dynamic Approximation.pdf` · **Pages:** 43 · Converted by `scripts/paper2md.py` from the original PDF. **Equations are extracted glyph-by-glyph and may be mangled — check the PDF before quoting any formula.**

<!-- page 1 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation

MEHRAN ALIDOOST NIA, Department of Computer Science and Engineering, Shahid Beheshti University, Tehran, Iran RADU CALINESCU, Department of Computer Science, University of York, York, United Kingdom of Great Britain and Northern Ireland MEHDI KARGAHI, Department of Computer and Electrical Engineering, University of Tehran, Tehran, Iran, and School of Computer Science, Institute for Research in Fundamental Sciences (IPM), Iran ALESSANDRO ABATE, University of Oxford, Oxford, United Kingdom of Great Britain and Northern Ireland

In dynamic environments, safety-critical autonomous systems must adapt to environmental changes without violating safety requirements. Model verification at runtime supports adaptation through the periodic analysis of continually updated models. A major limitation of the technique is the high overhead associated with the regular analyses of large state-space models. Our article introduces an adaptive approximation strategy that tackles this limitation by delaying unnecessary model updates, significantly reducing the overheads of these analyses. The strategy is applicable to Markov decision processes (MDPs) and is partitioned into components that can be analyzed independently and approximately. Each component is assigned a priority that depends on its impact on the accuracy of verification, and only the highest-priority components affected by changes are scheduled for updating/approximating. A complete update and verification of the entire model is triggered infrequently when the accuracy drops below a predefined threshold. We provide theoretical guarantees and proofs which ensure that our strategy can be applied without impacting the overall safety of the verified autonomous system. The experimental results from a case study in which we applied the strategy to a rescue robot team show that it is fully robust against safety-critical errors and can achieve a decision accuracy of over 97%.

```math
CCS Concepts: • Computer systems organization →Robotic autonomy; • Software and its engineering
→Model checking;
```

Additional Key Words and Phrases: self-adaptive systems, runtime model verification, formal approximation, Markov models, safety-critical systems

This work is partly funded by the Assuring Autonomy International Programme (AAIP). Authors’ Contact Information: Mehran Alidoost Nia (corresponding author), Department of Computer Science and Engineering, Shahid Beheshti University, Tehran, Iran; e-mail: alidoostnia@sbu.ac.ir; Radu Calinescu, Department of Computer Science, University of York, York, United Kingdom of Great Britain and Northern Ireland; e-mail: radu.calinescu@york.ac.uk; Mehdi Kargahi, Department of Computer and Electrical Engineering, University of Tehran, Tehran, Iran, and School of Computer Science, Institute for Research in Fundamental Sciences (IPM), Iran; e-mail: kargahi@ut.ac.ir; Alessandro Abate, University of Oxford, Oxford, United Kingdom of Great Britain and Northern Ireland; e-mail: alessandro.abate@cs.ox.ac.uk. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org. © 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM 1556-4703/2025/3-ART3 https://doi.org/10.1145/3708560

<!-- page 2 -->

3:2 M. Alidoost Nia et al.

ACM Reference format: Mehran Alidoost Nia, Radu Calinescu, Mehdi Kargahi, and Alessandro Abate. 2025. Efficient Model Verification at Runtime through Adaptive Dynamic Approximation. ACM Trans. Autonom. Adapt. Syst. 20, 1, Article 3 (March 2025), 43 pages. https://doi.org/10.1145/3708560

1 Introduction Self-adaptive and autonomous systems must continuously monitor and analyze the environment and the local system to take care of changes and trigger appropriate adaptation action(s) against them whenever needed. Choosing the right adaptation action depends on the accuracy of adaptation decisions at runtime. In safety-critical applications, the autonomous systems must deploy a rigorous technique to guarantee the accuracy of decisions [37]. A common approach that is widely adopted by the community is the model-driven technique. In this approach, the model of the system is verified against a set of predefined properties [6] to enable making accurate decisions. The stochastic nature of the environment and sequential decision-making in the autonomous system raise the need for Markov decision processes (MDPs) [21]. As the system works through a dynamic environment, the frequency of changes is relatively high. We reflect the changes in the model by a few parameters in a parametric MDP (PMDP), in which the parameters, in our case, mostly imply the possibility of any partial changes in the physical environment that affect the system’s safety. The system can deploy formal verification techniques to verify the system model against a few properties to fulfill the safety and optimization requirements of the autonomous system.

Due to the variability of the model, we need to deploy quantitative verification of models at runtime [11]. Runtime quantitative verification (RQV) is a model-based approach for periodic verification of the system model at runtime. We can dynamically measure quantitative aspects of the autonomous system to ensure that the system meets the expected requirements [50]. On the contrary, there is a model-free runtime verification (RV) technique, a classic approach to escape the limitations of model-checking at runtime [24], e.g., the state-space explosion problem. In this research, however, we utilize the benefits of a model-based approach using formal modeling of the autonomous system to capture both the stochastic behavior of the system and the environment and to analyze the model using incremental logic [28]. Our work centers on strengthening formal models to verify the system behavior at runtime. Instead of relying on observed traces or properties, as is popular in the RV context, we utilize a predefined model to reference the expected system behavior. While RV often aims to overcome the limitations of model-based verification by directly monitoring the system execution, our approach integrates formal methods (like model checking) into the RV process. This allows us to benefit from the strengths of formal verification techniques while still operating within the dynamic context of a running system. We also address the limitation of the model-based verification approach through careful dealing with the abstraction and state-space explosion challenges. The use of models helps to provide a controlled and well-defined environment for verification, mitigating the issues associated with the complexity of real-world systems.

Our proposed approach divides the model into components. When the components are updated periodically, if they are subject to any change, the affected components need to be updated and verified again [15, 48]. In this research, the main approach is to keep the number of updates as low as possible. Therefore, the verification results for most of the components remain valid, and reusing them reduces the cost of deploying the model-based verification technique at runtime.

<!-- page 3 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:3

We face two issues regarding the feasibility of RQV.1 The first is the state-space explosion problem that is handled using an incremental approximation technique [4], as stated earlier. We divide the model into sub-models as strongly connected components (SCCs) and apply 휀-approximate bisimulation technique [1, 8, 31, 56] to each sub-model separately under an aggregation algorithm that calculates the whole model outcome. It divides the SCCs into fixed SCCs (FSCCs) and parametric SCCs (PSCCs). FSCCs are processed offline; however, PSCCs may be subject to change and need runtime model verification. If a parameter is changed at runtime, we need to only re-approximate/re-verify the sub-models affected by that change. We elaborate a specific upper bound for errors for the 휀-approximate technique and establish a logical connection between the accuracy of decisions and the error in RQV of the model.

The second issue is the feasibility of the proposed framework in resource-constrained systems [36]. The ubiquitous nature of most safety-critical autonomous systems is the main obstacle against the system’s access to unlimited resources. We introduce an adaptive approximation strategy that includes minor and major approximation parts considering resource constraints in autonomous systems. The system decides to switch between these two based on the expected accuracy of the results. The system decides to use the minor approximation that causes a delay in updating a few parameters in each round and postpones re-approximation/re-verification of a few components of the model. The system continuously checks the verification results and monitors the changes to control errors. If the error in the results increases, the autonomous system decides to trigger the major approximation. The autonomous system stops the sensitive functionalities of the system that may endanger the safety of the mission and updates the whole model [33]. Afterward, the autonomous system continues its main functionalities and triggers the minor approximation again. Invoking the major approximation undermines the optimization requirements of the system, e.g., the autonomous system accomplishes the mission late but is still safe. In this article, we propose a comprehensive framework for implementing the adaptive strategy that executes the minor approximation by the power of a two-level scheduling algorithm.

To meet the system’s safety requirements, we propose a set of theoretical guarantees. We define a threshold for changes for each component. It shows how much the system can tolerate the errors caused by delays in updates while safety requirements are guaranteed. We show how these thresholds are computed in design time and how the minor approximation uses them to determine which components are prioritized to be updated. We prove that the minor approximation guarantees the safety of the autonomous system if the thresholds are not exceeded. On the other hand, the minor approach tries to keep the update errors of the components under given thresholds. To keep track of changes at runtime, we propose two analyzing steps that are done periodically: change-driven analysis that concerns meeting the threshold constraints and result-driven analysis that performs an acceptance test to the verification results. In both cases, if any deviation is detected, the major approximation is triggered.

Consider a model associated with a robotic arm that must be verified against this property: “The robotic arm will execute an emergency stop when the probability of collision within the next three workflow steps exceeds 80%.” The robot uses the probability of collision to understand the stochastic behavior of the environment and adjust its behavior against any possible change from the environment. Thus, the robot is capable of anticipating critical events, such as collisions that may endanger the main functionalities of the system [43]. If such collision is anticipated, the autonomous system issues a few adaptation actions to avoid collision in advance, e.g., it reduces speed. For a safety-critical autonomous system, two essential features must be considered at

1In this research, by RQV we mean quantitative verification of “models” at runtime [11, 14], which differs from model-free RV [24].

<!-- page 4 -->

3:4 M. Alidoost Nia et al.

runtime: detecting the changes from the environment and accurate decision-making. To detect the changes, the controlling part repeatedly monitors the environment and the local system and verifies if the system model fulfills a few predefined properties. Accurate decisions necessitate using a standard monitoring, analyzing, planning, executing (MAPE) loop in the autonomous system [34, 35]. In this research, we elaborate on a case study of a rescue robot team tasked with transporting safety-critical equipment to the target position. They must avoid collision with an obstacle through the way to the target. The team Mworks within a dynamic environment and must adaptively respond to the obstacles.

The main contributions of the research are as follows:

—We propose an adaptive approximation strategy to distribute the approximation tasks at

runtime by enforcing delay in updating the model. —We prove that the adaptive approximation strategy guarantees the accuracy of the synthesized

actions. —We conduct theoretical error-bound analysis on the proposed approach and determine a

specific upper bound for errors caused by the minor approximation in adaptive strategy. —We elaborate a scheduling algorithm to support the adaptive approximation strategy at

runtime with limited resources. —We propose an approximation framework that meets the constraints of RV of autonomous

systems in safety-critical applications. —We model and analyze the operation of a rescue robot team as a case study that works within

a safety-critical environment.

The rest of the article is as follows. In the next section, we review the running example of the rescue robot team. In Section 3, the preliminaries of formal background are presented. Section 4 is dedicated to the theoretical foundations, proofs, and error-bound analysis. In Section 5, we present the system model for adaptive approximation strategy and formally define the main problem of the research. In Section 6, we present our RQV approach by investigating the proposed framework and the algorithms. The results are investigated in Section 7. The related work is discussed in Section 8. Finally, the article concludes in Section 9, and the future direction is highlighted.

2 Running Example Consider a rescue robot team including three robots that work together in order to carry critical equipment to the target position (see Figure 1). The team consists of a leader robot responsible for carrying the equipment, a caterpillar robot capable of removing obstacles through the path to avoid collisions, and a quadcopter that monitors the path for obstacles. The leader robot makes decisions, and it issues controlling commands to other robots. The robots have real-time communication, and all updates are periodically sent to the leader for decision-making. We review the operational scenario of the rescue team: the leader robot continues its movement toward the target position through the pre-determined path. The quadcopter detects an obstacle that the leader robot encounters in the next few steps. The monitoring data from the obstacles within the environment are updated and sent to the leader robot. The leader robot updates the model, conducts a new analysis of the updated model using the proposed framework, and decides whether the caterpillar must remove the obstacle. If the decision reveals that the elimination of the obstacle is essential, it manages to call the caterpillar robot for obstacle elimination. In the meantime, the leader robot decides whether it should reduce the speed until elimination is done or needs an emergency stop. When the caterpillar robot confirms that the obstacle is removed, the leader robot adjusts the speed and continues the path to the target position. The same autonomous decision-making process is repeated until the delivery of the equipment is finished.

<!-- page 5 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:5

**Fig. 1. The components of the self-adaptive system model include the environment (unmanaged components), the rescue team, including leader (equipment carrier), caterpillar, and monitoring robots (managed components), and the controlling MAPE loop for the autonomous decision-making process (managing components). Unmanaged components refer to those that we have no control over and the system (those we can manage) must adapt according to them.**

In order to implement the rescue robot team scenario in the real world, the team has a set of goals to achieve. The most significant goal is to deliver the equipment safely to the target position. To fulfill this requirement, the leader robot must avoid any collision with obstacles. To do this, the leader robot has a few options, such as reducing the speed, triggering an emergency stop, and calling for the caterpillar robot. The leader robot decides the best adaptive action that guarantees the safety of the equipment. If the leader robot encounters a partial obstacle, it may only reduce its speed. In case of more significant obstacles, it decides to trigger an emergency stop and calls for the caterpillar robot to eliminate the obstacle from the road. The team’s secondary requirement is to deliver the equipment as soon as possible. However, the safety of the equipment has more priority than the delivery time. If the leader robot uses the actions that shorten the delivery time, it gains positive points, namely rewards. Therefore, the system tends to deliver the equipment soon; however, safety must be guaranteed, e.g., choosing the optimized path that takes less time for delivery of the equipment in a safe manner.

## 3 Preliminaries

This section reviews the formal background related to modelling, verification, approximation, and similarity measurement metrics of self-adaptive systems.

3.1 MDP Discrete-time Markov chain (DTMC) is a probabilistic model used in self-adaptive systems to capture the behavior of the system through discrete intervals. Each transition at a discrete-time interval is determined using a probability distribution function. Definition 3.1 formally presents a DTMC.

Definition 3.1 (DTMC). A DTMC over a set of atomic propositions 퐴푃is defined as a tuple 푀= (푆,푆0, 푃, 퐿), where 푆is a (finite) set of states, 푆0 ⊆푆is a set of possible initial states, 푃:

<!-- page 6 -->

3:6 M. Alidoost Nia et al.

```math
푠,푠′∈푆푃(푠,푠′) = 1, and 퐿: 푆→2퐴푃
```

```math
푆× 푆→[0, 1] is a probabilistic transition relation in which Í
```

maps each given state to a subset of 퐴푃.

An MDP is used for modelling sequential decision-making when the system has uncertainty [26]. A discrete-time MDP can capture the probabilistic and nondeterministic behavior of the system and brings stochastic phenomena to the model. We formally denote an MDP through Definition 3.2.

Definition 3.2 (MDP). A discrete-time MDP is formally denoted by a tuple 푀= (푆,퐴, 푃, 푅), where 푆= {푠1, . . . ,푠푛} is the finite set of states, 퐴= {푎1, . . . ,푎푙} indicates the set of actions (choices), 푃: 푆× 퐴× 푆→[0, 1] shows the transition probability function, in which ∀푠∈푆, ∀푎∈퐴: Í

푠′ ∈푆푃(푠,푎,푠′) = 1, and 푅: 푆× 퐴→R specifies the reward function that maps each transition to a real number.

When it comes to using an MDP to model a self-adaptive system, the nondeterministic choices among available actions in each state must be resolved. We define the policy mechanism by Definition 3.3 that resolves which action should be taken in each state.

Definition 3.3 (Policy). The policy mechanism for an MDP 푀is denoted by a function 훿: 푆→ 퐷(퐴) such that for each state 푠∈푆, it selects a probability distribution 훿(푠) over 퐴, and 퐷denotes a distribution function.

As mentioned earlier, the self-adaptive systems are supposed to work through a dynamic environment so that the model may be changed periodically. To address the dynamic nature of the environment and components of the local system, we use PMDP constructed by a set of probabilistic parameters that can be updated at runtime. Definition 3.4 formally presents a PMDP.

Definition 3.4 (PMDP). A PMDP is denoted by a tuple 푀= (푆,퐴,푉, 푃, 푅), where 푆, 퐴, and 푅are as in Definition 3.2. 푉indicates a finite set of probabilistic parameters. 푃: 푆× 퐴× 푆× 푉→[0, 1] denotes the parametric transition probability function that maps each state-action-next state tuple and a probabilistic parameter to a real number between 0 and 1. The function 푃captures the transition probabilities which depend on the parameters in 푉, and these parameters may change over time, reflecting the dynamic nature of the transitions. Note that the valuation vector of parameters 푉is represented by 휃∈Θ, where 휃is the current valuation of the parameters and Θ defines the space for every possible evaluation.

Example 3.1. During this example, we show how we can model our running example using an MDP. The model of the environment indicates the obstacle that the robots may face. The model is constructed using the data gathered by the monitoring robot, and is updated by new data at runtime. The process of transforming the data into a Markov model is discussed in [49].

We have used the extended Pearson-Tukey three-point approximation technique [32] for data modelling. The result of the obstacle model is denoted by Figure 2(a) where each node is branched into three nodes, each representing the occurrence of “no obstacle,” “partial obstacle,” and “obstacle” in the half meter, respectively. The option “no obstacle” states that the leader robot can pass through the predetermined path with its regular speed without any stop. The option “partial obstacle” is referred to an obstacle that the leader robot can handle, but the robot needs to reduce speed for safety purposes. The option “obstacle” determines the situation that the size of the obstacle is considerable, and must be eliminated by the caterpillar robot before passage. The environment model is a finite parametric DTMC in which the parameters indicate the probability of facing obstacle (푝표푏푠), no obstacle (푝푛표푏푠), and partial obstacle in the next half meter. The parameters are updated at runtime. Figure 2(b) represents the distance model that is synchronized with the obstacle model in order to reflect the position of the robots. The combination between the environment and

<!-- page 7 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:7

(a) (b)

**Fig. 2. The environment model: (a) the obstacle model of the environment resulted from a data-driven approach. 푝푛표푏푠and 푝표푏푠denote the probability that the leader robot faces “no obstacle” and “obstacle” in the next half meter. In addition, 푑and 푑푖푠푡represent the current position of the leader robot and the final target distance. (b) The distance model of the environment is synchronized with other parts of the system so that each state indicates the next half meter progress of the robot team.**

(a) (b) (c)

**Fig. 3. The model of the local system including the rescue robot team members: (a) the model of the monitoring robot, (b) the model of caterpillar, and (c) the model of the leader robot.**

the distance models gives our physical environment model. Two models synchronize with common distance step “d,” which is initially the half meter. It means that for every half meter, the model must determine if an obstacle is appearing or not. In addition, we have an auxiliary parameter called “dist,” showing the total distance between the starting point and the destination. We use the PRISM probabilistic model-checker [38] for modeling and verification of the system. The PRISM code of the model is described through Listing A1 (see Appendix A.1).

The robots’ model includes three sub-models of the rescue robot team. The first is the leader robot. Figure 3(c) denotes the behavior of the robot against partial and considerable obstacles. The 푧variable represents the states of the leader robot. As denoted by the figure, the leader robot can “stop,” “run,” “e-stop” or emergency stop, and “reduce speed.” The changes in these states are synchronized with the environment model, and the probabilistic parameters “no,” “po,” and

<!-- page 8 -->

3:8 M. Alidoost Nia et al.

“ob” represent the probability of facing no obstacle, partial obstacle, and an obstacle, respectively. Partial obstacles are the ones that could be easily passed by reducing speed. If the monitoring robot detects an obstacle, the leader robot decides to trigger an emergency stop, and the caterpillar robot (see Figure 3(b)) starts the operation of removing that obstacle. The caterpillar robot also has a state variable 푦, showing its state including “standby,” “handle,” and “remove.” These states denote the current business of the caterpillar robot. The first shows its readiness for work, the second represents that the robot is handling the obstacle, and the third illustrates that removing the obstacle is completed. In addition, the 푓variable denotes the state of the environment. If any obstacle is detected, the value of 푓will be 2; “hand” and “st” are two guards for handling an obstacle and finishing the caterpillar duty, respectively. If a partial obstacle is detected, the leader robot reduces its speed and tries to pass the obstacle safely. Listings A2, A3, and A4 (see Appendix A.2) denote the PRISM codes for robots’ models. The actions in the leader module include 표푏, 푝표, 푛표, and 푑푠, which represent the actions in the face of an obstacle, partial obstacle, no obstacle, and receiving to the destination, respectively. The non-determinism through the actions is modeled by the MDP and resolved at runtime by system policies. 푝ℎ푎푛푑in the caterpillar model denotes the probability of handling the obstacle by the caterpillar robot. Once the obstacle is removed, the state of the leader robot is changed to run. 푝푚표푛illustrates the probability of detecting a change within the monitoring process that leads to updating the model of the environment with new data. The details of the monitoring robot model are presented in Figure 3(a). The monitoring robot model has a state variable 푥that represents “monitor,” “detect,” and “update” situations in collecting new data from the environment. If an obstacle is detected, the monitoring robot declares it and updates the model to propagate the new information to the leader and caterpillar robots. A PMDP models all five components of the system together.

3.2 Formal Properties The requirements of the system are defined as a few formal properties. To express quantitative and probabilistic properties for verification of autonomous system models, we use probabilistic computation tree logic (PCTL) [19] as denoted in Definition 3.5.

Definition 3.5 (PCTL). Considering the transition probability function 푃, the formula 푃⊲⊳푝[휑] asserts that the probability of 휑being true satisfies the bound ⊲⊳푝, where ⊲⊳∈{>, ≥, <, ≤}, p is a probability (푝∈[0, 1]), 휑and 휓denote state and path formulas, respectively. More formally, the syntax of PCTL is defined as follows:

```math
(푠푡푎푡푒푓표푟푚푢푙푎) 휑::= 푡푟푢푒| 푏| 휑1 ∧휑2 | ¬휑| 푃⊲⊳푝[휓],
(1)
```

```math
(푝푎푡ℎ푓표푟푚푢푙푎) 휓::= 휑1 ∪≤푡휑2 | 휑1 ∪휑2 | 푋휑,
(2)
```

where ∪denotes the Until operator, X indicates the Next operator, and 푏∈퐴푃(AP is the set of atomic propositions). Assume that 푟expresses the rule for computation of reward structure, max denotes the maximization policy of the total expected reward, 푅indicates reward operator, 퐹is an operator showing the “Eventually” or “Finally” logic in PCTL, and 휑reflects a set of states that represent an expression or a label. Formula (3) denotes the general form of a PCTL formula that is used to calculate the maximum total expected reward of the model in which 휑is finally satisfied and 푟denotes the reward structure:

푅푟

```math
푚푎푥=? [퐹휑].
(3)
```

Example 3.2. The rescue robot team needs two types of requirements. The first is the safety requirement in which the safety of the equipment must be guaranteed. As denoted in Table 1, the

<!-- page 9 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:9

**Table 1. The Supported Templates and Examples for Expressing the Properties by the Framework**

Name (Operator) Template Property Example Description

```math
State
formulas
휑1 ∧휑2 | ¬휑| 푃⊲⊳푝[휓]
푃≥1[퐹≤10“stop” ∧“safe”]
```

Next 푋휑 푃≤0.05[푋“obstacle”]

```math
Untila
휑1 ∪≤푛휑2
푃≥0.95[“obstacle” ∪≤3
```

Bounded

an is a natural number less than 50. bIn this research, each workflow step of the robots corresponds to a transition in our models.

first example expresses the safety requirement of the equipment delivery by a PCTL formula. It says that with probability 1, the leader robot receives to the destination (label “stop”) in 10 steps (5 meters) and collides with no obstacle (label “safe”). This is a simple safety example, and all PRISM codes for safety properties are explained in detail in Appendix A.3, which are denoted by Listing A5 (see Appendix A.3). The second requirement is the optimization of the total reward (utility) of the system. As denoted by Listing A5 (see Appendix A.3), the third property ensures the safety of the equipment while maximizing the total reward of the system in a way that the system finds the best possible actions that can reduce the delivery time. This property is inspired by the PCTL formula denoted in Formula 3. We refer to it as the optimization requirement.

### 3.3 Quantitative Verification

The reward mechanism is the pivot for quantitative decision-making (e.g., an optimization decision) [3] where the reward structure is assigned to states and/or actions [26].

Definition 3.6 (Expected Reward). Total expected reward for a path 휋= 푠0,푠1, . . . ,푠푛over an MDP 푀is denoted by 퐸(휋), and calculated using (4):

### 푛−1 Õ

퐸(휋) =

푖=1

where 푅(푠푖,푎) indicates the reward value assigned to the transition (푠푖,푠푖+1) in ith step by action 푎. To calculate the maximum expected reward (MER), we traverse all the reachable paths Π =

The equipment is safely transmitted to the target position.

The probability that the leader robot faces an obstacle in the next step is at most 0.05.

The probability that in maximum three workflow steps,b the obstacle is removed, is greater than 0.95.

“running”]

```math
푃(푠푖,푎,푠푖+1) × 푅(푠푖,푎),
(4)
```

{휋1, 휋2, . . . , 휋푚} starting from initial states to final states determined based on the given property. The MER is calculated based on formula (5):

```math
MER = max{퐸(휋푗)}, 푗∈{1, . . . ,푚}.
(5)
```

<!-- page 10 -->

3:10 M. Alidoost Nia et al.

**Fig. 4. The environment model is initialized for the next three steps of the system where the probability of facing a partial obstacle is zero.**

The self-adaptive systems need RQV to verify the system against the properties, and secondly synthesize the sequence of actions that must be executed in the next few steps. Definition 3.7 denotes RQV and its outcomes.

Definition 3.7 (RQV). RQV verifies an MDP 푀with the current valuation vector 휃∈Θ for its parameters against the predefined properties Φ = {Φ1 . . . Φ푛} (푛is finite) that calculates MER as 푈 and a set of synthesized actions as 훼⊆퐴. Formally, RQV is denoted by (6):

```math
(훼,푈) = 푅푄푉(푀(휃), Φ),
(6)
```

where 푖∈N and the set of properties Φ = Φ1, Φ2, . . . , Φ푖is defined by the PCTL formula.

Given an MDP and a PCTL formula, probabilistic model checkers such as PRISM [38] or Storm [22] can compute a set of actions 훼and calculate the total utility of the system 푈. Note that this verification can be performed at runtime, whenever the probabilities change.

Example 3.3. Consider the model denoted by Figures 4 and 3 that consist of two parts: the first is the environment model, and the second is the model of the robots team. We investigate the model for a subsequent three workflows (1.5 meters). Consider the reward value of all transitions is calculated according to Listing A6 (see Appendix A.3). In addition, the probability of facing partial obstacles is assumed zero in this example, and for the sake of simplicity, only the leader robot model is considered. The initialized model of the environment for the three successive steps is denoted by Figure 4, where the gray states denote the situations, which in our scenario do not happen. If a gray state is detected (e.g., an obstacle really exists but is not detected), the situation for the leader robot is unsafe.

The model is composed of two sets of states 푆1 = {푠푡표푝,푟푢푛,푒_푠푡표푝,푟푒푑푢푐푒_푠푝푒푒푑} and 푆2 = {푖푛푖푡,푛표푏푠1,표푏푠1,푛표푏푠2,표푏푠2,푛표푏푠3,표푏푠3,푛표푏푠4,표푏푠4,푛표푏푠5,표푏푠5,푛표푏푠6,표푏푠6,푛표푏푠7,표푏푠7}, actions퐴= {푝표,푛표,표푏,푑푠}, a set of parameters 푉= {푝1, 푝2, 푝3}, and a set of initial states 푆0 = {푠푡표푝,푖푛푖푡}. We want to verify the model against the property 푅푟

푚푎푥=?[퐹≤3 “푆퐴퐹퐸”], where label “SAFE” refers to the states that are safe for the leader robot according to the safety requirements stated in Section 3.2, where all next states of the environment are correctly detected, and the leader robot adjusts its behavior according to the right state of the environment. In this example, the probability of facing no obstacle above 0.95% is assumed a safe transition policy. The parameters valuation is assumed

<!-- page 11 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:11

푝1 = 0.05, 푝2 = 0.99, 푝3 = 0.98. The model checker verifies the model against the property to find the best “SAFE” path.

Starting from the initial, we must find a path with length three that maximizes the total expected reward and keeps the system safe. Investigating all reachable paths, path 휋1 maximizes the total expected reward of the system while the safety of the leader robot is preserved. The path 휋1 describes a trace starting from the initial states of the leader robot model (see Figure 3(c)) and the environment (see Figure 4) that is (푠푡표푝,푖푛푖푡). The leader robot continues in “푠푡표푝” states because of the existence of an obstacle which is denoted by 표푏푠1 in the environment model. When the probability of facing an “obstacle” is very low, the leader robot state changes to “푟푢푛” and stays in the same state for the next two steps. Applying formulas (4) and (5), MER is calculated as follows:

(푝푎푡ℎ)휋1 = (푠푡표푝,푖푛푖푡).(푠푡표푝,표푏푠1).(푟푢푛,푛표푏푠3).(푟푢푛,푛표푏푠5) (MER)퐸(휋1) = (0.95 × 0) + (0.98 × 2) + (0.96 × 2) = 3.94. The autonomous system plans the sequence of actions훼= {표푏,푛표,푛표} for the next three workflow steps of the leader robot.

3.4 Formal Approximation We start by presenting trace (a similar concept to a path) and the notion of trace equivalence in Markov models, which are defined by Definitions 3.8 and 3.9, respectively.

Definition 3.8 (Traces). Assume that 푀be an MDP and the set of its traces is represented by Traces(s). It contains the minimal set that fulfills three conditions for each state 푠,푠′ ∈푆, corresponding actions 푎∈퐴, and the set of final states 푆퐹⊆푆:

```math
(1) 휖∈푇푟푎푐푒푠(푠),
(2) √∈푇푟푎푐푒푠(푠) ⇔푇푟푎푐푒푠(푠) contains at least a final state,
(3) 푎휎∈푇푟푎푐푒푠(푠) −→∃푠
```

```math
′ ∈푆, (푠푎−→푠′) ∧휎∈푇푟푎푐푒푠(푠
```

′ : 푠

′), where 휖, √, and 휎denote empty input, (successful) termination, and a sample trace of states and action, respectively. In addition, 푠푎−→푠′ denotes a transition from state 푠by action 푎to state 푠′.

Definition 3.9 (Trace Equivalence). Let 푠,푠′ ∈푆be two states of an MDP. We say that the two states are trace equivalent if and only if starting from each of those states, they have equal sets of traces, which is presented as: 푠,푠′ ∈푆are trace equivalent ⇔푇푟푎푐푒푠(푠) = 푇푟푎푐푒푠(푠′).

We use a special type of probabilistic bisimulation [9] as approximate technique, namely 휀-approximate probabilistic bisimulation or simply 휀-bisimulation [1, 8, 56]. It works based on the state bisimilarity rules that are presented in Definition 3.10. In this approach, bisimilar states, referring to those states that reflect a similar behavior, are merged. 휀is a threshold for probabilistic bisimulation. As the size of 휀increases, more reduction is expected.

Definition 3.10 (휀-Approximate Bisimulation). Consider that 푀is an MDP with countable statespace, 푠1,푠2 ∈푆, 푎∈퐴, and 휀∈[0, 1], then the relation R휀⊆푆× 푆is a binary symmetric relation that is called 휀-approximate probabilistic bisimulation relation if the following conditions are fulfilled:

```math
(1) ∀(푠1,푠2) ∈R휀, ∃푎∈퐴푠.푡. 푠1 푎−→· 푎푛푑푠2 푎−→·,
```

```math
(2) ∀(푠1,푠2) ∈R휀, ∀b푆⊆푆푡ℎ푒푛푃(푠2, R휀(b푆)) ≥푃(푠1, b푆) −휀,
```

<!-- page 12 -->

3:12 M. Alidoost Nia et al.

where R denotes the bisimilar relationship between two states, b푆refers to a 휀-bisimilar set of states, R휀represents the 휀-bisimilar relationship on bisimilar states, and R휀(b푆) is a corresponding set of 휀-bisimilar formally defined as R휀(b푆) = {푠

```math
′ ∈푆| ∃푠∈b푆| 푠R 푠
```

′}. In addition, 푠1 푎−→· denotes a transition from state 푠1 by action 푎to every possible state.

As presented through Definition 3.10, the 휀-approximate relation simply expresses that for each state change in 푠1 dominating in set b푆, 푠2 can have a choice with maximum similarity into the set 푅휀(b푆) where the difference is tolerated up to threshold 휀. In our previous research, we proposed an average metric for error-bound of 휀-bisimulation, namely AVEB [4]. We formally denoted that the error of applying 휀-bisimulation to an MDP is bounded by | 휀× 푟× ( 푘+1

2 )| where 푘is the length of the trace.

The approximation has a cost and brings some errors to the results. As discussed in [30], the best metric works for evaluating an approximate method that uses bisimilar traces is Total Variation which is presented in Definition 3.11. It determines an upper bound for errors after applying 휖-bisimilar approximation. As denoted by Formula 7, it calculates the supremum of the distance between each two bisimilar parts of the model.

Definition 3.11 (Total Variation). For an MDP 푀, assume that 푠1,푠2 ∈푆, and 푃푘and 푃′

푘denote probability transition functions. We define Total Variation metric 푑푇푉(7) on a 휎-algebra of subsets of Ω as an upper-bound 푠푢푝(supremum) for the distance between each two probability measures each corresponding to the transitions in a trace with length 푘starting from 푠1 and 푠2:

푑푇푉(푃푘, 푃′

푘) := 푠푢푝{푠1,푠2,.} |푃푘(푠1, .) −푃′

```math
푘(푠2, .)|.
(7)
```

푑푇푉is a metric that calculates the difference between two probability transition functions. It is useful when we want to set an upper bound for errors resulting from approximation and is the most similar metric to statistical distance [59]. Another metric for measuring the probability difference is the Hellinger distance [61] used for quantifying the similarity between two probability distributions. As denoted by Formula 8, it constructs a bounded metric over two given probability distributions where the maximum distance is 1 if one of them reflects a probability of 0. To calculate the similarity, it determines the direct distance between two probability functions in space. Therefore, the formula has a pattern like the Euclidean distance.

Definition 3.12 (Hellinger Distance). For two discrete probability distributions 푃푘and 푃′

푘, the Hellinger distance is defined by (8) inferred by Euclidean norm:

v u t 푘 Õ

푘) = 1 √

q

푑퐻(푃푘, 푃′

p

푃푖−

푃′

```math
푖)2.
(8)
```

(

2

푖=1

There is an interesting relationship between 푑푇푉and 푑퐻in which inequality (9) is held for two probability distributions 푃푘and 푃′

푘[10]:

√

퐻(푃푘, 푃′

푘) ≤푑푇푉(푃푘, 푃′

```math
2푑퐻(푃푘, 푃′
푘).
(9)
```

푑2

푘) ≤

√

2푑퐻(푃푘, 푃′ 푘) is always greater than or equals 푑푇푉because the values reflected by them are in the range of [0, 1]. The calculated lower bound in Formula 9 has a proof which can be found in [10]. This equation is a significant result for binding the upper-bound of errors. Later, we use them to prove an upper-bound of the approximation error.

By looking at Formula 8, we can easily see that

<!-- page 13 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:13

## 4 Theoretical Findings

In this section, we investigate the errors caused by delaying the updates in the parameters’ valuation and guarantee a certain upper bound for the error of decisions. We denote the approximate model (caused by the incremental approximation) and the delayed-update approximate model (caused by the adaptive approximation strategy) with 푀퐴and 푀퐴′, respectively. We show parameters of the model by 푝푖∈푉= {푝1 . . . 푝푛} (푛is finite) for 푀퐴and 푝′

푖∈푉′ = {푝′

## 1 . . . 푝′ 푛} for 푀퐴′. According to Definitions 3.7 and 3.11, we measure the difference between 푀퐴and 푀퐴′ in terms of:

—Synthesized actions: 훼and 훼′

—Total utility: 푈퐴and 푈퐴′

where the total utilities are calculated for a few workflow steps 푘by 푈퐴= Í푘

푖=1 푝푖× 푟푖and 푈퐴′ = Í푘

푖and 훼′ are the delayed-update parameter valuation for 푝푖 (evaluated by 휃푖) and synthesized actions belong to 푀퐴′, and 푟푖represents the reward of step 푖.

푖=1 푝′

푖× 푟푖. Consider that 푝′

The accuracy of the synthesized actions guarantees the accuracy of decisions. In addition, it decreases the difference between the total utility of RQV in 푀퐴and 푀퐴′. We argue that by keeping 훼= 훼′, the system is still safe, even if푈퐴≠푈퐴′. However, the error is bounded. The first step toward the error-bound analysis of 푅푄푉(푀퐴′, Φ푖) is to investigate the role of 훾푗in each component 퐶푗.

### 4.1 Threshold for Changes

The total update error of the component퐶푗is calculated using the difference between the parameters’ valuation between the updated and delayed-update models as denoted by (10):

### 푘 Õ

훾′

|푝푖−푝′

```math
푖|.
(10)
```

푗=

푖=1

To determine the error bound, we calculate the maximum allowed deviation from the accurate valuation of the parameters. The deviation is investigated by comparing the path leading the system to its maximum utility and the nearest utility to the maximum. We introduce a metric called tolerable error [3] which is denoted by 푈+(푘).

Definition 4.1 (Tolerable Error). Assume that path 휋푚with length 푘(푘is finite) contains a set of actions 훼that maximizes the total utility of the system 푈푚and 휋푛with length 푘determines the second greatest total utility of the system 푈푛. The tolerable error of the system is calculated for any path with length 푘by (11):

```math
푈+(푘) = 푈푚−푈푛.
(11)
```

We extend the notion of tolerable error to the tolerable valuation error 훾푗by assuming identical reward for reaching all states. Intuitively, this threshold is estimated by the difference of the parameters’ valuation corresponding to 휋푚and 휋푛. We need to construct parameters’ valuation tuples as (푝푚, 푝푛) where each probability belongs to the transitions on paths 휋푚and 휋푛. We map them to the Euclidean space [17], and calculate the difference between tuples by ||√푝푛−√푝푚||2. We know that the Euclidean distance dominates the Helinger distance as denoted by (12):

```math
2
||√푝푛−√푝푚||2 ≤푑퐸(푝푛, 푝푚).
(12)
```

푑퐻(푝푛, 푝푚) = 1 √

One can calculate (10) by 푑푇푉, and according to the relationship denoted by (9), 푑퐻is an upper bound for 훾′

푗. In addition, we denoted that the threshold 훾푗is calculated by Euclidean distance. According to the relationship shown in (12), 푑퐻(푝푛, 푝푚) is a tight and conservative choice for limiting the parameters’ valuation error. Consequently, 훾푗for any component 퐶푗is calculated by

<!-- page 14 -->

3:14 M. Alidoost Nia et al.

**Fig. 5. An example of PMDP with 푛components for the use in proof of Theorem 1.**

푑퐻(푝푛, 푝푚), and can be expanded to (13) for all tuples (푝푛, 푝푚) each related to the paths 휋푚and 휋푛 with length 푘:

v u t 푘 Õ

훾푗= 푑퐻(푝푛, 푝푚) = 1 √

p

p

푃푚푖−

```math
푃푛푖)2.
(13)
```

(

2

푖=1

4.2 Theoretical Error Analysis In this section, we illustrate how meeting the update thresholds leads the self-adaptive system toward an accurate decision-making. At first, we discuss the relationship between the accuracy of synthesized actions and 훾′

푗.

```math
Theorem 1 (Accuracy of Synthesized Actions). Considering a delayed-update approximate
model 푀퐴′, ∀퐶푗∈푀퐴′, if 훾′
```

푗≤훾푗, then 푅푄푉1(푀퐴, Φ푖) = 푅푄푉1(푀퐴′, Φ푖)2 meaning that 훼= 훼′.

Proof. Investigating the formal proof of Theorem 1, we start by how the threshold must be calculated in a sub-model. As we calculate the maximum total utility of the system in each RQV, the error in the results can be tolerated as much as the distance between the maximum total utility of the system 푈퐴

푘for a path with length 푘. 훾푗 ensures that the error does not lead to a wrong path (e.g., the path that 푈+

푘and the second maximum total utility, namely 푈+

푘is calculated over it). Figure 5 denotes an assumed model with a set of SCCs, each shown by a 퐶푖label (푖∈{1 . . .푛} and 푛is finite), being surrounded by gray circles. Each state may have inner and outer transitions. The inner transitions connect the states within an SCC, and outer transitions establish a loose connection among SCCs. As denoted by the figure, the path 휋1 = 푠1푠2 . . .푠푘implies the maximum total utility of the system if the parameters of the model are updated. In addition, 휋2 = 푠′

1푠′ 2 . . .푠′ 푘and 휋3 = 푠′′

## 1 푠′′ 2 . . .푠′′ 푘denote the paths associated with 푈퐴′

푘 and 푈+

푘. We measure the possible scenarios for all paths with length 푙≤푘in each sub-model and determine a certain error boundary based on the fact 푈+

푘< 푈퐴

푘. As the reward for transitioning to each state is assumed to be equal, the upper bound for changes in parameters of each sub-model 퐶푗is calculated using (14) according to Definition 3.11:

### 푘 Õ

### 푘 Õ

푝′′

푑푇푉(푝푛, 푝푚) := 푠푢푝|

푝푖−

```math
푖|.
(14)
```

푖=1

푖=1

푘and 푈퐴

푘, one can infer the threshold as 훾푗= 푑퐻(푝푛, 푝푚) according to (13). We assumed that 훾′

According to the distance between 푈+

푗≤훾푗and the same fact is reflected by the upper bound

2Index 1 refers to the first element of tuple (훼,푈) resulted by the RQV function which is defined by Definition 3.7.

<!-- page 15 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:15

calculated in (14) which is mathematically bounded by the threshold 훾푗because of the relation between Helinger and Total Variation denoted earlier by (9). In our proof, we applied the worst-case scenario to calculate the upper bound safely. It means that two paths 휋1 and 휋3 have no shared sub-path, and all parameters are affected by the delayed-update error.

푘and 푈퐴′

Now, we calculate the distance D between 푈퐴

푘 as (15):

### 푘 Õ

### 푘 Õ

### D = |푈퐴

푘−푈퐴′

푝′

푝푖× 푟푖−

```math
푖× 푟푖|.
(15)
```

푘| = |

푖=1

푖=1

Considering the constant reward 푟for all transitions, the distance is reduced to (16):

### 푘 Õ

### 푘 Õ

푝′

푖| = 푟× 훾′

### D = 푟× |

푝푖−

```math
푗.
(16)
```

푖=1

푖=1

According to the assumption, we know that 훾′

푗≤훾푗, and by considering (14), we can infer that the distance D is less than the tolerated error boundary between 푈퐴

푘and 푈+

푘. To this end, the minor approximation guarantees that if 훾′

푗≤훾푗, then the selected path corresponding to 푈퐴′

푘 is the same as the path associated with 푈퐴

푘. Therefore, the synthesized actions are the same, as the two models execute the same traces. □

Corollary 1 (Error of Delayed-Update Model). For any component 퐶푗within the delayedupdate approximate model 푀퐴′ with threshold of change 훾푗, if 훾′

```math
푗≤훾푗, then the error of RQV is
bounded by 푟× Í푛
```

푗=1 훾푗.

Proof. As denoted in the proof of Theorem 1, we showed that for each component 퐶푗, the total error is calculated by the difference between푈퐴

푘and푈퐴′

푘(see Equation (16)). Assume that the model is divided into 푛components (푛∈N is finite). Therefore, the total error of the model equals to the sum of errors in all components calculated by 푟× Í푛

```math
푗≤훾푗, the
total error resulted by delaying in update of a few parameters, is bounded by 푟× Í푛
```

푗=1 훾′

푗. Considering the assumption 훾′

푗=1 훾푗. □

Corollary 2 (Total Error). For a delayed-update approximate model 푀퐴′ which is approximated by 휀-approximate bisimulation, the error of RQV is bounded by |푈퐶

### 푘| ≤푟(Í푛

푘−푈퐴′

푗=1 훾푗+ 휀푘), where 푈퐶

푘denotes the maximum utility of the concrete model for a trace with length 푘.

Proof. We calculate the incremental error of the system affected by both 휀-approximate bisimulation technique and minor approximation. The former is calculated in [4] as {휀× 푘× 푟}, and the latter is determined by Corollary 1 as 푟× Í푛

푗=1 훾푗. The total error of these two parts is bounded by their additive errors as {푟× (Í푛

푗=1 훾푗+ 휀푘)}. □

Corollary 3 (Minor Approximation). The minor approximation guarantees the accuracy of decisions in delayed-update approximate model.

```math
푗≤훾푗for all components 퐶푗∈퐶.
According to Theorem 1, if the condition 훾′
```

Proof. The minor approximation runs under the condition 훾′

푗≤훾푗holds, RQV of the delayed-update model achieves the same decisions (synthesized actions) like RQV of the updated model. Therefore, the minor approximation approach guarantees the accuracy of decisions. □

As the minor approximation leads to accurate decisions, the safety of the autonomous system is guaranteed. However, if the condition 훾′

푗≤훾푗does not hold, the autonomous system does not trigger the minor approximation, but invokes the major approximation, immediately. The theorem and the corollaries assure the utilization of formal approximate technique in safety-critical applications where the accuracy of decisions is significant.

<!-- page 16 -->

3:16 M. Alidoost Nia et al.

## 5 Adaptive Approximation Strategy

### 5.1 System Model and Assumptions

Regarding the system model, the following assumptions are considered:

—A PMDP constructs the integrated model of the autonomous system. —The model is divided into a set of sub-models using the SCC extraction algorithm [55], and

each sub-model is approximated/verified independently [4]. —There is a mechanism for aggregating the verification result of sub-models [4]. —Each change is reflected by the parameters’ valuation update in each round of MAPE. —Each sub-model has a threshold for change which is computed offline. When the change

exceeds the threshold, that sub-model needs to be reconstructed/re-approximated. —Each delayed-update sub-model has a freshness value that indicates the age of the sub-model

since the last reconstruction/re-approximation. —The model has a global threshold of change and freshness value for the entire system model.

### 5.2 Problem Definition

The size of the model is relatively large and must be reduced by approximation techniques [4]. Due to the dynamicity of the environment, the number of changes is considerable, and the autonomous system needs to reconstruct/re-approximate the model to include new changes. The main issues are the system’s limited resources and temporal constraints for decision-making in safety-critical applications. The main problem of the research is how we can reduce the approximation/verification overhead at runtime while the safety requirement of the system is guaranteed. An early solution to this problem is to use the incremental approximation technique [4], divide the model into a set of sub-models, and approximate each sub-model independently. When the new change is monitored, only the affected sub-models need to be re-approximated. This approach works for system models that experience partial changes meaning that only a few sub-models are affected. Cyber-physical systems like ubiquitous robots have limited resources, and frequent changes impose considerable overhead. The idea of this research is to propagate the overhead of reconstruction/reapproximation of the model by postponing unnecessary updates and prioritizing updates of the sub-models concerning their impact on the safety requirement. In this regard, we define two types of approximation approaches:

Minor Approximation. The self-adaptive system tends to only approximate a few sub-models in each round based on the resource constraints and divides the overhead of the approximation into several rounds of MAPE. Each sub-model has its local threshold 훾for change and freshness value 푓. Threshold 훾denotes the total, minor changes in parameters’ valuation that the sub-model can tolerate. If the additive value of changes exceeds 훾, the sub-model is prioritized for update and needs to be re-approximated by applying the new parameters’ valuation. In addition, the freshness value indicates the age of the last change by which the sub-model is not updated. If the system has additional resources, the sub-models with the worst freshness values take the priority to be updated/re-approximated.

Major Approximation. When the error in decision-making results increases, the approximation must be renewed globally for all sub-models to meet the system’s safety requirements. We propose two analysis methods for this purpose: change-driven analysis and result-driven analysis. The first is conducted based on the global threshold for changes Γ. The global change is incrementally grown when the minor changes are increased in a relevant number of sub-models. As for the result-driven analysis, the system periodically compares a few current results 푦′ with the expected results 푦 employing acceptance test [45, 53]. If the deviation of the result is considerable, the self-adaptive system triggers a major approximation strategy to improve the accuracy of the results.

<!-- page 17 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:17

**Fig. 6. Comparing the effect of minor and major approximations on the accuracy of the verification results in a dynamic environment.**

Adaptive Approximation Strategy. In our proposed framework, the autonomous system can adaptively switch between the two types of approximation techniques, i.e., Minor and Major. The autonomous system tries to keep itself aligned with the minor approximation because it is more efficient and better matches the resource limitations of the autonomous system, especially at runtime. However, suppose the system could not tolerate the errors caused by the minor approximation. In that case, the managing part adaptively switches to the major approximation technique and waits until all model components are updated. After that, the autonomous system again switches to the minor approximation, and all parts of the autonomous system return to their ordinary duties.

Figure 6 denotes the effect of minor and major approximation approaches on the accuracy of decisions when the frequency of updates is relatively high. On delaying the parameters’ update process, the accuracy of verification results may be decreased because the model needs to fully match the instantaneous situation of the system. The system executes the minor approximation in several rounds in order to update a few components. After triggering the first minor strategy, the accuracy of the results increases partially. If the dynamicity of the environment is high, the minor approximation cannot handle the major waves of changes, and the system decides to trigger the major approximation after 26 minutes. The managing part (e.g., the leader robot) decides to fire an emergency stop action and waits until the major approximation strategy is executed. This action keeps the accuracy of the results above a predefined threshold, e.g., 95%, to meet the system’s safety requirements. After applying the major approximation, the system’s accuracy increased drastically, switching to the minor approximation adaptively.

Problem Definition. Given a PMDP 푀with a set of parameters 푉= {푝1, . . . , 푝푚} (푚is finite), a set of properties Φ = {Φ1, . . . , Φ푛} (푛is countable) including safety and optimization requirements and a set of sub-models 퐶= {퐶1, . . . ,퐶푗} where each sub-model has a configuration set 푐푗= {푓푗,훾푗,훾′

푗}. Propose a scheduling algorithm for implementation of adaptive approximation strategy that prioritizes re-approximation of each sub-model 퐶푗based on its deviation from the expected parameters’ valuation 훾′

푗with threshold 훾푗, freshness value 푓푗, and possible resources 퐿by applying the minor approximation. An approximation task 휏푗= (푑푗,푒푗) for each component 퐶푗within a look-ahead horizon 퐻is assumed where 푑푗and 푒푗denote the deadline and execution time. The scheduling must avoid using the major approximation as much as possible, and must perform change-/result-driven analysis to ensure the safety requirements of the system.

<!-- page 18 -->

3:18 M. Alidoost Nia et al.

**Fig. 7. The architecture of the resource-aware approximation framework for RV of safety-critical self-adaptive systems.**

## 6 RQV Approach

Our practical solution to the main problem of the system is proposed as a framework presented in Figure 7. We divide it into design-time and runtime solutions in which a considerable overhead of the system is reduced by extensive offline pre-computations. The framework works according to the requirements of the standard MAPE loop and aims at efficient verification of the autonomous system model in safety-critical applications. It is composed of the following components and engines:

—System Model Manager: It constructs the parametric model of the system for the first time,

and divides the model into a set of independent sub-models 퐶1 . . .퐶푗including parametric and non-parametric (fixed) ones. —Approximation Engine: The engine approximates each sub-model by new parameters’ valuation

푈푝푑푎푡푒(휃). Then, the engine updates current values for changes and freshness of the sub-

models as a tuple (훾′, 푓). —Monitoring: It consists of a few sensors and monitoring devices that extract the changes and

maps the changes to parametric valuations at the beginning of each MAPE step. —Scheduler: It is composed of two algorithms: the priority assignment algorithm and the

scheduling algorithm which are centralized. —Verification Engine: It verifies the model against a set of pre-defined properties Φ and the next

adaptation actions 훼⊆퐴are decided if need be.

We define the following metrics and parameters that are used in our proposed approximation framework.

—Update Error 훾′

푗of Component 퐶푗: It denotes the additive error caused by changes from a component’s parameters when a few valuation updates are postponed. —Threshold for Update Error 훾푗of Component 퐶푗: It implies the maximum tolerable update

error in a component that guarantees the safety of the system.

<!-- page 19 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:19

—Update Error Γ′ of the Model: The total additive values of the update error in all components

of the model. —Threshold for Update Error Γ of the Model: Maximum tolerable error in the model. —Freshness Value 푓푗for Component 퐶푗: It shows the number of MAPE rounds that updating a

component is postponed. —Freshness Value F of the Model: It denotes the number of components in the model in which

their freshness value is not zero.

Note that only훾푗and Γ need to be adjusted at design time. However, the value for the thresholds is updated at runtime via the MAPE-K loop. Other discussed parameters are initialized autonomously, and updated by the software-controlled loop.

### 6.1 The Minor Approximation in Practice

The idea of the minor approximation is to distribute the overhead of the approximation tasks into a look-ahead horizon 퐻(a time slot including several rounds of MAPE). Therefore, we can eliminate the state-space explosion problem for verifying the autonomous system model at runtime, and the system could handle the verification with its limited resources by adjusting the look-ahead horizon in the model. We implement the minor approximation by a two-level scheduling algorithm. The first level is a priority assignment algorithm that is responsible for converting the changes and freshness values of each component into a quantitative number, illustrating the priority of that task denoted by 휚푖(the highest value determines the most prioritized task). The second level includes a scheduling algorithm that schedules the maximum feasible approximate/verification tasks based on the priority assignment values, fitting into the look-ahead horizon 퐻. On one hand, the minor approximation aims at feasibility of runtime approximation by reducing the frequency of updates and consequently, the frequency of running approximation tasks. On the other hand, it leverages the accuracy of verification results by prioritizing the most significant approximation tasks.

Each component is a sub-model of the MDP, and has states and transitions, in which each component is separately verified. Then the results are aggregated using a centralized algorithm [4]. In addition, as shown in Algorithm 1, the algorithm gets the configuration of the components as 퐶(푓,훾′,훾) and a task set corresponding to the components as 휏(푑,푒) where 푑and 푒denote the deadline and the execution time of tasks. The deadlines of the tasks are all sub-multiples of 퐻, and must be feasible within each MAPE loop period. It means in each period of the MAPE loop, we schedule verification tasks to meet the decision-making deadlines of the analyzing step. The deadlines and execution time of components are calculated empirically, according to the size of the components and the number of dynamic parameters within them. For all 휏푖∈휏, if the component experiences a change (meaning 훾′

푖≠0 표푟푓푖≠0), the priority value 휚푖is calculated based on the formula illustrated in lines 6–7. The algorithm utilizes the Hellinger distance criteria for prioritizing each approximation task. It grants higher priorities to the tasks that their change values 훾′

푖has the minimum distance to their threshold 훾푖. The freshness values 푓푖are multiplied to the distance’s inverse to increase the priority of older components. Then, the set of priority-assigned tasks L is sorted and sent back to the scheduling algorithm. The algorithm schedules the possible approximation tasks in 퐻. We have used the earliest deadline first (EDF) algorithm for scheduling the approximation tasks inspired by [20].

Each time, we add a new high-priority task from L to the feasibility test set 퐾and check whether adding the new task is feasible regarding the EDF feasibility algorithm [7]. If the outcome is positive, we add the task and look for more. In each step, the task’s execution time is added to 휁, and at the next step, the feasibility of adding a new task to the task set is firstly checked by the 휁constraint. The feasibility test algorithm determines which task set is feasible for scheduling regarding the

<!-- page 20 -->

3:20 M. Alidoost Nia et al.

Algorithm 1: A Two-Level Scheduling Algorithm for Prioritizing Approximation Tasks

```math
Input:휏(푑,푒),퐶(푓,훾′,훾)
Result: A subset of approximation tasks 퐾∈휏scheduled by EDF
Initialization;
for each 휏푖∈휏do
```

if (훾′

```math
푖≠0 표푟푓푖≠0) then
푑퐻(훾′
```

푖−√훾푖|;

푖,훾푖) = 1 √

훾′

## 2 | p

휚푖= 1 푑퐻(훾′

푖,훾푖) × 푓푖;

Priority_Assignment(휏푖, 휚푖); Append(L,휏푖); end end Quick_Sort(L, 휚,푑푒푐); for each 휏푖∈L do

if (휁+ 푒푖≤퐻) then

if Schedulability_Test(퐾,휏푖) then

Append(퐾,휏푖); 휁= 휁+ 푒푖; end end end return EDF(퐾);

deadline of the tasks and the size of the look-ahead horizon. Then, the approximation tasks are scheduled by EDF as 퐸퐷퐹(퐾) and sent to the approximation engine for execution.

We use soft real-time logic [62] to implement the adaptive approximation strategy. In real-time systems, the design space is categorized into two high-level approaches [54]. The first is hard real time, and the second is soft real time. In a hard real-time approach, missing a deadline has serious consequences, while in a soft real-time design, missing a deadline only leads to losing utility. The second approach is matched correctly to the logic of the proposed system in which missing a deadline may lead to the major approximation. In our proposed system, all safety properties of the autonomous system are guaranteed and separated from the scheduling algorithm, which implements the minor approximation. Furthermore, to assure the safety-critical aspects of the system, we perform change-/result-driven analysis (see Section 6.2). In the case of the rescue robot team, if a deadline is missed, the autonomous system only loses the utility of delivering the equipment fast.

6.2 Change- and Result-Driven Analysis We perform two types of analyses on the autonomous system. The first is the change-driven analysis that is concerned about the input changes. The second is the result-driven analysis that aims at executing a set of acceptance tests to assure the accuracy of the results. We start with the change-driven analysis that ensures the result of RQV does not exceed a predefined threshold. Applying this analysis, we need to investigate how Γ can be calculated. An approach to define Γ is to incrementally calculate the total 푑퐻(훾′

푖,훾푖) for all components where all 훾′

푖values are initially zero. Therefore, one can calculate the total threshold of changes as Γ = 1 √

## 2 Í훾푖. This analysis aims

<!-- page 21 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:21

Algorithm 2: Procedure for Applying the Result-Driven Analysis

Input: 푦′ = (푈퐴′,훾′), 푌= {푦1 . . .푦푛} initial 푦as the similarity set for (each 푦푖∈푌) do

푦′) ≤휀) then Append(푦, 푦푖); end end 푦푚푖푛=Supremum(푦); 푦푚푎푥=Infimum(푦);

if (푑퐻(훾′

푦푖,훾′

```math
if (푦푚푖푛≤푦′ ≤푦푚푎푥) then
```

return true; else

### 푈푎푣푔= (Í푚

### 푖=0 푈푦푖)/푚; Δ′ =

```math
|(푈퐴′)2 −(푈푎푣푔)2|/푈푎푣푔;
if (Δ′ ≤Δ) then
```

p

return true; end end Major_Approximation(); return false;

to avoid wrong decisions in autonomous systems in a situation where the number of changes is increased. Therefore, we choose a more conservative approach and define the global threshold Γ as the average case of all local thresholds. It means that if the parameters of all components are changed more than half of their allowed update thresholds, the system proactively predicts that the system’s accuracy may fall within the next few rounds of MAPE. Consequently, the change-driven analysis triggers the major approximation if the total value of changes Γ′ exceeds the threshold Γ that is calculated using (17):

### 푛 Õ

### Γ = 1

```math
훾푖.
(17)
```

## 2 √

2

푖=1

The result-driven analysis is another assurance technique that aims at controlling the output of RQV. According to Algorithm 2, we compare the result of the system 푦′ that contains total changes of the components 훾′ and total utility of the late-update model 푈퐴′, with a set of reference, values 푌. We analyze the result in two levels: the first is to compare the result and investigate whether it is in the accepted range, and the second is to compute the current deviation of measurement Δ′

and compare it to the threshold Δ (determined experimentally). The distance between the current value and each reference value is compared, and if the outcome shows that they are similar, we add the reference value to the similarity set 푦. Then, we come up with a custom range denoted by (푦푚푖푛,푦푚푎푥) and confirm the validity of the result if the result is in that range. Otherwise, we calculate the current rate of change (RoC) factor using formulas denoted in lines 13–14 and decide based on the value of Δ′. If the outcome satisfies the condition Δ′ ≤Δ, the result passes the test, and the system continues the minor approximation. If any of both conditions could not be satisfied (see lines 10 and 15), the system fails to accept the result, and consequently, the major

<!-- page 22 -->

3:22 M. Alidoost Nia et al.

approximation is invoked. Note that the construction of the dataset and related computations are done at design time as denoted in Figure 7.

6.3 Formal Properties Support Consider the notations and formulas defined through Definition 3.5 and Table 1. The system fully supports the state formulas of PCTL that are denoted in the second row of the table. As for the first example of what the system supports, the safety property 푃≥1[“푠푡표푝” ∧“푠푎푓푒”] is expressed that concerns about the transmission safety of equipment to the target position. The labels “푠푡표푝” and “푠푎푓푒” denote the target position and safety of the equipment, respectively. The third row of the table shows the supported template for the next operator. The sample property 푃≤0.05[푋“표푏푠푡푎푐푙푒”] indicates the probability of facing an obstacle in the next workflow step. In addition, the system supports the Bounded Until operator. To balance the application requirements and the complexity of model-checking, we decided to bind the steps to at most 50. It means that we do not support unbounded until in our proposed framework. As for another example, the property 푃≥0.95[“표푏푠푡푎푐푙푒” ∪≤3 “푟푢푛푛푖푛푔”] expresses the minimum probability for removing the obstacle in a maximum of three workflow steps. The labels “표푏푠푡푎푐푙푒” and “푟푢푛푛푖푛푔” denote facing with obstacle and running state of the leader robot, respectively. Note that bounded until is used in system model presentation through Listing A5 (see Appendix A.3) by the “퐹푖푛푎푙푙푦” operator because (bounded) until expressions technically can be converted to “퐹푖푛푎푙푙푦” expressions under PCTL constraints, e.g., 퐹≤푛휑= 푡푟푢푒∪≤푛휑[5].

To reduce the complexity of the framework, we decided to capture distance in our model rather than explicit time. Capturing the sequential order of the actions taken by the robot team is adequate for concluding the arguments of the paper. However, we have considered explicit time in the execution order of the approximation tasks. As time is a critical factor in our feasibility test (please see Sections 6.1 and 6.2), we elaborated temporal analysis in the design step of the framework and captured sequential order and distance-based behavior of the robots in our models.

7 Experimental Results In this section, we discuss the experimental results. All experiments are conducted on the case study of the rescue robot team. We use Prism 4.5 as the verification engine of the framework [38]. The codes of our framework are developed by the JAVA programming language available in [47]. All experiments are executed on a PC using a CPU with 3.10 GHz speed and 4GB RAM. We have designed a set of experiments to discuss different aspects of the research, including the viability of minor approximation in autonomous systems, error-bound analysis, safety assessment, and performance evaluation. The experimental results have been reported after 100 successful runs, and the results are reported as statistically valid averages.

### 7.1 The Result of the Adaptive Approximation Strategy

Before starting a discussion around the experiments, we give an overview of how the computations are done. In our framework, the most expensive computations are done offline. We refer to constructing the components (SCCs), determining parametric components, calculating the threshold of update errors, the total threshold for update errors, upper/lower bounds for acceptance test, and applying 휀-approximate technique for the first time. These parts are no longer considered as computational overhead. At runtime, only a few updated components are scheduled for approximation/verification by the minor approximation, and an acceptance test is executed at the end of each round of MAPE. The experiments are designed and conducted according to the assumptions mentioned above.

<!-- page 23 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:23

**Table 2. Comparing State Space and Average Approximation/Verification Time of the Autonomous System**

Model under Different Scenarios

Distance (m) Concrete Model Incremental Approximation Adaptive Approximation

Space Average time (s) Space Average time (s) Space Average time (s)

10 250K 0.35 77K 0.08 77K 0.08 20 1M 0.72 220K 0.12 220K 0.09 50 6.6M 1.55 588K 0.41 588K 0.35 100 27M 2.8 3.15M 1.32 3.15M 0.78 200 107M 6.1 9.2M 1.81 9.2M 0.96 500 673M 17.8 21M 2.35 21M 1.22 1,000 2.7B 195 98M 3.66 98M 1.78

Table 2 presents the state-space and verification time of the proposed method applied to the rescue robot team model. We can model the team at different distances between 10 and 1,000 meters. A concrete model refers to a precise model without applying approximation. Space shows the number of states, and time denotes the total verification time. Incremental approximation refers to the technique in which we divide the model into components and independently approximate/verify each component by only major approximation. As we can see, the state-space of the model after approximation is reduced drastically. This technique only re-approximates/re-verifies the components that are subjected to change. The adaptive approximation technique (our proposed framework) includes the same state-space as for incremental approximation; however, it takes less approximation/verification time than the incremental approximation technique because it postpones unnecessary changes. The average time is calculated by the results of 100 repeated experiments for 20 first rounds of MAPE.

By looking at Table 2, we can see a range of 10–1,000 meters simulations of the environment model. As this range increases, the look-ahead horizon increases as well, and the parameters of the model may become uncertain for long distances because predicting and monitoring a long distance is very difficult in practice. On the other hand, stretching the distance affects the size of the concrete model, ranging from 250K to 2.7B states. For example, even constructing the concrete model on a dedicated computer system for 2.7B states has many difficulties, as we did. Considering an autonomous system, the resource limitations may cause state-space explosion even for a 100M states model. The incremental approximation approach initially alleviates the problem by reducing the states of the model. Then, our proposed adaptive approximation strategy makes it feasible for larger models to be used according to the limitations of the autonomous systems at runtime. However, choosing the right distance depends on different design variables like the capacity of the autonomous system, the deadlines for computing the results, the dynamicity of the environment, and how much the look-ahead horizon is stretched.

As the capacity of the autonomous system is limited, in each round of MAPE, only a certain number of components are prioritized to schedule. Figure 8 denotes the number of affected components in each round of MAPE and indicates which number of those components are updated. When a component is updated with new parameter(s), it needs re-approximation/re-verification. According to the figure, the number of affected components is more than the processing capacity of the autonomous system, and this is why the adaptive approximation strategy works for runtime approximation/verification of such resource-limited systems.

We have simulated the dynamicity of the environment using a RoC factor. It indicates how much the changes are frequent through the environment and how many times the autonomous

<!-- page 24 -->

3:24 M. Alidoost Nia et al.

**Fig. 8. The number of affected components by the changes in 20 rounds of MAPE.**

system should expect to be affected by the changes. For example, if the RoC of the environment is calculated to be 10% (or 0.1), the autonomous system expects to encounter 1 change out of the next 10 workflows. We have investigated the resiliency of the proposed technique against different rates of changes coming from the environment.

Figures 9 and 10 denote the size of the change in parameters of the five most high-prioritized components of the model that are simulated by RoC 10% and 20%, respectively. The experiment is executed for 20 rounds of MAPE under each RoC. The update error for components (훾′

푗) does not exceed from the corresponding thresholds (훾푗). Therefore, the system continues its work under the minor approximation. Considering the set of thresholds for these five components as 0.3, 0.26, 0.35, 0.3, and 0.22, we can see that in a few rounds of MAPE in Figure 10, the update error is near the threshold, e.g., in round 5, 훾′

4 = 0.25 is near 훾4 = 0.3, and in round 7, 훾′ 2 = 0.22 is near 훾2 = 0.26. However, the threshold of errors is not exceeded, and according to Theorem 1, the accuracy of synthesized actions is guaranteed.

Figure 11 denotes the changes in each of the five components under RoC = 30%. As we can see, the number of changes in each component is increased compared to RoC = 20%. In rounds 10 and 15, we can see two black slots that belong to components 5 and 2, respectively. These indicate that the update errors in those components exceed from the predefined thresholds (in round 10, 훾′

5 = 0.24 > 훾5 = 0.22, and in round 15, 훾′ 2 = 0.28 > 훾5 = 0.26). According to Theorem 1, the minor approximation does not guarantee the accuracy of synthesized actions anymore, and the leader robot triggers an emergency stop, and the major approximation is executed. As for the examination, once we continued with minor approximation, interestingly, the accuracy of the synthesized actions in round 15 was similar to the incremental approximation technique. However, we encountered an error in the decision by executing the minor approximation in round 10. The total update error Γ′ is periodically calculated in all rounds of MAPE. The results indicate that the system does not exceed the threshold Γ = 2.5 in any 20 first rounds of MAPE. Therefore, Γ′ did not affect the minor approximation.

<!-- page 25 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:25

**Fig. 9. Order of changes in five sample components of the model affected by RoC = 0.1 in 20 rounds of MAPE.**

**Fig. 10. Order of changes in five sample components of the model affected by RoC = 0.2 in 20 rounds of MAPE.**

7.2 Error Analysis According to Theorem 1 and its corollaries, the minor approximation guarantees the accuracy of synthesized actions. Nevertheless, it does not guarantee the accuracy of the total utility of the system. In this experiment with RoC = 10%, we calculate the total utility resulting from the incremental approximation that uses the major approximation all time (푈퐴), the adaptive approximation strategy (푈퐴′), and tolerable error of the system (푈+) that Figure 12 denotes. When the total utility of the approximation strategy is less than the tolerable error, the output of decisions may contain an error. According to the figure, the amounts of 푈퐴and 푈퐴′ are greater than 푈+. Therefore, the decision-making process of the system is accurate and is not affected by approximation error.

<!-- page 26 -->

3:26 M. Alidoost Nia et al.

**Fig. 11. Order of changes in five sample components of the model affected by RoC = 0.3 in 20 rounds of MAPE.**

**Fig. 12. Comparing the verification results of the adaptive approximation strategy (푈퐴′), incremental approximation (푈퐴), and tolerable error (푈+).**

Considering Algorithm 2, we calculate upper/lower bounds of accepted values offline as 푦푚푎푥= 25.6 and 푦푚푖푛= 10.25 according to the history of previous executions. If the value is out of the accepted range, the system calls the major approximation strategy. As denoted by Figure 13, two dashed lines correspond to 푦푚푎푥and 푦푚푖푛. The calculated values between these two are accepted, and the outer ones are rejected. In the 15th round of MAPE, the system detects a deviation from the accepted values in the results associated with RoC = 20%. We can see a similar deviation in the 18th round of RoC = 30%. The system moves these two results for further analysis by evaluating

<!-- page 27 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:27

**Fig. 13. The results of acceptance test in 20 rounds of MAPE under different values of RoC.**

the deviation of measurement Δ′. In the second round of analysis, the result associated with RoC = 20% is accepted, and the result associated with RoC = 30% fails to pass the test. Therefore, the only rejected result in the acceptance test is the point related to the 18th round of MAPE in RoC = 30%.

To demonstrate the validity and generality of our experiments under different RoC values, we conducted an ANOVA [18]. The purpose of this analysis is to validate the significance of our experimental results statistically. ANOVA allows us to compare multiple groups to determine if there are any statistically significant differences between them. In our study, we used ANOVA to compare the performance metrics under different RoC values. As shown in Table 3, the experimental results are significant at p < 0.01, indicating a high level of confidence in the findings. A p-value of less than 0.01 is strong evidence against the null hypothesis, suggesting that the observed differences are statistically significant. In Table 3, the columns represent the data at different RoC values. The table includes the following metrics:

—푁: Number of data points. —Í푋: Sum of the values. —Í푋2: Sum of the squares of the values. —Mean: Average value. —SS: Sum of squares. —df: Degrees of freedom. —MS: Mean sum of squares.

After obtaining a p-value below 0.01, we confidently reject the null hypothesis, confirming the significance of our results. The specifics of our analysis can be found in Table 3. The theoretical framework outlined in Section 4 further strengthens the validity of our research methodology, which is consistent with the statistical validation we have explored.

### 7.3 Safety Assessment

We verify the autonomous system model against two safety properties denoted in Listing A5 (see Appendix A.3). To assess the safety of the results, we first define true-negative (TN), true-positive

<!-- page 28 -->

3:28 M. Alidoost Nia et al.

**Table 3. ANOVA Test for Our Experimental Results under Different RoC Values**

Parameters RoC = 10% RoC = 20% RoC = 30% Total

푁 20 20 20 60 Í푋 353.49 391.84 442.2 1,187.53 푀푒푎푛 17.6745 19.592 22.11 19.792 Í푋2 6,322.9075 7,898.163 916.2646 24,137.3351 Standard deviation 1.9888 3.4123 2.7069 3.2769

Source SS df MS Test Result

Between results 197.9386 2 98.9693 F = 12.95039 Within results 435.6048 57 7.6422 Total 633.5434 59 푝−푣푎푙푢푒= 0.000023

**Table 4. Defining the Types of Results in the Autonomous System (the Rescue Robot Team)**

Type of Property Type of results Description

Emergency stop TN “no obstacle” is correctly identified. TP “obstacle” is correctly identified. FN “no obstacle” is incorrectly identified. FP “obstacle” is incorrectly identified.

Reduce speed TN “no partial obstacle” is correctly identified. TP “partial obstacle” is correctly identified. FN “no partial obstacle” is incorrectly identified. FP “partial obstacle” is incorrectly identified.

(TP), false-negative (FN), and false-positive (FP) results, shown in Table 4. FN results endanger the safety of the autonomous system because they happen when “no obstacle” is incorrectly identified. In the case of the rescue robot team, they may lead to massive damage to the equipment, and the mission may fail.

To ensure the safety of the autonomous system, we must care about the true-positive rate (TPR) or Sensitivity of the result [57]. We define Sensitivity by (18) that measures the ratio of positive results that are correctly identified:

```math
(푆푒푛푠푖푡푖푣푖푡푦) 푇푃푅=
푇푃
푇푃+ 퐹푁.
(18)
```

We define the true-negative rate (TNR) or Specificity by (19) that measures the ratio of negative results that are correctly identified:

```math
(푆푝푒푐푖푓푖푐푖푡푦) 푇푁푅=
푇푁
푇푁+ 퐹푃.
(19)
```

Finally, the total accuracy of the results in the proposed framework is calculated using (20):

```math
(퐴푐푐푢푟푎푐푦) 퐴퐶퐶=
푇푃+푇푁
푇푁+푇푃+ 퐹푃+ 퐹푁.
(20)
```

As depicted in Figures 14 and 15, the results of 10 experiments from 20 rounds of MAPE are presented. Investigating the verification results for two safety properties, the outcomes do not

<!-- page 29 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:29

**Fig. 14. The safety assurance by emergency stop against obstacles that include no FN error.**

**Fig. 15. The safety assurance by reducing speed against partial obstacles that include no FN error.**

include any FN error. According to Table 4, the results do not contain any item in which “no obstacle” or “no partial obstacle” is incorrectly identified, and it assures the safety of the system.

On running the experiments under 100 different situations of the environment, the system’s Sensitivity for both properties is calculated at 100%. This affirms the safety assurance of the autonomous system under the minor approximation approach, where in both theory (see Section 4) and practice, we demonstrated that the proposed framework is 100% resistant against type I (FN) errors. In addition, the Specificity and Accuracy of the system are calculated in the ranges of 96.7–98.3% and 97–98.5%, respectively. We have tested the proposed experimental results by the ANOVA statistical analysis approaches, and the test revealed the significance of the result data at p < 0.01, which reflects the reliability of the data analyzed in our experiments.

The system’s primary goal is to verify the system model against safety properties efficiently. In our theoretical investigations, we could show the framework’s validity regarding the system’s functional safety. Theorem 1 proves that the thresholds for changes concretely prevent the error in synthesized actions of the verification process. This means that the system can tolerate an error

<!-- page 30 -->

3:30 M. Alidoost Nia et al.

as much as these thresholds to keep the verification results valid. We engineer the framework on this theoretical basis that our adaptive dynamic approximation strategy does not allow the system to exceed the fixed thresholds. Besides the efficiency it brings to the entire verification process by allowing delays in updates, the strategy guarantees the accuracy of decisions regarding the safety properties. According to the experimental results, the framework follows the same behavior in practice. We can extend the framework to any applications with limited resources that need a formal guarantee for the safety properties of the system. As the tolerated error of the system (error bound) is deterministic in our approach, one can decide if the total error of the system is acceptable for their application or not.

Regarding the general safety properties like live-lock/deadlock [60], we have tested our model using the PRISM model-checker. We detected partial deadlock issues eliminated in the early steps of modeling and design. In addition, to check whether the model suffers from divergence problems [23], we adjusted the size of workflow steps in our models and the corresponding PCTL formulas. As we did not observe any infinite (or large) values for long distances in the model, it is not likely that our model is affected by the divergence problem. However, if there were any divergence problems, we might have faced issues regarding the computation of the accumulated utility of the system in different situations. Therefore, our proposed framework is also validated against the general safety properties.

Our top priority in this research is the safety of autonomous systems. We ensure this safety by using model verification at runtime to adapt the system to environmental changes. Our proposed framework guarantees this safety. Without our framework, adapting at runtime becomes challenging and potentially endangers the safety of the system when encountering environmental hazards such as obstacles.

7.4 Performance Evaluation The efficiency of the proposed system is based on offline processes, including the partitioning algorithm, calculation of thresholds, and the first-round approximation of the components. Only a few tasks are executed periodically at runtime. We compare the performance of the adaptive approximation strategy with incremental approximation in terms of execution time in the first 20 rounds of MAPE. As we can see in Figure 16, after the first round of approximation, the system is stabilized with uniform execution time because the system is enforced to use a set of limited resources by the adaptive strategy. The experiment is conducted by RoC = 10%, and the accuracy of synthesized actions for delayed-update approximation is similar to the incremental approximation technique; however, the adaptive approximation strategy promises better performance.

The system executes three major algorithms to implement the adaptive approximation strategy. The first is the two-level scheduling algorithm that prioritizes and schedules the approximation/verification tasks at runtime (see Algorithm 1). The complexity of the algorithm is 푂(m2). However, m is an integer number lower than 20, indicating the system’s capacity for executing the prioritized tasks. Therefore, the overhead of computations is negligible. The second algorithm is the result-driven analysis (see Algorithm 2). The computational overhead of the algorithm is associated with the similarity set processed offline, and the acceptance criteria are once checked in each round. Therefore, the complexity of the algorithm is linear and negligible at runtime. The third part of the algorithm is about applying approximation/verification to each component. According to the previous research [4], the complexity of applying incremental approximation/verification is 푂(n푙표푔(n)) where n is the maximum number of states among all components. Then, the complexity of executing the adaptive approximation strategy is 푂(n푙표푔(n)) in each round of MAPE. Note that all these three algorithms only affect the analysis step of the MAPE loop, and their computational overhead on the other parts of the controller is negligible.

<!-- page 31 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:31

**Fig. 16. Comparing the approximation time of the adaptive approximation strategy (delayed update) and the incremental approximation.**

7.5 Limitations of the Research Despite the promising results demonstrated in our study, several limitations require further consideration. Firstly, our investigation is confined to a single case study involving a team of rescue robots. While this case study effectively showcased the robustness and safety of our adaptive approximation strategy, it only guarantees the same level of performance across other safety-critical applications. Extending our framework to diverse domains, such as unmanned aerial vehicles and autonomous cars, requires comprehensive experimentation and validation. Each application has unique operational challenges and safety requirements that might impact the effectiveness and reliability of our proposed solution. Hence, further studies are essential to generalize the applicability of our strategy across various autonomous systems.

Secondly, our proposed framework currently only supports a partial range of PCTL operators. Specifically, it lacks support for the Until operator, which is crucial for expressing certain temporal properties. Instead, we only support the Bounded Until operator, which is limited to an examination of 50 steps. This constraint restricts the expressiveness of the safety and optimization properties that can be verified using our framework. Expanding support to include the full spectrum of PCTL operators would enhance the versatility and applicability of our solution, allowing for more comprehensive model verification in dynamic environments.

Moreover, the state-space explosion issue addressed in our case study may vary significantly in other applications. The computational demands and capacity required for real-time applications could differ based on the specific characteristics and complexity of the state-space in those contexts. This variability means that the computational overheads and efficiency may not directly translate to other scenarios. Evaluations on the computational capacity and real-time performance need to be conducted in diverse settings better to understand the scalability and limitations of our approach. Addressing these limitations through further research will be essential to fully realizing the potential of our strategy.

8 Related Work In this section, we give an overview on the related work, and then, we compare the most similar ones to our proposed framework.

<!-- page 32 -->

3:32 M. Alidoost Nia et al.

8.1 Review of the Related Work In the context of adaptation strategies, Filieri et al. proposed a set of control strategies for selfadaptive systems that aimed at applying the control theory to the design process of self-adaptive systems [27]. However, this research is not purely software-controlled, the research has similarities in terms of strategy determination for a self-adaptive system. Van Der Donckt et al. tackled the problem of time-consuming analysis in self-adaptive systems that have large adaptation space [58]. They proposed a deep learning-based approach that fills the existing gap between the threshold and optimization goals, namely DLASeR. Cámara et al. targeted the challenge of runtime adaptation of mobile service robots and their underlying software architecture [16]. They elaborated a new approach that considers both aspects under uncertainty and improves the quality of adaptation decisions. Calinescu et al. conducted a comprehensive investigation on various aspects of uncertainty in self-adaptive systems [13]. The results revealed the role of engineering in self-adaptive systems to address unanticipated changes. The research outcome recommends the use of confidence intervals and probabilities for handling uncertainties. Maia et al. investigated defiant components that cannot meet local and global requirements through adaptation [44]. To address the issue of defiant components, they have proposed cautious adaptation that concerns supporting the changes through the behavior of the defiant components.

In terms of approximation techniques, Lohar et al. presented a probabilistic approach for analyzing the approximation error of the system [42]. They proposed a new metric for computation of refined error-bound that is sound with some probability. Abate et al. conducted a comprehensive survey on state reduction techniques and investigated their advantages/disadvantages through theoretical reasoning [2]. Then, they proposed a framework based on aggregation and truncation techniques with a certain upper bound of errors. Polymenakos et al. proposed safety guarantees for analyzing Gaussian processes [52]. They derived a probability upper bound for iterative predictions bounded by a given threshold 휀> 0. Alidoost Nia et al. proposed a theoretically supported faulttolerant technique that guarantees the estimation of missed parameters of the system caused by monitoring faults [3]. The system used the previous behavior of the environment to estimate the current valuation of the missed probabilistic variables. The upper bound for estimation errors is guaranteed and employed in safety-critical applications. Alidoost Nia et al. proposed an incremental approximation technique that uses 휀-bisimulation for reducing the state-space of the model [4]. Each component is approximated separately, and the results of the previous approximations are used in the following rounds. The upper bound for errors was formally investigated and determined as {휀× 푟× 푘} in the worst-case scenario. In a similar research study, Fang et al. proposed a fast parametric model-checking (fPMC) technique based on a fragmentation technique [25]. They partitioned the PMDP into a set of independent fragments so that the given property is independently analyzed in each fragment. Lavaei et al. elaborated a compositional technique for abstracting the interconnected discrete-time stochastic control systems [40]. They used the stochastic simulation function for quantifying the distance between the subsystems. 휀-approximate bisimulation is another technique used to approximate Markov chains a threshold for probability of the transitions [8]. This technique empowers the classic bisimulation technique to highly reduce the size of the model, where the approximation error-bound can be calculated theoretically.

Efficient verification techniques are another category of related work that are comparable to our research outcome. The first is the incremental verification technique [39]. In this approach, the model is divided into a set of components, and each component is verified separately. Then, the results are aggregated using an iterative algorithm. Proactive latency-aware stochastic dynamic programming technique (PLA-SDP) is another research that uses the power of stochastic dynamic programming to eliminate the runtime overhead by constructing most of the

<!-- page 33 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:33

model offline [46]. Another research in this context is Evo-Checker, which is designed for the formal verification and optimization of systems modeled as PMDPs [29]. It combines evolutionary algorithms with model checking to optimize the parameter space of PMDPs, ensuring that the system meets specified probabilistic properties.

In the context of safety-critical applications, our work is comparable to a research work developed by Li et al. [41]. They investigated the applications of cyber-physical space systems and proposed a new approach for validation by separation of concerns in the design step and early validation of the system via statistical model-checking. Luckcuck et al. surveyed formal verification techniques for autonomous robotics [43]. They addressed the formal challenges in both the verification and specification of robot systems and were concerned about autonomous decision-making for complex safety-critical robotics. In another research, Alidoost Nia et al. [3] proposed a resilient verification technique that forecasts the valuation of the parameters if a few are missed in some rounds of MAPE due to transient faults. This technique matches safety-critical applications that work in an unreliable environment. In a similar research study, a new approach is proposed called data-efficient verification [51]. In this approach, Bayesian Inference is employed to verify a parametric model using limited data. Another research that strengthens the reliability of verification results is FACT [12], which is a probabilistic model checker that computes confidence intervals for properties of Markov chains with unknown transition probabilities based on the observed data. This research extends quantitative verification to domains where unknown estimation errors are unacceptable.

### 8.2 Comparison

At the end of this section, we compare our proposed framework and achievements with related work regarding scalability, methodology, and the expected results. As shown in Table 5, we compare our proposed framework with a set of related work including the incremental approximation technique [4], fPMC [25], the 휖-approximate bisimulation technique [8], the incremental verification technique [39], a PLA-SDP [46], data-efficient verification technique [51], a resilient verification framework [3], a machine learning-based evolutionary algorithm for model-checking (EvoChecker) [29], and the FACT verification framework [12]. The incremental approximation framework is an efficient solution to model-based verification at runtime, and it tries to reuse the previously verified components of the model as much as possible. fPMC is a verification framework for parametric Markov chains that divides the model into fragments. However, we do not observe any application of it for runtime model-checking. 휖-approximate bisimulation is a technique for model reduction based on the probabilistic behavior of the model and merging similar states into one state. It has a static approach; however, the reduced approximate model has particular applications in dynamic verification techniques like our proposed framework. PLA-SDP is a verification technique that is aware of the resource and latency of operations at runtime and tries to adaptively adjust the system’s behavior at runtime due to changes. Data efficient verification is another technique concerned with verifying incomplete models at runtime that facilitates the verification process when a few parameters of the model are unknown at runtime. The resilient verification technique follows the same approach: the system uses a dynamic model that captures changes at runtime and resists the runtime monitoring errors when the framework cannot update a few model parameters due to transient faults. EvoChecker is a machine learning technique for efficient verification of Markov chain models. FACT is a verification framework that uses heuristic algorithms to verify the models with confidence intervals.

According to Table 5, the first evaluation metric is computational complexity, which concerns the computational resources, a proposed algorithm/framework consumed in operation. In terms of complexity, only those designed for runtime deployment have linear complexity. More precisely, our proposed framework reduces the overhead of computations to 푂(푛푙표푔푛) order, which is comparable

<!-- page 34 -->

3:34 M. Alidoost Nia et al.

**Table 5. Comparing the Current Research with Related Work**

LargeScale Model Support

Distr. System Support

Frameworks and Techniques

Resource Aware

Complexity

Verification Type

Approximation Support Efficiency Model Support

Theoretical Error Bound

Update delay and model reduction

Our proposed framework

Polynomial Dynamic Dynamic Approximation

Parametric MDP 푟× Í푛

푗=1 훾푗 Yes Yes Yes

Incremental approximation [4]

Model partitioning and reduction

Polynomial Dynamic Incremental approximation

### PMDP |휀푟( 푘+1

## 2 )| Yes No Yes

fPMC [25] Exp. Static Model fragmentation

Model Partitioning

Parametric Markov Chain N/A No No No

휖-approximate [8] 푛7 Static Bisimulation Model reduction Markov chain 푑푇푉 Yes No No

Incremental verification [39]

Polynomial Dynamic N/A Model partitioning MDP N/A No No Yes

PLA-SDP [46] Exp. Dynamic N/A Dynamic programming MDP N/A Yes Yes No

Data efficient verification [51]

N/A Dynamic Bayesian inference

Data efficiency

Parametric MDP N/A No No No

Resilient verification [3] Linear Dynamic Parameter estimation

Verification delay PMDP 푈+ (푘) Yes No Yes

Inverted generational distance (퐼퐼퐺퐷)

EvoChecker [29] Linear Dynamic N/A Machine learning approach

Markov chains, MDP, PA, PTA

No No Yes

Confidence interval optimization

FACT [12] N/A Static Heuristic algorithm

Parametric markov chain N/A No No Yes

to incremental approximation and verification frameworks. The second metric is about verification type, divided into dynamic and static types. Dynamic refers to the frameworks/techniques that accept structural changes at runtime, capture the changes into their system model, and verify the updated model. On the other hand, the static techniques support only fixed model verification at runtime, as seen in the related frameworks and techniques. The third evaluation metric is formal approximation support, which is crucial for model-based RV. Formal approximation is a technique to deal with state-space explosion. Our proposed framework benefits from two levels of approximation: the first is the incremental approximation technique that aims at reducing the model using probabilistic similarities, and the second is the dynamic approximation technique, which tries to delay updates and reuses the previously verified components of the model as much as possible.

Model-based verification techniques are resource-consuming and require efficient approaches. The fourth metric is about the efficiency of the proposed approach. As discussed, our framework tries to postpone updating the model alongside partitioning the model into SCCs. Similarly, the incremental approximation, fPMC, 휖-approximate bisimulation, and incremental verification techniques use the partitioning idea. However, delaying updates at runtime is only our innovation compared to other related work.

Regarding model support, our proposed framework focuses on the most general and challenging Markov model, namely, PMDP, which fits the requirements of a dynamic, model-based verification framework. As one of the most significant metrics, our proposed framework is supported by rigorous theoretical error bound, which needs to be included in most related work. Furthermore, our proposed framework supports distributed/decentralized verification. One of the unique specifications of our proposed framework is that the framework is resource-aware. This means that the entire verification method can be adjusted based on the resource constraints and deadlines of the tasks.

<!-- page 35 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:35

It helps the system to cope with the state-space explosion problem dynamically. In addition, the proposed framework can be deployed for large-scale systems using two levels of approximations throughout its operations.

## 9 Conclusion and Future Work

In this article, we tackle the problem of autonomous decision-making in safety-critical autonomous systems. Due to resource constraints, employing a model-driven approach is challenging, especially at runtime. Therefore, applying an approximation technique is necessary to make the model decidable. We divide the model into a set of components so that only the updated components of the model need re-approximation/re-verification at runtime. We propose a dynamic two-levels adaptive strategy that delays unnecessary updates. The system performs updates only to the most significant components that impact the accuracy of the decisions. The minor approximation prioritizes the approximation tasks according to the system’s capacity and periodically checks the results’ accuracy. If any deviation is obtained, the system triggers the major approximation. It enforces an emergency stop for sensitive functionalities, updates/approximates all components, and triggers minor approximations again. We propose a set of theoretical supports and establish a logical connection between the experimental results and theoretical foundations. The results confirm that the adaptive approximation strategy guarantees the autonomous systems’ safety requirements. We investigate the sensitivity and accuracy of the proposed framework in a case study of a rescue robot team. The experiments show that the proposed system is resistant to 100% against safety-critical errors, and the accuracy of decisions is evaluated above 97% overall.

As for future work, we will investigate the best approximation strategy by applying a reinforcement learning algorithm. The formal specification that the system is verified against is an optimization policy. We will design an agent for learning the best strategy by maximizing the total utility. The autonomous system will be equipped to decide proactively which approximation strategy is the best according to the environment and the previous knowledge of the system.

## References

[1] Alessandro Abate. 2013. Approximation metrics based on probabilistic bisimulations for general state-space Markov processes: A survey. Electronic Notes in Theoretical Computer Science 297 (2013), 3–25. DOI: https://doi.org/10.1016/j. entcs.2013.12.002

[2] Alessandro Abate, Roman Andriushchenko, Milan Češka, and Marta Kwiatkowska. 2021. Adaptive formal approxima- tions of Markov chains. Performance Evaluation 148 (2021), 102207. DOI: https://doi.org/10.1016/j.peva.2021.102207

[3] Mehran Alidoost Nia, Mehdi Kargahi, and Alessandro Abate. 2021. Resilient monitoring in self-adaptive systems through behavioral parameter estimation. Journal of Systems Architecture 118 (2021), 102177. DOI: https://doi.org/10. 1016/j.sysarc.2021.102177

[4] Mehran Alidoost Nia, Mehdi Kargahi, and Fathiyeh Faghih. 2020. Probabilistic approximation of runtime quantitative verification in self-adaptive systems. Microprocessors and Microsystems 72 (2020), 102943. DOI: https://doi.org/10. 1016/j.micpro.2019.102943

[5] Christel Baier and Joost-Pieter Katoen. 2008. Principles of Model Checking. MIT press.

[6] Matthias Becker, Markus Luckey, and Steffen Becker. 2012. Model-driven performance engineering of self-adaptive systems: A survey. In Proceedings of the 8th International ACM SIGSOFT Conference on Quality of Software Architectures (QoSA ’12). ACM, New York, NY, 117–122. DOI: https://doi.org/10.1145/2304696.2304716

[7] Marko Bertogna and Sanjoy Baruah. 2011. Tests for global EDF schedulability analysis. Journal of Systems Architecture 57, 5 (2011), 487–497. DOI: https://doi.org/10.1016/j.sysarc.2010.09.004

[8] Gaoang Bian and Alessandro Abate. 2017. On the relationship between bisimulation and trace equivalence in an approximate probabilistic context. In Proceedings of 20th International Conference on Foundations of Software Science and Computation Structures. Javier Esparza and Andrzej S. Murawski (Eds.), Springer, Berlin, 321–337.

[9] Stanislav Böhm, Stefan Göller, and Petr Jančar. 2014. Bisimulation equivalence and regularity for real-time one-counter automata. Journal of Computer and System Sciences 80, 4 (June 2014), 720–743. DOI: https://doi.org/10.1016/j.jcss. 2013.11.003

<!-- page 36 -->

3:36 M. Alidoost Nia et al.

[10] Yuhang Cai and Lek-Heng Lim. 2022. Distances between probability distributions of different dimensions. IEEE Transactions on Information Theory 68, 6 (2022), 4020–4031. DOI: https://doi.org/10.1109/TIT.2022.3148923

[11] Radu Calinescu, Simos Gerasimou, Kenneth Johnson, and Colin Paterson. 2017. Using runtime quantitative verification to provide assurance evidence for self-adaptive software. In Software Engineering for Self-Adaptive Systems III. Assurances. Rogério de Lemos, David Garlan, Carlo Ghezzi, and Holger Giese (Eds.), Springer International Publishing, Cham, 223–248.

[12] Radu Calinescu, Kenneth Johnson, and Colin Paterson. 2016. FACT: A probabilistic model checker for formal verifica- tion with confidence intervals. In Proceedings of the 22nd International Conference on Tools and Algorithms for the Construction and Analysis of Systems, Vol. 9636. Springer-Verlag, Berlin, 540–546. DOI: https://doi.org/10.1007/978-3662-49674-9_32

[13] Radu Calinescu, Raffaela Mirandola, Diego Perez-Palacin, and Danny Weyns. 2020. Understanding uncertainty in self- adaptive systems. In Proceedings of the 2020 IEEE International Conference on Autonomic Computing and Self-Organizing Systems (ACSOS), 242–251. DOI: https://doi.org/10.1109/ACSOS49614.2020.00047

[14] Radu Calinescu, Colin Paterson, and Kenneth Johnson. 2021. Efficient parametric model checking using domain knowledge. IEEE Transactions on Software Engineering 47, 6 (2021), 1114–1133. DOI: https://doi.org/10.1109/TSE.2019. 2912958

[15] Radu Calinescu, Danny Weyns, Simos Gerasimou, Muhammad Usman Iftikhar, Ibrahim Habli, and Tim Kelly. 2018. En- gineering trustworthy self-adaptive software with dynamic assurance cases. IEEE Transactions on Software Engineering 44, 11 (2018), 1039–1069. DOI: https://doi.org/10.1109/TSE.2017.2738640

[16] Javier Cámara, Bradley Schmerl, and David Garlan. 2020. Software architecture and task plan co-adaptation for mobile service robots. In Proceedings of the IEEE/ACM 15th International Symposium on Software Engineering for Adaptive and Self-Managing Systems (SEAMS ’20). ACM, New York, NY, 125–136. DOI: https://doi.org/10.1145/3387939.3391591

[17] Sung-Hyuk Cha. 2007. Comprehensive survey on distance/similarity measures between probability density functions. International Journal of Mathematical Models and Methods in Applied Sciences 1, 4 (2007), 300–307.

[18] Leslie Chandrakantha. 2014. Learning ANOVA concepts using simulation. In Proceedings of the 2014 Zone 1 Conference of the American Society for Engineering Education, 1–5. DOI: https://doi.org/10.1109/ASEEZone1.2014.6820644

[19] Frank Ciesinski and Marcus Größer. 2004. On Probabilistic Computation Tree Logic. Springer, Berlin, 147–188. DOI: https://doi.org/10.1007/978-3-540-24611-4_5

[20] Robert I. Davis, Liliana Cucu-Grosjean, Marko Bertogna, and Alan Burns. 2016. A review of priority assignment in real-time systems. Journal of Systems Architecture 65 (2016), 64–82. DOI: https://doi.org/10.1016/j.sysarc.2016.04.002

[21] Dionisio de Niz, Bjorn Andersson, and Gabriel Moreno. 2018. Safety enforcement for the verification of autonomous systems. In Proceedings of Autonomous Systems: Sensors, Vehicles, Security, and the Internet of Everything, Vol. 10643. Michael C. Dudzik and Jennifer C. Ricklin (Eds.), International Society for Optics and Photonics, SPIE, 1064303. DOI: https://doi.org/10.1117/12.2307575

[22] Christian Dehnert, Sebastian Junges, Joost-Pieter Katoen, and Matthias Volk. 2017. A storm is coming: A modern probabilistic model checker. In Computer Aided Verification, Rupak Majumdar and Viktor Kunčak (Eds.), Springer International Publishing, Cham, 592–600.

[23] Alexandros Evangelidis and David Parker. 2019. Quantitative verification of numerical stability for Kalman filters. In Formal Methods—The Next 30 Years, Maurice H. ter Beek, Annabelle McIver, and José N. Oliveira (Eds.), Springer International Publishing, Cham, 425–441.

[24] Yliès Falcone, Srđan Krstić, Giles Reger, and Dmitriy Traytel. 2021. A taxonomy for classifying runtime verification tools. International Journal on Software Tools and Technology Transfer 23, 2 (April 2021), 255–284. DOI: https://doi.org/ 10.1007/s10009-021-00609-z

[25] Xinwei Fang, Radu Calinescu, Simos Gerasimou, and Faisal Alhwikem. 2021. Fast parametric model checking through model fragmentation. In Proceedings of the 43rd International Conference on Software Engineering (ICSE ’21). IEEE Press, 835–846. DOI: https://doi.org/10.1109/ICSE43902.2021.00081

[26] Eugene A. Feinberg and Adam Shwartz. 2012. Handbook of Markov Decision Processes: Methods and Applications, Vol.

40. Springer Science & Business Media.

[27] Antonio Filieri, Martina Maggio, Konstantinos Angelopoulos, Nicolás D’ippolito, Ilias Gerostathopoulos, Andreas Berndt Hempel, Henry Hoffmann, Pooyan Jamshidi, Evangelia Kalyvianaki, Cristian Klein, et al. 2017. Control strategies for self-adaptive software systems. ACM Transactions on Autonomous and Adaptive Systems. 11, 4, Article 24 (Feb. 2017), 31 pages. DOI: https://doi.org/10.1145/3024188

[28] Paul Gainer, Ernst Moritz Hahn, and Sven Schewe. 2018. Incremental verification of parametric and reconfigurable Markov chains. In Quantitative Evaluation of Systems, Annabelle McIver and Andras Horvath (Eds.), Springer International Publishing, Cham, 140–156.

[29] Simos Gerasimou. 2016. Runtime Quantitative Verification of Self-Adaptive Systems. Ph.D. Dissertation. University of York.

<!-- page 37 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:37

[30] Alison L. Gibbs and Francis Edward Su. 2002. On choosing and bounding probability metrics. International Statistical Review/Revue Internationale de Statistique 70, 3 (2002), 419–435. Retrieved from http://www.jstor.org/stable/1403865

[31] Sofie Haesaert, Alessandro Abate, and Paul M. J. Van den Hof. 2016. Verification of general Markov decision processes by approximate similarity relations and policy refinement. In Quantitative Evaluation of Systems. Gul Agha and Benny Van Houdt (Eds.), Springer International Publishing, Cham, 227–243.

[32] Robert K. Hammond and J. Eric Bickel. 2013. Reexamining discrete approximations to continuous distributions. Decision Analysis 10, 1 (March 2013), 6–25. DOI: https://doi.org/10.1287/deca.1120.0260

[33] Afshin Hasani, Mehran Alidoost Nia, and Reza Ebrahimi Atani. 2024. Balancing safety and security in autonomous driving systems: A machine learning approach with safety-first prioritization. In Proceedings of the 1st workshop on Recent Advances in Resilient and Trustworthy Machine Learning (ARTMAN ’24). IEEE Press, 1–12.

[34] Markus C. Huebscher and Julie A. McCann. 2008. A survey of autonomic computing—Degrees, models, and applica- tions. ACM Computing Surveys 40, 3, Article 7 (Aug. 2008), 28 pages. DOI: https://doi.org/10.1145/1380584.1380585

[35] J.O. Kephart and D.M. Chess. 2003. The vision of autonomic computing. Computer 36, 1 (2003), 41–50. DOI: https: //doi.org/10.1109/MC.2003.1160055

[36] Christian Krupitzer, Felix Maximilian Roth, Sebastian VanSyckel, Gregor Schiele, and Christian Becker. 2015. A survey on engineering approaches for self-adaptive systems. Pervasive and Mobile Computing 17 (2015), 184–206. DOI: https://doi.org/10.1016/j.pmcj.2014.09.009

[37] Marta Kwiatkowska. 2016. Advances and challenges of quantitative verification and synthesis for cyber-physical systems. In Proceedings of 2016 Science of Security for Cyber-Physical Systems Workshop (SOSCYPS), 1–5. DOI: https: //doi.org/10.1109/SOSCYPS.2016.7579999

[38] Marta Kwiatkowska, Gethin Norman, and David Parker. 2011. PRISM 4.0: Verification of probabilistic real-time systems. In Computer Aided Verification. Ganesh Gopalakrishnan and Shaz Qadeer (Eds.), Springer, Berlin, 585–591.

[39] Marta Kwiatkowska, David Parker, and Hongyang Qu. 2011. Incremental quantitative verification for Markov decision processes. In Proceedings of the 2011 IEEE/IFIP 41st International Conference on Dependable Systems & Networks (DSN), 359–370. DOI: https://doi.org/10.1109/DSN.2011.5958249

[40] Abolfazl Lavaei, Sadegh Esmaeil Zadeh Soudjani, Rupak Majumdar, and Majid Zamani. 2017. Compositional ab- stractions of interconnected discrete-time stochastic control systems. In Proceedings of the 2017 IEEE 56th Annual Conference on Decision and Control (CDC). 3551–3556. DOI: https://doi.org/10.1109/CDC.2017.8264180

[41] Nianyu Li, Christos Tsigkanos, Zhi Jin, Zhenjiang Hu, and Carlo Ghezzi. 2020. Early validation of cyber–physical space systems via multi-concerns integration. Journal of Systems and Software 170 (2020), 110742. DOI: https://doi. org/10.1016/j.jss.2020.110742

[42] Debasmita Lohar, Milos Prokop, and Eva Darulova. 2019. Sound probabilistic numerical error analysis. In Integrated Formal Methods. Wolfgang Ahrendt and Silvia Lizeth Tapia Tarifa (Eds.), Springer International Publishing, Cham, 322–340.

[43] Matt Luckcuck, Marie Farrell, Louise A. Dennis, Clare Dixon, and Michael Fisher. 2019. Formal specification and verification of autonomous robotic systems: A survey. ACM Computing Surveys 52, 5, Article 100 (Sept. 2019), 41 pages. DOI: https://doi.org/10.1145/3342355

[44] Paulo Henrique Maia, Lucas Vieira, Matheus Chagas, Yijun Yu, Andrea Zisman, and Bashar Nuseibeh. 2019. Cautious adaptation of defiant components. In Proceedings of the 2019 34th IEEE/ACM International Conference on Automated Software Engineering (ASE), 974–985. DOI: https://doi.org/10.1109/ASE.2019.00094

[45] Francisco Martín Rico, Francisco J. Rodríguez-Lera, Jonatan Ginés Clavero, Ángel Manuel Guerrero-Higueras, and Vicente Matellán Olivera. 2020. An acceptance test for assistive robots. Sensors 20, 14 (2020), 3912.

[46] Gabriel A. Moreno, Javier Cámara, David Garlan, and Bradley Schmerl. 2018. Flexible and efficient decision-making for proactive latency-aware self-adaptation. ACM Transactions on Autonomous and Adaptive Systems 13, 1, Article 3 (April 2018), 36 pages. DOI: https://doi.org/10.1145/3149180

[47] Mehran Alidoost Nia. 2021. An Exemplar of Runtime Approximation Framework for Self-Adaptive Systems in Safety- Critical Applications. Retrieved December 10, 2024 from https://github.com/alidoostnia/Runtime-ApproximationFramework-for-Self-Adaptive-Systems

[48] Mehran Alidoost Nia. 2022. Runtime Probabilistic Analysis of Self-Adaptive Systems via Formal Approximation Tech- niques. Ph.D. Dissertation. University of Tehran, Iran.

[49] Mehran Alidoost Nia, Mehdi Kargahi, and Alessandro Abate. 2020. Self-adaptation with imperfect monitoring in solar energy harvesting systems. In Proceedings of the 2020 CSI/CPSSI International Symposium on Real-Time and Embedded Systems and Technologies (RTEST), 1–8. DOI: https://doi.org/10.1109/RTEST49666.2020.9140148

[50] Gethin Norman and David Parker. 2014. Quantitative Verification: Formal Guarantees for Timeliness, Reliability and Performance. Technical Report. The London Mathematical Society and the Smith Institute.

<!-- page 38 -->

3:38 M. Alidoost Nia et al.

[51] Elizabeth Polgreen, Viraj B. Wijesuriya, Sofie Haesaert, and Alessandro Abate. 2017. Automated experiment design for data-efficient verification of parametric Markov decision processes. In Quantitative Evaluation of Systems. Nathalie Bertrand and Luca Bortolussi (Eds.), Springer International Publishing, Cham, 259–274.

[52] Kyriakos Polymenakos, Luca Laurenti, Andrea Patane, Jan-Peter Calliess, Luca Cardelli, Marta Kwiatkowska, Alessandro Abate, and Stephen Roberts. 2020. Safety guarantees for iterative predictions with Gaussian processes. In Proceedings of the 2020 59th IEEE Conference on Decision and Control (CDC), 3187–3193. DOI: https: //doi.org/10.1109/CDC42340.2020.9304029

[53] Seung Yeob Shin, Shiva Nejati, Mehrdad Sabetzadeh, Lionel C. Briand, and Frank Zimmer. 2018. Test case prioritization for acceptance testing of cyber physical systems: A multi-objective search-based approach. In Proceedings of the 27th ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA ’18). ACM, New York, NY, 49–60. DOI: https://doi.org/10.1145/3213846.3213852

[54] Amit Kumar Singh, Piotr Dziurzanski, Hashan Roshantha Mendis, and Leandro Soares Indrusiak. 2017. A survey and comparative study of hard and soft real-time dynamic resource allocation strategies for multi-/many-core systems. ACM Computing Survreys 50, 2, Article 24 (April 2017), 40 pages. DOI: https://doi.org/10.1145/3057267

[55] Robert Tarjan. 1971. Depth-first search and linear graph algorithms. In Proceedings of the 12th Annual Symposium on Switching and Automata Theory (swat ’71), 114–121. DOI: https://doi.org/10.1109/SWAT.1971.10

[56] Ilya Tkachev and Alessandro Abate. 2014. On approximation metrics for linear temporal model-checking of stochastic systems. In Proceedings of the 17th International Conference on Hybrid Systems: Computation and Control (HSCC ’14). ACM, New York, NY, 193–202. DOI: https://doi.org/10.1145/2562059.2562118

[57] Robert Trevethan. 2017. Sensitivity, specificity, and predictive values: Foundations, pliabilities, and pitfalls in research and practice. Frontiers in Public Health 5 (2017), 307.

[58] Jeroen Van Der Donckt, Danny Weyns, Federico Quin, Jonas Van Der Donckt, and Sam Michiels. 2020. Applying deep learning to reduce large adaptation spaces of self-adaptive systems with multiple types of goals. In Proceedings of the IEEE/ACM 15th International Symposium on Software Engineering for Adaptive and Self-Managing Systems (SEAMS ’20). ACM, New York, NY, 20–30. DOI: https://doi.org/10.1145/3387939.3391605

[59] Thomas Watson. 2018. Communication complexity of statistical distance. ACM Transactions on Computation Theory 10, 1, Article 2 (Jan. 2018), 11 pages. DOI: https://doi.org/10.1145/3170708

[60] Kangfeng Ye, Ana Cavalcanti, Simon Foster, Alvaro Miyazawa, and Jim Woodcock. 2022. Probabilistic modelling and verification using RoboChart and PRISM. Software and Systems Modeling 21, 2 (April 2022), 667–716. DOI: https://doi.org/10.1007/s10270-021-00916-8

[61] Yayun Zheng, Fang Yang, Jinqiao Duan, and Jürgen Kurths. 2021. Quantifying model uncertainty for the observed non-Gaussian data by the Hellinger distance. Communications in Nonlinear Science and Numerical Simulation 96 (2021), 105720. DOI: https://doi.org/10.1016/j.cnsns.2021.105720

[62] Adam Ziebinski, Rafal Cupek, Marek Drewniak, and Bartlomiej Wolny. 2019. Soft real-time systems for low-cost unmanned ground vehicle. 2019. In Proceedings of the 11th International Conference on Computational Collective Intelligence, Part II (ICCCI ’19). Springer-Verlag, Berlin, 196–206. DOI: https://doi.org/10.1007/978-3-030-28374-2_17 Appendices A Models in PRISM Style We provide PRISM codes associated with each part of the rescue robot team’s models. A.1 Environment Model The model shown in Listing A1 corresponds to the environmental and distance models presented in Figure 2 in PRISM style. As you can see in the code, we have defined two variables 표푏푠and 푑, respectively, representing obstacle state (see Figure 2(a)) and current distance (see Figure 2(b)). For example, if 표푏푠= 1, it means that in the next step with distance 푑, no obstacle is expected. The variables 푝표푏푠and 푝푛표푏푠refer to the probability of facing an obstacle or no obstacle in the next workflow step, respectively. Furthermore, the variable 푥comes from Listing A4 and shows the state of the monitoring robot. We can adjust the look-ahead horizon and the distance model by changing the value of constants 푑푖푠푡and 푢푝at the beginning of the emulations.

<!-- page 39 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:39 1 const double pnobs; 2 const double pobs; 3 const int dist; 4 const int up; 5 module Env 6 obs :[0..up] init 0; 7 d:[0..100] init 0; // global distance 8 [s] (((obs*3)+3) <=up) & d<dist -5 & x!=2 -> 9 pnobs:(obs '=(obs*3)+3) & (d'=d+5) 10 +pobs:(obs '=(obs*3)+2) & (d'=d+5) 11 +1-pnobs -pobs:(obs '=(obs*3)+1) & (d'=d+5); 12 [s] x=2 & d<dist -5 & obs!=0 -> (obs '=0) & (d'=d+5); 13 endmodule Listing A1. The PRISM code for the model of the environment. A.2 The Models of the Rescue Robot Team In this part, we provide the model of three robots in the rescue robot team. The first PRISM code shown in Listing A2 corresponds to the model presented in Figure 3(c), which denotes the behavior of the leader robot in accordance with the environment model and the distance limitations in different states, including “stop,” “run,” “emergency_stop,” and “reduce_speed.” As denoted in the code, different actions are captured by the model when no obstacle (푛표), obstacle (표푏), and partial obstacle (푝표) is detected. In addition, 푑푠shows the situation where the leader robot receives the destination target. 1 module Leader 2 z:[0..3] init 1;//0=stop , 1=run , 2=e-stop , 3= reduce speed 3 4 [ob] z=0 -> (z'=0); 5 [po] z=0 -> (z'=1); 6 [no] z=0 -> (z'=1); 7 8 [ob] z=1&d!=dist -> (z'=2); 9 [po] z=1&d!=dist -> (z'=3); 10 [no] z=1&d!=dist -> (z'=1); 11 [ds] z=1&d=dist -> (z'=0); 12 13 [ob] z=2 -> (z'=2); 14 [po] z=2 -> (z'=1); 15 [no] z=2 -> (z'=1); 16 17 [ob] z=3&d!=dist -> (z'=2); 18 [po] z=3&d!=dist -> (z'=3); 19 [no] z=3&d!=dist -> (z'=1); 20 [ds] z=3&d=dist -> (z'=0); 21 22 endmodule Listing A2. The PRISM code for Leader robot.

<!-- page 40 -->

3:40 M. Alidoost Nia et al. Listings A3 and A4 present the PRISM code for caterpillar and monitoring robots, respectively, corresponding to Figure 3(b) and (a). If the monitoring robot detects any obstacle, it will be reflected in the caterpillar model (푓= 2), and the state of the robot is changed to “handle” (푦= 1). 푝ℎ푎푛푑 denotes the probability of handling the obstacle. Once the obstacle is removed (푦= 2), the state of the caterpillar robot changes to “standby” (푦= 0). The monitoring robot continuously tries to detect the changes. If any change is detected (푥= 1), it will update the model (푥= 2) by changing the values of the probabilistic parameters in the environment model. 1 formula f=mod(obs ,3); 2 const double phand; 3 module Caterpillar 4 y:[0..2] init 0;//0=standby , 1=handle , 2= remove 5 [s] y=0 & (f!=2) -> (y'=0); 6 [s] y=0 & (f=2) -> (y'=1); 7 [hand] y=1 -> phand:(y'=2)+1-phand:(y'=1); 8 [st] y=2 -> (y'=0); 9 endmodule Listing A3. The PRISM code for Caterpillar robot. 1 const double pmon; 2 module Monitor 3 x:[0..2] init 0;//0=monitor , 1= detect change , 2= update 4 [s] x=0 -> pmon:(x'=0)+1-pmon:(x'=1); 5 [s] x=1 -> (x'=2); 6 [s] x=2 -> (x'=0); 7 endmodule Listing A4. The PRISM code for Monitoring robot. A.3 Formal Properties and Reward Structure The code presented in Listing A5 describes the formal properties that the model is verified against. In this part, we introduce a few labels in our model. The labels “obstacle” and “partial_obstacle” refer to detecting an obstacle in the next state of the environment. “obstacle” denotes a serious barrier that the caterpillar robot should remove, and the leader robot must be stopped in that situation, which is denoted by the “emergency_stop” label. However, a “partial_obstacle” can be easily passed by reducing speed, which is denoted by the “reduce_speed” label. In addition, the “running” and “stop” labels show the state of the leader robot. The two first properties ensure the safety of the Leader robot. The first states if an obstacle is detected in the next workflow step and the Leader robot is running, the next state must be “stop” or “emergency_stop” to ensure the safety of the equipment. The second property expresses the same logic in facing a partial obstacle, and if the Leader robot is running, it must transit to “reduce_speed” or “stop.” The third and fourth properties calculate the MER of the system for three different labels. In addition, Listing A6 denotes the reward rules (values) for these different labels.

<!-- page 41 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:41 1 // safety requirements 2 filter(forall ,(" obstacle "&" running ") => 3 (P >=1[(X(" emergency_stop "|" stop"))])) 4 filter(forall ,(" partial_obstacle "&" running ") => 5 (P >=1[X(" reduce_speed "|" stop")])) 6 // optimization requirements 7 R{" general "}max =?[" emergency_stop "&(F <=3 "running ")] 8 R{" general "}max =?[F <=30 "stop"] Listing A5. The PCTL formula for the system properties in PRISM style. 1 rewards "general" 2 "running" : 2; 3 "reduce_speed" : 1; 4 "emergency_stop" : 0; 5 endrewards Listing A6. The reward structure for the robot team in PRISM style. B Notations and Nomenclatures Tables B1 and B2 present the notations and nomenclatures of the article, respectively. Table B1. Table of Notations

| Notation | Description | Notation | Description |
|---|---|---|---|
| 훾′ | Update error of a component | 퐴 | Action set |
| 훾 | Threshold for 훾′ | 푅 | Cumulative reward |
| Γ′ | Total update error | Γ | Threshold for Γ′ |
| 푓 | Freshness of a component | 휏 | Task set |
| F | Freshness of the model | 푒 푖 | Execution time |
| 푀 | Concrete model | 푑 푖 | Deadline |
| 훼 | Synthesized actions | 푎 | An action |
| 푈 | Utility | 푆 | Set of states |
| 푆 퐹 | Set of final states | 퐷 | Distribution function |
| 퐴푃 | Set of atomic propositions | 푏 | An atomic proposition |
| 푃 | Probability function | 푠 | A state |
| 푉 | Set of variables | 훿 | Policy |
| 휙 | A state formula | Φ | Set of properties |
| 휓 | A path formula | 푋 | Next operator |
| 퐹 | Finally operator | ∪ | Until operator |
| ∪≤푛 | Bounded Until operator | 퐸 | Expected reward |
| 휋 | A path | Π | Set of paths |
| 휃 | Variables’ evaluation | Θ | Set of evaluations |
| 푠 0 | An initial state | 푆 √0 | A set of initial states |
| 휖 | Terminal |  | Termination |
| 휎 | A sample trace | 휀 | Threshold of bisimilarity |

(Continued)

<!-- page 42 -->

3:42 M. Alidoost Nia et al. Table B1. Continued

| Notation | Description | Notation | Description |
|---|---|---|---|
| R휀 | 휀-bisimilar relation | R | Relation |
| 푆 b | 휀-bisimilar set of states | 푘 | Length of a trace/path |
| 푑 푇푉 | Total variation | 푠푢푝 | Supremum |
| 푑 퐻 | Hellinger distance | 퐶 | Set of components |
| 퐶 푗 | A component | 푣 | A probabilistic parameter |
| 푀퐴 | Approximate model | 푀퐴′ | Delayed-update approximate model |
| 푈+ | Tolerable error | D | Utility error |
| L | High priority task set | 휁 | Total execution time |
| 퐻 | Look-ahead horizon | 휚 | Priority |
| 푌 | Set of reference values | 푦 푖 | Expected verification result |
| 푦′ 푖 | Current verification result | 푇푟푎푐푒푠() | A set of traces |
| Δ | Threshold for Δ′ | 푈 푎푣푔 | Average utility |
| Δ′ | Deviation of results | R | Real numbers |
| 퐾 | Feasible task set | N | Natural numbers |
| 푈퐶 | Utility of concrete model | 푈퐴 | Utility of approximate model |
| 푈퐴′ | Utility of approximate delayed-update model | 푟 | Reward |
| 퐿 | Possible resources | 푟 푖 | Reward for step 푖 |
| Ω | Space | 푚푎푥 | Maximization policy |
| 푝 푛표푏푠 | Probability of facing no obstacle | 푝 표푏푠 | Probability of facing an obstacle |
| 푝 ℎ푎푛푑 | Probability of handling an obstacle | 푝 푚표푛 | Probability of detecting a change |
| 푑 | Current position | 푑푖푠푡 | Final target distance |

<!-- page 43 -->

Efficient Model Verification at Runtime through Adaptive Dynamic Approximation 3:43 Table B2. Table of Nomenclatures

| Nomenclature | Description |
|---|---|
| 푅푄푉 | Runtime quantitative verification |
| 퐷푄푉 | Design time quantitative verification |
| 푀퐷푃 | Markov decision process |
| 푃푀퐷푃 | Parametric Markov decision process |
| 푆퐴푆 | Self-adaptive system |
| 퐶푃푆 | Cyber-physical system |
| 푆퐶퐶 | Strongly-connected components |
| 푃푆퐶퐶 | Parametric SCC |
| 퐹푆퐶퐶 | Fixed SCC |
| 푀퐴푃퐸 | Monitoring, analyzing, planning, executing |
| 퐸푃푇 | Extended Pearson-Tukey |
| 푃퐶푇퐿 | Probabilistic computation tree logic |
| MER | Maximum expected reward |
| 퐸퐷퐹 | Earliest deadline first |
| 푅표퐶 | Rate of change |
| 푇푁 | True negative |
| 푇푃 | True positive |
| 퐹푁 | False negative |
| 퐹푃 | False positive |
| 푇푃푅 | True-positive Rate |
| 푇푁푅 | True-negative Rate |
| 퐴퐶퐶 | Accuracy |
| 푇푉 | Total variation |
| 푅표퐶 | Rate of changes |

Received 17 December 2023; revised 11 October 2024; accepted 5 December 2024
