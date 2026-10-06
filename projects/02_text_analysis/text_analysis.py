# Mini Project #2
# Text Analysis Tool
    # Total words + Total Characters
    # Longest + Shortest Word
    # Most + Least Frequent Word
    # Repeating + Non repeating word
    # Final Text Summary

sentence = input("Enter a sentence: ").lower()

words = sentence.split()
checked_words = []

total_words = 0
total_character = 0

longest_word = ""
shortest_word = ""

most_frequent = ""
least_frequent = ""

highest_count = 0
lowest_count = float('inf')

repeating_words = []
non_repeating_words = []

for word in words:
    total_words = total_words + 1
    total_character = total_character + len(word)

    if len(word) > len(longest_word):
        longest_word = word

    if shortest_word == "":
        shortest_word = word

    else:
        if len(word) < len(shortest_word):
            shortest_word = word

average_word_length = total_character / total_words

for word in words:
    if word not in checked_words:
        count = 0
        
        for check in words:
            if word == check:
                count = count + 1

        if count > highest_count:
            highest_count = count
            most_frequent = word

        if count < lowest_count:
            lowest_count = count
            least_frequent = word

        checked_words.append(word)

        if count > 1:
            repeating_words.append(word)

        if count == 1:
            non_repeating_words.append(word)

print("\n-----TEXT ANALYSIS------")

print("\nLongest Word: ", longest_word)
print("Shortest Word: ", shortest_word)
print("Average Word Length: ", average_word_length)

print("Total Words: ", total_words)
print("Total Character: ", total_character)

print("Most Frequent Word: ", most_frequent)
print("Frequency: ", highest_count)

print("Least Frequent Word: ", least_frequent)
print("Frequency: ", lowest_count)

if not repeating_words:
    print("No repeating words.")

else:
    print("\nRepeating word: ")

    for word in repeating_words:
        print(word)

if not non_repeating_words:
    print("No non-repeating words.")

else:
    print("\nNon repeating word: ")

    for word in non_repeating_words:
        print(word)

