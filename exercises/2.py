#2. Working with multiple data types( string, int, float, bool)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
height_meters = float(input("Enter your height: "))
student_input = input("Are you a student? (yes/no): ")
is_student = student_input.lower() == "yes"

print("\n--- Here is the data we collected ---")
print(type(name))
print(type(age))
print(type(height_meters))
print(type(is_student))

print(f"\nHi {name} how are you? you are {age} years old, and you are {height_meters} tall, and it is {is_student} that you are a student.")