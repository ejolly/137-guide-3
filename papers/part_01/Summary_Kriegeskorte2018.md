### Full Citation
Kriegeskorte, N. & Douglas, P. (2018). Cognitive computational neuroscience. *Nature Neuroscience*.

### Topic Tags
computational neuroscience, representational models, deep neural networks, Marr’s levels, task-performing models

### Core Question / Problem
How can cognitive science, computational neuroscience, and artificial intelligence be productively integrated to explain brain information processing? The paper asks what it means to “understand the brain” and argues for building task-performing computational models that are constrained by brain and behavioral data.

### Conceptual or Computational Framework
The authors propose a *cognitive computational neuroscience* program: development of brain‑computational models (BCMs) that (a) perform cognitive tasks, (b) are neurobiologically plausible at an appropriate level, and (c) predict detailed patterns of brain activity and behavior. Mapped to Marr’s levels: the work stresses integrating the computational level (what problem is solved), algorithmic/representational level (how representations and algorithms realize the computation), and the implementational level (how neural dynamics plausibly implement those algorithms).

### Methods Overview
This is a synthesis / review. It surveys representational analyses (encoding/decoding/RSA), connectivity and dynamical models, neural network (deep) models, and cognitive-level formalisms (production systems, reinforcement learning, Bayesian models). The paper highlights studies that test models’ internal representations against neuronal and fMRI data (e.g., deep nets predicting ventral-stream responses).

### Key Findings
- Representational and decoding approaches reveal what information is present in brain regions but are insufficient alone to explain computational mechanisms.
- Deep convolutional neural networks optimized for object classification currently provide the best image-computable models of ventral-stream representations.
- Cognitive-level models (e.g., Bayesian, reinforcement learning, production systems) remain invaluable for higher-level cognition; they complement neural-net models where biological fidelity is low.
- The field needs *task‑performing* models that bridge behavior and neural dynamics, tested with carefully designed tasks, shared datasets, and quantitative tests.

### Interpretation & Significance
The paper argues for a cultural and methodological shift: move from isolated experiments and verbal theorizing toward large-scale, task-driven computational models evaluated against brain and behavioral data. This agenda frames much of modern computational social cognition — not just mapping functions to regions but building mechanistic models that *do* the cognitive work.

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: would appreciate the emphasis on behavior arising from person × environment × representation (task worlds as environments).
- Marr: would approve of integrating computational, algorithmic, and implementational levels — but would insist on clear separation of levels when designing tests.
- Brunswik: would emphasize ecological validity and probabilistic cues — the paper’s call for naturalistic tasks and big datasets resonates with Brunswikian probabilistic functionalism.

### Teaching Hooks
- Show the *representational similarity* figure (ventral-stream ↔ deep-net layers) and ask students to predict which network layer will best match early vs late visual areas.
- Analogy: building a car (task) vs mapping engine parts (implementation) — both necessary to understand driving behavior.

### Pedagogical Lens
- Conceptual difficulty: 3.5/5
- Prerequisites: basic ML (what a neural net does), fMRI basics, Marr’s levels.
- Common misconceptions: "A brain map = an algorithm"; "high decoding accuracy implies understanding."
- Discussion prompt: Design a simple task and propose how you would test two competing BCMs using brain and behavioral data.

### Connections
- Links to Predictive Mind (generative models), Marr’s levels, and modern debates about interpretability of large models.

### Key Quotes or Phrases
- “What I cannot create, I do not understand.”  
- “Task‑performing computational models that explain how cognition arises from neurobiologically plausible dynamic components will be central to a new cognitive computational neuroscience.”

### Concept Graph
- Task design → model training → neural representation similarity → behavioral prediction.
- Cognitive model (top-down) ↔ neural implementation (bottom-up) — both constrain each other.

### Relevant Terms
- **Existing Terms Used:** Marr’s levels, generative model, representational models, decoding, neural network, predictive mind.

(end of summary)