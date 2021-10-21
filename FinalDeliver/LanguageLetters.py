"""
Project 1 LanguageLetters.py 
Maddie Sirok & Valentina Colorado
CIS4367.01 
Last modified 10/20/21

Class LanguageLetters allows user to open text file, remove white spaces, and save it into a new file. 
To impliment this class use TESTER-LanguageLetter.py 
"""

from typing import NewType
import re

class LanguageLetters:
      
  print("Running Language Letters")    
 
  def remove(string): # function to remove spaces string
    pattern = re.compile(r'\s+') #removes 
    string = re.sub(pattern,'',string)
    return string
        
  def openFile(fileName): #opens and saves file without spaces in a new file
    print("\nrunning LanguageLetters.py ")
    text = open(fileName+".txt", "r")   #open original and new files
    newText =open("newFile","w")        #creates "newFile" 
    file = LanguageLetters.remove(text.read()) #calls remove function
    print(file, file=newText)           #prints contents of file into new file that stores original file minus the white space
    
    print(file[0:300])
    newText.close() #close file
    text.close()    #close file
    
    return file    
      