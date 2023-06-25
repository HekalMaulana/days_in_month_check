def is_leap(year):
    leap_year = True
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return leap_year
            else:
                leap_year = False
                return leap_year
        else:
            return leap_year
    else:
        leap_year = False
        return leap_year


def days_in_month( years, months):
    month = months - 1
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = is_leap(years)

    if leap_year == True:
        month_days[1] += 1
        return month_days[month]
    else:
        return month_days[month]



# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
