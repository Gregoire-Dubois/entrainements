"""
demander a l'utilisateur son nom et le faire apparaitre avec la bonne civilité

"""

n = input("Quel est ton nom ?")
s = input("Quel est ton sexe ? masculin / féminin")
h = 0
civh = "Monsieur"
civf = "Madame"

if s == "masculin" :
    print("Bonjour", civh, n)
else:
    print("Bonjour", civf, n)