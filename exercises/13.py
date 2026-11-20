#Multiplying an integer by a constant

def day_and_months(age):
  days_alive = age * 365
  months_alive = age * 12

  return days_alive, months_alive

age = int(input("How old are you? "))

days_alive, months_alive = day_and_months(age)

print(f"You have lived for {days_alive} days on the earth.")
print(f"You have lived for {months_alive} months on the earth.")
