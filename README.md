# WolfisTournament
Tournament bot for league og legends. simple  and free to use.

# Structure.
- lib => Librarys, code librarys we make our and other lifes easier.
- Tournament.py => Main entry point.
- Readme.md => we need to doc our progress and how to use.
- LICENSE => MIT, use it and have fun.
- rewuirements.txt => Modules needed to run the bot.




# Tasks

### Lomix
#### https://tinydb.readthedocs.io/en/latest/index.html
- config
    - finish config.
    - config shema.

### Syncx
#### https://discordpy.readthedocs.io/en/latest/api.html
- basic discord bot.
    - Welche commands?
    - Datendarstellung.
    - reactions?


- Discord Bot / Config
    - Permissions.
        - wer darf erstellen.
        - wer ändern.

### ZéroTwó#5019
#### https://developer.riotgames.com/apis 
- Riot Api
    - anfragen
    - welche api's




player.json

'player_list':   [
                    {
                        'player': 'NAME',
                        'rank'  : 'RANK',
                        'tournament' : 'TOURNAMENT'    # can hold multiple tournaments
                    }

                ]

# tournament.json will be deleted after the Tournament is over and the bot postest an embed with the winner
tournament.json                                         #Tournament will be replaced by the tournament name to differentiate beetween multiple tournaments.

'config':       [
                    {
                        'startTime': 'TIMESTAMP',
                        'winner': 'PLAYER'
                    }
                ]

'brackets':     [
                    {
                        'round': 'ROUND',
                        'player1': 'PLAYER',
                        'player2': 'PLAYER',
                        'winner': 'PLAYER'
                    }
                ]