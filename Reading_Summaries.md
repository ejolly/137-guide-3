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

## 2010 — Epley, N., & Waytz, A. (2010). Mind perception. *In S. T. Fiske (Ed.), Handbook of Social Psychology (5th ed.).*

**Full Citation:** Epley, N. & Waytz, A. (2010). Mind perception. *In S. T. Fiske (Ed.), Handbook of Social Psychology* (5th ed.). Wiley.

**Topic Tags:** mentalizing, mind perception, anthropomorphism, agency, experience, attribution

### Core Question / Problem
When and why do people attribute minds to others (including non-human agents), and what are the psychological consequences of those attributions?

### Conceptual or Computational Framework
This chapter frames mind perception as a two-dimensional representational space — **Experience** (capacity to feel) and **Agency** (capacity to act/plan) — that underlies anthropomorphism and mentalizing. At the computational level, the problem is: given observable behavior, how should a perceiver infer hidden mental-state variables (feelings, intentions) for prediction and social coordination? Algorithmically, people use quick heuristics (similarity, causal uncertainty, need for social connection) and stance-taking (intentional/design/physical) to map observable cues to latent mental attributes. Implementationally, the chapter points to neural correlates (e.g., mPFC) for social inference.

### Methods Overview
This is a theory-and-review chapter synthesizing developmental studies (infancy sensitivity to goal-directed motion), experimental manipulations that trigger anthropomorphism (loneliness, lack of control), neuroimaging contrasts showing differential MPFC activation, and cross-species comparisons. The chapter emphasizes converging behavioral and correlational evidence rather than a single new experiment.

### Key Findings
- People represent minds along two stable dimensions: **Agency** and **Experience**. 
- Perceiver motives (need for understanding, control, or social connection) and perceived target features (human-likeness, unpredictability, similarity) jointly determine mind attributions.
- Attributing mind changes moral treatment: agents are more blameworthy; patients more deserving of moral rights.
- Anthropomorphism can be adaptive (satisfying effectance or social needs) and maladaptive (objectification or moral neglect).

### Interpretation & Significance
Epley & Waytz synthesize scattered literatures into a compact representational model that explains when people ascribe minds and why it matters for moral judgment and social behavior. For the course’s computational lens, their synthesis shows how representational constraints (agency vs experience) guide fast inference strategies that act like approximate generative models for social prediction.

### Computational-Social-Cognitive-Scientist Hat
- Kurt Lewin: This account operationalizes *B = f(P, E)* by showing how perceiver state (P) and environment/target (E) map to representations (R) of mind.
- David Marr: Marr’s computational level = “explain/predict others’ behavior”; algorithmic = the two-dimension heuristic + stance-taking; implementational = social brain circuits (mPFC, TPJ).
- Egon Brunswik: Ecological validity arises from the reliability of cues (human-like motion, contingency).

### Teaching Hooks
- Play a short Heider & Simmel clip (triangles) and ask students to annotate perceived feelings/intentions.
- Analogy: mind perception as a 2‑axis map (agency x experience) — place pets, infants, robots, corporations on the map.

### Pedagogical Lens
- Pre-requisite ideas: Attributions, basic experimental logic, representational models
- Common misconceptions: Anthropomorphism = irrational; in fact it is often goal-directed inference.
- Prompt: "Design a 5-minute experiment that tests whether loneliness increases agency or experience attributions to a household object."

### Connections
- Marr’s levels, intentional stance (Dennett), predictive mind, moral typecasting.

### Key Quotes or Phrases
- "Mind perception organizes in terms of capacity to feel and capacity to plan." 
- "Ascribing a mind confers moral standing and responsibility."

### Concept Graph
- Perceiver motives → (increase) Anthopomorphism because they raise need for effectance.
- Humanlike cues → (increase) Agency/Experience because of cue reliability.
- Mind attribution → (causes) Moral status shifts (rights or blame).

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

**Full Citation:** Greifeneder, R. (Year). Chapters 1–2. *[book/edited volume]*.

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

**Full Citation:** Moskowitz, D. S. — Chapter 2: *We Create Internal Mental Representations of External Reality.* (Chapter PDF provided)

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

**Full Citation:** Moskowitz, G. B. (Year). Chapter 1. *Introduction to Social Cognition.*

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

**Full Citation:** Pennington — *History of Social Cognition* (uploaded PDF; historical chapter)

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