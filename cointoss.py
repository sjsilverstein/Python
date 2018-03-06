def coinToss(num):
	l = 0
	hCount = 0
	tCount = 0
	import random
	while l < num:
		l+= 1
		coinflip = random.randint(0,1) 
		if coinflip == 1:
			hCount+=1
			print "Attempt #"+str(l)+": Throwing a coin... It's a head! ... Got "+str(hCount)+" head(s) so far and "+str(tCount)+" tail(s) so far"
		else:
			tCount+=1
			print "Attempt #"+str(l)+": Throwing a coin... It's a tail! ... Got "+str(hCount)+" head(s) so far and "+str(tCount)+" tail(s) so far"
	print "Ending the program, thank you!"
	return True
coinToss(5000)
