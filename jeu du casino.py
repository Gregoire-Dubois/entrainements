"""
jeu roulette du casino

RESOLU

"""
from random import randrange

alea = 0
choix_joueur = 0 # nombre choisi par le joueur pour faire partie
wallet = 500
gain = 0
mise = 0
saisie = "" # saisie du joueur pour continuer le jeu

couleur_a = "" # couleur aléatoire
couleur_j = "" # couleur du joueur

while saisie != "stop":
    try:
        saisie = str(input("souhaitez vous jouer ? Tapez 'stop' pour mettre fin à la partie."))
        if saisie == "stop":
            break

        else:
            alea = randrange(0, 50)
            print(alea)
            if alea %2 == 0 :
                couleur_a = "rouge"
            else:
                couleur_a="noir"

            try:
                choix_joueur = int(input("saisissez un nombre entre 0 et 50 inclus"))
                if choix_joueur % 2 == 0:
                    couleur_j = "rouge"
                else:
                    couleur_j = "noir"
                mise = int(input("Combien voulez vous miser ?"))

                if mise>0 :
                    if mise <= wallet:
                        if choix_joueur == alea:
                            gain = mise * 3
                            wallet = wallet + gain
                            print("Félicitation, vous avez gagné. Votre mise de", mise, couleur_a,
                                  " est multipliée par 3 et votre wallet contien maintenant",
                                  wallet, "euro")

                        elif choix_joueur % 2 == 0 and alea % 2 == 0:
                            gain = mise * 50 / 100
                            wallet = wallet + gain
                            print("Pas mal, votre numéro misé est", couleur_a, "comme le numéro sorti. 50 % de votre mise "
                            "alimentent votre walette qui contient maintenant" ,wallet," euro.")

                        elif choix_joueur % 2 != 0 and alea % 2 != 0:
                            gain = mise * 50 / 100
                            wallet = wallet + gain
                            print("Pas mal, votre numéro misé est", couleur_a, "comme le numéro sorti. 50 % de votre mise "
                            "alimentent votre walette qui contient maintenant" ,wallet," euro.")
                        else:
                            wallet = wallet - mise
                            print(
                                "Domamge,vous avez choisis le numéro", choix_joueur, "de couleur", couleur_j, ". Le numéro sorti de "
                                "la roulette est", alea, couleur_a, ". Votre mise de", mise, "est déduite de votre wallet qui est maintenant de", wallet, "euro")
                    else:
                        print("Vous ne pouvez miser plus que ce que vous avez sur vous. La maison ne fait pas de crédit")
                else:
                    print("Vous ne pouvez pas miser des valeurs négatives")
                    continue
            except ValueError:
                print("Vous ne pouvez entrer que des valeurs numériques entières")
                continue

    except:
        continue

    if wallet <= 0:
        print("Vous avez épuisé votre budget de jeu et la maison ne fait pas de crédit. Fin de partie")
        break
    else:
        pass