# Exam Generation Recipe

This document provides step-by-step instructions for generating classroom-ready exam versions from a question bank.

---

## Overview

The exam generation system creates **two types of files** for each of 4 exam versions:

**Student Versions** (classroom-ready):
- Clean formatting with no answer markers
- Custom header with exam date
- Instructions block for students
- Bonus question appended (if provided)

**Answer Key Versions** (for grading):
- Bold answer markers (**correct answer**)
- Original header format
- NO bonus question

**Outputs per challenge:**
- 4 student versions: `challenge-XX-vA.md` through `vD.md`
- 4 answer keys: `challenge-XX-vA-with-key.md` through `vD-with-key.md`
- 1 grading reference: `exam-map.md`

**Total: 9 files**

**Reproducibility:** Uses fixed random seeds (0, 1, 2, 3) to ensure identical output on repeated runs.

---

## Directory Structure

```
challenges/
├── shuffle_exam.py               # The generation script
├── EXAM_RECIPE.md               # This file
│
├── challenge_01/
│   ├── question-bank-with-answers.md     # INPUT: Your question bank
│   ├── bonus-question.md                 # INPUT: Bonus question (optional)
│   │
│   ├── challenge-01-vA.md                # OUTPUT: Student version A
│   ├── challenge-01-vB.md                # OUTPUT: Student version B
│   ├── challenge-01-vC.md                # OUTPUT: Student version C
│   ├── challenge-01-vD.md                # OUTPUT: Student version D
│   │
│   ├── challenge-01-vA-with-key.md       # OUTPUT: Answer key A
│   ├── challenge-01-vB-with-key.md       # OUTPUT: Answer key B
│   ├── challenge-01-vC-with-key.md       # OUTPUT: Answer key C
│   ├── challenge-01-vD-with-key.md       # OUTPUT: Answer key D
│   │
│   └── exam-map.md                       # OUTPUT: Grading reference
│
├── challenge_02/
│   ├── question-bank-with-answers.md
│   ├── bonus-question.md
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

Create `question-bank-with-answers.md` in the challenge directory.

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

### 3. Create Bonus Question (Optional)

Create `bonus-question.md` in the challenge directory.

**Format:**

```markdown
### Bonus
Did you use the course provided NotebookLM (AI assistance)?

- **A** I didn't use it at all
- **B** I tried it once or twice
- **C** I used it to help prepare
- **D** I used it consistently
```

**Notes:**
- Same format as regular questions (4 choices A-D)
- No correct answer marking needed (free points)
- Period after letter is optional
- Automatically appended to student versions only

### 4. Run the Script

**Basic usage** (will prompt for exam date):

```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/
```

**With exam date specified:**

```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-18-25"
```

**With custom point values:**

```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/ \
  --exam-date "Fri Oct-18-25" \
  --question-points 3 \
  --bonus-points 5
```

**Command-line options:**
- `--exam-date`: Date in format "Day Mon-DD-YY" (e.g., "Fri Oct-18-25")
- `--question-points`: Points per question (default: 2)
- `--bonus-points`: Points for bonus question (default: 2)

**The script will:**
1. Validate the question bank format
2. Parse all questions
3. Generate 4 versions with marked answers
4. Create answer key copies (`-with-key.md`)
5. Transform to student versions (clean, with header/instructions/bonus)
6. Create exam map
7. Print detailed summary

### 5. Verify Output

Check that 9 files were created:

```bash
ls -lh challenges/challenge_01/challenge-01-v*.md challenges/challenge_01/exam-map.md
```

Expected output:
```
challenge-01-vA.md              (student version)
challenge-01-vA-with-key.md     (answer key)
challenge-01-vB.md              (student version)
challenge-01-vB-with-key.md     (answer key)
challenge-01-vC.md              (student version)
challenge-01-vC-with-key.md     (answer key)
challenge-01-vD.md              (student version)
challenge-01-vD-with-key.md     (answer key)
exam-map.md                     (grading reference)
```

---

## Validation

The script automatically validates your question bank and will **abort** if it finds:

- ❌ Questions without exactly 4 choices
- ❌ Questions without exactly 1 correct answer marked
- ❌ Questions with multiple correct answers
- ❌ Empty question text
- ⚠️  Empty choice text (warning only)

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

### ✅ File Counts

```bash
# Count all version files (should be 8: 4 student + 4 keys)
ls challenges/challenge_01/challenge-01-v*.md | wc -l
# Should output: 8
```

### ✅ Question Counts (all versions should match)

```bash
for v in A B C D; do
  echo -n "Version $v: "
  grep -c "^### [0-9]" challenges/challenge_01/challenge-01-v$v.md
done
```

### ✅ Student Versions Have NO Bold Answers

```bash
# Should return nothing (empty)
grep "^\- \*\*[A-D]\.\*\* \*\*" challenges/challenge_01/challenge-01-vA.md
```

### ✅ Answer Keys HAVE Bold Answers

```bash
# Should return count equal to question count
grep -c "^\- \*\*[A-D]\.\*\* \*\*" challenges/challenge_01/challenge-01-vA-with-key.md
```

### ✅ Student Versions Have New Header

```bash
head -1 challenges/challenge_01/challenge-01-vA.md
# Should output: # Challenge 01 - Fri Oct-18-25
```

### ✅ Bonus Question in Student Versions

```bash
grep "Bonus Question" challenges/challenge_01/challenge-01-vA.md
# Should find it
```

### ✅ NO Bonus in Answer Keys

```bash
grep "Bonus Question" challenges/challenge_01/challenge-01-vA-with-key.md
# Should output: nothing (empty)
```

### ✅ Spot-Check Answer Shuffling

```bash
# Show student version Q1 (no bold answers)
sed -n '10,17p' challenges/challenge_01/challenge-01-vA.md

# Show answer key Q1 (with bold answer)
sed -n '3,10p' challenges/challenge_01/challenge-01-vA-with-key.md

# Verify same question but one has bold answer, one doesn't
```

### ✅ Verify Reproducibility

```bash
# Run twice with same date
python3 challenges/shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-18-25"
python3 challenges/shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-18-25"

# Check with git (should show no changes)
git diff challenges/challenge_01/challenge-01-v*.md
```

---

## Understanding the Output

### Student Versions (`challenge-XX-vY.md`)

**Purpose:** Print and distribute to students in classroom

**Header:**
```markdown
# Challenge 01 - Fri Oct-18-25

**Instructions:**

You will have the full lecture time to answer all 26 multiple choice questions. Each question is worth 2 points. Think carefully about what each question asks and what each answer claims - we're not trying to trick you! Good luck!

---
```

**Questions:** Clean format with NO bold answer markers
```markdown
### 1.
What is Theory of Mind?

- **A.** First choice
- **B.** Second choice
- **C.** Third choice
- **D.** Fourth choice
```

**Bonus:** Appended at end (if `bonus-question.md` exists)
```markdown
### Bonus Question

**No right answer - Free 2 points!**

Did you use NotebookLM?

- **A.** I didn't use it at all
- **B.** I tried it once or twice
- **C.** I used it to help prepare
- **D.** I used it consistently
```

**Use cases:**
- Print for in-class exams
- Upload to Canvas for online exams
- Distribute via email

### Answer Key Versions (`challenge-XX-vY-with-key.md`)

**Purpose:** For instructor and TAs to grade exams

**Header:**
```markdown
# Challenge 01 Question Bank Version A - 26 total
```

**Questions:** With bold answer markers
```markdown
### 1.
What is Theory of Mind?

- **A.** First choice
- **B.** **Correct answer (bold indicates this is right)**
- **C.** Third choice
- **D.** Fourth choice
```

**NO Bonus Question** (bonus doesn't need grading - free points)

**Use cases:**
- Quick reference while grading
- Creating rubrics
- Reviewing student performance

### Exam Map (`exam-map.md`)

**Purpose:** Cross-reference for TAs grading multiple versions

**Section 1: Quick Answer Keys**

Tables for rapid lookup:

```markdown
## Version A Answer Key

| Q# | Correct Answer | Source Question | Question Preview |
|----|----------------|-----------------|------------------|
| 1  | **C**          | A-Q1           | What is Theory... |
| 2  | **B**          | A-Q2           | Which statement... |
```

**Section 2: Cross-Reference**

Shows where each Version A question appears in other versions:

```markdown
### Version A - Question 1
**Correct Answer: C**

- Version B: Question 14 (Correct: C)
- Version C: Question 5 (Correct: C)
- Version D: Question 17 (Correct: A)
```

**Use cases:**
- Verify consistent grading across versions
- Find questions across versions
- Debug grading discrepancies

---

## Version Differences

|                    | Version A    | Versions B, C, D |
|--------------------|--------------|------------------|
| Question order     | Original     | Shuffled         |
| Answer order       | Original     | Shuffled         |
| Random seed        | 0 (no shuffle) | 1, 2, 3        |
| Use case           | Reference    | Student distribution |

All versions have:
- Same questions (just reordered)
- Same correct answers (just different A/B/C/D positions)
- Student version + Answer key version
- Bonus question (student versions only)

---

## Reproducibility Details

### Fixed Random Seeds

The script uses **fixed random seeds** for deterministic output:

- **Version A:** Seed = 0 (questions not shuffled, answers not shuffled)
- **Version B:** Seed = 1
- **Version C:** Seed = 2
- **Version D:** Seed = 3

**Why this matters:**
- Running script multiple times produces **identical files**
- You can regenerate exams if files are lost
- Git diffs show actual content changes, not random reordering
- TAs can verify exam integrity

### Changing Seeds

If you need different shuffles, edit `shuffle_exam.py` lines 532-562:

```python
random.seed(1)  # Change to random.seed(100)
version_b_qs = shuffle_and_write_version(...)

random.seed(2)  # Change to random.seed(200)
version_c_qs = shuffle_and_write_version(...)

random.seed(3)  # Change to random.seed(300)
version_d_qs = shuffle_and_write_version(...)
```

Or use dynamic seeds for truly random shuffles:
```python
import time
random.seed(int(time.time()))
```

---

## Troubleshooting

### Script fails with "Directory not found"

```
❌ Error: Directory not found: challenges/challenge_XX
```

**Solution:**
```bash
mkdir -p challenges/challenge_XX
```

### Script fails with "Input file not found"

```
❌ Error: Input file not found: challenges/challenge_XX/question-bank-with-answers.md
Expected file: question-bank-with-answers.md
```

**Solution:** Ensure your input file is named exactly `question-bank-with-answers.md`

### Script prompts for exam date

```
📅 Exam date required for student versions.
Format: Day Mon-DD-YY (e.g., 'Fri Oct-17-25')
Enter exam date:
```

**Solution:** Either enter the date interactively, or use `--exam-date` flag:
```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-18-25"
```

### Invalid date format error

```
❌ Invalid date format: Friday October 18 2025
Expected format: 'Fri Oct-17-25' (Day Mon-DD-YY)
```

**Solution:** Use exact format: `"Fri Oct-18-25"`
- Day: 3 letters (Mon, Tue, Wed, Thu, Fri, Sat, Sun)
- Month: 3 letters (Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec)
- Day number: 2 digits (01-31)
- Year: 2 digits (25 for 2025)

### Validation errors

```
❌ VALIDATION ERRORS:
  - Q5: Expected 4 choices, found 3
  - Q12: Multiple correct answers marked (2)
```

**Common causes:**
1. **Missing choice:** Add the missing A/B/C/D choice
2. **Multiple bold answers:** Only ONE answer should have `**text**`
3. **Formatting error:** Check exact format `- **A.** **text**` for correct
4. **Extra newlines:** Remove blank lines between choices

**Solution:** Open `question-bank-with-answers.md` and fix the indicated question

### Wrong question count

```bash
grep -c "^### [0-9]" challenge-01-vA.md
# Expected: 26, Got: 24
```

**Solution:** Check for:
- Questions with formatting errors (skipped by validator)
- Missing `### N.` headers
- Extra whitespace in headers: `###1.` vs `### 1.`

### Student versions still have bold answers

```bash
grep "^\- \*\*[A-D]\.\*\* \*\*" challenges/challenge_01/challenge-01-vA.md
# Should be empty, but shows matches
```

**Solution:**
1. Check you're looking at the right file (not `*-with-key.md`)
2. Re-run the script
3. Verify script version is up to date

### Bonus question not appearing

```bash
grep "Bonus Question" challenges/challenge_01/challenge-01-vA.md
# Returns nothing
```

**Solution:**
1. Check `bonus-question.md` exists in challenge directory
2. Verify bonus file has correct format (4 choices A-D)
3. Re-run the script

---

## Advanced Usage

### Multiple Challenges

Generate exams for multiple challenges:

```bash
for i in 01 02 03; do
  python3 challenges/shuffle_exam.py challenges/challenge_$i/ \
    --exam-date "Fri Oct-18-25"
done
```

### Custom Point Values

Different point allocations:

```bash
# 3 points per question, 5 point bonus
python3 challenges/shuffle_exam.py challenges/challenge_01/ \
  --exam-date "Mon Oct-21-25" \
  --question-points 3 \
  --bonus-points 5
```

### View Help

```bash
python3 challenges/shuffle_exam.py --help
```

### Custom Challenge Naming

The script extracts challenge numbers from directory names:

- `challenge_01/` → "Challenge 01"
- `challenge-02/` → "Challenge 02"
- `CHALLENGE_03/` → "Challenge 03"

### Integration with Git

**Recommended workflow:**

1. Create `question-bank-with-answers.md` and `bonus-question.md`
2. Run generation script
3. Review generated versions (spot-check answers)
4. Commit everything:

```bash
git add challenges/challenge_01/
git commit -m "Add Challenge 01 exam versions for Oct-18-25"
```

**Files to track:**
- ✅ `question-bank-with-answers.md` (source of truth)
- ✅ `bonus-question.md` (bonus question)
- ✅ `challenge-01-vA.md` through `vD.md` (student versions)
- ✅ `challenge-01-vA-with-key.md` through `vD-with-key.md` (answer keys)
- ✅ `exam-map.md` (grading reference)
- ❌ Don't commit: old `question-bank-version-*.md` files (deprecated format)

---

## Quick Reference

### Generate exams with date

```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-18-25"
```

### Verify all file types created

```bash
# Should be 8 version files + 1 exam map = 9 files
ls challenges/challenge_01/challenge-01-v*.md challenges/challenge_01/exam-map.md | wc -l
```

### Check student version has NO bold answers

```bash
grep "^\- \*\*[A-D]\.\*\* \*\*" challenges/challenge_01/challenge-01-vA.md
# Should return: nothing (empty)
```

### Check answer key HAS bold answers

```bash
grep -c "^\- \*\*[A-D]\.\*\* \*\*" challenges/challenge_01/challenge-01-vA-with-key.md
# Should return: 26 (or your question count)
```

### Verify bonus question

```bash
# Student version - should have bonus
tail -10 challenges/challenge_01/challenge-01-vA.md

# Answer key - should NOT have bonus
tail -10 challenges/challenge_01/challenge-01-vA-with-key.md
```

### Test reproducibility

```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-18-25"
git diff challenges/challenge_01/
# Should show: no changes
```

---

## Summary

**To generate exam versions:**

1. Create `challenges/challenge_XX/question-bank-with-answers.md`
2. Create `challenges/challenge_XX/bonus-question.md` (optional)
3. Run: `python3 challenges/shuffle_exam.py challenges/challenge_XX/ --exam-date "Fri Oct-18-25"`
4. Verify 9 files created (4 student + 4 keys + 1 map)
5. Print student versions for classroom
6. Use answer keys and exam-map.md for grading

**Key features:**
- ✅ Automatic validation (4 choices, 1 correct answer)
- ✅ Reproducible output (fixed seeds)
- ✅ Works with any number of questions
- ✅ Student-ready format (clean, with instructions)
- ✅ Answer keys for grading
- ✅ Bonus question support
- ✅ Configurable point values
- ✅ Cross-reference for TAs
- ✅ Clear error messages

**Remember:** Student versions are clean and classroom-ready. Answer key versions have bold markers for grading.
