# qui implementeremo il modello per esaminare le nostre features ed avere dei risultati e delle analytics di
# spessore sui nostri dati, che abbiamo creato con molta difficoltà

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression, Ridge, Lasso
import scipy.stats as stats
import matplotlib.pyplot as plt
import ScrapingMethods as sc
from scipy.optimize import minimize
from sklearn.metrics import make_scorer

# importiamo il dataset

df = pd.read_excel(r"C:\Users\39328\OneDrive\Desktop\Storing di cose di dubbia utilità futura\CamereMilanoBooking1.xlsx")

# Puliamolo
df = sc.cleanAndEncodeAccomodationDataset(df, keep_names=True, keep_type=True, remove_outliers=False, price_limit=500,
                                          del_rating_reviews=False, exclude_luxury=False, price_per_person=False)

# mettiamo le reviews come int, perché di base non lo sono

df['Reviews'] = df['Reviews'].astype(str).str.replace('.', '', regex=True).astype(int)

# creiamo una funzione

w1 = 1
w2 = 1
w3 = 1

df['Function'] = (df['Reviews']*w1 + df['Rating']*w2) / df['Price']*w3

print('\n')

print('Migliore Alternativa:', df['Type'][df['Function'] == df['Function'].max()].reset_index()['Type'][0],
      'at', df['Name'][df['Function'] == df['Function'].max()].reset_index()['Name'][0])


df.to_excel(r"C:\Users\39328\OneDrive\Desktop\Storing di cose di dubbia utilità futura\CamereMilanoBookingTest.xlsx")




