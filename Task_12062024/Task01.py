# Program to check whether the given year is a leap year

year = int(input("Enter the Year: "))
if year % 4 == 0 or year % 400 == 0:
    print("This year is a leap year")
elif year % 100 != 0:
    print("This year is not a leap year")
else:
    print("Invalid Entry")
