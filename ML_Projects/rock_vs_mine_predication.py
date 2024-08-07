# -*- coding: utf-8 -*-
"""Rock_vs_Mine_Predication.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18XaQ6X2KDkLjPPUL5OT9hcOgL-j9gBh_
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""**Load the data**"""

sonar_data = pd.read_csv('/content/sonar data.csv', header=None)

sonar_data.head(2)

sonar_data.shape

"""**Statistical Measure**"""

sonar_data.describe()

sonar_data[60].value_counts()

sonar_data.groupby(60).mean()

"""**separeting data and labels**"""

X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

print(X)
print(Y)

"""**Training and Test data**"""

X_train,X_test,Y_train,Y_test = train_test_split(X,Y, stratify=Y, test_size=0.1, random_state=1)

print(X.shape, X_train.shape, X_test.shape)

"""**Model Training**"""

model = LogisticRegression()

model.fit(X_train, Y_train)

"""**Model Evaluation**"""

#accurcy on training data
x_training_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(x_training_prediction, Y_train)

print(f'Accuracy on training data: {training_data_accuracy}')

#accurcy on training data
x_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(x_test_prediction, Y_test)

print(f'Accuracy on test data: {test_data_accuracy}')

"""**Making A Predictive system**"""

input_data = (0.0090,0.0062,0.0253,0.0489,0.1197,0.1589,0.1392,0.0987,0.0955,0.1895,0.1896,0.2547,0.4073,0.2988,0.2901,0.5326,0.4022,0.1571,0.3024,0.3907,0.3542,0.4438,0.6414,0.4601,0.6009,0.8690,0.8345,0.7669,0.5081,0.4620,0.5380,0.5375,0.3844,0.3601,0.7402,0.7761,0.3858,0.0667,0.3684,0.6114,0.3510,0.2312,0.2195,0.3051,0.1937,0.1570,0.0479,0.0538,0.0146,0.0068,0.0187,0.0059,0.0095,0.0194,0.0080,0.0152,0.0158,0.0053,0.0189,0.0102)

#changing the data into numpy array
input_data_as_numpy_array = np.asarray(input_data)

#reshaped the array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]=='R'):
  print("The object is Rock")

else:
  print("The object is Mine")

