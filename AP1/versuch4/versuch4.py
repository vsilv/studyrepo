# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
h=22.61
d=15.13
m=5.70
Sx=1.0
Sm=0.03
Sd=Sh=0.05
r_m=m/(np.pi*(d/2)**2*h)
v=(np.pi*(d/2)**2*h)
Sr_m=r_m*np.sqrt((Sm/m)**2+v**2*((2*Sd/d)**2+(Sh/h)**2))
def calc(x0,x1,x2):
	beta=(x1-x2)/(x1-x0)
	r_f=r_m*beta
	Sbeta2=((x1-x2)**2+(x0-x2)**2+(x0-x1)**2)*Sx**2/(x0-x1)**4
	S_r_f=r_f*np.sqrt((Sm/m)**2+(Sh/h)**2+(2*Sd/d)**2+(Sbeta2/beta**2))
	print "Dichte der Flüssigkeit:",1000*r_f.mean(),"+-",1000*r_f.std()
	print "Unsicherheit vs Std:",1000*S_r_f,1000*r_f.std()
def calc2(x2,x1,x0):
	beta=(x1-x2)/(x1-x0)
	r_m_=0.998*beta
	r_f=0.998
	Sr_f=0.001
	Sbeta2=((x1-x2)**2+(x0-x2)**2+(x0-x1)**2)*Sx**2/(x0-x1)**4
	Sr_m_=r_f*np.sqrt((Sr_f/r_f)**2+(Sbeta2/beta**2))
	print "Dichte der Masse:",r_m_.mean(),"+-",Sr_m_
	print "theoretische Masse:",r_m*1000,"+-",1000*Sr_m
	print "Unsicherheit vs Std:",Sr_m_,r_m_.std()
# Zylindermessung mit Wasser
x0=np.array([415,443,402,434,469],dtype=np.float)
x1=np.array([394,424,382,414,449],dtype=np.float)
x2=np.array([409,438,396,428,463],dtype=np.float)
calc(x0,x1,x2)
calc2(x0,x1,x2)
# Zylindermessung mit unbekannter Flüssigkeit
x0=np.array([468,456,435,416,397],dtype=np.float)
x1=np.array([448,436,415,396,377],dtype=np.float)
x2=np.array([459,447,426,407,389],dtype=np.float)
calc(x0,x1,x2)
#Steighöhe in den Kapillaren
def sigma(d,h,r_f,g):
	Sd=0.1
	Sh=0.25
	Sr_f=0.086
	Sg=0.01
	sigma_=d*h*r_f*g/4
	Ssigma_=sigma_*np.sqrt((Sr_f/r_f)**2+(Sd/d)**2+(Sh/h)**2+(Sg/g)**2)
	print "sigma:",sigma_/1000 ,"+-=",Ssigma_/1000
	print "Abweichung:",0.66/sigma_*100,"%"
sigma(1.51,13.96,0.9958,9.81)
sigma(0.40,34.09,0.9958,9.81)
sigma(0.80,29.17,0.9958,9.81)
# Messung der Oberflächenspannung
s_wasser= 3.4/(2*25.61)
Ss_wasser=s_wasser*np.sqrt((0.1/3.4)**2+(0.05/25.61)**2)
print "Oberflächenspannung Wasser:",s_wasser,"+-",Ss_wasser
s_ethanol= 1.15/(2*25.61)
Ss_ethanol=s_ethanol*np.sqrt((0.1/1.15)**2+(0.05/25.61)**2)
print "Oberflächenspannung Ethanol:",s_ethanol,"+-",Ss_ethanol

plt.figure()
Ss=0.10
SF=0.15
s=np.array([2.00,2.50,3.00,3.50,4.00,4.25,4.50,4.75,5.00,5.25])
F=np.array([0.25,0.70,1.50,2.15,2.70,2.95,3.10,3.25,3.35,3.40])
plt.errorbar(s,F, yerr=SF,xerr=Ss,fmt='.')
s=np.array([3.00,3.50,4.00,4.50,4.75,5.00,5.15])
F=np.array([1.55,2.20,2.70,3.10,3.30,3.35,3.38])
plt.errorbar(s,F, yerr=SF,xerr=Ss,fmt='.')
s=np.array([3.00,3.50,4.00,4.25,4.50,4.60,4.70,4.80,4.90,5.00,5.10])
F=np.array([1.50,2.20,2.75,3.00,3.20,3.20,3.25,3.30,3.35,3.36,3.40])
plt.errorbar(s,F, yerr=SF,xerr=Ss,fmt='.')
plt.xlabel("s in mm")
plt.ylabel("F in mN")
plt.plot([0,6],[3.4,3.4])
plt.title(ur"Messung der Oberflächenspannung von Wasser")
plt.grid(True)
plt.show()
plt.figure()
plt.title(ur"Messung der Oberflächenspannung von Ethanol")
s=np.array([0.00,0.50,1.00,1.50,2.00,2.50,2.75,3.00])
F=np.array([-0.6,-0.45,-0.1,0.3,0.65,0.90,1.05,1.10])
plt.errorbar(s,F, yerr=SF,xerr=Ss,fmt='.')
s=np.array([1.00,1.50,2.00,2.50,2.60,2.70,2.80,2.90,3.00])
F=np.array([-0.05,0.30,0.70,0.90,0.95,1.00,1.05,1.05,1.15])
plt.errorbar(s,F, yerr=SF,xerr=Ss,fmt='.')
s=np.array([1.00,1.50,2.00,2.50,2.60,2.70,2.80,2.90,3.00])
F=np.array([-0.05,0.3,0.65,0.95,1.00,1.05,1.05,1.10,1.15])
plt.errorbar(s,F, yerr=SF,xerr=Ss,fmt='.')
plt.xlabel("s in mm")
plt.ylabel("F in mN")
plt.plot([0,3.5],[1.15,1.15])
plt.grid(True)
plt.show()

