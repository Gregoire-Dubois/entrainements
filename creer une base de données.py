import sqlite3
""" 
# Crééer base de données

fichierDonnee = "bd_test.sq3"
conn = sqlite3.connect(fichierDonnee)
cur = conn.cursor()
cur.execute("CREATE TABLE membres (age INTEGER, nom TEXT, taille REAL)")
cur.execute("INSERT INTO membres (age,nom,taille) VALUES(21, 'Dupont', 1.87)")
conn.commit()
cur.close()
conn.close()

# connexion à une base de données
conn = sqlite3.connect("bd_test.sq3")
cur = conn.cursor()
cur.execute("SELECT * FROM membres")
wanted = 0
for l in cur :
    print(l)
conn.commit()
cur.close()
conn.close()

# supprimer des enregistrements

conn = sqlite3.connect("bd_test.sq3")
cur = conn.cursor()
cur.execute("DELETE FROM membres WHERE nom = 'fredo'")
conn.commit()
cur.close()
conn.close()

# R2cupérer une donnée dans la base
wanted = ("Moncoeur",)
connexion = sqlite3.connect("baseD.sq3")
curseur = connexion.cursor()
curseur.execute("SELECT nom, age, taille FROM membres WHERE nom = ?", wanted)
personne = curseur.fetchone()
print(personne)
connexion.close()

"""
