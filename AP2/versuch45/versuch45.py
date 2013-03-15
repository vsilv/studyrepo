# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
import ocd

messung21=ocd.open_csv("messung21.csv")
U=sy.Symbol("U")
I=sy.Symbol("I")
var=[U,I]

def plot21():
	plt.figure()
	(a,b,Sa,Sb,Sy)=ocd.plot_var(I,U,var,messung21,True)
	plt.xlabel("I in A")
	plt.ylabel("U in V")
	plt.title(ur"Ohmscher Widerstand")
	print "a:",a,"+-",Sa
	print "b:",b,"+-",Sb
	plt.xlim(0,1.4)
	plt.show()

