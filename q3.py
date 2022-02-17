year = 0
while len(str(year)) != 4:
    year = input("Enter a four digit number ")
    year = int(year)
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("Input is a leap year.")
else:
    print("Input is not a leap year.")