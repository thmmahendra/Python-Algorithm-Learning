# Mini Project #3
# Student Score Analyzer
    # Total Student + Total Score + Average
    # Highest + Lowest Score
    # Pass + Fail Analysis
    # Above + Below Average
    # Final Class Report

scores = input("Enter student scores: ").split()

total_students = 0
total_scores = 0

highest_score = float('-inf')
lowest_score = float('inf')

for score in scores:
    score = int(score)

    total_students = total_students + 1
    total_scores = total_scores + score

    if score > highest_score:
        highest_score = score

    if score < lowest_score:
        lowest_score = score

average = total_scores / total_students

print("Total Students: ", total_students)
print("Total Scores: ", total_scores)
print("Average: ", average)

print("Highest Score: ", highest_score)
print("Lowestt Score: ", lowest_score)

