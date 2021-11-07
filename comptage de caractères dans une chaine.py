"""
soit la liste suivante :
['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien',
'Alexandre-Benoît', 'Louise']
Écrivez un script qui affiche chacun de ces noms avec le nombre de caractères correspondant.

"""

l = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien','Alexandre-Benoît', 'Louise']
m = len(l)
i=0
for l[i] in l :
    print(len(l[i]), "caractère dans le prénom ",l[i])
