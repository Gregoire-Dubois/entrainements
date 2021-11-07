"""
dans marmiton ne récupérer que les ingrédients et les stocker dans une base de données sqlte

"""

#Création des imports
import time
from bs4 import BeautifulSoup
import requests

# définition de l'URL de base
start_url="https://www.marmiton.org/recettes/index/ingredient/"

# Création de la liste des lettres de l'alphabet

table_asci_start = chr(97)
#table_asci_end = chr(122)
#letters = ['','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letters=['','b']
#boucle d'itération dans la liste de l'alphabet
for i in letters:
     new_url = start_url+i #URL mise a jour
     page = requests.get(new_url)
     soup = BeautifulSoup(page.content, "html.parser")
     results = soup.find(id="content")
     ingredients = results.find_all("div", class_="index-item-card") #recipe-results fix-inline-block

     for ingredient in ingredients:
          ing=ingredient.find("div", class_="index-item-card-name") #index-item-card-name
          print(ing.text.strip())
          time.sleep(5)

          with open("ingrédients.txt", "a") as file :
               for i in ing:
                    time.sleep(5)
                    file.write(f"{i}\n")


