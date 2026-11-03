 Placement Readiness Tracker

## Purpose

This Python command-line project stores student practice-test scores, calculates averages and grades, identifies the top scorer, and lists students who need extra practice. A separate program solves the runner-up score problem.

## Files

- `tracker.py`: Student data, input validation, result functions, and formatted output.
- `runner_up.py`: Second-highest distinct score solution using standard input/output.
- `TEST_CASES.md`: Runner-up inputs, expected outputs, and observed outputs.

## Requirements

Python 3 and Git. The Python programs use only the standard library; no external packages are needed.

## Run the tracker

```bash
python3 tracker.py
```

The program starts with five sample students and asks for one more. Names and roll numbers are strings. Scores are converted to floats. Each score must be between 0 and 100 inclusive; invalid input is rejected using a loop.

Example entries:

```text
Add one student
Enter name: varun
Enter roll number: CSE006
Enter aptitude score (0-100): 12
Enter verbal score (0-100): 34
Enter coding score (0-100): 56

```

The result table will include:

```text
PLACEMENT READINESS RESULTS
Roll No    Name          Aptitude   Verbal   Coding   Average  Grade
-----------------------------------------------------------------------------
CSE001     Sangita           85.0     80.0     90.0     85.00  A
CSE002     Punit             65.0     70.0     75.0     70.00  B
CSE003     Tom               45.0     50.0     55.0     50.00  C
CSE004     Neha              20.0     30.0     40.0     30.00  Needs practice
CSE005     Zoya              90.0     95.0     85.0     90.00  A
CSE006     varun             12.0     34.0     56.0     34.00  Needs practice

Top scorer: Zoya (CSE005)
Highest average: 90.00

Students needing practice (average below 40):
- Neha (CSE004): 30.00

## Grade boundaries

- A: average >= 80.
- B: 60 <= average < 80.
- C: 40 <= average < 60.
- Needs practice: average < 40.

`top_scorer(students)` returns the student dictionary. If averages tie, it returns the first student with the highest average. `needs_practice(students)` uses the default limit of 40.

## Run the runner-up solution

```bash
python3 runner_up.py
```

Enter `n` on the first line and all `n` scores on the next line.

Sample input:

```text
5
70 85 85 60 90
```

Sample output:

```text
85
```

The solution removes duplicates with a set, sorts the distinct scores in ascending order, and prints the second-last value. Input follows the assignment constraints: 2 <= n <= 100, scores between 0 and 100, and at least two distinct scores.

## Data storage

Student data is held in memory for one run. Running the program again starts from the original five records.

## AI use declaration

I used ChatGPT to understand the assignment, draft the Python programs and report text, and plan testing and Git documentation.
````
