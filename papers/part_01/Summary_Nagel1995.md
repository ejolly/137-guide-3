## 1995 — Nagel, R. (1995). Unraveling in Guessing Games: An experimental study. *Journal of Economic Behavior & Organization.*

**Full Citation:** Nagel, R. (1995). Unraveling in guessing games: An experimental study. *Journal of Economic Behavior & Organization.*

**Topic Tags:** Iterated reasoning, Level‑k models, Keynesian beauty contest, Bounded rationality

### Core Question / Problem
How deep do people reason about others’ reasoning in “guessing games” (like the 2/3 of the average game)? Which empirical pattern best describes human iterated reasoning: stepwise k‑levels, noisy depth limits, or convergence dynamics?

### Conceptual or Computational Framework
Nagel formalizes depth‑limited iterative reasoning (level‑k thinking) as a parsimonious model of strategic thought. Players pick a number (often 0–100) and the winning target is a fixed function of others’ choices (typically 2/3 of the average). Nash equilibrium (iterated elimination to 0) requires infinite depth; human behavior typically shows bounded depth.

### Methods Overview
Controlled laboratory experiments where participants submit guesses in a beauty‑contest/guessing game. Key manipulations: single‑shot vs repeated play, information about others’ behavior, and group size. Main observations: modal clusters at values corresponding to shallow iterated steps (e.g., 33, 22), indicating finite k‑levels.

### Key Findings
- Distribution of guesses clusters near simple iterated solutions (33 = one step; 22 = two steps), consistent with level‑k reasoning and bounded iterative depth.
- Repeated play and feedback can shift distributions toward lower numbers (more unraveling), but convergence to the Nash equilibrium (0) is slow and often incomplete.
- Individual differences are large; many subjects use heuristic one‑ or two‑step reasoning rather than deep recursion.

### Interpretation & Significance
Nagel’s study operationalized iterated reasoning and demonstrated that human strategic reasoning is depth‑limited; this provides empirical grounding for level‑k and cognitive hierarchy models used widely in behavioral game theory. It also highlights the computational cost of higher‑order belief representations.

### Computational‑Social‑Cognitive‑Scientist Hat
- Computational goal: best‑respond to others when others are themselves strategic.
- Algorithmic description: finite recursion (k‑step updates), potentially noisy; mental representation stores a bounded model of others' strategies.
- Implements bounded rationality: resource constraints (cognitive depth) shape behavior.

### Teaching Hooks
- Run a live classroom Keynesian beauty contest and plot histogram to reveal peaks at k‑levels.
- Ask students to predict modal choices for k=0,1,2 and compare to data.

### Connections
Ties to bounded rationality (Herbert Simon), mentalizing (depth of representing others’ beliefs), and modern work on recursive theory of mind in cognitive development.

### Key Quotes or Phrases
- “Most subjects behave as if they perform only a few steps of iterative reasoning.”

### Concept Graph
- Iterated reasoning → level‑k distributions (k = 0,1,2…).
  - **Keynesian Beauty Contest:** A game where players guess 2/3 of the group average; equilibrium at 0 but humans show bounded unraveling.
  - **Level‑k model:** Agents assume others are at level k−1 and best‑respond.

### Relevant Terms
- **Existing Terms Used:** Bounded Rationality; Representation; Predictive Mind (as cognitive limitation metaphor). fileciteturn3file0
- **New Terms to Add:**
  - **Iterated Reasoning (k‑level):** A process where agents recursively model others’ choices to a bounded depth. **Definition:** Practical model for strategic depth and bounded Theory of Mind.