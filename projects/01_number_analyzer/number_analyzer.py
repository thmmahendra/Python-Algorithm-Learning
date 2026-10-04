# Mini Project #1
# Number Statistics Analyzer
    # Total Numbers
    # Sum
    # Average
    # Largest
    # Smallest
    # Second Largest distinct
    # Second Smallest distinct
    # Duplicate values
    # Unique values

numbers = input("Enter the numbers: ").split()

total_number = 0
total_sum = 0

largest = float('-inf')
second_largest = float('-inf')

smallest = float('inf')
second_smallest= float('inf')

checked_numbers = []
found_duplicate = False

unique_value = []
found_unique = False

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

for num in numbers:
    if num not in checked_numbers:
        count = 0

        for check in numbers:
            if check == num:
                count = count + 1

        if count > 1:
            print("Duplicate Values: ", num)
            found_duplicate = True

        if count == 1:
            unique_value.append(num)
            found_unique = True

        checked_numbers.append(num)

for value in unique_value:
    print("Unique values: ", value)

if found_unique == False:
    print("No unique values.")

if found_duplicate == False:
    print("No duplicate values.")

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



