#MULTILPLY
a = [2,4,10,16]
b = 5

def multiply(a,b):
	c=[]
	for s in range(len(a)):
		c.append(a[s]*b)
	print c

multiply(a,b)