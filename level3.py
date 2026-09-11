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

'''
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





