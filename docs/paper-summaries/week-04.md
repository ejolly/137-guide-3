# Paper Summaries - Week 04

---

## Simon, H. A. (1990). Invariants of human behavior. *Annual Review of Psychology*, *41*, 1–19.

**Full Citation:** Simon, H. A. (1990). Invariants of human behavior. *Annual Review of Psychology*, 41, 1–19.

**Topic Tags:** Bounded rationality, physical symbol systems, cognitive architecture, heuristic search, recognition processes, adaptive systems, computational limits, satisficing, individual differences, social cognition, expertise, problem-solving.

### Core Question / Problem

How can psychology identify fundamental invariants of human behavior when people are highly adaptive systems whose behavior flexibly responds to environmental demands? What unifying principles explain how bounded cognitive systems achieve intelligent behavior despite severe computational constraints?

### Conceptual or Computational Framework

Simon grounds the paper in **artificial systems theory**: humans are adaptive systems shaped by environmental pressures, analogous to computers. The central framework rests on the **Physical Symbol System Hypothesis** (Newell & Simon, 1976), which proposes that intelligence emerges when a system can input, output, store, and manipulate symbol structures. This maps precisely to **Simon's scissors metaphor**—behavior emerges at the intersection of task environment structure and cognitive capabilities. At **Marr's computational level**, the theory explains what intelligence must accomplish; at the algorithmic level, it details heuristic search, recognition, and pattern mechanisms; the implementational level remains largely unmapped to neural hardware. Rather than seeking invariants like physics' conservation laws, psychology seeks "laws of qualitative structure"—robust principles governing adaptive systems operating under bounded rationality.

### Methods Overview

This is a theoretical-integrative paper synthesizing three decades of information-processing psychology research (primarily computational modeling and laboratory studies). Simon reviews empirical work employing think-aloud protocols, reaction time measures, eye-movement recordings, and computer simulations (e.g., EPAM, GPS) to test hypotheses about human cognition. Key domains include chess expertise, medical diagnosis, problem-solving (Tower of Hanoi, algebra), pattern recognition, and individual differences in complex tasks. The paper draws on comparative analysis of human versus machine intelligence across varied task environments.

### Key Findings / Claims

- **Bounded rationality as fundamental invariant**: Human short-term memory holds ~6 chunks; recognition takes ~1 second; reaction times measure in tens–hundreds of milliseconds. These constraints make optimization impossible; intelligence must approximate instead.

- **Recognition as primary mechanism**: Experts solve problems through rapid pattern matching (50,000+ stored cues) rather than systematic search. This explains "intuitive" expertise in chess, medicine, and professional domains.

- **Heuristic search and satisficing**: When recognition fails, people use selective search guided by domain-specific heuristics or weak methods (satisficing—accepting "good enough" rather than optimal; means-ends analysis reducing goal distance). These methods are cognitively feasible adaptations to bounded rationality.

- **Knowledge as dominant source of individual differences**: Expert-novice gaps reflect accumulated knowledge and strategy repertoires, not innate processing differences. Even lightning calculators show no faster basic processes—their advantage is stored arithmetic facts and computational shortcuts.

- **Procedural vs. substantive rationality**: Explaining behavior requires describing both task requirements and actual cognitive processes. Task-only analysis (rational choice models) fails because bounded-rational systems use context-dependent approximations.

### Interpretation & Significance

This paper unifies cognitive psychology by establishing that seemingly diverse phenomena (expertise, problem-solving, individual differences, reasoning) arise from a coherent set of mechanisms constrained by computational limits. Critically, Simon rejects the notion that information-processing psychology is "incomplete" because it cannot yet explain neural implementation—psychology can advance at the symbolic level, just as biochemistry preceded atomic physics. The framework enables bridging previously isolated subfields (developmental, individual differences, psycholinguistics, social psychology) by anchoring all in knowledge structures and bounded-rational processes. Most importantly, it shifts focus from whether people are "rational" to *how* they achieve adaptive behavior under severe computational constraints—a fundamentally ecological and realistic view of cognition aligned with field theory (person-situation interaction) principles.

### Computational-Social-Cognitive-Scientist Hat

**What would Herb Simon think?** Simon himself articulates this: bounded rationality is not a failure of optimization but an **appropriate adaptation to real-world complexity**. The scissors metaphor captures Lewin's insight perfectly—behavior is jointly determined by internal computational architecture and external structure.  

**What would Kurt Lewin think?** Lewin's equation B = f(P,E) finds exact expression here: behavior emerges from the interaction of physiological limits (P: ~6 chunks, ~1 second recognition, millisecond reaction times) and task environment structure (E: problem space complexity, cue distribution, domain knowledge demands). Neither the person nor the environment alone determines behavior; neither psychology of "pure" cognition nor rational analysis of tasks suffices.

### Connections

- **To subsequent bounded rationality research**: Simon's framework directly enabled Tversky & Kahneman's heuristics-and-biases tradition by explaining *why* systematic deviations from optimization emerge from bounded-rational algorithms (satisficing, anchoring, availability).

- **To expertise research**: Ericsson and Charness built directly on Simon's recognition and chunking mechanisms to explain the 10,000-hour rule and deliberate practice in expert performance across domains.

- **To cognitive architecture debates**: Anderson's ACT*, Newell's SOAR, and McClelland & Rumelhart's connectionist systems all attempt to implement Simon's proposed components (memories, EPAM discrimination nets, GPS problem solver, production systems) at different levels of abstraction.

- **To social cognition and situated learning**: The recognition that performance depends on socially acquired knowledge (e.g., Voss et al.'s agricultural reform problem) presages contemporary emphasis on distributed cognition and cognitive apprenticeship—intelligence is fundamentally social.

---

## Cushman, F., & Gershman, S. (2019). Editors' Introduction: Computational Approaches to Social Cognition. *Topics in Cognitive Science*, *11*(2), 281–298.

**Full Citation**: Cushman, F., & Gershman, S. (2019). Editors' Introduction: Computational Approaches to Social Cognition. *Topics in Cognitive Science*, 11(2), 281–298.

**Topic Tags**: Computational social science, formal methods, Bayesian inference, decision-making, game theory, reinforcement learning, social cognition, theory development, person-situation interaction, strategic interaction

### Core Question / Problem

How can computational and formal methods—long absent from social psychology—illuminate the mechanisms underlying social cognition and help discover the "hidden logic of familiar things"? This paper addresses the historical tension between social psychology's founders (Lewin, Heider, Festinger) who championed formalization, and contemporary social psychology's turn away from formal theory toward documenting surprising empirical effects.

### Conceptual or Computational Framework

The paper argues that three formal frameworks—Bayesian inference, value-based decision theory, and game theory—provide the conceptual and computational scaffolding to unify diverse social psychological phenomena. These frameworks exemplify Marr's computational level: they specify *what* the mind solves (inference problems, optimization problems, strategic equilibria) independent of neural or algorithmic implementation. Critically, they embody Simon's scissors principle by showing how cognition and environment interact through well-defined formal structures (generative models, utility functions, payoff matrices). The approach recovers Lewin's vision of discovering hidden logic through abstraction and systematization rather than merely accumulating effects.

### Methods Overview

This is a conceptual and theoretical integration paper introducing a special issue. Rather than presenting empirical studies, Cushman and Gershman synthesize research across computational cognitive science and social psychology, illustrating how formal methods applied to three domains—inference, choice, and strategic interaction—generate novel theoretical insights. They use concrete examples (trait inference, popularity bias, romantic commitment) and case studies of contributing papers to demonstrate mechanistic clarity.

### Key Findings / Claims

- **Formal methods enable abstraction**: Bayesian models of trait inference unify seemingly contradictory findings about negativity bias and diagnosticity by formalizing how people update beliefs given evidence. This abstraction reveals that diverse phenomena (stealing, giving, smart acts, dumb acts) follow common probabilistic principles.

- **Value-based decision models explain social behavior**: Reinforcement learning frameworks—distinguishing model-based (deliberative) from model-free (habitual) decision-making—illuminate domains from prejudice to trust to morality. These tools organize neural, behavioral, and psychological data into a unified account of how people assign value and make choices.

- **Game theory formalizes strategic interaction**: Nash equilibria, commitment signaling, and social dilemmas provide precise language for understanding cooperation, romantic relationships, communication, and revenge—phenomena that resist non-formal description because optimal behavior depends on others' choices.

- **Computational methods achieve two seemingly opposite goals**: They enable both radical simplification (by identifying abstract commonalities across disparate cases) and sophisticated complexity (by allowing symbolic representation of high-dimensional theories our brains cannot hold intuitively).

### Interpretation & Significance

This work directly addresses a crisis in social psychology: the field has drifted from its founders' ambition to discover general principles and hidden logic toward emphasizing counterintuitive effects and folk-concept rearrangement. Cushman and Gershman argue that this drift impoverishes the field by sacrificing breadth and mechanistic depth for novelty and accessibility. The paper's significance lies in demonstrating that formal methods—long dismissed as unnecessary or obscuring in social psychology—are in fact indispensable for organizing complex phenomena and building theories that generalize across cognitive, developmental, clinical, and social domains. By showing how Bayesian, decision-theoretic, and game-theoretic frameworks illuminate real social phenomena (moral judgment, learning from teachers, collective intelligence, romantic commitment), the authors make a compelling case for computational social science as continuous with—not opposed to—the founders' vision.

### Computational-Social-Cognitive-Scientist Hat

**What would Herbert Simon think?**: Simon lamented the gap between formal theory and folk psychology. Cushman and Gershman show that formal methods don't obscure folk concepts but rather reveal their hidden structure. The "scissors" metaphor—cognition cutting through the environment—is perfectly illustrated by Bayesian models of trait inference: agents' cognitive operations (Bayesian inversion) are precisely matched to the structure of social problems (diagnosing dispositions from behavior). This is not mere formalism but mechanistic insight into how bounded rationality solves real social problems.

**What would Kurt Lewin think?**: Lewin despaired that psychology was "piling up facts" without conceptual structure. Cushman and Gershman's Bayesian, decision-theoretic, and game-theoretic frameworks exactly embody Lewin's dream: abstract, formal structures that unify diverse phenomena (B = f(P,E) for person-environment interaction becomes precisely specified in formal models). The paper rehabilitates Lewin's vision by showing that early efforts (his equation, Heider's notation) failed not because formalization is useless but because they lacked sufficient mathematical power. Contemporary computational frameworks succeed where earlier efforts floundered.

### Connections

- **To Marr's three levels**: The paper implicitly operates at Marr's computational level, specifying what the mind *solves*. Bayesian models formalize inference problems; decision theory formalizes value maximization; game theory formalizes strategic choice. This computational specification remains independent of—and compatible with—algorithmic and neural implementations.

- **To developmental and clinical psychology**: Bayesian frameworks apply to how children learn causal models; reinforcement learning explains habit formation and compulsive behavior; game theory models cooperation and defection across development. The authors note that computational methods provide a "lingua franca" allowing theories from social, cognitive, developmental, and clinical psychology to speak to each other.

- **To economics and neuroscience**: Expected utility theory, reinforcement learning, and game theory originated outside psychology yet have proven essential to understanding neural coding of value, economic choice, and brain-based decision-making. Cushman and Gershman position social psychology to reclaim and integrate these frameworks rather than ceding them to neighboring fields.

- **To the special issue papers**: The introduction previews contributions on social learning (Velez & Gweon), teaching and active learning (Yang et al.), emotion in theory of mind (Ong et al.), popularity bias (Le Mens et al.), collective intelligence (Krafft), romantic commitment (Bear & Rand), and moral judgment (Yu, Siegel, & Crockett)—all demonstrating that formal methods generate novel, precise, testable predictions about familiar social phenomena.

---

## The Royal Swedish Academy of Sciences. (2002). *Foundations of Behavioral and Experimental Economics: Daniel Kahneman and Vernon Smith*. Advanced Information on the Prize in Economic Sciences 2002, December 17.

**Full Citation**: The Royal Swedish Academy of Sciences. 2002. *Foundations of Behavioral and Experimental Economics: Daniel Kahneman and Vernon Smith*. Advanced Information on the Prize in Economic Sciences 2002, December 17.

**Topic Tags**: behavioral economics, experimental methods, decision-making under uncertainty, heuristics and biases, prospect theory, market mechanisms, bounded rationality, loss aversion, judgment under risk

### Core Question / Problem

How do humans actually make economic decisions, and can laboratory experiments serve as a valid empirical methodology for testing economic theory? This paper addresses the fundamental gap between the rationalistic assumptions of classical economics (homo oeconomicus) and the systematic deviations from rational behavior observed in real human decision-making.

### Conceptual or Computational Framework

The work synthesizes two converging traditions: Vernon Smith's experimental economics, which applies controlled laboratory methods to test market mechanisms and institutional design, and Daniel Kahneman's cognitive psychology approach, which documents systematic deviations from expected-utility maximization through heuristics and biases. This maps directly to Simon's "scissors" metaphor—how cognition (mental limitations, bounded rationality) interacts with context (market institutions, decision frames) to produce actual behavior. The framework also aligns with Marr's levels: Smith addresses the computational level (what markets should achieve) and algorithmic level (how specific auction institutions enable price discovery), while Kahneman illuminates the implementational level (how human minds actually process probabilistic information).

### Methods Overview

Vernon Smith conducted controlled double oral auctions with university students assigned roles as buyers and sellers, each with private reservation prices. Participants' earnings depended on their trades relative to these reservation prices, using the "induced-value method" to control preferences. Daniel Kahneman and Amos Tversky employed surveys and controlled experiments, presenting subjects with choice problems involving monetary gambles and asking them to categorize individuals or make probabilistic judgments. Both researchers conducted repeated trials and varied experimental parameters (market institutions for Smith; problem framings and stakes for Kahneman) while holding other conditions constant.

### Key Findings / Claims

- **Market efficiency paradox (Smith)**: Contrary to expectations, competitive double auctions produce trading prices that converge rapidly to theoretical equilibrium prices even though individual subjects lack information to compute equilibrium. Market institutions matter: continuous price adjustment achieves faster convergence than posted-price mechanisms.

- **Systematic deviations from rationality (Kahneman)**: Humans employ mental shortcuts (heuristics) that systematically violate probability theory—the "law of small numbers" causes overinference from small samples; "representativeness" leads subjects to ignore base rates; "availability" biases probability judgment toward salient but unrepresentative information. Effect magnitudes are substantial: loss aversion approximately doubles the pain of losses relative to equivalent gains.

- **Prospect theory**: Decision-making is reference-dependent (gains/losses relative to status quo, not absolute wealth), features loss aversion, and involves probability distortion (overweighting small probabilities, underweighting large ones). This descriptive model explains the Allais paradox and other violations of expected-utility theory that axiomatic models cannot accommodate.

### Interpretation & Significance

These findings revolutionized how economists understand human behavior by demonstrating that deviations from rationality are neither random nor negligible—they are systematic, predictable, and large enough to require fundamental theoretical revision. Smith established that controlled experiments are not merely permissible in economics but essential for understanding how market institutions shape outcomes; this legitimized experimental methodology as central to economic science. Kahneman's work bridged economics and psychology by showing that cognitive constraints are not quirks but foundational to understanding choice architecture. Together, they initiated behavioral economics as a major research program, shifting the field from assuming rational actors in simple models to recognizing bounded rationality, context-dependence, and psychological realism as necessary for adequate economic theory.

### Computational-Social-Cognitive-Scientist Hat

**What would Herb Simon think?**: Simon's concept of bounded rationality anticipated these findings perfectly—humans cannot achieve global optimization under uncertainty and must rely on simplified decision rules (satisficing rather than maximizing). Smith's market experiments and Kahneman's heuristics research both demonstrate the "scissors" at work: cognition (limited processing capacity, reliance on mental shortcuts) cuts against environment (complex probability spaces, information asymmetries), producing adaptive but non-rational behavior.

**What would Kurt Lewin think?**: The research vindicates Lewin's interactionist framework. Market behavior is not fixed personality trait but emerges from person-environment fit: individuals with identical preferences produce different aggregate outcomes depending on market institution (Smith), and identical choice problems elicit different preferences depending on problem framing (Kahneman). Neither the person's utility function nor the objective decision structure alone determines behavior—only their interaction.

### Connections

- **Fairness and reciprocity**: Kahneman's later work with Knetsch and Thaler (1986) extends these insights to show fairness concerns and loss aversion shape market behavior in ultimatum games and endowment effects, seeds of extensive experimental research on social preferences.

- **Behavioral finance applications**: The law of small numbers and representativeness heuristic explain systematic anomalies in financial markets—excess sensitivity of stock prices to short sequences of news (Shiller, 1981), bubbles driven by representativeness-based overvaluation of trending stocks.

- **Institutional design and policy**: Smith's "wind tunnel" methodology—testing auction designs and mechanism proposals experimentally before real-world deployment—became standard practice for deregulation and spectrum allocation policy, demonstrating practical value of experimental methods.

- **Contemporary behavioral economics**: The framework established here undergirds modern work on choice architecture, default effects, and nudges (Thaler & Sunstein), showing how context-dependence and bounded rationality can be leveraged for social welfare improvements.

---

## Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. *Cognitive Psychology*, *5*(2), 207–232.

**Full Citation**: Tversky, Amos & Kahneman, Daniel, 1973. "Availability: A heuristic for judging frequency and probability." *Cognitive Psychology*, 5(2), pp. 207–232.

**Topic Tags**: heuristics, bounded rationality, probability judgment, frequency estimation, systematic bias, mental availability, representativeness, cognitive shortcuts, decision-making under uncertainty

### Core Question / Problem

How do people estimate the frequency of events or the probability of outcomes when they cannot enumerate all relevant instances? The paper addresses the psychological mechanisms underlying probability and frequency judgments—a fundamental question given that classical probability theory offers no insight into how human minds actually perform these ubiquitous tasks.

### Conceptual or Computational Framework

The authors propose that people employ a limited number of heuristics to reduce complex probability judgments to simpler assessments. Specifically, the **availability heuristic** suggests that people estimate the frequency or probability of an event by assessing the ease with which instances or associations come to mind. This connects directly to Herbert Simon's "scissors" metaphor: cognition is bounded by both the environment's structure (which events are objectively frequent?) and the mind's processing capacity (which events are easy to retrieve or construct?). At Marr's levels, availability operates at the algorithmic level—describing the mental procedure people actually use—rather than claiming normative optimality at the computational level.

### Methods Overview

The paper reports ten empirical studies (N = approximately 1,500 subjects across studies) using diverse tasks: word-construction problems (N = 42), category retrieval (N = 28), word-frequency judgment (N = 152), path enumeration in combinatorial structures (N = 54), committee combinations (N = 118), numerical extrapolation (N = 201), and binomial path estimation (N = 73). Key designs included comparing estimated frequencies to actual production counts, manipulating task presentation to vary availability, and measuring both accuracy and bias in frequency estimates. Primary measures were median or mean estimates compared against objectively correct values.

### Key Findings / Claims

- **Availability as accurate cue**: In Studies 1 and 2, product-moment correlations between estimated and actual frequencies were exceptionally high (r = 0.96 for word construction; r = 0.93 for retrieval), demonstrating that people can quickly and accurately assess availability when sufficient instances are produced or retrieved.

- **Systematic availability biases**: When availability is decoupled from true frequency, judgments systematically diverge from reality. In Study 3, 105 of 152 subjects incorrectly judged words beginning with K to be more frequent than words with K in the third position, despite the latter being twice as common. Median estimate was 2:1 favoring first position when the true ratio is 1:2 (p < 0.001). This bias persists across multiple experimental variations, including within-subject designs and financial incentive manipulations.

- **Availability shapes combinatorial intuition**: Studies 4–5 revealed that people judge combinatorial outcomes (paths through structures, committee formations) as more frequent when instances are easier to construct or visualize. In path-counting tasks, 46 of 54 subjects misjudged the number of paths (true count = 512 in both structures), erring in the direction predicted by differential path availability—shorter, more distinctive paths in one structure were judged more numerous than equally valid but less salient paths in another.

- **Non-transparent biases**: Even with explicit monetary incentives and varied task presentations, availability bias proved robust. Subjects did not spontaneously correct their estimates when presented with formally identical problems using different representations (path diagram vs. card-drawing game), suggesting the bias operates at a relatively automatic level independent of conscious deliberation.

### Interpretation & Significance

This work fundamentally reframes human judgment as operating through ecological heuristics rather than normative probability calculations. Availability is ecologically valid because, generally, frequent events are easier to recall than rare ones. However, the availability heuristic produces systematic errors when factors unrelated to actual frequency (memorability, recent media exposure, vividness) inflate subjective ease of retrieval. The theoretical significance lies in showing that human probability judgment is tractable—not random—but follows predictable, mechanistic principles rooted in memory and construction processes. This bridges classical probability theory with cognitive mechanisms, grounding decision-making in the computational constraints of human minds. The paper's emphasis on availability bias has been foundational to behavioral economics and the study of judgment heuristics, demonstrating that bounded rationality is not a deficit but an adaptation to environments where mental resources must be allocated selectively.

### Computational-Social-Cognitive-Scientist Hat

**What would Herb Simon think?**: The availability heuristic exemplifies satisficing—people do not compute objective probabilities (which would require exhaustive enumeration) but instead use a fast, frugal rule that typically works well. Simon's scissors apply directly: the ease of mental construction is shaped by both environmental structure (true frequencies correlate with retrievability) and cognitive architecture (working memory constraints, associative strength). This heuristic exploits the correlation between availability and frequency to achieve good-enough judgments with minimal computation.

**What would Kurt Lewin think?**: Lewin's equation B = f(P,E) captures a key insight from these studies. The person's judgment of frequency depends jointly on personal factors (memory salience, cognitive effort) and environmental factors (actual frequency, recent exemplars, media representations). The systematic availability biases observed reveal person-by-environment interactions: the same objective frequency is judged differently depending on presentation format, individual experience, and cognitive context. The clinical example of the clinician judging suicide risk (discussed late in the paper) illustrates how personal availability of salient cases and the situational framing of scenarios conspire to produce biased judgments.

### Connections

- **Representativeness heuristic** (Kahneman & Tversky's companion work): Whereas availability relies on ease of retrieval, representativeness relies on degree of similarity to a category prototype. The two heuristics can pull in different directions; Study 7 shows that problem representation (path diagram emphasizing individual instances vs. card game emphasizing aggregate composition) determines whether availability or representativeness dominates.

- **Anchoring and adjustment**: The underestimation of combinatorial values in Studies 5–6 reflects extrapolation from partial computation—an instance of how people use initial impressions as anchors and insufficiently adjust when scaling to larger problems.

- **Medical decision-making and base-rate neglect**: The clinician example (judging suicide probability) connects to later research on how physicians make probabilistic judgments about rare diagnoses, where availability of recent memorable cases can override base-rate information.

- **Contemporary bounded rationality frameworks**: Subsequent work on ecological rationality and fast-and-frugal heuristics builds directly on this foundation, asking when simple heuristics outperform complex calculations in realistic environments.

---

## Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*, *47*(2), 263-291.

**Full Citation:** Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica, 47*(2), 263-291.

**Topic Tags:** decision-making, risk perception, bounded rationality, heuristics, cognitive biases, choice behavior, expected utility theory, loss aversion, reference dependence, probability weighting

### Core Question / Problem

Why do people systematically violate expected utility theory when making decisions under risk? Specifically, how can we develop a descriptive model that captures pervasive patterns like the certainty effect and isolation effect—phenomena inconsistent with rational choice axioms?

### Conceptual or Computational Framework

Prospect theory abandons the assumption that people evaluate final states of wealth in favor of *gains and losses relative to a reference point*. The theory maps onto Simon's bounded rationality framework: rather than achieving optimal calculation, decision-makers employ cognitive simplifications (editing operations) followed by a two-stage evaluation process. This aligns with Marr's levels: the computational goal is to choose among risky alternatives; the algorithm involves editing and evaluation phases; the implementation uses value and decision-weight functions. The framework rejects probability weighting as identity (π(p) = p), proposing instead that decision weights systematically distort probabilities.

### Methods Overview

Hypothetical choice experiments with university students and faculty (N ranging from 66–95 per problem) across Israeli and Swedish universities. Subjects rated preferences between carefully constructed pairs of monetary prospects with explicit probabilities. Key manipulations included framing (gains vs. losses), probability magnitude (high vs. low), and problem structure (standard vs. sequential formulations). Measures captured binary preference patterns and analyzed modal choices for systematic deviations from utility theory axioms.

### Key Findings / Claims

- **The Certainty Effect (Problems 1–2, 5–6):** People overweight certain outcomes relative to probable ones. 82% chose a sure gain of 2,400 over a 33% chance of 2,500 (higher expected value), yet when both options were equally uncertain (0.33 vs. 0.34 probabilities), 83% reversed preference. This violates the substitution axiom.

- **The Reflection Effect (Table I):** Risk aversion in gains flips to risk seeking in losses. The same preference reversal pattern holds for negative prospects, implying that the certainty effect operates symmetrically—it inflates the aversion to losses as well as the desirability of gains.

- **Isolation Effect (Problems 10–12):** When identical prospects are presented in different decision structures, preferences reverse. Problem 10 (sequential game with shared first stage) induced 78% to choose a risky option, while Problem 4 (identical final odds, standard formulation) induced only 35%. This shows that *how* a problem is framed—not just the probabilities and outcomes—determines choice.

### Interpretation & Significance

This paper fundamentally challenges the descriptive validity of expected utility theory and establishes that human decision-making is reference-dependent and non-linear in probability. Rather than treating this as irrationality, Kahneman and Tversky propose it reflects perceptual and cognitive constraints: the mind naturally evaluates changes, not absolute states. This reframes decision-making anomalies not as failures but as signatures of a different decision calculus. The value function's S-shape (concave for gains, convex for losses, steeper for losses) explains why people simultaneously buy lottery tickets and insurance—overweighting of small probabilities drives both. This work established bounded rationality as a rigorous scientific enterprise, moving beyond normative ideals to descriptive accuracy about how minds actually work.

### Computational-Social-Cognitive-Scientist Hat

**What would Herb Simon think?** Simon's scissors metaphor applies directly: Kahneman and Tversky show that the *cognition* side (editing operations, limited probability discrimination, reference-dependent valuation) produces systematic deviations when the *context* (environment) presents uncertainty. Their framework operationalizes satisficing: decision-makers simplify complex prospects through cancellation, rounding, and dominance detection—satisfactory heuristics rather than optimal algorithms.

**What would Kurt Lewin think?** Lewin's equation B = f(P, E) appears in the isolation effect and shift-of-reference section: behavior depends jointly on person and environment. The same person exhibits different risk attitudes depending on whether the reference point is the status quo (inducing conservatism) or a recent loss (inducing adventurousness). The field theory perspective explains why *formulation* matters as much as *substance*—psychological reality is constructed through the decision context, not given objectively.

### Connections

- **Allais Paradox (Allais, 1953):** Kahneman and Tversky systematically extend and reinterpret Allais's foundational counterexample to expected utility, showing it reflects subcertainty (π(p) + π(1-p) < 1), a general weighting property, not an isolated anomaly.

- **Markowitz's S-shaped utility (1952):** Anticipated the concave-then-convex value function, but Markowitz retained the expectation principle. Prospect theory abandons that constraint, explaining violations of substitution that Markowitz's framework could not.

- **Subsequent research on framing effects (Tversky & Kahneman, 1981):** The isolation effect directly presages systematic studies showing that identical choice problems yield opposite preferences when framed as "gains" versus "losses"—demonstrating the centrality of reference points in human judgment.

- **Modern behavioral economics:** This paper opened the field. Contemporary work on loss aversion magnitude (~2.25:1 ratio), probability weighting curvature, and reference dependence all trace to these foundational empirical patterns and theoretical structures.

---

## Lieder, F., & Griffiths, T. L. (2020). Resource-rational analysis: Understanding human cognition as the optimal use of limited computational resources. *Behavioral and Brain Sciences*, *43*, e1: 1–60.

**Full Citation**: Lieder, F., & Griffiths, T. L. (2020). Resource-rational analysis: Understanding human cognition as the optimal use of limited computational resources. *Behavioral and Brain Sciences*, 43, e1: 1–60. https://doi.org/10.1017/S0140525X1900061X

**Topic Tags**: bounded rationality, cognitive biases, computational constraints, resource optimization, decision-making, mental representations, cognitive architecture, heuristics, Marr's levels of analysis, Simon's bounded rationality

### Core Question / Problem

How can we model human cognition as fundamentally rational when extensive empirical evidence reveals systematic violations of logic, probability theory, and expected utility maximization? The paper addresses the tension between people's remarkable cognitive abilities and their consistent "irrational" errors, proposing that both reflect optimal adaptation to limited computational resources.

### Conceptual or Computational Framework

Resource-rational analysis integrates two complementary approaches: (1) **rational principles** that specify optimal solutions to computational problems, and (2) **cognitive constraints** that capture realistic limitations in processing speed, working memory, and attention. The framework maps onto **Marr's levels**: resource-rational analysis connects the computational level (what the mind should compute) to the algorithmic level (how it actually computes it with limited resources). This echoes **Simon's scissors metaphor**—cognition emerges from the interaction between mind's limited capacities and environmental structure. The central equation defines a resource-rational mechanism as one that maximizes expected utility minus the computational cost of achieving it (Equation 3), where "cost" includes time, neural energy, and cognitive effort.

### Methods Overview

This is a theoretical and integrative target article rather than an empirical study. The authors synthesize research across psychology, neuroscience, economics, AI, and linguistics—reviewing experimental findings and computational models from existing literature. The paper systematically examines resource-rational explanations for cognitive biases in decision-making (satisficing, rational inattention, probability matching), memory (working memory capacity allocation), attention (optimal allocation under uncertainty), reasoning (frame problem, hypothesis generation), and executive function. Key empirical examples include studies of perceptual decision-making (drift-diffusion models with optimal stopping thresholds), multi-alternative risky choice (discovery of the SAT-TTB heuristic), and neural encoding efficiency under metabolic constraints.

### Key Findings / Claims

- **Cognitive biases as rational shortcuts**: Many "irrational" phenomena—anchoring, base-rate neglect, probability matching, overconfidence—reflect bounded-optimal solutions that trade accuracy for speed and computational effort. When time and cognitive resources are costly, these biases become adaptive.

- **Unifying explanatory framework**: Resource rationality provides a single mathematical principle (Equation 3) that explains diverse phenomena across perception, memory, reasoning, attention, and decision-making—replacing the fragmented heuristics-and-biases literature with coherent mechanistic models.

- **Cognitive constraints as design features**: Working memory capacity, attentional limits, and neural noise constraints are not incidental failures but necessary consequences of optimal resource use. Shared neural resources that produce multitasking costs actually enable faster learning through generalization (effect size: resource constraints improve long-term performance).

- **Reconciling mind and mechanism**: Resource-rational models predict actual decision thresholds people use, aspiration levels in sequential search, hypothesis generation strategies, and mental effort allocation—achieving ~86% of the bounded-optimal trade-off between quality and time cost in planning tasks.

### Interpretation & Significance

This work fundamentally shifts how we interpret human cognition. Rather than viewing cognitive biases as evidence of irrationality or evolutionary kluges, resource-rational analysis reveals them as **signatures of intelligent adaptation to real constraints**. The framework bridges the explanatory gap between psychology's descriptive models and AI/neuroscience' computational theories by providing a common language: bounded optimality. Its significance lies in three dimensions: (1) **theoretical**: replacing loose "bounded rationality" with precise mathematical criteria; (2) **practical**: enabling automatic discovery of heuristics people should use and tools for cognitive improvement; (3) **interdisciplinary**: connecting psychology to neuroscience (via metabolic constraints), to economics (via information costs), and to AI (via algorithmic efficiency). This reframes the human rationality debate: the question becomes not "are people rational?" but "to what actual constraints are their mechanisms optimally adapted?"

### Computational-Social-Cognitive-Scientist Hat

**What would Herb Simon think?**: The paper explicitly invokes Simon's insight that the mind emerges from scissors—the interaction of limited cognitive architecture with environmental structure. Resource-rational analysis operationalizes satisficing and bounded rationality quantitatively: it specifies *which* heuristics people should use and *why*, grounded in the mathematics of constrained optimization. Simon argued we must accept "the environment may lie, in part, within the skin of the biological organism"; resource-rational analysis embeds neural constraints (metabolic costs, processing speed) directly into models of rational cognition.

**What would Kurt Lewin think?**: The equation B = f(P, E) finds expression here as cognition = f(mind's computational capacities, environmental structure). Resource rationality shows how the same person generates different cognitive strategies across contexts—not because of personality shifts but because environmental structure changes which heuristics are bounded-optimal. For instance, the SAT-TTB heuristic emerges as optimal when one outcome dominates; Take-The-Best heuristic emerges when cues vary in validity. The person adapts rationally to the field.

### Connections

- **Ecological rationality (Gigerenzer & Selten)**: Resource-rational analysis is the mathematical completion of ecological rationality—specifying *how* simple heuristics exploit environmental structure and *why* they often outperform complex computation under real constraints.

- **Rational analysis (Anderson, 1990)**: The paper extends Anderson's framework from minimal computational assumptions to explicit modeling of computational costs, moving from the computational level toward the algorithmic level while maintaining rational principles.

- **Bayesian cognitive science (Griffiths et al.)**: While building on Bayesian frameworks, resource-rational analysis explains why people deviate from Bayesian inference: approximations and simplifications are not bugs but features of bounded-optimal reasoning under time pressure and cognitive load.

- **Computational neuroscience and efficient coding**: The principle that neural representations should trade off information content against metabolic cost connects to contemporary work on sparse coding, neural efficiency, and energy-constrained computation—showing how rational principles at the cognitive level map to principles governing neural implementation.

- **Contemporary decision science**: Links to recent work on optimal decision thresholds (perceptual and value-based), information search (rational inattention), and strategy adaptation (strategy selection and change theory), providing unifying mechanistic explanations across these previously disparate literatures.


This paper is foundational for understanding how social cognition emerges from the rational use of limited resources. For a social cognition course, it offers several teaching advantages:

1. **Reconciles apparent contradictions**: Students often struggle with why humans are simultaneously capable of sophisticated inferences and prone to systematic errors. Resource-rational analysis shows both reflect the same adaptive principle.

2. **Mechanistic clarity**: The paper moves beyond descriptive accounts ("people use heuristics") to explain *why* specific mechanisms are rational given constraints—making cognition predictable from first principles.

3. **Mathematical grounding**: Equations 3 and 4 provide precise normative standards, enabling quantitative assessments of human rationality rather than vague categorical judgments.

4. **Bridges disciplines**: For students interested in connections between psychology, AI, neuroscience, or economics, this framework demonstrates how a single principle (bounded optimality) unifies these fields.

5. **Practical implications**: The paper discusses applications to cognitive training, decision support, and improving human judgment—demonstrating theoretical relevance to real-world problems.

### Caveats & Challenges

The authors acknowledge significant limitations: 
1. **Identifying constraints**: It remains difficult to measure actual cognitive constraints independently; most analyses estimate constraints through model fitting, risking circular reasoning.
2. **Applicability scope**: Resource-rational models have been developed primarily for controlled laboratory paradigms; scaling to real-world decisions with unknown options and outcomes remains unexplored.
3. **Assumptions about adaptation**: The theory assumes cognitive mechanisms are adapted through evolution or learning—problematic for novel, infrequent decisions with minimal evolutionary relevance or learning history.
4. **Measuring constraint validity**: Resource-rational predictions are only as good as assumptions about computational costs and capacity limits; future work must establish independent empirical measures of processing speed, working memory limits, and neural efficiency.

