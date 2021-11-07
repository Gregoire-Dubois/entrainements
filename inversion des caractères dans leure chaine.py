"""
Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l’inversant.

Ainsi par exemple, « zorglub » deviendra « bulgroz ».

"""
entree = "texte de merde qui me casse les ..."
lg = len(entree)
rst = ""
i = lg - 1

while i >= 0 :
    rst = rst + entree[i]
    i = i -1
print(rst)


