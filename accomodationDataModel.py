# qui implementeremo il modello per esaminare le nostre features ed avere dei risultati e delle analytics di
# spessore sui nostri dati, che abbiamo creato con molta difficoltà

import pandas as pd
import numpy as np
import statsmodels.api as sm
import ScrapingMethods as sc
from sklearn.linear_model import LinearRegression, Ridge, Lasso
import scipy.stats as stats
import matplotlib.pyplot as plt

# importiamo il dataset

df = pd.read_excel(r"C:\Users\39328\OneDrive\Desktop\Storing di cose di dubbia utilità futura\CamereMilanoBooking1.xlsx")

# Puliamolo
df = sc.cleanAndEncodeAccomodationDataset(df, remove_outliers=False, price_limit=800, del_rating_reviews=True,
                                          exclude_luxury=False, price_per_person=False)

# Il nostro df è pronto. Partiamo Esaminando i coefficienti di regressione lineare. Usiamo statsmodels per vedre l'effetto
# di ogni variabile

regressors = df.loc[:, df.columns != 'Price']
#regressors = sm.add_constant(regressors)
dependent = df['Price']

coeff = sm.OLS(dependent, regressors).fit()

print(coeff.summary())
print('\n')

tfHrfrontDesk = 0
nonSmokingRooms = 1
restaurant = 1
privateParking = 0
coffeMakerInRooms = 0
roomService = 0
bar = 1
WiFi = 1
pets = 0
breakfast = 1
distanceFromCentre = 15
typeAcc = 1

stanza8 = [ tfHrfrontDesk, nonSmokingRooms, restaurant, privateParking, coffeMakerInRooms,roomService,
           bar, WiFi, pets, breakfast, distanceFromCentre, 1]
stanza4 = [ tfHrfrontDesk, nonSmokingRooms, restaurant, privateParking, coffeMakerInRooms,roomService,
           bar, WiFi, pets,breakfast, distanceFromCentre, 4]
stanzaTripla = [ tfHrfrontDesk, nonSmokingRooms, restaurant, privateParking, 1,roomService,
                bar, WiFi, pets,breakfast, distanceFromCentre, 7]
stanzaDoppia = [ tfHrfrontDesk, nonSmokingRooms, restaurant, privateParking, 1,roomService,
                bar, WiFi, pets,breakfast, distanceFromCentre, 8]
stanzaSingola = [ tfHrfrontDesk, nonSmokingRooms, restaurant, privateParking, 1,roomService,
                 bar, WiFi, pets,breakfast, distanceFromCentre, 9]


listino = [stanza8, stanza4, stanzaTripla, stanzaDoppia, stanzaSingola]

# Facciamo una prova con Sklearn

modelLasso = Lasso(alpha = 1e-12, fit_intercept=True, positive=True)
modelLasso.fit(regressors, dependent)

modelRidge = Ridge(alpha = 100, fit_intercept=True, positive=True)
modelRidge.fit(regressors, dependent)

modelLR = LinearRegression(fit_intercept=True, positive=True)
modelLR.fit(regressors, dependent)

print('Model: Lasso Linear')
for it, type in enumerate(listino):

    if it == 0:
        nome = '1 bed in 8 People Dorm'
    if it == 1:
        nome = '1 bed in 4 People Dorm'
    if it == 2:
        nome = 'Triple Room (per Person)'
    if it == 3:
        nome = 'Double Room (per Person)'
    if it == 4:
        nome = 'Single Room (per Person)'

    toPredict = pd.DataFrame(np.array(type).reshape(1, -1), columns = regressors.columns)
    print('Price of', nome, ': €', round((modelLasso.predict(toPredict)[0]), 2) )

print('\n')
print('Model R-Squared:', modelLasso.score(regressors, dependent))

print('\n')
print('Model: Ridge Linear')
for it, type in enumerate(listino):

    if it == 0:
        nome = '1 bed in 8 People Dorm'
    if it == 1:
        nome = '1 bed in 4 People Dorm'
    if it == 2:
        nome = 'Triple Room (per Person)'
    if it == 3:
        nome = 'Double Room (per Person)'
    if it == 4:
        nome = 'Single Room (per Person)'

    toPredictRidge = pd.DataFrame(np.array(type).reshape(1, -1), columns = regressors.columns)
    print('Price of', nome, ': €', round((modelRidge.predict(toPredictRidge)[0]), 2) )

print('\n')
print('Model R-Squared:', modelRidge.score(regressors, dependent))

print('\n')
print('Model: Linear Regression')
for it, type in enumerate(listino):

    if it == 0:
        nome = '1 bed in 8 People Dorm'
    if it == 1:
        nome = '1 bed in 4 People Dorm'
    if it == 2:
        nome = 'Triple Room (per Person)'
    if it == 3:
        nome = 'Double Room (per Person)'
    if it == 4:
        nome = 'Single Room (per Person)'

    toPredict = pd.DataFrame(np.array(type).reshape(1, -1), columns = regressors.columns)
    print('Price of', nome, ': €', round((modelLR.predict(toPredict)[0]), 2) )

print('\n')
print('Model R-Squared:', modelLR.score(regressors, dependent))


