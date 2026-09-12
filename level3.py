# Challenge #1
# Write a program that:

    # Gets a word from the user.
    # Traverses the string.
    # Counts the characters manually.
    # Prints the final count.
'''
words = input("Enter the words: ")

char_count = 0

for char in words:
    char_count = char_count + 1

print("You entered: ", words,
      "\n Number of Characters: ", char_count)


# Challenge #2
# Write a program that:

    # Asks for a word.
    # Asks for a character.
    # Counts how many times that character appears.
    # Print the final result.

words = input("Enter a words: ")

character = input("Enter a character: ")

char_count = 0

for char in words:
    if char == character:
        char_count = char_count + 1

print(character, "appeared: ", char_count, "times")


# Challenge #3
# Reverse String
# Create a program that:

    # Gets a word from the user.
    # Starts at the last index.
    # Moves backward.
    # Builds a new string.
    # Prints the reversed string.

    # You can use a while loop for this challenge.

words = input("Enter a words: ")

reversed_words = ""

index = len(words) -1

while index >= 0:
    reversed_words = reversed_words + words[index]
    index = index - 1

print(reversed_words)

# Challenge #4
# Write a program that asks the user for a word or sentence and counts how many vowels it contains.

words = input("Enter the words: ")

char_count = 0

for char in words:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        char_count = char_count + 1

print("Vowels: ", char_count)

# Challenge #5
# Count Consonants

words = input("Enter the words: ")

char_count = 0

for char in words:
    if char.isalpha() and char != "a" and char != "e" and char != "i" and char != "o" and char != "u":
            char_count = char_count + 1

print("Consonants Count: ", char_count)

# Challenge #6
# Count Vowels and Consonants

words = input("Enter the words: ")

vowels_count = 0
consonants_count = 0

for char in words:

    if char.isalpha():

        if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
            vowels_count = vowels_count + 1
        else:
            consonants_count = consonants_count + 1

print("Vowels count: ", vowels_count)
print("Consonants Counts: ", consonants_count)
'''
# Challenge #7
# Count how many words it contains

words = input("Enter the words: ")

word_count = 0
in_word = False

for char in words:
    if char.isalpha():

        if not in_word:
            word_count = word_count + 1
            in_word = True

    else:
        in_word = False

print(word_count)
    


