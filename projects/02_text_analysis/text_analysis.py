# Mini Project #2
# Text Analysis Tool

sentence = input("Enter a sentence: ").lower()

words = sentence.split()

total_words = 0
total_character = 0

longest_word = ""
shortest_word = ""

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

print("Longest Word: ", longest_word)
print("Shortest Word: ", shortest_word)


print("Total Words: ", total_words)
print("Total Character: ", total_character)


