"""Assignment 1"""
import csv
import numpy as np

### Constants
OFFSET_C_TO_F = 32
FACTOR_C_TO_F = 1.8
PATH_TO_WEATHERDATA = './../../../data/weather_data.csv'
THREASHHOLDTEMPERATURE = 25

#### Functions
def changetofahrenheit(celsius):
    """
    This function changes temperature above 25°C to Fahrenheit
    """
    temp =[]
    for i in celsius:
        if float(i[1]) > THREASHHOLDTEMPERATURE:
            temp.append(float(i[1]) * FACTOR_C_TO_F + OFFSET_C_TO_F)
        else:
            temp.append(float(i[1]))
    return temp

def avg_windspeed(ds):
    """
    calculate the wind speed of u and v
    """
    ws = 0
    for i in ds:
        u = float(i[3])
        v = float(i[4])
        ws += (u * u + v * v) **0.5
        avg_ws = ws / len(ds)
    return avg_ws

### Dataset
file = open(PATH_TO_WEATHERDATA)
ds =list(csv.reader(file))
file.close()

# Changing Dataset
ds = ds[1:] # remove first row
data=[]
for i in ds:
    data.append([i[0],i[1],i[2],i[3],i[4]])


### Start Calculations
# Temperature
temp = changetofahrenheit(data)
sum_temp = np.sum(temp)
avg_temp = np.mean(temp)
print('sum of temperature', sum_temp)
print('avg of temperature', avg_temp)

# Windspeed
avg_ws = avg_windspeed(data)
print('avg of windspeed', avg_ws)
