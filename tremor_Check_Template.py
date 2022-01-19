#Tremor_Check: Initial code to determine if tremor is occuring
#Uses myoware voltage input to determine when tremors occur

#Import Libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

#Define functions

# moving_Average: Calculates the average trendline based on N readings
### interval: The number of readings
### window_size: How close your trendline is to the actual line
def moving_Average(interval, window_size): 
    window = np.ones(int(window_size)) / float(window_size)
    return np.convolve(interval, window, 'same')

# intensity_Check: Determines if the average intensity is a tremor
### val: The average intensity over N readings
def intensity_Check(val): 
    if (val > sensitivity): #Sensitivity var used to tweak the tremor threshold
        tremor = "Yes"
    else:
        tremor = "No"
    return tremor

# animate: Updates the graph in real-time every t seconds
### i: The n'th interation
def animate(i, x, y):
    #Update lists
    x.append(i)         #Append current x and y to their lists 
    y.append(freq.val)  #This value will need to be changed to be the myoware voltage

    x = x[-50:]         #Take 50 most recent readings
    y = y[-50:]

    #Graph that bad boy
    ax1.clear()         #Reset the plots
    ax2.clear()
    ax1.set(title="Myoware Readings", xlabel="Time(10ms)", ylabel="Voltage(mV)") #Label your work >:(
    ax2.set(title="Linearized Intensity", xlabel="Time(10ms)", ylabel="Amplitude(Absolute)")
    
    ax1.plot(x,y)       #Plot the raw data
    if (i > 50):        #If sufficient readings have been taken to get an average
        y_ave = moving_Average(y, (len(y)/(len(y)/(ave_sensitivity))))  #Average y value accounting for curve
        intensity = abs(y-y_ave)    #Difference between average value and true value (noise)
        intensity_ave = int(sum(intensity[-20:])/0.2 - (y[-1:])) / 1000  #Converting intensity into an absolute val between 0-1
        if (intensity_ave < 0): #Redundancy to prevent negative values
            intensity_ave = 0
        ax1.plot(x, y_ave, "r") #Plot average curve over real curve
        ax2.plot(x, intensity, "g") #Plot the tremor amplitude

        tremorCheck = intensity_Check(intensity_ave)    #Check if tremor is occuring
        tremor.set_text(tremorCheck)        #Update text
        amplitude.set_text(intensity_ave)   
    

#Real coding hours
#Declare variables
x= []       #Array for time interval
y = []      #Array for Myoware voltage
y_ave = []  #Array for average curve
i = 0       #Initialize time_step
t = 10     #Time between readings (ms)
sensitivity = 0.3
ave_sensitivity = 4

#Formatting the figure space
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)    #Plot for data + average
ax2 = fig.add_subplot(2,2,2)    #Plot for amplitude
box1 = ax1.get_position()       #Moving stuff around
box1.x0 = box1.x0 - 0.02
box1.x1 = box1.x1 - 0.02
ax1.set_position(box1)

#Text boxes to update
fig.text(0.44, 0.25, "Tremor?")
tremor = fig.text(0.54, 0.25, "N/A")
fig.text(0.375, 0.35, "Avg Intensity?")
amplitude = fig.text(0.54, 0.35, "Hot")

#Add slider to emulate trembling (could be removed after)
axfreq = plt.axes([0.25, 0.15, 0.65, 0.03])
freq = Slider(axfreq, 'Frequency', 0.0, 100, 50)

#Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(x,y), interval=t)
plt.show()