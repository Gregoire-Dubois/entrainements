"""
Écrivez un programme qui calcule la période d’un pendule simple de longueur donnée.

"""
from math import *
l = input("saisis la longueur")
g = input("saisis le g")

div = int(l)/int(g)
carre = sqrt(div)
r = carre *(2*pi)
print("la périodicité du pendule est de ", str(r))