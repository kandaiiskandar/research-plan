# ProSh - Probabilistic Shielding for Model-free Reinforcement Learning

> **Source PDF:** `ProSh - Probabilistic Shielding for Model-free Reinforcement Learning.pdf` · **Pages:** 3 · Converted by `scripts/paper2md.py` from the original PDF. **Equations are extracted glyph-by-glyph and may be mangled — check the PDF before quoting any formula.**

<!-- page 1 -->

ProSh: Probabilistic Shielding for Model-free Reinforcement Learning

Edwin Hamel-de le Court†

Gaspard Ohlmann†

Francesco Belardinelli

Imperial College London, United Kingdom e.hamel-de-le-court@imperial.ac.uk

Independent Researcher

Imperial College London, United Kingdom francesco.belardinelli@imperial.ac.uk

Mulhouse, France gaspard.ohlmann@outlook.com

### ABSTRACT

expected cost below a given threshold. Traditional methods, such as Lagrangian approaches [2, 10, 12], allow to converge towards a safe policy, but do not provide formal guarantees on safety, neither during training nor on the provided policy.

Safety is a major concern in reinforcement learning (RL): we aim at developing RL systems that not only perform optimally, but are also safe to deploy by providing formal guarantees about their safety. To this end, we introduce Probabilistic Shielding via Risk Augmentation (ProSh), a model-free algorithm for safe reinforcement learning under cost constraints. ProSh augments the Constrained MDP state space with a risk budget and enforces safety by applying a shield to the agent’s policy distribution using a learned cost critic. The shield ensures that all sampled actions remain safe in expectation. We also show that optimality is preserved when the environment is deterministic. Since ProSh is model-free, safety during training depends on the knowledge we have acquired about the environment. We provide a tight upper-bound on the cost in expectation, depending only on the backup-critic accuracy, that is always satisfied during training. Under mild, practically achievable assumptions, ProSh guarantees safety even at training time, as shown in the experiments.

We introduce ProSh: a novel probabilistic shielding method that ensures safety also at training time, in model-free RL. Unlike classic shielding methods that restrict unsafe actions based on a model of the environment, ProSh operates on distributions, augments the CMDP with a risk budget, and uses a learned cost critic to guide safe exploration. Crucially, ProSh does not assume access to a simulator or environment abstraction, and is compatible with continuous environments. We provide a formal bound for the safety of ProSh. In addition, we show that ProSh is optimal in the deterministic setting and that it is safe in both cases up to a controllable and vanishing coefficient. The full version of this paper is available at [7].

## 2 PROSH: THE AUGMENTATION METHOD

Our approach uses risk-augmentation, similar to [6], whereby each state is paired with a risk budget that represents the expected cost the agent is allowed to incur from that point onward. To each state–action pair (𝑠,𝑎) with 𝑎∈𝐴(𝑠), we associate an estimate of the achievable minimum expected cost, denoted by the critic 𝑄𝑏(𝑠,𝑎), and define 𝑄𝑏(𝑠) = min𝑎∈𝐴(𝑠) 𝑄𝑏(𝑠,𝑎).

### KEYWORDS

Safe Reinforcement Learning, Formal Methods, Shielding, Probabilistic Temporal Logic, Stochastic Systems

ACM Reference Format: Edwin Hamel-de le Court†, Gaspard Ohlmann†, and Francesco Belardinelli. 2026. ProSh: Probabilistic Shielding for Model-free Reinforcement Learning. In Proc. of the 25th International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2026), Paphos, Cyprus, May 25 – 29, 2026, IFAAMAS, 3 pages. https://doi.org/10.65109/KCVZ6904

Definition 1 (Risk-augmented CMDP). For any CMDP M = (𝑆,𝐴,𝑠𝑖, 𝑃, 𝑅,𝐶,𝑑,𝛾𝑟,𝛾𝑐), we augment the set of states and actions, 𝑆= 𝑆× R and 𝐴(𝑠,𝑥) = 𝐴× R. The Transition Probability Function is defined as 𝑃((𝑠′,𝑥′)|(𝑎,𝑦𝑎), (𝑠,𝑥)) = 𝑃(𝑠′|𝑠,𝑎) if 𝛾𝑐𝑥′ = 𝑦−𝑄𝑏(𝑠,𝑎) + 𝛾𝑐𝑄𝑏(𝑠′) and 0 otherwise.

† These authors contributed equally to this work.

The transition function 𝑃ensures that the corresponding risk is spread coherently to each state in the non-deterministic case.

## 1 INTRODUCTION

We consider policies that keep the risk budget synchronized with the CMDP dynamics. For these policies, the risk budget corresponds, up to a controllable factor, to an upper bound of the expected cost. We call these the 𝑄𝑏-shielded policies. These policies are safe, see [7] for the complete theoretical framework.

A key challenge in AI is designing agents that learn to act optimally in unknown environments [14]. Reinforcement Learning (RL) – particularly when combined with deep neural networks – has made impressive strides in domains such as games [9], ro-

botics [5], and autonomous driving [4]. However, ensuring safety during both training and deployment remains a critical barrier to real-world adoption. This paper focuses on safe learning in Constrained Markov Decision Processes (CMDPs), where agents maximize the expected discounted reward, while keeping the cumulative

Definition 2 (𝑄𝑏-Shielded policies). We define the backup policy 𝜋𝑏on M as for any 𝑠∈𝑆, 𝜋𝑏(𝑠) = 𝛿𝑎0, where 𝑄𝑏(𝑠,𝑎0) = min𝑎∈𝐴(𝑠) 𝑄𝑏(𝑠,𝑎).

A policy 𝜋is said to be 𝑄𝑏-shielded if for any (𝑠,𝑥) ∈ ¯S, if 𝑥≥𝑄𝑏(𝑠), there exist (𝑃𝑎)𝑎∈𝐴(𝑠) and (𝑦𝑎)𝑎∈𝐴(𝑠), with 𝑦𝑎≥𝑄𝑏(𝑠,𝑎) for all 𝑎∈𝐴(𝑠), such that for all (𝑠,𝑥) ∈𝑆,

This work is licensed under a Creative Commons Attribution International 4.0 License.

∑︁

∑︁

𝜋(𝑠,𝑥) =

𝑃𝑎𝛿(𝑎,𝑦𝑎), 𝑥≥

𝑃𝑎𝑦𝑎,

Proc. of the 25th International Conference on Autonomous Agents and Multiagent Systems (AAMAS 2026), C. Amato, L. Dennis, V. Mascardi, J. Thangarajah (eds.), May 25 – 29, 2026, Paphos, Cyprus. © 2026 International Foundation for Autonomous Agents and Multiagent Systems (www.ifaamas.org). https://doi.org/10.65109/KCVZ6904

𝑎∈𝐴(𝑠)

𝑎∈𝐴(𝑠)

and 𝜋(𝑠,𝑥) = 𝛿(𝜋𝑏(𝑠),𝑥) when 𝑥< 𝑄𝑏(𝑠).

<!-- page 2 -->

Remark 1 (On assumption 𝚫𝒃→0). Under several assumptions (e.g. tabular case, Over-parameterized neural networks,Batch (fitted) Q-evaluation) , we have Δ𝑏→0 [3, 8, 15, 16].

The policies are shielded when they always allow a budget for the actions larger than the estimated minimal cost of taking this action. Moreover, the total budget allowed for the actions is, in expectancy, smaller than the current budget. For a shielded policy 𝜋, there exists a policy 𝜋simulating 𝜋in M that we call the projection of 𝜋onto M. We now present the 𝑄𝑏-shield, denoted Ξ𝑄𝑏, that takes an augmented policy and outputs a 𝑄𝑏-shielded policy.

## 3 EXPERIMENTAL EVALUATION

We compared ProSh with PPO-Saute [11], TD3-Lagrangian [10], PID-TD3 [13], FOCOPS [17] and CPO [1]. Please refer to [7] for the complete benchmark. ProSh maintains a high level of safety during training. PPO-Saute is the only other algorithm that achieves a comparable level of safety, although with reduced performance. The results suggest that ProSh provides the best trade-off between safety and performance in the evaluated environments, especially when ensuring safety is critical.

Theorem 1. Let 𝜋𝑏be the policy that chooses (𝜋𝑏(𝑠),𝑄𝑏(𝑠,𝑎)) in any augmented state (𝑠,𝑥), and 𝑉be the set of augmented policies

```math
¯𝜋such that for any (𝑠,𝑥), there exist (𝑃𝑎)𝑎∈𝐴(𝑠) and (𝑦𝑎)𝑎∈𝐴(𝑠) with
𝑦𝑎≥𝑄𝑏(𝑠,𝑎) satisfying ¯𝜋(𝑠,𝑥) = Í
```

𝑎𝑃𝑎𝛿(𝑎,𝑦𝑎). For any 𝜋∈𝑉, the policy Ξ𝑄𝑏(𝜋) defined as

𝛿(𝜋𝑏(𝑠),𝑥), for 𝑥< 𝑄𝑏(𝑠),

Ξ𝑄𝑏(𝜋)(𝑠,𝑥) =

the mixture (1 −𝜆)𝜋+ 𝜆𝜋𝑏, 𝑥≤𝑄𝑏(𝑠),

Cost - HalfCheetah

Reward - HalfCheetah

40

TD3Lag TD3PID ProSh

35

where 𝜆= (𝑥−Í

𝑎𝑃𝑎𝑦𝑎), is called the 𝑄𝑏shield of 𝜋and is 𝑄𝑏-shielded.

𝑎𝑃𝑎𝑦𝑎)/(𝑄𝑏(𝑠,𝑎) −Í

8000

30

Episode Reward

6000

25

Episode Cost

TD3Lag TD3PID ProSh Max Cost

20

Learning Algorithm. We present a minimal version of the training loop for the main actor in Algorithm 1. A complete implementation is proposed in [7]. The shield acts on distribution, rather than actions. It uses the values provided by the critic 𝑄𝑏and combines it with the backup action to obtain a safe distribution.

4000

15

10

2000

5

0

0

### 0.0 0.2 0.4 0.6 0.8 1.0 Training Steps 1e6

### 0.0 0.2 0.4 0.6 0.8 1.0 Training Steps 1e6

Cost - HalfCheetah

Reward - HalfCheetah

40

3000

CPO FOCOPS PPOSaute ProSh Max Cost

CPO FOCOPS PPOSaute ProSh

Algorithm 1 ProSh: Main Actor only

35

2500

30

1: Input: cost budget 𝑑, margin 𝛿, cost discount 𝛾𝑐

2000

Episode Reward

25

Episode Cost

2: Initialize main actor ¯𝜋𝜓 𝑟, backup critic 𝑄𝜃

1500

20

𝑏 3: for each episode do

1000

15

500

```math
4:
𝑠←𝑠𝑖, 𝑥←𝑑−𝛿
```

10

0

5: while not done do

5

−500

6: Shield: 𝜇safe ←Ξ𝑄𝑏( ¯𝜋𝜓

𝑟)(𝑠,𝑥)

0

### 0.0 0.2 0.4 0.6 0.8 1.0 Training Steps 1e6

### 0.0 0.2 0.4 0.6 0.8 1.0 Training Steps 1e6

7: Sample (𝑎,𝑦) ∼𝜇safe 8: Execute (𝑎,𝑦), observe (𝑠′,𝑥′), reward 𝑟, cost 𝑐

Cost - PointCircle

Reward - PointCircle

9: Store transition ((𝑠,𝑥), (𝑎,𝑦),𝑟,𝑐, (𝑠′,𝑟′))

40

60

TD3Lag TD3PID ProSh Max Cost

```math
10:
𝑠←𝑠′, 𝑟←𝑟′
```

35

50

11: end while

30

40

Episode Reward

25

12: Update: • Update 𝜋𝜃using shielded distributions from memory

Episode Cost

30

20

15

13: end for

20

10

14: return projected policy 𝜋𝜓 𝑟

10

TD3Lag TD3PID ProSh

5

0

0

### 0.0 0.2 0.4 0.6 0.8 1.0 Training Steps 1e6

### 0.0 0.2 0.4 0.6 0.8 1.0 Training Steps 1e6

The shield precedes sampling, so the exploration is budget-safe. The choice of the RL update for 𝜃is open (e.g., PG, PPO, A2C). Additionally, the backup critic 𝑄𝑏can be learned, either in parallel, off-policy, or even pre-computed. The following theorem holds.

Cost - PointCircle

Reward - PointCircle

40

50

CPO FOCOPS PPOSaute ProSh Max Cost

35

40

30

Episode Reward

25

30

Episode Cost

Theorem 2 (Safety and near-Optimality). (i) At any step of the algorithm, the output policy ¯𝜋satisfies, with 𝑄∗

20

𝑏the minimal cost and 𝑥0 ≥𝑄𝑏(𝑠0),

20

15

10

CPO FOCOPS PPOSaute ProSh

10

```math
C ¯
M (𝑠0,𝑥0) ( ¯𝜋) ≤𝑥0 + 2Δ𝑏
```

5

## 1 −𝛾𝑐 , Δ𝑏= ||𝑄𝑏−𝑄∗

𝑏||∞

0

0

### 0.0 0.2 0.4 0.6 0.8 1.0 Training Steps 1e6

### 0.0 0.2 0.4 0.6 0.8 1.0 Training Steps 1e6

(ii) The algorithm is asymptotically optimal in deterministic en-

```math
vironments as Δ𝑏→0. More precisely, with Π the set of all
policies in M,there exists a shielded policy 𝜋with cost at most
𝑑+2E for E = 2Δ𝑏
```

Acknowledgments. The research presented in this paper was supported by the EPSRC grant number EP/X015823/1, ”An abstractionbased technique for Safe Reinforcement Learning”.

1−𝛾𝑐, such that R( ¯𝜋) ≥max𝜋∈Π, 𝐶(𝜋)≤𝑑R(𝜋).

<!-- page 3 -->

## References

arXiv:2510.15720 [cs.LG] https://arxiv.org/abs/2510.15720

[8] Xingtu Liu. 2024. Information-Theoretic Generalization Bounds for Batch Rein-

[1] Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel. 2017. Constrained forcement Learning. Entropy 26, 11 (2024), 995.

[9] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Policy Optimization. In Proceedings of the 34th International Conference on Machine Learning (Proceedings of Machine Learning Research, Vol. 70), Doina Precup and Yee Whye Teh (Eds.). PMLR, 22–31. https://proceedings.mlr.press/v70/achiam17a. html

[2] Joshua Achiam, David Held, Aviv Tamar, and Pieter Abbeel. 2019. Benchmarking Antonoglou, Daan Wierstra, and Martin A. Riedmiller. 2013. Playing Atari with Deep Reinforcement Learning. CoRR abs/1312.5602 (2013). arXiv:1312.5602 http://arxiv.org/abs/1312.5602

[10] Alex Ray, Joshua Achiam, and Dario Amodei. 2019. Benchmarking Safe Explo- Safe Exploration in Deep Reinforcement Learning. arXiv preprint arXiv:1805.05800 (2019).

[3] Alekh Agarwal, Sham Kakade, Nan Jiang, and Wen Sun. 2020. Flambe: Structural ration in Deep Reinforcement Learning. In arXiv preprint arXiv:1910.01708.

[11] Aivar Sootla, Alexander I. Cowen-Rivers, Taher Jafferjee, Ziyan Wang, David Mguni, Jun Wang, and Haitham Bou-Ammar. 2022. Saute RL: Almost Surely Safe Reinforcement Learning Using State Augmentation. arXiv:2202.06558 [cs.LG] https://arxiv.org/abs/2202.06558

[12] Adam Stooke, Joshua Achiam, and Pieter Abbeel. 2020. Responsive Safety in Complexity and Representation Learning of Low Rank MDPs. In Advances in Neural Information Processing Systems (NeurIPS).

[4] Alex Kendall, Jeffrey Hawke, David Janz, Przemyslaw Mazur, Daniele Reda, John- Mark Allen, Vinh-Dieu Lam, Alex Bewley, and Amar Shah. 2019. Learning to Drive in a Day. In International Conference on Robotics and Automation, ICRA 2019, Montreal, QC, Canada, May 20-24, 2019. IEEE, 8248–8254. https://doi.org/ 10.1109/ICRA.2019.8793742

[5] Jens Kober, J. Bagnell, and Jan Peters. 2013. Reinforcement Learning in Robotics: Reinforcement Learning by PID Lagrangian Methods. In ICML.

[13] Adam Stooke, Joshua Achiam, and Pieter Abbeel. 2020. Responsive Safety in Re- inforcement Learning by PID Lagrangian Methods. arXiv:2007.03964 [math.OC] https://arxiv.org/abs/2007.03964

[14] Richard S Sutton and Andrew G Barto. 2018. Reinforcement Learning: An Intro- A Survey. The International Journal of Robotics Research 32 (09 2013), 1238–1274. https://doi.org/10.1177/0278364913495721

[6] Edwin Hamel-De le Court, Francesco Belardinelli, and Alexander W. Goodall. duction (2nd ed.). MIT press, Cambridge, MA.

[15] Christopher J. C. H. Watkins and Peter Dayan. 1992. Q-Learning. Machine Learning 8, 3–4 (1992), 279–292.

[16] Zhihan Xie, Qi Cai, Ethan Zhou, Alexander Risteski, and Alexander G. Gray. 2021.

2025. Probabilistic Shielding for Safe Reinforcement Learning. In AAAI-25, Sponsored by the Association for the Advancement of Artificial Intelligence, February 25 - March 4, 2025, Philadelphia, PA, USA, Toby Walsh, Julie Shah, and Zico Kolter (Eds.). AAAI Press, 16091–16099. https://doi.org/10.1609/AAAI.V39I15.33767

[7] Edwin Hamel-De le Court, Gaspard Ohlmann, and Francesco Belardinelli. Bellman Error is a Good Proxy for Value Error. In International Conference on Machine Learning (ICML).

[17] Yiming Zhang, Quan Vuong, and Keith W. Ross. 2020. First Order Constrained Optimization in Policy Space. arXiv:2002.06506 [cs.LG] https://arxiv.org/abs/ 2002.06506

2025. ProSh: Probabilistic Shielding for Model-free Reinforcement Learning.
