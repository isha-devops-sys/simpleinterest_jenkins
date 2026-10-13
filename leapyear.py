import sys
def leapyear(year):
    if (year %4 == 0):
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


if _name_ == "_main_":
    year = int(sys.argv[1])
    leapyear(year)
