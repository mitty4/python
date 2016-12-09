class Bike(object):
	def __init__(self,price,max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
		print "Woah, nice new bike!"

	def display_info(self):
		print "price: " + str(self.price)
		print "top speed: " + str(self.max_speed)
		print "miles: " + str(self.miles)
		return self
	def ride(self):
		self.miles += 10
		print "riding (+10 mileage)"
		return self
	def reverse(self):
		self.miles -= 5
		print "reversing (-5 mileage)" 
		return self

speedster = Bike(15, 40)
mountain = Bike(12, 20)
road = Bike(10, 30)

speedster.display_info().ride().reverse()
mountain.display_info().ride().reverse()
road.display_info().ride().reverse()
