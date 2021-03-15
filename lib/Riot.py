import aiohttp
import urllib.parse

token = 'RGAPI-2c516d12-1f3f-4263-affe-46cc9c004c3e'

class PlayerClass:
    def __init__(self):
        self.timeout = aiohttp.ClientTimeout(total=120)  # `0` value to disable timeout
        self.headers = {
            'User-Agent': 'Python3.9.1+ WolfisTournament Bot',
            'X-Riot-Token': token,
            'App':'Nami-tan',
            "Content-Type": "application/json"
            }


    async def getPlayer(self,Playername):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+urllib.parse.quote(Playername),headers=self.headers, timeout=self.timeout) as r:
                if r.status == 200 or r.status == 202:
                    resJson = await r.json()
                    return Player(resJson)
                else:
                    return r.status

class Player:
    def __init__(self,data):
        self.Playername = data['name']
        self.id = data['id']
        self.accountId = data['accountId']
        self.puuid = data['puuid']
        self.summonerLevel = data['summonerLevel']

        self.timeout = aiohttp.ClientTimeout(total=120)  # `0` value to disable timeout
        self.headers = {
            'User-Agent': 'Python3.9.1+ WolfisTournament Bot',
            'X-Riot-Token': token,
            'App':'Nami-tan',
            "Content-Type": "application/json"
            }

    async def VerifyPlayer(self,code:str):
        async with aiohttp.ClientSession() as session:
                async with session.get("https://euw1.api.riotgames.com/lol/platform/v4/third-party-code/by-summoner/"+self.id,headers=self.headers, timeout=self.timeout) as r:
                    if r.status == 200 or r.status == 202:
                        OnlineCode = str(await r.text()).replace("\"","")
                        return True if OnlineCode == code else False
                    else:
                        return False