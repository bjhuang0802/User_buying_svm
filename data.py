#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import random
import numpy as np

def data(rate):
    #0(string).uid, 1(int).member 0/1, 2(int).session, 3(float). tstime, 
    #4(int). ADs, 5(int). no. product-view, 6(float). maximum time of a product view 
    items=[]
    y=[]
    invitems={}
    raw0 = csv.reader(open('dic_0_uuid.txt'))
    raw1 = csv.reader(open('dic_1_member.txt'))
    raw2 = csv.reader(open('dic_2_sessions.txt'))
    raw3 = csv.reader(open('dic_3_tstime.txt'))
    raw4 = csv.reader(open('dic_4_ADs.txt'))
    raw6 = csv.reader(open('dic_product_summary.txt'))
    rawf = csv.reader(open('dic_ever_final.txt'))
    features=['Member','no.sessions','Total Time','no. ADs','no. uniqe product-view','maximum time of product-view']
    i=0
    for row in raw0:
        items.append([str(row[0])])
        invitems[str(row[0])]=int(i)
        for x in range(1,7):
            items[i].append(0)
        y.append(1)
        i +=1

    for row in raw1:
        x=invitems[str(row[0])]
        items[x][1]=1

    for row in raw2:
        x=invitems[str(row[0])]
        items[x][2]=int(row[1])

    for row in raw3:
        x=invitems[str(row[0])]
        items[x][3]=float(row[1])

    for row in raw4:
        x=invitems[str(row[0])]
        items[x][4]=int(row[1])

    for row in raw6:
        x=invitems[str(row[0])]
        items[x][5]=int(row[1])
        items[x][6]=float(row[2])

    for row in rawf:
        x=invitems[str(row[0])]
        y[x]=2

    #0(string).uid, 1(int).member 0/1, 2(int).session, 3(float). tstime, 
    #4(int). ADs, 5(int). no. product-view, 6(float). maximum time of a product view 
    train_y=[]
    train_x=[]
    for i in range(0,len(items)):
        if items[i][3] >0:
            if y[i] == 2:
                train_x.append(items[i][1:])
                train_y.append(y[i])
            else:
                 if random.random() <rate:
                    train_x.append(items[i][1:])
                    train_y.append(y[i])

    return train_x,train_y,features
