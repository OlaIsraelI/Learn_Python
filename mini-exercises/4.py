#Converting string to int and float

def convert_string(user_input):
  as_float = float(user_input)

  as_int = int(as_float)

  return as_float, as_int

user_input = input("Enter a price in whole number: ").strip()

as_float, as_int = convert_string(user_input)

print(f"Original string {user_input}")
print(f"As Integer: {as_int}")
print(f"As float: {as_float}")