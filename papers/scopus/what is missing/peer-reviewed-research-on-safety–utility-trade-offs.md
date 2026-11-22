

## Key Gaps and Limitations in Previous Studies

Several limitations and gaps have been identified in peer-reviewed research on safety–utility trade-offs in selective prediction, probabilistic shielding, learning to defer, and partial AI abstention for safety-critical human-facing decision support. Below is a structured summary of what is missing from previous studies:

---

### **Major Gaps Identified**

| **Area**                | **Missing Elements / Limitations**                                                                                  | **Confidence** |
|------------------------|---------------------------------------------------------------------------------------------------------------------|---------------|
| **Human Factors**      | Most prior work assumes human behavior remains unchanged when interacting with AI, neglecting the dynamic nature of human-AI collaboration and its impact on outcomes [1] . | High          |
| **Model Accessibility**| Existing selective prediction methods often require access to model internals or retraining, which is impractical for powerful, closed-source models like GPT-4 [2] [3] . | High          |
| **Out-of-Domain Robustness** | Selective prediction techniques frequently fail in out-of-domain settings, limiting their reliability in real-world applications [4] [5] . | High          |
| **Benchmarking & Evaluation** | Lack of standardized, publicly available datasets and common evaluation protocols makes it difficult to compare algorithms across studies and conditions [6] . | High          |
| **Quantification of Trade-offs** | The trade-off between coverage (how many cases are handled by the model) and risk (potential for harm) is rarely quantified, especially in medical imaging [7] . | Moderate      |
| **Uncertainty Quantification** | Traditional uncertainty quantification methods struggle with LLMs due to computational constraints and unique sources of uncertainty (e.g., input ambiguity, reasoning path divergence) [8] . | Moderate      |
| **Statistical Guarantees** | Heuristic approaches to uncertainty quantification lack statistical guarantees for key metrics like false discovery rate in selective prediction tasks [9] . | Moderate      |
| **Real-Time Deployment** | Real-time deployment is hindered by computational demands and lack of robust, efficient algorithms [6] [10] . | Moderate      |
| **Multiple Experts**    | Learning to defer with multiple experts faces challenges in optimally assigning instances, balancing accuracy and computational cost, and lacks robust optimization strategies [11] . | Moderate      |

---

### **Additional Challenges**

- **Transparency and Trust:** Existing approaches often lack mechanisms to foster transparency and awareness of model limitations, which is crucial for appropriate trust in human-AI systems [12] .
- **Distributional Shifts:** Many models are not robust to shifts between training and test data distributions, leading to increased dependence on human intervention and reduced reliability [4] .
- **Regulatory and Safety Standards:** There are gaps in aligning AI-enabled medical devices with regulatory safety standards and protocols [13] .

---

### **Summary Table**

| **Limitation**                  | **Description**                                                                                 | **Cited Abstracts** |
|---------------------------------|-----------------------------------------------------------------------------------------------|---------------------|
| Human-AI interaction modeling   | Assumes static human behavior, lacks dynamic collaboration modeling                            | [1]                 |
| Closed-source model adaptation  | Requires model internals/retraining, impractical for LLMs                                      | [2] [3]             |
| Out-of-domain performance       | Poor reliability in unfamiliar settings                                                        | [4] [5]              |
| Benchmarking & evaluation       | No standardized datasets/protocols                                                             | [6]                 |
| Coverage-risk quantification    | Rarely quantified in medical imaging                                                           | [7]                 |
| Uncertainty quantification      | Struggles with LLMs, lacks statistical guarantees                                              | [8] [9]            |
| Real-time deployment            | Computationally demanding, lacks efficient algorithms                                          | [6] [10]             |
| Multi-expert deferral           | Lacks robust assignment and optimization strategies                                            | [11]                |
| Transparency & trust            | Insufficient mechanisms for fostering trust                                                    | [12]                |
| Regulatory alignment            | Gaps in safety standards for medical devices                                                   | [13]                |

---

**In summary, previous studies often overlook human factors, lack robust evaluation protocols, struggle with out-of-domain robustness, and face challenges in uncertainty quantification and real-time deployment. Addressing these gaps is essential for advancing safe and effective AI decision support in safety-critical domains.**

References
1. Role of Human-AI Interaction in Selective Prediction
Bondi, E., Koster, R., Sheahan, H., (...), Dvijotham, K.
Proceedings of the 36th AAAI Conference on Artificial Intelligence, AAAI 2022, 2022
https://www.scopus.com/pages/publications/85130545462?origin=scopusAI

2. Consistency and Uncertainty: Identifying Unreliable Responses from Black-Box Vision-Language Models for Selective Visual Question Answering
Khan, Z., Fu, Y.
Proceedings of the IEEE Computer Society Conference on Computer Vision and Pattern Recognition, 2024
https://www.scopus.com/pages/publications/85207255904?origin=scopusAI

3. Abstention is all you need
Schonwalder, E., Falkenberg, C., Hartmann, C., Lehner, W.
2025 IEEE 12th International Conference on Data Science and Advanced Analytics, DSAA 2025, 2025
https://www.scopus.com/pages/publications/105029899417?origin=scopusAI

4. ASPEST: Bridging the Gap Between Active Learning and Selective Prediction
Chen, J., Yoon, J., Ebrahimi, S., (...), Pfister, T.
Transactions on Machine Learning Research, 2024
https://www.scopus.com/pages/publications/85219584678?origin=scopusAI

5. Towards Improving Selective Prediction Ability of NLP Systems
Varshney, N., Mishra, S., Baral, C.
Proceedings of the Annual Meeting of the Association for Computational Linguistics, 2022
https://www.scopus.com/pages/publications/85137593267?origin=scopusAI

6. A Meta Analytic Review of Supervised and Unsupervised Learning Techniques For Real-Time Vehicle Fault Prediction and Safety Enhancement
Patil, K.S., Jain, A.
2025 IEEE International Conference on Advances in Computing Research on Science Engineering and Technology, ACROSET 2025, 2025
https://www.scopus.com/pages/publications/105031425325?origin=scopusAI

7. Uncertainty-Aware Selective Prediction in Brain-Tumour MRI Classification: Selective Risk Reduction and Component-Wise Reliability Findings
Alshamlan, H.
Bioengineering, 2026
https://www.scopus.com/pages/publications/105054513314?origin=scopusAI

8. Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey
Liu, X., Chen, T., Da, L., (...), Wei, H.
Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, 2025
https://www.scopus.com/pages/publications/105014313879?origin=scopusAI

9. COIN: Uncertainty-Guarding Selective Question Answering for Foundation Models with Provable Risk Guarantees
Wang, Z., Duan, J., Wang, Q., (...), Xu, K.
Proceedings of the AAAI Conference on Artificial Intelligence, 2026
https://www.scopus.com/pages/publications/105034885906?origin=scopusAI

10. Enabling Cooperative Autonomy in UUV Clusters: A Survey of Robust State Estimation and Information Fusion Techniques
Li, S., López-Benítez, M., Lim, E.G., (...), Qin, X.
Drones, 2025
https://www.scopus.com/pages/publications/105023082178?origin=scopusAI

11. Mastering Multiple-Expert Routing: Realizable H-Consistency and Strong Guarantees for Learning to Defer
Mao, A., Mohri, M., Zhong, Y.
Proceedings of Machine Learning Research, 2025
https://www.scopus.com/pages/publications/105023951024?origin=scopusAI

12. "I Know That I Don't know ⋯ and I Explain Why" Robust Abstention via Counterfactual Explanations
Bonsignori, V., Punzi, C., Pellungrini, R., Giannotti, F.
IEEE Access, 2026
https://www.scopus.com/pages/publications/105043092066?origin=scopusAI

13. Medical Device Safety: An Analytical International Survey of AI/ML-Enabled Medical Devices
Finn, O.O.
Proceedings - 2025 IEEE Conference on Artificial Intelligence, CAI 2025, 2025
https://www.scopus.com/pages/publications/105011290569?origin=scopusAI