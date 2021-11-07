"""
écrire un programme qui affiche des étoiles sous forme pyramidale

exemple :
*
**
***
****

 TERMINE

"""

a = "*" #Création de la chaine de caratère
i = 0 # création du compteur d'itération

while i < 10 : #boucle limitée à 10 tours
    i = i+1 # Incrémentation du compteur d'itération dans la limite de 10 tours
    etoile = a *i # Création de la variable conteneur du résultat
    print(etoile) #affichage du résultat par itération
