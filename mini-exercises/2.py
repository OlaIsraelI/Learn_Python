#Negative floor division check

def negative_floor_division(num, divisor):
  result1 = num / divisor
  result2 = num // divisor
  return result1, result2

negative_number = int(input("Enter a negtive whole number: "))
positive_divisor = int(input("Enter a positive divisor: "))

result1, result2 = negative_floor_division(negative_number, positive_divisor)

print(result1)
print(result2)