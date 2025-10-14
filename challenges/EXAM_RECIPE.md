# Exam Generation Recipe

This document provides step-by-step instructions for generating shuffled exam versions from a question bank.

---

## Overview

The exam generation system creates **4 versions** of each exam by shuffling:
1. **Question order** (except Version A, which remains in original order)
2. **Answer choice order** (all versions including A)

**Outputs:**
- `challenge-XX-vA.md` - Original question order (instructor reference)
- `challenge-XX-vB.md` - Shuffled questions & answers
- `challenge-XX-vC.md` - Shuffled questions & answers
- `challenge-XX-vD.md` - Shuffled questions & answers
- `exam-map.md` - Answer key and cross-reference for TAs

**Reproducibility:** Uses fixed random seeds (0, 1, 2, 3) to ensure identical output on repeated runs.

---

## Directory Structure

```
challenges/
├── shuffle_exam.py          # The generation script
├── EXAM_RECIPE.md          # This file
├── challenge_01/
│   ├── question-bank-with-answers.md   # INPUT: Your question bank
│   ├── challenge-01-vA.md              # OUTPUT: Version A
│   ├── challenge-01-vB.md              # OUTPUT: Version B
│   ├── challenge-01-vC.md              # OUTPUT: Version C
│   ├── challenge-01-vD.md              # OUTPUT: Version D
│   └── exam-map.md                     # OUTPUT: Grading key
├── challenge_02/
│   ├── question-bank-with-answers.md
│   └── ...
```

---

## Step-by-Step Instructions

### 1. Prepare Challenge Directory

Create a new challenge directory:

```bash
mkdir -p challenges/challenge_02
```

### 2. Create Question Bank

Create `question-bank-with-answers.md` in the challenge directory following the format below.

**Required format:**

```markdown
# Challenge X Question Bank - N total

### 1.
Question text goes here?

- **A.** First choice
- **B.** **Correct answer (bold text indicates correctness)**
- **C.** Third choice
- **D.** Fourth choice

### 2.
Another question?

- **A.** Choice text
- **B.** **Correct answer**
- **C.** Choice text
- **D.** Choice text
```

**Format requirements:**
- Header: `### N.` where N is question number (1, 2, 3...)
- Choices: `- **A.** text` or `- **A** text` (period optional)
- Correct answer: Wrap text in bold `**like this**`
- Exactly **4 choices** per question (A, B, C, D)
- Exactly **1 correct answer** per question
- HTML comments are automatically stripped

### 3. Run the Script

From the repository root:

```bash
# Specific challenge
python3 challenges/shuffle_exam.py challenges/challenge_01/

# Or from challenges/ directory
cd challenges
python3 shuffle_exam.py challenge_01/
```

**The script will:**
1. Validate the question bank format
2. Parse all questions
3. Generate 4 exam versions
4. Create the exam map
5. Print a summary

### 4. Verify Output

Check that 5 files were created:

```bash
ls -lh challenges/challenge_01/*.md
```

Expected output:
```
challenge-01-vA.md
challenge-01-vB.md
challenge-01-vC.md
challenge-01-vD.md
exam-map.md
question-bank-with-answers.md
```

---

## Validation

The script automatically validates your question bank and will **abort** if it finds:

- ❌ Questions without exactly 4 choices
- ❌ Questions without exactly 1 correct answer marked
- ❌ Questions with multiple correct answers
- ❌ Empty question text
- ⚠️ Empty choice text (warning only)

**Example validation error:**

```
❌ VALIDATION ERRORS:
  - Q5: Expected 4 choices, found 3
  - Q12: Multiple correct answers marked (2)

❌ Validation failed. Please fix errors before generating exam versions.
```

---

## Verification Checklist

After generation, verify:

**✅ File counts:**
```bash
# Count generated files
ls challenges/challenge_01/challenge-01-v*.md | wc -l
# Should output: 4
```

**✅ Question counts (all versions should match):**
```bash
for v in A B C D; do
  count=$(grep -c "^### [0-9]" challenges/challenge_01/challenge-01-v$v.md)
  echo "Version $v: $count questions"
done
```

**✅ Correct answer counts (should equal question count):**
```bash
for v in A B C D; do
  count=$(grep -c "^\- \*\*[A-D]\.\*\* \*\*" challenges/challenge_01/challenge-01-v$v.md)
  echo "Version $v: $count correct answers marked"
done
```

**✅ Spot-check answer shuffling:**

Pick a question and verify the same correct answer text appears with different letters across versions:

```bash
# Show Question 1 from Version A
sed -n '3,9p' challenges/challenge_01/challenge-01-vA.md

# Find where that question appears in Version B using exam-map.md
grep "Version B:" challenges/challenge_01/exam-map.md | head -1
```

**✅ Verify reproducibility:**

Run the script twice and compare outputs:

```bash
# First run
python3 challenges/shuffle_exam.py challenges/challenge_01/

# Second run (should produce identical files)
python3 challenges/shuffle_exam.py challenges/challenge_01/

# Check with git
git diff challenges/challenge_01/
# Should show no differences in generated files
```

---

## Understanding the Output

### Version A - Instructor Reference

- **Question order:** Original (matches your input file)
- **Answer order:** Original
- **Use case:** Instructor reference, creating rubrics

### Versions B, C, D - Student Exams

- **Question order:** Randomly shuffled (different for each version)
- **Answer order:** Randomly shuffled (different for each version)
- **Random seeds:** B=1, C=2, D=3 (reproducible)
- **Use case:** Distribute to students to prevent copying

### exam-map.md - TA Grading Guide

**Section 1: Quick Answer Keys**

Tables for rapid lookup while grading:

```markdown
## Version B Answer Key

| Q# | Correct Answer | Source Question | Question Preview |
|----|----------------|-----------------|------------------|
| 1  | **A**          | A-Q7           | Two patients... |
| 2  | **B**          | A-Q20          | In the chimp... |
```

**Section 2: Cross-Reference**

Shows where each Version A question appears in other versions:

```markdown
### Version A - Question 1
**Correct Answer: C**

- Version B: Question 12 (Correct: A)
- Version C: Question 5 (Correct: B)
- Version D: Question 3 (Correct: C)
```

**Useful for:**
- Finding questions across versions
- Verifying consistent grading
- Debugging discrepancies

---

## Reproducibility Details

### Random Seeds

The script uses **fixed random seeds** for deterministic output:

- **Version A:** No shuffling (original order)
- **Version B:** Seed = 1
- **Version C:** Seed = 2
- **Version D:** Seed = 3

**Why this matters:**
- Running the script multiple times produces **identical files**
- You can regenerate exams if files are lost
- Git diffs show actual content changes, not random reordering

### Changing Seeds

If you need different shuffles, edit `shuffle_exam.py`:

```python
# Around line 334-356
random.seed(1)  # Change to random.seed(100)
version_b_qs = shuffle_and_write_version(...)

random.seed(2)  # Change to random.seed(200)
version_c_qs = shuffle_and_write_version(...)

random.seed(3)  # Change to random.seed(300)
version_d_qs = shuffle_and_write_version(...)
```

Or use dynamic seeds:
```python
import time
random.seed(int(time.time()))  # Different every run
```

---

## Troubleshooting

### Script fails with "Directory not found"

```
❌ Error: Directory not found: challenges/challenge_XX
```

**Solution:** Create the directory first:
```bash
mkdir -p challenges/challenge_XX
```

### Script fails with "Input file not found"

```
❌ Error: Input file not found: challenges/challenge_XX/question-bank-with-answers.md
Expected file: question-bank-with-answers.md
```

**Solution:** Ensure your input file is named exactly `question-bank-with-answers.md` and placed in the challenge directory.

### Validation errors

```
❌ VALIDATION ERRORS:
  - Q5: Expected 4 choices, found 3
```

**Common causes:**
1. **Missing choice:** Add the missing choice
2. **Formatting error:** Check for exact format `- **A.** text`
3. **Extra newlines:** Remove blank lines between choices
4. **Wrong letter:** Ensure choices are A, B, C, D only

**Solution:** Open `question-bank-with-answers.md` and fix the indicated question.

### Wrong question count

```bash
grep -c "^### [0-9]" challenge-01-vA.md
# Expected: 26, Got: 24
```

**Solution:** Check for:
- Questions with formatting errors (skipped by validator)
- Missing `### N.` headers
- Extra whitespace in headers

### Answers not shuffling

**Verify shuffling worked:**

```bash
# Get Version A, Question 1
sed -n '3,9p' challenges/challenge_01/challenge-01-vA.md

# Get Version B, same question (check exam-map.md for location)
# Compare - correct answer text should be same, but different letter
```

**If not shuffling:** Check that you're using the updated `shuffle_exam.py` script.

---

## Advanced Usage

### Multiple Challenges

Generate exams for multiple challenges in sequence:

```bash
for i in 01 02 03; do
  python3 challenges/shuffle_exam.py challenges/challenge_$i/
done
```

### Custom Challenge Naming

The script extracts challenge numbers from directory names:

- `challenge_01/` → "Challenge 01"
- `challenge-02/` → "Challenge 02"
- `CHALLENGE_03/` → "Challenge 03"

### Integration with Git

**Recommended workflow:**

1. Create `question-bank-with-answers.md`
2. Run generation script
3. Review generated versions
4. Commit everything:

```bash
git add challenges/challenge_01/
git commit -m "Add Challenge 01 exam versions"
```

**Files to track:**
- ✅ `question-bank-with-answers.md` (source of truth)
- ✅ `challenge-01-vA.md` through `vD.md` (for distribution)
- ✅ `exam-map.md` (for grading)

---

## Quick Reference

### Generate exams
```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/
```

### Verify question counts
```bash
for v in A B C D; do
  echo -n "Version $v: "
  grep -c "^### [0-9]" challenges/challenge_01/challenge-01-v$v.md
done
```

### Verify correct answer counts
```bash
for v in A B C D; do
  echo -n "Version $v: "
  grep -c "^\- \*\*[A-D]\.\*\* \*\*" challenges/challenge_01/challenge-01-v$v.md
done
```

### Test reproducibility
```bash
# Generate twice, check for differences
python3 challenges/shuffle_exam.py challenges/challenge_01/
git diff challenges/challenge_01/
# Should show no changes
```

---

## Summary

**To generate exam versions:**

1. Create `challenges/challenge_XX/question-bank-with-answers.md`
2. Run `python3 challenges/shuffle_exam.py challenges/challenge_XX/`
3. Verify 5 files created (4 versions + exam-map.md)
4. Check question counts match
5. Distribute versions to students
6. Use `exam-map.md` for grading

**Key features:**
- ✅ Automatic validation
- ✅ Reproducible output (fixed seeds)
- ✅ Works with any number of questions
- ✅ Handles both `**A.**` and `**A**` formats
- ✅ Clear error messages
- ✅ Cross-reference for TAs
