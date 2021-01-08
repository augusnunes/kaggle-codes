import requests
import cassiopeia as cass
import pandas as pd
import time

key = input("Sua chave da API: ")
#ammount_pages = int(input("Número de páginas de players: "))
#elos = [e if e != "" for e int input("Elos em CapsLock separador por espaço: ").split()] # elo in CAPS
#divs = [e if e != "" for e int input("Divisões em números romanos: ").split()] # I II III IV
cass.set_riot_api_key(key)

ammount_pages = 1
elos = ["SILVER"]
divs = ["IV"]
queue = "RANKED_SOLO_5x5"
regiao = "https://br1.api.riotgames.com"

# Dados dos jogadores
# data = None 
# for page in range(1,ammount_pages+1):
#     for elo in elos:
#         for div in divs:
#             players = requests.get(f'{regiao}/lol/league/v4/entries/{queue}/{elo}/{div}?page={page}&api_key={key}')
#             data = pd.DataFrame(players.json())
#             data.to_csv(f"{elo}-{div}-{page}.csv")

data = pd.read_csv("SILVER-IV-1.csv")

finalDf = None
for player in data.loc[63:,'summonerName']:
    try:
        summoner = cass.Summoner(name=player, region="BR")
        match = cass.MatchHistory(summoner=summoner, queues = [cass.Queue(queue)])
        for matchId in range(20):
            try:
                targetMatch = match[matchId]
                matchData = {}
                if not targetMatch.is_remake:
                    matchData['match_duration'] = targetMatch.duration.seconds
                    for team in targetMatch.teams:
                        if team.win:
                            matchData['team_win'] = team.side.name 
                        side = team.side.name+'_team_' 
                        matchData[side+'barons'] = team.baron_kills
                        matchData[side+'heralds'] = team.rift_herald_kills
                        matchData[side+'dragons'] = team.dragon_kills
                        matchData[side+'towers'] = team.tower_kills
                        matchData[side+'inhibitors'] = team.inhibitor_kills
                        # inicializando variáveis individuais 
                        matchData[side+'kills'] = 0
                        matchData[side+'assists'] = 0
                        matchData[side+'deaths'] = 0
                        matchData[side+'damage_dealt_objectives'] = 0
                        matchData[side+'damage_dealt_towers'] = 0
                        matchData[side+'damage_self_mitigated'] = 0
                        matchData[side+'physical_damage_dealt'] = 0
                        matchData[side+'magic_damage_dealt'] = 0
                        matchData[side+'total_gold_earned'] = 0
                        matchData[side+'vision_score'] = 0
                        matchData[side+'time_crowd_control_dealt'] = 0
                        matchData[side+'cs_permin_0-10'] = 0
                        matchData[side+'cs_permin_10-20'] = 0
                        matchData[side+'xp_permin_0-10'] = 0
                        matchData[side+'xp_permin_10-20'] = 0
                        for participant in team.participants:
                            stats = participant.stats
                            tl = participant.timeline 
                            matchData[side+'kills'] += stats.kills
                            matchData[side+'assists'] += stats.assists
                            matchData[side+'deaths'] += stats.deaths
                            matchData[side+'damage_dealt_objectives'] += stats.damage_dealt_to_objectives
                            matchData[side+'damage_dealt_towers'] += stats.damage_dealt_to_turrets
                            matchData[side+'damage_self_mitigated'] += stats.damage_self_mitigated
                            matchData[side+'physical_damage_dealt'] += stats.physical_damage_dealt_to_champions
                            matchData[side+'magic_damage_dealt'] += stats.magic_damage_dealt_to_champions
                            matchData[side+'total_gold_earned'] += stats.gold_earned
                            matchData[side+'vision_score'] += stats.vision_score
                            matchData[side+'time_crowd_control_dealt'] += stats.total_time_crowd_control_dealt
                            cs = tl.creeps_per_min_deltas
                            for key in cs.keys():
                                if key == '0-10':
                                    matchData[side+'cs_permin_0-10'] = cs[key]
                                    matchData[side+'cs_permin_10-20'] = cs[key]
                                elif key == '10-20':
                                    matchData[side+'cs_permin_10-20'] += cs[key]
                            xp = tl.xp_per_min_deltas
                            for key in xp.keys():
                                if key == '0-10':
                                    matchData[side+'xp_permin_0-10'] += xp[key]
                                    matchData[side+'xp_permin_10-20'] += xp[key]
                                elif key == '10-20':
                                    matchData[side+'xp_permin_10-20'] += xp[key]

                if type(finalDf) == type(None):
                    finalDf = pd.DataFrame(columns=matchData.keys())
                    finalDf = pd.merge(finalDf, pd.DataFrame([matchData]), how='outer' )
                    continue
                finalDf = pd.merge(finalDf, pd.DataFrame([matchData]), how='outer' )
                finalDf.to_csv('final_data.csv', index=False)
            except:
                continue
        
    except:
        continue