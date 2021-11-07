"""
Dans cet exercice, nous allons réecrire cette fonction mais nous la nommerons somme. La fonction somme prend en entrée
une liste de nombres et renvoie la somme de ces nombres. Ici, vous n'avez pas le droit d'utiliser la fonction sum de
Python. Le but de cet exercice est d'apprendre à implémenter une fonction qui existe déjà et gagner en confiance sur nos
capacités à faire des choses que d'autres programmeurs plus expérimentés ont déjà fait.

"""

def somme():
    l = [5,2,6,8,9,4]
    r = 0
    for chiffre in l :
       r = r + chiffre
    print(r)

somme()