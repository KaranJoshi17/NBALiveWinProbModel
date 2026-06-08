# creates the target variable

# 1 = home team won
# 0 = home team lost

import pandas as pd
import gameStateBuilder


def FinalScoreResult(game_states_df) -> int:

    final_row = game_states_df.iloc[-1]
    whoWon = 0

    final_home_score = final_row["home_score"]
    final_away_score = final_row["away_score"]


    if final_home_score > final_away_score:
        whoWon = 1
    else:
        whoWon = 0

    return whoWon

        




    
