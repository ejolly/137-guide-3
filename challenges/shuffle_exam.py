#!/usr/bin/env python3
"""
Generate shuffled exam versions from the original question bank.
Shuffles both question order and answer choice order while preserving correctness.

Usage:
    python3 shuffle_exam.py <challenge_directory> [options]
    python3 shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-17-25"
    python3 shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-17-25" --skip-render

Output:
    Markdown files (9 total):
      Student versions (classroom-ready):
        - challenge-XX-vA.md (clean, with instructions & bonus)
        - challenge-XX-vB.md (shuffled, clean, with instructions & bonus)
        - challenge-XX-vC.md (shuffled, clean, with instructions & bonus)
        - challenge-XX-vD.md (shuffled, clean, with instructions & bonus)

      Answer keys (for grading):
        - challenge-XX-vA-with-key.md (original order, marked answers)
        - challenge-XX-vB-with-key.md (shuffled, marked answers)
        - challenge-XX-vC-with-key.md (shuffled, marked answers)
        - challenge-XX-vD-with-key.md (shuffled, marked answers)

      Grading reference:
        - exam-map.md (answer key and cross-reference)

    Rendered artifacts in output/ (18 total - unless --skip-render):
      - PDF versions of all 9 markdown files (via pandoc + typst)
      - DOCX versions of all 9 markdown files (via pandoc)

Format normalization:
    - Input: Accepts both `- **A.**` and `- **A**` bullet formats
    - Output: Normalizes to `**(A)** text` format (no bullets, with trailing spaces)
"""

import re
import random
import sys
import argparse
import subprocess
from pathlib import Path


class ExamValidator:
    """Validates exam question bank format and content."""

    def __init__(self):
        self.errors = []
        self.warnings = []

    def validate_question(self, question_num, question_data):
        """Validate a single question."""
        # Check for exactly 4 choices
        if len(question_data['choices']) != 4:
            self.errors.append(
                f"Q{question_num}: Expected 4 choices, found {len(question_data['choices'])}"
            )
            return False

        # Check for exactly one correct answer
        correct_count = sum(1 for c in question_data['choices'] if c['is_correct'])
        if correct_count == 0:
            self.errors.append(f"Q{question_num}: No correct answer marked")
            return False
        elif correct_count > 1:
            self.errors.append(
                f"Q{question_num}: Multiple correct answers marked ({correct_count})"
            )
            return False

        # Check for non-empty question text
        if not question_data['question_text'].strip():
            self.errors.append(f"Q{question_num}: Empty question text")
            return False

        # Check for non-empty choice text
        for i, choice in enumerate(question_data['choices'], 1):
            if not choice['text'].strip():
                self.warnings.append(
                    f"Q{question_num}, Choice {choice['original_letter']}: Empty choice text"
                )

        return True

    def report(self):
        """Print validation report."""
        if self.errors:
            print("\n❌ VALIDATION ERRORS:")
            for error in self.errors:
                print(f"  - {error}")
            return False

        if self.warnings:
            print("\n⚠️  WARNINGS:")
            for warning in self.warnings:
                print(f"  - {warning}")

        return True


def parse_question_bank(content, validator=None):
    """Parse the markdown file into structured question data."""
    questions = []

    # Remove HTML comments first
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

    # Split by question headers (### followed by number)
    pattern = r'\n### (\d+)\.?\s*\n'
    splits = re.split(pattern, content)

    # splits will be: ['header', '1', 'q1 content', '2', 'q2 content', ...]
    for i in range(1, len(splits), 2):
        if i + 1 >= len(splits):
            break

        question_num = int(splits[i])
        block = splits[i + 1]

        lines = block.strip().split('\n')

        # Find where the question text ends and choices begin
        question_lines = []
        choices = []
        in_choices = False

        for line in lines:
            stripped = line.strip()
            if stripped.startswith('- **'):
                in_choices = True
                # Parse choice - handle both "- **A.**" and "- **A**" formats
                match = re.match(r'- \*\*([A-D])\.?\*\* (.+)', line)
                if match:
                    letter, text = match.groups()
                    # Check if this choice is correct (has bold text)
                    is_correct = text.startswith('**') and text.endswith('**')
                    # Remove bold markers from text
                    clean_text = text.replace('**', '')
                    choices.append({
                        'original_letter': letter,
                        'normalized_letter': f'({letter})',  # Store normalized format
                        'text': clean_text,
                        'is_correct': is_correct
                    })
            elif not in_choices and stripped:  # Only add non-empty lines
                question_lines.append(line)

        question_text = '\n'.join(question_lines).strip()

        # Find which choice is correct
        correct_choice = next((c for c in choices if c['is_correct']), None)

        question_data = {
            'original_num': question_num,
            'question_text': question_text,
            'choices': choices,
            'correct_choice': correct_choice
        }

        # Validate if validator provided
        if validator:
            if validator.validate_question(question_num, question_data):
                questions.append(question_data)
        else:
            questions.append(question_data)

    return questions


def shuffle_and_write_version(questions, version_letter, output_path, challenge_name):
    """Create a shuffled version of the exam with marked answers."""
    # Shuffle question order
    shuffled_questions = questions.copy()
    random.shuffle(shuffled_questions)

    total_questions = len(questions)
    output_lines = [f"# {challenge_name} Question Bank Version {version_letter} - {total_questions} total\n"]

    for new_num, q in enumerate(shuffled_questions, 1):
        # Shuffle answer choices
        shuffled_choices = q['choices'].copy()
        random.shuffle(shuffled_choices)

        # Write question
        output_lines.append(f"### {new_num}.")
        output_lines.append(q['question_text'])
        output_lines.append("")

        # Write choices with normalized format: **(A)** text  (with trailing spaces)
        for new_letter, choice in zip(['A', 'B', 'C', 'D'], shuffled_choices):
            if choice['is_correct']:
                output_lines.append(f"**({new_letter})** **{choice['text']}**  ")
            else:
                output_lines.append(f"**({new_letter})** {choice['text']}  ")

        output_lines.append("")

    # Write file
    with open(output_path, 'w') as f:
        f.write('\n'.join(output_lines))

    return shuffled_questions


def write_version_a(questions, output_path, challenge_name):
    """Write Version A without shuffling (original order) with marked answers."""
    total_questions = len(questions)
    output_lines = [f"# {challenge_name} Question Bank Version A - {total_questions} total\n"]

    for q in questions:
        output_lines.append(f"### {q['original_num']}.")
        output_lines.append(q['question_text'])
        output_lines.append("")

        # Write choices in normalized format: **(A)** text  (with trailing spaces)
        for letter, choice in zip(['A', 'B', 'C', 'D'], q['choices']):
            if choice['is_correct']:
                output_lines.append(f"**({letter})** **{choice['text']}**  ")
            else:
                output_lines.append(f"**({letter})** {choice['text']}  ")
        output_lines.append("")

    with open(output_path, 'w') as f:
        f.write('\n'.join(output_lines))


def create_exam_map(version_a_qs, version_b_qs, version_c_qs, version_d_qs, output_path, challenge_name):
    """Create a mapping document for TAs to use when grading."""

    lines = [f"# {challenge_name} - Exam Version Answer Key & Question Map\n"]
    lines.append("This document helps TAs grade different exam versions.\n")
    lines.append("---\n")

    # Create answer keys for each version
    for version_letter, questions in [('A', version_a_qs), ('B', version_b_qs),
                                       ('C', version_c_qs), ('D', version_d_qs)]:
        lines.append(f"## Version {version_letter} Answer Key\n")
        lines.append("| Q# | Correct Answer | Source Question | Question Preview |")
        lines.append("|----|----------------|-----------------|------------------|")

        for new_num, q in enumerate(questions, 1):
            # Find correct answer letter in shuffled version
            correct_text = q['correct_choice']['text']
            correct_letter = None
            for letter, choice in zip(['A', 'B', 'C', 'D'], q['choices']):
                if choice['text'] == correct_text:
                    correct_letter = letter
                    break

            # Get question preview (first 50 chars)
            preview = q['question_text'].split('\n')[0][:50] + "..."

            lines.append(f"| {new_num} | **{correct_letter}** | A-Q{q['original_num']} | {preview} |")

        lines.append("")

    # Create cross-reference section
    lines.append("\n---\n")
    lines.append("## Cross-Reference: Version A to Other Versions\n")
    lines.append("Use this to find where a Version A question appears in other versions.\n")

    for orig_q in version_a_qs:
        lines.append(f"\n### Version A - Question {orig_q['original_num']}")

        # Find correct answer in version A
        a_correct = None
        for letter, choice in zip(['A', 'B', 'C', 'D'], orig_q['choices']):
            if choice['is_correct']:
                a_correct = letter
                break

        lines.append(f"**Correct Answer: {a_correct}**\n")

        # Find this question in other versions
        for version_letter, questions in [('B', version_b_qs), ('C', version_c_qs), ('D', version_d_qs)]:
            for new_num, q in enumerate(questions, 1):
                if q['original_num'] == orig_q['original_num']:
                    # Find correct letter in this version
                    correct_text = q['correct_choice']['text']
                    correct_letter = None
                    for letter, choice in zip(['A', 'B', 'C', 'D'], q['choices']):
                        if choice['text'] == correct_text:
                            correct_letter = letter
                            break

                    lines.append(f"- Version {version_letter}: Question {new_num} (Correct: {correct_letter})")

    with open(output_path, 'w') as f:
        f.write('\n'.join(lines))


def render_artifacts(challenge_dir, challenge_num):
    """
    Render PDF and DOCX versions of all exam files using pandoc.

    Creates output/ subdirectory with:
    - 4 student PDFs + 4 student DOCX
    - 4 key PDFs + 4 key DOCX
    - 1 map PDF + 1 map DOCX

    Total: 18 artifact files

    Continues on errors and reports failures at the end.
    """
    # Create output directory
    output_dir = challenge_dir / "output"
    output_dir.mkdir(exist_ok=True)

    # Track successes and failures
    successes = []
    failures = []

    # List of all files to render
    files_to_render = []

    # Add student versions
    for version in ['A', 'B', 'C', 'D']:
        files_to_render.append(challenge_dir / f"challenge-{challenge_num}-v{version}.md")

    # Add answer keys
    for version in ['A', 'B', 'C', 'D']:
        files_to_render.append(challenge_dir / f"challenge-{challenge_num}-v{version}-with-key.md")

    # Add exam map
    files_to_render.append(challenge_dir / "exam-map.md")

    # Render each file to both PDF and DOCX
    for md_file in files_to_render:
        if not md_file.exists():
            failures.append({
                'file': md_file.name,
                'format': 'N/A',
                'error': f"Source file not found: {md_file}"
            })
            continue

        # Render PDF
        pdf_file = output_dir / f"{md_file.stem}.pdf"
        try:
            result = subprocess.run(
                ['pandoc', str(md_file), '-o', str(pdf_file), '-t', 'typst'],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                successes.append(pdf_file.name)
            else:
                failures.append({
                    'file': md_file.name,
                    'format': 'PDF',
                    'error': result.stderr.strip() or 'Unknown error'
                })
        except subprocess.TimeoutExpired:
            failures.append({
                'file': md_file.name,
                'format': 'PDF',
                'error': 'Timeout after 30 seconds'
            })
        except FileNotFoundError:
            failures.append({
                'file': md_file.name,
                'format': 'PDF',
                'error': 'pandoc not found - check installation'
            })
        except Exception as e:
            failures.append({
                'file': md_file.name,
                'format': 'PDF',
                'error': str(e)
            })

        # Render DOCX
        docx_file = output_dir / f"{md_file.stem}.docx"
        try:
            result = subprocess.run(
                ['pandoc', str(md_file), '-o', str(docx_file)],
                capture_output=True,
                text=True,
                timeout=30
            )
            if result.returncode == 0:
                successes.append(docx_file.name)
            else:
                failures.append({
                    'file': md_file.name,
                    'format': 'DOCX',
                    'error': result.stderr.strip() or 'Unknown error'
                })
        except subprocess.TimeoutExpired:
            failures.append({
                'file': md_file.name,
                'format': 'DOCX',
                'error': 'Timeout after 30 seconds'
            })
        except FileNotFoundError:
            failures.append({
                'file': md_file.name,
                'format': 'DOCX',
                'error': 'pandoc not found - check installation'
            })
        except Exception as e:
            failures.append({
                'file': md_file.name,
                'format': 'DOCX',
                'error': str(e)
            })

    # Print summary
    total_expected = len(files_to_render) * 2  # Each file -> PDF + DOCX
    success_count = len(successes)
    failure_count = len(failures)

    print(f"\n📦 Rendering artifacts to {output_dir}/")

    if failure_count == 0:
        print(f"✅ Successfully rendered {success_count}/{total_expected} artifacts")
    else:
        print(f"⚠️  Rendered {success_count}/{total_expected} artifacts ({failure_count} failures)")
        print(f"\nFailed renders:")
        for fail in failures:
            print(f"  - {fail['file']} ({fail['format']}): {fail['error']}")

        print(f"\n💡 Possible fixes:")
        print(f"  - Check pandoc is installed: pandoc --version")
        print(f"  - For PDF errors: Check typst backend is available (pandoc 3.0+)")
        print(f"  - For DOCX errors: Check file has valid markdown")
        print(f"  - Try rendering manually:")
        print(f"      pandoc {files_to_render[0].name} -o output.pdf -t typst")
        print(f"      pandoc {files_to_render[0].name} -o output.docx")

    return success_count, failure_count


def extract_challenge_name(challenge_dir):
    """Extract challenge name from directory path."""
    # e.g., "challenges/challenge_01/" -> "Challenge 01"
    dir_name = Path(challenge_dir).name
    match = re.match(r'challenge[_-]?(\d+)', dir_name, re.IGNORECASE)
    if match:
        num = match.group(1)
        return f"Challenge {num}"
    return "Challenge"


def get_exam_date(date_arg):
    """Get exam date from args or prompt user."""
    if date_arg:
        # Validate format: "Day Mon-DD-YY"
        if re.match(r'^[A-Z][a-z]{2} [A-Z][a-z]{2}-\d{2}-\d{2}$', date_arg):
            return date_arg
        else:
            print(f"❌ Invalid date format: {date_arg}")
            print("Expected format: 'Fri Oct-17-25' (Day Mon-DD-YY)")
            sys.exit(1)

    # Prompt user
    print("\n📅 Exam date required for student versions.")
    print("Format: Day Mon-DD-YY (e.g., 'Fri Oct-17-25')")
    date_input = input("Enter exam date: ").strip()

    # Validate
    if re.match(r'^[A-Z][a-z]{2} [A-Z][a-z]{2}-\d{2}-\d{2}$', date_input):
        return date_input
    else:
        print("❌ Invalid format. Please restart and use correct format.")
        sys.exit(1)


def create_answer_key_copy(version_file, output_path):
    """Create a copy of the version file as the answer key."""
    with open(version_file, 'r') as f:
        content = f.read()

    with open(output_path, 'w') as f:
        f.write(content)


def parse_bonus_question(bonus_file):
    """Parse bonus question from markdown file."""
    with open(bonus_file, 'r') as f:
        content = f.read()

    # Remove header if present
    content = re.sub(r'^###\s+Bonus\s*\n', '', content.strip())

    lines = content.split('\n')
    question_lines = []
    choices = []
    in_choices = False

    for line in lines:
        stripped = line.strip()
        if stripped.startswith('- **'):
            in_choices = True
            # Parse choice and normalize to (A)/(B)/(C)/(D) format with trailing spaces
            match = re.match(r'- \*\*([A-D])\.?\*\* (.+)', line)
            if match:
                letter, text = match.groups()
                choices.append(f"**({letter})** {text}  ")
        elif not in_choices and stripped:
            question_lines.append(line)

    question_text = '\n'.join(question_lines).strip()
    return question_text, choices


def create_student_header(challenge_name, exam_date):
    """Create student-friendly header."""
    # Extract challenge number
    challenge_num = re.search(r'\d+', challenge_name).group()

    return f"# Challenge {challenge_num} - {exam_date}"


def create_instructions_block(question_count, points_per_q):
    """Create instructions block for students."""
    return f"""
**Instructions:**

You will have the full lecture time to answer all {question_count} multiple choice questions. Each question is worth {points_per_q} points. Think carefully about what each question asks and what each answer claims - we're not trying to trick you! Good luck!

---
"""


def create_bonus_section(bonus_file, bonus_points):
    """Parse and format bonus question for student version."""
    question_text, choices = parse_bonus_question(bonus_file)

    section = f"""### Bonus Question

**No right answer - Free {bonus_points} points!**

{question_text}

"""

    for choice in choices:
        section += choice + "\n"

    return section.strip()


def transform_to_student_version(version_file, challenge_name, exam_date,
                                 question_count, question_points,
                                 bonus_points, bonus_file):
    """Transform answer key version to student-ready version."""

    # Read current content
    with open(version_file, 'r') as f:
        content = f.read()

    # Step 1: Replace header with student-friendly header
    new_header = create_student_header(challenge_name, exam_date)

    # Replace old header (first line)
    lines = content.split('\n')
    lines[0] = new_header

    # Step 2: Add instructions block after header
    instructions = create_instructions_block(question_count, question_points)
    # Insert after header and before first empty line
    lines.insert(1, instructions)
    content = '\n'.join(lines)

    # Step 3: Remove bold answer markers
    # Pattern: **(A)** **text**   -> **(A)** text
    content = re.sub(
        r'(\*\*\([A-D]\)\*\* )\*\*(.+?)\*\*  $',
        r'\1\2  ',
        content,
        flags=re.MULTILINE
    )

    # Step 4: Append bonus question if exists
    if bonus_file.exists():
        bonus_content = create_bonus_section(bonus_file, bonus_points)
        content += "\n\n" + bonus_content

    # Write back
    with open(version_file, 'w') as f:
        f.write(content)


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Generate shuffled exam versions from question bank',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Interactive date prompt
  python3 shuffle_exam.py challenges/challenge_01/

  # Specify exam date
  python3 shuffle_exam.py challenges/challenge_01/ --exam-date "Fri Oct-17-25"

  # Custom point values
  python3 shuffle_exam.py challenges/challenge_01/ \\
    --exam-date "Fri Oct-17-25" \\
    --question-points 3 \\
    --bonus-points 5
        """
    )

    parser.add_argument(
        'challenge_dir',
        nargs='?',
        default='challenges/challenge_01',
        help='Challenge directory path (default: challenges/challenge_01)'
    )

    parser.add_argument(
        '--exam-date',
        help='Exam date in format "Day Mon-DD-YY" (e.g., "Fri Oct-17-25")'
    )

    parser.add_argument(
        '--question-points',
        type=int,
        default=2,
        help='Points per question (default: 2)'
    )

    parser.add_argument(
        '--bonus-points',
        type=int,
        default=2,
        help='Points for bonus question (default: 2)'
    )

    parser.add_argument(
        '--skip-render',
        action='store_true',
        help='Skip PDF/DOCX rendering (default: False)'
    )

    return parser.parse_args()


def main():
    # Parse command line arguments
    args = parse_arguments()
    challenge_dir = Path(args.challenge_dir)

    # Validate directory exists
    if not challenge_dir.exists():
        print(f"❌ Error: Directory not found: {challenge_dir}")
        print(f"Usage: python3 {sys.argv[0]} <challenge_directory>")
        sys.exit(1)

    # Find input file
    input_file = challenge_dir / "question-bank-with-answers.md"
    if not input_file.exists():
        print(f"❌ Error: Input file not found: {input_file}")
        print(f"Expected file: question-bank-with-answers.md")
        sys.exit(1)

    print(f"📁 Processing: {challenge_dir}")
    print(f"📄 Input file: {input_file.name}")

    # Get exam date
    exam_date = get_exam_date(args.exam_date)
    print(f"📅 Exam date: {exam_date}\n")

    # Extract challenge name and number for file naming
    challenge_name = extract_challenge_name(challenge_dir)
    challenge_num = re.search(r'\d+', challenge_name).group() if re.search(r'\d+', challenge_name) else "01"

    # Read original file
    with open(input_file, 'r') as f:
        content = f.read()

    # Validate and parse questions
    validator = ExamValidator()
    questions = parse_question_bank(content, validator)

    # Check validation results
    if not validator.report():
        print("\n❌ Validation failed. Please fix errors before generating exam versions.")
        sys.exit(1)

    question_count = len(questions)
    print(f"✅ Parsed {question_count} valid questions\n")

    # Check for bonus question
    bonus_file = challenge_dir / "bonus-question.md"
    has_bonus = bonus_file.exists()

    # Set base random seed for reproducibility
    random.seed(0)

    # ===== STEP 1: Generate initial versions with marked answers =====
    print("📝 Generating initial versions with marked answers...")

    # Version A is the original (no shuffling) - keep original order
    version_a_qs = questions.copy()
    output_a = challenge_dir / f"challenge-{challenge_num}-vA.md"
    write_version_a(version_a_qs, output_a, challenge_name)

    # Generate other versions with different random seeds
    random.seed(1)
    version_b_qs = shuffle_and_write_version(
        questions, 'B',
        challenge_dir / f"challenge-{challenge_num}-vB.md",
        challenge_name
    )

    random.seed(2)
    version_c_qs = shuffle_and_write_version(
        questions, 'C',
        challenge_dir / f"challenge-{challenge_num}-vC.md",
        challenge_name
    )

    random.seed(3)
    version_d_qs = shuffle_and_write_version(
        questions, 'D',
        challenge_dir / f"challenge-{challenge_num}-vD.md",
        challenge_name
    )

    # ===== STEP 2: Create answer key copies =====
    print("🔑 Creating answer key copies...")

    for version_letter in ['A', 'B', 'C', 'D']:
        version_file = challenge_dir / f"challenge-{challenge_num}-v{version_letter}.md"
        key_file = challenge_dir / f"challenge-{challenge_num}-v{version_letter}-with-key.md"
        create_answer_key_copy(version_file, key_file)
        print(f"  ✅ {key_file.name}")

    # ===== STEP 3: Transform student versions =====
    print("\n📋 Transforming to student-ready versions...")

    for version_letter in ['A', 'B', 'C', 'D']:
        version_file = challenge_dir / f"challenge-{challenge_num}-v{version_letter}.md"
        transform_to_student_version(
            version_file,
            challenge_name,
            exam_date,
            question_count,
            args.question_points,
            args.bonus_points,
            bonus_file
        )
        print(f"  ✅ {version_file.name}")

    # ===== STEP 4: Create exam map =====
    print("\n🗺️  Creating exam map...")
    exam_map_path = challenge_dir / "exam-map.md"
    create_exam_map(
        version_a_qs, version_b_qs, version_c_qs, version_d_qs,
        exam_map_path, challenge_name
    )
    print(f"  ✅ {exam_map_path.name}")

    # ===== STEP 5: Render artifacts (PDF + DOCX) =====
    if not args.skip_render:
        render_success, render_failure = render_artifacts(challenge_dir, challenge_num)
    else:
        print("\n⏭️  Skipping artifact rendering (--skip-render flag set)")
        render_success, render_failure = 0, 0

    # ===== SUMMARY =====
    total_base_points = question_count * args.question_points
    total_points = total_base_points + (args.bonus_points if has_bonus else 0)

    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    print(f"Challenge: {challenge_name}")
    print(f"Exam Date: {exam_date}")
    print(f"Questions: {question_count} ({args.question_points} points each = {total_base_points} points)")
    print(f"Bonus: {'Yes' if has_bonus else 'No'} ({args.bonus_points} points)" if has_bonus else "Bonus: No")
    print(f"Total Possible: {total_points} points")
    print(f"\nFiles Generated:")
    print(f"  Student Versions (classroom-ready):")
    for v in ['A', 'B', 'C', 'D']:
        print(f"    ✅ challenge-{challenge_num}-v{v}.md")
    print(f"\n  Answer Keys (for grading):")
    for v in ['A', 'B', 'C', 'D']:
        print(f"    ✅ challenge-{challenge_num}-v{v}-with-key.md")
    print(f"\n  Grading Reference:")
    print(f"    ✅ exam-map.md")

    if not args.skip_render:
        print(f"\n  Rendered Artifacts (output/):")
        if render_failure == 0:
            print(f"    ✅ {render_success} PDFs and DOCX files")
        else:
            print(f"    ⚠️  {render_success} files rendered, {render_failure} failed")

    print(f"\nOutput directory: {challenge_dir}")
    print(f"Random seeds: A=none, B=1, C=2, D=3")
    print("\n✅ All exam versions generated successfully!")


if __name__ == '__main__':
    main()
