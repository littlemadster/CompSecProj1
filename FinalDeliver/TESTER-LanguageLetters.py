"""
Project 1
Tester File: LanguageLetters.py
By Maddie Sirok && Valentina Colorado
CIS4367.01 
Last modified 10/20/21

TESTER FILE for LanguageLetters.py
Tests each method in class
"""
from LanguageLetters import LanguageLetters


def main():
    print("To run LanguageLetters please input a filename that is in the same directory as both LanguageLetter.py and Tester-LanguageLetters.py")
    fileInput = input("Enter file name: ") #user input for the file name

    LanguageLetters.openFile(fileInput)    #run LanguageLetters.py
   
main()