# Review Challenge
# Find Largest and smallest numbers

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





