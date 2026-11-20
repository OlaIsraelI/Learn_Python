#Compound price with tax discount

def calulate_price (price, tax, discount):
  total = price + tax - discount
  return total

item_price = float(input("What is the price of the item? "))
tax_percentage = float(input("What is the tax percentage? "))
discount_amount = float(input("What is the discount amount? "))

total = calulate_price(item_price, tax_percentage, discount_amount)

print(f"The total amount payable is {total}.")