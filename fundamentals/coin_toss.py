# COIN TOSS
def toss():
	i = 1
	heads = 0
	tails = 0
	while i < 11:
		import random
		random_num = round(random.random())
		if(random_num == 1):
			heads += 1
			print 'Attempt #'+str(i)+'  heads!' 
		else:
			tails += 1
			print 'Attempt #'+str(i)+'  tails!' 
		i = i + 1
	print 'Heads Count:' + str(heads)
	print 'Tails Count:' + str(tails)

toss()
