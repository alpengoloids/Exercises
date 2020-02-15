class Person():
	name = ""
	def _init_(self):
		self.name=""
	
	def talk(self):
		print("Hi! I am %s." % (self.name))
		
miguelito = Person()
miguelito.name = "Miguelito Rivera"
miguelito.talk()