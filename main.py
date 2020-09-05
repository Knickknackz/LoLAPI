import requests
import pyot
import os
import random

from cassiopeia import Champion
import cassiopeia as cass

#client = commands.Bot(command_prefix='$')
#token = 'NzUxODcwMTU2NDU5NzM3MTE4.X1PXpg.HPBdv-yDUHyblZ002KjY7nwZ1fQ'
riotKey = 'RGAPI-1fd8be60-c664-4c17-b9d9-6a6a10e6716e'

cass.set_riot_api_key(riotKey)  # This overrides the value set in your configuration/settings.
cass.set_default_region("NA")

summoner = cass.get_summoner(name="Knickknackz")
print("{name} is a level {level} summoner on the {region} server.".format(name=summoner.name,
                                                                          level=summoner.level,
                                                                          region=summoner.region))
print(cass.get_champion('Aatrox'))

champions = cass.get_champions()
random_champion = random.choice(champions)
print("He enjoys playing champions such as {name}.".format(name=random_champion.name))

challenger_league = cass.get_challenger_league(queue=cass.Queue.ranked_solo_fives)
best_na = challenger_league[0].summoner
print("He's not as good as {name} at League, but probably a better python programmer!".format(name=best_na.name))