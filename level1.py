# Challenge #1
# Write a Python program that asks the user to enter a number and determines whether the number is: Positive or Negative

number = int(input("Enter the number:"))

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")

# Challenge #2
# Determine whether a number is even or odd

number = int(input("Enter the number:"))

if number % 2 == 0:
    print("Even")

else:
    print("Odd")

# Challenge #3
# Find the largest of three numbers

first_num = int(input("Enter the first number:"))
second_num = int(input("Enter the second number:"))
third_num = int(input("Enter the third number:"))

if first_num >= second_num and first_num >= third_num:
    print("Largest:", first_num)

elif second_num >= first_num and second_num >= third_num:
    print("Largest:", second_num)

else:
    print("Largest:", third_num)

# Challenge #4
# Create a program that asks for a person's age and determines whether they are eligible to vote.

age = int(input("Enter your age:"))

if age >= 18 and age <= 100:
    print("Eligible to vote")
else:
    print("Not Eligible")

# Challenge #5
# Write a program that asks the user for a number n and calculates the sum of all numbers from 1 to n.

numbers = int(input("Enter the number:"))

total = 0

for num in range(1, numbers + 1):
    total = total + num

print(total)

# Challenge #6
# Write a program that asks the user for a positive number n and prints the numbers from 1 to n using a while loop.

numbers = int(input("Enter the positive number:"))

count = 1

while count <= numbers:
    print(count)
    count = count + 1


# Challenge #7
# Ask the user for a positive number n and calculate the sum from 1 to n, but this time you must use a while loop.

numbers = int(input("Enter the positive number:"))

count = 1
total = 0

while count <= numbers:
    total = total + count
    count = count + 1

print(total)

# Challenge #8
# Create a program that repeatedly asks the user to enter a number.

while True:
    numbers = int(input("Enter the number:"))

    if numbers == 0:
        break

    print("You entered: ", numbers)   

# Challenge #9
# Write a program that:
    # 1. Continuously asks the user for numbers.
    # 2. Stops when the user enters 0.
    # 3. Counts how many nonzero numbers were entered.
    # 4. Prints the final count after the loop.

count = 0

while True:
    numbers = int(input("Enter the positive number: "))


    if numbers == 0:
        break

    count = count + 1

print("Numbers entered: ", count)

# Challenge #10
# Write a program that
    # Continuously asks for numbers.
    # Stops when the user enters 0.
    # Counts only the even numbers entered.
    # Prints the final count after the loop.

count = 0

while True:
    numbers = int(input("Enter your number"))

    if numbers == 0:
        break

    if numbers % 2 == 0:
        count = count + 1

print("Even number entered: ", count)

# Challenge #11
# Write a program that
    # Continuously asks for numbers.
    # Stops when the user enters 0.
    # Counts how many even numbers were entered.
    # Counts how many odd numbers were entered.
    # Prints both totals after the loop.

even_count = 0
odd_count = 0

while True:
    numbers = int(input("Enter the number: "))

    if numbers == 0:
        break

    if numbers % 2 == 0:
        even_count = even_count + 1

    else:
        odd_count = odd_count + 1

print("Even number entered: ", even_count)
print("Odd number entered: ", odd_count)

# Challenge #12
# Write a program that
    # Continuously asks for numbers.
    # Stops when the user enters 0.
    # Finds the largest nonzero number entered.
    # Prints the largest number after the loop.

largest = float('-inf')

while True:
    numbers = int(input("Enter the number: "))

    if numbers == 0:
        break

    if numbers > largest:
        largest = numbers

print("Largest Number: ", largest)


# Challenge #13
# Write a program that
    # Continuously asks for numbers.
    # Stops when the user enters 0.
    # Find the smallest nonzero number.
    # Prints it after the loop.
    #It must work with both positive and negative numbers.

smallest = float('inf')

while True:
    numbers = int(input("Enter the number: "))

    if numbers == 0:
        break

    if numbers < smallest:
        smallest = numbers

print("Smallest Number: ", smallest)

# Challenge #14
# Write a program that
    # Repeatedly asks for numbers.
    # Stops when the user enters 0.
    # Calculates the sum of all nonzero numbers.
    # Counts how many numbers were entered.
    # Calculates their average.
    # Prints the sum, count, and average after the loop.

total = 0
count = 0

while True:
    numbers = int(input("Enter the number: "))

    if numbers == 0:
        break

    total = total + numbers
    count = count + 1

average = total / count

print(total, count, average)

# Challenge #15
# Write a program that repeatedly accepts numbers and stops at 0.
    # It should count:
    # Positive numbers.
    # Negative numbers
    # Even numbers.
    # Odd numbers.


