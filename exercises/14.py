#True division and floor division

def true_floor_division(num1, num2):
  true_division = num1 / num2
  floor_division = num1 // num2
  return true_division, floor_division

num1 = float(input("Type a number: "))
num2 = float(input("Type another number: "))

true_division, floor_division = true_floor_division(num1, num2)

print(f"The floor division is {floor_division}")
print(f"The true division is {true_division}")