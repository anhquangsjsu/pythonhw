import time

def calculate_time(func):
	"""
	A decorator that print out the total execution time of a function

	This function will take in another function and print out the total 
	seconds the function executed

	Parameters
	----------
	function
			function to be executed and execution time of this function will be calculated
	Return
	------
	wrapper function
			A decorated version of the function being passed into the decorator
	"""
	def wrapper():
		"""
		A wrapper function that call the function being passed in to the decorator

		this function will calculate the time in between the execution of the passed function 
		and print out the total time in seconds to the user
		"""
		start_time = time.time()
		func()
		end_time = round(time.time() - start_time)
		print(f"Total time {end_time}")
	return wrapper

@calculate_time
def some_func():
	print("some function")

some_func()
