# Mini Project #2 — Text Analysis Tool

In this project, applying concepts learned
in Levels 1–3 of my Python Algorithms course.

## Goal

Build a Python program that analyses a sentence using strings,
loops, conditions, lists, and frequency counting.

## Project Requirements

- Count the total words.
- Count characters, with the treatment of spaces clearly defined.
- Find the longest and shortest words.
- Find the most and least frequent words.
- Identify repeating words.
- Identify words that occur exactly once.
- Display each result clearly.

## Concepts Practised

- Reading user input
- Converting text to lowercase
- Splitting a sentence into words
- Loops and conditional statements
- Counters and comparisons
- Frequency counting
- Avoiding duplicate output using a list

## Requirements

Python 3.

## How to Run

Open a terminal inside this project folder and run:

    python text_analysis_tool.py

Enter a sentence when prompted.

## Example

Input:

    Python is fun and python is useful

After converting to lowercase:

    python is fun and python is useful

Expected word-analysis results:

| Calculation | Result |
|---|---|
| Total words | 7 |
| Longest word | python |
| Shortest word | is |
| Most frequent word | python — 2 occurrences |
| Least frequent word | fun — 1 occurrence |
| Repeating words | python, is |
| Words occurring exactly once | fun, and, useful |

These results assume the first word encountered is selected
when multiple words tie.

Character counts for this example:

    - Including spaces: 33
    - Excluding spaces: 27

Document which character-counting rule the program uses.

## Text-Processing Rules

- Convert input to lowercase before comparing words.
- Split words using whitespace.
- Punctuation remains attached to words unless explicitly removed.
    For example, `python` and `python!` are different words.
- State how the program handles ties for length and frequency.

## Cases to Check

- An empty sentence
- Only spaces
- A single word
- All words being the same
- All words occurring once
- Mixed uppercase and lowercase
- Multiple spaces between words
- Words with punctuation
- Ties in word length or frequency

## Learning Reflection

After completing the project, record:

- What I learned
- Mistakes I corrected
- Limitations of the program
- Time and space complexity

## Course Sequence

1. Number Statistics Analyzer
2. Text Analysis Tool
3. Student Score Analyzer