import libnum
import random
import sys
import sympy
#https://asecuritysite.com/zero/z_df
n=sympy.randprime(0, 10000)
x=int(input('Enter Secret:'))

g=int(input('Enter generator:'))
h=int(input('Enter another generator value:'))

# Victor sends r to Peggy
r=random.randint(0,n)

print ("Victor sends (r): :",r)

# Peggy generates a random number r1
# And computes r2 = r-r1 x
r1=random.randint(0,n)
r2=(r-r1*x)

print ("\nPeggy R1: :",r1)
print ("Peggy R2:",r2)


c1=(pow(g,x,n)*pow(h,r1,n)) % n

if (r2>0):
  commit_peggy=(pow(c1,x,n)*pow(h,r2,n)) % n
else:
  val=pow(h,-r2,n)
  commit_peggy=(pow(c1,x,n)*libnum.invmod(val,n)) % n


print ("\nCommit from Peggy:",commit_peggy)

commit_victor = (pow(g,x*x,n)*pow(h,r)) %n

print ("Commit from Victor:",commit_victor)

if (commit_victor==commit_peggy):
  print ("\nPeggy has proven she knows: ",x)
else:
  print('Peggy does not know:',x)