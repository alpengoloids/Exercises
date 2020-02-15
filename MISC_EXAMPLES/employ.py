class Employee:
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

a = Employee("Jose", 2009)
print (a.empCount)
b = Employee("Lito", 232)
print (a.empCount)