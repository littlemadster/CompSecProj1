"""
Project 1
Maddie Sirok & Valentina Colorado
LanguageLetters.py
"""

class LanguageLetters:
    
    # function to remove spaces string
    def removeSpace(string):
       return "".join(string.replace("\n",""))

    # function to open and save file without spaces in a new file
    def openFile():
        
        text = open("nuDAim.txt", "r") # opens file to read
        newText =open("newFile","w") # creates new file to write

        file = removeSpace(text.read()) # removes spaces
        print(file, file=newText) 

        # closes file
        newText.close() 
        text.close()
        return file    
