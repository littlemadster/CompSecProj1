class open_text:
#function to remove spaces string
    def remove(string):
        return "".join(string.split())
        
    
#opens and saves file without spaces in a new file
    text = open("nuDAim.txt", "r")
    newText =open("newFile","w")
    print(remove(text.read()), file=newText)

    newText.close()
    text.close()

    
