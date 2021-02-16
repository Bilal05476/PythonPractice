import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1=chr(random.randint(97,122)) #Generate a random LowerCase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,122)) #Generate a random LowerCase letter (based on ASCII code)
Digit1=int(random.randint(48,57)) #Generate a random Digit (based on ASCII code)
Digit2=int(random.randint(48,57)) #Generate a random Digit (based on ASCII code)
Symbol1=chr(random.randint(33,152)) #Generate a random Symbol (based on ASCII code)
Symbol2=chr(random.randint(33,152)) #Generate a random Symbol (based on ASCII code)

#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + str(Digit1) + Symbol1 + str(Digit2) + Symbol2
password = shuffle(password)

#Ouput
print(password)