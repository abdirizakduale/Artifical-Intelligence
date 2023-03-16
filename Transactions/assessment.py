import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


#importing data

data = pd.read_csv('train.csv')

data['MSRP'] = data['PurchasePrice']/(1 - data['DiscountPct'])


#cdate = 'CustomerBirthDate'
#odate = 'OrderDate'

data = data[['ID','OrderID','CustomerID','CustomerState','CustomerBirthDate','OrderDate','ProductDepartment','ProductSize','ProductCost','DiscountPct','PurchasePrice','MSRP','Returned'
]]

#print(data.iloc[:, 8:12])
#data[cdate] = pd.to_datetime(data[cdate], format='%Y-%m-%d')
#data[odate] = pd.to_datetime(data[odate], format='%Y-%m-%d')

input_values = data.iloc[:, 8:12].values

#input_values = data.iloc[:, 0:10].values

prediction = data.iloc[:, 12]

first_col = data.iloc[:, 0]

#Spillting the data up

input_train, input_test, prediction_train, prediction_test = train_test_split(input_values, prediction, test_size = 0.2, random_state = 0)

#Scaling features

stan_s = StandardScaler()

input_train = stan_s.fit_transform(input_train)
input_test = stan_s.transform(input_test)

#Artificial Neural Network

model = Sequential()
model.add(Dense(units = 2.5, kernel_initializer = 'uniform', activation = 'relu', input_dim = 4))
model.add(Dense(units = 2.5, kernel_initializer = 'uniform', activation = 'relu'))
model.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#training and testing

model.fit(input_train, prediction_train, batch_size = 10, epochs = 20)

final_pred = model.predict(input_test)

# Uncomment to see my unfisished output

#print(data.iloc[:, 0], final_pred)

# This contails only my fianl prediction
print(final_pred)
