import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
variants = [rock, paper, scissors]
choice = int(input("What do you Choose? Type 0 for Rock, 1 For Paper and 2 for Scissors:\n"))

if choice == 0 or choice == 1 or choice == 2:
  print(variants[choice])
  
  computer_choice = random.randint(0, 2)
  print("Computer chose:\n\n" + variants[computer_choice])

  if choice == computer_choice:
    print("It's a draw!")
  elif choice == 0 and computer_choice == 2:
    print("You win!")
  elif choice == 1 and computer_choice == 0:
    print("You win!")
  elif choice == 2 and computer_choice == 1:
    print("You win!")
  else:
    print("You lost!")

else:
    print("That's not a valid choice!")