from enc_section_cipher import *
from dec_section_cipher import * 

def input_file():
    file_name = raw_input("What is the name of the input File? ")
    f = open(file_name, 'r')
    text = f.read()
    f.close()
    return text

def output_file(result):
    file_name = raw_input("What would you like to call the output File? ")
    f = open(file_name, 'w')
    f.write(result)
    f.close
    return

def encrypt():
    ftf = raw_input("Input Plaintext Through the Command-Line (C) or a File (F)? ")
    otf = raw_input("Output Cipher Text into a File (Y/N)? ")

    if ftf == 'F' or ftf == 'f':
        text = input_file()
        print "Plaintext:\n" + text
    else:
        text = raw_input("Plaintext: ")

    shift = int(raw_input("Shift Number: ")) 
    rail = int(raw_input("Rail Number: "))

    for i in range(1, 8):
        if i == 1:
            result = step1_1(text, shift)
        elif i == 2:
            result = step2_1(result)
        elif i == 3:
            result = step3_1(result)
        elif i == 4:
            result = step4_1(result)
        elif i == 5:
            result = step5_1(result)
        elif i == 6:
            result = step6_1(result)
        else:
            result = step7_1(result, rail)

    if otf == 'Y' or otf == 'y':
        output_file(result)
    print "\nCipher Text:\n" + result
    return

def decrypt():
    ftf = raw_input("Input Cipher Text Through Command-Line (C) or a File (F)? ")
    otf = raw_input("Output Plaintext into a File (Y/N)? ")

    if ftf == 'F' or ftf == 'f':
        text = input_file()
        print "Cipher Text:\n" + text
    else:
        text = raw_input("Cipher Text: ")

    shift = int(raw_input("Shift Number: "))
    rail = int(raw_input("Rail Number: "))
    alpha = raw_input("Alphabet: ")

    for i in range(1, 8):
        if i == 1:
            result = step1_2(text, rail)
        elif i == 2:
            result = step2_2(result)
        elif i == 3:
            result = step3_2(result)
        elif i == 4:
            result = step4_2(result)
        elif i == 5:
            result = step5_2(result)
        elif i == 6:
            result = step6_2(result, alpha)
        else:
            result = step7_2(result, shift)

    if otf == 'Y' or otf == 'y':
        output_file(result)
    print "\nPlaintext:\n" + result
    return

def info():
    print "-Encryption-\t\t\t\t-Decryption-"
    print "\nRequirements:\t\t\t\tRequirements:"
    print "-Shift Key",
    print "\t\t\t\t-Cipher Text"
    print "-Rail Key",
    print "\t\t\t\t-Shift Key"
    print "\t\t\t\t\t-Rail Key"
    print "Invalid Characters:",
    print "\t\t\t-Alphabet"
    print "-,^,(,),-,+,=,_,~,`,\',\""

exit = 0

print "\n   _____           __  _                _______       __             \n  / ___/___  _____/ /_(_)___  ____     / ____(_)___  / /_  ___  _____\n  \__ \/ _ \/ ___/ __/ / __ \/ __ \   / /   / / __ \/ __ \/ _ \/ ___/\n ___/ /  __/ /__/ /_/ / /_/ / / / /  / /___/ / /_/ / / / /  __/ /    \n/____/\___/\___/\__/_/\____/_/ /_/   \____/_/ .___/_/ /_/\___/_/     \n                                           /_/                       "

print "\nWelcome to Section Encryption!"
while exit == 0:
    choice = raw_input("\nWould You Like to Encrypt (E), Decrypt (D), Get Information (I), or Quit (Q)? ")
    if choice == 'E' or choice == 'e':
        print "\n----Encription----"
        encrypt()
    elif choice == 'D' or choice == 'd':
        print "\n----Decryption----"
        decrypt()
    elif choice == 'I' or choice == 'i':
        print "\n----Information----"
        info()
    elif choice == 'Q' or choice == 'q':
        print "\n----Quiting----"
        exit = 1
    else:
        print "\n----Invalid Input----"
