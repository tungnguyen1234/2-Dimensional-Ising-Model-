#!/bin/sh

#  problem 8.26.sh
#  Thermal Physics
#
#  Created by Tung Nguyen on 4/20/19.
#  This file has the same packages as the file problem 8.29 -d.py.
#  But this file is used for drawing the graph of colleration length and temperature

#Program Ising
import random as rd
import numpy as np
import pylab as py
import matplotlib.pyplot as plt
from matplotlib import colors

size = 20 # The size of the lattice
Temp = []
for T in np.arange(2.5,3.5,0.05): # Temperature array
    Temp.append(T)

#Define the potential different when flipping a dipole:
def deltaU(i,j,s,size=20):
    if i == 0:
        top = s[size-1,j]
    else:
        top = s[i-1,j]
    if i == size-1:
        bottom = s[0,j]
    else:
        bottom = s[i+1,j]
    if j == 0:
        left = s[i,size-1]
    else:
        left = s[i,j-1]
    if j == size-1:
        right = s[i,0]
    else:
        right = s[i,j+1]
    Ediff = 2*s[i,j]*(top+bottom+left+right)
    # Put colors inside the grid:
    return Ediff

def isingmodel(T,size=20):
    # Initial array of zero inputs
    s = np.zeros((size, size))
    
    #Generate a random array of grids
    for i in range(0,size):
        for j in range(0,size):
            if rd.uniform(0,1) <.5:
                s[i,j] = 1
            else:
                s[i,j] = -1
    # Create the process of magnetization of the grids
    for interation in range(1,100*size**2):
        i = int(rd.uniform(0,1)*size)
        j = int(rd.uniform(0,1)*size)
        Ediff = deltaU(i,j,s,size)
        if Ediff <= 0:
            s[i,j]= -s[i,j]
        elif rd.uniform(0,1) < np.exp(-Ediff/T):
            s[i,j]= -s[i,j]
    return s

# Define the correlative function calculating over a data
def Col(data, size =20):
    index = np.zeros(size)
    index += 0.01
    sum = np.zeros(size)
    spin = np.zeros(size)
    for p in range(1,100*size**2):
        i = int(rd.uniform(0,1)*size)
        j = int(rd.uniform(0,1)*size)
        k = int(rd.uniform(0,1)*size)
        m = int(rd.uniform(0,1)*size) 
        r1 = np.sqrt((i - k)**2 + (j - m)**2)
        r2 = np.sqrt((i - k + size)**2 + (j - m)**2)
        r3 = np.sqrt((i - k)**2 + (j - m + size)**2)
        r4 = np.sqrt((i - k - size)**2 + (j - m)**2)
        r5 = np.sqrt((i - k)**2 + (j - m - size)**2)
        r6 = np.sqrt((i - k + size)**2 + (j - m + size)**2)
        r7 = np.sqrt((i - k - size)**2 + (j - m - size)**2)
        r8 = np.sqrt((i - k - size)**2 + (j - m + size)**2)
        r9 = np.sqrt((i - k + size)**2 + (j - m - size)**2)
        rad = int(np.min((r1, r2, r3, r4, r5, r6, r7, r8, r9)))
        if (rad>0):
            index[rad] += 1
            sum[rad] += data[i,j]*data[k,m]
            spin[rad] += data[i,j]

#Create a plot database for the collaboration function
    collaborative = []
    for rad in range(0,size):
        average = sum[rad]/index[rad] - (spin[rad]/index[rad])**2;
        collaborative.append(average)
    return collaborative
