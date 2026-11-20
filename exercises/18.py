#Minutes to hours and remaining minutes

def minutes_to_hours(minutes):
  total_hours = minutes // 60 
  total_minutes = minutes % 60
  return total_hours, total_minutes

hours = int(input("How many minutes did you use? "))

total_hours, total_minutes = minutes_to_hours(hours)

print(f"You used a total of {total_hours} hours, and {total_minutes} minutes.")