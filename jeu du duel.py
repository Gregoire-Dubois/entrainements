"""
"Jeu" dans lequel 2 adversaire s'affrontent.

chacun a 250 points de vie

si l'attaque du joueur 1 contre le joureur 2 fonctionne alors, joueur deux perd des points.

Celui qui arrive a 0 ou moins de 0 points de vie a perdu

RESOLU mais peut s'amélirer avec des classes et des fonctions

"""
import random

name_player_one = input("entrez le nom du joueur 1")
name_player_two = input("Entrez le nom du joueur 2")
life_player_one = 250
life_player_two = 250
game_over = 0
precison_player_one = random.randrange(0, 10)
precison_player_two = random.randrange(0, 10)
hazard_player_one = random.randrange(0, 10)
hazard_player_two = random.randrange(0, 10)

print("Le combat commence")
while life_player_one > game_over and life_player_two > game_over :

    dammages_player_one = random.randrange(5, 50)
    dammages_player_two = random.randrange(5, 50)

    life_player_one = life_player_one - dammages_player_one
    life_player_two = life_player_two - dammages_player_two

    try_player_one = 0
    try_player_two = 0

    if precison_player_one == hazard_player_one :
        life_player_two = life_player_two - dammages_player_two
        try_player_one = 0

    else :
        if precison_player_two == hazard_player_two :
            life_player_one = life_player_one - dammages_player_one
            try_player_two = 0

        else:
            pass



    if try_player_one == 0 :
        print(name_player_one, "lance une attaque et touche sa cible")
    else:
        print(name_player_one, "lance une attaque et rate sa cible")

    if try_player_two == 0 :
        print(name_player_two, "lance une attaque et touche sa cible")
    else:
        print(name_player_two, "lance une attaque et rate sa cible")

    print(name_player_one, "perd", dammages_player_one, " et il lui reste ", life_player_one, " points de vie")
    print(name_player_two, " perd ", dammages_player_two, " et il lui reste ", life_player_two, " points de vie")

if life_player_one <= game_over :
    print(name_player_two, "gagne")
else :
    print(name_player_one, "gagne")
