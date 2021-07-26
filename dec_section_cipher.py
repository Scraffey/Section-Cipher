import base64

def step1_2(text, key):
    rail = [['\n' for i in range(len(text))] for j in range(key)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(text)):
            if ((rail[i][j] == '*') and (index < len(text))):
                rail[i][j] = text[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(text)):
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    return("".join(result))

def step2_2(text):
    return base64.b64decode(text)

def step3_2(text):
    return ''.join(chr(int(text[i*8:i*8+8],2)) for i in range(len(text)//8))

def step4_2(text):
    custom_cipher = { 'Z':"AAAAAAAA", 'z':"AAAAAAAB", 'Y':"AAAAAABA", 'y':"AAAAABAA", 'X':"AAAABAAA", 'x': "AAABAAAA", 'W':"AABAAAAA" , 'w':"ABAAAAAA", 'V':"BAAAAAAA", 'v':"AAAAAABB", 'U':"AAAAABAB", 'u':"AAAABAAB", 'T':"AAABAAAB", 't':"AABAAAAB", 'S':"ABAAAAAB", 's':"BAAAAAAB", 'R':"AAAAABBB", 'r':"AAAABABB", 'Q':"AAABAABB", 'q':"AABAAABB", 'P':"ABAAAABB", 'p':"BAAAAABB", 'O':"AAAABBBB", 'o':"AAABABBB", 'N':"AABAABBB", 'n':"ABAAABBB", 'M':"BAAAABBB", 'm':"AAABBBBB", 'L':"AABABBBB", 'l':"ABAABBBB", 'K':"BAAABBBB", 'k':"AABBBBBB", 'J':"ABABBBBB", 'j':"BAABBBBB", 'I':"ABBBBBBB", 'i':"BABBBBBB", 'H':"BBBBBBBB", 'h':"AAAABBAB", 'G':"AAABABAB", 'g':"AABAABAB", 'F':"ABAAABAB", 'f':"BAAAABAB", 'E':"AAABBBAB", 'e':"AABABBAB", 'D':"ABAABBAB", 'd':"BAAABBAB", 'C':"AABBBBAB", 'c':"ABABBBAB", 'B':"BAABBBAB", 'b':"ABBBBBAB", 'A':"BABBBBAB", 'a':"BBBBBBAB", '0':"AAABBAAB", '1':"AABABAAB", '2':"ABAABAAB", '3':"BAAABAAB", '4':"AABBBAAB", '5':"ABABBAAB", '6':"BAABBAAB", '7':"ABBBBAAB", '8':"BABBBAAB", '9':"BBBBBAAB", '!':"AABBAAAB", '@':"ABABAAAB", '#':"BAABAAAB", '$':"ABBBAAAB", '%':"BABBAAAB", '&':"BBBBAAAB", '*':"BBBAAAAB", ' ':"BBAAAABB"}
    l = []
    results = ""
    for i in range(1, (len(text)/8)+1):
        l.append(text[((i-1)*8):(i*8)])

    for cipher_text in l:
        for letter, code in custom_cipher.items():
            if cipher_text == code:
                results += letter

    return results

def step5_2(text):
    key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
    result = ""
    for letter in text:
        if letter in alphabet:
            result += key[alphabet.find(letter)]
        else:
            result += letter
    return result

def step6_2(text, alphabet):
    key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*"
    result = ""
    for letter in text:
        if letter in alphabet:
            result += key[alphabet.find(letter)]
        else:
            result += letter

    return result

def step7_2(text, s):
    s = s * -1
    result = ""
    for i in range (len(text)):
        char = text[i]
        if(char.isalpha() == 0):
            result += char
        elif(char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif(char.lower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

# text = raw_input("Cipher Text: ")
# rail = int(raw_input("Second Number: "))
# alpha = raw_input("Alphabet: ")
# shift = int(raw_input("Shift Number: "))

# for i in range(1, 8):
    # print "Step " + str(i) + ":"
    # if i == 1:
        # result = step1_2(text, rail)
    # elif i == 2:
        # result = step2_2(result)
    # elif i == 3:
        # result = step3_2(result)
    # elif i == 4:
        # result = step4_2(result)
    # elif i == 5:
        # result = step5_2(result)
    # elif i == 6:
        # result = step6_2(result, alpha)
    # else:
        # result = step7_2(result, shift)
    # print result + "\n"
# print "\nPlaintext:\n" + result
