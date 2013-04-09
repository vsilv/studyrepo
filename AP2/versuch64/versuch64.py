# -*- coding: utf-8 -*-
import ocd
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

messung211=ocd.open_csv("211.csv")
messung212=ocd.open_csv("212.csv")
f = sy.Symbol("f")
Ue = sy.Symbol("Ue")
Ua = sy.Symbol("Ua")
var=[f,Ue,Ua]
f_=np.linspace(0,120000,1000)
def plot_ver():
	fig=plt.figure(figsize=(16,12))
	ocd.plot_var(f,Ua/Ue,var,messung212)
	t=ocd.plot_var(f,Ua/Ue,var,messung211,True)
        (a,b,Sa,Sb,Sy)=t
        textstr=ur"$a= (%.3f\pm %.3f)V$    $b= (%.3f\pm %.3f)\frac{V}{A}$"%(a,Sa,b,Sb)
        props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
        plt.text(0.05, 0.9, textstr,  fontsize=14, verticalalignment="top", bbox=props)

	plt.ylim(0,100)
	plt.xlabel("f in Hz")
	plt.ylabel(ur"Linearer Verstärker")
	plt.show()
##### Frequenzabhängiger Verstärker #####
messung213=ocd.open_csv("213.csv")
R1 = 4700
R2 = 470000
R3 = 47000
C2 = 2.2E-9
f_ = 10**np.linspace(0,6,1000)
w = 2 * np.pi * f_
v1 = 1. / (R1 * np.sqrt(C2**2.*w**2+1./R2**2))
v2 = 1. / (R1 * np.sqrt((R3/(R2**2+1./(w**2*C2**2))+1./R2)**2+1./(w**2*C2**2*(R3**2+1./(w**2*C2**2))**2)) )
def plot_ver2():
	fig=plt.figure(figsize=(16,12))
	ocd.plot_var(f,Ua/Ue,var,messung213)
	#ocd.plot_var(f,v1,var,messung213)
	#ocd.plot_var(f,v2,var,messung213)
        plt.plot(f_,v1)
        plt.plot(f_,v2)
        plt.xscale("log",nonpox="clip")
        plt.yscale("log",nonpox="clip")
        plt.grid(True)
	plt.xlabel("f in Hz")
	plt.ylabel(ur"Frequenzabhängiger Verstärker")
	plt.show()

### 2.3. Spannungsfolger
### 231 Linearer Verlauf
messung231=ocd.open_csv("231.csv")
Ue = sy.Symbol("Ue")
Ua = sy.Symbol("Ua")
var = [Ue,Ua]
def plot_Ue_Ua():
        fig=plt.figure(figsize=(16,12))
        t=ocd.plot_var(Ue,Ua,var,messung231,True,choices=range(10,16)+range(3,8))
        ocd.plot_var(Ue,Ua,var,messung231,False)
        (a,b,Sa,Sb,Sy)=t
        textstr=ur"$a= (%.3f\pm %.3f)V$    $b= (%.3f\pm %.3f)\frac{V}{A}$"%(a,Sa,b,Sb)
        props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
        plt.text(0.05, 0.9, textstr,  fontsize=14, verticalalignment="top", bbox=props)


        plt.grid(True)
        plt.xlabel("Ue in V")
        plt.ylabel(ur"Ua in V")
        plt.show()
### Sättigungsverhalten
### Messung 232
messung232a=ocd.open_csv("232a.csv")
messung232b=ocd.open_csv("232b.csv")
Ia = sy.Symbol("Ia")
var += [Ia]
def plot_Ue_Ua_R():
        fig=plt.figure(figsize=(16,12))
        ocd.plot_var(Ue,Ua,var,messung232a,choices=range(4))
        ocd.plot_var(Ue,Ua,var,messung232a,choices=range(4,8))
        ocd.plot_var(Ue,Ua,var,messung232a,choices=range(8,12))
        plt.grid(True)
        plt.xlabel("Ue in V")
        plt.ylabel(ur"Ua in V")
        plt.title(ur"Sättigungsverhalten bei 100 Ohm Ausgangswiderstand")
        plt.show()
def plot_Ue_Ua():
        fig=plt.figure(figsize=(16,12))
        ocd.plot_var(Ue,Ua,var,messung232b,choices=range(4))
        ocd.plot_var(Ue,Ua,var,messung232b,choices=range(4,8))
        ocd.plot_var(Ue,Ua,var,messung232b,choices=range(8,12))
        plt.grid(True)
        plt.xlabel("Ue in V")
        plt.ylabel(ur"Ua in V")
        plt.title(ur"Sättigungsverhalten ohne Ausgangswiderstand")
        plt.show()

def plot_Ia_Ua():
        fig=plt.figure(figsize=(16,12))
        t=ocd.plot_var(Ia,Ua,var,messung232a,True,choices=[2,5,9])

        t2=ocd.plot_var(Ia,Ua,var,messung232b,True,choices=[0,4,11])

        (a,b,Sa,Sb,Sy)=t
        textstr=ur"$a= (%.3f\pm %.3f)V$    $b= (%.1f\pm %.1f)\frac{V}{A}$"%(a,Sa,b,Sb)
        props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
        plt.text(0.002, 12.2, textstr,  fontsize=14, verticalalignment="top", bbox=props)

        (a,b,Sa,Sb,Sy)=t2
        textstr=ur"$a= (%.3f\pm %.3f)V$    $b= (%.1f\pm %.1f)\frac{V}{A}$"%(a,Sa,b,Sb)
        props = dict(boxstyle="round", facecolor="wheat", alpha=0.5)
        plt.text(0.008, 13, textstr,  fontsize=14, verticalalignment="top", bbox=props)

 
        plt.grid(True)
        plt.xlabel("Ia in A")
        plt.title(ur"Sättigungsspannung in Abhängigkeit des Stromes")
        plt.ylabel(ur"Us in V")
        plt.show()
plot_Ia_Ua()
