"""
Convertir une note scolaire N quelconque, entrée par l’utilisateur sous forme de points (par exemple 27 sur 85),
en une note standardisée suivant le code ci-après :

Note                Appréciation
N> 80%              A
80 % > N >= 60%     B
60 % > N >= 50%     C
50 % > N >= 40%     D
N < 40 %            E

"""
print("saisissez une note entre 0 et 100")
x = int(input())

if x > 80 :
    print("A")
elif x < 80 and x > 60 :
    print("B")
elif x <60 and x > 50  :
    print("C")
elif x < 50 and x > 40 :
    print("D")
elif x < 40 :
    print("E")