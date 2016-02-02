import pandas as pd
import matplotlib.pyplot as plt
import sys
import matplotlib

dsadasdadsadsad
sdasadsadsadsa
sdan
sdasasda
sss


df = pd.read_csv(csv_file)

DayofWeek = {'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
DayofWeekBinary = {'Monday':[0,0,0,0,0,0,1],
             'Tuesday':[0,0,0,0,0,1,0],
             'Wednesday':[0,0,0,0,1,0,0],
             'Thursday':[0,0,0,1,0,0,0],
             'Friday':[0,0,1,0,0,0,0],
             'Saturday':[0,1,0,0,0,0,0],
             'Sunday':[1,0,0,0,0,0,0]}



week = df['Week #']
dayofweek = df['Day of Week'].apply(lambda x: DayofWeek[x])
dayofweekbinary = df['Day of Week'].apply(lambda x: DayofWeekBinary[x])
backupstarttime = df['Backup Start Time - Hour of Day']
workflowid = df['Work-Flow-ID']
filename = df['File Name']
sizeofbackup = df['Size of Backup (GB)']
backuptime = df['Backup Time (hour)']


#plot
#for workflow0
mask = workflowid == 'work_flow_0'
workflow_0 = df[mask]

#test in workflow0 and file0

#print(test)








