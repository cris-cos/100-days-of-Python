
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

age_days = int(age) * 365
age_90 = 90 * 365

days_left = age_90 - age_days
weeks_left = int(days_left / 7)
months_left = (90 - int(age)) * 12

message = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."
print(message)
