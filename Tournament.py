import discord

from lib.Riot import PlayerClass

client = discord.Client()
PlayerManager = PlayerClass()

@client.event
async def on_ready():
    ZéroTwó = await PlayerManager.getPlayer("ZéroTwó")
    print(await ZéroTwó.VerifyPlayer('HalloNami'))


@client.event
async def on_message(msg):
    print(msg)

client.run('NzY4OTUxMTk5MDI5NjU3NjIx.X5H7nA.LEpGSPLhM6HNcVXAAd-xzv3W348')