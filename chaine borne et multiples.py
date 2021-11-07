"""
Écrire un programme qui, étant données deux bornes entières a et b, additionne les nombres multiples de 3 et de 5 compris
entre ces bornes. Prendre par exemple a = 0, b = 32 ; le résultat devrait être alors 0+15+30=45.
Modifier légèrement ce programme pour qu’il additionne les nombres multiples de 3 ou de 5 compris entre les bornes a et b.
Avec les bornes 0 et 32, le résultat devrait donc être : 0+3+ 5 +6+9+10+12+15+18+20+21+24+25+27+30=225.

"""

c = 5
t = 3

i = 0
liste = []
cal = 0
som = 0
som2 = 0

while i < 20 :
    i = i + 1
    y = t * i
    x = c * i
    if x  % 5 == 0 :
        som = som + x
        if x % 3 == 0 :
            som = som +x
            if x < 32 :
               liste=[liste, x]
print(liste)
