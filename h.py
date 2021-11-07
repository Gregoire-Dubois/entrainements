"""
Écrivez un programme qui convertisse en mètres par seconde et en km/h une vitesse fournie
par l’utilisateur en miles/heure. (Rappel : 1 mile = 1609 mètres)
"""

vitesse = input("Saisis ta vitesse en miles par heure")
kmh = int(vitesse) * 1.609
ms = int(vitesse) * 1609 / 3600

pluriel = "metres"
singulier = "metre"

if ms and kmh > 1 :
    print("la vitesse de", str(vitesse), " MPH équivaut à ", str(kmh), " km/h ce qui fait", ms, pluriel, "seconde")
else:
    print("la vitesse de", str(vitesse), " MPH équivaut à ", str(kmh), " km/h ce qui fait", ms, singulier, "seconde")
