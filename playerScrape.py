import requests
import pandas as pd

url = "https://www.nrl.com/players/data"

ids = []
players = []
querystring = {"competition": "111", "team": "0"}

headers = {
    'authority': "www.nrl.com",
    'accept': "application/json, text/plain, */*",
    'accept-language': "en-AU,en;q=0.9",
    'cookie': "ASP.NET_SessionId=butunmzhddaacbqefa20ogzg",
    'referer': "https://www.nrl.com/players?competition=111&team=500011",
    'sec-ch-ua': "^\^"
    }

r = requests.request("GET", url, headers=headers, params=querystring)

data = r.json()
for p in data['filterTeams']:
    ids.append(p["value"])

for team_id in ids:
    querystring = {"competition": "111", "team": f"{team_id}"}

    headers = {
        'authority': "www.nrl.com",
        'accept': "application/json, text/plain, */*",
        'accept-language': "en-AU,en;q=0.9",
        'cookie': "ASP.NET_SessionId=butunmzhddaacbqefa20ogzg",
        'referer': "https://www.nrl.com/players?competition=111&team=500011",
        'sec-ch-ua': "^\^"
    }

    r = requests.request("GET", url, headers=headers, params=querystring)

    data = r.json()
    for p in data['profileGroups'][0]['profiles']:
        players.append(p)

df = pd.json_normalize(players)
df.to_csv('playerdata.csv')
