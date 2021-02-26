number = float(input("Which number do you want to check? "))

if number % 2 == 0:
  print("This is an even number.")
elif number % 2 == 1:
  print("This is an odd number.")
else:
  print("The input was not an integer.")