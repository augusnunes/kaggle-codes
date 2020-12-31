import requests


key = input()
ammount_pages = int(input())
elos = [e if e != "" for e int input().split()] # elo in CAPS
divs = [e if e != "" for e int input().split()] # I II III IV
queue = "RANKED_SOLO_5x5"

regiao = "https://br1.api.riotgames.com"

# Dados dos jogadores
data = None 
for page in range(ammount_pages):
    for elo in elos:
        for div in divs:
            players = requests.get(f'{regiao}/lol/league/v4/entries/{queue}/{elo}/{div}?page={page}&api_key={key}')
            data = pd.DataFrame(players.json())
            data.to_csv(f"{div}-{tier}-{page}.csv")

# Dados do jogos dos jogadores
games = None
for player in data.loc[:,'summonerName']:
    query = requests.get(f'{regiao}/lol/summoner/v4/summoners/by-name/{player}?api_key={key}')
    if query.status_code != 200:
        continue
    info = pd.DataFrame([query.json()])
    accountId_player = info.accountId.values[0]
    query = requests.get(f'{regiao}/lol/match/v4/matchlists/by-account/{accountId_player}?api_key={key}')
    if query.status_code != 200:
        continue
    info = pd.DataFrame(query.json()[0])
    indexes = np.random.randint(info.shape[0], size = 10)
    info = info.loc[indexes,:]
    if games == None:
        games = pd.DataFrame(columns=info.columns)
    games = pd.merge(games, info, how='outer')
games.to_csv("games.csv")

# Procurando por informações dos Jogos
## games.
# query = requests.get(f'{regiao}/lol/match/v4/timelines/by-match/{gameId}?api_key={key}')
finalDf = 
for gameId in gamesloc[:,'gameId']:
    query = requests.get(f'{regiao}/lol/match/v4/timelines/by-match/{gameId}?api_key={key}')
    if query.status_code !=200:
        continue
    
