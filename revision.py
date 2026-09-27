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
'''

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




