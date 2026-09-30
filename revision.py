# Review Challenge #1
# Find Largest and smallest numbers
'''
numbers = input("Enter the numbers: ").split()

largest = float('-inf')
smallest = float('inf')

for num in numbers:
    num = int(num)

    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest Number: ", largest)
print("Smallest Number: ", smallest)


# Review Challenge #2
# Find Second Largest Number

numbers = input("Enter the numbers: ").split()

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    num = int(num)

    if num > largest:
        second_largest = largest
        largest = num

    else:
        if num > second_largest and num != largest:
            second_largest = num

if second_largest == float('-inf'):
    print("No second largest distinct number.")

else:
    print("Second Largest Number: ", second_largest)

# Review Challenge #3
# Duplicate Value

numbers = input("Enter the numbers: ").split()

checked_numbers =[]
found_duplicate = False

for num in numbers:
    if num not in checked_numbers:
        count = 0

        for check in numbers:
            if num == check:
                count = count + 1

        if count > 1:
            print(num)
            found_duplicate = True

        checked_numbers.append(num)

if found_duplicate == False:
    print("No duplicate values")


# Review Challenge #4
# Reverse String

words = input("Enter a word: ")

reversed_words = ""

index = len(words) - 1

while index >= 0:
    reversed_words = reversed_words + words[index]
    index = index - 1

print(reversed_words)
'''

# Review Challenge #5
# Anagram Checker

first_word = input("Enter a first word: ").lower()
seond_word = input("Enter a second word: ").lower()

if len(first_word) != len(seond_word):
    are_anagrams = False

else:
    are_anagrams = True

    for character in first_word:
        count_first = 0
        count_second = 0

        for check in first_word:
            if character == check:
                count_first = count_first + 1

        for check in seond_word:
            if character == check:
                count_second = count_second + 1

        if count_first != count_second:
            are_anagrams = False
            break

if are_anagrams:
    print("Anagrams")

else:
    print("Not Anagrams")



        
















