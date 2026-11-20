#Floating point clean and quick formatting 

def add_float_numbers(a, b):
  add = a + b
  return add

a = float(input("Type a first decimal number (i.e. 2.5) "))
b = float(input("Type a second decimal number (i.e. 3.1) "))

add = add_float_numbers(a, b)
print(f"The quick formatting is {add}")
print(f"The clean formatting is {add:.2f}")
