from tinydb import TinyDB, Query
from datetime import datetime
import asyncio

class cfg:
    def __init__(self):
        self.Playerdb       = TinyDB('player.json')
        self.Tournament     = None
        self.player_list    = self.Playerdb.table('player_list')
        self.bracket_list   = self.Playerdb.table('bracket_list')
        self.query          = Query()

    async def generate_tournament(self, tournament:str, start:datetime):
        if(TinyDB(tournament+'.json').tables == []):
            self.Tournament = TinyDB(tournament+'.json')
            config = self.Tournament.table('config')
            config.insert({'startTime': str(start), 'winner': '-----'})
            print(start)


    async def get_player(self, player:str):  
        if str(self.player_list.search(self.query.player == player)) != '[]':
            return self.player_list.search(self.query.player), self.player_list.search(self.query.rank),
    
    async def set_bracket(self):  
        return

    

    async def set_player(self, player:str, rank:str, tournament:str):
        if self.player_list.search(self.query.player == player) == []:
            self.player_list.insert({'player': player,'rank': rank, 'tournament': tournament})
            return True
        elif self.player_list.search(self.query.player == player) != [] and self.player_list.search(self.query.tournament == tournament) != []:
            return
        else:
            return False

Main = cfg()
asyncio.run(Main.set_player('Lominex', 'Gold 3', 'LukiTurnier'))
asyncio.run(Main.set_player('Syncx', 'Gold 3', 'LukiTurnier'))
asyncio.run(Main.set_player('ZeroTwo', 'Gold 3', 'LukiTurnier'))
asyncio.run(Main.generate_tournament('LukiTurnier', datetime(2021, 3, 17,19,00,00,00)))
