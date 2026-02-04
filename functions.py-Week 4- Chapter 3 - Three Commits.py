# IMPORT STATEMENTS
# (None)

# FUNCTION DEFINITIONS
def print_bio(name, age, goal):
    # 2. Inside the function, use string multiplication (*) for a border line.
    print("*" * 25)
    # 3. Print the bio details using the parameter names.
    print("Name: " + name + " Age: " + str(age) + " Goal: " + goal)
    # 2. Inside the function, use string multiplication (*) for a border line.
    print("*" * 25)

# PROGRAM LOGIC
print_bio("Brittany Curry", 29, "Learn Python")
print_bio("Robin Williams", 63, "Make people laugh.")
print_bio("Leroy Gibbs", 67, "Solve naval crimes.")