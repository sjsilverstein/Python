def drawStars(arr):
	for i in range (0, len(arr)):
		newStr =""
		count = 0
		while count < arr[i]:
			count+=1
			newStr+="*"
		print newStr
	return True
x = [4, 6, 1, 3, 5, 7, 25]
drawStars(x)

# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. 
# When a string is passed, instead of displaying *, display the first letter of the string according to the example below. 
# You may use the .lower() string method for this part.

def drawStars2(arr):
	for i in range (0, len(arr)):
		newStr =""
		count = 0
		if isinstance(arr[i], int):
			while count < arr[i]:
				count+=1
				newStr+="*"
			print newStr
		else:
			while count < len(arr[i]):
				count+=1
				newStr+= arr[i][0].lower()
			print newStr
	return True
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
drawStars2(x)

