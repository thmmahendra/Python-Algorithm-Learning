# Mini Project #2
# Text Analysis Tool

sentence = input("Enter a sentence: ").lower()

words = sentence.split()

total_words = 0
total_character = 0

for word in words:
    total_words = total_words + 1
    total_character = total_character + len(word)

print("Total Words: ", total_words)
print("Total Character: ", total_character)

