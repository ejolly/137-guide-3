# Exam Generation Recipe

This document provides step-by-step instructions for generating classroom-ready exam versions from a question bank.

**Working Directory:** All commands in this document assume you're running from the repository root. If you're in the `challenges/` directory, adjust paths accordingly (e.g., `python3 shuffle_exam.py challenge_01/` instead of `python3 challenges/shuffle_exam.py challenges/challenge_01/`).

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
- 18 rendered artifacts: 9 PDFs + 9 DOCX files in `output/` subdirectory

**Total: 27 files** (9 markdown + 18 rendered artifacts)

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
│   ├── exam-map.md                       # OUTPUT: Grading reference
│   │
│   └── output/                           # OUTPUT: Rendered artifacts
│       ├── challenge-01-vA.pdf
│       ├── challenge-01-vA.docx
│       ├── challenge-01-vB.pdf
│       ├── challenge-01-vB.docx
│       ├── challenge-01-vC.pdf
│       ├── challenge-01-vC.docx
│       ├── challenge-01-vD.pdf
│       ├── challenge-01-vD.docx
│       ├── challenge-01-vA-with-key.pdf
│       ├── challenge-01-vA-with-key.docx
│       ├── challenge-01-vB-with-key.pdf
│       ├── challenge-01-vB-with-key.docx
│       ├── challenge-01-vC-with-key.pdf
│       ├── challenge-01-vC-with-key.docx
│       ├── challenge-01-vD-with-key.pdf
│       ├── challenge-01-vD-with-key.docx
│       ├── exam-map.pdf
│       └── exam-map.docx
│
├── challenge_02/
│   ├── question-bank-with-answers.md
│   ├── bonus-question.md
│   ├── output/
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
- Choices: `- **A.** text` or `- **A** text` (period optional in input)
  - **Note:** The pipeline automatically normalizes all choices to `**(A)** text  ` format (no bullets, parentheses around letter, 2 trailing spaces)
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

**Basic usage** (will prompt for exam date, with rendering):

```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/
```

**With exam date specified:**

```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-18-25"
```

**Skip rendering** (faster for iterating on content):

```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-18-25" --skip-render
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
- `--skip-render`: Skip PDF and DOCX rendering (useful for fast iteration)

**The script will:**
1. Validate the question bank format
2. Parse all questions and normalize answer format to `**(A)** text  `
3. Generate 4 versions with marked answers
4. Create answer key copies (`-with-key.md`)
5. Transform to student versions (clean, with header/instructions/bonus)
6. Create exam map
7. Render all 9 markdown files to PDF and DOCX (unless `--skip-render`)
8. Print detailed summary

### 5. Verify Output

**Check markdown files (9 files):**

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

**Check rendered artifacts (18 files in output/):**

```bash
ls -lh challenges/challenge_01/output/
```

Expected output:
```
challenge-01-vA.pdf
challenge-01-vA.docx
challenge-01-vA-with-key.pdf
challenge-01-vA-with-key.docx
challenge-01-vB.pdf
challenge-01-vB.docx
challenge-01-vB-with-key.pdf
challenge-01-vB-with-key.docx
challenge-01-vC.pdf
challenge-01-vC.docx
challenge-01-vC-with-key.pdf
challenge-01-vC-with-key.docx
challenge-01-vD.pdf
challenge-01-vD.docx
challenge-01-vD-with-key.pdf
challenge-01-vD-with-key.docx
exam-map.pdf
exam-map.docx
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
# Count markdown version files (should be 8: 4 student + 4 keys)
ls challenges/challenge_01/challenge-01-v*.md | wc -l
# Should output: 8

# Count PDF files (should be 9)
ls challenges/challenge_01/output/*.pdf | wc -l
# Should output: 9

# Count DOCX files (should be 9)
ls challenges/challenge_01/output/*.docx | wc -l
# Should output: 9
```

### ✅ Question Counts (all versions should match)

```bash
for v in A B C D; do
  echo -n "Version $v: "
  grep -c "^### [0-9]" challenges/challenge_01/challenge-01-v$v.md
done
```

### ✅ Answer Format Normalized

```bash
# Check that choices use new format: **(A)** text (not bullets)
grep "^\*\*([A-D])\*\*" challenges/challenge_01/challenge-01-vA.md | head -3
# Should show format like: **(A)** First choice
```

### ✅ Student Versions Have NO Bold Answers

```bash
# Should return nothing (empty)
grep "^\*\*([A-D])\*\* \*\*" challenges/challenge_01/challenge-01-vA.md
```

### ✅ Answer Keys HAVE Bold Answers

```bash
# Should return count equal to question count
grep -c "^\*\*([A-D])\*\* \*\*" challenges/challenge_01/challenge-01-vA-with-key.md
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

### ✅ Verify Exam-Map Alignment

**Critical:** Verify that the exam-map actually matches the generated exam files (catches data structure bugs):

```bash
# Check Version A, Question 1 - exam-map says correct answer is A
grep "| 1 |" challenges/challenge_01/exam-map.md | head -1
# Should show: | 1 | **A** | A-Q1 | ...

# Verify the actual answer key file has bold marker on A
sed -n '3,10p' challenges/challenge_01/challenge-01-vA-with-key.md
# Should show: **(A)** **The mind is a blank slate...** (bold on A)
```

**Check Version B alignment:**
```bash
# Check what exam-map says for Version B Question 1
sed -n '/^## Version B/,/^## Version C/p' challenges/challenge_01/exam-map.md | grep "| 1 |"
# Note which letter is marked as correct

# Verify in actual Version B answer key
sed -n '/^### 1\./,/^### 2\./p' challenges/challenge_01/challenge-01-vB-with-key.md
# Check that the same letter has the bold marker
```

**Why this matters:** This catches bugs where the exam-map reports incorrect answer keys due to data structure issues during shuffling.

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

**(A)** First choice
**(B)** Second choice
**(C)** Third choice
**(D)** Fourth choice
```

**Bonus:** Appended at end (if `bonus-question.md` exists)
```markdown
### Bonus Question

**No right answer - Free 2 points!**

Did you use NotebookLM?

**(A)** I didn't use it at all
**(B)** I tried it once or twice
**(C)** I used it to help prepare
**(D)** I used it consistently
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

**(A)** First choice
**(B)** **Correct answer (bold indicates this is right)**
**(C)** Third choice
**(D)** Fourth choice
```

**NO Bonus Question** (bonus doesn't need grading - free points)

**Use cases:**
- Quick reference while grading
- Creating rubrics
- Reviewing student performance

### Exam Map (`exam-map.md`)

**Purpose:** Cross-reference for TAs grading multiple versions

**Section 1: Quick Answer Keys**

Tables for rapid lookup (split into two tables for better PDF rendering):

```markdown
## Version A Answer Key

### Questions 1-13

| Q# | Correct Answer | Source Question | Question Preview |
|----|----------------|-----------------|------------------|
| 1  | **A**          | A-Q1           | What key idea... |
| 2  | **D**          | A-Q2           | Which statement... |
...
| 13 | **B**          | A-Q13          | The lecture proposes... |

### Questions 14-26

| Q# | Correct Answer | Source Question | Question Preview |
|----|----------------|-----------------|------------------|
| 14 | **D**          | A-Q14          | A robot makes... |
| 15 | **C**          | A-Q15          | The research by... |
...
| 26 | **D**          | A-Q26          | In iterative... |
```

**Section 2: Cross-Reference**

Shows where each Version A question appears in other versions (note how correct answer letters vary):

```markdown
### Version A - Question 1
**Correct Answer: A**

- Version B: Question 14 (Correct: C)
- Version C: Question 5 (Correct: C)
- Version D: Question 17 (Correct: A)

### Version A - Question 6
**Correct Answer: B**

- Version B: Question 7 (Correct: C)
- Version C: Question 22 (Correct: A)
- Version D: Question 6 (Correct: D)
```

The varying correct answers (A, B, C, D across versions) prevent answer-pattern cheating.

**Use cases:**
- Verify consistent grading across versions
- Find questions across versions
- Debug grading discrepancies

### Rendered Artifacts (`output/*.pdf` and `output/*.docx`)

**Purpose:** Distribution-ready formats for all markdown files

**Contents:**
- 9 PDF files (4 student + 4 keys + 1 map)
- 9 DOCX files (4 student + 4 keys + 1 map)

**Generated using:** Pandoc with typst backend for PDFs, standard backend for DOCX

**Format characteristics:**
- PDFs: Clean, professional formatting suitable for printing
- DOCX: Editable Word documents for last-minute changes

**Use cases:**
- **PDFs for students:** Print directly for in-class exams
- **PDFs for Canvas:** Upload as exam files (students can't edit)
- **DOCX for editing:** Make last-minute corrections or adjustments
- **DOCX for accessibility:** Convert to other formats if needed
- **Answer key PDFs:** Distribute to TAs for grading reference

**Notes:**
- Rendering requires pandoc to be installed
- Use `--skip-render` flag to skip this step during content iteration
- If rendering fails, markdown files are still usable
- PDFs use typst backend for better formatting (fallback to default if unavailable)
- **Exam-map tables are split at question 13** to prevent PDF rendering issues with long tables

---

## Version Differences

|                    | Version A        | Versions B, C, D |
|--------------------|------------------|------------------|
| Question order     | Original         | Shuffled         |
| Answer order       | **Shuffled**     | Shuffled         |
| Random seed        | 0                | 1, 2, 3          |
| Use case           | Reference        | Student distribution |

**Important:** All 4 versions now shuffle answer choices independently, meaning the correct answer for the same question will be different letters (A, B, C, or D) across versions. This prevents answer-pattern cheating.

All versions have:
- Same questions (just reordered in B, C, D)
- **Varied correct answer positions** (e.g., Q1 might be A in Version A, C in Version B, D in Version C)
- Student version + Answer key version
- Bonus question (student versions only)

---

## Reproducibility Details

### Fixed Random Seeds

The script uses **fixed random seeds** for deterministic output:

- **Version A:** Seed = 0 (questions in **original order**, answer choices **shuffled**)
- **Version B:** Seed = 1 (questions **shuffled**, answer choices **shuffled**)
- **Version C:** Seed = 2 (questions **shuffled**, answer choices **shuffled**)
- **Version D:** Seed = 3 (questions **shuffled**, answer choices **shuffled**)

**Why this matters:**
- Running script multiple times produces **identical files**
- You can regenerate exams if files are lost
- Git diffs show actual content changes, not random reordering
- TAs can verify exam integrity
- **Answer positions vary across all versions** - prevents students from memorizing answer patterns

### Changing Seeds

If you need different shuffles, edit `shuffle_exam.py` around lines 473-500 (search for `random.seed`):

```python
random.seed(1)  # Change to random.seed(100) for different shuffling
version_b_qs = shuffle_and_write_version(...)

random.seed(2)  # Change to random.seed(200)
version_c_qs = shuffle_and_write_version(...)

random.seed(3)  # Change to random.seed(300)
version_d_qs = shuffle_and_write_version(...)
```

**Note:** Changing seeds will produce different shuffles, breaking reproducibility. Only change if you need completely new versions.

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
grep "^\*\*([A-D])\*\* \*\*" challenges/challenge_01/challenge-01-vA.md
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

### Rendering fails with pandoc errors

```
⚠️  Rendering failed: [Errno 2] No such file or directory: 'pandoc'
```

**Common causes and solutions:**

1. **Pandoc not installed:**
   ```bash
   # macOS
   brew install pandoc

   # Linux (Ubuntu/Debian)
   sudo apt-get install pandoc

   # Linux (Fedora)
   sudo dnf install pandoc
   ```

2. **Typst backend unavailable:**
   - Script will automatically fall back to default PDF rendering
   - For best results, ensure pandoc version >= 3.0

3. **Invalid markdown in generated files:**
   - Check markdown files manually
   - Look for malformed formatting
   - Re-run with `--skip-render` to isolate the issue

4. **Permission errors:**
   ```bash
   # Ensure output directory is writable
   chmod -R u+w challenges/challenge_01/output/
   ```

5. **Skip rendering temporarily:**
   ```bash
   # Use --skip-render to bypass rendering issues
   python3 challenges/shuffle_exam.py challenges/challenge_01/ \
     --exam-date "Fri Oct-18-25" --skip-render
   ```

**Note:** Markdown files are always generated first, so rendering failures won't prevent you from having usable exam files.

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
- ❌ Don't commit: Rendered artifacts (`*.pdf`, `*.docx`) - automatically gitignored and regenerated from markdown

---

## Quick Reference

### Generate exams with date (with rendering)

```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-18-25"
```

### Generate exams without rendering (faster iteration)

```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-18-25" --skip-render
```

### Verify all file types created

```bash
# Markdown files: Should be 8 version files + 1 exam map = 9 files
ls challenges/challenge_01/challenge-01-v*.md challenges/challenge_01/exam-map.md | wc -l

# PDF files: Should be 9
ls challenges/challenge_01/output/*.pdf | wc -l

# DOCX files: Should be 9
ls challenges/challenge_01/output/*.docx | wc -l
```

### Check answer format is normalized

```bash
grep "^\*\*([A-D])\*\*" challenges/challenge_01/challenge-01-vA.md | head -3
# Should show: **(A)** text format (not bullets)
```

### Check student version has NO bold answers

```bash
grep "^\*\*([A-D])\*\* \*\*" challenges/challenge_01/challenge-01-vA.md
# Should return: nothing (empty)
```

### Check answer key HAS bold answers

```bash
grep -c "^\*\*([A-D])\*\* \*\*" challenges/challenge_01/challenge-01-vA-with-key.md
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
4. Verify 27 files created:
   - 9 markdown files (4 student + 4 keys + 1 map)
   - 18 rendered artifacts (9 PDFs + 9 DOCX in `output/`)
5. Print or upload student version PDFs for classroom
6. Use answer key PDFs and exam-map.pdf for grading

**Key features:**
- ✅ Automatic validation (4 choices, 1 correct answer)
- ✅ Answer format normalization (`**(A)** text  ` with 2 trailing spaces)
- ✅ **Answer shuffling across all versions** - prevents answer-pattern cheating
- ✅ Reproducible output (fixed seeds 0, 1, 2, 3)
- ✅ Works with any number of questions
- ✅ Student-ready format (clean, with instructions)
- ✅ Answer keys for grading (with bold markers)
- ✅ Bonus question support (appended to student versions only)
- ✅ Configurable point values
- ✅ Cross-reference exam-map for TAs (split tables for better PDF rendering)
- ✅ PDF rendering for distribution (via pandoc + typst)
- ✅ DOCX rendering for editing (via pandoc)
- ✅ Graceful failure handling (markdown always generated)
- ✅ Clear error messages

**Remember:** Student versions are clean and classroom-ready. Answer key versions have bold markers for grading. PDFs are ready for printing or Canvas upload.
