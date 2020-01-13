#!/bin/sh

#  Script.py
#  
#
#  Created by Tung Nguyen on 4/30/19.
#  http://scipy-lectures.org/intro/scipy/auto_examples/plot_curve_fit.html
# https://www.math.arizona.edu/~tgk/541/chap1.pdf
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
# https://www.researchgate.net/figure/Correlation-length-as-a-function-of-temperature-for-a-simulation-of-the-Ising-Model-Near_fig4_225375861


import pylab as py
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("list 0.5 - 3.5 .txt", float)
x_data = data[:,0]
y_data = data[:,1]

py.scatter(x_data,y_data)
py.xlabel("Temperature")
py.ylabel("Magnitude")
py.show()
