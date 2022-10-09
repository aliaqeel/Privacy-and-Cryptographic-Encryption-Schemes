import random
import base64

#references and took help from:
#https://www.geeksforgeeks.org/implementing-shamirs-secret-sharing-scheme-in-python/
#https://en.wikipedia.org/wiki/Lagrange_polynomial
#https://pycryptodome.readthedocs.io/en/latest/src/protocol/ss.html
#http://point-at-infinity.org/ssss/demo.html
#https://www.geeksforgeeks.org/how-to-convert-bytes-to-int-in-python/
#https://python-forum.io/thread-16834.s
#https://github.com/ergl/sss_py/blob/master/sss/shamir.py
def sharegeneration(no_shares, threshold, secret,space):
    coeff = []
    for _ in range(threshold - 1):
        interm = random.randrange(1, space)
        coeff.append(interm)
    coeff.append(secret)
    share = []
    for i in range(1, no_shares+ 1):
        x = random.randrange(1,space)
        share.append((x, (polyequation(x, coeff))))
    return share

def polyequation(x, coefficients):
    poly = 0
    for power, coeff in enumerate(coefficients[::-1]):
        poly += x ** power * coeff
    return poly
def reconstructionlagrange(shares,space):
    sum = 0
    for xvalue, yvalue in shares:
        prod = 1
        for xval, _ in shares:
            if xval != xvalue:
                temp = (xval - xvalue) % space
                # https: // en.wikipedia.org / wiki / Extended_Euclidean_algorithm
                (temp1, tnew) = (0, 1)
                (reo, rnew) = (space, temp)
                while rnew != 0:
                    quotient = reo // rnew
                    (temp1, tnew) = (tnew, temp1 - (quotient * tnew))
                    (reo, rnew) = (rnew, reo - (quotient * rnew))

                if temp1 < 0:
                    temp1 += space
                t1 = temp1 % space
                divs = (xval * t1) % space

                prod = (prod * divs) % space
        sum = (sum + ((yvalue * prod) % space)) % space
    return sum


def shamiersecretsharingscheme():
    space = 23112941343471735359619678378979
    no_shares = int(input('Enter number of shares:'))
    print('Number of Shares:', no_shares)
    threshold = int(input('Enter the threshold:'))
    print('Threshold:', threshold)
    secret = input('Input Secret:')
    print('Secret:',secret)
    secret2 = []
    if no_shares < threshold:
        print("number of shares smaller than threshold")
        exit(0)
    else:
        # Converting secret string to byte array
        secretbyte_array = bytes(secret,'utf-8')
        # Share Generation
        int_val = int.from_bytes(secretbyte_array, "big")
        shares = sharegeneration(no_shares, threshold, int_val, space)
        print('====Shares====')
        for i,j in enumerate(shares):
            print(base64.b64encode(str(j[1]).encode()))
    #reconstruction
    picktshares = random.sample(shares, threshold)
    print('====Selected Shares====')
    for i, j in enumerate(picktshares):
        print(base64.b64encode(str(j[1]).encode()))
    s = reconstructionlagrange(picktshares,space)
    str1 = str(s)
    lenstr= len(str1)
    secretbyte = s.to_bytes(lenstr,'big')
    origstring = secretbyte.decode('utf-8')
    print('Reconstructed secret:' , origstring[-len(secret):])

shamiersecretsharingscheme()