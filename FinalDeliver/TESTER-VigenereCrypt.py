"""
Project 1
TESTER FILE: VigenereCrypt.py
Maddie Sirok & Valentina Colorado
"""

from VigenereCrypt import VigenereCrypt

def main():

    asciiLetters = ['+', '=', '*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    plainText = 'COMputERseCURityPrOJEctOnE' #example plain text

    key = 'ValMa' #example key

    print("Testing encryption()")
    encryption = VigenereCrypt.encrypt(plainText, key, asciiLetters) #encrypts string
    print('e = ' + encryption  + "\n")

    print("Testing decryption()")    
    decryption = VigenereCrypt.decrypt(encryption, key, asciiLetters) #decrypts string
    print('d = ' + decryption +  "\n")    


main()
