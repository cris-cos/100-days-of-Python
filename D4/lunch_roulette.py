import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

people = len(names)
draw = random.randint(0, people-1)

print(f"The lucky bastard paying for lunch today is {names[draw]}")

#Jane, Millard, Angela, Lord Bananabread, Cocran