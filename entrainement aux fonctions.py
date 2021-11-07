
def make_album(name_album=None, name_singer=None):
    next_loop = True

    while next_loop:

        print("Entrez le nom du chanteur et de l'album")
        name_album = input("\n Nom de l'album ==>")
        if name_album == "q":
            break
        name_singer = input("\n Nom du chanteur ==>")
        if name_singer == "q":
            break

        cd = {'singer' : name_singer, 'album' : name_album}
        print(cd)
---------------------------------------------------------------

def print_model(unprinting, complete_printing):
    while unprinting :
        current_designe = unprinting.pop()
        print(f"Impressions du modèle {current_designe}")
        complete_printing.append(current_designe)

def show_complet_model(complete_printing):
    print("Les modèles suivants ont été imprimés")
    for complet_models in complete_printing:
        print(complet_models)

unprinting= ['couque de téléphone', 'protège tibia', 'boullede billard']
complete_printing=[]

print_model(unprinting,complete_printing)
show_complet_model(complete_printing)

---------------------------------------------------------------
"""
def show_message(messages):
    for message in messages :
        envoi = message
        print(f"{envoi}")


def send_message(unsend_messages, sent_message):
    for unsend_message in unsend_messages[:]:
        sent_message.append(unsend_message)
        unsend_messages.pop()
    print(f"\n Messages envoyés {sent_message}")
    print(f"\n Messages non envoyés {unsend_messages}")


a=["bonjour, comment vas tu ?", "Un café s'il vous plait", "Il faut beau aujourd'hui", "j'aime le chocolat"]
b=[]

"""

---------------------------------------------------------------

def send_message(unsend_messages, sent_message):
    copy_unsend_messages=[]
    sent_message=[]

    for message in unsend_messages[:]:
        copy_unsend_messages.append(message)

    for i in copy_unsend_messages[:]:
        sent_message.append(i)
        copy_unsend_messages.pop()

    print(f"Messages envoyés : {sent_message}")
    print(f"Messages supprimés sont : {copy_unsend_messages}")
    print(f"liste d'origine des messages {unsend_messages}")

a=["bonjour, comment vas tu ?", "Un café s'il vous plait", "Il faut beau aujourd'hui", "Plutot un chocolat chaud"]
b=[]

send_message(a,b)
---------------------------------------------------------------
"""

def built_user(first_name, last_name, **user_info):
    user_info['name'] = first_name
    user_info['second_name'] = last_name
    return user_info

x = built_user('Dubois', 'Grégoire', domaine='assurances', légitimité='aucune')
print(x)

"""
""" 
def build_profil(first_name, laste_name, **info):
    info['nom']= first_name.title()
    info['prenom']=laste_name.title()
    return info

x=build_profil('dubois', 'grégoire', birthday='24/01/1986', profession='assureur')
print(x)
"""
"""   
def car(builder, model, km="", **kwargs):
    describe_car = builder, model, kwargs
    if km == "":
        return f"{describe_car}"
    else:
        return builder, model, km, kwargs

bm= car('bmw', 'série 1', '43000', dammage = 'portière AVG', assureur = 'AXA', couleur ='bleue')
print(bm)

"""