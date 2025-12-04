# Part 3 - Week 7 Lecture Notes

## Wed-11-12 Social Group Formation and Categorization

**Big Questions.** How do social groups form from the ground up? What minimal conditions are sufficient to create in-group bias and intergroup conflict, and can these dynamics be reversed?

### Key Ideas
- **Perception as Categorization (Bruner):** Perception is not passive but involves actively categorizing inputs into meaningful groups—inferring "what is this thing?" from sensory cues
- **Signal Construction:** social groups emerge from environmental signals (resource scarcity, labels) and psychological processes (categorization, reciprocity, transitivity)
- **robbers cave experiment:** demonstrated that competition for scarce resources creates intergroup conflict, but superordinate goals requiring cooperation can reduce hostility
- **minimal group paradigm (tajfel):** even arbitrary group assignment (coin flip, random labels) produces in-group bias—people favor their own group despite no rational incentive
- **transitivity:** how impressions and opinions pass between people; if you're on team blue and i'm on team blue, how you treat team red influences how i treat them
- **reciprocity and group formation:** direct and indirect reciprocity combined with transitivity are sufficient computational ingredients for groups to emerge from repeated interactions
- **out-group homogeneity effect:** people assume out-group members are more similar to each other and different from themselves, collapsing out-group variation while maintaining individuation within their in-group (wilder's studies with artwork preferences).

### Lecture notes

**part 3 framework: social signals**
- part 1 focused on **lewin's equation** (behavior as function of person and environment), part 2 on **simon's scissors** (bounded rationality), part 3 examines **social signals**
- social signals comprise both external inputs (faces, communication, thin slices) and internal states (self, memory, emotion)
- the guiding framework: how do we construct meaning from social information in the environment?

**bruner's foundational insight: perception as categorization**
- jerome bruner (cognitive revolution era) argued that **perception is fundamentally an act of categorization**
- we don't passively register sensory information—we actively infer category membership: "this is an orange" involves placing input into a category
- **key quote:** "perception involves an act of categorization...the use of cues in inferring the categorical identity of a perceived object is as much a feature of perception as the sensory stuff from which the percepts are made"
- perception requires the same cognitive complexity as mathematical reasoning—it's not "effortless" but involves inference, expectations, mental models, and cultural knowledge
- what we perceive is shaped by: concepts, causal reasoning, cultural context, goals, beliefs, and mental models of how things work

**robbers cave experiment (muzafer sherif, 1950s)**
- funded by rockefeller family; inspired by questions similar to *lord of the flies*
- **design:** 22 fifth-grade boys at summer camp divided into two groups (eagles and rattlers)
- **phase 1 - competition:** boys competed in games; kept score. even outside structured activities, conflict emerged—hard boundaries formed between groups
- **phase 2 - resource scarcity:** experimenters made food and resources scarcer, dramatically exacerbating conflict. boys rated the other group extremely negatively despite minimal interaction
- **phase 3 - superordinate goals:** created situation requiring cooperation (food truck stuck, needed both groups to push it uphill). working together toward shared goal reduced hostility and restored camaraderie
- **key findings:**
  - when competition for resources becomes scarce, intergroup conflict almost always increases (true for humans and non-humans)
  - when cooperation toward shared goals is necessary, intergroup conflict decreases
  - **environmental signals alone** (resource availability, goal structure) can create or dissolve group divisions—before identity, values, race, or gender enter the picture
- **ethical note:** would be completely unethical by today's standards, but foundational for understanding naturalistic group dynamics

**minimal group paradigm (henri tajfel, 1970s)**
- **research question:** what are the *minimal* conditions needed to turn people against each other?
- researchers wanted a control condition with no group bias, but couldn't achieve it
- **design:** participants randomly assigned to groups (told it was based on "estimation ability" but actually random). no interaction between participants; anonymous resource allocation decisions with no personal benefit
- **finding:** even with completely arbitrary group membership (eventually told participants it was a coin flip), people still showed **in-group bias**—consistently gave more resources to their own group
- **theoretical explanation:** **social identity theory**—people use group membership to construct their sense of self. simply being categorized as part of a group links that group to personal identity, motivating people to elevate in-group status
- variants conducted globally show minimal group distinctions affect attention, perception, memory, and emotions—same mental processes as real group identities
- **positive applications:** creating new superordinate groups can temporarily help people overcome entrenched biases (though external factors can negate this)

**from individual rationality to social context**
- individuals don't simply maximize expected value, expected utility, or even follow prospect theory in isolation
- **part of the environment is other people**—what others do, think, and how they behave influences our actions
- the interaction between **perception and categorization feeds back on itself**: categorize yourself as part of a group → take actions reinforcing that membership → strengthens the category

**transitivity and group dynamics**
- **transitivity:** how opinions and impressions pass between people (not strict mathematical sense)
- example: if i'm team blue and you're team blue, how you treat team red influences both how i treat team red and how i treat you
- connects to mechanisms from part 2:
  - **direct reciprocity:** i cooperate with you based on past interactions
  - **indirect reciprocity:** how you treat others affects how i treat you and them
  - **spatial selection:** labels, colors, names make it easier to sort into categories
- transitivity is the interplay between being influenced by others' actions and the environment affording categorical organization

**computational model: gray et al. (2014)**
- used **computer simulations** (not human experiments) to test if reciprocity and transitivity alone can generate group formation
- agents repeatedly play prisoner's dilemmas; move closer/farther based on game outcomes and influence from neighbors
- **key parameters:**
  - **reciprocity:** how much agents respond to others' cooperation/defection
  - **transitivity:** how much agents are influenced by third-party relationships
  - **trust:** baseline cooperation rate
- **results:** groups reliably form from these simple rules—sometimes one large group, sometimes multiple clusters
- turning down reciprocity → agents freeze, no groups form
- turning down trust → groups form more slowly, less cohesion
- **insight:** reciprocity + transitivity are sufficient computational ingredients for dots on a screen (representing simplified human decision-making) to form social groups

### Highlights
- **perception is never neutral:** bruner's insight that categorization is built into perception itself challenges the notion of passive observation—every act of seeing involves inference about category membership and meaning
- **environmental signals drive group formation:** the robbers cave experiment demonstrates that resource scarcity alone can create intergroup hostility, while superordinate goals requiring cooperation can dissolve it—suggesting interventions at the situational level can be powerful
- **arbitrary labels are enough:** tajfel's minimal group paradigm reveals that even random, meaningless group assignments produce in-group bias, suggesting how easily real-world categories (race, nationality, political affiliation) can activate these dynamics
- **computational simplicity, social complexity:** gray et al. (2014) show that just two mechanisms—reciprocity and transitivity—are sufficient for groups to emerge from repeated interactions, providing a foundation for understanding more complex social phenomena in upcoming lectures
- **bridge to part 3 topics:** today's focus on basic group formation sets the stage for examining face perception (external signals), stereotypes (how categories carry content), self and emotion (internal signals), and social networks (how structure constrains signal flow)

---

## Fri-11-14 Social Categorization and Stereotyping

**big questions.** why do we automatically group people into categories, and what are the cognitive benefits and costs of this process? how does categorization shape our perception of individuals and groups?

### Key ideas

- **bounded rationality of categorization:** categorization functions as a cognitive heuristic that simplifies the complex social world, saving precious cognitive resources by making simplifying assumptions rather than tracking every individual's unique properties.

- **stereotype content model:** a two-dimensional framework (warmth × competence) for understanding how people categorize social groups, enabling predictions about unobserved behaviors and traits by assigning individuals to categorical clusters.

- **trade-offs of fast-and-frugal stereotyping:** while efficient, stereotyping fails in diverse/changing environments, makes poor predictions about specific individuals, and provides inadequate guidance for treating individuals - better served by slower processes like causal inference, simulation, and theory of mind.

### Lecture notes

**out-group perception: wilder's studies**

alan wilder's experiments demonstrated that in the absence of any other information, people reliably make assumptions about out-group members - specifically, that they must be different in some way. the experimental design was simple: assign people to two arbitrary groups and have them complete surveys predicting either their own group members' preferences or out-group members' preferences about abstract artwork.

key findings:
- participants assumed out-group members were arbitrarily more different from themselves
- they assumed all out-group members felt the same way about artwork preferences, essentially treating the entire out-group as a singular individual
- they didn't do this for in-groups - in-group members were individuated while out-group members were collapsed into homogeneous categories
- this demonstrates that merely being told someone is "not on your side" helps people manufacture reasons to reinforce categorical perceptual perspectives

**computational perspective: why categorize?**

rather than simply condemning categorization as harmful, the we asked a computational question: what is the function of categorization? the answer connects to part 2's bounded rationality framework:

the social world is extraordinarily complex - many people, diverse behaviors, constant interactions. just as you can't calculate the odds perfectly for a single complex decision, you can't scale that up to thinking about all entities in the world. categorization simplifies perception, functioning as a heuristic that saves precious cognitive resources. by making simplifying assumptions, you don't have to think as hard. this connects bounded optimality and resource rationality to social phenomena like othering - the tendency to collapse out-group variation helps make decisions faster and makes the complexity of the social world manageable for action and interaction.

**three-step process of social categorization**

we outlined how categorization works in practice:

1. **detecting cues:** making predictions from signals (biological motion, movement patterns) - similar to animacy detection from earlier in the course
2. **categorization:** taking cues and mapping them onto recognized categories, collecting evidence to fit things into coherent groupings
3. **knowledge enrichment:** applying pre-existing knowledge about the assigned category to enrich understanding - like seeing an unusually shaped water bottle and knowing what to do with it without needing to see every variation

**trait theory and the stereotype content model**

in the 1960s-70s, social psychology developed trait theory to describe a taxonomy of people. early experiments (surveys of people's interactions) revealed that social attributes seem to cluster along at least two dimensions:

- **social/emotional qualities:** helpful, sincere vs. unpopular
- **intellectual/cognitive capacity:** persistent, determined vs. frivolous, foolish

this evolved into the highly influential stereotype content model (fiske et al., 2002), which organizes social perception along two axes:

- **warmth:** social/emotional goodness
- **competence:** intellectual/cognitive capacity

the model argues that people categorize individuals and social groups into clusters based on high/low combinations of these dimensions. making quick assumptions about where someone falls (e.g., low competence/low warmth vs. high competence/low warmth) allows predictions about that individual's characteristics. this same logic of trait attribution to individuals extends to how we think about social groups.

the visual analogy: instead of tracking individual dots scattered across warmth-competence space, people simplify by assuming there are just "red dots, blue dots, and green dots" - categorical clusters. once you know what red dots do, anything that signals "red dot" allows assumptions about behavior and motivations.

**stereotyping as mechanistic process**

from a mechanistic standpoint, stereotyping facilitates inferences about unobserved behaviors and traits. just as you haven't seen every object but can interact with new ones through categorical understanding, simplifying assumptions facilitate predictions about how to behave, how others are behaving, and why they're doing what they're doing - even when you haven't met everyone in the world.

**trade-offs: when fast-and-frugal fails**

as a heuristic, stereotyping is fast and frugal - automatically categorizing is efficient and better than needing to figure out every new object from scratch. but like all heuristics, it has trade-offs:

1. **poor performance in diverse/changing environments:** you'll be wrong more often than right
2. **poor predictions about specific individuals:** lewin showed that behavior results from people × environments; simon added that adaptive responses to environments matter. stereotyping, by design, doesn't account for individual-environment interactions
3. **poor guidance for actions toward individuals:** mispredicting a person means mistreating them

**alternative algorithms for social cognition**

We emphasized that stereotyping isn't something we should necessarily avoid - it happens automatically as a consequence of our tendency to categorize perceptions. however, for treating individuals, we have other optimal algorithms from earlier in the course:

- **causal inference:** slower, more deliberate, refined over experience - leverage understanding of how things work in the world to understand why a person does what they do
- **simulation:** even without experience with a specific person, imagine what you would do in their situation - this is the opposite of stereotyping because you're not relying on cues about their category, but imagining yourself in their position
- **theory of mind:** includes simulation but extends to empathy and altruism - making inferences about what another person needs, likes, or feels even without direct interaction

these processes are slower and take more time but provide more accurate understanding of individuals than categorical heuristics.

### Highlights

- the minimal group paradigm and transitivity together explain why arbitrary social divisions create real psychological and behavioral consequences - even knowing about these effects doesn't prevent them from occurring.

- categorization serves a bounded rationality function: the social world's complexity requires cognitive shortcuts, making stereotyping an inevitable consequence of resource-limited cognition rather than simply a moral failing.

- the stereotype content model (fiske et al., 2002) provides a foundational two-dimensional framework (warmth × competence) that has influenced decades of research on social perception and continues to shape how we understand first impressions and group-based judgments.

- out-group homogeneity bias (wilder's artwork studies) reveals a key asymmetry: we maintain rich, individuated representations of in-group members while collapsing out-group variation, treating diverse individuals as a singular category even when group membership is completely arbitrary.

- we connected three parts of the course: part 1's causal inference and simulation provide alternatives to stereotyping; part 2's bounded rationality explains why stereotyping exists; part 3 explores when these fast-and-frugal social heuristics break down and harm our understanding of specific individuals.
