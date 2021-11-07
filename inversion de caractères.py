"""
écrire une chaine de caractère initiale puis l'inverser

"""
import random

texte = input("saisi ton message, je vais y mettre le border")
random.shuffle(texte)
print(texte)