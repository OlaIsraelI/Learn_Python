#Mini Warm-up Exercise
#1. Dictionary: Month Name to Number
import calendar
from datetime import date

MONTH = {"january":1, "febuary":2, "march":3, "april":4, "may":5, "june":6, "july":7, "august":8, "september":9, "october": 10, "november":11, "december":12}

birth_day = int(input("What is the day of your birth (1 - 31)? ").strip())
birth_month = input("What is your birth month (name or 1-12)? ").strip().lower()
birth_year = int(input("What is your birth year (e.g., 1996)? ").strip())

if birth_month in MONTH:
  birth_month = MONTH[birth_month]
else:
  birth_month = int(birth_month)

  today = date.today()

  curr_year, curr_month, curr_day = today.year, today.month, today.day

  years = curr_year - birth_year
  months = curr_month - birth_month
  day = curr_day - birth_day
