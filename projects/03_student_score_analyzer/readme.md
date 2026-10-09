# Mini Project #3 — Student Score Analyzer

In this project, applying concepts learned
in Levels 1–3 of my Python Algorithms course.

## Goal

Build a Python program that summarises student scores using
loops, conditions, lists, and arithmetic.

## Project Requirements

- Count the total students.
- Calculate the total and average scores.
- Find the highest and lowest scores.
- Count students who passed and failed.
- Count students scoring above, below, and equal to the average.
- Display a clear summary.

Each entered score represents one student.

## Concepts Practised

- Reading and splitting user input
- Converting input into numbers
- Loops and conditional statements
- Counters and running totals
- Tracking highest and lowest values
- Calculating an average
- Comparing each score with the average

## Requirements

Python 3.

## How to Run

Open a terminal inside this project folder and run:

    python student_score_analyzer.py

Enter scores separated by spaces when prompted.

## Example

Input:

    80 60 40 20 50

Expected results, using a pass mark of 40:

| Calculation | Result |
|---|---|
| Total students | 5 |
| Total scores | 250 |
| Average score | 50 |
| Highest score | 80 |
| Lowest score | 20 |
| Passed students | 4 |
| Failed students | 1 |
| Above average | 2 |
| Below average | 2 |
| Equal to average | 1 |

A score equal to the pass mark counts as a pass.

## Analysis Rules

- Count repeated scores separately because they represent
  different students.
- Calculate the class average before counting students above,
  below, or equal to it.
- Use the unrounded average for comparisons.
- Keep passing status separate from comparison with the average:
  a student can pass while scoring below the class average.

## Cases to Check

- Empty input
- A single student
- All scores being the same
- All students passing
- All students failing
- A score exactly equal to the pass mark
- Scores exactly equal to the average
- An average containing a decimal
- Non-numeric input and scores outside the permitted range

## Learning Reflection

After completing the project, record:

- What I learned
- Mistakes I corrected
- Inputs the program does not yet handle
- Time and space complexity

## Course Sequence

1. Number Statistics Analyzer
2. Text Analysis Tool
3. Student Score Analyzer