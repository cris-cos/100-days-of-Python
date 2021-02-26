print("Wellcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
  print("You can ride!")
  age = int(input("What's your age again?"))
  if age <= 5:
    print("5$")
  elif age <= 18:
    print("7$")
  else:
    print("12$")
else:
  print("Sorry, you got some growing up to do!")