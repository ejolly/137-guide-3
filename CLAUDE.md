# CLAUDE.md - Paper Summaries Formatting Guide

This document outlines the standardized formatting for academic paper summaries in `Reading_Summaries.md` and the efficient workflow for maintaining consistency.

---

## Overview

The `Reading_Summaries.md` file contains structured summaries of ~27+ academic papers for a social cognition course. Each paper follows a standardized format to ensure consistency and readability.

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

When asked to standardize or fix formatting in `Reading_Summaries.md`:

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
   - `git add Reading_Summaries.md`
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

---

## Common Tasks

### Adding New Paper Summaries

When new papers are added to `Reading_Summaries.md`:

**Task:** "I've added [N] new paper summaries. Can you have a sub-agent review them for consistent formatting and fix any issues?"

**Sub-agent instructions:**
```
Review the [N] newest citations in Reading_Summaries.md and ensure they follow the standardized format:

1. H2 Title Line: ## YEAR — Author(s). (YEAR). Title. *Journal/Source.*
   - Em-dash after year, italicized source, period inside asterisk

2. Full Citation: **Full Citation:** [standard format]
   - Bold label, citation on same line

3. Topic Tags: **Topic Tags:** tag1, tag2, tag3
   - Bold label, comma-separated

4. Section Headers: All h3 (###)

5. Concept Graph: Nested definitions if present

Fix any issues using the Edit tool and report:
- Which papers were reviewed
- What issues were found
- What fixes were applied
```

---

### Full Reformatting (Multiple Steps)

If reformatting the entire document from scratch:

**Steps:**
1. Citation headings → Bold labels
2. Topic Tags headings → Bold labels
3. All section headers → h3
4. H2 title lines → Standardized format
5. Extra sections → Nested lists under Concept Graph

**Workflow:**
- Do each step separately
- Use sub-agent → verification sub-agent → stage → commit cycle
- Wait for user approval between steps

---

## Examples of Common Fixes

### Fix H2 Title

**Before:**
```markdown
## 2007 — Gray, H. M., Gray, K., & Wegner, D. M. (2007). Dimensions of Mind Perception. *Science*, 315, 619–619.
```

**After:**
```markdown
## 2007 — Gray, H. M., Gray, K., & Wegner, D. M. (2007). Dimensions of Mind Perception. *Science.*
```
*(Remove volume/page numbers from H2; keep in Full Citation)*

---

### Fix Citation Format

**Before:**
```markdown
### Full Citation
Dennett, D. C. (1971). Intentional Systems. *The Journal of Philosophy* / collected essays.
```

**After:**
```markdown
**Full Citation:** Dennett, D. C. (1971). Intentional Systems. *The Journal of Philosophy.*
```
*(Bold label, same line, remove extraneous notes)*

---

### Fix Topic Tags

**Before:**
```markdown
##### Topic Tags
- Attribution theory
- Animacy
- Intentional stance
```

**After:**
```markdown
**Topic Tags:** Attribution theory, Animacy, Intentional stance
```
*(Bold label, comma-separated, same line)*

---

### Convert Standalone Definition to Nested

**Before:**
```markdown
### Concept Graph
- Main relationships here

### Synchrony
**Definition:** Time-locked coupling across neural signals...
**Related Concepts:** resonance, entrainment
```

**After:**
```markdown
### Concept Graph
- Main relationships here
  - **Synchrony:** Time-locked coupling across neural signals... **Related Concepts:** resonance, entrainment
```

---

## Key Principles

1. **Consistency is paramount** - All papers should follow the exact same format
2. **Use sub-agents liberally** - They save your context and work in parallel
3. **Always verify** - Second sub-agent catches edge cases
4. **Commit incrementally** - Smaller commits are easier to review
5. **Document changes** - Always report what was done and why

---

## Quick Reference Checklist

When reviewing a paper summary, verify:

- [ ] H2 uses em-dash (—), not hyphen (-)
- [ ] H2 source is italicized with period inside: `*Source.*`
- [ ] H2 title is NOT italicized
- [ ] Full Citation has bold label on same line
- [ ] Topic Tags has bold label, comma-separated
- [ ] All section headers are h3 (`###`)
- [ ] No h5 (`#####`) headers remain
- [ ] Concept Graph contains nested definitions (if applicable)
- [ ] No standalone definition h3 sections after Concept Graph
- [ ] Proper spacing between sections (blank line after each)

---

## Notes

- This format was standardized across 27+ papers in January 2025
- The workflow using sub-agents was optimized to handle large-scale reformatting efficiently
- When in doubt, refer to existing papers as examples
- File is under version control; use `git status` and `git add` before commits
