row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

coordinates = position.split(" ")
X = int(coordinates[1]) - 1
Y = int(coordinates[0]) - 1

map[X][Y] = "💰"

print(f"{row1}\n{row2}\n{row3}")