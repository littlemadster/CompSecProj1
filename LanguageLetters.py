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
        textTest = open("testText.txt", "r") # TESTER FILE
        newText =open("newFile","w") # creates new file to write

        file = removeSpace(text.read()) # removes spaces
        fileTest = removeSpace(testText.read()) # TESTER FILE
        print(file, file=newText) 

        # closes file
        newText.close() 
        testText.close() # TESTER FILE
        text.close()
        
        return fileTest # TESTER FILE
        #return file    
