print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price = 0

if size == "S":
  price = 15
elif size == "M":
  price = 20
elif size == "L":
  price = 25
else:
  print("No pizza it is")

if add_pepperoni == "Y" and size == "S":
  price += 2
elif add_pepperoni == "Y":
  price += 3
else:
  print("No extra pepperoni for you")

if extra_cheese == "Y":
  price += 3
else:
  print("No extra cheese for you")

print(f"Your pizza will cost {price} dollars")