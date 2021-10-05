def tripler(func):
	"""
	A decorator that execute a function 3 times

	This function will take in another function and call such function 3 times

	Parameters
	----------
	function
			function to be executed 3 times
	Return
	------
	wrapper function
			A decorated version of the function being passed into the decorator
	"""
	def wrapper():
		func()
		func()
		func()
	return wrapper
@tripler
def my_func():
	print("I will be called 3 times")

my_func()
