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

# Challenge #8
# Find the longest word

words = input("Enter the words: ")

current_word = ""
longest_word = ""

for char in words:

    if char.isalpha():
        current_word = current_word + char

    else:
        if len(current_word) > len(longest_word):
            longest_word = current_word

        current_word = ""

if len(current_word) > len(longest_word):
    longest_word = current_word

print("Longest Words: ", longest_word)

# Challenge #9
# Reverse each word

words = input("Enter the words: ")

current_word = ""
reversed_word = ""
result = ""

for char in words:

    if char.isalpha():
        current_word = current_word + char

    else:
        index = len(current_word) - 1

        while index >= 0:
            reversed_word = reversed_word + current_word[index]
            index = index - 1

        
        result = result + reversed_word + char          
          
        current_word = ""
        reversed_word = ""  


index = len(current_word) - 1

while index >= 0:
    reversed_word = reversed_word + current_word[index]
    index = index - 1

        
result = result + reversed_word 

print("Output: ", result)

# Challenge #10
# Reverse Word Order

words = input("Enter the words: ")

current_word = ""
reversed_word = ""
result = ""
word_list = []

for char in words:
    if char.isalpha():
        current_word = current_word + char
        
    else:
        word_list.append(current_word)
        index = len(word_list) - 1
        current_word = ""
   
word_list.append(current_word)

index = len(word_list) - 1

while index >= 0:
    reversed_word = reversed_word + word_list[index]

    if index > 0:
        reversed_word = reversed_word + " "
        
    index = index - 1

print("Output: ", reversed_word)

# Challenge #11
# Counts words by lengths

words = input("Enter the words: ")

count = 0
current_word = ""

for char in words:
    if char.isalpha():
        current_word = current_word + char

    else:
        if len(current_word) > 3:
            count = count + 1

        current_word = ""

if len(current_word) > 3:
    count = count + 1
            
print("Output: ", count)

# Challenge #12
# Count short words

words = input("Enter the words: ")

short_count = 0
short_word = ""

for char in words:
    if char.isalpha():
        short_word = short_word + char

    else:
        if len(short_word) < 4:
            short_count = short_count + 1

        short_word = ""

if len(short_word) < 4:
    short_count = short_count + 1

print("Output: ", short_count)

# Challenge #13
# Find the shortest word

words = input("Enter the words: ")

current_word = ""
shortest_word = ""

for char in words:
    if char.isalpha():
        current_word = current_word + char

    else:
        if shortest_word == "":
            shortest_word = current_word

        elif len(current_word) < len(shortest_word):
            shortest_word = current_word

        current_word = ""

if current_word != "" and len(current_word) < len(shortest_word):
    shortest_word = current_word

print("Shortest words :", shortest_word)

# Challenge #14
# Find the Longest Word Length

words = input("Enter the words: ")

current_word = ""
longest_length = 0

for char in words:
    if char.isalpha():
        current_word = current_word + char

    else:
        if len(current_word) > longest_length:
            longest_length = len(current_word) 

        current_word = ""

if len(current_word) > longest_length:
    longest_length = len(current_word)

print("Output: ", longest_length)

# Challenge #15
# Count words starting with a specific letter

words = input("Enter the words: ")
target = input("Enter the targeted word: ")

current_word = ""
count = 0

for char in words:
    if char.isalpha():
        current_word = current_word + char

    else:
        if current_word != "":
            if current_word[0].lower() == target.lower():
                count = count + 1

            current_word = ""

if current_word != "":
    if current_word[0].lower() == target.lower():
        count = count + 1

print("Output: ", count)

# Challenge #16
# Count words ending with a specific lettwer

words = input("Enter the word: ")
target = input("Enter the target letter: ")

current_word = ""
count = 0

for char in words:
    if char.isalpha():
        current_word = current_word + char

    else:
        if current_word != "":
            if current_word[len(current_word) - 1].lower() == target.lower():
                count = count + 1

            current_word = ""

if current_word != "":
    if current_word[len(current_word) - 1].lower() == target.lower():
        count = count + 1

print("Output: ", count)

# Challenge #17
# Count words with repeated characters
    # Part #1 
    # Duplicate Detection

current_word = input("Enter the words: ")
seen = ""
has_repeat = False

for letter in current_word:
    if letter in seen:
        has_repeat = True
        break

    else:
        seen = seen + letter
    
print("Output: ", has_repeat) 

    # Part #2
    # Combine and count the repeated characters

words = input("Enter the words: ")

current_word = ""
count = 0

for char in words:
    if char.isalpha():
        current_word = current_word + char

    else:
        if current_word != "":
            seen = ""

            for letter in current_word:
                if letter in seen:
                    count = count + 1
                    break

                else:
                    seen = seen + letter

            current_word = ""

if current_word != "":
     seen = ""

     for letter in current_word:
          if letter in seen:
               count = count + 1
               break
          else:
               seen = seen + letter

print("Output: ", count) 

# Challenge #18
# Find the first repeated character

current_word = input("Enter the words: ")

seen = ""
repeat_char = ""

for letter in current_word:
    if letter in seen:
        repeat_char = letter
        break

    else:
        seen = seen + letter

if repeat_char != "":
    print("Output: ", repeat_char)

else:
    print("No repeated character")

# Challenge #19
# Find the first non repeated character

current_word = input("Enter the word: ")

unique_char = ""

for letter in current_word:
    count = 0

    for check in current_word:
        if letter == check:
            count = count + 1

    if count == 1:
        unique_char = letter
        break

if unique_char != "":
    print("Output: ", unique_char)

else:
    print("No unique character")

# Challenge #20
# Find the most frequent character

current_word = input("Enter the words: ")

most_char = ""
most_count = 0

for letter in current_word:
    count = 0

    for check in current_word:
        if letter == check:
            count = count + 1

    if count > most_count:
        most_count = count
        most_char = letter
        

if most_char != "":
    print("Output: ", most_char)

else:
    print("No most character found.")

# Challenge #21
# Find the least frequent character

current_word = input("Enter the words: ")

least_char = ""
least_count = float('inf')

for letter in current_word:
    count = 0

    for check in current_word:
        if letter == check:
            count = count + 1

    if count < least_count:
        least_count = count
        least_char = letter

if least_char != "":
    print("Output: ", least_char)

else:
    print("No least character found")

# Challenge #22
# Write a program that check if a string is a Palindrome

current_word = input("Enter the word: ").lower()

is_palindrome = True

left = 0
right = len(current_word) - 1


while left < right:
    if current_word[left] != current_word[right]:
        is_palindrome = False
        break

    left = left + 1
    right = right - 1

if is_palindrome:
    print("Palindrome")

else:
    print("Not Palindrome")

# Challenge #23 
# Anagram Checker
    # Two words are anagrams when they contain the same characters with the same frequency, but possibly in a different order

first_words = input("Enter the words: ").lower()
second_words = input("Enter the words: ").lower()


if len(first_words) != len(second_words):
    are_anagrams = False

else:
    are_anagrams = True

    for character in first_words:
        count_first = 0
        count_second = 0

        for check in first_words:
            if character == check:
                count_first = count_first + 1

        for check in second_words:
            if character == check:
                count_second = count_second + 1

        if count_first != count_second:
            are_anagrams = False
            break

if are_anagrams:
    print("Anagrams")

else:
    print("Not Anagrams")

# Challenge #24 Word Frequency
# Count how many times each word appears

sentence = input("Enter a sentence: ").lower()

words = sentence.split()
checked_words = []

for word in words:
    if word not in checked_words:
        count = 0

        for check in words:
            if word == check:
                count = count + 1

        print(word, count)

        checked_words.append(word)

# Challenge #25
# Most frequent words

sentence = input("Enter a sentence: ").lower()

words = sentence.split()
checked_words = []
frequent_word = ""
highest_count = 0


for word in words:
    if word not in checked_words:
        count = 0

        for check in words:
            if word == check:
                count = count + 1
        if count > highest_count:
            highest_count = count
            frequent_word = word

        checked_words.append(word)

print("Most Frequent Words: ", frequent_word)
print("Frequency: ", highest_count)
'''

# Challenge #26
# Least frequent words

sentence = input("Enter a sentence: ").lower()

words = sentence.split()
checked_words = []

least_frequent_word = ""
least_count = float('inf')

for word in words:
    if word not in checked_words:
        count = 0

        for check in words:
            if word == check:
                count = count + 1

        if count < least_count:
            least_count = count
            least_frequent_word = word

        checked_words.append(word)

print("Least Frequent Words: ", least_frequent_word)
print("Frequency: ", least_count)























