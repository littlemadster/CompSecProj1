"""
Project 1 VigenereCrypt.py
Maddie Sirok & Valentina Colorado
CIS4367.01
Last modified: 10/20/21

Class that will encrypt & decrypt using the Vigenere Cipher
Use TESTER-VigenereCrypt.py to run the encryption and decryption functions

"""

class VigenereCrypt:
    
    # y = e + k mod 29
    def encrypt(plainT, keyS, asciiLetters): #function takes plaintext, key, and alphabet
        
        plainT = plainT.upper() #makes plaintext all uppercase
        keyS = keyS.upper() #makes key all uppercase
        cipherText = '' #creates empty string for ciphertext to be created
        
        #indicies for converting letter to ascii code
        plain = 0
        key = 0 
        cipher = 0
        
        for letter in range(len(plainT)): #loop for length of the plaintext
            
            for i in range(29): #gets ascii numeric for plaintext
                if asciiLetters[i] == plainT[letter]:
                    plain = i #letter converts to ascii
                    
            #print('plain: ' + str(plain)) #prints ascii of letter (TESTING PURPOSES)
            
            for j in range(29): # gets ascii numeric for key
                if asciiLetters[j] == keyS[letter % len(keyS)]:
                    key = j

            #print('key: ' + str(key)) #prints ascii of letter (TESTING PURPOSES)

            cipher = (plain + key) % 29 # encryption algorithm to solve for cipherText index
            
            cipherText += asciiLetters[cipher] # appends letter to ciphertext string


        return(cipherText) #returns cipherText string


    # y = c - k mod 29
    def decrypt(cipherT, keyS, asciiLetters): #function takes ciphertext, key, and alphabet

        cipherT = cipherT.upper() # makes ciphertext all uppercase
        keyS = keyS.upper() # makes key all uppercase
        plainText = '' # empty string for plaintext to be appended to

        # indicies for converting letter to ascii code
        plain = 0
        key = 0
        cipher = 0

        for letter in range(len(cipherT)): #loop for  length of ciphertext
           
            for i in range(29): # gets ascii numeric for ciphertext
                if asciiLetters[i] == cipherT[letter]:
                    cipher = i
            
            #print('cipher: ' + str(cipher)) #prints ascii of letter (TESTING PURPOSES)
            
            for j in range(29): # gets ascii numeric for key
                if asciiLetters[j] == keyS[letter % len(keyS)]:
                    key = j
            
            #print('key: ' + str(key))  #prints ascii of letter (TESTING PURPOSES)

            plain = (cipher - key) % 29 # decryption algorithm ot solve for cipherText index
            
            plainText += asciiLetters[plain] # appends letter to plaintext string


        return(plainText) #returns cipherText string


