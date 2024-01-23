import time
#dictionary for scrambled rotors
alphadict={
    "A": "B", "B": "C", "C": "D", "D": "E", "E": "F",
    "F": "G", "G": "H", "H": "I", "I": "J", "J": "K",
    "K": "L", "L": "M", "M": " ", "N": "O", "O": "P",
    "P": "Q", "Q": "R", "R": "S", "S": "T", "T": "U",
    "U": "V", "V": "W", "W": "X", "X": "Y", "Y": "Z",
    "Z": "A", " ": "N"
}
#converting number to alphabet
numberToAlpha={
    1: "B", 2: "C", 3: "D", 4: "E", 5: "F",
    6: "G", 7: "H", 8: "I", 9: "J", 10: "K",
    11: "L", 12: "M", 13: "N", 14: "O", 15: "P",
    16: "Q", 17: "R", 18: "S", 19: "T", 20: "U",
    21: "V", 22: "W", 23: "X", 24: "Y", 25: "Z",
    0: "A", 26: " "
}
#converting alphabet to number
alphaToNumber={
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4,
    "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
    "K": 10, "L": 11, "M": 12, "N": 13, "O": 14,
    "P": 15, "Q": 16, "R": 17, "S": 18, "T": 19,
    "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24,
    "Z": 25, " ": 26
}
#reflector for bouncing back signal(for commutativity)
reflector={
    "A": "Z", "B": "Y", "C": "X", "D": "W", "E": "V",
    "F": "U", "G": "T", "H": "S", "I": "R", "J": "Q",
    "K": "P", "L": "O", "M": "N", "N": "M", "O": "L",
    "P": "K", "Q": "J", "R": "I", "S": "H", "T": "G",
    "U": "F", "V": "E", "W": "D", "X": "C", "Y": "B",
    "Z": "A", " ": " "
}
#asking the counter values
print("Enter a value for rotor-1 :")
rotorPosition1=int(input()) 
print("Enter a value for rotor-2 :")
rotorPosition2=int(input()) 
print("Enter a value for rotor-3 :")
rotorPosition3=int(input()) 
rotorCount1=0
rotorCount2=0
rotorCount3=0
#declaration of an empty for storing output
output=[]
#function to retrieve key value from dictionary
def get_key(val):
    for key, value in alphadict.items():
         if val == value:
             return key
print("Enter a SENTENCE to encrypt or decrypt in UPPERCASE:")
sentence=input() #taking input
sentence=sentence+'/' #adding '/' as termination character
counter=0 #initializing counter for letter input
while(True):
    letter=sentence[counter]
    if(letter=="/"):
        break
    #input rotor
    inputrotor=alphadict[letter]
    alphaTonumber0=(alphaToNumber[inputrotor]+rotorPosition1)%27 #alpha to number within 26
    numberToAlpha0=numberToAlpha[alphaTonumber0] #number to alpha
    #rotor 2 
    rotor1=alphadict[numberToAlpha0]
    alphaTonumber1=((alphaToNumber[rotor1]+rotorPosition2)%27) #alpha to number within 26
    numberToAlpha1=numberToAlpha[alphaTonumber1] #number to alpha 
    #rotor 3
    rotor2=alphadict[numberToAlpha1]
    alphaTonumber2=((alphaToNumber[rotor2]+rotorPosition3)%27) #alpha to number within 26
    numberToAlpha2=numberToAlpha[alphaTonumber2]
    #reflector
    back=reflector[numberToAlpha2]
    #rotor back 3
    alphaToNumberBack2=(alphaToNumber[back]-rotorPosition3)%27
    numberToAlphaBack2=numberToAlpha[alphaToNumberBack2]
    rotor3_back=get_key(numberToAlphaBack2)
    #rotor back 2
    alphaToNumberBack1=(alphaToNumber[rotor3_back]-rotorPosition2)%27
    numberToAlphaBack1=numberToAlpha[alphaToNumberBack1]
    rotor2_back=get_key(numberToAlphaBack1)
    #rotor back 1
    alphaToNumberBack0=(alphaToNumber[rotor2_back]-rotorPosition1)%27
    numberToAlphaBack0=numberToAlpha[alphaToNumberBack0]
    rotor1_back=get_key(numberToAlphaBack0)
    rotorPosition1+=1
    if(rotorPosition1%27==0): #fastest rotor (this will reset after 27th ) rotorCount1
        rotorPosition1=1 #resetting rotor1 position
        #rotorCount1+=1
        rotorPosition2+=1
        if(rotorPosition2%27==0): #medium rotor
            rotorPosition2=1 #resetting rotor2 position
            #rotorCount2+=1
            rotorPosition3+=1
            if(rotorPosition3%27==0): #slowest rotor
                rotorPosition3=1 #resetting rotor3 position
                #rotorCount3+=1
            
    output.append(rotor1_back)
    counter+=1

print("Your encoded/decoded message is displaying:")
#printing message in a single line
word=''.join(str(letters) for letters in output)
print(word)
time.sleep(10)    


