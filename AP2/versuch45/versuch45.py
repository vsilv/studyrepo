# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
import ocd

messung21=ocd.open_csv("messung21.csv")
messung22=ocd.open_csv("messung22.csv")
messung231=ocd.open_csv("messung231.csv")
messung2321=ocd.open_csv("messung2321.csv")
messung2322=ocd.open_csv("messung2322.csv")
U=sy.Symbol("U")
I=sy.Symbol("I")
var=[U,I]

def plot21():
	plt.figure()
	(a,b,Sa,Sb,Sy)=ocd.plot_var(I,U,var,messung21,True)
	ocd.plot_var(I,U,var,messung22)
	plt.xlabel("I in A")
	plt.ylabel("U in V")
	plt.title(ur"Ohmscher Widerstand und Glühbirne")
	print "a:",a,"+-",Sa
	print "b:",b,"+-",Sb
	plt.xlim(0,0.3)
	plt.ylim(0,2.1)
	plt.show()
def plot231a():
	plt.figure()
	ocd.plot_var(I,U,var,messung231)
	plt.xlabel("I in A")
	plt.ylabel("U in V")
	plt.title(ur"Diode")
	plt.show()
def plot231b():
	plt.figure()
	ax=ocd.plot_var(I,U,var,messung231)
	ax.set_xscale("log", nonposx='clip')
	plt.xlabel("I in A")
	plt.ylabel("U in V")
	plt.title(ur"Diode")
	plt.show()
def plot2321():
	plt.figure()
	ax=ocd.plot_var(I,U,var,messung2321,True)
	ax=ocd.plot_var(I,U,var,messung2322)
	plt.xlabel("I in A")
	plt.ylabel("U in V")
	plt.title("Diode in Sperrrichtung mit Schaltung 1")
	plt.show()
####transistor
messung241=ocd.open_csv("messung241.csv")
messung243=ocd.open_csv("messung243.csv")
IC=sy.Symbol("IC")
IB=sy.Symbol("IB")
UBE=sy.Symbol("UBE")
UCE=sy.Symbol("UCE")
var=[IC,IB,UBE,UCE]
def plot241a():
	plt.figure()
	ax=ocd.plot_var(UBE,IB,var,messung241)
	plt.ylabel("IB in A")
	plt.xlabel("UBE in V")
	plt.title("Transistor")
	plt.show()
def plot241b():
	plt.figure()
	ax=ocd.plot_var(UBE,IC,var,messung241)
	plt.ylabel("IC in A")
	plt.xlabel("UBE in V")
	plt.title("Transistor")
	plt.show()
def plot243():
	plt.figure()
	ax=ocd.plot_var(UCE,IC,var,messung243)
	plt.ylabel("IC in A")
	plt.xlabel("UCE in V")
	plt.title("Transistor")
	plt.show()
plot243()
