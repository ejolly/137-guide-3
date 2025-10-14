## 2019 — Thornton, M. A., Weaverdyck, M. E., & Tamir, D. I. (2019). The brain represents people as the mental states they habitually experience. *Nature Communications.*

**Full Citation:** Thornton, M. A., Weaverdyck, M. E., & Tamir, D. I. (2019). The brain represents people as the mental states they habitually experience. *Nature Communications, 10*, 2291.

**Topic Tags:** Person Representation, Summed State Hypothesis, Neural Traits, Social Prediction

### Core Question / Problem
How are person‑specific representations organized in the brain? Do we represent people by stable trait dimensions, or by the *frequency‑weighted sum* of the mental states they habitually experience (the “summed state” hypothesis)?

### Conceptual or Computational Framework
The summed state hypothesis frames person representation as a linear generative model: person pattern ≈ Σ frequency(state_i) × pattern(state_i). This is contrasted with trait‑based models (low‑dimensional trait vectors). The analysis spans Marr’s levels: computational goal (represent idiosyncratic persons), algorithmic hypothesis (summed state encoding), and implementational test (fMRI pattern reconstruction).

### Methods Overview
Multi‑method approach: (1) fMRI—separate participants rated famous people and isolated mental states; (2) behavioral online ratings of state frequencies per person; (3) text and behavioral datasets (biographical text similarity, choice predictions) to test generalizability. Pattern‑reconstruction and model‑comparison metrics assessed whether summed state or trait models better predict neural/person similarity.

### Key Findings
- Frequency‑weighted sums of state‑specific neural patterns accurately reconstruct neural person‑patterns across subjects.  
- The summed state model outperforms trait‑based models across neural, behavioral, and textual data (higher correlations, better model fits).  
- Summed states predicted interpersonal choice behavior and reflected reliable neural variance underlying person perception.

### Interpretation & Significance
The brain appears to encode people compositionally via the mental states they typically experience. This mechanism is powerful because states are both observable (through expressions, actions) and computationally tractable: summation is a straightforward aggregation that supports prediction and generalization.

### Computational‑Social‑Cognitive‑Scientist Hat
The summed state account implies a generative representational codec: estimating person‑specific priors over state distributions. Models of social prediction should therefore maintain a state‑frequency histogram per person and use it to predict future behavior. This maps onto Bayesian models with state priors that are updated with observations.

### Teaching Hooks
- Demonstration: reconstruct a classmate’s likely behavior by summing frequent states (e.g., stressed, curious) and compare to trait descriptions.  
- Data activity: show figure 3 scatterplots and have students interpret which model fits better (summed states vs. traits). fileciteturn1file8

### Pedagogical Lens
Use this paper to illustrate compositional representations and connect to the course’s computational goals: how simple generative rules (linear summation) can create rich person models useful for prediction.

### Connections
Links to Thornton & Tamir’s broader program (mental‑state centric models), trait psychology (Whole‑Trait theory), and neural pattern‑based approaches to social cognition. Also relates to predictive processing: person models provide priors that shape state prediction.

### Key Quotes or Phrases
- “People are represented as the sums of the mental states they experience.” fileciteturn1file8

### Concept Graph
- Person representation = Σ frequency(state) × state pattern.  
  - **Summed State Hypothesis:** compositionally builds person encodings from state representations. **Notable Figures:** Tamir, Thornton. **Related Concepts:** Representation; Predictive Mind.

### Relevant Terms
- **Existing Terms Used:** Representation; Mentalizing; Predictive Mind; Transition Structure. fileciteturn1file12
- **New Terms to Add:**  
  - **Summed State Representation:** A compositional person encoding defined as the frequency‑weighted sum of mental‑state representations. **Definition:** A compact, generative representation supporting person‑specific prediction. **Related Concepts:** Generative Model; Person Representation.

---

*Instructor note:* This paper is ideal for teaching compositionality and Marr’s algorithmic/implementational linkage—showing how a simple summation rule has measurable neural signatures and behavioral consequences.

