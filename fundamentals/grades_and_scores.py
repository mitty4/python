#GRADES AND SCORES
r = [60,67,90,89]
def grades_and_scores(r):
	a = "A"
	b = "B"
	c = "C"
	d = "D"
	print "Scores and Grades"
	for count in range(len(r)):
		s = r[count]
		if(s>=90):
			print "Score: "+str(s)+ "; "+"Your grade is: "+a
		elif(s>=80):
			print "Score: "+str(s)+ "; "+"Your grade is: "+b
		elif(s>=70):
			print "Score: "+str(s)+ "; "+"Your grade is: "+c
		elif(s>=60):
			print "Score: "+str(s)+ "; "+"Your grade is: "+d
	print "End of Program. Bye!"
grades_and_scores(r)
