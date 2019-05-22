import random
from random import randint
class Number:
    # Initializer
    def __init__(self):
      self.number = []
      self.cantDigits = 4
      self.error = ""
      self.regular = 0
      self.correct = 0
    # Random number
    def createNumber(self):
      while len(self.number) < self.cantDigits:
            digit=random.randrange(0, 9)
            if digit not in self.number: #Check if a digit not in number
                self.number.append(digit)
      return self.number
      print (self.number)
    def checkNumber(self, number):
      if self.number==number:
            return True
      else:
            correct, regular = 0,0
            print(self.number)
            for x in self.number:
                  for y in number:
                        if x == y: #Check if a digit belongs to the number
                              if self.number.index(x) == number.index(y) : #Check if it's the same position
                                    correct+=1
                              else:
                                regular+=1
                                print(regular)
            self.correct=correct
            print (regular)
            self.regular=regular
            print (self.regular)
            return False
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
        arrayNumber = [digit for digit in number]
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
      self.isValid, self.isCorrect = False, False
  def agent(self):
    #ask for number
    while self.isCorrect == False:
      inputNumber = input("Por favor, ingresa un número de 4 dígitos: ")
      self.isValid = self.objectNumber.validateNumber(inputNumber)
      if self.isValid == False:
        print("Error: {}".format(self.objectNumber.error))
      else:
        inputNumberArray=[int(digit) for digit in inputNumber]
        self.isCorrect = self.objectNumber.checkNumber(inputNumberArray)    
        if self.isCorrect == False:
          print("El número {} es incorrecto".format(inputNumber))
          print("Hay {} correctas y {} regulares".format(self.objectNumber.correct, self.objectNumber.regular ))
        else:
          print("Felicitaciones! El número {} es correcto".format(inputNumber))

objectAgent = Agent()
objectAgent.agent()