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
# hpc = hpc.drop(['Date', 'Time'], axis=1).set_index('DT')
hpc = hpc['1/2/2007':'3/2/2007'].convert_objects(convert_numeric=True)
hpc = hpc[0:2881]
# create plotting variables
x = pd.date_range('2/1/2007', '2/3/2007 00:00', freq='T')
y = hpc['Global_active_power']
#plt.plot(y, color='k')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y, color='k')
ax.set_xticklabels(['Thur', '', '', '', 'Fri', '', '', '','Sat'])
ax.set_yticklabels(['0', '',  '2', '', '4', '', '6'])
#plt.xlabel('Global Active Power (kilowatts)')
ax.set_ylabel('Global Active Power (kilowatts)')
#plt.title('Global Active Power')
pylab.show()