import libnum
import random
import sys
#https://asecuritysite.com/encryption/go_el_homo3
def getgenerator(p):
    for x in range(1, p):
        rand = x
        exp = 1
        next = rand % p

        while (next != 1):
            next = (next * rand) % p
            exp = exp + 1

        if (exp == p - 1):
            return rand
prime = 1009
g = getgenerator(prime)
x = random.randint(1, prime)
Y = pow(g, x, prime)

def elgamalenc(M):
    k = random.randint(1, prime)
    a = pow(g, k, prime)
    b = (pow(Y, k, prime) * pow(g,M,prime))
    return a,b

def elgamaldec(a,b,x,prime):
    s = pow(a,x,prime)
    temp = libnum.invmod(s, prime)
    message = (b * temp) % prime
    return message



print("\n Private key:", x)
print(" generator:", g)
print("Y:", Y)
print("(P,g,Y):", prime, g, Y)

message1 = int(input('Enter first message:'))

print('First Message is:',message1)
a1,b1=elgamalenc(message1)
print('First cipher text is:',a1,b1)

message2 = int(input('Enter second message:'))
print('Second message is:',message2)
a2,b2 = elgamalenc(message2)
print('Second cipher text is:',a2,b2)

totala = a1 * a2
totalb = b1 * b2

plaintext = elgamaldec(totala,totalb,x,prime)
print('Decrypt message is:',plaintext)

for i in range(0,1000000):
    result = pow(g, (i), prime)
    if (result==plaintext):
        print('Original additive value is:',i)
        print('Verified Additive Homomorphism of ElGamal')
        break




