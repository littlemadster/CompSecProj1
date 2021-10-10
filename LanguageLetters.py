"""
Project 1
Maddie Sirok & Valentina Colorado
LanguageLetters.py
"""

class LanguageLetters:
  print("Running Language Letters")    
  # function to remove spaces string
  def remove(string):
    return "".join(string.replace("\n",""))
        
  #opens and saves file without spaces in a new file
  def openFile(fileName):
    print("running open text")
   #open original and new files
    text = open(fileName+".txt", "r")
    newText =open("newFile","w")
    file = LanguageLetters.remove(text.read())
    print(file, file=newText)
    
    print(file)
    newText.close()
    text.close()
    #return file    
      