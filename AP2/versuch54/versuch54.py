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
<<<<<<< HEAD
=======
        
plot_sekundaer()



>>>>>>> b9dee791187f2e45caf5604496a8606185957703
################## Kennlinien
R = sy.Symbol("R")
Ieff1 = sy.Symbol("Ieff1")
Ieff2 = sy.Symbol("Ieff2")
Ueff1 = sy.Symbol("Ueff1")
Ueff2 = sy.Symbol("Ueff2")
<<<<<<< HEAD
w_=ocd.Groesse("w","rad/s",np.array([2*np.pi*50]),np.array([1]))
w=sy.Symbol("w")
L_=ocd.Groesse("L","H",np.array([1.37]),np.array([0.03]))
L = sy.Symbol("L")
Rfe_=ocd.Groesse("Rfe","ohm",np.array([640]),np.array([30]))
Rfe = sy.Symbol("Rfe")
Cs_ = ocd.Groesse("Cs","F",np.array([89.3E-6]),np.array([0]))
C_ = ocd.Groesse("C","F",np.array([156.7E-6]),np.array([0]))
Cs = sy.Symbol("Cs")
C = sy.Symbol("C")
Pw1 = sy.Symbol("P")
var = [R,  w ,Ieff1,Ieff2,Ueff1,Ueff2,Pw1,L,Rfe, C, Cs]
messung221=ocd.open_csv("221.csv")+[Rfe_,L_,w_]
messung222=ocd.open_csv("222.csv")+[Rfe_,L_,w_,C_,Cs_]
Ps1 = Ueff1 * Ieff1
Ps2 = Ueff2 * Ieff2
Pw2 = Ps2
eta = Pw2 / Pw1
phi1 = sy.acos(Pw1/Ps1)
ue=-256./200
Rs=ue**2*R
phi1_theo=sy.atan(Rfe*Rs/(w*L*(Rs+Rfe)))
phi1_theo_capa=sy.atan(Rfe/(w*L)*((L/Cs - (Rs**2 + 1. / (w**2*Cs**2)))/(Rfe*Rs+(Rs**2+1./(w**2*Cs**2)))))
phi2_theo= sy.atan(1./(R*w*C))
def plot1a():
        fig=plt.figure(figsize=(16,12))
        t1=ocd.plot_var(Ieff2,Ueff2/Ueff1,var,messung221,True)
        (a,b,Sa,Sb,Sy)=t1
        textstr=ur"$a= (%.3f\pm %.3f)V$    $b= (%.3f\pm %.3f)\frac{V}{A}$"%(a,Sa,b,Sb)
        print textstr
        props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)

        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_{eff2}$ in A",fontsize=16)
        plt.ylabel(ur"$\frac{Ueff2}{Ueff1}$",fontsize=16)
        plt.title(ur"Spannungsverhältnis" )
        plt.text(0.05, 0.95, textstr,  fontsize=14, verticalalignment="top", bbox=props)
        plt.grid(True)
        plt.show()
def plot1a_kleine_stroeme():
        fig=plt.figure(figsize=(16,12))
        t1=ocd.plot_var(Ieff2,Ueff2/Ueff1,var,messung221,True,choices = np.arange(7,21,1))
        (a,b,Sa,Sb,Sy)=t1

        textstr=ur"$a= (%.3f\pm %.3f)V$    $b= (%.3f\pm %.3f)\frac{V}{A}$"%(a,Sa,b,Sb)
        print textstr
        props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)

        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_{eff2}$ in A",fontsize=16)
        plt.ylabel(ur"$\frac{Ueff2}{Ueff1}$",fontsize=16)
        plt.title(ur"Spannungsverhältnis" )
        plt.text(0.05, 0.95, textstr,  fontsize=14, verticalalignment="top", bbox=props)
=======
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
>>>>>>> b9dee791187f2e45caf5604496a8606185957703
        plt.grid(True)
        plt.show()
def plot1b():
        fig=plt.figure(figsize=(16,12))
<<<<<<< HEAD
        t1=ocd.plot_var(Ieff2,Pw1,var,messung221,True)
        t1=ocd.plot_var(Ieff2,Pw2,var,messung221,True,2)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_{eff2}$ in A",fontsize=16)
        plt.ylabel(ur"P in W",fontsize=16)
        plt.title(ur"Primär und Sekundärsleistung")
        plt.grid(True)
        plt.show()

def plot1c():
        fig=plt.figure(figsize=(16,12))
        t1=ocd.plot_var(Ieff2,eta,var,messung221,False)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_{eff2}$ in A",fontsize=16)
        plt.ylabel(ur"$\eta$",fontsize=16)
        plt.title("Wirkungsgrad")
        plt.grid(True)
        plt.show()

def plot1d():
        fig=plt.figure(figsize=(16,12))
        t1=ocd.plot_var(Ieff2,-phi1,var,messung221,False)
        t1=ocd.plot_var(Ieff2,-phi1_theo,var,messung221,False)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_{eff2}$ in A",fontsize=16)
        plt.ylabel(ur"$\phi$",fontsize=16)
        plt.title("Phasenverschiebung")
        plt.grid(True)
        plt.show()
plot1d()

##################### 222
=======
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
>>>>>>> b9dee791187f2e45caf5604496a8606185957703
def plot2a():
        fig=plt.figure(figsize=(16,12))
        t1=ocd.plot_var(Ieff2,Ueff2/Ueff1,var,messung222,False)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
<<<<<<< HEAD
        plt.xlabel(ur"$I_{eff2}$ in $A$")
=======
        plt.xlabel(ur"$I_eff2$")
>>>>>>> b9dee791187f2e45caf5604496a8606185957703
        plt.ylabel(ur"$\frac{Ueff2}{Ueff1}$")
        plt.title(ur"Messung 222: Spannungsverhältnis $\frac{Ueff2}{Ueff1}$")
        plt.grid(True)
        plt.show()
def plot2b():
        fig=plt.figure(figsize=(16,12))
<<<<<<< HEAD
        t1=ocd.plot_var(Ieff2,Pw2,var,messung222,False)
        t1=ocd.plot_var(Ieff2,Pw1,var,messung222,False)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_{eff2}$ in $A$")
        plt.ylabel(ur"$P_{s,1}$ in $W$")
        plt.title(ur"Messung 222: Sekundärsleistung")
=======
        P2= Ueff2*Ieff2
        t1=ocd.plot_var(Ieff2,P2,var,messung222,False)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_eff2$")
        plt.ylabel(ur"$P_{s,1}$")
        plt.title("Messung 222: Sekundärsleistung")
>>>>>>> b9dee791187f2e45caf5604496a8606185957703
        plt.grid(True)
        plt.show()
def plot2c():
        fig=plt.figure(figsize=(16,12))
<<<<<<< HEAD
        t1=ocd.plot_var(Ieff2,-phi1,var,messung222,False,choices=np.arange(-1,-8,-1))
        t1=ocd.plot_var(Ieff2,phi1,var,messung222,False,choices=np.arange(0,17,1))
        t1=ocd.plot_var(Ieff2,phi1_theo_capa,var,messung222,False)
        t1=ocd.plot_var(Ieff2,phi2_theo,var,messung222,False)
        #plt.xscale("log",nonpox="clip")
        #plt.yscale("log",nonpox="clip")
        plt.xlabel(ur"$I_{eff2}$ in A",fontsize=16)
        plt.ylabel(ur"$\phi$ in radianten",fontsize=16)
        plt.title("Phasenverschiebung")
        plt.grid(True)
        plt.show()


=======
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
>>>>>>> b9dee791187f2e45caf5604496a8606185957703
