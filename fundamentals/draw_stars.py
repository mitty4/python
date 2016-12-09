#DRAW STARS

#Part I

a = [4,6,1,3,5,7,25]
def draw_stars(a):
	for i in range(len(a)):
		print 'Stars'+'*'*a[i]

draw_stars(a)

#PartII

a = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
def draw_random(a):
	i=0
	for i in range(len(a)):
		if(type(a[i]) == int):
			print 'Number: '+' *'*a[i]
		elif(type(a[i]) == str):
			print 'Name: '+a[i]+' '+a[i][0].lower()*len(a[i])
draw_random(a)