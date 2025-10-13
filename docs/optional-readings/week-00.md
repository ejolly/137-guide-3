# Optional Readings — Introduction

---

## 2024 — Jolly, E., & Chang, L. (2024). The Flatland Fallacy: Over‑reliance on low‑dimensional explanations in social cognition. *Preprint.*

**Full Citation:** Jolly, E. & Chang, L. (2024). The Flatland Fallacy: Over‑reliance on low‑dimensional explanations in social cognition. *Preprint / Conference paper.*

**Topic Tags:** Flatland Fallacy, mentalizing, representation, naturalistic behavior, predictive models

### Core Question / Problem
Why do many models in social cognition over‑simplify complex social phenomena (the "Flatland Fallacy") and what are the consequences for theory and experiment? The paper diagnoses the problem and proposes remedies centered on richer representations and naturalistic tasks.

### Conceptual or Computational Framework
The authors argue from a computational‑representational standpoint: social cognition requires multi‑dimensional, structured representations (causal, compositional, temporal) and algorithms that operate within realistic task worlds. Marr's levels appear as a guiding frame: computational aim (predict others), algorithmic representation (compositional generative models / transition structure), and implementational plausibility (neural dynamics that can approximate required inference).

### Methods Overview
The paper mixes argument, illustrative simulations, and re-analyses of existing datasets. Core methodological recommendations include moving to naturalistic stimuli, analyzing transition structure in behavior streams, and evaluating models on their ability to generalize across contexts.

### Key Findings
- Low‑dimensional summaries (e.g., single scalar biases) often miss structural constraints that explain why behaviors generalize.
- Transition structure — knowledge about how states evolve — is a powerful, testable signal for prediction in social contexts.
- Rich generative models (hierarchical, compositional) better capture one‑shot learning and inference about others' goals.
- Empirical tests require time‑continuous tasks, richer annotations, and model‑based behavioral signatures rather than simple aggregate statistics.

### Interpretation & Significance
The Flatland Fallacy critique pushes the field to (1) adopt richer representational hypotheses, (2) design tasks that reveal structural inferences (not just point estimates), and (3) adopt cross‑disciplinary standards (shared tasks, datasets, model tests) akin to Kriegeskorte et al.'s recommendations for cognitive computational neuroscience.

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: would endorse emphasis on person × environment (task worlds) interactions.
- Marr: would require explicit separation of levels and formal definitions of representations.
- Brunswik: would welcome the call for ecological sampling and attention to probabilistic cues.

### Connections
- Ties to Predictive Mind, Generative Models, Transition Structure, and representational analyses.

### Key Quotes or Phrases
- "Reducing social cognition to a few axes risks throwing away the very structure that enables prediction."
- "Naturalistic tasks reveal the transition structure that low‑dimensional summaries obscure."

### Concept Graph
- Rich representations → better generalization because they capture causal & compositional structure.
- Transition structure → predictive accuracy → behavioral adaptation.

---

## 2006 — Mitchell, J. P. (2006). Mentalizing and Marr: An information‑processing approach to the study of social cognition. *Brain Research.*

**Full Citation:** Mitchell, J. P. (2006). Mentalizing and Marr: An information‑processing approach to the study of social cognition. *Brain Research.*

**Topic Tags:** Mentalizing, Marr's levels, Representations, Predictive mind

### Core Question / Problem
How can Marr's levels (computational, algorithmic, implementational) be usefully applied to "mentalizing" — the process by which perceivers represent and predict others' minds?

### Conceptual or Computational Framework
Mitchell argues for an information‑processing (Marr‑informed) view of mentalizing: (1) computational level—what is the goal? (infer beliefs, desires, likely actions); (2) algorithmic level—what representations / computations map observations to inferred mental states? (generative models, Bayesian inference, heuristics); (3) implementational level—how might these computations be realized neurally (mPFC, TPJ networks implicated). The paper bridges classic social cognition (attribution) with formal models (predictive/generative modeling).

### Methods Overview
The paper is theoretical and integrative: it reviews behavioral evidence, neuroimaging results, and computational proposals that instantiate Marr's levels in social cognition research.

### Key Findings / Claims
- Mentalizing tasks can be decomposed cleanly by Marr's levels, yielding clearer hypotheses and experimental designs.
- Algorithmic proposals include both explicit rule‑based mappings and probabilistic generative models that predict others' behavior from latent mental states.
- Neural data suggest specialized circuitry but do not fully determine algorithmic format; multiple algorithms may be implemented by overlapping brain systems.

### Interpretation & Significance
Mitchell reframes social cognition as computational inference. This matters pedagogically: it offers students a systematic vocabulary (goals, representations, algorithms) and connects classical theories (Heider's attribution) to modern predictive and Bayesian frameworks. It makes clear how one can design experiments to pit algorithmic hypotheses against each other.

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: R (representations) are central; B = f(P,E,R) fits naturally into Marr's algorithmic level.
- Marr: Would applaud the explicit mapping of social goals (why infer mental states) to candidate algorithms (how).
- Brunswik: Would emphasize probabilistic cue‑validity and ecological sampling in building generative models.

### Connections
- Links explicitly to predictive processing, generative models, and neuroimaging work on mPFC/TPJ.

### Key Quotes or Phrases
- "Applying Marr clarifies what questions social neuroscientists should ask: what is being computed, how, and by what machinery?"
- "Mentalizing is best viewed as an inference problem about hidden causes."

### Concept Graph
- Observations → Algorithm (representation: generative model) → Inferred beliefs/desires → Predicted action

---

## n.d. — Greifeneder, R. (n.d.). Chapters 1–2. *Social Cognition: How Individuals Construct Social Reality.*

**Full Citation:** Greifeneder, R. (n.d.). Chapters 1–2. *Social Cognition: How Individuals Construct Social Reality.*

**Topic Tags:** social cognition, top‑down vs bottom‑up processing, context dependency, attention, adaptation, heuristics

### Core Question / Problem
How is social cognition distinct from general cognitive processing? Greifeneder argues social cognition is specialized for context‑sensitive, adaptive processing that supports fast, effective behavior in complex social environments.

### Conceptual or Computational Framework
The chapters frame social cognition as an adaptive information‑processing system: constrained resources force tradeoffs (speed vs accuracy), encouraging use of heuristics, top‑down priors, and socially tuned representations. Map to Marr's levels: computational (goals: adaptive social prediction and coordination), algorithmic (heuristics, schemas, attention allocation, top‑down/bottom‑up interplay), implementational (neural attention networks implicit but not specified). See course glossary on Predictive Mind and Representation for framing.

### Methods Overview
These are textbook chapters — synthetic review and didactic examples (e.g., the Wason selection task framed as social contract; gorilla inattentional blindness example). Empirical touchpoints are cited throughout (Cosmides on social‑contract improvements to reasoning; classic illusions showing context dependence).

### Key Findings
- Social context dramatically reshapes the information people use (Wason selection results; context turns hard logic into solvable problems).
- Perception and judgment are highly context dependent and use top‑down construals to be "good enough" for social action.
- Attention and memory are organized around socially relevant goals: we omit irrelevant detail and amplify trait‑consistent information via schemas and motivated processing.

### Interpretation & Significance
The chapters provide an integrated argument that social cognition is not merely "cognition + social stimuli" but often uses distinct adaptive procedures (heuristics, priors) that make human social performance efficient. This supports a predictive/representational view of social perception: representations and priors scaffold rapid social inferences (links to Generative Model and Predictive Mind in the course glossary).

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: B = f(P,E), extended — add R (representations) to explain context sensitivity and goal‑directed construals.
- Marr: Computational goal = predict social outcomes; algorithmic = heuristics and schemas; implementational = attention systems and cortical circuits (not deeply specified in these chapters).
- Brunswik: Emphasize ecological validity — social cues are noisy, so cue‑utilization matches the ecological demands described.

### Connections
- Links to Predictive Mind, Generative Models, Representation (course glossary).

### Key Quotes or Phrases
- "Social cognition needs to be highly adaptive and sensitive to the requirements of a situation."

### Concept Graph
- Social context → activates priors (why?) → changes attention allocation → alters judgment/outcome.

---

## 2025 — Moskowitz, D. (2025). Introduction to social cognition and social inference. *Social Cognition Textbook.*

**Full Citation:** Moskowitz, D. (2025). Introduction to social cognition and social inference. *Social Cognition Textbook.*

**Topic Tags:** social cognition, attribution, mentalizing, predictive mind, ecological tasks

### Core Question / Problem
What are the core mechanisms by which people infer others' mental states and predict social behavior? This introductory piece frames social cognition as an interplay of perceptual cues, internal generative models, and contextual constraints.

### Conceptual or Computational Framework
The chapter frames social inference as probabilistic, generative, and structured: perceivers combine sensory evidence with priors (about agents, goals, and social norms) to infer latent mental states. Marr's levels appear implicitly: computational goals (predict others), algorithmic representations (beliefs, goals, transition models), and neural implementation (brain regions/networks for mentalizing).

### Methods Overview
Surveys common experimental paradigms: Heider & Simmel animations, false‑belief tasks, point‑light biological motion, and more naturalistic observation paradigms. Emphasizes combining behavioral measures with neuroimaging and model‑based analyses.

### Key Findings / Themes
- Mentalizing is often automatic, triggered by animacy/agency cues; attribution processes map perceived actions onto candidate mental states.
- Representational richness (causal and temporal structure) supports fast generalization and prediction.
- Laboratory tasks illuminate mechanisms but can miss dynamics found in richer, temporally extended social interactions.

### Interpretation & Significance
As an introduction, the chapter situates social cognition within broader computational perspectives (predictive mind, generative models) and motivates a research program that integrates formal models with ecological methods.

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: the chapter's emphasis on person×environment echoes field theory.
- Marr: would call for formalizing the computational goal and deriving algorithms.
- Brunswik: would emphasize sampling of cues across contexts.

### Connections
- Directly ties to Predictive Mind, Attribution Theory, Mentalizing, and the Flatland Fallacy critique.

### Key Quotes or Phrases
- "Perception of agency and animacy is often the perceptual doorway through which more elaborate belief‑attribution is built."

### Concept Graph
- Sensory evidence + Priors → Inferred mental states → Predicted behavior
- Animacy/agency cues → trigger automatic mentalizing

---

## n.d. — Moskowitz, G. B. (n.d.). Chapter 1. *Introduction to Social Cognition.*

**Full Citation:** Moskowitz, G. B. (n.d.). Chapter 1. *Introduction to Social Cognition.*

**Topic Tags:** motivated reasoning, self‑esteem maintenance, epistemic needs, just‑world hypothesis, impression formation

### Core Question / Problem
How do motivational forces — particularly needs to maintain self‑esteem and a sense of control — shape basic social cognition (impression formation, attribution, memory)?

### Conceptual or Computational Framework
Moskowitz frames social cognition as a goal‑directed process where epistemic and self‑protective motives bias information encoding and causal attribution. At Marr's levels: computational = preserve self‑concept while making valid social predictions; algorithmic = biased sampling, defensive attribution, selective discounting of disconfirming evidence; implementational = cognitive strategies like selective attention and memory reconsolidation.

### Methods Overview
Chapter summarizes classic experiments (e.g., Miller 1976 feedback paradigm; Sicoli & Ross 1977 manipulated success/failure feedback) and contemporary work showing how observers discount threatening information and question source reliability when feedback is negative.

### Key Findings
- People protect self‑esteem by reinterpreting negative feedback as situational (external attribution) and positive feedback as internal (ability).
- When observers give threatening feedback, perceivers often attack the observer's credibility rather than update their self‑view — a motivated reasoning strategy.
- Epistemic needs shape impressions even from sparse or ambiguous input (creating meaning where objective evidence is thin).

### Interpretation & Significance
The chapter foregrounds motivation as central to social inference: cognitive mechanisms (attention, memory, attribution) are not neutral processors but are tuned by goals. This reframes "errors" in social judgment as adaptive responses to protect identity and manage uncertainty — linking to course themes of Representations and Predictive Mind (priors shaped by motivation).

### Computational‑Social‑Cognitive‑Scientist Hat
- Lewin: Motives are part of the life‑space that shape behavior (B = f(P,E,R)).
- Marr: Computational goal includes self‑preservation; algorithmic implementations are biased sampling and selective memory.

### Connections
- Links to Attribution Theory, Mentalizing, and Predictive Mind (priors shaped by motivation).

### Key Quotes or Phrases
- "When the observer states the participant is responsible for a success, the participant judges the observer accurate; for failures, the observer is judged biased."

### Concept Graph
- Threatening feedback → motivated discounting → preserves self‑esteem → alters social judgment.
  - **Epistemic Need:** A motivational drive for coherent, controllable explanations that encourages meaning‑making even from weak evidence. **Related Concepts:** Motivated Reasoning, Just‑World Hypothesis.

---
