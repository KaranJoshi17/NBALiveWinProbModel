# downloades and fetches the detailed play by play logs


from nba_api.stats.endpoints import playbyplayv3
import pandas as pd

game_id = "0022500010"
pbp = playbyplayv3.PlayByPlayV3(game_id=game_id)

df = pbp.get_data_frames()[0]

print(df.columns)
pd.set_option('display.max_columns', None)
print(df.head(20).to_string())