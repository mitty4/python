class Car(object):
	def __init__(self,price,speed,fuel,mileage):
		self.price = price
		self.speed = speed
		self.mileage = mileage
		if(self.mileage >10000):
			self.tax = .15
		else:
			self.tax = .12
		self.fuel = fuel
		if(self.fuel>0 or self.fuel<=4):
			if(self.fuel == 4):
				self.fuel = "Full"
			elif(self.fuel >=2 or self.fuel <4):
				self.fuel = "Kind of Full"
			elif(self.fuel <2):
				self.fuel = "Kind of Full"
		print "Woah, nice car!"

	def display_all(self):
		print "Price: " + str(self.price)
		print "Speed: " + str(self.speed)
		print "Mileage: " + str(self.mileage)
		print "Fuel: " + str(self.fuel)
		print "Tax: " + str(self.tax)

arg1 = Car(2000, 35, 4, 15)
arg1.display_all()

