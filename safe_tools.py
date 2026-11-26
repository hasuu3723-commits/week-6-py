
# Python Week 6 Assignment - Safe Tools

# Function 1: Safely divide two numbers
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


# Function 2: Safely convert text into a whole number
def safe_number(text):
    try:
        return int(text)
    except ValueError:
        return "Not a number"


# Function 3: Safely get a value from a dictionary
def get_field(learner, key):
    try:
        return learner[key]
    except KeyError:
        return "Field not found"


# Test the functions
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_number("42"))
print(safe_number("abc"))

learner = {"name": "Amina", "score": 82}
print(get_field(learner, "score"))
print(get_field(learner, "email"))
