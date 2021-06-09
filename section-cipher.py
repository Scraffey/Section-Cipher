import base64

def step1(text, s):
    result = ""
    for i in range (len(text)):
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

def step2(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = "fcpevqkzgmtrayonujdlwhbxsi"
    result = ""
    for letter in text:
        if letter.lower() in alphabet:
            result += key[alphabet.find(letter.lower())]
        else:
            result += letter
    return result

def step3(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = "zyxwvutsrqponmlkjihgfedcba"
    result = ""
    for letter in text:
        if letter.lower() in alphabet:
            result += key[alphabet.find(letter.lower())]
        else:
            result += letter
    return result

def step4_code(letter):
    custom_cipher = { 'Z':"ABBAA", 'z':"ABBAA", 'Y':"AAABA", 'y':"AAABA", 'X':"ABABA", 'x': "ABABA", 'W':"AABBA" , 'w':"AABBA", 'V':"ABBBA", 'v':"ABBBA", 'U':"BAAAA", 'u':"BAAAA", 'T':"BBAAA", 't':"BBAAA", 'S':"BABAA", 's':"BABAA", 'R':"BBBAA", 'r':"BBBAA", 'Q':"BAABA", 'q':"BAABA", 'P':"BBABA", 'p':"BBABA", 'O':"BABBA", 'o':"BABBA", 'N':"BBBBA", 'n':"BBBBA", 'M':"AAAAB", 'm':"AAAAB", 'L':"ABAAB", 'l':"ABAAB", 'K':"AABAB", 'k':"AABAB", 'J':"ABBAB", 'j':"ABBAB", 'I':"AAABB", 'i':"AAABB", 'H':"ABABB", 'h':"ABABB", 'G':"AABBB", 'g':"AABBB", 'F':"ABBBB", 'f':"ABBBB", 'E':"BAAAB", 'e':"BAAAB", 'D':"BBAAB", 'd':"BBAAB", 'C':"BABAB", 'c':"BABAB", 'B':"BBBAB", 'b':"BBBAB", 'A':"BAABB", 'a':"BAABB"}
    
    code = custom_cipher[letter]
    return code

def step4(text):
    custom_cipher = { 'Z':"ABBAA", 'z':"ABBAA", 'Y':"AAABA", 'y':"AAABA", 'X':"ABABA", 'x': "ABABA", 'W':"AABBA" , 'w':"AABBA", 'V':"ABBBA", 'v':"ABBBA", 'U':"BAAAA", 'u':"BAAAA", 'T':"BBAAA", 't':"BBAAA", 'S':"BABAA", 's':"BABAA", 'R':"BBBAA", 'r':"BBBAA", 'Q':"BAABA", 'q':"BAABA", 'P':"BBABA", 'p':"BBABA", 'O':"BABBA", 'o':"BABBA", 'N':"BBBBA", 'n':"BBBBA", 'M':"AAAAB", 'm':"AAAAB", 'L':"ABAAB", 'l':"ABAAB", 'K':"AABAB", 'k':"AABAB", 'J':"ABBAB", 'j':"ABBAB", 'I':"AAABB", 'i':"AAABB", 'H':"ABABB", 'h':"ABABB", 'G':"AABBB", 'g':"AABBB", 'F':"ABBBB", 'f':"ABBBB", 'E':"BAAAB", 'e':"BAAAB", 'D':"BBAAB", 'd':"BBAAB", 'C':"BABAB", 'c':"BABAB", 'B':"BBBAB", 'b':"BBBAB", 'A':"BAABB", 'a':"BAABB"}
    encrypted = []

    for letter in text:
        code = step4_code(letter)
        encrypted.append(code)

    return ''.join(encrypted)

def step5(text):
    return  ' '.join(format(ord(i),'b').zfill(8) for i in text)

def step6(text):
    return base64.b64encode(text)

def alphabet_position(letter):
    alphabet_pos = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3,
'd':3, 'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8,
'i':8, 'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12,
'N': 13, 'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16,
'R':17, 'r':17, 'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21,
'v':21, 'W':22, 'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25
}
    pos = alphabet_pos[letter]
    return pos

def rotate(letter, rot):
    shift = 97 if letter.islower() else 65
    return chr((ord(letter) + rot - shift) % 26 + shift)

def step7(text, key):
    alphabet_pos = {'A':0, 'a':0, 'B':1, 'b':1, 'C':2, 'c':2, 'D':3, 'd':3,
'E':4, 'e':4, 'F':5, 'f':5, 'G':6, 'g':6, 'H':7, 'h':7, 'I':8, 'i':8,
'J':9, 'j':9, 'K':10, 'k':10, 'L':11, 'l':11, 'M':12, 'm':12, 'N': 13,
'n':13, 'O':14, 'o':14, 'P':15, 'p':15, 'Q':16, 'q':16, 'R':17, 'r':17,
'S':18, 's':18, 'T':19, 't':19, 'U':20, 'u':20, 'V':21, 'v':21, 'W':22,
'w':22, 'X':23, 'x':23, 'Y':24, 'y':24, 'Z':25, 'z':25 }
    encrypted = []    
    starting_index = 0
    for letter in text:
        rotation = alphabet_position(key[starting_index])
    
        if not letter in alphabet_pos:
            encrypted.append(letter)
        elif letter.isalpha():            
            encrypted.append(rotate(letter, rotation))

        if starting_index == (len(key) - 1): 
            starting_index = 0
        else: 
            starting_index += 1

    return ''.join(encrypted)  

def step8(text, key):
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

text = raw_input("Word(s) or Phrase(s) to Encrypt: ")
s = int(raw_input("Shift Number: "))
key = raw_input("Key: ")
key2 = int(raw_input("Second Key: "))
print "\n"

for i in range(1, 9):
    print "Step " + str(i) + ": ",
    if i == 1:
        result = step1(text, s)
    elif i == 2:
        result = step2(result)
    elif i == 3:
        result = step3(result)
    elif i == 4:
        result = step4(result)
    elif i == 5:
        result = step5(result)
    elif i == 6:
        result = step6(result)
    elif i == 7:
        result = step7(result, key)
    else: 
        result = step8(result, key2)
    print result
