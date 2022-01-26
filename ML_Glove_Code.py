#Code to be written to microcontroller, with appropriate inputs and outputs



#libraries
from ipaddress import collapse_addresses
from sqlite3 import Row
from tkinter import Y
import sklearn
from sklearn.model_selection import train_test_split as tts
from sklearn import svm
from sklearn.metrics import accuracy_score

import numpy as np
import pandas as pd

#inputs
#a -> accelerometer, ax ay az (normalized -1 to 1)
#g -> gyrometer, gx, gy, gz (normalized -1 to 1)
#m -> myoware, intensity input (normalized intensity 0 to 1), currently only this is available
#data -> training set 

#importing data file

col_list = [f'{i+1}' for i in range(0,15)]
df = pd.read_csv("Data.csv", usecols=col_list).drop(0)

clenchedfist = df[['2','3']].dropna() #test sample
mughold = df[['5','6']].dropna().rename(columns = {'5': '2', '6': '3'})
pouring = df[['8','9']].dropna().rename(columns = {'8': '2', '9': '3'})
leftright = df[['11','12']].dropna().rename(columns = {'11': '2', '12': '3'})
fingering = df[['14','15']].dropna().rename(columns = {'14': '2', '15': '3'})

frames = [clenchedfist, mughold, pouring, leftright, fingering]

data = pd.concat(frames).dropna()

X = data[['2']].astype(np.int32).to_numpy()
y = data[['3']].astype(np.int32).to_numpy()

X_train, X_test, y_train, y_test = tts(X,y,test_size=0.2)

model = svm.SVC()
model.fit(X_train, y_train.ravel())

predictions = model.predict(X_test)

acc = accuracy_score(y_test, predictions)

print(f"Accuracy of model: {acc*100}%")




#outputs
#

#Code 1 (TremorCheck)
    #Inputs -> Everything or myoware
    #Outputs -> tremor yes/no + intensity
#Code 2 (MovementCheck)
    #Inputs -> Accel and Gyro
    #Outputs -> Move yes/no + direction?
#Code 3 (RPM)
    #Inputs -> Everything (Accel, Gyro, Myo) + Move, Tremor and intensity
    #Outputs -> RPM

