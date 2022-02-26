# Python program to illustrate
# while loop
count = 0
while count < 3:
    count = count + 1
    print("Hello Geek")

condition = True

if condition:
    pass
# execute these statements
else:
    pass
# execute these statements

condition = False

while condition:
    pass
# execute these statements
else:
    pass
# execute these statements

# Python program to illustrate
# combining else with while
count = 0
while count < 3:
    count = count + 1
    print("Hello Geek")
else:
    print("In Else Block")

# Python program to illustrate
# Single statement while block
count = 0
while count == 0: print("Hello Geek")

# Python program to illustrate
# Iterating over range 0 to n-1

n = 4
for i in range(0, n):
    print(i)

# Python program to illustrate
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
	print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
	print(i)

# Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s:
	print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
	print("%s %d" % (i, d[i]))

# Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
	print(i),

# Python program to illustrate
# Iterating by index

list_vals = ["geeks", "for", "geeks"]
for index in range(len(list_vals)):
	print(list_vals[index])

# Python program to illustrate
# combining else with for

list_vals = ["geeks", "for", "geeks"]
for index in range(len(list_vals)):
	print(list_vals[index])
else:
	print("Inside Else Block")


# Python program to illustrate
# nested for loops in Python
from __future__ import print_function
for i in range(1, 5):
	for j in range(i):
		print(i, end=' ')
	print()


# Prints all letters except 'e' and 's'
for letter in 'geeksforgeeks':
	if letter == 'e' or letter == 's':
		continue
	print('Current Letter :', letter)
	var = 10

for letter in 'geeksforgeeks':

	# break the loop as soon it sees 'e'
	# or 's'
	if letter == 'e' or letter == 's':
		break

print('Current Letter :', letter)

# An empty loop
for letter in 'geeksforgeeks':
	pass
print('Last Letter :', letter)


# A simple for loop example

fruits = ["apple", "orange", "kiwi"]

for fruit in fruits:
	print(fruit)


fruits = ["apple", "orange", "kiwi"]

# Creating an iterator object
# from that iterable i.e fruits
iter_obj = iter(fruits)

# Infinite while loop
while True:
	try:
		# getting the next item
		fruit = next(iter_obj)
		print(fruit)
	except StopIteration:
		# if StopIteration is raised,
		# break from loop
		break



