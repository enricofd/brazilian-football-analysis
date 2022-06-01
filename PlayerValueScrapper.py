import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

df = pd.ExcelFile('database.xlsx').parse('Sheet1')
player_list = []
player_tags = []

player_list.append(df['name'].astype("string"))
for player_name in player_list[0]:
    player_tag = player_name.lower()
    if " " in player_tag:
        player_tag = player_tag.replace(" ", "-")
    player_tags.append(player_tag)

def extractData(page_link):
    pageTree = requests.get(page_link, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    link = "https://www.transfermarkt.com.br" + 

    jogadores_valor = pageSoup.find_all("a", {"class": ["data-header__market-value-wrapper"]})