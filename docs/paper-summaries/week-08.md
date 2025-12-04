# Week 08 Paper Summaries

## Face Perception and First Impressions

---

## Oosterhof, N. N., & Todorov, A. (2008). The functional basis of face evaluation. *Proceedings of the National Academy of Sciences*, 105(32), 11087-11092.

**Topic Tags**: face perception, trait inference, trustworthiness, dominance, valence evaluation, emotional expression overgeneralization, principal components analysis, computational modeling, social cognition, first impressions, amygdala, approach-avoidance behavior

### Core Question / Problem
Why do people spontaneously and rapidly evaluate emotionally neutral faces on multiple trait dimensions (e.g., trustworthiness, dominance, attractiveness), and what fundamental dimensions underlie these highly correlated judgments that predict important social outcomes despite not necessarily being accurate?

### Conceptual or Computational Framework
The study employs an overgeneralization hypothesis as its theoretical foundation: trait evaluations of neutral faces are constructed from facial cues that have evolutionary significance. Computationally, the authors use a data-driven approach combining principal components analysis (PCA) of behavioral judgments with 3D statistical face modeling (based on 50 principal components from laser-scanned faces). This maps to Marr's levels by identifying the computational goal (inferring intentions and capacity for harm), the algorithmic level (dimensional reduction via PCA, linear modeling of face space), and implementational cues (specific facial features resembling expressions and maturity markers).

### Methods Overview
Study 1: 55 participants generated unconstrained face descriptions, yielding 14 trait categories. Studies 2.1-2.15: 327 participants rated 66 emotionally neutral photographs on these traits plus dominance (9-point scales; Cronbach's ± e0.90). PCA revealed two dimensions. Studies 3-4: 54 participants judged 300 computer-generated faces on trustworthiness and dominance to build predictive models. Studies 5-6: 36 participants validated models by judging faces varying systematically along modeled dimensions. Studies 7-12: 84 participants categorized emotions and rated faces on anger-happiness, baby-faced-mature, and feminine-masculine scales to identify facial cues. Studies 13-14: 39 participants rated threat to test dimensional model predictions.

### Key Findings / Claims

- **Two-dimensional structure**: PCA identified valence (PC1: 63.3% variance) and dominance (PC2: 18.3% variance) as orthogonal dimensions underlying all trait judgments. Trustworthiness judgments correlated r=0.92 with valence; dominance judgments correlated r=0.87 with PC2.

- **Differential sensitivity to facial cues**: Valence/trustworthiness dimension was highly sensitive to features resembling happy vs. angry expressions (linear F(1,18)=123.10, p<0.001 for anger-happiness judgments). Dominance dimension was sensitive to facial maturity and masculinity cues (linear F(1,15)=16.40, p<0.001 for maturity with masked features) but not to emotional expression cues (F<1 for anger-happiness).

- **Threat as composite judgment**: Threat judgments were reproduced as a function of the two orthogonal dimensions (both trustworthiness r=-0.65 and dominance r=0.68 correlated with threat; p<0.001). A threat vector constructed by rotating trustworthiness and dominance vectors 45° predicted actual threat judgments with 0.98 SD correspondence.

### Interpretation & Significance
This work provides a unifying computational framework showing that diverse social judgments from faces reduce to two fundamental dimensions reflecting evolutionarily adaptive concerns: inferring harmful intentions (valence) and capacity to implement those intentions (dominance). The overgeneralization mechanism explains why face judgments are rapid and compelling yet often inaccuratethey misattribute evolutionarily significant cues (emotional expressions signaling approach/avoidance, physical strength markers) to stable personality traits. The amygdala's involvement in trustworthiness evaluation likely reflects general valence processing rather than specific trait assessment. This framework accounts for real-world impact of face judgments (electoral success, sentencing decisions) while explaining their limited validity in predicting actual personality or behavior.

### Computational-Social-Cognitive-Scientist Hat

**What would Herb Simon think?** Simon would recognize this as a quintessential satisficing solution exemplifying bounded rationality. Rather than conducting time-intensive, information-rich personality assessments, the cognitive system rapidly categorizes faces using readily available perceptual cues (expression-like features, structural markers of strength). The two-dimensional solution represents an efficient computational reductioncollapsing infinite trait space into the minimal representation needed for adaptive decision-making: "Can this person harm me?" (dominance) and "Will they?" (valence). This embodies Simon's scissors: the environment provides evolutionary pressures making certain cues statistically predictive (angry expressions historically signaled danger), while cognitive architecture exploits these regularities through overgeneralization heuristics that trade accuracy for speed.

**What would Kurt Lewin think?** Lewin would emphasize that these face evaluations demonstrate B = f(P,E) at multiple levels. The perceiver brings evolved perceptual sensitivities (P: amygdala reactivity, expression detection mechanisms), but the behavioral outcome (trait inference) emerges from interaction with environmental structure (E: the specific facial configuration). Critically, Lewin would note that the "psychological field" here involves a mismatchperceivers respond to neutral faces as if they were emotion-laden social situations requiring immediate approach/avoidance decisions. The functional basis is adaptation to ancestral environments where such rapid categorization had survival value, but modern environments present these cues in contexts (job interviews, elections, courtrooms) where their diagnostic validity is minimal, creating systematic person-environment misalignment.

### Connections

- **Links to Ekman's basic emotions research**: The valence dimension's sensitivity to anger and happiness expressions builds on universal emotion recognition work, suggesting trait inference co-opts emotion perception machinery.

- **Relates to Zebrowitz's babyface overgeneralization**: The dominance dimension's sensitivity to facial maturity cues (baby-faced features reduced perceived dominance) directly confirms Zebrowitz's theoretical predictions about overgeneralizing developmental cues.

- **Contemporary relevance to AI fairness and face-based algorithms**: This dimensional model has become foundational for understanding biases in face-based AI systems (hiring algorithms, criminal risk assessment tools) that may inadvertently encode these evolved but accuracy-limited heuristics, raising critical questions about automated decision-making from facial features.

---

## Zebrowitz, L. A. (2004). The origin of first impressions. *Journal of Cultural and Evolutionary Psychology*, 2(1-2), 93-108.

**Topic Tags**: first impressions, face perception, overgeneralization, attractiveness, babyface effect, emotion perception, facial identity, fitness cues, ecological theory, social perception, consensual judgments, trait attribution, halo effect

### Core Question / Problem
Why do people form consensual first impressions from facial appearance, and how do they achieve this agreement? The paper addresses the origins of widespread consensus in trait judgments made from neutral facial photographs across cultures, ages, and raters.

### Conceptual or Computational Framework
The paper proposes four face overgeneralization hypotheses grounded in ecological theory of social perception (derived from Gibson's object perception theory). The framework maps to both Simon's scissors (structured facial information in the environment interacts with evolved perceptual preparedness) and Marr's computational level (the adaptive function is detecting fitness, age, emotion, and identity information). The core mechanism is overgeneralization: psychological qualities accurately revealed by functionally significant facial markers (babies, emotions, familiar identities, or fitness-related anomalies) are overgeneralized to faces that merely resemble these categories. These errors are adaptive because failing to respond appropriately to actual babies, emotions, identities, or unfit individuals would be more costly than false alarms.

### Methods Overview
The paper reviews existing evidence and presents new analyses. Archival data reanalysis examined attractiveness, averageness, symmetry, and masculinity ratings alongside IQ scores and health measures from representative samples, testing predictions separately for faces above versus below median appearance values. Connectionist modeling studies used neural networks trained to discriminate 60 anomalous faces (from medical atlases) from 60 normal faces, then tested on 80 normal faces varying in attractiveness. Networks used normalized facial metrics from 64 landmark points as inputs. Trait ratings (health, intelligence, sociability, warmth, strength) were collected on 7-point scales with high inter-rater reliability.

### Key Findings / Claims
- **Bad genes hypothesis supported**: Low attractiveness, averageness, symmetry, and masculinity validly predicted low fitness (IQ, health) in faces below the median, but high levels of these qualities did not predict high fitness in faces above the median. People accurately judged intelligence and health from faces below median attractiveness but showed no accuracy for faces above the median.

- **Overgeneralization confirmed**: Perceivers utilized attractiveness and its components as cues to intelligence and health across the entire attractiveness range, even where these cues had no validity (above median). Connectionist networks trained to detect anomalous faces predicted trait impressions of normal faces - those resembling anomalous faces were judged less healthy, intelligent, attractive, sociable, warm, and strong, independent of actual health/IQ and controlling for babyfaceness and smiling.

- **Multiple overgeneralization effects**: Evidence supported babyface overgeneralization (babyfaced adults perceived as weak, submissive, naive), emotion overgeneralization (neutral faces resembling emotions judged accordingly), and identity overgeneralization (strangers resembling known individuals judged similarly).

### Interpretation & Significance
This work reframes the attractiveness halo effect as an adaptive overgeneralization rather than arbitrary social construction. By distinguishing "bad genes" (low attractiveness signals low fitness) from "good genes" (high attractiveness signals high fitness), the research reveals that facial perception is calibrated to detect problems rather than optimize mate selection. The ecological approach successfully generates novel, testable predictions about when impressions will be accurate versus erroneous, advancing beyond purely cognitive or evolutionary accounts. The findings suggest people may not simply "avoid the worst" but that anomalous face overgeneralization may have fostered selection of highly attractive mates despite this not being strictly necessary for viable offspring. This demonstrates how evolutionary and ecological principles can elucidate socially significant phenomena that traditional social cognition frameworks struggle to explain.

### Computational-Social-Cognitive-Scientist Hat
**What would Herb Simon think?** Simon would appreciate the "bad genes" finding as classic satisficing - the perceptual system evolved to detect "good enough" (not unfit) rather than optimize for maximum fitness. The overgeneralization represents bounded rationality: using simple heuristics (resemblance to anomalous faces) that work well enough in ancestral environments where truly anomalous faces were the real threat. The scissors cut at the joint between structured environmental information (facial metrics that actually predict low fitness) and cognitive adaptation (preparedness to respond to those markers).

**What would Kurt Lewin think?** Lewin's B = f(P,E) is perfectly embodied here: impressions emerge from the interaction between person characteristics (evolved perceptual mechanisms, individual experience with faces) and environmental structure (the actual distribution of facial features in the population). The finding that accuracy holds only for below-median faces suggests the "life space" is asymmetrically structured - the psychologically real environment emphasizes threat detection over optimization. Lewin might note that changing the environmental context (e.g., encountering more truly anomalous faces) could recalibrate the overgeneralization threshold through perceptual learning.

### Connections
- Links to **attractiveness and mate selection research**: Refines good genes hypothesis by showing fitness detection operates primarily at the low end of the distribution, with implications for sexual selection theory.
- Connects to **stereotype accuracy literature**: Demonstrates when facial stereotypes have kernel-of-truth (below median attractiveness) versus when they are pure overgeneralization (above median).
- Relates to **stigmatization and social exclusion**: Provides evolutionary mechanism for why facially anomalous or unattractive individuals face discrimination - overgeneralized disease/defect avoidance.
- Bridges to **neural network models of face processing**: Shows that similarity-based generalization in artificial neural networks captures human overgeneralization patterns, validating connectionist approaches to social perception.
- Connects forward to **contemporary work on AI bias**: The overgeneralization mechanisms may be preserved in machine learning systems trained on human judgments, potentially perpetuating systematic errors.

---

## Zebrowitz, L. A. (2017). First Impressions From Faces. *Current Directions in Psychological Science*, 26(3), 237-242.

**Topic Tags**: first impressions, overgeneralization effects, facial cues, baby-face overgeneralization, familiar-face overgeneralization, unfit-face overgeneralization, emotional-face overgeneralization, warmth/trustworthiness dimension, power/dominance dimension, impression accuracy, ecological theory of social perception, person perception, facial appearance, stereotype formation

### Core Question / Problem

Why do humans form rapid, consensual first impressions from faces that often prove inaccurate, yet this tendency appears universal across cultures and emerges early in development? This paradox suggests an adaptive function despite the potential for error and significant social consequences in domains like electoral success, judicial decisions, and employment.

### Conceptual or Computational Framework

The paper proposes that consensual first impressions reflect overgeneralizations of adaptive responses to facial cues. Facial qualities that ordinarily reveal important social information (e.g., age, familiarity, fitness, emotional state) influence impressions even when the target only physically resemblesbut does not actually belong tothe relevant category. This ecological approach emphasizes that impression formation evolved to respond to valid environmental regularities (adaptive context), but bounded cognitive systems overapply these heuristics (Simon's scissors). The framework identifies four overgeneralization mechanisms: baby-face, familiar-face, unfit-face, and emotional-face overgeneralization.

### Methods Overview

This is a theoretical review synthesizing research using diverse methods including: human raters judging neutral-expression face photographs for trait impressions (e.g., warmth, dominance, competence); computer modeling of facial metrics to quantify structural features; cross-cultural studies including indigenous Tsimane people in Bolivia; developmental studies with infants and children; and studies linking facial impressions to real-world outcomes. Key manipulations include varying facial babyfaceness, attractiveness, race, emotion resemblance, and specific features like eyebrow position.

### Key Findings / Claims

- First impressions from faces are formed rapidly (100 milliseconds or less) and automatically, with remarkable cross-cultural consensus extending to remote indigenous populations and appearing in infants and young children.
- Four overgeneralization effects explain consensual impressions: (1) baby-face overgeneralization leads to impressions of higher warmth and lower power/competence for more babyish faces; (2) familiar-face overgeneralization produces more positive impressions of familiar-looking strangers; (3) unfit-face overgeneralization causes unattractive faces to be judged as lower in warmth, power, competence, and health (the attractiveness halo effect); (4) emotional-face overgeneralization means neutral faces resembling angry expressions elicit impressions of higher dominance and lower warmth, while those resembling happy expressions elicit warmth impressions.
- These overgeneralization effects contribute to gender, age, and racial stereotypes: women's greater babyfaceness contributes to perceptions of higher warmth and lower power; older faces' resemblance to anomalous faces produces impressions of lower warmth and health; and emotion-resemblance patterns in Black and Asian faces can both suppress and create racial stereotypes (e.g., Black faces' greater resemblance to happy expressions suppresses some negative stereotypes, while their unfamiliarity enhances others).

### Interpretation & Significance

This work resolves the paradox of universal yet error-prone facial impressions by grounding them in adaptive ecological responses that get overgeneralized. The framework advances social cognition by identifying specific structural mechanisms underlying impression formation and explaining why culturally universal impressions can still be inaccurate. It bridges evolutionary, ecological, and social-cognitive perspectives, showing how adaptive perceptual systems designed for valid category detection (babies, emotions, fitness markers) produce systematic biases when applied to within-category variation. The real-world consequencesaffecting elections, legal judgments, and employmentunderscore the practical importance of understanding these mechanisms rather than simply documenting impression consensus or accuracy.

### Computational-Social-Cognitive-Scientist Hat

What would Herb Simon think? This exemplifies bounded rationality perfectly: the cognitive system uses fast, frugal heuristics (facial resemblance to adaptive categories) as a satisficing solution to the computationally expensive problem of accurately assessing strangers' traits. The "scissors" are evident: one blade is the environmental structure (valid correlations between facial features and traits in babies, emotions, fitness markers), the other is the cognitive architecture that overgeneralizes these patterns. The system sacrifices accuracy for speed and efficiency, accepting systematic errors as the cost of rapid social judgments.

What would Kurt Lewin think? The overgeneralization framework embodies B = f(P,E) by showing how behavior toward targets emerges from the interaction between perceiver characteristics (evolved perceptual mechanisms, prior experiences determining familiar-face effects, goals influencing attention to fitness cues) and environmental features (the target's actual facial structure). The field forces are particularly evident in how facial cues create psychological approach-avoidance vectors (e.g., baby-faced people inhibit aggression; attractive people elicit approach) that shape social interaction outcomes through self-fulfilling and self-defeating prophecies.

### Connections

- Extends Asch's classic impression formation work by identifying the actual stimulus information (facial structure) underlying trait inferences, moving beyond trait-word lists to ecological validity.
- Links to Todorov's work on computational modeling of face-based trait judgments and the two-dimensional structure (warmth/trustworthiness and power/dominance) underlying social perception.
- Connects to the mere-exposure effect literature by demonstrating generalized mere-exposure: familiarity effects extend from repeated exposure to novel faces resembling familiar ones, broadening understanding of implicit preference formation and in-group favoritism mechanisms.

---

## Peterson, J. C., Uddenberg, S., Griffiths, T. L., Todorov, A., & Suchow, J. W. (2022). Deep models of superficial face judgments. *Proceedings of the National Academy of Sciences*, 119(17), e2115228119.

**Topic Tags**: face perception, social trait inferences, trustworthiness, first impressions, deep neural networks, generative adversarial networks (GANs), StyleGAN2, computational modeling, impression formation, trait attribution, face space, ecological validity, facial attributes

### Core Question / Problem

How can we comprehensively model the diverse psychological attributes that people infer from faces (ranging from objective properties like age to subjective social traits like trustworthiness) across the full space of possible faces, contexts, and viewing conditions using expressive computational representations?

### Conceptual or Computational Framework

The paper bridges deep learning representations and psychological attribute judgments through a data-driven mapping approach. It uses StyleGAN2a generative adversarial network trained on 70,000 face photographsto provide 512-dimensional feature representations of faces, then learns linear mappings from these features to human attribute judgments via ridge regression. This approach aligns with Marr's levels by addressing the computational problem (what attributes are inferred), the algorithmic level (linear combinations of deep features predict judgments), and hints at implementation (neural network representations may parallel perceptual processing). The framework captures Simon's scissors by modeling how rich contextual variation in faces (lighting, pose, expression, accessories) interacts with cognitive inference processes.

### Methods Overview

The study collected over 1 million human judgments (the "One Million Impressions" dataset) from 4,157 participants rating 1,004 synthetic photorealistic faces generated by StyleGAN2 on 34 attributes. Attributes spanned three classes: relatively objective properties (age, adiposity, hair color), subjective social traits (trustworthy, dominant, smart), and fully subjective dimensions (familiar, looks like you). Each face received at least 30 ratings per attribute in a between-subjects design using continuous slider scales. Ridge regression with 10-fold cross-validation mapped 512-dimensional StyleGAN2 feature vectors to average attribute ratings, with regularization parameter » optimized for generalization. Twenty preregistered validation experiments (N=1,000) tested whether model-based face manipulations actually changed observers' impressions.

### Key Findings / Claims

- **Prediction accuracy approached human interrater reliability** for most attributes, with R² values ranging from 0.5 to nearly 0.8, though attributes like familiar, typical, and gay showed substantial gaps between model performance and reliability ceiling. The model's predictive performance would not have been achievable with fewer faces, fewer judgments per face, or lower-dimensional representations.

- **Large-scale data were critical**: Performance scaled with the number of rated faces (most attributes benefited through the full 100-1,000 face range), number of ratings per face (gains continued beyond 30 raters), and feature dimensionality (though as few as 10 dimensions captured bulk variance for some attributes, others benefited from the full 512 dimensions).

- **Validation experiments confirmed causal efficacy**: All 20 preregistered experiments showed that model-based manipulations systematically altered participants' impressions in the predicted direction (all F(2,98) > 14.13, p < 0.000005, ·² > 0.223) for both synthetic and real face photographs, demonstrating that the models capture psychologically meaningful dimensions rather than statistical artifacts.

### Interpretation & Significance

This work demonstrates that combining expressive deep learning representations with large-scale behavioral data can produce scientifically useful models of complex psychological phenomena that previously resisted comprehensive characterization. The approach enables infinite stimulus generation along controlled psychological dimensions, manipulation of arbitrary photographs to evoke target impressions, and prediction of impressions for any face imageadvancing face perception research beyond the limitations of landmark-based interpolation or parametric 3D meshes. The framework is general enough to model any attribute measurable via image annotations and provides a foundation for understanding how diverse physical cues combine to drive trait inferences, though interpretation remains challenging due to the naturalistic variation captured (e.g., distinguishing whether trustworthiness judgments reflect facial structure, expression, lighting, or accessories).

### Computational-Social-Cognitive-Scientist Hat

**What would Herb Simon think?** Simon would appreciate how this work exemplifies the scissors metaphor: the "blade" of cognitive simplicity (people make rapid, consistent trait inferences) cuts in coordination with the "blade" of environmental complexity (the vast space of possible faces, contexts, and viewing conditions). The linear models achieving near-ceiling performance suggest bounded rationalitypeople may use relatively simple decision rules (weighted combinations of perceptual features) to navigate an explosively complex stimulus space. The finding that as few as 10 dimensions can capture bulk variance for some attributes supports Simon's view that minds satisfice rather than optimize, extracting "good enough" information from high-dimensional inputs.

**What would Kurt Lewin think?** Lewin would emphasize that face judgments exemplify B = f(P,E): the behavior (trait inference) emerges from the interaction between person factors (shared stereotypes, individual differences in ratings) and environmental factors (facial features, context, lighting, accessories). The correlation analyses revealing that some attributes cluster while others remain independent (e.g., smart-attractive r = 0.01) suggest that the psychological "field" of face perception has distinct regions. Lewin might be particularly interested in how the same physical stimulus evokes different impressions depending on the broader context (e.g., how "attractive" changes meaning when rating children versus adults), and how manipulating one dimension (e.g., smartness) can inadvertently alter others (e.g., spawning glasses), revealing the interconnected field structure of social perception.

### Connections

- **Overgeneralization hypothesis**: Extends work by Zebrowitz and others showing that trait inferences arise from overgeneralizing valid cues (e.g., neotenous features signaling youth get misapplied to infer trustworthiness in adults); the model quantifies these multidimensional relationships across 34 attributes.

- **Cultural universality and variation**: Relates to recent cross-cultural work (Jones et al., 2021) questioning whether dimensional models of face perception generalize globally; the present model captures impressions from predominantly White North American raters, raising questions about cultural specificity of the learned mappings.

- **Ecological approach to perception**: The inclusion of naturalistic variation (lighting, accessories, context) aligns with Gibson's emphasis on studying perception in rich environments, contrasting with highly controlled lab stimuli; however, this makes it harder to isolate which cues drive specific inferencesa tension between ecological validity and experimental control.

---

## Agüera y Arcas, B., Mitchell, M., & Todorov, A. (2017). Physiognomy's New Clothes. *Medium*, May 6, 2017.

**Topic Tags**: physiognomy, scientific racism, machine learning bias, facial perception, social judgment, criminality detection, algorithmic fairness, trustworthiness stereotypes, essentialism, feedback loops, implicit bias

### Core Question / Problem
Can machine learning systems accurately infer criminality from facial appearance, or do such systems simply reproduce historical biases embedded in physiognomythe pseudoscientific practice of judging character from physical features? This paper critiques a 2016 study claiming 90% accuracy in predicting criminal status from ID photos, examining whether AI "launders" human prejudice through apparent objectivity.

### Conceptual or Computational Framework
The authors analyze supervised learning using convolutional neural networks (CNNs), which optimize millions of parameters to learn patterns from labeled training data. However, they demonstrate that these systems cannot distinguish causally meaningful correlations from incidental onesembodying Simon's scissors principle where the algorithm's "cuts" depend entirely on the structure of biased training environments (criminal justice data reflecting systematic discrimination). At Marr's computational level, the task appears to be "classify faces by criminality," but algorithmically it reduces to "detect correlates of judicial bias," and implementationally it amplifies the very stereotypes (facial expressions, contextual cues) that influence human judges.

### Methods Overview
Critical analysis of Wu & Zhang's (2016) study using 1,856 Chinese male ID photos (730 labeled "criminals," 1,126 "non-criminals") trained with AlexNet CNN architecture. Authors examine technical validity, explore what visual features the model learns (e.g., lip curvature, eye spacing, facial expressions), compare to human perception research on "trustworthiness" stereotypes, and review historical and contemporary evidence on bias in criminal judgment and face perception.

### Key Findings / Claims
- Wu & Zhang's claimed 90% accuracy likely reflects overfitting (insufficient training data for CNN complexity) and systematic confounds between groups (e.g., clothing, subtle expressions, demographic differences) rather than genuine criminality detection.
- Visual inspection reveals "criminal" images show frowning while "non-criminal" images show slight smilingsuperficial cues unrelated to actual criminal behavior but easily detected by deep learning.
- Research demonstrates humans cannot reliably infer character from faces despite strong stereotypical impressions; "untrustworthy" facial appearance predicts harsher legal judgments but not actual untrustworthiness or criminal behavior.
- The correlation likely reflects a circular process: facial appearance influences judicial bias ’ biased convictions create training labels ’ algorithms learn to predict judicial bias ’ systems are misinterpreted as detecting criminality ’ legitimizes and amplifies original bias.

### Interpretation & Significance
This work provides essential critical analysis of how machine learning can resurrect discredited pseudoscience by cloaking human prejudice in computational objectivity. It reveals that algorithmic "fairness" requires understanding not just technical implementation but the social processes generating training data. The criminal justice system's systematic biases (e.g., Black Americans incarcerated at 7× the rate of whites despite similar behavior) mean that predicting "criminality" from conviction records actually predicts exposure to discriminatory judgment. The paper demonstrates why seemingly objective AI systems require scrutiny of their entire causal chainfrom data collection through deploymentand warns against feedback loops where algorithmic predictions influence future human judgments that generate new training data.

### Computational-Social-Cognitive-Scientist Hat
**What would Herb Simon think?** Simon would recognize this as a catastrophic failure to map the task environment correctly. The scissors' blades don't fit: one blade (the algorithm) is designed to find stable patterns, but the other blade (the "criminality" label) actually measures unstable, context-dependent social judgments contaminated by the very facial features being predicted. The researchers committed the fundamental error of treating a satisficing heuristic (human judges using facial appearance) as ground truth, when bounded rationality predicts judges rely on cognitively available cues (appearance) precisely because true criminality assessment is computationally intractable.

**What would Kurt Lewin think?** Lewin's B = f(P,E) is violated at every level. The researchers treat "criminality" as a person property (P) when it's actually an outcome of person-environment interaction: the same individual in different circumstances (different legal systems, socioeconomic contexts, or even photographer conditions) produces different "criminality" classifications. Moreover, the measurement context (E) differs systematically between groups (mugshot conditions vs. campus photos in cited studies; possible demographic confounds in web-scraped vs. police-provided images), yet these environmental forces are attributed to person essences. Lewin would see this as psychological fascismusing pseudoscientific essentialism to deny the power of social fields.

### Connections
- Links to Todorov's work on facial trustworthiness stereotypes and their developmental origins (even 3-4 year olds show these biases), demonstrating these are learned cultural associations rather than accurate intuitions.
- Connects to Lombroso's 19th-century criminology and the broader history of scientific racism (Francis Galton's eugenics, Nazi physiognomy), showing modern ML can resurrect these frameworks with new legitimacy.
- Relates to contemporary algorithmic fairness research on "predictive policing" feedback loops, where biased deployment creates biased data that reinforces biasparticularly relevant given criminal justice system's documented racial disparities in arrest, conviction, and sentencing.
- Parallels gender essentialism in STEM (Victorian beliefs about women's mathematical incapacity became self-fulfilling through educational exclusion), illustrating how social structures can appear to validate prejudiced predictions.
- Connects to research on overgeneralization of emotion perception: "resting faces" that resemble emotional expressions (e.g., slightly downturned mouth appearing hostile) create persistent misattributions that compound over social interactions.
