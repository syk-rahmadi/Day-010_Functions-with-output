def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")


# TODO: Add more code here 👇
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        if is_leap(year):
            print("29 days")
        else:
            print("28 days")
    else:
        return(month_days[month - 1])


# 🚨 Do NOT change any of the code below
year = int(input("Give your year number!"))  # Enter a year
month = int(input("Give your month number!"))  # Enter a month
days = days_in_month(year, month)
print(days)

