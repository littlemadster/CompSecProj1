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

 #need to calculate IC
        for i in range (keyLength):
                print("If key length were: ",i)
                for j in range (i+1): #print sequence and shift i spaces 
                    print("Sequence",j,originalSplit[j:] +originalSplit[:j])
                    
            

        return originalSplit
        
   