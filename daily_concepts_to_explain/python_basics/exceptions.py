# initialize the amount variable
amount = 10000

# check that You are eligible to
# purchase Dsa Self Paced or not
if amount > 2999:
    print("You are eligible to purchase Dsa Self Paced")

# initialize the amount variable
marks = 10000

# perform division with 0
a = marks / 0
print(a)

# Python program to handle simple runtime error
# Python 3

a = [1, 2, 3]
try:
    print("Second element = %d" % (a[1]))
    # Throws error since there are only 3 elements in array
    print("Fourth element = %d" % (a[3]))
except:
    print("An error occurred")


# Program to handle multiple errors with one
# except statement
# Python 3

def fun(_a):
    if _a < 4:
        # throws ZeroDivisionError for a = 3
        b = _a / (_a - 3)

    # throws NameError if a >= 4
    print("Value of b = ", b)


try:
    fun(3)
    fun(5)

# note that braces () are necessary here for
# multiple exceptions
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")


# Program to depict else clause with try-except
# Python 3
# Function which returns a/b
def a_by_b(_a, b):
    try:
        c = ((_a + b) / (_a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)


# Driver program to test above function
a_by_b(2.0, 3.0)
a_by_b(3.0, 3.0)

# Python program to demonstrate finally

# No exception raised in try block
try:
    k = 5 // 0  # raises divide by zero exception.
    print(k)

# handles zero division exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')

# Program to depict Raising Exception

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not
