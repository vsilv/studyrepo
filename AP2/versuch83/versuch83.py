# -*- coding: utf-8 -*-
import sympy as sy
import ocd
import matplotlib.pyplot as plt
import numpy as np


############ Daten der Spulenwicklungen ##############
messung21=ocd.open_csv("21.csv")
messung21[2].Sx+=np.std(messung21[2].x[2:])
messung22=ocd.open_csv("22.csv")
Uz = sy.Symbol("Uz")
UA = sy.Symbol("UA")
N  = sy.Symbol("N")
alpha = sy.Symbol("alpha")
var=[Uz,UA,N,alpha]
def plot21():
        fig=plt.figure(figsize=(16,12))
        t=ocd.plot_var(Uz,N,var,messung21,False)
        #(a,b,Sa,Sb,Sy)=t
        #textstr=ur"$a= (%.3f\pm %.3f)V$    $b= (%.3f\pm %.3f)\frac{V}{A}$"%(a,Sa,b,Sb)
        #plt.title(ur"Bestimmung des ohmschen Widerstandes der Primärspule",fontsize=16, family= "monospace")
        #props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
        #plt.text(0.05, 0.9, textstr,  fontsize=14, verticalalignment="top", bbox=props)
        plt.xlabel(ur"Uz in V")
        plt.ylabel(ur"N") 
	plt.title(ur"Messung 2.1 Zählrohrcharakteristik")
        plt.grid(True)
        plt.show()
def plot22():
	fig=plt.figure(figsize=(16,12))
        t=ocd.plot_var(sy.sin(alpha),N,var,messung22,False)
        #(a,b,Sa,Sb,Sy)=t
        #textstr=ur"$a= (%.3f\pm %.3f)V$    $b= (%.3f\pm %.3f)\frac{V}{A}$"%(a,Sa,b,Sb)
        #plt.title(ur"Bestimmung des ohmschen Widerstandes der Primärspule",fontsize=16, family= "monospace")
        #props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
        #plt.text(0.05, 0.9, textstr,  fontsize=14, verticalalignment="top", bbox=props)
        plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$sin(\alpha)$")
        plt.ylabel(ur"N")
	plt.title(ur"Messung 2.2 Röntgenemissionsspektrum")
        plt.grid(True)
        plt.show()
def bremsstrahlung():
	fig=plt.figure(figsize=(16,12))
        t=ocd.plot_var(sy.sin(alpha),N,var,messung22,False)
        #(a,b,Sa,Sb,Sy)=t
        #textstr=ur"$a= (%.3f\pm %.3f)V$    $b= (%.3f\pm %.3f)\frac{V}{A}$"%(a,Sa,b,Sb)
        #plt.title(ur"Bestimmung des ohmschen Widerstandes der Primärspule",fontsize=16, family= "monospace")
        #props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
        #plt.text(0.05, 0.9, textstr,  fontsize=14, verticalalignment="top", bbox=props)
        plt.xlabel(ur"$sin(\alpha)$")
        plt.ylabel(ur"N")
	plt.title(ur"Messung 2.2 Röntgenemissionsspektrum")
        plt.grid(True)
        plt.show()

bremsstrahlung()
