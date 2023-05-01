# Dataset V3
# Smart way to generate the game dataset: we just want WINS

import pandas as pd
import numpy as np
import random
import Forza4Methods as f4
import time

data = pd.read_excel(r"C:\Users\39328\OneDrive\Desktop\Davide\Velleità\Forza 4 Algoritmo\Dataset\finalDataSetV3.xlsx")

start = time.time()

totalGames = 500

games = list()
for game in range(0, totalGames):
    games.append(f4.V3DataBase_generateSingleMatch())
    print('Progress:', round((game/totalGames)*100, 2), '%')
games = pd.concat([series for series in games], axis = 0)
games = games.drop_duplicates().fillna(0)

games = games.reset_index()
del[games['index']]

finalData = pd.concat([data, games], axis = 0)

finalData.to_excel(r"C:\Users\39328\OneDrive\Desktop\Davide\Velleità\Forza 4 Algoritmo\Dataset\finalDataSetV3.xlsx",
               index = False)

print('\n')
print('Database size:', len(finalData['Win1']))
print('Total Wins (X):', len(finalData['Win1'][finalData['Win1'] == 1]))
print('Total Wins (O):', len(finalData['WIn2'][finalData['WIn2'] == 1]))

end = time.time()

print('\n')
print(totalGames, 'Games Created in:', round((end-start)/60, 0), 'Minutes')