import sys
#https://asecuritysite.com/zero/z
import sympy
p=sympy.randprime(0, 10000)
g=int(input('Enter generator:'))
x=int(input('Enter Secret'))
r=int(input('enter random value:'))
print ('Prime Number:',p)
print ('Generator:',g)
print ('Secret:',x)
print ('Random Value:',r)
y= g**x % p
print ('Y:',y)
C = g**r % p
print ('C:',C)
cipher1=g**((x+r)%(p-1))  % p
print ('cipher1:',cipher1)
cipher2=C*y %p
print ('cipher2:',cipher2)
if (cipher1==cipher2):
	print ('Well done ... have you proven that you know x')
else:
	print ('Not proven')