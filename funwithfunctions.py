# Create a function called odd_even that counts from 1 to 2000. 
# As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.

# def oddEven(num):
# 	for x in range(1,num+1):
# 		if x % 2 == 0:
# 			print "Number is " +str(x)+". This is an even number."
# 		else:
# 			print "Number is "+str(x)+". This is an odd number."
# oddEven(2000)

# Create a function called 'multiply' that iterates through each value in a list 
# (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

def multiply (takeMe, againAndagain):
	newList = []
	for i in range(0, len(takeMe)):
		newList.append(takeMe[i]*againAndagain)
	return newList
# a = [2,4,10,16]
# print a
# b = multiply(a, 5)
# print b

# Write a function that takes the multiply function call as an argument. 
# Your new function should return the multiplied list as a two-dimensional list. 
# Each internal list should contain the 1's times the number in the original list. Here's an example:

def layered_multiples(arr):
	print arr
	newArr=[]
	for i in range(0, len(arr)):
		arr2=[]
		for j in range (0, arr[i]):
			arr2.append(1)
		newArr.append(arr2)
	return newArr

# def onesarr(num):
# 	aArr = []
# 	while len(aArr) != num:
# 		aArr.append(1)
# 	print aArr
# 	return aArr

y = multiply([2,4,5],3)
print y
# for i in range (0, len(y)):
# 	onesarr(y[i])
x = layered_multiples(multiply([2,4,5],3))
print x