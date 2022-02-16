N = 35
while N >= 31 or N < 0:
    N = input("Enter the root of number till which you want to print multiples of 2: ")
    N = int(N)
for i in range(1, N+1):
    print(2**i)
