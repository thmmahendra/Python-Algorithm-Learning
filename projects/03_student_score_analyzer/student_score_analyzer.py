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

passed_students = 0
failed_students = 0

above_average = 0
below_average = 0
equal_average = 0

for score in scores:
    score = int(score)

    total_students = total_students + 1
    total_scores = total_scores + score

    if score > highest_score:
        highest_score = score

    if score < lowest_score:
        lowest_score = score

    if score >= 40:
        passed_students = passed_students + 1

    else:
        failed_students = failed_students + 1

average = total_scores / total_students

for score in scores:
    score = int(score)

    if score > average:
        above_average = above_average + 1

    if score < average:
        below_average = below_average + 1

    else:
        if score == average:
            equal_average = equal_average + 1

print("Total Students: ", total_students)
print("Total Scores: ", total_scores)
print("Average: ", average)

print("Highest Score: ", highest_score)
print("Lowest Score: ", lowest_score)

print("Passed Students: ", passed_students)
print("Failed Students: ", failed_students)

print("Above: ", above_average)
print("Below: ", below_average)
print("Equal to Average: ", equal_average)



