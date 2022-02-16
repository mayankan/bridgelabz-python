import random
noOfTimes = 0
while int(noOfTimes) < 1:
    noOfTimes = input("Enter the number of times to Flip Coin ")
output = random.choices([0, 1], k=int(noOfTimes))
percentage = (sum(output)/int(noOfTimes))
print(percentage)