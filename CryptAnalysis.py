# CryptAnalysis Class
from VigenereEncryption import mainVig


asciiLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '=', '+', '*']
asciiProb = [10.15, 1.54, 1.49, 4.70, 9.38, 2.03, 2.86, 2.09, 8.43, 0.61, 3.14, 5.28, 8.54, 3.47, 1.92, 1.84, 0.02, 5.82, 6.59, 7.69, 4.48, 2.42, 0.14, 0.16, 0.71, 0.07, 1.34, 1.80, 1.31]

def printProp(string, lettersBase, probBase):

    letterCount = [0] * 29
    letterProb = [0] * 29

    for letterString in range(len(string)): #loops through each letter in string
        for letterAlph in range(29): #loops through each letter in alphabet
            if lettersBase[letterAlph] == string[letterString]: 
                #increase count for letter
                letterCount[letterAlph] += 1

    for j in range(29):
        letterProb[j] = (letterCount[j] / len(string)) * 100
        print(str(lettersBase[j]) + ': ' + str("{:.4f}".format(letterProb[j])) + "\t" + lettersBase[j] + ': ' + str("{:.4f}".format(asciiProb[j])))
        


def main():
    str = mainVig()
    print("string received!! \n running crypto analysis: ")
    printProp(str, asciiLetters, asciiProb)
    

main()

