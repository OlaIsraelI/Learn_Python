#10 Exercises to cover this concept fully

#1. The favourite colour statement
# favourite_colour = "blue"
# print(f"My favourite colour is {favourite_colour}")

#2. Working with multiple data types( string, int, float, bool)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height_meters = float(input("Enter your height: "))
student_input = input("Are you a student? (yes/no): ")
is_student = student_input.lower() == "yes"

print("\n--- Here is the data we collected ---")
print(name)
print(age)
print(height_meters)
print(is_student)

print(f"\nHi {name} how are you? you are {age} years old, and you are {height_meters} tall, and it is {is_student} that you are a student.")