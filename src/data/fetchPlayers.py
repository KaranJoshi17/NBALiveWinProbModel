from nba_api.stats.static import players , teams

player_dict = players.get_players()

tatum = [player for player in player_dict if player['full_name'] == 'Jayson Tatum'][0]

team_dict = teams.get_teams()

celtics = [team for team in team_dict if team['full_name'] == 'Boston Celtics'][0]
# print(celtics)