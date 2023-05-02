import Forza4Methods as f4

import pandas as pd
import Forza4Methods as f4
import random
import numpy as np
import time

start = time.time()

base = pd.read_excel(r"C:\Users\39328\OneDrive\Desktop\Davide\Velleità\Forza 4 Algoritmo\Dataset\finalDataSetV3 - GreedyMix.xlsx")
baseLen = len(base['Win1'])

d = f4.greedyV3Data(baseLen)

end = time.time()
print('\n')
print('Greedy-Method Games Created in:', round((end-start)/60, 0), 'Minutes')

