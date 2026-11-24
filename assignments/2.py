#Mini Warm-up Exercise
#2. Days in a Given Month & Year
# Helper function to check a given year


#A function to check if year is a leap year
def is_leap_year (year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return True
  else:
    return False

#A function to check the number of days in a month
def days_in_month (month, year):
  if month in [1, 3, 5, 7, 8, 10, 12]:
    return 31

  elif month in [4, 6, 9, 11]:
    return 30

  elif month == 2:
    if is_leap_year(year):
      return 29
    else: 
      return 28 
  else:
    return "Invalid Month"

month = int(input("In what month were you born? (1-12) "))
year = int(input("What year were you born? "))

days = days_in_month(month, year)
print(f"Month {month} in year {year} has {days} days")