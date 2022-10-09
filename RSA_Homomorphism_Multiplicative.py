import random


#further References
#https://www.cuemath.com/numbers/prime-numbers-1-to-500/
#https://en.wikipedia.org/wiki/RSA_(cryptosystem)
#https://www.delftstack.com/howto/python/python-generate-prime-number/
#took help from previous semester cryptography slides as well

#generating prime numbers
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



#euclidean algo reference:
#https://www.youtube.com/watch?v=p5gn2hj51hs
#https://www.youtube.com/watch?v=dzPiEfxLvtE
def relativelyPrime(num1, num2):
    while num2 != 0:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    if num1 == 1:
        return True

#extended eucludean algo reference:
#https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
#https://www.youtube.com/watch?v=5tezzRkdXfo
#https://www.youtube.com/watch?v=kYasb426Yjk
def calculateD(num1,num2):
    gcd, num, y = extendedeuclideanalgorithm(num1,num2)
    if num < 0:
        num = num + num2
    return num

def extendedeuclideanalgorithm(num1 , num2):
    #base case
    if num1 == 0:
        gcd = num2
        xold = 1
        yold = 0
        return gcd,yold,xold
    else:
        remainder = num2 % num1
        gcd, xnew, ynew = extendedeuclideanalgorithm(remainder, num1)
        quotient = num2 // num1
        xold = ynew - quotient * xnew
        yold = xnew
        return gcd,xold,yold
def keygenerationalgo(keylength):
    prime1 = generateprime(keylength)
    prime2 = generateprime(keylength)
    print('Prime p:'+ str(prime1))
    print('Prime q:' + str(prime2))
    #
    n = prime1 * prime2
    phiofN = (prime1 - 1) * (prime2 - 1)  # totient
    print("Euler Totient of n: " + str(phiofN))
    # choosing e by checking if e is relative prime to euler totient of n
    while not False:
        e = random.randrange(1, phiofN)
        if (relativelyPrime(e, phiofN)):
            break

    # choose d such d is inverse mod of ed = 1 mod phiofN
    d = calculateD(e, phiofN)

    return e,d, n

#for encryption and decryption took help from previous introduction to computer security practice to understand pow function
def rsaencryption(e,n,message):
    inter = 0
    #interimlit = []
    #ciphertext = ""
    #for i in message:
    #    interimlit.append(str(pow(ord(i), e, n)))
    #ciphertext = ciphertext.join(map(str,interimlit))

    inter = pow(message,e,n)
    return inter

def rsadecryption(d,n,intermlit):
    plaintext = 0
    for item in intermlit:
            #plaintext = plaintext + chr(pow(item, d, n))
            plaintext = pow(item,d,n)
    return plaintext

#print(keygenerationalgo(3))
def rsa():
    enctext=""
    enctext1=""
    print("Name: Ali Aqeel Zafar")
    print("Neptune ID: AAFZDE")
    keylength = int(input("Enter the length of the primes:"))
    e,d,n=keygenerationalgo(keylength)
    print('Public Key Pair:' + '(' + str(e) + ',' + str(n) + ')')
    print('Private Key Pair:' + '(' + str(d) + ',' + str(n) + ')')

    message1 = int(input("Enter first number to encrypt with public key:"))
    enctext = rsaencryption(e,n,message1)
    print('Encrypted Number is:', enctext)

    message2 = int(input("Enter second number to encrypt with public key:"))
    enctext1 = rsaencryption(e,n,message2)

    print('Encrypted Number is:', enctext1)


    intermlit3 = enctext * enctext1
    print('Encrypted Product Answer is:',intermlit3)
    intermlit4 = []
    intermlit4.append(intermlit3)
    plaintext = rsadecryption(d,n,intermlit4)
    print('Decrypted Message:', plaintext)

    answer = message1 * message2
    print('Original Product Answer:',answer)
    if plaintext == answer:
        print("Verified Multiplicative Homomorphism of RSA")
    else:
        print("Not Multiplicative Homomorphism of RSA")

rsa()