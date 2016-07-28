#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import numpy as np
#import pprint

fp = open('dic_time_per_log.txt','w')
fp1= open('dic_3_tstime.txt','w')
#0.uid,  1.No. of AD 
uidtime=[]
rawfile = csv.reader(open('logs_sort.csv'))
rawuuid = csv.reader(open('dic_0_uuid.txt'))

i=0
for row in rawfile:
    uidtime.append([])
    uidtime[i].append(str(row[0]))
    uidtime[i].append(int(row[1]))
    uidtime[i].append(str(row[2]))
    uidtime[i].append(int(row[3]))
    uidtime[i].append(0)
    i +=1

sstime={}
for row in rawuuid:
    sstime[str(row[0])]=0
ss=1
#sstime=0
for i in range(0,len(uidtime)-1):
    if str(uidtime[i+1][0]) == str(uidtime[i][0]):
        time=uidtime[i+1][1]-uidtime[i][1]
        time = time * 1.0/60.0
        if time < 30.0:
            uidtime[i][4]=time
            sstime[str(uidtime[i][0])]=sstime[str(uidtime[i][0])] +time
            print >>fp,'%s,%12d,%s,%8d,%6.2f' %(uidtime[i][0],uidtime[i][1],uidtime[i][2],uidtime[i][3],uidtime[i][4])
        else:
            uidtime[i][4]=0
            #print '%5d,%s,%6.2f' %(ss,uidtime[i][0],sstime)
            #print>>fp1, '%s,%6.2f' %(uidtime[i][0],sstime)
            print >>fp,'%s,%12d,%s,%8d,%6.2f' %(uidtime[i][0],uidtime[i][1],uidtime[i][2],uidtime[i][3],uidtime[i][4])
            ss = ss+1
            #sstime =0
        
    else:
        uidtime[i][4]==0
        print >>fp,'%s,%12d,%s,%8d,%6.2f' %(uidtime[i][0],uidtime[i][1],uidtime[i][2],uidtime[i][3],uidtime[i][4])
        #print >>fp1,'%s,%6.2f' %(uidtime[i][0],sstime)
        #print 'ss:%5d' %(ss)
        ss = ss+1
    
for row in sstime:
    print >>fp1,'%s,%6.2f' %(row,sstime[row])
    #print '%s,%6.2f' %(row,sstime[row])
print 'Finish general time evaluation.'
