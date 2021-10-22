"""
Project 1 TESTER FILE: LanguageLetters, Vigenere and CryptAnalysis
Maddie Sirok & Valentina Colorado
CIS4367.01
Date modified: 10/20/21

Master test file that uses all three classes and decrypts the file contents based on user cryptanalysis and key input.
"""
from LanguageLetters import LanguageLetters
from VigenereCrypt import VigenereCrypt
from CryptAnalysis import CryptAnalysis

def main():
    asciiLetters = ['+', '=', '*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    asciiProb = [ 1.80, 1.34, 1.31, 10.15, 1.54, 1.49, 4.70, 9.38, 2.03, 2.86, 2.09, 8.43, 0.61, 3.14, 5.28, 8.54, 3.47, 1.92, 1.84, 0.02, 5.82, 6.59, 7.69, 4.48, 2.42, 0.14, 0.16, 0.71, 0.07]

    
    #language letters
    print("To run LanguageLetters please input a filename that is in the same directory as both LanguageLetter.py and Tester-LanguageLetters.py")
    print("HINT: try ......'salad'")
    fileInput = input("Enter file name: ") #user input for the file name

    plaintext = LanguageLetters.openFile(fileInput)    #run LanguageLetters.py

    #cryptanalysis

    print("Testing printProb()")
    CryptAnalysis.printProb(plaintext, asciiLetters, asciiProb) #prints letter probability

    print("Testing branchString()")
    for i in range(6): #for each  key size (1-5)

        branchFile = CryptAnalysis.branchString(plaintext, i) #branches string
        branchesNum = len(branchFile) #finds number of branches

        for j in range(0, branchesNum):
            CryptAnalysis.printProb(branchFile[j], asciiLetters, asciiProb) #letter analysis/print



    #Vigenere Crypt
    print('Based off cryptanalysis you should be able to calculate the key...')
    print('HINT: try "*SUN*"')
    keyInput= input('Please Enter Key: ') #user inputs key

    print("Testing decryption()")    
    decryption = VigenereCrypt.decrypt(plaintext, keyInput, asciiLetters) #decrypts string
    print("Decryption is saved into a new text file named decryptedText.txt")
    decryptionText =open("decryptedText.txt","w") #opens new file where decrytion is saved 
    decryptionText.write(decryption) #writes contents to file

    print('First 100 decrypted characters: ' + decryption[0:100] +  "\n") 

    decryptionText.close()

main()
