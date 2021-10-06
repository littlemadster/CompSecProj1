"""
Project 1
Encrypt & Decrypt Vigenere Cipher
"""
import math
from openText import open_text

#asciiValues[29] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
asciiLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '=', '+', '*']


# y = e + k mod 26
def encrypt(plainT, keyS): #function takes plaintext letter and key letter
    plainT = plainT.upper()
    keyS = keyS.upper()
    cipherText = ''
    plain = 0
    key = 0
    cipher = 0
    
    for letter in range(len(plainT)):
        
        for i in range(29): # gets ascii numeric for plaintext
            if asciiLetters[i] == plainT[letter]:
                plain = i
        #print('plain: ' + str(plain))
        
        for j in range(29): # gets ascii numeric for key
            if asciiLetters[j] == keyS[letter % len(keyS)]:
                key = j
        #print('key: ' + str(key))

        cipher = (plain + key) % 29
        
        cipherText += asciiLetters[cipher]


    return(cipherText)
    #return letter value of asciiLetters[c]

def decrypt(cipherT, keyS):

    cipherT = cipherT.upper()
    keyS = keyS.upper()
    plainText = ''
    plain = 0
    key = 0
    cipher = 0

    for letter in range(len(cipherT)):

       
        for i in range(29): # gets ascii numeric for plaintext
            if asciiLetters[i] == cipherT[letter]:
                cipher = i
        #print('cipher: ' + str(cipher))
        
        for j in range(29): # gets ascii numeric for key
            if asciiLetters[j] == keyS[letter % len(keyS)]:
                key = j
        #print('key: ' + str(key))

        plain = (cipher - key) % 29
        
        plainText += asciiLetters[plain]


    return(plainText)
    
    

def mainVig():
    textFile = open_text()
    plainText = textFile
   # print(plainText)
    key = 'lee'
   # print('encrypt:')
    encryption = encrypt(plainText, key)
    #print('decrypt:')
    decryption = decrypt(encryption, key)
  #  print('e = ' + encryption)
   # print('d = ' + decryption)
    print("sending over string for cryptanalysis..")
    return decryption
    


mainVig()

