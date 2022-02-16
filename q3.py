year = 0
while len(str(year)) != 4:
    year = input("Enter a four digit number ")
print("Input is a leap year.") if int(year) % 4 == 0 else print("Input is not a leap year.")

