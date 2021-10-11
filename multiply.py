def multiply_list(list):
	"""
	Multiple all elements in the list
	
	This function take in a list then loop through it. For each loop, the previous result will be used to multiply
	with the next element in the list. The initial result is 1. After the calculation, the function will return
	the result.

	Parameters
	----------
	list[int]
			the input list whose elements are to be multiplied
	
	Returns
	-------
	int
		the quotation of all the elements in the list

	Example:
	-------
	 multiply_list([1,2,3]) #return 6
	"""
	#To store the quotation result to use after each loop
	result = 1
	for number in list:
		if (is_number(number) == False):
			return False
		result = result * float(number)
	return result

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