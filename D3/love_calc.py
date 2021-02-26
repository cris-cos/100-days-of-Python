print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

stringy = name1 + name2
stringy = stringy.lower()

t = int(stringy.count("t"))
r = int(stringy.count("r"))
u = int(stringy.count("u"))
e = int(stringy.count("e"))
digit1 = t + r + u + e
print(digit1)

l = int(stringy.count("l"))
o = int(stringy.count("o"))
v = int(stringy.count("v"))
digit2 = l + o + v + e
print(digit2)

score = int(str(digit1) + str(digit2))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")