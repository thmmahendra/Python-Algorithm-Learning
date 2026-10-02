# Mini Project #1
# Number Statistics Analyzer

numbers = input("Enter the numbers: ").split()

total_number = 0
total_sum = 0

for num in numbers:
    num = int(num)

    total_number = total_number + numbers
    total_sum = total_sum + numbers

average = total_sum / total_number

print("Total Numbers: ", total_number)
print("Total Sum: ", total_sum)
print("Average: ", average)