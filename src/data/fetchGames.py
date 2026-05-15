# fetches the game ids and stuff 

import fetchPlayers

import pandas as pd 
from nba_api.stats.endpoints import leaguegamefinder , boxscoreadvancedv3 , playergamelog


# gameFinder = leaguegamefinder.LeagueGameFinder(date_from_nullable="12/25/2025" , date_to_nullable="12/25/2025")
# games = gameFinder.get_data_frames()[0]

# print(games[['GAME_ID' , 'MATCHUP' , 'GAME_DATE']])


gamelog_tatum = playergamelog.PlayerGameLog(player_id = '1628369', season='2026') 
gamelog_tatum_df = gamelog_tatum.get_data_frames()[0]
print(gamelog_tatum_df)

