# Python program to illustrate
# *args for variable number of arguments
def my_fun(*argv):
	for arg in argv:
		print (arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# Python program to illustrate
# *args with first extra argument
def my_fun(arg1, *argv):
	print ("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)


my_fun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# Python program to illustrate
# *kwargs for variable number of keyword arguments


def myFun(**kwargs):
	for key, value in kwargs.items():
		print ("%s == %s" %(key, value))


# Driver code
myFun(first ='Geeks', mid ='for', last='Geeks')

# Python program to illustrate **kwargs for
# variable number of keyword arguments with
# one extra argument.


def myFun(arg1, **kwargs):
	for key, value in kwargs.items():
		print ("%s == %s" %(key, value))


# Driver code
myFun("Hi", first ='Geeks', mid ='for', last='Geeks')


def myFun(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(**kwargs)


def myFun(*args,**kwargs):
	print("args: ", args)
	print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")

