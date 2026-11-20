def operator_precedence(a, b, c):
  calculate = a + b * c ** 2
  precedence = ((a + b) * c) ** 2
  return calculate, precedence

a = int(input("Type a first number: "))
b = int(input("Type a second number: "))
c = int(input("Type a third number: "))

calculate, precedence = operator_precedence(a, b, c)

print(calculate)
print(precedence)