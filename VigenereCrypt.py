"""
Project 1
Maddie Sirok & Valentina Colorado
Class that will encrypt & decrypt using the Vigenere Cipher
"""

class VigenereCrypt:
    
    # y = e + k mod 29
    def encrypt(plainT, keyS, asciiLetters): #function takes plaintext letter and key letter
        
        plainT = plainT.upper() # makes plaintext all uppercase
        keyS = keyS.upper() # makes key all uppercase
        cipherText = '' # creates empty string for ciphertext to be created
        
        # indicies for converting letter to ascii code
        plain = 0
        key = 0 
        cipher = 0
        
        for letter in range(len(plainT)): # loop for length of the plaintext
            
            for i in range(29): # gets ascii numeric for plaintext
                if asciiLetters[i] == plainT[letter]:
                    plain = i # letter converts to ascii
            # prints ascii of letter (TESTING PURPOSES)
            #print('plain: ' + str(plain))
            
            for j in range(29): # gets ascii numeric for key
                if asciiLetters[j] == keyS[letter % len(keyS)]:
                    key = j
            # prints ascii of letter (TESTING PURPOSES)
            #print('key: ' + str(key))

            cipher = (plain + key) % 29 # encryption algorithm
            
            cipherText += asciiLetters[cipher] # adds encrypted letter to ciphertext string


        return(cipherText)
        #return letter value of asciiLetters[c]

    # y = c - k mod 29
    def decrypt(cipherT, keyS, asciiLetters):

        cipherT = cipherT.upper() # makes ciphertext all uppercase
        keyS = keyS.upper() # makes key all uppercase
        plainText = '' # empty string for plaintext to be appended to

        # indicies for converting letter to ascii code
        plain = 0
        key = 0
        cipher = 0

        for letter in range(len(cipherT)):

           
            for i in range(29): # gets ascii numeric for plaintext
                if asciiLetters[i] == cipherT[letter]:
                    cipher = i
            # prints ascii of letter (TESTING PURPOSES)
            #print('cipher: ' + str(cipher))
            
            for j in range(29): # gets ascii numeric for key
                if asciiLetters[j] == keyS[letter % len(keyS)]:
                    key = j
            # prints ascii of letter (TESTING PURPOSES)
            #print('key: ' + str(key))

            plain = (cipher - key) % 29 # decryption algorithm
            
            plainText += asciiLetters[plain] # appends plaintext to plaintext string


        return(plainText)
        #return letter value of asciiLetters[c]

