print("Wellcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

price = 0

if height >= 120:
  print("You can ride!")
  
  age = int(input("What's your age again?"))
  if age <= 5:
    price = 5
  elif age <= 18:
    price = 7
  # midlife crisis means free rollercoasters
  elif age >= 45 and age <= 55:
    price = 0
  else:
    price = 12
  
  photo = input("Do you want a photo? Y or N")
  if photo == "Y":
    price += 3
  
  print(f"Your ticket will cost {price}$")

else:
  print("Sorry, you got some growing up to do!")