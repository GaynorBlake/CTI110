def days_in_feb(user_year):
    if user_year % 4 == 0 and (user_year % 100 != 0 or user_year % 400 == 0):
        return 29
    else:
        return 28


if __name__ == '__main__':
    year = int(input())
    days = days_in_feb(year)
    print("{} has {} days in February.".format(year, days))
