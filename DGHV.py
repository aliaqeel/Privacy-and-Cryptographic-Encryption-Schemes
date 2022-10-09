from random import SystemRandom
import math

cryptogen = SystemRandom()
p = 0
m = int(input("bit to encrypt:"))
while p % 2 == 0:
    p = cryptogen.randrange(3000,5000)
q = cryptogen.randrange(math.pow(2,100),math.pow(2,1000))
r = cryptogen.randrange(2,100)

encrypted = q * p + 2 * r + m
print("encrypted:",encrypted)
decrypted = (encrypted % p) % 2
print("decrypted:",decrypted)