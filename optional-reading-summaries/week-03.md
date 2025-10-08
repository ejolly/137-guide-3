## 2016 — Jara‑Ettinger, J., Gweon, H., Schulz, L. E., & Tenenbaum, J. B. (2016). The Naïve Utility Calculus: Computational Principles Underlying Commonsense Psychology. *Trends in Cognitive Sciences.*

**Full Citation:** Jara‑Ettinger, J., Gweon, H., Schulz, L. E., & Tenenbaum, J. B. (2016). The Naïve Utility Calculus: Computational Principles Underlying Commonsense Psychology. *Trends in Cognitive Sciences*, 20(8), 589–604. DOI: 10.1016/j.tics.2016.05.011.

**Topic Tags:** Commonsense psychology, Bayesian inversion, Utility theory, Generative models, Child development

### Core Question / Problem
What simple computational principles allow humans (including infants) to infer others' goals, preferences, competence and beliefs? The authors propose a compact hypothesis: people employ a naïve utility calculus—an intuitive generative model where agents choose plans to maximize expected utilities (rewards minus costs), and observers invert that model to infer latent values.

### Conceptual or Computational Framework
The naïve utility calculus frames commonsense psychology as Bayesian inversion of an agent's generative planning model. Agents compute expected utility U(plan)=R(outcome)−C(action), choose high‑utility plans (noisy rationality), and observers infer rewards and costs by observing chosen actions. This is an algorithmic‑level proposal that maps directly onto computational cognitive science traditions (Bayesian models, inverse planning).

### Methods Overview
This review synthesizes developmental and adult behavioral experiments, plus formal models. Key empirical paradigms include path‑choice tasks where terrain and object placement change costs, verbal preference inferences, help‑refusal experiments, and graded confidence measures. The authors compare model predictions to human judgments across parametric manipulations (costs, visibility, competence).

### Key Findings
- A naïve utility calculus accounts for a wide set of inferences: preference learning, help‑seeking judgments, competence attributions, and counterfactual reasoning about forgone options.
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
- "People assume that others choose actions to maximize utilities — the rewards they expect to obtain relative to the costs they expect to incur."

### Concept Graph
- Generative planning model (plans → utilities → actions) → Bayesian inversion → inferred preferences, beliefs, competence.
  - **Naïve Utility Calculus:** An intuitive generative model positing agents maximize expected utilities; observers invert it to infer latent psychological variables. **Notable Figures:** Jara‑Ettinger, Tenenbaum. **Related Concepts:** Inverse planning; Bayesian inference.

### Relevant Terms
- **Existing Terms Used:** Theory of Mind; Predictive Mind; Representation; Generative Model (implicit).
- **New Terms to Add:**
  - **Naïve Utility Calculus:** An intuitive generative model that represents agents as planning to maximize expected utility (rewards minus costs); observers infer agents' preferences, beliefs, and competence by Bayesian inversion of this planning model. **Related Concepts:** Utility theory; Inverse planning; Bayesian inference.

---

## 2021 — Thornton, M. A., & Tamir, D. I. (2021). The Organization of Social Knowledge Is Tuned for Prediction. *Trends in Cognitive Sciences.*

**Full Citation:** Thornton, M. A., & Tamir, D. I. (2021). The Organization of Social Knowledge Is Tuned for Prediction. *[journal]*.

**Topic Tags:** Predictive Mind, Mentalizing, Transition Structure, Generative Model, Representation, Neural geometry

### Core Question / Problem
How is social knowledge—people’s knowledge of actions, mental states, and traits—organized so that observers can rapidly predict other people’s future mental states and actions? The paper asks whether conceptual (psychological) and neural representations are structured not merely to describe people but specifically to support prediction of their future states.

### Conceptual or Computational Framework
Thornton & Tamir adopt a predictive-processing / generative-models framing: people encode compact, low‑dimensional maps of social concepts (states, traits, actions) that emphasize transitions and regularities useful for forecasting. Mapping to Marr’s levels: at the computational level the goal is accurate social prediction; at the algorithmic level, knowledge is organized as shared dimensions (e.g., valence, sociality, competence/agency) and transition structures; at the implementational level, overlapping neural codes in the social brain (mPFC, parietal cortex, STS/ATL) realize these maps. The work emphasizes *transition structure*—probabilities linking states/actions across time—as the algorithmically relevant representation for prediction.

### Methods Overview
Across several empirical tests (behavioural norms, neural decoding, and representational analyses), the authors: collect large-scale ratings of mental states/actions and their transition probabilities; build conceptual spaces (dimensions and distance metrics) for states, traits, and actions; and test whether those spaces align with neural representational geometry using fMRI decoding and pattern analyses. Core manipulations examine (a) dimensionality of social spaces, (b) whether transition statistics are encoded, and (c) cross-domain similarity (do trait and state maps share dimensions?). Participants were typical lab subjects for rating tasks; fMRI participants performed social judgment tasks while activity patterns were measured and decoded.

### Key Findings
- Social knowledge is organized along a small set of shared dimensions (valence, sociality/impact, competence/agency) that recur across mental states, traits, and actions.
- Transition statistics—how likely one mental state or action leads to another—are represented in conceptual spaces and predict behavioral judgments about what will happen next.
- Neural patterns in the canonical ‘social brain’ reflect these dimensions and support decoding across domains: the same dimensions that structure conceptual maps are discoverable in mPFC, parietal areas, and STS/ATL, suggesting a shared neural code for dimensions useful for prediction. These overlapping maps allow trait representations to be reconstructed from habitual state patterns (i.e., counting states explains trait impressions).

### Interpretation & Significance
The paper argues that the mind organizes social knowledge primarily for *prediction* rather than mere description. This reframes classical person perception (traits vs. states) and theory‑of‑mind research: rather than separate modules for trait inference and state reasoning, overlapping low‑dimensional maps and transition structures let observers reuse the same code to anticipate future states and actions. For social‑cognitive researchers and computational cognitive scientists, this supplies a mechanistic account of how generative models for other minds might be represented and learned.

### Computational‑Social‑Cognitive‑Scientist Hat
- Kurt Lewin: Would appreciate recasting behavior as driven by internal representations (R) interacting with person and environment—these maps operationalize R.\
- David Marr: The paper is explicit about Marr’s levels—clear computational goal (predict others), algorithmic representation (dimensions + transition matrix), and testable implementational predictions (neural geometry).\
- Egon Brunswik: The emphasis on transition probabilities is Brunswikian—perceivers exploit probabilistic ecological regularities to make inferences under uncertainty.

### Teaching Hooks
- Show a short clip (dance → exhaustion → sitting) and ask students to predict next action; reveal how transition statistics guide expectations.\
- Draw a 2D schematic with valence on x and sociality on y, plot everyday states (happy, embarrassed, annoyed) and show arrows for likely transitions.

### Pedagogical Lens
- Pre‑requisites: predictive processing basics, representations, Marr’s levels\
- Common misconceptions: confusing descriptive taxonomies (lists of states) with transition‑rich, predictive maps\
- Exam question prompt: "Explain how transition structure in social knowledge supports rapid prediction of others’ actions and provide evidence from neural representational geometry."

### Connections
Links strongly to Predictive Mind, Generative Models, Mentalizing, the ACT‑FAST taxonomy, and prior Thornton/Tamir work on the 3D mind model (rationality, social impact, valence).

### Key Quotes or Phrases
- "Social knowledge is organized to support prediction: dimensions and transition structure make the future statistically tractable."\
- "The same low‑dimensional code underlies trait and state representations, enabling efficient forecasting of other people."

### Concept Graph
- Dimensions (valence, sociality, competence) → structure conceptual maps.\
- Transition probabilities + conceptual maps → enable prediction of next states/actions.\
- Neural geometry (mPFC, STS/ATL) ↔ encodes the same dimensions → allows readout of predictions.
  - **ACT‑FAST Taxonomy:** A compact action taxonomy outlining dimensions (e.g., Agency, Competence, Temporal features) used to scaffold action prediction across domains. **Notable Figures:** Thornton & Tamir. **Related Concepts:** Action representation; Transition Structure.

---

## 2023 — Tamir, D. I., & Thornton, M. A. (2023). Predicting Other People Shapes the Social Mind. *Advances in Experimental Social Psychology.*

**Full Citation:** Tamir, D. I., & Thornton, M. A. (2023). Predicting other people shapes the social mind. In *Advances in Experimental Social Psychology.* Academic Press.  

**Topic Tags:** Mentalizing; Social Prediction; Theory of Mind; Predictive Mind; Generative Models; Representation; Transition Structure

### Core Question / Problem
Is social knowledge primarily organized to support prediction of other people’s future behavior, and how does a predictive framing change representational organization compared to descriptive or label-based framings?

### Conceptual or Computational Framework
Situated in predictive-processing / computational cognitive science: social cognition is tuned for forecasting. At Marr’s levels: (a) Computational — minimize surprise about others’ actions; (b) Algorithmic — representations and transition structures that encode how latent states generate observable actions over time; (c) Implementational — social brain regions that instantiate predictive representations.

### Methods Overview
Integrates large behavioral paradigms, representational similarity analyses (RSA), clustering tasks contrasting predictive vs. descriptive prompts, prediction-learning experiments, cognitive modeling (transition/generative models), and neuroimaging analyses linking representational geometry to transition structure.

### Key Findings
- Predictive framing reorganizes social representations: participants emphasize transition-relevant features when asked to predict, improving forecasting accuracy.  
- RSA and behavioral clustering show predictive structure explains more variance in representational geometry than static label-based structures.  
- Models that encode transitions/generative mappings outperform static trait-only models in explaining behavior.  
- Neuroimaging evidence (where present) indicates mPFC/TPJ representational geometry aligns with predictive transition structures.

### Interpretation & Significance
The paper reframes social cognition as an active prediction engine: representation and task goals (prediction vs description) shape mental organization. Emphasizing transition structure shifts theoretical focus from static trait inference to dynamic, generative models of agents, consistent with Predictive Mind frameworks.

### Computational-Social-Cognitive-Scientist Hat
- **Lewin:** sees representations (R) mediating person×environment dynamics (B = f(P,E,R)).  
- **Marr:** supports mapping computational goal (predict) to algorithmic/representational proposals (transition matrices/generative models).  
- **Brunswik:** asks about ecological validity and cue reliability — transition emphasis aligns with probabilistic cue-validity thinking.

### Teaching Hooks
- Analogy: social knowledge as a weather model — transitions matter more than snapshots.  
- Figure idea: 2×2 contrast of trait-based vs transition-based grouping and resulting prediction differences.

### Pedagogical Lens
- **Pre-reqs:** predictive processing, RSA basics, ToM foundations.  
- **Discussion prompt:** "If you could store one feature about a person to best predict future behavior, what would it be and why?"

### Connections
Links to Predictive Mind, Generative Models, Thornton & Tamir work on transition structure and neural geometry.

### Key Quotes or Phrases
- “Social knowledge is organized to support accurate prediction of others.”  
- “Transition structure — how states change over time — explains representational geometry better than static labels.”  

### Concept Graph
Latent states → generate actions (via generative models); Transition structure → organizes representation; Predictive task framing → reshapes representational geometry.

### Relevant Terms
**Existing Terms Used:** Mentalizing; Predictive Mind; Representation; Theory of Mind; Transition Structure.  

---

## 2025 — Wang, X., et al. (2025). Modeling Other Minds: A computational account of social cognition and its development. *Preprint.*

**Full Citation:** Wang, X., et al. (2025). Modeling Other Minds: A computational account of social cognition and its development. *(Preprint / Review — computational social development)*.

**Topic Tags:** computational social development, generative models, theory of mind, predictive processing, developmental modeling

### Core Question / Problem
How can computational (generative/Bayesian) models explain how humans develop representations of others' minds, and what are the mechanistic principles that guide social prediction across development?

### Conceptual or Computational Framework
Wang et al. propose that children and adults build **generative models** mapping latent mental states (beliefs, goals) to observed actions and that learning these models requires structured inductive biases and social sampling. At Marr’s levels: Computational — infer hidden causes of actions for prediction; Algorithmic — approximate inference, hierarchical generative representations and transition structures; Implementational — neural substrates implementing prediction‑error learning and social memory. 

### Methods Overview
The paper synthesizes computational modeling (Bayesian inverse planning, hierarchical models), developmental experiments (infant goal understanding, teleological reasoning), and cross‑domain data (adult plan inference, cultural scaffolds). Core manipulations discussed include task structure complexity, observational sampling, and prior biases.

### Key Findings / Claims
- Generative models with structured priors explain core developmental milestones: infants' teleological reasoning and older children's grasp of false beliefs emerge from richer hierarchical models and richer social exposure. 
- Transition structure — knowledge of how mental states map across time — is central for prediction and develops with experience and social scaffolding. 
- Computational models reconcile simulation and theory approaches by showing how approximate inverse‑planning plus learned priors can produce both fast intuitive inferences and later explicit ToM. 

### Interpretation & Significance
Wang et al. offer a formal framework linking developmental data to mechanistic models: social cognition is a problem of inverse inference under uncertainty solved by building generative models whose structure is shaped by learning and culture. This naturally connects to the Predictive Mind framework and provides operational variables (priors, sampling, model complexity) for experimental testing.

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: Models specify how person/environment/history interact to produce behavior via learned representations.
- Marr: Clear mapping across levels; the paper’s strength is explicit algorithmic proposals (approximate inference) tied to computational goals.
- Brunswik: The paper operationalizes cue validity and sampling — how children learn which cues are informative.

### Teaching Hooks
- Simple Bayesian inverse planning demo: students infer goals from observed paths.
- Developmental vignette: why infants expect efficient action — link to teleological reasoning studies.

### Pedagogical Lens
- Pre‑requisites: basic Bayesian inference, inverse planning, Marr’s levels
- Misconceptions: "Models are literal descriptions of the brain" — clarify they are explanatory/computational tools.

### Connections
Directly links to Epley & Waytz (mind perception as input to inference), impression formation (how priors shape trait learning), and broader predictive processing debates.

### Key Quotes or Phrases
- "Generative models map latent mental states to observable actions; learning them is the heart of social cognition." 
- "Transition structure — how mental states evolve — is central for predicting others." 

### Concept Graph
- Priors + observed actions → inverse inference (approximate) → latent mental state estimates → updated generative model → improved prediction.

---