#Code to be written to microcontroller, with appropriate inputs and outputs



#libraries
import sklearn
from sklearn.model_selection import train_test_split as tts;
from sklearn import svm;

import numpy as np
import pandas as pd

#inputs
#a -> accelerometer, ax ay az (normalized -1 to 1)
#g -> gyrometer, gx, gy, gz (normalized -1 to 1)
#m -> myoware, intensity input (normalized intensity 0 to 1), currently only this is available
#data -> training set 

#importing data file

col_list = []

for i in range(0,14):
    col_list.append('{}'.format(i+1))


df = pd.read_csv("Data.csv", usecols=col_list)

data1 = df[0:2]

print(data1)

#X = df[['CH1']].values
#y = df[['Tremor?']].values










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

