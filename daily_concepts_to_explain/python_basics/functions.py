# A simple Python function

def fun():
    print("Welcome to GFG")


# Driver code to call a function
fun()


# A simple Python function to check
# whether x is even or odd


def even_odd(x):
    if x % 2 == 0:
        print("even")
    else:
        print("odd")


# Driver code to call the function
even_odd(2)
even_odd(3)


# Python program to demonstrate
# default arguments


def my_fun(x, y=50):
    print("x: ", x)
    print("y: ", y)


# Driver code (We call myFun() with only
# argument)
my_fun(10)


# Python program to demonstrate Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)


# Keyword arguments
student(firstname='Geeks', lastname='Practice')
student(lastname='Practice', firstname='Geeks')


# Python program to illustrate
# *args for variable number of arguments


def my_fun(*argv):
    for arg in argv:
        print(arg)


my_fun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# Python program to illustrate
# *kwargs for variable number of keyword arguments


def my_fun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
my_fun(first='Geeks', mid='for', last='Geeks')


# A simple Python function to check
# whether x is even or odd


def even_odd(x):
    """Function to check if the number is even or odd"""

    if x % 2 == 0:
        print("even")
    else:
        print("odd")


# Driver code to call the function
print(even_odd.__doc__)


def square_value(num):
    """This function returns the square value of the entered number"""
    return num ** 2


print(square_value(2))
print(square_value(-4))


# Here x is a new reference to same list lst
def my_fun(x):
    x[0] = 20


# Driver Code (Note that lst is modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
my_fun(lst)
print(lst)


def my_fun(x):
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = [20, 30, 40]


# Driver Code (Note that lst is not modified
# after function call.)
lst = [10, 11, 12, 13, 14, 15]
my_fun(lst)
print(lst)


def my_fun(x):
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = [20, 30, 40]


# Driver Code (Note that lst is not modified
# after function call.
lst = [10, 11, 12, 13, 14, 15]
my_fun(lst)
print(lst)


def my_fun(x):
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = 20


# Driver Code (Note that lst is not modified
# after function call.
x = 10
my_fun(x)
print(x)


def swap(x, y):
    temp = x
    x = y
    y = temp


# Driver code
x = 2
y = 3
swap(x, y)
print(x)
print(y)


# Python code to illustrate the cube of a number
# using lambda function


def cube(x): return x * x * x


cube_v2 = lambda x: x * x * x

print(cube(7))
print(cube_v2(7))


# Python program to
# demonstrate accessing of
# variables of nested functions

def f1():
    s = 'I love GeeksforGeeks'

    def f2():
        print(s)

    f2()


# Driver's code
f1()

