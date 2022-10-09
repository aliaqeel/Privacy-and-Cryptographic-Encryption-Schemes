def hex2base64(s):
    scale = 16
    num_of_bits = 8
    binary_number = bin(int(s, scale))[2:].zfill(num_of_bits)
    print(binary_number)

    base64_table = {
        '000000':'A',
        '000001':'B',
        '000010':'C',
        '000011':'D',
        '000100':'E',
        '000101':'F',
        '000110':'G',
        '000111':'H',
        '001000':'I',
        '001001':'J',
        '001010':'K',
        '001011':'L',
        '001100':'M',
        '001101':'N',
        '001110':'O',
        '001111':'P',
        '010000':'Q',
        '010001':'R',
        '010010':'S',
        '010011':'T',
        '010100':'U',
        '010101':'V',
        '010110':'W',
        '010111':'X',
        '011000':'Y',
        '011001':'Z',
        '011010':'a',
        '011011':'b',
        '011100':'c',
        '011101':'d',
        '011110':'e',
        '011111':'f',
        '100000':'g',
        '100001':'h',
        '100010':'i',
        '100011':'j',
        '100100':'k',
        '100101':'l',
        '100110':'m',
        '100111':'n',
        '101000':'o',
        '101001':'p',
        '101010	':'q',
        '101011':'r',
        '101100':'s',
        '101101':'t',
        '101110':'u',
        '101111':'v',
        '110000':'w',
        '110001':'x',
        '110010':'y',
        '110011':'z',
        '110100':'0',
        '110101':'1',
        '110110':'2',
        '110111':'3',
        '111000':'4',
        '111001':'5',
        '111010':'6',
        '111011':'7',
        '111100':'8',
        '111101':'9',
        '111110	':'+',
        '111111':'/',
    }
    base64string = ''
    if len(binary_number) % 6 != 0:
        #print(binary_number)
        binary_string = str(binary_number)
        #print(len(binary_string))
        padding_number = (len(binary_string) % 6) // 2
        if padding_number == 2:
           # print(padding_number)
            padded_string = binary_string.ljust(len(binary_string) + 2, '0')
        if padding_number == 1:
            #print(padding_number)
            padded_string = binary_string.ljust(len(binary_string) + 4, '0')

        n = 6
        split_strings = [padded_string[index: index + 6] for index in range(0, len(padded_string), 6)]

        for i in split_strings:
            for j in base64_table:
                if i == j:
                    base64string += base64_table[j]
        if padding_number == 2:

            print(base64string+'==')
        if padding_number == 1:
            print(base64string+ '==')

    else:
        binary_string = str(binary_number)
        padding_number = (len(binary_string) % 6) // 2
        n = 6
        split_strings = [binary_string[index: index + 6] for index in range(0, len(binary_string), 6)]
        print(split_strings)
        for i in split_strings:
            for j in base64_table:
                if i == j:
                    base64string += base64_table[j]
        if padding_number == 2:
            print(base64string + '==')
        if padding_number == 1:
            print(base64string + '==')




s = '3D'
hex2base64(s)