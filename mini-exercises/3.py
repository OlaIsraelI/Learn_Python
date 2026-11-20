#Compound assignment 

def calculate_balance():

  balance = 10000
  print(f"\nThe amount in the account is {balance}")

  balance += 500
  print(f"\nThe user just deposited 500, final balance is {balance}")

  balance -= 250
  print(f"\nThe user just withdrew 250, final balance is {balance}")

  balance *= 1.1
  print(f"The user received a 10% bonus, fianl balance is {balance}")

  balance //= 2
  print(f"After splitting in halve, final balance is {balance}")

  return balance

print(calculate_balance())