"""
écrire une fonction qui prend une chaine de caractères et enlève les voyelles.

Résolu

"""
def voyelle() :
    entree = input("tapez votre message")
    sortie = ""
    for i in entree :
        if i == "a" or i =="e" or i == "i" or i == "o" or i == "u" or i == "y" :
            pass
        else:
            sortie = sortie + i

    print(sortie)

