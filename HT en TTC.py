"""
demander a l'utilisateur de saisir un HT
convertir ce HT en TTC avec une TVA a 20%
tant que l'utilisateur veut continuer on boucle
"""
#coding:utf-8


def calcul_Tva() :
    ht = float(input("Saisissez le prix HT"))
    tx = float(input("saisissez le taux de TVA; exemple 3; 5 ; 20"))
    mt_tva = (ht*tx)/100
    ttc = ht + mt_tva
    print("Le montant ht de " + str(ht) + "correspond à " + str(mt_tva) +" euro de TVA soit un montant TTC de " + str(ttc) + " euros")

continuer = True

while continuer :
    calcul_Tva()

    choix = input("voulez vous recommencer ? oui ou non")

    if choix == "oui" :
        continue
    else:
        print("bye")
        break



