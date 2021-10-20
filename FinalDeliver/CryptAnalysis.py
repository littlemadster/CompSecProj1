"""
Project 1 CryptAnalysis.py
Maddie Sirok & Valentina Colorado
CIS4367.01
Last modified: 10/20/21

Class that will analyze the text by calculating letter frequency
Referece TESTER-CryptAnalysis.py to see the testing implementation for each method 
"""

from LanguageLetters import LanguageLetters #reference to open file
import math

class CryptAnalysis:

    def letterCounter(string, alphabet): #takes string and alphabet and dscounts the frequency of letters

        letterCount = [0] * 29 #creates list for counter for letters and array for probabilities of letters   

        for letterString in range(len(string)): #loops through each letter in string
            for letterAlph in range(29): #loops through each letter in alphabet
                if alphabet[letterAlph] == string[letterString]: #checks which letter it is
                    letterCount[letterAlph] += 1 #increase count for letter

        return letterCount #returns list of all letter frequencies


    def printProb(string, alphabet, probAlphab): # takes string, alphabet, alphabet frequency to print probility table

        lettCount = CryptAnalysis.letterCounter(string, alphabet) #calls letterCount
        letterProb = [0] * 29 #create list of length 29 to store probability in

        for j in range(29): # loops to calculate and print probabilities
            letterProb[j] = (lettCount[j] / len(string)) * 100 #calculates probability of letter
            print(str(alphabet[j]) + ': ' + str("{:.4f}".format(letterProb[j])) + "\t" + alphabet[j] + ': ' + str("{:.4f}".format(probAlphab[j]))) #prints table for letter
        print('\n')
        

    def calcProb(string, alphabet): # takes string and alphabet to calculate probability independent of printing

        lettCount = CryptAnalysis.letterCounter(string, alphabet) #calls letterCount
        letterProb = [0] * 29 #create list of length 29 to store probability in

        for j in range(29): # loops to calculate and print probabilities
            letterProb[j] = (lettCount[j] / len(string)) * 100 #calculates probability of letter

        return letterProb #returns list of letter frequency in %

    def branchString(stringFile, keyLength): #branches the file based on key size to analyze for key length
        
        branchedString = [] * keyLength
        fileName = stringFile

        #CASE: for each key length 1-5
        #creates empty string for each branch, saves respective ith +...+ ith+n letter in it, then adds strings to a list
        if keyLength == 1:
            print("Key Length = 1:")
                  
            string1 = ''
            
            for i in range(0, keyLength):
                string1 = fileName

            branchedString.append(string1)

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

        return branchedString #retuns list of each branched string

            
