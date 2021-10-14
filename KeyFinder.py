"""
project 1 
KeyFinder.py
Maddie Sirok && Valentina Colorado
"""

from LanguageLetters import LanguageLetters

class KeyFinder:

    def main(fileName,keyLength):


        #print original string
        original = LanguageLetters.openFile(fileName)
        originalSplit = original[0:50] # take only the first 50 char 
        print("\n"+originalSplit)

        for i in range(keyLength): #print sequence and shift i spaces 
            print("Sequence",i,originalSplit[i:] +originalSplit[:i])
         


        #need to calculate IC

        return originalSplit




