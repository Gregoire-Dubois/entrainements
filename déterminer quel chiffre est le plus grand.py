"""
5.13 Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée.
Par exemple, si on l’appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15], ce programme devrait afficher :
le plus grand élément de cette liste a la valeur 75.

"""
l = len(source)
i = 0

min = 1000

while i < l :
    if source[i] < min :

        min = source[i]
    i = i + 1
print("Le plus petit est : ", min)