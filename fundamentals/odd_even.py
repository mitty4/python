#ODD/EVEN
a = [1,2,3,4]
b = 3

def multiply(x,y):
	odd = []
	even = []
	for count in range(0, len(x)):
		c = x[count]*y
		if c % 2 == 0:
			even.append(c)
		else:
			odd.append(c)
	print 'Even: '+str(even)
	print 'Odd: '+str(odd)

multiply(a,b)