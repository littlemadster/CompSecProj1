"""
Project 1 LanguageLetters.py 
Maddie Sirok & Valentina Colorado
CIS4367.01 
Last modified 10/20/21 more information on https://github.com/littlemadster/CompSecProj1/tree/main

Class LanguageLetters allows user to open text file, remove white spaces, and save it into a new file. 
To impliment this class use TESTER-LanguageLetter.py 
"""

class LanguageLetters:
      
  print("Running Language Letters")    
 
  def remove(string): # function to remove spaces string
    return "".join(string.replace("\n",""))
        
  def openFile(fileName): #opens and saves file without spaces in a new file
    print("running open text")
    text = open(fileName+".txt", "r")   #open original and new files
    newText =open("newFile","w")        #creates "newFile" 
    file = LanguageLetters.remove(text.read()) #calls remove function
    print(file, file=newText)           #prints contents of file into new file that stores original file minus the white space

    print(file[0:100])############################################
    newText.close() #close file
    text.close()    #close file
    
    return file    
      