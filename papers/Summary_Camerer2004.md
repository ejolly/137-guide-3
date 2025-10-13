## 2004 — Camerer, C. F., Ho, T.-H., & Chong, J.-K. (2004). A Cognitive Hierarchy Model of Games. *The Quarterly Journal of Economics.*

**Full Citation:** Camerer, C. F., Ho, T.-H., & Chong, J.-K. (2004). A Cognitive Hierarchy Model of Games. *The Quarterly Journal of Economics*, 119(3), 861–898.

**Topic Tags:** bounded rationality, level-k thinking, cognitive hierarchy, game theory, predictive models

### Core Question / Problem
How can we predict one-shot game behavior when players are *not* in Nash equilibrium because they differ in how many steps of strategic thinking they perform? The paper asks whether a simple, falsifiable model of limited iterative reasoning (Cognitive Hierarchy, CH) can explain systematic departures from equilibrium across many experimental games.

### Conceptual or Computational Framework
CH assumes players come in discrete reasoning types (0,1,2,...) and that each k-step player best-responds to a mixture of lower-level types (0..k−1). The authors impose a Poisson distribution on the population frequencies of k (a one-parameter family), producing the *Poisson-CH* model. This places the proposal cleanly at Marr’s algorithmic level (how representations of others’ strategies are computed), while the single parameter τ (mean steps) provides a compact cognitive-level summary amenable to estimation.

### Methods Overview
The authors operationalize CH across many published and new one-shot games (beauty-contest variants, 2–4 strategy matrix games, market-entry games, mixed-equilibrium games). They solve the model recursively (starting from randomized 0-step play), estimate τ by maximum likelihood or moment-matching (minimizing prediction error of sample means), bootstrap confidence intervals, and compare Poisson-CH to Nash and alternative level-k models.

### Key Findings
- A Poisson mean τ between ~1 and 2 (median ≈ 1.6, omnibus suggestion τ≈1.5) fits a wide variety of data sets well, especially beauty-contest games where equilibrium predicts zero but observed means cluster around 20–35.
- Poisson-CH explains why some games rapidly approximate equilibrium (entry games) while others do not (beauty contest): in some structures higher-step reasoning washes out earlier levels’ randomness; in others limited steps produce systematic bias.
- CH almost always fits better than Nash in one-shot games; it corrects many of Nash’s worst errors while not performing much worse when Nash works.
- CH has measurable “economic value”: forecasting with CH increases expected payoffs relative to average subject behavior (10–70% of the clairvoyant upper bound in datasets shown).

### Interpretation & Significance
The paper reframes disequilibrium not as noise but as structured heterogeneity of recursive reasoning depths. By formalizing *how many* steps people take and how they model others (only lower-step types), CH provides a generative account linking cognitive limits (working memory, cost of thinking) to aggregate strategic outcomes. The Poisson simplification makes the theory parsimonious and predictive across domains.

### Computational‑Social‑Cognitive‑Scientist Hat
Viewed from computational cognitive science, CH is a compact algorithmic-level model of social recursive reasoning: it specifies representations (distributions over opponent types), transformations (best-response mapping), and a simple parametric prior (Poisson τ) over computational depth. This bridges Marr’s levels: the computational-level goal (predict others under bounded cognition) is implemented by an algorithmic recursion and instantiated in behavioral patterns (entry monotonicity; beauty-contest averages).

### Teaching Hooks
- Run an in-class Keynesian beauty contest: show how equilibrium predicts 0 but observed averages cluster around 20–35; then fit a τ≈1.5 intuitively.
- Use the entry-game diagram (Fig. I) to illustrate how limited steps produce monotonic entry yet systematic over/underentry.
- Contrast CH with Quantal Response / QRE: CH relaxes mutual consistency; QRE relaxes best-response.

### Pedagogical Lens
Emphasize mechanism over fit: what cognitive assumptions produce the distributional signatures? Discuss why a Poisson prior is psychologically plausible (decaying mass for higher k) and how incentives or training shift τ (stakes/experience increase τ).

### Connections
Links to bounded rationality, level‑k models, predictive-processing themes (agents form predictions about others’ actions), and cognitive-cost accounts of reasoning depth (Gabaix & Laibson style cost–benefit).

### Key Quotes or Phrases
- “An average of 1.5 steps fits data from many games.”
- CH provides a behavioral refinement: it “weakens” mutual consistency but keeps best-response for k≥1.

### Concept Graph
- Limited recursive reasoning → population mixture of k‑types → aggregate choice distributions.
  - **Cognitive Hierarchy (CH):** Players are categorized by k steps of iterated best-response; k‑step players best-respond to types 0..k−1. **Notable Figures:** Camerer, Ho, Chong. **Related Concepts:** level‑k, bounded rationality, iterated deletion.
  - **Poisson‑CH:** A Poisson prior f(k)=e^{−τ}τ^{k}/k! over types compresses heterogeneity into one parameter τ. **Definition:** τ is mean (and variance) of thinking steps. **Notable Figures:** Camerer et al. **Related Concepts:** parametric priors; cognitive cost models.
  - **Beauty‑Contest / Keynesian Game:** Diagnostic task (guess p×mean) that reveals depth of iterative thinking. **Related Concepts:** dominance‑solvable games; experimental diagnostics.

### Relevant Terms
**Existing Terms Used:** Marr’s Computational Level; Marr’s Algorithmic Level; Representation.

**New Terms to Add:**
### Cognitive Hierarchy (CH)
A theory positing discrete levels of iterative strategic reasoning (0,1,2…). Lower‑level players randomize; k‑step players best‑respond to a normalized mixture of types 0..k−1. **Notable Figures:** C. Camerer, T.-H. Ho, J.-K. Chong. **Related Concepts:** level‑k, bounded rationality, iterative deletion.

### Poisson‑CH
A parsimonious instantiation of CH that assumes f(k) follows a Poisson(τ). The single parameter τ captures the mean depth of reasoning in a population; empirically τ≈1–2 in many labs. **Notable Figures:** Camerer et al. **Related Concepts:** parametric priors, cognitive cost models.

