"""
Project 1
TESTER FILE: VigenereCrypt.py
Maddie Sirok & Valentina Colorado
"""

from VigenereCrypt import VigenereCrypt

def main():

    asciiLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '=', '+', '*']

    plainText = 'MYLITTLEPONY'

    key = 'lee'
    encryption = VigenereCrypt.encrypt(plainText, key, asciiLetters)
    decryption = VigenereCrypt.decrypt(encryption, key, asciiLetters)
    print('e = ' + encryption)
    print('d = ' + decryption)    


main()
