#Compound price with tax discount

def calulate_price (price, tax, discount):
  tax_amount = price * (tax / 100)
  total = price + tax_amount - discount
  return total

item_price = float(input("What is the price of the item? "))
tax_percentage = float(input("What is the tax percentage? "))
discount_amount = float(input("What is the discount amount? "))

total = calulate_price(item_price, tax_percentage, discount_amount)

print(f"The total price payable is {total}.")