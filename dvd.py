"""
Créer une base de données pour des films. l'utilisateur aura 3 possiblités :
                                Créer un titre dans sa base (V)

                                Chercher un titre :
                                    Par nom (V)
                                    Type de film
                                    lancer la lecture

                                Supprimer un titre

                Le tout doit être stocké dans un fichier texte
"""
import json

films = {}

def recherhceFilm(): # cherhcer un film dans la liste
    r = input("quel film cherches tu ? ")
    compteur = 0

    with open("dvd.txt", "r") as fichier:
        fichier.read()
        for film in films.values() :
            if r in film :
                compteur = compteur + 1
                break
            else:
                pass

        if compteur == 1 :
            print("Le film ", r, " est dans la base de films")
        else:
            print("Le film ", r, " n'est pas dans la base de films")


def creerFilm(): # ajouter un film
    c = input("Quel film veux tu créer dans la base ?")
    k = input("Quelle est la catégorie de ce film")

    presence = 0
    with open("dvd.txt", "r") as fichier:
        fichier.read()
        presence = 0
        for film in fichier :
            if c in film and k in film:
                presence = presence + 1
                break
            else:
                pass

    if presence == 1 :
        print("le Film", c," existe déjà dans la base à la rubrique")
    else :
        films[k] = [c]
        with open("dvd.txt", "a") as fichier:
            fichier.write(json.dumps(films))

# boucle de démarage
q = " "
while q != "" :
    print("Que voulez vous faire ? Ajouter un film : taper '1' / Chercher un film : taper '2' / Supprimer un film : taper '3'"
              " / quitter presser Entrer")
    q = input("Tapez votre choix")

    if q == "1" :
        creerFilm()

    elif q == "2" :
        recherhceFilm()

print("Fin du programme")

    # ajouter une fonction de supression
