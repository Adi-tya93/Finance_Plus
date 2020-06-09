import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

plt.style.use('bmh')

df = pd.read_csv('stockrev.csv')

plt.figure(figsize=(16, 8))
plt.title('Microsoft')
plt.xlabel('Days')
plt.ylabel('Open Price in USD')
plt.plot(df['1. open'])
plt.show

# had to drop each cloumn individually. Reason: Using df[1. open] gives an array instead of pandas data frame
df = df.drop(columns=['date',  '2. high',	'3. low',	'4. close',	'5. volume'])

future_days = 25
df['Prediction'] = df[['1. open']].shift(-future_days)

# create the feature data set (X) and convert it to a numpy array and remove the last '2*x' rows/days
X = np.array(df.drop(['Prediction'], 1))[:-(2*future_days)]

# create the target data set (y) and convert it to numpy array and get all of the taget values except the last "2*x" rows
y = np.array(df['Prediction'])[:-(2*future_days)]

# Didnt need to split as we are using last 25 days to test. But just in case for accuracy checks
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.01)

tree = DecisionTreeRegressor().fit(X_train, y_train)
lr = LinearRegression().fit(X_train, y_train)

X_future = df.drop(['Prediction'], 1)[:-future_days]
X_future = X_future.tail(future_days)
X_future = np.array(X_future)

tree_prediction = tree.predict(X_future)
print(np.array(df.drop(['Prediction'], 1))[-future_days:])
print()
print(tree_prediction)
print()
lr_prediction = lr.predict(X_future)
print(lr_prediction)

actual = df['1. open'][-100:]
valid = df[-future_days:]
valid['Predictions'] = tree_prediction
valid = valid['Predictions']

ar = list()
for index, items in enumerate(actual):
    ar.append([index, 0, items])

print(ar)

for index, items in enumerate(valid):
    ar[index + 75][1] = items

print(ar)


#predictions = tree_prediction

#valid = df[-future_days:]
#valid['Predictions'] = predictions
#plt.figure(figsize=(16, 8))
# plt.title('Model')
# plt.xlabel('Days')
#plt.ylabel('Open Price in USD')
#plt.plot(df['1. open'][-100:])
#plt.plot(valid[['1. open', 'Predictions']])
#plt.legend(['Original', 'Valid', 'Prediction'])
# plt.show

#predictions = lr_prediction

#valid = df[-future_days:]
#valid['Predictions'] = predictions
#plt.figure(figsize=(16, 8))
# plt.title('Model')
# plt.xlabel('Days')
#plt.ylabel('Open Price in USD')
#plt.plot(df['1. open'][-100:])
#plt.plot(valid[['1. open', 'Predictions']])
#plt.legend(['Original', 'Valid', 'Prediction'])
# plt.show
