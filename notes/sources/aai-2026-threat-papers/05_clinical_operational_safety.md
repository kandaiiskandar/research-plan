# Defining Operational Safety in Clinical Artificial Intelligence Systems

> Source PDF: `Defining operational safety in clinical artificial intelligence systems(1).pdf`

> Extraction note: Text extracted from the uploaded PDF using Poppler `pdftotext -layout`. Page boundaries are preserved below. Formatting, equations, tables, and multi-column reading order may not perfectly match the original PDF. Use the original PDF for authoritative visual/layout verification.


---

## PDF Page 1

```text
                                    npj | digital medicine                                                                                                                                Article
                                    Published in partnership with Seoul National University Bundang Hospital




                                                                                                                                                      https://doi.org/10.1038/s41746-026-02450-7


                                    Deﬁning operational safety in clinical
                                    artiﬁcial intelligence systems
                                                                                                                                                                                    Check for updates

                                    Young-Tak Kim1, Hyunji Kim1, Manisha Bahl1, Michael H. Lev1, Ramon Gilberto González1,
                                    Michael S. Gee1 & Synho Do1,2,3


                                    The clinical adoption of artiﬁcial intelligence (AI) has focused on enabling automation, but conventional
                                    accuracy metrics fail to answer a key question: when is it safe to trust an AI system? We introduce the
                                    Safety-Aware Receiver Operating Characteristic (SA-ROC) framework, which deﬁnes operational
                                    safety as an ability to meet pre-speciﬁed reliability levels. The SA-ROC curve delineates a Rule-in and a
                  1234567890():,;
1234567890():,;




                                    Rule-out Safe Zone, where autonomous action is permitted, and a Gray Zone, where human review is
                                    mandated. To quantify this non-automated workload, we introduce the Gray Zone Area (ΓArea), a metric
                                    measuring the operational cost of indecision. Our framework reveals a key reversal: in a case study of
                                    two FDA-cleared algorithms for cancer screening, the model with a statistically superior AUC was
                                    found to be operationally less safe for high-conﬁdence screening. SA-ROC enables active
                                    governance, translating clinical policy into optimized workﬂows that inform operational safety and
                                    complement regulatory safety evaluation.


                                    A paradox has emerged in clinical artiﬁcial intelligence (AI): despite hun-          clinical time-series16, and empirically validating reliability for medical image
                                    dreds of algorithms demonstrating high discriminative power in statistical           classiﬁcation17. Nonetheless, these powerful methods often provide a set of
                                    benchmarks and achieving regulatory approval, their integration into rou-            heterogeneous analytical signals, such as coverage-valid label sets, spatially
                                    tine care remains tentative1–3. The reason is not merely a lack of accuracy, but     deﬁned safe regions, abstention ﬂags18, which leave clinicians to shoulder the
                                    a signiﬁcant gap between an AI’s validated statistical performance and the           cognitive burden of mentally integrating them into a concrete operating
                                    operational safety required for clinical trust, leaving a ‘validation debt’ that     policy6,7,19. This lack of a uniﬁed operational directive presents a key
                                    must be paid at the point of care4,5. This uncertainty presents clinicians with      translational gap between statistical validation and safe clinical
                                    a signiﬁcant challenge: navigating between reliance on an opaque algorithm           automation20,21.
                                    and the risk of defensive over-testing, while remaining accountable for the                To address this translational gap, we introduce the Safety-Aware
                                    AI’s potential errors6–8. This challenge in establishing trust is a key barrier to   Receiver Operating Characteristic (SA-ROC) framework, a tool designed
                                    realizing the full potential of AI in safely automating cognitive tasks and          speciﬁcally to synthesize these heterogeneous analytical signals into a uni-
                                    reducing clinician burden9.                                                          ﬁed operational directive. This synthesis enables safe, partial automation by
                                          Contemporary methods offer valuable but partial guidance for safe              setting clear, actionable trust conditions instead of imposing additional
                                    automation: decision-curve analysis gauges clinical utility10, selective pre-        cognitive burden on clinicians (Fig. 1). In this work, we deﬁne operational
                                    diction enables abstention under cost trade-offs11, and conformal prediction         safety as knowing the precise conditions under which a clinician can con-
                                    provides ﬁnite-sample, distribution-free coverage of set-valued outputs6.            ﬁdently act on an AI’s recommendation to rule in or rule out a disease. To
                                    Importantly, a growing body of work has begun to push conformal pre-                 translate this principle into a clear operational map, the framework uses a
                                    diction beyond pure accuracy toward operational safety assurances, for               key hyperparameter: the safety level (α). The safety level (α) represents the
                                    example, delivering sample-efﬁcient safety guarantees for robotic warning            clinical reliability target set by the clinician, indicating the minimum per-
                                    systems12, deﬁning probabilistically certiﬁed safe regions in input space            formance threshold required to establish actionable trust. It is deﬁned by
                                    where local error rates are bounded13, and improving statistical reliability of      two speciﬁc objectives: the rule-in safety level (α+), which denotes the
                                    interpretable rule-based classiﬁers via a novel score function for conformal         minimum acceptable positive predictive value (PPV) required to trust a
                                    prediction14. In medicine, conformal prediction has been applied to surface          rule-in action, and the rule-out safety level (α⁻), which denotes the minimum
                                    and manage uncertainty across tasks, ﬂagging ambiguous cases or forming              acceptable negative predictive value (NPV) required to trust a rule-out
                                    prediction sets for disease course monitoring15, reducing false alarms in            action.


                                    1
                                        Department of Radiology, Massachusetts General Hospital, Harvard Medical School, Boston, MA, USA. 2Kempner Institute, Harvard University, Boston, MA, USA.
                                    3
                                        KU-KIST Graduate School of Converging Science and Technology, Korea University, Seoul, Republic of Korea.     e-mail: sdo@mgh.harvard.edu


                                    npj Digital Medicine | (2026)9:281                                                                                                                                 1
```

---

## PDF Page 2

```text
https://doi.org/10.1038/s41746-026-02450-7                                                                                                                                                                                                                                                                Article

       a

                                                                                                                                                                                                                                 How well does                           TPR
                                                                                                                                                                                                                                 the AI discriminate?

                                                                                                                                                                                                                                                                                  FPR
                                                                                                                                                   1             High
                                                                                                                                                                                                                                                                       Conventional ROC and
                                                                                                                                                                 risk
                                                                                                                                                                                                                                                                     Discrimination Performance
                                                              Input                                        Output
                                                                                                                                                                                                                      Evaluation Axis
                                                                                                                                                                 Low
                                                                                                                                                   0             risk
                                      Patient Data                           Clinical AI Model                                 Predicted Risk Score                                                                                                                      TPR

                                                                                                                                                                                                                                 How safe can it
                                                                                                                                                                                                                                 be automated?
                                                                                                                                                                                                                                                                                FPR
                                                                                                                                                                                                                                                                     Safety-Aware ROC with
                                                                                                                                                                                                                                                                     Operational Safety Profile
       b                                                                                                                                                                                    c
                                                                 e.g., PPV = 100%                                                                                                                                        -                                                                    +
       High risk 1                                                                                                               +                                                                                  α⁻Z Safe                              Z Gray                            Z Safe α⁺
                                                                                                    Rule-in Safe Zone ( Z Safe ):
                                                                                                    The score range where the PPV meets                                                                          100%                                                                                 100%
                                                                                                    the safety level (PPV ≥ α⁺ )                                                                                  95%                                                                                 95%
                                                                                                    Reliable enough for confident escalation                                                                      90%                                                                                 90%
                                       0.8
                                                                                                                                                                                                                        0        0.2            0.4        0.6                    0.8           1
                                                                                                                                                                                                                        Low risk             Predicted Risk Score                       High risk
           Predicted Risk Score




                                       0.6                                                          Gray Zone ( Z Gray ):                                                                   d
                                                                                                    The score range of algorithmic uncertainty                                                                                                            Rule-out Safe Zone
                                                                                                    where reliability fails to meet the safety level                                                                                                    90%        95%      100% α⁻
                                                                                                                                                                                                                                                                                                      −
                                                                                                    Mandating human expert review                                                                                                                                                                 Z Safe
                                       0.4                                                                                                                                                                                                                                                        1


                                                                                                                                                                                                                                   θ
                                                                                                                                                                                                                                                                                                  0.8
                                       0.2                                                                                                 −                                                                                                 90
                                                                                                    Rule-out Safe Zone ( Z Safe ):                                                                                                      Z Gray
                                                                                                    The score range where the NPV meets
                                                                                                                                                                                                                                                                                                  0.6




                                                                                                                                                                                                                                                                                                           Sensitivity
                                                                                                    the safety level (NPV ≥ α⁻)                                                                                                                          95
                                                                                                                                                                                                                90%                                     Z Gray
                                                                                                    Reliable to be safely deprioritized
                                                                                                                                                                                            Rule-in Safe Zone
        Low risk 0
                                                                 e.g., NPV = 100%
                                                                                                                                                                                                                                                                                                  0.4
                                                      Negative    Positive                          The safety level required to answer:
                                                                                                                                                                                                                                                                          100
                                                                                                    Rule-in Safety Level (α⁺)                                                                                   95%                                                      Z Gray
                                                                                                                                                                                                                                                                                                  0.2
                                             Positive Predictive Value =                            How strong must the evidence be for                                                                                         Gray Zone Area (ΓArea):
                                                                                                    a positive prediction to warrant clinical action?                                                                           The area of the Gray Zone

                                                                                                    Rule-out Safety Level (α⁻  )                                                                                100%                                                                              0
                                                                                                                                                                                                                       +
                                                                                                    How strong must the evidence be for                                                                           α⁺ Z Safe 0          0.2          0.4            0.6          0.8         1
                                         Negative Predictive Value =
                                                                                                    a negative prediction to justify clinical inaction?                                                                                            1 - Specificity

                                                                   90                       95                       100
       e                                                          Z Gray                  Z Gray                    Z Gray                                  f
                                      100                                                                                1                                                                                                                         1               Rule-in
                                                                                                                                                                                                                                                                   Safe Zone
                                                                              Stricter Safety
                                                                              → More Human Review
                                       80                                                                                  0.8                                                                                                                    0.8
                                                                                                                                                                                                                                                                                         Marked for
           % of Cohort in Gray Zone




                                                                                                                                  Gray Zone Area (ΓArea )




                                                                                                                                                                                                                                                                                        Priority Action
                                                                                                                                                                 Patient Data                       Clinical AI Model
                                       60                                                                                  0.6                                                                                                                    0.6
                                              Less Stringent Safety                                                                                             Rule-in Safety Level (α⁺)                                                                          Gray Zone
                                              → Higher Degree of Automation                                                                                     95%
                                       40                                                                                  0.4                                  Rule-out Safety Level (α⁻)                                                        0.4
                                                                                                                                                                99%                                                                                                                     Needs Full
                                                                                                                                                                                                                                                                                      Clinical Review
                                       20                                                                                  0.2                                                                                                                    0.2
                                                                                                                                                                                                                                                                   Rule-out
                                                                                    % of Cohort in Gray Zone                                                                                                                                                       Safe Zone
                                                                                    Gray Zone Area (ΓArea)
                                        0                                                                                  0                                                                                                                       0
                                                 86      88        90        92      94            96      98       100                                                                        Safety Level                                        Predicted                            Deprioritize
                                                                      Safety Level (α, %)                                                                                                   Defined by Clinician                                   Risk Score                           with Caution

Fig. 1 | Conceptual diagram of the Safety-Aware ROC (SA-ROC) framework. a A                                                                                          operational landscape by color-coding segments according to their corresponding
standard AI model produces a continuous risk score (i.e., the predicted probability                                                                                  zones. The optimal threshold θ is indicated. The Gray Zone Area (ΓArea) is shown as
from a binary classiﬁer) for each patient. This output can be evaluated along two                                                                                    a shaded rectangle in the top-left corner, providing an integrated view of both
distinct axes: its discriminative performance, often assessed using metrics like the                                                                                 discrimination and operational uncertainty. e The Safety Proﬁle Curve plots the
area under the ROC curve, and its operational safety, which is visualized and                                                                                        Gray Zone proportion and ΓArea across the safety levels (α), where α denotes α+ = α⁻
quantiﬁed by the SA-ROC framework. b The framework partitions the model’s                                                                                            and asymmetric targets are written explicitly. This enables evaluation of the trade-
score distribution. Based on a user-deﬁned safety criterion (α), it identiﬁes a Rule-in                                                                              off between safety and automation. f The framework maps AI outputs to a three-
Safe Zone (Z þ                                                  
              Safe ) at high scores and a Rule-out Safe Zone (Z Safe ) at low scores, and an                                                                         tiered clinical workﬂow: autonomous de-prioritization (Rule-out Safe Zone),
intermediate Gray Zone (Z Gray ). c Score-range partitioning based on varying safety                                                                                 essential human review (Gray Zone), and autonomous case escalation (Rule-in Safe
levels (α). Each bar demonstrates how increasing the required reliability shrinks the                                                                                Zone), thereby guiding clinical decisions and reducing cognitive burden.
Safe Zones and expands the Gray Zone. d The SA-ROC curve visualizes the model’s




npj Digital Medicine | (2026)9:281                                                                                                                                                                                                                                                                                       2
```

---

## PDF Page 3

```text
https://doi.org/10.1038/s41746-026-02450-7                                                                                                                                                                                                                                                                                                                                                       Article

      The core function of the SA-ROC framework is to take these clinician-                                                                                                                                        SA-ROC framework enables a critical shift from using AI as a static pre-
deﬁned reliability targets (α+ and α−) as inputs, analyze the local data, and                                                                                                                                      diction tool to deploying it as a dynamically governed component of the
then automatically identify the speciﬁc prediction score thresholds required                                                                                                                                       clinical workﬂow.
to achieve those targets. Thus, this process identiﬁes two distinct score                                                                                                                                                In this paper, we demonstrate the framework’s effectiveness through
cutoffs: a high-score cutoff deﬁning the start of the Rule-in Safe Zone (which                                                                                                                                     extensive simulations and a real-world case study using two FDA-cleared AI
satisﬁes α+) and a low-score cutoff deﬁning the end of the Rule-out Safe Zone                                                                                                                                      solutions that are machine learning classiﬁers implemented as a convolu-
(which satisﬁes α⁻). Based on these data-driven thresholds, the framework                                                                                                                                          tional neural network (CNN) and perform binary classiﬁcation for cancer
then partitions the model’s predictions into three distinct zones. The ﬁrst is                                                                                                                                     detection. By showing how diverse operational policies can be derived to
the Rule-in Safe Zone, which represents a range of high-risk scores where the                                                                                                                                      meet speciﬁc clinical demands, this work offers a systematic framework for
model’s performance meets or exceeds the speciﬁed reliability target (α+) for                                                                                                                                      developing, governing, and validating clinical AI. To address the persistent
ruling in; cases in this zone are deemed reliable enough for autonomous                                                                                                                                            gap between statistical performance and clinical trust, our ultimate goal is to
escalation or action. The second is the Rule-out Safe Zone, which represents                                                                                                                                       provide the methodology required to establish operational trustworthiness
a range of low-risk scores where the model’s performance meets or exceeds                                                                                                                                          for practical clinical automation.
the speciﬁed reliability target (α⁻) for ruling out; cases in this zone are deemed
reliable enough for autonomous de-prioritization. The third is the Gray                                                                                                                                            Results
Zone, which corresponds to the intermediate range of uncertainty where the                                                                                                                                         Score distribution proﬁle determines operational safety
model’s reliability fails to meet either the rule-in (α+) or rule-out (α⁻) safety                                                                                                                                  A single metric like area under the curve (AUC) does not capture an AI’s full
target, signifying that these cases are designated for mandatory human                                                                                                                                             operational value, which is better understood through its distribution of
expert review. To quantify the operational burden of this non-automated                                                                                                                                            prediction scores. To illustrate this, our simulation studies use the SA-ROC
cohort, the framework introduces the Gray Zone Area (ΓArea), a novel metric                                                                                                                                        framework to analyze four distinct AI models, exhibiting how different score
that allows stakeholders to evaluate the trade-off between the desired safety                                                                                                                                      distribution proﬁles produce substantially different operational character-
level (α) and the consequential cost of indecision.                                                                                                                                                                istics. For instance, a model with a modest AUC of 0.768 but with scores
      This framework’s primary utility lies in its ability to facilitate a practical                                                                                                                               sharply peaked for positive cases established a robust Rule-in Safe Zone,
human-in-the-loop workﬂow, a process we term policy-driven automation.                                                                                                                                             making it effective for high-conﬁdence conﬁrmation tasks (Fig. 2a). Con-
This workﬂow is not ﬁxed; it is actively governed by the clinical policies                                                                                                                                         versely, another model with a similar AUC of 0.780 but skewed towards
derived within the framework. These policies can be established in two                                                                                                                                             negative cases produced an expansive Rule-out Safe Zone ideal for high-
primary ways: either by directly choosing the safety level (α), or, for more                                                                                                                                       volume screening (Fig. 2b). Both scenarios demonstrate that signiﬁcant
complex scenarios, by deﬁning a clinical utility function that balances the                                                                                                                                        operational value can emerge from models optimized for speciﬁc clinical
costs of errors against the beneﬁts of correct decisions, allowing the fra-                                                                                                                                        functions, even when their overall performance is not top-tier. This prin-
mework to derive the optimal policy automatically. This process entails                                                                                                                                            ciple becomes particularly important, however, when comparing models
having the AI system autonomously handle all cases within the resulting                                                                                                                                            where aggregate metrics show no difference.
Safe Zones (e.g., for autonomous de-prioritization or escalation), while the                                                                                                                                             We contrasted two high-performing models with nearly identical
diagnostically challenging cases within the Gray Zone are, by design, esca-                                                                                                                                        AUCs of 0.960 and found their operational safety proﬁles diverged mark-
lated for human review. By translating clinical policy into AI behavior, the                                                                                                                                       edly under the most stringent conditions (α = 100%). The model with wider,

      a                                         90%         95%                100%          α⁺                                                                                        α⁻                     b α⁻                 100%              95%        90%                                                                                             90% 95%      100%            α⁻
                                     θ                                                        +                                                                                            −                        −                                                         θ                                                                                                                  −
                                                                                             Z Safe                                                                                    Z Safe                  Z Safe                                                                                                                                                                        Z Safe
                                                                                                                                                                                       1                                                                                                                                                                                                     1

                 5                                                                                                                                                                                                      5
                                                                                                                                                                                       0.8                                                                                                                                                                                                   0.8

                 4                                                                                                                                                                                                      4
                                                                                                                                                                             90
                                                                                                                                                                                       0.6                                                                                                                                                                                                   0.6
                                                                                                                                                                                                Sensitivity




                                                                                                                                                                                                                                                                                                                                                                                                      Sensitivity
                                                                                                                                                                            Z Gray
                 3                                                                                90%                                                                                                                   3
       Density




                                                                                                                                                                                                              Density




                                                                                                                                                                       95
                                                                                                                                                                   Z Gray              0.4                                                                                                                                                                                                   0.4
                                                                                                                                                                             100
                 2                                                                                                                                                          Z Gray                                      2

                                                                                                                                                                                       0.2                                                                                                                                                                           95
                                                                                                                                                                                                                                                                                                                                                                                             0.2
                 1                                                                              100%                                                                                                                    1                                                                                                                                          Z Gray
                                                                                                                                                                                                                                                                                                                                                           90        100
                                                                                                                                                                                                                                                                                                                                                          Z Gray   Z Gray
                                                                                                                                                              AUC: 0.768                                                                                                                                                                                                    AUC: 0.780
                 0                                                                                                                                                                     0                                0                                                                                                                                                                    0
                                                                                                           +                                                                                                                                                                                                             +
                     0   0.2             0.4              0.6            0.8             1            α⁺ Z Safe 0           0.2            0.4       0.6         0.8               1                                        0           0.2            0.4             0.6              0.8            1            α⁺ Z Safe 0         0.2              0.4        0.6      0.8         1
                                     Predicted Risk Score                                                                                  1 - Specificity                                                                                          Predicted Risk Score                                                                                 1 - Specificity
      c α⁻ 100%                95%             90%    90%         95%            100%        α⁺                           90%                      95%                      100% α⁻                           d α⁻ 100%                   95%          90%           90%          95%           100%       α⁺                          90%                95%               100%             α⁻
             −                                        θ                                       +                                                                                            −                        −                                           θ                                           +                                                                                    −
        Z Safe                                                                               Z Safe                                                                                    Z Safe                  Z Safe                                                                                      Z Safe                                                                            Z Safe
                                                                                                                    90
                                                                                                                                                                                       1                                                                                                                                          90
                                                                                                                                                                                                                                                                                                                                                                                             1
                                                                                                                Z Gray                                                                                                                                                                                                        Z Gray
                 5                                                                                                         95
                                                                                                                                                                                                                        5
                                                                                                                         Z Gray                                                                                                                                                                                                         95
                                                                                                  90%                                                                                                                                                                                                           90%                    Z Gray
                                                                                                                                                                                       0.8                                                                                                                                                                                                   0.8
                                                                                                                                   100                                                                                                                                                                                                           100
                                                                                                                                  Z Gray                                                                                                                                                                                                        Z Gray
                 4                                                                                                                                                                                                      4
                                                                                                                                                                                       0.6                                                                                                                      95%                                                                          0.6
                                                                                                                                                                                                Sensitivity




                                                                                                                                                                                                                                                                                                                                                                                                      Sensitivity




                 3                                                                                                                                                                                                      3
       Density




                                                                                                                                                                                                              Density




                                                                                                  95%
                                                                                                                                                                                                                                                                                                                                                          Γ 1 : 0.344
                                                                                                                                                                                       0.4                                                                                                                                                                                                   0.4
                 2                                                                                                                                                                                                      2
                                                                                                                                                             Γ 1 : 0.709
                                                                                                                                                                                       0.2                                                                                                                    100%                                                                           0.2
                 1                                                                                                                                                                                                      1
                                                                                                100%
                                                                                                                                                              AUC: 0.960                                                                                                                                                                                                    AUC: 0.960
                 0                                                                                                                                                                     0                                0                                                                                                                                                                    0
                                                                                                           +                                                                                                                                                                                                             +
                     0   0.2             0.4              0.6            0.8             1            α⁺ Z Safe 0           0.2            0.4       0.6         0.8               1                                        0           0.2            0.4             0.6              0.8            1            α⁺ Z Safe 0         0.2              0.4        0.6      0.8         1
                                     Predicted Risk Score                                                                                  1 - Specificity                                                                                          Predicted Risk Score                                                                                 1 - Specificity


                                                                                                                                                                                   +                                                                    −                                        α
                                                                   Class Distribution                                                              Rule-in Safe Zone ( Z Safe )                                                 Rule-out Safe Zone ( Z Safe )                     Gray Zone ( Z Gray )
                                                                        Positive Cases       Negative Cases              Overlap Region               α⁺= 100%              α⁺= 95%                   α⁺= 90%                      α⁻= 100%       α⁻= 95%           α⁻= 90%          α = 100%        α = 95%           α = 90%



Fig. 2 | Simulated scenarios illustrating how score distribution shapes affect the                                                                                                                                 the sum of sensitivity and speciﬁcity. a A model with a skewed distribution creating a
Safety-Aware ROC (SA-ROC) curve. Each panel shows a model with a distinct                                                                                                                                          strong Rule-in Safe Zone, suitable for conﬁdent case escalation. b A model with an
operational safety proﬁle, with speciﬁc AUC and the Gray Zone Area (ΓArea) values                                                                                                                                  opposing distribution skew, creating an expansive Rule-out Safe Zone ideal for safely
provided in the plots. Speciﬁcally, Γ1 denotes the Gray Zone Area at the maximal                                                                                                                                   excluding low-risk cases. c A high-AUC model with wide, overlapping distributions
safety level (α = 100%). The plotted Gray Zones are computed under a symmetric                                                                                                                                     resulting in a large Gray Zone and high operational uncertainty. d A model with the
setting, where α denotes α+ = α⁻, reﬂecting equal PPV and NPV targets. The circular                                                                                                                                same high AUC but narrow, well-separated distributions, resulting in a substantially
marker on each ROC curve denotes the threshold θ, deﬁned as the point maximizing                                                                                                                                   smaller Gray Zone and more reliable automation.



npj Digital Medicine | (2026)9:281                                                                                                                                                                                                                                                                                                                                                                                  3
```

---

## PDF Page 4

```text
https://doi.org/10.1038/s41746-026-02450-7                                                                                                                                                                                                                                                                                                             Article

       a                                                    FDA-Cleared AI Solution #1                                                                            FDA-Cleared AI Solution #2                                                        b
                                                                                                                                                                                                                                                                                  300
                                                               90%               95%               100%            α⁻                                                                           90%, 95%, 100%             α⁻                                                                  θAI #1
                                                                                                                       −                                                                                                       −




                                                                                                                                                                                                                                                                       Density
                                                                                                                   Z Safe                                                                                                  Z Safe                                                 150
                                                                                                                   1                                                                                                       1
                                                                                                                                                                                                                                                                                    0
                                                                                                                                                                                                                                                                                   1

                                                                                                                   0.8                                                                                                     0.8
                                                    90




                                                                                                                                                                                                                                                    Score of FDA-Cleared AI #2
                                                   Z Gray                                                                                                                                                                                                                         0.8
                                                                95
               90%                                             Z Gray
                                                                                                                   0.6                                                                                                     0.6




                                                                                                                            Sensitivity




                                                                                                                                                                                                                                    Sensitivity
                                                                                                                                                                                                                                                                                  0.6
               95%                                                                          100
                                                                                        Z Gray
                                                                                                                   0.4                                                  90                                                 0.4
                                                                                                                                                                       Z Gray                                                                                                     0.4
                                                                                                                                                                        95
                                                                                                                                          90%                          Z Gray
       100%                                                                                                                                                                                                                                                                                                                                         θAI #2
                                                                                                                   0.2                    95%                                                                              0.2                                                    0.2
                                                                                AUC: 0.928 (0.911–0.943)                                                                                AUC: 0.882 (0.861–0.901)
                                                                                Γ 1 : 0.415 (0.358–0.452)                                                               100             Γ 1 : 0.430 (0.389–0.469)
                                                                                                                                          100%                         Z Gray
                                                                                Γ 0.95 : 0.158 (0.101–0.232)                                                                            Γ 0.95 : 0.403 (0.332–0.460)
                                                                                Γ 0.90 : 0.061 (0.035–0.102)       0                                                                    Γ 0.90 : 0.356 (0.280–0.414)       0                                                       0
                                        +                                                                                                           +
                                  α⁺ Z Safe 0            0.2            0.4         0.6           0.8          1                            α⁺ Z Safe 0           0.2            0.4          0.6       0.8            1                                                                0        0.2       0.4       0.6       0.8         1 0    150 300
                                                                                                                                                                                                                                                                                                                                                 Density
                                                                              1 - Specificity                                                                                   1 - Specificity                                                                                                  Score of FDA-Cleared AI #1
                                                                 +                                                                                                α
                                   Rule-in Safe Zone ( Z Safe )                  α⁺= 100%           α⁺= 95%                α⁺= 90%                 Gray Zone ( Z Gray )           α = 100%           α = 95%        α = 90%                                                                    Positive Case        Rule-in Safe Zone (α⁺= 100%)
                                                                 −                                                                                                                                                                                                                             Negative Case        Rule-out Safe Zone (α⁻= 100%)
                                  Rule-out Safe Zone ( Z Safe )                  α⁻= 100%           α⁻= 95%                α⁻= 90%
       c                                                                                                                                                                 d
                                                                                                                                           90           95      100                                 FDA-Cleared                                                                  Cross-Model                        FDA-Cleared
                                                                                                                                          Z Gray     Z Gray   Z Gray
                                  100                                                                                                                                                               AI Solution #1                                                               Concordance                        AI Solution #2
                                                FDA-Cleared AI Solution #1
       % of Cohort in Gray Zone




                                                                                                                                                                                             Rule-in Safe Zone (α⁺= 100%)                                                                                      Rule-in Safe Zone (α⁺= 100%)
                                   80           FDA-Cleared AI Solution #2                                                                                                                                    170 (17.0%)                                                                                      67 (6.7%)
                                                                                                                                                                                                                                                                                   50 (5.0%)                            67 (6.7%)
                                   60                                                                                                                                                                 170 (17.0%)
                                                                                                                                                                                                                                    120 (12.0%)
                                                                                                                                                                             True Positive                                                                                                  17 (1.7%)
                                                                                                                                                                                                                                                                                                                                              True Positive
                                   40                                                                                                                                         338 (33.8%)
                                                                                                                                                                                                                                                                                                                       333 (33.3%)            400 (40.0%)
                                                                                                                                                                                                      168 (16.8%)
                                   20
                                                                                                                                                                         False Positive                                                                                                                          Gray Zone
                                    0                                                                                                                                        95 (9.5%)                                                                                                                           643 (64.3%)
                                                                                                                                                                        False Negative                                                                                            483 (48.3%)
                                        50                     60                      70                 80                               90                  100                                          Gray Zone
                                                                                                                                                                             62 (6.2%)
                                                                                     Safety Level (α, %)                                                                                                   663 (66.3%)                                                                                                                        False Positive
                                                                                                                                                                                                                                                                                                                                              310 (31.0%)
                                  0.5
                                                FDA-Cleared AI Solution #1
                                                                                                                                                                                                      338 (33.8%)
       Gray Zone Area (ΓArea )




                                  0.4           FDA-Cleared AI Solution #2                                                                                                True Negative                                             163 (16.3%)
                                                                                                                                                                            505 (50.5%)                                                                                                     40 (4.0%)
                                  0.3                                                                                                                                                                                                                                                                                                         True Negative
                                                                                                                                                                                                                                                                                                                                              290 (29.0%)
                                                                                                                                                                                                      167 (16.7%)
                                  0.2                                                                                                                                                                                                                                             127 (12.7%)

                                  0.1                                                                                                                                                    Rule-out Safe Zone (α⁻= 100%)                                                                                         Rule-out Safe Zone (α⁻= 100%)
                                                                                                                                                                                                           167 (16.7%)                                                                                         290 (29.0%)
                                    0
                                        50                     60                      70                 80                               90                  100                 True Positive          True Negative                           Rule-in Safe Zone                                     Rule-out Safe Zone           Gray Zone (α = 100%)

                                                                                     Safety Level (α, %)                                                                           False Positive         False Negative                          Rule-in Concordance                                   Rule-out Concordance         Gray Zone Concordance


Fig. 3 | Comparative operational safety analysis of two FDA-cleared mammo-                                                                                                              and θAI #2 are marked to indicate each model’s decision boundary. c Safety Proﬁle
graphy AI solutions. a Safety-Aware ROC (SA-ROC) curves for AI Solution #1 and                                                                                                          Curves comparing the two models across levels ranging from 50% to 100%; top:
#2, Rule-in Safe (red), Rule-out Safe (blue), and Gray (gray) Zones deﬁned at                                                                                                           percentage of cases in the Gray Zone; bottom: corresponding ΓArea values. d Sankey
α = 90%, 95%, and 100%. AUC and ΓArea are shown with 95% conﬁdence intervals;                                                                                                           diagrams showing case disposition at α = 100%, from reference standard (outside) to
speciﬁcally, Γ1, Γ0.95, and Γ0.90 denote the Gray Zone Areas at safety levels α = 100%,                                                                                                 Safe Zone classiﬁcation (center) for each model, with the center panel visualizing
95%, and 90%, respectively. Each ROC curve includes a circular marker indicating                                                                                                        cross-model zone concordance. All zones and metrics are computed under a sym-
the predeﬁned threshold θ, as provided by the respective AI vendors. b Scatter plot                                                                                                     metric safety policy, where α denotes α+ = α⁻, indicating equal PPV and NPV
comparing predicted scores from both models, overlaid on a 2D Safe Zone grid at                                                                                                         thresholds.
α = 100%, illustrating cross-model agreement and disagreement. Thresholds θAI #1


overlapping distributions resulted in a large Gray Zone (ΓArea = 0.709),                                                                                                                reduction at moderate safety levels (α < 95%; Fig. 3c). However, this trade-
leaving a high burden of non-automated workload (Fig. 2c). In stark con-                                                                                                                off reverses when maximal safety is the priority. At the highest safety level of
trast, the model with narrow, well-separated distributions yielded a sub-                                                                                                               α = 100%, where no false negatives in the Rule-out Safe Zone are tolerated,
stantially smaller Gray Zone (ΓArea = 0.344), enabling a far greater degree of                                                                                                          the operational superiority of AI #2 emerges. AI #2 conﬁdently and correctly
safe automation (Fig. 2d). These scenarios show that the SA-ROC frame-                                                                                                                  ruled out 290 true negative cases, which safely removed 29.0% of the entire
work can distinguish models with nearly identical AUCs but different                                                                                                                    patient cohort from the radiologist’s workload. This represents a substantial
capacities for safe automation. This positions the framework as a valuable                                                                                                              improvement over AI #1, which cleared only 167 cases (16.7% of the
diagnostic tool in the AI development lifecycle, providing the capability to                                                                                                            cohort), with a difference of 123 cases in the Rule-out Safe Zone in favor of
dissect how a model’s intrinsic characteristics interact with a given data                                                                                                              AI #2 (95% conﬁdence interval: 87.0–150.0). Crucially, 163 of the cases that
distribution, thereby identifying speciﬁc weaknesses and guiding targeted                                                                                                               AI #1 left in its uncertain Gray Zone were conﬁdently ruled out by AI #2
efforts in both model reﬁnement and data curation.                                                                                                                                      (Fig. 3d). This result shows that the AUC can be misleading and that models
                                                                                                                                                                                        should be evaluated for their operational safety to understand their true
Performance reversal between FDA-cleared AI solutions                                                                                                                                   clinical utility. Furthermore, this granular analysis suggests the potential for
A comparison of two FDA-cleared mammography AIs shows a notable                                                                                                                         synergistic implementation strategies. For instance, a hybrid workﬂow
performance reversal: the model with superior statistical performance was                                                                                                               could ﬁrst leverage AI #2 for its superior high-conﬁdence rule-out capability
not the most operationally robust for high-conﬁdence screening. Although                                                                                                                to reduce the initial workload, and then triage the remaining, more
AI Solution #1 demonstrated a higher AUC than AI Solution #2 (0.928 vs.                                                                                                                 ambiguous cases with AI #1, potentially capitalizing on the distinct strengths
0.882; Fig. 3a, b), this advantage translated to better operational efﬁciency                                                                                                           of both models. Additionally, to assess generalizability, we analyzed
only for less stringent tasks, as evidenced by its more rapid Gray Zone                                                                                                                 operational stability across varying prevalence conditions (1%–40%) to


npj Digital Medicine | (2026)9:281                                                                                                                                                                                                                                                                                                                             4
```

---

## PDF Page 5

```text
https://doi.org/10.1038/s41746-026-02450-7                                                                                                                                                                                         Article

                                                         FDA-Cleared AI Solution #1                                                                                          FDA-Cleared AI Solution #2
                                                Rule-out Safe Zone     Gray Zone       Rule-in Safe Zone                                                           Rule-out Safe Zone     Gray Zone      Rule-in Safe Zone
                                     Human                                                                                                              Human
                                             68.3     58.0      58.5     61.6      90.0      93.8      98.2                                                     64.1       64.1    64.1     64.7      93.4     95.7      98.5
                               100   Acc (%)                                                                                                      100   Acc (%)
       Human Performance (%)




                                                                                                                          Human Performance (%)
                                80                                                                                                                 80


                                60                                                                                                                 60


                                40                                                                                                                 40


                                20                                                                                                                 20
                                     Stricter                                                                 Stricter                                  Stricter                                                                Stricter
                                     Rule-out                                                                 Rule-in                                   Rule-out                                                                Rule-in
                                 0                                                                                                                  0
                                            100%     95%     90%          90       90%      95%     100%                                                       100%     95%     90%          90       90%      95%     100%
                                                                         Z Gray                                                                                                             Z Gray
                                            Rule-out Safe Level (α⁻
                                                                  )                Rule-in Safe Level (α⁺
                                                                                                        )                                                      Rule-out Safe Level (α⁻
                                                                                                                                                                                     )                Rule-in Safe Level (α⁺
                                                                                                                                                                                                                           )

                                                                       True Positive          True Negative              False Positive                                False Negative       Accuracy

Fig. 4 | Analysis of human radiologist performance within safety and Gray Zones                                           out Safe Zones (α⁻ = 100%, 95%, 90%). The stacked bars are colored by the radi-
of the FDA-cleared AI solutions. The charts show the proportional diagnostic                                              ologist’s outcome: true positive (blue), true negative (green), false positive (red), and
outcomes of human assessments on cases stratiﬁed by the Safe Zones of AI Solution                                         false negative (purple). Red triangles and corresponding numeric labels indicate the
#1 and #2. For each model, cases are grouped into Rule-in Safe Zones (α+ = 100%,                                          overall human accuracy within each zone.
95%, 90%), the Gray Zone deﬁned under the α = 90% safety level (Z 90
                                                                  Gray ), and Rule-




characterize the distinct stability proﬁles of each model and to investigate the                                                Beyond direct rules, the framework navigates more complex scenarios
dynamics of the performance reversal in the Rule-out Safe Zone (α⁻ = 100%)                                                by maximizing a clinical utility function that weighs the nuanced costs of
(see Supplementary Note 1).                                                                                               errors against the beneﬁts of correct decisions. While a balanced utility
                                                                                                                          function (Fig. 5d) offers a sensible default optimization, the framework’s
Patterns of human diagnostic behavior in AI Safe Zones                                                                    utility is particularly evident in its ability to resolve policies with stringent
By stratifying cases into distinct zones of reliability, the SA-ROC framework                                             clinical mandates. Faced with a ‘strictly non-negligent’ policy where missing
provides a new perspective to understand the decision-making patterns of                                                  a cancer is unacceptable (Fig. 5e), the optimal strategy becomes highly
human radiologists and compare them with the AI’s safety assessment. Our                                                  conservative: to achieve the target of 100% NPV, the AI eliminates its ability
analysis revealed the most critical human-AI discordance in the Rule-out                                                  to rule out any case, deferring all but the most certain positive calls to human
Safe Zone (Fig. 4). Here, where the AI was most conﬁdent that cases were                                                  review. In stark contrast, a policy engineered to minimize the harm from
low-risk (e.g., α⁻ = 100%), human accuracy was paradoxically at its lowest.                                               false positives (Fig. 5f) compels the AI to be exceptionally cautious, achieving
This was driven by a high rate of false positives. In other words, radiologists                                           the target of 100% PPV by sacriﬁcing broad detection for absolute certainty.
frequently ﬂagged these AI-identiﬁed safe cases as suspicious, a tendency                                                 These scenarios show the SA-ROC framework functioning as a versatile
often described as diagnostic over-calling in high-stakes screening. The                                                  governance tool, enabling stakeholders to translate speciﬁc clinical, eco-
framework identiﬁes a large cohort where the AI’s reliable assessment can                                                 nomic, or ethical priorities into predictable and transparent AI policies.
help counterbalance a clinical bias towards over-investigation, potentially
reducing unnecessary recalls.                                                                                             Discussion
     Conversely, the other zones validated the framework’s logic through                                                  A fundamental question from clinicians grappling with AI is not simply
strong human-AI alignment. In the Rule-in Safe Zone, the high accuracy of                                                 “How accurate is it?” but rather, “Under which conditions, and to what
human radiologists (e.g., above 98% at α+=100%) conﬁrmed that the AI                                                      extent, can I safely trust its judgment?” Our case study comparing two FDA-
successfully identiﬁed cases with a high likelihood of disease. The Gray Zone                                             cleared mammography AI solutions helps address this question by pro-
functioned as a domain of shared uncertainty where both AI and human                                                      viding a quantitative method for assessing operational safety. The higher-
experts struggled, afﬁrming its role as the designated area requiring essential,                                          AUC model was the less robust choice for high-volume screening requiring
focused human review. This stratiﬁcation provides a practical blueprint for                                               near-perfect reliability. This insight, often overlooked by conventional
calibrating clinical trust by showing where AI can safely de-escalate care and                                            metrics, reveals a critical gap between statistical validation and clinical safety
where human expertise remains essential.                                                                                  that impedes AI adoption4,22,23. The SA-ROC framework was designed to
                                                                                                                          bridge this gap and provide a basis for actionable trust. It moves beyond
Operational safety proﬁles for policy-driven automation                                                                   simply evaluating a model’s operational safety to guiding its safe deploy-
A key contribution of the SA-ROC framework is its ability to translate                                                    ment, enabling users to deﬁne the precise conditions under which an AI can
explicit institutional rules and priorities into quantiﬁable AI behavior,                                                 be trusted to meet speciﬁc clinical demands. This may help shift the con-
enabling the AI to function as a dynamically governed component of the                                                    versation around AI from a focus on statistical superiority toward a practical
clinical workﬂow. The framework ﬁrst demonstrates this capability by                                                      dialogue on operational safety and trustworthiness.
forging policies from direct clinical constraints. While a balanced policy                                                     The SA-ROC framework augments the traditional receiver operating
serves as a baseline by meeting moderate bidirectional conﬁdence targets                                                  characteristic (ROC) curve24, reframing it from a static plot of statistical
(Fig. 5a), the framework’s ﬂexibility becomes particularly evident when                                                   performance into a dynamic, visual map of a model’s operational safety
accommodating specialized, competing demands. For instance, a policy                                                      landscape. This approach is situated within a broader ﬁeld of advanced ROC
tailored for high-precision specialist referrals (Fig. 5b) enforces a stringent                                           methodologies. For example, some methods emphasize top-ranked pre-
PPV of over 99%, which directly trades off against rule-out conﬁdence.                                                    dictions (concentrated ROC)25 or weight the clinical importance of ﬁndings
Conversely, a policy designed for high-volume screening (Fig. 5c) mandates                                                (weighted alternative free-response ROC)26. However, the primary objective
near-perfect rule-out conﬁdence (NPV ≥ 99%), thus codifying a different                                                   of SA-ROC is fundamentally different. These established methods typically
clinical priority at the expense of PPV.                                                                                  aim to reﬁne the evaluation of a model’s intrinsic properties. In contrast, the


npj Digital Medicine | (2026)9:281                                                                                                                                                                                                         5
```

---

## PDF Page 6

```text
https://doi.org/10.1038/s41746-026-02450-7                                                                                                                            Article




Fig. 5 | Operational safety proﬁles of AI Solution #1 under varying clinician-            panels, the ROC curve is color-coded to indicate the Rule-in Safe Zone (red), Rule-
deﬁned policies. a–c Policies deﬁned by explicit constraints on reliability. Each         out Safe Zone (blue), and Gray Zone (gray). The thresholds for rule-in and rule-out
panel shows how the same AI model behaves when its Safe Zones are customized to           are marked by a star and a diamond, respectively. The speciﬁed safety levels (α+ and
different clinician-deﬁned safety levels (α+ and α⁻). d–f Policies derived from utility   α⁻) are labeled, with the percentage of the cohort in each corresponding zone shown
maximization. These panels show the optimal policy and corresponding thresholds           in parentheses. The shaded rectangle in the top-left corner represents the Gray Zone
derived by maximizing a pre-deﬁned utility function. The table within each panel          Area (ΓArea). TP: true positive, TN: true negative, FP: false positive, FN: false
details this optimal policy, listing the outcome class, the number of cases for that      negative, Cg: cases deferred to the Gray Zone, pg: proportion of the cohort deferred to
outcome, the pre-deﬁned per-case utility value, the calculated total value (Cases ×       the Gray Zone.
Utility), and the ﬁnal total expected utility (the sum of all total values). Within all


SA-ROC framework’s central innovation is not to better assess a model’s                   cases30. Several statistical frameworks also have been developed, such as
inherent performance, but to link its output directly to an extrinsic,                    selective prediction, which provides rules for a model to abstain based on the
clinician-deﬁned safety policy. Instead of analyzing a ﬁxed aspect of the                 potential cost of an error11,31, while conformal prediction generates a set of
curve, our framework allows users to impose a policy-driven mandate, such                 possible outcomes with a rigorous guarantee that the set will contain the true
as “a negative ﬁnding must be at least 99% reliable”, which then actively                 answer in a pre-speciﬁed percentage of the cases (e.g., 95%)12,14,32. Building
partitions the entire ROC space. This partitioning creates three distinct                 on the principles of conformal prediction, probabilistic safety regions extend
operational zones: a Rule-in Safe Zone and a Rule-out Safe Zone, where the                such probabilistic guarantees to the input space, providing bounded error
AI can be trusted for autonomous action, and the intermediate Gray Zone,                  regions with deﬁned conﬁdence levels13. However, while these methods
which designates where human expertise remains indispensable.                             provide a robust statistical method for a model to abstain, a gap remains in
      The evaluation of medical AI is shifting from a focus on predictive                 translating their outputs into an actionable clinical policy. The SA-ROC
accuracy toward trustworthiness and the communication of uncertainty27.                   framework is designed to bridge this exact gap. To further clarify the con-
The SA-ROC framework contributes to this evolving ﬁeld by serving as an                   ceptual distinctions, Table 1 summarizes the comparative characteristics of
important translational bridge between established statistical theories of                SA-ROC, selective prediction, conformal prediction, and probabilistic safety
uncertainty and the practical demands of operational safety. Indeed, the                  regions in terms of their objectives, key parameters, and decision-level
ability for a model to say, “I don’t know” and abstain from prediction when               outputs. While selective prediction typically optimizes the risk-coverage
uncertain is a necessary capability for safe clinical deployment6. This has               trade-off 31 or minimizes global costs11 via unidirectional rejection, SA-ROC
spurred the development of new safety paradigms such as zero-error tol-                   enforces bidirectional safety constraints. It treats clinical reliability targets
erance, which aims to set new standards for reliability by having AI operate              (e.g., PPV ≥ 95%) not as variables to be traded off for efﬁciency, but as non-
only in scenarios where errors can be minimized28. This trend extends even                negotiable constraints that simultaneously deﬁne Safe Zones for both Rule-
to foundational tasks like data annotation, where systems can automatically               in and Rule-out. Similarly, while conformal prediction provides rigorous
generate reliable labels based on quantitative similarity to an internal                  statistical coverage through dynamic prediction sets33 (e.g., variable set sizes
reference atlas29. In parallel, for clinical deployment, various frameworks               per patient), SA-ROC operationalizes these signals into static triage zones.
have been developed to enable a model to abstain from prediction. For                     By converting variable outputs into deﬁnitive actions (e.g., “Automated
example, algorithmic uncertainty has been incorporated into deep learning                 Rule-out” vs. “Manual Review”), our framework enables the establishment
models to provide ‘no prediction’ options for highly uncertain clinical                   of standardized clinical protocols. This operational logic is anchored by the


npj Digital Medicine | (2026)9:281                                                                                                                                             6
```

---

## PDF Page 7

```text
https://doi.org/10.1038/s41746-026-02450-7                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Article

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          primary hyperparameter, α, which serves not as a mere statistical sig-




                                                                                                                                                                                          Error probability bound with conﬁdence (e.g., 1%
                                                                                                                                    Probabilistic certiﬁcation of a low-error region in




                                                                                                                                                                                                                                                                                                 Which types of cases can be safely predicted



                                                                                                                                                                                                                                                                                                                                                    scores, unlike PSR’s dependency on speciﬁc
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          niﬁcance level, but as the explicit threshold for these safety policies. This




                                                                                                                                                                                                                                                                                                                                                    Operates as a governance layer on output
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          reframes the problem: the Gray Zone is no longer just a region of statistical




                                                                                                                                                                                                                                             Certiﬁed subset of cases where model
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ambiguity but the direct result of an explicit safety policy. Our framework,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          therefore, does not replace these statistical methods but connects their

                                                                                                     Probabilistic Safety Regions
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          principles to clinical reality, making their abstract guarantees operationally




                                                                                                                                                                                          error with 95% conﬁdence)




                                                                                                                                                                                                                                                                                                 with guaranteed low error?
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          meaningful. This design effectively decouples the clinical safety policy from
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          the underlying statistical mechanics, establishing SA-ROC as a modular




                                                                                                                                                                                                                                             predictions are trusted




                                                                                                                                                                                                                                                                                                                                                    adjustable classiﬁers.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          governance layer capable of evolving with advanced estimators. For
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          instance, future implementations could utilize conformal risk control
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          algorithms34 to derive zone thresholds, thereby combining SA-ROC’s
                                                                                                                                    input space




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          operational utility with rigorous ﬁnite-sample guarantees for intrinsic
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          error rates.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Beyond visualization, SA-ROC quantiﬁes deferred workload via ΓArea,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          enabling workload and automation planning. This cost has signiﬁcant
                                                                                                                                                                                                                                                                                                 Which set of labels is guaranteed to contain the


                                                                                                                                                                                                                                                                                                                                                    Provides static operational zones for deﬁnitive                                                                                                                                                       implications for all stakeholders: for clinicians, it predicts the daily workload
                                                                                                                                                                                                                                                                                                                                                    action, avoiding CP’s interpretation-heavy
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          from deferred cases; for health systems, it represents the economic toll of
                                                                                                                                    Marginal coverage guarantee for a set of




                                                                                                                                                                                                                                             A set of possible labels for a given case




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          logistical bottlenecks; and for developers, it provides a concrete target for
                                                                                                                                                                                          Signiﬁcance level (e.g., 5% error rate)




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          shrinking a model’s operational uncertainty. Clinically, the magnitude of
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ΓArea serves as a direct indicator of the operational cost required to maintain
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          the desired safety level. A small ΓArea suggests that the model can autono-
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          mously handle the majority of cases with high conﬁdence, leading to a
                                                                                                     Conformal Prediction




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          streamlined workﬂow and high automation efﬁciency. Conversely, a large
                                                                                                                                                                                                                                                                                                 truth for this case?




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ΓArea indicates a signiﬁcant proportion of ambiguous cases where the model
                                                                                                                                    possible labels




                                                                                                                                                                                                                                                                                                                                                    dynamic sets.




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          cannot guarantee safety. In such scenarios, the framework signals a need for
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          increased human resource allocation, as these gray cases must be diverted to
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          expert clinicians for manual review to prevent medical errors. This cost is
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          not merely theoretical; recent empirical studies have demonstrated its
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          tangible impact on physicians. For example, AI tools lacking transparent
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          uncertainty management have been shown to increase radiologists’ burnout
                                                                                                                                                                                                                                             Binary decision for each case: Predict or Abstain




                                                                                                                                                                                                                                                                                                                                                                                                      CP conformal prediction, NPV negative predictive value, PPV positive predictive value, PSR probabilistic safety regions, SP selective prediction.
                                                                                                                                                                                          Target coverage or abstention Cost (e.g., cover




                                                                                                                                                                                                                                                                                                                                                    Enforces safety as a non-negotiable constraint




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          risk35 and paradoxically increase the time physicians spend reviewing
                                                                                                                                                                                                                                                                                                                                                    regardless of workload, avoiding SP’s safety-
               Table 1 | Comparison of SA-ROC with related uncertainty-aware prediction frameworks


                                                                                                                                    Risk–coverage optimization under a target




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          information rather than reducing it36. Strategically managing this cost is
                                                                                                                                                                                                                                                                                                 Given the risk/cost, should the AI make a




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          therefore crucial, and the framework enables this by revealing the inherent
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          trade-off between the desired safety level (α) and the size of the Gray Zone.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          The Safety Proﬁle Curve (Fig. 1e) illustrates the trade-off between α and
                                                                                                                                    coverage or abstention cost




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Gray Zone size, aiding in the selection of an elbow point that maximizes
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          reliability without disproportionately increasing workload. Models with
                                                                                                                                                                                                                                                                                                 prediction for this case?




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          small ΓArea at high α levels are better suited for safe automation in clinical
                                                                                                     Selective Prediction




                                                                                                                                                                                                                                                                                                                                                    efﬁciency trade-off.




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          workﬂows. Consequently, this single metric enables a transparent dialogue
                                                                                                                                                                                          80% of cases)




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          about the trade-offs between safety and automation efﬁciency.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                The framework extends beyond simply quantifying uncertainty to
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          actively govern an AI’s behavior, offering a path for it to evolve from a static
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          tool toward an adaptable component in clinical practice. Our framework
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          makes this governance possible by enabling the formulation of optimal
                                                                                                                                                                                                                                                                                                 Under what conditions is it safe to trust the AI
                                                                                                                                    Operational safety under a clinician-deﬁned




                                                                                                                                                                                                                                                                                                                                                    Decouples safety policy from architecture to




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          policies tailored to speciﬁc clinical contexts, achieved through either explicit
                                                                                                                                                                                                                                             Three-zone workﬂow (Rule-in, Rule-out,




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          constraints or utility maximization. This policy-driven capability is crucial
                                                                                                                                                                                          Clinical reliability target (e.g., 95% PPV,




                                                                                                                                                                                                                                                                                                                                                    enforce bidirectional constraints on any




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          because it resists the one-size-ﬁts-all fallacy that often hinders AI adoption,
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          where a single model conﬁguration is expected to perform optimally across
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          diverse clinical settings37,38. Our prevalence simulation analysis (see Sup-
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          plementary Note 1) provides a clear example, demonstrating how two high-
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          performing AI solutions respond in vastly different ways to shifts in epi-
                                                                                                     SA-ROC Framework




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          demiological context. We found that a model’s operational stability is not a
                                                                                                                                                                                                                                                                                                 for a clinical task?




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ﬁxed property but is critically linked to its intrinsic score distribution,
                                                                                                                                                                                                                                                                                                                                                    scoring model.




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          reinforcing the need for local, policy-driven validation. By enabling insti-
                                                                                                                                                                                                                                             Gray Zone)
                                                                                                                                                                                          99% NPV)




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          tutions to deploy the same validated AI model under distinct, locally-
                                                                                                                                    policy




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          optimized policies, our framework can help shift AI integration from a
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          purely technical challenge toward a transparent process of clinical govern-
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ance, where operational reality is explicitly shaped by declared values.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                Our work has several limitations that open new avenues for research.
                                                                                                                                                                                          Key hyperparameter




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          First, a primary limitation of our study pertains to its validation scope. The
                                                                                                                                                                                                                                             Output for clinical




                                                                                                                                                                                                                                                                                                                                                    Key distinction of




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          generalizability of the SA-ROC framework represents an important area for
                                                                                                                                                                                                                                                                                                 Core question
                                                                                                                                    Primary goal




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          future research. This validation is particularly important because the Safe
                                                                                                                                                                                                                                                                                                 addressed


                                                                                                                                                                                                                                                                                                                                                    SA-ROC
                                                                                                                                                                                                                                             decision




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Zones are deﬁned by prevalence-dependent metrics (PPV and NPV). We
                                                                                                     Aspect




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          performed an initial assessment of this effect using a bootstrap-based
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          simulation on our dataset to analyze operational stability under varying


npj Digital Medicine | (2026)9:281                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       7
```

---

## PDF Page 8

```text
https://doi.org/10.1038/s41746-026-02450-7                                                                                                                Article

prevalence conditions. However, this simulation does not replace the need          augmentation and feature engineering to ‘shrink’ the clinically-relevant
for real-world validation. Even with resampling, our analysis remains              uncertainty. Employing the Gray Zone as a targeted dataset enables more
constrained by the retrospective dataset of 1000 cases. At high α levels (e.g.,    sophisticated model improvement strategies, such as directly integrating its
nearing 100%), thresholds rely on the sparse tails of the prediction score         size into the loss function for minimization or optimizing the model’s policy
distribution, leading to potential instability that bootstrap intervals may not    by incorporating the utility values for each outcome as a reward signal
fully mitigate. Therefore, evaluation on large-scale, multi-center datasets is     within a reinforcement learning framework. Furthermore, for researchers,
essential for calibrating the framework and deﬁning its optimal role in real-      this cohort may highlight atypical disease presentations or rare subtypes that
world clinical workﬂows. Second, prospective validation through user stu-          represent gaps in current clinical understanding itself, thus pointing toward
dies is essential to understand clinical interaction, workﬂow impact, cog-         new avenues of medical research. In this light, the Gray Zone can be
nitive load, and potential biases such as over-reliance on the Safe Zone           reframed from a cost of indecision into a resource for innovation, creating a
designation. Third, while the user-deﬁned safety level (α) allows clinical         positive feedback loop for improving both AI models and clinical
context speciﬁcity, its variability complicates standardized model compar-         knowledge.
isons and regulatory agreement, highlighting the need for establishing
benchmark α values via expert consensus. Fourth, the current ΓArea metric          Methods
captures total operational uncertainty, encompassing both data and model           The Safety-Aware ROC framework
sources. Future work could aim to disentangle these factors through con-           The SA-ROC framework is a visual-analytic tool designed to augment the
trolled comparative analyses to determine whether the operational burden           traditional ROC curve with operational safety information. It provides a
stems primarily from input data complexity or model limitations. Finally,          structured approach to move beyond evaluating a model’s statistical per-
while our study focuses on binary classiﬁcation, future research will adapt        formance by visualizing its operational safety in a clinical context. We
the SA-ROC framework to complex tasks such as multi-class problems and             conceptualize this as a complete end-to-end operational framework (Fig. 6),
large language model assessments. Such efforts could contribute to the             which consists of three key stages. First, a retrospective safety proﬁling stage
development of robust operational safety standards for a wider range of            uses local data to analyze a model and generate a calibrated safety map,
clinical AI. A long-term goal of this research is to contribute to the devel-      which represents the comprehensive set of Zone area information corre-
opment of widely adopted standards for translating statistical performance         sponding to α+ and α⁻ across all possible risk scores and thresholds (Fig. 6a).
into demonstrable operational safety for clinical AI applications.                 Second, a policy governance stage allows clinical decision-makers to use this
      Looking ahead, SA-ROC is designed to do both: automate what is safe          map to deﬁne a formal, binding operational policy (Fig. 6b). Third, a pro-
and learn from what is uncertain. This dual capability allows it to advance        spective workﬂow integration stage implements this policy to triage new
clinical practice while also facilitating AI model reﬁnement and scientiﬁc         cases, contrasting with conventional workﬂows to streamline human-AI
discovery. The impact of our framework could be realized through its               interaction and mitigate cognitive load (Fig. 6c). The framework achieves
potential to reshape clinical workﬂows. By identifying a large volume of           this by systematically partitioning the model’s range of prediction scores
normal cases, the framework enables signiﬁcant changes to clinical practice        into distinct zones based on clinician-deﬁned reliability criteria. This pro-
and the nature of the human-AI partnership. For instance, in high-resource         cess also enables the active design of AI decision policies tailored to speciﬁc
settings, it enables a safe, partial automation workﬂow: the AI autonomously       clinical needs.
handles the vast majority of cases in the Safe Zones, allowing specialists to
focus their expertise only on complex cases deferred to the Gray Zone,             Deﬁning the Safe Zones and the Gray Zone
thereby enhancing throughput and mitigating burnout. This impact could             The framework’s safety assessment is built upon two clinically intuitive
be signiﬁcant in low- and middle-income countries, where a validated safe          metrics: PPV, the probability that a positive prediction is correct, and NPV,
AI can empower trained healthcare workers to manage most negative cases,           the probability that a negative prediction is correct. To translate these
democratizing access to high-quality diagnostics39–41. Explicitly deﬁned Safe      metrics into a formal policy, the framework uses clinician-deﬁned safety
Zones also have the potential to reshape the human-AI interface by ﬁltering        levels. The framework deﬁnes two distinct safety targets. The rule-in safety
out low-risk safe cases, potentially mitigating alert fatigue42 and potentially    level (α+) is the minimum acceptable PPV required for a positive prediction.
reducing clinical decision fatigue43. However, this new dynamic introduces         The rule-out safety level (α⁻) is the minimum acceptable NPV for a negative
important challenges, such as automation bias44 and legal liability45 if rare      prediction.
errors occur. To mitigate this speciﬁc risk of over-reliance within ‘Safe                A clinical safety policy is established by setting speciﬁc values for these
Zones’, actual clinical deployment must prioritize human-AI interaction            levels (e.g., α+ ≥ 95% and α⁻ ≥ 99%). Based on these clinician-deﬁned targets,
designs that go beyond passive display. Speciﬁcally, interfaces can incor-         the framework partitions the model’s predictions into three opera-
porate cognitive forcing functions46 such as ‘on-demand’ access where the          tional zones:
safety status remains hidden until explicitly requested, ‘update’ protocols          • The Rule-in Safe Zone (Z þ      Safe ) consists of high-risk scores where the
requiring clinicians to input a provisional diagnosis before viewing the AI              model’s PPV meets or exceeds the speciﬁed α+ target, indicating these
output, or ‘wait’ mechanisms that introduce a mandatory delay. These                     cases are reliable enough for autonomous escalation or clinical action
interventions are designed to disrupt heuristic reliance and compel analy-               under the deﬁned safety policy.
tical thinking before the AI’s safety status is accepted. Conversely, labeling a     • The Rule-out Safe Zone (Z       Safe ) consists of low-risk scores where the
case as part of the Gray Zone may heighten clinician vigilance but could                 model’s NPV meets or exceeds the speciﬁed α⁻ target, permitting
introduce cognitive burdens if not thoughtfully implemented47,48, empha-                 automated deprioritization under the deﬁned safety policy.
sizing that successful integration of safe AI is ultimately a human-centered         • The Gray Zone (Z Gray ) is the intermediate range of scores where the
design challenge where interface and workﬂow are as critical as the algo-                model’s reliability fails to meet either the rule-out (α⁻) or rule-in (α+)
rithm itself. Therefore, future prospective studies are essential to understand          safety level. These predictions are considered uncertain and require
these deeper cognitive and psychological impacts.                                        essential human expert review.
      In parallel, our framework reframes the Gray Zone from a model
failure into a resource for model improvement and scientiﬁc discovery. By                The formal deﬁnitions of the Safe Zones are established using the
deﬁnition, the cases that consistently fall into this zone are the most            following notation. Let S be the complete set of samples in a dataset. For each
ambiguous and diagnostically challenging, representing the limits of the           sample i ∈ S, the binary classiﬁcation model assigns a continuous risk score
current model’s knowledge. Systematic analysis of this cohort offers a             si ∈ [0, 1], representing the model’s predicted probability. Each sample has a
powerful opportunity for a continuous learning loop49,50. For developers, it       corresponding true class label yi, where yi ∈ {C1, C0} for the positive and
pinpoints a model’s speciﬁc weaknesses, enabling targeted data                     negative classes, respectively. The zones are deﬁned by identifying the set of


npj Digital Medicine | (2026)9:281                                                                                                                                8
```

---

## PDF Page 9

```text
https://doi.org/10.1038/s41746-026-02450-7                                                                                                                                                              Article

        a Retrospective Safety Profiling                                                    b Policy Governance

        Local Patient Cohort                                                                                              Goal-Driven Method



          AI Score Logs                 SA-ROC Analysis        Calibrated Safety Map        Clinical AI Council                                          Define Safety Policy      Operational Policy



        Reference Standard                                                                                                Utility-Driven Method

                                                                                                                                          Policy Implementation



        c Prospective Workflow Integration
                                                                                                                           Rule-in Safe Zone                                       Targeted Attention


                                                                        SA-ROC Guided
                                                                             Workflow        SA-ROC Triage                     Gray Zone                Clinician with SA-ROC     Streamlined Workflow




                                                                                                                          Rule-out Safe Zone                                     Reduced Cognitive Load

         New Patient Case                 Patient Data
                                                                   AI Inference

                                                                                                                                                                                 High Vigilance Demand
                                                                                                                  Conventional Workflow

                                                                                                                                                      Clinician without SA-ROC        Alert Fatigue




                                                                                                                                                                                  Cognitive Exhaustion


Fig. 6 | The SA-ROC end-to-end operational framework: from retrospective                                 map from local data, which allows clinical decision-makers to deﬁne an operational
calibration to prospective workﬂow integration. This diagram illustrates the three                       policy. This policy is then implemented to augment each new AI inference, enabling
stages of the framework: a Retrospective safety proﬁling. b Policy governance.                           a safer, more targeted human-AI interaction and reducing cognitive load compared
c Prospective workﬂow integration. The framework ﬁrst generates a calibrated safety                      to conventional workﬂows.



scores, s, that satisfy the safety criteria by searching over all possible decision                      Quantifying the non-automated workload with the Gray Zone
thresholds, τ′. Speciﬁcally, we performed an empirical linear scan over all                              To provide a single, quantitative measure of a model’s operational uncer-
unique, sorted prediction scores in the dataset to identify the precise                                  tainty, we introduce the Gray Zone Area (ΓArea). This index directly mea-
boundaries without discretization gaps. This search aims to ﬁnd the                                      sures the size of the Gray Zone in the ROC space, representing the clinical
boundaries that satisfy the clinician-deﬁned rule-in safety level (α+) and                               workload or ‘cost of indecision’ that the AI model imposes. Alongside this,
rule-out safety level (α⁻). The search for these boundaries utilizes the inﬁ-                            the percentage of the total cohort that falls into the Gray Zone serves as
mum (inf) and supremum (sup) operators to ﬁnd the greatest lower bound                                   another intuitive metric to directly quantify the non-automated workload. A
and least upper bound of the set of qualifying thresholds. By utilizing these                            model with a smaller ΓArea is more operationally efﬁcient because it safely
operators, the framework enforces a monotonicity constraint, ensuring that                               automates a larger portion of the workload while meeting the speciﬁed
the resulting Safe Zones are deﬁned as contiguous intervals bounded by a                                 safety criteria. The framework also utilizes a Safety Proﬁle Curve, which
single threshold. Logical conditions are evaluated using the indicator                                   plots both the percentage of the cohort in the Gray Zone and the ΓArea
function, I(⋅), which returns 1 if a condition is true and 0 otherwise.                                  against a range of safety levels (α). This curve visualizes the trade-off between
     Based on this notation, the Safe Zones are formally deﬁned as:                                      safety and workload, allowing stakeholders to select an optimal operational
     Rule-in Safe Zone (Z þ    Safe ): The set of scores s where the PPV is at least                     policy.
the rule-in safety level, α+.                                                                                 The Gray Zone Area (ΓArea) quantiﬁes the size of the uncertain region
                                                                                                         in the ROC space (Fig. 7). Let τ þSafe be the inﬁmum (lowest score) of the Rule-
              (                 (        P                                      ))
                                                     si ≥ τ 0 and yi ¼ C 1                               in Safe Zone and τ Safe be the supremum (highest score) of the Rule-out Safe
                                             i2S I
    Zþ
     Safe ¼       s j s ≥ inf τ j   0
                                                     P             0
                                                                            ≥α þ
                                                                                               ð1Þ       Zone. The ΓArea is the area of the rectangle in ROC space deﬁned by the false
                                                       i2S I si ≥ τ                                      positive rate (FPR) at the rule-out boundary (τ   Safe ) and the true positive rate
                                                                                                         (TPR) at the rule-in boundary (τ þ    Safe ):
     Rule-out Safe Zone (Z    Safe ): The set of scores s where the NPV is at least
                                                                                                                                                             þ 
the rule-out safety level, α⁻.                                                                                                     ΓArea ¼ FPR τ 
                                                                                                                                                 Safe × 1  TPR τ Safe                                      ð4Þ
              (                 (         P                                          ))
                                              i2S I    s < τ 0 and yi ¼ C0
    Z
     Safe ¼       s j s < sup τ 0 j                   Pi                 ≥ α                ð2Þ
                                                         i2S I si < τ
                                                                      0

                                                                                                         Visualization of the safety landscape on the ROC curve
                                                                                                         The core of our method is the visualization of this safety landscape on the
     Gray Zone (Z Gray ): The set of scores s not included in either Safe Zone.                          ROC curve. The SA-ROC curve is constructed by color-coding the segments
                                                                                                         of the standard ROC curve based on the zone to which their corresponding
                                               = Zþ
                               Z Gray ¼ fs j s 2           
                                                  Safe ∪ Z Safe g                              ð3Þ       threshold (τ), the cutoff applied to the model’s continuous risk scores to



npj Digital Medicine | (2026)9:281                                                                                                                                                                            9
```

---

## PDF Page 10

```text
https://doi.org/10.1038/s41746-026-02450-7                                                                                                                                                          Article

                                              Zone Partitioning in Score Space                                                 Safety-Aware ROC Curve
                                                                                                                                                                  − )
                                                                                                                                                            FPR( τSafe
                                      τ−
                                       Safe                  θ                        τ+
                                                                                       Safe                                0                                                     −
                                                                                                                                                                             Z Safe
                                                                                                                                     FPR( τ−
                                                                                                                                           Safe )
                                                                                                                      1                                                      1


                   Positive
                                                                                                                                 θ                                           0.8

                                                                                                                    + )
                                                                                                          1 - TPR( τSafe                Z Gray
                                  −                                                      +                                                                                   0.6




                                                                                                                                                                                      Sensitivity
                              Z Safe                             Z Gray                Z Safe


                                                                                                               + )                                                           0.4
                                                                                                         TPR( τSafe
                  Negative
                                                                                                                                              − ) × (1 - TPR( τ+ ))
                                                                                                                                ΓArea = FPR( τSafe             Safe          0.2



                                                                                                                                                                             0
                                                                                                                      +
                              0               0.2      0.4                0.6   0.8           1                   Z Safe 0     0.2         0.4      0.6      0.8         1
                                                     Predicted Risk Score                                                                 1 - Specificity

Fig. 7 | Illustrative computation of ΓArea mapping from score space to ROC space.                 mapping of these thresholds to the ROC space, where the rule-out threshold (τ        Safe )
The scatter plot visualizes the distribution of predicted risk scores for positive (pink          deﬁnes the boundary for the false positive rate (FPR(τ þSafe )) and the rule-in threshold
circles) and negative (green circles) cases, where the score range is partitioned into            (τ þ                                                              þ
                                                                                                     Safe ) deﬁnes the boundary for the true positive rate (TPR(τ Safe )). The Gray Zone
three operational zones—Rule-out Safe (Z                                               þ
                                            Safe ), Gray ðZ Gray ), and Rule-in Safe (Z Safe )    Area (ΓArea) is computed as the geometric area of the shaded rectangle formed by
                                                  þ
—deﬁned by the safety thresholds (τ Safe and τ Safe ). Arrows illustrate the direct               these coordinates in ROC space. The standard optimal threshold is denoted by θ.



make binary predictions, belongs. Segments where the threshold τ falls                            settings for each parameter is provided in Fig. 8b. Examples of how different
within the Safe Zones (Z þ            
                            Safe or Z Safe ) are colored to indicate safety, with                 clinical scenarios (e.g., high-volume screening or pure cohort extraction for
different colors potentially representing different safety levels (e.g., α = 90%,                 research, etc.) translate into speciﬁc policy constraints are provided in
95%, 100%). For these visualizations, we employ a standard SA-ROC                                 Supplementary Table 1.
conﬁguration. In this setting, we use a symmetric safety parameter α                                    The second utility-driven paradigm, policy derivation via utility
(implying α+ = α⁻) to standardize the evaluation of operational uncertainty                       maximization (Fig. 9), reframes policy design as an optimization problem
across uniform tiers, whereas the framework fundamentally treats these                            that balances the beneﬁts of correct decisions against the costs of errors and
parameters as operationally independent values to be tuned according to                           indecision. The process operates by assigning a speciﬁc clinical or economic
speciﬁc clinical needs. Segments where the threshold τ falls within the Gray                      value, or utility, to each of the ﬁve possible outcomes for a case: a true
Zone (Z Gray ) are colored with a neutral color (e.g., gray) to visually represent                positive (TP, Utility UTP), true negative (TN, Utility UTN), false positive (FP,
uncertainty. This visualization provides an intuitive and immediate                               Utility UFP), false negative (FN, Utility UFN), and deferral to the Gray Zone
understanding of a model’s operational characteristics, showing not only                          (Utility, UGray). Users can assign positive utility to correct decisions and
how well it discriminates but also where on its decision spectrum it is safe                      negative utility (penalties) to errors, such as a high penalty for a missed
to use.                                                                                           cancer (a false negative). Examples of how these utility values can be
      To explicitly quantify the operational cost of safety, the framework                        assigned to reﬂect different clinical policy goals (e.g., Minimize FN vs.
further generates the Safety Proﬁle Curve. This curve plots the magnitude of                      Minimize FP Impact, etc.) are provided in Supplementary Table 2. The
the Gray Zone as a function of the target safety level, thereby visualizing the                   framework then systematically identiﬁes the policy that maximizes the total
trade-off between reliability stringency and clinician workload. This curve is                    expected utility across all cases. For a policy deﬁned by a pair of score
also generated using the standard SA-ROC conﬁguration (α+ = α⁻), pro-                             thresholds, the total expected utility (UTotal) is the weighted sum of the
viding a streamlined view of how the operational cost scales with a uniﬁed                        outcomes:
safety target.
                                                                                                     U Total ¼ nTP U TP þ nTN U TN þ nFP U FP þ nFN U FN þ nGray U Gray                                 ð5Þ
Deriving operational policies from clinical goals
A key capability of the SA-ROC framework is its ability to actively shape an                      where n is the number of cases in each respective category. The framework
AI’s operational policy rather than just passively evaluate it. This is achieved                  performs a systematic search across all valid threshold pairs to ﬁnd the
through two primary paradigms for translating clinical priorities into a                          policy that maximizes this function.
formal policy.
      The ﬁrst goal-driven paradigm, policy deﬁnition via direct constraints                      Simulation studies
(Fig. 8), allows users to derive a policy from the interplay between three key                    We conducted simulation studies to demonstrate how the SA-ROC frame-
parameters: rule-in reliability (governed by α+), rule-out reliability (gov-                      work reveals operational differences obscured by traditional metrics (Fig. 2).
erned by α⁻), and the clinical workload (represented by the proportion of the                     We generated synthetic datasets to simulate the continuous risk scores
cohort deferred to the Gray Zone, pg). By deﬁning any two of these as explicit                    (ranging from 0 to 1) produced by clinical AI models. Each dataset was
constraints, the framework automatically optimizes for the third (Fig. 8a).                       created by drawing 5,000 samples for the negative class (C0) and 5,000 for the
For instance, a user might prioritize high safety standards for both ruling in                    positive class (C1) from pairs of Beta distributions51. Speciﬁcally, we employed
and ruling out cases by setting targets for α+ and α⁻. The framework then                         ﬁxed distribution parameters selected to generate a wide variety of score
calculates the resulting Gray Zone size, which represents the workload                            distribution shapes. This approach allowed us to observe distinct operational
required to meet those dual-safety goals. Alternatively, a user could set a                       behaviors of the Safe and Gray Zone, ranging from wide uncertain regions to
primary safety target (e.g., a high α⁻ for ruling out cases) and a maximum                        narrow effective automation zones, under controlled theoretical conditions.
acceptable workload, allowing the framework to determine the best possible                        From these generated models, we selected four representative scenarios to
rule-in reliability (α+) achievable under those constraints. A conceptual                         highlight key principles. These scenarios included models with modest overall
guide to the strategic trade-offs involved in calibrating the ‘low’ versus ‘high’                 performance but skewed distributions that produced either a strong Rule-in


npj Digital Medicine | (2026)9:281                                                                                                                                                                      10
```

---

## PDF Page 11

```text
https://doi.org/10.1038/s41746-026-02450-7                                                                                                                             Article




Fig. 8 | Framework for deriving operational policies. a Three governance pathways             the proportion of cases deferred to the Gray Zone, pg). b Conceptual illustration of
for policy formulation. Each policy is determined by constraining any two of the              the strategic trade-offs encountered when adjusting the parameters between ‘low’
three parameters: rule-in safety level (α+), rule-out safety level (α⁻), or workload (i.e.,   and ‘high’ settings. FP: false positive, FN: false negative.


Safe Zone or a strong Rule-out Safe Zone. Additionally, we created two                        Solution #1 and AI Solution #2. While speciﬁc architectural details are pro-
scenarios with nearly identical high AUCs of 0.960 but contrasting dis-                       prietary, both solutions are FDA-cleared deep learning algorithms based on
tribution overlaps, resulting in one model with a wide Gray Zone (indicating                  CNN architectures, trained on large clinical datasets to analyze mammo-
high uncertainty) and another with a narrow Gray Zone (indicating higher                      graphy images. Both AI solutions take a mammogram as input and output a
potential for safe automation). These curated scenarios were designed to                      continuous risk score ranging from 0 to 1, representing the likelihood of breast
clearly show how a model’s underlying score distribution, not just its                        cancer. Their inclusion serves to demonstrate the SA-ROC framework’s utility
aggregate AUC, dictates its practical operational safety proﬁle.                              as a model-agnostic tool for evaluating diverse, clinically adopted AI solutions,
                                                                                              operating irrespective of their internal implementation differences. This study
Retrospective validation using FDA-cleared AI solutions                                       was conducted under the approval of the Massachusetts General Hospital
To validate our framework’s utility on a real-world application, we performed                 Institutional Review Board (IRB No. 2023P003130), with a waiver for patient
a retrospective analysis of two anonymized, commercially available, FDA-                      informed consent. The dataset comprised 1000 screening mammograms with
cleared AI solutions for breast cancer detection. These were referred to as AI                a 40% disease prevalence (400 malignant and 600 benign cases), where the


npj Digital Medicine | (2026)9:281                                                                                                                                             11
```

---

## PDF Page 12

```text
https://doi.org/10.1038/s41746-026-02450-7                                                                                                                                                                    Article

       Case Stratification by All Feasible Policies                    Applying the Customized Utility Function                                       Identifying the Optimal Policy
                                                                                                                                                         on the Utility Landscape
                                                                                           +100

                          All Feasible Policies                                      True Positive
                                                                                                                                                25k              Maximum Utility Point
                                                                                           -100                                                 20k
                                                                                                                                                 15k
                                                      Rule-in Safe Zone             False Positive                                               10k
                                                                                                                                                   5k
                                                                                                                                          Total     0
                                                                                           -10                                                                                                     Optimal Policy
                                                                                                                                          Utility -5k
         Patient Cohort     SA-ROC Triage                 Gray Zone               Gray Zone Deferral                                              -10k
                                                                                                                    Calculation of                -15k                                      0.50
                                                                                                                 Total Expected Utility              0.75                                0.60
                                                                                           +20                                                          0.80
                                                                                                                                                                                     0.70
                                                                                                                                                          0.85
                                                      Rule-out Safe Zone            True Negative                                             Rule-out                            0.80    Rule-in
                                                                                                                                                               0.90
                                                                                                                                           Safety Level                       0.90
                                                                                                                                                                                          Safety Level
                                                                                                                                                   (α⁻)            0.95                   (α⁺)
                                                                                           -200

                                                                                    False Negative


Fig. 9 | Conceptual diagram of the utility maximization process for optimal                            true negative, or false negative. The customized utility function, using the values pre-
policy identiﬁcation. The SA-ROC triage mechanism evaluates all feasible policies,                     deﬁned by the decision-maker, assigns speciﬁc scores to each of these outcomes. The
each deﬁned by a pair of safety levels (α+ and α⁻). For each policy under con-                         calculation of total expected utility then sums these utility scores across all patients in
sideration, patients are stratiﬁed into the Rule-in Safe Zone, Gray Zone, or Rule-out                  the cohort for that speciﬁc policy. Finally, the framework searches across all feasible
Safe Zone. Comparing these zone assignments with the reference standard yields ﬁve                     policies (the entire landscape of α+ and α⁻ combinations) to identify the optimal
potential outcomes for each patient: true positive, false positive, Gray Zone deferral,                policy corresponding to the maximum utility point on the utility landscape.



reference standard for malignancy was established by biopsy and for benign                             3.    van de Sande, D. et al. To warrant clinical adoption AI models require a
cases by long-term radiological follow-up. In parallel, the initial diagnostic                               multi-faceted implementation evaluation. NPJ Digit. Med. 7, 58 (2024).
assessment by the original reading radiologist for each case was also collected                        4.    Cabitza, F., Campagner, A. & Balsano, C. Bridging the “last mile” gap
to serve as a human performance benchmark, with outcomes (true positive,                                     between AI implementation and operation: “data awareness” that
true negative, false positive, and false negative) determined against the same                               matters. Ann. Transl. Med. 8, 501 (2020).
deﬁnitive reference standard. We applied the SA-ROC framework to the risk                              5.    Seneviratne, M. G., Shah, N. H. & Chu, L. Bridging the implementation
scores from both AI solutions, and to ensure statistical robustness, 95%                                     gap of machine learning in healthcare. BMJ Innov 6, 45–47 (2020).
conﬁdence intervals for all key metrics, including AUC and the ΓArea values                            6.    Kompa, B., Snoek, J. & Beam, A. L. Second opinion needed:
derived at ﬁxed safety levels (e.g., 90%, 95%, 100%), were estimated via a                                   communicating uncertainty in medical machine learning. NPJ Digit.
nonparametric percentile bootstrap procedure. Speciﬁcally, 2000 bootstrap                                    Med. 4, 4 (2021).
samples were generated by resampling with replacement from the dataset. For                            7.    Chua, M. et al. Tackling prediction uncertainty in machine learning for
each bootstrap sample, the metrics were recalculated, and the 2.5th and 97.5th                               healthcare. Nat. Biomed. Eng. 7, 711–718 (2023).
percentiles of the empirical distribution of each metric were taken as the                             8.    McMahon, G. T. The risks and challenges of artiﬁcial intelligence in
bounds of the 95% conﬁdence interval. Furthermore, to analyze operational                                    endocrinology. J. Clin. Endocrinol. Metab. 109, e1468–e1471 (2024).
stability under varying prevalence conditions (1%–40%), we conducted a                                 9.    Topol, E. J. High-performance medicine: the convergence of human
separate simulation analysis (see Supplementary Note 1). Based on the                                        and artiﬁcial intelligence. Nat. Med. 25, 44–56 (2019).
assumption of ﬁxed class-conditional score distributions, we generated syn-                            10.   Vickers, A. J. & Elkin, E. B. Decision curve analysis: a novel method for
thetic cohorts to empirically derive bootstrap-based conﬁdence intervals.                                    evaluating prediction models. Med. Decis. Making 26, 565–574
Speciﬁcally, to maximize the effective sample size of the reference distribution,                            (2006).
we held the complete negative cohort constant (N = 600) as a stable baseline                           11.   Swaminathan, A. et al. Selective prediction for extracting unstructured
and generated synthetic cohorts by resampling positive cases with replace-                                   clinical data. J. Am. Med. Inform. Assoc. 31, 188–197 (2024).
ment to match the target disease prevalence.                                                           12.   Luo, R. et al. Sample-efﬁcient safety assurances using conformal
                                                                                                             prediction. Int. J. Robot. Res. 43, 1409–1424 (2024).
Data availability                                                                                      13.   Carlevaro, A., Alamo, T., Dabbene, F. & Mongelli, M. Probabilistic
The data that support the ﬁndings of this study are available from the                                       safety regions via ﬁnite families of adjustable classiﬁers. IEEE Trans.
corresponding author upon reasonable request. Access to the data is subject                                  Neural Netw. Learn. Syst. 36, 16198–16212 (2025).
to institutional regulations and data use agreements due to the inclusion of                           14.   Narteni, S., Carlevaro, A., Dabbene, F., Muselli, M. & Mongelli, M. A
clinical information. Requests will be evaluated to ensure compliance with                                   novel score function for conformal prediction in rule-based binary
privacy and ethical standards, and qualiﬁed researchers may obtain access                                    classiﬁcation. Pattern Recognit. 112219 (2025).
for non-commercial academic use.                                                                       15.   Sreenivasan, A. P. et al. Conformal prediction enables disease course
                                                                                                             prediction and allows individualized diagnostic uncertainty in multiple
Code availability                                                                                            sclerosis. NPJ Digit. Med. 8, 224 (2025).
The code used to implement the SA-ROC framework is available at https://                               16.   Dalal, S., Ardabili, A. K. & Bonavia, A. S. Time-series deep learning and
github.com/MGH-LMIC/SA-ROC. The code is written in Python 3.9.                                               conformal prediction for improved sepsis diagnosis in primarily non-
                                                                                                             ICU hospitalized patients. Comput. Biol. Med. 193, 110497 (2025).
Received: 29 August 2025; Accepted: 8 February 2026;                                                   17.   Fayyad, J., Alijani, S. & Najjaran, H. Empirical validation of conformal
                                                                                                             prediction for trustworthy skin lesions classiﬁcation. Comput.
                                                                                                             Methods Programs Biomed. 253, 108231 (2024).
References                                                                                             18.   Sadinle, M., Lei, J. & Wasserman, L. Least ambiguous set-valued
1.   Sharma, M. et al. Artiﬁcial intelligence applications in health care                                    classiﬁers with bounded error levels. J. Am. Stat. Assoc. 114, 223–234
     practice: scoping review. J. Med. Internet Res. 24, e40238 (2022).                                      (2019).
2.   Marwaha, J. S. & Kvedar, J. C. Crossing the chasm from model                                      19.   Deng, J. et al. So you’ve got a high AUC, now what? An overview of
     performance to clinical impact: the need to improve implementation                                      important considerations when bringing machine-learning models
     and evaluation of AI. NPJ Digit. Med. 5, 25 (2022).                                                     from computer to bedside. Med. Decis. Making 45, 640–653 (2025).


npj Digital Medicine | (2026)9:281                                                                                                                                                                                  12
```

---

## PDF Page 13

```text
https://doi.org/10.1038/s41746-026-02450-7                                                                                                               Article

20. Kelly, C. J., Karthikesalingam, A., Suleyman, M., Corrado, G. & King,               environments because of sensory overload: algorithm development
    D. Key challenges for delivering clinical impact with artiﬁcial                     and validation. J. Med. Internet Res. 21, e15406 (2019).
    intelligence. BMC Med 17, 195 (2019).                                         43.   Grignoli, N. et al. Clinical decision fatigue: a systematic and scoping
21. Alam, L. & Mueller, S. Examining the effect of explanation on                       review with meta-synthesis. Fam. Med. Community Health 13,
    satisfaction and trust in AI diagnostic systems. BMC Med. Inform.                   e003033 (2025).
    Decis. Mak. 21, 178 (2021).                                                   44.   Abdelwanis, M., Alarafati, H. K., Tammam, M. M. S. & Simsekler, M. C.
22. Afroogh, S., Akbari, A., Malone, E., Kargar, M. & Alambeigi, H. Trust in            E. Exploring the risks of automation bias in healthcare artiﬁcial
    AI: progress, challenges, and future directions. Humanit. Soc. Sci.                 intelligence applications: A Bowtie analysis. J. Saf. Sci. Resil. 5,
    Commun. 11, 1568 (2024).                                                            460–469 (2024).
23. Hassan, M., Kushniruk, A. & Borycki, E. Barriers to and facilitators of       45.   Cestonaro, C., Delicati, A., Marcante, B., Caenazzo, L. & Tozzo, P. Deﬁning
    artiﬁcial intelligence adoption in health care: scoping review. JMIR                medical liability when artiﬁcial intelligence is applied on diagnostic
    Hum. Factors 11, e48633 (2024).                                                     algorithms: a systematic review. Front. Med. 10, 1305756 (2023).
24. Hanley, J. A. & McNeil, B. J. The meaning and use of the area under a         46.   Buçinca, Z., Malaya, M. B. & Gajos, K. Z. To trust or to think: cognitive
    receiver operating characteristic (ROC) curve. Radiology 143, 29–36 (1982).         forcing functions can reduce overreliance on AI in AI-assisted
25. Swamidass, S. J., Azencott, C.-A., Daily, K. & Baldi, P. A CROC                     decision-making. Proc. ACM Hum. Comput. Interact. 5, 1–21 (2021).
    stronger than ROC: measuring, visualizing and optimizing early                47.   Han, P. K. et al. How physicians manage medical uncertainty: a
    retrieval. Bioinformatics 26, 1348–1356 (2010).                                     qualitative study and conceptual taxonomy. Med. Decis. Making 41,
26. Chakraborty, D. P. & Winter, L. Free-response methodology: alternate                275–291 (2021).
    analysis and a new observer-performance experiment. Radiology                 48.   Mohammadi, F. G. & Sebro, R. Artiﬁcial intelligence impact on burnout
    174, 873–881 (1990).                                                                in radiologists—alleviation or exacerbation?. JAMA Netw. Open 7,
27. Begoli, E., Bhattacharya, T. & Kusnezov, D. The need for uncertainty                e2448720 (2024).
    quantiﬁcation in machine-assisted medical decision making. Nat.               49.   Feng, J. et al. Clinical artiﬁcial intelligence quality improvement:
    Mach. Intell. 1, 20–23 (2019).                                                      towards continual monitoring and updating of AI algorithms in
28. Do, S. Explainable & safe artiﬁcial intelligence in radiology. J. Korean            healthcare. NPJ Digit. Med. 5, 66 (2022).
    Soc. Radiol. 85, 834–847 (2024).                                              50.   Bruno, P., Quarta, A. & Calimeri, F. Continual learning in medicine: a
29. Kim, D. et al. Accurate auto-labeling of chest X-ray images based on                systematic literature review. Neural Process. Lett. 57, 2 (2025).
    quantitative similarity to an explainable AI model. Nat. Commun. 13,          51.   Gupta, A. K. & Nadarajah, S. Handbook of Beta Distribution and Its
    1867 (2022).                                                                        Applications (CRC press, Boca Raton, FL USA, 2004).
30. Yoon, B. C. et al. Incorporating algorithmic uncertainty into a clinical
    machine deep learning algorithm for urgent head CTs. PLoS One 18,             Acknowledgements
    e0281900 (2023).                                                              This study received no funding.
31. Geifman, Y. & El-Yaniv, R. SelectiveNet: A deep neural network with an
    integrated reject option. Proc. Mach. Learn. Res. 97, 2151–2159 (2019).       Author contributions
32. Shafer, G. & Vovk, V. A tutorial on conformal prediction. J. Mach.            Y.-T.K. led the development of the SA-ROC framework, including its con-
    Learn. Res. 9, 371–421 (2008).                                                ceptualization, methodology, implementation, formal analysis, and drafting
33. Angelopoulos, A. N. & Bates, S. Conformal prediction: a gentle                of the original manuscript. H.K. participated in the methodology and formal
    introduction. Found. Trends Mach. Learn. 16, 494–591 (2023).                  analysis, and contributed to the review and revision of the manuscript. M.B.
34. Angelopoulos, A. N., Bates, S., Fisch, A., Lei, L. & Schuster, T.             collected and organized clinical data, and contributed to the review and
    Conformal risk control. Proc. Int. Conf. Learn. Represent.                    revision of the manuscript. M.H.L., R.G.G., and M.S.G. provided critical
    55198–55218, (2024).                                                          feedback and revised the manuscript. S.D. conceived and designed the
35. Liu, H. et al. Artiﬁcial intelligence and radiologist burnout. JAMA Netw.     study, contributed to the conceptualization, methodology, implementation,
    Open 7, e2448714 (2024).                                                      formal analysis, and resources, supervised the study, and critically reviewed
36. Tai-Seale, M. et al. AI-generated draft replies integrated into health        and revised the manuscript.
    records and physicians’ electronic communication. JAMA Netw.
    Open 7, e246565 (2024).                                                       Competing interests
37. Ong Ly, C. et al. Shortcut learning in medical AI hinders generalization:     M.B. reports serving as an expert panelist for 2nd.MD, as a consultant to
    method for estimating AI model generalization without external data.          Hologic, Inc. and Lunit, Inc., and institutional research grant support from
    NPJ Digit. Med. 7, 124 (2024).                                                both companies. M.H.L. reports serving as a consultant to GE Medical
38. Eche, T., Schwartz, L. H., Mokrane, F.-Z. & Dercle, L. Toward                 Systems and Seagen Pharm. S.D. reports institutional research grant
    generalizability in the deployment of artiﬁcial intelligence in radiology:    support from HEM Pharma and institutional research credits from Amazon
    role of computation stress testing to overcome underspeciﬁcation.             Web Services (AWS). All other authors declare no competing interests.
    Radiol. Artif. Intell. 3, e210097 (2021).
39. Ciecierski-Holmes, T., Singh, R., Axt, M., Brenner, S. & Barteit, S.          Additional information
    Artiﬁcial intelligence for strengthening healthcare systems in low- and       Supplementary information The online version contains
    middle-income countries: a systematic scoping review. NPJ Digit.              supplementary material available at
    Med. 5, 162 (2022).                                                           https://doi.org/10.1038/s41746-026-02450-7.
40. Alami, H. et al. Artiﬁcial intelligence in health care: laying the
    foundation for responsible, sustainable, and inclusive innovation in          Correspondence and requests for materials should be addressed to
    low- and middle-income countries. Global. Health 16, 52 (2020).               Synho Do.
41. Oduoye, M. O. et al. Impacts of the advancement in artiﬁcial
    intelligence on laboratory medicine in low- and middle-income                 Reprints and permissions information is available at
    countries: challenges and recommendations—a literature review.                http://www.nature.com/reprints
    Health Sci. Rep. 7, e1794 (2024).
42. Fernandes, C. O., Miles, S., Lucena, C. J. P. D. & Cowan, D. Artiﬁcial        Publisher’s note Springer Nature remains neutral with regard to
    intelligence technologies for coping with alarm fatigue in hospital           jurisdictional claims in published maps and institutional afﬁliations.


npj Digital Medicine | (2026)9:281                                                                                                                              13
```

---

## PDF Page 14

```text
https://doi.org/10.1038/s41746-026-02450-7                                       Article

Open Access This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format, as long
as you give appropriate credit to the original author(s) and the source,
provide a link to the Creative Commons licence, and indicate if changes
were made. The images or other third party material in this article are
included in the article’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted
by statutory regulation or exceeds the permitted use, you will need to
obtain permission directly from the copyright holder. To view a copy of this
licence, visit http://creativecommons.org/licenses/by/4.0/.

© The Author(s) 2026




npj Digital Medicine | (2026)9:281                                                   14
```
