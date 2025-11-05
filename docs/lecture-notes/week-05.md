# Part 2 - Week 5 Lecture Notes

## Mon-10-27 Prospect Theory

**Big Questions.** Why do humans systematically deviate from the predictions of Expected Utility Theory (EUT)? What do biases like loss aversion and framing reveal about human rationality, and how can these be reframed as adaptive rather than flawed?

### Key Ideas

* **Violations of EUT:** Real people prefer certainty and avoid ambiguity, violating EUT’s axioms (completeness, transitivity, independence, continuity).
* **Certainty Effect:** People disproportionately favor sure outcomes over probabilistic ones, even when the expected value is lower.
* **Ambiguity Aversion:** We avoid options with uncertain or unknown probabilities, preferring environments where we have more information.
* **Prospect Theory (Kahneman & Tversky, 1979):** Introduced *subjective value* and *subjective probability* as dual sources of bias. People transform both outcomes (via a **value function**) and probabilities (via a **weighting function**).
* **Loss Aversion:** Losses loom larger than equivalent gains—roughly 2x as psychologically impactful.
* **Framing:** Risk-averse for gains, risk-seeking for losses.
* **Anchoring/Reference Dependence:** Outcomes are judged relative to a reference point (not absolute value).
* **Availability/Representativeness:** Probability judgments rely on ease of recall and similarity to known examples.
* **Behavioral Economics:** Prospect Theory marked a paradigm shift—from seeing humans as *irrational* (“homo economicus”) to *boundedly rational* agents whose cognitive biases follow predictable patterns.

### Lecture Notes

* **From Homo Economicus to Human Bias:** EUT’s idealized, logical decision-maker (“economic man”) failed to describe real behavior. Kahneman & Tversky reframed this: humans aren’t irrational—they’re predictably biased.
* **Subjective Transformations:** Prospect Theory replaces objective math with psychological functions:

  * **Value Function:** Concave for gains, convex for losses, steeper for losses than gains (asymmetrical curve centered at the reference point).
  * **Weighting Function:** Overweights small probabilities and underweights large ones.
* **Descriptive vs Normative Theories:** EUT is normative (how rational agents *should* decide), while Prospect Theory is descriptive (how people *actually* decide).
* **Nobel Prize Context:** Kahneman’s 2002 Nobel lecture emphasized psychology’s integration into economics—rationality redefined as a psychological process of judgment, not abstract logic.
* **From Description to Explanation:** Prospect Theory described *what* people do; later frameworks (Rational Analysis, Resource Rationality) explain *why* they do it.
* **Resource Rationality (Lieder & Griffiths, 2020):** Humans maximize the expected *utility of cognition*, balancing accuracy, effort, and computational cost. Rationality = bounded optimality given environmental and cognitive constraints.
* **The Resource Rational Recipe:**

  1. Define task and environment.
  2. Characterize available cognitive resources.
  3. Enumerate possible strategies.
  4. Evaluate trade-offs (time, accuracy, effort).
  5. Predict the bounded-optimal (resource-rational) strategy.
* **From Homo Economicus to Homo Heuristicus:** Decision-making strategies are rational *if they fit the structure of the environment*. Biases are often *adaptive heuristics* optimized for ecological conditions.

### Highlights

* **Prospect Theory:** Descriptive model of human choice; integrates subjective value and probability.
* **Resource Rationality:** Bridges descriptive psychology with computational rationality; humans trade off cost vs. benefit of thought.
* **Key Terms:** *Certainty Effect*, *Loss Aversion*, *Framing*, *Anchoring*, *Availability Heuristic*, *Bounded Optimality*.
* **Readings:**  Gigerenzer & Brighton (2009); Moskowitz (Chap 8)

---

## Wed-10-29 Game Theory

**Big Questions.** How can we formalize strategic interaction between agents? When do individual rational choices conflict with collective benefit?

### Key Ideas

* **Game Theory:** A mathematical framework for analyzing strategic decisions made by two or more agents whose outcomes are interdependent.

  * **Game:** Any situation where outcomes depend on the actions of multiple players.
  * **Strategy:** Possible actions available to each player.
  * **Payoff:** The reward or outcome received by each player depending on joint choices.
* **Prisoner’s Dilemma (PD):** A classic two-player game illustrating tension between individual and collective rationality.

  * Mutual cooperation → moderate rewards for both.
  * One defects → defector wins big, cooperator loses.
  * Both defect → both worse off.
* **Nash Equilibrium (John Nash):** A state where no player can improve their outcome by unilaterally changing their strategy.
* **Non-zero-sum vs. Zero-sum Games:** Zero-sum = one’s gain is another’s loss (e.g., poker); non-zero-sum = interdependent but potentially cooperative outcomes (e.g., group projects, traffic coordination).
* **Applications:** Cold War nuclear arms race, AI competition, business strategies.
* **Modern Example:** “AI Prisoner’s Dilemma”—two firms investing heavily in AI; mutual cooperation would maximize joint benefit, but competition drives overinvestment.

### Lecture Notes

* **Video Demonstration:** *Veritasium* and *Nicky Case’s Evolution of Trust* introduced PD visually and interactively.
* **Rationality in Conflict:** In PD, individual rationality (defection) leads to collectively suboptimal outcomes—an example of “tragedy of the commons.”
* **Interpretation:** The Nash equilibrium is *individually* rational but *socially* inefficient.
* **Behavioral Insights:** Real humans often cooperate more than strict rational models predict—trust and repeated interaction matter.
* **Repeated Games:** Cooperation emerges when players interact multiple times; defection is punished through reputation or reciprocity.
* **Historical Context:** Post-WWII and Cold War tensions inspired game-theoretic modeling of deterrence and cooperation.

### Highlights

* **Core Equation:** Payoffs depend on both players’ actions.
* **Key Terms:** *Prisoner’s Dilemma*, *Nash Equilibrium*, *Cooperation vs. Defection*, *Zero-sum vs. Non-zero-sum*, *Strategic Interaction*.
* **Readings:** Hofstadter (1983); Axelrod (1981)

---

## Fri-10-31 Game Theory II

**Big Questions.** Why does cooperation persist in competitive environments? How do repeated interactions and simple strategies like “Tit-for-Tat” explain social trust?

### Key Ideas

* **Axelrod’s Tournament (1981):** A landmark computer simulation testing strategies in the repeated Prisoner’s Dilemma. Participants (scientists) submitted programs; the simplest—**Tit-for-Tat (TFT)**—won.
* **Tit-for-Tat Strategy:**

  * *Nice* — never defects first.
  * *Forgiving* — retaliates once but quickly returns to cooperation.
  * *Retaliatory* — punishes defection immediately.
  * *Clear* — easily recognizable behavior fosters trust.
* **Outcome:** Nice and forgiving strategies outperformed complex or exploitative ones.
* **Resilient Cooperation:** Even a small number of cooperators can shift group behavior toward long-term collaboration.
* **Empirical Evidence:** Mao et al. (2017, *Nature Communications*) showed “resilient cooperators” stabilize cooperation in human populations playing repeated PD over weeks.
* **Conditions for Cooperation:**

  1. **Repeated Interactions** – Future encounters incentivize reciprocity.
  2. **Mutual Benefit** – Non-zero-sum environments allow shared gain.
  3. **Communication** – Reduces misinterpretation and restores trust.
* **From Theory to Practice:** Cooperation depends on ecological structure—the “scissors” of Simon again: behavior shaped by environment × cognition.
* **Biases as Adaptive:** Framing, loss aversion, and availability heuristics can be *ecologically rational*—they exploit structured regularities in real-world decision environments.

### Lecture Notes

* **Video Examples:** Veritasium’s “Evolution of Trust” and simulations of Axelrod’s tournament.
* **Findings:**

  * TFT succeeds because it’s simple, transparent, and promotes stable reciprocity.
  * “Copycat” (TFT variant) wins in dynamic environments where forgiveness prevents endless retaliation.
  * Cooperation declines when interactions are one-shot or communication is impossible.
* **Human Studies:** Mao et al. (2017) showed that about 40% of participants adopting cooperative strategies can stabilize entire populations.
* **Reframing Biases:** Loss aversion → survival sensitivity to danger; framing → flexible contextual adaptation; availability → efficient pattern-matching; anchoring → reusing prior computations.
* **Integration:** From Homo Economicus → Homo Heuristicus → Homo Cooperativus.

### Highlights

* **Axelrod (1981):** Cooperation evolves via repeated interaction and reciprocity.
* **Mao et al. (2017):** Human experiments confirm long-run cooperation stability.
* **Key Terms:** *Tit-for-Tat*, *Resilient Cooperation*, *Reciprocity*, *Bounded Optimality*, *Homo Heuristicus*.
* **Readings:** Axelrod (1985); Mao et al. (2017)

---

### Week 5 Summary

* Rationality and cooperation emerge from adaptation, not perfection.
* Prospect Theory reframed human bias as systematic; Resource Rationality explained *why* those biases exist.
* Game Theory revealed that cooperation and fairness can arise through repeated, structured interaction.
* Across theories, the human mind is *resource-rational*: making the best possible use of limited information, time, and social context.