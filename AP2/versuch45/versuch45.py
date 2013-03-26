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
	plt.figure(figsize=(16,12))
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
	plt.figure(figsize=(16,12))
	ocd.plot_var(I,U,var,messung231)
        plt.grid(True)
	plt.xlabel("I in A")
	plt.ylabel("U in V")
	plt.title(ur"Kennlinie der Diode")
	plt.show()
def plot231b():
	plt.figure(figsize=(16,12))
	ocd.plot_var(I,U,var,messung231)
	plt.xscale("log", nonposx='clip')
        plt.grid(True)
	plt.xlabel("I in A")
	plt.ylabel("U in V")
	plt.title(ur"Kennlinie der Diode (in logarithmischer Darstellung)")

def plot232():
	plt.figure(figsize=(16,12))
	ax=ocd.plot_var(I,U,var,messung2321,True)
	ax=ocd.plot_var(I,U,var,messung2322)
	plt.xlabel("I in A")
	plt.ylabel("U in V")
	plt.title("Diode in Sperrrichtung mit den beiden Schaltungen")
	plt.show()
def plot233a():
	plt.figure(figsize=(16,12))
	ocd.plot_deriv_var(I,U/1000,var,messung231)
	plt.xscale("log", nonposx='clip')
        plt.grid(True)
	plt.xlabel("I in A")
        plt.ylabel("R in kOhm")
	plt.title(ur"Kennlinie der Diode")
        plt.show()
def plot233b():
	plt.figure(figsize=(16,12))
	ocd.plot_deriv_var(I,U,var,messung22)
        plt.grid(True)
	plt.xlabel("I in A")
        plt.ylabel("R in Ohm")
	plt.title(ur"Ableitung der Kennlinie der Glühlampe")
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
	plt.figure(figsize=(16,12))
	ax=ocd.plot_var(UBE,IB,var,messung241)
	plt.ylabel("IB in A")
	plt.xlabel("UBE in V")
	plt.title("Transistor")
        plt.grid(True)
	plt.show()
def plot241b():
	plt.figure(figsize=(16,12))
	(a,b,Sa,Sb,Sy)=ocd.plot_var(IB,IC,var,messung241,True)
	plt.ylabel("IC in A")
	plt.xlabel("IB in A")
	plt.title("Transistor")
        print "a:",a,"+-",Sa
        print "b:",b,"+-",Sb

        plt.grid(True)
	plt.show()
def plot243a():
	plt.figure(figsize=(16,12))
	ocd.plot_var(UCE,IC,var,messung243,choices=range(0,21))
	ocd.plot_var(UCE,IC,var,messung243,choices=range(21,43))
	ocd.plot_var(UCE,IC,var,messung243,choices=range(43,58))
	plt.ylabel("IC in A")
	plt.xlabel("UCE in V")
	plt.title("Transistor")
        plt.grid(True)
	plt.show()
def plot244_eingangswiderstand():
	plt.figure(figsize=(16,12))
	ocd.plot_deriv_var(IB,UBE,var,messung241)
        plt.grid(True)
	plt.xlabel("IB in A")
        plt.ylabel("Eingangswiderstand R in Ohm")
	plt.title(ur"Differentieller Eingangswiderstand")
        plt.show()
def plot245_beta():
	plt.figure(figsize=(16,12))
	ocd.plot_deriv_var(IB,IC,var,messung241)
        plt.grid(True)
	plt.xlabel("IB in A")
        plt.ylabel(ur"$\beta$")
	plt.title(ur"Kleinsignal-Stromverstärkung $\beta$")
        plt.show()




plot241b()
