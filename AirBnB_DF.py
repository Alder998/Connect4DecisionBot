import ScrapingMethods as sc
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

data = pd.read_excel(r"C:\Users\39328\OneDrive\Desktop\Storing di cose di dubbia utilità futura\ExperienceDBTot - Backup.xlsx")

dfBase = sc.createTrainDatasetAirBnB(data, granuarity=3)

print('\n')
print('Length of Test Set:', len(dfBase['rating']))
print('\n')

split = train_test_split(dfBase, test_size=0.25, random_state=1893)

trainSet = split[1].reset_index()
del[trainSet['index']]
testSet = split[0].reset_index()
del[testSet['index']]

# Proviamo a prevedere con un KNN, ottimizziamo un minimo il numero di k

# Definiamo il train set
y_train = np.array(trainSet['Good Choice']).reshape(-1, 1)
y_train = np.ravel(y_train)
X_train = np.array(trainSet[['Price', 'rating', 'Reviews (number)', 'Not Italy']])

# Definiamo il test set
X_test = np.array(testSet[['Price', 'rating', 'Reviews (number)', 'Not Italy']])
y_test = np.array(testSet['Good Choice']).reshape(-1, 1)
y_test = np.ravel(y_test)

# Prendiamo tra i 5 e i 25 neighbors, selezioniamo quello con lo score R2 maggiore

possibleK = np.arange(5, 25)

scoreList = list()
KList = list()
for k in possibleK:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    scoreP = clf.score(X_test, y_test)
    scoreList.append(scoreP)
    KList.append(k)

scoreList = pd.Series(scoreList)
KList = pd.Series(KList)
scoreBase = pd.concat([KList, scoreList], axis = 1).set_axis(['K-Value', 'Score'], axis = 1)

bestK = scoreBase['K-Value'][scoreBase['Score'] == scoreBase['Score'].max()].reset_index()['K-Value'][0]

clf = KNeighborsClassifier(n_neighbors=bestK)
clf.fit(X_train, y_train)

test_score = clf.score(X_test, y_test)

print('Model Score ( k =', bestK, ') : ', round(test_score*100, 2), '%')

print('\n')
probab = list()
for prob in (clf.predict_proba(X_test)):
    probab.append(prob[1])

probabilityToBeGoodChoice = pd.DataFrame(probab).set_axis(['Probability KNN'], axis=1)

# Creiamo il DataFrame Finale

dfFinal = pd.concat([testSet, probabilityToBeGoodChoice], axis=1)

# Creiamo un Output che sia una top ten dei posti dove andare

TopTen = dfFinal.sort_values(by = 'Probability KNN', ascending=False)
TopTen = TopTen.drop_duplicates(subset = 'Place', keep = 'first').reset_index()
del[TopTen['index']]

print('Top 10 Best places to go holiday this summer:')
print('\n')

topTenCounter = np.arange(1, 10)
for value in topTenCounter:
    print(TopTen['Place'][value], '(', TopTen['Country'][value], ')' , '== Probability to be a good choice:',
              TopTen['Probability KNN'][value] )

dfFinal.to_excel(
        r"C:\Users\39328\OneDrive\Desktop\Storing di cose di dubbia utilità futura\ExperienceDBTot - ProvaProb - KNN.xlsx")



