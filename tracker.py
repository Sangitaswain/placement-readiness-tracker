"""Record practice scores and display placement-readiness results."""


def average(student):
    """Return the mean of the student's three scores."""
    return (student["aptitude"] + student["verbal"] + student["coding"]) / 3


def grade(avg):
    """Return the grade using the assignment's exact boundaries."""
    if avg >= 80:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Needs practice"


def top_scorer(students):
    """Return the student with the highest average; the first wins a tie."""
    return max(students, key=average)


def needs_practice(students, limit=40):
    """Return students whose average is strictly below the given limit."""
    practice_students = []
    for student in students:
        if average(student) < limit:
            practice_students.append(student)
    return practice_students


def read_text(prompt):
    """Keep asking until the user supplies non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def read_score(subject):
    """Convert a score to float and reject non-numeric or out-of-range input."""
    while True:
        try:
            score = float(input(f"Enter {subject} score (0-100): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if 0 <= score <= 100:
            return score
        print("Invalid score. Please enter a value from 0 to 100.")


def add_student(students):
    """Read one additional student and append a dictionary to the list."""
    print("\nAdd one student")
    student = {
        "name": read_text("Enter name: "),
        # Roll numbers stay as strings, preserving letters and leading zeros.
        "roll_no": read_text("Enter roll number: "),
        "aptitude": read_score("aptitude"),
        "verbal": read_score("verbal"),
        "coding": read_score("coding"),
    }
    students.append(student)


def print_results(students):
    """Print each result in a table, followed by the two required summaries."""
    print("\nPLACEMENT READINESS RESULTS")
    header = (
        f"{'Roll No':<10} {'Name':<12} {'Aptitude':>9} {'Verbal':>8} "
        f"{'Coding':>8} {'Average':>9}  {'Grade':<14}"
    )
    print(header)
    print("-" * len(header))

    for student in students:
        avg = average(student)
        print(
            f"{student['roll_no']:<10} {student['name']:<12} "
            f"{student['aptitude']:>9.1f} {student['verbal']:>8.1f} "
            f"{student['coding']:>8.1f} {avg:>9.2f}  {grade(avg):<14}"
        )

    topper = top_scorer(students)
    print(f"\nTop scorer: {topper['name']} ({topper['roll_no']})")
    print(f"Highest average: {average(topper):.2f}")

    # Leaving out the second argument demonstrates the default limit of 40.
    practice_students = needs_practice(students)
    print("\nStudents needing practice (average below 40):")
    if practice_students:
        for student in practice_students:
            print(
                f"- {student['name']} ({student['roll_no']}): "
                f"{average(student):.2f}"
            )
    else:
        print("No students need extra practice under this criterion.")


def main():
    """Start with five students, add a sixth through input, and show results."""
    students = [
        {"name": "Sangita", "roll_no": "CSE001", "aptitude": 85, "verbal": 80, "coding": 90},
        {"name": "Punit", "roll_no": "CSE002", "aptitude": 65, "verbal": 70, "coding": 75},
        {"name": "Tom", "roll_no": "CSE003", "aptitude": 45, "verbal": 50, "coding": 55},
        {"name": "Neha", "roll_no": "CSE004", "aptitude": 20, "verbal": 30, "coding": 40},
        {"name": "Zoya", "roll_no": "CSE005", "aptitude": 90, "verbal": 95, "coding": 85},
    ]

    print("PLACEMENT READINESS TRACKER")
    print(f"Initial student records: {len(students)}")
    add_student(students)
    print(f"\nTotal student records: {len(students)}")
    print_results(students)


# Run the interactive program only when this file is executed directly.
if __name__ == "__main__":
    main()

