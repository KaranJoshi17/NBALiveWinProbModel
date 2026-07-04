# TRAINS THE MODEL

import pandas as pd
import time_utils.py

from sklearn import train_test_split , LogisticRegression , accuracyscore , joblib


# load the data
df = pd.read_csv("dec25_2025_games.csv")


# the feature part

seconds_remaining = timeToSeconds()




# train part


model = LogisticRegression()




