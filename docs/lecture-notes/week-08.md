# Part 3 - Week 8 Lecture Notes

## Mon-11-17 Stereotypes as Overgeneralization & Face Perception
**Big Questions.** Why do we categorize people into stereotypes despite living in diverse, changing environments? How do first impressions from faces drive rapid social judgments, and what are the consequences?

### Key Ideas
- **Stereotyping as Heuristic:** Categorization simplifies percepts by collapsing individual variability into group labels, reducing demands on attention, memory, and decision-making
- **Stereotype Content Model (Warmth × Competence):** Groups are bundled along two primary dimensions—warmth (trustworthiness, friendliness) and competence (ability, intelligence)—creating a trait space for social categorization
- **Text Embeddings:** Statistical models that convert words into numerical representations, capturing semantic similarity (e.g., "statistics" clusters with "math"; used to analyze historical stereotype content)
- **Overgeneralization Hypothesis (Zebrowitz):** Stereotyping emerges from ancient adaptive mechanisms for rapid friend-or-foe detection, but becomes inaccurate when applied to diverse modern environments
- **First Impressions (200ms):** Face perception triggers automatic judgments within ~200 milliseconds; while impressions can change with more information, initial snap judgments stabilize quickly
- **Oosterhof & Todorov Two-Dimensional Model:** Computational face analysis reveals two primary axes of judgment—trustworthiness (rounder features) and dominance/threat (sharper features)

### Lecture Notes

**The Adaptive Function of Categorization**
- Perception is an act of categorization, influenced by multiple factors (context, prior knowledge, features)
- Categorization serves as a bounded rational strategy: helps constrain cognitive resources (attention, memory, effort, decision time)
- In the social domain, categorization means collapsing the rich variability of out-group individuals into simplified group labels or identities
- Classic experiments (from previous lectures) demonstrated how we perceive out-group members as more similar to each other than they actually are (out-group homogeneity effect)

**Stereotype Content Model: Warmth and Competence Dimensions**
- Building on trait theory (individuals vary along dimensions capturing intellectual capacity, social disposition), Susan Fiske, Amy Cuddy, and colleagues (2002) proposed groups are perceived along two primary axes:
  - **Warmth dimension:** How friendly, trustworthy, or well-intentioned a group seems
  - **Competence dimension:** How capable, intelligent, or skilled a group appears
- Stereotyping involves placing individuals/groups into a two-dimensional trait space (warmth × competence), then using that categorization to make automatic inferences about unobserved behaviors and traits
- This serves as a heuristic: once categorized, future encounters allow rapid predictions without detailed individual assessment
- **Critical limitation:** Stereotyping is only adaptive in unchanging, homogeneous environments where group membership reliably predicts individual traits

**Temporal Dynamics of Stereotypes: Evidence from Natural Language**
- Charlesworth and colleagues analyzed 200 years of Google Books text to track stereotype content over time
- Methodology: Extracted descriptions of social groups (Black/White, men/women, young/old, rich/poor) and analyzed top 10-50 associated trait words per decade
- Used **text embeddings** (same technology underlying ChatGPT) to convert words into numerical representations capturing semantic similarity
  - Example: "statistics" and "math" cluster together; "lion" and "tiger" cluster together
  - Embeddings allow quantitative comparison of how similar group descriptions are across time periods
- **Key findings:**
  - **Context matters:** Descriptions vary significantly by source (news, informational articles, books) and time period, showing stereotype content is shaped by social context
  - **Change over time:** Top trait associations for groups drift across decades, reflecting changing societal attitudes
  - **Some consistency:** Despite variation in specific words, some enduring biases about group identities persist
  - **Moderate differentiation:** Groups are described more similarly to each other than intuition suggests; hard categorical boundaries are less stable than we might expect
- **Implication:** Stereotypes are noisy, unstable, and change with social context—they only work well in static, homogeneous environments that no longer reflect modern reality

**The Overgeneralization Hypothesis**
- Leslie Zebrowitz proposed that stereotyping arises from **overgeneralizing** an ancient adaptive mechanism
- **Original adaptive function:** Rapid perception-based judgments for survival-critical assessments (friend or foe? potential mate?)
- **The mechanism is stable:** The ability to make quick snap judgments based on perceptual cues has remained consistent over evolutionary time
- **The content is unstable:** What specific traits/categories we map onto people changes based on current social context, making stereotypes inaccurate and error-prone
- **Modern problem:** Social category membership is a weak predictor of individual traits and behavior
- Even though we have an automatic disposition to categorize (like mentalizing), it represents an **overgeneralization** in diverse modern environments—we have more powerful cognitive tools available for understanding individuals

**External Signals: Face Perception Basics**
- Shifting from abstract shapes (triangles, dots) to the most obvious social signal: **faces**
- **Speed of impression formation:** Almost all face-based judgments form within the first **200 milliseconds** of viewing
  - This doesn't mean impressions are locked/unchangeable
  - It means giving people more time doesn't significantly alter initial snap judgments after ~200ms
- **Automaticity and biological basis:**
  - Faces immediately capture attention
  - Newborns (within one hour of birth) preferentially attend to faces or face-like configurations
  - Attention to faces comes with **automatic attributions** of internal states: Is this person threatening? Trustworthy? What are they feeling?
- Parallel to Heider-Simmel shapes: perception automatically triggers inferences about mental states behind the stimulus

**Computational Face Perception: Oosterhof & Todorov (2008)**
- Landmark study using 3D facial meshes scanned from hundreds of real faces
- Methodology:
  - Showed participants many faces and collected unconstrained descriptions (likability, trustworthiness, preferences)
  - Built a statistical model mapping facial features (smiles, eyebrow raises, furrows) to quick impressions (1-200ms judgments)
  - Generated **artificial synthetic faces** representative of different impression profiles
- **Key finding:** Two primary axes of face evaluation emerged from the data:
  1. **Trustworthiness dimension:** Rounder facial features associated with higher trustworthiness judgments
  2. **Dominance/threat dimension:** Sharper, more angular features associated with perceptions of dominance and aggression
- The model never explicitly learned word meanings—it statistically characterized how faces map to judgments based on how people naturally described them

**Modern Advances: Deep Learning Face Models**
- Same authors (Oosterhof & Todorov) recently published updated work using deep neural networks
- Fed the model millions of face images using modern AI technology
- Generated **100% synthetic faces** (not real people) informed by patterns in human first impressions
- Richer, more complex feature representations than original 2008 work
- Can tease apart nuanced facial features driving different impression dimensions (attractiveness, competence, etc.)
- **Caution:** Not a simple one-to-one mapping (e.g., "this skin color = competence")—the space of features driving impressions is rich and multidimensional, some intuitive and some non-obvious

**Real-World Consequences of Face-Based Impressions**
- Perceptions shape reality: first impressions have measurable real-world effects
- **Open question:** Are these impressions accurate? (Does an "untrustworthy-looking" face predict defection in Prisoner's Dilemma?)
- **What we know:** Even without any contextual information about individuals, faces alone powerfully drive impressions
- People perceived as more competent, trustworthy, or dominant based on facial appearance face different treatment and outcomes

### Highlights
- Stereotyping is a **bounded rational heuristic** that collapses individual variability into group categories to save cognitive resources, but only adaptive in unchanging, homogeneous environments that don't reflect modern diversity
- **Charlesworth et al.'s text embedding analysis** of 200 years of Google Books reveals stereotype content is **unstable and context-dependent**, drifting with societal changes while maintaining some enduring biases—contradicting the notion that stereotypes are fixed
- The **overgeneralization hypothesis** (Zebrowitz) explains stereotyping as ancient adaptive mechanisms (friend-or-foe detection) misapplied to modern contexts: the **mechanism is stable** (rapid snap judgments), but the **content is unstable and inaccurate** (category membership poorly predicts individual traits)
- Face perception operates with remarkable speed (**~200ms for stable impressions**) and automaticity (newborns preferentially attend to faces), triggering immediate attributions about internal states and traits
- **Oosterhof & Todorov's computational models** (2008 and recent deep learning updates) reveal two primary dimensions of face evaluation—**trustworthiness** (rounder features) and **dominance** (sharper features)—with modern AI enabling richer, more nuanced mappings between facial features and first impressions that shape real-world treatment of individuals

---

## Wed-11-19 Face Perception and the Limits of Physiognomy
**Big Questions.** How do we make rapid judgments from faces, and what are the limits of using facial features to predict behavior? What is the relationship between face perception, stereotyping, and the dangers of AI systems claiming to detect personality or character from faces?

### Key Ideas
- **Face-like stimuli capture attention**: Newborns as young as one hour old orient toward face-like patterns, suggesting an innate attentional bias
- **200-millisecond judgments**: First impressions from faces stabilize within 200ms of exposure, representing extremely rapid social evaluation
- **Two-dimensional evaluation space**: Face judgments organize around **trustworthiness** (intentions toward me) and **dominance** (ability to enact those intentions)
- **Emotional resemblance as primary cue**: The strongest predictor of face impressions is structural resemblance to emotional expressions (happiness signals trustworthiness, anger signals dominance)
- **Overgeneralization hypothesis**: Face perception involves detecting cues → mapping onto categories → applying category knowledge, but this process overgeneralizes from momentary expressions to stable traits
- **Perception is construction, not objective reality**: Face impressions reflect subjective experience, predict the perceiver's behavior, but do not accurately predict the target's future behavior
- **Physiognomy fallacy**: The belief that facial features reliably predict character or behavior is a scientific fallacy with dangerous historical precedents (Lombroso, Nazi racial science)
- **AI models capture subjectivity, not objectivity**: Deep learning models can predict human impressions but should never be treated as detecting objective truth about personality or behavior

### Lecture Notes

**Foundations of Face Perception**

From the moment of birth, faces dominate our attention. Studies with newborns as young as one hour old demonstrate that face-like configurations in proper orientation immediately capture attention, suggesting an evolutionary prepared perceptual system. This attentional bias is followed by remarkably rapid evaluation processes.

Within **200 milliseconds** of viewing a face, people form stable impressions that don't significantly change with additional viewing time. These snap judgments aren't random—they organize systematically around two fundamental dimensions identified by **Oosterhof and Todorov (2008)**: **trustworthiness** (addressing "what are this person's intentions toward me?") and **dominance** (addressing "what is this person's ability to enact those intentions?"). These dimensions parallel other theoretical frameworks discussed in the course: the **Stereotype Content Model's** warmth and competence dimensions, and trait theory's historical focus on intellectual capacity and positivity/negativity of intentions.

**Cues Driving Face Impressions**

According to **Zebrowitz's** work, several categories of facial cues inform our impressions:
- **Attractiveness/value**: Features that drive approach motivation
- **Familiarity**: Demographics and features signaling "like me"
- **Baby-facedness**: Softer, rounder features (similar to how circles vs. triangles evoke different emotions in the Heider-Simmel animation)
- **Emotional resemblance**: The most powerful cue—structural resemblance to emotional expressions

Recent research demonstrates that **emotional resemblance is by far the strongest predictor** of face impressions. When people rate thousands of faces on trustworthiness and dominance, the extent to which a neutral face structurally resembles happiness or anger overwhelms other predictors. Even subtle hints of a smile or furrowed brow—features that might be barely noticeable—drive judgments of trustworthiness (happiness resemblance) and dominance (anger resemblance).

**The Three-Step Process: Detection, Categorization, Application**

Face perception follows the same process introduced in Part 1 of the course:
1. **Detect cues** in the environment (emotional expression-like features)
2. **Map cues onto category knowledge** (this looks like happiness; what do I know about happy people?)
3. **Apply category knowledge** to the target (this person is probably trustworthy)

This process is **automatic and constructive**—just as we couldn't help attributing mental states to moving shapes in the Heider-Simmel animation, we automatically make inferences from faces. Face perception is inherently a form of **stereotyping**: taking attributes and making inferences about individuals based on category membership.

**The Construction of Impressions**

Face impressions are **constructed** from social signals, not directly read from objective reality. In natural contexts, faces do provide meaningful information—they signal internal states and intentions **in that moment**. When someone smiles for a photograph, there's typically a connection between their facial display and their internal state. More often than not, people smile when happy, so inferring happiness from a smile isn't unreasonable given no other information.

However, the critical limitation is **temporal specificity**: a snapshot provides information about a momentary state, not stable personality traits or future behavior. Using snapshot judgments to make inferences over longer time periods "starts to fall apart really quickly."

**Face Impressions Predict Our Behavior, Not Theirs**

Face impressions are **reliable**—they consistently predict the perceiver's own behavior. Classic research shows that people's snap judgments of politicians' faces from official photographs reliably predict voting behavior, with judgments of competence correlating with vote margins. Similarly, trustworthiness impressions predict whether we approach or avoid someone.

But critically, **impressions don't predict the target's actual behavior**. Your impression of someone as trustworthy tells you about what you'll do next, not what they'll do next. This parallels the Heider-Simmel demonstration: what you subjectively saw predicts what you'll write when asked about it, but there was never a "correct answer" about the shapes' intentions. The same applies to face perception—there's no objectively "correct" personality reading from a face.

**Physiognomy: Historical and Contemporary Dangers**

In Alex Todorov's critical analysis, the lecture traced the return of **physiognomy**—the discredited belief that facial structure reveals character. This pseudoscience has deep historical roots (ancient Greeks, Renaissance polymaths) and reached its peak in the 19th century with figures like:
- **Cesare Lombroso**: "Father of criminal anthropology" who claimed criminals were evolutionary degenerates identifiable by facial features; his influence compared to Darwin's *Origin of Species*
- **Francis Galton**: Created composite photographs of "criminal types" (notably, all white faces in his studies)
- **Nazi racial science**: Used similar "scientific" justifications for categorization and persecution

The lecture emphasized: "This is the same kind of problems that people were dealing with in the 19th century. It hasn't changed at all. It's just the tools are new."

**Modern AI and the Physiognomy Fallacy**

Contemporary AI companies claim to detect personality traits, criminality, sexual orientation, and other characteristics from faces. Todorov and colleagues (including computer scientists Blaise Agüera y Arcas and Margaret Mitchell from Google) have written extensively critiquing these claims. Examples include:
- Israeli startup Faception claiming to identify "terrorists, pedophiles, bingo players" from faces, targeting homeland security
- Stanford study published in a prestigious journal claiming 70% accuracy for women, 80% for men in detecting sexual orientation from faces
- Various companies offering personality prediction from video

The fundamental error: treating **subjective impressions as objective accuracy**. Research demonstrates that "preconceptions and contexts around photographs are just as important as faces themselves." Everyone curates how they present themselves in photographs, making the idea of a "correct" reading scientifically nonsensical.

As Todorov stated: "The idea that there's a perfect correspondence between a person and their image is a psychological illusion. It's fueled by our experience with familiar people." With familiar people, we instantly recognize images and this evokes memories and feelings. But this doesn't mean strangers' faces objectively reveal their personality.

**The Overgeneralization Framework**

Social cognitive scientists understand face impressions as **overgeneralizations**. Snapshots can provide momentary indicators of internal state, but we overgeneralize from photographs, applying momentary signals to stable character judgments. Taking this overgeneralization as objective accuracy is a **scientific fallacy**—equivalent to claiming there's a "right answer" about what the Heider-Simmel shapes were "really" doing.

**Using AI as Cognitive Science Tools**

The lecture concluded with appropriate uses of AI for face perception research. Rather than claiming to detect objective personality traits, models can help reverse-engineer the subjective mapping process. The **deep learning face model** paper by Todorov's lab demonstrates this approach:

The researchers:
1. Collected judgments from people rating millions of faces on dozens of dimensions (trustworthiness, competence, age, attractiveness, emotion, demographics, stereotypes)
2. Trained deep learning models to predict these subjective ratings from facial images
3. Used the model to visualize what cues drive different impressions by morphing faces along rating dimensions

**Key findings**:
- The model learned to increase smile-like features for higher trustworthiness ratings
- For competence/intelligence ratings, **glasses emerged as a strong predictor**—something no theorist would have predicted a priori since glasses are a relatively recent invention
- Different dimensions revealed different cue combinations (baby-facedness, attractiveness, emotional expression)

The models don't tell us anything about objective personality. Instead, they reveal **how we integrate signals to construct impressions**—functioning as tools for cognitive science rather than objective detectors. As the abstract emphasizes, these models map between photographs and impressions, revealing the transformation from cues to subjective experience.

**Critical Distinction**

The operative word in the paper title ("Deep Models of Social Judgments") is **"judgments"**—these are models of subjective human perception, not objective truth. Models can capture our subjectivities and predict our impressions, but "we should never assume and try to think that what they're capturing is objectivity."

### Highlights

- Face perception is fundamentally a process of **categorization and stereotyping**, mapping detected cues onto category knowledge and applying that knowledge to individuals—the same three-step process underlying animacy detection and theory of mind
- **Emotional resemblance is the dominant cue**: Among all proposed factors (baby-facedness, attractiveness, demographics, facial width-to-height ratio), structural resemblance to emotional expressions—particularly happiness for trustworthiness and anger for dominance—most strongly predicts face impressions (relevant to **Oosterhof & Todorov 2008**)
- Face impressions are **reliable but not accurate**: they consistently predict the perceiver's own behavior (voting, approach/avoidance) but don't predict the target's future behavior, paralleling how Heider-Simmel interpretations predict what you'll write but not what shapes will do next
- **Physiognomy represents a scientific fallacy** with dangerous historical precedents from Lombroso to Nazi racial science; contemporary AI systems claiming to detect personality, criminality, or sexual orientation from faces repeat these errors with new tools (**Agüera y Arcas et al. 2017** critique)
- Modern deep learning approaches (like Todorov's model in the final paper) offer legitimate cognitive science value when used to **reverse-engineer subjective perception** rather than claim objective detection—revealing how cues like glasses (for competence) or smiles (for trustworthiness) shape our constructed impressions

---

## Fri-11-21 Computational Social Cognition: Face Perception and Affective Computing
**Big Questions.** How can AI models help us understand face perception while avoiding the trap of assuming they capture "objective truth" about people? What role does conceptual knowledge play in shaping what we perceive when we look at faces?

### Key Ideas
- **AI as Imitation Machines:** Modern AI systems (computer vision, facial expression models) are trained to imitate human judgments, not to discover objective truths about faces or mental states
- **Subjective Consistency vs. Accuracy:** Models can capture the consistency across human observers, but impressions predict the perceiver's behavior, not the target's actual traits or mental states
- **High-Dimensional Face Perception:** Moving beyond two-dimensional models (warmth/competence, trustworthiness/dominance) to embrace the full complexity of how multiple facial features, concepts, demographics, and social categories interact
- **Conceptual Knowledge Shapes Perception:** Our pre-existing concepts about traits, demographics, and social categories literally influence what we perceive in faces—perception is not just bottom-up processing
- **Facial Action Coding System (FACS):** A systematic categorization of facial muscle movements (action units) that forms the foundation of most modern facial expression recognition systems
- **Context Matters:** The same face can produce very different impressions depending on contextual information (name, setting, cultural background)

### Lecture Notes

#### The Limits of AI Face Perception Models

The lecture began by reviewing core ideas from the previous session about how we construct impressions from faces. When we perceive facial cues that resemble emotional expressions (happiness → trustworthy, anger → dominant), we use our categorical knowledge to inform judgments. However, a critical distinction emerged: **your impression predicts your own behavior but does not predict the other person's actual behavior or mental states.**

This distinction becomes crucial when building AI models. The predominant approach to modern AI is **training systems to imitate what people do**—whether computer vision models or language models. This means AI models can only reproduce human-like judgments about faces, not access a person's true mental states or traits. As with the **Turing test** (Alan Turing's proposal that a machine is intelligent if we cannot distinguish its output from a human's), these models pass for human-like performance, but this is fundamentally different from accessing objective reality.

The instructor emphasized that the **history of social cognition research demonstrates how stereotyping and impression formation reflect our tendency to generalize inaccurately from faces.** When we train a model using human judgments as "correct answers," we risk perpetuating the false assumption that these represent objective accuracy. AI models are really **expert imitation machines**—clever tools that replicate human patterns without knowing the underlying algorithms the brain uses.

#### Models as Tools for Understanding Subjective Consistency

Rather than viewing this limitation negatively, the lecture reframed AI models as **scientific tools for capturing subjective consistency across individuals.** A model that is sophisticated enough with sufficient data can reveal patterns in how groups of people consistently perceive faces, even if those perceptions don't map to objective truth.

This perspective allows researchers to explore cognition in more **ecologically valid ways.** The instructor noted that almost all theories about person perception seem to fall into approximately **two-dimensional spaces**—warmth × competence (Stereotype Content Model), trustworthiness × dominance (face evaluation)—but questioned whether this reflects the true essence of social cognition or is merely an oversimplification.

One of the instructor's early papers argued for expanding beyond these low-dimensional frameworks. By using AI to handle more **data diversity** (posed images, spontaneous expressions, images from the wild), researchers can test multiple factors simultaneously and unpack how humans integrate complex features when making judgments.

The **Peterson et al. model** exemplifies this approach by learning the complex mapping between visual features (edges, shapes, facial features, smiles, glasses, demographics) and the diverse judgments people make. These models show that face perception isn't just about dominance or trustworthiness—it's about **all of these dimensions together**. The model can characterize the full high-dimensional space of impressions.

#### Conceptual Knowledge Shapes Visual Perception

A major theoretical point: **human conceptual knowledge shapes our perceptions.** It's not enough to model visual input and the signals faces broadcast; we must also account for the **concepts** people bring to the task.

The **Freeman et al. work** demonstrated this empirically. Researchers measured people's ratings of concepts (relationships between different trait words) and their ratings of faces. The remarkable finding: there is **high consistency between how people associate concepts and how they make facial judgments.** The way you think about what "warmth," "dominance," or "kindness" means—and how these concepts relate to demographic categories (race, gender, age) and social categories (old/young, sick/healthy)—literally shapes what you perceive in a face.

When broken out by **stereotyped groups**, the conceptual structure differs. For example, people from different cultures might have different relationships between caring (C) and unhappy (U). One culture might see these as incompatible (if caring → not unhappy), while another sees them as potentially co-occurring (caring people can be unhappy). Given the **same input face**, these different conceptual relationships lead to **very different impressions.**

This framework suggests face perception is not just constructed from signals but also from **pre-existing conceptual knowledge** about:
- **Traits** (what warmth, dominance, kindness mean)
- **Demographics** (what it means to be Caucasian, Asian, etc.)
- **Social categories** (being old, young, sick)

#### Social Constructionism and Real-World Context

A recent paper on **social constructionism** illustrates real-world consequences. The example of "Sarah" demonstrates how perception integrates different types of information:

1. **Name/application context (no visual info):** When employers see "Sarah" on a resume with European-sounding name and previous jobs, they assume she's white and treat her application accordingly.

2. **Visual context (public setting):** When walking through the city wearing a hijab, others perceive her as a Black Muslim woman and react with suspicion. Upon hearing her Irish accent, they revise their impression (maybe mixed race).

3. **Driver's license context:** A facial image with just a name—what impressions might officials form from this limited information?

The lecture emphasized that **context matters tremendously.** The same individual is perceived radically differently depending on what information is available and in what setting. Modern computational social cognition aims to incorporate this complexity—how visual inputs, conceptual knowledge, cultural norms, and situational context all interact during impression formation.

#### Affective Computing and Facial Expression Recognition

The second half of the lecture introduced **affective computing**—using computational methods to detect and interpret emotional expressions. This field emerged from the **Facial Action Coding System (FACS)** developed in the 1970s by Paul Ekman and colleagues.

**FACS basics:**
- The face has over **40 different muscles**
- FACS labels these muscles and identifies patterns of **muscle movements** called **action units (AUs)**
- Complex combinations of AUs describe expressions (e.g., smiling involves specific AU combinations)
- This taxonomy can be applied to any face image

FACS powers almost all modern computer vision systems for facial expression recognition. The process involves:
1. **Face detection:** Is there a face in the image? Where?
2. **Face structure/landmarks:** Identifying key facial landmarks (eyes, nose, mouth)
3. **Orientation:** Is the face in profile, head-on, looking up/down?
4. **Action unit/emotion detection:** What muscular configurations are present?

Given enough labeled training data (humans annotating which AUs are present), models can be trained to predict how humans would rate any new face.

#### Problems with Current Affective Computing Models

The instructor posed the critical question: **If we're teaching machines to look at faces like people, how good are people at looking at faces?** The answer: people are pretty consistent but **not universally so**—cultural background, individual experience, and context create variability.

When comparing **state-of-the-art algorithms to humans**, the algorithms perform even worse, especially on **spontaneous expressions** (real people emoting in response to events) versus **posed expressions** (lab experiments). The models leave much to be desired.

Two problems emerged:
1. **There is no notion of objectivity to begin with.** Everyone sees something slightly different shaped by their culture and experiences.
2. **State-of-the-art algorithms can approximate what people consistently agree on, but they miss all the additional complexity and context.**

The idea that models can be "correct" about facial expressions is **flawed at its premise** because people themselves are inconsistent with each other.

#### A New Approach: Data-Driven Psychological Models

The instructor's lab developed a different approach with their **Py-FEAT toolbox.** Rather than treating model outputs as right/wrong answers, they use models for what they're good at: **seeing the whole picture over time.**

In an example study, people were filmed giving good news versus bad news. When analyzing all the facial action units over time, the raw patterns are complex and hard to interpret. Rather than labeling these as "correct" expressions of positive/negative emotion, the researchers asked: **Can we identify a particular configuration of facial movements that consistently separates these two contexts?**

Using hundreds of data points across people, they identified **the key parts of the face that separate positive versus negative communicative signals.** Critically, this isn't "the facial expression of bad news" but rather **the facial features that differentiate the communicative signal** in these contexts.

This approach produces **compact, psychologically informed models** that can be shared and applied to new contexts, experiments, and datasets. Rather than claiming to detect objective emotions, these models capture meaningful patterns that distinguish social contexts.

#### Models as Cumulative Scientific Tools

The lecture concluded with Alan Newell's vision: **models should be things we share and build upon as scientists.** Rather than disparate theories, we should iteratively refine models over time, adding what they miss.

**Modern affective computing** attempts to bring together:
- The best computational models of facial movements
- Rich, diverse data (spontaneous expressions, varied contexts)
- Psychological theory about how conceptual knowledge shapes perception

The goal is developing **more comprehensive accounts of how people process social signals** while avoiding the trap of treating model outputs as objective truth about individuals.

### Highlights
- Face perception involves more than two dimensions: High-dimensional models (like Peterson et al.) can capture the complexity of how humans integrate multiple features, going beyond traditional warmth/competence or trustworthiness/dominance frameworks
- AI models reproduce human biases, not ground truth: When trained on human judgments, computer vision systems learn to imitate stereotypes and impression formation processes, highlighting the importance of never conflating model predictions with objective accuracy about individuals
- Conceptual knowledge literally shapes what we see: Freeman et al. demonstrated that our pre-existing beliefs about how traits, demographics, and social categories relate to each other influences facial perception—perception is not purely bottom-up visual processing
- Context dramatically changes social perception: The Sarah example illustrates how the same individual is perceived completely differently depending on available information (name, visual appearance, setting)—challenging simplified lab-based approaches to social cognition
- Affective computing can reveal patterns without claiming objectivity: The Py-FEAT approach uses computational models as tools to identify consistent facial configurations that distinguish social contexts, rather than claiming to detect "true" emotions

---

### Week 8 Summary

- **Stereotyping as overgeneralization:** Face perception and social categorization reflect ancient adaptive mechanisms that overgeneralize in modern diverse environments—the mechanism (rapid judgment) is stable, but the content (what categories mean) is unstable and context-dependent.
- **Two-dimensional face space:** Oosterhof & Todorov's framework reveals trustworthiness and dominance as fundamental axes of face evaluation, driven primarily by emotional resemblance (happiness → trustworthy, anger → dominant).
- **Impressions predict our behavior, not theirs:** Face-based judgments are reliable (consistent across perceivers) but not accurate (don't predict target behavior)—a critical distinction that exposes the physiognomy fallacy.
- **AI as imitation, not detection:** Modern AI systems learn to replicate human judgments, not access objective truth; they can serve as tools for understanding subjective consistency while perpetuating biases if misused.
- **Conceptual knowledge shapes perception:** What we perceive in faces depends not just on visual input but on our pre-existing concepts about traits, demographics, and social categories—perception is constructed, not passively received.
