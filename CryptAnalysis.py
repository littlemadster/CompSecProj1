"""
Project 1
Maddie Sirok & Valentina Colorado
"""

class CryptAnalysis:

    def letterCounter(string, alphabet):

        # creates array for counter for letters and array for probabilities of letters
        letterCount = [0] * 29    

        for letterString in range(len(string)): #loops through each letter in string
            for letterAlph in range(29): #loops through each letter in alphabet
                if alphabet[letterAlph] == string[letterString]: 
                    #increase count for letter
                    letterCount[letterAlph] += 1

        return letterCount


    def printProb(string, alphabet, probAlphab): # takes string, alphabet, probability table, and size of key (int)

        lettCount = letterCounter(string, alphabet)

        for j in range(29): # loops to calculate and print probabilities
            letterProb[j] = (lettCount[j] / len(string)) * 100
            print(str(alphabet[j]) + ': ' + str("{:.4f}".format(letterProb[j])) + "\t" + alphabet[j] + ': ' + str("{:.4f}".format(probAlphab[j])))
 

            
