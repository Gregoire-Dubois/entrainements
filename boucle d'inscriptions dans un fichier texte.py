fichier= "fichier test en txt.txt"
hye=""
sortie=""
while True:
    if hye == "stop":
        print("fin de programme")
        break

    else:
        hye = input("quel est votre nom ? Ou tapez 'stop' pour arreter")
        with open(fichier, "a") as filin:
            if hye != "stop":
                print("Bienvenue", hye)
                filin.write(f"{hye.title()}\n")
            else:
                print("fin de programme")
                break