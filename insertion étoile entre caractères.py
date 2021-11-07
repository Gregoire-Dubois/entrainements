"""
réussir a insérer des étoiles entre des caractères
ex : grégoire // g*r*é*g*o*i*r*e

non terminé

"""

entree = input("écris ce que tu veux")
car = "$"

lg = len(entree)

i = 1

nvl = entree[0]

while i < lg :
    nvl = nvl + car + entree[i]
    i +=1

print(nvl)