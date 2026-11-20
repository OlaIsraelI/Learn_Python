#Change the denomination breakdown

def break_number_into_units(number):
  thousands = number // 1000
  remainder = number % 1000
  five_hundreds = remainder // 500
  remainder1 = remainder % 500
  hundred = remainder1 // 100
  left_over = remainder1 % 100

  return thousands, five_hundreds, hundred, left_over

number = int(input("Type a number: "))

thousand, five_hundreds, hundred, left_over = break_number_into_units(number)

print(f"The original amount is {number}")
print(f"The thousand remaining is {thousand}")
print(f"The five hundred remaining is {five_hundreds}")
print(f"The hundred remaining is {hundred}")
print(f"The leftover is {left_over}")