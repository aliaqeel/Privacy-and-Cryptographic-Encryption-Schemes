import random
#https://www.codespeedy.com/elgamal-encryption-algorithm-in-python/

#To fing gcd of two numbers
def gcd(num1,num2):
    if(num2==0):
        return num1
    else:
        return gcd(num2,num1%num2)
#For key generation i.e. large random number
def keygeneration(num):
    keys= random.randint(pow(10,20),num)
    while gcd(num,keys)!=1:
        keys=random.randint(pow(10,20),num)
    return keys
#For asymetric encryption
def encryption(msg,q,h,g):
    ciphertext=[]
    k=keygeneration(q)
    s=pow(h,k,q)
    c1=pow(g,k,q)
    for i in range(0,len(msg)):
        ciphertext.append(msg[i])
    print("g^r: ",c1)
    print("h^r : ",s)
    for i in range(0,len(ciphertext)):
        ciphertext[i]=s*ord(ciphertext[i])
    return ciphertext,c1
#For decryption
def decryption(ciphertext,c1,key,q):
    plaintext=[]
    h=pow(c1,key,q)
    for i in range(0,len(ciphertext)):
        plaintext.append(chr(int(ciphertext[i]/h)))
    return plaintext
message=input("Enter message:")
q=random.randint(pow(10,20),pow(10,50))
g=random.randint(2,q)
key=keygeneration(q)
h=pow(g,key,q)
print("g:",g)
print("h:",h)
ciphertext,c1=encryption(message,q,h,g)
print("Plain Message:",message)
print("Encrypted Message:",ciphertext)
plaintext=decryption(ciphertext,c1,key,q)
plainmsg=''.join(plaintext)
print("Decryted Message=",plainmsg)