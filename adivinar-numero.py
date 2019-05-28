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
            self.dictionary=[]
      # Random number
      def createNumber(self):
            number=[]
            while len(number) < self.cantDigits:
                  digit=random.randrange(0, 9)
                  if digit not in number: #Check if a digit not in number
                        number.append(digit)
            print (number)
            self.number=number
            return number
      
      def checkNumber(self, number):
            if self.number==number:
                  return True
            else:
                  correct, regular = 0,0
                  for x in self.number:
                        for y in number:
                              if x == y: #Check if a digit belongs to the number
                                    if self.number.index(x) == number.index(y) : #Check if it's the same position
                                          correct+=1
                                    else:
                                          regular+=1
                  self.correct=correct
                  self.regular=regular
                  return False
      def checkNumberAlt(self, numberOne, numberTwo):
            correct, regular = 0,0
            for x in numberOne:
                  for y in numberTwo:
                        if x == y: #Check if a digit belongs to the number
                              if numberOne.index(x) == numberTwo.index(y) : #Check if it's the same position
                                    correct+=1
                              else:
                                    regular+=1
            self.correct=correct
            self.regular=regular
            resp=(correct, regular)
            return resp 
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
      
      def convertList(self,list):
            s = [str(i) for i in list]
            res = int("".join(s))
            return res

      def guessNumber(self, dic):
            self.dictionary.append(dic.copy())
            numberInt = self.convertList(dic['number'])
            matches = False
            while matches == False:
                  c=0
                  valid = False
                  while valid == False:
                        numberInt += 1
                        number = str(numberInt)
                        print("numberstr:", number, "numberint", numberInt)
                        if len(number) == 3: #validar 4 digitos
                              number ='0'+ number
                        if number == '9999': #Validar 4 digitos
                              numberInt = 123
                              number = "0123"
                        checkNoDuplicates = self.validateNumber(number)
                        if checkNoDuplicates == True:
                              valid = True
                  for x in self.dictionary:
                        numberArray=[int(digit) for digit in number]
                        resp = self.checkNumberAlt(x['number'],numberArray)
                        if resp[0] == x['correct'] and resp[1] == x['regular']:
                              c += 1
                        if c == len(self.dictionary):
                              matches = True
                              return numberArray
            return None 
             
            
class Agent:
      objectNumber = Number()
      # newNumber = None
      def __init__(self):
            # self.newNumber = self.objectNumber.createNumber()
            self.isValid, self.isCorrect = False, False
      def agentTwo(self):
            isValid=False
            isCorrect=False
            newNumber=self.objectNumber.createNumber() #Create number
            Dict = {'number': newNumber, 'correct': None, 'regular': None}
            while isCorrect==False:
                  print ("¿El número {} es correcto?".format(newNumber))
                  correct=input("¿ingresa 'si' si el numero es correcto: ")
                  if correct=='si':
                        isCorrect=True
                        break
                  Dict = {'number': newNumber, 'correct': None, 'regular': None}
                  inCorrect = input("¿Cuántas cifras son correctas?: ")
                  inRegular = input("¿Cuántas cifras son regulares?: ")
                  try:
                        inCorrect = int(inCorrect)
                        inRegular = int(inRegular)
                        total = inCorrect + inRegular
                        if inCorrect > 4 and inRegular > 4 and total > 4:
                              print("Ingresa un número entre 0 y 4")
                        else:
                              Dict['correct']=inCorrect
                              Dict['regular']=inRegular
                              newNumber=self.objectNumber.guessNumber(Dict)
                              if newNumber == None:
                                    print ("No pude encontrar el número. ¿Habrás confundido algún ingreso de datos?")
                                    break
                  except ValueError:
                        print ('Ingresa un número válido')
            print("Bien jugado!")

      def agentOne(self):
            self.objectNumber.createNumber() #Create number
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
            
      def agent(self):
            inp = ""
            while inp != "1" and inp != "2":
                  inp = input("Escribe 1 para adivinar un número o elige 2 para que yo adivine el número que piensas!: ")
                  if inp != "1" and inp != "2":
                        print("Error: Escribe 1 o 2")
            if inp == "1":
                  Agent.agentOne(self)
            if inp == "2":
                  Agent.agentTwo(self)

objectAgent = Agent()
objectAgent.agent()