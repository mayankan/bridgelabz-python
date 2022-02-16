import random
noOfTimes = 0
while noOfTimes < 1:
    noOfTimes = input("Enter the number of times to Flip Coin: ")
    noOfTimes = int(noOfTimes)
output = random.choices([0, 1], k=noOfTimes)
percentage = (sum(output)/noOfTimes)
print(percentage)