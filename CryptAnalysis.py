"""
Project 1
Maddie Sirok & Valentina Colorado
"""

from LanguageLetters import LanguageLetters

class CryptAnalysis:

    '''def letterCounter(string, alphabet):

        # creates array for counter for letters and array for probabilities of letters
        letterCount = [0] * 29    

        for letterString in range(len(string)): #loops through each letter in string
            for letterAlph in range(29): #loops through each letter in alphabet
                if alphabet[letterAlph] == string[letterString]: 
                    #increase count for letter
                    letterCount[letterAlph] += 1

        return letterCount


    def printProb(string, alphabet, probAlphab): # takes string, alphabet, probability table, and size of key (int)

        lettCount = letterCounter(string, alphabet)

        for j in range(29): # loops to calculate and print probabilities
            letterProb[j] = (lettCount[j] / len(string)) * 100
            print(str(alphabet[j]) + ': ' + str("{:.4f}".format(letterProb[j])) + "\t" + alphabet[j] + ': ' + str("{:.4f}".format(probAlphab[j])))'''
 

    def branchString(fileName, key): # TODO: EDIT TO BE KEY

        keyLength = len(key)

        original = LanguageLetters.openFile(fileName)
        fileName = original[0:50] # take only the first 50 char 
        print("\n"+fileName + "\n")
        branchedString = []
        
        if keyLength == 1:
            print("Key Length = 1:")
                  
            string1 = ''
            
            for i in range(0, keyLength):
                string1 = fileName

            branchedStrings.append(string1)

        if keyLength == 2:
            print("Key Length = 2:")

            string1 = ''
            string2 = ''
            
            for i in range(0, keyLength, 2):
                string1 = fileName[i::i+2]
                string2 = fileName[i+1::i+2]

            branchedString.append(string1)
            branchedString.append(string2)
                
        if keyLength == 3:
            print("Key Length = 3:")

            string1 = ''
            string2 = ''
            string3 = ''
            
            for i in range(0, keyLength, 3):
                string1 = fileName[i::i+3]
                string2 = fileName[i+1::i+3]
                string3 = fileName[i+2::i+3]

            branchedString.append(string1)
            branchedString.append(string2)
            branchedString.append(string3)
            

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

            branchedString.append(string1)
            branchedString.append(string2)
            branchedString.append(string3)
            branchedString.append(string4)

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

            branchedString.append(string1)
            branchedString.append(string2)
            branchedString.append(string3)
            branchedString.append(string4)
            branchedString.append(string5)

    


        return branchedString
