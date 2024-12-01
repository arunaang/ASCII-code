#Random Password Generator helped by www.101computing.net/random-password-generator/
import random

# shuff function do shuffle all the characters of a string
def shuff(string):
  rList = list(string)
  random.shuffle(rList)
  return ''.join(rList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
#Generate more characters here
lowercaseLetter1= chr(random.randint(97,120))#Generate a random Lowercase letter (based on ASCII code)
lowercaseLetter2= chr(random.randint(97,120))#Generate a random Lowercase letter (based on ASCII code)
digit1 = chr(random.randint(48,57)) #Generate a random number 0 to 9 (based on ASCII code)
digit2 = chr(random.randint(48, 57)) #Generate a random number 0 to 9 (based on ASCII code)
punc1 = chr(random.randint(0,127)) #Generate a random specialized character (based on ASCII code)
punc2 = chr(random.randint(0, 127)) #Generate a random specialized character (based on ASCII code)

#Generate password using all the characters, in random order
password1 = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punc1 + punc2
password = shuff(password1)

#Ouput
print(password)