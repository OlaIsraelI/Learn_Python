#Power and Square root calculator

def calculate_power_and_function (base, exponent):
  power = base ** exponent
  square_root = base ** 0.5
  return power, square_root

base_number = float(input("Type a base number: "))
exponent = float(input("Type an exponent: "))

power_result, square_root_result = calculate_power_and_function(base_number, exponent)

print(f"The power is {power_result}")
print(f"The square root is {square_root_result}")