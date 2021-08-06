# Section Cipher
7 Layer Cipher - Python Script 

## Main Program
The main program used is section-cipher.py, however, the encryption and decryption programs can be used separately with some light editing to the comments

### Input
Input can be provided through the command-line or by a text file
* Encryption
    * Plaintext
    * Shift Number
    * Rail Number
* Decryption
    * Cipher Text
    * Shift Number
    * Rail Number
    * Alphabet

### Output
Output can be displayed on the terminal or written to a file
* Encryption
    * Randomized Alphabet
    * Cipher Text
* Decryption
    * Plaintext

### Invalid Characters
These are characters that will not be encrypted or decrypted correctly by the program
* ^
* (
* )
* '-'
* '+'
* =
* _
* ~
* `
* '
* "

## Encryption Program
Separate Program Dedicated to Encrypting the Plaintext - enc_section_cipher.py
* Includes a Step by Step view of the Encryption
* Does not support input from a file or output to a file

## Decryption Program
Separate Program Dedicated to Decrypting the Cipher Text - dec_section_cipher.py
* Includes a Step by Step view of the Decryption
* Does not support input from a file or output to a file

## Examples
Examples of the Programs being used on basic phrases/words
* Old-Test1.txt & Old-Test2.txt
    * Test Conducted with only the Encryption Program (Includes Ciphers not Currently Used in this Version)
* Test3.txt
    * Test Conducted using the Encryption and Decryption Programs Separately
* Test4.txt
    * Test Conducted using the Main Program for both Encryption and Decryption
