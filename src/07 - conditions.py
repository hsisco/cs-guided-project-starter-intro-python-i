"""
Conditions
"""

# 1. Comparing or evaluating expressions
x = 2
print(x == 2)  # prints out True
print(x == 3)  # prints out False
print(x < 3)  # prints out True

# 2. "and" & "or"
name = "Sean"
age = 31
if name == "Matt" and age == 31:
    print("Your name is Matt, and you are also 31 years old.")

if name == "Matt" or name == "Sean":
    print("Your name is either Matt or Sean.")

# if person and person["name"]:
#       ...
# # First check if the person object exists before checking if the object contains the desired data

# 3. "in"
my_name = "Beej"
names = ["Matt", "Sean"]
if my_name in names:
    print("Your name is either Matt or Sean.")

# 4. "if", "elif", "else"
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True:  # else if
    print("another statement is True")
    pass
else:
    # do another thing
    print("from inside else")
    pass

# 5. "is" matches instances and not values
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False

# 6. "not" inverts a boolean
print(not False)  # Prints out True
print((not False) == (False))  # Prints out False


"""
YOU DO
3 minute timer
"""
# Modify the supplied code so that all of the statements evaluate to True
# change this code
number = 20
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

print(bool(number > 15))
# number = 15+

print(bool(first_array))
# first_array exists, so the bool is True

print(len(second_array) == 2)
# Make second_array have 2 indexes

print(len(first_array) + len(second_array) == 5)
# second_array has 2, so first_array must have 3 indexes

print(first_array and first_array[0] == 1)
# first_array exists, AND the 0 index reads 1

print(not second_number)
# second_number must be Falsey (0) so the 'NOT second_number' can print True