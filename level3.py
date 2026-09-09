# Challenge #1
# Write a program that:

    # Gets a word from the user.
    # Traverses the string.
    # Counts the characters manually.
    # Prints the final count.

words = input("Enter the words: ")

char_count = 0

for char in words:
    char_count = char_count + 1

print("You entered: ", words,
      "\nNumber of Characters: ", char_count)


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


