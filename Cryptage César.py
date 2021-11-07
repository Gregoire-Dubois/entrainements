"""
Cryptage César

Utiliser la table ascii
 ord('x') --> permet de donner la valeur numérique d'une lettre
 chr(45) --> permet de donner la lettre d'une valeur numérique

"""
class CryptCesar:

    """Création de la classe destinée à crypter et décrypter le césar"""

    def __init__(self, gap):
        self.gap = gap

    def code_word():

        print('Entrez votre message')
        entry_message = input('--> ')
        letters = []
        out_put = []
        list_out = ""

        for letter in entry_message:
            letters.append(letter)

        for letter in letters:
            convert = chr(ord(letter) + 4)
            for c in convert:
                out_put.append(c)
                list_out = "".join(out_put)
        print(list_out)


x=CryptCesar
x.code_word()

