import Forza4Methods as f4

import pandas as pd
import Forza4Methods as f4
import random
import numpy as np

baseData = pd.read_excel(r"C:\Users\39328\OneDrive\Desktop\Davide\Velleità\Forza 4 Algoritmo\10kGamesSimulator.xlsx")

ind = 0  # 630 ha una vittoria obliqua destra e una sinistra

game = baseData.loc[:, baseData.columns != 'Win'].iloc[ind]

sGame = f4.convertToVisualGame(game)

print(sGame)

print(f4.isWin(game))


