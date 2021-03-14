from tinydb import TinyDB, Query
import asyncio

class cfg:
    def __init__(self, db:str):
        self.Tournamentdb   = TinyDB(db)
        self.player_list    = self.Tournamentdb.table('player_list')
        self.bracket_list   = self.Tournamentdb.table('bracket_list')
        self.query          = Query()


    async def get_player(self):  
        return
    
    async def set_bracket(self):  
        return

    async def set_player(self, player:str, rank:str, tournament:str):
        if str(self.player_list.search(self.query.player == player)) == '[]':
            self.player_list.insert({'player': player,'rank': rank, 'tournament': tournament})
            return True
        else:
            return False

Main = cfg('Luki.json')
asyncio.run(Main.set_player('Lominex', 'Gold 3', 'LukiTurnier'))
asyncio.run(Main.set_player('Syncx', 'Gold 3', 'LukiTurnier'))
asyncio.run(Main.set_player('ZeroTwo', 'Gold 3', 'LukiTurnier'))
