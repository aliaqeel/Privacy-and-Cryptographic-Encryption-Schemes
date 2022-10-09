#Task 2:
#took help from following website:
#https://www.geeksforgeeks.org/implementation-diffie-hellman-algorithm/
#https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
#https://www.youtube.com/watch?v=d1KXDGgwIpA

#Diffie Hellman works like for example there is generator g which is a prime number and n which is very big. Then
#the g and n are kept in the public space between John and Robert. John generate a secret value 'a' which is kept with
#himself personally and Robert generates also a secret value 'b' and keep to himself personally. Then John does
#g^a mod n. This is the public key of john. Then Robert does g^b mod n. This is the public key of Robert.
#The public of John and Robert is exchanged between John and Robert. Then secret key is made by doing (g^a)^b mod n
# by John and (g^b)^a mod n by Robert, both the output is same and it is the secret key. Then use this secret key to
#and xor it with the message.

#took from Week 3 solution
def string2hex(message):
    ret = ""
    for c in message:
        ret += hex(ord(c))[2:].rjust(2,'0')
    return ret
#took from big assignment 2
def bin_xor(a, b):
    astring = a.zfill(max(len(a),len(b)))
    bstring = b.zfill(max(len(a),len(b)))
    answer = ''
    for i in range(len(astring)):
        part1 = astring[i]
        part2 = bstring[i]
        if part1 == part2:
            answer =answer + "0"
        else:
            answer = answer +  "1"
    return answer
#took from week 2 solution
def bin2hex(binary):
    return hex(int(binary,2))[2:]

#took from week 3 solution
def hex2string(hex_message):
    ret = ""
    for i in range(0,len(hex_message),2):
        ret += chr(int(hex_message[i:i+2],16))
    return ret
#taking out secret value of John
string2hex = string2hex('Rex')
secretvaluejohn = int(string2hex,16)
g=3
n=2028857979862237691943174470742898169688801549038549581
#calculating public key of john
publickeyjohn = pow(g,secretvaluejohn,n)
print('Task 2:')
print('johns public key:',publickeyjohn)
#public key of robert
publickeyrobert = 578425925095371405568892112463356253556793923333715515
#secret key of John and Robert
secretkeyjohnandrobert = pow(publickeyrobert,secretvaluejohn,n)
print('general secret key:',secretkeyjohnandrobert)
ciphermessage = 1149155915763596984568311658058053247814715602575369297
ciphermessagebinary = str(bin(ciphermessage)[2:])
secretkeyjohnandrobertbinary = str(bin(secretkeyjohnandrobert)[2:])

#xoring the cipher message sent by John with the secret key to to find out the original message
original_message = bin_xor(ciphermessagebinary,secretkeyjohnandrobertbinary)
original_message_hex = bin2hex(original_message)
original_message_string = hex2string(original_message_hex)
print('original message sent by John:',original_message_string)