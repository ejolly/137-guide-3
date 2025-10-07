## 2016 — Jara‑Ettinger, J., Gweon, H., Schulz, L. E., & Tenenbaum, J. B. (2016). The Naïve Utility Calculus: Computational Principles Underlying Commonsense Psychology. *Trends in Cognitive Sciences.*

**Full Citation:** Jara‑Ettinger, J., Gweon, H., Schulz, L. E., & Tenenbaum, J. B. (2016). The Naïve Utility Calculus: Computational Principles Underlying Commonsense Psychology. *Trends in Cognitive Sciences*, 20(8), 589–604. DOI: 10.1016/j.tics.2016.05.011.

**Topic Tags:** Commonsense psychology, Bayesian inversion, Utility theory, Generative models, Child development

### Core Question / Problem
What simple computational principles allow humans (including infants) to infer others’ goals, preferences, competence and beliefs? The authors propose a compact hypothesis: people employ a naïve utility calculus—an intuitive generative model where agents choose plans to maximize expected utilities (rewards minus costs), and observers invert that model to infer latent values.

### Conceptual or Computational Framework
The naïve utility calculus frames commonsense psychology as Bayesian inversion of an agent’s generative planning model. Agents compute expected utility U(plan)=R(outcome)−C(action), choose high‑utility plans (noisy rationality), and observers infer rewards and costs by observing chosen actions. This is an algorithmic‑level proposal that maps directly onto computational cognitive science traditions (Bayesian models, inverse planning). fileciteturn2file12

### Methods Overview
This review synthesizes developmental and adult behavioral experiments, plus formal models. Key empirical paradigms include path‑choice tasks where terrain and object placement change costs, verbal preference inferences, help‑refusal experiments, and graded confidence measures. The authors compare model predictions to human judgments across parametric manipulations (costs, visibility, competence).

### Key Findings
- A naïve utility calculus accounts for a wide set of inferences: preference learning, help‑seeking judgments, competence attributions, and counterfactual reasoning about forgone options. fileciteturn2file10
- Observers interpret effortful, costly actions as stronger evidence of preference; route choices inform beliefs about cost estimates and competence; action omissions can be informative when utilities are considered.
- Modeling choices with Bayesian inverse planning captures graded human judgments and confidence, explaining both developmental continuities and adult reasoning biases.

### Interpretation & Significance
The proposal unifies diverse phenomena under a single, testable computational framework. It shifts the explanatory burden from rule lists to a compact generative model (plans → utilities → actions) and emphasizes that much of commonsense social inference is explainable as Bayesian inversion. Importantly, it links early infant reasoning to the same computational core that supports adult social cognition.

### Computational‑Social‑Cognitive‑Scientist Hat
Formally, the observer computes p(costs,rewards | observed actions) ∝ p(actions | plan(costs,rewards)) p(prior). The likelihood runs the generative planner forward to compute action probabilities; the inversion yields posteriors over objectives. Extensions incorporate reward/cost uncertainty, limited competence, and noisy planning.

### Teaching Hooks
- Classroom demo: show different paths to a goal with varying costs and ask students to infer preferences/competence; compare with model predictions.
- Exercise: implement a minimal inverse‑planning algorithm for a grid world where actions have costs and outcomes have rewards.

### Pedagogical Lens
Use the utility calculus to bridge normative economic ideas and everyday social reasoning: emphasize that this is an *intuitive* model (not normative human rationality) that is nevertheless computationally powerful and developmentally early.

### Connections
Connects to simulation/forward‑model ideas (both use generative models), predictive brain frameworks, theory‑of‑mind development, and Bayesian models of cognition more broadly.

### Key Quotes or Phrases
- “People assume that others choose actions to maximize utilities — the rewards they expect to obtain relative to the costs they expect to incur.” fileciteturn2file12

### Concept Graph
- Generative planning model (plans → utilities → actions) → Bayesian inversion → inferred preferences, beliefs, competence.
  - **Naïve Utility Calculus:** An intuitive generative model positing agents maximize expected utilities; observers invert it to infer latent psychological variables. **Notable Figures:** Jara‑Ettinger, Tenenbaum. **Related Concepts:** Inverse planning; Bayesian inference.

### Relevant Terms
- **Existing Terms Used:** Theory of Mind; Predictive Mind; Representation; Generative Model (implicit). fileciteturn1file2
- **New Terms to Add:** 
  - **Naïve Utility Calculus:** An intuitive generative model that represents agents as planning to maximize expected utility (rewards minus costs); observers infer agents’ preferences, beliefs, and competence by Bayesian inversion of this planning model. **Related Concepts:** Utility theory; Inverse planning; Bayesian inference.
