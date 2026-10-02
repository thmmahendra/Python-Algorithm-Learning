# Mini Project #1
# Number Statistics Analyzer

numbers = input("Enter the numbers: ").split()

total_number = 0
total_sum = 0

largest = float('-inf')
smallest = float('inf')

for num in numbers:
    num = int(num)

    total_number = total_number + 1
    total_sum = total_sum + num

    if num > largest:
        largest = num

    if num  < smallest:
        smallest = num


average = total_sum / total_number

print("Total Numbers: ", total_number)
print("Total Sum: ", total_sum)
print("Average: ", average)

print("Largest Number: ", largest)
print("Smallest Number: ", smallest)

