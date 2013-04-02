# -*- coding: utf-8 -*-
import sympy as sy
import ocd
import matplotlib.pyplot as plt
import numpy as np


############ Daten der Spulenwicklungen ##############
messung211=ocd.open_csv("211.csv")
U1 = sy.Symbol("U1")
U2 = sy.Symbol("U2")
I1 = sy.Symbol("I1")
I2 = sy.Symbol("I2")
var=[U1,U2,I1,I2]
def plot_primaer():
        fig=plt.figure(figsize=(16,12))
        t=ocd.plot_var(I1,U1,var,messung211,True)
        (a,b,Sa,Sb,Sy)=t
        textstr=ur"$a= (%.3f\pm %.3f)V$    $b= (%.3f\pm %.3f)\frac{V}{A}$"%(a,Sa,b,Sb)
        plt.title(ur"Bestimmung des ohmschen Widerstandes der Primärspule",fontsize=16, family= "monospace")
        props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
        plt.text(0.05, 0.9, textstr,  fontsize=14, verticalalignment="top", bbox=props)
        plt.xlabel(ur"I in A")
        plt.ylabel(ur"U in V")
        plt.grid(True)
        plt.show()
def plot_sekundaer():
        fig=plt.figure(figsize=(16,12))
        t=ocd.plot_var(I2,U2,var,messung211,True)
        (a,b,Sa,Sb,Sy)=t
        textstr=ur"$a= (%.3f\pm %.3f)V$    $b= (%.3f\pm %.3f)\frac{V}{A}$"%(a,Sa,b,Sb)
        plt.title(ur"Bestimmung des ohmschen Widerstandes der Sekundärspule",fontsize=16, family= "monospace")
        props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
        plt.text(0.05, 0.9, textstr,  fontsize=14, verticalalignment="top", bbox=props)
        plt.xlabel(ur"I in A")
        plt.ylabel(ur"U in V")
        plt.grid(True)
        plt.show()
        
plot_sekundaer()



################## Kennlinien
R = sy.Symbol("R")
Ieff1 = sy.Symbol("Ieff1")
Ieff2 = sy.Symbol("Ieff2")
Ueff1 = sy.Symbol("Ueff1")
Ueff2 = sy.Symbol("Ueff2")
P = sy.Symbol("P")
var = [R, Ieff1,Ieff2,Ueff1,Ueff2,P]
messung221=ocd.open_csv("221.csv")
def plot1a():
        fig=plt.figure(figsize=(16,12))
        t1=ocd.plot_var(Ieff2,Ueff2/Ueff1,var,messung221,True)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_eff2$")
        plt.ylabel(ur"$\frac{Ueff2}{Ueff1}$")
        plt.title(ur"Spannungsverhältnis $\frac{Ueff2}{Ueff1}$")
        plt.grid(True)
        plt.show()
def plot1b():
        fig=plt.figure(figsize=(16,12))
        P2= Ueff2*Ieff2
        t1=ocd.plot_var(Ieff2,P2,var,messung221,False)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_eff2$")
        plt.ylabel(ur"$P_{s,1}$")
        plt.title("Sekundärsleistung")
        plt.grid(True)
        plt.show()
def plot1c():
        fig=plt.figure(figsize=(16,12))
        P2= Ueff2*Ieff2
        eta= P2 / P
        t1=ocd.plot_var(Ieff2,eta,var,messung221,False)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_eff2$")
        plt.ylabel(ur"$\eta$")
        plt.title("Wirkungsgrad")
        plt.grid(True)
        plt.show()
def plot1c():
        fig=plt.figure(figsize=(16,12))
        P2= Ueff2*Ieff2
        t1=ocd.plot_var(Ieff2,P,var,messung221,True)
        t1=ocd.plot_var(Ieff2,P2,var,messung221,True,2)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_eff2$")
        plt.ylabel(ur"$P$")
        plt.title("Vergleich der von $P1$ mit $P2$")
        plt.grid(True)
        plt.show()
##################### 222
messung222=ocd.open_csv("222.csv")
def plot2a():
        fig=plt.figure(figsize=(16,12))
        t1=ocd.plot_var(Ieff2,Ueff2/Ueff1,var,messung222,False)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_eff2$")
        plt.ylabel(ur"$\frac{Ueff2}{Ueff1}$")
        plt.title(ur"Messung 222: Spannungsverhältnis $\frac{Ueff2}{Ueff1}$")
        plt.grid(True)
        plt.show()
def plot2b():
        fig=plt.figure(figsize=(16,12))
        P2= Ueff2*Ieff2
        t1=ocd.plot_var(Ieff2,P2,var,messung222,False)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_eff2$")
        plt.ylabel(ur"$P_{s,1}$")
        plt.title("Messung 222: Sekundärsleistung")
        plt.grid(True)
        plt.show()
def plot2c():
        fig=plt.figure(figsize=(16,12))
        P2= Ueff2*Ieff2
        eta= P2 / P
        t1=ocd.plot_var(Ieff2,eta,var,messung222,False)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_eff2$")
        plt.ylabel(ur"$\eta$")
        plt.title("Messung 222: Wirkungsgrad")
        plt.grid(True)
        plt.show()
def plot2d():
        fig=plt.figure(figsize=(16,12))
        P2= Ueff2*Ieff2
        t1=ocd.plot_var(Ieff2,P,var,messung222,False)
        t1=ocd.plot_var(Ieff2,P2,var,messung222,False)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_eff2$")
        plt.ylabel(ur"$P$")
        plt.title("Messung 222: Vergleich der von $P1$ mit $P2$")
        plt.grid(True)
        plt.show()
