# -*- coding: utf-8 -*-
import ocd
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

messung21=ocd.open_csv("21.csv")
messung22=ocd.open_csv("22.csv")
messung23=ocd.open_csv("23.csv")

f = sy.Symbol("f")
Ua0 = sy.Symbol("Ua0")
Uc0 = sy.Symbol("Uc0")
dt = sy.Symbol("dt")
var=[f,Ua0,Uc0,dt]
##theorie
f_ = np.linspace(0,300E3,1000)
f0 = 149.5E3
w_ = 2*np.pi*f_
w = 2 * sy.pi * f
L = 953E-6
w0 = f0*2*np.pi
def get_a(v_max):
       R = L * w0 / v_max
       a = w_ / np.sqrt(L**2*(w0**2-w_**2)**2+w_**2*R**2)
       return a
def get_v(v_max):
       R = L * w0 / v_max
       v = w0**2 / np.sqrt((w_**2-w0**2)**2+w_**2*R**2/L**2)
       return v
def plot_all_b():
        fig=plt.figure(figsize=(16,12))
        plt.grid(True)
        R_ = 6*10**np.linspace(1,6,1000)

        v_ = L * w0 / R_
        f2 = np.sqrt(w0**2 - R_**2 / (2*L**2))/(2*np.pi)
        #plt.plot(f2,v_,"-")
        C_ = ocd.Groesse("C","F",np.array([1.18922759294E-9]),np.array([7.604340813225311e-12]))
        C = sy.Symbol("C")
        ocd.plot_var(f,C*w*Uc0/Ua0,var+[C],messung21+[C_])
        ocd.plot_var(f,C*w*Uc0/Ua0,var+[C],messung22+[C_])
        ocd.plot_var(f,C*w*Uc0/Ua0,var+[C],messung23+[C_])
        
        plt.title(ur"getriebener, gedämpfter Oszillator")
        plt.xlabel("Frequenz in Hz")
        plt.ylabel(ur"$I_{0}/U_{a0}$ in A/V")

        plt.plot(f_,get_a(14.39),"r--")
        plt.plot(f_,get_a(3.33),"r--")
        plt.plot(f_,get_a(6.57),"r--")

        plt.xlim(0,3.1E5)
        plt.show()
def plot_all_c():
        fig=plt.figure(figsize=(16,12))
        plt.grid(True)
        R_ = 6*10**np.linspace(1,6,1000)

        v_ = L * w0 / R_
        f2 = np.sqrt(w0**2 - R_**2 / (2*L**2))/(2*np.pi)
        plt.plot(f2,v_,"-")
        ocd.plot_var(f,Uc0/Ua0,var,messung21)
        ocd.plot_var(f,Uc0/Ua0,var,messung22)
        ocd.plot_var(f,Uc0/Ua0,var,messung23)
        plt.plot(f_,get_v(14.39),"r--")
        plt.plot(f_,get_v(3.33),"r--")
        plt.plot(f_,get_v(6.57),"r--")
        plt.title(ur"getriebener, gedämpfter Oszillator")
        plt.xlabel("Frequenz in Hz")
        plt.ylabel(ur"$U_{c0}/U_{a0}$")

        plt.xlim(0,3.1E5)
        plt.show()
plot_all_c()
def theo_delta(f_,v):
        w_ = 2 * np.pi *f_
        C = 1. / ( w0**2 * L ) 
        print C
        R_ = L * w0 / v
        delta = np.mod(np.arctan(w_ * R_ / (L *( ( 1. / ( L * C ) - w_**2 )) ) ),np.pi)
        return delta

def plot_dt():
        fig=plt.figure(figsize=(16,12))
        plt.grid(True)
        T = 1 / f
        phi = 2*sy.pi * dt / T 
        
        ocd.plot_var(f,phi,var,messung21)
        ocd.plot_var(f,phi,var,messung22)
        ocd.plot_var(f,phi,var,messung23)
        f_ = np.linspace(0,300000,1000)
        plt.plot(f_,theo_delta(f_,14.39))
        plt.plot(f_,theo_delta(f_,3.33))
        plt.plot(f_,theo_delta(f_,6.57))
         
        
        plt.ylim(0,np.pi)
        plt.xlim(-0.1E5,3.1E5)
        plt.title(ur"Phasenverschiebung des getriebenen, gedämpften Oszillators")
        plt.xlabel("Frequenz in Hz")
        plt.ylabel("Phasenverschiebung in Radianten")

        plt.show()


v_ = ocd.Groesse("v","dimensionless",np.array([3.33]),np.array([0.3]))
w0_ = ocd.Groesse("w0","Hz",np.array([939E3]),np.array([3E3]))
L_ = ocd.Groesse("L","H",np.array([953E-6]),np.array([0]))
v = sy.Symbol("v")
w0 = sy.Symbol("w0")
L = sy.Symbol("L")
(R_, expr, Sexpr)=ocd.eval_expr(L*w0/v,[v,w0,L],[v_,w0_,L_],"R")
print "R=",R_
R = sy.Symbol("R")
var = [R,L,w0]
werte = [R_,L_,w0_]
(f_, expr, Sexpr) = ocd.eval_expr(sy.sqrt(w0**2-R**2/(4*L**2))/(2*sy.pi),var,werte,"f")
print f_
sy.pprint(Sexpr)
