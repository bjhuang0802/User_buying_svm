#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import numpy as np


rawuuid = csv.reader(open('dic_0_uuid.txt'))
fp=open('dic_product_time.txt')
rawptime = csv.reader(fp)
fp1=open('dic_product_summary.txt','w')

sstime={}
ptime={}
for row in rawuuid:
    ptime[str(row[0])]={}

for row in rawptime:
    ptime[str(row[0])][str(row[1])]=0.0

fp.seek(0)
for row in rawptime:
    ptime[str(row[0])][str(row[1])] += float(row[2]) 


parray=[[]]
i=0
for key, value in ptime.iteritems():
    if len(value) >0:
        s=value.values()
        s1=sorted(s)
        parray[i].append(key)
        parray[i].append(len(value))
        parray[i].append(s1[0])
        i += 1
        parray.append([])

del parray[-1]

for x in range(0,len(parray)):
    #print '%s,%d,%6.2f' %(parray[x][0],parray[x][1],parray[x][2])
    print >>fp1,'%s,%d,%6.2f' %(parray[x][0],parray[x][1],parray[x][2])

        #print key, len(value), s1[0]