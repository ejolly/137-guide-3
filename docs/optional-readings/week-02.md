# Optional Readings — Week 2

## Blakemore & Decety (2001). From the perception of action to the understanding of intention

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

## Brüne & Brüne-Cohrs (2006). Theory of mind: Evolution, ontogeny, brain mechanisms and psychopathology

**Full Citation:** Brüne, M., & Brüne‑Cohrs, U. (2006). Theory of mind—evolution, ontogeny, brain mechanisms and psychopathology. *Source.*

**Topic Tags:** Theory of Mind, Evolution, Developmental Psychopathology, Social Neuroscience

### Core Question / Problem
How did theory of mind (ToM) evolve and develop in humans, what are its neural substrates, and how do disturbances in ToM relate to psychiatric disorders? The review asks: is ToM an evolved, partially innate capacity tuned by social environment, and how do neural implementations explain both normal and pathological variation?

### Conceptual or Computational Framework
The authors situate ToM as an evolved cognitive adaptation for social complexity. They mix evolutionary explanation (selection for social inference), ontogenetic constraints (long developmental trajectory), and neural-implementation accounts (a distributed social brain: medial prefrontal cortex, STS, ACC, inferior parietal). The framing aligns with Marr's levels: adaptive function (computational), representational/algorithmic proposals (mental state attribution, imitation, biological-motion tracking), and implementational neuroanatomy.

### Methods Overview
This is a synthetic review integrating comparative primate data, developmental studies (false‑belief tasks, infant looking-time), lesion and neuroimaging findings, and clinical studies in autism spectrum disorders, schizophrenia, and personality disorders. The review emphasizes cross-method convergence rather than original empirical data.

### Key Findings
- Phylogeny: Precursors of ToM exist in nonhuman primates (monitoring biological motion, joint attention, mimicry) but human ToM is uniquely elaborated.
- Ontogeny: ToM appears to be scaffolded by early social interaction; infants show precursors (goal attribution), while explicit belief‑attribution develops later and depends on social input.
- Neural mechanisms: A distributed network—medial PFC, temporo‑parietal junction (TPJ)/STS, ACC, and inferior parietal regions—supports different ToM subprocesses.
- Psychopathology: Diverse disorders show selective ToM impairments—autism (developmental delay or impairment), schizophrenia and affective disorders (context‑dependent deficits), and certain personality disorders (atypical attribution biases).

### Interpretation & Significance
The review argues for ToM as both an evolved capacity and a developmentally plastic skill dependent on social experience. Neural specializations reflect modularized operations (e.g., agents' goals vs. beliefs), but are not strictly domain‑specific—variation across disorders suggests overlapping circuits and compensatory processes.

### Computational‑Social‑Cognitive‑Scientist Hat
From a modeling perspective: ToM could be formalized as a generative model that maps hidden mental states to observed actions, with priors shaped by social ecology. Developmental trajectories can be modeled as hierarchical Bayesian learning with limited data early in life, and psychopathology as altered priors or inference noise.

### Connections
Links to Predictive Mind (priors for social inference), Marr's levels (function → algorithm → implementation), and clinical neuropsychology. Also ties to literature on imitation and joint attention as learning mechanisms.

### Key Quotes or Phrases
- "Theory of mind comprises an innate cognitive capacity represented in a dedicated neural network…" (p.1).
- "Psychopathology almost always involves disturbances of social reasoning."

### Concept Graph
- Social complexity → selection pressure → ToM capacity.
  - **Medial PFC / TPJ:** inference about beliefs and traits. **Notable Figures:** Frith, Mitchell. **Related Concepts:** Default mode network; trait inference.
  - **STS / Biological Motion:** input for animacy detection. **Definition:** motion cues that signal agency. **Related Concepts:** Animacy; Intentional stance.

### Relevant Terms
- **Existing Terms Used:** Theory of Mind; Mentalizing; Animacy; Intentional Stance; Predictive Mind; Representation. fileciteturn1file16 fileciteturn1file2
- **New Terms to Add:**
  - **Social Brain Network (as reviewed):** The constellation of medial PFC, TPJ/STS, ACC, and inferior parietal cortex implicated in ToM. **Definition:** neural substrate mapping from perceived behavior to inferred mental states. **Related Concepts:** Default Mode Network; Mentalizing.

---

## Frith & Frith (1999). Interacting minds: A biological basis

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

## Haslam (2006). Dehumanization: An integrative review

**Full Citation:** Haslam, N. (2006). Dehumanization: An Integrative Review. *Personality and Social Psychology Review*, 10(3), 252–264.

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

---

## Moran et al. (2014). Spontaneous mentalizing predicts the fundamental attribution error

**Full Citation:** Moran, J. M., Jolly, E., & Mitchell, J. P. (2014). Spontaneous mentalizing predicts the fundamental attribution error. *Journal of Cognitive Neuroscience, 26*(3), 569–578.

**Topic Tags:** Spontaneous Mentalizing, Fundamental Attribution Error, Default Mode Network, Social Neuroscience

### Core Question / Problem
Why do people tend to favor dispositional explanations (the fundamental attribution error, FAE) even when situational factors are obvious? The paper asks whether spontaneous activation of mentalizing processes and associated neural systems (default mode network) predicts dispositional attributions.

### Conceptual or Computational Framework
The paper frames FAE as a default inference strategy arising from spontaneous activation of mentalizing machinery (intentional stance). They connect dispositional inference to activity in core mentalizing regions (medial PFC, TPJ) and situational inference to limbic/temporal regions (e.g., amygdala, temporal pole).

### Methods Overview
Multi-experiment approach combining fMRI with behavioral attribution tasks. Key paradigm: participants read ambiguous scenarios and later provide dispositional vs. situational explanations while brain activity (and resting-state network architecture) is measured. Contrasts isolate brain regions predicting dispositional vs. situational attributions.

### Key Findings
- Spontaneous recruitment of core mentalizing regions (dmPFC, TPJ) during initial reading predicted later dispositional attributions.
- These regions are part of the default mode network, whose high baseline activity may bias perceivers toward dispositional inference.
- Individuals with reduced default network activity (e.g., autism) may show reduced FAE — supporting a mechanistic link between spontaneous mentalizing and attribution bias.

### Interpretation & Significance
The study reframes FAE not as merely a cognitive shortcut or effort‑saving heuristic but as a consequence of an adaptive, automatically engaged system for understanding others. The default network's tonic activity may create a processing bias: adopting the intentional stance is the brain's baseline approach to social input.

### Computational‑Social‑Cognitive‑Scientist Hat
Model implication: a prioritized prior favoring dispositional causes—implemented via default network baseline—requires cognitive effort to override (situational re‑weighting). Models of social inference should include tonic activation of mind‑attribution priors and a control process to integrate situational evidence.

### Connections
Bridges attribution theory, Default Mode Network research, and developmental work on autism. Directly links to the Brüne review's neural localization and Thornton's work on person representations via mental states.

### Key Quotes or Phrases
- "A lifetime of reflexively considering others' mental states… creates a default strategy for understanding other minds." (Moran et al., p.573). fileciteturn1file6

### Concept Graph
- Default Mode Network baseline activity → spontaneous mentalizing → dispositional attributions (FAE).
  - **dmPFC / TPJ:** spontaneous trait inference. **Related Concepts:** Mentalizing; Intentional stance.

### Relevant Terms
- **Existing Terms Used:** Mentalizing; Intentional Stance; Default Mode Network (as discussed in course readings). fileciteturn1file6 fileciteturn1file2
- **New Terms to Add:**
  - **Tonic Mentalizing Bias:** baseline neural propensity (default network activity) to interpret actions via dispositional inferences. **Definition:** an a priori weighting toward internal-state explanations that must be modulated by evidence. **Related Concepts:** Predictive Mind; Default Mode Network.

---

## Pitcher & Ungerleider (2021). Evidence for a third visual pathway specialized for social perception

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

## Premack & Woodruff (1978). Does the chimpanzee have a theory of mind?

**Full Citation:** Premack, D., & Woodruff, G. (1978). Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences.*

**Topic Tags:** theory of mind (ToM), mentalizing, comparative cognition, experimental logic

### Core Question / Problem
Can non-human primates (chimpanzees) attribute mental states (beliefs, desires, intentions) to others — i.e., do they possess a theory of mind?

### Conceptual or Computational Framework
Premack & Woodruff frame ToM as an ability to infer hidden mental states from observed behaviour and situational context. Experimentally, they probe whether chimps can predict another agent's behavior based on the agent's (possibly false) beliefs — a classic computational question about representing other minds.

### Methods Overview
Longitudinal/descriptive experimental paradigms: observational reports and structured tasks where chimpanzees interact with informed or uninformed trainers separated by mesh partitions; senders and receivers manipulate signals to test whether chimpanzees understand others' knowledge states.

### Key Findings
- Evidence suggested some chimpanzees could flexibly use information about another's knowledge or intention (e.g., pointing strategies to inform a benevolent trainer or to deceive a selfish one).
- Results were suggestive but not definitive; Premack & Woodruff urged more controlled tests (e.g., false-belief style tasks) to settle whether chimp performance reflects mindreading or sophisticated behavioral reading.

### Interpretation & Significance
Premack & Woodruff's paper launched ToM as an empirical question and a research program. It reframed comparative cognition: rather than assuming human uniqueness, it asked what computational representations (if any) animals use to predict others. The paper set the stage for decades of follow-ups that refined tasks (false-belief tasks, looking-time measures) and clarified species differences.

### Computational–Social–Cognitive–Scientist Hat
- Lewin: behavior depends on person and environment; Premack's tasks manipulated informational environments to reveal internal representations.
- Marr: computational goal = predict other's behavior; algorithmic question = what representations/operations support this? Implementational = neural substrates across species.
- Brunswik: stresses ecological validity — animal tests must respect natural communicative contexts (senders/receivers).

### Connections
- Directly ties to the course glossary's ToM entry (Premack & Woodruff 1978) and subsequent human infant literature.

### Key Quotes or Phrases
- "The test is quite simple." (description of sender/receiver setup) — a good lecture vignette.

### Concept Graph
- Observed behavior + context → inferred knowledge state → predictive behavior (sender/receiver strategy)
- Controlled manipulations → distinguish mentalizing vs behavior-reading

---

## Sievers et al. (2021). Visual and auditory brain areas share a representational structure that supports emotion perception

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

### Connections
Links to Sievers et al. (2013, 2019) on crossmodal structure, work on pSTS/pSTG in action and emotion understanding, and to predictive processing accounts where priors tune sensory representations.

### Key Quotes or Phrases
- "Auditory and visual cortex represent emotional music and movement in comparable terms."
- "Sensory brain regions represent conjunctions of task‑relevant features, reducing the need for downstream inferential processing."

### Concept Graph
- Stimulus features (speed, jitter, consonance, size, up/down) → sensory representational geometry (because distance in feature space maps to neural pattern distance).
- Sensory representational geometry → emotion judgments (because configural combinations align with perceived emotions).
- pSTG (supramodal) ↔ sensory cortices (facilitates crossmodal comparison and integration).

### Relevant Terms
**Existing Terms Used:**
- representation
- cross‑modal dynamics
- mentalizing (related, as emotion perception supports social inferences)
- Marr's levels
- animacy

---

## Thornton & Tamir (2021). The organization of social knowledge is tuned for prediction

**Full Citation:** Thornton, M. A., & Tamir, D. I. (2021). The Organization of Social Knowledge Is Tuned for Prediction. *[journal]*.

**Topic Tags:** Predictive Mind, Mentalizing, Transition Structure, Generative Model, Representation, Neural geometry

### Core Question / Problem
How is social knowledge—people's knowledge of actions, mental states, and traits—organized so that observers can rapidly predict other people's future mental states and actions? The paper asks whether conceptual (psychological) and neural representations are structured not merely to describe people but specifically to support prediction of their future states.

### Conceptual or Computational Framework
Thornton & Tamir adopt a predictive-processing / generative-models framing: people encode compact, low‑dimensional maps of social concepts (states, traits, actions) that emphasize transitions and regularities useful for forecasting. Mapping to Marr's levels: at the computational level the goal is accurate social prediction; at the algorithmic level, knowledge is organized as shared dimensions (e.g., valence, sociality, competence/agency) and transition structures; at the implementational level, overlapping neural codes in the social brain (mPFC, parietal cortex, STS/ATL) realize these maps. The work emphasizes *transition structure*—probabilities linking states/actions across time—as the algorithmically relevant representation for prediction.

### Methods Overview
Across several empirical tests (behavioural norms, neural decoding, and representational analyses), the authors: collect large-scale ratings of mental states/actions and their transition probabilities; build conceptual spaces (dimensions and distance metrics) for states, traits, and actions; and test whether those spaces align with neural representational geometry using fMRI decoding and pattern analyses. Core manipulations examine (a) dimensionality of social spaces, (b) whether transition statistics are encoded, and (c) cross-domain similarity (do trait and state maps share dimensions?). Participants were typical lab subjects for rating tasks; fMRI participants performed social judgment tasks while activity patterns were measured and decoded.

### Key Findings
- Social knowledge is organized along a small set of shared dimensions (valence, sociality/impact, competence/agency) that recur across mental states, traits, and actions.
- Transition statistics—how likely one mental state or action leads to another—are represented in conceptual spaces and predict behavioral judgments about what will happen next.
- Neural patterns in the canonical 'social brain' reflect these dimensions and support decoding across domains: the same dimensions that structure conceptual maps are discoverable in mPFC, parietal areas, and STS/ATL, suggesting a shared neural code for dimensions useful for prediction. These overlapping maps allow trait representations to be reconstructed from habitual state patterns (i.e., counting states explains trait impressions).

### Interpretation & Significance
The paper argues that the mind organizes social knowledge primarily for *prediction* rather than mere description. This reframes classical person perception (traits vs. states) and theory‑of‑mind research: rather than separate modules for trait inference and state reasoning, overlapping low‑dimensional maps and transition structures let observers reuse the same code to anticipate future states and actions. For social‑cognitive researchers and computational cognitive scientists, this supplies a mechanistic account of how generative models for other minds might be represented and learned.

### Computational‑Social‑Cognitive‑Scientist Hat
- Kurt Lewin: Would appreciate recasting behavior as driven by internal representations (R) interacting with person and environment—these maps operationalize R.
- David Marr: The paper is explicit about Marr's levels—clear computational goal (predict others), algorithmic representation (dimensions + transition matrix), and testable implementational predictions (neural geometry).
- Egon Brunswik: The emphasis on transition probabilities is Brunswikian—perceivers exploit probabilistic ecological regularities to make inferences under uncertainty.

### Connections
Links strongly to Predictive Mind, Generative Models, Mentalizing, the ACT‑FAST taxonomy, and prior Thornton/Tamir work on the 3D mind model (rationality, social impact, valence).

### Key Quotes or Phrases
- "Social knowledge is organized to support prediction: dimensions and transition structure make the future statistically tractable."
- "The same low‑dimensional code underlies trait and state representations, enabling efficient forecasting of other people."

### Concept Graph
- Dimensions (valence, sociality, competence) → structure conceptual maps.
- Transition probabilities + conceptual maps → enable prediction of next states/actions.
- Neural geometry (mPFC, STS/ATL) ↔ encodes the same dimensions → allows readout of predictions.

### Relevant Terms
**Existing Terms Used:** Predictive Mind; Generative Model; Representation; Transition Structure; Mentalizing; Marr's Levels.

**New Terms to Add:**
- **ACT‑FAST Taxonomy:** A compact action taxonomy outlining dimensions (e.g., Agency, Competence, Temporal features) used to scaffold action prediction across domains. **Notable Figures:** Thornton & Tamir. **Related Concepts:** Action representation; Transition Structure.

---

## Thornton et al. (2019). The brain represents people as the mental states they habitually experience

**Full Citation:** Thornton, M. A., Weaverdyck, M. E., & Tamir, D. I. (2019). The brain represents people as the mental states they habitually experience. *Nature Communications, 10*, 2291.

**Topic Tags:** Person Representation, Summed State Hypothesis, Neural Traits, Social Prediction

### Core Question / Problem
How are person‑specific representations organized in the brain? Do we represent people by stable trait dimensions, or by the *frequency‑weighted sum* of the mental states they habitually experience (the "summed state" hypothesis)?

### Conceptual or Computational Framework
The summed state hypothesis frames person representation as a linear generative model: person pattern ≈ Σ frequency(state_i) × pattern(state_i). This is contrasted with trait‑based models (low‑dimensional trait vectors). The analysis spans Marr's levels: computational goal (represent idiosyncratic persons), algorithmic hypothesis (summed state encoding), and implementational test (fMRI pattern reconstruction).

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

### Connections
Links to Thornton & Tamir's broader program (mental‑state centric models), trait psychology (Whole‑Trait theory), and neural pattern‑based approaches to social cognition. Also relates to predictive processing: person models provide priors that shape state prediction.

### Key Quotes or Phrases
- "People are represented as the sums of the mental states they experience." fileciteturn1file8

### Concept Graph
- Person representation = Σ frequency(state) × state pattern.
  - **Summed State Hypothesis:** compositionally builds person encodings from state representations. **Notable Figures:** Tamir, Thornton. **Related Concepts:** Representation; Predictive Mind.

### Relevant Terms
- **Existing Terms Used:** Representation; Mentalizing; Predictive Mind; Transition Structure. fileciteturn1file12
- **New Terms to Add:**
  - **Summed State Representation:** A compositional person encoding defined as the frequency‑weighted sum of mental‑state representations. **Definition:** A compact, generative representation supporting person‑specific prediction. **Related Concepts:** Generative Model; Person Representation.

---

*Instructor note:* This paper is ideal for teaching compositionality and Marr's algorithmic/implementational linkage—showing how a simple summation rule has measurable neural signatures and behavioral consequences.

---

## Vainio et al. (2025). Is Kiki angry and Bouba happy? Association between emotions, shapes, and sounds

**Full Citation:** Vainio, L., Mo, X., & Vainio, M. (2025). Is Kiki angry and Bouba happy? Association between emotions, shapes, and sounds. *Psychological Research, 89*, 124.

**Topic Tags:** Sound Symbolism, Kiki‑Bouba Effect, Cross‑Modal Emotion, Implicit Association

### Core Question / Problem
What mechanisms underlie the kiki‑bouba effect (angular vs. round shapes mapped to certain sounds)? Specifically, are emotion/arousal associations a mediating factor, and do explicit and implicit association tests reveal the same mapping patterns?

### Conceptual or Computational Framework
The authors propose an emotional‑mediation account: shapes and pseudowords share higher‑order emotional properties (e.g., high arousal ↔ kiki, anger ↔ angular). They test whether explicit and implicit measures tap the same or different processes—suggesting multiple routes to cross‑modal correspondence (articulatory vs. acoustic vs. emotional mediation).

### Methods Overview
Three experiments combining explicit association tasks and implicit measures (IAT), reaction‑time analyses, and manipulation of congruency across emotion/shape/sound pairings. Stimuli included angular vs. rounded shapes, kiki‑like vs. bouba‑like pseudowords (auditory), and facial expressions (angry, happy, calm).

### Key Findings
- Explicit association tasks reliably link kiki‑like words and angular shapes to high‑arousal/angry expressions and bouba‑like words and rounded shapes to low‑arousal/happy/calm expressions.
- Implicit Association Test (IAT) responses showed a robust link between shapes and emotions, but the implicit link between aurally presented pseudowords and emotions was weaker or absent.
- Conclusion: emotional mediation plausibly contributes to the kiki‑bouba effect for visual shapes, but phonetic/articulatory routes also play a role; explicit and implicit tasks tap partially distinct processes.

### Interpretation & Significance
The study argues for a multi‑route account: shape–emotion associations are processed implicitly (perhaps perceptual arousal mapping), while sound–emotion links may require explicit attention or be mediated by articulatory/learning processes. This refines accounts of sound symbolism by showing domain‑specific differences in implicit processing.

### Computational‑Social‑Cognitive‑Scientist Hat
Modeling implication: multiple feature spaces (visual curvature, acoustic spectral centroid, arousal axis) map onto emotion space; explicit tasks access higher‑level mappings that may integrate articulatory knowledge, while implicit tasks reflect low‑level perceptual–affective coupling. A latent variable model with cross‑modal loadings could capture these effects.

### Connections
Ties to Sievers et al. (2013, 2019) on cross‑modal emotion codes, articulatory theories (Ramachandran & Hubbard), and literature on sound symbolism and language evolution.

### Key Quotes or Phrases
- "The kiki‑bouba effect… can be partially based on emotional mediation processes." fileciteturn1file11

### Concept Graph
- Angular shape ↔ high arousal / anger; Round shape ↔ low arousal / happiness.
  - **Shape‑Emotion Correspondence:** perceptual mapping between curvature and affective valence/arousal. **Related Concepts:** Cross‑Modal Dynamics; Kiki‑Bouba effect.

### Relevant Terms
- **Existing Terms Used:** Cross‑Modal Dynamics; Animacy (as perceptual affordance); Predictive Mind (as framework for multimodal expectations). fileciteturn1file11 fileciteturn1file2
- **New Terms to Add:**
  - **Emotional Mediation (in sound symbolism):** The hypothesis that cross‑modal correspondences (shape↔sound) are partly mediated by shared mappings to affect/arousal dimensions. **Definition:** A latent affect axis that links low‑level perceptual features across modalities. **Related Concepts:** Cross‑Modal Dynamics; Arousal.

---

*Instructor note:* Great reading for demonstrating experimental methods (IAT vs. explicit tasks) and for linking perceptual primitives to social/emotional meaning.

---

## Wang et al. (2015). The uncanny valley: Existence and explanations

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

## Waytz et al. (2010). Causes and consequences of mind perception

**Full Citation:** Waytz, A., Gray, K., Epley, N., & Wegner, D. M. (2010). Causes and consequences of mind perception. *Trends in Cognitive Sciences.*

**Topic Tags:** mentalizing, mind perception, anthropomorphism, agency, experience, dehumanization, moral cognition

### Core Question / Problem
When and why do people perceive minds in others (including non-human entities), and what are the psychological and social consequences of that perception?

### Conceptual or Computational Framework
Waytz et al. synthesize behavioral, developmental, and neuroscientific evidence under a dual-dimension model of mind perception: **Agency** (capacity to plan/act) and **Experience** (capacity to feel). At Marr's levels: computationally the goal is to infer hidden mental states to predict and connect; algorithmically people use coarse perceptual Turing tests followed by higher-order inference (heuristics like similarity, unpredictability, and effectance); implementationally, neural markers (e.g., mPFC engagement) index mind-attribution.

### Methods Overview
This is a theory-driven review integrating experiments across paradigms: morphing faces (animacy tipping points), EEG/fMRI studies of face and social perception, behavioral priming (belief in gods, surveillance cues), and social-psychological manipulations (loneliness, control threats) that alter anthropomorphism.

### Key Findings
- Mind perception operates on two separable axes: **Experience** and **Agency**, which can be dissociated in judgments. (See Gray et al., 2007.)
- Perceiver motives shape mind attribution: lack of causal control or high causal uncertainty increases ascriptions of agency (people explain unpredictability with minds). Loneliness and need for social connection increase attributions of mental states to non-humans.
- Target properties matter: humanlike appearance, humanlike motion, and perceived similarity increase mind attribution; out-group members, objects, or dehumanized targets receive lower mind ratings.
- Consequences: attributing mind confers moral status (moral patient = experience) and moral responsibility (agentic capacity). Conversely, denying mind enables dehumanization and moral exclusion.

### Interpretation & Significance
This paper reframes **mentalizing** not only as state inference (ToM) but as a graded perception system with clear antecedents and moral consequences. It connects basic perceptual triggers to higher-order social outcomes (e.g., punishment, empathy, moral typecasting). For the course's computational lens, mind perception is an adaptive inference system that trades off accuracy and efficiency: fast detectors flag candidate minds, but higher-level reasoning (and social motives) determine commitment.

### Computational-Social-Cognitive-Scientist Hat
**What would Kurt Lewin think?** Lewin's *B = f(P,E)* maps nicely: perceiver motives (P) and target features (E) jointly determine mind-attribution (B). He'd appreciate the field-theoretic, interactionist framing.

**What would David Marr think?** Marr would ask for explicit algorithms and representations: what are the decision rules for moving from low-level face/ motion signals to high-level mind-ascription? The two-stage detector+filter is a good start at Marr's algorithmic level.

**What would Egon Brunswik think?** Brunswik would emphasize ecological validity: which environmental cues are reliable indicators of mind and how do perceivers weight noisy cues (lens model)? The paper's cue-competition results fit a Brunswikian perspective.

### Connections
Links to: animacy/biological motion research, dehumanization literature, implicit bias (mPFC differences), and predictive-processing views (the role of expectancy/prediction in tagging minds).

### Key Quotes or Phrases
- "People think about other minds in terms of two distinct dimensions: experience and agency."
- "Attributing mind confers moral rights; denying mind licenses harm."

### Concept Graph
- Perceiver motives (loneliness, lack of control) → increase mind attribution because they satisfy needs for connection/effectance.
- Target cues (human likeness, unpredictability) → increase mind attribution because they signal agency/experience.
- Mind attribution → alters moral status (patient vs. agent) → changes helping/punishing behaviors.

---