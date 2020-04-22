# password_creator.py

import random
import string

def crear_pass(n):
    allChars = list(string.ascii_letters) + list(string.digits) + list(string.punctuation)
    passphrase = []

    for i in range(n):
        tmp = random.choice(allChars)
        passphrase.append(tmp)
    
    res = "".join(passphrase)
    return res

n = input("Input the length of Password: ")
test = crear_pass(n)
try:
    print(test)
except:
    print("The length of password is required!")
