"""
A partir d'une liste, compléter une seconde dans laquelle il y a des blancs

"""

listeA = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

listeB = ["a","","c","d","","f","","h","i","j","","l","m","n","o","p","","","","t","u","v","w","x","y",""]

listeC= []
for i, j in zip(listeA, listeB) :
    if i == j :
        listeC = listeC, i
    elif i or j == "":
        listeC = listeC, i

print(listeC)

