"""
Objectif du script, ouvrir le fichier remy.txt qui contient de la data

il faut extraire l'ensemble des données qui sont placée entre les ||

puis les exporter vers un autre fichier text

RESOLU

import re #importe expression régulière
recup = ""
with open("remy.txt", 'r') as filin: #ouvre en lecture le fichier
    lignes = filin.readlines()
    for ligne in lignes: #lecture ligne par ligne du fichier
        wanted = re.findall(r"\|(.*?)\|",ligne) #définition de l'expression régulière
        for result in wanted: #balayage des résultats
            recup = recup + f"{result}\n" #incrémentation de la liste recup avec un renvoi à la ligne apres chaque correspondance

with open("remy sortie.txt", "w") as filout: #ouverture d'un fichier txt
    for code in recup: #pour chaque code contenu dans recup
        filout.write(code) #le code est écrit dans le fichier txt

"""

import re #importe expression régulière
recup = ""
with open("input.txt", 'r') as filin: #ouvre en lecture le fichier
    lignes = filin.readlines()
    for ligne in lignes: #lecture ligne par ligne du fichier
        wanted = re.findall(r"\|(.*?)\|",ligne) #définition de l'expression régulière
        for result in wanted: #balayage des résultats
            recup = recup + f"{result}\n" #incrémentation de la liste recup avec un renvoi à la ligne apres chaque correspondance

with open("output.txt", "w") as filout: #ouverture d'un fichier txt
    for code in recup: #pour chaque code contenu dans recup
        filout.write(code) #le code est écrit dans le fichier txt

    print("End of script")




