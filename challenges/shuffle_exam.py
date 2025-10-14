#!/usr/bin/env python3
"""
Generate shuffled exam versions from the original question bank.
Shuffles both question order and answer choice order while preserving correctness.

Usage:
    python3 shuffle_exam.py <challenge_directory>
    python3 shuffle_exam.py challenges/challenge_01/

Output:
    - challenge-XX-vA.md (original order)
    - challenge-XX-vB.md (shuffled)
    - challenge-XX-vC.md (shuffled)
    - challenge-XX-vD.md (shuffled)
    - exam-map.md (answer key and cross-reference)
"""

import re
import random
import sys
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
    """Create a shuffled version of the exam."""
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

        # Write choices with new letters (using period for consistency)
        for new_letter, choice in zip(['A', 'B', 'C', 'D'], shuffled_choices):
            if choice['is_correct']:
                output_lines.append(f"- **{new_letter}.** **{choice['text']}**")
            else:
                output_lines.append(f"- **{new_letter}.** {choice['text']}")

        output_lines.append("")

    # Write file
    with open(output_path, 'w') as f:
        f.write('\n'.join(output_lines))

    return shuffled_questions


def write_version_a(questions, output_path, challenge_name):
    """Write Version A without shuffling (original order)."""
    total_questions = len(questions)
    output_lines = [f"# {challenge_name} Question Bank Version A - {total_questions} total\n"]

    for q in questions:
        output_lines.append(f"### {q['original_num']}.")
        output_lines.append(q['question_text'])
        output_lines.append("")

        # Write choices in original order
        for letter, choice in zip(['A', 'B', 'C', 'D'], q['choices']):
            if choice['is_correct']:
                output_lines.append(f"- **{letter}.** **{choice['text']}**")
            else:
                output_lines.append(f"- **{letter}.** {choice['text']}")
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


def extract_challenge_name(challenge_dir):
    """Extract challenge name from directory path."""
    # e.g., "challenges/challenge_01/" -> "Challenge 01"
    dir_name = Path(challenge_dir).name
    match = re.match(r'challenge[_-]?(\d+)', dir_name, re.IGNORECASE)
    if match:
        num = match.group(1)
        return f"Challenge {num}"
    return "Challenge"


def main():
    # Parse command line arguments
    if len(sys.argv) > 1:
        challenge_dir = Path(sys.argv[1])
    else:
        challenge_dir = Path("challenges/challenge_01")

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
    print(f"📄 Input file: {input_file.name}\n")

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

    print(f"✅ Parsed {len(questions)} valid questions\n")

    # Set base random seed for reproducibility
    random.seed(0)

    # Version A is the original (no shuffling) - keep original order
    version_a_qs = questions.copy()
    output_a = challenge_dir / f"challenge-{challenge_num}-vA.md"
    write_version_a(version_a_qs, output_a, challenge_name)
    print(f"✅ Created: {output_a.name} (original order)")

    # Generate other versions with different random seeds
    random.seed(1)
    version_b_qs = shuffle_and_write_version(
        questions, 'B',
        challenge_dir / f"challenge-{challenge_num}-vB.md",
        challenge_name
    )
    print(f"✅ Created: challenge-{challenge_num}-vB.md (shuffled)")

    random.seed(2)
    version_c_qs = shuffle_and_write_version(
        questions, 'C',
        challenge_dir / f"challenge-{challenge_num}-vC.md",
        challenge_name
    )
    print(f"✅ Created: challenge-{challenge_num}-vC.md (shuffled)")

    random.seed(3)
    version_d_qs = shuffle_and_write_version(
        questions, 'D',
        challenge_dir / f"challenge-{challenge_num}-vD.md",
        challenge_name
    )
    print(f"✅ Created: challenge-{challenge_num}-vD.md (shuffled)")

    # Create exam map
    exam_map_path = challenge_dir / "exam-map.md"
    create_exam_map(
        version_a_qs, version_b_qs, version_c_qs, version_d_qs,
        exam_map_path, challenge_name
    )
    print(f"✅ Created: {exam_map_path.name} (answer key & cross-reference)\n")

    # Print summary
    print("=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    print(f"Challenge: {challenge_name}")
    print(f"Questions: {len(questions)}")
    print(f"Versions: 4 (A=original, B/C/D=shuffled)")
    print(f"Output directory: {challenge_dir}")
    print(f"\nRandom seeds used: A=none, B=1, C=2, D=3")
    print("\n✅ All exam versions generated successfully!")


if __name__ == '__main__':
    main()
