#Bill Splitter

def bill_splitter(bill, people):
  owning = bill / people
  return f"Each person owes {owning}."

total_bill_amount = float(input("What is the total amount? "))
number_of_people = int(input("How many people are splitting it? "))

print(bill_splitter(total_bill_amount, number_of_people))