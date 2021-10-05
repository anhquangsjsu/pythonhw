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
		result = result * number
	return result
