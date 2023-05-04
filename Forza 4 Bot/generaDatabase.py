
import Forza4Methods as f4
import pandas as pd

#f4.updateDataBase(50000)

#df = pd.read_excel(r"C:\Users\39328\OneDrive\Desktop\Davide\Velleità\Forza 4 Algoritmo\Dataset\finalDataSet.xlsx")

df = pd.read_excel(r"C:\Users\39328\OneDrive\Desktop\Davide\Velleità\Forza 4 Algoritmo\Dataset\finalDataSetV3 - GreedyMix.xlsx").dropna()

df['Win'] = df['Win1']
del[df['Win1']]
del[df['WIn2']]

f4.createModel(df, testSize=0.20,  version='V3')

