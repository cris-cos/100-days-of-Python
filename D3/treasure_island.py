print("Wellcome to trasure island. Your mission is to find my treasure.\n")
direction = input("Wich way do you want to go, right or left?\n")

if direction.lower() == "left":
  transport = input("You reached the ocean. What will you do, swim or wait for a boat?\n")
  if transport.lower() == "wait":
    color = input("You took the boat and reached the island. You see 3 doors, do you open red blue or yellow?\n")
    if color.lower() == "yellow":
      print("You found the treasure!\n")
    else:
      print("You died opening the door.\n")
  elif transport.lower() == "swim":
    print("You managed to drown in water 2 inch deep.\n")
  else:
    print("You did not choose a valid option and fell off the map.\n")
elif direction.lower() == "right":
  print("You fell off the map.\n")
else:
  print("You did not choose a valid option and fell off the map.\n")