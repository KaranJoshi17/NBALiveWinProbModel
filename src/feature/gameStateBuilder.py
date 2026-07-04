
import pandas as pd

from nba_api.stats.endpoints import playbyplayv3 

def build_game_states(pbp_df):

    snapshots = []

    for _, row in pbp_df.itterows():

        action_type = row["actionType"]

        if action_type != "Made Shot":
            continue

        home_score = row["scoreHome"]
        away_score = row["scoreAway"]

        score_diff = home_score - away_score

        snapshot = {
            "period": row["period"],
            "clock": row("clock"),
            "home_score": home_score, 
            "away_score": away_score,
            "score_diff": score_diff
        }

        snapshots.append(snapshot)

    return pd.DataFrame(snapshots) 
    
  
