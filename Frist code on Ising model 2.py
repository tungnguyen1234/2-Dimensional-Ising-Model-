#Program Ising
import random as rd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

size = 400
T = 4.00
B = 1

# Initial array of zero inputs
s = np.zeros((size, size))

#Generate a random array of grids
for i in range(0,size):
    for j in range(0,size):
        if rd.uniform(0,1) <.5:
            s[i,j] = 1
        else:
            s[i,j] = -1


#Define the potential different og flipping a dipole:
def deltaU(i,j):
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
    Ediff = 2*s[i,j]*(top+bottom+left+right)-s[i,j]
# Put colors inside the grid:
    return Ediff


for interation in range(1,100*size**2):
    #rand = rd.uniform(0,1)
    #rand1 = rd.uniform(0,1)
    i = int(rd.uniform(0,1)*size)
    j = int(rd.uniform(0,1)*size)
    Ediff = deltaU(i,j)
    if Ediff <= 0:
        s[i,j]= -s[i,j]
    elif rd.uniform(0,1) < np.exp(-Ediff/T):
        s[i,j]= -s[i,j]

#denote as data for graphing
data = s

# create discrete colormap
cmap = colors.ListedColormap(['white', 'black'])
bounds = [-1,0,1]
norm = colors.BoundaryNorm(bounds, cmap.N)
fig, ax = plt.subplots()
ax.imshow(data, cmap=cmap , norm=norm)

# draw gridlines
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
#ax.set_xticks(np.arange(-.5, size, 1));
#ax.set_yticks(np.arange(-.5, size, 1));
plt.show()

