def remainder(num1, num2):
  result = num1 * num2
  if result % 2 == 0:
    return f"The result is {result} which is Even."
  return f"The result is {result} which is Odd."


num1 = int(input("Choose any number? "))
num2 = int(input("Choose another number? "))


print(remainder(num1, num2))