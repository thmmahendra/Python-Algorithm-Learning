
# Challenge #1
# Write a program that:

    # Repeatedly accepts numbers.
    # Stops at 0.
    # Finds the largest number.
    # Finds the smallest number.
    # Works with negative number

largest = float('-inf')
smallest = float('inf')

while True:
    numbers = int(input("Enter the numbers: "))

    if numbers == 0:
        break

    if numbers > largest:
        largest = numbers

    if numbers < smallest:
        smallest = numbers

print(
    "Largest: ", largest, 
    "\n Smallest: ", smallest)
        
# Challenge #2
# Given numbers entered until 0, find the second largest number.

largest = float('-inf')
second_largest = float('-inf')

while True:
    numbers = int(input("Enter the number: "))

    if numbers == 0:
        break

    if numbers > largest:
        second_largest = largest
        largest = numbers

    elif numbers > second_largest:
        second_largest = numbers

print(
    "Largest: ", largest,
    "\n Second Largest: ", second_largest
)

# Challenge #3
# Continuously accept numbers until 0, then find:

    # Smallest number
    # Second smallest number

smallest = float('inf')
second_smallest = float('inf')

while True:
    numbers = int(input("Enter the number: "))

    if numbers == 0:
        break

    if numbers < smallest:
        second_smallest = smallest
        smallest = numbers

    elif numbers < second_smallest:
        second_smallest = numbers

print(
    "Smallest: ", smallest,
    "\n Second Smallest: ", second_smallest
)

# Challenge #4
# Write a program that:

   # Continuously asks the user for numbers.
   # Stops when 0 is entered.
   # Then asks the user for one target number.
   # Counts how many times that target appeared.
   # Prints the count.

numbers = []

while True:
    number = int(input("Enter the number: "))

    if number == 0:
        break

    numbers.append(number)

target = int(input("Enter the target number: "))

count = 0

for num in numbers:
    if num == target:
        count = count + 1

print(target, "appeared :", count, "times")


# Challenge #5
# Create a program that asks the user for several numbers, stores them in a list, then creates a new reversed list.

original_num = []
reverse_num = []

while True:
    numbers = int(input("Enter the number: "))

    if numbers == 0:
        break

    original_num.append(numbers)


for index in range(len(original_num) - 1, 
                   -1, 
                   -1
                   ):  # range(start, stop, step)
    
    reverse_num.append(original_num[index])
    
print(original_num, reverse_num)

# Challenge #6
# Reverse List Using while
# Write a program yourself that you can use predefined list and build the reverse manually

numbers = [10, 20, 30, 40, 50]

reversed_numbers = []

index = len(numbers) - 1

while index >= 0:
    reversed_numbers.append(numbers[index])
    index = index - 1

print(reversed_numbers)

# Challenge #7
# Find the number in a list

numbers = [10, 25, 7, 40, 15, 30]

target = int(input("Enter the target: "))
found = False

for num in numbers:
    if num == target:
        found = True

print(found)

# Challenge #8
# Linear Search with break

numbers = [10, 25, 7, 40, 15, 30]

target = int(input("Enter the target: "))

found = False

for num in numbers:
    if num == target:
        found = True
        break
if found:
    print("Found")

else:
    print("Not Found")

# Challenge #9
# Find the index/ Linear Search + Indexing

numbers = [10, 25, 7, 40, 15, 30]

target = int(input("Enter the target: "))

found = False

index = 0

found_index = -1

for num in numbers:
    if num == target:
        found = True
        found_index = index
        break

    index = index + 1
if found:
    print("Index: ", found_index)

else:
    print("Not Found")

# Challenge #10
# Count Occurrences + Find First Index
    # Find the first index of a target.
    # Count how many times the target appears.

numbers = [10, 25, 7, 25, 40, 25, 15]

target = int(input("Enter the number: "))
count = 0
first_index = -1
index = 0

for num in numbers:
    if num == target:
        count = count + 1

        if first_index == -1:
            first_index = index

    index = index + 1

if first_index != -1:
    print("First Index: ", first_index,
          "\n Occurrence", count)

else:
    print("Not Found")

# Challenge #11
    # Reverse a List In Place
    # Two pointers + list swapping

numbers = [10, 20, 30, 40, 50]

right = len(numbers) - 1
left = 0

while left < right:
    numbers[left], numbers[right] = numbers[right], numbers[left]

    left = left + 1
    right = right - 1

print(numbers)

# Challenge #12
# Check if a List is a Palindrome

numbers = [1, 2, 3, 2, 1]

is_palindrome = True

left = 0
right = len(numbers) - 1

while left < right:
    if numbers[left] != numbers[right]:
        is_palindrome = False
        break

    left = left + 1
    right = right - 1

if is_palindrome:
    print("Palindrome")

else:
    print("Not Palindrome")