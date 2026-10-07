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

for score in scores:
    score = int(score)

    total_students = total_students + 1
    total_scores = total_scores + score

average = total_scores / total_students

print("Total Students: ", total_students)
print("Total Scores: ", total_scores)
print("Average: ", average)


