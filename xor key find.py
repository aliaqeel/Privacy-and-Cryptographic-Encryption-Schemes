def find_key(input):
    bin_in=str(bin(int(input,16)))[2:]
    while len(bin_in) %8 != 0:
    #make sure there are no missing leading zeros
        bin_in = "0" + bin_in
    for i in range(0,256):
    #loop through all possible 1Byte-keys
        key=str(bin(i))[2:].zfill(8)
        j = 0
        result_bin = ""
        while j < len(bin_in):
        #loop through the input as binary
            if bin_in[j]==key[j%8]:
                result_bin += "0"
            else:
                result_bin += "1"
            j += 1
        j = 0
        result = ""
        while j < len(result_bin):
        #convert each 8Bits to to a decimal int and then the corresponding ascii symbol
            result += chr(int(str(int(result_bin[j:j+8],2))))
            j += 8
        print("key: " + key + " text: " + result)
find_key("e9c88081f8ced481c9c0d7c481c7ced4cfc581ccc480")

