import requests
import json

r = requests.get("https://ddragon.leagueoflegends.com/cdn/11.20.1/data/en_US/champion.json")

with open("champions.txt", "w") as f:
    f.write(str(r.json()["data"].keys()))
