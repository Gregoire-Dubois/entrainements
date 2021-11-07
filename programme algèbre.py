"""
programme qui permet de calculer
- aire d'un cercle
- aire d'un carré
- volume d'un cube

limiter les résultats à  2 décimaux
"""

boucle = ""


def aire_carre():
    cote_Un = float(input("Entrez la mesure en cm du 1er côté"))
    cote_Deux = float(input("Entrez la mesure en cm du 2nd côté"))

    if cote_Un != 0 and cote_Deux != 0:
        aire = cote_Un * cote_Deux
        print("L'aire du carré représente", aire, " cm2")
    else:
        print("Le calcule de l'aire ne peut se faire avec la valeur de 0")


def aire_cercle():
    rayon = float(input("Entrez le rayon du cercle"))
    aire = 3.14 * (rayon * rayon)
    print("l'aire du cercle de rayon de", str(rayon), " cm représente une aire de", str(aire), "cm2")


def volume_cube():
    arete = float(input("entrez la taille d'une des 3 arêtes du cube"))
    volume = arete * arete * arete
    print("Le volume d'un cuble dont les arêtes sont de ", str(arete), "cm représente un volume de", str(volume), "cm3")


while boucle != "exite":

    print("Tapez 1 pour calculer l'aire d'un carré, 2 pour calculer l'aire d'un disque, 3 pour le volume d'un cube. "
          "faite 'exite' pour terminer le programme")
    boucle = str(input("saisisser la commande de votre choix"))

    if boucle == "1":
        aire_carre()
    elif boucle == "2":
        aire_cercle()
    elif boucle == "3":
        volume_cube()
    elif boucle == "exite":
        print("fin du programme")
