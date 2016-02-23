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
hpc = pd.read_csv('household_power_consumption.txt', sep=';', index_col=['Date'], usecols=['Sub_metering_1', 'Sub_metering_2', 'Sub_metering_3', 'Date'])
# hpc = hpc.drop(['Date', 'Time'], axis=1).set_index('DT')
hpc = hpc['1/2/2007':'3/2/2007'].convert_objects(convert_numeric=True)
hpc = hpc[0:2881]
# create plotting variables
x = pd.date_range('2/1/2007', '2/3/2007 00:00', freq='T')
y1 = hpc.Sub_metering_1
y2 = hpc.Sub_metering_2
y3 = hpc.Sub_metering_3

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(x, y1, color='k', label='Sub_metering_1')
ax.plot(x, y2, color='r', label='Sub_metering_2')
ax.plot(x, y3, color='b', label='Sub_metering_3')
ax.legend(loc='best')
ax.set_xticklabels(['Thur', '', '', '', 'Fri', '', '', '','Sat'])
ax.set_yticklabels(['0', '',  '10', '', '20', '', '30'])

#plt.xlabel('Global Active Power (kilowatts)')
ax.set_ylabel('Energy sub metering')
#plt.title('Global Active Power')
pylab.show()