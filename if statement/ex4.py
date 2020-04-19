year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 40 == 0:
    print("%d is leap year"%(year))
else:
    print("%d is not leap year"%(year))