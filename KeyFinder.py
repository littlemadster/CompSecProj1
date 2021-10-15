"""
project 1 
KeyFinder.py
Maddie Sirok && Valentina Colorado
"""

from LanguageLetters import LanguageLetters

class KeyFinder:


    def findKeyLength(fileName, keyLength): # TODO: EDIT TO BE KEY

        keyLength = keyLength

        original = LanguageLetters.openFile(fileName)
        fileName = original[0:50] # take only the first 50 char 
        print("\n"+fileName + "\n")
        
        if keyLength == 1:
            print("Key Length = 1:")
                  
            string1 = ''
            
            for i in range(0, keyLength):
                string1 = fileName
            print(string1)

        if keyLength == 2:
            print("Key Length = 2:")

            string1 = ''
            string2 = ''
            
            for i in range(0, keyLength, 2):
                string1 = fileName[i::i+2]
                string2 = fileName[i+1::i+2]
                
            print(string1)
            print(string2)
                
        if keyLength == 3:
            print("Key Length = 3:")

            string1 = ''
            string2 = ''
            string3 = ''
            
            for i in range(0, keyLength, 3):
                string1 = fileName[i::i+3]
                string2 = fileName[i+1::i+3]
                string3 = fileName[i+2::i+3]
                
            print(string1)
            print(string2)
            print(string3)
            

        if keyLength == 4:
            print("Key Length = 4:")

            string1 = ''
            string2 = ''
            string3 = ''
            string4 = ''
            
            for i in range(0, keyLength, 4):
                string1 = fileName[i::i+4]
                string2 = fileName[i+1::i+4]
                string3 = fileName[i+2::i+4]
                string4 = fileName[i+3::i+4]
                
            print(string1)
            print(string2)
            print(string3)
            print(string4)

        if keyLength == 5:
            print("Key Length = 5:")

            string1 = ''
            string2 = ''
            string3 = ''
            string4 = ''
            string5 = ''
            
            for i in range(0, keyLength, 5):
                string1 = fileName[i::i+5]
                string2 = fileName[i+1::i+5]
                string3 = fileName[i+2::i+5]
                string4 = fileName[i+3::i+5]
                string5 = fileName[i+4::i+5]
                
            print(string1)
            print(string2)
            print(string3)
            print(string4)
            print(string5)
        
   
