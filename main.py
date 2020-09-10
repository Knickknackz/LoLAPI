import requests
import pyot
import os
import random
import bisect
from cassiopeia import Champion, Champions
import cassiopeia as cass

#client = commands.Bot(command_prefix='$')
token = os.environ.get('LOL_BOT_TOKEN')
riotKey = os.environ.get('RIOT_API')

cass.set_riot_api_key(riotKey)  # This overrides the value set in your configuration/settings.
cass.set_default_region("NA")

bottom_winrate = []
top_winrate = []
support_winrate = []
mid_winrate = []
jungle_winrate = []

"""

"""
champions = cass.get_champions()
for champion in champions:
    wr = champion.win_rates
    full_name = champion.name + champion.title
    if cass.Position.utility in wr:
        support_winrate.append([champion.name, round(wr[cass.Position.utility]*100, 2)])
    if cass.Position.middle in wr:
        mid_winrate.append([champion.name, round(wr[cass.Position.middle] * 100, 2)])
    if cass.Position.bottom in wr:
        bottom_winrate.append([champion.name, round(wr[cass.Position.bottom] * 100, 2)])
    if cass.Position.top in wr:
        top_winrate.append([champion.name, round(wr[cass.Position.top] * 100, 2)])
    if cass.Position.jungle in wr:
        jungle_winrate.append([champion.name, round(wr[cass.Position.jungle] * 100, 2)])

bottom_winrate.sort(key=lambda x:x[1])
top_winrate.sort(key=lambda x:x[1])
mid_winrate.sort(key=lambda x:x[1])
support_winrate.sort(key=lambda x:x[1])
jungle_winrate.sort(key=lambda x:x[1])

print("Top 5 // Bottom 5 Bot Winrates")
for i in range(1,6):
    print(str(i) + ': ' + bottom_winrate[-i][0] + ': ' + str(bottom_winrate[-i][1]) + '% // '+
          str(i) + ': ' + bottom_winrate[i-1][0] + ': ' + str(bottom_winrate[i-1][1]) + '\n')

print("Top 5 // Bottom 5 Support Winrates")
for i in range(1,6):
    print(str(i) + ': ' + support_winrate[-i][0] + ': ' + str(support_winrate[-i][1]) + '% // '+
          str(i) + ': ' + support_winrate[i-1][0] + ': ' + str(support_winrate[i-1][1]) + '\n')

print("Top 5 // Bottom 5 Top Winrates")
for i in range(1,6):
    print(str(i) + ': ' + top_winrate[-i][0] + ': ' + str(top_winrate[-i][1]) + '% // '+
          str(i) + ': ' + top_winrate[i-1][0] + ': ' + str(top_winrate[i-1][1]) + '\n')

print("Top 5 // Bottom 5 Jungle Winrates")
for i in range(1,6):
    print(str(i) + ': ' + jungle_winrate[-i][0] + ': ' + str(jungle_winrate[-i][1]) + '% // '+
          str(i) + ': ' + jungle_winrate[i-1][0] + ': ' + str(jungle_winrate[i-1][1]) + '\n')

print("Top 5 // Bottom 5 Middle Winrates")
for i in range(1,6):
    print(str(i) + ': ' + mid_winrate[-i][0] + ': ' + str(mid_winrate[-i][1]) + '% // '+
          str(i) + ': ' + mid_winrate[i-1][0] + ': ' + str(mid_winrate[i-1][1]) + '\n')

"""
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
"""