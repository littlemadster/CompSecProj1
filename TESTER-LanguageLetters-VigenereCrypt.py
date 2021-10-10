"""
project 1 
TESTER-LanguageLetters and VigenereCrypt

Maddie Sirok && Valentina Colorado
"""
from LanguageLetters import LanguageLetters
from VigenereCrypt import VigenereCrypt

def main():
    #run LanguageLetters
    file = LanguageLetters.openFile("wordFile")

    #run VigenereCrypt
    asciiLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '=', '+', '*']

    plainText = file

    key = 'lee'
    encryption = VigenereCrypt.encrypt(plainText, key, asciiLetters)
    decryption = VigenereCrypt.decrypt(encryption, key, asciiLetters)
    print('e =\n' + encryption)
    print('d =\n' + decryption)    



main()
