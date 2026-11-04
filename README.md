# Placement Readiness Tracker

## Purpose

This Python command-line project records placement practice-test scores, calculates averages and grades, identifies the top scorer, and lists students who need extra practice. A separate program solves the runner-up score problem.

## Files

- `tracker.py`: Student records, input validation, required functions, and formatted results.
- `runner_up.py`: Second-highest distinct score solution using standard input/output.
- `TEST_CASES.md`: Test inputs, expected outputs, and actual outputs from three runs.

## Requirements

Python 3 and Git. No external Python packages are required.

## Run the tracker

```bash
python3 tracker.py
```

The program starts with five sample students and asks for one additional student. Names and roll numbers are strings. Scores are converted to floats and must be between 0 and 100 inclusive. A loop rejects out-of-range values, and non-numeric input is handled without ending the program.

Sample accepted entries:

```text
Name: Varun
Roll number: CSE006
Aptitude: 100
Verbal: 72
Coding: 90
```

During validation testing, aptitude 101 and coding abc were rejected before the accepted values above were entered.

Sample output:

```text
PLACEMENT READINESS RESULTS
Roll No    Name          Aptitude   Verbal   Coding   Average  Grade
-----------------------------------------------------------------------------
CSE001     Sangita           85.0     80.0     90.0     85.00  A
CSE002     Punit             65.0     70.0     75.0     70.00  B
CSE003     Tom               45.0     50.0     55.0     50.00  C
CSE004     Neha              20.0     30.0     40.0     30.00  Needs practice
CSE005     Zoya              90.0     95.0     85.0     90.00  A
CSE006     Varun            100.0     72.0     90.0     87.33  A

Top scorer: Zoya (CSE005)
Highest average: 90.00

Students needing practice (average below 40):
- Neha (CSE004): 30.00
```

## Grade boundaries

- A: average >= 80.
- B: 60 <= average < 80.
- C: 40 <= average < 60.
- Needs practice: average < 40.

`average(student)` returns the mean of three scores. `top_scorer(students)` returns the student dictionary with the highest average; the first highest record is returned if averages tie. `needs_practice(students)` demonstrates the default limit of 40.

## Run the runner-up solution

```bash
python3 runner_up.py
```

Enter n on the first line and all n scores on the second line. The program waits for input without printing a prompt.

Sample input:

```text
5
70 85 85 60 90
```

Sample output:

```text
85
```

The solution removes duplicates with a set, sorts the distinct scores in ascending order, and selects the second-last value. Valid input satisfies 2 <= n <= 100, scores from 0 to 100, and at least two distinct scores.

To supply the sample input automatically:

```bash
printf '5\n70 85 85 60 90\n' | python3 runner_up.py
```

## Testing

The three own test cases in `TEST_CASES.md` returned 90, 0, and 20, matching their expected outputs. They cover a repeated maximum, zero with duplicates, and minimum input size.

## Data storage

Student records are stored in memory for one execution. Starting the tracker again restores the original five sample records.

## AI use declaration

I used ChatGPT for concept clarification, code drafting and debugging, and report preparation, and Claude to review the submission.
