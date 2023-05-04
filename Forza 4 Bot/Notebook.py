import Forza4Methods as f4

import pandas as pd
import Forza4Methods as f4
import random
import numpy as np
import time
from sklearn.model_selection import train_test_split

#start = time.time()
#
#base = pd.read_excel(r"C:\Users\39328\OneDrive\Desktop\Davide\Velleità\Forza 4 Algoritmo\Dataset\finalDataSetV3 - GreedyMix.xlsx")
#baseLen = len(base['Win1'])
#
##baseLen= 10
#
#d = f4.greedyV3Data(baseLen)
#
#end = time.time()
#print('\n')
#print('Greedy-Method Games Created in:', round((end-start)/60, 0), 'Minutes')


baseData = pd.read_excel(r"C:\Users\39328\OneDrive\Desktop\Davide\Velleità\Forza 4 Algoritmo\10kGamesSimulator.xlsx")

ind = 334  # 630 ha una vittoria obliqua destra e una sinistra

winInd = baseData['Win'][ind]
if winInd == 1:
    print('Win: Yes')
if winInd == 0:
    print('Win: No')

print('\n')

game = baseData.loc[:, baseData.columns != 'Win'].iloc[ind]
gameExample = pd.DataFrame(game).set_axis([0], axis = 1)

sGame = f4.convertToVisualGame(game)

print(sGame)

print('\n')

a = f4.MLBlockOpponentWin(gameExample, model = 'SVM', version = 'V1_Opponent')

print(a)