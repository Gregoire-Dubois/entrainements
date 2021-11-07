from math import sqrt

print("Entrez un nombre entier")

x = int(input())

if sqrt(x):
    print("La racine carré est ", str(sqrt(x)))
else:
    print("le carré ne peut être calculé")