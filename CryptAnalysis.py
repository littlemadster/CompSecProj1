"""
Project 1
Maddie Sirok & Valentina Colorado
"""

class CryptAnalysis:

    def printProb(string, lettersBase, probBase):

        letterCount = [0] * 29
        letterProb = [0] * 29

        for letterString in range(len(string)): #loops through each letter in string
            for letterAlph in range(29): #loops through each letter in alphabet
                if lettersBase[letterAlph] == string[letterString]: 
                    #increase count for letter
                    letterCount[letterAlph] += 1

        for j in range(29):
            letterProb[j] = (letterCount[j] / len(string)) * 100
            print(str(lettersBase[j]) + ': ' + str("{:.4f}".format(letterProb[j])) + "\t" + lettersBase[j] + ': ' + str("{:.4f}".format(probBase[j])))
            

