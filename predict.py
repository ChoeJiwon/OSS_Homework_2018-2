import numpy as np
import pandas as pd
import requests
import dataManager
import time
import ChampionData
import crawl_winrate
import django
from sklearn.externals import joblib

#api key and base constants
API_BASE = dataManager.API_BASE
API_BASE_CHAMPIONGG = dataManager.API_BASE_CHAMPIONGG
API_KEY_LIST = dataManager.API_KEY_LIST
API_KEY_CHAMPIONGG = dataManager.API_BASE_CHAMPIONGG

#request url constants
MATCHES_REQUEST_ACCOUNT = dataManager.MATCHES_REQUEST_ACCOUNT
MATCHES_REQUEST_MATCHID = dataManager.MATCHES_REQUEST_MATCHID
CHAMPIONS_REQUEST = dataManager.CHAMPIONS_REQUEST
MASTERY_REQUEST = dataManager.MASTERY_REQUEST
SUMMONER_REQUEST = dataManager.SUMMONER_REQUEST
SUMMONER_REQUEST_NAME = dataManager.SUMMONER_REQUEST_NAME
LEAGUE_REQUEST = dataManager.LEAGUE_REQUEST
CHAMPION_REQUEST_GG = dataManager.CHAMPION_REQUEST_GG

#data file save paths
DATA_FILE_PATH = dataManager.DATA_FILE_PATH
ROLE_LIST = dataManager.ROLE_LIST
#global helper variable for api switching
cur_api = 0

'''
    FUNCTIONS
'''
#helper function to get a request from the api database. We will be using multiple api keys for speedup.
#Takes in the url without the api key, returns -1 if request error, otherwise returns a json() data structure
def get_request(url):
    global cur_api
    req = requests.get(url+API_KEY_LIST[cur_api])
    cur_api += 1
    if cur_api == len(API_KEY_LIST):
        time.sleep(1.2)
        cur_api = 0
    if req.status_code != 200:
        print("Request error: ", req.status_code)
        return -1
    return req.json()

'''
#Takes a summoner name and returns its id
def get_summoner_id(summoner_name):
    req = get_request(SUMMONER_REQUEST_NAME+summoner_name+"?"+dataManager.API_KEY)
    if req == -1: return -1
    return {'accountId':req['accountId'], 'summonerId':req['id']}
'''
'''
Main predict function. Takes the summoner names of top, jg, mid, adc, sup in order, and takes
the champion names of top, jg, mid, adc, sup of both teams in order. Generates sample featureset
for use with interactive mode.
'''

def predict(allyteam, enemyteam):
    #First, convert all summoners to summoner ids
    #player_id = [get_summoner_id(summoners[i]) for i in range(5)]
    #Then, convert all champion names to champion ids
    ally_id, enemy_id = [0 for i in range(5)], [0 for i in range(5)]
    feature = [[]]
    champion_winrate = [0 for i in range(5)]
    for j in range(5):
        allyteam[j] = allyteam[j].lower()
        enemyteam[j] = enemyteam[j].lower()
        champion_winrate[j]=crawl_winrate.get_Winrate(allyteam[j],enemyteam[j],ROLE_LIST[j])

        '''
        for i in CHAMP_NAME:
            i = i.upper()
            l = allyteam[j].upper()
            k = enemyteam[j].upper()
            if i == l:
                i = i.lower()
                ally_id[j] = ChNameToID(i)
            if i == k:
                i = i.lower()
                enemy_id[j] = ChNameToID(i)
        '''

    result = champion_winrate[0]*0.2 + champion_winrate[1]*0.3 + champion_winrate[2]*0.3 + champion_winrate[3]*0.1 + champion_winrate[4]*0.1

    return result

#mlpc = joblib.load('models/mlpc.pkl')
#gbc = joblib.load('models/gbc.pkl')
print("Ready for user input")
while(1):
    allychampions = [input("Enter Ally Champion with role " + ROLE_LIST[i] + ": ") for i in range(5)]
    enemychampions = [input("Enter Enemy Champion with role " + ROLE_LIST[i] + ": ") for i in range(5)]
    Win_rate= predict(allychampions, enemychampions)
    print("Predicting with ",Win_rate,"% chance")
    break
