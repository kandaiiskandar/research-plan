# Cost-sensitive security controls for continuous integration pipelines

> **Source PDF:** `Cost-sensitive security controls for continuous integration pipelines.pdf` · **Pages:** 16 · Converted by `scripts/paper2md.py` from the original PDF. **Equations are extracted glyph-by-glyph and may be mangled — check the PDF before quoting any formula.**

<!-- page 1 -->

Computers & Security 171 (2026) 105124

Contents lists available at ScienceDirect

Computers & Security

journal homepage: www.elsevier.com/locate/cose

Full Length Article

Cost-sensitive security controls for continuous integration pipelines

The-Vinh Nguyen

Thai Nguyen University of Information and Communication Technology, Vietnam

### A R T I C L E I N F O

### A B S T R A C T

CI security controls combine contract, semantic, policy, provenance, dependency, and review evidence before release. Binary gates are difficult to tune: low thresholds interrupt benign changes, while high thresholds allow residual security risk to pass. This study evaluates a cost-sensitive decision framework that aggregates stage evidence and selects thresholds under explicit trade-offs among escaped risk, bad-block rate, and review load. The evaluation uses a deterministic campaign with 960 integration changes, 60 seeded replicates across eight stress profiles, a REST interface check, and a retrospective publication-cohort audit of 32,281 GitHub-reviewed security advisories linked to the CISA Known Exploited Vulnerabilities catalog. In the deterministic campaign, threshold 5 holds changes containing 99.35% of generated risk with one false block; across seeded campaigns, mean held-change risk coverage is 99.30% under baseline conditions. At 1% faulty-change prevalence, trans­ ported mean precision is 77.7% at threshold 5 and 29.0% at threshold 3. Stratified score permutation reduces threshold-5 held-change risk coverage to 65.25%, exposing dependence on the generator’s score ordering. In the advisory audit, a balanced unweighted point covers 96.23% of observed KEV risk at 48.58% review share, while a review-limited regularized point covers 62.26% at 3.45%. Current EPSS is stronger on the matched CVE subset, so the audit demonstrates cross-domain risk–workload analysis rather than validating the CI gate or establishing scoring superiority. The results support explicit, locally validated operating points rather than universal thresholds.

Dataset link: https://github.com/ictu-se/risk- calibrated-security-gates-replication

Keywords: DevSecOps Continuous integration Cost-sensitive classification Security gates Software supply chain

## 1. Introduction

tests detect seeded behavioral changes (Offutt et al. 1996). Directed random testing, grammar-based fuzzing, and symbolic execution expand the explored input space (Godefroid et al. 2005, 2008; Cadar et al. 2008). Search-based generation automates test construction (Fraser and Arcuri 2011). REST API fuzzing and access-control policy testing extend these ideas to services and authorization rules (Atlidakis et al. 2019; Pretschner et al. 2008; Martin et al. 2006). These techniques improve the chance that a fault becomes observable. They do not, by themselves, define when heterogeneous evidence from multiple stages is severe enough to block a CI change.

Modern software delivery pipelines increasingly operate as security- control points rather than as simple build scripts. Security-assurance and practitioner studies treat verification as a lifecycle activity and show that selecting, integrating, and maintaining controls remain organiza­ tional challenges (Shukla et al., 2022; Sinan et al. 2025). Software-supply-chain research adds provenance and dependency -integrity obligations (Newman et al. 2022; Torres-Arias et al. 2019; Gokkaya et al. 2026). API-facing systems add contract, authentication, and authorization checks; peer-reviewed REST testing and security studies show that these obligations expose distinct behavioral and access-control failures (Atlidakis et al. 2019; Santos Filho et al. 2025). A single integration change can therefore trigger contract checks, semantic checks, security scans, policy checks, provenance checks, dependency checks, and review or adjudication stages.

Vulnerability-prioritization research addresses another part of the problem by distinguishing severity from observed exploitation and by showing that neither signal alone fully represents operational risk (Allodi and Massacci 2014; Jacobs et al. 2021; Mell et al. 2024). Recent security-control and supply-chain studies also emphasize repeatable controls, traceability, release integrity, and the difficulty of maintaining controls across the software lifecycle (Sinan et al. 2025; Skandylas and Asplund 2025; Tang et al. 2025; Gokkaya et al. 2026). Those studies justify risk-sensitive decisions, but they do not give an empirical oper­ ating frontier for a CI gate that must trade escaped risk against bad-block

Existing software-testing research gives strong techniques for pro­ ducing evidence, but it leaves a separate decision problem for the pipeline gate. Model-based testing defines behavior models and ex­ pected outputs (Utting et al. 2012). Mutation testing evaluates whether

E-mail address: vinhnt@ictu.edu.vn.

https://doi.org/10.1016/j.cose.2026.105124 Received 7 July 2026; Received in revised form 24 July 2026; Accepted 17 August 2026

Available online 25 August 2026 0167-4048/© 2026 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

<!-- page 2 -->

rate, review capacity, and drift. In practice, teams often collapse evi­ dence into warning counts, severity labels, or fixed pass–fail rules. Such rules are hard to justify when evidence stages differ in fault coverage, false-positive behavior, and review cost.

without changing the paper’s central object: the release decision made after heterogeneous assurance evidence has been produced.

## 2. Related work

The gap addressed here is the cost-sensitive decision layer between security-test evidence and release blocking. Prior work has focused mainly on test adequacy and generated evidence (Bertolino 2007; Utting et al. 2012; Offutt et al. 1996), service exploration (Atlidakis et al. 2019), or policy-coverage measurement (Pretschner et al. 2008; Martin et al. 2006); this paper asks how a gate aggregates evidence once contract, semantic, security, policy, provenance, dependency, and adjudication stages have produced signals. The novelty is the combi­ nation of four elements in one empirical study: a multi-stage risk-score model for integration changes; threshold operating points that report escaped risk, bad-block rate, review load, and prevalence-sensitive precision; robustness analyses across bootstrap resampling, seeded campaigns, domains, periods, stress profiles, and generator-coupling perturbations; and stage ablations and aggregator comparisons that test distinct marginal risk coverage. A retrospective advisory audit separately demonstrates how the same cost-sensitive analysis describes a cross-domain prioritization task with observed-exploitation labels. This is a cost-sensitive decision problem rather than a new scanner, fuzzer, or policy language.

Security and reliability testing research provides the first foundation for this study: failures become observable only when a test has an input model and an oracle that match the relevant fault class (Bertolino 2007; Whittaker 2000). Model-based testing makes the model explicit by deriving test obligations from behavioral specifications (Utting et al. 2012). Mutation testing takes a complementary view: it evaluates whether a suite distinguishes the original program from seeded behav­ ioral changes (Offutt et al. 1996). These traditions motivate the bench­ mark’s injected-fault design, but they primarily assess whether evidence can be produced. They do not define how a CI gate converts a hetero­ geneous set of evidence items into a release-blocking decision.

Automated test generation and program exploration broaden the evidence available to a pipeline. Directed random testing and grammar- based whitebox fuzzing combine generated inputs with execution feedback (Godefroid et al. 2005, 2008). Symbolic execution systems such as KLEE generate high-coverage tests by solving path constraints (Cadar et al. 2008). Search-based test generation automates suite con­ struction using fitness objectives (Fraser and Arcuri 2011). REST API fuzzing adapts these ideas to stateful service interfaces and request se­ quences (Atlidakis et al. 2019). These approaches expand pre-release fault discovery, but their output is still evidence: failing requests, alerts, coverage signals, or counterexamples. A pipeline gate must still decide whether the combined evidence justifies blocking a change, reviewing it, or allowing it to proceed.

This paper studies cost-sensitive security gates for integration pipe­ lines using a controlled benchmark of changes to integration contracts and pipeline artifacts. Each change may contain schema, semantic, se­ curity, policy, provenance, dependency, or ambiguous faults. Each assurance stage emits an evidence score and adjudication burden. A change whose accumulated score exceeds the threshold is held for re­ view; because release does not proceed until review, the benchmark treats it as blocked pending review. Because the benchmark is gener­ ated, the evaluation distinguishes stability within the simulator from evidence validity outside it and examines precision under alternative deployment prevalences (Davis and Goadrich 2006; Saito and Rehmsmeier 2015). The study asks five questions:

Access-control and API-policy work provides a second foundation. RBAC separates users, roles, permissions, and sessions; ABAC general­ izes authorization decisions through subject, object, action, and envi­ ronment attributes (Sandhu et al. 1996; Ferraiolo et al. 2001; Servos and Osborn 2017). Policy-testing research then studies coverage and oracle design for authorization rules (Pretschner et al. 2008; Martin et al. 2006). REST API research further separates interface conformance, stateful exploration, and object-level authorization failures (Atlidakis et al. 2019; Santos Filho et al. 2025). This literature explains why con­ tract, policy, and authorization evidence must be separated, but it does not evaluate a multi-stage CI threshold that also contains semantic, dependency, provenance, and adjudication signals.

RQ1: How do gate thresholds trade off held-change risk coverage, escaped risk, bad-block rate, review load, and precision under alternative faulty-change prevalences? RQ2: How stable are selected thresholds across bootstrap resam­ pling, seeded benchmark variation, domains, periods, and stress profiles, and how strongly are the results coupled to the generator? RQ3: Which evidence stages contribute distinct marginal risk coverage, and do alternative aggregators change the simulated frontier? RQ4: How do capacity limits, period-held-out transfer, and cost as­ sumptions change threshold selection? RQ5a: Does the gate interface remain feasible when evidence crosses a local REST service boundary? RQ5b: Do declared cost profiles produce distinct risk–workload operating points in a retrospective advisory-level demonstration with observed KEV outcomes?

Risk and secure-development research provides a third foundation. Empirical vulnerability studies distinguish severity from exploitation evidence and show why prioritization requires more than a nominal severity label (Allodi and Massacci 2014; Jacobs et al. 2021; Mell et al. 2024). Security-assurance, software-supply-chain, and control-integration studies translate this concern into repeatable veri­ fication, traceability, provenance, and dependency-integrity activities (Shukla et al. 2022; Newman et al. 2022; Torres-Arias et al. 2019; Gokkaya et al. 2026; Sinan et al. 2025). Recent security-engineering studies also examine automated security testing and pre-integration patch risk assessment (Skandylas and Asplund 2025; Tang et al. 2025). These sources motivate risk-sensitive pipeline controls; they are not empirical gate-decision methods. They do not report how held-change risk coverage, escaped risk, false-positive rate, and review load change as a CI threshold moves.

The evaluation contains a deterministic campaign with 960 inte­ gration changes and 1865 injected fault events, plus a seeded campaign with 60 replicate benchmarks, eight stress profiles, and 4800 threshold evaluations. The paper makes four contributions. First, it defines a cost- sensitive gate model for multi-stage integration assurance. Second, it reports threshold frontiers that expose the trade-off among held-change risk coverage, escaped risk, bad-block rate, review load, and prevalence- sensitive precision. Third, it evaluates stability through bootstrap in­ tervals, seeded campaigns, domain and period breakdowns, stress pro­ files, and generator-coupling perturbations. Fourth, it provides capacity analysis, period-held-out simulation, cost sensitivity, evidence-stage ablations, aggregator comparisons, and a retrospective cross-domain advisory demonstration. These additions qualify the operating frontier

Deployment ecosystems also include policy-as-code mechanisms such as OPA/Rego and supply-chain assurance schemes such as SLSA. Peer-reviewed work on Sigstore and in-toto provides the related signing and provenance evidence (Newman et al. 2022; Torres-Arias et al. 2019). Recent studies further catalog software-supply-chain risks, inte­ grate automated security and compliance analysis into DevSecOps pipelines, and evaluate policy-driven isolation in enterprise delivery environments (Gokkaya et al. 2026; Achbarou et al. 2026; Bhatnagar 2026). These systems and studies strengthen the evidence-producing and enforcement layers; the present work instead evaluates the

<!-- page 3 -->

cost-sensitive release decision made after such controls emit heteroge­ neous evidence.

p(F, W, E|X) = p(F|X) p(W|F, X) p(E|F, X).

Operational reliability work adds another relevant constraint. Flaky- test research shows that automated signals can vary across executions and environments, while debugging work emphasizes the connection between observed symptoms and actionable causes (Bell et al. 2018; Zeller 2002). For CI security gates, this means a threshold cannot be evaluated only by mean detection performance. It also requires lower-tail behavior under stress, stability across benchmark slices, and evidence-stage ablations that indicate which signal family drives the decision.

Context contains domain, change type, criticality, churn, and tem­ poral period. It first controls fault occurrence, count, family, and severity; fault family and severity then affect both the risk proxy and stage evidence. Period and stress profiles alter the fault mix, detection probability, and false-positive behavior. Thus W and E are conditionally coupled through the same generated faults rather than independently observed, which is the circularity tested in RQ2.

The generator first samples fault occurrence, count, family, and severity from fixed profiles conditioned on change type, criticality, churn, and period. Each faulty change contains one–eight events on a five-level severity scale. For stage s and fault family f, a declared 7 × 7 coverage matrix Psf controls detection, while a corresponding signal matrix Msf, severity, period, stress, and deterministic hash-derived variation determine evidence magnitude. False-positive evidence is generated separately for non-faulty changes. This sequence makes the score–outcome coupling explicit without treating simulated stage behavior as measured tool accuracy.

The present study is positioned at the intersection of these lines of work. It assumes that specialized testing, scanning, policy, dependency, provenance, and adjudication stages can produce evidence. Its object of study is the cost-sensitive decision that follows: how to set and evaluate thresholds over heterogeneous evidence streams. The contribution therefore differs from a new fuzzer, authorization model, or vulnera­ bility score. It provides an empirical gate framework with operating frontiers, seeded and stress analysis, capacity and cost sensitivity, stage ablations, aggregator comparisons, and a separate advisory-level demonstration of the cost-sensitive analysis.

All profiles, bounds, multipliers, matrices, and seed salts were fixed design constants; they were not estimated from an organization, refitted during analysis, or optimized against the reported frontier. Their role is to encode controlled specialization and stress counterfactuals. The public replication package supplies the exact executable parameteriza­ tion and frozen-output checks, while the manuscript reports the de­ pendency structure and parameter provenance needed to interpret the results.

## 3. Cost-Sensitive gate model

Let c be an integration change and A be the set of assurance stages. In the benchmark, A contains contract, semantic, security, policy, provenance, dependency, and adjudication stages. Each stage s ∈A emits a non-negative evidence score es(c) and adjudication burden qs(c). The gate score is

## 4. Experimental design

∑

R(c) =

es(c).

### 4.1. Controlled simulation benchmark

s∈A

A threshold t holds a change for review when R(c) ≥t; the bench­ mark records this intervention as blocked pending review. The scores are non-probabilistic evidence magnitudes, so threshold selection is not probability calibration. The unweighted sum is compared with a fixed weighted sum, normalized sum, maximum-stage score, alert count, mandatory-core-stage rule, security-stage-only rule, change-criticality rule, regularized cost-sensitive combiner, and a label-derived fault- severity oracle. The fixed weights follow the simulator’s predeclared primary-stage signal magnitudes and are rescaled to mean one; they are not fitted to outcomes. The oracle is reported only as an unattainable upper bound because it uses injected-fault severity. Normalization and model fitting use only the selection partition, and the public replication package records every evaluated configuration.

The deterministic campaign is a controlled simulation, not an observed CI dataset. It contains 960 generated integration changes across six domains: civil registry, social benefits, public health, educa­ tion, land administration, and open data. Four temporal periods model baseline behavior, policy bursts, dependency bursts, and semantic drift. Table 2 summarizes 615 faulty changes, 345 non-faulty controls, 1865 injected fault events, and total simulated risk weight of 16,395.47. The resulting 64.06% faulty-change prevalence is deliberately fault-rich and is not treated as representative of a live pipeline.

Fault events are assigned to seven families: schema, semantic, se­ curity, policy, provenance, dependency, and ambiguous faults; Table 1 reports their deterministic-campaign composition. Fault type and severity determine the simulated risk weight, while fault type, severity, and stage-specific coverage determine evidence magnitude. The gener­ ator therefore couples the evaluation target to the predictor by con­ struction. Seeded replication measures stability within this data- generating process; it does not remove the coupling or establish external validity. The association is quantified directly, and weight and score permutations determine how much of the held-change risk frontier depends on it.

The seventh stage deterministically models structured adjudication of ambiguous and cross-cutting evidence; no language model is invoked. Its detection, score, and false-positive behavior follow the same seeded generation process as the other simulated stages.

Risk weight is assigned at fault-event level. Each injected fault v has a type, severity, and domain multiplier. Service criticality affects the generated fault rate and can raise the severity of security and policy events before weighting. The benchmark uses a controlled multiplica­ tive form:

### 4.2. Seeded stress campaign

```math
w(v) = b(typev) × g(severityv) × d(domainv),
```

The extended campaign generates 60 seeded simulation replicates. Each replicate contains 960 changes, while domain, change type, fault count, fault type, severity, detection, and false-positive draws vary through deterministic seed salts. Table 2 reports the resulting variation: fault events have mean 1939.67 with a p05–p95 interval of 1874.25–2049.05. The campaign evaluates eight stress profiles per seed: baseline, semantic drift, noisy policy, dependency burst, adjudication constrained, compound drift, strict adjudication, and high-noise low- signal. With ten thresholds, this produces 4800 threshold evaluations.

where b is the base weight for the fault family, g scales by severity, and d scales by domain criticality. The formula is not a substitute for CVSS or organization-specific risk scoring. It is a controlled proxy that follows the same separation of fault impact and context used in security-scoring practice.

The generator is deterministic: named salts, record identifiers, and a seed prefix are hashed to reproduce every draw and the 60 campaigns. Let X denote change context, F the generated fault records, W their risk weights, and E the stage evidence. Its dependency structure is

<!-- page 4 -->

**Table 1 Fault-family composition in the deterministic campaign; risk share is a percentage.**

**Table 2 Deterministic scale and seeded-campaign variation. Parentheses give p05–p95 across 60 seeded campaigns.**

Fault family Events Mean severity Risk share

Scope Measure Value/mean p05–p95

Security 284 4.11 22.54 Policy 318 4.01 22.11 Semantic 400 3.16 21.85 Provenance 273 3.73 13.66 Dependency 246 3.00 9.31 Schema 205 3.01 6.33 Ambiguous 139 3.00 4.20

Deterministic Integration changes 960 – Deterministic Faulty changes 615 – Deterministic Safe changes 345 – Deterministic Fault events 1865 – Deterministic Total risk weight 16,395.47 – Seeded Faulty changes 639.57 620.95–661.05 Seeded Safe changes 320.43 298.95–339.05 Seeded Fault events 1939.67 1874.25–2049.05 Seeded Total risk weight 17,001.32 16,290.83–17,921.39

### 4.3. Interface feasibility check

only on selection-cohort evidence and KEV outcomes provides an alternative aggregation. The combiner uses the observed-label conven­ tion, encoding non-KEV records as unlabeled-zero cases for descriptive ranking; it is not a positive–unlabeled risk estimator. Fixed baselines use critical severity, high-or-critical severity, or remediation availability. A current EPSS snapshot provides the exploitation-prioritization baseline on the CVE-matched subset (Jacobs et al. 2021). KEV-derived fields are excluded from predictor construction. KEV linkage is used only as an observed-positive outcome; non-KEV advisories remain unlabeled rather than confirmed negatives. The study reports routed and missed observed KEV counts, routed and unrouted unlabeled counts, observed-KEV yield, KEV recall, review share, and observed-KEV risk coverage.

The benchmark models integration changes and evidence records rather than deployed microservices. This design isolates the gate- decision problem from transport effects such as network latency, retry behavior, caching, asynchronous queues, and middleware-specific seri­ alization. The gate itself requires only stable evidence records: a change identifier, stage identifier, evidence score, adjudication burden, and fault or policy family when ground truth is available for evaluation. A production deployment would keep the same gate interface but add adapters that canonicalize service responses, normalize scanner and policy outputs, and attach provenance to each evidence item.

The modeled stages correspond to common DevSecOps control points. Contract evidence maps to schema and OpenAPI checks; se­ mantic evidence maps to regression and invariant checks; security evi­ dence maps to vulnerability and misuse checks; policy evidence maps to authorization and access-control checks; provenance evidence maps to build, signing, and artifact-lineage checks; dependency evidence maps to package and vulnerability feeds; adjudication evidence maps to structured review outcomes. Production systems would add retry pol­ icies, idempotent test fixtures, response canonicalization, and quaran­ tine rules for unstable observations. These additions affect evidence quality, but they do not change the threshold equations in Section 4.6. The stress profiles model the resulting degradation through lower signal strength and higher false-positive pressure.

The audit is retrospective. The snapshots preserve current advisory metadata rather than reconstructing every field as it appeared on its original publication date, and KEV is a selective record of observed exploitation rather than a complete exploit census. Uncertainty is assessed with advisory, ecosystem-cluster, and CVE-cluster bootstrap. Because each linked CVE occurs in one advisory, CVE-cluster resampling equals advisory resampling and CVE deduplication leaves all point es­ timates unchanged. A 2023–2024-only analysis reduces right-censoring, and a positive–unlabeled sensitivity analysis varies the assumed latent- positive rate among routed non-KEV advisories. The audit therefore evaluates advisory attention under an observed-risk proxy; it does not establish project reachability, dependency exposure, prospective exploit prediction, or CI-gate effectiveness.

The interface check uses a FastAPI service that returns JSON evi­ dence records for the seven simulated stages. It sends 144 local HTTP requests across six endpoints and records serialization, middleware, and client latency. The cases and labels remain generated. Consequently, this check demonstrates only that the scoring interface crosses a REST boundary; it is not production validation and contributes no external- validity claim.

### 4.5. Robustness and decision analyses

The evaluation extends the primary threshold sweep in six ways. Nonparametric bootstrap resampling estimates uncertainty; domain, period, and stress matrices expose slice dependence; and review- capacity curves evaluate fixed budgets. Declared cost scenarios select thresholds under different relative penalties. Period-held-out compari­ sons test transfer inside the simulator. Finally, risk-weight and score permutations quantify generator coupling, while paired seeded com­ parisons evaluate alternative aggregators and stage removals. The advisory audit freezes scaling and thresholds on the earlier cohort, evaluates them on the later publication cohort, and adds ecosystem- cluster, mature-cohort, positive–unlabeled, and EPSS-matched analyses.

### 4.4. Retrospective cross-domain advisory audit

The external study joins a pinned current snapshot of GitHub- reviewed security advisories with the CISA Known Exploited Vulnera­ bilities (KEV) catalog. After excluding 867 withdrawn records, the corpus contains 32,281 advisories; exact CVE-alias linkage identifies 124 observed KEV cases. Advisories published through 2022 form a selection cohort of 14,265 records with 77 observed KEV cases. The later publication cohort contains 18,016 records with 47 observed KEV cases. The cohorts contain 13,105 and 15,758 unique CVEs, respectively, with no CVE overlap; the remaining 1160 and 2258 advisories have no CVE alias. No CVE occurs in more than one advisory record in either cohort. This retrospective split tests whether fixed decision rules produce distinct advisory risk–workload points across publication cohorts; it is not prospective temporal validation of a CI control.

### 4.6. Metrics

Let C be the set of evaluated changes and V be the set of injected fault events. Each event v ∈V belongs to a change c(v), has risk weight w(v), and may be detected by one or more evidence stages. The faulty- change set is F = {c ∈C : ∃v ∈V , c(v) = c}, and the safe-change set is N = C \F . For threshold t, the gate set Gt = {c ∈C : R(c) ≥t} contains changes held for review (blocked pending review).

Six evidence stages are computed solely from advisory fields avail­ able independently of KEV membership: severity, remediation avail­ ability, affected-package breadth, affected-version complexity, reference substantiation, and disclosure detail. Numeric stages are scaled by selection-cohort 95th percentiles and clipped to [0, 1]. The primary score is their unweighted sum; a regularized combiner fitted

The primary security outcome is held-change risk coverage:

∑

```math
v∈V :c(v)∈Gtw(v)
∑
```

HRC(t) =

v∈V w(v) .

<!-- page 5 -->

This metric locates risk in changes held pending review; it does not claim that every underlying fault is detected or remediated. Escaped-risk share is the remaining weighted risk:

∑

```math
v∈V :c(v)∈Kt,kw(v)
```

HRCk(t) =

∑

v∈V w(v) .

Stage-ablation loss for removing stage s is

ER(t) = 1 −HRC(t).

Δs(t) = HRCfull(t) −HRC−s(t).

```math
High-severity held-change risk coverage is computed over V H =
{v ∈V : severity(v) ≥4}:
```

Cost scenarios select thresholds by minimizing a weighted loss over escaped risk, review load, and bad-block rate:

∑

```math
v∈V H:c(v)∈Gtw(v)
∑
```

HHRC(t) =

v∈V Hw(v) .

```math
Lossθ(t) = αθER(t) + βθRL(t) + γθBB(t), t∗
```

θ = argmin

t∈T Lossθ(t).

Change-level classification uses

The evaluation uses four decision profiles, each of which selects the minimum-loss threshold on the evaluated grid. The risk-averse profile places the largest relative emphasis on escaped risk; the balanced profile distributes weight across escaped risk, review load, and safe-change interruption; the review-limited profile places the largest relative emphasis on normalized review load; and the false-block-sensitive pro­ file places the largest relative emphasis on safe-change interruption. The profile names describe relative preferences rather than hard constraints on bad-block rate, held-change risk coverage, or queue size.

TP(t) = |Gt ∩F |, FP(t) = |Gt ∩N |,

FN(t) = |F \Gt|, TN(t) = |N \Gt|.

Bad-block rate, change recall, precision, false-discovery rate, speci­ ficity, and reviewed-change share are

BB(t) = FP(t)

### |N | ,

The loss coefficients are fixed before comparison. Risk-averse uses (α, β,γ) = (1.00,0.10,0.10); balanced uses (0.65,0.35,0.15); review-limited uses (0.32, 0.95, 0.12); and false-block-sensitive uses (0.45, 0.25, 1.20). These dimensionless profiles are decision scenarios, not estimates of monetary loss.

Rec(t) = TP(t) TP(t) + FN(t),

Prec(t) = TP(t) TP(t) + FP(t),

For the advisory audit, KEV-linked advisories are observed positives and all remaining advisories are unlabeled. Review burden assigns one unit to every routed advisory. A separate two-term loss,

FDR(t) = FP(t) TP(t) + FP(t),

Lossadv

```math
θ (t) = αθERKEV(t) + βθRS(t),
```

Spec(t) = TN(t) TN(t) + FP(t),

selects risk-averse, balanced, and review-limited points on the earlier cohort; no bad-block term is used because non-KEV does not denote a safe or negative advisory. The selected thresholds are then applied un­ changed to the later publication cohort. This cross-domain audit pre­ serves only the risk–workload structure of the decision analysis.

RS(t) = TP(t) + FP(t)

|C | .

Here, RS is the share of changes held for review, whereas RL, defined below, weights those changes by adjudication burden. A bad block is a safe change unnecessarily held for review. The evaluation does not use F1: equal weighting of precision and recall conflicts with the study’s declared asymmetric decision costs. When a denominator is zero in a seeded replicate, the corresponding ratio is treated as undefined for that replicate and excluded from the aggregate for that metric.

For an advisory i, the observed-risk weight is wKEV

i = 1 + 1(i has known ransomware use) when i is KEV-linked and zero other­ wise. Thus

∑

i∈Gt∩KEVwKEV

i ∑

HRCKEV(t) =

, ERKEV(t) = 1 −HRCKEV(t).

i∈KEVwKEV

i

Known ransomware use is excluded from evidence construction and applied only after scoring as an outcome weight.

Precision is transported to a target faulty-change prevalence π while holding the measured true- and false-positive rates fixed:

PPV(t, π) = Rec(t)π Rec(t)π + BB(t)(1 −π).

## 5. Results

### 5.1. RQ1: threshold operating points and prevalence transport

The corresponding transported review and false-block shares are

RS(t, π) = Rec(t)π + BB(t)(1 −π), FBS(t, π) = BB(t)(1 −π).

The deterministic campaign contains 615 faulty and 345 safe changes, so confusion counts are required to interpret the apparent frontier. Table 3 reports TP, FP, FN, and TN for every evaluated threshold. Threshold 3 holds changes containing nearly all generated risk, but its nine false blocks produce a 2.61% false-positive rate among safe changes. Threshold 5 removes seven true blocks and fifteen reviews relative to threshold 3 while reducing false blocks from nine to one. Threshold 20 produces no false block, but misses 308 of 615 faulty changes. Precision is inflated by this fault-rich composition and cannot be transported unchanged to a lower-prevalence pipeline.

The analysis evaluates π from 0.5% to 20%, plus the as-built simu­ lation prevalence, and reports expected true and false blocks per 1000 changes. This is analytical sensitivity analysis rather than additional observed data (Davis and Goadrich 2006; Saito and Rehmsmeier 2015).

Review effort uses stage-level adjudication burden. Let q(c) = ∑

s∈A qs(c). Normalized review load is

∑

```math
c∈Gtq(c)
∑
```

RL(t) =

c∈C q(c),

Prevalence transport changes this interpretation. Fig. 2 applies each seeded campaign’s true- and false-positive rates to target prevalences without claiming that the target domains share the simulation’s score distribution. At 1% faulty-change prevalence, threshold-3 mean preci­ sion falls to 29.05% (p05–p95: 18.28–44.55%), implying 26.74 false blocks among 36.67 blocks per 1000 changes. Threshold 5 is less sen­ sitive but still falls to 77.65% (51.45–100.00%), with 3.55 expected false

which is invariant to the evaluated threshold grid.

Review-capacity analysis ranks Gt by decreasing score R(c). If Kt,k denotes the top k ranked changes in Gt, the capacity-limited held-change risk coverage is

<!-- page 6 -->

**Table 3 Complete change-level confusion counts and operating metrics in the deter­ ministic campaign. Percentages are reported for precision, recall, and review share.**

**Table 4 Thresholds re-selected after prevalence transport under fixed cost profiles.**

Faulty prevalence

Risk- averse

Balanced Review- limited

False-block- sensitive

t TP FP FN TN Precision Recall Review share

0.5% 5 5 5 5 1% 5 5 5 5 5% 5 5 5 5 10% 3 5 8 5 20% 3 5 11 5

1 615 86 0 259 87.73 100.00 73.02 2 614 47 1 298 92.89 99.84 68.85 3 614 9 1 336 98.56 99.84 64.90 5 607 1 8 344 99.84 98.70 63.33 8 580 0 35 345 100.00 94.31 60.42 11 549 0 66 345 100.00 89.27 57.19 14 479 0 136 345 100.00 77.89 49.90 17 394 0 221 345 100.00 64.07 41.04 20 307 0 308 345 100.00 49.92 31.98 25 170 0 445 345 100.00 27.64 17.71

**Table 5 Bootstrap confidence intervals for deterministic threshold behavior; risk and recall values are percentages.**

t HRC mean HRC low HRC high Recall interval

blocks among 13.33 blocks. At 5% prevalence, mean precision is 66.92% for threshold 3 and 93.83% for threshold 5. The result does not estimate the prevalence of any named organization; it shows why site-specific base rates are required before interruption cost can be interpreted.

1 100.00 100.00 100.00 100.00–100.00 3 99.87 99.61 100.00 99.50–100.00 5 99.35 98.85 99.79 97.86–99.51 8 97.24 96.32 98.21 92.48–96.15

The corresponding mean false-discovery rates are 70.95% and 22.35% at 1% prevalence for thresholds 3 and 5, respectively; at 5% prevalence they fall to 33.08% and 6.17%. Reporting both precision and its complement makes the expected interruption burden explicit rather than hiding it behind the fault-rich benchmark.

only risk-weighted summaries. The generated number of faulty changes varies by seed, so these entries are means and need not be integers. At threshold 5, the gate averages 625.57 true blocks, 1.15 false blocks, 14.00 misses, and 319.28 true passes; its mean precision is 99.82% and it reviews 65.28% of changes. The zero mean false-positive count at thresholds 8–14 raises precision to 100%, but misses increase from 44.32 to 153.52. Seed-level counts remain available in the replication package for recomputation of every aggregate.

Re-selecting thresholds under each target prevalence gives the pro­ file matrix in Table 4. Because burden cannot be transported from class rates alone, this analysis uses the separate loss Lossπ

θ(t) = αθER(t) + βθRS(t,π) + γθFBS(t,π), not the burden-weighted primary loss. Threshold 5 remains selected through 5% prevalence; at 10–20%, risk-averse and review-limited profiles diverge. Thus threshold 5 is not declared uni­ versally balanced: it is the minimum-loss point only under the stated prevalence and cost assumptions.

Table 8 shows that the balanced threshold is not driven by a single easy slice. At threshold 5, held-change risk coverage ranges from 98.65% in social benefits to 100.00% in public health and open data. Period results range from 97.95% in the baseline period to 99.82% in the policy-burst period. The baseline period is the weakest slice due to lower mean risk scores rather than a drift-specific gate failure.

Fig. 3 plots the deterministic threshold sweep in precision–recall space. Thresholds 3 and 5 lie close on the fault-rich benchmark, con­ firming why a single F1 score would not distinguish them. Fig. 2 supplies the necessary base-rate sensitivity, so the PR view is an operating diagnostic rather than independent support for threshold 5.

Threshold stability weakens as thresholds increase. Table 9 and Fig. 6 show that, at threshold 5, held-change risk spread is 1.35 per­ centage points across domains, 1.86 points across periods, and 0.39 points across deterministic stress profiles. At threshold 14, the corre­ sponding spreads become 9.89, 10.43, and 3.08 points. This pattern is evidence against choosing high thresholds solely to eliminate bad- blocks: higher thresholds amplify deployment-slice sensitivity.

Fig. 4 shows the trade-off curve. Thresholds below 5 give marginal additional risk coverage but materially increase bad-block rate. Thresholds above 8 remove bad-blocks but progressively increase escaped risk.

Stress profiles expose the lower tail. Table 10 and Fig. 7 show that baseline p05 held-change risk coverage at threshold 5 is 98.83%. The high-noise low-signal profile lowers the p05 value to 95.68% and raises bad-block p95 to 2.51%. Compound drift is similar, with p05 coverage of 95.83%. Strict adjudication is less severe for false blocks but reduces mean coverage to 98.25%. These intervals establish stability under repeated draws from the declared generator; they do not establish sta­ bility after the score–risk relationship changes.

Fig. 5 clarifies the operating frontier. Threshold 2 is dominated by threshold 3: both escape 0.12% of risk, but threshold 3 reviews fewer changes and reduces bad-block rate from 13.62% to 2.61%. Moving from threshold 5 to 8 eliminates bad-blocks in this deterministic campaign, but escaped risk rises from 0.65% to 2.73%. The cost of fewer reviews grows rapidly after threshold 14.

### 5.2. RQ2: seeded stability and stress behavior with generator coupling

Fig. 8 isolates the corresponding interruption intervals: noise- dominated profiles widen the upper tail of safe-change blocking.

Bootstrap resampling of the deterministic campaign gives the same threshold ordering. Table 5 shows that threshold 5 has mean held- change risk coverage of 99.35%, with a 98.85–99.79% interval, while threshold 8 has lower coverage of 97.24% and a wider 96.32–98.21% interval. The confidence band for threshold 5 remains separated from the higher-threshold zero-bad-block region, so the deterministic oper­ ating point is not only a point estimate.

Fig. 9 shows that cost-based threshold choice is profile-dependent. Under the balanced scenario, threshold 5 is selected in 96.67% of baseline seeds and 100% of high-noise low-signal seeds. Under the risk- averse scenario, threshold 3 dominates most profiles. Under false-block sensitivity, threshold 8 becomes more common in noisy settings: it eliminates many safe-change interruptions at the cost of additional escaped risk.

The seeded campaign confirms that threshold 5 is not a single-run artifact under baseline conditions. Table 6 shows that threshold 5 has mean held-change risk coverage of 99.30%, with p05 98.83% and p95 99.58% across 60 seeded campaigns. Threshold 3 has higher mean coverage of 99.75%, but its mean bad-block rate is 2.70%. Threshold 8 eliminates bad-blocks in the seeded baseline summary, but mean coverage falls to 97.24%.

Generated total risk and aggregate evidence have Pearson correla­ tion 0.921 and Spearman correlation 0.918 at change level. Permuting event weights globally or within fault family leaves threshold-5 held- change risk coverage near 99.4%, because high-scoring changes retain the same generated fault structure. In contrast, permuting scores within domain–period strata reduces mean coverage to 65.25% (p05–p95: 63.07–67.44%). Fig. 10 separates robustness to weight perturbation

Table 7 reports the corresponding classification counts rather than

<!-- page 7 -->

**Table 6 Baseline seeded threshold summary across 60 campaigns. Percent values are shown as mean with p05–p95 range.**

**Table 9 Held-change risk spread across benchmark slices.**

Dimension t = 3 t = 5 t = 8 t = 11 t = 14

t Held-change risk

Bad block Change recall Reviewed changes

Domain spread 0.83 1.35 4.05 5.49 9.89 Period spread 0.70 1.86 4.08 7.68 10.43 Stress spread 0.32 0.39 1.41 2.96 3.08

## 3 99.75 (99.55–99.94)

### 643.87 (621.00–671.10) 5 99.30 (98.83–99.58)

2.70 (1.25–4.50)

99.32 (98.87–99.84)

### 626.72 (609.90–651.05) 8 97.24 (96.39–97.90)

0.36 (0.00–0.93)

97.81 (96.67–98.68)

**Table 10 Threshold-5 stress behavior across 60 seeded campaigns. Percent values are shown as mean with p05–p95 range.**

### 595.25 (575.85–620.15) 11 93.27 (91.67–94.78)

0.00 (0.00–0.00)

93.07 (91.65–94.49)

### 549.32 (530.95–578.20) 14 86.64 (84.64–88.48)

0.00 (0.00–0.00)

85.88 (83.65–88.35)

Profile Held-change risk Bad block Recall

0.00 (0.00–0.00)

75.99 (73.51–79.34)

486.05 (466.80–508.05)

Baseline 99.30 (98.83–99.58)

### 97.81 (96.67–98.68) Adjudication

0.36 (0.00–0.93)

### 97.29 (95.92–98.13) Semantic drift 98.87 (98.29–99.31)

99.05 (98.47–99.44)

0.33 (0.00–0.92)

constrained

**Table 7 Mean seeded confusion counts and classification performance across 60 baseline campaigns. Each campaign contains 960 changes.**

### 96.99 (95.73–98.12) Dependency burst 99.02 (98.62–99.47)

0.36 (0.00–0.93)

### 97.33 (96.15–98.39) Noisy policy 99.16 (98.72–99.54)

0.45 (0.00–1.13)

t TP FP FN TN Precision Review share

### 97.61 (96.31–98.58) Strict adjudication 98.25 (97.44–98.96)

0.60 (0.00–1.34)

3 635.23 8.63 4.33 311.80 98.66 67.07 5 625.57 1.15 14.00 319.28 99.82 65.28 8 595.25 0.00 44.32 320.43 100.00 62.01 11 549.32 0.00 90.25 320.43 100.00 57.22 14 486.05 0.00 153.52 320.43 100.00 50.63

### 95.98 (94.19–97.20) Compound drift 96.88 (95.83–97.88)

0.39 (0.00–0.93)

### 93.92 (92.30–95.63) High-noise low-

0.91 (0.00–1.69)

96.91 (95.68–98.06)

1.56 (0.62–2.51)

94.04 (92.19–95.92)

signal

**Table 8 Domain and period behavior at threshold 5 in the deterministic campaign.**

have the same division of labor.

The data-derived implementation check in Fig. 1 visualizes the same stage–family specialization declared in the generator.

Group Slice Changes Faults Bad block Held risk

Domain Social benefits 215 450 0.00 98.65 Domain Land administration 149 258 0.00 99.17 Domain Civil registry 201 383 0.00 99.29 Domain Education 96 201 0.00 99.67 Domain Open data 180 328 1.37 100.00 Domain Public health 119 245 0.00 100.00 Period Baseline 240 341 0.00 97.95 Period Dependency burst 240 505 1.25 99.33 Period Semantic drift 240 566 0.00 99.81 Period Policy burst 240 453 0.00 99.82

Alternative aggregators yield overlapping simulated frontiers. Table 13 summarizes period-held-out evaluation across 60 seeds. The unweighted sum has mean held-change risk coverage of 98.81%, mean precision 99.94%, and review share 67.59%. The fixed weighted sum, regularized combiner, normalized sum, and maximum-stage rule differ in coverage by <0.14 percentage points on average; their paired p05–p95 differences relative to the unweighted sum all span zero. The fixed weighted sum reduces mean coverage by 0.12 points and review share by 0.21 points relative to the unweighted sum. Alert count is less precise, while the security-only rule loses 35.47 points of coverage. Change criticality alone reviews 95.10% of changes at only 69.89% precision. The fault-severity oracle reaches 100% precision and 99.71% held-change risk coverage, but it consumes the hidden generated label and is included only as an unattainable upper bound. The mandatory- core rule is unstable because it requires a specific stage even when another simulated stage carries the injected signal. The appropriate conclusion is equivalence within the simulated uncertainty, not supe­ riority of the original aggregation rule.

from dependence on the generator’s score ordering; the 34.10-point reduction identifies that ordering as a major source of the simulated frontier.

### 5.3. RQ3: stage contributions and aggregator choice

Ablations show complementarity but do not support a strict ranking of all stages. Table 11 reports mean held-change risk loss after removal together with precision and workload. Precision stays between 99.85% and 99.90%, while review share falls by different amounts; the primary ablation effect is therefore lost recall and weighted-risk coverage rather than additional false blocks. Semantic and security removal differ by only 0.10 percentage points; the paired bootstrap interval for this dif­ ference is [−0.09, 0.31] percentage points and includes zero. Their losses are both larger than the policy loss: semantic minus policy is 0.39 points (95% interval 0.23–0.55), and security minus policy is 0.29 points (0.10–0.47). Removing adjudication has the smallest mean risk effect. These are marginal effects within a deliberately specialized simulator, not estimates of universal stage importance.

### 5.4. RQ4: cost scenarios and period-held-out transfer

Review capacity is front-loaded on the evaluated capacity grid. Fig. 11 and Table 14 show that a 300-change review queue captures 61.35% of total risk under thresholds 3, 5, 8, and 11, reflecting the concentration of risk in the top-ranked changes. Reaching 90% on this grid requires using all threshold-eligible changes: 608 reviewed changes at threshold 5 and 580 at threshold 8. This supports using capacity analysis as a separate decision input rather than relying only on the threshold curve.

Table 12 explains the ablation pattern. Contract evidence specializes in schema failures, semantic evidence in semantic failures, security and dependency evidence overlap on dependency-linked security failures, policy evidence specializes in policy failures, provenance evidence in provenance failures, and deterministic adjudication contributes to ambiguous and cross-cutting cases. This specialization is part of the generator specification rather than independent evidence that real tools

Cost scenarios change the selected threshold by assigning different penalties to escaped risk, normalized review load, and safe-change interruption. Table 15 shows that, in the deterministic campaign, the risk-averse scenario selects threshold 3, the balanced and false-block- sensitive scenarios select threshold 5, and the review-limited scenario selects threshold 25. The review-limited selection illustrates the price of

<!-- page 8 -->

transfers poorly, with 42.74% test coverage and 31.74% test recall. Because training and test periods share one generator, this is temporal stress within a simulation rather than external transfer.

**Table 11 Replicated stage ablation at threshold 5 across 60 seeded campaigns. Risk loss, recall, precision, and review share are percentages; risk loss and recall show mean with p05–p95.**

The transfer results reinforce the decision-model implication: threshold stability is conditional on a declared cost profile, so different profiles can rationally select different operating points from the same evidence.

Configuration Risk loss Recall Precision Review

Without semantic 2.19 (1.36–2.87)

93.96 (92.46–95.17)

### 99.86 62.68

Without security 2.09 (1.29–3.15)

95.02 (93.59–96.27)

### 99.90 63.37

### 5.5. RQ5a: interface feasibility check

Without policy 1.81 (1.10–2.57)

95.29 (93.79–96.53)

### 99.87 63.57

The interface check executes 144 local HTTP requests against a FastAPI service covering six endpoint families, with 116 generated faulty cases and 28 generated safe cases. Table 17 gives complete clas­ sification and workload fields. Threshold 5 holds changes containing 99.01% of generated risk and produces no false block in this small run; threshold 3 covers all generated risk but also blocks 14 safe cases, lowering precision to 89.23%. Mean client-observed latency remains below one millisecond. This experiment verifies serialization and scoring across a REST boundary only.

Without contract 1.52 (1.09–2.22)

94.43 (92.98–95.77)

### 99.85 63.00

Without

1.35 (0.80–1.95)

95.37 (93.90–96.38)

### 99.86 63.62

provenance

Without

0.94 (0.42–1.62)

96.04 (94.71–97.30)

### 99.88 64.06

dependency

Without

0.64 (0.24–1.21)

96.52 (95.02–97.65)

### 99.88 64.38

adjudication

**Table 12 Primary and secondary evidence stages by fault family in the deterministic campaign; coverage and gap are percentages.**

### 5.6. RQ5b: retrospective advisory-level demonstration

Table 18 reports thresholds selected on advisories published through 2022 and applied without refitting to the later publication cohort of 18,016 advisories. The balanced unweighted point covers 96.23% of observed KEV risk and recalls 45 of 47 observed KEV cases while reviewing 48.58% of advisories. Ecosystem-cluster bootstrap intervals are 87.49–100.00% for observed-risk coverage and 44.58–53.28% for review share. The review-limited regularized point covers 62.26% at 3.45% review share. These points demonstrate distinct advisory risk–workload trade-offs; they do not validate a project-level CI gate.

Fault family Primary stage

Coverage Secondary stage

Coverage Gap

Schema Contract 94.63 Semantic 15.12 79.51 Semantic Semantic 91.50 Adjudication 45.50 46.00 Security Security 87.68 Dependency 52.11 35.57 Policy Policy 90.57 Adjudication 46.54 44.03 Provenance Provenance 87.91 Adjudication 40.66 47.25 Dependency Dependency 88.62 Security 53.66 34.96 Ambiguous Adjudication 70.50 Provenance 30.94 39.56

Table 19 uses positive–unlabeled terminology. The balanced un­ weighted point has 0.51% observed-KEV yield; the review-limited regularized point reaches 4.35% by trading observed-positive recall for a smaller queue. The routed non-KEV share is not a false-discovery rate because KEV is a selective exploitation record and non-KEV advi­ sories are not confirmed negatives.

heavily penalizing review effort: zero bad-blocks and lower normalized review load come with only 38.94% held-change risk coverage in the deterministic campaign.

Period-held-out selection gives a second view of within-generator transfer. Table 16 shows that thresholds selected on the baseline and policy-burst periods retain high generated-risk coverage for the balanced and false-block-sensitive scenarios: test held-change risk coverage is 99.57%, test recall is 98.80%, and test false-positive rate is 0.68%. The risk-averse threshold transfers with complete generated-risk coverage but a 3.42% false-positive rate. The review-limited threshold

The EPSS comparison in Table 20 is computed on 15,305 later-cohort advisories with current EPSS coverage, including all 47 observed KEV cases. The comparison is retrospective because both EPSS and advisory features come from current snapshots. EPSS dominates the manuscript’s scores at both budgets: at 1%, its observed-KEV average precision is

**Fig. 1. Implemented evidence-stage specialization by generated fault family. The data-derived coverage values verify the declared generator configuration rather than estimate real-tool effectiveness.**

<!-- page 9 -->

**Fig. 2. Precision transported across assumed faulty-change prevalences using seeded true- and false-positive rates. Bands denote p05–p95 across 60 campaigns.**

**Fig. 3. Deterministic precision–recall curve over all evaluated thresholds. The dashed line is the generated faulty-change prevalence.**

0.600, observed-KEV yield is 23.38%, and observed-risk coverage is 77.36%. The regularized combiner reaches 12.99% yield and 49.06% coverage, while the unweighted score reaches 7.79% and 30.19%. Because non-KEV advisories are unlabeled rather than confirmed neg­ atives, this AP is descriptive under the observed-label convention and is not average precision for all exploited vulnerabilities. This baseline rules out a superiority claim for the advisory score and confines the external contribution to the cost-sensitive analysis.

a much larger queue. In the less-censored 2023–2024 cohort, the balanced unweighted point covers all 17 observed KEV cases at 46.65% review share; its review-limited point covers 70.00% of observed risk at 3.52%. Under assumed latent-positive rates of 0.1%, 0.5%, and 1.0% among routed non-KEV advisories, estimated routed yield is 0.61%, 1.01%, and 1.51% for the balanced point and 4.44%, 4.83%, and 5.30% for the regularized review-limited point. These sensitivities do not convert unlabeled advisories into negatives or prospective outcomes.

Fig. 12 shows why a single advisory operating point is insufficient. The regularized review-limited point gives nearly the critical-only observed-risk coverage (62.26% versus 64.15%) at 3.45% rather than 11.50% review share, while the balanced point gives higher coverage at

## 6. Discussion

For security operations, the main result is that a CI gate can be

<!-- page 10 -->

**Fig. 4. Threshold selection trades escaped risk against review interruption in the deterministic campaign.**

**Fig. 5. Escaped-risk and bad-block frontier. Marker size reflects review load, and labels denote thresholds.**

reported as a cost-sensitive control rather than as an opaque pass-fail rule. Recent studies on control integration and automated security testing emphasize practical deployment, control validation, and pre- integration risk detection (Sinan et al. 2025; Skandylas and Asplund 2025; Tang et al. 2025). The threshold frontier adds a missing oper­ ating view: it quantifies how much weighted risk is located in changes held pending review, how many benign changes it interrupts, how much review capacity it consumes, and how stable these quantities remain under stress.

ordering, so repeatability within the generator is not independent evi­ dence validity.

The threshold results also clarify the relationship with generated testing. REST API fuzzing, directed testing, symbolic execution, grammar-based exploration, and search-based generation can all in­ crease the number and diversity of observable failures (Atlidakis et al. 2019; Godefroid et al. 2005, 2008; Cadar et al. 2008; Fraser and Arcuri 2011). The gate studied here does not compete with those tech­ niques. It assumes evidence can be produced by specialized stages, then evaluates the decision boundary over that evidence. Within the declared simulator, the ablation results illustrate the value of combining stages: semantic and security removals each lose more risk coverage than policy removal, although their paired difference is not distinguishable. The aggregator comparison likewise finds no material improvement over the unweighted sum within the simulator.

The results align with prior testing work in one respect: the value of a test or gate depends on the fault model and oracle, not only on the number of executed checks (Bertolino 2007; Whittaker 2000). Model-based and mutation-testing work make this dependence concrete by tying tests to explicit behavioral models and seeded faults (Utting et al. 2012; Offutt et al. 1996). A cost-sensitive gate extends that lesson to CI decisions. It is not enough to know that a scanner or contract test emitted evidence. The pipeline also needs to know how much weighted risk the gate routes into review and how often the same threshold holds safe changes. The coupling analysis qualifies this result: part of the strong simulated frontier follows from the generated score

The access-control and policy-testing literature provides a useful analogy. RBAC and ABAC separate authorization models from applica­ tion code (Sandhu et al. 1996; Ferraiolo et al. 2001; Servos and Osborn 2017). Policy-testing work then asks which policy rules and decisions are covered by generated tests (Pretschner et al. 2008; Martin et al.

<!-- page 11 -->

**Fig. 6. Higher thresholds amplify held-change risk spread across domains, periods, and stress profiles; spreads are percentage points.**

**Fig. 7. Threshold-5 held-change risk intervals across stress profiles.**

2006). A CI gate faces a similar decomposition. Security, policy, con­ tract, dependency, and provenance evidence are different signals, and a threshold collapses them into an operational decision. The results show that this collapse can be measured. Within the generated benchmark, threshold 5 occupies a balanced point and threshold 3 a risk-averse point. Neither is universal; prevalence transport shows that rare faulty changes increase the interruption burden, especially at threshold 3 (Davis and Goadrich 2006; Saito and Rehmsmeier 2015).

not claim that simulated evidence replaces a field deployment. It isolates the decision layer after security checks have emitted normalized evi­ dence. The FastAPI mini case study establishes interface feasibility rather than external effectiveness. The retrospective advisory audit shows that the framework can express materially different risk–work­ load points in another prioritization domain, consistent with evidence that severity and exploitation are not interchangeable (Allodi and Massacci 2014; Jacobs et al. 2021; Mell et al. 2024). Current EPSS performs substantially better on the matched subset, so the audit neither validates the CI gate nor establishes a competitive exploit predictor. It instead bounds the claim: the decision-analysis framework transfers, while evidence design and scoring must be validated for each domain.

The stress results sharpen this interpretation. A deterministic campaign alone would overstate certainty. The seeded campaign shows that baseline threshold-5 behavior is stable, but lower-tail risk coverage degrades under compound drift and high-noise low-signal stress. This agrees with evidence from flaky-test and debugging research: opera­ tional signals can be unstable when environment, timing, or observa­ tional noise changes (Bell et al. 2018; Zeller 2002). A production gate would therefore monitor mean and lower-tail held-change risk coverage, bad-block p95, and profile-specific drift.

Risk weighting requires care. The controlled weighting scheme re­ flects empirical distinctions among severity, exploitation evidence, and operational context (Allodi and Massacci 2014; Jacobs et al. 2021; Mell et al. 2024). It also follows the control-oriented view of security assur­ ance and software-supply-chain research (Shukla et al. 2022; Newman et al. 2022; Torres-Arias et al. 2019; Gokkaya et al. 2026). It is an

The deployment interpretation is conditional. The benchmark does

<!-- page 12 -->

**Fig. 8. Bad-block intervals at threshold 5. Noise-dominated profiles mainly widen interruption risk.**

**Fig. 9. Threshold-selection frequency across seeded campaigns for selected stress profiles and cost scenarios.**

experiment-specific severity proxy rather than an organization-independent severity scale. In practice, organizations would adapt weights to incident classes, service criticality, legal expo­ sure, recovery cost, and customer impact. The empirical method remains applicable: replace the benchmark weights with the organization’s scoring model and recompute the threshold frontier.

emergency review triage from normal release gates.

## 7. Threats to validity

Construct validity is limited by the benchmark’s risk weights, evi­ dence scores, and fault families. Held-change risk coverage measures risk located in changes pending review, not confirmed remediation or prevented loss. The simulated evidence stages encode specialization rather than execute commercial scanners. In the advisory audit, KEV linkage is a selective observed-positive proxy; non-KEV advisories remain unlabeled, and current metadata does not establish project exposure or reachability. The study therefore reports observed-KEV

The capacity analysis has practical implications for review queues. The first 300 reviewed changes contain 61.35% of risk in the deter­ ministic campaign, so the risk ranking is strongly front-loaded. That does not make 300 reviews sufficient or imply remediation. Higher assurance targets require reviewing nearly all changes above the threshold. Pipeline owners can use this distinction to separate

<!-- page 13 -->

**Fig. 10. Threshold-5 held-change risk coverage under generator-coupling perturbations. Intervals summarize 1000 permutations.**

yield and non-KEV routed share rather than external precision or false- discovery rate.

**Table 13 Period-held-out aggregator comparison across 60 seeded campaigns. Precision, review share, and held-change risk coverage are percentages; parentheses give p05–p95 coverage.**

Internal validity is affected by the deterministic generator and by coupling between injected faults and evidence stages. The extended campaign reduces dependence on a single generated dataset, while score and weight permutations quantify how much the frontier depends on generated ordering. Cost coefficients are fixed in code. Advisory scaling

Aggregator Precision Review share Held-change risk

Unweighted sum 99.94 67.59 98.81 (97.65–99.58) Fixed weighted sum 99.94 67.38 98.68 (97.73–99.38) Regularized combiner 99.85 67.76 98.72 (97.20–99.66) Normalized sum 99.82 67.67 98.68 (97.52–99.62) Maximum stage 99.51 68.32 98.75 (97.51–99.69) Alert count 98.24 68.37 98.21 (93.99–99.26) Fault-severity oracle 100.00 69.00 99.71 (99.49–100.00) Change criticality only 69.89 95.10 95.64 (80.12–100.00) Mandatory core stage 73.74 89.34 91.33 (34.24–100.00) Security only 95.91 41.42 63.34 (59.21–67.49)

**Table 14 Review-capacity sensitivity at threshold 5 in the deterministic campaign; held- change risk columns are percentages.**

Capacity Reviews Held risk High-severity risk

## 100 100 25.17 29.28 200 200 44.65 49.28 300 300 61.35 64.90 500 500 89.10 90.52 All above threshold 608 99.35 99.29

**Fig. 11. Smallest evaluated review budget meeting each held-change risk target.**

<!-- page 14 -->

**Table 15 Cost-scenario threshold choices in the deterministic campaign. Loss is unitless; held-change risk, bad block, and normalized review load are percentages.**

**Table 20 Current-EPSS matched comparison at fixed advisory review budgets. Yield, recall, and risk coverage are percentages.**

Scenario t Loss Held risk Bad block Review load

Method Obs.- KEV AP

1% budget 3% budget

Risk-averse 3 0.1023 99.88 2.61 98.42 Balanced 5 0.3475 99.35 0.29 97.95 False-block-sensitive 5 0.2513 99.35 0.29 97.95 Review-limited 25 0.5871 38.94 0.00 41.23

​​Yield Recall Risk Yield Recall Risk Current

### 0.600 23.38 76.60 77.36 8.70 85.11 84.91

EPSS

Regularized 0.172 12.99 42.55 49.06 5.22 51.06 56.60 Unweighted 0.084 7.79 25.53 30.19 4.13 40.43 45.28 Severity

### 0.012 3.90 12.77 13.21 2.17 21.28 22.64

**Table 16 Threshold selection on baseline/policy periods and evaluation on dependency/ semantic periods; risk and bad-block values are percentages.**

only

EPSS superiority further shows that the manuscript’s advisory features should not replace a domain-specific exploitation model.

Scenario t Train risk Test risk Test bad block

Risk-averse 3 99.72 100.00 3.42 Balanced 5 99.07 99.57 0.68 False-block-sensitive 5 99.07 99.57 0.68 Review-limited 25 34.11 42.74 0.00

Conclusion validity is constrained by the selected seeds, stress pro­ files, thresholds, permutation draws, and 47 observed KEV cases. Advisory-, ecosystem-, and CVE-cluster bootstrap intervals address sampling and dependence; the latter equals advisory resampling here because linked CVEs are unique to advisory records, and the cohorts are CVE-disjoint. The 2023–2024 sensitivity reduces but cannot eliminate right-censoring, and the positive–unlabeled sensitivity does not identify which non-KEV advisories are latent positives. Additional generators, historical snapshots, or deployment settings could change the estimates.

**Table 17 Interface feasibility classification over generated HTTP evidence records. Pre­ cision, recall, and review share are percentages.**

t TP FP FN TN Precision Recall Review share

## 3 116 14 0 14 89.23 100.00 90.28 5 112 0 4 28 100.00 96.55 77.78 8 75 0 41 28 100.00 64.66 52.08

## 8. Conclusion

Cost-sensitive security gates provide a measurable way to choose CI thresholds when pipelines emit heterogeneous assurance evidence. In the deterministic campaign, threshold 5 holds changes containing 99.35% of generated risk with one false block; the seeded, stress, prevalence, and coupling analyses delimit that result. The REST mini case establishes interface feasibility. The retrospective advisory demonstration produces distinct risk–workload points but does not validate the CI gate, and current EPSS is stronger on the matched CVE subset. The contribution is therefore a decision-analysis framework for reporting escaped risk, interruption, capacity, and stress behavior. Deployment requires local validation of evidence, prevalence, costs, review effectiveness, and capacity.

**Table 18 Retrospective advisory audit on the later publication cohort. Thresholds are selected on the earlier cohort; review, recall, and observed KEV risk coverage are percentages.**

Policy Profile t Review KEV rec. KEV risk

Unweighted Risk-averse 3.75 71.03 95.74 96.23 Unweighted Balanced 4.00 48.58 95.74 96.23 Unweighted Review-limited 5.25 2.90 40.43 45.28 Regularized Balanced 0.450 11.57 74.47 77.36 Regularized Review-limited 0.743 3.45 57.45 62.26 Critical only Fixed — 11.50 59.57 64.15 High/critical Fixed — 46.34 93.62 94.34 Fixed version Fixed — 86.75 93.62 94.34

Funding

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

Table 19 Advisory-level counts for selected operating points. UW and Reg. denote un­ weighted and regularized scoring; R, M, and U denote routed, missed, and unrouted; “unlabeled” denotes non-KEV advisories. Yield and routed non-KEV share are percentages.

Ethics statement

The study analyzes public software artifacts and generated bench­ mark records and involves no human participants, personal data, or animal subjects; ethics approval and consent were therefore not applicable.

Operating point

R- KEV

R- unlab.

M- KEV

U- unlab.

Yield R- nonKEV

UW/risk 45 12,752 2 5217 0.35 99.65 UW/balanced 45 8707 2 9262 0.51 99.49 UW/review 19 503 28 17,466 3.64 96.36 Reg./balanced 35 2049 12 15,920 1.68 98.32 Reg./review 27 594 20 17,375 4.35 95.65

Declaration of generative AI and AI-assisted technologies in the manuscript preparation process

During the preparation of this work, the author used ChatGPT to support language editing and manuscript organization. The author reviewed and edited all output, independently verified the analyses, references, numerical results, and conclusions, and takes full re­ sponsibility for the content of the article. Generative AI was not used to create study data, labels, or figures.

and threshold selection use only the earlier publication cohort, and KEV- derived fields are excluded from evidence construction. The current snapshot does not reconstruct historical feature states, so the split is retrospective rather than prospective.

External validity is limited by the absence of large deployed pro­ duction services. The FastAPI mini case adds transport realism but only establishes interface feasibility. The public-advisory corpus broadens the decision analysis to observed exploitation outcomes, yet remains a cross-domain attention audit rather than observed CI decisions. Current

CRediT authorship contribution statement

The-Vinh Nguyen: Writing – review & editing, Writing – original draft, Visualization, Validation, Software, Methodology, Formal

<!-- page 15 -->

**Fig. 12. Retrospective publication-cohort advisory risk–workload frontier. Markers show profiles selected on the earlier cohort; fixed rules provide descrip­ tive baselines.**

analysis, Data curation, Conceptualization.

Ferraiolo, David F., Sandhu, Ravi, Gavrila, Serban, Kuhn, D.Richard,

Chandramouli, Ramaswamy, 2001. Proposed NIST standard for role-based access control. ACM Trans. Inf. Syst. Secur. 4 (3), 224–274. https://doi.org/10.1145/ 501978.501980. Fraser, Gordon, Arcuri, Andrea, 2011. EvoSuite: automatic test suite generation for

Declaration of competing interest

object-oriented software. In: Proceedings of the 19th ACM SIGSOFT Symposium and the 13th European Conference on Foundations of Software Engineering, pp. 416–419. https://doi.org/10.1145/2025113.2025179. Godefroid, Patrice, Kiezun, Adam, Levin, Michael Y., 2008. Grammar-based Whitebox

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

fuzzing. In: Proceedings of the ACM SIGPLAN Conference on Programming Language Design and Implementation, pp. 206–215. https://doi.org/10.1145/ 1375581.1375607. Godefroid, Patrice, Klarlund, Nils, Sen, Koushik, 2005. DART: directed automated

Data availability

random testing. In: Proceedings of the ACM SIGPLAN Conference on Programming Language Design and Implementation, pp. 213–223. https://doi.org/10.1145/ 1065010.1065036. Gokkaya, Betul, Aniello, Leonardo, Halak, Basel, 2026. Software supply chain: a

https://github.com/ictu-se/risk-calibrated-security-gates- replication (The public replication package at contains the experiment code, versioned configurations, provenance records, and derived results needed to reproduce the simulation and retrospective advisory audit.)

taxonomy of attacks, mitigations and risk assessment strategies. J. Inf. Secur. Appl. 97, 104324. https://doi.org/10.1016/j.jisa.2025.104324. Jacobs, Jay, Romanosky, Sasha, Edwards, Benjamin, Adjerid, Idris, Roytman, Michael,

2021. Exploit prediction scoring system (EPSS). Digit. Threats: Res. Pract. 2 (3), 1–17. https://doi.org/10.1145/3436242. Martin, Evan, Xie, Tao, Yu, Ting, 2006. Defining and measuring policy coverage in

## References

testing access control policies. In: Proceedings of the 8th International Conference on Information and Communications Security, pp. 139–158. https://doi.org/10.1007/ 11935308_11. Mell, Peter, Bojanova, Irena, Galhardo, Carlos Eduardo, 2024. Measuring the Achbarou, Omar, Lachgar, Mohamed, Badouri, Youssef El, Rhouddani, Monsef, Tahalli, Anas, Dhimni, Roa El, 2026. SafeOps+: an integrated platform for automated security analysis and compliance in DevSecOps pipelines. SoftwareX 33, 102465. https://doi.org/10.1016/j.softx.2025.102465. Allodi, Luca, Massacci, Fabio, 2014. Comparing vulnerability severity and exploits using exploitation of weaknesses in the wild. IT Prof 26 (3), 14–21. https://doi.org/ 10.1109/MITP.2024.3399485. Newman, Zachary, Meyers, John Speed, Torres-Arias, Santiago, 2022. Sigstore: software case-control studies. ACM Trans. Inf. Syst. Secur. 17 (1), 1–20. https://doi.org/ 10.1145/2630069. Atlidakis, Vaggelis, Godefroid, Patrice, Polishchuk, Marina, 2019. RESTler: stateful REST signing for everybody. In: Proceedings of the 2022 ACM SIGSAC Conference on Computer and Communications Security, pp. 2353–2367. https://doi.org/10.1145/ 3548606.3560596. Offutt, A.Jefferson, Lee, Ammei, Rothermel, Gregg, Untch, Roland H., Zapf, Christian, API fuzzing. In: Proceedings of the 41st International Conference on Software Engineering, pp. 748–758. https://doi.org/10.1109/ICSE.2019.00083. Bell, Jonathan, Legunsen, Owolabi, Hilton, Michael, Eloussi, Lamyaa, Yung, Tifany,

1996. An experimental determination of sufficient mutant operators. ACM Trans. Softw. Eng. Methodol. 5 (2), 99–118. https://doi.org/10.1145/227607.227610. Pretschner, Alexander, Mouelhi, Tejeddine, Le Traon, Yves, 2008. Model-based tests for Marinov, Darko, 2018. DeFlaker: automatically detecting flaky tests. In: Proceedings of the 40th International Conference on Software Engineering, pp. 433–444. https:// doi.org/10.1145/3180155.3180164. Bertolino, Antonia., 2007. Software testing research: achievements, challenges, dreams. access control policies. In: Proceedings of the 1st International Conference on Software Testing, Verification, and Validation, pp. 338–347. https://doi.org/ 10.1109/ICST.2008.44. Saito, Takaya, Rehmsmeier, Marc, 2015. The precision–recall plot is more informative Future Softw. Eng. 85–103. https://doi.org/10.1109/FOSE.2007.25. Bhatnagar, Gaurav., 2026. A policy-driven branching and environment isolation strategy than the ROC plot when evaluating binary classifiers on imbalanced datasets. PLOS ONE 10 (3), e0118432. https://doi.org/10.1371/journal.pone.0118432. Sandhu, Ravi S., Coyne, Edward J., Feinstein, Hal L., Youman, Charles E., 1996. Role- for enterprise DevSecOps: an empirical industrial case study. IEEE Access 14, 78181–78190. https://doi.org/10.1109/ACCESS.2026.3694956. Cadar, Cristian, Dunbar, Daniel, Engler, Dawson, 2008. KLEE: unassisted and automatic based access control models. Comput. (Long Beach Calif) 29 (2), 38–47. https://doi. org/10.1109/2.485845. Santos Filho, Ailton, Rodríguez, Ricardo J., Feitosa, Eduardo L., 2025. Automated broken generation of high-coverage tests for complex systems programs. In: Proceedings of the 8th USENIX Symposium on Operating Systems Design and Implementation, pp. 209–224. https://www.usenix.org/legacy/event/osdi08/tech/full_papers/ cadar/cadar.pdf. Davis, Jesse, Goadrich, Mark, 2006. The relationship between precision–recall and ROC object-level authorization attack detection in REST APIs through OpenAPI to colored Petri nets transformation. Int. J. Inf. Secur. 24, 83. https://doi.org/10.1007/s10207- 024-00970-5. curves. In: Proceedings of the 23rd International Conference on Machine Learning, pp. 233–240. https://doi.org/10.1145/1143844.1143874.

<!-- page 16 -->

Servos, Daniel, Osborn, Sylvia L., 2017. Current research and open problems in attribute- Tang, Benxiao, Zhang, Shilin, Zhu, Fei, Ye, Aoshuang, 2025. CAPRA: context-aware based access control. ACM Comput. Surv. 49 (4), 1–45. https://doi.org/10.1145/ 3007204. Shukla, Ankur, Katt, Basel, Nweke, Livinus Obiora, Yeng, Prosper Kandabongee, patch risk assessment for detecting immature vulnerability in open-source software. Comput. Secur. 157, 104540. https://doi.org/10.1016/j.cose.2025.104540. Torres-Arias, Santiago, Afzali, Hammad, Kuppusamy, Trishank Karthik, Curtmola, Reza, Weldehawaryat, Goitom Kahsay, 2022. System security assurance: a systematic literature review. Comput. Sci. Rev. 45, 100496. https://doi.org/10.1016/j. cosrev.2022.100496. Sinan, Maysa, Shahin, Mojtaba, Gondal, Iqbal, 2025. Implementing and integrating Cappos, Justin, 2019. In-toto: providing farm-to-table guarantees for bits and bytes. In: 28th USENIX Security Symposium, pp. 1393–1410. Utting, Mark, Pretschner, Alexander, Legeard, Bruno, 2012. A taxonomy of model-based testing approaches. Softw. Test. Verif. Reliab. 22 (5), 297–312. https://doi.org/ 10.1002/stvr.456. Whittaker, James A., 2000. What is software testing? And why is it so hard? IEEE Softw. security controls: a practitioners’ perspective. Comput. Secur. 156, 104516. https:// doi.org/10.1016/j.cose.2025.104516. Skandylas, Charilaos, Asplund, Mikael, 2025. Automated penetration testing: 17 (1), 70–79. https://doi.org/10.1109/52.819971. Zeller, Andreas., 2002. Isolating cause-effect chains from computer programs. ACM formalization and realization. Comput. Secur. 155, 104454. https://doi.org/ 10.1016/j.cose.2025.104454. SIGSOFT Softw. Eng. Notes 27 (6), 1–10. https://doi.org/10.1145/605466.605468.
