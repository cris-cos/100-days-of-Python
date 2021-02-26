import random

draw = random.randint(0, 100)

if draw % 2 == 0:
  print("Heads!")
else:
  print("Tail!")