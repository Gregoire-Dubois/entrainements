"""
le but du programme est de tranférer des données du fichier B dans le A en supprimant celle du A

"""
x=[]

y=[]

fichierA="fichierA.txt"
fichierB="fichierB.txt"

with open(fichierA, 'r') as filin1:
    li1 = filin1.read()
    x=x+list(li1)
    print(x)





