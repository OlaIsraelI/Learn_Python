#3. Inspecting Data Types
name = input("Enter a new name: ")
age = int(input("Enter your age: "))
speed_limit = float(input("Enter the Speed Limit: "))
is_true = input("Are you a student? (yes/no): ").lower() == "yes"

print(type(name))
print(type(age))
print(type(speed_limit))
print(type(is_true))