# CLAUDE.md

The `docs/index.md` file contains the full list of papers htstructured summaries of academic papers for a social cognition course. Each paper follows a standardized format to ensure consistency and readability.

---

## Standardized Format Specification

### 1. H2 Title Line

**Format:** `## YEAR — Author(s). (YEAR). Title. *Journal/Source.*`

**Rules:**
- Use em-dash (—) after the first year, not hyphen (-)
- Italicize journal/source name with `*asterisks*`
- Title text is NOT italicized
- Year appears twice: once at start, once in parentheses after author(s)
- For undated entries: `## n.d. — Author. (n.d.). Title. *Source.*`
- Period goes INSIDE the closing asterisk: `*Source.*`
- Keep author names concise (primary author + et al. if multiple, or list 2-3 authors max)

**Examples:**
```markdown
## 1944 — Heider, F., & Simmel, M. (1944). An Experimental Study of Apparent Behavior. *Journal of Psychology.*

## 2007 — Gray, H. M., Gray, K., & Wegner, D. M. (2007). Dimensions of Mind Perception. *Science.*

## n.d. — Dennett, D. C. (n.d.). A Précis of The Intentional Stance. *Philosophical Review.*
```

---

### 2. Full Citation

**Format:** `**Full Citation:** Author(s). (YEAR). Title. *Journal/Source.*`

**Rules:**
- Bold label `**Full Citation:**` followed by citation on same line
- This can include full details (volume, issue, pages) that don't appear in H2
- Maintain standard academic citation format

**Example:**
```markdown
**Full Citation:** Heider, F., & Simmel, M. (1944). *An Experimental Study of Apparent Behavior.* Journal of Psychology.
```

---

### 3. Topic Tags

**Format:** `**Topic Tags:** tag1, tag2, tag3`

**Rules:**
- Bold label `**Topic Tags:**` followed by tags on same line
- Tags are comma-separated (no bullets, no heading)
- Maintain original tag content

**Example:**
```markdown
**Topic Tags:** Attribution theory, Animacy, Intentional stance
```

---

### 4. Section Headers

**Format:** All section headers use `###` (h3)

**Standard sections (in order):**
1. `### Core Question / Problem`
2. `### Conceptual or Computational Framework`
3. `### Methods Overview`
4. `### Key Findings` (or Key Findings / Claims / Proposals)
5. `### Interpretation & Significance`
6. `### Computational‑Social‑Cognitive‑Scientist Hat`
7. `### Teaching Hooks`
8. `### Pedagogical Lens`
9. `### Connections`
10. `### Key Quotes or Phrases`
11. `### Concept Graph`

**Rules:**
- ALL section headers must be h3 (`###`), never h5 (`#####`)
- Not all papers have all sections
- Some papers may have additional unique sections

---

### 5. Concept Graph with Nested Definitions

Some papers include glossary-style definitions. These should be nested bullet lists under the `### Concept Graph` section.

**Format:**
```markdown
### Concept Graph
- Main concept relationships here
- More relationships here
  - **Term Name:** Definition text. **Notable Figures:** X. **Related Concepts:** Y, Z.
  - **Another Term:** Definition text. **Notable Figures:** A. **Related Concepts:** B, C.
```

**Rules:**
- Definitions are nested with 2-space indentation
- Term names are bold
- Use bold labels: `**Notable Figures:**`, `**Related Concepts:**`, `**Definition:**`
- NO standalone h3 definition sections after the Concept Graph

**Example:**
```markdown
### Concept Graph
- Symbolic tokens + Operators → compositional reasoning.
- IPL / GPS implementations → historic demonstrations of symbolic adequacy.
  - **Newell & Simon Test:** A set of practical criteria for evaluating whether a theory of cognition can adequately express and operate on the symbolic structures it posits. **Notable Figures:** A. Newell, H. A. Simon. **Related Concepts:** Physical Symbol System; Representation.
```

---

## Efficient Workflow for Formatting Tasks

### General Approach

When asked to standardize or fix formatting:

1. **Break into discrete steps** - Each type of change (citations, tags, headers, etc.) should be one step
2. **Use sub-agents for each step** - Delegate to general-purpose sub-agents to save context
3. **Have a second sub-agent verify** - Always have a separate sub-agent check the work
4. **Stage for commit after each step** - Use `git add` and `git status` after verification
5. **Wait for user approval** - User reviews and commits before proceeding to next step

### Step-by-Step Process Template

For each formatting change:

```markdown
1. DELEGATE: Launch sub-agent with clear instructions
   - Specify exact format requirements
   - Include examples
   - Ask for summary report

2. VERIFY: Launch second sub-agent to check work
   - Different agent for fresh perspective
   - Check for edge cases
   - Fix any issues found

3. STAGE: Prepare for commit
   - `git add changed/created file`
   - `git status` to confirm

4. REPORT: Summarize to user
   - What was changed
   - Number of items affected
   - Any issues found/fixed
   - Confirmation it's ready for review

5. WAIT: User commits before proceeding
```

### Why This Workflow?

- **Sub-agents save context**: Each sub-agent gets fresh context, avoiding token limitations
- **Verification catches errors**: Second pair of eyes prevents mistakes
- **Incremental commits**: Easier to review and rollback if needed
- **Clear communication**: User always knows what's happening


