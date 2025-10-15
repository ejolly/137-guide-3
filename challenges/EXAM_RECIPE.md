# Exam Generation Recipe - Agent Execution Specification

**Purpose:** This document provides deterministic instructions for Claude Code agents to generate classroom-ready exam versions from a question bank with zero variance and comprehensive verification.

**User Command:** "Generate exams for challenge XX"

---

## 🎯 AGENT INTERFACE

### User Command Patterns

The user will say one of:
- "generate exams for challenge 01"
- "create exam versions for challenge_02"
- "run exam generation for challenge 03"
- `/generate-exam` (slash command - prompts for challenge number)

### Required Information Collection

Follow this sequence to collect required inputs:

#### 1. Challenge Number
- **IF** not specified in user command: **PROMPT** "Which challenge number? (e.g., 01, 02, 03)"
- **EXTRACT** number from user response
- **CONSTRUCT** path: `challenges/challenge_{XX}/` where `{XX}` is zero-padded (01, 02, etc.)
- **STORE** as `challenge_num` and `challenge_dir`

#### 2. Exam Date
- **PROMPT** "Enter exam date in format 'Day Mon-DD-YY' (e.g., 'Fri Oct-18-25'):"
- **VALIDATE** format matches regex: `^(Mon|Tue|Wed|Thu|Fri|Sat|Sun) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)-\d{2}-\d{2}$`
- **IF** invalid: **RE-PROMPT** with message: "Invalid format. Use 'Day Mon-DD-YY' like 'Fri Oct-18-25'"
- **STORE** as `exam_date`

#### 3. Point Values (Optional)
- **PROMPT** "Use default point values? (2 points per question, 2 for bonus) [Y/n]:"
- **IF** user responds 'n' or 'N':
  - **PROMPT** "Points per question:"
  - **STORE** as `question_points`
  - **PROMPT** "Points for bonus question:"
  - **STORE** as `bonus_points`
- **OTHERWISE**: **SET** `question_points = 2` and `bonus_points = 2`

#### 4. Rendering Option
- **PROMPT** "Render PDF and DOCX files? (Requires pandoc) [Y/n]:"
- **IF** user responds 'n' or 'N':
  - **SET** `skip_render = true`
  - **NOTE** to user: "Will skip rendering - only markdown files will be verified"
- **OTHERWISE**: **SET** `skip_render = false`

### Execution Announcement

Once all inputs collected, **ANNOUNCE** to user:

```
Starting exam generation for challenge {XX}
- Date: {exam_date}
- Points: {question_points} per question, {bonus_points} for bonus
- Rendering: {enabled/disabled}

Proceeding with execution...
```

**THEN** proceed to **EXECUTION PROTOCOL**

---

## 📋 EXECUTION PROTOCOL

Execute these steps **sequentially**. **DO NOT** stop between steps unless **ERROR PROTOCOL** is triggered.

### STEP 1: Pre-Flight Validation

**Purpose:** Verify required files exist before generation

#### Check 1.1: Challenge Directory Exists

**COMMAND:**
```bash
test -d {challenge_dir} && echo "PASS" || echo "FAIL"
```

**EXPECTED OUTPUT:** `PASS`

**IF** output is `FAIL`: **TRIGGER ERROR PROTOCOL** with:
- **Error:** "Challenge directory does not exist"
- **Path:** `{challenge_dir}`
- **Diagnosis:** "Directory has not been created"
- **Fix:** `mkdir -p {challenge_dir}`

#### Check 1.2: Question Bank Exists

**COMMAND:**
```bash
test -f {challenge_dir}/question-bank-with-answers.md && echo "PASS" || echo "FAIL"
```

**EXPECTED OUTPUT:** `PASS`

**IF** output is `FAIL`: **TRIGGER ERROR PROTOCOL** with:
- **Error:** "question-bank-with-answers.md not found"
- **Path:** `{challenge_dir}/question-bank-with-answers.md`
- **Diagnosis:** "Input file missing"
- **Fix:** "Create the question bank file following the format in REFERENCE DOCUMENTATION section"

#### Check 1.3: Bonus Question Exists (Optional)

**COMMAND:**
```bash
test -f {challenge_dir}/bonus-question.md && echo "PRESENT" || echo "ABSENT"
```

**STORE** result as `bonus_exists` (true if PRESENT, false if ABSENT)

**NOTE** to user: "Bonus question: {PRESENT/ABSENT}"

### STEP 2: Execute Generation Script

**Purpose:** Generate all exam versions, answer keys, and exam map

#### Command 2.1: Run Generation Script

**CONSTRUCT** command:
```bash
python3 challenges/shuffle_exam.py {challenge_dir} \
  --exam-date "{exam_date}" \
  --question-points {question_points} \
  --bonus-points {bonus_points}
```

**IF** `skip_render` is true, **APPEND**: `--skip-render`

**EXECUTE** the constructed command

**CAPTURE:**
- All stdout → store as `generation_output`
- All stderr → store as `generation_errors`
- Exit code → store as `generation_exit_code`

**IF** `generation_exit_code` ≠ 0: **TRIGGER ERROR PROTOCOL** with:
- **Error:** "Generation script failed"
- **Exit Code:** `{generation_exit_code}`
- **Output:** Full contents of `generation_output` and `generation_errors`
- **Diagnosis:** Parse error messages for validation errors, file errors, or pandoc errors
- **Fix:** Based on error type (see ERROR PROTOCOL section)

**OTHERWISE**: **ANNOUNCE** "Generation complete. Running verification checks..."

### STEP 3: Execute Automated Verification Suite

**Purpose:** Verify all outputs are correct and complete

**RUN** all checks defined in **AUTOMATED VERIFICATION SUITE** section

**COLLECT** results for each check in structured format:
- Check name
- Expected value
- Actual value
- Status (PASS/FAIL)

**COUNT** total PASS and FAIL results

**IF** any check status is FAIL: **TRIGGER ERROR PROTOCOL** with all failure details

**OTHERWISE**: **PROCEED** to STEP 4

### STEP 4: Generate Completion Report

**Purpose:** Present comprehensive results to user

**USE** the **REPORTING FORMAT** template to generate final report

**INCLUDE:**
- All generated file paths
- All verification results
- Sample questions for user review
- Next steps (git commit commands)

**PRESENT** report to user

**ANNOUNCE:** "Exam generation complete. All verification checks passed."

---

## ✅ AUTOMATED VERIFICATION SUITE

Execute **ALL** checks in this section. Record PASS/FAIL status for each.

**Variables used:**
- `{challenge_dir}` = full path to challenge directory
- `{challenge_num}` = zero-padded challenge number (e.g., "01")
- `{bonus_exists}` = true/false from STEP 1.3
- `{skip_render}` = true/false from input collection

### CHECK 1: File Count - Markdown Version Files

**COMMAND:**
```bash
ls {challenge_dir}/challenge-{challenge_num}-v*.md 2>/dev/null | wc -l
```

**EXPECTED OUTPUT:** `8`

**EXTRACT** actual count from output (trim whitespace)

**COMPARE:** actual MUST EQUAL 8

**STORE RESULT AS:** `md_version_file_count_check` (PASS/FAIL)

**IF FAIL:** Store details: "Expected 8 markdown version files, found {actual}"

### CHECK 2: File Count - Exam Map

**COMMAND:**
```bash
test -f {challenge_dir}/exam-map.md && echo "PASS" || echo "FAIL"
```

**EXPECTED OUTPUT:** `PASS`

**STORE RESULT AS:** `exam_map_exists_check` (PASS/FAIL)

**IF FAIL:** Store details: "exam-map.md not found"

### CHECK 3: File Count - PDFs (if rendering enabled)

**IF** `skip_render` is false:

**COMMAND:**
```bash
ls {challenge_dir}/output/*.pdf 2>/dev/null | wc -l
```

**EXPECTED OUTPUT:** `9`

**EXTRACT** actual count from output (trim whitespace)

**COMPARE:** actual MUST EQUAL 9

**STORE RESULT AS:** `pdf_file_count_check` (PASS/FAIL)

**IF FAIL:** Store details: "Expected 9 PDF files, found {actual}"

**OTHERWISE** (skip_render is true): **SKIP** this check, store as SKIPPED

### CHECK 4: File Count - DOCX (if rendering enabled)

**IF** `skip_render` is false:

**COMMAND:**
```bash
ls {challenge_dir}/output/*.docx 2>/dev/null | wc -l
```

**EXPECTED OUTPUT:** `9`

**EXTRACT** actual count from output (trim whitespace)

**COMPARE:** actual MUST EQUAL 9

**STORE RESULT AS:** `docx_file_count_check` (PASS/FAIL)

**IF FAIL:** Store details: "Expected 9 DOCX files, found {actual}"

**OTHERWISE** (skip_render is true): **SKIP** this check, store as SKIPPED

### CHECK 5: Answer Format Normalization

**PURPOSE:** Verify choices use format `**(A)** text  ` (not bullets)

**COMMAND:**
```bash
grep "^\*\*([A-D])\*\*" {challenge_dir}/challenge-{challenge_num}-vA.md | head -1
```

**EXPECTED:** Output matches regex `^\*\*\([A-D]\)\*\* .+`

**VERIFY:** Output is non-empty and matches pattern

**STORE RESULT AS:** `answer_format_check` (PASS/FAIL)

**IF FAIL:** Store details: "Answer format not normalized. Expected '**(A)** text' format"

### CHECK 6: Student Version - No Bold Answers

**PURPOSE:** Verify student versions have NO bold answer markers

**FOR EACH** version in [A, B, C, D]:

**COMMAND:**
```bash
grep -c "^\*\*([A-D])\*\* \*\*" {challenge_dir}/challenge-{challenge_num}-v{version}.md
```

**EXPECTED OUTPUT:** `0`

**EXTRACT** actual count from output

**COMPARE:** actual MUST EQUAL 0

**STORE RESULT AS:** `student_clean_v{version}_check` (PASS/FAIL)

**IF FAIL:** Store details: "Version {version} student file has {actual} bold answers (should be 0)"

### CHECK 7: Answer Key - Has Bold Answers

**PURPOSE:** Verify answer keys have bold markers on correct answers

**FOR EACH** version in [A, B, C, D]:

**COMMAND:**
```bash
grep -c "^\*\*([A-D])\*\* \*\*" {challenge_dir}/challenge-{challenge_num}-v{version}-with-key.md
```

**EXPECTED OUTPUT:** Greater than 0

**EXTRACT** actual count from output

**COMPARE:** actual MUST BE > 0

**STORE RESULT AS:** `answer_key_v{version}_check` (PASS/FAIL)

**STORE COUNT AS:** `answer_key_v{version}_count` (for reporting)

**IF FAIL:** Store details: "Version {version} answer key has 0 bold answers (should have at least 1)"

### CHECK 8: Student Version - Bonus Question Presence

**PURPOSE:** Verify bonus question in student versions (if bonus file exists)

**IF** `bonus_exists` is true:

**FOR EACH** version in [A, B, C, D]:

**COMMAND:**
```bash
grep -c "Bonus Question" {challenge_dir}/challenge-{challenge_num}-v{version}.md
```

**EXPECTED OUTPUT:** `1`

**EXTRACT** actual count from output

**COMPARE:** actual MUST EQUAL 1

**STORE RESULT AS:** `student_bonus_v{version}_check` (PASS/FAIL)

**IF FAIL:** Store details: "Version {version} missing bonus question"

**OTHERWISE** (bonus_exists is false): **SKIP** this check for all versions, store as SKIPPED

### CHECK 9: Answer Key - NO Bonus Question

**PURPOSE:** Verify answer keys do NOT have bonus question

**FOR EACH** version in [A, B, C, D]:

**COMMAND:**
```bash
grep -c "Bonus Question" {challenge_dir}/challenge-{challenge_num}-v{version}-with-key.md
```

**EXPECTED OUTPUT:** `0`

**EXTRACT** actual count from output

**COMPARE:** actual MUST EQUAL 0

**STORE RESULT AS:** `answer_key_no_bonus_v{version}_check` (PASS/FAIL)

**IF FAIL:** Store details: "Version {version} answer key has bonus question (should not)"

### CHECK 10: Question Count Consistency

**PURPOSE:** Verify all versions have same number of questions

**FOR EACH** version in [A, B, C, D]:

**COMMAND:**
```bash
grep -c "^### [0-9]" {challenge_dir}/challenge-{challenge_num}-v{version}.md
```

**EXTRACT** count from output

**STORE AS:** `question_count_v{version}`

**AFTER** collecting all 4 counts:

**VERIFY:** All counts are identical (vA = vB = vC = vD)

**STORE RESULT AS:** `question_count_consistency_check` (PASS/FAIL)

**STORE COUNT AS:** `total_questions` (for reporting)

**IF FAIL:** Store details: "Question counts differ: vA={vA}, vB={vB}, vC={vC}, vD={vD}"

### CHECK 11: Student Version Header Format

**PURPOSE:** Verify student versions have correct header with exam date

**COMMAND:**
```bash
head -1 {challenge_dir}/challenge-{challenge_num}-vA.md
```

**EXPECTED OUTPUT:** `# Challenge {challenge_num} - {exam_date}`

**COMPARE:** Output MUST match expected (case-sensitive)

**STORE RESULT AS:** `student_header_check` (PASS/FAIL)

**IF FAIL:** Store details: "Student version header incorrect. Expected '# Challenge {challenge_num} - {exam_date}', got '{actual}'"

### CHECK 12: Answer Key Header Format

**PURPOSE:** Verify answer keys have original header format

**COMMAND:**
```bash
head -1 {challenge_dir}/challenge-{challenge_num}-vA-with-key.md
```

**EXPECTED OUTPUT:** Matches regex `^# Challenge \d+ Question Bank Version [A-D] - \d+ total$`

**VERIFY:** Output matches pattern

**STORE RESULT AS:** `answer_key_header_check` (PASS/FAIL)

**IF FAIL:** Store details: "Answer key header format incorrect"

### CHECK 13: Exam Map Alignment - Version A Q1

**PURPOSE:** Verify exam-map correct answer matches answer key bold marker

**STEP 1:** Extract correct answer from exam-map for Version A Question 1

**COMMAND:**
```bash
sed -n '/^## Version A/,/^## Version B/p' {challenge_dir}/exam-map.md | grep "| 1 " | head -1 | awk -F'|' '{print $3}' | tr -d ' *'
```

**EXTRACT** letter (A, B, C, or D)

**STORE AS:** `exam_map_vA_q1_answer`

**STEP 2:** Extract bold answer from answer key for Version A Question 1

**COMMAND:**
```bash
sed -n '/^### 1\./,/^### 2\./p' {challenge_dir}/challenge-{challenge_num}-vA-with-key.md | grep -o "^\*\*([A-D])\*\* \*\*" | sed 's/[^A-D]//g' | head -1
```

**EXTRACT** letter (A, B, C, or D)

**STORE AS:** `answer_key_vA_q1_answer`

**STEP 3:** Compare

**COMPARE:** `exam_map_vA_q1_answer` MUST EQUAL `answer_key_vA_q1_answer`

**STORE RESULT AS:** `exam_map_alignment_vA_q1_check` (PASS/FAIL)

**IF FAIL:** Store details: "Exam map says Version A Q1 answer is {exam_map}, but answer key has {answer_key} marked bold"

### CHECK 14: Exam Map Alignment - Sample from Each Version

**PURPOSE:** Verify exam-map alignment for one question from versions B, C, D

**FOR EACH** version in [B, C, D]:

**STEP 1:** Extract correct answer from exam-map for Version {V} Question 1

**COMMAND:**
```bash
sed -n '/^## Version {V}/,/^## Version /p' {challenge_dir}/exam-map.md | grep "| 1 " | head -1 | awk -F'|' '{print $3}' | tr -d ' *'
```

**EXTRACT** letter

**STORE AS:** `exam_map_v{V}_q1_answer`

**STEP 2:** Extract bold answer from answer key

**COMMAND:**
```bash
sed -n '/^### 1\./,/^### 2\./p' {challenge_dir}/challenge-{challenge_num}-v{V}-with-key.md | grep -o "^\*\*([A-D])\*\* \*\*" | sed 's/[^A-D]//g' | head -1
```

**EXTRACT** letter

**STORE AS:** `answer_key_v{V}_q1_answer`

**STEP 3:** Compare

**COMPARE:** exam_map value MUST EQUAL answer_key value

**STORE RESULT AS:** `exam_map_alignment_v{V}_q1_check` (PASS/FAIL)

**IF FAIL:** Store details: "Exam map says Version {V} Q1 answer is {exam_map}, but answer key has {answer_key} marked bold"

### CHECK 15: No HTML Comments in Output

**PURPOSE:** Verify HTML comments have been stripped from generated files

**COMMAND:**
```bash
grep -c "<!--" {challenge_dir}/challenge-{challenge_num}-vA.md
```

**EXPECTED OUTPUT:** `0`

**EXTRACT** actual count

**COMPARE:** actual MUST EQUAL 0

**STORE RESULT AS:** `html_comments_check` (PASS/FAIL)

**IF FAIL:** Store details: "Found {actual} HTML comments in generated files (should be 0)"

---

## ⚠️ ERROR PROTOCOL

**When to trigger:** Any verification check FAILS **OR** any command exits with non-zero code **OR** unexpected output encountered

**Actions:**

1. **STOP EXECUTION** immediately
2. **DO NOT** proceed to next step
3. **DIAGNOSE** the issue using patterns below
4. **PROPOSE FIX** to user
5. **WAIT** for user approval before executing any fixes
6. **DO NOT CONTINUE** until issue resolved

### Error Diagnosis and Fix Proposals

#### ERROR PATTERN: Pre-Flight Check Failures

**Symptoms:** STEP 1 checks fail (directory or files not found)

**Diagnosis:** Required inputs not created yet

**Proposed Fixes:**

**IF** directory doesn't exist:
```
PROPOSED FIX:
Create the challenge directory:

mkdir -p {challenge_dir}

Then you'll need to create the question-bank-with-answers.md file.
See REFERENCE DOCUMENTATION section for format requirements.

Reply "done" when ready to retry.
```

**IF** question-bank-with-answers.md doesn't exist:
```
PROPOSED FIX:
Create the question bank file:

{challenge_dir}/question-bank-with-answers.md

Format requirements:
- Header: ### 1. ### 2. etc.
- Choices: - **A.** text, - **B.** text, etc.
- Mark correct answer: - **B.** **correct text**
- Exactly 4 choices per question
- Exactly 1 correct answer per question

See REFERENCE DOCUMENTATION section for detailed format.

Reply "done" when ready to retry.
```

#### ERROR PATTERN: Generation Script Validation Errors

**Symptoms:** Script exits with validation error messages in output

**Diagnosis:** Question bank formatting issues

**Proposed Fix Template:**
```
PROPOSED FIX:
The question bank has formatting errors:

{paste relevant error lines from generation_errors}

Common issues:
- Missing choice (need exactly 4: A, B, C, D)
- Multiple bold answers (only 1 per question)
- Missing bold answer (need exactly 1 per question)
- Incorrect header format (use ### 1. ### 2. etc.)

Check question bank file:
{challenge_dir}/question-bank-with-answers.md

Fix the indicated questions, then reply "retry" to run generation again.
```

#### ERROR PATTERN: File Count Mismatches

**Symptoms:** CHECK 1, 2, 3, or 4 fails - file counts don't match expected

**Diagnosis:** Script didn't generate all files OR files were generated in wrong location

**Proposed Fix Template:**
```
PROPOSED FIX:
Expected {expected} files, found {actual}.

Checking what files exist:

{run ls commands to show actual files}

Possible causes:
1. Script failed partway through (check generation output above for errors)
2. Files generated in wrong location
3. Permissions issue

Proposed action:
{if actual = 0}: Script likely failed - check error output above
{if actual < expected}: Some files missing - may need to re-run
{if actual > expected}: Extra files present - may need to clean directory first

Reply with:
- "retry" to run generation again
- "show-output" to see full generation output
- OR provide other instructions
```

#### ERROR PATTERN: Answer Format Issues

**Symptoms:** CHECK 5, 6, or 7 fails - bold markers wrong or missing

**Diagnosis:** Script logic error OR question bank format error

**Proposed Fix Template:**
```
PROPOSED FIX:
Answer formatting issue detected:

{describe specific failure}

This usually indicates:
1. Script version issue (check shuffle_exam.py is up to date)
2. Question bank has malformed bold markers

Let me check a sample question:

{run command to show first question from affected file}

Reply with:
- "show-questions" to see more samples
- "retry" to regenerate
- OR provide guidance
```

#### ERROR PATTERN: Exam Map Alignment Failures

**Symptoms:** CHECK 13 or 14 fails - exam-map doesn't match answer keys

**Diagnosis:** CRITICAL - data structure bug in shuffle_exam.py OR answer extraction failed

**Proposed Fix Template:**
```
🚨 CRITICAL: Exam map alignment failure

Exam map says: Version {V} Q{N} answer is {letter1}
Answer key has: {letter2} marked as bold

This is a critical error - exams cannot be used for grading until resolved.

Let me show the actual question:

{run commands to extract and display the full question from both exam-map and answer key}

This indicates either:
1. Data structure bug in shuffle_exam.py (answer tracking lost during shuffle)
2. Answer extraction regex failed (command error)

RECOMMENDED ACTION:
Do NOT use these exam files. Investigation required.

Reply with:
- "investigate" to see more details
- "retry" to regenerate and check if reproducible
- OR provide guidance
```

#### ERROR PATTERN: Pandoc/Rendering Failures

**Symptoms:** Script fails during rendering phase (if not using --skip-render)

**Diagnosis:** Pandoc not installed OR pandoc version incompatible OR markdown format issue

**Proposed Fix Template:**
```
PROPOSED FIX:
Rendering failed with error:

{paste relevant error from generation_errors}

Common causes:

1. Pandoc not installed:
   Check: which pandoc
   Fix: brew install pandoc  (macOS)
        sudo apt-get install pandoc  (Linux)

2. Pandoc version too old:
   Check: pandoc --version
   Need: >= 2.0

3. Markdown format issue in generated files

Recommended action:
You can proceed without rendering (markdown files are complete and usable).
Or install/update pandoc and retry.

Reply with:
- "skip-render" to regenerate without rendering
- "retry" after installing pandoc
- OR provide guidance
```

### Error Recovery Process

**After proposing fix and receiving user approval:**

1. **IF** user says "retry" or "done":
   - **RETURN TO** STEP 1 of EXECUTION PROTOCOL
   - **RE-RUN** from beginning with same inputs
   - **DO NOT** skip pre-flight checks

2. **IF** user provides alternative fix:
   - **EXECUTE** user's instructions
   - **THEN RETURN TO** STEP 1 of EXECUTION PROTOCOL

3. **IF** user says "skip" or "ignore":
   - **ASK** user to confirm: "Are you sure you want to skip this verification? This may result in unusable exam files. Reply 'confirm skip' to proceed."
   - **IF** user confirms: **CONTINUE** to next step (marking failed check as SKIPPED)
   - **OTHERWISE**: **WAIT** for alternative instruction

### Error Message Template

**Use this template when presenting errors to user:**

```
❌ EXAM GENERATION ERROR

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FAILED CHECK: {check_name}
STEP: {step_number} - {step_name}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXPECTED: {expected_output}
ACTUAL:   {actual_output}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DIAGNOSIS:
{root_cause_explanation}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROPOSED FIX:
{specific_fix_with_commands}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Reply with:
• "retry" - to re-run generation after fix
• "show-output" - to see full command output
• "investigate" - to see more diagnostic details
• OR provide alternative instructions
```

---

## 📊 REPORTING FORMAT

**Use this exact template when presenting final results to user:**

```
✅ EXAM GENERATION COMPLETE

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CHALLENGE {challenge_num}
DATE: {exam_date}
POINTS: {question_points} per question, {bonus_points} bonus
QUESTIONS: {total_questions} {+ bonus if bonus_exists}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 FILES GENERATED

Markdown Files (9):
✅ Student versions (4):
   • {challenge_dir}/challenge-{challenge_num}-vA.md
   • {challenge_dir}/challenge-{challenge_num}-vB.md
   • {challenge_dir}/challenge-{challenge_num}-vC.md
   • {challenge_dir}/challenge-{challenge_num}-vD.md

✅ Answer keys (4):
   • {challenge_dir}/challenge-{challenge_num}-vA-with-key.md
   • {challenge_dir}/challenge-{challenge_num}-vB-with-key.md
   • {challenge_dir}/challenge-{challenge_num}-vC-with-key.md
   • {challenge_dir}/challenge-{challenge_num}-vD-with-key.md

✅ Exam map (1):
   • {challenge_dir}/exam-map.md

{IF skip_render is false:}
Rendered Files (18):
✅ PDFs (9):
   • {challenge_dir}/output/challenge-{challenge_num}-v*.pdf
   • {challenge_dir}/output/challenge-{challenge_num}-v*-with-key.pdf
   • {challenge_dir}/output/exam-map.pdf

✅ DOCX (9):
   • {challenge_dir}/output/challenge-{challenge_num}-v*.docx
   • {challenge_dir}/output/challenge-{challenge_num}-v*-with-key.docx
   • {challenge_dir}/output/exam-map.docx

TOTAL: 27 files
{END IF}

{IF skip_render is true:}
Rendered Files: SKIPPED (use --no-skip-render to generate PDFs and DOCX)

TOTAL: 9 files
{END IF}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ VERIFICATION RESULTS

File Counts:
  ✅ Markdown version files: 8 found
  ✅ Exam map: present
  {IF skip_render is false:}
  ✅ PDF files: 9 found
  ✅ DOCX files: 9 found
  {END IF}

Format Validation:
  ✅ Answer format normalized: **(A)** text
  ✅ Student versions: clean (no bold answers)
    • Version A: 0 bold markers
    • Version B: 0 bold markers
    • Version C: 0 bold markers
    • Version D: 0 bold markers
  ✅ Answer keys: {answer_key_vA_count} answers marked per version
    • Version A: {answer_key_vA_count} bold markers
    • Version B: {answer_key_vB_count} bold markers
    • Version C: {answer_key_vC_count} bold markers
    • Version D: {answer_key_vD_count} bold markers

Content Validation:
  {IF bonus_exists:}
  ✅ Bonus question: present in student versions, absent in keys
  {ELSE:}
  ⚠️  Bonus question: not included (bonus-question.md not found)
  {END IF}
  ✅ Question count: {total_questions} questions consistent across all versions
  ✅ Headers: correct format for student versions and answer keys
  ✅ HTML comments: stripped from output

Critical Verification:
  ✅ Exam map alignment verified:
    • Version A Q1: {exam_map_vA_q1_answer} ✓
    • Version B Q1: {exam_map_vB_q1_answer} ✓
    • Version C Q1: {exam_map_vC_q1_answer} ✓
    • Version D Q1: {exam_map_vD_q1_answer} ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 SAMPLE QUESTIONS FOR REVIEW

Version A - Question 1 (Student Version):
{run: sed -n '/^### 1\./,/^### 2\./p' {challenge_dir}/challenge-{challenge_num}-vA.md | head -n 8}

Version A - Question 1 (Answer Key):
{run: sed -n '/^### 1\./,/^### 2\./p' {challenge_dir}/challenge-{challenge_num}-vA-with-key.md | head -n 8}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 NEXT STEPS

1. REVIEW: Spot-check questions in the sample above
   • Student version should have NO bold answers
   • Answer key should have ONE bold answer per question

2. REVIEW FILES:
   Student versions:
   • {challenge_dir}/challenge-{challenge_num}-vA.md

   Answer keys:
   • {challenge_dir}/challenge-{challenge_num}-vA-with-key.md

   Grading reference:
   • {challenge_dir}/exam-map.md

3. PRINT/DISTRIBUTE:
   {IF skip_render is false:}
   Student PDFs: {challenge_dir}/output/challenge-{challenge_num}-v[A-D].pdf
   Answer PDFs: {challenge_dir}/output/challenge-{challenge_num}-v[A-D]-with-key.pdf
   {ELSE:}
   Re-run with rendering enabled to generate PDFs for distribution
   {END IF}

4. COMMIT (when satisfied):
   git add {challenge_dir}/
   git status
   git commit -m "Add Challenge {challenge_num} exam versions for {exam_date}"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ All verification checks passed
✅ Exam files ready for distribution

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**IF ANY CHECKS FAILED:**

Replace relevant ✅ with ❌ and modify the final status:

```
⚠️  VERIFICATION COMPLETED WITH ISSUES

The following checks failed:
❌ {check_name_1}: {failure_details_1}
❌ {check_name_2}: {failure_details_2}

RECOMMENDED ACTION:
{specific recommendation based on which checks failed}

⚠️  Review issues before using exam files
```

---

## 📚 REFERENCE DOCUMENTATION

The following sections provide detailed reference information for human readers and troubleshooting.

**Note:** Agents executing the workflow should follow **EXECUTION PROTOCOL** section and only reference this section when directed by **ERROR PROTOCOL**.

### Overview

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

### Directory Structure

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
```

### Question Bank Format

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

### Bonus Question Format

Create `bonus-question.md` in the challenge directory (optional).

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

### Understanding the Output Files

#### Student Versions (`challenge-XX-vY.md`)

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

#### Answer Key Versions (`challenge-XX-vY-with-key.md`)

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

#### Exam Map (`exam-map.md`)

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

### Version Differences

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

### Reproducibility Details

#### Fixed Random Seeds

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

#### Changing Seeds

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

### Manual Verification Commands

These commands are for **human verification** only. Agents should use the **AUTOMATED VERIFICATION SUITE** instead.

#### Check file counts

```bash
# Count markdown version files (should be 8: 4 student + 4 keys)
ls challenges/challenge_01/challenge-01-v*.md | wc -l

# Count PDF files (should be 9)
ls challenges/challenge_01/output/*.pdf | wc -l

# Count DOCX files (should be 9)
ls challenges/challenge_01/output/*.docx | wc -l
```

#### Check question counts

```bash
for v in A B C D; do
  echo -n "Version $v: "
  grep -c "^### [0-9]" challenges/challenge_01/challenge-01-v$v.md
done
```

#### Check answer format

```bash
# Check that choices use new format: **(A)** text (not bullets)
grep "^\*\*([A-D])\*\*" challenges/challenge_01/challenge-01-vA.md | head -3
```

#### Check student versions have NO bold answers

```bash
# Should return nothing (empty)
grep "^\*\*([A-D])\*\* \*\*" challenges/challenge_01/challenge-01-vA.md
```

#### Check answer keys HAVE bold answers

```bash
# Should return count equal to question count
grep -c "^\*\*([A-D])\*\* \*\*" challenges/challenge_01/challenge-01-vA-with-key.md
```

#### Check headers

```bash
# Student version - should show custom header with date
head -1 challenges/challenge_01/challenge-01-vA.md

# Answer key - should show original header
head -1 challenges/challenge_01/challenge-01-vA-with-key.md
```

#### Check bonus question

```bash
# Student version - should have bonus
grep "Bonus Question" challenges/challenge_01/challenge-01-vA.md

# Answer key - should NOT have bonus
grep "Bonus Question" challenges/challenge_01/challenge-01-vA-with-key.md
```

#### Check exam-map alignment

```bash
# Check Version A, Question 1 - exam-map says correct answer
grep "| 1 |" challenges/challenge_01/exam-map.md | head -1

# Verify the actual answer key file has bold marker on same letter
sed -n '3,10p' challenges/challenge_01/challenge-01-vA-with-key.md
```

#### Test reproducibility

```bash
# Run twice with same date
python3 challenges/shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-18-25"
python3 challenges/shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-18-25"

# Check with git (should show no changes)
git diff challenges/challenge_01/challenge-01-v*.md
```

### Troubleshooting Common Issues

**Note:** This section is for **human troubleshooting** only. Agents should use **ERROR PROTOCOL** section instead.

#### Script fails with "Directory not found"

```
❌ Error: Directory not found: challenges/challenge_XX
```

**Solution:**
```bash
mkdir -p challenges/challenge_XX
```

#### Script fails with "Input file not found"

```
❌ Error: Input file not found: challenges/challenge_XX/question-bank-with-answers.md
```

**Solution:** Create the file with correct name: `question-bank-with-answers.md`

#### Validation errors

```
❌ VALIDATION ERRORS:
  - Q5: Expected 4 choices, found 3
  - Q12: Multiple correct answers marked (2)
```

**Common causes:**
1. **Missing choice:** Add the missing A/B/C/D choice
2. **Multiple bold answers:** Only ONE answer should have `**text**`
3. **Formatting error:** Check exact format `- **A.** text` for choices
4. **Extra newlines:** Remove blank lines between choices

#### Rendering fails with pandoc errors

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

2. **Skip rendering temporarily:**
   ```bash
   python3 challenges/shuffle_exam.py challenges/challenge_01/ \
     --exam-date "Fri Oct-18-25" --skip-render
   ```

### Command-Line Options Reference

**Basic usage:**
```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/
```

**With exam date:**
```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-18-25"
```

**Skip rendering:**
```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-18-25" --skip-render
```

**Custom point values:**
```bash
python3 challenges/shuffle_exam.py challenges/challenge_01/ \
  --exam-date "Fri Oct-18-25" \
  --question-points 3 \
  --bonus-points 5
```

**Options:**
- `--exam-date`: Date in format "Day Mon-DD-YY" (e.g., "Fri Oct-18-25")
- `--question-points`: Points per question (default: 2)
- `--bonus-points`: Points for bonus question (default: 2)
- `--skip-render`: Skip PDF and DOCX rendering

### Git Workflow

**Recommended workflow:**

1. Create `question-bank-with-answers.md` and `bonus-question.md`
2. Run generation script
3. Review generated versions
4. Commit everything:

```bash
git add challenges/challenge_01/
git status
git commit -m "Add Challenge 01 exam versions for Oct-18-25"
```

**Files to track:**
- ✅ `question-bank-with-answers.md` (source of truth)
- ✅ `bonus-question.md` (bonus question)
- ✅ `challenge-01-vA.md` through `vD.md` (student versions)
- ✅ `challenge-01-vA-with-key.md` through `vD-with-key.md` (answer keys)
- ✅ `exam-map.md` (grading reference)
- ❌ Don't commit: Rendered artifacts (`*.pdf`, `*.docx`) - automatically regenerated

---

## Summary

**Key Features:**
- ✅ Automatic validation (4 choices, 1 correct answer)
- ✅ Answer format normalization (`**(A)** text  ` with 2 trailing spaces)
- ✅ **Answer shuffling across all versions** - prevents answer-pattern cheating
- ✅ Reproducible output (fixed seeds 0, 1, 2, 3)
- ✅ Works with any number of questions
- ✅ Student-ready format (clean, with instructions)
- ✅ Answer keys for grading (with bold markers)
- ✅ Bonus question support (appended to student versions only)
- ✅ Configurable point values
- ✅ Cross-reference exam-map for TAs
- ✅ PDF and DOCX rendering (via pandoc)
- ✅ Comprehensive automated verification
- ✅ Clear error messages and recovery protocols

**Remember:** Student versions are clean and classroom-ready. Answer key versions have bold markers for grading. PDFs are ready for printing or Canvas upload.
