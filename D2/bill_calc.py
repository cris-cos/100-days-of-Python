
print("Wellcome to the bill splitter!")
bill = float(input("What was the bill amount?\n$"))
tip = int(input("What is the tip percentage? (10, 12, 15, etc):\n"))
party = int(input("How many people are splitting the bill?\n"))

bill_with_tip = bill + (tip / 100 * bill)
party_bill = round((bill_with_tip / party), 2)

print(f"Each person should pay {party_bill}")

