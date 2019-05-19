import random
from random import randint
class Number:
    # Initializer
    def __init__(self):
      self.number = []
      self.cantDigits = 4
      self.error=""
    # Random number
    def createNumber(self):
      while len(self.number) < self.cantDigits:
            digit=random.randrange(0, 9)
            if digit not in self.number:
                self.number.append(digit)
      return self.number
      print (self.number)
    def validateNumber(self,number):
        #limited to numbers
        if str.isdigit(number)==False:
            self.error="introduce solo dígitos."
            return False
        #Limited to four digit
        if len(number) != self.cantDigits:
            self.error="introduce un número de {} cifras.".format(self.cantDigits)
            return False
        #Limited to different digits
        arrayNumber = [digit for digit in number] #Sacar
        differentValues = len(set(arrayNumber)) == len(arrayNumber)  #check if are different values, return true or false
        if differentValues == False:
            self.error="introduce un número con todos sus dígitos distintos."
            return False
        return True
class Agent:
  objectNumber = Number()
  newNumber = None
  def __init__(self):
      self.newNumber = self.objectNumber.createNumber()
  def agent(self):
    #ask for number
    inputNumber = input("Por favor, ingresa un número de 4 dígitos: ")
    isValid = self.objectNumber.validateNumber(inputNumber)
    if isValid:
          print("El número {} es correcto".format(inputNumber))
    else:
          print("Error: {}".format(self.objectNumber.error))
         
objectAgent = Agent()
objectAgent.agent()