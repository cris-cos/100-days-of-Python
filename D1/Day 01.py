print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("\n\nDay 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")

print ("\n\nHello" + " " + "Angela\n\n")

print("Day 1 - String Manipulation")
print("String Concatenation is done with the + sign.")
print("e.g. print('Hello ' + 'world')")
print("New lines can be created with a backslash and n (\\n)\n\n")

print("Hello " + input("What is your name?\n") + "!\n\n")

print(str(len(input("What is your name?\n"))) + "\n\n")

a = input("a: ")
b = input("b: ")
c = b
b = a
a = c
print("a: " + a)
print("b: " + b)

#1. Create a greeting for your program.
print("Welcome to the band name generator!\n")
#2. Ask the user for the city that they grew up in.
city = input("What's the name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet = input("What's the name of your first pet?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Here is the name of your future band: \n" + pet + " de la " + city + "\n\n")