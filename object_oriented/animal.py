class Animal(object):
	"""docstring for ClassName"""
	def __init__(self, name, health):
		self.name = name
		self.health = health
	def display_health(self):
		print self.health
		return self
	def walk(self):
		self.health -=1
		print "walking"+' (- 1!)'
		return self
	def run(self):
		self.health -=5
		print "running"+' (- 5!)'
		return self
	def display_health(self):
		print self.health
		return self

animal= Animal("animal", 100)
animal.walk().run().display_health()

class Dog(Animal):
	def __init__(self):
		super(Dog, self).__init__("", 0)
		self.health = 150
	def pet(self):
		self.health += 5
		print "petting"+' (+ 5!)'
		return self

dog = Dog()
dog.walk().run().pet().display_health()

class Dragon(Animal):
	def __init__(self):
		super(Dragon, self).__init__("",0)
		self.health = 170
	def fly(self):
		self.health -= 10
		print "flying"+' (- 10!)'
		return self
	def display_health(self):
		print "This is a Dragon! Health: "+str(self.health)
		return self
						
dragon = Dragon()
dragon.walk().run().fly().display_health()




