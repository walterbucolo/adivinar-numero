import random
from random import randint
class Number:
    # Initializer
    def __init__(self):
      self.number = []
      self.cantDigits = 4
    # Random number
    def createNumber(self):
      while len(self.number) < self.cantDigits:
            digit=random.randrange(0, 9)
            if digit not in self.number:
                self.number.append(digit)
      return self.number
      print (self.number)
   
objectNumber = Number()
newNumber = objectNumber.createNumber()
print("El número es {}".format(newNumber))