name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
	newDict = {}
	for i in range (len(list1)):
		newDict[list1[i]] = list2[i]
	return newDict
#print make_dict(name, favorite_animal)

# Hacker Challenge:
# If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.

name2 = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal2 = ["horse", "cat", "spider"]

def make_dict2(list1, list2):
	newDict = {}
	if len(list1) > len(list2):
		for i in range(0, len(list1)-len(list2)):
			list2.append('undefined')
			print list1
			print list2
		newDict = make_dict(list1, list2)
	elif len(list1) < len(list2):
		for i in range(0, len(list2)-len(list1)):
			list1.append('undefined')
			print list1
			print list2
		newDict = make_dict(list2, list1)
	else:
		print list1
		print list2
		newDict = make_dict(list1, list2)
	print newDict
	return True

#make_dict2(name2, favorite_animal2)
make_dict2(favorite_animal2, name2)

