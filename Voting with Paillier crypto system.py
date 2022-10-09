from phe import paillier
public_key, private_key = paillier.generate_paillier_keypair()
voting_list = []
num = int(input('How many voters: '))
for n in range(num):
    vote = int(input('Enter 1 or 0: '))
    voting_list.append(vote)

encrypted_number_list = [public_key.encrypt(x) for x in voting_list]
totalvotes=private_key.decrypt(sum(encrypted_number_list))
if totalvotes >= 3:
    print("Joe is chosen as our Chairman")
else:
    print("Joe is not chosen as our Chairman")


