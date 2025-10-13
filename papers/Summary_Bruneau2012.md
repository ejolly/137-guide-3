## 2012 — Bruneau, E., & Saxe, R. (2012). The power of being heard: The benefits of ‘perspective-giving’ in the context of intergroup conflict. *Cognition and Emotion.*

**Full Citation:** Bruneau, E. G., & Saxe, R. (2012). The power of being heard: The benefits of ‘perspective-giving’ in the context of intergroup conflict. *Cognition and Emotion.*

**Topic Tags:** Perspective-taking, Perspective-giving, Intergroup conflict, Dialogue interventions

### Core Question / Problem
Do brief structured dyadic interactions change attitudes in intergroup conflict, and does *being heard* (perspective‑giving) differ from *hearing the other* (perspective‑taking) in their effects? The paper asks which facet of dialog (giving vs taking) drives attitude change across groups with asymmetric power.

### Conceptual or Computational Framework
Grounded in social psychological theories of intergroup contact and bias reduction, the authors frame the mechanism as asymmetric influence shaped by group power: the *perspective‑giving* agent is allowed to express constraints and grievances (signal), whereas *perspective‑taking* requires accurate encoding and summarizing of another’s input (modeling). From a computational-leaning lens: perspective‑giving supplies data that alters the observer’s priors about an outgroup; perspective‑taking functions like a bidirectional belief-update that modifies representations via mutual inference.

### Methods Overview
Two field experiments with structured, short-format dyadic exchanges:
- Study 1: Mexican immigrants and White Americans (Arizona). Cross-group dyads interacted via video/text. Conditions: perspective‑giving (write about life difficulties), perspective‑taking (summarize partner), control (non-interactive essay).
- Study 2: Israelis and Palestinians in the Middle East with similar structured assignments.
Key dependent measures: attitude change toward outgroup, measured pre/post and compared across conditions and groups.

### Key Findings
- Perspective‑giving produced stronger positive attitude change for lower-power groups (e.g., Mexican immigrants, Palestinians) while perspective‑taking produced stronger gains for higher‑power groups (e.g., White Americans, Israelis). fileciteturn2file0
- Control (non-interactive writing) did not yield the same benefits as interactive perspective‑giving — highlighting that *being heard* (feedback loop) matters beyond mere expression. fileciteturn2file0
- Effects depend on an interaction between condition and group membership — likely reflecting asymmetries in credibility, power, and what counts as informative evidence.

### Interpretation & Significance
Mechanistically, the results suggest that attitude updating in conflict settings depends on who supplies evidence (the speaker) and who performs the encoding (the listener). For disempowered groups, giving perspective is informationally potent — it changes the priors held by the other side because it reveals constraints and motives not otherwise visible. For empowered groups, being accurately summarized signals acknowledgment and reduces defensive inference.

### Computational‑Social‑Cognitive‑Scientist Hat
Map to Marr’s levels:
- Computational: goal = reduce intergroup bias through evidence integration and social signal exchange.
- Algorithmic: perspective‑giving supplies rich likelihoods; perspective‑taking performs belief-updating operations (summarization, weighting).
- Implementational: dyadic exchange, mediated by language and perceived power, determines which signals get encoded or ignored.
Predictive‑mind framing: perspective‑giving reduces model mismatch (prediction error) for listeners who had stronger negative priors.

### Teaching Hooks
- Small in-class roleplay: assign pairs asymmetric roles (giver vs summarizer) and measure attitude shift.
- Quick demo: show how control writing vs interactive summarization influences perceived sincerity.

### Pedagogical Lens
Emphasize power-asymmetric updating — tie to Lewin’s *B = f(P, E)* by showing how the same dialog procedure yields different B because P (group membership/power) modulates information salience.

### Connections
Connects to literature on contact theory, narrative psychology, and recent computational accounts of social inference (belief updating, predictive processing). Also relevant to synchronization and trust-building mechanisms.

### Key Quotes or Phrases
- “The critical role of being heard.” fileciteturn2file0

### Concept Graph
- Perspective‑giving → supplies informative signals about constraints & motives.
  - **Perspective-giving:** Participant expresses difficulties/constraints; this increases observer’s evidence for situational explanations. **Notable Figures:** Bruneau & Saxe. **Related Concepts:** Attitude updating; Power asymmetry.
- Perspective‑taking → accurate summarization reduces defensive inference.
  - **Perspective-taking:** Listener summarizes partner’s statement; signals acknowledgment. **Related Concepts:** Mentalizing; Attribution.

### Relevant Terms
- **Existing Terms Used:** Mentalizing; Predictive Mind; Representation; Field Theory (Lewin); Attribution Theory; Intentional Stance. fileciteturn2file1
- **New Terms to Add:**
  - **Perspective‑giving:** A structured communicative action wherein one individual expresses their lived constraints or grievances to a listener. **Definition:** A social signal that supplies evidence about situational causes and motives. **Related Concepts:** Contact interventions; Attitude updating.
  - **Perspective‑taking (dialogic):** An interactive summarization behavior by a listener that signals accurate encoding and acknowledgment. **Definition:** A behavioral signal that reduces defensive priors and supports mutual model alignment.