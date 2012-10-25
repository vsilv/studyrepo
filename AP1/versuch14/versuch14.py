# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import mylib
x = np.array([29.3,29.0,28.8,28.5,28.25,28.0,27.75,27.5,27.375,27.25])
d = np.array([86.0,80.0,76.5,70.6,65.00,56.0,49.50,41.5,33.000,27.00])
Sd= np.array([0.6 ,1.0 ,0.6 ,1.0 ,2.0  ,1.0 ,1.5  ,2.0 ,2.5   ,2.5  ])
Sx = 0.01
x0 = 29.90
Sx0= 0.1
A  = 90.5
SA = 0.3
s  = 63.7/2
Ss = 0.2/2
r=0.00435/2
#Auswertung
b  = x0-x
Sb = np.sqrt(Sx0**2+Sx**2)

theta=(d-b)/s
Stheta=theta*np.sqrt((Sd**2+Sb**2)/(d-b)**2+(Ss/s)**2)

k = np.cos(theta/2)
Sk= np.sin(theta/2)/2*Stheta

k=np.concatenate([k,-k])
Sk=np.concatenate([Sk,Sk])

theta=np.concatenate([theta,-theta])
Stheta=np.concatenate([Stheta,Stheta])

b=np.concatenate([b,-b])

(a,m,Sa,Sm,Sy)=mylib.gerade(k,b)
print "R=",m-r,"+-",Sm
print "max. fehler",m*np.sqrt((Sb/b)**2+(Sk/k)**2)

def plot1():
	plt.figure()
	plt.errorbar(k,b,xerr=Sk,yerr=Sb,fmt=".")
	plt.plot([k.min(),k.max()],[a+m*k.min(),a+m*k.max()])
	plt.ylabel(ur"Stoßparameter $b$ in $cm$",fontsize=20)
	plt.xlabel(ur"$\cos(\frac{\theta}{2})$",fontsize=20)
	plt.title(ur"Berechnung von $R$")
	plt.grid(True)
	plt.show()
def wirkungsquerschnitt():
	plt.figure()
	plt.errorbar(theta,b,Stheta,Sb,fmt=".")
	plt.show()
