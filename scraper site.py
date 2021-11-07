"""
Sur le site test : récupérer :
- intitulé de poste => #ResultsContainer > div:nth-child(1) > div > div > div.media > div.media-content > h2
- localisation => <p class="location">Stewartbury, AA</p>

"""

from bs4 import BeautifulSoup
import requests

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")
situations = results.find_all("div", class_="content")
number = 0
for situation in situations:
    number = number+1
    location_element = situation.find("p", class_="location")
    print(number, location_element.text.strip())

