
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

---

