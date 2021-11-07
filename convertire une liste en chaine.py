"""
Écrivez un programme qui affiche « proprement » tous les éléments d’une liste. Si on l’appli-
quait par exemple à la liste t2 de l’exercice ci-dessus, on devrait obtenir :
Janvier Février Mars Avril Mai Juin Juillet Août Septembre Octobre Novembre
Décembre

"""

t2 = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre",
"Décembre"]
t3 = " "

lg = len(t2)

rst = " "

i = 0

while i <lg :
    rst = rst + t3 + t2[i]
    i = i +1

print(rst)
