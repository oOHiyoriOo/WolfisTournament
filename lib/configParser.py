import os

from dotenv import load_dotenv
from tinydb import TinyDB, Query

class cfg:
    def __init__(self):
        load_dotenv()
        self.RiotToken = os.getenv("RiotToken")
        self.CDB = TinyDB('./db/config.json')
        self.query = Query()

    def get(self,key:str):
        return self.CDB.search(self.query.key == key)

    def set(self,key:str,value:str): # ill first try checking if the value exist to use update if it does.
        if str(self.CDB.search(self.query.key == key)) == "[]": # assume its a new value
            self.CDB.insert({'key':key,'value':value}) # using insert to add the new value.
        else:
            MySQL.execute("UPDATE config SET Value = '{}' where CKey = '{}';".format(value,key),log,read,True) # updating it.
