my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def toTuples(arr):
	newArr =[]
	for key in my_dict:
		newArr.append((key, my_dict[key]))
	return newArr
x = toTuples(my_dict)
print x