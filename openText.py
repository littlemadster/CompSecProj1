from os import remove

class one_text():
    print("opening file...")
#function to remove spaces string
def remove(string):
   return "".join(string.replace("\n",""))
        
    #opens and saves file without spaces in a new file
def one_text():
    #open original and new files
    text = open("nuDAim.txt", "r")
    newText =open("newFile","w")

    file = remove(text.read())
    print(file, file=newText)
        
    newText.close()
    text.close()
    return file    
    
one_text()
    
