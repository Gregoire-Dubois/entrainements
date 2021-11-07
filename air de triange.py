"""
Écrivez un programme qui calcule le périmètre et l’aire d’un triangle quelconque dont l’utilisateur fournit les 3 côtés.

"""
c_Un = input("saisissez la longueur du premier coté")
c_Deux = input("saisissez la longueur du second coté")
c_Troix = input("saisissez la longueur du troisième coté")

air = int(c_Un) * int(c_Deux) /2

perimetre = int(c_Un) + int(c_Deux) + int(c_Troix)

print("Le périmètre de triangle est ", perimetre, " et a comme air ", air)