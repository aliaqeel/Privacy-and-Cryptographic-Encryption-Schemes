import random
import sys
#https://asecuritysite.com/encryption/chaum
q=10009

s=random.randint(1,1000)
r=random.randint(1,1000)



g=3
a=10
b=13
A=pow(g,a,q)
B=pow(g,b, q)
C=pow(g,(a*b),q)

y1=pow(g,r,q)
y2=pow(B,r,q)

z=(r+a*s) % q
print("Victor and Peggy agree of (g,A, B and C):(",g,A,B,C,")")
print("\nPeggy generates random number:",r)
print("Peggy sends y1 (g^r, B^r):(",y1,y2,")")
print("Victor sends a challenge:",s)
print("Peggy computes z=r+as (mod q):",z)
print("\nVictor now checks these are the same:")
print("Victor checks g^z:",pow(g,z,q))
print("Victor checks A^s y1:",(A**s * y1) % q)
if(pow(g,z,q)==(A**s * y1) % q):
        print("Victor checked g^z and A^sy1 mod q and the values are same")
print("\nVictor now checks these are the same")
print("Victor checks B^z=", pow(B,z,q))
print("Victor checks C^s y2=",(C**s * y2) % q)
if(pow(B,z,q)==(C**s * y2) % q):
        print("Victor checked B^z and C^sy2 mod q and the values are same")