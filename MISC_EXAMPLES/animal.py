class Animal():
    no_of_legs = 0
    animal_class = ""

    def move(self):
        print ("Moving")

class Dog(Animal):
    def __init__(self):
         self.breed = ""
		 
    def move(self):
	    print ("Moving....")
		
labrador = Dog()
labrador.move()
bird = Animal()
bird.move()