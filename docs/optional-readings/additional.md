# Additional

## 2005 — Augusto, L. M. (2005). Review: Symbols and Knowledge Systems. *Journal of Knowledge Structures & Systems.*

**Full Citation:** Augusto, L. M. (2005). Review: Symbols and Knowledge Systems. *Journal of Knowledge Structures & Systems* (review/overview).

**Topic Tags:** Symbolic Processing, Physical Symbol System, Representation, Newell & Simon Test, Information Processing Languages

### Core Question / Problem
What role do symbolic representations and symbolic systems play in modeling cognition? The review surveys historical and conceptual roots of symbolic processing, the architecture of symbolic systems (memory, control, operators), and criteria for when symbolic representations are an appropriate model of cognition.

### Conceptual or Computational Framework
The paper sits at the computational/algorithmic tradition of cognitive science (Newell & Simon, physical symbol system hypothesis). It treats cognition as symbol manipulation implemented via programming languages and control architectures (e.g., IPL, GPS). At Marr’s levels: computationally the goal is to explain human problem solving and high‑level cognition; algorithmically the mechanisms are symbolic operators acting over structured representations (lists, trees); implementationally these can be instantiated in software or neural hardware but the focus is on formal criteria for symbolic adequacy.

### Methods Overview
This is a conceptual review synthesizing historical sources (Newell & Simon, IPL, GPS), formal discussions of representation and interpretation, and proposed evaluation criteria (e.g., the Newell & Simon Test). No novel experimental data; evidence is drawn from classic program demonstrations (e.g., GPS proofs, theorem provers, planning programs) and comparative arguments about expressivity and interpretable operations.

### Key Findings / Points
- Symbolic systems (SS) are characterized by explicit memory, control structures, operators, and interpretable symbol tokens; IPL is an early practical language for such systems. 
- The authors argue for explicit criteria (the Newell & Simon Test) to judge theories of cognition by their ability to express and operate on symbolic structures—arguing this is a higher bar than the Turing Test for claims about cognitive adequacy. 
- Symbols offer "distal access": they connect concrete perceptual patterns to abstract, manipulable representations enabling compositionality and generalization. The review highlights tradeoffs between symbolic expressivity and implementation cost.

### Interpretation & Significance
For students of cognitive science, the review clarifies why symbolic architectures dominated early computational models: they provide transparency (interpretable operators), compositionality (build complex structures from parts), and a language for reasoning about representations. This matters in social cognition because symbolic vs. statistical/connectionist approaches imply different assumptions about representation, learnability, and the kinds of inferences an agent can make (e.g., rule‑based attribution vs. learned predictive transitions).

### Computational‑Social‑Cognitive‑Scientist Hat
- Kurt Lewin: symbolic models reframe internal representations (R) as explicit computational tokens mediating B = f(P, E, R).\
- David Marr: paper focuses on algorithmic machinery (representations + operators) and asks whether symbolic architectures match the computational goal of human reasoning.\
- Egon Brunswik: would press for evaluation of symbolic models against ecological validity—do they capture probabilistic transition statistics humans use?

### Connections
Connects to Representations, Marr’s Levels, the Physical/Design/Intentional stances (how much structure should be assumed), and debates between symbolic vs. statistical models of social prediction.

### Key Quotes or Phrases
- "Symbolic systems provide compositional representations and operators that make abstract reasoning tractable."\
- "The Newell & Simon Test asks whether a theory can express and manipulate the structures it claims to explain."

### Concept Graph
- Symbolic tokens + Operators → compositional reasoning.\
- IPL / GPS implementations → historic demonstrations of symbolic adequacy.\
- Newell & Simon Test → evaluation criterion for cognitive theories.
  - **Newell & Simon Test:** A set of practical criteria for evaluating whether a theory of cognition can adequately express and operate on the symbolic structures it posits (a stronger test than the Turing test for claims about cognitive architectures). **Notable Figures:** A. Newell, H. A. Simon. **Related Concepts:** Physical Symbol System; Representation.
  - **Symbolic System (SS):** A canonical architecture composed of Memory, Control, Input/Output, and Operators (Assign, Copy, Read, Write, Do, Continue‐IF, Quote, Behave). Serves as a template for testing symbolic theories. **Notable Figures:** Newell & Simon. **Related Concepts:** IPL, GPS.

---











## 2013 — Clark, A. (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behavioral and Brain Sciences.*

**Full Citation:** Clark, A. (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. *Behavioral and Brain Sciences*.

**Topic Tags:** predictive processing, generative models, action-oriented processing, representation, Marr's levels

### Core Question / Problem
Can a unified, action-oriented predictive processing framework (hierarchical generative models minimizing prediction error) plausibly explain perception, action, attention, and higher-level cognition, and if so, what are its limits?

### Conceptual or Computational Framework
Clark advances an **action-oriented predictive processing** framework: the brain implements hierarchical generative models that predict lower-level inputs; prediction errors update models and guide action (active inference). This sits squarely at Marr’s computational level (goal: minimize surprisal/prediction error), provides algorithmic proposals (hierarchical predictive coding, precision-weighted prediction errors), and points toward implementational hypotheses (neural circuits carrying prediction and error signals). 

### Methods Overview
This is a synthetic, theoretical target article. Clark evaluates computational models (Bayesian generative models, predictive coding), surveys empirical phenomena (bi-stable perception, attention, sensory integration), and integrates prior computational neuroscience (Friston, Rao & Ballard) and philosophical debate on enactivism and embodiment.

### Key Findings
- Predictive architectures offer a **unifying explanatory skeleton** that brings perception, action, and attention into a single family of processes driven by prediction-error minimization. 
- Action can be cast as a form of prediction (proprioceptive predictions) that changes the world to fit predictions (active inference).
- The framework scales to explain diverse phenomena (receptive field effects, cue integration, bi-stable perception) while connecting to neural implementation hypotheses (precision-weighting as a proxy for attentional gain). 
- Clark highlights **open challenges**: how far can these models extend to high-level reasoning, imagination, and culturally scaffolded human thought? What is the distribution of explanatory weight between low-level Bayesian machinery and socio-cultural scaffolding? 

### Interpretation & Significance
Clark’s paper reframes classical distinctions: perception ≈ inference; action ≈ prediction-driven sampling; attention ≈ precision-weighting. The major significance for social cognition is that **predictive architectures provide concrete machinery** for anticipating others — linking generative models of agents’ actions to mentalizing and ToM. Clark also insists the story must be hybridized with embodied, situated, and socio-cultural accounts to explain uniquely human cognition.

### Computational–Social–Cognitive–Scientist Hat
- Lewin: B = f(P,E) updated: add R (representations) that embody expectations and scaffold action. Clark’s emphasis on environmental structuring echoes Lewin’s life-space shaping.
- Marr: computational goal is minimization of surprisal/prediction error; algorithmic level = hierarchical generative models; implementational level = precision-weighted neuronal signaling. 
- Brunswik: statistical structure of the environment matters — Clark emphasizes sensitivity to environmental statistics and path-dependence in human environments. 

### Connections
- Links to Hohwy’s formal account of PEM (Predictive Error Minimization) and empirical work on social prediction (Tamir & Thornton).
- Provides mechanistic glue between representation-focused cognitive science and embodied/situated cognition.

### Key Quotes or Phrases
- “Action-oriented predictive processing models promise to bring cognition, perception, action, and attention together within a common framework.” 
- “Believing and perceiving, although conceptually distinct, emerge as deeply mechanically intertwined.” 

### Concept Graph
- Generative model → predicts sensory input → prediction error drives model update.
- Precision-weighting → modulates influence of prediction error → implements attention.
- Action (active inference) → changes sensory input → reduces prediction error.

---

## 2013 — Hohwy, J. (2013). The Predictive Mind. *Oxford University Press.*

**Full Citation:** Hohwy, J. (2013). *The Predictive Mind* (excerpts/analysis). (uploaded as Howy - PredictiveMind.pdf)

**Topic Tags:** prediction error minimization (PEM), content vs covariance, perception as hypothesis testing, binding, misperception

### Core Question / Problem
What is the best philosophical and computational framing to explain perception as prediction-error minimization (PEM), and does PEM deliver truth-tracking (content) or only covariance-based regularities?

### Conceptual or Computational Framework
Hohwy argues PEM/Hierarchical Predictive Coding offers a principled account: perception and action serve to minimize surprisal via top-down predictions and bottom-up error signals. The account presses philosophical questions about **representational content** (how covariance becomes content) and practical worries about self-fulfilling prophecies and the limits of PEM. 

### Methods Overview
Philosophical analysis grounded in computational neuroscience—evaluates formal PEM proposals, engages with counterexamples (illusory binding, misperception), and examines implications for content, truth, and the organism’s phenotype.

### Key Findings
- PEM explains many perceptual phenomena and provides a tight computational story for learning and perception (prediction and precision control). 
- Important **philosophical problems remain**: linking statistical covariance (what PEM naturally provides) to representational content (truth-value) — the “Hard Problem of Content.” Without this bridge, PEM explains why some percepts are statistically unusual but not necessarily why they are false. 
- Hohwy acknowledges constraints (phenotype, expected states) that stop the system collapsing into pathological self-fulfilling strategies (e.g., hiding in dark rooms). 

### Interpretation & Significance
Hohwy’s book sharpens predictive-processing into a philosophically rigorous theory—one that is computationally powerful but faces meta-theoretical issues about content. For social cognition, the content problem matters: attributing beliefs/desires (ToM) requires contentful representations, so PEM proponents must show how social content arises from covariance-based learning.

### Computational–Social–Cognitive–Scientist Hat
- Lewin: PEM provides mechanistic form to “life space” priors (R) that bias behavior.
- Marr: PEM gives computational goals (minimize surprisal) and algorithmic sketches (hierarchical inference), but implementational claims must still be empirically validated.
- Brunswik: highlights the role of environmental informational covariance; Hohwy questions whether covariance suffices for content. 

### Connections
- Directly connects to Clark (2013) on action-oriented predictive processing and to empirical attempts to link precision-weighting to attention.

### Key Quotes or Phrases
- “PEM is what enables creatures like us to hone and refine our internal models or representations about the world.” 
- “If covariance and content are logically distinct, then it is not obvious that mirrors do in fact have any contentful properties.” 

### Concept Graph
- Prediction (generative model) → Prediction error → Model update (learning)
- Phenotype constraints → restrict self-fulfilling minimization strategies
- Covariance vs Content tension → philosophical challenge for PEM

---

## 2013 — Uleman, J. S., & Kressel, L. (2013). A brief history of theory and research on impression formation. *The Oxford Handbook of Social Cognition.*

**Full Citation:** Uleman, J. S., & Kressel, L. (2013). A brief history of theory and research on impression formation. *(Annual Review / Social Cognition review chapter)*.

**Topic Tags:** impression formation, person perception, attribution, heuristics, warmth/competence

### Core Question / Problem
How do perceivers form stable impressions from limited behavioral data, what representational structures support impressions (e.g., trait inference, schema), and how have theories evolved historically?

### Conceptual or Computational Framework
Uleman & Kressel trace impression formation from trait averaging and associative network models to modern constructive frameworks emphasizing schemata and predictive representations. Map: Computational (goal = accurate social inference and memory efficiency), Algorithmic (representations: trait nodes, schemas, associative weights), Implementational (memory systems, attention).

### Methods Overview
This review synthesizes decades of laboratory paradigms: trait inference tasks, spontaneous trait transference, person memory paradigms, and comparative judgments across individuals and groups. Key manipulations include exposure content (behavior descriptions), trait diagnosticity, and context (semantic priming, group stereotypes).

### Key Findings
- Impression formation exhibits regularities: two fundamental evaluative dimensions (warmth/competence) robustly structure judgments across targets and contexts. 
- Schemas and associative networks explain many ordering and memory effects: perceivers use prior knowledge to fill gaps and generate stable trait impressions even from sparse data. 
- Perceiver goals, attention, and social visibility modulate accuracy vs bias: reputations are more accurate for well‑known targets; for unfamiliar targets, prior theories drive impressions. 

### Interpretation & Significance
The paper situates impression formation as both adaptive (fast, memory‑efficient) and error‑prone (biases from priors and schemas). For computational social cognition, it highlights the need to model how priors, evidence sampling, and representational compression trade off accuracy for efficiency — a classic rational analysis problem.

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: Impression = R in B = f(P,E,R) — internal "life‑space" encoding of others.
- Marr: Algorithmic focus on how trait‑based or schema representations map behaviors to predictions.
- Brunswik: Stresses ecological validity — cue reliability matters for accurate impressions.

### Connections
Links to mind perception (pre‑attributional stages), stereotyping research, and predictive processing via priors/schemas.

### Key Quotes or Phrases
- "Two fundamental dimensions — warmth and competence — keep reappearing in impressions of both individuals and groups." 
- "Reputations are more accurate for well‑known individuals; for less‑known targets, prior theories dominate." 

### Concept Graph
- Observed behaviors → trait inference (diagnostic weighting) → memory/schema updating → predicted future behavior.

## 2018 — Kriegeskorte, N., & Douglas, P. (2018). Cognitive computational neuroscience. *Nature Neuroscience.*

**Full Citation:** Kriegeskorte, N. & Douglas, P. (2018). Cognitive computational neuroscience. *Nature Neuroscience*.

**Topic Tags:** computational neuroscience, representational models, deep neural networks, Marr's levels, task-performing models

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

### Connections
- Links to Predictive Mind (generative models), Marr’s levels, and modern debates about interpretability of large models.

### Key Quotes or Phrases
- “What I cannot create, I do not understand.”  
- “Task‑performing computational models that explain how cognition arises from neurobiologically plausible dynamic components will be central to a new cognitive computational neuroscience.”

### Concept Graph
- Task design → model training → neural representation similarity → behavioral prediction.
- Cognitive model (top-down) ↔ neural implementation (bottom-up) — both constrain each other.

---

## 2023 — Wheatley, T., Thornton, M. A., Stolk, A., & Chang, L. J. (2023). The Emerging Science of Interacting Minds. *Perspectives on Psychological Science.*

**Full Citation:** Wheatley, T., Thornton, M. A., Stolk, A., & Chang, L. J. (2023). The emerging science of interacting minds. *Perspectives on Psychological Science: A Journal of the Association for Psychological Science.* https://doi.org/10.1177/17456916231200177  

**Topic Tags:** Interacting Minds; Synchrony; Mutual Prediction; Neural Coupling; Cross-Modal Dynamics; Representation

### Core Question / Problem
How should cognitive science conceptualize and study *interacting minds* — cognition that arises in real-time social interaction — and what computational and neural mechanisms support interpersonal coordination, synchrony, and shared meaning?

### Conceptual or Computational Framework
The authors synthesize dynamical-systems (coupled oscillators, synchrony), predictive-processing (mutual prediction, joint error minimization), and representation-level accounts (shared representations, representational alignment). Mapped to Marr: (a) Computational — coordinate behavior and communication; (b) Algorithmic — predictive loops, phase-locking, cross-modal alignment; (c) Implementational — inter-brain coupling measurable with hyperscanning and shared representational patterns in social brain areas.  

### Methods Overview
Review integrates behavioral synchrony tasks, musical/movement naturalistic stimuli, computational models (coupled oscillators), and neuroimaging hyperscanning (EEG/fMRI) plus multivariate representational analyses and causal perturbations.

### Key Findings / Synthesized Insights
- **Synchrony as mechanism:** temporal alignment across behavior, physiology, and neural signals supports affiliation and smoother prediction.  
- **Mutual prediction:** reciprocal generative models (each agent predicts the other) can produce spontaneous alignment.  
- **Cross-modal codes:** movement and music share dynamic structures facilitating cross-modal emotion/action understanding.  
- **Neural coupling:** hyperscanning shows interbrain synchrony correlates with cooperative success and shared meaning; representational alignment occurs in social brain regions.

### Interpretation & Significance
The review reframes social cognition as an emergent, interactive phenomenon: cognition arises from coupling across agents, implying new computational goals (e.g., minimize joint prediction error) and methods (hyperscanning, naturalistic interaction tasks). It argues for importing dynamical systems and control theory tools into social cognitive science.  

### Computational-Social-Cognitive-Scientist Hat
- **Lewin:** person-in-environment dynamics fit a Lewinian life-space perspective.  
- **Marr:** pushes for clear computational goals for interaction (joint error minimization) and algorithmic proposals mapping to measurable signals.  
- **Brunswik:** asks about ecological cue validity for interaction cues — the review addresses this with cross-modal/synchrony evidence.  

### Connections
Ties to Predictive Mind, Biological Motion (as interaction cue), Cross-Modal Dynamics, and empirical synchrony literature (e.g., Sievers et al., Wheatley et al. 2012).  

### Key Quotes or Phrases
- “Interaction is not simply two isolated minds added together — it is an emergent process of coupling.”  

### Concept Graph
Action timing ↔ partner prediction (aligned timing reduces mutual prediction error); Cross-modal dynamics → shared meaning; Neural coupling ↔ behavioral synchrony.

### Relevant Terms
**Existing Terms Used:** Synchrony; Predictive Mind; Cross-Modal Dynamics; Representation.  

---


## 2025 — Carvalho, F., & Lampinen, A. (2025). Naturalistic computational cognitive science: Models and theories that capture the full range of natural behavior. *Preprint.*

**Full Citation:** Carvalho, F. & Lampinen, A. (2025). Naturalistic computational cognitive science: Models and theories that capture the full range of natural behavior. *(Uploaded PDF).*

**Topic Tags:** naturalistic tasks, ecological validity, computational models, shared datasets

### Core Question / Problem
How should computational cognitive science evolve to explain real‑world behavior rather than constrained laboratory tasks? The authors argue for methods and models that embrace naturalistic data and testing regimes.

### Conceptual or Computational Framework
A synthesis arguing for the combination of (i) generative models that capture causal, compositional structure, (ii) scalable learning algorithms (amortized inference, meta‑learning), and (iii) experimental designs that collect continuous, multimodal behavior in rich environments. Marr’s levels motivate aligning computational goals with implementational constraints to maintain plausibility.

### Methods Overview
Recommendations include deploying virtual reality and continuous recording (video, motion, physiology), leveraging large‑scale annotated datasets, using hierarchical Bayesian and neural‑hybrid models, and developing benchmark tasks/test suites shared across labs.

### Key Findings / Proposals
- Naturalistic data expose representational demands (temporal structure, multi‑agent dynamics) that small lab tasks cannot.
- Hybrid models (neural networks with structured generative cores) are promising: they combine representational flexibility with inductive structure for sample‑efficient learning.
- Methodologically, the field needs open benchmarks, standardized tasks, and adversarial cooperation across labs (sharing tasks/data/models/tests).

### Interpretation & Significance
This paper operationalizes the “big data + big models” vision for cognitive science, emphasizing reproducibility and ecological validity. For social cognition, its approach directly supports studying dynamic mentalizing, multi‑agent interaction, and cultural/contextual effects.

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: supportive of studying behavior as a function of life‑space dynamics in natural environments.
- Marr: would insist on precise computational goals and testable predictions despite ecological complexity.
- Brunswik: would welcome the multimodal, probabilistic sampling approach to environmental cues.

### Connections
- Bridges Predictive Mind, Flatland Fallacy critique, and Kriegeskorte et al.’s call for task‑performing models.

### Key Quotes or Phrases
- “To explain natural behavior we must meet naturalistic data on its own terms: temporally rich, multimodal, and socially structured.”

---