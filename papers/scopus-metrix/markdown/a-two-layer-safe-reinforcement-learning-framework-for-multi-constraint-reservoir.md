# A two-layer safe reinforcement learning framework for multi-constraint reservoir operation- Integrating action masking and lagrangian dual method

> **Source PDF:** `A two-layer safe reinforcement learning framework for multi-constraint reservoir operation- Integrating action masking and lagrangian dual method.pdf` · **Pages:** 19 · Converted by `scripts/paper2md.py` from the original PDF. **Equations are extracted glyph-by-glyph and may be mangled — check the PDF before quoting any formula.**

<!-- page 1 -->

Contents lists available at ScienceDirect

Journal of Hydrology

journal homepage: www.elsevier.com/locate/jhydrol

A two-layer safe reinforcement learning framework for multi-constraint reservoir operation: Integrating action masking and lagrangian dual method

Zaichao Xie a, Xiaoli Zhang b,∗, Wei Xu a iD, Guoguo Lin c, Dong Li d, Shuncai Zhang a, Hongyan Chen a, Sheng Yang a

a College of River and Ocean Engineering, Chongqing Jiaotong University, Chongqing, 400074, China b College of Water Resources, North China University of Water Resources and Electric Power, Zhengzhou, 450046, China c Chongqing Yufa Water Conservancy Research Institute Co., Ltd., Chongqing, 401120, China d Chongqing Shipping Construction Development (Group) Co., Ltd., Chongqing, 500112, China

### H I G H L I G H T S

• Two-layer SafeRL for multi-constraint reservoir operation. • Validated on the Three Gorges Reservoir using 60 years of daily inflows. • Lagrangian dual cuts total cost by 71.5% and increases generation reward by 4.9%. • FullMask reduces action-correction violations from 21–79% to 0%. • Square mapping increases total energy generation by 0.54% over the linear baseline.

### A R T I C L E I N F O

### A B S T R A C T

Reservoir operation is a safety-critical sequential decision problem that must balance multiple operational objec­ tives under strict water-level and release constraints. However, Deep Reinforcement Learning (DRL) algorithms frequently violate safety constraints during exploration, limiting their applicability in real-world engineering. This study proposes a two-layer Safe Reinforcement Learning (SafeRL) framework. The first layer is a state-driven ac­ tion mask that filters infeasible actions before policy sampling; the second layer is a Proximal Policy Optimization (PPO)-Lagrangian implementation that adaptively adjusts the constraint multiplier to balance safety and perfor­ mance. Unlike single-mechanism approaches that rely solely on post-hoc correction or fixed penalties, this design combines proactive filtering with adaptive optimization. Additionally, a non-linear action mapping is introduced to improve learning efficiency in constraint-critical regions. The framework is validated on the Three Gorges Reservoir using 60 years (1965–2024) of daily inflow records. Results show that the Lagrangian dual method reduces the total absolute constraint cost by 71.5% and increases generation reward by 4.9% compared with the correction-based baseline. In the baseline evaluation, the FullMask reduces the action-correction violation rate from 21–79% to zero, and the square mapping yields a further 0.54% gain in total energy generation. These results support the proposed SafeRL framework as a model-consistent decision-support approach for long-horizon reservoir operation under the modeled constraints.

This manuscript was handled by Dan Lu, Editor-in-Chief, with the assistance of Mohammad Zounemat-Kermani, Associate Editor

Keywords: Reservoir operation Safe reinforcement learning Lagrangian dual method Action masking Non-linear action mapping Three gorges reservoir

## 1 . Introduction

and safety constraints. During flood seasons, water levels must remain below flood limits to preserve flood-control storage and reduce flood risk (Donnelly et al., 2022). During drawdown periods, the drawdown rate must be limited because rapid water-level decline can destabilize reser­ voir banks and trigger landslides (Chen et al., 2023; Jian et al., 2014; Igityan et al., 2025). During dry seasons, relatively high water levels

Globally, tens of thousands of large reservoirs provide hydropower, irrigation, and water supply (Yeh, 1985; Schmitt and Rosa, 2024). Their operating decisions directly affect the safety and economic develop­ ment of hundreds of millions of people (Labadie, 2004; Moghaddam et al., 2025). In practice, reservoir operation must satisfy strict physical

∗Corresponding author. Email addresses: zaichao2027@163.com (Z. Xie), zxl436@163.com (X. Zhang).

https://doi.org/10.1016/j.jhydrol.2026.135694 Received 27 January 2026; Received in revised form 12 May 2026; Accepted 13 May 2026

Available online 15 May 2026 0022-1694/© 2026 Elsevier B.V. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

<!-- page 2 -->

Z. Xie, X. Zhang, W. Xu et al.

are needed to secure power generation and water supply (Liu et al., 2025). Meanwhile, releases must stay within the safe capacities of outlet facilities and downstream channels (Gosden et al., 2014; Rosita et al., 2025; Thepjunthra et al., 2025). Together, these operational constraints define the feasible region for reservoir operation. Violations can lead to severe consequences and therefore require safety-aware intelligent operation methods.

Beyond constraint handling mechanisms, action space design also af­ fects safety and learning efficiency. Discrete action spaces are widely used in reservoir operation for their training stability and deploy­ ment ease. However, the action mapping scheme directly influences exploration behavior and safety (Gu et al., 2024; Kåge et al., 2025). Traditional linear mapping uniformly distributes discrete actions across the entire flow range, failing to consider varying precision requirements in different regions.

Deep reinforcement learning (DRL) has gained attention in reser­ voir operation because it supports end-to-end learning and adaptive sequential decision-making (Mnih et al., 2015; Jiang et al., 2024; Negm et al., 2024). Early studies demonstrated this potential: Castelletti et al. (2010) applied fitted Q-iteration to Lake Maggiore management, and Xu et al. (2021) pioneered deep Q-networks for reservoir optimiza­ tion. However, standard DRL methods optimize cumulative reward and may explore actions that violate water-level or release constraints, lead­ ing to non-convergent training or hazardous policies (Liu et al., 2021; Kahn et al., 2017). Although standard DRL algorithms may perform well in simulation, they are often difficult to deploy in real reservoir sys­ tems due to strict, state-dependent physical constraints (Satija et al., 2020). Therefore, constructing practical Safe Reinforcement Learning (SafeRL) frameworks has become increasingly important for intelligent reservoir operation (Kåge et al., 2025). Such safety requirements are commonly formalized using the constrained Markov decision process (CMDP) framework.

Variable resolution discretization has been shown to improve learn­ ing efficiency by allocating higher resolution to critical regions (Munos and Moore, 2002), and recent work demonstrates that adaptive dis­ cretization can capture multimodal behavior patterns (Dadashi et al., 2022; Sinclair et al., 2020; Fujimoto et al., 2019). In reservoir operation, this need for variable resolution is particularly pronounced. Low-release regions require high-precision control to balance ecology, navigation, and power generation, whereas high-release flood control can tolerate lower precision. However, current research predominantly employs lin­ ear action mappings, which compromise both learning efficiency and fine-grained safety control. There is limited systematic research on how different non-linear action mappings affect the balance between safety, energy production and training stability under strict multi-constraint settings.

To bridge these gaps, this study proposes a two-layer SafeRL frame­ work for multi-constraint reservoir operation, validated on the Three Gorges Reservoir using 60 years (1965–2024) of daily inflow records from the Changjiang Water Resources Commission. The framework in­ tegrates a state-driven action mask with an adaptive PPO-Lagrangian optimizer to form a unified two-layer safety architecture and evalu­ ates its effectiveness through controlled ablation experiments within a unified PPO-based setting. Additionally, non-linear action mappings are introduced as a complementary action-representation module to improve learning efficiency in constraint-critical regions.

SafeRL typically employs the CMDP framework, where Altman (1999) formalized safety as expected cost constraints. Achiam et al. (2017) proposed constrained policy optimization (CPO), which en­ sures monotonic constraint satisfaction through trust-region updates. However, CPO requires computing second-order policy derivatives and approximating the Fisher information matrix inverse, resulting in high computational cost and implementation challenges in largescale networks (Liu et al., 2021). In comparison, the Lagrangian dual method offers a computationally efficient alternative by introduc­ ing learnable multipliers that adaptively adjust constraint penalties (Zhang et al., 2022; Stooke et al., 2020). Incorporating proportionalintegral-derivative (PID) controllers to adjust multipliers can further accelerate convergence. This approach has been successfully applied in autonomous driving, power systems and chemical process control (Li et al., 2025; Xu and Lin, 2024; Zheng et al., 2023). However, in reservoir operation, current studies mainly address single or simple com­ bined constraints (Kåge et al., 2025). The effectiveness of Lagrangian methods in complex reservoir systems with multiple heterogeneous, state-dependent constraints remains unverified. A recent comprehensive survey of constraint formulations in SafeRL highlights that singlemechanism approaches often struggle to balance safety guarantees with performance optimization in complex constrained environments (Wachi et al., 2024).

## 2 . Methods

Fig. 1 shows the two-layer safety architecture proposed in this study. This framework integrates a proactive safety filtering layer (right, or­ ange) and an adaptive constraint optimization layer (left, blue) to support feasible and efficient reservoir operation under the modeled constraints.

The proactive safety filtering layer employs action masking to elim­ inate infeasible actions before policy sampling, providing hard feasi­ bility enforcement with respect to the modeled physical constraints (Section 2.2). The adaptive constraint optimization layer uses the Lagrangian dual method to adaptively adjust constraint penalties during training, balancing safety and performance (Section 2.3). The two layers work synergistically: action masking prevents immediate violations by filtering unsafe actions, while Lagrangian optimization guides long-term policy learning by adaptively balancing safety and performance.

To address these limitations, a layered safety perspective is adopted in which learning-based strategies are complemented by safety filters (Choi et al., 2025). Action masking serves as a widely used proactive safety filtering technique and has shown substantial effectiveness in many domains. It has enhanced decision safety and sample efficiency in applications such as real-time strategy games (Huang and Ontañón, 2022; Hou et al., 2023b) and unmanned aerial vehicle (UAV) path planning (Hou et al., 2023a; Rizvi and Boyle, 2024). Theoretically, un­ der specific conditions, action masking does not affect the convergence to the optimal policy and can significantly reduce sample complex­ ity during training (Huang and Ontañón, 2022; Wang et al., 2024). Nevertheless, research on action masking in reservoir operation remains limited. Current studies mainly focus on handling static upper and lower bound constraints, while generally not addressing state-dependent dy­ namic constraints. These dynamic constraints arise from water balance, time-varying water-level limits and multi-step coupling effects (Xu et al., 2025). In particular, there is a critical need to develop physically consis­ tent, state-driven masks that can be integrated with Lagrangian methods and evaluated over long-term operation.

The step-by-step decision propagation across the two layers is delin­ eated as follows:

(1) Policy Output (Agent Intention): Based on the current reser­

voir state, the policy network proposes a preliminary action preference distribution intended to maximize expected long-term rewards. (2) Proactive Filtering (Layer 1): Before any action is executed, a

state-driven action mask calculates the absolute physical safety boundaries. It blocks infeasible actions proposed by the policy, acting as a feasibility filter with respect to the encoded constraints (e.g., preventing modeled overtopping or emptying states). (3) Environment Execution: The agent selects a safe operation from

the filtered feasible options, which is then mapped to the actual physical release via a non-linear action mapping mechanism, and applies it to the simulation. It then receives an operational reward

<!-- page 3 -->

Z. Xie, X. Zhang, W. Xu et al.

**Fig. 1. Flowchart of the two-layer safety architecture. Layer 1 (action masking) filters infeasible actions before sampling, while layer 2 (PPO-Lagrangian) updates the policy using constraint-violation feedback from masked trajectories.**

(e.g., energy-generation value) along with constraint penalties if any soft operational boundaries are crossed. (4) Adaptive Optimization (Layer 2): The Lagrangian method eval­

a continuous 4-year daily trajectory, and temporal dependency is car­ ried by the physical state-transition dynamics, the inflow and forecast inputs, and the periodic time encoding in Eq. (2). The present setup should therefore be interpreted as offline policy learning with exogenous forecast inputs; it does not assimilate real-time forecast updates, prop­ agate forecast-error distributions through the policy, or perform online parameter adaptation during deployment.

uates the accumulated constraint penalties to dynamically adjust the constraint–penalty weight (dual multiplier). This continuous feedback gradually reshapes the agent’s intrinsic policy toward safer operational regions, reducing its reliance on the Layer 1 safety net in future decisions.

In the implementation, these state variables are converted into dimensionless inputs before being fed to the policy network using physically meaningful reference scales (details in Appendix C). This variable-wise physical normalization improves numerical conditioning while preserving the chronological order and relative temporal variation within each episode, so it should not be interpreted as replacing explicit uncertainty modeling or online adaptation. The resulting state represen­ tation is intentionally kept compact and physics-informed, allowing each component to retain direct hydrological or operational meaning and to remain consistent with the constraint-driven mask construction.

The complete framework is formalized within the Constrained Markov Decision Process (CMDP) paradigm described below.

2.1 . Problem formulation: CMDP for reservoir operation

This study employs the CMDP to formalize sequential decisionmaking problems with safety constraints. The reservoir system is de­ scribed by the tuple

The action space A represents the set of available release decisions. It uses a discretized set of 𝑁 candidate releases: A = {𝑎0, 𝑎1, … , 𝑎𝑁−1}. Each discrete action corresponds to a candidate release decision, and the action-to-release mapping is specified below when deriving feasible action intervals for masking.

```math
M = (S, A, 𝑃, 𝑟, 𝑐, 𝜌0, 𝛾, 𝑑)
(1)
```

where S is the state space containing information about the reservoir state; A is the action space representing the set of available opera­ tion decisions; 𝑃(𝑠𝑡+1 ∣𝑠𝑡, 𝑎𝑡) is the state-transition kernel; 𝑟(𝑠𝑡, 𝑎𝑡) is the immediate reward term for generation benefit; 𝑐(𝑠𝑡, 𝑎𝑡) ≥0 is the constraint–cost function for the remaining operational requirements and safety penalties; 𝜌0 is the initial state distribution; 𝛾∈(0, 1) is the dis­ count factor controlling the weight of future rewards; and 𝑑> 0 is the upper bound of the expected average violation metric defined in Eq. (9), representing the acceptable level of safety risk.

The transition function 𝑃 is determined by the physical dynamics of the reservoir. Reservoir storage and water level follow the principle of mass conservation. The water balance equation is

𝑉𝑡+1 = 𝑉𝑡+ (𝑄in,𝑡−𝑄out,𝑡

```math
) Δ𝑡
(3)
```

where 𝑉𝑡 is storage at the beginning of step 𝑡 (m3); 𝑄out,𝑡 is the release corresponding to action 𝑎𝑡 (m3/s); and Δ𝑡 is the dispatch time step length (s). Storage and water level are related through a stage-storage curve 𝑓𝑉 that is strictly monotonically increasing. The water level at the next time step is then determined through its inverse function:

The state space S should capture the key information for reservoir operation. The state vector is defined as follows:

𝑠𝑡= (ℎ𝑡, 𝑄in,𝑡, 𝑄future,𝑡, ℎmin,𝑡, ℎmax,𝑡, 𝐞𝑡

```math
)
(2)
```

ℎ𝑡+1 = 𝑓−1

```math
𝑉(𝑉𝑡+1)
(4)
```

where 𝑡 denotes the discrete time step index; ℎ𝑡 is the water level at the start of step 𝑡 (m); 𝑄in,𝑡 is the predicted mean inflow during step 𝑡 (m3/s); 𝑄future,𝑡 is the 7-day-ahead mean inflow forecast (m3/s); ℎmin,𝑡 and ℎmax,𝑡 are the lower and upper water-level limits at step 𝑡 (m); and 𝐞𝑡= [sin(2𝜋𝑡∕𝑇year), cos(2𝜋𝑡∕𝑇year)] is a two-dimensional periodic time en­ coding that captures the annual seasonality, where 𝑇year is the number of time steps in a year.

Eqs. (3) and (4) ensure that the environment dynamics obey mass con­ servation and topography, providing the physical basis for constraint design.

In the generic formulation above, 𝑄out,𝑡 denotes the actual reser­ voir outflow applied in the mass-balance update. In the Three Gorges case-study implementation, the RL action controls turbine-generation discharge. When flood-control rules trigger spills during flood periods, the actual outflow used in the state transition is computed as 𝑄out,𝑡= 𝑄gen,𝑡+ 𝑄spill,𝑡.

Here, 𝑄in,𝑡 and 𝑄future,𝑡 are treated as forecast inputs. To isolate the effect of the safety mechanisms in the controlled experiments, deter­ ministic forecasts within the look-ahead horizon are used rather than an explicit forecast-uncertainty model. This does not mean that the data are treated as static independent samples: each episode remains

To distinguish the action pipeline, three action variables are used when needed. 𝑎net

𝑡 denotes the direct network output before masking;

<!-- page 4 -->

Z. Xie, X. Zhang, W. Xu et al.

probabilistic flood-risk or flood-damage objective; instead, it is enforced structurally through hard feasibility constraints, including dynamic sea­ sonal water-level bounds, release–capacity limits, and flood-season spill routing. The present CMDP is also a single-reservoir formulation, so co­ ordinated storage-release decisions across multiple reservoirs are outside its current scope.

**Table 1 Definition of constraint–cost components.**

Cost Type Symbol Trigger Condition Formula

√(𝑄eco −𝑄out,𝑡)∕𝑄eco Guaranteed-power cost 𝑐power 𝑃𝑡< 𝑃guaranteed 𝛽power

Ecological flow cost 𝑐eco 𝑄out,𝑡< 𝑄eco 𝛽eco

√

(𝑃guaranteed −𝑃𝑡)∕𝑃guaranteed Navigation flow cost 𝑐nav 𝑄out,𝑡< 𝑄nav 𝛽nav

√(𝑄nav −𝑄out,𝑡)∕𝑄nav

√

In the CMDP formulation, the optimization objective of the policy 𝜋(𝑎∣𝑠) is to maximize discounted cumulative reward while satisfying long-term constraints. The expected cumulative reward is defined as:

𝑡 ≠𝑎mask

‖𝑎exec

𝑡 −𝑎mask

𝑡 ‖

Action adjustment cost 𝑐action 𝑎exec

𝑡 𝛽action

### [ 𝑇∑

]

𝑎mask

𝑡 denotes the action issued by the agent after optional masking (thus 𝑎mask

𝐽(𝜋) = E𝑠0∼𝜌0, 𝑎𝑡∼𝜋, 𝑠𝑡+1∼𝑃

𝛾𝑡𝑟(𝑠𝑡, 𝑎𝑡)

```math
(7)
```

𝑡 = 𝑎net

𝑡 when no mask is applied); and 𝑎exec

𝑡 denotes the final action executed by the environment after any environment-side correction or routing logic.

𝑡=0

To align the CMDP constraint definition with the practical PPOLagrangian implementation, this study constrains an expected average violation metric derived from step-wise constraint costs. Specifically, the raw step-wise constraint cost 𝑐(𝑠𝑡, 𝑎𝑡) is first normalized and thresholded to form a non-negative violation metric: ̂

The constraint-cost function 𝑐(𝑠𝑡, 𝑎𝑡) aggregates the negative objec­ tive terms and safety penalties across multiple operational dimensions:

```math
𝑐(𝑠𝑡, 𝑎𝑡) = 𝑐eco + 𝑐power + 𝑐nav + 𝑐action
(5)
```

𝑍 , 𝑣(𝑠𝑡, 𝑎𝑡) = max (0,̂ 𝑐(𝑠𝑡, 𝑎𝑡) −𝜖tol

```math
)
(8)
```

𝑐(𝑠𝑡, 𝑎𝑡) = 𝑐(𝑠𝑡, 𝑎𝑡)

The first three components—minimum ecological base flow, guaranteedpower output, and minimum navigation flow—encode the correspond­ ing operational objectives; their threshold values (𝑄eco, 𝑃guaranteed, 𝑄nav) follow the reservoir’s operational requirements and dispatch regulations issued by the Changjiang Water Resources Commission, together with site-specific engineering practices. The fourth component (𝑐action) quan­ tifies the discrepancy between the agent-issued action 𝑎mask

where ̂𝑐(𝑠𝑡, 𝑎𝑡) is the normalized constraint cost; 𝑣(𝑠𝑡, 𝑎𝑡) is the step-wise violation metric that captures violations exceeding the tolerance level; 𝑍> 0 is a normalization factor; and 𝜖tol ≥0 is a tolerance threshold for minor violations. The expected average violation over an episode is defined as: ̄

𝑡 and the environment-executed action 𝑎exec

𝑡 . This term is logged for all methods as a unified measure of environment intervention; in the penalty-based and Lagrangian methods it also enters the optimization objective, whereas in the correction-based baseline it is recorded for diagnosis and compar­ ison but is not subtracted from the training reward. Table 1 defines each component and its corresponding formula. Note: Each cost component is activated only when its trigger condition holds; otherwise it is zero. The square-root (concave) functional form is adopted as a penalty-shaping design: it produces a steep gradient near the threshold, encouraging the policy to avoid marginal violations, while growing sub-linearly for large deviations, preventing the cost term from dominating the reward signal during early training. Thus, 𝑐action records any mismatch between the agent-issued and executed actions, regardless of whether it arises from post-hoc correction, emergency recovery from extreme states, or spill routing. The equal-coefficient setting provides a neutral baseline for the controlled ablation experiments, isolating the effect of the safety mechanisms from subjective preference weighting. It is not intended as a calibrated preference model for deployment, but only fixes the cost scale so that the safety mechanisms can be compared under the same objective specification.

### [ 1 𝑇+ 1

]

𝑇∑

𝑉(𝜋) = E𝑠0∼𝜌0, 𝑎𝑡∼𝜋, 𝑠𝑡+1∼𝑃

𝑣(𝑠𝑡, 𝑎𝑡)

```math
(9)
```

𝑡=0

where 𝑇 is the episode length. The constrained optimization problem of the CMDP is formulated as:

𝜋 𝐽(𝜋),

max

```math
(10)
```

s.t.̄ 𝑉(𝜋) ≤𝑑

Two complementary forms of “violation” are distinguished in this study. (i) Action-correction violations occur when the final executed action differs from the action issued by the agent (𝑎exec

𝑡 ≠𝑎mask

𝑡 ). This event indicates that the environment has intervened (via correc­ tion or routing at execution time) to enforce physical feasibility, and its frequency is reported as the violation rate (%). The proactive ac­ tion mask aims to prevent these interventions by blocking currently infeasible actions before sampling. (ii) Cost-based (soft) violations are quantified by the violation metric 𝑣(𝑠𝑡, 𝑎𝑡) in Eq. (8), derived from the multi-dimensional constraint cost 𝑐(𝑠𝑡, 𝑎𝑡). This metric is used for PPO-Lagrangian reward reconstruction and dual updates. During train­ ing, 𝑣𝑡 is recorded and averaged (̄𝑣) to update 𝜆. During evaluation, the learned policy is executed on held-out inflow years and both the action-correction violation rate and cost-based satisfaction statistics (e.g., satisfaction rates for guaranteed-power, navigation, and ecology) are reported.

This study represents multi-objective reservoir operation through a reward–cost decomposition. Energy generation is treated as the posi­ tive reward term, whereas navigation, ecology, guaranteed-power, and action-adjustment objectives are expressed as cost terms. The reward term is defined as the normalized energy generation:

𝑟(𝑠𝑡, 𝑎𝑡) = 𝐸𝑡−𝐸min 𝐸max −𝐸min

Eq. (10) establishes the mathematical foundation for the subsequent two-layer safety architecture: proactive safety filtering (Section 2.2) and adaptive constraint optimization (Section 2.3).

```math
(6)
```

where 𝐸𝑡= 𝑃𝑡⋅Δ𝑡 is the cumulative energy generation (MWh) during time step 𝑡; 𝑃𝑡 is the average power output (MW) calculated from the release 𝑄out,𝑡 and the effective head; 𝐸min is the minimum energy gener­ ation corresponding to the guaranteed-power output over Δ𝑡; and 𝐸max is the maximum energy generation corresponding to the installed capacity over Δ𝑡.

2.2 . Proactive safety filtering: state-driven action mask

This section presents the first-layer safety mechanism: a state-driven action mask for proactive safety filtering. This mechanism filters out infeasible actions by setting their probabilities to zero before sampling, ensuring that every sampled action lies in the modeled state-dependent admissible set and can serve as the agent-issued action 𝑎mask

Within this formulation, the modeled objective scope should be read carefully. Hydropower generation is the only directly maximized reward term. Ecological base flow, navigation flow, and guaranteed-power re­ quirements are represented explicitly through the corresponding cost components and the satisfaction indicators reported later in evalua­ tion. Flood-season operating safety is not optimized here as a separate

𝑡 .

2.2.1 . Role of the action mask in policy sampling The policy network 𝜋𝜃 takes state 𝑠𝑡 as input and outputs a logit vector 𝐳(𝑠𝑡) = [𝑧0, 𝑧1, … , 𝑧𝑁−1]⊤, where 𝑧𝑖 represents the unnormalized

<!-- page 5 -->

Z. Xie, X. Zhang, W. Xu et al.

log-probability for action 𝑎𝑖. The action masking mechanism introduces a binary mask vector 𝑀(𝑠𝑡) = [𝑚0, 𝑚1, … , 𝑚𝑁−1]⊤, where 𝑚𝑖= 1 indicates that action 𝑎𝑖 is feasible and 𝑚𝑖= 0 indicates infeasibility. By applying a large negative bias to infeasible actions before the Softmax operation, their probabilities are forced to zero. The resulting policy probability distribution after action masking is: ̃

Combining Eqs. (15) and (17) with the physical capacity constraints (𝑄min, 𝑄max), the feasible release interval is:

𝑄out,𝑡∈[𝑄phys

```math
]
(18)
```

min , 𝑄phys

max

where

{

}

𝑉𝑡−𝑉limit,𝑡

𝑄phys

⎧ ⎪ ⎨ ⎪⎩

𝑄min, 𝑄in,𝑡+

,

min = max

𝑗∶𝑚𝑗=1 exp(𝑧𝑗), if 𝑚𝑖= 1,

exp(𝑧𝑖) ∑

Δ𝑡

```math
}
(19)
```

{

𝜋𝜃(𝑎𝑖∣𝑠𝑡) =

```math
(11)
```

𝑉𝑡−𝑉low,𝑡

0, if 𝑚𝑖= 0.

𝑄phys

𝑄max, 𝑄in,𝑡+

max = min

Δ𝑡

Eq. (19) ensures that the release simultaneously satisfies both the water level constraints and the capacity constraints through the max and min operators. This feasible release interval [𝑄phys

The action mask restricts the policy to the safe action set Asafe(𝑠𝑡) = {𝑎𝑖∣𝑚𝑖= 1} and ensures

min , 𝑄phys

max ] is mapped to the action index interval [𝑎min, 𝑎max] as follows: ̃

∑

```math
𝜋𝜃(𝑎𝑖∣𝑠𝑡) = 1,̃
𝜋𝜃(𝑎𝑖∣𝑠𝑡) = 0 for all 𝑎𝑖∉Asafe(𝑠𝑡)
(12)
```

𝑎𝑖∈Asafe(𝑠𝑡)̃

𝑄phys

max = 𝑄phys

min −𝑄min 𝑄max −𝑄min

max −𝑄min 𝑄max −𝑄min

𝑄phys

,̃ 𝑄phys

min =

```math
(20)
```

During the sampling phase, the masked policy ̃𝜋𝜃 selects actions from Asafe(𝑠𝑡) according to Eq. (11), ensuring that the sampled action satis­ fies the modeled current-state physical constraints. This sampled action is the agent-issued action 𝑎mask

𝑢min = 𝑔−1(̃𝑄phys

min ), 𝑢max = 𝑔−1(̃𝑄phys

```math
max )
(21)
```

𝑡 . This mechanism enforces current-state feasibility through logit adjustment without modifying the network ar­ chitecture, maintaining compatibility with standard DRL algorithms. Environment-side correction can still occur if accumulated earlier deci­ sions drive the reservoir into emergency states or if spill routing modifies the realized discharge, in which case the final executed action 𝑎exec

𝑎min = min (𝑁−1, max(0, round(𝑢min ⋅(𝑁−1)))),

```math
𝑎max = min (𝑁−1, max(0, round(𝑢max ⋅(𝑁−1))))
(22)
```

The binary mask vector is constructed as

𝑡 may still differ from 𝑎mask

{

```math
1,
if 𝑎min ≤𝑖≤𝑎max,
```

𝑡 . Hence, zero action-correction violations remain an empirical outcome of successful training rather than a purely formal consequence of masking alone.

𝑚𝑖=

```math
(23)
```

0, otherwise.

where 𝑔−1(⋅) is the inverse of the monotonic mapping 𝑔(⋅) defined above, mapping normalized releases to the normalized action variable 𝑢. For the linear mapping 𝑔(𝑢) = 𝑢, the above expressions reduce to the standard linear scaling. Thus, the masking mechanism dynamically computes the feasible action set at each time step, completing the mapping from physi­ cal constraints to mask vector and ensuring that policy sampling remains consistent with the modeled feasible action set under both linear and non-linear action mappings.

2.2.2 . Derivation of safe action intervals The upper and lower bounds of release are derived based on the wa­ ter balance Eq. (3) and the water-level constraints (ℎmin,𝑡 and ℎmax,𝑡 in Eq. (2)). Let 𝑄min and 𝑄max denote the minimum and maximum physical release capacities of the reservoir, respectively (m3/s). To connect phys­ ical feasibility in release space with discrete action indices, a monotonic action-to-release mapping is used. Let 𝑖∈{0, 1, … , 𝑁−1} denote a dis­ crete action index and define its normalized form 𝑢= 𝑖∕(𝑁−1) ∈[0, 1]. The physical release corresponding to 𝑢 is

2.2.3 . BaseMask and FullMask Beyond the storage constraints derived above, reservoir operation involves additional constraints such as water-level fluctuation rates, dryseason release-to-inflow ratios, and release rate-of-change limits. Based on the source and completeness of constraints, two types of masks are designed: a BaseMask and a FullMask.

```math
𝑄out = 𝑄min + (𝑄max −𝑄min) 𝑔(𝑢)
(13)
```

where 𝑔∶[0, 1] →[0, 1] is strictly monotonically increasing with 𝑔(0) = 0 and 𝑔(1) = 1. The inverse mapping 𝑔−1 maps normalized releases back to 𝑢 and is used below to convert feasible release intervals into feasible action-index intervals.

The BaseMask includes reservoir-specific operating rules derived from dispatch regulations and engineering practice. The rules are statedependent and are often expressed as conditional statements, e.g., “if the inflow satisfies condition A, then the release must satisfy condi­ tion B”. Derived from the dispatch regulations of the Three Gorges Reservoir issued by the Changjiang Water Resources Commission to­ gether with engineering practice, the BaseMask reflects established operational knowledge and is easy to implement. However, because its design relies on manual summarization, it may overlook multi-step cou­ pling constraints, leading to a pseudo-feasible region where an action appears feasible in the short term but inevitably causes constraint vi­ olations over multiple steps. Detailed implementations and parameter settings are provided in Appendix A.

To prevent the water level from exceeding the maximum allow­ able level ℎmax,𝑡 after executing action 𝑎𝑡, the reservoir storage must not surpass 𝑉limit,𝑡= 𝑓𝑉(ℎmax,𝑡), where 𝑉limit,𝑡 is the storage capacity corresponding to ℎmax,𝑡 (m3):

```math
𝑉𝑡+1 = 𝑉𝑡+ (𝑄in,𝑡−𝑄out,𝑡)Δ𝑡≤𝑉limit,𝑡
(14)
```

From Eq. (14), the minimum allowable release is:

𝑉𝑡−𝑉limit,𝑡

𝑄out,𝑡≥𝑄in,𝑡+

```math
Δ𝑡
(15)
```

Similarly, to prevent the reservoir storage from dropping below the min­ imum allowable level, the storage must satisfy 𝑉𝑡+1 ≥𝑉low,𝑡, where 𝑉low,𝑡= 𝑓𝑉(ℎmin,𝑡) is the storage capacity corresponding to ℎmin,𝑡 (m3):

The FullMask is a physics-based mask constructed from general phys­ ical constraints, thereby forming a comprehensive safety system without requiring reservoir-specific expert rules. The general constraints include:

```math
𝑉𝑡+1 = 𝑉𝑡+ (𝑄in,𝑡−𝑄out,𝑡)Δ𝑡≥𝑉low,𝑡
(16)
```

(1) Storage constraints as defined in Eqs. (15)–(19) to ensure that the

post-action water level remains within allowable bounds; (2) Water-level fluctuation rate constraints, which limit the change

Thus, the maximum allowable release is:

𝑉𝑡−𝑉low,𝑡

in water level between consecutive time steps to prevent rapid drawdown;

𝑄out,𝑡≤𝑄in,𝑡+

```math
Δ𝑡
(17)
```

<!-- page 6 -->

Z. Xie, X. Zhang, W. Xu et al.

[ℎmin,𝑡, ℎmax,𝑡] for state 𝑠𝑡. The projected action 𝑎exec

(3) Release-to-inflow ratio constraints during the dry season to pre­

𝑡 is then executed by the environment. Any resulting mismatch 𝑎exec

𝑡 ≠𝑎mask

vent over-release, ensuring that the cumulative release over a specified period does not exceed a threshold proportion of cumulative inflow; (4) Release rate-of-change constraints, restricting variations in re­

𝑡 is still logged through 𝑐action for unified diagnosis and cross-method comparison, but it is not subtracted from the correction-based training objective.

Penalty-based method. This method incorporates constraint viola­ tions directly into the reward function, enabling the policy gradient to receive constraint information during training. Given a fixed penalty coefficient 𝜆fix > 0, the modified immediate reward is: ̃

lease between adjacent periods to maintain downstream channel stability; (5) Water-level exceedance protection, which enforces an emergency

release when water levels exceed safe thresholds to prioritize flood safety over other objectives.

```math
𝑟(𝑠𝑡, 𝑎𝑡) = 𝑟(𝑠𝑡, 𝑎𝑡) −𝜆fix 𝑐(𝑠𝑡, 𝑎𝑡)
(25)
```

Relative to the correction-based baseline, the same logged cost components—including the action-adjustment term 𝑐action—are explic­ itly injected into the learning objective through the fixed coefficient 𝜆fix.

The specific implementation and parameter settings for each constraint are given in Appendix B.

The mask framework therefore provides two complementary fea­ sibility filters: the reservoir-specific BaseMask and the more transfer­ able physics-based FullMask. More generally, while the BaseMask is reservoir- and regulation-specific, most components of the FullMask are derived from universal mass-conservation relationships and generic op­ erational limits, and can therefore be transferred to other reservoirs by re-parameterizing a small set of physical curves (e.g., stage–storage rela­ tionships, dynamic level bounds) and facility capacities. In the proposed framework, the BaseMask is treated as an optional reservoir-specific prior rather than a prerequisite for constructing the FullMask. If expert rules are partially misspecified or unavailable, a physics-based FullMask can still be constructed from basic engineering descriptors (e.g., stage– storage curve, release capacity limits, and time-varying level bounds) and used as the primary proactive safety filter. Experiment B empirically validates this design choice.

The CMDP becomes an unconstrained MDP@:

### [ 𝑇∑

]

𝛾𝑡̃ 𝑟(𝑠𝑡, 𝑎𝑡)

𝜋 E𝑠0∼𝜌0, 𝜏∼𝜋

max

```math
(26)
```

𝑡=0

where 𝜏 denotes a trajectory. This unconstrained formulation can be optimized using standard DRL algorithms. However, selecting an appro­ priate fixed penalty weight is challenging for reservoir operation with multiple heterogeneous constraints of varying importance.

2.3.2 . Lagrangian dual method The Lagrangian dual method introduces a learnable Lagrangian mul­ tiplier 𝜆 to adaptively adjust constraint penalties during training. This study integrates this method with the Proximal Policy Optimization (PPO) algorithm to form the PPO-Lagrangian framework. Based on Eq. (10), the augmented Lagrangian function is constructed:

2.3 . Adaptive constraint optimization: lagrangian dual method

This section presents adaptive constraint optimization via the Lagrangian dual method and first reviews the baseline constrainthandling approaches for context.

```math
L(𝜋, 𝜆) = 𝐽(𝜋) −𝜆(̄𝑉(𝜋) −𝑑)
(27)
```

where 𝜆≥0 is the learnable dual variable. Training alternates between two phases to solve the saddle-point problem defined by Eq. (27):

2.3.1 . Baseline constraint-handling methods For the CMDP framework, the choice of constraint-handling mecha­ nism affects both the performance and safety of the algorithm. This study compares three methods: the correction-based method, the penaltybased method and the Lagrangian dual method. Their fundamental dis­ tinction lies in how and when the constraint cost 𝑐(𝑠𝑡, 𝑎𝑡) is incorporated into the decision-making process.

Phase 1: Policy update (Lines 4–12 in Algorithm 1). With fixed 𝜆, the policy is optimized under the modified reward ̃𝑟𝜆(𝑠𝑡, 𝑎𝑡) = 𝑟(𝑠𝑡, 𝑎𝑡) − 𝜆𝑣(𝑠𝑡, 𝑎𝑡), where 𝑣(𝑠𝑡, 𝑎𝑡) is the violation metric defined in Eq. (8). This converts the constrained optimization into an unconstrained problem where violations are penalized through the reward signal. The policy network parameters 𝜃 and value network parameters 𝜙 are updated via multiple epochs of stochastic gradient descent on the PPO objective.

Beyond these three approaches, the SafeRL/CMDP literature also includes trust-region constrained-policy updates (e.g., CPO) and other Lagrangian variants (e.g., PID-style adaptation). This study focuses on the correction, fixed-penalty, and Lagrangian dual paradigms because they can be implemented in a unified PPO-based framework suitable for long-horizon, multi-constraint reservoir operation with discrete actions and action masking. CPO-type methods are discussed in the Introduction as important references but are not adopted as baselines here because their reliance on second-order policy updates and Fisher-informationmatrix inversion makes them substantially more burdensome in the present long-horizon discrete-action setting.

Phase 2: Dual variable update (Lines 13–18 in Algorithm 1). With fixed policy, 𝜆 is adjusted based on the empirical constraint satisfaction. The dual update rule is:

𝜆𝑘+1 = [𝜆𝑘+ 𝛼𝜆(̄𝑣−𝑑)]

```math
+
(28)
```

where 𝑘 indexes iterations; 𝛼𝜆> 0 is the dual learning rate; ̄𝑣 is the es­ timated average violation at iteration 𝑘 (computed as the batch mean of 𝑣𝑡); and [⋅]+ denotes projection onto the non-negative axis. When average violations exceed the threshold 𝑑, 𝜆 increases to strengthen penalties; when violations are well controlled, 𝜆 stabilizes or decreases, allowing the policy to focus more on performance optimization.

Correction-based method. Safety constraints are treated as hard boundaries, and actions are corrected after the fact to ensure decision feasibility. At each time step 𝑡, the policy network 𝜋𝜃 outputs a candidate action 𝑎net

In Layer 2, adaptivity is implemented through data-driven updates of the dual multiplier 𝜆 via Eq. (28) based on the observed violation metric 𝑣𝑡, so the adaptive behavior arises directly from violation-feedbackdriven dual adjustment during training.

𝑡 . Because no proactive mask is applied in this baseline, the action issued by the agent is 𝑎mask

𝑡 = 𝑎net

𝑡 . The water balance equation (Eq. 3) is used to predict the resulting water level ℎ𝑡+1. If the water level exceeds the allowable range [ℎmin,𝑡, ℎmax,𝑡], the environment projects the issued action back into the safe action set Asafe(𝑠𝑡) using a projection operator Π:

To integrate this theoretical framework into the PPO implementa­ tion, step-wise constraint costs 𝑐𝑡 are converted into the violation metric 𝑣𝑡 using Eq. (8) with a normalization factor 𝑍> 0 and a tolerance thresh­ old 𝜖tol ≥0. This preprocessing mitigates heterogeneous scaling across constraint types (Table 1) and tolerates minor violations. The resulting 𝑣𝑡 is used in both reward reconstruction (̃𝑟𝑡= 𝑟𝑡−𝜆⋅𝑣𝑡) and dual updates via the batch average ̄𝑣.

𝑎exec

𝑡 = ΠAsafe(𝑠𝑡)(𝑎mask

```math
𝑡
)
(24)
```

where Π projects the agent-issued action to the nearest safe action, and Asafe(𝑠𝑡) is the set of actions that result in water levels within

<!-- page 7 -->

Z. Xie, X. Zhang, W. Xu et al.

Algorithm 1 Lagrangian-based constrained PPO (PPO-Lagrangian).

1: Input: CMDP environment M; policy parameters 𝜃; value param­ eters 𝜙; initial dual variable 𝜆≥0; constraint threshold 𝑑; dual learning rate 𝛼𝜆; normalization factor 𝑍; violation threshold 𝜖tol; dual update interval 𝐾; maximum dual upper bound 𝜆max (optional). 2: Initialize 𝜆, 𝜃, 𝜙; reset environment; clear experience buffer. 3: for iteration 𝑘= 1, 2, … , 𝐾max do 4: Collect trajectories {(𝑠𝑡, 𝑎𝑡, 𝑟𝑡, 𝑐𝑡)} using current policy 𝜋𝜃 (use ̃𝜋𝜃 in Eq. (11) when action masking is enabled) 5: for each time step 𝑡 in the batch do 6: ̂ 𝑐𝑡= 𝑐𝑡∕𝑍 ⊳ normalized cost 7: 𝑣𝑡= max(0,̂ 𝑐𝑡−𝜖tol) ⊳ violation metric 8: ̃ 𝑟𝑡= 𝑟𝑡−𝜆⋅𝑣𝑡 ⊳ reconstructed reward 9: end for 10: Using {̃𝑟𝑡} and {𝑠𝑡, 𝑎𝑡}, compute advantages ̂𝐴𝑡(𝜆) with value function 𝑉𝜙 11: Construct PPO loss 𝐿PPO(𝜃, 𝜙; 𝜆) (clipped policy loss + value loss + entropy) 12: Update (𝜃, 𝜙) by several epochs of stochastic gradient descent (SGD)@: (𝜃, 𝜙) ←(𝜃, 𝜙) −𝜂∇𝜃,𝜙𝐿PPO 13: ̄ 𝑣= 1

**Fig. 2. Flowchart of the PPO-Lagrangian implementation. The black paths repre­ sent standard PPO components, while the purple paths indicate the Lagrangianbased constraint-handling extensions. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)**

∑

𝑡𝑣𝑡 ⊳ average violation in batch 14: if 𝑘(mod 𝐾) == 0 then ⊳ dual update 15: 𝜆←𝜆+ 𝛼𝜆⋅(̄𝑣−𝑑) 16: (optional) 𝜆←min(𝜆, 𝜆max) 17: 𝜆←max(0, 𝜆) ⊳ projection onto [0, 𝜆max] 18: end if 19: end for 20: Output: Trained policy 𝜋𝜃∗ aimed at satisfying ̄𝑉(𝜋𝜃∗) ≤𝑑 under the modeled constraints.

𝑁

2.4 . Non-linear action mapping

A common baseline in reservoir-operation DRL uses a linear mapping between action indices and physical releases, allocating uniform resolu­ tion across the entire release range. This makes it difficult to simulta­ neously achieve fine-grained control in low-flow regimes and effective flood response in high-flow regimes. This section introduces non-linear mappings that allocate different action densities to different release intervals. The feasible release interval [𝑄phys

min , 𝑄phys

max ] is computed in phys­ ical space (Eqs. (15)–(19)), then mapped to action indices via the inverse function 𝑔−1 defined below, maintaining compatibility with the masking mechanism.

Parameter definition, rationale, and practical tuning. In this im­ plementation, the constraint cost is already normalized, and therefore 𝑍= 1.0 is used. A small tolerance 𝜖tol = 0.05 is applied so that negligible numerical fluctuations do not trigger dual updates, while still penalizing meaningful violations. The dual learning rate 𝛼𝜆 controls how fast 𝜆 re­ acts to constraint pressure, and the update interval 𝐾 smooths the dual updates by aggregating ̄𝑣 over several iterations; together they act as a low-pass filter that avoids over-reacting to transient violation spikes. No explicit upper bound is imposed on 𝜆; the non-negativity projection remains active. On the primal side, standard PPO stabilizers (clipped objective, entropy regularization, and advantage/value normalization) further reduce policy-update oscillations. The fixed dual hyperparam­ eters (𝑑, 𝛼𝜆, 𝐾, 𝑍, 𝜖tol) used across Experiments A–C are reported in Appendix C (Table C.9) to keep the mechanism-level comparisons di­ rectly comparable. Their local sensitivity is examined separately in Supplementary Material Section S5 through a three-seed re-evaluation of representative settings. In that supplementary check, the adopted default lies within a stable working range for this study: a larger 𝛼𝜆 reduces mean reward and generation, whereas a looser threshold 𝑑 introduces oc­ casional action-correction violations. Together with the dual-trajectory pattern reported later in Fig. 5, these results provide local empirical sup­ port for the stability and reproducibility of the adopted defaults in the present study.

Let the discrete action space have size 𝑁. The normalized index for an action 𝑎∈{0, 1, … , 𝑁−1} is

```math
𝑢=
𝑎
𝑁−1 ∈[0, 1]
(29)
```

where 𝑢 is the normalized action variable. The non-linear mapping is defined as

```math
𝑄out = 𝑄min + (𝑄max −𝑄min) 𝑔(𝑢)
(30)
```

where 𝑔∶[0, 1] →[0, 1] is a strictly monotonically increasing function that satisfies the boundary conditions 𝑔(0) = 0 and 𝑔(1) = 1. Typical mapping functions include:

• Linear mapping: 𝑔(𝑢) = 𝑢, which distributes uniform resolution across the entire release range; • Power mapping: 𝑔(𝑢) = 𝑢𝑘 (𝑘> 1), which concentrates action den­ sity in low-release regimes. In Experiment C, 𝑘 is set to 2 (square mapping, C2) and 3 (cubic mapping, C3); • Logarithmic mapping: 𝑔(𝑢) = log(1 + 𝛼𝑢)∕log(1 + 𝛼) (𝛼> 0), which concentrates action density in high-release regimes; • Exponential mapping: 𝑔(𝑢) = (exp(𝛼𝑢)−1)∕(exp(𝛼)−1) (𝛼> 0), which offers more flexible control of resolution.

Algorithm 1 formalizes the PPO-Lagrangian implementation used in this study, and Fig. 2 visualizes the workflow.

Fig. 2 distinguishes between standard PPO components (black flow) and the constraint-handling extensions introduced in this study (purple flow). The extensions preprocess 𝑐𝑡 into 𝑣𝑡, incorporate 𝑣𝑡 into the re­ constructed reward ̃𝑟𝑡= 𝑟𝑡−𝜆⋅𝑣𝑡, and update 𝜆 periodically to balance constraint satisfaction and performance.

The inverse function 𝑔−1 ∶[0, 1] →[0, 1] maps normalized releases back to normalized action variables. Given a physical release 𝑄out ∈ [𝑄min, 𝑄max] with its normalized form ̃𝑄= (𝑄out −𝑄min)∕(𝑄max −𝑄min),

<!-- page 8 -->

Z. Xie, X. Zhang, W. Xu et al.

**Fig. 3. Location of the Three Gorges Reservoir and its controlled basin in the upper Yangtze River.**

the corresponding normalized action variable 𝑢 is:

**Table 2 Main Three Gorges case-study parameters used in this study.**

```math
𝑢= 𝑔−1(̃𝑄)
(31)
```

Parameter Value Unit

Controlled catchment area 1.0 × 106 km2

and then the action is quantized into a discrete action index as

Historical inflow record length 60 (1965–2024) years Mean annual runoff 398.65 billion m3

Main runoff season share (May to October) 74.46 % Installed capacity 22,500 MW Maximum aggregate turbine-generation discharge 31,187 m3/s Flood-control limited water level 145 m Routine flood-season operating level about 145–146.5 m Normal pool level 175 m Ecological minimum flow 6000 m3/s Navigation minimum release 6500 m3/s

```math
𝑎= round(𝑢⋅(𝑁−1))
(32)
```

where round(⋅) denotes rounding to the nearest integer.

## 3 . Experimental setup

Building upon the framework proposed in Section 2, this study conducts multi-year experiments with daily time steps on the Three Gorges Reservoir to evaluate safe long-horizon operation under multi­ ple constraints. This section introduces the case study, data sources, and experimental design, while implementation-level settings and runtime statistics are reported in Appendix C.

interpolation, and the compact policy inputs were converted to modelready dimensionless quantities using the physics-guided normalization described in Section 2.

The key operating constraints are formulated as follows. The safety constraints require that the water level must not exceed the dynamic upper and lower operating bounds, and the actual outflow must remain consistent with the safe operating capacities of the power-generation and spillway systems. The ecological and navigation constraints follow the threshold values summarized in Table 2, consistent with the op­ erating practices and published studies of the Three Gorges Reservoir (Zheng, 2016; Rheinheimer et al., 2016).

3.1 . Case description

The Three Gorges Reservoir is selected as the case study for model validation. Located on the mainstream of the upper Yangtze River in central China (Fig. 3), it represents a typical large hydropower reser­ voir with long-horizon, multi-constraint operating requirements. The key case-study, dataset, and operational descriptors used in this study are summarized in Table 2. Further engineering details on the character­ istic water levels and the generating-unit rated-discharge breakdown are summarized in Appendix D. The stage–storage relationship is obtained from engineering measurements through piecewise fitting and interpo­ lation. Plant parameters such as unit efficiency curves and guaranteed output are obtained from published literature and engineering docu­ ments. All hydrological and operational data have undergone quality control and engineering checks.

As described in Section 2, the RL agent controls turbine–generation discharge; when flood-control rules require total outflow to exceed the maximum aggregate turbine capacity, the excess is treated as spill by a rule-based module. Accordingly, the implementation uses a reward– cost scalarization: long-horizon energy generation enters as the positive reward term, while the navigation, ecological, and guaranteed-power objectives enter as costs. Flood-control spill routing is represented by an environment-side rule rather than by a dedicated flood-control optimization model.

Table 2 consolidates the main Three Gorges case-study parameters that were previously distributed across the text. The hydrological data are sourced from the Hydrological Yearbook of the Changjiang Water Resources Commission, and annual runoff ranking is used to define the P5/P25/P50/P75/P95 representative years for the training/evalu­ ation split described below. Here, the P-values denote annual-runoff exceedance-probability classes, with lower P indicating wetter years and higher P indicating drier years.

3.2 . Experimental design

To systematically evaluate the impact of different constrainthandling mechanisms, proactive safety-filtering strategies, and actionspace designs on long-term operational performance, this study adopts a staged experimental design. All experiments are conducted within the same Three Gorges simulation environment, where the environmental dynamics, state space, action space, and constraints remain consistent.

Using the quality-controlled 60-year inflow series summarized in Table 2, the stage–storage relation was implemented through piecewise

<!-- page 9 -->

Z. Xie, X. Zhang, W. Xu et al.

**Fig. 4. Evolution of performance and constraint satisfaction during training. (a) maximum return; (b) generation reward; (c) action adjustment cost; (d) guaranteedpower cost; (e) navigation flow cost; (f) ecological flow cost. The three curves represent correction (A1, pink), penalty (A2, green) and Lagrangian (A3, blue). Shaded areas denote the standard deviation over five runs. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)**

Controlled-variable testing is applied only to the constraint-handling module, the action-masking strategy, and the action-mapping scheme; the underlying task reward function 𝑟(𝑠𝑡, 𝑎𝑡) and the constraint-cost def­ initions 𝑐(𝑠𝑡, 𝑎𝑡) are kept identical across all configurations, and the compared methods differ only in how constraint costs are incorporated into the learning signal and optimization.

Experiment A (constraint handling). Using a linear actionrelease mapping, this study compares three representative strategies: Correction-based (A1), fixed penalty-based (A2, 𝜆fix = 1.0), and PPOLagrangian (A3).

Experiment B (action masking). Based on A3, this study com­ pares three mask strengths: NoMask (B1), BaseMask (B2; operating rules in Appendix A), and FullMask (B3; general physical constraints in Appendix B).

Data partitioning. Based on the 60-year inflow series from 1965 to 2024, annual runoff volumes were calculated for each year and ranked to obtain empirical exceedance-probability classes. Five representative years labeled P95, P75, P50, P25, and P5 were then selected to represent extreme dry, dry, average, wet, and extreme wet hydrological condi­ tions, respectively. These representative years were isolated to form an independent evaluation set, while the remaining years formed the train­ ing set. All policies were trained offline on the historical training years and then evaluated with fixed parameters on the held-out representative years. No receding-horizon replanning, online fine-tuning, or continual policy updating was performed in this evaluation protocol. All compara­ tive experiments used the same inflow sequences and initial water levels to ensure comparability of results. Unless otherwise noted, the term base­ line evaluation below refers to this nominal held-out evaluation on the five representative years without additional inflow perturbations; sepa­ rate stress-test evaluations under perturbed inflows are reported in the Supplementary Material.

Experiment C (action mapping). Under the unified framework “PPO-Lagrangian + FullMask” (A3+B3), this study compares five map­ ping functions in Section 2.4: Linear (C1), Square (C2), Cubic (C3), Exponential (C4) and Logarithmic (C5).

Computational environment and runtime. All experiments were conducted on a workstation equipped with an Intel Core i5-12400F CPU and an NVIDIA GeForce RTX 3060 GPU, using PyTorch 2.4.1 under Windows. Each training run used 50 rounds with six parallel environ­ ments (300 cumulative 4-year episodes; 438,000 environment steps). The wall-clock training time per run ranges from approximately 19 to 29 minutes depending on the configuration, and the end-of-training eval­ uation of one episode requires about 4.0–5.3 s. The constrained PPO layer adds moderate training overhead relative to the fixed-penalty base­ line: A3 requires 24.20 ± 0.02 min versus 19.22 ± 0.02 min for A2, while evaluation time changes only from 4.39 ± 0.04 to 4.45 ± 0.14 s. Adding the state-driven mask likewise introduces a moderate overhead mainly through per-step feasible-set computation: B3 requires 27.89 ± 0.11 min versus 24.20 ± 0.02 min for B1, with evaluation time increasing from 4.45 ± 0.14 to 5.03 ± 0.09 s. By contrast, the five action-mapping vari­ ants remain within a narrow runtime band (27.89–28.51 min training; 4.99–5.28 s evaluation). Detailed runtime statistics for all configurations are reported in Table C.10 in Appendix C.

Within the Three Gorges case, this evaluation split spans five held-out hydrological classes from extreme dry (P95) to extreme wet (P5), pro­ viding a finite dry-to-wet regime check under one reservoir’s operating rules. It should not, however, be interpreted as universal generalization across arbitrary basins, hydroclimatic regimes, or operating institutions.

Experimental configuration. The overall design consists of three experiment groups. Each training run uses 50 collection-update rounds with six parallel environments; in each round, every environment gen­ erates one 4-year episode (365 × 4 daily steps, with leap days removed). This corresponds to 300 cumulative episodes and 365×4×6×50 = 438,000 environment steps per run. All experiments were repeated with five dif­ ferent random seeds, and the mean and standard deviation are reported to ensure statistical reliability.

## 4 . Results and analysis

4.1 . Experiment A: comparison of constraint-handling mechanisms

Performance differences among the three methods arise from differ­ ent constraint-handling principles. The correction-based method (A1)

<!-- page 10 -->

Z. Xie, X. Zhang, W. Xu et al.

coupling between penalty adjustment and constraint satisfaction, with the average violation ̄𝑣 (blue) converging toward the threshold 𝑑= 0.2 and the final violation metric reaching 0.21 ± 0.02 (Table 3).

**Table 3 Summary of training performance for Experiment A (cost metrics are reported as negative penalty terms, so values closer to zero indicate better constraint satisfaction).**

Fig. 5(b) shows that the penalty term 𝜆⋅𝑣(𝑠, 𝑎) first rises and then falls: it rises from about 0.25 to a peak of 2.6 around episode 120, where high soft violations and a rising 𝜆 jointly apply the strongest penalization, and then declines to about 1.0 as ̄𝑣 decreases toward the threshold 𝑑= 0.2. The stabilization of 𝜆 in the final stage (green band in Fig. 5(a) and the smooth approach of ̄𝑣 toward 𝑑 indicate stable primal–dual dynam­ ics. This rise-then-fall pattern reveals the essence of the PPO-Lagrangian method: rather than pursuing 𝑣(𝑠, 𝑎) = 0 at all times, it dynamically adjusts penalty strength to seek a Pareto-optimal balance. When soft vi­ olations decrease, the penalty term drops because 𝑣(𝑠, 𝑎) itself becomes small, even though 𝜆 may still grow, allowing the policy to devote more capacity to objective optimization and avoiding the over-conservatism of fixed-penalty methods.

Metric A1 A2 A3

Maximum return (mean ± std) −299.46 ± 202.49 −723.34 ± 283.34 −293.69 ± 239.69 Generation reward 379.73 ± 26.75 384.00 ± 27.06 398.52 ± 28.07 Action adjustment cost −24.98 ± 3.09 −14.34 ± 2.86 −2.85 ± 1.68 Guaranteed-power cost −98.92 ± 20.55 −90.02 ± 22.41 −26.28 ± 24.22 Navigation flow cost −384.04 ± 48.57 −341.50 ± 51.25 −115.50 ± 75.42 Ecological flow cost −2.13 ± 1.85 −1.50 ± 1.11 −0.49 ± 0.71 Final 𝜆 – – 6.53 ± 0.37 Final average violation – – 0.21 ± 0.02

implements constraint satisfaction through projection: after the policy network outputs an action, infeasible actions are projected back to the feasible set. While this projection guarantees adherence to hard con­ straint boundaries, it also creates a mismatch between the policy-issued action and the environment-executed action, weakening credit assign­ ment and making it harder for the policy to learn avoidance strategies from experience. As shown in Fig. 4 and Table 3, the reward curve of A1 improves slowly with the action adjustment cost remaining stable at −24.98 ± 3.09 and the navigation flow cost remaining at −384.04 ± 48.57, indicating that the execution-time projection severely limits learning effectiveness.

A paired bootstrap analysis (20,000 resamples; paired by seed across the five random seeds) on the held-out evaluation outputs further sup­ ports the robustness of these evaluation-time action-correction and sat­ isfaction improvements. Compared with the fixed-penalty baseline (A2), the PPO-Lagrangian configuration (A3) reduces the action-correction violation rate by 20.76 percentage points (95% CI@: [14.39, 26.50]) and improves the navigation satisfaction rate by 8.45 percentage points (95% CI@: [4.53, 12.15]). Similar trends are observed versus the correction-based baseline (A1). These intervals summarize empirical variability across random seeds and paired evaluation outputs, rather than predictive hydrological uncertainty or forecast-error propagation.

The penalty-based method (A2) injects constraint information into the reward function using a fixed weight (𝜆fix = 1.0, used here as a rep­ resentative fixed-penalty setting for comparison), yet it faces an inherent tuning trade-off. If the weight is too small, constraint information is drowned out by task rewards; if it is too large, the penalty dominates the learning signal. In the experiment, 𝜆fix = 1.0 achieves a 42.6% reduction in the action adjustment cost compared with A1 (from −24.98 to −14.34, Table 3), but results in the lowest return (−723.34±283.34, Table 3) with a large standard deviation. This behavior reflects a structural limitation of fixed-penalty methods in heterogeneous multi-constraint problems: a single coefficient cannot adapt across constraints or training stages, often leading to unstable learning and suboptimal trade-offs.

A stage-wise trajectory analysis reported in the Supplementary Material further shows that the mid-training rise of 𝜆 is associated with persistent seasonal feasibility pressure—especially flood-season physical feasibility and refill-stage minimum-release trade-offs—rather than with a single static constraint family.

4.2 . Experiment B: comparison of action-mask mechanisms

After establishing the advantage of the Lagrangian method in Experiment A, Experiment B introduces action masks of different strengths—NoMask (B1), BaseMask (B2) and FullMask (B3)—to verify the synergy between proactive safety filtering and adaptive constraint optimization. Table 4 summarizes key performance indicators for the three configurations across different periods.

The PPO-Lagrangian method (A3) introduces a dynamically adjusted Lagrangian multiplier 𝜆, converting the constrained optimization into an unconstrained saddle-point problem. As shown in Fig. 4 and Table 3, A3 achieves the best performance across all six metrics. Its generation reward reaches 398.52, a 4.9% increase over A1 (379.73) and a 3.8% increase over A2 (384.00). More importantly, A3 reduces all cost terms by large margins: the action adjustment cost drops to −2.85 ± 1.68, an 88.6% improvement over A1; the navigation flow cost falls by 69.9% relative to A1 (from −384.04 to −115.50); and the guaranteed-power and ecological-flow costs likewise decrease substantially (Table 3). By sum­ ming the absolute values of these four negative penalty metrics, the total absolute constraint cost decreases from 510.07 in A1 to 145.12 in A3, corresponding to a 71.5% reduction. The return curve of A3 fluctuates during early exploration but begins a sustained rise after the 100th cu­ mulative episode and converges stably around −294 (Fig. 4(a). These results suggest that the adaptive dual variable can improve safety and efficiency simultaneously in this setting rather than forcing a simple trade-off.

Fig. 6 further compares the learning dynamics of the three masking strategies. B3 reaches higher returns and near-zero action-adjustment costs at much earlier logged checkpoints than B1 and B2, indicating substantially improved sample efficiency. Over the first 20 logged check­ points, the mean return of B3 is −233.69, compared with −901.66 for B2 and −975.76 for B1; over the same window, the mean action-adjustment cost of B3 is only −6.11, versus −561.30 and −613.93, respectively. This gap quantitatively confirms that the FullMask improves sample effi­ ciency by removing infeasible exploration and keeping policy updates within a much smaller yet still sufficient feasible subspace.

Beyond these aggregate learning-curve summaries, Fig. 7 shows how the mask shapes the evolution of policy actions. From a threedimensional time-space perspective, the three mask configurations behave very differently. In B1 (NoMask), trajectories from different training stages fluctuate violently across the action space and frequently touch the feasible boundaries; even in the late stage the trajectory still oscillates widely. Relying solely on reward penalties makes it difficult for the agent to learn a stable safe boundary, so the policy remains in a high-risk exploratory state.

The Lagrangian dual method mitigates the limitations of the other two methods in this tested setting through joint evolution of the policy and dual variables. Fig. 5(a) displays the evolution of 𝜆, which pro­ gresses through three stages: a slow rise to about 2.5 during exploration (0–50 episodes), an acceleration to about 6.0 during the growth phase (50–250 episodes), and convergence to 6.53 ± 0.37 in the stable phase (250–300 episodes). This trajectory reflects a dynamic balance: when constraint violations are frequent, 𝜆 increases to reinforce safety; once constraints are effectively controlled, 𝜆 stabilizes and the policy shifts toward objective optimization. Fig. 5(b) further reveals the temporal

In Fig. 7, the gray feasible band is the time-varying interval bounded by 𝑎min(𝑡) and 𝑎max(𝑡), and the overlaid boundary curves make these lower and upper limits directly readable. For B1, the band covers the full action-index range because no proactive mask is applied; for B2 and B3, it is computed by the BaseMask and FullMask, respectively. In B2, this feasible band is initially compressed into a narrow strip, forcing the

<!-- page 11 -->

Z. Xie, X. Zhang, W. Xu et al.

**Fig. 5. Internal mechanism of the Lagrangian dual method. (a) Evolution of the Lagrangian multiplier 𝜆, showing three stages: Exploration Stage (yellow, 0–50 episodes), Growth Stage (blue, 50–250 episodes) and stable Stage (green, 250–300 episodes); (b) dynamic relationship between the average violation ̄𝑣 (blue solid line) and the penalty term 𝜆⋅𝑣(𝑠, 𝑎) (orange dashed line), with the horizontal dashed line representing the constraint threshold 𝑑. Shaded areas denote the standard deviation over five runs. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)**

**Table 4 Comparison of action space and action-correction violations by period for Experiment B (Viol. (%) denotes the percentage of time steps with 𝑎exec**

𝑡 ≠𝑎mask

𝑡 , i.e., environment intervention/correction).

Period Strategy Mean avail. Min Max Viol. (%) Mean agent Mean exec. Diff.

(a) Drawdown B1 99.00 99.00 99.00 21.46 38.71 42.57 −3.86 B2 34.54 21.00 70.00 60.49 29.43 40.80 −11.37 B3 18.32 0.00 59.00 0.00 43.82 43.82 0.00

(b) Flood B1 99.00 99.00 99.00 34.13 59.76 58.62 1.14 B2 20.19 0.00 82.00 3.48 57.89 58.28 −0.39 B3 20.66 0.00 82.00 0.00 58.30 58.30 0.00

(c) Refill B1 99.00 99.00 99.00 78.82 13.55 23.93 −10.38 B2 48.67 0.00 72.00 1.18 24.15 24.41 −0.26 B3 39.98 0.00 82.00 0.00 23.71 23.71 0.00

early-stage trajectory into a low-release region and trapping the policy in an overly conservative local optimum. Although the feasible region later widens and the policy moves back toward the middle of the band, the early over-restriction causes systematic under-release: B2’s actioncorrection violation rate during the drawdown period reaches 60.49%, far higher than B1’s 21.46% (Table 4). This indicates that a partially mis­ specified or overly simplified rule-based mask can be counterproductive in long-horizon operation.

releases are needed to empty storage quickly (Fig. 8(a). B1 (pink) shows many upward-tilting paired lines: the agent outputs smaller releases (mean 38.71) and the environment corrects them upward (mean 42.57). B2 (green) exhibits even larger separations—agent ac­ tions concentrate at low values (mean 29.43) while executed actions are shifted to 40.80—yielding an action-correction violation rate of 60.49% (Table 4). The BaseMask retains releases that are currently feasible but violate future constraints, because failing to release enough water early leaves insufficient capacity for incoming floods. B3 (blue) shows close alignment between agent outputs and executed actions through waterbalance-based filtering. A similarly strong pattern appears in the refill period (11 Sep–31 Oct, Fig. 8(c): B1’s agent concentrates actions near zero for rapid refill, but the environment forces them above 20 to satisfy ecological and navigation flows, resulting in a 78.82% violation rate; B3 again shows zero corrections, with the agent actively selecting actions in the 20–40 range. In the flood season (11 Jun–10 Sep, Fig. 8(b), all three strategies show similar distributions around mid-high releases of about 60. During this period, high inflows impose large release require­ ments and leave relatively limited room for policy divergence regardless of mask type.

B3’s gray feasible band presents a smoother stepped shape and is gen­ erally narrower than B2’s, particularly during the drawdown and refill periods, reflecting further trimming of the action space by water-balance rules. Across training, the trajectory moves from the safety baseline to­ ward the upper feasible boundary and, by the late stage, almost overlaps the gray band. This near-complete alignment indicates that the FullMask not only removes infeasible actions before sampling but also guides the policy toward a restricted yet sufficient feasible region. Relative to the rule-based BaseMask, it therefore offers a more transferable feasibility filter when detailed operating tables are unavailable, provided that the key physical and operational constraints have been explicitly encoded.

Fig. 8 reveals the micro-level mechanisms of the mask across three key periods. The paired-line shifts in these rain-cloud plots are inter­ preted as action-correction events, i.e., 𝑎exec

In this comparison, B1 and B2 represent single-mechanism variants, whereas B3 combines proactive masking with adaptive constrained op­ timization as a two-layer design. Taken together, Table 4 and Figs. 7 and

𝑡 ≠𝑎mask

𝑡 . The contrast is most striking in the drawdown period (1 May–10 June), where large

<!-- page 12 -->

Z. Xie, X. Zhang, W. Xu et al.

**Fig. 6. Training dynamics under different action-mask strategies in Experiment B. Panels report (a) maximum return, (b) generation reward, (c) action adjustment cost, (d) guaranteed-power cost, (e) navigation flow cost, and (f) ecological flow cost for B1 (NoMask), B2 (BaseMask), and B3 (FullMask). Shaded areas denote the standard deviation over five runs.**

**Fig. 7. Panorama of action evolution. Three-dimensional plots show action trajectories across training phases (early/middle/late; see legend) for B1 (NoMask), B2 (BaseMask) and B3 (FullMask). The gray semi-transparent band shows the time-varying feasible action interval, and the overlaid boundary curves indicate its lower and upper bounds 𝑎min(𝑡) and 𝑎max(𝑡). For B1, the band spans the full action-index range (0–99); for B2 and B3, the band is computed by the BaseMask and FullMask, respectively. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)**

8 show that B3 achieves zero action-correction violations in all periods, whereas B2 still exhibits 60.49% violations in drawdown and B1 ranges from 21.46% to 78.82%. Without proactive filtering (B1), broad explo­ ration in the full action space still triggers execution-time interventions despite dual self-regulation; if a rule-based mask is overly restrictive or partially misspecified (B2), early exploration is biased toward con­ servative local optima. By contrast, the FullMask removes infeasible actions before sampling and works with PPO-Lagrangian to keep trajec­ tories within a restricted but sufficiently feasible decision subspace. This

pattern supports the complementarity of proactive filtering and adaptive constrained optimization under the modeled constraints.

4.3 . Experiment C: analysis of non-linear action mappings

Experiment C compares five mapping functions—linear (C1), square (C2), cubic (C3), exponential (C4) and logarithmic (C5)—within the uni­ fied framework (“PPO-Lagrangian + FullMask”) to analyze how action density affects learning.

<!-- page 13 -->

Z. Xie, X. Zhang, W. Xu et al.

**Fig. 8. Period-specific action-execution rain-cloud plots. Sub-figures (a), (b), and (c) correspond to the drawdown, flood, and refill periods. Each plot shows agent actions (left) and executed actions (right) as distributions (half-violin plots) and box plots, with paired lines connecting agent actions to executed actions. Non-flat paired lines indicate action-correction events (i.e., 𝑎exec**

𝑡 ≠𝑎mask

𝑡 ); upward (downward) shifts correspond to the environment increasing (decreasing) the executed release relative to the agent output. Colors denote strategies: pink for B1, green for B2, and blue for B3. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)

**Fig. 9. Training dynamics of five mapping functions. (a) Maximum return; (b) generation reward; (c) action adjustment cost; (d) guaranteed-power cost; (e) navigation flow cost; (f) ecological flow cost. Shaded areas denote the standard deviation over five runs.**

action adjustment cost (−0.09±0.09) and soft constraints. Concentrating actions at high releases (logarithmic mapping) likely contributes to under-sampling in low-release regions and hence poorer learning.

Training dynamics show that action density significantly influences convergence speed. Fig. 9(a) shows distinct learning trajectories. C2 (square) and C3 (cubic) rise quickly and surpass the −2000 return thresh­ old within 50 episodes. In the middle phase, their returns stabilize between −500 and 0. Concentrating action density in low-release regions gives the agent more choices near ecological flows (6,000–10,000 m3/s) and navigation flows (15,000–20,000 m3/s). C1 (linear) has a flatter learning curve and stabilizes around −1000 (Fig. 9(a). Uniform action density results in sparse sampling near boundaries. C4 (exponential) is intermediate. C5 (logarithmic) performs poorly; its return hovers between −5000 and −6000.

Fig. 9(c)–f confirms these patterns. Action adjustment costs for C5 fluctuate widely early in training (generally below −1.3) and only stabi­ lize after 200 episodes. C2 and C3 quickly converge to near zero within 50 episodes. Soft-constraint curves show that C2 and C3 improve navi­ gation and ecological constraints rapidly and stably, reaching near-zero costs, whereas C5 sustains high costs (Fig. 9(e)–f).

Evaluations further verify these findings. Table 6 reports that C2 achieves the highest total energy generation (420.93 TWh), 0.54% higher than C1 (418.68 TWh). C3 ranks second (420.31 TWh). C4 (418.44 TWh) is similar to C1. C5 (411.41 TWh) is significantly lower, down 1.74%. In terms of safety, C2, C3, and C4 achieve zero actioncorrection violations (i.e., no time steps with 𝑎exec

Table 5 reports the final ten-episode statistics and summarizes these differences. C2 ranks first with a return of 371.85 ± 50.85 (Table 5), fol­ lowed by C3 (364.05±58.94). Their standard deviations are smaller than those of other configurations, indicating better convergence stability. C4’s return (327.50±75.27) is better than C1 (244.49±124.31) but clearly lower than C2. C5 has the worst performance. C2 also achieves the high­ est generation reward (410.86 ± 27.72) and the lowest action adjustment cost (−0.01 ± 0.01) (Table 5). C5 performs worst in generation reward,

𝑡 ≠𝑎mask

𝑡 ); C1 has 0.05% minor action-correction violations and C5 has 0.88% (Table 6). Satisfaction rates show that C1, C2, and C4 maintain almost 100% satisfaction of the guaranteed-power, navigation, and ecological require­ ments. C3 has a slight drop of 0.05% in navigation satisfaction. C5

<!-- page 14 -->

Z. Xie, X. Zhang, W. Xu et al.

**Table 5 Summary of training performance for Experiment C (final 10 episodes).**

Metric C1 (Linear) C2 (Square) C3 (Cubic) C4 (Exp.) C5 (Log.)

Maximum return 244.49 ± 124.31 371.85 ± 50.85 364.05 ± 58.94 327.50 ± 75.27 74.79 ± 99.84 Generation reward 397.39 ± 26.98 410.86 ± 27.72 410.43 ± 27.80 404.86 ± 27.02 375.38 ± 30.58 Action adjustment cost −0.02 ± 0.01 −0.01 ± 0.01 −0.02 ± 0.03 −0.01 ± 0.01 −0.09 ± 0.09 Guaranteed-power cost −37.60 ± 29.44 −7.83 ± 8.67 −10.63 ± 12.73 −17.38 ± 16.25 −80.25 ± 25.94 Navigation flow cost −113.80 ± 80.88 −30.14 ± 25.88 −38.79 ± 32.11 −58.78 ± 45.08 −221.46 ± 63.67 Ecological flow cost −0.41 ± 0.47 −0.08 ± 0.14 −0.57 ± 1.19 −0.22 ± 0.29 −2.00 ± 3.30

**Table 6 Comparison of overall performance in evaluation for Experiment C (Violation rate (%) denotes the percentage of time steps with 𝑎exec**

𝑡 ≠𝑎mask

𝑡 , i.e., action-correction events).

Metric C1 C2 C3 C4 C5

Total energy generation (TWh) 418.68 420.93 420.31 418.44 411.41 Mean action 25.77 43.00 55.00 31.78 14.54 Violation rate (%) 0.05 0.00 0.00 0.00 0.88 Guaranteed-power satisfaction (%) 100.00 100.00 100.00 100.00 97.75 Navigation satisfaction (%) 100.00 100.00 99.95 100.00 97.75 Ecological satisfaction (%) 100.00 100.00 100.00 100.00 99.56

has clearly lower satisfaction rates (97.75% for guaranteed-power and navigation, 99.56% for ecology) and a lower mean action (14.54), in­ dicating overly conservative behavior. Taken together, Table 6 makes the single-reservoir evaluation scope explicit: it reports not only en­ ergy generation, but also action-correction feasibility and satisfaction of the guaranteed-power, navigation, and ecological requirements that are explicitly modeled in this study. Flood-season operating safety is not reported here as a separate optimization metric; instead, it enters through the feasibility-preserving water-level/release constraints and the resulting violation statistics under the modeled operating rules.

protects execution-time feasibility, the dual variable regulates long-run soft-constraint pressure, and non-linear action mapping improves con­ trol authority in the low-release regime, where ecological, navigation, and guaranteed-power constraints are most sensitive. For reservoir man­ agement, credible decision-support use therefore depends on embedding safety simultaneously in feasible-action generation, policy learning, and action-space design.

This finding complements and extends recent SafeRL studies in water resources. Recent DRL-based reservoir operation studies have typically adopted single-mechanism constraint treatments or reward-shaping for­ mulations rather than explicitly layered safety architectures (Kåge et al., 2025; Xu et al., 2025). As the correction-based and fixed-penalty base­ lines in the present study illustrate, post-hoc constraint projection can introduce an issue/executed-action mismatch that weakens policy credit assignment, while fixed penalties require manual tuning that cannot adapt across heterogeneous constraints. The present ablation evidence shows that the Lagrangian dual mechanism mitigates both limitations in the tested setting. This aligns with broader SafeRL theory (Stooke et al., 2020; Liu et al., 2021), yet its behavior has received limited reservoirspecific evaluation in long-horizon operation with multiple interacting physical constraints. Meanwhile, existing action-masking applications in related domains (Rizvi and Boyle, 2024; Wang et al., 2024) have focused on static or combinatorial action spaces, whereas the FullMask devel­ oped here operates on a continuously time-varying feasible set driven by water-balance physics, demonstrating that proactive filtering can be extended to dynamic, physically coupled constraint settings.

Fig. 10 presents five-year time series of water level and release. All mappings maintain the normal annual rhythm with mean year-end levels around 172 m. C1–C4 show similar high-flow release patterns during the flood season; C2 and C3 have slightly smaller fluctuations during low release times. C5 exhibits systematically higher releases with larger refill-period fluctuations, leading to lower year-end water levels (mean 171.60 m with an 8.1 m range, versus 172.44–172.60 m and 2–3 m for other mappings).

These results indicate that resolution near low-release constraint boundaries matters. Linear mapping allocates fewer actions there, whereas square and cubic mappings densify the critical region and provide richer gradient feedback. However, more density is not al­ ways better: C3 remains competitive, yet its denser low-release spacing slightly worsens navigation cost relative to C2 (−38.79 vs. −30.14, Table 5) and becomes less stable at higher discretization resolutions, where its navigation satisfaction drops to 87.12% at 𝑁= 150 in the Supplementary Material. Together with the stress-test comparison re­ ported in the Supplementary Material, these results suggest that the square mapping offers the best balance between low-release precision and high-release flexibility in this case.

Relative to representative penalized-PPO, CPO-type, adaptiveLagrangian, and masking-only approaches, the present framework com­ bines pre-sampling feasibility filtering with adaptive dual adjustment in a lightweight controller suited to the current discrete-action reser­ voir setting (Zhang et al., 2022; Achiam et al., 2017; Stooke et al., 2020; Huang and Ontañón, 2022). An expanded literature-level posi­ tioning of these representative families is provided in Supplementary Material Section S8. We additionally compared the final configura­ tion with a POA-style deterministic planning baseline under the same 1460-day evaluator inflow, equal-weight objective, modeled constraints, and square-mapped discrete action representation. Both methods sat­ isfied the modeled guarantees with zero action-correction violations, while the two-layer SafeRL controller achieved slightly higher gen­ eration together with higher mean storage and lower spill discharge (Supplementary Material Section S9). This comparison provides one aligned cross-paradigm reference for the present case, but it does not imply universal superiority over broader SafeRL or reservoir-operation

## 5 . Discussion and outlook

5.1 . Integrated insight

The main implication of this study is that safe long-horizon reser­ voir control cannot be reduced to a single mechanism (Gu et al., 2024; Wachi et al., 2024; Choi et al., 2025). In the Three Gorges case, adap­ tive Lagrangian optimization improves the safety–performance tradeoff, but the clearest gains emerge only when it is combined with a physically consistent proactive filter and an action representation that allocates resolution where constraints are most active. The resulting picture is operational rather than purely algorithmic: the action mask

<!-- page 15 -->

Z. Xie, X. Zhang, W. Xu et al.

**Fig. 10. Time series of reservoir operation under five representative hydrological years (from wettest to driest: P5, P25, P50, P75, P95). The blue line denotes water level (left axis), purple line denotes release (right axis), and gray line denotes inflow (right axis). Red dots indicate year-end water levels. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)**

families, whose fully fair benchmarking would still require harmonized forecast assumptions, information availability, objective definitions, and offline-versus-closed-loop execution protocols (Yeh, 1985; Labadie, 2004). The present case study therefore combines three modeled compo­ nents: direct maximization of hydropower generation, explicit soft op­ erational requirements for ecology/navigation/guaranteed power, and a hard feasibility envelope for flood-season operating safety implemented through water-level/release constraints and spill routing. Coordinated multi-reservoir balancing is not evaluated here and remains a future extension rather than a demonstrated capability.

the Xiluodu and Xiangjiaba reservoirs provide evidence at two scales: dry-to-wet regime diversity within one reservoir, and cross-reservoir applicability on additional independent single-reservoir systems. Across reservoirs, the main changes are the physical parameterization and soft-constraint specification—for example, the stage–storage curve 𝑓𝑉 (Eq. 4), release–capacity limits, time-varying operating bounds, and the thresholds associated with navigation, ecology, and guaranteed-power output (Yeh, 1985; Labadie, 2004). Different operational priorities can likewise be handled by adjusting the soft-constraint terms and letting the Lagrangian multipliers rebalance safety versus performance dur­ ing training. In this sense, the current evidence supports portability by re-parameterization and retraining rather than direct model reuse, zero-shot transfer, or universal performance stability across all hy­ drological regimes. The BaseMask (Appendix A) remains optional and reservoir-specific, and can be simplified or omitted when expert rules are incomplete or unavailable.

From a practical deployment perspective under the modeled con­ straints, the FullMask can serve as a model-based feasibility checker that intercepts agent outputs before they reach the dispatch system while re­ maining compatible with existing rule-based operating procedures. The Lagrangian mechanism allows operators to express soft-constraint pri­ orities through thresholds and cost definitions, providing a structured basis for retuning when requirements change. However, the framework can enforce only the constraints that are explicitly encoded in the state, mask, and cost specification. The zero action-correction violation rate achieved by the full framework (B3) in the baseline evaluation is there­ fore encouraging for decision-support use on the held-out representative years, but only with respect to the modeled feasible region rather than all possible real-world contingencies.

5.3 . Boundary conditions and future directions

The present results should nevertheless be read within clear bound­ ary conditions. First, the safety guarantee is model-consistent rather than probabilistic: the action mask enforces feasibility with respect to the modeled physical constraints under deterministic forecast inputs, not under arbitrary stochastic inflow uncertainty. More fundamen­ tally, both safety layers rely on the correctness and completeness of the encoded constraint set. Real reservoir operation may involve un­ certain, time-varying, or partially observed requirements—including emergency flood-control rules, downstream ecological demands, tem­ porary navigation restrictions, or operator interventions—that are not fully represented by a fixed CMDP specification (Wachi et al., 2024; Kahn et al., 2017; Xu et al., 2025; Liu et al., 2025). Under such con­ ditions, the framework can protect only against the encoded subset of constraints, and deployment reliability may degrade if important

5.2 . Cross-reservoir applicability

Although the Three Gorges Reservoir is used as a representative longhorizon, multi-constraint case, the proposed framework is not tied to a single reservoir layout. Its reusable core is the CMDP formulation together with state-driven masking and PPO-Lagrangian optimization. Together with the held-out P95/P75/P50/P25/P5 evaluation years in the main manuscript, the supplementary retrain-and-evaluate results on

<!-- page 16 -->

Z. Xie, X. Zhang, W. Xu et al.

rules are missing, outdated, or misparameterized. Conservative masking margins, periodic parameter calibration and rule updating, stress testing, and human-in-the-loop override therefore remain important practical safeguards. The Supplementary Material provides additional evidence under adverse inflow perturbations and an evaluation-only probe under perturbed current- and future-inflow inputs. These checks character­ ize the robustness of a fixed trained policy under the tested pertur­ bations, but they do not constitute forecast-aware training, explicit uncertainty quantification, or an adaptation mechanism for long-term non-stationary hydroclimatic change. The current controller also relies on a compact Markov-style state description rather than an explicit recurrent sequence encoder, so longer-lag temporal effects are repre­ sented through state design and physical transitions rather than learned memory. Addressing such non-stationarity would require periodically updating the inflow/scenario distribution and recalibrating or retrain­ ing the policy, potentially using warm starts under evolving climate conditions (Negm et al., 2024; Kåge et al., 2025).

safety ablations under a transparent state design. Richer normalization schemes and higher-dimensional multi-reservoir representations remain meaningful next steps.

From a computational perspective, the added cost of the two safety layers remains moderate for the present offline single-reservoir case rather than changing the order of magnitude of the training workflow. Relative to the fixed-penalty baseline, PPO-Lagrangian increases the mean training time by about 5 min per run while leaving evaluation time nearly unchanged. Relative to NoMask, the FullMask adds about 3.7 min of training time and about 0.6 s of evaluation time, mainly be­ cause the feasible action interval must be recomputed at every step. In contrast, the choice among the five action mappings changes runtime only marginally. These costs are acceptable in the current offline setting, but they would rise with larger action spaces, more elaborate mask logic, or coordinated multi-reservoir control, where both feasibility checking and tuning effort would become more demanding.

Finally, uncertainty and interpretability are addressed here through empirical evidence rather than dedicated auxiliary modules. Multiseed variability bands, paired bootstrap confidence intervals, and stress-test evaluations under perturbed inflows therefore provide em­ pirical variability and robustness evidence for the fixed-policy ex­ periments, rather than predictive hydrological uncertainty estimates. Policy behavior is interpreted mainly through feasible-action regions, action-correction patterns, and dual-variable dynamics. More generic activation-maximization analyses are not pursued here because un­ constrained maximizers need not correspond to physically realizable reservoir states under continuity and operating constraints. The study does not claim formal global optimality, approximation guarantees, or a standalone uncertainty-quantification framework under deep nonconvex function approximation. These boundaries point naturally to future work on uncertainty-aware SafeRL, broader cross-system evalua­ tion, and larger-scale coordinated reservoir operation (Gu et al., 2024; Wachi et al., 2024; Kahn et al., 2017).

Second, the quantitative optima observed here—such as the pre­ ferred discretization pattern or the precise safety–performance trade-off point—remain reservoir-specific. The current evidence therefore sup­ ports neither universal hyperparameter optimality nor universal hydro­ logical generalization; it is limited to the evaluated dry-to-wet represen­ tative years in the Three Gorges case and to the supplementary retrainand-evaluate demonstrations on Xiluodu and Xiangjiaba. Broader eval­ uations on additional systems and targeted priority-shift tests (e.g., stricter ecological or navigation requirements) would strengthen the evidence for cross-system applicability. Extending the framework to coordinated multi-reservoir or basin-scale operation would require ad­ ditional coupling states, joint release decisions, and likely hierarchical or decomposed control structures (Labadie, 2004; Liu et al., 2025). A practical route is to preserve the local physics-consistent mask at the reservoir level, introduce only the most decision-relevant coupling variables into the policy state, and combine this parsimonious represen­ tation with hierarchical or decomposed coordination. Transfer learning or warm-start initialization across related reservoirs may further reduce training costs in such larger systems.

## 6 . Conclusions

This study proposes a two-layer SafeRL framework for multiconstraint reservoir operation and evaluates three key design elements— constraint handling, action masking, and non-linear action mapping—in the Three Gorges long-term operation case. The main findings are as follows:

Third, the controlled ablations intentionally keep the underlying task reward and constraint-cost definitions fixed so that mechanism effects can be isolated. Alternative reward definitions or cost weightings may therefore lead to different performance–safety trade-offs. The default coefficient setting 𝛽𝑖= 1.0 is used as a neutral baseline for the constraintcost components, while application-specific coefficient tuning remains an important engineering extension. In practical reservoir operation, however, such coefficients encode a calibration of competing opera­ tional priorities rather than a physically unique optimum, and different hydrological, institutional, or stakeholder settings may justify differ­ ent trade-off choices (Yeh, 1985; Labadie, 2004; Rheinheimer et al., 2016; Liu et al., 2025). The equal-coefficient setting adopted here should therefore be read only as a controlled reference for mechanism-level comparison, not as a deployment-ready calibration. The adaptive dual multipliers adjust penalty pressure given the specified cost components, coefficients, and acceptable thresholds; they do not replace the engineer­ ing calibration of these quantities. The multiplier-related defaults should likewise be interpreted as reproducible study settings rather than univer­ sally optimal choices. The supplementary three-seed sensitivity analysis indicates a usable stability margin around the adopted Layer-2 defaults, but also shows identifiable failure modes: overly aggressive dual learn­ ing rates degrade the safety–performance trade-off, and looser violation thresholds permit occasional issued/executed-action mismatches. The stable tuning range may therefore shift across reservoirs, objective prior­ ities, and state representations. The current implementation also adopts a compact physics-informed state design with lightweight physical normalization because each policy input must remain directly inter­ pretable for real-time mask construction. The present study therefore does not benchmark automated feature-extraction pipelines or dedicated predictive-uncertainty modules, focusing instead on mechanism-level

(1) Among the tested mechanisms, the Lagrangian dual method

shows the most favorable overall constraint-handling perfor­ mance in this setting. By adaptively adjusting the constraint weight, it increases generation reward by 4.9% and reduces the total absolute constraint cost by 71.5% relative to the correctionbased baseline. (2) Among the tested masking strategies, the FullMask is the one

that achieves zero action-correction violations in the baseline evaluation under the modeled constraints. As a proactive safety filter, it aligns agent outputs with the modeled feasible region and works together with Lagrangian optimization to improve feasibility during training and evaluation. (3) As a complementary enhancement to the two-layer architec­

ture, non-linear action mappings further improve learning effi­ ciency. By concentrating actions in critical low-release regions, the square mapping yields a 0.54% increase in total energy generation over the linear baseline while maintaining zero actioncorrection violations in the baseline evaluation.

Overall, in the Three Gorges Reservoir case, the two-layer safety architecture provides a practically relevant SafeRL workflow for modelconsistent decision support under the modeled operating conditions. The controlled ablations clarify the distinct roles of adaptive constrained

<!-- page 17 -->

Z. Xie, X. Zhang, W. Xu et al.

optimization, proactive safety filtering, and action-space design in longhorizon reservoir operation, and provide a methodological reference for safety-critical water-resources decision problems.

Appendix B . Generic physical constraints for reservoir operation (FullMask)

Unlike the BaseMask, which encodes reservoir-specific operating rules, the FullMask is constructed from transferable physics-based con­ straints. Table B.8 summarizes the constraint families and corresponding formulations used to construct the FullMask in this study.

CRediT authorship contribution statement

Zaichao Xie: Writing – original draft, Software, Methodology, Conceptualization. Xiaoli Zhang: Writing – review & editing, Supervision. Wei Xu: Resources, Project administration. Guoguo Lin: Resources. Dong Li: Resources. Shuncai Zhang: Validation, Formal analysis. Hongyan Chen: Visualization, Formal analysis. Sheng Yang: Visualization, Formal analysis.

Table B.8 General physical constraints for the FullMask.

Constraint type Formula/Condition Physical meaning Period

𝑉𝑡−𝑉limit,𝑡

𝑄out,𝑡≥𝑄in,𝑡+

High storage limit

Δ𝑡 Prevent exceeding storage upper limit.

All

𝑉𝑡−𝑉low,𝑡

𝑄out,𝑡≤𝑄in,𝑡+

Low storage protection

Δ𝑡 Prevent dropping below lower limit.

All

Declaration of generative AI and AI-assisted technologies in the writing process

Dry-season flow 𝑄out,𝑡≤2𝑄in,𝑡 Maintain high water level.

Jan–Mar, Nov–Dec Release change rate

During the preparation of this work, the authors used ChatGPT (OpenAI) to improve the language clarity, grammar, and readability of the manuscript. After using this tool, the authors reviewed and edited the content as needed and take full responsibility for the content of the published article.

𝑄out,𝑡≤2𝑄out,𝑡−1 Ensure smooth operation.

All

Level exceedance If ℎ𝑡> ℎmax,𝑡, 𝑄out,𝑡= 𝑄max

Emergency release for flood safety.

All

Appendix C . Core hyperparameters of the algorithms

Declaration of competing interest

**Table C.9 details the core hyperparameter settings used in the reinforcement learning experiments.**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

**Table C.9 Core hyperparameter settings.**

Acknowledgements

Category Name Symbol/Code Value

This work was supported by the National Key R&D Program of China (2023YFC3006605), the Training Program for Young Backbone Teachers in Henan Higher Education Institutions, the Chongqing Transportation Science and Technology Project (CQJT-CZKJ2025-08), and the Chongqing Jiaotong University Graduate Research Innovation Project (2025B0018).

Environment Episode MAX_EPISODE_STEP 365 × 4 Training Parallel environments – 6 Training rounds – 50 Cumulative episodes – 6 × 50 = 300 Environment Action dim ACTION_SHAPE 100 Rewards All coefficients – 1.0 PPO Config Learning rate LR 0.001 (Adam) Discount factor 𝛾 0.99 Generalized advan­ tage estimation (GAE) parameter

Appendix A . Operating rules for the reservoir (BaseMask)

𝜆gae 0.95

Table A.7 lists the reservoir-specific operating rules used in Experiment B for the BaseMask. These rules are derived from the dis­ patch regulations of the Three Gorges Reservoir issued by the Changjiang Water Resources Commission and guide release decisions during the key refill period from August to October. Supplementary constraints:

Clip ratio 𝜖 0.2 Updates per cycle UPDATE_NUM 10 Entropy weight entropy_weight 0.016 Lagrangian Threshold 𝑑 0.2 Dual learning rate 𝛼𝜆 0.01 Init multiplier 𝜆0 1.0 Update interval 𝐾 4 Cost normalizer 𝑍 1.0 Tolerance threshold 𝜖tol 0.05 Upper bound (optional) 𝜆max — (not used) Mask Perturbation 𝜖adv 0.05

• Navigation guarantee: Jun–Dec, min release ≥ navigation re­ quirement. • Ramping rates: Refill period Δℎ≤3.0 m/d; Flood season |Δℎ| ≤ 2.0 m/d; Dry season |Δℎ| ≤0.6 m/d.

State normalization details. The water-level-related variables (ℎ𝑡, ℎmin,𝑡, ℎmax,𝑡) are mapped to [0, 1] using (ℎ−ℎglobal

min )∕(ℎglobal

max −ℎglobal

min ), where the bounds correspond to the absolute dead water level and design flood level. The inflow-related variables (𝑄in,𝑡, 𝑄future,𝑡) are

Table A.7 Specific operating rules for the Three Gorges reservoir (BaseMask).

Period Inflow (𝑄in, m3/s)

Release (𝑄out, m3/s)

Explanation

scaled as 𝑄∕𝑄global

max , where 𝑄global

max represents the historical maximum flood peak. The periodic encoding 𝐞𝑡 is already bounded within [−1, 1]. Because these transformations use fixed physical reference scales and are applied variable-wise, they preserve the original daily sequence order and within-sequence temporal variation rather than removing hydrologic persistence. This lightweight physical normalization keeps heterogeneous state factors on comparable scales while remaining fully consistent with the methodological state definition. Network architecture and training implementation details. In addi­ tion to the scalar hyperparameters summarized in Table C.9, the policy

August > 18, 000 ≥18, 000 Maintain min release to prevent rapid level rise. ≤18, 000 = 𝑄in Release equals inflow (open gate). September > 10, 000 ≥10, 000 Ensure basic release capacity. (8000, 10000] = 𝑄in Balance inflow and release. ≤8, 000 = 8, 000 Fix release at 8,000, begin storing. October > 8, 000 ≥8, 000 Maintain min release. ≤8, 000 = 𝑄in Maintain balance.

<!-- page 18 -->

Z. Xie, X. Zhang, W. Xu et al.

**Table C.10 Wall-clock runtime statistics (mean ± std over five ran­ dom seeds). Training denotes the wall-clock time to finish 50 rounds with 6 parallel environments (300 cumula­ tive episodes); evaluation denotes the time of a single evaluation episode at the end of training.**

**Table D.11 Characteristic water levels and corresponding storage for the Three Gorges case.**

Name Water level (m) Storage (108 m3)

Check flood level 180.4 450.44 Design flood level 175.0 393.00 Normal pool level 175.0 393.00 Flood-control limited water level 145.0 171.50 Dry-season drawdown low water level 155.0 228.00

Configuration Training (min) Evaluation (s)

```math
A1 (Correction)
18.77 ± 0.11
4.04 ± 0.12
A2 (Penalty)
19.22 ± 0.02
4.39 ± 0.04
A3 (PPO-Lagrangian)
24.20 ± 0.02
4.45 ± 0.14
```

```math
B1 (NoMask)
24.20 ± 0.02
4.45 ± 0.14
B2 (BaseMask)
28.28 ± 1.18
5.13 ± 0.56
B3 (FullMask)
27.89 ± 0.11
5.03 ± 0.09
```

**Table D.12 Rated-discharge breakdown of all generating units in the Three Gorges case.**

Powerhouse Unit count

Rated head (m)

Rated discharge per unit (m3/s)

Subtotal (m3/s)

C1 (Linear) 27.89 ± 0.11 5.03 ± 0.09 C2 (Square) 28.12 ± 0.04 5.18 ± 0.22 C3 (Cubic) 28.14 ± 0.04 5.04 ± 0.05 C4 (Exp.) 28.17 ± 0.03 4.99 ± 0.08 C5 (Log.) 28.51 ± 1.06 5.28 ± 0.32

Left-bank powerhouse (VGS) 7 80.6 995.6 6969.2 Left-bank powerhouse (ALSTOM)

## 7 80.6 991.8 6942.6

Right-bank powerhouse (Dongfang)

## 4 85.0 928.5 3714.0

Right-bank powerhouse (ALSTOM)

## 4 80.6 1000.0 4000.0

uses an actor–critic model with a shared multilayer perceptron (MLP) encoder and separate actor/critic heads. The encoder hidden-size list is [512, 512, 256]; both the actor head and critic head use one addi­ tional hidden layer of size 256 before the output layers. The experiments adopt a discrete action space with action_shape=100. PPO optimiza­ tion uses multiple epochs per data collection (epoch_per_collect=10), advantage normalization (adv_norm=True) and value normalization (value_norm=True). The complete training configuration files are provided in a public repository: https://github.com/lovemevol/PPOLagrangian-Paper. Training data scale and on-policy buffering. The PPO implementa­ tion is on-policy and maintains only a rollout buffer that stores the most recent trajectories collected for policy updates (i.e., no experience replay is used). The trainable quantities are the standard actor–critic network parameters learned from the rollout data. Each training run consists of 50 collection-update rounds with 6 parallel 4-year episodes per round, equivalent to 300 cumulative episodes and 438,000 environ­ ment steps (Table C.10), providing a concrete reference for the data scale and memory footprint of the training procedure.

Right-bank powerhouse (Harbin)

## 4 85.0 928.5 3714.0

Underground powerhouse (Dongfang)

## 2 85.0 928.5 1857.0

Underground powerhouse (ALSTOM)

## 2 80.6 1000.0 2000.0

Underground powerhouse (Harbin)

## 2 85.0 928.5 1857.0

Power supply station (Harbin)

## 2 85.0 66.81 133.62

Total 34 + 2 – – 31,187.42

Appendix E . Supplementary data

Supplementary data for this article can be found online at doi:10. 1016/j.jhydrol.2026.135694.

Data availability

The historical inflow data used in this study were obtained from the Changjiang Water Resources Commission Hydrological Yearbook and are subject to institutional access restrictions due to operational security considerations; access to the original records therefore fol­ lows the Commission’s data-governance procedures rather than open redistribution through this paper. Key operational rules, physical con­ straint parameters, and engineering-parameter clarifications used in the experiments are provided in Appendices A–D, while additional robust­ ness, cross-reservoir, and trajectory-diagnostic results are provided in the Supplementary Material. The public repository https://github.com/ lovemevol/PPO-Lagrangian-Paper contains the full DRL training con­ figuration files, released supplementary result tables, and a README describing the public reproducibility scope. Trained model checkpoints and additional experiment outputs can be provided upon reasonable request.

Computational environment and wall-clock cost

To improve reproducibility, this study reports the computational environment and the wall-clock runtime (training and evaluation) aggre­ gated over five random seeds. Table C.10 summarizes the training time for 50 rounds with 6 parallel environments (300 cumulative episodes; 438,000 environment steps) and the time required for one evaluation episode at the end of training.

Appendix D . Engineering parameters for the three gorges case

To improve the traceability of the engineering parameters discussed in Section 3.1, this appendix summarizes the characteristic water lev­ els and the generating-unit rated-discharge breakdown used in the Three Gorges implementation. The characteristic water levels follow the Preliminary Design Report of the Changjiang Three Gorges Water Conservancy Project; the generating-unit data follow the Ministry of Water Resources regulation document Dispatching Regulations for the Three Gorges (Normal Operation Period)–Gezhouba Cascade Hydropower Project. The latter is also the source used to compute the maximum aggregate turbine-generation discharge reported in the manuscript (Tables D.11 and D.12).

## References

Achiam, J., Held, D., Tamar, A., Abbeel, P., 2017. Constrained policy optimization. In: Proceedings of the 34th International Conference on Machine Learning. PMLR, pp. 22–31. Altman, E., 1999. Constrained Markov Decision Processes. Routledge, New York, https: //doi.org/10.1201/9781315140223 Castelletti, A., Galelli, S., Restelli, M., Soncini-Sessa, R., 2010. Tree-based reinforcement learning for optimal water reservoir operation. Water Resour. Res. 46, W09507. https: //doi.org/10.1029/2009WR008898 Chen, H., Zou, J., Wang, X., Lv, P., Tan, Z., Cheng, L., Wei, Q., 2023. Inducing factors and deformation mechanism of the zhangjiacitang landslide in the three gorges reservoir area. Sci. Rep. 13, 15115. https://doi.org/10.1038/s41598-023-40186-6 Choi, J.J., Aloor, J.J., Li, J., Mendoza, M.G., Balakrishnan, H., Tomlin, C., 2025. Resolving Accordingly, the value reported in Section 3.1 (approximately 31,187 m3/s) refers to the maximum aggregate turbine-generation discharge rather than to the total flood-release or dam-spill capacity. conflicting constraints in multi-agent reinforcement learning with layered safety. In:

<!-- page 19 -->

Z. Xie, X. Zhang, W. Xu et al. Proceedings of Robotics: Science and Systems (RSS XXI), https://doi.org/10.15607/ RSS.2025.XXI.094. paper 094. Dadashi, R., Hussenot, L., Vincent, D., Girgin, S., Raichuk, A., Geist, M., Pietquin, O., 2022. Moghaddam, H.K., Rahimzadeh Kivi, Z., Abtahizadeh, E., Abolfathi, S., 2025. Sustainable water allocation under climate change: Deep learning approaches to predict drinking water shortages. J. Environ. Manag. 385, 125600. https://doi.org/10.1016/j.jenvman. 2025.125600 Munos, R., Moore, A., 2002. Variable resolution discretization in optimal control. Mach. Continuous control with action quantization from demonstrations. In: Proceedings of the 39th International Conference on Machine Learning. PMLR, pp. 4537–4557, https: //proceedings.mlr.press/v162/dadashi22a.html. Donnelly, J., Abolfathi, S., Pearson, J., Chatrabgoun, O., Daneshkhah, A., 2022. Gaussian Learn. 49, 291–323. https://doi.org/10.1023/A:1017992615625 Negm, A., Ma, X., Aggidis, G., 2024. Deep reinforcement learning challenges and oppor­ process emulation of spatio-temporal outputs of a 2D inland flood model. Water Res. 225, 119100. https://doi.org/10.1016/j.watres.2022.119100 Fujimoto, S., Meger, D., Precup, D., 2019. Off-policy deep reinforcement learning with­ tunities for urban water systems. Water Res. 253, 121145. https://doi.org/10.1016/j. watres.2024.121145 Rheinheimer, D.E., Liu, P., Guo, S., 2016. Re-operating the Three Gorges Reservoir for envi­ out exploration. In: Proceedings of the 36th International Conference on Machine Learning. PMLR, pp. 2052–2062, https://proceedings.mlr.press/v97/fujimoto19a. html. Gosden, J., Dutton, T., Hart, D., 2014. Guide to drawdown capacity for reservoir safety ronmental flows: a preliminary assessment of trade-offs. River Res. Appl. 32, 257–266. https://doi.org/10.1002/rra.2866 Rizvi, D., Boyle, D., 2024. Multi-agent reinforcement learning with action masking for uav-enabled mobile communications. IEEE Trans. Mach. Learn. Commun. Netw.. https: //doi.org/10.1109/TMLCN.2024.3367552 Rosita, H., Juwono, P.T., Limantara, L.M., Yuliani, E., 2025. A predictive model for es­ and emergency planning. Dams and Reservoirs 24, 134–135. https://doi.org/10.1680/ jdare.14.00023 Gu, S., Yang, L., Du, Y., Chen, G., Walter, F., Wang, J., Knoll, A., 2024. A review of safe timating reservoir impounding time based on the net inflow and storage volume. J. Hum. Earth Future 6, 332–345. https://doi.org/10.28991/HEF-2025-06-02-06 Satija, H., Amortila, P., Pineau, J., 2020. Constrained markov decision processes via back­ reinforcement learning: Methods, theories, and applications. IEEE Trans. Pattern Anal. Mach. Intell. 46, 11216–11235. https://doi.org/10.1109/TPAMI.2024.3457538 Hou, Y., Liang, X., Lv, M., Yang, Q., Li, Y., 2023a. Subtask-masked curriculum learning for ward value functions. In: Proceedings of the 37th International Conference on Machine Learning. PMLR, pp. 8502–8511. Schmitt, R.J.P., Rosa, L., 2024. Dams for hydropower and irrigation: trends, challenges, reinforcement learning with application to uav maneuver decision-making. Eng. Appl. Artif. Intell. 125, 106703. https://doi.org/10.1016/j.engappai.2023.106703 Hou, Y., Liang, X., Zhang, J., Yang, Q., Yang, A., Wang, N., 2023b. Exploring the use of and alternatives. Renew. Sustain. Energy Rev. 199, 114439. https://doi.org/10.1016/ j.rser.2024.114439 Sinclair, S.R., Wang, T., Jain, G., Banerjee, S., Yu, C.L., 2020. Adaptive discretization invalid action masking in reinforcement learning: a comparative study of on-policy and off-policy algorithms in real-time strategy games. Appl. Sci. 13, 8283. https://doi. org/10.3390/app13148283 Huang, S., Ontañón, S., 2022. A closer look at invalid action masking in policy gradient for model-based reinforcement learning. In: Larochelle, H., Ranzato, M., Hadsell, R., Balcan, M.F., Lin, H.T. (Eds.), Advances in Neural Information Processing Systems 33. Curran Associates, Inc, pp. 3659–3671. Stooke, A., Achiam, J., Abbeel, P., 2020. Responsive safety in reinforcement learning algorithms. In: Proceedings of the 35th International FLAIRS Conference, https://doi. org/10.32473/flairs.v35i.130584, p. 130584. Igityan, H., Elbakyan, E., Hakobyan, H., Petrosyan, V., Karamyan, R., Gevorgyan, A., 2025. by pid lagrangian methods. In: Proceedings of the 37th International Conference on Machine Learning. PMLR, pp. 9133–9143. Thepjunthra, W., Mairaing, W., Jinakulwipat, M., Chalermpornchai, T., Kunsuwan, B., Methodology of studies for construction of water reservoir dams in countries prone to landslide hazard. Civ. Eng. J. 11, 279–289. https://doi.org/10.28991/CEJ-2025-01101-016 Jian, W., Xu, Q., Yang, H., Wang, F., 2014. Mechanism and failure process of qianjiangping

2025. Piezometer time-lag and pore pressure ratio for identification of dam internal erosion. Civ. Eng. J. 11, 1162–1179. https://doi.org/10.28991/CEJ-2025-011-03-019 Wachi, A., Shen, X., Sui, Y., 2024. A survey of constraint formulations in safe reinforce­ landslide in the three gorges reservoir, china. Environ. Earth Sci. 72, 2999–3013. https: //doi.org/10.1007/s12665-013-3021-6 Jiang, Q., Li, J., Sun, Y., Huang, J., Zou, R., Ma, W., Guo, H., Wang, Z., Liu, Y., 2024. ment learning. In: Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence, Survey Track, pp. 8262–8271, https://doi.org/10.24963/ijcai. 2024/913 Wang, Z., Li, X., Sun, L., Zhang, H., Liu, H., Wang, J., 2024. Learning state-specific ac­ Deep-reinforcement-learning-based water diversion strategy. Environmental Science & Ecotechnology 17, 100298. https://doi.org/10.1016/j.ese.2023.100298 Kahn, G., Villaflor, A., Pong, V., Abbeel, P., Levine, S., 2017. Uncertainty-aware rein­ tion masks for reinforcement learning. Algorithms 17, 60. https://doi.org/10.3390/ a17020060 Xu, J., Lin, Y., 2024. Energy management for hybrid electric vehicles using safe forcement learning for collision avoidance. In: Proceedings of the 2017 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 2572–2579, https://doi.org/10.1109/IROS.2017.8206074 Kåge, L., Milić, V., Andersson, M., Wallén, M., 2025. Reinforcement learning applica­ hybrid-action reinforcement learning. Mathematics 12, 663. https://doi.org/10.3390/ math12050663 Xu, W., Meng, F., Guo, W., Li, X., Fu, G., 2021. Deep reinforcement learning for optimal tions in water resource management: a systematic literature review. Front. Water 7, 1537868. https://doi.org/10.3389/frwa.2025.1537868 Labadie, J.W., 2004. Optimal operation of multireservoir systems: State-of-the-art review. hydropower reservoir operation. J. Water Resour. Plan. Manag. 147, 04021045. https: //doi.org/10.1061/(ASCE)WR.1943-5452.0001409 Xu, J., Qiao, J., Sun, Q., Shen, K., 2025. A deep reinforcement learning framework for J. Water Resour. Plan. Manag. 130, 93–111. https://doi.org/10.1061/(ASCE)07339496(2004)130:2(93) Li, Z., Wang, M., Zhao, H., 2025. Vehicle lateral control based on augmented lagrangian cascade reservoir operations under runoff uncertainty. Water 17, 2324. https://doi. org/10.3390/w17162324 Yeh, W.W.G., 1985. Reservoir management and operations models: A state-of- ddpg algorithm. Appl. Sci. 15, 5463. https://doi.org/10.3390/app15105463 Liu, Y., Halev, A., Liu, X., 2021. Policy learning with constraints in model-free rein­ the-art review. Water Resour. Res. 21, 1797–1818. https://doi.org/10.1029/ WR021i012p01797 Zhang, L., Shen, L., Yang, L., Chen, S., Yuan, B., Wang, X., Tao, D., 2022. Penalized forcement learning: A survey. In: Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence (IJCAI-21), pp. 4508–4515, https://doi.org/10. 24963/ijcai.2021/614 Liu, J., Zhang, H., Zhang, L., Wei, J., Wu, D., Wang, C., Yang, S., Hu, J., 2025. Analysis proximal policy optimization for safe reinforcement learning. In: Proceedings of the Thirty-First International Joint Conference on Artificial Intelligence (IJCAI-22), pp. 3716–3722, https://doi.org/10.24963/ijcai.2022/516 Zheng, S., 2016. Reflections on the Three Gorges Project since its operation. Engineering of dynamic risk transmission in cascade reservoirs driven by multi-objective optimal operation. Sustainability 17, 9623. https://doi.org/10.3390/su17219623 Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A.A., Veness, J., Bellemare, M.G., Graves, 2, 389–397. https://doi.org/10.1016/J.ENG.2016.04.002 Zheng, J., Jia, R., Liu, S., He, D., Li, K., Wang, F.Y., 2023. Safe reinforcement learning A., Riedmiller, M., Fidjeland, A.K., Ostrovski, G., et al., 2015. Human-level control through deep reinforcement learning. Nature 518, 529–533. https://doi.org/10.1038/ nature14236 for industrial optimal control: a case study from metallurgical industry. Inf. Sci. 649, 119684. https://doi.org/10.1016/j.ins.2023.119684
