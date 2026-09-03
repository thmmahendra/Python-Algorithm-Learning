#Write a Python program that asks the user to enter a number and determines whether the number is: Positive or Negative

number = int(input("Enter the number:"))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("0")
