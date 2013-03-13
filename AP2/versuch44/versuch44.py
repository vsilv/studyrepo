# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
import ocd
messung=ocd.open_csv("messung252.csv")
messung=ocd.open_csv("messung253.csv")
messung=ocd.open_csv("messung254.csv")
U=sy.Symbol("U")
I=sy.Symbol("I")
R=sy.Symbol("R")
var=[U,I,R]

plt.figure()
ocd.plot_var(I,U,var,messung,True)
plt.show()

