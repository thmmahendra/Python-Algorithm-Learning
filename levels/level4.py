# Challenge #1
# Creating Your First Dictionary
'''
student = {
    "name": "Mahendra",
    "age": 25,
    "score": 90
}

print(student)

# Challenge #2
# Accessing Dictionary Values

student = {
    "name": "Mahendra",
    "age": 25,
    "score": 90
}

print("Name: ", student["name"])
print("Age: ", student["age"])
print("Score: ", student["score"])

# Challenge #3
# Adding a New Key-value Pair

student = {
    "name": "Mahendra",
    "age": 25,
    "score": 90
}

student["city"] = "Kathmandu"

print(student)

# Challenge #4
# Updating an Existing Value

student = {
    "name": "Mahendra",
    "age": 25,
    "score": 90,
    "city": "Kathmandu"
}

student["score"] = 95

print(student)

# Challenge #5
# Removing a Key-value Pair

student = {
    "name": "Mahendra",
    "age": 25,
    "score": 90,
    "city": "Kathmandu"
}

del student["city"]

print(student)
'''

# Challenge #6
# Checking Whether a Key exists

student = {
    "name": "Mahendra",
    "age": 25,
    "score": 90
}

if "city" in student:
    print("City Exists")

else:
    print("City does not exists")
