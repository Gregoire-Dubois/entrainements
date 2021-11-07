"""
Script qui demande à l'utilsateur le nombre de joueurs et qui créé les groupes de façon aléatoire
1 saisir le nom des joueurs séparé par ";"
2 saisir le nombre de groupes
3 récupérer les joueurs dans une liste
4 utiliser le nombre groupe pour ventiler
5 faire apparaitre les groupes
"""
from random import shuffle

nb_team = int(input("combien d'équipes voulez vous constituer ?"))
l = []
players = input("saisir les noms des joueurs:")
players.split(",")
l = list(players.split())
shuffle(l) # aléa dans la liste
ll = len(l) # longueur de l'indeice
lm = ll/2 # moitié de l'indice de la liste
team = 1
x= []

if ll % nb_team == 0 :
    team = 0
    while team < nb_team:
        team = team + 1
    print("L'équipe n° ", str(team), "est composée de ")

elif ll / nb_team :
    team = 0
    while team < nb_team :
        team = team + 1
    print("L'équipe n° ", str(team), "est composée de ")

else:
    print(" y a un pb")
"""


"""