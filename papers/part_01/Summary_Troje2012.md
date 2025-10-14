## 2012 — Troje, N. F. (2012). What is biological motion: Definition, stimuli, and paradigms. *In Social Perception: Detection and Interpretation of Animacy, Agency, and Intention (Rutherford & Kuhlmeier, eds.). MIT Press.*

**Full Citation:** Troje, N. F. (2012). What is biological motion?: Definition, stimuli and paradigms. In M. D. Rutherford & V. A. Kuhlmeier (Eds.), *Social Perception: Detection and Interpretation of Animacy, Agency, and Intention.* MIT Press.

**Topic Tags:** biological motion, point-light displays, animacy, life motion, perception

### Core Question / Problem
What do researchers mean by “biological motion”? Troje traces the historical lineage from Johansson’s point-light displays to modern work that asks not only how the visual system recovers articulated structure from non-rigid motion, but also what social information (actor, action, style, animacy) can be read out from motion alone.

### Conceptual or Computational Framework
Troje positions “biological motion” within a broader class he calls **life motion** (all motion that signals living beings). He distinguishes intrinsic (deforming-body) versus extrinsic (object trajectory) motion and separates global, structure-from-motion processes (configuration recovered from correlated part motions) from local, shape-independent invariants (e.g., foot acceleration consistent with gravity). This maps naturally onto Marr‑style distinctions: the computational goal (detect life, infer actor/action), algorithmic cues (local acceleration patterns, global kinematic templates), and implementational considerations (STS and other neural areas).

### Methods Overview
The chapter reviews standard experimental paradigms:
- Point‑light stimuli and stick-figure variants (Johansson tradition).
- Detection tasks (is a walker present?), direction tasks (which way is the walker facing?), and masked/noise paradigms.
- Scrambling manipulations (spatial/temporal) that isolate local vs global cues.
- Stylistic manipulations for person identification, sex, emotion, and intention (kinematic synthesis and morphs).

### Key Findings
- Point‑light displays robustly convey identity, sex, emotion, and intention despite minimal form cues (Johansson; Cutting).
- Two largely independent information channels can support common tasks (e.g., facing direction): (i) motion-mediated reconstruction of articulated shape and (ii) local motion invariants (notably foot trajectory/acceleration). Troje & Westhoff (2006) highlight the “local inversion effect” tied to foot acceleration profiles that obey gravitational constraints.
- Scrambled displays are not “non-biological”: they preserve life‑detection cues, so treating them as null controls is conceptually risky.
- The superior temporal sulcus (STS) responds in many—but not all—biological motion contrasts; STS responses appear heterogeneous and sensitive to stimulus type and task.
- Life‑detection cues (vertical acceleration, foot dynamics) appear evolutionarily old and available early in development (neonatal/animal data cited).

### Interpretation & Significance
Troje argues for precision in terminology: reserve “biological motion” for intrinsic deformable-body motion, use “animate motion” for whole‑object kinematics, and “life motion” for the broad class. Importantly, motion carries both redundant and complementary signals: global configuration supports identity and action parsing while local invariants provide fast, shape‑independent life detection and orientation cues. This redundancy explains robustness but complicates experimental design and interpretation (masking confounds, control stimuli).

### Computational‑Social‑Cognitive‑Scientist Hat
Modeling biological motion benefits from a hybrid architecture: early mid‑level filters tuned to local invariants (life detector) gate attention and feed higher‑order configurational reconstruction modules that instantiate kinematic templates (generative models of gait, action). From a predictive‑processing stance, local invariants provide strong priors (is this animate?), while template‑based inference recovers higher fidelity hypotheses about identity/action and computes prediction errors across frames.

### Teaching Hooks
- Demo: show a point‑light walker, scrambled walker, upside‑down walker — students guess what cues they used.
- In‑class exercise: tweak foot acceleration (simulated) and ask whether the stimulus still 'looks alive.'
- Short homework: map Johansson’s tasks to Marr’s three levels.

### Pedagogical Lens
Favor mechanistic clarity: explain why local acceleration patterns are diagnostic (ballistic foot motion under gravity) and how global form can be reconstructed from temporal correlations in joint motion. Use simple generative sketches (stick-figure + pendulum analogy) to convey intuition.

### Connections
Links to animacy perception (Heider & Simmel tradition), action understanding, STS and social neuroscience, computer animation (style transfer), and developmental sensitivity to life motion cues.

### Key Quotes or Phrases
- “Life motion” as umbrella term for motion that signals living beings.
- “Life detector” for filters sensitive to ballistic invariants in foot motion.

### Concept Graph
- Life motion → {extrinsic (animate motion), intrinsic (biological motion)}
  - **Life Detector:** local visual filters sensitive to foot acceleration consistent with gravity. **Notable Figures:** Troje, Chang. **Related Concepts:** Animacy; early attention orienting.
  - **Structure-from-motion:** global integration of part motions to yield articulated 3D shape. **Notable Figures:** Johansson, Ullman. **Related Concepts:** Point‑light displays; STS.

### Relevant Terms
- **Existing Terms Used:** Biological Motion, Animacy, Intentional Stance.
