# import needed libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes as ax
import pylab

# change to proper directory
os.chdir('C:\Users\Matt\Desktop\Python Projects\Exploratory Data Analysis')

# load file, select proper date range, convert row to numeric dtypes
hpc = pd.read_csv('household_power_consumption.txt', sep=';', index_col=['Date'], usecols=['Global_active_power', 'Date'])
hpc = hpc['1/2/2007':'2/2/2007'].convert_objects(convert_numeric=True)

# create plotting variables
y = pd.value_counts(hpc.Global_active_power, bins=np.arange(0, 8, 0.5), sort=False)
index = y.index

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.bar(index, y, width=0.5, color='r')
ax.set_xlabel('Global Active Power (kilowatts)')
ax.set_ylabel('Frequency')
ax.set_title('Global Active Power')
pylab.show()


# hpc[hpc['Global_active_power'] > 4]
