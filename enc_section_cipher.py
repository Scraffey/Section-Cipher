import base64
import random

def step1_1(text, s):
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

def random_alpha(alphabet):
    l = list(alphabet)
    random.shuffle(l)
    key = ''.join(l)
    return key

def step2_1(text):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*"
    key = random_alpha(alphabet)
    result = ""
    for letter in text:
        if letter in alphabet:
            result += key[alphabet.find(letter)]
        else:
            result += letter
    
    print "\nRandomized Alphabet: " + key + "\n"

    return result

def step3_1(text):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"
    result = ""
    for letter in text:
        if letter in alphabet:
            result += key[alphabet.find(letter)]
        else:
            result += letter
    return result

def step4_code(letter):
    custom_cipher = { 'Z':"AAAAAAAA", 'z':"AAAAAAAB", 'Y':"AAAAAABA", 'y':"AAAAABAA", 'X':"AAAABAAA", 'x': "AAABAAAA", 'W':"AABAAAAA" , 'w':"ABAAAAAA", 'V':"BAAAAAAA", 'v':"AAAAAABB", 'U':"AAAAABAB", 'u':"AAAABAAB", 'T':"AAABAAAB", 't':"AABAAAAB", 'S':"ABAAAAAB", 's':"BAAAAAAB", 'R':"AAAAABBB", 'r':"AAAABABB", 'Q':"AAABAABB", 'q':"AABAAABB", 'P':"ABAAAABB", 'p':"BAAAAABB", 'O':"AAAABBBB", 'o':"AAABABBB", 'N':"AABAABBB", 'n':"ABAAABBB", 'M':"BAAAABBB", 'm':"AAABBBBB", 'L':"AABABBBB", 'l':"ABAABBBB", 'K':"BAAABBBB", 'k':"AABBBBBB", 'J':"ABABBBBB", 'j':"BAABBBBB", 'I':"ABBBBBBB", 'i':"BABBBBBB", 'H':"BBBBBBBB", 'h':"AAAABBAB", 'G':"AAABABAB", 'g':"AABAABAB", 'F':"ABAAABAB", 'f':"BAAAABAB", 'E':"AAABBBAB", 'e':"AABABBAB", 'D':"ABAABBAB", 'd':"BAAABBAB", 'C':"AABBBBAB", 'c':"ABABBBAB", 'B':"BAABBBAB", 'b':"ABBBBBAB", 'A':"BABBBBAB", 'a':"BBBBBBAB", '0':"AAABBAAB", '1':"AABABAAB", '2':"ABAABAAB", '3':"BAAABAAB", '4':"AABBBAAB", '5':"ABABBAAB", '6':"BAABBAAB", '7':"ABBBBAAB", '8':"BABBBAAB", '9':"BBBBBAAB", '!':"AABBAAAB", '@':"ABABAAAB", '#':"BAABAAAB", '$':"ABBBAAAB", '%':"BABBAAAB", '&':"BBBBAAAB", '*':"BBBAAAAB", ' ':"BBAAAABB"}
    code = custom_cipher[letter]
    return code

def step4_1(text):
    encrypted = []

    for letter in text:
        code = step4_code(letter)
        encrypted.append(code)

    return ''.join(encrypted)

def step5_1(text):
    return  ''.join(format(ord(i),'b').zfill(8) for i in text)

def step6_1(text):
    return base64.b64encode(text)

def step7_1(text, key):
    rail = [['\n' for i in range(len(text))]
                  for j in range(key)]
    
    dir_down = False
    row, col = 0, 0
      
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
          
        rail[row][col] = text[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))

# text = raw_input("Plaintext: ")
# shift = int(raw_input("Shift Number: "))
# rail = int(raw_input("Second Number: "))

# for i in range(1, 8):
    # print "Step " + str(i) + ":"
    # if i == 1:
        # result = step1_1(text, shift)
    # elif i == 2:
        # result = step2_1(result)
    # elif i == 3:
        # result = step3_1(result)
    # elif i == 4:
        # result = step4_1(result)
    # elif i == 5:
        # result = step5_1(result)
    # elif i == 6:
        # result = step6_1(result)
    # else: 
        # result = step7_1(result, rail)
    # print result + "\n"
# print "Cipher Text:\n" + result
