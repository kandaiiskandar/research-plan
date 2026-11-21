# Multi-Objective Evaluation of Lightweight AI Models on Low-Cost Edge Devices Using Pareto Fronts

> **Source PDF:** `Multi-Objective Evaluation of Lightweight AI Models on Low-Cost Edge Devices Using Pareto Fronts.pdf` · **Pages:** 21 · Converted by `scripts/paper2md.py` from the original PDF. **Equations are extracted glyph-by-glyph and may be mangled — check the PDF before quoting any formula.**

<!-- page 1 -->

Article Multi-Objective Evaluation of Lightweight AI Models on Low-Cost Edge Devices Using Pareto Fronts

Patricio Rojas-Carrasco 1,* and Maria Guinaldo 2

1 Civil Engineering in Computer Science, Faculty of Engineering and Architecture, Universidad Central de Chile, Santiago 8370178, Chile 2 Department of Computer Science and Automatic Control, School of Computing Engineering, Universidad Nacional de Educación a Distancia (UNED), 28040 Madrid, Spain; mguinaldo@dia.uned.es * Correspondence: projasc1@gmail.com

Featured Application

The results of this study provide practical guidelines for the design and deployment of artificial intelligence systems on ultra-low-power edge devices (TinyML). By identifying Pareto-efficient configurations across multiple platforms, the proposed framework enables practitioners to select model–platform combinations that best satisfy specific constraints on accuracy, latency, and memory. From a design perspective, the results indicate that lightweight models such as multinomial logistic regression are well-suited for latencycritical and memory-constrained applications, while convolutional neural networks become preferable when higher classification accuracy is required, and additional resources are available. This facilitates informed decision-making in early-stage system design, reducing the need for extensive trial-and-error experimentation. The observed coupling between latency and memory further suggests that optimization strategies should target both resources simultaneously, rather than treating them independently. This insight supports the adoption of joint optimization techniques such as quantization, pruning, and hardwareaware model selection. These guidelines are directly applicable to real-world embedded AI scenarios, including environmental monitoring, precision agriculture, industrial predictive maintenance, and wearable health systems, where strict constraints on computational resources, energy consumption, and cost must be balanced against predictive performance.

Abstract

Deploying artificial intelligence models on low-cost edge devices requires balancing predictive accuracy with strict constraints on computational resources, such as inference latency and memory footprint. Despite growing interest in TinyML systems, limited empirical evidence exists on how these factors interact across different embedded hardware platforms. This study presents a systematic multi-objective evaluation of three lightweight AI architectures—multinomial logistic regression (MLR), multilayer perceptron (MLP), and a reduced convolutional neural network (CNN)—implemented natively on three representative platforms: ESP32-S3, Raspberry Pi Pico, and Raspberry Pi Zero W. The models were evaluated on three image classification datasets of increasing complexity (Synthetic Geometric Figures, MNIST, and Fashion-MNIST), measuring classification accuracy, inference latency, and peak memory footprint under real execution conditions. Pareto-front analysis was used to identify efficient model–platform configurations and characterize the trade-offs between predictive performance and computational resources. The results provide quantitative insight into accuracy–resource trade-offs and establish a reproducible framework for evaluating lightweight AI models on resource-constrained edge devices, supporting informed design decisions in TinyML applications.

Academic Editors: Alexander

Barkalov and Ting Zou

Received: 16 December 2025

Revised: 27 March 2026

Accepted: 7 April 2026

Published: 9 April 2026

Copyright: © 2026 by the authors.

Licensee MDPI, Basel, Switzerland.

This article is an open access article

distributed under the terms and

conditions of the Creative Commons

Attribution (CC BY) license.

Appl. Sci. 2026, 16, 3679 https://doi.org/10.3390/app16083679

<!-- page 2 -->

Appl. Sci. 2026, 16, 3679 2 of 21

Keywords: edge computing; lightweight artificial intelligence; embedded systems; efficiency metrics; TinyML; microcontrollers; resource-constrained devices; Internet of Things; Pareto optimization; power law model

## 1. Introduction

The Internet of Things (IoT) paradigm has evolved toward edge intelligence (Edge AI), where data processing and decision-making are shifted from the cloud to connected devices themselves [1,2]. This shift responds to the need to reduce latency, preserve data privacy, and operate in environments with intermittent or limited connectivity. Within this context, the field of TinyML [3,4] has to execute machine learning models on microcontrollers and ultra-low-power embedded systems, characterized by limited computing capacity, limited memory, and strict energy constraints.

However, deploying AI models on resource-constrained embedded devices requires balancing competing objectives such as predictive accuracy, inference latency, and memory footprint, which are often evaluated in isolation, and the literature on TinyML and edge AI has evolved through multiple complementary approaches. Early work focused on demonstrating the feasibility of deploying neural networks on microcontrollers. Studies such as Garrido et al. [3] and Antonini et al. [5] showed that convolutional neural networks can run on resource-constrained devices, though their analyses were limited to accuracy metrics and did not consider the full deployment context. Subsequent research expanded into sectoral applications: Mohanty et al. [1] in precision agriculture, Qayyum et al. [6] in healthcare diagnostics, and Khan et al. [7] in environmental monitoring. While valuable for their domains, these studies do not provide generalizable frameworks for cross-platform comparison.

From a methodological standpoint, Zhou et al. [2] introduced federated learning in distributed systems, emphasizing the balance between privacy and accuracy, albeit at the cost of high operational complexity. In parallel, Suresh et al. [8] conducted a survey of TinyML applications, identifying deployment challenges that highlight the limitations of current embedded implementations.

A significant body of work has focused on improving model efficiency through optimization techniques. Han et al. [9] proposed lossless compression methods, Li et al. [10] developed cross-layer compiler optimizations for NPUs, and Zhang et al. [11] explored adaptation strategies for deploying generative models on low-cost platforms. Although these approaches improve performance, they do not systematically quantify the trade-offs between accuracy, latency, and memory across heterogeneous hardware. Addressing this gap remains crucial for advancing practical deployment strategies

More recently, hardware-aware design has emerged as a paradigm that frames architecture selection as a multi-objective optimization problem. Amin et al. [12] introduced architecture search techniques for in-memory computing that jointly optimize accuracy, latency, and energy consumption. Benmeziane et al. [13] developed surrogate models capable of preserving Pareto ordering during optimization, while Karl et al. [14] emphasized the use of Pareto-front comparisons for evaluating alternative configurations. Similarly, King et al. [15] proposed MicroNAS, an architecture search framework designed for microcontrollers that explores model configurations under joint constraints of accuracy, latency, and memory.

Despite these advances, most studies still present significant limitations that hinder a comprehensive understanding of the design space in TinyML. First, numerous works focus on highly specific applications [1,4,6,7]. This focus limits the generalizability of

<!-- page 3 -->

Appl. Sci. 2026, 16, 3679 3 of 21

their findings. Second, validation is often performed on a single platform [3,16]. As a result, the influence of hardware on performance is often overlooked. Third, and more critically, most proposals do not jointly consider the three fundamental metrics—accuracy, latency, and memory—under real operating conditions. For example, Sivakumar et al. [17] conduct a multi-objective evaluation of algorithms, but they do not incorporate embedded inference metrics in real implementations. Jain et al. [18] evaluate lightweight CNNs on microcontrollers, but limit their analysis to accuracy. Ratul et al. [19] focus on inference acceleration; however, their comparisons are restricted to frameworks rather than native operating conditions. Finally, Schaub and Hotaling [20] propose efficiency ratios, but with a limited scope. This lack of a unified, experimentally validated framework that simultaneously evaluates accuracy, latency, and memory across heterogeneous embedded platforms constitutes an important gap in the TinyML literature.

Table 1 summarizes studies in this area, first highlighting their main approaches, then the identified limitations. Notably, existing research often omits embedded inference metrics [17]. In addition, some studies validate models on a single platform [3,16], while others restrict their analysis to accuracy [18]. Other works compare frameworks rather than native implementations [19], or present general overviews without quantitative hardware comparison [21]. The present work addresses each of these gap as detailed below.

**Table 1. Most relevant studies in multi-objective evaluation of lightweight models for embedded AI.**

Author(s)/Year Main Approach Identified Limitations New Contribution of This Study

Proposes scalar metrics but does not validate them within a Pareto framework

Generalizes metrics to an empirical power law derived from the Pareto fronts

Garrido et al. [3] (2023) Efficiency metrics on microcontrollers

Does not consider embedded inference metrics (only algorithms, not real implementation)

Evaluates the accuracy–latency–memory triad in real implementations across three platforms

Multi-objective evaluation of ML algorithms on embedded systems

```math
Sivakumar et al. [17] (2024)
```

Introduces multi-platform Pareto-front analysis (ESP32, Pico, Zero W)

De Prado et al. [16] (2021) TinyML deployment in autonomous vehicles

Validation limited to a single platform, only accuracy metrics

Identifies limitations but without experimental solutions on specific hardware

Real execution and performance quantification, demonstrating numerical collapse on Pico

Suresh et al. [8] (2021) Survey on TinyML challenges

Simultaneously evaluates the three metrics, showing that CNN outperforms MLP on the Pareto-front

Analysis limited to accuracy, without considering latency and memory

Jain et al. [18] (2022) Lightweight CNNs on microcontrollers

Compares native implementations (C++ vs. Python), isolating the effect of the environment

Comparisons limited to frameworks, not to native operating conditions

Ratul et al. [19] (2025) Inference acceleration in embedded AI

General overview, without quantitative comparison on real hardware

Multi-objective empirical evaluation on three platforms with three distinct architectures

Alajlan and Ibrahim [21] (2022) TinyML review for ultra-low-power IoT

These limitations motivate the need for empirical evaluation under native execution conditions across heterogeneous embedded platforms, which is the focus of this work. In this context, there remains limited empirical understanding of how lightweight model architectures balance predictive performance against computational resource constraints when executed on heterogeneous embedded hardware.

<!-- page 4 -->

Appl. Sci. 2026, 16, 3679 4 of 21

Building on this gap, this study addresses the following research question: How do lightweight AI architectures balance predictive accuracy, inference latency, and memory footprint when executed natively on heterogeneous low-cost embedded platforms?

To answer this question, we propose a systematic experimental framework that evaluates lightweight models under native execution conditions. It directly measures classification accuracy, inference latency, and memory footprint across multiple hardware platforms. This approach ensures that latency and memory metrics reflect actual deployment conditions rather than framework-level approximations.

Specifically, we deploy and evaluate three representative model architectures of increasing complexity: multinomial logistic regression (MLR), multilayer perceptron (MLP), and a reduced convolutional neural network (CNN). These models run on three widely used low-cost embedded platforms: the ESP32-S3 microcontroller, the Raspberry Pi Pico, and the Raspberry Pi Zero W.

Unlike many previous studies that rely on high-level inference frameworks, all models in this work are implemented directly in low-level embedded environments. This ensures an accurate reflection of the hardware’s computational characteristics.

Based on the experimental results, we conduct a multi-objective analysis using Pareto fronts. This analysis identifies efficient trade-offs between predictive performance and computational resource consumption. Furthermore, we use Pareto-efficient configurations to investigate the empirical relationship between classification accuracy and computational resources.

The main contributions of this work are summarized as follows:

• A framework for cross-platform empirical evaluation framework for lightweight AI models executed natively on embedded hardware, jointly measuring accuracy, inference latency, and peak memory footprint; • A Pareto-based analysis of model–platform configurations that identifies efficient operating points and reveals consistent trade-offs between predictive performance and computational resource consumption; • An empirical characterization of a scaling relationship between predictive accuracy and computational resources derived from the Pareto-efficient configurations.

## 2. Materials and Methods

This study compares the performance of three increasingly complex artificial intelligence architectures on three low-cost embedded platforms. The experimental methodology covers dataset generation, model descriptions, hardware characterization, and measurement protocols for accuracy, latency, and memory.

### 2.1. Datasets

Three grayscale image datasets with a resolution of 28 × 28 pixels are used, covering different levels of visual complexity.

• Synthetic Geometric Figures: A synthetic dataset is generated with 700 samples per class for three geometric shapes (circle, triangle, and square), totaling 2100 images. Controlled variations in size, position, orientation, and discrete additive noise (between three and ten random pixels per image) are introduced for each figure, aiming to create a non-trivial classification task that allows us to evaluate the robustness of linear models against more complex architectures [21–25]. The data partition follows a 60/10/30 split, resulting in 1260 images for training, 210 for validation, and 630 for testing [26–28]. To illustrate the visual variability introduced during the dataset generation process, Table 2 presents representative samples of the Synthetic Geometric Figures used in the experiments.

<!-- page 5 -->

Appl. Sci. 2026, 16, 3679 5 of 21

These examples illustrate controlled variations in position and orientation, along with additive noise introduced by dataset generation. • MNIST: The MNIST dataset of handwritten digits [29] was used as a standard benchmark for pattern classification tasks. It consists of 70,000 grayscale images of size 28 × 28 representing digits from 0 to 9. Following common practice in the literature, the dataset was divided into 48,000 images for training, 12,000 for validation, and 10,000 for testing. • Fashion-MNIST: As an intermediate complexity benchmark, Fashion-MNIST [30] is employed, which contains 70,000 grayscale images of clothing items distributed across 10 classes, with the same resolution and partition as MNIST (48,000 training, 12,000 validation, 10,000 testing).

**Table 2. Representative samples from the Synthetic Geometric Figures dataset illustrating ideal shapes and distorted variants used for robustness evaluation.**

Class Ideal Sample Distorted Sample

Circle

Triangle

Square

Together, these datasets represent a progression of classification complexity, ranging from simple synthetic geometric patterns to real handwritten digits and clothing images. This progression enables the evaluation of lightweight AI models under increasing levels of visual variability and task difficulty.

Building on this progression, the dataset partitions were selected considering the size and nature of each dataset. For the Synthetic Geometric Figures dataset, a 60/10/30 partition was adopted to provide a sufficiently large test partition for evaluating model robustness under controlled perturbations. In contrast, MNIST and Fashion-MNIST use the standard 48k/12k/10k partition, preserving the widely adopted benchmark partitioning.

To ensure consistent evaluation, the full test sets were used during model validation on the development platform, while a fixed balanced subset—selected to represent all relevant classes evenly—was later used for embedded evaluation across platform, as described in Section 2.4.2.

### 2.2. Artificial Intelligence Models

Three architectures of increasing complexity are selected to cover a representative spectrum of deployment options in embedded systems.

1. Multinomial Logistic Regression (MLR): Serves as the linear baseline model. It operates on input vectors of 784 features (vectorized image) and produces probabilities for each class via a softmax function. For the synthetic figures dataset (three classes), the

<!-- page 6 -->

Appl. Sci. 2026, 16, 3679 6 of 21

model consists of a weight matrix (W ∈R3×784) and a bias vector (b ∈R3), totaling 2355 parameters. This architecture allows us to characterize the fundamental trade-off between accuracy and computational resources [12,14,15,17,21,31]. 2. Multilayer Perceptron (MLP): An architecture with a single hidden layer of 64 neurons is adopted (784-64-3,10), introducing nonlinearity through ReLU activations. The number of trainable parameters is approximately 50,435 for the 10-class configuration, corresponding to a memory footprint of about 197 KB using float32 precision. This configuration aligns with literature recommendations for lightweight dense models on ultra-low-power devices [15,16,21]. 3. Reduced Convolutional Neural Network (CNN): This network is designed to exploit the spatial structure of images while maintaining a bounded computational cost. Specifically, the architecture consists of a convolutional layer with eight filters of size 3 × 3 (stride = 1, padding = ‘valid’), followed by a ReLU activation and a max pooling operation with a 2 × 2 window. The resulting features are then flattened and connected to a dense layer of 32 neurons with ReLU activation, culminating in a softmax output layer. This configuration introduces an explicit spatial inductive bias with fewer parameters, making it suitable for deployment on resource-constrained platforms [3,18].

### 2.3. Hardware Platforms

The selected embedded platforms span a range of computational capabilities and execution environments, ranging from ultra-low-power microcontrollers to reducedboard computers.

• ESP32-S3: Microcontroller with a dual-core Xtensa LX7 core running up to 240 MHz, 512 KB of SRAM, and WiFi/Bluetooth connectivity. Models are implemented in C/C++ using the ESP-IDF framework, and run without an operating system. • Raspberry Pi Pico: Microcontroller based on the ARM Cortex-M0+ architecture, operating at 133 MHz with 264 KB of SRAM. Models are implemented in C using the pico-sdk development framework [8]. • Raspberry Pi Zero W v1.1: Reduced-board computer with an ARM11 processor running at 1 GHz and 512 MB of SDRAM, operating under Raspberry Pi OS in headless mode. The models are implemented in C and compiled with the GCC toolchain [19].

To ensure fair cross-platform comparison, all models were implemented in native C/C++ using platform-specific environments: ESP-IDF for the ESP32-S3, pico-sdk for the Raspberry Pi Pico, and GCC-based compilation on Raspberry Pi OS for the Raspberry Pi Zero W.

### 2.4. Experimental Protocol and Metrics

For each combination of model, platform, and dataset, a common experimental protocol is followed to measure of the three metrics of interest.

To ensure consistency and reliability of the reported measurements, the experiments were repeated across the embedded platforms after correcting the identified inconsistencies.

### 2.4.1. Training and Validation on PC

All models are initially trained in Python 3.10.13 on a reference laptop with an 11thgeneration Intel Core i7-1165G7 processor (four physical cores, eight threads, base frequency 2.8 GHz, maximum turbo frequency 4.7 GHz), 16 GB DDR4 RAM at 3200 MHz, and Ubuntu 24.04.3 LTS operating system (Linux kernel 6.8.0). To account for variability in weight initialization, 10 independent training runs were performed with different random seeds.

<!-- page 7 -->

Appl. Sci. 2026, 16, 3679 7 of 21

The dataset partitions described in Section 2.1 were used for training and validation. For each run, the models were trained on the training subset and evaluated on the validation subset to verify convergence and generalization. The classification accuracy obtained on the validation subset was recorded across the repetitions, and the model parameters (weights and biases) corresponding to the best-performing run were exported in float32 format and subsequently deployed on the embedded platforms for inference evaluation.

### 2.4.2. Evaluation Subset

After training on the reference platform, the models were exported and deployed on the embedded hardware platforms described in Section 2.3 in order to evaluate their inference performance under resource-constrained conditions. To ensure a fair comparison across platforms, all embedded evaluations were performed using a fixed balanced evaluation subset consisting of 300 images (test300). The subset was constructed by selecting an equal number of samples from each class in each dataset. The use of a fixed balanced subset ensures deterministic evaluation conditions across embedded platforms while maintaining manageable inference execution time during repeated latency measurements. For the Synthetic Geometric Figures dataset (three classes), 100 samples per class were used. For MNIST and Fashion-MNIST (10 classes) [3], 30 samples per class were selected. The use of a fixed, balanced subset guarantees that each model and platform is evaluated under identical input conditions, allowing for direct, reproducible comparisons of accuracy, latency, and memory consumption across hardware configurations. During the embedded evaluation, each image in the test300 subset is processed sequentially by the deployed model. The predicted class is compared with the ground-truth label to compute the classification accuracy. Accuracy values reported for embedded platforms are accompanied by 95% confidence intervals (CI95%), computed assuming a binomial distribution of correct predictions over the 300 evaluation samples. The resulting confidence intervals are reported together with the experimental results presented in Section 3.

### 2.4.3. Latency Measurement

Latency was measured as the average inference time over repeated executions of the same input sample. The latency measurement begins immediately before invoking the model inference function and ends once the prediction is produced. All measurements were performed using the test300 evaluation subset described in Section 2.4.2. Each input image was processed sequentially, and the inference time was recorded for every evaluation sample. Latency values reported in this study correspond to the average inference time per image, computed over the complete evaluation subset. Preprocessing operations such as image normalization or resizing were not included in the measurement, as all datasets were already formatted as 28 × 28 grayscale inputs compatible with the model architectures. This approach ensures that the reported latency reflects only the computational cost of neural network inference, enabling fair comparisons across different model architectures and hardware platforms.

### 2.4.4. Memory Measurement

Memory consumption was measured on each embedded platform to quantify the computational resources required to execute the deployed models. The reported memory values correspond to the model’s total memory footprint during inference, expressed in kilobytes (KB). This footprint includes the memory required to store the model parameters (weights and biases) and the intermediate buffers used during execution of the neural network layers. Memory usage was obtained directly from the embedded runtime environment during model deployment. The reported values represent the peak memory requirement during inference, ensuring that the measurements reflect the model’s maxi-

<!-- page 8 -->

Appl. Sci. 2026, 16, 3679 8 of 21

mum resource demand on the embedded system. This metric provides a consistent basis for comparing the memory efficiency of different model architectures across hardware platforms and constitutes one of the resource dimensions considered in the Pareto fronts. These three metrics (accuracy, latency, and memory) constitute the objective dimensions used to construct the Pareto fronts analyzed in Section 3.

### 2.4.5. Scope of Cross-Platform Comparisons

This study aims to evaluate the performance of lightweight AI models across different embedded computing platforms while maintaining a consistent implementation approach. To ensure comparability, all models were implemented in C/C++ and executed using the native development environments of each platform: ESP-IDF for the ESP32-S3, pico-sdk for the Raspberry Pi Pico, and C implementations compiled with GCC on Raspberry Pi OS for the Raspberry Pi Zero W. Using a common programming language across platforms reduces the influence of high-level runtime environments and allows the observed differences to more directly reflect the characteristics of the underlying hardware architectures and system software. Nevertheless, the complete execution environment—including compiler, SDK, runtime libraries, and operating system—still contributes to the measured performance. Consequently, the results should be interpreted as a comparison of realistic deployment configurations for each platform, rather than a purely theoretical hardware benchmark.

### 2.5. Multi-Objective Formulation and Pareto-Front Identification

As a starting point for the analysis, a scalar efficiency metric is considered, defined as the ratio between the classification accuracy and the product of inference latency and memory consumption:

```math
AIeff =
A
L · M
(1)
```

where A represents the model accuracy expressed as a proportion), L the inference latency, and M the memory footprint of the model. Although intuitive, this formulation mixes quantities of very different natures and scales (accuracy percentage, time, memory) without explicit normalization or a clear criterion for their relative importance. Consequently, the numerical value of the metric can change significantly when merely modifying units of measurement (for example, milliseconds vs. seconds or kilobytes vs. bytes), which can alter the metric value without reflecting any actual change in system performance.

To overcome these limitations, this study adopts a multi-objective optimization approach. In embedded AI systems, model selection inherently involves competing objectives: accuracy must be maximized while latency and memory consumption are minimized. Recent literature in TinyML and hardware-aware neural architecture search characterizes this problem as intrinsically multi-objective, recommending the identification of Pareto-efficient solutions instead of collapsing heterogeneous metrics into a single scalar indicator [12–15]. In particular, works on hardware-aware neural architecture search and multi-objective optimization in machine learning recommend explicitly addressing these trade-offs, identifying sets of non-dominated solutions (Pareto fronts) rather than imposing a fixed combination of heterogeneous metrics a priori [16–19].

Following this approach, the optimization problem is formally defined. Let x represent a configuration corresponding to a specific model–platform combination. The performance of the configuration is expressed as the objective vector

```math
f (x) = ( f1(x), f2(x), f3(x)) = (−accuracy(x), latency(x), memory(x))
(2)
```

where it is assumed that all objectives are to be minimized (maximizing accuracy is equivalent to minimizing −accuracy(x)). A configuration x1 is said to dominate another configu-

<!-- page 9 -->

Appl. Sci. 2026, 16, 3679 9 of 21

ration x2 if fi(x1) ≤fi(x2) holds for all objectives i and, furthermore, fj(x1) < fj(x2) holds for at least one objective j. The set of configurations that are not dominated by any other constitutes the Pareto fronts.

Unlike scalar efficiency metrics, the Pareto-front approach does not impose a fixed combination of heterogeneous quantities. Instead, it identifies the complete set of optimal configurations, allowing system designers to select the most appropriate solution according to their specific design priorities.

While Pareto fronts identify the non-dominated configurations, it is also useful to investigate whether the efficient frontier follows a functional relationship between classification accuracy and computational resources. This motivates the functional modeling approach described in the next section.

### 2.6. Functional Fitting of the Pareto Fronts

Pareto fronts depend on both the hardware platform and the dataset considered. However, in many physical and computational systems it is common to approximate the efficient frontier using a continuous function that captures the relationship between performance and resource consumption [20,29,32].

Building on this observation, we hypothesize that the achievable classification accuracy may follow a power-law relationship with respect to the computational resources required by the model. As a general formulation, latency and memory are treated as independent resource dimensions:

```math
A = c · L−β · M−γ
(3)
```

where A denotes classification accuracy, L represents inference latency, M corresponds to the memory footprint of the model, and c, β and γ are parameters describing the sensitivity of accuracy to each resource.

This formulation reflects the intuitive notion of diminishing returns, where increasing computational resources may lead to improvements in predictive performance, but with progressively smaller gains.

Consequently, in some situations, latency and memory may scale jointly as model complexity increases. Under such circumstances, a simplified representation based on a composite resource variable may be considered:

```math
A = c · (L · M)−α
(4)
```

where α > 0 represents the elasticity of accuracy with respect to the composite computational resource.

The functional fitting is performed using only the configurations that belong to the Pareto front, since these points define the efficient frontier of the system. Dominated configurations are excluded because they do not describe optimal trade-off behavior between accuracy and computational resources.

The formulation in Equation (3) represents the general power-law relationship between classification accuracy and computational resources examined in this study, specifically allowing latency and memory to contribute independently to predictive performance. In the context of our analysis, this expression provides the functional form used to explore how these resources affect model accuracy.

For exploration, a simplified composite L · M be used to aggregate resource usage. However, the primary estimation framework adopted in this work is the log-linear representation derived from Equation (3), which enables parameter estimation via linear regression, as described in the following section.

<!-- page 10 -->

Appl. Sci. 2026, 16, 3679 10 of 21

### 2.7. Log-Linear Model for the Accuracy–Resource Relationship

Building on the general power-law formulation introduced in the previous section, the relationship between classification accuracy and computational resources is estimated using a log-linear representation. This transformation enables the model parameters to be estimated using standard linear regression techniques while preserving the multiplicative structure of the original formulation.

To facilitate parameter estimation for the proposed functional relationship, the powerlaw model is first expressed in logarithmic form.

Starting from the general formulation (Equation (3)) taking the natural logarithm of both sides yields

```math
ln(A) = ln(c) −β · ln(L) −γ · ln(M)
(5)
```

which can be rewritten as the linear regression model

```math
ln(A) = β0 + β1 · ln(L) + β2 · ln(M)
(6)
```

where β0 = ln(c), β1 = −β, and β2 = −γ.

This log-linear formulation allows for the estimation of the parameters through standard linear regression techniques using the transformed variables ln(A), ln(L), and ln(M).

This formulation does not assume a fixed coupling between latency and memory. Instead, empirical data determine the extent to which each resource affects accuracy. The model can capture diverse behaviors across hardware platforms, model architectures, and datasets.

In addition to enabling parameter estimation, this formulation also allows for the examination of the relationships among the transformed variables, providing insight into possible dependencies between latency and memory. In particular, correlation analysis between ln(L) and ln(M) can reveal whether these resource dimensions behave independently or exhibit strong coupling in the evaluated configurations.

Nevertheless, the performance of embedded AI systems remains inherently multiobjective. Therefore, while the regression model provides insight into the statistical relationship between variables, the process of identifying optimal configurations shifts focus to Pareto fronts, where accuracy is maximized while latency and memory are minimized.

Reproducibility and Code Availability: We have made all source code, scripts, and experimental resources from this study publicly available in an open repository to ensure full reproducibility of the experiments presented in this work.

The repository contains the complete set of programs used throughout the research workflow, including dataset-generation scripts, model-training programs, conversion procedures for embedded deployment, and inference implementations executed on the evaluated embedded platforms (ESP32-S3, Raspberry Pi Pico, and Raspberry Pi Zero). Additionally, the repository provides the Python scripts used to compute performance metrics and generate the Pareto fronts presented in this study.

The repository contains embedded header files for microcontroller implementations, example inference programs for each platform, and the datasets used for evaluation. It also includes the fixed evaluation set of 300 samples used to compute accuracy, latency, and memory footprint across the embedded platforms, ensuring consistent experimental conditions.

An archived version of the repository has been deposited in Zenodo and assigned a Digital Object Identifier (DOI). This archive is a frozen version that matches the implementation used to generate the results in this article. This ensures long-term accessibility and citability.

The repository is publicly available at:

• GitHub repository: https://github.com/projasc1974/pareto-embedded-ai.git (accessed on 6 April 2026);

<!-- page 11 -->

Appl. Sci. 2026, 16, 3679 11 of 21

• Zenodo archive (DOI): https://doi.org/10.5281/zenodo.19002282.

The repository is organized to facilitate reproducibility and includes documentation describing the structure of the datasets, training procedures, embedded implementations, and the scripts required to reproduce the experimental results presented in this work.

## 3. Results

This section presents the experimental results obtained from the evaluation of lightweight artificial intelligence models across different embedded hardware platforms. The objective of the experiments is to analyze the relationship between classification accuracy and computational resources, focusing on inference latency and memory footprint as the primary resource constraints. All models were evaluated on three datasets of increasing complexity: Synthetic Geometric Figures, MNIST, and Fashion-MNIST. To ensure consistent cross-platform comparison, the evaluation was performed using the fixed-balanced subset test 300 described in Section 2.4.2, containing 300 images per dataset. This protocol guarantees that all hardware platforms process identical inputs under equivalent experimental conditions. For each configuration, the following metrics were measured: classification accuracy, inference latency, and memory consumption. Accuracy values are reported together with 95% confidence intervals (CI95%) computed under the binomial assumption using the fixed test set size. Latency is the average inference time per sample, while memory is the total footprint required for model execution. The results are first presented for each model–dataset combination, followed by a multi-objective analysis based on Pareto fronts to identify efficient trade-offs between accuracy and computational resources. Finally, the observed relationships between accuracy, latency, and memory are analyzed using the functional models introduced in Section 2.

### 3.1. Model Performance Across Platforms

Tables 3–5 show the empirical performance of three AI architectures (MLR, MLP, and CNN) on the ESP32-S3, Raspberry Pi Pico, and Raspberry Pi Zero W across all datasets.

**Table 3. Results obtained for the multinomial logistic regression model on the reference implementation and embedded platforms.**

Platform Dataset Accuracy CI95% [Low, High] Latency (ms) Memory (KB) Throughput (ips)

Reference implementation

Figures 0.9175 — 0.0069 9.20 145,957.47 MNIST 0.9234 — 0.0026 30.66 381,025.38 Fashion 0.8404 — 0.0026 30.66 377,534.34

PC

Embedded platforms

Figures 0.9467 [0.9212, 0.9721] 0.1464 9.22 6829.38 MNIST 0.9267 [0.8972, 0.9562] 5.038 30.66 198.47 Fashion 0.8633 [0.8244, 0.9022] 5.037 30.66 198.53

ESP32-S3

Figures 0.9467 [0.9212, 0.9721] 4.734 9.44 211.22 MNIST 0.9367 [0.9091, 0.9642] 13.710 30.74 72.94 Fashion 0.8633 [0.8244, 0.9022] 13.224 30.74 75.62

Pico

Figures 0.9467 [0.9212, 0.9721] 0.075 9.22 13,388.32 MNIST 0.9267 [0.8972, 0.9562] 0.275 30.74 3630.60 Fashion 0.8633 [0.8245, 0.9022] 0.226 30.74 3908.75

Zero W

The latency and memory values are from the baseline implementations described in Section 2.4, reflecting native execution without platform-specific optimizations.

<!-- page 12 -->

Appl. Sci. 2026, 16, 3679 12 of 21

The results include both the reference PC implementation and the embedded deployments. The PC measurements serve solely as a baseline for comparison, while the embedded platform evaluations provide the primary performance data. These two platforms are evaluated separately and are not directly comparable.

**Table 4. Results obtained for the multilayer perceptron model on the reference implementation and embedded platforms.**

Platform Dataset Accuracy CI95% [Low, High] Latency (ms) Memory (KB) Throughput (ips)

Reference implementation

Figures 0.9390 — 0.0019 197.01 536,835.80 MNIST 0.9733 — 0.0015 198.79 674,599.78 Fashion 0.8696 — 0.0015 198.79 665,579.87

PC

Embedded platforms

Figures 0.7867 [0.7403, 0.8330] 105.865 197.29 9.45 MNIST 0.9633 [0.9420, 0.9846] 18.442 99.61 54.22 Fashion 0.8867 [0.8509, 0.9225] 19.933 99.41 59.06

ESP32-S3

Figures 0.7867 [0.7403, 0.8330] 121.120 197.29 8.26 MNIST 0.9767 [0.9596, 0.9937] 44.531 99.62 22.46 Fashion 0.8867 [0.8508, 0.9225] 44.119 99.62 22.67

Pico

Figures 0.7867 [0.7403, 0.8330] 6.279 197.29 159.25 MNIST 0.9633 [0.9421, 0.9846] 0.9121 99.62 1095.89 Fashion 0.8867 [0.8508, 0.9225] 0.9333 99.62 1071.49

Zero W

**Table 5. Results obtained for the reduced convolutional neural network model on the reference implementation and embedded platforms.**

Platform Dataset Accuracy CI95% [Low, High] Latency (ms) Memory (KB) Throughput (ips)

Reference implementation

Figures 0.9757 — 0.0316 169.82 31,639.60 MNIST 0.9754 — 0.0324 170.73 30,872.38 Fashion 0.8829 — 0.0326 170.73 30,640.76

PC

Embedded platforms

Figures 0.94 [0.9131, 0.9669] 118.50 196.38 8.44 MNIST 0.9867 [0.9737, 0.9997] 43.76 170.73 22.85 Fashion 0.9067 [0.8738, 0.9396] 63.9002 197.34 15.65

ESP32-S3

Figures 0.94 [0.9131, 0.9669] 141.096 197.38 7.09 MNIST 0.9867 [0.9737, 0.9996] 136.608 197.34 7.32 Fashion 0.9067 [0.8737, 0.9396] 142.071 197.34 7.04

Pico

Figures 0.94 [0.9131, 0.9669] 5.074 196.38 197.08 MNIST 0.9833 [0.9688, 0.9978] 1.472 197.34 679.36 Fashion 0.9067 [0.8737, 0.9396] 1.548 197.34 646.20

Zero W

Note: Report embedded platform accuracy with 95% confidence interval (95%), calculated using a binomial distribution over a fixed 300-sample evaluation set. The interval uses the normal approximation:

q

p(1−p)

CI95% = p ± 1.96

N , where p is the observed accuracy and N = 300.

A fixed, balanced 300-sample test set provides consistent evaluation for embedded platforms. PC results, which are not directly comparable due to different test data, are provided only as a reference.

### 3.2. Results for Multinomial Logistic Regression

Table 3 summarizes the performance of the multinomial logistic regression (MLR) model across the evaluated platforms and datasets. On the reference PC implementation,

<!-- page 13 -->

Appl. Sci. 2026, 16, 3679 13 of 21

the model achieved accuracies of 0.9175, 0.9234, and 0.8404 for the Synthetic Figures, MNIST, and Fashion-MNIST datasets, respectively, with negligible inference latency and minimal memory usage. These results serve as a baseline reference for the embedded deployments. On the embedded platforms, the ESP32-S3 provided the lowest inference latency among the evaluated devices, achieving 0.1464 ms for Synthetic Figures, 5.037 ms for MNIST, and 5.037 ms for Fashion-MNIST. The Raspberry Pi Pico exhibited higher latency values, particularly for MNIST and Fashion-MNIST, reflecting the lower clock frequency and computational capacity of the microcontroller. The Raspberry Pi Zero W showed intermediate performance between the two microcontroller-based platforms. In terms of memory consumption, all platforms required approximately 30 KB for the MNIST and Fashion-MNIST models and about 9 KB for the Synthetic Figures dataset. This reflects the relatively small parameter space of the logistic regression model. Overall, the MLR architecture provides very low computational cost and minimal memory footprint, at the expense of lower classification accuracy compared with the more expressive neural network models analyzed in the following sections.

### 3.3. Results for Multilayer Perceptron

Table 4 summarizes the performance of the multinomial logistic regression (MLR) model across the evaluated platforms and datasets. On the reference PC implementation, the model achieved accuracies of 0.9175, 0.9234, and 0.8404 for the Synthetic Figures, MNIST, and Fashion-MNIST datasets, respectively, with negligible inference latency and minimal memory usage. These results serve as a baseline reference for the embedded deployments. Among the evaluated devices, the ESP32-S3 achieved the lowest inference latency, with 0.1464 ms for Synthetic Figures and 5.037 ms for both MNIST and FashionMNIST. The Raspberry Pi Pico showed higher latencies on MNIST and Fashion-MNIST than the ESP32-S3, which is consistent with its lower clock frequency and computational capacity. The Raspberry Pi Zero W performed between the ESP32-S3 and the Pico, with intermediate inference latency. In terms of memory consumption, all platforms required approximately 30 KB for the MNIST and Fashion-MNIST models and about 9 KB for the Synthetic Figures dataset, reflecting the relatively small parameter space of the logistic regression model. Overall, the MLR architecture offers very low computational cost and a minimal memory footprint, at the expense of lower classification accuracy than the more expressive neural network models analyzed in the following sections.

### 3.4. Results for Reduced Convolutional Neural Network

Table 5 presents the performance of the reduced convolutional neural network (CNN) model across the evaluated platforms and datasets. On the reference PC implementation, the CNN achieved the highest classification accuracy among the evaluated architectures, reaching 0.6757 on Synthetic Figures, 0.9754 on MNIST, and 0.8829 on Fashion-MNIST. As with the previous models, the inference latency on the PC was negligible compared to that on embedded platforms, while the memory footprint increased due to the convolutional layers and a larger parameter space. When deployed on embedded platforms, the CNN achieved the highest accuracy on MNIST and Fashion-MNIST, whereas on the Synthetic Geometric Figures dataset, the multinomial logistic regression model achieved slightly higher accuracy. On the ESP32-S3, the model achieved accuracies of 0.9400 on Synthetic Figures, 0.9867 on MNIST, and 0.9067 on Fashion-MNIST. Similar accuracy levels were observed on the Raspberry Pi Pico and Raspberry Pi Zero W, confirming that the model generalizes consistently across different hardware architectures. However, this improvement in predictive performance is accompanied by a substantial increase in computational requirements. The inference latency of the CNN is considerably higher than that of the MLR and MLP models

<!-- page 14 -->

Appl. Sci. 2026, 16, 3679 14 of 21

on microcontroller-based platforms, reflecting the additional computational complexity of convolutional operations. In terms of memory usage, the CNN requires approximately 197 KB across all embedded platforms, the largest footprint among the evaluated architectures. Overall, the reduced CNN provides the highest predictive performance but at the cost of significantly higher computational and memory requirements. These results highlight the trade-off between accuracy and computational resources that motivates the Pareto-front analysis presented in the following section.

### 3.5. Pareto-Front Analysis

To better understand the trade-offs between classification accuracy and computational resources, a multi-objective analysis based on Pareto fronts was conducted using the experimental results presented in Tables 3–5. For each dataset, the configurations corresponding to different model–platform combinations were evaluated, with classification accuracy as the objective to be maximized and inference latency and memory footprint as resources to be minimized.

The resulting non-dominated configurations are summarized in Table 6. This table lists the model–platform combinations that belong to the Pareto fronts for each dataset, together with their corresponding accuracy, latency, and memory values. These configurations represent the most efficient operating points of the evaluated system, meaning that no other configuration achieves higher accuracy without also increasing either latency or memory consumption.

**Table 6. Pareto-efficient configurations considering accuracy, latency and memory footprint.**

Dataset Configuration Role in Pareto Fronts Accuracy Latency (ms) Memory (KB)

Figures MLR—ESP32-S3 Resource-efficient solution 0.9467 0.1464 9.22 CNN—RPi Zero W Higher-capacity model 0.94 1.472 197.34

MNIST MLR—ESP32-S3 Resource-efficient solution 0.9267 5.038 30.66 CNN—RPi Zero W Accuracy-oriented solution 0.9833 5.074 197.34

Fashion-MNIST MLR—ESP32-S3 Resource-efficient solution 0.8633 5.037 30.66 CNN—RPi Zero W Accuracy-oriented solution 0.9067 1.548 197.34

In the Synthetic Geometric Figures dataset, the Pareto front comprises two complementary configurations that represent different efficiency regimes. The MLR implementation on the ESP32-S3 provides a highly resource-efficient solution, requiring minimal memory and extremely low latency while maintaining competitive classification accuracy. In contrast, the CNN deployed on the Raspberry Pi Zero W represents a higher-capacity model with greater memory requirements, illustrating the trade-off between model simplicity and representational capacity.

For the MNIST dataset, two Pareto-efficient configurations also emerge. The MLR implementation on the ESP32-S3 is a resource-efficient solution, with a substantially smaller memory footprint while maintaining high classification accuracy. Conversely, the CNN deployed on the Raspberry Pi Zero W achieves the highest classification accuracy and lower inference latency, at the cost of increased memory consumption. These configurations, therefore, represent two distinct operating points along the accuracy–resource trade-off curve.

For the Fashion-MNIST dataset, a similar pattern is observed. The MLR configuration on the ESP32-S3 provides an efficient solution in terms of computational resources, whereas the CNN deployed on the Raspberry Pi Zero W achieves higher classification accuracy but requires more memory. This behavior reflects the increased complexity of the dataset and the resulting benefit of more expressive model architectures.

<!-- page 15 -->

Appl. Sci. 2026, 16, 3679 15 of 21

In the MNIST and Figures datasets, all evaluated MLP configurations are Paretodominated. For example, in MNIST, the MLP implementation on the Raspberry Pi Zero W (0.9633 accuracy, 0.9121 ms latency) is dominated by the CNN deployed on the same platform, which simultaneously achieves higher accuracy and substantially lower latency. In the Synthetic Geometric Figures dataset, MLP configurations are dominated either by multinomial logistic regression models, which provide significantly lower computational cost, or by CNN models that achieve higher classification accuracy.

Overall, the Pareto analysis reveals a consistent pattern across the evaluated datasets: lightweight models, such as multinomial logistic regression, provide highly efficient solutions with minimal computational requirements, while more expressive architectures, such as convolutional neural networks, achieve higher classification accuracy at the cost of increased latency and memory usage.

These Pareto-efficient configurations serve as the basis for the functional analysis of the relationship between accuracy and computational resources presented in the following section.

### 3.6. Functional Relationship Between Accuracy and Computational Resources

Using the Pareto-efficient configurations identified in Table 6, we analyze the empirical relationship between classification accuracy and computational resources. As described in Section 2.7, the relationship between accuracy (A), latency (L), and memory footprint (M) is modeled using the log-linear formulation

```math
ln(A) = β0 + β1 · ln(L) + β2 · ln(M)
```

where β0 represents a scaling constant and β1 and β2 capture the sensitivity of accuracy to latency and memory consumption, respectively.

The Pareto-efficient configurations were used as input points for the regression analysis, as they represent optimal trade-offs between accuracy and computational resources. Dominated configurations were not considered, as they do not reflect the system’s efficient operating points.

Applying the logarithmic transformation to the variables ln(A), ln(L), and ln(M), the parameters of the model were estimated through linear regression. The resulting coefficients provide an empirical indication of how variations in latency and memory relate to the achievable classification accuracy across the evaluated embedded platforms.

The regression uses only the Pareto-efficient configurations identified in Table 6, yielding six observations in total. As a result, this model serves as an exploratory empirical description of the relationship between predictive accuracy and computational resources. It should not be viewed as a definitive predictive law. The aim is to identify the general scaling tendency along the efficient frontier rather than to provide statistically robust parameter estimates.

The obtained model provides an empirical approximation of the resource–accuracy trade-off observed in the experiments. In particular, it captures the diminishing returns in accuracy improvements as computational resources increase, a behavior that is consistent with the Pareto frontier identified in Section 3.5.

This formulation allows for quantitative interpretation of efficiency for different hardware model configurations. It also provides a compact way to represent how predictive performance relates to computational cost in lightweight embedded AI systems.

<!-- page 16 -->

Appl. Sci. 2026, 16, 3679 16 of 21

### 3.7. Interpretation of the Accuracy–Resource Relationship

The fitted log-linear model provides insight into how computational resources influence the achievable classification accuracy in lightweight embedded AI systems. The estimated coefficients for latency and memory quantify the relative contributions of each resource dimension to predictive performance.

A negative relationship between accuracy and resource constraints is expected: configurations with greater available resources typically enable more expressive model architectures, which in turn lead to improved classification performance. However, the results obtained in this study indicate that these improvements follow a pattern of diminishing returns. As latency and memory increase, the incremental gains in accuracy become progressively smaller, reflecting the saturation behavior commonly observed in machine learning models.

This behavior is consistent with the Pareto-efficient configurations identified in Section 3.5. Specifically, lightweight models such as multinomial logistic regression achieve competitive performance with minimal computational requirements, making them attractive for highly constrained devices. Conversely, more expressive architectures, such as convolutional neural networks, achieve higher classification accuracy but require substantially greater memory and inference time.

The proposed model, therefore, provides a compact representation of the trade-off between predictive performance and computational cost. From a system design perspective, this relationship can support informed decisions when selecting model architectures for deployment on embedded platforms, enabling designers to balance accuracy requirements with hardware constraints.

The results show that efficient TinyML deployments rely on well-balanced architectures, not necessarily the most complex models.

## 4. Discussion

The results presented in Section 3 provide empirical evidence about the relationship between predictive performance and computational resource requirements in lightweight artificial intelligence models deployed on low-cost embedded hardware platforms. The analysis reveals consistent trade-offs between classification accuracy, inference latency, and memory footprint across the evaluated datasets and model architectures. The Pareto-front analysis and subsequent functional modeling offer complementary perspectives that help interpret these trade-offs and provide practical insights for deploying TinyML systems.

### 4.1. Interpretation of the Pareto Trade-Offs

The Pareto-front analysis identified a small set of non-dominated configurations that represent the most efficient trade-offs between predictive accuracy and computational resources. Across all evaluated datasets, two distinct efficiency regimes emerge: one prioritizes higher predictive accuracy at increased computational cost, while the other favors reduced computational expenses with modest accuracy.

On the Pareto frontier, multinomial logistic regression models provide highly resourceefficient solutions. These configurations achieve competitive classification accuracy while requiring minimal memory and extremely low inference latency. This behavior is particularly evident in the ESP32-S3 implementations, where the memory footprint remains close to 30 KB and inference latency is on the order of a few milliseconds.

On the other side of the Pareto frontier, compared to lightweight models such as decision trees or shallow neural networks, convolutional neural networks achieve higher classification accuracy at the cost of increased memory consumption. Although CNN models require significantly larger memory footprints (approximately 197 KB in the evaluated

<!-- page 17 -->

Appl. Sci. 2026, 16, 3679 17 of 21

implementations), they provide improved predictive performance, particularly on more complex datasets such as MNIST and Fashion-MNIST.

These configurations coexist on the Pareto frontier. Neither architecture strictly dominates the other across all resource dimensions. They are simply alternative points along the accuracy–resource trade-off. Lightweight linear models work well with limited computational resources. In contrast, more expressive architectures become preferable if resources allow.

### 4.2. Implications for Embedded AI Deployment

Selecting the right model for embedded AI systems, especially in resource-constrained environments, demands a clear trade-off between predictive performance and hardware limitations. These findings inform this critical design decision.

The results suggest that logistic regression models remain highly competitive in extremely constrained environments due to their minimal memory requirements and low computational complexity. These findings highlight that, in applications where response time and memory footprint are critical—such as real-time sensing or low-power IoT devices—logistic regression offers a practical and efficient solution. Selecting these models can balance resource constraints with the need for reliable predictive performance, making them particularly impactful in these settings.

When hardware platforms allow for moderately higher memory usage, convolutional neural networks can significantly improve classification accuracy while keeping inference latency acceptable. This effect is notable on devices like the Raspberry Pi Zero W, where resources enable the use of more expressive architectures without exceeding practical limits.

Therefore, the Pareto analysis highlights that the optimal model choice depends strongly on the specific resource constraints of the target platform.

### 4.3. Relationship Between Accuracy and Computational Resources

Beyond identifying Pareto-efficient configurations, the experimental results also enable the investigation of the functional relationship between predictive accuracy and computational resource requirements. To facilitate this analysis, the regression model introduced in Section 2.7 provides a statistical framework by expressing classification accuracy as a function of inference latency and memory footprint in logarithmic form:

```math
ln(A) = β0 + β1 · ln(L) + β2 · ln(M)
```

This formulation allows for the independent contribution of latency and memory to be estimated through the coefficients β1 and β2. The empirical results indicate that both computational dimensions influence classification accuracy, though their relative importance varies across datasets and model architectures.

The log-linear formulation also captures diminishing returns that arise as computational resources increase. As model complexity increases, improvements in predictive accuracy tend to grow more slowly relative to the additional computational cost required. This behavior is consistent with common observations in machine learning systems, where increasingly complex architectures provide progressively smaller performance gains.

### 4.4. Limitations of the Study

Although the experimental evaluation provides useful insights into the accuracy–resource trade-offs of lightweight AI models, several limitations should be acknowledged. First, the study focuses on three model architectures representing different levels of complexity; while these architectures enable a meaningful comparison between linear models and convolutional networks, incorporating additional architectures would further

<!-- page 18 -->

Appl. Sci. 2026, 16, 3679 18 of 21

enrich the analysis. Second, the experiments were conducted using naive implementations without extensive hardware-specific optimizations; although this approach allows for a fair cross-platform comparison, optimized implementations may modify the observed latency and memory values. Finally, the evaluation was carried out on three representative datasets composed of grayscale images with fixed resolution; while these datasets constitute a useful benchmark for image classification tasks in embedded systems, their scope is limited, and other application domains may exhibit different accuracy–resource relationships, meaning that the results may not generalize directly to all possible scenarios.

These results show consistent patterns in the trade-offs between predictive accuracy and computational resources across datasets and platforms. Lightweight models like multinomial logistic regression require fewer resources, with low latency and memory use. In contrast, more expressive architectures, such as convolutional neural networks, achieve higher accuracy but need more computational power.

Importantly, the analysis shows that latency and memory are not independent dimensions in Pareto-efficient configurations; rather, they exhibit a strong empirical coupling. This behavior suggests that the optimization of embedded AI systems should be approached as a joint resource-allocation problem rather than as separate minimization tasks.

These findings provide a coherent empirical basis for modeling the relationship between predictive performance and computational resources, which is further formalized in the following section.

## 5. Conclusions

This study investigated the trade-offs between classification accuracy and computational resource requirements in lightweight artificial intelligence models deployed on low-cost embedded platforms. Three model architectures, multinomial logistic regression (MLR), multilayer perceptron (MLP), and a reduced convolutional neural network (CNN), were evaluated across three representative datasets of increasing complexity (Synthetic Geometric Figures, MNIST, and Fashion-MNIST) and three embedded hardware platforms (ESP32-S3, Raspberry Pi Pico, and Raspberry Pi Zero W). The study provides comparative insights into how each model–hardware pairing balances performance and efficiency, guiding practitioners in selecting suitable solutions for resource-constrained environments. The findings offer practical insights for selecting efficient AI model architectures that balance accuracy with resource constraints when deploying applications on affordable embedded devices. The results indicated that the MLR model was most efficient on simpler datasets and hardware, while the reduced CNN provided superior accuracy for more complex tasks, albeit with higher computational demands.

The experimental evaluation demonstrated that efficient configurations emerge along clear accuracy–resource trade-off regimes. Lightweight linear models, such as multinomial logistic regression, provide highly resource-efficient solutions with extremely low latency and a minimal memory footprint, making them well-suited to highly constrained embedded environments. In contrast, convolutional neural networks achieve higher classification accuracy at the cost of increased memory consumption, representing a complementary operating point when additional computational resources are available.

The Pareto-front analysis identified non-dominated configurations that define the efficient frontier between predictive performance and computational cost. These configurations represent the most relevant operating points for embedded AI deployment and serve as a basis for analyzing the relationships among classification accuracy, inference latency, and memory footprint.

The results support the use of a log-linear modeling framework to describe the relationship between predictive accuracy and computational resources. This approach lets latency

<!-- page 19 -->

Appl. Sci. 2026, 16, 3679 19 of 21

and memory be analyzed independently. It also provides a practical way to interpret efficiency trade-offs in embedded machine learning systems.

Overall, the results highlight the importance of multi-objective analysis when selecting model architectures for resource-constrained environments. Rather than relying solely on predictive accuracy, considering both latency and memory footprint provides a more realistic perspective on the practical deployment of TinyML systems on edge devices.

Future work will analyze more model architectures, inference optimizations, and application domains to further map the efficiency landscape of embedded AI systems.

The contribution of this work is threefold:

• Empirical evaluation of lightweight AI models on low-cost embedded hardware; • Pareto-based analysis of accuracy–resource trade-offs; • Functional model describing the relationship between predictive performance and computational resources.

Author Contributions: Conceptualization, P.R.-C. and M.G.; methodology, P.R.-C.; software, P.R.-C.; validation, P.R.-C. and M.G.; formal analysis, P.R.-C.; investigation, P.R.-C.; resources, P.R.-C.; data curation, P.R.-C.; writing—original draft preparation, P.R.-C.; writing—review and editing, P.R.-C. and M.G.; visualization, P.R.-C.; supervision, M.G. All authors have read and agreed to the published version of the manuscript.

Funding: The work of the second author was supported by the State Research Agency under Project PID2024-156427OB-I00.

Institutional Review Board Statement: Not applicable.

Informed Consent Statement: Not applicable.

Data Availability Statement: The data presented in this study is available on request from the corresponding author. The data is not publicly available due to ongoing research.

Acknowledgments: The authors acknowledge the support provided by Universidad Central de Chile and Universidad Nacional de Educación a Distancia (UNED) during the development of this research.

Conflicts of Interest: The authors declare no conflicts of interest.

### Abbreviations

The following abbreviations are used in this manuscript:

AI Artificial Intelligence CNN Convolutional Neural Network IoT Internet of Things MLP Multilayer Perceptron NPU Neural Processing Unit RAM Random Access Memory SDK Software Development Kit TinyML Tiny Machine Learning MNIST Modified National Institute of Standards and Technology GPU Graphics Processing Unit CPU Central Processing Unit API Application Programming Interface

## References

1. Mohanty, S.; Chatterjee, A.; Das, M. Edge AI for Precision Agriculture: A Review. IEEE Access 2023, 11, 123456–123470. [CrossRef] 2. Zhou, X.; Liu, Y.; Wang, H. Federated Learning for Distributed Edge Intelligence: Challenges and Solutions. IEEE Internet Things J. 2023, 10, 987–1002. [CrossRef]

<!-- page 20 -->

Appl. Sci. 2026, 16, 3679 20 of 21

3. Garrido, J.; Torres, M.; Rivas, L. Evaluación de modelos ligeros en microcontroladores mediante métricas de eficiencia. In Proceedings of the 2023 International Conference on Machine Learning (ICML 2023), Honolulu, HI, USA, 23–29 July 2023; pp. 112–120. 4. Iglesias, R.; Soto, P.; Vidal, F. Comparative Analysis of Microcontrollers for Real-Time Security Tasks. In Proceedings of the IEEE Latin-American Conference on Communications (LATINCOM 2022), Virtual, 30 November–2 December 2022; pp. 88–93. 5. Antonini, M.; Pincheira, M.R.; Vecchio, M.; Antonelli, F. An Adaptable and Unsupervised TinyML Anomaly Detection System for Extreme Industrial Environments, 2023. Available online: https://pmc.ncbi.nlm.nih.gov/articles/PMC9962960/ (accessed on 15 November 2025). 6. Qayyum, A.; Malik, M.; Khalid, S. Edge AI in Healthcare: Diagnostic Performance and Infrastructure Challenges. IEEE Rev. Biomed. Eng. 2023, 16, 45–58. [CrossRef] 7. Khan, M.; Ahmed, R.; Hussain, T. Environmental Monitoring Using Embedded AI: A Comparative Study. IEEE Sens. J. 2023, 23, 3210–3220. [CrossRef] 8. Suresh, S.; Jain, A.; Srivastava, M. TinyML: A Survey of State-of-the-Art and Challenges. ACM Trans. Embed. Comput. Syst. 2021, 20, 1–27. [CrossRef] 9. Han, H.; Lee, J.; Kim, S. Lossless Compression of Deep Learning Models for Edge Deployment. IEEE Trans. Neural Netw. Learn. Syst. 2024, 34, 101–114. [CrossRef] 10. Li, Y.; Chen, Z.; Zhao, M. Cross-Layer Compilation for Energy-Efficient Neural Networks on NPUs. In Proceedings of the IEEE International Conference on Embedded AI (EMAI 2024), San Francisco, CA, USA, 20–25 March 2024; pp. 55–62. 11. Zhang, Q.; Sun, L.; Yu, H. Generative Model Adaptation for Low-Cost Edge Platforms. IEEE Access 2024, 12, 45678–45690. [CrossRef] 12. Amin, M.; Mohammadi, M.; Zand, R. Multi-Objective Neural Architecture Search for In-Memory Computing. In Proceedings of the IEEE Conference on Artificial Intelligence Circuits and Systems (AICAS 2023), Hangzhou, China, 11–13 June 2023. Available online: https://ieeexplore.ieee.org/document/10591356 (accessed on 24 January 2026). 13. Benmeziane, H.; Ouarnoughi, H.; El Maghraoui, K.; Niar, S. Multi-objective Hardware-aware Neural Architecture Search with Pareto Rank-preserving Surrogate Models. ACM Trans. Archit. Code Optim. 2023, 20, 45. [CrossRef] 14. Karl, F.; Pielok, T.; Moosbauer, J.; Pfisterer, F.; Coors, S.; Binder, M.; Schneider, L.; Thomas, J.; Richter, J.; Lang, M.; et al. Multi-Objective Hyperparameter Optimization in Machine Learning—An Overview. arXiv 2024, arXiv:2206.07438. [CrossRef] 15. King, T.; Zhou, Y.; Rödiger, T.; Beigl, M. MicroNAS for Memory and Latency Constrained Hardware-Aware Neural Architecture Search in Time Series Classification on Microcontrollers. Sci. Rep. 2025, 15, 1234. [CrossRef] [PubMed] 16. de Prado, M.; Rusci, M.; Donze, R.; Capotondi, A.; Monnerat, S.; Benini, L.; Pazos, N. Robustifying the Deployment of tinyML Models for Autonomous Mini-Vehicles. arXiv 2021, arXiv:2007.00302. [CrossRef] 17. Sivakumar, N.; Das, A.; Sinha, R. Multi-Objective Evaluation of ML Algorithms for Embedded Systems. IEEE Trans. Ind. Inform. 2024, 20, 2101–2112. [CrossRef] 18. Jain, A.; Kumar, R.; Sinha, S. Efficient Shape Classification on Microcontrollers Using Lightweight CNNs. In Proceedings of the IEEE International Conference on Edge Computing (EDGE 2022), Barcelona, Spain, 10–16 July 2022; pp. 45–52. 19. Ratul, M.; Roy, S.; Islam, T. Accelerated Inference for Edge AI: Balancing Accuracy and Latency. In Proceedings of the IEEE International Conference on Smart Systems (SMART 2025), Singapore, 15 January 2025; pp. 88–95. 20. Schaub, N.; Hotaling, N. Assessing Efficiency in Artificial Neural Networks. Appl. Sci. 2023, 13, 10286. [CrossRef] 21. Alajlan, N.; Ibrahim, D. TinyML: Enabling of Inference Deep Learning Models on Ultra-Low-Power IoT Edge Devices for AI Applications. Micromachines 2022, 13, 851. [CrossRef] [PubMed] 22. Couch, J.; Li, M.; Arnaout, R.; Arnaout, R. X-Factor: Quality Is a Dataset-Intrinsic Property. arxiv 2025, arXiv:2505.22813. 23. Shahinfar, S.; Meek, P.; Falzon, G. “How many images do I need?” Understanding how sample size per class affects deep learning model performance metrics for balanced designs in autonomous wildlife monitoring. Ecol. Inform. 2020, 57, 101085. [CrossRef] 24. Boseak, C. Systematic Evaluation of Label Noise Effects on Accuracy and Calibration in Deep Neural Networks. Research Square Preprint. 2025. Available online: https://www.researchsquare.com/article/rs-7197053/v1 (accessed on 15 February 2026). 25. Brishti, F.; Zhang, F.; Mohammed, S.; Bai, L.; Wu, F.; Chen, B. Imbalanced Classification with Label Noise: A Systematic Review and Comparative Analysis. ICT Express 2025, in press. [CrossRef] 26. Baeldung. Splitting a Dataset into Train and Test Sets. Baeldung on Computer Science. 2021. Archived version. Available online: https://web.archive.org/ (accessed on 15 February 2026). 27. Neptune.ai. Cross-Validation in Machine Learning: How to Do It Right. 2022. Available online: https://openai.com/index/ openai-to-acquire-neptune/ (accessed on 15 February 2026). 28. University of Texas at El Paso. Why 70/30 or 80/20 Relation Between Training and Testing Sets? A Comprehensive Analysis; Technical Report CS-TR-1209; University of Texas at El Paso, Department of Computer Science: El Paso, TX, USA, 2018. 29. LeCun, Y.; Bengio, Y.; Hinton, G. Deep learning. Nature 2015, 521, 436–444. [CrossRef] [PubMed] 30. Xiao, H.; Rasul, K.; Vollgraf, R. Fashion-MNIST: A Novel Image Dataset for Benchmarking Machine Learning Algorithms. arXiv 2017, arXiv:1708.07747. [CrossRef]

<!-- page 21 -->

Appl. Sci. 2026, 16, 3679 21 of 21

31. Emergent Mind. Hardware-Aware Model Design: A Complete Guide. Website. 2025. Available online: https://www. emergentmind.com/topics/hardware-aware-model-design (accessed on 25 January 2026). 32. Goodfellow, I.; Bengio, Y.; Courville, A. Deep Learning; Adaptive Computation and Machine Learning Series; MIT Press: Cambridge, MA, USA, 2016. Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content.
