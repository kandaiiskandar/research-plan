# DSA-SafetyBench: A Safety-Aware Benchmark for Artificial-Intelligence-Based Dynamic Security Assessment in Energy Systems

> Source PDF: `DSA-SafetyBench- A safety-aware benchmark for artificial-intelligence-based dynamic security assessment in energy systems.pdf`

> Extraction note: Text extracted from the uploaded PDF using Poppler `pdftotext -layout`. Page boundaries are preserved below. Formatting, equations, tables, and multi-column reading order may not perfectly match the original PDF. Use the original PDF for authoritative visual/layout verification.


---

## PDF Page 1

```text
                                                                        Energy and AI 25 (2026) 100811


                                                                    Contents lists available at ScienceDirect


                                                                            Energy and AI
                                                           journal homepage: www.elsevier.com/locate/egyai




DSA-SafetyBench: A safety-aware benchmark for artificial-intelligence-based
dynamic security assessment in energy systems
Mohamed Shamseldein
Ain Shams University, Department of Electrical Engineering, Egypt



GRAPHICAL                 ABSTRACT




HIGHLIGHTS

• DSA-SafetyBench scores AI-based DSA decisions, not only trajectories.
• Seven ML baselines produce all-unsafe calibrated decisions.
• Paired bootstrap finds no statistically separable architecture winner.
• SFR baselines expose information-set and effective-inertia limits.
• Artifacts include records, schema, scorer, and robustness scripts.




ARTICLE                INFO                               ABSTRACT

Keywords:                                                 Benchmarks have accelerated progress in coding, mathematics, and language, but artificial-intelligence-based
Dynamic security assessment                               dynamic security assessment (DSA) lacks a safety-aware benchmark for operational decisions. We introduce
Artificial intelligence                                   DSA-SafetyBench, an IEEE 39-bus protocol that tests whether machine-learning models produce useful
Safety-aware benchmarking
                                                          frequency-security decisions, not only accurate trajectories. It defines fixed splits, unsafe labels, validation-
Frequency security
                                                          calibrated thresholds, decision-level metrics, repeated-seed paired-bootstrap uncertainty, per-scenario records,
Swing-frequency response
Dynamic state estimation
                                                          and swing-frequency-response (SFR) physics baselines with explicit information sets. On the base benchmark,
                                                          regression-derived safety decisions are near-degenerate: models with acceptable trajectory errors rank unsafe
                                                          events near the base rate and produce all-safe or all-unsafe policies. A three-class auxiliary safety head improves
                                                          ranking, but five-seed evaluation does not separate architectures. On the expanded benchmark (820 scenarios,
                                                          219 unsafe), denser coverage raises PR-AUC yet all seven methods still collapse to all-unsafe hard decisions
                                                          under F2-opt, target-recall, and fixed-alarm-budget tests. SFR baselines show complementary limits: ambient



     E-mail address: mohamed.shamseldein@eng.asu.edu.eg.

https://doi.org/10.1016/j.egyai.2026.100811
Received 21 May 2026; Received in revised form 31 May 2026; Accepted 9 June 2026
Available online 18 June 2026
2666-5468/© 2026 The Author. Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-
nc-nd/4.0/).
```

---

## PDF Page 2

```text
M. Shamseldein                                                                                                                    Energy and AI 25 (2026) 100811


                                                dynamic state estimation is weak, 5 s event-triggered fitting is delayed nowcasting, and nameplate inertia is
                                                not a stable anchor. Crucially, a leak-free event-triggered information set – each model sees only the first
                                                0.5–2 s of the measured frequency response, aligned with the event-triggered physics estimator’s measurement
                                                window – largely reduces the collapse and recovers non-trivial low-false-alarm operating points across IEEE 39,
                                                NPCC (140-bus), and WECC (179-bus, renewable-rich), with remaining threshold- and system-dependent limits.
                                                DSA-SafetyBench shows artificial-intelligence-based DSA claims require decision-level, multi-seed, physics-
                                                aware evaluation, and that event-triggered screening is a constructive path where pre-event descriptors are
                                                insufficient.




                                                                                 2. Contributions
1. Introduction
                                                                                    1. We define DSA-SafetyBench, a safety-aware benchmark protocol
     Dynamic security assessment (DSA) is an operational screening                     and artifact package for ML-DSA. It includes fixed scenario splits,
problem: after a disturbance, an operator needs to know whether the                    per-scenario prediction records, unsafe-event labels, validation-
power system will remain within security limits or whether preventive                  calibrated hard decisions, decision-level metrics, paired boot-
or corrective action is required. For frequency-security assessment, the               strap uncertainty over repeated seeds, a prediction schema, a
critical outcomes are unsafe frequency nadirs – the lowest frequency                   case inventory, and a reproducible benchmark scoring script.
reached after the event – and divergent trajectories. Average trajectory            2. We provide an IEEE 39-bus reference implementation with two
quality is secondary if the resulting decision is false-safe.                          benchmark streams: a base stream that reveals regression-derived
     Within energy-system operation, this problem sits at the intersection             decision weaknesses under sparse unsafe samples, and an ex-
of wide-area measurement, data-driven analytics, and physics-based                     panded SFR-compatible stream with 820 load-step and generator-
decision support, making it a useful test case for evaluating artificial               output-loss scenarios for matched physics comparisons.
intelligence claims under operational security constraints.                         3. We implement a baseline suite covering regression-only ML,
     Progress in other artificial intelligence domains is often measured               auxiliary-safety-head ML, no-history and history-aware sequence
through standardized benchmarks with fixed tasks, held-out splits,                     models, and SFR-class physics baselines with explicit
shared scoring scripts, and baseline leaderboards. Coding and                          information-set accounting.
mathematical-reasoning benchmarks do not merely report whether a                    4. We show benchmark findings that are hidden by common ML-
model fits training data; they test whether model outputs solve the                    DSA reporting practice: regression-derived safety assessment can
intended task under a defined scoring protocol. Artificial-intelligence-               produce all-safe or all-unsafe policies, single-seed architecture
based DSA needs the same discipline. A DSA benchmark should ask                        rankings are not reliable, and denser unsafe coverage improves
not only whether a model predicts trajectories accurately, but whether                 ranking without yielding statistically separable model winners.
it ranks unsafe cases, supports calibrated decisions, remains stable
                                                                                    5. We audit benchmark validity assumptions, including simula-
across seeds, and is compared against physics baselines under explicitly
                                                                                       tor history-channel causality and SFR disturbance compatibility.
declared information sets.
                                                                                       The audit shows that history channels are not causally consumed
     Recent machine-learning-based DSA (ML-DSA) studies often report
                                                                                       by the simulator, and the SFR-family results expose weak ambi-
aggregate accuracy, trajectory mean-squared error, or nadir mean ab-
                                                                                       ent DSE, near-oracle delayed nowcasting, competitive first-order
solute error. These metrics are useful but incomplete under the class
                                                                                       envelope fitting, and strongly contingency-dependent effective
imbalance typical of simulated security datasets. A model can report
                                                                                       inertia.
high accuracy by predicting every case as safe, or low nadir error by
                                                                                    6. We identify a constructive path: a leak-free event-triggered infor-
fitting common stable trajectories while failing to rank rare unsafe
                                                                                       mation set, in which each model observes only the first 0.5–2 s
cases. This paper treats that decision-level gap as the object of study.
                                                                                       of the measured frequency response. This measurement window
     The broader artificial-intelligence-evaluation literature has long
                                                                                       is aligned with the event-triggered physics estimator; it largely
warned that single-seed rankings, imbalanced labels, and threshold
                                                                                       reduces the all-unsafe collapse and recovers usable low-false-
choices can change conclusions. The DSA-specific contribution is to
                                                                                       alarm operating points. This result holds across IEEE 39, NPCC
show how those known risks manifest in power-system security, where
                                                                                       (140-bus), and WECC (179-bus, renewable-rich), which also ex-
asymmetric operational cost, trajectory-regression surrogates for secu-
                                                                                       ternally validate the protocol under a common early-response
rity decisions, and physics baselines with limited applicability interact.
                                                                                       information set.
     This paper introduces DSA-SafetyBench to make these validity
checks explicit. The benchmark separates simulator information-set
audits from decision-level scoring: historical or scenario features are          3. Related work
credited only when they are causally connected to the simulated
dynamics, and machine-learning forecasts are evaluated by unsafe-                3.1. Artificial intelligence and power-system benchmarks
event ranking, calibrated hard decisions, and repeated-seed uncertainty
rather than by trajectory error alone.                                               Power-system research already has several influential benchmark
     Physics baselines are treated with the same care. Aggregate swing-          traditions, but they target different operational questions than ML-
frequency response (SFR) methods require a scalar active-power dis-              DSA safety decisions. PGLib-OPF standardizes AC optimal-power-flow
turbance and defensible dynamic parameters. Some scenarios, such                 formulations and network data so optimization algorithms can be com-
as self-clearing bus faults, are not SFR-compatible. Others, such as             pared on common cases [1]. L2RPN and Grid2Op turn transmission-
load steps and generator-output-loss events, are SFR-compatible but              grid operation into an interactive topology-control benchmark for
expose dynamic-state-estimation (DSE) issues: multi-mode ambient dy-             reinforcement-learning agents under operational constraints [2]. Pow-
namics, unstable nameplate-inertia anchoring, and early-window iden-             erGym provides an OpenAI-Gym-style benchmark for distribution-system
tifiability. The benchmark asks what each method can claim under the             volt-var control, with IEEE feeder variants and physical voltage and
information it is actually allowed to use.                                       loss objectives [3]. Public transient-stability datasets for the IEEE New

                                                                             2
```

---

## PDF Page 3

```text
M. Shamseldein                                                                                                                  Energy and AI 25 (2026) 100811


England 39-bus system provide useful data for ML-based TSA classi-               3.5. Evaluation under rare unsafe events
fication and feature studies [4], and recent DSA dataset-generation
work emphasizes sampling near the security boundary to improve                       Operational DSA is a rare-event screening task. Accuracy is dom-
data-driven assessment [5].                                                      inated by the safe class, and thresholded metrics depend strongly
    These efforts establish the value of shared cases, public datasets,          on calibration. Precision–recall analysis, F-score variants emphasizing
and standardized evaluation in power systems. They do not, how-                  recall, unsafe miss rate, false alarm rate, repeated seeds, and paired
ever, provide a benchmark protocol for safety-aware ML-DSA decisions             uncertainty estimates are therefore central to the protocol [23–25].
with fixed scenario identifiers, repeated training seeds, per-scenario           Selective classification and conformal prediction provide related safety-
prediction records, hard-decision calibration, unsafe-miss and false-            critical ML tools for abstention and uncertainty quantification, but
alarm reporting, paired scenario-level uncertainty, and physics-baseline         DSA-SafetyBench focuses on the more direct operating question of
information-set accounting. DSA-SafetyBench is designed to fill that             whether a model can rank and threshold unsafe events under fixed
gap rather than replace OPF, topology-control, volt-var, or general TSA          alarm budgets [26,27]. The five-seed results show that single-seed
datasets.                                                                        architecture rankings can invert on the same benchmark, which is itself
                                                                                 a methodological warning for ML-DSA comparison studies.
3.2. Machine-learning dynamic security assessment
                                                                                 4. DSA-SafetyBench design

    ML-based DSA has been studied with feedforward, convolutional,
                                                                                 4.1. Benchmark task and scoring protocol
recurrent, graph-based, and attention-based architectures that map pre-
contingency operating conditions or short post-contingency measure-
                                                                                     DSA-SafetyBench defines a model-facing task, a scoring protocol,
ments to stability labels, trajectory forecasts, or security margins [6–
                                                                                 and a per-scenario record format. A model receives the scenario inputs
10]. These approaches are attractive because they can amortize expen-
                                                                                 allowed by its information set and returns an unsafe score, an optional
sive time-domain simulation into fast online inference. However, many
                                                                                 calibrated hard decision, and any regression output such as predicted
studies emphasize aggregate accuracy or regression quality, which can
                                                                                 nadir. The benchmark scorer evaluates those submissions against fixed
obscure unsafe-event performance when unsafe samples are sparse.
                                                                                 scenario identifiers, fixed splits, and hidden or released labels depend-
    Trajectory-prediction formulations are especially relevant here be-          ing on the evaluation setting. The full per-scenario record includes
cause nadir and RoCoF can be derived from predicted frequency tra-               scenario identifier, split, unsafe score, calibrated hard decision, de-
jectories. The results show that this derivation is not automatically            cision source, predicted nadir, true nadir, unsafe label, unsafe type,
reliable: a trajectory predictor can have acceptable average error while         active-power disturbance, model name, and training seed. The required
failing to rank rare unsafe events. The benchmark therefore separates            fields for the benchmark scorer are scenario identifier, unsafe score, and
trajectory fidelity from safety ranking.                                         unsafe label; the remaining fields enable calibrated-decision metrics,
    The benchmark is not intended to exhaust the full design space of            nadir MAE, class-stratified reporting, and SFR information-set audits.
rare-event learning. Cost-sensitive losses, ranking losses, conformal pre-       Fig. 1 summarizes the workflow from time-domain simulation through
diction, selective classification, and uncertainty-aware screening may           declared information sets, validation thresholding, decision metrics,
improve operational decision quality. The goal here is narrower: to test         paired-bootstrap uncertainty, and released per-scenario records.
common trajectory-regression and auxiliary-safety-head formulations                  The reference task is online frequency-security assessment after a
under safety-aware metrics and explicitly declared information sets.             contingency. For each scenario, the target trajectory is the center-of-
                                                                                 inertia frequency deviation over the post-event simulation window.
3.3. Sequence models and causal grid histories                                   A scenario is labeled unsafe if the trajectory crosses the frequency-
                                                                                 security nadir threshold (−0.1 Hz) or diverges; otherwise it is labeled
    Long-horizon    sequence    models,    including   LSTM     [11],            safe. The −0.1 Hz value is a benchmark security threshold chosen to
Transformer [12], TCN [13], neural ODE or liquid-time-constant mod-              create a controlled rare-event screening task with measurable class
els [14–16], and state-space models such as Mamba [17,18], offer                 separation; it is not intended as a universal grid-code, protection,
natural tools for history-aware DSA. The benchmark keeps these ar-               or under-frequency-load-shedding criterion. Unsafe cases are further
                                                                                 stratified into nadir-threshold-violating and divergent outcomes. This
chitectures in the comparison but does not claim a causal-history
                                                                                 three-class label is used for safety supervision and for stratified re-
advantage where the simulator data do not support one. Long-context
                                                                                 porting, while aggregate binary unsafe labels are used for operational
modeling is meaningful only if historical channels actually drive the
                                                                                 metrics such as unsafe miss and false alarm rates.
simulated or measured dynamics.
                                                                                     The operational error asymmetry is central: a false-safe decision can
                                                                                 expose the system to an unsafe event, while a false-unsafe decision
3.4. SFR, dynamic state estimation, and information sets                         is conservative but increases alarm burden. We therefore do not use
                                                                                 aggregate accuracy as a primary metric. Instead, we report PR-AUC
   Aggregate SFR models approximate system frequency response with               for unsafe-event ranking, F2-opt to emphasize unsafe recall, validation-
low-order swing and governor dynamics [19,20]. They are interpretable            calibrated hard decisions, unsafe miss rate, false alarm rate, nadir MAE,
and operationally attractive, but they require a well-defined active-            and per-class recall for nadir-threshold-violating and divergent cases.
power disturbance and effective dynamic parameters. DSE can estimate             F2 is the F-score with 𝛽 = 2, weighting recall more heavily than
such parameters from ambient or early post-event measurements, but               precision.
the information set matters [21,22]. Fitting a model from the full
post-event trajectory gives an oracle upper bound, while ambient                 4.2. ML models and safety supervision
and event-triggered estimates face model-class mismatch, measurement
noise, window-length limits, and parameter identifiability.                         We evaluate standard sequence and snapshot ML baselines under
   The benchmark therefore distinguishes SFR-oracle, ambient SFR-                a matched train/validation/test split: LiquidMamba variants, Liquid-
DSE, event-triggered SFR-DSE, noisy event-triggered SFR-DSE, and mis-            Pure without history, LSTM, Transformer+LSTM, Mamba+LSTM, TCN,
specified SFR-DSE. This avoids the common practice of comparing ML               and CNN-1D. The regression-only form of each model predicts a fre-
against a single ‘‘SFR’’ row whose assumptions are not specified.                quency trajectory and derives a safety score from the predicted nadir.

                                                                             3
```

---

## PDF Page 4

```text
M. Shamseldein                                                                                                                        Energy and AI 25 (2026) 100811




Fig. 1. DSA-SafetyBench workflow. The protocol starts from time-domain simulations, fixes scenario identities and train/validation/test splits, declares the
information available to each model or physics baseline, calibrates hard decisions on validation data, reports decision-level safety metrics, estimates uncertainty
with paired repeated-seed bootstrapping, and releases per-scenario records for reuse.


The safety-aware form keeps the trajectory head but adds a parallel                  and save per-scenario records covering identity (seed, scenario identi-
three-class auxiliary safety head.                                                   fier, model name, and split), prediction (unsafe score, calibrated hard
    The auxiliary head operates on the event-decoder hidden sequence,                decision, decision source, and regression nadir), ground truth (unsafe
not on the predicted nadir. For each model, the hidden sequence                      label, unsafe type, and true nadir), and disturbance characterization
is pooled by concatenating its temporal mean, temporal maximum,                      (active-power imbalance). The same scenario identities are evaluated
first hidden state, and final hidden state. The pooled vector is passed              across seeds; the repeated-seed dimension captures training stochas-
through LayerNorm, a linear projection from 4d to d, ReLU, and a final               ticity rather than a different test set. The two resampling dimensions
linear layer with three logits for the safe, nadir-threshold-violating,              correspond to two distinct uncertainty sources: the repeated training
and divergent classes. The protocol does not feed predicted nadir into               seeds isolate epistemic uncertainty arising from model initialization and
the safety head, because ablation experiments showed that predicted                  optimization, while resampling scenarios within each seed reflects the
nadir is least reliable on the unsafe tail and can anchor the classifier to          aleatory variability of the disturbance population. This distinction is
regression errors.                                                                   consistent with sociotechnical risk-analysis work, where expert judg-
    The training objective combines trajectory loss and auxiliary safety             ment, model assumptions, data limitations, and scenario variability are
focal loss. The focal-loss defaults are global alpha 0.5 and gamma 2.0,              treated as separate contributors to uncertainty [28,29]. Reporting both,
with class labels drawn from the three-way safety target. Checkpoint                 rather than a single-seed point estimate, is precisely what exposes the
selection uses validation safety PR-AUC rather than trajectory MSE                   non-replicable architecture rankings that single-seed studies miss.
when safety supervision is active. Hard decisions are calibrated on the                  For paired comparisons, we use the saved per-scenario records so
validation split by selecting the unsafe-score threshold that maximizes              that method differences are computed on matched scenario identi-
F2. This design intentionally separates two questions that are often con-            ties. The protocol is a two-level paired bootstrap: resample scenarios
flated: whether a model predicts average trajectories well, and whether              within each seed, compute method-pair differences per seed, then
it ranks rare unsafe events well enough for operational screening.                   average seed-level differences and bootstrap across seeds. Confidence
    Auxiliary-head architecture and focal-loss settings are held fixed               intervals are percentile intervals computed with 2000 bootstrap repli-
across models to avoid uneven hyperparameter search. The results
                                                                                     cates. For the base-benchmark auxiliary-head summary, where only
therefore test whether simple, explicit safety supervision is sufficient
                                                                                     seed-level aggregate intervals were available, Table 4 reports seed-
to turn common ML-DSA architectures into useful operational screen-
                                                                                     resampling intervals and treats them as robustness diagnostics; the
ers; they are not a final statement about the best possible rare-event
                                                                                     expanded-benchmark pairwise intervals use the saved per-scenario
classifier.
                                                                                     records. Because all top-method confidence intervals include zero on
    In addition to the regression-only and auxiliary-head forms, we eval-
                                                                                     the base benchmark, no architecture winner is claimed from that
uate an event-triggered form under a deliberately restricted, leak-free
                                                                                     dataset.    Multiple-comparison       correction   is   therefore     not
information set. The model observes only the first 𝜏 seconds of the mea-
                                                                                     decision-changing: all unadjusted pairwise intervals already fail to
sured center-of-inertia frequency response, supplied through a derived
                                                                                     separate the top methods.
observation channel and an explicit observation mask, with all later
                                                                                         This no-winner conclusion is interpreted with the available unsafe-
samples masked and with no fault location, disturbance magnitude,
                                                                                     event support in view. With approximately 10 unsafe events per strat-
generator identity, or inertia value provided. Because the frequency
                                                                                     ified test split in the base benchmark, single-seed and even five-
nadir forms several seconds after the disturbance, the first 𝜏 seconds do
                                                                                     seed paired confidence intervals are inherently wide. The expanded
not include the final nadir or divergence outcome, so the model must
infer severity from the early rate of change and slope; the information              benchmark enriches unsafe coverage to 26.7% (219 of 820 scenarios;
set is therefore leak-free. This measurement window is aligned with                  124/420 load-step and 95/400 generator-output-loss) to test whether
the event-triggered SFR-DSE physics baseline defined below. SFR-DSE                  the no-winner finding persists under tighter intervals or whether some
additionally requires a characterized active-power disturbance, so the               methods separate when the unsafe set is denser.
comparison is matched on early-response timing while retaining ex-
plicit input differences. We sweep 𝜏 ∈ {0.5, 1.0, 2.0} s, mirroring the              4.4. Simulator and information-set audit
SFR-DSE event-triggered window family; results are reported in the
event-triggered screening subsection of the Results.                                     A common motivation for history-aware DSA is the hypothesis that
                                                                                     24-hour SCADA histories encode path-dependent latent stress unavail-
4.3. Repeated seeds and bootstrap protocol                                           able to snapshot models. We audit that assumption before interpreting
                                                                                     any model advantage.
  Single-seed comparisons are fragile when the unsafe set is sparse.                     The data generator contains history-like fields such as load history,
We therefore repeat the top-method benchmark over five random seeds                  latent stress, and AGC/governor proxies. A controlled audit varies

                                                                                 4
```

---

## PDF Page 5

```text
M. Shamseldein                                                                                                                      Energy and AI 25 (2026) 100811


Table 1
Controlled audit of candidate history and stress mechanisms in the IEEE 39-bus data generator. A mechanism is marked observable only if changing its control
value produces measurable trajectory variation in the transient simulation. The audit shows that only inertia scaling is causally consumed by the simulator; the
history-like channels are ML inputs but do not drive ANDES transient dynamics.
 Mechanism                         Status                 Levels      Nadir spread (Hz)      SFR 𝛼 spread       Interpretation
 Damping scale                     No observable effect   3           0.000                  0.000              Control value changes, but the trajectory and
                                                                                                                fitted response do not measurably change.
 Inertia scale                     Observable             5           0.122                  1.111              Control value changes aggregate inertia and
                                                                                                                produces measurable nadir and fitted-response
                                                                                                                variation.
 Latent stress                     No observable effect   3           0.000                  0.000              Control value changes, but the trajectory and
                                                                                                                fitted response do not measurably change.
 History load profile              Not consumed           –           –                      –                  Written as an ML history feature, but not applied
                                                                                                                to ANDES PQ injections before transient
                                                                                                                simulation.
 AGC/governor history proxy        Not consumed           –           –                      –                  Written as synthetic history inputs, but not
                                                                                                                consumed by simulator governor or AGC dynamics.



each candidate stress mechanism and measures the resulting trajec-                 and parameters from time-synchronized measurements [21,22]. Event-
tory variation. Table 1 summarizes the result: inertia scaling pro-                triggered SFR-DSE fits parameters from the first 1, 2, or 5 s of measured
duces measurable nadir and fitted-response variation; damping scaling              post-disturbance response. Noisy variants inject deterministic noise
and latent stress have no observable effect; and the load-history and              at three times the nominal measurement-noise level into the event
AGC/governor-history proxy fields are written as ML inputs but are not             window, and misspecified variants fit a first-order monotone step model
consumed by ANDES transient dynamics. These fields may be corre-                   to the same windows.
lated with scenario metadata, but they do not drive the post-event dy-                 This separation makes the operational assumptions visible rather
namics. Therefore, any performance difference between history-aware                than hiding them in a single ‘‘SFR’’ row. Table 2 summarizes the
and no-history models on the base benchmark cannot be interpreted as               per-method allowed inputs, decision timing, and deployability so that
evidence of learned physical path dependence.                                      the machine-learning and physics comparisons are read under explicit
    This audit determines the information-set rules used in the bench-             information-set declarations.
mark. ML methods may use scenario features and trajectories available
in the dataset, but no claim is made that history encodes causal latent            4.6. External systems for generalization
state unless the simulator actually consumes that history. Physics base-
lines are evaluated only when their required disturbance information                   To test whether DSA-SafetyBench instantiates beyond the IEEE 39-
is available without using the post-event response.                                bus reference, we apply the same generation, labeling, splitting, and
                                                                                   scoring pipeline to two larger systems: the 140-bus NPCC system and
                                                                                   the 179-bus WECC system, the latter a renewable-rich Western In-
4.5. SFR-class physics baselines
                                                                                   terconnection case. Both are screened before use with a nadir-spread
                                                                                   criterion: the disturbance family must produce at least a 0.05 Hz spread
    Self-clearing bus-fault scenarios are not SFR-compatible by con-
                                                                                   in frequency nadir across the operating range, so that the benchmark
struction. A second-order aggregate SFR model requires a scalar active-
                                                                                   contains a non-degenerate mix of safe and unsafe outcomes. Under the
power disturbance, 𝛥𝑃𝑑 , and follows the standard aggregate frequency-
                                                                                   generator-trip and load-step disturbance classes both clear this screen
response abstractions used for nadir and primary-frequency-response
                                                                                   (NPCC 0.106 Hz, WECC 0.058 Hz); self-clearing bus faults produce
analysis [19,20]. A temporary bus fault produces a spatial and time-
                                                                                   negligible nadir spread and are unsuitable for this screen.
varying voltage depression whose net frequency impact depends on
                                                                                       The disturbance class is adapted per system because the generator-
network and protection dynamics. We therefore block SFR rows on the
                                                                                   output-loss generator requires a TGOV1N governor model that NPCC
base benchmark rather than infer 𝛥𝑃𝑑 from the response.
                                                                                   (TGOV1) and WECC (IEEEG1) do not provide. NPCC therefore uses
    The expanded benchmark introduces SFR-compatible load-step and
                                                                                   generator-trip scenarios and WECC uses load-step scenarios at
generator-output-loss scenarios. For load steps, 𝛥𝑃𝑑 is the imposed                convergence-screened buses, both governor-agnostic and both vali-
active-load increase. For generator-output-loss scenarios, 𝛥𝑃𝑑 is the              dated to produce a usable safe/unsafe mix (NPCC 17% unsafe, WECC
specified fraction of the pre-event generator active power, implemented            31% unsafe in the test split). These streams are scoped: they use short
as a partial active-power loss rather than necessarily as a full gener-            ambient windows and are intended for the leak-free event-triggered
ator disconnection. Partial generator-output loss represents runback,              ML comparison reported in the Results, not for a full ambient SFR-DSE
derating, mechanical-power reduction, or other partial active-power-               physics replication. They serve as external validation of the protocol
loss events; it also provides a controllable disturbance magnitude for             under a common early-response information set rather than as replace-
spanning safe and unsafe regimes. A calibration study found that                   ments for the IEEE 39-bus reference benchmark, which remains the
25%–100% generator-output loss was uniformly too severe for the                    primary result.
tested generators, so the balanced dataset uses 15, 30, 45, and 60%.
    Inertia scaling over 0.7–1.3 is interpreted as a controlled proxy for          5. Results
changes in online synchronous generation, retirements, commitment,
or synchronous-condenser availability rather than as a literal single              5.1. Regression-derived safety is degenerate on the base benchmark
operating action. The final expanded dataset contains 420 load-step
scenarios and 400 generator-output-loss scenarios.                                     On the base IEEE 39-bus dataset, the seed-42 stratified test split
    The SFR family is separated by information set. SFR-oracle fits a              contains 83 scenarios, including 10 unsafe cases. A ground-truth nadir
damped second-order SFR response to the full post-event trajectory                 score achieves PR-AUC 0.722 and F2-opt 0.833, confirming that the
and serves only as an upper-bound anchor; it is not deployable be-                 safety labels are learnable from a sufficiently accurate nadir signal. The
cause it uses the response being evaluated. Ambient SFR-DSE estimates              learned regression-derived safety scores do not preserve that signal.
shape parameters from pre-event stochastic-load frequency measure-                 Across the regression-only model forms, PR-AUC clusters near the
ments, reflecting the broader DSE objective of tracking dynamic states             unsafe base rate (10/83 = 0.120), spanning 0.092 for LiquidMamba to

                                                                               5
```

---

## PDF Page 6

```text
M. Shamseldein                                                                                                                                  Energy and AI 25 (2026) 100811


Table 2
Information-set and decision-timing rules for DSA-SafetyBench baselines. The table separates screening methods, non-deployable upper bounds, pre-event
estimators, and delayed event-triggered nowcasts so that ML and physics baselines are not compared under hidden information asymmetries.
 Method                           Allowed inputs                                  Uses measured             Decision timing                    Deployability
                                                                                  post-event response?
 Regression ML                    Scenario, history, and fault descriptor         No                        Screening once scenario inputs     Deployable screening
                                  features allowed by the benchmark split;                                  are available.
                                  predicted trajectory is model output.
 Auxiliary-head ML                Same scenario, history, and fault               No                        Screening once scenario inputs     Deployable screening
                                  descriptors; unsafe score is produced                                     are available.
                                  from the decoder hidden representation.
 SFR-oracle                       Full observed post-event frequency              Yes, full response        After the event record.            Non-deployable upper bound
                                  response and active-power disturbance.
 Ambient SFR-DSE                  Pre-event ambient frequency                     No                        Parameters before the event;       Deployable if disturbance is
                                  measurements and active-power                                             decision once disturbance is       characterized
                                  disturbance.                                                              known.
 Event-triggered SFR-DSE          First 1, 2, or 5 s of measured                  Yes, early response       After selected measurement         Delayed nowcast
                                  post-disturbance response and                                             window.
                                  active-power disturbance.
 Noisy/misspecified SFR-DSE       Same event-triggered window with                Yes, early response       After selected measurement         Robustness and model-class
                                  injected measurement noise or                                             window.                            baseline
                                  reduced-order model.


                 Table 3
                 Regression-derived safety decisions on the IEEE 39-bus base-benchmark test split. The test set contains 83 scenarios, including
                 10 unsafe events. PR-AUC is near the unsafe base rate for all learned models, and thresholded decisions produce either all-safe
                 behavior or excessive false alarms. Unsafe miss is the false-safe rate.
                   Model                             PR-AUC              F2-opt               Unsafe miss            False alarm             Nadir MAE (Hz)
                   LiquidMamba (tau-gate)            0.092               0.348                1.000                  0.000                   0.129
                   LiquidPure (No History)           0.151               0.357                1.000                  0.000                   0.192
                   LSTM (History)                    0.112               0.420                1.000                  0.000                   0.021
                   Mamba+LSTM                        0.109               0.439                1.000                  0.000                   0.029
                   Transformer+LSTM                  0.136               0.459                0.000                  1.000                   0.083
                   TCN (History)                     0.101               0.417                1.000                  0.041                   0.157
                   CNN-1D (Snapshot)                 0.148               0.495                1.000                  0.000                   0.175



0.151 for LiquidPure; Table 3 reports the full PR-AUC, F2-opt, unsafe                       the optimizer reduces average error while allocating little capacity to
miss, false-alarm, and nadir-MAE results.                                                   rare nadir excursions or divergent cases. When a hard safety decision
    Most regression-derived models predict no unsafe cases at the                           is then derived from the predicted nadir, small systematic errors near
benchmark’s −0.1 Hz threshold, yielding 100% unsafe miss rates.                             the security threshold become one-sided decision failures: either all-
Transformer+LSTM moves in the opposite direction, producing a 100%                          safe behavior when unsafe excursions are smoothed away, or all-unsafe
false-alarm rate. Nadir MAE does not resolve the problem: LSTM and                          behavior when the learned trajectory bias shifts nadirs below the
Mamba+LSTM have low nadir MAE but still near-random unsafe-event                            threshold.
ranking. The primary issue is therefore not trajectory error alone; it                          The auxiliary safety head reduces but does not eliminate this
is the mismatch between regression training and rare unsafe-event                           architecture-level fragility. It gives each model a direct gradient on un-
decision quality.                                                                           safe outcomes, but the five-seed benchmark still shows unstable rank-
                                                                                            ings and overlapping paired confidence intervals. The decision-level
5.2. Decision patterns under regression-derived safety                                      conclusion is therefore broader than any one architecture: regression-
                                                                                            only training under sparse unsafe samples is not a reliable route to
    We dedicate a subsection to decision patterns because they explain
                                                                                            operational DSA screening.
why aggregate trajectory metrics were misleading. Under regression-
derived safety, the models do not produce a single uniform error pat-
                                                                                            5.3. Auxiliary safety supervision helps but does not establish a winner
tern. Several architectures, including LSTM and Mamba+LSTM, learn
stable-looking trajectory regressors whose thresholded nadirs produce
                                                                                                Adding the auxiliary three-class safety head improves unsafe-event
all-safe decisions. This produces low alarm burden but catastrophic
unsafe miss rates. Transformer+LSTM shows the opposite pattern on                           ranking for several models. In the seed-42 single-seed analysis on
the seed-42 split: it marks every case unsafe, eliminating unsafe misses                    the base benchmark, Transformer+LSTM and LiquidPure reach PR-
at the cost of a 100% false-alarm rate.                                                     AUC around 0.59, while LiquidMamba reaches 0.401. Calibration also
    This decision-level mode collapse is more operationally relevant                        exposes different operating points: Transformer+LSTM can reach 20%
than whether the average trajectory appears smooth. These results                           unsafe miss with 16.4% false alarm, while LiquidMamba reaches 30%
show that recurrent, attention, and hybrid sequence models occupy                           unsafe miss but with 49.3% false alarm. The base-benchmark five-seed
different regions of the safety-accuracy tradeoff: some preserve trajec-                    evaluation reported in Table 4 uses the four highest-PR-AUC methods
tory accuracy while suppressing rare unsafe excursions, while others                        from this single-seed pass, while the expanded-benchmark evaluation
become overly sensitive and alarm on nearly all scenarios. The safety-                      below uses the full seven-model baseline suite over five seeds to remove
aware metrics sharpen that observation. Mode collapse is not merely                         the seed-42 preselection confound entirely.
a visual artifact in predicted trajectories; it becomes a degenerate                            The single-seed ranking is not reliable. In the base-benchmark five-
operating policy when a regression model is converted into a binary                         seed evaluation of the top four methods, LiquidMamba has the highest
security decision.                                                                          mean PR-AUC at 0.408, but paired differences versus the other top
    The mechanism is consistent with gradient starvation on the unsafe                      methods are not statistically separated. Mean PR-AUC values are 0.408
tail: trajectory-regression loss is dominated by stable trajectories, so                    for LiquidMamba, 0.370 for LSTM, 0.361 for Transformer+LSTM, and

                                                                                        6
```

---

## PDF Page 7

```text
M. Shamseldein                                                                                                                               Energy and AI 25 (2026) 100811


                 Table 4
                 Base-benchmark five-seed auxiliary safety-head summary for the four methods selected from the seed-42 screening pass. Bootstrap
                 intervals resample seeds and should be read as robustness diagnostics rather than population guarantees; all paired PR-AUC and
                 F2-opt differences among the top four include zero.
                  Model                          PR-AUC          PR-AUC 95% CI            F2-opt      F2 95% CI             Unsafe miss       False alarm
                  LiquidMamba (tau-gate)         0.408           [0.257, 0.534]           0.532       [0.456, 0.608]        0.220             0.512
                  LSTM (History)                 0.370           [0.233, 0.506]           0.530       [0.459, 0.600]        0.300             0.422
                  Transformer+LSTM               0.361           [0.287, 0.476]           0.547       [0.487, 0.612]        0.440             0.241
                  LiquidPure (No History)        0.280           [0.122, 0.455]           0.489       [0.418, 0.576]        0.220             0.614


                 Table 5
                 Expanded-benchmark five-seed ML safety evaluation across all seven baselines (no seed-42 preselection). Panel A reports model-
                 level means. Panel B reports representative paired scenario-within-seed bootstrap PR-AUC differences using 2000 percentile
                 bootstrap replicates; all 21 pairwise PR-AUC intervals include zero, and F2-opt differences are zero by construction because
                 every method selects the all-unsafe hard decision (F2 = 0.647 = unsafe-base-rate F2). Zero-difference rows are retained to show
                 tied saved unsafe-score arrays for those model pairs. Panel C reports a test-set operating-point diagnostic: even when thresholds
                 are selected to maximize unsafe recall subject to false-alarm-rate budgets of 5%, 10%, and 20%, every method achieves zero
                 unsafe recall.
                  Panel A: Model-level means (seven models, five seeds each)
                  Model                                     PR-AUC                    F2-opt               Unsafe miss      False alarm   Nadir MAE (Hz)
                  Mamba+LSTM                                0.686                     0.647                0.000            1.000         0.123
                  LSTM (History)                            0.653                     0.647                0.000            1.000         0.124
                  LiquidPure (No History)                   0.653                     0.647                0.000            1.000         0.258
                  CNN-1D (Snapshot)                         0.630                     0.647                0.000            1.000         0.211
                  TCN (History)                             0.630                     0.647                0.000            1.000         1.091
                  Transformer+LSTM                          0.590                     0.647                0.000            1.000         0.101
                  LiquidMamba (tau-gate)                    0.568                     0.647                0.000            1.000         0.289
                  Panel B: Representative paired bootstrap PR-AUC differences
                  Comparison                                𝛥 PR-AUC                  95% CI               Interpretation
                  Mamba + LSTM − LiquidMamba                +0.032                    [−0.010, +0.082]     Not statistically separated
                  Mamba + LSTM − LSTM                       +0.006                    [−0.013, +0.036]     Not statistically separated
                  Mamba + LSTM − LiquidPure                 +0.006                    [−0.013, +0.036]     Not statistically separated
                  Mamba + LSTM − Transformer+LSTM           +0.036                    [+0.000, +0.092]     Borderline; CI touches zero
                  Mamba + LSTM − CNN-1D                     +0.016                    [−0.001, +0.063]     Not statistically separated
                  LSTM − LiquidPure                         +0.000                    [+0.000, +0.000]     Identical scores in this run
                  LSTM − LiquidMamba                        +0.025                    [−0.006, +0.076]     Not statistically separated
                  LiquidPure − LiquidMamba                  +0.025                    [−0.006, +0.076]     Not statistically separated
                  CNN-1D − TCN                              +0.000                    [+0.000, +0.000]     Identical scores in this run
                  Panel C: Fixed false-alarm-budget diagnostic
                  False-alarm budget                        Best mean unsafe recall   Mean unsafe miss     Models
                  5%                                        0.000                     1.000                All seven methods
                  10%                                       0.000                     1.000                All seven methods
                  20%                                       0.000                     1.000                All seven methods



0.280 for LiquidPure. All pairwise PR-AUC and F2-opt confidence                            validation-calibrated threshold. All 21 pairwise PR-AUC bootstrap in-
intervals include zero. Thresholded metrics show tradeoffs rather than                     tervals include zero; even the largest separation, Mamba+LSTM minus
dominance: LiquidPure and LiquidMamba have lower unsafe miss rates                         LiquidMamba at +0.032, has 95% CI [−0.010, +0.082]. Mamba+LSTM
but high false-alarm rates, while Transformer+LSTM has lower false                         has the highest mean PR-AUC, but it was not among the initial top-4
alarms but higher unsafe miss. Table 4 details the base-benchmark                          selected from seed 42, which directly illustrates the seed-42 preselec-
five-seed top-four summary.                                                                tion bias that the full seven-model run removes. Table 5 reports the
    This is the principal ML finding for the base benchmark. Safety                        complete model list, representative pairwise CIs, and the fixed-false-
supervision changes the apparent model landscape, but the data do                          alarm diagnostic, and Figs. 2 and 3 show the per-seed PR curves and
not support a robust architecture winner. The architecture ranked                          rank heatmap.
first depends on which seed is reported, which directly challenges                             LiquidMamba has the lowest mean PR-AUC among the seven base-
single-seed ML-DSA comparison claims.                                                      lines, but the paired CIs versus every other model include zero. This is
                                                                                           evidence against a LiquidMamba-centered claim, not evidence for a sta-
5.4. The expanded benchmark tests whether denser unsafe coverage stabi-                    tistically proven LiquidMamba disadvantage. Conversely, Mamba+LSTM
lizes ML rankings                                                                          has the highest mean PR-AUC at 0.686, but its CIs versus LSTM,
                                                                                           LiquidPure, CNN-1D, and TCN also include zero, so no statistically
    On the expanded dataset (820 scenarios spanning load-step and                          separable leading architecture is identified.
generator-output-loss classes), all seven ML baselines were trained over                       The more consequential expanded-benchmark result is decision-
five seeds without seed-42 preselection, which avoids the selection-bias                   threshold behavior. Despite mean PR-AUCs ranging from 0.568 to
confound of restricting the multi-seed comparison to top-4 candidates                      0.686 across the seven models, every model achieves an F2-opt of ex-
chosen on a single seed. The five-seed mean PR-AUC values span                             actly 0.647, the F2 of the trivial all-unsafe policy under the test unsafe
Mamba+LSTM at 0.686, LSTM at 0.653, LiquidPure at 0.653, CNN-1D                            base rate of 44/164 = 0.268. Every model therefore has unsafe miss rate
at 0.630, TCN at 0.630, Transformer+LSTM at 0.590, and LiquidMamba                         0.0 and false alarm rate 1.0 under the validation-calibrated F2-opt hard
(tau-gate) at 0.568. F2-opt is identical at 0.647 across all seven methods                 decision. A secondary test-set-calibrated target-recall analysis, which
because every model selects the trivial all-unsafe operating point at the                  eliminates validation-set mismatch by selecting thresholds directly on

                                                                                      7
```

---

## PDF Page 8

```text
M. Shamseldein                                                                                                                     Energy and AI 25 (2026) 100811




Fig. 2. Precision–recall curves for all seven auxiliary safety-head models on the expanded benchmark. Faint lines show individual training seeds and thick lines
show seed-averaged behavior. The dashed horizontal line is the unsafe-event base rate. Denser unsafe coverage improves ranking relative to the base benchmark,
but the methods remain statistically inseparable and hard-decision calibration selects all-unsafe policies.




Fig. 3. Seed-level ranking heatmap for all seven auxiliary safety-head models on the expanded benchmark. Cells report rank by PR-AUC for each training seed.
The ranking remains seed-sensitive, and paired bootstrap intervals do not support a statistically separable architecture winner.


the test scores, also selects all-unsafe decisions for every method and            geometry. The PR-AUC improvement therefore does not translate into
seed at 0.90 and 0.95 target recall.                                               an operationally useful operating point under F2-opt, target-recall, or
   An alarm-budget analysis reaches the same conclusion from the                   fixed-alarm-budget calibration.
opposite direction. When thresholds are selected directly on the test
scores to maximize unsafe recall subject to false-alarm-rate budgets
of 5%, 10%, or 20%, every ML method has mean unsafe recall 0.0                     5.5. Threshold sensitivity
across the five seeds. In these score distributions, the first threshold
that recovers unsafe cases also alarms on roughly half of the safe
cases. Monotone probability calibration, such as Platt scaling or iso-                The all-unsafe operating point could in principle be an artifact of
tonic calibration, can change probability values but cannot create a               the specific −0.1 Hz benchmark threshold. To test this, we re-derive
low-false-alarm operating point when the score ranking itself has this             unsafe labels at −0.05 Hz, −0.10 Hz, and −0.20 Hz directly from the

                                                                               8
```

---

## PDF Page 9

```text
M. Shamseldein                                                                                                                         Energy and AI 25 (2026) 100811


                 Table 6
                 Threshold sensitivity of the expanded-benchmark ML safety evaluation. For each candidate threshold, unsafe labels are re-derived
                 from the saved per-scenario true-nadir values, and metrics are recomputed on the existing seven-model five-seed score arrays
                 without retraining. Last column counts the number of models for which a majority of seeds still maximize F2 by predicting
                 all-unsafe.
                  Threshold (Hz)              Mean unsafe base rate             Mean F2-opt (across models)              Models selecting all-unsafe
                  −0.05                       0.635                             0.897                                    7/7
                  −0.10                       0.268                             0.647                                    7/7
                  −0.20                       0.030                             0.211                                    1/7


                 Table 7
                 Calibration-policy comparison on the expanded benchmark. Each cell reports mean unsafe recall (left) and mean false-alarm rate
                 (right) across five seeds, for one (model, policy) pair. F2-opt, target-recall (TR), and false-alarm-budget (FAR) policies are all
                 derived directly from the saved test scores without retraining. Across all seven models, every recall-prioritizing policy selects
                 all-unsafe decisions (recall = 1.0, FAR = 1.0), and every false-alarm-constrained policy selects zero-recall decisions.
                  Model                       F2-opt            TR90             TR95              FAR 5%           FAR 10%            FAR 20%
                  Mamba+LSTM                  1.000/1.000       1.000/1.000      1.000/1.000       0.000/0.000      0.000/0.000        0.000/0.000
                  LSTM (History)              1.000/1.000       1.000/1.000      1.000/1.000       0.000/0.000      0.000/0.000        0.000/0.000
                  LiquidPure (No History)     1.000/1.000       1.000/1.000      1.000/1.000       0.000/0.000      0.000/0.000        0.000/0.000
                  CNN-1D (Snapshot)           1.000/1.000       1.000/1.000      1.000/1.000       0.000/0.000      0.000/0.000        0.000/0.000
                  TCN (History)               1.000/1.000       1.000/1.000      1.000/1.000       0.000/0.000      0.000/0.000        0.000/0.000
                  Transformer+LSTM            1.000/1.000       1.000/1.000      1.000/1.000       0.000/0.000      0.000/0.000        0.000/0.000
                  LiquidMamba (tau-gate)      1.000/1.000       1.000/1.000      1.000/1.000       0.000/0.000      0.000/0.000        0.000/0.000



saved per-scenario true-nadir records, recompute PR-AUC and the test-                the dynamic simulation. Thus, even a statistical advantage would not
set-calibrated F2-opt operating point, and check whether the all-unsafe              prove path-dependent latent-state learning unless the simulator history
result persists at each threshold. No retraining is required.                        pathways were made causal and the result replicated.
    Table 6 reports the per-model summary at each threshold. At                         We therefore do not claim that 24-hour history captures latent stress
−0.05 Hz and −0.10 Hz, all seven models select the trivial all-unsafe                in the base benchmark. History-aware modeling remains a possible
operating point on a majority of seeds. At the much more selective                   future direction; it is not a demonstrated contribution of this dataset.
−0.20 Hz threshold, the unsafe base rate drops to a small minority
and only one of the seven models still maximizes F2 by predicting                    5.8. SFR applicability is scenario-class dependent
all-unsafe; the others avoid that specific operating point but still have
low absolute PR-AUC. The threshold-collapse finding is therefore robust                  The SFR evaluation intentionally excludes the bus-fault rows be-
across the operationally realistic threshold range and is not an artifact            cause no scalar active-power disturbance is available without leaking
of the chosen −0.1 Hz label.                                                         the post-event response. This is not a missing-metadata issue; it is a
                                                                                     model-applicability issue. Self-clearing bus faults remain useful for ML
5.6. Calibration-policy robustness                                                   benchmarking, but they are outside the clean aggregate SFR distur-
                                                                                     bance class unless a follow-on trip or topology change is recorded with
    The operational question is whether any post-hoc calibration policy              a defensible scalar disturbance proxy.
can recover a useful operating point from these score distributions. We                  The expanded benchmark therefore uses load-step and generator-
compute the operating point of every (model, seed) under six policies:               output-loss scenarios for SFR-evaluable comparisons. This creates a
F2-opt, target recall 0.90, target recall 0.95, and false-alarm budgets              matched physics benchmark without retrofitting SFR to scenarios where
5%, 10%, and 20%. The first three policies trade false alarms for                    its assumptions do not apply. In the expanded set, the SFR-compatible
recall; the last three constrain false alarms and report whatever recall             scenario classes contain 420 load-step scenarios and 400 generator-
remains. Together they bound the achievable operating-point space                    output-loss scenarios, with unsafe rates of 29.5% and 23.8%, respec-
under monotone score transformations.                                                tively.
    Table 7 reports mean unsafe recall and mean false-alarm rate by
(model, policy). Every model and every policy falls into one of two                  5.9. Expanded-benchmark SFR baselines expose model-class and information-
undesirable operating regimes: (i) under F2-opt, target-recall 0.90, and             set costs
target-recall 0.95, every method achieves unsafe recall 1.0 at the cost
of false-alarm rate 1.0, the trivial all-unsafe operating point; (ii) under              SFR-class baselines apply the physical nadir threshold directly to
false-alarm budgets of 5%, 10%, and 20%, every method achieves                       predicted nadir, bypassing the learned-calibration step that produced
zero unsafe recall, because the first threshold that begins to identify              the all-unsafe collapse in ML methods. This is one explicit operational
unsafe cases also alarms on a non-trivial fraction of safe cases. Since              advantage of physics-based decision rules in the rare-event regime.
these policies span the operationally useful boundary of monotone                        Table 8 reports per-variant nadir MAE for both SFR-compatible
calibration, and Platt and isotonic calibration both preserve the score              scenario classes.
ordering, no monotone calibration can repair the operating point on                      The headline pattern is consistent across classes: oracle accuracy
these scores.                                                                        is near 0.008–0.009 Hz, ambient DSE is about an order of magni-
                                                                                     tude worse, and 5 s event-triggered DSE matches oracle within about
5.7. History channels need causal validation                                         0.001 Hz. These values separate three information sets: a full-response
                                                                                     oracle upper bound, a pre-event ambient estimator, and an event-
    The data do not support the history-aware claim. LiquidPure, which               triggered estimator that commits after observing only the first part
has no history input, can match or exceed LiquidMamba in single-seed                 of the transient. SFR-oracle is used only as a model-class ceiling; the
safety ranking, and the five-seed benchmark does not statistically sepa-             operational comparisons are the ambient and event-triggered variants.
rate LiquidMamba from the no-history baseline. More importantly, the                     The ambient-PSD finding remains based on dedicated stochastic-
simulator audit shows that the history channels are not causal inputs to             load calibration scenarios rather than a full-dataset PSD survey, but

                                                                                 9
```

---

## PDF Page 10

```text
M. Shamseldein                                                                                                                    Energy and AI 25 (2026) 100811


                               Table 8
                               Expanded-benchmark SFR-family nadir MAE by scenario class. The table separates information
                               sets and estimator variants: full-response oracle, pre-event ambient DSE, event-triggered DSE,
                               noisy event-triggered DSE, and misspecified first-order event-window fits.
                                Variant                            Load-step MAE (Hz)            Generator-output-loss MAE (Hz)
                                SFR-oracle                         0.0076                        0.0090
                                Ambient SFR-DSE                    0.0798                        0.0706
                                Event-triggered 1 s                0.0134                        0.0165
                                Event-triggered 2 s                0.0131                        0.0146
                                Event-triggered 5 s                0.0071                        0.0077
                                Noisy event-triggered 1 s          0.0306                        0.0133
                                Noisy event-triggered 2 s          0.0191                        0.0177
                                Noisy event-triggered 5 s          0.0065                        0.0064
                                Misspecified first-order 1 s       0.0206                        0.0371
                                Misspecified first-order 2 s       0.0249                        0.1376
                                Misspecified first-order 5 s       0.0044                        0.0087




Fig. 4. Ambient center-of-inertia frequency-deviation PSD from the 300 s stochastic-load calibration scenario. The spectrum shows a persistent low-frequency
peak and an SFR-band peak after detrending, suggesting that ambient SFR-DSE may face multi-mode model-class mismatch. The figure is used as an identifiability
diagnostic rather than as a complete modal decomposition.


the expanded SFR batch confirms that the ambient estimator is weak at              sum is therefore not expected to be a stable per-system conversion
scale. Ambient SFR-DSE has nadir MAE 0.0754 overall, 0.0798 on load-               factor for every contingency.
step scenarios, and 0.0706 on generator-output-loss scenarios. This                    These findings are not implementation errors. They identify oper-
remains about an order of magnitude worse than 5 s event-triggered                 ational baseline risks that must be controlled before using enhanced
DSE, supporting the interpretation that pre-event ambient PSD fitting              SFR-DSE as a reference method: model-class mismatch, multi-mode am-
is limited by multi-mode response and effective-parameter identifiabil-            bient response, unstable effective-inertia anchoring, and early-window
ity. Fig. 4 shows the ambient COI frequency-deviation PSD from the                 identifiability.
calibration scenario, with a low-frequency peak and an SFR-band peak
that motivate the multi-mode interpretation.                                       5.10. Event-triggered SFR-DSE shows early-window identifiability costs
     We extend the nameplate-anchor analysis from the five-scenario
calibration subset to the full expanded SFR-compatible set. Across all                 Event-triggered SFR-DSE avoids both ambient PSD amplitude de-
SFR-oracle records, 𝑀oracle ∕𝑀nameplate,pretrip has mean 0.0090, median            pendence and nameplate-M anchoring by fitting effective parameters
0.0052, coefficient of variation 128.4%, and class-specific coefficients           from the measured early disturbance response. Fig. 6 reports the full 1
of variation 127.6% for load-step and 123.9% for generator-output-loss.            s, 2 s, and 5 s window sweep by scenario class.
This variability is far too large for a fixed per-system unit conversion               The headline pattern is monotone for the second-order event-trigg-
and supports the conclusion that effective SFR inertia is contingency-             ered estimator: 2 s improves on 1 s, and 5 s improves further. The noisy
dependent. Fig. 5 plots the per-scenario M-anchor ratios by scenario               event-triggered variants follow the same qualitative pattern: noise most
class and inertia regime.                                                          strongly affects the 1 s window, while 2 s and 5 s fits are less sensitive
     This instability is physically plausible. Aggregate nameplate inertia         because they contain more response information. The 5 s row reflects
sums stored kinetic energy across online machines, but an effective SFR            delayed nowcasting rather than early prediction: the nadir-forming
inertia fitted to a particular COI response depends on modal partic-               response is largely visible by 5 s, so the fit commits after observing
ipation: which machines swing coherently, which modes are excited                  most of the post-disturbance dynamics.
by the disturbance location and type, and how governor and network                     A five-scenario calibration subset showed a non-monotone relation-
dynamics shape the measured aggregate response. A single nameplate                 ship, where the 2 s estimator was worse than the 1 s estimator, but

                                                                              10
```

---

## PDF Page 11

```text
M. Shamseldein                                                                                                                          Energy and AI 25 (2026) 100811




Fig. 5. Effective SFR inertia from the oracle fit relative to pre-event aggregate nameplate inertia on the expanded benchmark. Points show 𝑀oracle ∕𝑀nameplate,pretrip
by scenario class and inertia regime. The broad spread indicates that nameplate aggregate inertia is not a stable per-system conversion factor for effective SFR
inertia.




Fig. 6. Nadir MAE for the SFR baseline family on the expanded benchmark, stratified by scenario class. The variants separate information sets: full-response
oracle, pre-event ambient DSE, event-triggered DSE, noisy event-triggered DSE, and misspecified first-order event-window fits.


that pattern does not persist at scale. The expanded-benchmark result                 observes only the first 𝜏 seconds of the measured center-of-inertia
is monotone in the expected direction: 2 s improves on 1 s, and 5 s                   frequency response (a derived observation channel with an explicit
improves further. The calibration-subset anomaly is therefore a small-                observation mask), with all later samples masked and with no fault
sample artifact, and the expanded-benchmark monotone trend is the                     location, disturbance magnitude, generator identity, or inertia value
main result.                                                                          provided. This information set is leak-free—the frequency nadir forms
    The misspecified first-order event-window model adds a parsimony                  several seconds after the disturbance, so the first 𝜏 seconds do not
test. Fig. 6 shows a sharp 2 s degradation for this first-order fit, even             include the final nadir or divergence outcome, and the model must
though the 5 s first-order envelope gives the best overall nadir MAE.                 infer severity from the early rate of change and slope. The measurement
The 2 s misspecified fit can lock onto a confidently wrong steady-state               window is aligned with the event-triggered SFR-DSE baseline, while
estimate when the window contains enough rising-edge information                      the SFR baseline also uses a characterized active-power disturbance;
to constrain the fit but not enough settling behavior to identify the                 the comparison is therefore explicit about the shared response window
envelope. The 5 s parsimony advantage observed in the calibration                     and the remaining input differences.
                                                                                          Under this event-triggered information set the all-unsafe collapse
subset persists in the overall mean and is sharpest on load-step sce-
                                                                                      largely disappears. Table 9 reports, for observation windows 𝜏 ∈
narios. The interpretation is not that the first-order model is physically
                                                                                      {0.5, 1.0, 2.0} s on all three systems, the number of the seven architec-
superior; it is that, once the nadir-forming trajectory is mostly observed
                                                                                      tures that collapse to an all-unsafe decision at the −0.10 Hz threshold
and overshoot is modest, a lower-variance two-parameter envelope can
                                                                                      and the mean unsafe recall achievable within a 20% false-alarm budget.
outperform a more flexible three-parameter second-order fit for nadir
                                                                                      Where the descriptor-based information set yielded zero unsafe recall
estimation.
                                                                                      at every false-alarm budget, the event-triggered information set yields
                                                                                      non-trivial operating points: on IEEE 39, two of seven models still
5.11. Event-triggered ML screening: A leak-free information set that avoids           collapse but the remainder reach 27%–39% unsafe recall at a 20%
collapse                                                                              false-alarm budget; on NPCC and WECC no models collapse at 𝜏 ≥
                                                                                      1 s and recall reaches 41% and 59% respectively. Recall increases
    The all-unsafe collapse documented above is established under a                   monotonically with the observation window on all three systems –
regression/descriptor information set: each model predicts the post-                  the expected early-warning-versus-delay tradeoff, since longer windows
event frequency trajectory from pre-event and event-descriptor inputs                 expose more of the nadir-forming response – mirroring the monotone
and derives a safety decision from the predicted nadir. A natural ques-               improvement of the event-triggered SFR-DSE physics estimator. The
tion is whether the collapse reflects a fundamental limit of artificial-              𝜏 = 2 s window approaches delayed nowcasting in the same sense as
intelligence-based DSA or the specific information set the model is                   the 5 s SFR-DSE fit, so 𝜏 ∈ {0.5, 1.0} s is the genuine early-warning
given. We therefore add an event-triggered information set: the model                 regime.

                                                                                 11
```

---

## PDF Page 12

```text
M. Shamseldein                                                                                                                       Energy and AI 25 (2026) 100811


                      Table 9
                      Event-triggered ML screening across systems and observation windows 𝜏 under a leak-free information set (only
                      the first 𝜏 s of the measured center-of-inertia frequency response; no disturbance descriptors). ‘‘Collapse’’ is the
                      number of the seven architectures producing an all-unsafe decision at the −0.10 Hz threshold on a majority of
                      seeds; ‘‘Recall@20%FAR’’ is the mean unsafe recall across architectures within a 20% false-alarm budget. The
                      descriptor-based information set yields zero recall at every budget, shown for reference.
                        System                     Metric                                  𝜏=0.5 s            𝜏=1.0 s            𝜏=2.0 s
                        IEEE 39                    Collapse @ −0.10 Hz (of 7)              2                  2                  2
                        IEEE 39                    Recall @ 20% FAR                        0.27               0.35               0.39
                        NPCC (140-bus)             Collapse @ −0.10 Hz (of 7)              0                  0                  0
                        NPCC (140-bus)             Recall @ 20% FAR                        0.30               0.41               0.41
                        WECC (179-bus)             Collapse @ −0.10 Hz (of 7)              2                  0                  0
                        WECC (179-bus)             Recall @ 20% FAR                        0.46               0.57               0.59



    This result reframes the benchmark’s message constructively.                     6. Conclusion
Artificial-intelligence-based DSA does not collapse because the task is
infeasible; it collapses when the model is asked to decide safety from                   DSA-SafetyBench is a benchmark and methodology contribution for
pre-event descriptors that do not pin down disturbance severity. Given               artificial-intelligence-based dynamic security assessment. It supplies a
an early measured response window aligned with the physics event-                    task definition, scoring protocol, per-scenario record format, repeated-
triggered estimator, common architectures recover usable, low-false-                 seed protocol, and reference baseline suite for testing whether machine-
                                                                                     learning models produce operationally meaningful security decisions.
alarm operating points, and they do so consistently across a 39-bus, a
                                                                                     Under that benchmark, regression-derived machine-learning safety de-
140-bus, and a 179-bus renewable-rich system. The constructive direc-
                                                                                     cisions can be degenerate even when trajectory metrics look accept-
tion for artificial-intelligence-based DSA is therefore an event-triggered
                                                                                     able. Explicit three-class safety supervision improves unsafe-event rank-
screening information set with explicit early-warning-versus-delay ac-
                                                                                     ing, but five-seed evaluation does not establish a statistically sepa-
counting, not a new architecture: the no-separable-winner finding also               rable architecture winner. On the expanded benchmark, denser un-
holds under the event-triggered information set, where at most five of               safe coverage improves unsafe-event ranking but still leads to all-
twenty-one pairwise PR-AUC intervals exclude zero on any system and                  unsafe hard decisions under recall-weighted F-score, target-recall, and
none do on NPCC.                                                                     fixed-alarm-budget analyses.
    We state two limits plainly. First, the collapse is reduced but not                  The simulator audit shows that the reported synthetic history fields
universally eliminated: at the lenient −0.05 Hz threshold, where the un-             are not causally wired into the transient simulator. Future history-
safe base rate is high, four of seven IEEE 39 models and all seven NPCC              aware DSA work therefore needs either repaired simulator pathways
models still collapse, so the constructive claim is threshold-dependent.             or measured operational histories where the causal connection is phys-
Second, the recovered operating points are usable rather than strong –               ically present.
IEEE 39 reaches 27%–39% unsafe recall at a 20% false-alarm budget                        The descriptor-based collapse is robust along two natural axes. The
depending on the window – so event-triggered ML screening is best                    full seven-model five-seed run on the expanded benchmark removes
treated as a complementary prioritization layer, not a replacement for               seed-42 preselection bias; no architecture separates statistically from
                                                                                     the others. Threshold sensitivity at −0.05 Hz, −0.10 Hz, and −0.20 Hz
physics-based assessment.
                                                                                     shows the all-unsafe collapse persists across the operationally realis-
                                                                                     tic threshold range and is not an artifact of the chosen label, and
5.12. Runtime and operational considerations                                         calibration-policy robustness across F2-opt, target recall 0.90 and 0.95,
                                                                                     and false-alarm budgets 5%–20% shows no monotone post-hoc cal-
                                                                                     ibration recovers a useful operating point from the descriptor-based
    The ML models are fast at inference once trained. On the expanded
                                                                                     scores.
benchmark, GPU batched per-sample inference time ranges from about                       The collapse is, however, information-set-dependent rather than
0.04 ms for LSTM and Transformer+LSTM to 0.56 ms for LiquidMamba                     fundamental to artificial-intelligence-based dynamic security assess-
on the evaluated workstation, excluding simulator and data-loading                   ment. Under a leak-free event-triggered information set – each model
time. The SFR event-triggered variants require little computation after              sees only the first 0.5–2 s of the measured center-of-inertia frequency
the measurement window is available; their limiting factor is not                    response, aligned with the event-triggered physics estimator’s mea-
numerical fit time but the observation delay. A 5 s event-triggered fit              surement window – the all-unsafe collapse is largely removed and
is near oracle quality in this benchmark, but it is a delayed nowcast                usable low-false-alarm operating points emerge across the IEEE 39,
rather than a preventive early-warning decision and may be too late                  NPCC, and WECC systems, subject to threshold- and system-dependent
for protection actions that operate on sub-second timescales.                        limits, with recall increasing monotonically as the observation win-
    The operational recommendation is therefore conservative. For                    dow lengthens. The benchmark’s constructive message is therefore
operators with reliable disturbance characterization and a validated                 that artificial-intelligence-based dynamic security assessment collapses
aggregate response model, SFR-class methods with explicit information-               when asked to decide safety from pre-event descriptors that do not
                                                                                     pin down disturbance severity, and that an event-triggered screening
set documentation remain the appropriate reference baseline for
                                                                                     information set with explicit early-warning-versus-delay accounting is
frequency-security screening. ML-based DSA is better treated as a
                                                                                     the path on which common architectures become operationally useful.
complementary screening or prioritization layer until it demonstrates
                                                                                         The physics baselines add the other side of the same message.
stable low-false-alarm unsafe recall under multi-seed, safety-aware
                                                                                     Swing-frequency-response-class methods have explicit scenario-class
evaluation. Scaling to larger systems would require revalidating SFR-                and information-set limits, and enhanced dynamic state estimation
compatibility constraints, disturbance definitions, and per-system stress            is not trivial in practice: ambient estimation remains weak, name-
envelopes before transferring any benchmark conclusions. Deployment                  plate inertia is an unstable effective-parameter anchor, and event-
would also require bad-data handling, PMU/SCADA time-alignment                       triggered estimation approaches oracle quality only when the oper-
checks, missing-measurement logic, and validation on the target system               ator can wait long enough to observe most of the nadir-forming re-
rather than direct transfer of the IEEE 39-bus numerical rankings.                   sponse. Together, the base and expanded benchmark results show that

                                                                                12
```

---

## PDF Page 13

```text
M. Shamseldein                                                                                                                      Energy and AI 25 (2026) 100811


machine-learning dynamic-security claims require safety-aware met-                   8. Reproducibility
rics, multi-seed uncertainty estimates, threshold reporting, and physics-
baseline information-set accounting before operational superiority over                  The expanded benchmark uses ANDES 2.0.0 with the built-in IEEE
physics methods can be defended.                                                     39-bus case name IEEE 39. The ML split is 60/20/20 train/valida-
                                                                                     tion/test, and the five training seeds are 7, 42, 99, 123, and 2025. The
                                                                                     expanded benchmark contains 820 scenarios, with 420 load-step and
7. Limitations
                                                                                     400 generator-output-loss cases; the test split contains 164 scenarios,
                                                                                     including 44 unsafe cases.
    The descriptor-based reference benchmark, with its full ambient                      The evaluated workstation uses an AMD Ryzen 7 8845HS CPU
SFR-DSE physics family, is on the IEEE 39-bus system. NPCC (140-                     with 8 cores and 16 logical processors, 42 GB system memory, and
bus) and WECC (179-bus, renewable-rich) enter as external systems for                an NVIDIA GeForce RTX 4070 Laptop GPU. Per-sample ML inference
the leak-free event-triggered comparison, not as full descriptor-based               times on the expanded test set are approximately 0.04 ms for LSTM and
or ambient-SFR replications. Their streams are deliberately scoped: a                Transformer+LSTM, 0.31 ms for LiquidPure, and 0.56 ms for Liquid-
single governor-agnostic disturbance class each – generator-trip for                 Mamba. The artifact package includes per-scenario ML records for both
NPCC and load-step at convergence-screened buses for WECC, be-                       the top-four base-benchmark run and the full seven-model expanded-
cause the generator-output-loss generator requires a TGOV1N governor                 benchmark run, SFR-family records, calibrated thresholds, the paired
model that neither system provides – together with short ambient                     scenario bootstrap script, threshold-sensitivity and calibration-policy
windows and no ambient SFR-DSE family. The cross-system event-                       comparison scripts that operate on the saved per-scenario records
triggered result should therefore be read as protocol-level external                 without retraining, figure scripts, scenario manifests, a prediction-
validation under a common early-response information set rather than                 record schema, a benchmark scoring script, and a case-inventory file
as a complete multi-system benchmark. NPCC’s unsafe events are ad-                   documenting which ANDES systems are reported, screened, or future
ditionally concentrated in the largest generator trips, which limits                 extensions.
unsafe-class diversity on that system. Extending any system to a full                    For reference, the true nadir score on the base-benchmark seed-42
descriptor-based and ambient-SFR benchmark would require a cali-                     test split achieves PR-AUC 0.722 and F2-opt 0.833, confirming that the
brated stress envelope, split manifest, and SFR-compatibility audit of               safety labels are recoverable from an accurate nadir signal even though
                                                                                     learned regression-derived scores lose the unsafe-event ranking.
the kind already completed for IEEE 39.
    The constructive event-triggered result is threshold-dependent. At
the lenient −0.05 Hz threshold the all-unsafe collapse partially returns             CRediT authorship contribution statement
(four of seven IEEE 39 models and all seven NPCC models), and the
recovered IEEE 39 unsafe recall is modest (27%–39% at a 20% false-                       Mohamed Shamseldein: Writing – review & editing, Writing –
alarm budget, depending on the observation window). Event-triggered                  original draft, Visualization, Validation, Software, Resources, Project
ML screening is therefore a complementary prioritization layer that                  administration, Methodology, Investigation, Formal analysis, Data cu-
benefits from a longer observation window at the cost of decision delay,             ration, Conceptualization.
not a standalone replacement for physics-based assessment.
                                                                                     Declaration of Generative AI and AI-Assisted Technologies in the
    The base benchmark study uses five random seeds. That is sufficient
                                                                                     Manuscript Preparation Process
for the paper’s negative claim that the available data do not support
a statistically separable architecture winner. Five seeds may not be
                                                                                         During the preparation of this work, the author used OpenAI
sufficient for a strong positive claim in datasets where architectures
                                                                                     Codex/ChatGPT to assist with language editing, LaTeX formatting, code
separate cleanly; additional seeds are warranted in those settings. The
                                                                                     review, and drafting of analysis scripts. After using this tool, the author
paired bootstrap also treats scenarios as exchangeable within each seed
                                                                                     reviewed and edited the content as needed and takes full responsibility
after stratified splitting. Scenarios that share a disturbance class, inertia
                                                                                     for the content of the published article.
regime, or source bus/generator are not fully independent physical
experiments. Class-stratified reporting partly mitigates this issue, but
                                                                                     Funding statement
a block bootstrap by disturbance class or operating regime would be
more conservative in larger follow-on studies.
                                                                                         This research did not receive any specific grant from funding agen-
    The SFR-DSE conclusions are based on the expanded SFR-compatible
                                                                                     cies in the public, commercial, or not-for-profit sectors.
IEEE 39-bus stream under load-step and generator-output-loss distur-
bances. They do not generalize to bus faults, protection-driven topology
                                                                                     Declaration of competing interest
changes, or other systems without repeating the same disturbance-
compatibility and DSE-identifiability checks. The ambient PSD inter-
pretation also remains an interpretive check rather than a full modal                    The authors declare that they have no known competing finan-
                                                                                     cial interests or personal relationships that could have appeared to
identification. The observed low-frequency and SFR-band peaks suggest
                                                                                     influence the work reported in this paper.
multi-mode response, but confirming their modal origin would require
small-signal eigenanalysis and participation-factor analysis of the spe-
cific ANDES case. The present paper uses the PSD result to motivate                  Appendix A. Supplementary data
SFR-DSE caution, not to claim a complete modal decomposition.
    Finally, all scenarios are generated in the open-source ANDES                        Supplementary material related to this article can be found online
dynamic-simulation environment. Operational systems may differ be-                   at https://doi.org/10.1016/j.egyai.2026.100811.
cause of protection coordination, governor and AGC implementation
details, measurement quality, topology changes, and operator proce-                  Data availability
dures. The contribution is therefore a reproducible benchmark and
evaluation framework, not a claim that the exact numerical rankings                     Data will be made available on request.
will transfer unchanged to deployed control rooms.

                                                                                13
```

---

## PDF Page 14

```text
M. Shamseldein                                                                                                                                    Energy and AI 25 (2026) 100811


References                                                                                   [16] Lechner M, Hasani R, Amini A, Henzinger TA, Rus D, Grosu R. Neural circuit
                                                                                                  policies enabling auditable autonomy. Nat. Mach. Intell. 2020.
 [1] Babaeinejadsarookolaee S, Birchfield A, Christie R, Coffrin C, DeMarco C,               [17] Gu A, Dao T. Mamba: linear-time sequence modeling with selective state spaces.
     Diao R, et al. The power grid library, for benchmarking ac optimal power flow                2023, arXiv preprint arXiv:2312.00752.
     algorithms. 2019, arXiv:1908.02788.                                                     [18] Gu A, Goel K, Re C. Efficiently modeling long sequences with structured state
 [2] Marot A, Donnot B, Romero C, Veyrin-Forrer L, Lerousseau M, Donon B, et al.                  spaces. 2021, arXiv preprint arXiv:2111.00396.
     Learning to run a power network challenge for training topology controllers. In:        [19] Kundur P. Power System Stability and Control. New York, NY, USA: McGraw-Hill;
     Proceedings of Machine Learning Research. 2020.                                              1994.
 [3] Fan TH, Lee XY, Wang Y. Powergym: a reinforcement learning environment                  [20] Anderson P, Mirheydar M. A low-order system frequency response model. IEEE
     for volt-var control in power distribution systems. In: Proceedings of Machine               Trans Power Syst 1990;5(3):720–9.
     Learning Research. 2022.                                                                [21] Zhao J, Gomez-Exposito A, Netto M, Mili L, Abur A, Terzija V, et al. Power
 [4] Sarajcev P, Kunac A, Petrovic G, Despalatovic M. Ieee new england 39-bus test                system dynamic state estimation: Motivations, definitions, methodologies, and
     case: dataset for the transient stability assessment. 2022, Zenodo.                          future work. IEEE Trans Power Syst 2019;34(4):3188–98.
 [5] Giraud B, Charles L, Nakiganda AM, Vorwerk J, Chatzivasileiadis S. A dataset            [22] Liu Y, Singh A, Zhao J, Meliopoulos A, Pal B, Ariff M, et al. Dynamic state
     generation toolbox for dynamic security assessment: on the role of the security              estimation for power system control and protection. IEEE Trans Power Syst
     boundary. 2025, arXiv:2501.09513.                                                            2021;36(6):5909–21.
 [6] Cuevas M, Alvarez-Malebran R, Rahmann C, Ortiz D, Pena J, Rozas-                        [23] Davis J, Goadrich M. The relationship between precision–recall and roc curves.
     Valderrama R. Artificial intelligence techniques for dynamic security                        In: Proceedings of the 23rd international conference on machine learning. 2006,
     assessments–a survey. Artif Intell Rev 2024;57:340.                                          p. 233–40.
 [7] Alimi O, Ouahada K, Abu-Mahfouz A. A review of machine learning approaches              [24] Saito T, Rehmsmeier M. The precision–recall plot is more informative than the
     to power system security and stability. IEEE Access 2020;8:113512–31.                        roc plot when evaluating binary classifiers on imbalanced datasets. PLoS One
 [8] Qi H, Su R, Li C, Ren Z, Wang Y, Xu M, et al. A review on dynamic                            2015;10(3):e0118432.
     security assessment of power system based on machine learning. In: 2023 7th             [25] Niculescu-Mizil A, Caruana R. Predicting good probabilities with supervised
     International Conference on Power and Energy Engineering (ICPEE). 2023, p.                   learning. In: Proceedings of the 22nd international conference on machine
     173–8.                                                                                       learning. 2005, p. 625–32.
 [9] Shi Z, Yao W, Zeng L, Wen J, Fang J, Ai X, et al. Convolutional neural                  [26] Geifman Y, El-Yaniv R. Selective classification for deep neural networks. In:
     network-based power system transient stability assessment and instability mode               Advances in Neural Information Processing Systems. 2017, p. 30.
     prediction. Appl Energy 2020;263:114586.                                                [27] Angelopoulos AN, Bates S. A gentle introduction to conformal prediction and
[10] Huang R, Chen Y, Yin T, Huang Q, Tan J, Yu W, et al. Application of graph                    distribution-free uncertainty quantification. 2021, arXiv:2107.07511.
     convolutional networks to power system dynamics. 2021, arXiv preprint arXiv:            [28] Zarei E, Yazdi M, Moradi R, BahooToroody A. Expert judgment and uncertainty
     2103.15049.                                                                                  in sociotechnical systems analysis. In: Zarei E, editor. In: Safety causation
[11] Hochreiter S, Schmidhuber J. Long short-term memory. 1997,                                   analysis in sociotechnical systems: advanced models and techniques, Studies in
[12] Vaswani A, Shazeer N, Parmar N, Uszkoreit J, Jones L, Gomez N, et al. Attention              Systems, Decision and Control, vol. 541, Cham: Springer; 2024, p. 487–530.
     is all you need. In: Advances in neural information processing systems. 2017.                http://dx.doi.org/10.1007/978-3-031-62470-4_18.
[13] Bai S, Kolter JZ, Koltun V. An empirical evaluation of generic convolutional            [29] Yazdi M, Zarei E, Adumene S, Abbassi R, Rahnamayiezekavat P. Uncertainty
     and recurrent networks for sequence modeling. In: International Conference on                modeling in risk assessment of digitalized process systems. In: Methods in
     Learning Representations. 2018.                                                              Chemical Process Safety, vol. 6, Elsevier; 2022, p. 389–416. http://dx.doi.org/
[14] Chen RT, Rubanova Y, Bettencourt J, Duvenaud DK. Neural ordinary differential                10.1016/bs.mcps.2022.04.005.
     equations. In: Advances in neural information processing systems. 2018.
[15] Hasani R, Lechner M, Amini A, Rus D, Grosu R. Liquid time-constant networks.
     In: Proceedings of the AAAI conference on artificial intelligence. 2021.




                                                                                        14
```
