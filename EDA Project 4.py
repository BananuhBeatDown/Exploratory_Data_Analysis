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
hpc = pd.read_csv('household_power_consumption.txt', sep=';', index_col=['Date'])
# hpc = hpc.drop(['Date', 'Time'], axis=1).set_index('DT')
hpc = hpc['1/2/2007':'3/2/2007'].convert_objects(convert_numeric=True)
hpc = hpc[0:2881]
# create plotting variables
x = pd.date_range('2/1/2007', '2/3/2007 00:00', freq='T')
gap = hpc.Global_active_power
vol = hpc.Voltage
sm1 = hpc.Sub_metering_1
sm2 = hpc.Sub_metering_2
sm3 = hpc.Sub_metering_3
gre = hpc.Global_reactive_power

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(x, gap, color='k')
ax1.set_xticklabels(['Thur', '', '', '', 'Fri', '', '', '','Sat'])
ax1.set_yticklabels(['0', '', '2', '', '4', '', '6'])
ax1.set_xlabel('Global Active Power')

ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(x, vol, color='k')
ax2.set_xticklabels(['Thur', '', '', '', 'Fri', '', '', '','Sat'])
ax2.set_yticklabels(['234', '',  '238', '', '242', '', '246'])
ax2.set_ylabel('Voltage')
ax2.set_xlabel('datetime')

ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(x, sm1, color='k', label='Sub_metering_1')
ax3.plot(x, sm2, color='r', label='Sub_metering_2')
ax3.plot(x, sm3, color='b', label='Sub_metering_3')
ax3.legend(loc='best')
ax3.set_xticklabels(['Thur', '', '', '', 'Fri', '', '', '','Sat'])
ax3.set_yticklabels(['0', '',  '10', '', '20', '', '30'])
ax2.set_ylabel('Energy sub metering')

ax4 = fig.add_subplot(2, 2, 4)
ax4.plot(x, gre, color='k')
ax4.set_xticklabels(['Thur', '', '', '', 'Fri', '', '', '','Sat'])
ax4.set_ylabel('Global_reactive_power')
ax4.set_xlabel('datetime')

# plt.xlabel('Global Active Power (kilowatts)')
# plt.ylabel('Energy sub metering')
#plt.title('Global Active Power')
pylab.show()