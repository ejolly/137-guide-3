## 2001 — Blakemore, S.-J., & Decety, J. (2001). From the perception of action to the understanding of intention. *Nature Reviews Neuroscience.*

**Full Citation:** Blakemore, S.-J., & Decety, J. (2001). From the perception of action to the understanding of intention. *Nature Reviews Neuroscience*, 2(8), 561–574.

**Topic Tags:** Biological motion, Simulation theory, Forward models, Mentalizing, Theory of Mind

### Core Question / Problem
How do observers move from low-level perception of biological motion to high-level inferences about others’ intentions? The review asks which perceptual and neural mechanisms allow humans (and other animals) to extract intentions from observed action sequences.

### Conceptual or Computational Framework
The paper synthesizes psychophysics, developmental studies, and neuroimaging under a simulation-forward‑model framework: observers internally simulate observed actions using motor representations (forward models) and map predicted sensory consequences to intentions. This sits at Marr’s algorithmic/implementational interface: representations (motor plans, efference copies) + transformations (forward prediction) enable social inference.

### Methods Overview
This is a review—evidence synthesized includes: point‑light (Johansson) biological‑motion psychophysics, infant/developmental behavior showing early animacy detection, single‑cell and fMRI studies implicating the superior temporal sulcus (STS), inferior parietal regions, medial prefrontal cortex (mPFC), cerebellum and putative mirror‑system involvement (parietal / premotor circuits). Key paradigms: point‑light displays, Heider–Simmel animations, action observation vs execution contrasts, apparent‑motion manipulations, and imitation tasks.

### Key Findings
- Biological motion is processed as a special class of stimuli (point‑light displays) and drives automatic attributions of agency and intention. fileciteturn1file1
- The posterior STS is reliably activated by biological motion; medial PFC and temporo‑parietal regions by mental‑state attribution. Motor areas (premotor cortex, inferior parietal lobule) and cerebellum are recruited during action observation, especially when imitation or prediction demands are high. fileciteturn1file6
- Forward models (efference copy → predicted sensory consequences) provide a mechanism for distinguishing self‑caused from external events and can be co‑opted to estimate others’ intentions by simulating their motor commands.
- Imitation and simulation offer both developmental scaffolding for ToM and a mechanistic route to infer goals from kinematic forms.

### Interpretation & Significance
Blakemore & Decety position the brain as a “simulating machine” where perception and action systems overlap to support mentalizing. Rather than a purely inferential, propositional ToM, social understanding can arise from embodied predictive computations grounded in sensorimotor representations. The review connects early emergence of animacy detection to later, higher‑order theory‑of‑mind circuitry, suggesting continuity between perception and abstract mental‑state reasoning.

### Computational‑Social‑Cognitive‑Scientist Hat
Formalizing the claims: the observer’s generative model contains motor plans p(plan), a forward model f(plan) → predicted sensory trajectories, and a mapping from predicted trajectories to latent intentions. Reverse inference (Bayesian inversion) over plans given observed kinematics yields posterior beliefs about goals. This is compatible with Bayesian predictive frameworks and complements later “naïve utility” style models for goal inference.

### Teaching Hooks
- Demo: point‑light walker; ask students to infer sex, emotion, or intention from motion alone.
- Exercise: sketch a simple forward‑model pseudocode that maps a motor command to an expected trajectory and show how mismatch signals could update intention estimates.
- Discussion prompt: compare simulation (embodied) vs theory‑theory (propositional) routes to mindreading.

### Pedagogical Lens
Emphasize mechanism over chronology: students should grasp *how* motor representations could be repurposed for social inference (forward models + Bayesian inversion), not just that “mirror neurons = empathy.” Use diagrams to show signal flow: observed kinematics → motor resonance → forward prediction → inference over goals.

### Connections
Links to Marr’s levels (algorithmic: representations of motor plans; implementational: mirror‑system circuits), predictive coding frameworks, and developmental work on infants’ goal attribution. Also complements computational Bayesian models that invert generative action models.

### Key Quotes or Phrases
- “The brain is a powerful simulating machine, designed to detect biological motion in order to extract intentions.” fileciteturn1file15

### Concept Graph
- Biological motion → triggers animacy detection → engages STS and motor representations.
  - **Forward model:** A predictive mapping from motor command to expected sensory consequences. **Notable Figures:** Wolpert, Miall. **Related Concepts:** Efference copy; Motor prediction.
  - **Simulation theory:** Represent other minds by generating similar processes in oneself. **Notable Figures:** Goldman. **Related Concepts:** Mirror system; Imitation.

### Relevant Terms
- **Existing Terms Used:** Biological Motion; Mentalizing; Intentional Stance; Theory of Mind; Representation; Predictive Mind. fileciteturn1file2
