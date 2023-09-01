import requests, os, json
from dotenv import load_dotenv, find_dotenv

#load_dotenv(find_dotenv())
#linguagem = "pt_br"
#pesquisa = "bob"
#modo_jogo = "battlegrounds"
#token = os.environ.get('BLIZZARD_API_TOKEN')
#url = f"https://us.api.blizzard.com/hearthstone/cards?locale={linguagem}&textFilter={pesquisa}&access_token={token}"
#response = requests.get(url)
#for cards in response.json()["cards"]:
#    print(cards["image"])

metadata = json.load(open('metadata.json'))

for tipos in metadata["minionTypes"]:
    print(tipos)
