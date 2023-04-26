# giochiamo con i dati sul file dei rating, e vediamo se riusciamo a prevedere qualche cosa

import pandas as pd
import numpy as np
import sklearn as sk
import matplotlib as plt

# Prendiamo i Rating di S&P

sp500 = pd.read_excel(r"D:\Credit Rating Data\Excel\2022 - S&P 500 Ratings.xlsx")

# creiamo un Dataset fatto bene

# Seleziona solo le colonne utili, e cioè nome dell'azienda, data, view della società di rating, e rating
spRatingDf = sp500[['obligor_name', 'rating_action_date', 'rating_outlook', 'rating']]

# selezioniamo un preciso anno, nel nostro caso il 2021
spRatingDf = spRatingDf[(spRatingDf['rating_action_date'].astype(str)).str.contains('2020')]

# eliminiamo le aziende not-rated, e i NaN, e i valori duplicati
spRatingDf = spRatingDf[spRatingDf['rating'] != 'NR'].dropna()
spRatingDf = spRatingDf.drop_duplicates(subset = 'obligor_name').reset_index()
del[spRatingDf['index']]

print(spRatingDf)


