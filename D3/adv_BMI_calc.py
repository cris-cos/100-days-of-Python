height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = int(weight) / (float(height) ** 2)
bmi = round(bmi, 2)

if bmi < 18.5:
  print(f"Your BMI is {bmi}; You are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}; This is your ideal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}; You are slightly overweight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}; You are classified as obese.")
else:
  print(f"Your BMI is {bmi}; You are clinically (or morbidly) obese.")