#Code to be written to microcontroller, with appropriate inputs and outputs



#libraries
import sklearn
from sklearn import train_test_split as tts;
from sklearn import svm;

import numpy as np
import pandas as pd

#inputs
#a -> accelerometer, ax ay az (normalized -1 to 1)
#g -> gyrometer, gx, gy, gz (normalized -1 to 1)
#m -> myoware, intensity input (normalized intensity 0 to 1)
#data -> training set 


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

