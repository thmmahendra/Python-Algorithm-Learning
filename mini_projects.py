# Mini Project #1
# Number Statistics Analyzer

numbers = input("Enter the numbers: ").split()

total_number = 0
total_sum = 0

largest = float('-inf')
second_largest = float('-inf')

smallest = float('inf')
second_smallest= float('inf')

for num in numbers:
    num = int(num)

    total_number = total_number + 1
    total_sum = total_sum + num

    if num > largest:
        second_largest = largest
        largest = num

    else:
        if num > second_largest and num != largest:
            second_largest = num

    if num  < smallest:
        second_smallest = smallest
        smallest = num

    else:
        if num < second_smallest and num != smallest:
            second_smallest = num


average = total_sum / total_number

print("Total Numbers: ", total_number)
print("Total Sum: ", total_sum)
print("Average: ", average)

print("Largest Number: ", largest)

if second_largest == float('-inf'):
    print("No second largest distinct number.")

else: 
    print("Second Largest Number: ", second_largest)

print("Smallest Number: ", smallest)

if second_smallest == float('inf'):
    print("No second smallest distinct number.")

else:
    print("Second Smallest Number: ", second_smallest)

