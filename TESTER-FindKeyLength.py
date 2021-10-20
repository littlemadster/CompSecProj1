'''
TESTER-FindKeyLength
Maddie Sirok & Valentina Colorado
'''

from CryptAnalysis import CryptAnalysis
#from LanguageLetters import LanguageLetters
from VigenereCrypt import VigenereCrypt

def main():

    #file = LanguageLetters.openFile("salad")

    #run VigenereCrypt
    asciiLetters = [ '=', '+', '*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    asciiProb = [1.34, 1.80, 1.31, 10.15, 1.54, 1.49, 4.70, 9.38, 2.03, 2.86, 2.09, 8.43, 0.61, 3.14, 5.28, 8.54, 3.47, 1.92, 1.84, 0.02, 5.82, 6.59, 7.69, 4.48, 2.42, 0.14, 0.16, 0.71, 0.07]

    key = 'lee'

    for i in range(6):

        branchFile = CryptAnalysis.branchString('salad', i)
        branchesNum = len(branchFile)

        for k in range(len(branchFile)):
            print(branchFile[k])

        for j in range(0, branchesNum):
            CryptAnalysis.printProb(branchFile[j], asciiLetters, asciiProb)

    
main()
