# Write a function that generates ten scores between 60 and 100. 
# Each time a score is generated, your function should display what the grade is for a particular score

def gradeNum(num):
	myGrades = {'A':90,'B': 80, 'C':70,'D':60}
	for key in myGrades:
		if num >= myGrades[key]:
			return key

def randomGrades(num):
	import random
	while num > 0:
		num -=1
		randomGrade = random.randint(60,100)
		print "Score: "+str(randomGrade)+"; Your Grade is "+gradeNum(randomGrade)
	print "End of the grogram. Bye!"
	return True

randomGrades(10)
