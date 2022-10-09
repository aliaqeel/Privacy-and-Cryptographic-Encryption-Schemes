import libnum
import sys
#from Crypto.Util.number import getPrime
#from Crypto.Random import get_random_bytes
from random import randint
import sympy
import random
import math
def gcd(num1,num2):
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num1
#References
#https://www.youtube.com/watch?v=nTfRiToLhG8
#https://asecuritysite.com/encryption/homdiff
#https://asecuritysite.com/encryption/homdiff
#https://en.wikipedia.org/wiki/Paillier_cryptosystem

def lowestcommonfactor(num1,num2):
    for i in range(1,num1 * num2 +1):
        if i % num1 == 0 and i % num2 == 0:
            return i

#took from assignment 1
def generateprime(keylength):
    primenumberlist = []
    number = random.randrange(2, 2 ** keylength - 1)
    for iteration in range(0,number):
        prime = True
        for iteration2 in range(2,iteration):
            if iteration % iteration2 == 0:
                prime = False
        if prime:
            primenumberlist.append(iteration)
    return random.choice(primenumberlist)
def GenPrime(keylength):
    return sympy.randprime(2, 2 ** keylength - 1)

#took from assignment 1
def relativelyPrime(num1, num2):
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    if num1 == 1:
        return True
def Lfunc(x,n):
    a = x-1
    return a // n
#https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
def modInverse(num1,num2):
    for x in range(1,num2):
        a = num1 % num2
        b = x % num2
        c = (a * b) % num2
        if c == 1:
            return x

def keygeneration(keylength):
    while not False:
        p = generateprime(keylength)
        q = generateprime(keylength)
        if (gcd(p*q, (p-1)*(q-1))==1):
            break

    n = p * q
    print('P:',p)
    print('Q:', q)
    print("N is:",n)
    glambda = lowestcommonfactor(p-1,q-1)
    #glambda = math.lcm(p-1,q-1)
    print("Lambda is:", glambda)
    while not False:
        g = randint(1,n*n)
        #https://sharmaeklavya2.github.io/theoremdep/nodes/abstract-algebra/groups/znstar-is-a-group.html
        if (gcd(g,n * n) == 1):
            break
    print("g is :",g)
    Lgtem = pow(g,glambda,n*n)
    Lgtem1 = Lfunc(Lgtem,n)
    gMu = modInverse(Lgtem1,n)
    #gMu = libnum.invmod(Lfunc(pow(g,glambda,n*n),n),n)
    print("Mu is:",gMu)

    return glambda, n, g , gMu

def encryption(message,n,g):
    r = randint(0,n)
    ciphertext = ""
    #res = ((g**message) * (r**n))
    #ciphertext =res % (n*n)
    for i in message:
        res = ((g ** ord(i)) * (r ** n))
        ciphertext = ciphertext + str(res % (n * n)) + " "
    return ciphertext

def decryption(glambda,gMu,n,c):
    #cipres = (c**glambda) % (n*n)
    #cipMu = Lfunc(cipres,n)
    #plaintext = (cipMu * gMu) % n
    plaintext = ""
    cipherpart = c.split()
    for i in cipherpart:
        cipres = (int(i)**glambda) % (n*n)
        cipMu = Lfunc(cipres,n)
        plaintext = plaintext + chr((cipMu * gMu) % n)
    return plaintext

def Paillier():
    keylength = 9

    glambda, n, g , gMu = keygeneration(keylength)

    #message = int(input("Enter message:"))
    message = input("Enter message:")
    ciphertext = encryption(message,n,g)
    print("Cipher Text is:" ,ciphertext)

    plaintext = decryption(glambda,gMu,n,ciphertext)
    print("Plain Text is:", plaintext)

Paillier()




