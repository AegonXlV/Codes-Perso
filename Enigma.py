import string

alphabet_num = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

def Reassignement(liste, etalon=alphabet_num):
    L = []
    for i in liste:
        L.append(etalon[i])
    return L

def RotorsInitialisation(rotor,position):
    while rotor[0]!=position:
        rotor=rotor[-1:]+rotor[:-1]
    return rotor

                             #"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotorI_num   =  Reassignement("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
rotorII_num  =  Reassignement("AJDKSIRUXBLHWTMCQGZNPYFVOE")
rotorIII_num =  Reassignement("BDFHJLCPRTXVZNYEIWGAKMUSQO")
rotorIV_num  =  Reassignement("ESOVPZJAYQUIRHXLNFTGKDCMWB")
rotorV_num   =  Reassignement("VZBRGITYUPSDNHLXAWMJQOFECK")

rotors = [rotorI_num, rotorII_num, rotorIII_num, rotorIV_num, rotorV_num]
next_rotor_moves = [24, 19, 13, 17, 11] # = [X S M Q K]
                  # On the Window (Q E V J Z)

reflectorI_num = Reassignement("YRUHQSLDPXNGOKMIEBFZCWVJAT")
reflectorII_num = Reassignement("FVPJIAOYEDRZXWGCTKUQSBNMHL")

reflectors = [reflectorI_num, reflectorII_num]

# rt for rotor
rt=()
while len(rt)!=3:
    # entry = tuple(input("Wich rotors do youy choose ? From left to right ex : 1 2 3\n"))
    entry = ('1', ' ', '2', ' ', '3')
    for i in entry:
        if i !=" ":
            if int(i) in [1,2,3,4,5]:
                rt+=tuple(i)
rtp=()
while len(rtp)!=3:
    # entry = tuple(input("In wich position ? ex : A U X\n"))
    entry = ('E', 'A', 'B')
    for i in entry:
        if i !=" ":
            if i in string.ascii_uppercase:
                rtp+=tuple(i)

rotorA = RotorsInitialisation(rotors[int(rt[0])-1],alphabet_num[rtp[0]])
rotorB = RotorsInitialisation(rotors[int(rt[1])-1],alphabet_num[rtp[1]])
rotorC = RotorsInitialisation(rotors[int(rt[2])-1],alphabet_num[rtp[2]])
# print(rotorA)
# print(rotorB)
# print(rotorC)

# rf for reflector
# rf = int(input("Wich reflector ? (in Arabic numerals)\n"))
rf = 1
message = input("Message to code : \n")
retour=""

plugs = "QHENRMLTYSFGDVOKUI"

for entry in message: 
    
    """ 1st rotor """
    num = alphabet_num[entry] # Palcement de la lettre
    modif = rotorA[num-1]
    # print(string.ascii_uppercase[modif-1], end="")
    
    """ 2nd rotor """
    modif = rotorB[modif-1]
    # print(string.ascii_uppercase[modif-1], end="")

    """ 3rd rotor """
    modif = rotorC[modif-1]
    # print(string.ascii_uppercase[modif-1], end="")
    
    """ Reflector """
    modif = reflectors[rf-1][modif-1]
    # print(string.ascii_uppercase[modif-1], end="")
    
    """ 3rd rotor"""
    modif = rotorC[modif-1]
    # print(string.ascii_uppercase[modif-1], end="")
    
    """ 2nd rotor"""
    modif = rotorB[modif-1]
    # print(string.ascii_uppercase[modif-1], end="")
    
    """ 1st rotor"""
    modif = rotorA[modif-1]
    
    """ Affichage du resultat """
    retour +=string.ascii_uppercase[modif-1]
    # print(string.ascii_uppercase[modif-1])
    
    """ Avancement des rotors"""
    
    rotorA=rotorA[-1:]+rotorA[:-1]
    if rotorA[0]==next_rotor_moves[int(rt[0])-1]:
        rotorB=rotorB[-1:]+rotorB[:-1]
        if rotorB[0]==next_rotor_moves[int(rt[1])-1]:
            rotorC=rotorC[-1:]+rotorC[:-1]

print(retour)