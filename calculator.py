def calculator(num1, num2, op):
	"""
    combine two numbers by a operator

    This function take in two numbers and an operator string. It then check the operator to perform equivalent operations on the two number.
	For the case of division ( / and //) the function also check if the divider is 0 or not 

	Parameters
	----------
	num1:	float
			the first number of the operation

	num2:	float
			the second number of the operaiont

	op:		String
			the operator string determine the operation type

	Returns
	-------
	float
			the result operation of the two numbers based on the operator
	boolean
			the False value is return if the operation is not valid

	Example:
	-------
	calculator(1,2,"+") #return 3

	calculator(1,0,"/") #return False
    """	
	if(op == "+"):
		return num1 + num2
	elif(op == "-"):
		return num1 - num2
	elif(op == "/"):
		if (num2 == 0):
			return False
		return num1 / num2
	elif(op == "//"):
		if (num2 == 0):
			return False
		return num1 // num2
	elif(op == "*"):
		return num1 * num2
	elif(op == "**"):
		return num1 ** num2
	else:
		return False
def parse_input():
	"""
    Handle taking input from the user and call calculator()

	This function prompt input from the user, process the input string into a list
	it then check if the input is valid or not then call the calculator() and provide
	the function with 2 float number and a operator string to perform mathematic operations

	Returns
	-------
	boolean
			the False value is return if the input from the user is invalid (not enought parameters, invalid parameters)

    """
	user_input = input("Enter equation: ")
	params = user_input.split()
	if(len(params) < 3):
		return False
	if(is_number(params[0]) and is_number(params[2])):
		print(calculator(float(params[0]), float(params[2]), params[1]))
	else:
		return False
def is_number(str):
	"""
    A helper function to check if a str provided contain float or int

	This function will take in a string, try converting it to float the catch exception 
	if the value cannot be converted to float. It will return True when there is not exception
	False otherwise.
	
	Parameters
	----------
	str		String
			a string that is used to test if it contains numemeric values or not

	Returns
	-------
	boolean
			determine if the provided str is a float number or not 

    """
	try:
		float(str)
		return True
	except ValueError:
		return False

