# Stephen Silverstein
# https://github.com/sjsilverstein

# words = "It's thanksgiving day. It's my birthday,too!"
# print words.find('day')
# newString = words.replace('day', 'mounth')
# print newString
# x = [2,54,-2,7,12,98]
# print min(x)
# print max(x)
# x = ["hello",2,54,-2,7,12,98,"world"]
# print x[0] + x[len(x)-1]
# newList = []
# newList.append(x[0])
# newList.append(x[len(x)-1])
# print newList
# x = [19,2,54,-2,7,12,98,32,10,-3,6]
# x.sort()
# first = []
# last = []
# print x
# for idx in range(0, len(x)):
# 	if idx <= (len(x)/2):
# 		first.append(x[idx])
# 	elif idx > (len(x)/2):
# 		last.append(x[idx])
# print first
# # print last
# for num in range(1, 1001):
# 	print num
# for num in range(5,1000001, 5):
# 	print num
# a = [1, 2, 5, 10, 255, 3]
# print sum(a)
# # print sum(a)/len(a)
# sI = 45
# mI = 100
# bI = 455
# eI = 0
# spI = -23
# sS = "Rubber baby buggy bumpers"
# mS = "Experience is simply the name we give our mistakes"
# bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
# eS = ""
# aL = [1,7,4,21]
# mL = [3,5,7,34,3,2,113,65,8,89]
# lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
# eL = []
# spL = ['name','address','phone number','social security number']
# def filterType(testMe):
# 	if isinstance(testMe, int) == True:
# 		if testMe >= 100:
# 			print "That's a big number!"
# 		if testMe <=100:
# 			print "That's a small number."
# 	if isinstance(testMe, str) == True:
# 		if len(testMe) >= 50:
# 			print "Long Sentence."
# 		if len(testMe) <50:
# 			print "Short Sentence."
# 	if isinstance(testMe, list) == True:
# 		if len(testMe) >10:
# 			print "Big List"
# 		else:
# 			print "Short List"

# filterType(sI)
# filterType(mI)
# filterType(bI)
# filterType(eI)
# filterType(spI)
# filterType(sS)
# filterType(mS)
# filterType(bS)
# filterType(eS)
# filterType(aL)
# filterType(mL)
# filterType(lL)
# filterType(eL)
# filterType(spL)

# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, 
# concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, 
# the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

def arrType(arr):
	typeInt = False
	typeStr = False
	intSum = 0
	strTotal = ""
	for idx in range(0, len(arr)):
		if isinstance(arr[idx], int):
			intSum+=arr[idx]
			typeInt = True
		if isinstance(arr[idx], str):
			strTotal+=arr[idx]
			typeStr = True
	if typeInt == True and typeStr == True:
		print "The list you entered is of mixed type"
		print "String:"+strTotal
		print "Sum:" + str(intSum)
	elif typeInt == True:
		print "The list you entered is of integer type"
		print "Sum:" + str(intSum)
	else:
		print "The list you entered is of string type"
		print "String:"+ strtotal
l = ['magical unicorns',19,'hello',98.98,'world']
arrType(l)

