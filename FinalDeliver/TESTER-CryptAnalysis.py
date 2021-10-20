"""
Project 1 TESTER FILE: CryptAnalysis.py
Maddie Sirok & Valentina Colorado
CIS4367.01
Date modified: 10/20/21

TESTER FILE for class CryptAnalysis.py
Tests each method in class
"""

from CryptAnalysis import CryptAnalysis

def main():

    #language and letter probabilities
    asciiLetters = ['+', '=', '*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    asciiProb = [ 1.80, 1.34, 1.31, 10.15, 1.54, 1.49, 4.70, 9.38, 2.03, 2.86, 2.09, 8.43, 0.61, 3.14, 5.28, 8.54, 3.47, 1.92, 1.84, 0.02, 5.82, 6.59, 7.69, 4.48, 2.42, 0.14, 0.16, 0.71, 0.07]

    string = "ALIDOVIADOFIHSGOJHSPOIUFRHWSOR"
    print("Testing printProb()")
    CryptAnalysis.printProb(string, asciiLetters, asciiProb) #prints letter probability

    print("Testing calcProb()")
    print(CryptAnalysis.calcProb(string, asciiLetters)) #prints list of letter probabilities

    print("Testing branchString()")
    for i in range(6): #for each  key size (1-5)

        branchFile = CryptAnalysis.branchString(string, i) #branches string
        branchesNum = len(branchFile) #finds number of branches

        for k in range(len(branchFile)): 
            print(branchFile[k]) #prints each branch

        for j in range(0, branchesNum):
            CryptAnalysis.printProb(branchFile[j], asciiLetters, asciiProb) #letter analysis/print

main()
