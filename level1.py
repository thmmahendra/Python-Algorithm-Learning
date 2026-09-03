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


