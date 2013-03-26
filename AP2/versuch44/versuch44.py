# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
import ocd

messung251=ocd.open_csv("messung251.csv")
messung252=ocd.open_csv("messung252.csv")
messung253=ocd.open_csv("messung253.csv")
messung254=ocd.open_csv("messung254.csv")
U=sy.Symbol("U")
I=sy.Symbol("I")
R=sy.Symbol("R")
var=[U,I,R]

def plot253():
	plt.figure()
	(a,b,Sa,Sb,Sy)=ocd.plot_var(I,U,var,messung232,True)
	plt.xlabel("I in A")
	plt.ylabel("U in V")
	plt.title(ur"Spannungsstabilisiertes Netzgerät")
	print "a:",a,"+-",Sa
	print "b:",b,"+-",Sb
	plt.xlim(0,1.4)
	plt.show()
def plot252():
	plt.figure()
	(a,b,Sa,Sb,Sy)=ocd.plot_var(I,U,var,messung252,True)
	plt.xlabel("I in A")
	plt.ylabel("U in V")
	plt.title(ur"Bleiakku")
	print "a:",a,"+-",Sa
	print "b:",b,"+-",Sb
	plt.show()
def plot251():
	plt.figure()
	(a,b,Sa,Sb,Sy)=ocd.plot_var(I,U,var,messung251,True)
	plt.xlabel("I in A")
	plt.ylabel("U in V")
	plt.title(ur"Netzgerät mit mittlerem Innenwiderstand")
	print "a:",a,"+-",Sa
	print "b:",b,"+-",Sb
	plt.show()

def plot251_leistung():
	plt.figure()
	p=ocd.plot_var(I,U*I,var,messung251,True,2)
        print p	
	plt.xlabel("I in A")
	plt.ylabel("P in W")
	plt.title(ur"Leistungsanpassung")
	plt.show()

def plot254():
	plt.figure()
	(a,b,Sa,Sb,Sy)=ocd.plot_var(U,I,var,messung254,True)
	plt.xlabel("U in V")
	plt.ylabel("I in A")
	plt.title(ur"Stromstabilisiertes Netzgerät")
	print "a:",a,"+-",Sa
	print "b:",b,"+-",Sb

	plt.show()

plot254()
