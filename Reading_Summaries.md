# Paper Summaries

_Key-points and high-level summaries of papers mentioned in lecture or included in optional-readings on Canvas_

---

## 1944 — Heider, F., & Simmel, M. (1944). An Experimental Study of Apparent Behavior. *Journal of Psychology.*

**Full Citation:** Heider, F., & Simmel, M. (1944). *An Experimental Study of Apparent Behavior.* Journal of Psychology.

**Topic Tags:** Attribution theory, Animacy, Intentional stance

### Core Question / Problem
How do simple motion cues (shapes moving on a screen) provoke attributions of intentional action, social motives, and personality — i.e., when do observers treat abstract motion as “agents”?

### Conceptual or Computational Framework
Heider & Simmel operationalize the perceiver as a naïve scientist who infers internal states (beliefs, desires, intentions) from minimal perceptual input. At Marr’s levels: computationally, the problem is “infer causes (agents, goals) from motion”; algorithmically, it is mapping kinematic patterns to intentional explanations; implementational details are left unspecified.

### Methods Overview
Participants watched a short silent film showing geometric shapes (triangles, circle, rectangle) moving in a simple 2-D arena. They were asked to describe what they saw in their own words. The key manipulation is purely perceptual: only motion and spatial relations vary.

### Key Findings
- Nearly all observers provided narrativized, agentic descriptions (e.g., “the big triangle chased the little one to punish it”), attributing goals, beliefs, and social roles to geometric shapes.
- Motion patterns (self-propulsion, contingent interaction, approach/avoidance, goal-directed trajectories) reliably trigger attributions of animacy and intentionality.
- Observers spontaneously create causal and moral narratives from minimal cues.

### Interpretation & Significance
Heider & Simmel provide a clear demonstration that perception alone can trigger high-level social inferences. The study shows that agency detection and mentalizing are fast, automatic, and driven by diagnostic motion signatures — a foundational result for research on animacy perception, mentalizing, and the intentional stance.

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: B = f(P, E, R) — This shows how perceptual input P (motion) combined with prior Representations (R: schemas about agents) shapes behavior (attribution).
- Marr: Computational goal = infer hidden agents/goals; algorithmic = mapping motion features → intentional explanation; implementational = unspecified.
- Brunswik: Emphasizes ecological validity — motion cues are probabilistic signals of agency and the perceiver uses ecological sampling (available cues) to infer hidden causes.

### Teaching Hooks
- Show short clips from the original animation and ask students to write 2‑sentence narratives; compare across students.
- Live demo: Two dots move contingently vs. randomly; ask students “Which is alive?” and discuss why.

### Pedagogical Lens
- Pre‑requisites: basic idea of attribution and agency
- Common misconceptions: “Attribution requires rich cues” — Heider & Simmel show minimal cues suffice.
- Discussion prompt: What motion features would an algorithm use to decide “agent” vs “object”?

### Connections
- Links to animacy literature, biological motion (Johansson), and predictive‑processing accounts where small prediction errors about self‑propelled motion trigger agent hypotheses.

### Key Quotes or Phrases
- “Observers impose intentions and social roles on moving shapes.”  
- “Motion alone is sufficient to elicit richly structured social narratives.”

### Concept Graph
- Motion cues (self‑propulsion, contingency) → Animacy detection → Intentional stance → Mentalizing (goal/trait attributions)

---

## 1971 — Dennett, D. C. (1971). Intentional Systems. *The Journal of Philosophy.*

**Full Citation:** Dennett, D. C. (1971). Intentional Systems. *The Journal of Philosophy* / collected essays.

**Topic Tags:** intentional stance, design stance, physical stance, intentional systems, rationality, heuristics

### Core Question / Problem
What does it mean to treat systems (organisms, machines) as having beliefs and desires — and how useful is that strategy for explanation and prediction?

### Conceptual or Computational Framework
Dennett defines an Intentional System as any system whose behavior can be predicted by ascribing beliefs, desires, and rationality. He contrasts three explanatory stances: Physical (laws), Design (function), and Intentional (attributing mental states). The intentional stance is a heuristically powerful, stance‑level algorithm for prediction. Map to Marr: computational level = predicting behavior; algorithmic level = adopting a stance (rule set for ascription); implementational level = physical/biological substrate (irrelevant to stance validity).

### Methods Overview
Philosophical analysis and illustration (AI/chess, game theory, Skinner’s behaviorism counterexamples). Dennett uses thought experiments and cross‑disciplinary examples (economics, AI) to show how intentional descriptions simplify complex design problems.

### Key Findings
- Intentional characterization is useful even for non‑biological systems (chess programs) and yields genuine predictive power without needing metaphysical claims about consciousness.
- Treating agents as rational approximators explains why economics and game theory succeed even if psychology must explain that rationality.
- The concept is "uncluttered" — it avoids metaphysical commitments and focuses on predictive/organizational utility.

### Interpretation & Significance
Dennett offers a pragmatic account: intentionality as a tool, not a metaphysical property. For social cognition, this legitimizes mental‑state attribution as an adaptive predictive strategy (aligns with course’s Intentional Stance entry). It also explains cross‑disciplinary borrowings (AI, economics) where intentional terms function as useful heuristics. 

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: Intentional ascription is a representational heuristic within the life‑space affecting behavior prediction.
- Marr: Intentional stance sits at an algorithmic/heuristic level for social prediction.

### Teaching Hooks
- Use chess programs and thermostats to show when intentional attributions help/hinder prediction.  
- Contrast with Searle’s Chinese Room (see the Précis commentary) to spark debate about "real" intentionality.

### Pedagogical Lens
- Prereqs: Familiarity with basic philosophy of mind and attribution theory.
- Misconceptions: That ascribing beliefs requires consciousness.

### Connections
- Directly connects to Intentional Stance, Design Stance, Mentalizing, and Generative Models in the glossary. 

### Key Quotes or Phrases
- "The concept of an Intentional system is a relatively uncluttered and unmetaphysical notion."

### Concept Graph
- System complexity → choice of stance (physical/design/intentional) → prediction accuracy.

---

## 1973 — Johansson, G. (1973). Visual Perception of Biological Motion and a Model for Its Analysis. *Perception & Psychophysics.*

**Full Citation:** Johansson, G. (1973). Visual Perception of Biological Motion and a Model for Its Analysis. *Perception & Psychophysics*, 14(2), 201–211.  

**Topic Tags:** Biological Motion; Animacy; Perceptual Grouping; Vector Analysis; Representation

### Core Question / Problem
How can observers recover rich information about biological actions (walking, running, dancing) from extremely sparse motion signals (point-light displays), and what computational principles might the visual system use to perform this inference?

### Conceptual or Computational Framework
Johansson proposes a **visual vector-analysis** approach: the proximal motion field is decomposed into common (global/translatory) and residual (pendular/rotational) motion components; grouping is achieved by pooling elements that share equal motion components. Framed by Marr’s levels: (a) Computational — infer distal biological motion type from proximal motion; (b) Algorithmic — hierarchical vector decomposition and grouping; (c) Implementational — hypothesized low-level perceptual machinery (unspecified neural substrate).

### Methods Overview
Experimental manipulations use point-light displays (typically 10–12 joint markers, variants with as few as 5), transformations that add/subtract global motion components, and controlled perturbations (rotations, phase shifts). Measures include rapid recognition, verbal descriptions, and forced-choice identification by naive observers viewing brief sequences.

### Key Findings
- Sparse point-light configurations robustly evoke vivid impressions of human actions; observers identify actions quickly and reliably.  
- Recognition remains rapid (<1 s) and resilient to large manipulations of common motion components, supporting an automatic decomposition process.  
- Vector-analysis principles (subtract common components to reveal residual pendular/rotational motion) explain perception of articulated limbs and gait.  
- Even very minimal displays (≈5 points) can suffice for reliable identification — kinematic relations (phase, pendular timing) carry the bulk of information.

### Interpretation & Significance
This paper established point-light biological motion as a foundational paradigm for social perception: motion alone carries rich cues to animacy, action type, and identity. Johansson’s geometric-kinematic account emphasizes lawful, proximal computations that recover distal structure, seeding decades of work on biological motion, animacy detection, and neural substrates (e.g., STS/pSTS).

### Computational-Social-Cognitive-Scientist Hat
- **Lewin:** motion is ecologically valuable — life-space dynamics provide critical social information.
- **Marr:** applauds the explicit algorithmic account (vector decomposition) but asks for formal representation and error metrics.
- **Brunswik:** highlights which kinematic relations are reliable cues (phase, constant lengths) and how the system might weight them.

### Teaching Hooks
- Show classic point-light walker clips and ask students to name the action before revealing the source. 
- Demonstration: remove global translation and show residual pendular motion to illustrate decomposition.

### Pedagogical Lens
- **Conceptual difficulty:** 2–3/5.  
- **Pre-reqs:** basic motion perception, Gestalt grouping (common fate), central-projection geometry.  
- **Exam prompt:** Explain how subtracting a common motion component reveals pendular residuals that support limb perception.

### Connections
Links to Animacy, Mentalizing (motion cues can trigger social attributions), and Predictive Mind (motion provides input for forecasting actions). 

### Key Quotes or Phrases
- “10–12 such elements in adequate motion combinations evoke a compelling impression of human walking.” 

### Concept Graph
Joint-motion phase relations → perceived gait; Common-component subtraction → residual limb oscillation → animacy inference.

### Relevant Terms
**Existing Terms Used:** Biological Motion; Animacy; Perceptual Grouping; Representation. 

---

## 1978 — Premack, D., & Woodruff, G. (1978). Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences.*

**Full Citation:** Premack, D., & Woodruff, G. (1978). Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences*.

**Topic Tags:** theory of mind (ToM), mentalizing, comparative cognition, experimental logic

### Core Question / Problem
Can non-human primates (chimpanzees) attribute mental states (beliefs, desires, intentions) to others — i.e., do they possess a theory of mind?

### Conceptual or Computational Framework
Premack & Woodruff frame ToM as an ability to infer hidden mental states from observed behaviour and situational context. Experimentally, they probe whether chimps can predict another agent’s behavior based on the agent’s (possibly false) beliefs — a classic computational question about representing other minds.

### Methods Overview
Longitudinal/descriptive experimental paradigms: observational reports and structured tasks where chimpanzees interact with informed or uninformed trainers separated by mesh partitions; senders and receivers manipulate signals to test whether chimpanzees understand others’ knowledge states. 

### Key Findings
- Evidence suggested some chimpanzees could flexibly use information about another’s knowledge or intention (e.g., pointing strategies to inform a benevolent trainer or to deceive a selfish one).
- Results were suggestive but not definitive; Premack & Woodruff urged more controlled tests (e.g., false-belief style tasks) to settle whether chimp performance reflects mindreading or sophisticated behavioral reading. 

### Interpretation & Significance
Premack & Woodruff’s paper launched ToM as an empirical question and a research program. It reframed comparative cognition: rather than assuming human uniqueness, it asked what computational representations (if any) animals use to predict others. The paper set the stage for decades of follow-ups that refined tasks (false-belief tasks, looking-time measures) and clarified species differences.

### Computational–Social–Cognitive–Scientist Hat
- Lewin: behavior depends on person and environment; Premack’s tasks manipulated informational environments to reveal internal representations.
- Marr: computational goal = predict other’s behavior; algorithmic question = what representations/operations support this? Implementational = neural substrates across species.
- Brunswik: stresses ecological validity — animal tests must respect natural communicative contexts (senders/receivers).

### Teaching Hooks
- Recreate the sender-receiver experimental logic in class: students act as trainers with/without knowledge to see how others signal.
- Contrast Premack’s paradigms with infant false-belief tasks to show methodological evolution.

### Pedagogical Lens
- Pre-requisites: experimental logic, basic representational thinking
- Common misconceptions: early positive claims = definitive proof of ToM in chimps — clarify nuance and need for replication and stricter controls
- Discussion prompt: Design a modern controlled test (nonverbal) that would distinguish behavioral-reading from belief-attribution in chimpanzees.

### Connections
- Directly ties to the course glossary’s ToM entry (Premack & Woodruff 1978) and subsequent human infant literature. 

### Key Quotes or Phrases
- “The test is quite simple.” (description of sender/receiver setup) — a good lecture vignette. 

### Concept Graph
- Observed behavior + context → inferred knowledge state → predictive behavior (sender/receiver strategy)
- Controlled manipulations → distinguish mentalizing vs behavior-reading

---

## 1992 — Fodor, J. A. (1992). A theory of the child's theory of mind. *Cognition.*

**Full Citation:** Fodor, J. A. (1992). A theory of the child's theory of mind. *Cognition*, 44, 283–296.

**Topic Tags:** theory of mind, development, false belief, heuristics, representation

### Core Question / Problem
Why do young children fail classic false‑belief tasks (around age 3) but pass related tasks that seem closely analogous? Is there a conceptual change (stage‑like revolution) in the child's folk‑psychology, or can performance be explained by the computational heuristics children use?

### Conceptual or Computational Framework
Fodor proposes a **heuristic**/resource‑based account rather than radical conceptual discontinuity. He frames two heuristics (H1, H2): H1 predicts actions from desires alone (simpler); H2 predicts from desires+beliefs (computationally costlier). Children prefer H1 when it yields a unique prediction and resort to H2 only when H1 is underdetermined. This accounts for why 3‑year‑olds fail classic false‑belief tasks but succeed on some related paradigms.

### Methods Overview
Fodor reviews classic paradigms (Sally‑Anne false belief, deception, appearance‑reality, Polaroid/photograph tasks) and draws on variants and controls that tease apart whether children lack the concept of belief or merely prefer cheaper heuristics. He proposes experimental variants that would adjudicate his account (e.g., multi‑container division, object disappearance, not‑own belief with feedback manipulations).

### Key Findings / Arguments
- Empirical dissociations (children passing deception or appearance‑reality tasks yet failing false‑belief tasks) challenge strong claims that children lack any representation of belief.
- A heuristic ordering account parsimoniously predicts observed behavior without invoking radical conceptual change: children compute using H1 by default and invoke H2 selectively.
- Fodor generalizes the idea via markedness: adult representations normally have an "unmarked" (true) value; children exploit this and only deploy belief‑sensitive strategies when required by task constraints.
- The account yields precise, testable predictions and a set of experimental manipulations that should differentially affect 3‑ vs 4‑year‑olds.

### Interpretation & Significance
Fodor's paper reframes developmental ToM failure as a tradeoff between computational cost and predictive reliability rather than an all‑or‑none conceptual leap. This supports views that emphasize continuity (incremental tuning of heuristics and resources) and aligns with algorithmic‑level explanations (how children represent and compute), more than metaphysical claims about conceptual possession.

### Computational‑Social‑Cognitive‑Scientist Hat
Fodor's heuristics map naturally onto bounded‑rationality models and resource‑rational accounts: limited working memory / representational bandwidth favors reliance on simpler decision rules (H1) unless ambiguity forces recruitment of richer models (H2). This suggests computational models that implement priority ordering over inference rules with a cost function for representational complexity.

### Teaching Hooks
- Run the classic Sally‑Anne demo and then a multi‑container variant to show how task framing changes predicted performance under H1/H2.
- Classroom debate: Is development driven more by representational capacity or by heuristic strategy selection?

### Pedagogical Lens
Use Fodor to introduce students to the difference between conceptual‑change theories and resource/heuristic accounts. Emphasize falsifiability via the experimental variants Fodor proposes.

### Connections
Links developmental ToM to bounded rationality, predictive mind ideas (selective deployment of complex generative models), and the broader debate (simulation vs. theory‑theory).

### Key Quotes or Phrases
- "All that happens is that the trade‑off between predictive reliability and computational complexity increasingly favors the former as computation space gets cheaper."

### Concept Graph
- Heuristic ordering → developmental performance differences
  - **H1 (Desire heuristic):** predict action from desires alone when unique. **Related Concepts:** Simple desire psychology, bounded rationality.
  - **H2 (Belief+Desire heuristic):** incorporate beliefs when H1 is underdetermined. **Related Concepts:** False belief, metarepresentation.

### Relevant Terms
- **Existing Terms Used:** Theory of Mind, False‑Belief Task, Representation.

---

## 1999 — Frith, C. D., & Frith, U. (1999). Interacting Minds — A Biological Basis. *Science.*

**Full Citation:** Frith, C. D., & Frith, U. (1999). Interacting Minds—A Biological Basis. *Science*, 286, 1692–1695.

**Topic Tags:** mentalizing, theory of mind, STS, medial prefrontal cortex, development, autism

### Core Question / Problem
What are the neural and developmental foundations of mentalizing — the ability to represent other people's mental states — and how did this capacity evolve from perceptual and action‑representation systems?

### Conceptual or Computational Framework
Frith & Frith synthesize developmental psychology, neuropsychology, single‑cell and imaging data to propose a decomposed system for social cognition: (i) superior temporal sulcus (STS) and adjacent regions for detecting biological motion and representing others' actions; (ii) lateral inferior frontal/mirror‑system regions for action representation and goal inference; (iii) medial prefrontal/anterior cingulate regions for self‑related representations and the explicit reasoning about mental states (mentalizing). They interpret mentalizing as emerging from action systems rather than ventral object recognition modules.

### Methods Overview
The review integrates:
- Developmental paradigms (false‑belief/Sally‑Anne tasks; deception/sabotage).
- Neuroimaging (PET/fMRI) studies asking subjects to report on self or others' mental states.
- Single‑cell recordings in nonhuman primates (STS action‑selective cells; mirror neuron evidence in F5).
- Clinical dissociations (autism, schizophrenia, focal lesions).

### Key Findings
- Mentalizing has an identifiable developmental trajectory: joint attention in infancy → understanding pretense by ~18 months → reliable false‑belief reasoning by ~4 years.
- Autism shows selective deficits in early markers (joint attention, pointing, pretend play) and later in false‑belief tasks, suggesting specialized developmental disruption.
- Imaging converges on medial prefrontal regions and temporo‑parietal junction (TPJ) for mentalizing tasks; STS regions implicated in biological motion detection are adjacent to mentalizing activations.
- Single‑cell studies show STS neurons responsive to biological motion and to goal‑directed actions; mirror neurons in inferior frontal regions provide a putative substrate for mapping observed actions onto motor representations.
- Schizophrenia can show overactive or maladaptive mentalizing (delusional inference), implicating disturbances in the same networks (and interactions with executive functions).

### Interpretation & Significance
Frith & Frith argue mentalizing is neither wholly domain‑general nor magically human‑unique; rather, it builds on evolutionarily older action representation systems. The review frames social cognition as layered: perceptual detection of animate agents → action/goal parsing via mirror-like systems → explicit, self‑referential inferential processing in medial prefrontal cortex.

### Computational‑Social‑Cognitive‑Scientist Hat
Model mentalizing as hierarchical inference: low‑level detectors (biological motion filters) produce hypotheses about agents; mid‑level modules compute goal/intent representations via forward/inverse models (action ↔ goal mapping); high‑level modules run counterfactual simulations (beliefs about others' beliefs) and maintain self-other distinctions. This maps comfortably onto predictive‑processing accounts where prediction error at each level drives belief updating about agents' future actions.

### Teaching Hooks
- Use Sally‑Anne false belief demo with puppets; contrast with deception/sabotage tasks to highlight different computational demands.
- Show how STS responses to point‑light walkers (link to Troje) supply perceptual input to mentalizing.
- Discuss autism and schizophrenia as "failure modes" that illuminate system decomposition.

### Pedagogical Lens
Emphasize mechanistic decomposition (what each area contributes) rather than reifying "theory of mind" as a single module. Use developmental timelines to motivate computational cost and the heuristic vs. deliberative tradeoffs in children.

### Connections
Direct links to biological motion research (Troje), mirror neuron literature (Rizzolatti et al.), and predictive accounts of social cognition. Also relates to Dennett's Intentional Stance and debates about simulation vs. theory‑theory.

### Key Quotes or Phrases
- "The ability to 'mentalize' … depends on a dedicated and circumscribed brain system."
- "Our ability to mentalize seems to have evolved largely from the dorsal action system."

### Concept Graph
- Biological motion detection (STS) → Action/goal parsing (mirror/inferior frontal) → Mentalizing (medial PFC/ACC, TPJ).
  - **STS (biological motion):** detects animate movement; feeds goal inferences. **Notable Figures:** Oram, Perrett, Frith. **Related Concepts:** Point‑light displays; life detector.
  - **Medial PFC:** self‑state representation and explicit mental state reasoning. **Notable Figures:** Frith & Frith. **Related Concepts:** False‑belief reasoning; executive control.

### Relevant Terms
- **Existing Terms Used:** Mentalizing, Theory of Mind, Biological Motion, STS.

---

## 2001 — Blakemore, S.-J., & Decety, J. (2001). From the perception of action to the understanding of intention. *Nature Reviews Neuroscience.*

**Full Citation:** Blakemore, S.-J., & Decety, J. (2001). From the perception of action to the understanding of intention. *Nature Reviews Neuroscience*, 2(8), 561–574.

**Topic Tags:** Biological motion, Simulation theory, Forward models, Mentalizing, Theory of Mind

### Core Question / Problem
How do observers move from low-level perception of biological motion to high-level inferences about others' intentions? The review asks which perceptual and neural mechanisms allow humans (and other animals) to extract intentions from observed action sequences.

### Conceptual or Computational Framework
The paper synthesizes psychophysics, developmental studies, and neuroimaging under a simulation-forward‑model framework: observers internally simulate observed actions using motor representations (forward models) and map predicted sensory consequences to intentions. This sits at Marr's algorithmic/implementational interface: representations (motor plans, efference copies) + transformations (forward prediction) enable social inference.

### Methods Overview
This is a review—evidence synthesized includes: point‑light (Johansson) biological‑motion psychophysics, infant/developmental behavior showing early animacy detection, single‑cell and fMRI studies implicating the superior temporal sulcus (STS), inferior parietal regions, medial prefrontal cortex (mPFC), cerebellum and putative mirror‑system involvement (parietal / premotor circuits). Key paradigms: point‑light displays, Heider–Simmel animations, action observation vs execution contrasts, apparent‑motion manipulations, and imitation tasks.

### Key Findings
- Biological motion is processed as a special class of stimuli (point‑light displays) and drives automatic attributions of agency and intention.
- The posterior STS is reliably activated by biological motion; medial PFC and temporo‑parietal regions by mental‑state attribution. Motor areas (premotor cortex, inferior parietal lobule) and cerebellum are recruited during action observation, especially when imitation or prediction demands are high.
- Forward models (efference copy → predicted sensory consequences) provide a mechanism for distinguishing self‑caused from external events and can be co‑opted to estimate others' intentions by simulating their motor commands.
- Imitation and simulation offer both developmental scaffolding for ToM and a mechanistic route to infer goals from kinematic forms.

### Interpretation & Significance
Blakemore & Decety position the brain as a "simulating machine" where perception and action systems overlap to support mentalizing. Rather than a purely inferential, propositional ToM, social understanding can arise from embodied predictive computations grounded in sensorimotor representations. The review connects early emergence of animacy detection to later, higher‑order theory‑of‑mind circuitry, suggesting continuity between perception and abstract mental‑state reasoning.

### Computational‑Social‑Cognitive‑Scientist Hat
Formalizing the claims: the observer's generative model contains motor plans p(plan), a forward model f(plan) → predicted sensory trajectories, and a mapping from predicted trajectories to latent intentions. Reverse inference (Bayesian inversion) over plans given observed kinematics yields posterior beliefs about goals. This is compatible with Bayesian predictive frameworks and complements later "naïve utility" style models for goal inference.

### Teaching Hooks
- Demo: point‑light walker; ask students to infer sex, emotion, or intention from motion alone.
- Exercise: sketch a simple forward‑model pseudocode that maps a motor command to an expected trajectory and show how mismatch signals could update intention estimates.
- Discussion prompt: compare simulation (embodied) vs theory‑theory (propositional) routes to mindreading.

### Pedagogical Lens
Emphasize mechanism over chronology: students should grasp *how* motor representations could be repurposed for social inference (forward models + Bayesian inversion), not just that "mirror neurons = empathy." Use diagrams to show signal flow: observed kinematics → motor resonance → forward prediction → inference over goals.

### Connections
Links to Marr's levels (algorithmic: representations of motor plans; implementational: mirror‑system circuits), predictive coding frameworks, and developmental work on infants' goal attribution. Also complements computational Bayesian models that invert generative action models.

### Key Quotes or Phrases
- "The brain is a powerful simulating machine, designed to detect biological motion in order to extract intentions."

### Concept Graph
- Biological motion → triggers animacy detection → engages STS and motor representations.
  - **Forward model:** A predictive mapping from motor command to expected sensory consequences. **Notable Figures:** Wolpert, Miall. **Related Concepts:** Efference copy; Motor prediction.
  - **Simulation theory:** Represent other minds by generating similar processes in oneself. **Notable Figures:** Goldman. **Related Concepts:** Mirror system; Imitation.

### Relevant Terms
- **Existing Terms Used:** Biological Motion; Mentalizing; Intentional Stance; Theory of Mind; Representation; Predictive Mind.

---

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

### Teaching Hooks
- Show a simple GPS‑like problem (tower of Hanoi or logical deduction), then contrast with a modern neural learner solving the same problem—ask which is more interpretable and why.
- Diagram of a paradigmatic Symbolic System (Memory → Control → Operators → I/O) and walk through a toy operator (e.g., replace, copy).

### Pedagogical Lens
- Pre‑requisites: basic programming metaphors, representation vs. process, Turing machine familiarity\
- Common misconceptions: confusing symbolic manipulation with humanlike understanding; over‑generalizing the scope of symbolic models.\
- Exam prompt: "Describe the Newell & Simon Test and explain what it demands of a theory of cognition."

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

## 2005 — Saxe, R., & Wexler, A. (2005). Making sense of another mind: The role of the right temporo‑parietal junction. *Neuropsychologia.*

**Full Citation:** Saxe, R., & Wexler, A. (2005). Making sense of another mind: The role of the right temporo‑parietal junction. *Neuropsychologia*, 43(10), 1391–1399.

**Topic Tags:** RTPJ, Theory of Mind, Belief attribution, Mentalizing

### Core Question / Problem
What is the specific contribution of the right temporo‑parietal junction (RTPJ) to Theory of Mind? Saxe & Wexler review evidence that RTPJ plays a selective role in belief attribution (representing others' informational states) rather than more general social or attentional processes.

### Conceptual or Computational Framework
The authors argue for functional specialization: RTPJ implements computations required to represent others' beliefs (meta‑representations) — a clear mapping from cognitive function (belief‑attribution) to neural substrate.

### Methods Overview
Evidence comes from fMRI studies using false‑belief tasks, lesion case studies, and controlled contrasts separating belief reasoning from attentional/agency confounds.

### Key Findings
- RTPJ activation is reliably elicited by tasks requiring attribution of beliefs, especially when those beliefs diverge from reality.
- Adjacent regions implicated in attention, language, or perceptual processing do not share RTPJ's selective profile.
- Lesion and TMS studies suggest causal necessity: disrupting RTPJ impairs belief attribution.

### Interpretation & Significance
Saxe & Wexler sharpen the functional taxonomy of social brain regions. Identifying RTPJ's selective role supports computational modeling of ToM where a distinct module (or algorithmic process) computes meta‑representations of others' informational states.

### Computational‑Social‑Cognitive‑Scientist Hat
- Computational goal: infer other's epistemic state (what they believe).
- Algorithmic view: represent nested beliefs and update them based on perceived evidence.
- Implementation: RTPJ computes belief‑relevant conditional probabilities and supports perspective‑taking.

### Teaching Hooks
- Run through Sally‑Anne task and map which neural nodes are recruited when belief ≠ reality.
- Discuss how to design an fMRI contrast that isolates belief representation (control for attention, language).

### Connections
Directly connects to Mitchell (2009) on decomposing social cognition and to developmental false‑belief literature. It provides the neural anchor for belief computations in computational models.

### Concept Graph
- Belief attribution (RTPJ) → supports Theory of Mind.
  - **RTPJ:** Meta‑representational belief computations. **Notable Figures:** Saxe. **Related Concepts:** False‑belief; Mentalizing; Perspective taking.

### Relevant Terms
- **Existing Terms Used:** RTPJ, Theory of Mind, Mentalizing, False‑Belief Task.

---

## 2006 — Mitchell, J. P. (2006). Mentalizing and Marr: An information‑processing approach to the study of social cognition. *Brain Research.*

**Full Citation:** Mitchell, J. P. (2006). *Mentalizing and Marr: An information‑processing approach to the study of social cognition.* (Paper)

**Topic Tags:** Mentalizing, Marr's levels, Representations, Predictive mind

### Core Question / Problem
How can Marr’s levels (computational, algorithmic, implementational) be usefully applied to “mentalizing” — the process by which perceivers represent and predict others’ minds?

### Conceptual or Computational Framework
Mitchell argues for an information‑processing (Marr‑informed) view of mentalizing: (1) computational level—what is the goal? (infer beliefs, desires, likely actions); (2) algorithmic level—what representations / computations map observations to inferred mental states? (generative models, Bayesian inference, heuristics); (3) implementational level—how might these computations be realized neurally (mPFC, TPJ networks implicated). The paper bridges classic social cognition (attribution) with formal models (predictive/generative modeling).

### Methods Overview
The paper is theoretical and integrative: it reviews behavioral evidence, neuroimaging results, and computational proposals that instantiate Marr’s levels in social cognition research.

### Key Findings / Claims
- Mentalizing tasks can be decomposed cleanly by Marr’s levels, yielding clearer hypotheses and experimental designs.
- Algorithmic proposals include both explicit rule‑based mappings and probabilistic generative models that predict others’ behavior from latent mental states.
- Neural data suggest specialized circuitry but do not fully determine algorithmic format; multiple algorithms may be implemented by overlapping brain systems.

### Interpretation & Significance
Mitchell reframes social cognition as computational inference. This matters pedagogically: it offers students a systematic vocabulary (goals, representations, algorithms) and connects classical theories (Heider’s attribution) to modern predictive and Bayesian frameworks. It makes clear how one can design experiments to pit algorithmic hypotheses against each other.

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: R (representations) are central; B = f(P,E,R) fits naturally into Marr’s algorithmic level.
- Marr: Would applaud the explicit mapping of social goals (why infer mental states) to candidate algorithms (how).
- Brunswik: Would emphasize probabilistic cue‑validity and ecological sampling in building generative models.

### Teaching Hooks
- Small class activity: propose two algorithms (rule‑based vs Bayesian) to explain the same ToM dataset; what predictions differ?
- Figure: mapping of Marr’s three levels onto a simple false‑belief task.

### Pedagogical Lens
- Pre‑requisites: basic probability / Bayesian intuition, Marr’s levels
- Common misconceptions: conflating neural localization with algorithmic explanation.
- Exam prompt: Compare two algorithmic accounts of mentalizing and propose a critical experiment.

### Connections
- Links explicitly to predictive processing, generative models, and neuroimaging work on mPFC/TPJ.

### Key Quotes or Phrases
- “Applying Marr clarifies what questions social neuroscientists should ask: what is being computed, how, and by what machinery?”  
- “Mentalizing is best viewed as an inference problem about hidden causes.”

### Concept Graph
- Observations → Algorithm (representation: generative model) → Inferred beliefs/desires → Predicted action

---

## 2006 — Haslam, N. (2006). Dehumanization: An Integrative Review. *Personality and Social Psychology Review.*

**Full Citation:** Haslam, N. (2006). Dehumanization: An Integrative Review. *Personality and Social Psychology Review, 10*(3), 252–264.

**Topic Tags:** Dehumanization, Essentialism, Objectification, Infra‑humanization, Empathy, Social Cognition

### Core Question / Problem
How can we conceptually and empirically unify the many uses of "dehumanization" across domains (race/ethnicity, gender/pornography, disability, medicine, technology), and what are its psychological bases? Haslam argues that prior work lacked a clear analysis of what is being denied — "humanness" — and that clarifying that concept reveals two distinct forms of dehumanization.

### Conceptual or Computational Framework
Haslam distinguishes two senses of humanness: **Uniquely Human (UH)** properties (those that distinguish humans from animals — higher cognition, civility, moral refinement) and **Human Nature (HN)** properties (core, embodied, affective features such as warmth, emotionality, agency, depth). Denying UH → **animalistic dehumanization**; denying HN → **mechanistic dehumanization**. These map onto different semiotics, emotions, and social contexts, and can be formalized as two orthogonal latent dimensions of perceived humanness.

### Methods Overview
This is a theoretical integrative review that synthesizes historical, qualitative, and quantitative studies. Haslam draws on empirical work (including Haslam et al., 2004/2005 trait‑rating and GNAT studies), infra‑humanization findings (Leyens et al.), and cognitive‑neuroscientific/clinical observations (e.g., frontotemporal dementia, autism, psychopathy) to support the UH/HN distinction. Figures and a summary table illustrate the mapping between trait clusters and dehumanization forms (see Figure 1, p.6; Table 1, p.9).

### Key Findings
- Empirical trait ratings show UH and HN load on distinct sets of characteristics and are weakly or negatively correlated, supporting two separable senses of humanness.
- *Animalistic dehumanization* (denial of UH) is linked to intergroup contexts (racism, genocide), evokes disgust/contempt, uses vertical metaphors (less than human), and depends on essentialized group boundaries.
- *Mechanistic dehumanization* (denial of HN) portrays people as cold, inert, objectlike or machine‑like (e.g., in medicine, technology, objectification of women), evokes indifference, and often correlates with psychological distance and low empathy.
- Social‑cognitive mechanisms proposed include relational construals (Fiske's relational models), cognitive modality transfer (folk‑biology or technical thinking), explanatory asymmetries (Malle's reasons vs causal histories), social categorization, psychological distance, and empathy deficits.

### Interpretation & Significance
Haslam's model broadens dehumanization beyond spectacular violence to everyday perceptions (stereotypes, objectification, depersonalization). Conceptually, it turns a monolithic construct into two measurable dimensions (UH, HN), each with distinct predictors, affective signatures, and moral consequences. This reframing clarifies why similar phrasing ("not fully human") appears across diverse domains yet produces different social outcomes.

### Computational‑Social‑Cognitive‑Scientist Hat
Formalize perceived humanness as a 2D latent vector h = [UH, HN]. Downstream functions map h → {empathy, disgust, moral_exclusion, helping_intent}. Hypotheses:
- Increasing psychological distance reduces HN more than UH (ΔHN < 0), thereby lowering predicted empathy via a monotonic function E = f(HN).
- Essentialist group beliefs amplify animalistic dehumanization by shifting UH perceptions downward for outgroups (UH_outgroup = UH_baseline − ε_essentialism).
- Mechanistic dehumanization arises when construals are abstract (high-level) and when explanatory styles emphasize causal histories over belief‑based reasons; operationalize via coding of explanations.
Suggested operational tests: GNAT for implicit associations, trait‑rating batteries for UH/HN, manipulation of construal level (Trope & Liberman), and behavioral measures (willingness to punish/help; physiological empathy markers).

### Teaching Hooks
- Abu Ghraib images illustrate animalistic humiliation and disgust (discussion: why bodily exposure matters?).
- Objectification in pornography and medicine (mechanistic routes): explore Nussbaum (1999) and patient dehumanization in clinical settings.
- Infra‑humanization studies (Leyens et al.) as empirical bridge between UH denial and intergroup outcomes.

### Pedagogical Lens
For undergraduates, present the UH/HN distinction with simple vignettes: a homeless person being called "animal" (animalistic) vs. a patient spoken about as a case file (mechanistic). Use short GNAT demos or coding exercises where students rate traits and map them onto UH/HN.

### Connections
Links to course concepts: mentalizing/intentional stance (animacy cues trigger intentional stance; lack of HN undermines empathy and mentalizing), essentialism, psychological distance, predictive mind (reduced model complexity for distant/abstract others), objectification and moral exclusion.

### Key Quotes or Phrases
- "Two forms of dehumanization: the denial of uniquely human attributes and the denial of human nature." (p.252)
- "Animalistic dehumanization evokes disgust; mechanistic dehumanization evokes indifference." (pp.7–8)

### Concept Graph
- Humanness → two senses: UH (Uniquely Human) and HN (Human Nature).
  - **Uniquely Human (UH):** Traits that distinguish humans from animals (language, refinement, moral sensibility). **Notable Figures:** Haslam; Leyens. **Related Concepts:** Infra‑humanization, socialization.
  - **Human Nature (HN):** Core affective/agentive traits (warmth, emotionality, agency, depth). **Notable Figures:** Haslam. **Related Concepts:** Empathy, psychological distance, essentialism.
- **Animalistic Dehumanization:** Denial of UH → likening to animals; associated with disgust/contempt; prototypically intergroup. **Related Concepts:** Infra‑humanization, moral exclusion.
- **Mechanistic Dehumanization:** Denial of HN → likening to objects/machines; associated with indifference; occurs interpersonally and in institutional contexts. **Related Concepts:** Objectification, depersonalization.

### Relevant Terms
- **Existing Terms Used:** Animacy; Intentional Stance; Mentalizing; Agency; Experience; Empathy; Social Categorization; Psychological Distance; Essentialism; Objectification; Infra‑humanization. (See course glossary for canonical entries.)

- **New Terms to Add:**
  - **Uniquely Human (UH):** (Definition) Traits perceived as distinctive to humans (e.g., higher cognition, moral refinement). **Notable Figures:** Haslam. **Related Concepts:** Infra‑humanization; cultural learning.
  - **Human Nature (HN):** (Definition) Traits seen as core/innate to humans (e.g., warmth, emotionality, agency). **Notable Figures:** Haslam. **Related Concepts:** Empathy; essentialism.
  - **Animalistic Dehumanization:** (Definition) Denying UH traits; implicitly/explicitly likening others to animals; emotions: disgust/contempt. **Notable Figures:** Haslam; Leyens. **Related Concepts:** Moral exclusion; intergroup aggression.
  - **Mechanistic Dehumanization:** (Definition) Denying HN traits; representing others as objects/machines; emotions: indifference. **Notable Figures:** Haslam. **Related Concepts:** Objectification; medical dehumanization.

---

## 2007 — Gray, H. M., Gray, K., & Wegner, D. M. (2007). Dimensions of Mind Perception. *Science.*

**Full Citation:** Gray, H. M., Gray, K., & Wegner, D. M. (2007). Dimensions of Mind Perception. *Science*, 315, 619–619.

**Topic Tags:** mind perception, agency, experience, dimensionality reduction, social evaluation

### Core Question / Problem
Do people represent minds in others along meaningful dimensions, and if so, what are those dimensions and their psychological consequences?

### Conceptual or Computational Framework
Gray et al. provide experimental evidence for a low-dimensional representation of minds (primarily Agency and Experience). At Marr’s levels: computational goal = compress a high-dimensional space of possible mental features into tractable dimensions for fast inference; algorithmic = two-dimensional mapping; implementational = patterns of attribution consistent across participants and correlations with moral judgments.

### Methods Overview
Multiple experiments: participants rated a variety of targets (humans, animals, gods, robots) on trait adjectives; principal components / factor analyses revealed two stable dimensions. Follow-up behavioral measures connect dimensions to moral judgments and perceived responsibility.

### Key Findings
- A two-factor structure (Experience, Agency) captures most variance in mind attributions.
- These dimensions predict distinct moral consequences: Experience predicts moral rights (do not harm), Agency predicts moral responsibility (blame, praise).

### Interpretation & Significance
A compact representational account explains diverse phenomena — anthropomorphism, dehumanization, moral judgments — by showing that a small set of latent dimensions governs social inference. This aligns with computational cognitive science’s emphasis on compressed representations for efficient prediction.

### Teaching Hooks
- Quick rating exercise: give students target list (baby, dog, robot, corpse) and ask them to place each on two axes.
- Explain PCA as a method for discovering dimensions.

### Pedagogical Lens
- Difficulty: 2/5
- Pre-reqs: basic stats (factor/PCA), ToM
- Misconception: dimensions are mutually exclusive; many targets score on both.

### Connections
- Strongly connected to Epley & Waytz, Waytz et al., and course glossary terms like agency/experience and moral typecasting.

### Key Quotes or Phrases
- "Mind perception is organized along dimensions of experience and agency."

### Concept Graph
- Target features → (map to) Agency/Experience → (drive) moral judgments.

---

## 2009 — Mitchell, J. P. (2009). Social psychology as a natural kind. *Trends in Cognitive Sciences.*

**Full Citation:** Mitchell, J. P. (2009). *Social psychology as a natural kind.* Trends in Cognitive Sciences.

**Topic Tags:** mentalizing, mPFC, representation, natural kind, Marr’s levels

### Core Question / Problem
Why do diverse social-psychological phenomena (self-knowledge, attitudes, emotion, understanding others) repeatedly recruit a common set of brain systems—especially medial prefrontal cortex (mPFC)—and what does that convergence imply about social cognition as a domain?

### Conceptual or Computational Framework
Mitchell argues that social psychology constitutes a “natural kind”: a coherent domain with shared computational demands—representing persons and predicting their future states—and overlapping neural substrates (notably mPFC). At Marr’s levels, the **computational** goal is social prediction; **algorithmically**, person-level summaries and trait/valuation representations support inference; **implementationally**, subregions of mPFC contribute differentially to valuation vs person knowledge. 

### Methods Overview
Opinion/review synthesizing neuroimaging, lesion, and behavioral evidence showing convergent mPFC engagement across self/other judgment, impression formation, and affective tasks; highlights subregional dissociations and cross-task ubiquity. 

### Key Findings
- mPFC is consistently engaged across social tasks; ventral vs dorsal subregions map roughly onto valuation vs person-knowledge operations.  
- Convergent lesion and imaging evidence supports a shared representational workspace for social information.  
- The cross-phenomenon overlap motivates theory at the computational/algorithmic levels rather than mere functional localization. 

### Interpretation & Significance
If social tasks share goals and representations, we should build models that **do** person-level prediction and test them against behavior/brain data (not just map regions). This frames social cognition as mechanistically unified and guides hypothesis-driven experiments. 

### Computational-Social-Cognitive-Scientist Hat
- **Lewin:** Internal representations (R) in mPFC help explain B = f(P, E, R).  
- **Marr:** Separate *what* is computed (social prediction) from *how* (representations/inference) and *where* (mPFC network).

---

## 2009 — Mitchell, J. P. (2009). Inferences about mental states. *Philosophical Transactions of the Royal Society B.*

**Full Citation:** Mitchell, J. P. (2009). Inferences about mental states. *Philosophical Transactions of the Royal Society B.*

**Topic Tags:** Mentalizing, Theory of Mind, Representations, Computational Cognitive Science

### Core Question / Problem
How should social psychologists and cognitive neuroscientists think about the processes people use to infer others' mental states? Mitchell argues for treating social inference as a set of natural‑kind cognitive processes that can be studied with the same tools used elsewhere in cognitive science.

### Conceptual or Computational Framework
Mitchell frames social inference in Marr‑style terms: what is the goal of mentalizing (computational level), which representations and algorithms implement it (algorithmic level), and what neural substrates realize those computations (implementational level). He emphasizes the utility of treating social‑cognitive processes as natural kinds amenable to mechanistic decomposition.

### Methods Overview
The paper is a conceptual synthesis drawing on neuroimaging, lesion, and developmental literatures. Mitchell integrates findings on the default network, RTPJ, and medial prefrontal cortex (MPFC) to argue for separable roles in mental state attribution.

### Key Findings
- Social inference is not a unitary faculty but comprises subcomponents (belief reasoning, trait inference, affect attribution) that map onto partly separable neural systems.
- RTPJ appears selectively involved in belief attribution and perspective‑taking; MPFC contributes to trait inference and valuation‑like representations.
- The default network supports generative, counterfactual simulations enabling inferences about temporally or perceptually distal minds.

### Interpretation & Significance
Mitchell reframes social cognition as a set of representational and algorithmic problems — not merely folk‑psychological chatter. This reorientation clarifies how social inference fits within computational cognitive science and motivates precise questions about representations (e.g., belief‑desire structures) and transition dynamics.

### Computational‑Social‑Cognitive‑Scientist Hat
- Computational level: infer hidden mental variables (beliefs, desires, traits) that cause observable actions.
- Algorithmic level: combine perceptual evidence, prior knowledge, and generative models of agent behavior (Bayesian/causal inference).
- Implementational level: RTPJ for belief computations; MPFC for value/valence and trait‑level generalization; default network for simulation and episodic prospection.

### Teaching Hooks
- Use Sally‑Anne false‑belief as an example of representational requirements (belief ≠ reality).
- Contrast "mirroring" (vicarious experience) with representational inference (belief reasoning) to show multiple computational strategies.

### Pedagogical Lens
Highlight Marr's levels: ask students to specify the computational goal, propose an algorithm, and identify potential neural implementation — using a single social task (e.g., predicting whether someone will hide an object).

### Connections
Links directly to literature on RTPJ (Saxe & Wexler, 2005), mirroring vs self‑projection (Waytz & Mitchell, 2011), and the predictive mind framework.

### Key Quotes or Phrases
- "Social psychology as a natural kind" — treat social inference as mechanistic cognitive processes.
- "Representations matter" — what counts as an adequate theory is a generative model linking hidden states to behavior.

### Concept Graph
- Mentalizing → decomposes into belief attribution (RTPJ), trait inference (MPFC), affect inference (MPFC/OFC).
  - **RTPJ:** Belief attribution. **Notable Figures:** Saxe. **Related Concepts:** False‑belief, Perspective taking.
  - **MPFC:** Trait and valence processing. **Notable Figures:** Mitchell. **Related Concepts:** Reward, Valence, Generative models.

### Key Quotes or Phrases
- "Treating social cognition as a natural kind opens the tools of cognitive science to social inference."

### Relevant Terms
- **Existing Terms Used:** Mentalizing, Theory of Mind, RTPJ, MPFC, Representations, Marr's Levels.

---

## 2010 — Epley, N., & Waytz, A. (2010). Mind Perception. *In S. T. Fiske (Ed.), Handbook of Social Psychology (5th ed.).*

**Full Citation:** Epley, N., & Waytz, A. (2010). Mind Perception. In *Society & Animals* / Social Cognition chapter (selected pages).

**Topic Tags:** mentalizing, mind perception, animacy, agency, experience

### Core Question / Problem
How do people perceive "minds" in others (human and non‑human), what dimensions organize those perceptions, and how do those perceptions influence social judgment and behavior?

### Conceptual or Computational Framework
Epley & Waytz frame mind perception as a graded, two‑dimensional attributional space (Experience vs Agency) that functions as an early *preattributional* step in social cognition: first, perceivers ask “Does it have a mind?” then “What state is it in?”. This sits naturally at Marr’s Algorithmic level (representations: 2‑D mind space; operations: cues→attribution) and connects to the Computational level via the goal of enabling prediction and coordination in social environments.

### Methods Overview
This is a conceptual synthesis and review integrating laboratory experiments (e.g., cue manipulations that trigger animacy), developmental studies (infant sensitivity to teleology/goal-directed motion), cross‑cultural evidence, and moral judgment paradigms (e.g., attributions of responsibility and dehumanization). Core manipulations reviewed include motion cues, agency cues, moral contexts, and social distance (ingroup/outgroup).

### Key Findings
- Mind perception is structured primarily along two separable dimensions: **Experience** (capacity to feel) and **Agency** (capacity to plan/act). These vary independently across targets (e.g., pets = high experience/low agency; gods = high agency/low experience). 
- Perceivers use perceptual and contextual cues (animacy, goal‑directed motion, social closeness) to infer mind status; these inferences serve predictive and moral functions (assigning blame/praise, granting moral worth). 
- Mind perception is modulated by social distance and culture: ingroup members are attributed richer mental capacities than distant outgroups, and interdependent cultures show greater habitual perspective taking. 
- Errors and biases occur: people over‑attribute intentionality (leading to blame) and under‑attribute experience to dehumanized groups; activation of mind perception is effortful and context‑dependent. 

### Interpretation & Significance
Epley & Waytz show that mind perception is not a binary cognitive act but a graded representational mapping that scaffolds later causal attributions and moral evaluations. Mechanistically, the two‑dimensional representation compresses complex mental states into actionable summaries for social coordination and prediction. In course framing, this work demonstrates how Lewin’s B = f(P,E,R) benefits from an explicit representation (R) for other minds and connects to the Predictive Mind: attributing mental states improves prediction and coordination.

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: Mind perception supplies the “R” (representation) that mediates how person and environment produce behavior.
- Marr: Algorithmic level — the two‑dimensional mind map is the representation; computational level — goal is accurate social prediction & moral evaluation.
- Brunswik: Emphasizes cue validity and ecological sampling — which cues reliably indicate agency or experience across contexts.

### Teaching Hooks
- Show Heider & Simmel animation and ask students to rate Experience/Agency for shapes.
- Moral vignette: vary perceived agency (intentional vs accidental) to generate graded blame judgments.
- Cultural comparison activity: short negotiation task with manipulated interdependence prompts.

### Pedagogical Lens
- Pre‑requisites: basic attribution theory; Heider & Simmel; dimensions (warmth/competence) analogy.
- Common misconceptions: mind perception = ToM; actually it’s a perceptual/preattributional step.
- Exam prompt: "Explain how Experience and Agency differ and why each matters for moral judgment. Provide experimental evidence."

### Connections
Links to animacy, intentional stance, Theory of Mind, predictive processing, and dehumanization literature. Useful precursor reading before Wang et al. (2025).

### Key Quotes or Phrases
- "Mind perception is a pre‑attributional process: first do we see a mind, then what is that mind like?" 
- "Perceiving mindful agency is tied to causal responsibility; perceiving experience is tied to moral worth." 

### Concept Graph
- Perceptual cues → (animacy detection) → Mind presence estimate → Map onto (Agency, Experience) → Guides prediction & moral judgment.

---

## 2010 — Waytz, A., Gray, K., Epley, N., & Wegner, D. M. (2010). Causes and consequences of mind perception. *Trends in Cognitive Sciences.*

**Full Citation:** Waytz, A., Gray, K., Epley, N., & Wegner, D. M. (2010). Causes and consequences of mind perception. *Trends in Cognitive Sciences*.

**Topic Tags:** mentalizing, mind perception, anthropomorphism, agency, experience, dehumanization, moral cognition

### Core Question / Problem
When and why do people perceive minds in others (including non-human entities), and what are the psychological and social consequences of that perception?

### Conceptual or Computational Framework
Waytz et al. synthesize behavioral, developmental, and neuroscientific evidence under a dual-dimension model of mind perception: **Agency** (capacity to plan/act) and **Experience** (capacity to feel). At Marr’s levels: computationally the goal is to infer hidden mental states to predict and connect; algorithmically people use coarse perceptual Turing tests followed by higher-order inference (heuristics like similarity, unpredictability, and effectance); implementationally, neural markers (e.g., mPFC engagement) index mind-attribution.

### Methods Overview
This is a theory-driven review integrating experiments across paradigms: morphing faces (animacy tipping points), EEG/fMRI studies of face and social perception, behavioral priming (belief in gods, surveillance cues), and social-psychological manipulations (loneliness, control threats) that alter anthropomorphism.

### Key Findings
- Mind perception operates on two separable axes: **Experience** and **Agency**, which can be dissociated in judgments. (See Gray et al., 2007.)
- Perceiver motives shape mind attribution: lack of causal control or high causal uncertainty increases ascriptions of agency (people explain unpredictability with minds). Loneliness and need for social connection increase attributions of mental states to non-humans.
- Target properties matter: humanlike appearance, humanlike motion, and perceived similarity increase mind attribution; out-group members, objects, or dehumanized targets receive lower mind ratings.
- Consequences: attributing mind confers moral status (moral patient = experience) and moral responsibility (agentic capacity). Conversely, denying mind enables dehumanization and moral exclusion.

### Interpretation & Significance
This paper reframes **mentalizing** not only as state inference (ToM) but as a graded perception system with clear antecedents and moral consequences. It connects basic perceptual triggers to higher-order social outcomes (e.g., punishment, empathy, moral typecasting). For the course’s computational lens, mind perception is an adaptive inference system that trades off accuracy and efficiency: fast detectors flag candidate minds, but higher-level reasoning (and social motives) determine commitment.

### Computational-Social-Cognitive-Scientist Hat
**What would Kurt Lewin think?** Lewin’s *B = f(P,E)* maps nicely: perceiver motives (P) and target features (E) jointly determine mind-attribution (B). He’d appreciate the field-theoretic, interactionist framing.

**What would David Marr think?** Marr would ask for explicit algorithms and representations: what are the decision rules for moving from low-level face/ motion signals to high-level mind-ascription? The two-stage detector+filter is a good start at Marr’s algorithmic level.

**What would Egon Brunswik think?** Brunswik would emphasize ecological validity: which environmental cues are reliable indicators of mind and how do perceivers weight noisy cues (lens model)? The paper’s cue-competition results fit a Brunswikian perspective.

### Teaching Hooks
- Show Heider & Simmel animation and ask students to list verbs/mental states; contrast with an animation of random motion.
- Demonstration: show morphed faces continuum and have students mark the animacy tipping point.
- Classroom poll: “Which entities deserve moral rights?” then discuss agency vs. experience.

### Pedagogical Lens
**Pre-requisite ideas:** signal detection, basic ToM, stereotyping/dehumanization
**Common misconceptions:** mind-attribution is binary; perceiving mind equals moral approval
**Discussion question:** When is it adaptive to over-attribute minds? When is it adaptive to under-attribute them?

### Connections
Links to: animacy/biological motion research, dehumanization literature, implicit bias (mPFC differences), and predictive-processing views (the role of expectancy/prediction in tagging minds).

### Key Quotes or Phrases (for slides)
- "People think about other minds in terms of two distinct dimensions: experience and agency."
- "Attributing mind confers moral rights; denying mind licenses harm."

### Concept Graph
- Perceiver motives (loneliness, lack of control) → increase mind attribution because they satisfy needs for connection/effectance.
- Target cues (human likeness, unpredictability) → increase mind attribution because they signal agency/experience.
- Mind attribution → alters moral status (patient vs. agent) → changes helping/punishing behaviors.

---

## 2012 — Wheatley, T., Kang, O., Parkinson, C., & Looser, C. (2012). From Mind Perception to Mental Connection: Synchrony as a Mechanism for Social Understanding. *Social and Personality Psychology Compass.*

**Full Citation:** Wheatley, T., Kang, O., Parkinson, C., & Looser, C. (2012). From Mind Perception to Mental Connection: Synchrony as a Mechanism for Social Understanding. *Social and Personality Psychology Compass*.

**Topic Tags:** mind perception, synchrony, neural entrainment, social bonding, empathy, predictive processing

### Core Question / Problem
How do humans progress from detecting minds to forming deep interpersonal connection, and what role does synchrony (neural and behavioral entrainment) play as a mechanism for social understanding and bonding?

### Conceptual or Computational Framework
Wheatley et al. argue that mind detection (face/voice/motion Turing tests) is necessary but not sufficient for connection; effective social prediction and *synchrony* (temporal entrainment across neural/physiological/behavioral levels) enable mental connection. At Marr’s levels: computationally the system seeks to minimize prediction error about a partner’s dynamics; algorithmically synchrony aligns oscillatory phases across regions/agents to make communication windows efficient; implementationally neuronal coherence and oxytocinergic systems mediate reward and kin-like bonding.

### Methods Overview
A broad review spanning EEG/ERP face-animacy studies, point-light biological motion experiments, TMS studies of motor resonance, physiological coupling in rituals, tapping/synchrony behavioral paradigms (Hove & Risen; Wiltermuth & Heath), and psychopharmacological manipulations (oxytocin studies).

### Key Findings
- Perceptual systems run multi-stage Turing tests: early liberal detectors (face/voice/motion) flag candidates; later, discriminative processes (e.g., N400-like/400ms ERP activity) commit to animacy/mind status. 
- Implicit simulation (emotion contagion, motor resonance) provides a fast path to shared states; explicit simulation (perspective-taking) is slower and effortful.
- Behavioral synchrony (joint tapping, coordinated movement) reliably increases rapport, cooperation, and prosociality even among strangers. Experimental induction of synchrony increases trust and group cohesion.
- Neural synchrony yields processing efficiency (entrainment aligns communication windows across regions), and synchrony is experienced as pleasurable — plausibly recruiting reward (oxytocin, dopaminergic pathways) and promoting future affiliation.

### Interpretation & Significance
This review provides a mechanistic bridge between basic perceptual cues for mind detection (covered elsewhere) and higher-order social bonding. Synchrony functions as both an *index* (marker) and *mechanism* (causal factor) for connection — enabling efficient cross-brain communication and a subjective blurring of self/other that underlies empathy and group cohesion. For computational social cognition, synchrony is a biologically plausible algorithm for reducing prediction error in dynamic, interactive settings.

### Computational-Social-Cognitive-Scientist Hat
**What would Kurt Lewin think?** He would note that synchrony changes the person–environment field: shared temporal structure reduces interpersonal ‘distance’ in the life space, enabling collective action.

**What would David Marr think?** Marr would press for formal models of how oscillatory phase alignment alters representational quality and error signals; the review sketches testable algorithmic predictions (e.g., entrainment increases mutual information between agents).

**What would Egon Brunswik think?** He’d ask how reliable synchrony cues are as ecological indicators of kinship or similarity; wheatley’s kinship signaling hypothesis echoes Brunswik’s emphasis on cue validity.

### Teaching Hooks
- Play a pair of short video clips: one where two people spontaneously groove together and one asynchronous interaction; poll students on felt connection.
- Lab demo: simple tapping synchrony task (student pairs tap with metronome in vs out of phase) and report liking/trust in paired questionnaire.
- Discuss musical ensembles and religious rituals as engineered synchrony — relate to historical examples (marching, clapping).

### Pedagogical Lens
**Prerequisites:** neural oscillations basics, ToM vs. emotion contagion, signal detection
**Common misconceptions:** synchrony = mimicry; synchrony is always prosocial (it can be used for manipulation or exclusion)
**Exam prompt:** Design a simple experiment to test whether neural synchrony mediates the effect of behavioral synchrony on cooperative behavior.

### Connections
Ties to animacy detection (Wheatley’s ERP animacy tipping point work), mirror/resonance systems, oxytocin-trust literature, and predictive-processing frameworks (entrainment as phase-alignment to reduce prediction error).

### Key Quotes or Phrases
- "Synchrony may serve as an adaptive marker of genetic similarity; we synchronize most with similar others."
- "Neural synchrony reduces processing load and blurs self-other boundaries, producing pleasurable mental connection." 

### Concept Graph
- Mind detection (face/voice/motion) → simulation (resonance, contagion) → behavioral synchrony (anticipation) → neural entrainment → reward & bonding.
  - **Synchrony:** Time-locked coupling across neural, physiological, and behavioral signals between interacting agents that supports mutual prediction and partial access to internal states. **Related Concepts:** synchrony, resonance, neural entrainment, simulation.
  - **Neural efficiency (social sense):** A reduction in processing cost achieved when the perceiver and perceived entrain neural dynamics, aligning communication windows and lowering prediction-error propagation during interaction. **Related Concepts:** predictive processing, entrainment, reward.

---

## 2012 — Troje, N. F. (2012). What is biological motion: Definition, stimuli, and paradigms. *In Social Perception: Detection and Interpretation of Animacy, Agency, and Intention (Rutherford & Kuhlmeier, eds.). MIT Press.*

**Full Citation:** Troje, N. F. (2012). What is biological motion?: Definition, stimuli and paradigms. In M. D. Rutherford & V. A. Kuhlmeier (Eds.), *Social Perception: Detection and Interpretation of Animacy, Agency, and Intention.* MIT Press.

**Topic Tags:** biological motion, point-light displays, animacy, life motion, perception

### Core Question / Problem
What do researchers mean by "biological motion"? Troje traces the historical lineage from Johansson's point-light displays to modern work that asks not only how the visual system recovers articulated structure from non-rigid motion, but also what social information (actor, action, style, animacy) can be read out from motion alone.

### Conceptual or Computational Framework
Troje positions "biological motion" within a broader class he calls **life motion** (all motion that signals living beings). He distinguishes intrinsic (deforming-body) versus extrinsic (object trajectory) motion and separates global, structure-from-motion processes (configuration recovered from correlated part motions) from local, shape-independent invariants (e.g., foot acceleration consistent with gravity). This maps naturally onto Marr‑style distinctions: the computational goal (detect life, infer actor/action), algorithmic cues (local acceleration patterns, global kinematic templates), and implementational considerations (STS and other neural areas).

### Methods Overview
The chapter reviews standard experimental paradigms:
- Point‑light stimuli and stick-figure variants (Johansson tradition).
- Detection tasks (is a walker present?), direction tasks (which way is the walker facing?), and masked/noise paradigms.
- Scrambling manipulations (spatial/temporal) that isolate local vs global cues.
- Stylistic manipulations for person identification, sex, emotion, and intention (kinematic synthesis and morphs).

### Key Findings
- Point‑light displays robustly convey identity, sex, emotion, and intention despite minimal form cues (Johansson; Cutting).
- Two largely independent information channels can support common tasks (e.g., facing direction): (i) motion-mediated reconstruction of articulated shape and (ii) local motion invariants (notably foot trajectory/acceleration). Troje & Westhoff (2006) highlight the "local inversion effect" tied to foot acceleration profiles that obey gravitational constraints.
- Scrambled displays are not "non-biological": they preserve life‑detection cues, so treating them as null controls is conceptually risky.
- The superior temporal sulcus (STS) responds in many—but not all—biological motion contrasts; STS responses appear heterogeneous and sensitive to stimulus type and task.
- Life‑detection cues (vertical acceleration, foot dynamics) appear evolutionarily old and available early in development (neonatal/animal data cited).

### Interpretation & Significance
Troje argues for precision in terminology: reserve "biological motion" for intrinsic deformable-body motion, use "animate motion" for whole‑object kinematics, and "life motion" for the broad class. Importantly, motion carries both redundant and complementary signals: global configuration supports identity and action parsing while local invariants provide fast, shape‑independent life detection and orientation cues. This redundancy explains robustness but complicates experimental design and interpretation (masking confounds, control stimuli).

### Computational‑Social‑Cognitive‑Scientist Hat
Modeling biological motion benefits from a hybrid architecture: early mid‑level filters tuned to local invariants (life detector) gate attention and feed higher‑order configurational reconstruction modules that instantiate kinematic templates (generative models of gait, action). From a predictive‑processing stance, local invariants provide strong priors (is this animate?), while template‑based inference recovers higher fidelity hypotheses about identity/action and computes prediction errors across frames.

### Teaching Hooks
- Demo: show a point‑light walker, scrambled walker, upside‑down walker — students guess what cues they used.
- In‑class exercise: tweak foot acceleration (simulated) and ask whether the stimulus still 'looks alive.'
- Short homework: map Johansson's tasks to Marr's three levels.

### Pedagogical Lens
Favor mechanistic clarity: explain why local acceleration patterns are diagnostic (ballistic foot motion under gravity) and how global form can be reconstructed from temporal correlations in joint motion. Use simple generative sketches (stick-figure + pendulum analogy) to convey intuition.

### Connections
Links to animacy perception (Heider & Simmel tradition), action understanding, STS and social neuroscience, computer animation (style transfer), and developmental sensitivity to life motion cues.

### Key Quotes or Phrases
- "Life motion" as umbrella term for motion that signals living beings.
- "Life detector" for filters sensitive to ballistic invariants in foot motion.

### Concept Graph
- Life motion → {extrinsic (animate motion), intrinsic (biological motion)}
  - **Life Detector:** local visual filters sensitive to foot acceleration consistent with gravity. **Notable Figures:** Troje, Chang. **Related Concepts:** Animacy; early attention orienting.
  - **Structure-from-motion:** global integration of part motions to yield articulated 3D shape. **Notable Figures:** Johansson, Ullman. **Related Concepts:** Point‑light displays; STS.

### Relevant Terms
- **Existing Terms Used:** Biological Motion, Animacy, Intentional Stance.

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

### Teaching Hooks
- Show binocular rivalry (bi-stable perception) and explain switching as top-down hypothesis competition. 
- Active inference demo: a thermostat analogy (predict temperature; act to reduce error).
- Discuss a cultural artifact (e.g., learning to read) to illustrate socio-cultural “scaffolding” of priors.

### Pedagogical Lens
- Pre-requisites: basic Bayesian ideas, Marr’s levels, generative model intuition
- Common misconceptions: “Predictive processing says the brain is always 'top-down' and ignores sensory input” — clarify interplay and precision.
- Discussion prompt: Where should explanatory weight lie for uniquely human reasoning — in hierarchical predictive machinery or in socio-cultural scaffolding? Provide arguments for both.

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

### Teaching Hooks
- Discuss sheep-as-dog example: how an atypical percept can be explained statistically versus content-wise. 
- Classroom debate: Does covariance = content? Split students to argue for/against.

### Pedagogical Lens
- Pre-requisites: basics of Bayesian inference, predictive coding vocabulary
- Common misconception: PEM “proves” representational content — Hohwy’s work shows the gap needs addressing.
- Exam prompt: Evaluate whether PEM can account for false-belief reasoning in ToM.

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

### Teaching Hooks
- Short "vignette swap" in class: give students minimal behaviors and see how trait attributions converge.
- Warmth/Competence quadrant exercise with celebrities or brands.

### Pedagogical Lens
- Pre‑requisites: basic memory and schema theory, attribution basics
- Misconceptions: Averaging vs weighted diagnostic inference — perceivers often privilege diagnostic behaviors.
- Exam prompt: "Describe two models of impression formation (trait averaging vs schema‑based) and design an experiment to distinguish them."

### Connections
Links to mind perception (pre‑attributional stages), stereotyping research, and predictive processing via priors/schemas.

### Key Quotes or Phrases
- "Two fundamental dimensions — warmth and competence — keep reappearing in impressions of both individuals and groups." 
- "Reputations are more accurate for well‑known individuals; for less‑known targets, prior theories dominate." 

### Concept Graph
- Observed behaviors → trait inference (diagnostic weighting) → memory/schema updating → predicted future behavior.

--- 

## 2013 — Sievers, B., Polansky, L., Casey, M., & Wheatley, T. (2013). Music and movement share a dynamic structure that supports universal expressions of emotion. *PNAS.*

**Full Citation:** Sievers, B., Polansky, L., Casey, M., & Wheatley, T. (2013). *Music and movement share a dynamic structure that supports universal expressions of emotion.* Proceedings of the National Academy of Sciences.

**Topic Tags:** cross-modal dynamics, emotion, biological motion, representation

### Core Question / Problem
Do music and movement share a **common dynamic code** for emotion that generalizes across cultures? 

### Conceptual or Computational Framework
A cross-modal representational geometry: emotional meaning maps onto low-level dynamical features (tempo, jitter, amplitude) that receivers use for inference. **Computationally**, efficient affect communication; **algorithmically**, reduce high-dimensional dynamics to a low-dimensional emotion space. 

### Methods Overview
Participants sculpted music and animations with sliders to express emotions; a remote Kreung sample replicated mappings. Analyses: clustering in parameter space, Monte-Carlo tests, and ANOVA across settings. 

### Key Findings
- Music and movement converge on similar feature configurations for the same emotions (cross-modal clustering).  
- Broad cross-cultural similarity supports a shared code; dynamical features reliably predict perceived emotion. 

### Interpretation & Significance
Identifies concrete features for models of affect perception and generative social signaling—useful input channels to students’ predictive-processing intuitions about how we read others’ states. 

### Computational-Social-Cognitive-Scientist Hat
- **Brunswik:** Cue reliability across cultures → ecological validity.  
- **Marr:** Precisely specifies the *algorithmic* features likely read out by receivers. 

---

## 2014 — Skerry, A. E., & Saxe, R. (2014). A Common Neural Code for Perceived and Inferred Emotion. *Journal of Neuroscience.*

**Full Citation:** Skerry, A. E., & Saxe, R. (2014). A Common Neural Code for Perceived and Inferred Emotion. *Journal of Neuroscience*, 34(48), 15997–16008.

**Topic Tags:** Emotion perception, MPFC, Representational similarity, Mentalizing

### Core Question / Problem
Do perceived emotions (from faces) and inferred emotions (from contextual descriptions) share neural representations? Skerry & Saxe test whether MPFC/DMPFC contain modality‑independent codes for emotional valence and show that some regions generalize across perceptual and inferential routes.

### Conceptual or Computational Framework
Using a generative/inference perspective, the paper asks whether abstract emotion categories are represented independently of the input modality — implying higher‑level representations that support cross‑modal inference.

### Methods Overview
Multivoxel pattern analyses (MVPA) on fMRI data: participants viewed faces showing emotions and read situational descriptions; classifiers trained on one modality were tested on the other to probe shared codes. ROI and whole‑brain searchlight analyses identify regions with cross‑modal generalization.

### Key Findings
- MMPFC/DMPFC contain patterns that generalize across faces and situation descriptions for valence; other regions (OFC/VMPFC) did not show this cross‑modal code.
- Evidence indicates a shared neural code for attributed emotion in MPFC, supporting an abstract representational level for emotions beyond sensory specifics.
- Results suggest separable roles: sensory regions encode modality‑specific features; MPFC encodes abstracted affective dimensions.

### Interpretation & Significance
The study supports a representational hierarchy: perceptual input is mapped to abstract affective representations that can be accessed both when perceiving emotion and when inferring it from context. This bridges perception and inference — a core problem in social cognition.

### Computational‑Social‑Cognitive‑Scientist Hat
- Computational goal: infer affective valence regardless of input modality.
- Algorithmic strategy: map modality‑specific features into a shared representational space (dimensional valence/arousal).
- Implementation: MPFC/DMPFC as hubs for modality‑independent emotion codes; sensory cortices handle low‑level features.

### Teaching Hooks
- Demonstrate cross‑modal MVPA logic — train on faces, test on stories.
- Use bar charts from the paper (classification accuracy) to show generalization as evidence for shared codes.

### Connections
Links to Mitchell (2009) on representational abstraction and to clinical questions (how impairments in MPFC might disrupt social emotion inference).

### Concept Graph
- Perceptual emotion (faces) + Inferred emotion (situations) → common MPFC representation.
  - **MMPFC/DMPFC:** Abstract affective valence code. **Notable Figures:** Skerry, Saxe. **Related Concepts:** Representation; MVPA; Valence.

### Relevant Terms
- **Existing Terms Used:** MPFC, Representation, Mentalizing, Valence, MVPA.

---

## 2015 — Parkinson, C., & Wheatley, T. (2015). The repurposed social brain. *Philosophical Transactions of the Royal Society B.*

**Full Citation:** Parkinson, C., & Wheatley, T. (2015). *The repurposed social brain.* Philosophical Transactions of the Royal Society B.

**Topic Tags:** neural reuse, repurposing, social cognition, predictive models

### Core Question / Problem
How can brains solve novel social problems using “old” circuitry? The paper synthesizes evidence that perception/space/time systems are **repurposed** to compute social variables (e.g., social distance). 

### Conceptual or Computational Framework
A constraints-and-reuse account: **computationally**, social prediction is the goal; **algorithmically**, pre-existing representational primitives (spatial maps, timing, sensory codes) are reinterpreted to encode abstract social dimensions; **implementationally**, circuits originally tuned for perception/space are recruited in social tasks across evolutionary, cultural, and individual (instrumental) timescales. 

### Methods Overview
Review of comparative work, lesion cases, and neuroimaging/meta-analyses demonstrating overlaps between social and non-social maps (e.g., physical ↔ social distance). Distinguishes evolutionary, cultural, and instrumental repurposing. 

### Key Findings
- Overlapping cortical topographies for spatial/perceptual coding and social variables.  
- Multiple repurposing routes (evolutionary → cultural → instrumental) constrain and enable social computation.  
- Reuse explains both efficiency and limits of social algorithms. 

### Interpretation & Significance
Rather than a wholly specialized “social module,” social cognition emerges from flexible reuse—guiding models to leverage general representational tools the brain already computes. Pedagogically, this reframes the “social brain” debate as **where** specialization lies across Marr’s levels. 

### Computational-Social-Cognitive-Scientist Hat
- **Lewin:** Inherited representational constraints (R) shape behavior across environments.  
- **Marr:** Build mid-level models showing how spatial/temporal codes are reinterpreted to compute social variables. 

---

## 2015 — Wang, S., Lilienfeld, S. O., & Rochat, P. (2015). The Uncanny Valley: Existence and Explanations. *Review of General Psychology.*

**Full Citation:** Wang, S., Lilienfeld, S. O., & Rochat, P. (2015). The Uncanny Valley: Existence and Explanations. *Review of General Psychology*, 19(4), 393–407.

**Topic Tags:** Uncanny valley, Animacy, Anthropomorphism, Dehumanization, Face perception, Mind perception

### Core Question / Problem

Do "uncanny" reactions to highly humanlike artifacts reflect a real, measurable nonlinear relation between human likeness and likability (Mori's "uncanny valley") — and if so, what cognitive mechanisms produce it? The paper reviews empirical evidence, evaluates competing explanations, and proposes a new account called the Dehumanization hypothesis.

### Conceptual or Computational Framework

The authors situate the problem at the intersection of perceptual sensitivity (animacy detection), social‑cognitive attribution (mind perception / mentalizing), and evolutionary‑inspired affective responses (disgust, fear). They frame the uncanny as a cognitive–perceptual problem that can be tested statistically (linear vs. nonlinear relation between human likeness and likability) and mechanistically (two‑stage animacy → scrutiny → dehumanization process).

### Methods Overview

This is a conceptual, integrative review. The authors inspect empirical studies that used (a) morphed image continua, (b) ratings of real androids/avatars, (c) psychophysiological and neural measures (ERPs, fMRI), and (d) infant and nonhuman primate work. They critique measurement confounds in both independent (human likeness) and dependent ("shinwakan" → likability/affinity/eeriness) variables and propose a residual‑analysis test of Mori's curve as an empirical fix.

### Key Findings

- Evidence for an uncanny valley is mixed: some morph‑based studies and Mathur & Reichling (2016) show nonlinear dips in likability, while many studies of existing replicas do not.
- Methodological heterogeneity (how "likability/uncanniness" and "human likeness" are operationalized) likely explains divergent findings. The paper catalogs inconsistent translations of Mori's shinwakan and recommends multi‑indicator measures.
- Multiple mechanisms have been proposed (pathogen avoidance → disgust; mortality salience → terror management; evolutionary aesthetics; violation of expectation; categorical uncertainty; mind perception), but none singly account for the full pattern. The authors critique limited causal tests and ecological validity in many studies.
- They propose the Dehumanization hypothesis: realistic anthropomorphism creates an initial impression of humanness (quick animacy detection), which invites deeper scrutiny; detection of mechanistic or non‑human features then triggers dehumanization (perceiving the agent as lacking human nature or uniqueness), producing negative affect and the uncanny response.

### Interpretation & Significance

Wang et al. recast the uncanny problem from an engineering curve‑hunt into a psychological process question: what perceptual and social‑cognitive computations produce negative affect toward near‑human agents? This reframing emphasizes mechanisms (animacy detection, mind perception, dehumanization) that map directly onto course concepts such as Animacy, Mentalizing, and Representation. The paper also proposes concrete statistical and experimental tests that move the field toward principled, falsifiable models.

### Computational‑Social‑Cognitive‑Scientist Hat

From a Marr‑inspired perspective: at the computational level the problem is to predict when an agent will elicit positive social affiliation vs. aversive uncanniness. Algorithmically, the paper suggests a two‑stage pipeline: (1) fast form/animacy detection that triggers the Intentional Stance and anthropomorphism; (2) slower validation/scrutiny that compares predicted properties (agency, experience) with observed cues — large prediction errors (mismatch) drive dehumanization and negative valence. Implementationally, the authors point to ERP (N170 / late positive potentials) and fusiform/pSTS signatures consistent with these stages.

### Teaching Hooks

- Show students a short sequence of morphed faces (toy → doll → human) and collect instant likability/animacy judgments; use results to motivate categorical uncertainty vs. violation‑of‑expectation debates.
- Contrast reactions to a photorealistic CGI baby (e.g., an old demo) vs. a stylized robot to prompt discussion of anthropomorphism and dehumanization.

### Pedagogical Lens

Translate the paper's claims into predictive modeling exercises: have students build simple regressions of likability on human‑likeness and inspect residual patterns (is there a dip?). Then extend to a two‑process model where presentation time modulates whether animacy or dehumanization dominates.

### Connections

Links to course glossary concepts: Animacy and Mentalizing (perceptual triggers), Intentional Stance (why we adopt humanlike explanations), Representation & Predictive Mind (prediction/validation pipeline), and Synchrony (contrast: synchrony increases affiliation; uncanny responses reduce it).

### Key Quotes or Phrases

- "The uncanny valley hypothesis is ultimately an engineering problem..." (paper's framing).
- "We propose a Dehumanization hypothesis." (central proposal).

### Concept Graph

- Rapid animacy/form detection → anthropomorphism (fast, perceptual).
- Anthropomorphism → deeper scrutiny (slow, cognitive).
  - **Dehumanization hypothesis:** When scrutiny reveals mechanistic/nonhuman cues, observers deny human nature/uniqueness, producing negative affect and 'uncanniness.' **Notable Figures:** Wang, Lilienfeld, Rochat (2015). **Related Concepts:** Animacy, Mind Perception, Infrahumanization.
  - **Violated Expectation:** Mismatch between appearance and motion/voice. **Related Concepts:** Predictive Mind; Prediction Error.

### Relevant Terms

- **Existing Terms Used:** Animacy; Intentional Stance; Mentalizing; Agency; Representation; Predictive Mind.
- **New Terms to Add:**
  - **Uncanny valley:** Nonlinear relation (hypothesized) between human likeness and social affinity; a dip of negative affect for near‑human but imperfect replicas. **Notable Figures:** Masahiro Mori. **Related Concepts:** Animacy; Anthropomorphism; Dehumanization.
  - **Dehumanization hypothesis:** A process model proposing that anthropomorphism (initial attribution of humanness) followed by detection of mechanistic discrepancies leads observers to dehumanize replicas (deny human nature/uniqueness), producing uncanny affect. **Notable Figures:** Wang, Lilienfeld, Rochat (2015). **Related Concepts:** Infrahumanization; Mind Perception; Violation of Expectation.

---

## 2016 — Freeman, T. (2016). What is Mentalizing? An Overview. *British Journal of Psychotherapy.*

**Full Citation:** Freeman, T. (2016). What is Mentalizing? An Overview. *British Journal of Psychotherapy*, 32(2), 189–201.

**Topic Tags:** mentalizing, clinical mentalizing, social prediction, developmental trajectories

### Core Question / Problem
What is mentalizing (clinical and cognitive), how does it develop, and why is it central to both healthy social functioning and clinical disorders where it breaks down (e.g., borderline personality disorder)?

### Conceptual or Computational Framework
Freeman provides a clinically oriented account of mentalizing as a multi-component capacity: representing others' mental states, monitoring self-other boundaries, and using those representations to regulate social action. At Marr’s computational level: the goal is accurate prediction and regulation of social interactions. Algorithmically, mentalizing requires layered representations (beliefs, desires, meta-representations) and monitoring processes that arbitrate when to use self-projection vs analytic inference. Implementation links to attachment systems and neural circuitry supporting affect regulation.

### Methods Overview
Review integrating clinical case studies, developmental psychology, and theoretical synthesis from attachment theory and psychoanalytic research. Emphasizes longitudinal and therapeutic evidence that improving reflective functioning (mentalizing) benefits social outcomes.

### Key Findings
- Mentalizing spans implicit automatic inference and explicit controlled reasoning.
- Development relies on caregiver attunement and secure attachment; deficits produce clinical symptoms.
- Training mentalizing (e.g., mentalization-based therapy) improves outcomes in personality disorders.

### Interpretation & Significance
This overview links cognitive-science models of mental state inference to clinical practice, showing that mechanistic accounts of social prediction can inform therapeutic interventions. For PSYC 137, it provides a bridge from lab-based models (generative models, prediction errors) to real-world social functioning and psychopathology.

### Computational-Social-Cognitive-Scientist Hat
- Lewin: clinical states shift P (perceiver) and thus distort R (representations).
- Marr: computational goal = stable social coordination; algorithmic deficits explain symptoms.

### Teaching Hooks
- Case vignette exercise where students diagnose mentalizing failure and propose an intervention.
- Demonstrate implicit vs explicit mentalizing with rapid video inference vs reasoning prompts.

### Pedagogical Lens
- Difficulty: 3/5
- Pre-reqs: basic ToM, attachment theory
- Misconception: mentalizing is only 'theory of mind' — it's broader (self-other boundaries, emotion regulation).

### Connections
- Links to developmental ToM literature, predictive mind models, and therapeutic practices (MBT).

### Key Quotes or Phrases
- "Mentalizing is a process we are continually engaged in whether implicitly or explicitly."

### Concept Graph
- Attachment security → (supports) Accurate mentalizing → (improves) social regulation.

---

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

### Teaching Hooks
- Show the *representational similarity* figure (ventral-stream ↔ deep-net layers) and ask students to predict which network layer will best match early vs late visual areas.
- Analogy: building a car (task) vs mapping engine parts (implementation) — both necessary to understand driving behavior.

### Pedagogical Lens
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

---

## 2019 — Sievers, B., Lee, C., Haslett, W., & Wheatley, T. (2019). A multi-sensory code for emotional arousal. *Proceedings of the Royal Society B.*

**Full Citation:** Sievers, B., Lee, C., Haslett, W., & Wheatley, T. (2019). *A multi-sensory code for emotional arousal.* Proceedings of the Royal Society B.

**Topic Tags:** emotional arousal, spectral centroid, multi-sensory code, predictive models

### Core Question / Problem
Is there a single low-level statistic that robustly signals **arousal** across modalities? Tests spectral centroid as a supramodal cue used by senders and decoded by receivers. 

### Conceptual or Computational Framework
**Computationally**, arousal estimation is a low-dimensional decoding problem; **algorithmically**, extracting the central tendency of frequency content (spectral centroid) supports cross-modal arousal judgments (sound, speech, movement, visual form). 

### Methods Overview
Regression and Bayesian classifiers relate spectral-centroid-like features to arousal ratings across datasets (e.g., emotional speech), testing generalization and discrimination (AUCs). 

### Key Findings
- Higher spectral centroid → higher perceived arousal across modalities.  
- Classifiers using centroid features discriminate arousal strongly and generalize across datasets. 

### Interpretation & Significance
Provides an implementable feature for computational models of affect perception and cross-channel social communication—ideal for students’ projects linking signal processing to social inference. 

### Computational-Social-Cognitive-Scientist Hat
- **Lewin:** Adds a measurable R mediating P/E → behavior.  
- **Marr:** Clear *algorithmic* feature with plausible *implementational* correlates (neural coding of spectral statistics). 

---

## 2020 — Lockwood, P. L., Apps, M. A. J., & Klein-Flügge, M. (2020). Is there a 'social' brain? Implementations and algorithms. *Trends in Cognitive Sciences.*

**Full Citation:** Lockwood, P. L., Apps, M. A. J., & Klein-Flügge, M. (2020). Is there a 'social' brain? Implementations and algorithms. *Trends in Cognitive Sciences*.

**Topic Tags:** social brain, Marr's levels, algorithmic vs implementational, ACCg, social learning, ToM

### Core Question / Problem
Are there algorithms or brain implementations that are specialized for social cognition, or does social behavior reuse general-purpose mechanisms? How should we test social specificity across Marr’s levels?

### Conceptual or Computational Framework
The paper argues for careful separation of Marr’s levels when evaluating social specificity. It reviews candidate social algorithms (e.g., ToM-like belief inference, social valuation learning) and potential implementational specializations (e.g., ACCg). It advocates computational modeling + multivariate neural methods to bridge algorithm and implementation. 

### Methods Overview
A review and synthesis of computational modelling studies, neuroimaging findings, comparative evidence (non-human animals), and proposals for experimental designs that hold one level constant while probing another (e.g., vary task demands while keeping algorithmic structure fixed).

### Key Findings
- Some brain regions show social selectivity (ACCg strongest candidate), but social-specificity is clearer at implementation than at algorithmic level; algorithms like ToM show promise as socially specific. 
- Outstanding empirical questions: species differences, innate vs learned social algorithms, and whether social vs non-social distinctions are categorical or continuous. 

### Interpretation & Significance
The article reframes the “social brain” debate: rather than asking “is there a social brain?” it asks *where* (which Marr level) social specialization is plausible and how to design studies to answer that. For social cognition teaching, it emphasizes rigorous experimental logic: keep levels constant, use computational models to define candidate algorithms, and map predictions to neural data.

### Computational–Social–Cognitive–Scientist Hat
- Lewin: evolutionary/ontogenetic forces could bias implementations; Lockwood et al. encourage testing whether such biases are algorithmic or implementational.
- Marr: paper is explicitly Marr-oriented — advocates holding computational/algorithmic/implementational levels distinct in experiments. 
- Brunswik: comparative and ecological validity concerns — test across species and ecological contexts.

### Teaching Hooks
- Design a student lab: two tasks with identical algorithmic structure—one social, one non-social—and predict neural dissociations.
- Discuss ACCg as a case study (what patterns would confirm social specialization?).

### Pedagogical Lens
- Pre-requisites: Marr’s levels, basics of neuroimaging and computational models
- Common misconceptions: equating neural activation with algorithmic specificity
- Discussion prompt: Propose an experiment that isolates algorithmic social specificity.

### Connections
- Connects to theory-of-mind debates (Premack & Woodruff) and predictive frameworks (how predictive models might implement social algorithms).

### Key Quotes or Phrases
- “Are there algorithms that are socially specific? The strongest evidence suggests theory of mind processing.” 
- “Hold one level constant while examining the impact on another level.” 

### Concept Graph
- Algorithm (ToM) → neural implementation candidate (ACCg) → behavioral social predictions
- Comparative tests → evaluate innateness vs learning
- Continuous vs categorical social/non-social distinction → shapes experimental expectations

---

## 2020 — Perez-Osorio, J., & Wykowska, A. (2020). Adopting the Intentional Stance Toward Natural and Artificial Agents. *Philosophical Psychology.*

**Full Citation:** Perez-Osorio, J. & Wykowska, A. (2020). Adopting the Intentional Stance Toward Natural and Artificial Agents. *Philosophical Psychology* (accepted manuscript Feb 2019).

**Topic Tags:** intentional stance, human-robot interaction, social attunement, stance-taking

### Core Question / Problem
When and why do humans adopt the intentional stance — treating a system as if it has beliefs and desires — and what does it imply for interactions with artificial agents (robots, AI)?

### Conceptual or Computational Framework
The paper treats the intentional stance as an efficient predictive strategy: when the design or behavior of an agent makes intentional inference pay off, humans adopt it. Marr’s computational level: achieve accurate prediction in social settings; algorithmic: stance selection (physical/design/intentional) based on cue reliability, task demands, and cultural norms; implementational implications for robot design (appearance, contingency) to promote social attunement.

### Methods Overview
A literature review integrating philosophy (Dennett), developmental findings on stance emergence, cross-cultural variability, and HRI studies showing how robot appearance and contingency modulate adoption of the intentional stance.

### Key Findings
- Intentional stance is a fast, pragmatic strategy rather than a metaphysical claim about true intentionality.
- Robot features that increase contingency, goal-directed motion, and communicative signals increase adoption of the stance and social attunement.
- Cultural norms influence how readily people anthropomorphize and the norms governing acceptable stance adoption.

### Interpretation & Significance
For computational social cognition, the paper clarifies that adopting an intentional stance is an inference policy: agents (including designers) can manipulate cues to make mentalistic predictions more reliable, shaping social interaction. It connects philosophical theory (Dennett) directly to empirical HRI evidence.

### Teaching Hooks
- Show short clips of robots with varying human-likeness; ask students which stance they'd use and why.
- Mini design challenge: propose 3 features that would increase intentional stance adoption for a service robot.

### Pedagogical Lens
- Difficulty: 3/5
- Pre-reqs: intentional stance, agency, predictive models
- Misconception: adopting stance = believing the machine is conscious.

### Connections
- Links to Epley & Waytz, Gray et al., and course glossary entries on the intentional stance and animacy.

### Key Quotes or Phrases
- "Adopting the intentional stance is a pragmatic predictive strategy that facilitates social attunement."

### Concept Graph
- Robot cues (contingency, appearance) → (increase) Intentional stance adoption → (increase) Social attunement/perceived mind.

---

## 2021 — Pitcher, D., & Ungerleider, L. G. (2021). Evidence for a Third Visual Pathway Specialized for Social Perception. *Trends in Cognitive Sciences.*

**Full Citation:** Pitcher, D., & Ungerleider, L. G. (2021). Evidence for a third visual pathway specialized for social perception. *Trends in Cognitive Sciences*, 25(2), 100–112.

**Topic Tags:** Social perception, Visual pathways, STS, Biological motion, Third visual pathway

### Core Question / Problem
Does primate visual cortex contain more than the canonical dorsal and ventral pathways? Pitcher & Ungerleider synthesize anatomy, neurophysiology, fMRI and lesion evidence to propose a lateral/STS‑centered "third pathway" specialized for dynamic social perception (faces, bodies, gaze, expression, audiovisual speech).

### Conceptual or Computational Framework
The third pathway is an implementational/algorithmic claim: that early motion‑sensitive inputs (via MT/V5) feed a set of STS regions whose computations extract dynamic social cues and map them to higher‑level social interpretations (intent, expression, gaze).

### Methods Overview
This is an integrative review drawing on tracer anatomy in macaques, human fMRI (motion vs static faces), TMS/fMRI dissociations, and white‑matter tractography. Figures illustrate cortical connectivity and functional specialization of pSTS/aSTS.

### Key Findings
- Convergent evidence for a cortical stream projecting from early visual cortex (via MT) to STS that is anatomically and functionally distinct from ventral and dorsal streams.
- The STS responds selectively to biological motion, moving faces/bodies, eye‑gaze dynamics, and multisensory speech—functions critical to social perception.
- Disruption of STS regions selectively impairs dynamic face perception while sparing static identity processing (ventral stream).

### Interpretation & Significance
Introducing a third visual pathway reframes social perception as grounded in specific perceptual circuitry optimized for dynamic cues. This has implications for developmental disorders (autism) and for computational models: social inference requires fast extraction of temporal features (motion trajectories, gaze shifts) before higher‑level mentalizing.

### Computational‑Social‑Cognitive‑Scientist Hat
- Computational goal: extract agentive, intention‑relevant features from dynamic visual input.
- Algorithmic components: motion‑based segmentation, temporal pattern extraction, cross‑modal integration (audio+vision).
- Implementation: MT → pSTS/aSTS network (third pathway), projecting to nodes of social cognition (RTPJ, MPFC).

### Teaching Hooks
- Demonstrate with point‑light displays (biological motion) and static face images to show perceptual dissociations.
- Simple TMS thought experiment: predict which task (expression vs identity) would be impaired by targeted disruption.

### Pedagogical Lens
Use the third pathway to show how sensory preprocessing shapes higher social inference: representation of dynamic cues constrains what the mind can infer downstream.

### Connections
Connects to biological motion, animacy, and subsequent mentalizing computations in RTPJ/MPFC. Relevant to work on predictive coding of dynamic agents.

### Concept Graph
- Early visual cortex (V1) → MT/V5 (motion) → pSTS/aSTS (third pathway) → RTPJ/MPFC (mentalizing).
  - **Third Visual Pathway:** Motion→STS stream specialized for social signals. **Notable Figures:** Pitcher, Ungerleider. **Related Concepts:** Biological motion; STS; Animacy.

### Relevant Terms
- **Existing Terms Used:** Biological Motion, Animacy, STS, Representation, Mentalizing.
- **New Terms to Add:**
  - **Third Visual Pathway:** A lateral visual stream projecting from early visual areas via motion‑selective regions (MT/V5) into the superior temporal sulcus (STS), specialized for extracting dynamic social signals (gaze, expression, body movement). **Notable Figures:** Pitcher, Ungerleider. **Related Concepts:** MT/V5; STS; Social perception; Animacy.

---

## 2021 — Sievers, B., et al. (2021). Visual and auditory brain areas share a representational structure that supports emotion perception. *Current Biology.*

**Full Citation:** Beau Sievers, Carolyn Parkinson, Peter J. Kohler, James M. Hughes, Sergey V. Fogelson, Thalia Wheatley (2021). Visual and auditory brain areas share a representational structure that supports emotion perception. *Current Biology.*

**Topic Tags:** mentalizing, representation, cross-modal dynamics, emotion perception, representational similarity analysis (RSA), supramodal representation

### Core Question / Problem
Why do music and movement so reliably convey the same emotions? The paper asks whether auditory and visual sensory regions use a shared representational geometry that puts music and movement into directly comparable neural terms — and whether that shared geometry encodes simple stimulus features, task‑relevant feature conjunctions tied to emotion judgments, or both.

### Conceptual or Computational Framework
Sievers et al. use the language of **representational geometry** (Kriegeskorte-style RSA) to test two nested hypotheses: (H1) modality‑specific auditory and visual regions share the same representational geometry (separate regions, shared representations) and (H2) one or more supramodal regions (e.g., posterior superior temporal cortex) instantiate a unified geometry for both modalities. At Marr's levels: the **computational** level asks what problem is solved (detect/recover emotion across modalities); the **algorithmic** level is the RSA-measurable geometry and the feature/judgment RDMs (representations mapping stimuli → internal distances); the **implementational** level is the neural substrate (lingual gyrus, superior temporal gyrus, pSTG/pSTS and distributed occipito‑temporal areas).

### Methods Overview
Stimuli: short piano melodies and animations of a bouncing ball generated from the same 5 feature parameters (speed, irregularity/jitter, consonance/spikiness, ratio big/small movements, ratio up/down). Prototype emotions (angry, happy, peaceful, sad, scared), linear mixes (25–75%), and three neutral points produced 76 stimulus classes; 20 probabilistic exemplars per class.

Behavioral: N = 79 participants rated emotion content (5 sliders). fMRI: subset N = 20 completed 18 runs (1,368 stimulus impressions total), event‑related design with optimized timings; participants had prior familiarity from the behavioral task.

Analysis: searchlight RSA compared neural representational dissimilarity matrices (neural RDMs) to a model built from ten predictor RDMs (five stimulus‑feature RDMs; five emotion‑judgment RDMs). Multiple regression RSA produced R²_adj, b‑weights, and Spearman correlations; intermodal RSA and a model‑free region similarity permutation test provided converging evidence.

### Key Findings
- Behavioral ratings clustered tightly around stimulus classes, validating the stimulus design.
- A single model (feature + emotion‑judgment RDMs) explained patterns in visual cortex during animation and auditory cortex during music, supporting H1 (shared representational geometry across separate sensory regions).
- Peaks: left medial lingual gyrus (animation) and right anterior superior temporal gyrus (music) (mean R²_adj ≈ 0.15). Model‑free tests showed these region pairs more similar than expected by chance (r = 0.68, p < .001).
- pSTG showed overlapping model fits across participants, supporting H2 (a supramodal hub) in a subset of participants.
- Both stimulus‑feature predictors and emotion‑judgment predictors were significant contributors, supporting coexistence of the **simple features** (A1) and **environmental conjunctions** (A2) hypotheses.
- Exploratory intermodal RSA revealed visual areas (including left lingual gyrus) that represented stimuli presented in the non‑preferred modality (auditory), although modality‑specific activity remained dominant.

### Interpretation & Significance
The brain appears to construct a cross‑modal representational geometry that maps changes in stimulus features to changes in perceived emotion. This geometry lives both in modality‑specific sensory cortices (putting music and movement in common metric space) and, in some participants, in posterior superior temporal cortex as a supramodal node. Mechanistically, sensory areas code both elemental features and feature conjunctions that are informative about emotion; together these representations may enable rapid, "direct" perception of social signals and reduce reliance on slow inferential processing.

### Computational‑Social‑Cognitive‑Scientist Hat
- **Kurt Lewin**: He'd view this as formalizing how the person/environment relationship is encoded — representations (R) transform environmental dynamics into behavior‑relevant coordinates (B = f(P,E,R)).
- **David Marr**: Satisfied — the paper maps the *computational* goal (recover emotion across senses), proposes an *algorithmic* geometry (RDMs, feature-conjunctions), and localizes *implementational* substrates (lingual gyrus, STG/pSTG).
- **Egon Brunswik**: Would appreciate the ecological‑validity emphasis — using naturalistic, probabilistic feature mixtures and exploiting environmental covariation (conjunctive cues) to support perception.

### Teaching Hooks
- Play a matched music clip and show the ball animation for a prototypical emotion and ask students to rate emotion; then reveal the RSA result that sensory cortex represents them in similar metric space.
- Analogy: representational geometry is like a city map where distances (not raw coordinates) tell you how similar neighborhoods (stimuli) feel.

### Pedagogical Lens
- Conceptual difficulty: **3/5** (RSA and noise‑ceiling ideas require careful explanation).
- Prerequisites: multivariate neural patterns, correlation distance, basics of RSA, and notions of crossmodal processing.
- Common misconceptions: (1) “Supramodal” means only association cortex — here sensory cortices also share geometry; (2) direct perception implies no higher‑level inference — the paper argues for coexistence of both.
- Discussion prompt: How would you design a cross‑cultural test to separate iconic (shared) feature mappings from culturally learned conventions?

### Connections
Links to Sievers et al. (2013, 2019) on crossmodal structure, work on pSTS/pSTG in action and emotion understanding, and to predictive processing accounts where priors tune sensory representations.

### Key Quotes or Phrases
- "Auditory and visual cortex represent emotional music and movement in comparable terms."
- "Sensory brain regions represent conjunctions of task‑relevant features, reducing the need for downstream inferential processing."

### Concept Graph
- Stimulus features (speed, jitter, consonance, size, up/down) → sensory representational geometry (because distance in feature space maps to neural pattern distance).
- Sensory representational geometry → emotion judgments (because configural combinations align with perceived emotions).
- pSTG (supramodal) ↔ sensory cortices (facilitates crossmodal comparison and integration).
  - **Representation:** The format or structure by which the brain encodes information about the world. **Related Concepts:** cross-modal dynamics, neural geometry.
  - **Cross-modal dynamics:** How information from different sensory modalities (vision, audition) interacts and is integrated in the brain. **Related Concepts:** representation, supramodal representation.
  - **Mentalizing:** The process of reasoning about others' mental states; emotion perception from music and movement supports social inferences. **Related Concepts:** theory of mind, social cognition.
  - **Marr's levels:** David Marr's framework for analyzing cognitive systems at computational, algorithmic, and implementational levels. **Related Concepts:** computational modeling, levels of analysis.
  - **Animacy:** The perception of whether something is alive or capable of self-motion; related to detecting goal-directed movement. **Related Concepts:** biological motion, agency perception.

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

### Teaching Hooks
- Live in-class synchrony demo (clap-in-time) to feel affiliation effects.  
- Analogy: coupled metronomes synchronizing — short video demo.

### Pedagogical Lens
- **Conceptual difficulty:** 3–4/5.  
- **Pre-reqs:** basic dynamics (phase, frequency), predictive coding, RSA/hyperscanning basics.  
- **Common misconception:** neural synchrony ≠ merging minds; it’s correlation (sometimes causally relevant).

### Connections
Ties to Predictive Mind, Biological Motion (as interaction cue), Cross-Modal Dynamics, and empirical synchrony literature (e.g., Sievers et al., Wheatley et al. 2012).  

### Key Quotes or Phrases
- “Interaction is not simply two isolated minds added together — it is an emergent process of coupling.”  

### Concept Graph
Action timing ↔ partner prediction (aligned timing reduces mutual prediction error); Cross-modal dynamics → shared meaning; Neural coupling ↔ behavioral synchrony.

### Relevant Terms
**Existing Terms Used:** Synchrony; Predictive Mind; Cross-Modal Dynamics; Representation.  

---

## 2024 — Jolly, E., & Chang, L. (2024). The Flatland Fallacy: Over‑reliance on low‑dimensional explanations in social cognition. *Preprint.*

**Full Citation:** Jolly, E. & Chang, L. (2024). The Flatland Fallacy: Over‑reliance on low‑dimensional explanations in social cognition. *(Preprint / Conference paper — see uploaded PDF).*

**Topic Tags:** Flatland Fallacy, mentalizing, representation, naturalistic behavior, predictive models

### Core Question / Problem
Why do many models in social cognition over‑simplify complex social phenomena (the "Flatland Fallacy") and what are the consequences for theory and experiment? The paper diagnoses the problem and proposes remedies centered on richer representations and naturalistic tasks.

### Conceptual or Computational Framework
The authors argue from a computational‑representational standpoint: social cognition requires multi‑dimensional, structured representations (causal, compositional, temporal) and algorithms that operate within realistic task worlds. Marr’s levels appear as a guiding frame: computational aim (predict others), algorithmic representation (compositional generative models / transition structure), and implementational plausibility (neural dynamics that can approximate required inference).

### Methods Overview
The paper mixes argument, illustrative simulations, and re-analyses of existing datasets. Core methodological recommendations include moving to naturalistic stimuli, analyzing transition structure in behavior streams, and evaluating models on their ability to generalize across contexts.

### Key Findings
- Low‑dimensional summaries (e.g., single scalar biases) often miss structural constraints that explain why behaviors generalize.
- Transition structure — knowledge about how states evolve — is a powerful, testable signal for prediction in social contexts.
- Rich generative models (hierarchical, compositional) better capture one‑shot learning and inference about others’ goals.
- Empirical tests require time‑continuous tasks, richer annotations, and model‑based behavioral signatures rather than simple aggregate statistics.

### Interpretation & Significance
The Flatland Fallacy critique pushes the field to (1) adopt richer representational hypotheses, (2) design tasks that reveal structural inferences (not just point estimates), and (3) adopt cross‑disciplinary standards (shared tasks, datasets, model tests) akin to Kriegeskorte et al.’s recommendations for cognitive computational neuroscience.

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: would endorse emphasis on person × environment (task worlds) interactions.
- Marr: would require explicit separation of levels and formal definitions of representations.
- Brunswik: would welcome the call for ecological sampling and attention to probabilistic cues.

### Teaching Hooks
- Recreate a tiny “Flatland” example: simulate two agents with different internal state spaces and show how a low‑dimensional reading collapses crucial differences.
- Classroom exercise: ask students to design a one‑shot inference task where only a compositional generative model succeeds.

### Pedagogical Lens
- Difficulty: 4/5
- Prereqs: Bayesian inference, basic RL, simple generative models.
- Misconceptions: “more dimensions = overfitting” — clarify role of inductive bias and structured representations.

### Connections
- Ties to Predictive Mind, Generative Models, Transition Structure, and representational analyses.

### Key Quotes or Phrases
- “Reducing social cognition to a few axes risks throwing away the very structure that enables prediction.”  
- “Naturalistic tasks reveal the transition structure that low‑dimensional summaries obscure.”

### Concept Graph
- Rich representations → better generalization because they capture causal & compositional structure.
- Transition structure → predictive accuracy → behavioral adaptation.

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

### Teaching Hooks
- Assign students to annotate a short social video for goal transitions and test which model (simple RL vs hierarchical generative) predicts human annotations.

### Pedagogical Lens
- Difficulty: 4/5
- Prereqs: Bayesian models, basic deep learning, experimental design for naturalistic data.
- Misconception: Naturalistic = messy/unusable. Counter by showing how structure can be extracted and constrained by models.

### Connections
- Bridges Predictive Mind, Flatland Fallacy critique, and Kriegeskorte et al.’s call for task‑performing models.

### Key Quotes or Phrases
- “To explain natural behavior we must meet naturalistic data on its own terms: temporally rich, multimodal, and socially structured.”

---

## 2025 — Moskowitz, D. (2025). Introduction to social cognition and social inference. *In Social Cognition Textbook.*

**Full Citation:** Moskowitz, D. (2025). Introduction to social cognition and social inference. *(Uploaded PDF — introductory chapter).*

**Topic Tags:** social cognition, attribution, mentalizing, predictive mind, ecological tasks

### Core Question / Problem
What are the core mechanisms by which people infer others’ mental states and predict social behavior? This introductory piece frames social cognition as an interplay of perceptual cues, internal generative models, and contextual constraints.

### Conceptual or Computational Framework
The chapter frames social inference as probabilistic, generative, and structured: perceivers combine sensory evidence with priors (about agents, goals, and social norms) to infer latent mental states. Marr’s levels appear implicitly: computational goals (predict others), algorithmic representations (beliefs, goals, transition models), and neural implementation (brain regions/networks for mentalizing).

### Methods Overview
Surveys common experimental paradigms: Heider & Simmel animations, false‑belief tasks, point‑light biological motion, and more naturalistic observation paradigms. Emphasizes combining behavioral measures with neuroimaging and model‑based analyses.

### Key Findings / Themes
- Mentalizing is often automatic, triggered by animacy/agency cues; attribution processes map perceived actions onto candidate mental states.
- Representational richness (causal and temporal structure) supports fast generalization and prediction.
- Laboratory tasks illuminate mechanisms but can miss dynamics found in richer, temporally extended social interactions.

### Interpretation & Significance
As an introduction, the chapter situates social cognition within broader computational perspectives (predictive mind, generative models) and motivates a research program that integrates formal models with ecological methods.

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: the chapter’s emphasis on person×environment echoes field theory.
- Marr: would call for formalizing the computational goal and deriving algorithms.
- Brunswik: would emphasize sampling of cues across contexts.

### Teaching Hooks
- Use Heider & Simmel to illustrate how simple motion cues elicit rich attributions.
- Quick in‑class experiment: show point‑light walkers and ask for inferred emotion/intent.

### Pedagogical Lens
- Difficulty: 2.5/5
- Prereqs: basic probability, experimental design.
- Misconceptions: Attributions are always deliberative — many are rapid and automatic.

### Connections
- Directly ties to Predictive Mind, Attribution Theory, Mentalizing, and the Flatland Fallacy critique.

### Key Quotes or Phrases
- “Perception of agency and animacy is often the perceptual doorway through which more elaborate belief‑attribution is built.”

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

## n.d. — Dennett, D. C. (n.d.). A Précis of The Intentional Stance. *Philosophical Review.*

**Full Citation:** Dennett, D. C. (Précis). A Précis of *The Intentional Stance*.

**Topic Tags:** intentional stance, Searle critique, heuristic overlay, consensus in philosophy of mind

### Core Question / Problem
Why is the intentional stance defensible as a pragmatic, heuristic strategy given critiques (e.g., Searle's Chinese Room) that demand metaphysical grounding?

### Conceptual or Computational Framework
Dennett argues the stance is a "heuristic overlay" that captures a community of practices; disagreements often reflect overstatements rather than deep problems. The defense emphasizes explanatory power and empirical adequacy over metaphysical commitments. 

### Methods Overview
Essay‑length précis with commentary on contemporary debates (Sellars, Quine, Searle, Fodor) and notes on the consensus shifting toward a moderate, pragmatic view.

### Key Findings
- Responds to Searle: even if biochemistry produces intentionality, that doesn't resolve the epistemic/practical reasons we adopt the stance.   
- Philosophers are converging on seeing intentional attribution as a useful heuristic rather than a metaphysical claim. 

### Interpretation & Significance
The Précis helps students situate Dennett historically and shows why the Intentional Stance remains influential: it provides an operational toolkit for prediction and explanation across domains (AI, economics, psychology). 

### Teaching Hooks
- Pair the précis with the 1971 article and Searle’s Chinese Room thought experiment for an in‑class debate.

---

## n.d. — Greifeneder, R. (n.d.). Chapters 1–2. *Social Cognition: How Individuals Construct Social Reality.*

**Full Citation:** Greifeneder, R. (n.d.). Chapters 1–2. *Social Cognition: How Individuals Construct Social Reality.*

**Topic Tags:** social cognition, top‑down vs bottom‑up processing, context dependency, attention, adaptation, heuristics

### Core Question / Problem
How is social cognition distinct from general cognitive processing? Greifeneder argues social cognition is specialized for context‑sensitive, adaptive processing that supports fast, effective behavior in complex social environments.

### Conceptual or Computational Framework
The chapters frame social cognition as an adaptive information‑processing system: constrained resources force tradeoffs (speed vs accuracy), encouraging use of heuristics, top‑down priors, and socially tuned representations. Map to Marr’s levels: computational (goals: adaptive social prediction and coordination), algorithmic (heuristics, schemas, attention allocation, top‑down/bottom‑up interplay), implementational (neural attention networks implicit but not specified). See course glossary on Predictive Mind and Representation for framing.  

### Methods Overview
These are textbook chapters — synthetic review and didactic examples (e.g., the Wason selection task framed as social contract; gorilla inattentional blindness example). Empirical touchpoints are cited throughout (Cosmides on social‑contract improvements to reasoning; classic illusions showing context dependence).

### Key Findings
- Social context dramatically reshapes the information people use (Wason selection results; context turns hard logic into solvable problems).   
- Perception and judgment are highly context dependent and use top‑down construals to be “good enough” for social action.   
- Attention and memory are organized around socially relevant goals: we omit irrelevant detail and amplify trait‑consistent information via schemas and motivated processing.

### Interpretation & Significance
The chapters provide an integrated argument that social cognition is not merely “cognition + social stimuli” but often uses distinct adaptive procedures (heuristics, priors) that make human social performance efficient. This supports a predictive/representational view of social perception: representations and priors scaffold rapid social inferences (links to Generative Model and Predictive Mind in the course glossary).  

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: B = f(P,E), extended — add R (representations) to explain context sensitivity and goal‑directed construals.   
- Marr: Computational goal = predict social outcomes; algorithmic = heuristics and schemas; implementational = attention systems and cortical circuits (not deeply specified in these chapters).   
- Brunswik: Emphasize ecological validity — social cues are noisy, so cue‑utilization matches the ecological demands described.

### Teaching Hooks
- Show the gorilla video (inattentional blindness) and compare responses.  
- Give Wason tasks in social vs non‑social framing to demonstrate context effects (Box 1.1). 

### Pedagogical Lens
- Prereqs: basic perception, attention, and schemas.  
- Common misconceptions: "People always reason logically" — corrected by social framing effects.  
- Discussion prompt: When is a heuristic adaptive vs harmful in social settings?

### Connections
- Links to Predictive Mind, Generative Models, Representation (course glossary). 

### Key Quotes or Phrases
- "Social cognition needs to be highly adaptive and sensitive to the requirements of a situation." 

### Concept Graph
- Social context → activates priors (why?) → changes attention allocation → alters judgment/outcome.

---

## n.d. — Moskowitz, D. S. (n.d.). We Create Internal Mental Representations of External Reality. *In Social Cognition Textbook, Chapter 2.*

**Full Citation:** Moskowitz, D. S. (n.d.). We Create Internal Mental Representations of External Reality. *In Social Cognition Textbook, Chapter 2.*

**Topic Tags:** Schemas, Prototypes & Exemplars, Embodied cognition, Mindsets

### Core Question / Problem
How are social knowledge and categories represented (schemas, prototypes, exemplars), and how do these representations shape perception, memory, and behavior?

### Conceptual or Computational Framework
The chapter presents a representational‑processing framework: representations (schemas, exemplars, prototypes, frames, scripts) mediate perception and action. It highlights interactions between bottom‑up associative learning and top‑down schema effects (priors), consistent with predictive processing accounts.

### Methods Overview
Survey of classic experiments (e.g., Bartlett, Markus self‑schema studies, Cohen role schema work) and more modern experimental paradigms (priming, subliminal triggers, IF→THEN relational elicitation).

### Key Findings
- Representations are fuzzy, probabilistic, and can be organized as prototypes or exemplars; which representation is used depends on familiarity and context.
- Self‑schemas facilitate encoding and retrieval for self‑relevant traits (faster RTs, richer recall).
- Embodied cognition: bodily states (temperature, posture, facial muscles) can implicitly influence social judgments (warmth, affect), often outside awareness.
- Ideomotor/priming effects demonstrate that activated representations can trigger matching behaviors (e.g., elderly stereotype priming slows walking); but replication crises temper some strong claims.

### Interpretation & Significance
The chapter stitches together classical schema theory with emerging embodied and automaticity findings. Pedagogically it gives students an operational toolkit to think about how knowledge structures influence perception and action, and how mindsets and construal level moderate processing.

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: schemas are part of R in B = f(P,E,R) and shape goal‑directed action.
- Marr: computational goal = compress and infer category membership; algorithmic = exemplar matching vs prototype probability estimation.
- Brunswik: highlights cue validity and IF→THEN relations for relational theories.

### Teaching Hooks
- Demonstration: cold vs hot cup (embodied warmth) and subsequent social judgments (replicable conceptual discussion).
- Quick in‑class priming: show how schemas bias memory of a short vignette.

### Pedagogical Lens
- Pre‑requisites: basic memory and category theory, priming concepts
- Common misconceptions: overinterpreting priming/embodiment as always large; discuss replication and boundary conditions.
- Discussion prompt: When will exemplar vs prototype representations dominate?

### Connections
- Links to Heider’s animacy (schemas for agents), Mitchell’s Marr framing (representations as algorithmic objects), and later lectures on predictive models.

### Key Quotes or Phrases
- “Schemas serve as filters that make stimuli knowable and actionable.”  
- “Embodied states often trigger metaphorically linked social inferences outside awareness.”

### Concept Graph
- Experience → Associations → Schema (prototype/exemplar) → Perception & Memory biases → Behavior

---

## n.d. — Moskowitz, G. B. (n.d.). Introduction to Social Cognition. *In Social Cognition Textbook, Chapter 1.*

**Full Citation:** Moskowitz, G. B. (n.d.). Introduction to Social Cognition. *In Social Cognition Textbook, Chapter 1.*

**Topic Tags:** motivated reasoning, self‑esteem maintenance, epistemic needs, just‑world hypothesis, impression formation

### Core Question / Problem
How do motivational forces — particularly needs to maintain self‑esteem and a sense of control — shape basic social cognition (impression formation, attribution, memory)?

### Conceptual or Computational Framework
Moskowitz frames social cognition as a goal‑directed process where epistemic and self‑protective motives bias information encoding and causal attribution. At Marr’s levels: computational = preserve self‑concept while making valid social predictions; algorithmic = biased sampling, defensive attribution, selective discounting of disconfirming evidence; implementational = cognitive strategies like selective attention and memory reconsolidation. 

### Methods Overview
Chapter summarizes classic experiments (e.g., Miller 1976 feedback paradigm; Sicoli & Ross 1977 manipulated success/failure feedback) and contemporary work showing how observers discount threatening information and question source reliability when feedback is negative.

### Key Findings
- People protect self‑esteem by reinterpreting negative feedback as situational (external attribution) and positive feedback as internal (ability).   
- When observers give threatening feedback, perceivers often attack the observer’s credibility rather than update their self‑view — a motivated reasoning strategy.   
- Epistemic needs shape impressions even from sparse or ambiguous input (creating meaning where objective evidence is thin).

### Interpretation & Significance
The chapter foregrounds motivation as central to social inference: cognitive mechanisms (attention, memory, attribution) are not neutral processors but are tuned by goals. This reframes “errors” in social judgment as adaptive responses to protect identity and manage uncertainty — linking to course themes of Representations and Predictive Mind (priors shaped by motivation). 

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: Motives are part of the life‑space that shape behavior (B = f(P,E,R)).   
- Marr: Computational goal includes self‑preservation; algorithmic implementations are biased sampling and selective memory.

### Teaching Hooks
- Recreate Miller’s feedback manipulation as a classroom poll; compare reactions to positive vs negative feedback.  
- Discuss modern echo‑chamber phenomena (social media) as institutionalized motivated reasoning (Moskowitz cites contemporary social media work). 

### Pedagogical Lens
- Prereqs: Attribution theory, memory basics.  
- Misconception: People are primarily rational when judging self — corrected by motivated‑reasoning literature.

### Connections
- Links to Attribution Theory, Mentalizing, and Predictive Mind (priors shaped by motivation). 

### Key Quotes or Phrases
- "When the observer states the participant is responsible for a success, the participant judges the observer accurate; for failures, the observer is judged biased." 

### Concept Graph
- Threatening feedback → motivated discounting → preserves self‑esteem → alters social judgment.

---

## n.d. — Pennington, D. (n.d.). History of Social Cognition. *In Social Cognition Textbook.*

**Full Citation:** Pennington, D. (n.d.). History of Social Cognition. *In Social Cognition Textbook.*

**Topic Tags:** Field theory, Behaviorism, Cognitivism, Constructivism, Timeline terms

### Core Question / Problem
What historical schools of thought shaped the emergence of social cognition (behaviorism → Gestalt/cognitivism → computational cognitive science), and how do these lineages inform contemporary approaches?

### Conceptual or Computational Framework
Historical synthesis: maps intellectual lineage from empiricism & behaviorism through gestalt (Asch, Heider, Bartlett) to Marr’s levels and the predictive mind. Emphasizes how representational commitments (schemas, theories) reintroduced internal structure to explain social behavior.

### Methods Overview
Historical narrative drawing on primary papers and classical experiments (Asch impression formation, Bartlett memory work, Heider’s attributions).

### Key Findings / Claims
- Behaviorism sidelined mental explanations; Gestalt and cognitive pioneers reintroduced mental structure and meaning.
- Lewin’s field theory (B = f(P, E)) anticipated modern representation‑inclusive models (add R).
- The computational turn formalized representation and algorithmic levels (Marr), enabling modern generative/predictive frameworks.

### Interpretation & Significance
Provides students context: why contemporary social cognition focuses on representations, algorithms, and prediction. It explains conceptual shifts and why certain methods (reaction times, narration, neuroimaging) rose to prominence.

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: situates behavior as emergent from person and environment; modern accounts add explicit representation R.
- Marr: historical narrative culminates in Marr’s levels as a synthesis tool.
- Brunswik: historical emphasis on cue validity and ecological sampling is a throughline.

### Teaching Hooks
- Timeline slide: map major milestones (Behaviorism → Gestalt/Cognitivism → Computational Cognitive Science → Predictive Mind).
- Classroom debate: Was the cognitive revolution a reinstatement of “folk psychology” or a methodological advance?

### Pedagogical Lens
- Pre‑requisites: none beyond curiosity
- Misconceptions: that older theories are “wrong” rather than limited in scope.
- Discussion prompt: How did methodological limits of the behaviorist era shape the questions asked in social psychology?

### Connections
- Ties to all course modules: attributions, schemas, mentalizing, predictive models.

### Key Quotes or Phrases
- “Understanding the history clarifies why we now ask what representations do, not whether they exist.”  
- “Lewin’s field theory foreshadows the modern inclusion of Representations in behavior functions.”

### Concept Graph
- Historical movements → theories of mind (schemas, attribution, computation) → modern predictive frameworks