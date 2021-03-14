import os

from dotenv import load_dotenv

class cfg:
    def __init__(self):
        load_dotenv()
        self.RiotToken = os.getenv("RiotToken")
    
    def get(self,MySQL,key:str):
        return MySQL.execute("select value from config where CKey = '{}';".format(key),False,True)

    def set(self,MySQL,key:str,value:str,log:bool=False,read:bool=False): # ill first try checking if the value exist to use update if it does.
        if not MySQL.execute("SELECT value from config where CKey = '{}';".format(key),log,True): # assume its a new value if it returns -1
            MySQL.execute("INSERT INTO config (CKey,value) VALUES ('{}','{}');".format(key,value),log,read,True) # using insert to add the new value.
        else:
            MySQL.execute("UPDATE config SET Value = '{}' where CKey = '{}';".format(value,key),log,read,True) # updating it.
