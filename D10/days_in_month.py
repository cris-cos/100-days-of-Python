def is_leap(year):
    if year % 4 == 0:
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
        else:
            leap = True
    else:
        leap = False
    return leap
      
def days_in_month(year, month):
    if is_leap(year) == True:
        passmonth_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        passmonth_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return passmonth_days[month - 1]
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)