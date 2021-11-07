"""
Écrire une boucle de programme qui demande à l’utilisateur d’entrer des notes d’élèves. La boucle se terminera seulement
si l’utilisateur entre une valeur négative. Avec les notes ainsi entrées, construire progressivement une liste. Après chaque
entrée d’une nouvelle note (et donc à chaque itération de la boucle), afficher le nombre de notes entrées, la note la plus élevée,
la note la plus basse, la moyenne de toutes les notes.

A FINIR SUR LE POINT DE LA MOYENNE DES NOTES

"""
from statistics import mean

note = 0 #point de départ des notes

l = [] # liste vierge
x = len(l) # compteur d'objet de liste
stop = 0 #valeur d'arret
mini = 0 # note mini
maxi = 0 # note maxi
moyenne = 0
total = 0
v = 0 # conteneur de récupe pour la boucle for

 # compteur d'itération

while note >= stop : # mécanisme pour interrompre la boucle avec un négatif

    # récupération de la saisie et vérification que ce sont bien des entiers

    note = int(input("Entre la liste de tes notes"))

    # condition pour continuer la boucle tant que la valeur saisie est supéreure ou égale à 0

    if note >= 0 :
        l = l, note #incrémente les valeurs à la liste

    else:
        pass

    total = total + note

    # méthode de comparaison entre le plus grand et le plus petit

    if note <= 0 :
        pass
    elif note > maxi :
        maxi = note
    else:
        pass

        if note >=0 :
            mini = note
        elif note < maxi :
            mini = note
        else:
            pass

for e in l : # e est le pointeur dans la boucle
    v = v , e



print("le plus grand est ", str(maxi))
print("le plus petit est ", str(mini))
print("La liste des notes saisies est : ",l)
print("Le total des note est de ", total)
