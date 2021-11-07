"""
Jeu du pendu
A ajouter :
    on comptabilise les points
    afficher un dessin de pendu
"""
from random import randrange

mot_secret =""# varialbe du mot secret
essai = ""
tentative = 0
caractere = 0
bibli = ["tulipe", "rose", "cerise", "jacinthes", "pelouse"]
ln_essai=0
result_masque=""
tours = 8
x=0
jeu = True
joueur = ""
print("Quel est votre prénom ?")
joueur = input("Entrez votre prénom ")

while jeu:
    chances = 8
    print("Bonjour",joueur)
    b= len(bibli) #longeur du mot secret
    d = randrange(0, b)# générateur d'un nombre aléatoire dans la limite du nombre de mots dans le dictionnaire
    mot_secret = bibli[d] #désignation du mot secret
    print(mot_secret)
    masque = list(mot_secret) #attribue la valeur du mot secret au masque
    ln_masque =len(masque)

    for i, l in enumerate(mot_secret):
        masque[i] = "*"
    result_masque = ''.join(masque)
    print("Le mot à découvrir est ",result_masque)

    lettre =0
    result=""

    tour = True

    while tour:
        print(joueur,"vous disposz de ", chances, "chance(s)")
        tentative +=1
        chances = tours - tentative
        essai = input("\nSaisissez une lettre : \n")

        ln_essai =len(essai)

        if ln_essai > 1: #Bloque l'usage de plusieurs lettres
            print("Vous n'avez droit qu'a une lettre")
            continue

        for i, l in enumerate(mot_secret):
            if essai == l:
                masque[i]=essai
                lettre+=1
        result= ''.join(masque)
        print(result)

        if lettre == ln_masque:
            print("Félicitations vous avez trouvez le mot mystère")
            break

        if tentative == 8:
            print("Vous avez épuisé vos chances")
            tour = False

    rejouer = input("Rejouer ? Oui ou non ")
    if rejouer == "non":
        jeu = False
        print("Au revoir ", joueur)