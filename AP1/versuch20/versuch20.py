# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import mylib
#bestimmung der Eigenfrequenz
ST=0.01
t=np.array([17.88,17.83,17.83,17.85,17.80,17.82])/10
print "Periodendauer:",t.mean(),"+-",t.std()/np.sqrt(len(t))
w0=2*np.pi/t.mean()
Sw0=2*np.pi*t.std()/t.mean()**2
print "w0",w0,"+-",Sw0,"Rad/s"
def nsort(x,y):
	order=np.argsort(x)
	z=[]
	for p in order:
		z+=[y[p]]
	return z
#Drehzahlkennlinie
U=np.array([4,8,12,16,20,22])
T=np.array([9.46,4.61,3.03,2.23,1.78,1.60])/2
(a,b,Sa,Sb,Sy)=mylib.gerade(U,2*np.pi/T)
w=lambda U_:a+b*U_
w_sup=lambda U_:Sa+a+(Sb+b)*U_
w_inf=lambda U_:-Sa +a+(b-Sb)*U_
SU=0.05
Sw=lambda U_:np.sqrt(Sa**2+(b*U_)**2*((Sb/b)**2+(SU/U_)**2))
def Drehzahlkennlinie():
	plt.figure()
	plt.errorbar(U,np.pi*2/T,xerr=SU,yerr=ST,fmt=".")
	plt.xlabel("Motorspannung U in V")
	plt.ylabel("Erregerfrequenz w in Radianten/s")
	plt.title("Drehzahlkennlinie des Motors")
	plt.plot([U.min(),U.max()],[w(U.min()),w(U.max())])
	plt.plot([U.min(),U.max()],[w_sup(U.min()),w_sup(U.max())],"r--")
	plt.plot([U.min(),U.max()],[w_inf(U.min()),w_inf(U.max())],"r--")
	plt.grid()
	plt.show()
#Drehzahlkennlinie()
#Resonanzkurven
SA=0.2
SI=0.016
U=np.array([4,8,10,12,14,16,17,9,9.5,10.0,10.5,11.0,11.5,10.1,10.2,9.9,9.95])
#I=0.305
A1=np.array([0.6,1.0,5.25,1.1,0.42,0.25,0.2,2.0,3.0,5.2,3.2,2.1,1.4,5.3,4.8,5.6,5.6])
t1=np.array([0,0.04,0.44,0.66,0.56,0.47,0.44,0.08,0.12,0.42,0.64,0.67,0.67,0.5,0.55,0.37,0.39])
#I=0.498
A2=np.array([0.6,1.0,2.5,0.95,0.45,0.25,0.2,1.6,2.0,2.45,2.20,1.6,1.2,2.4,2.4,2.4,2.5])
t2=np.array([0,0.07,0.33,0.59,0.53,0.45,0.42,0.17,0.24,0.37,0.51,0.57,0.60,0.42,0.43,0.36,0.36])
#I=0.798
A3=np.array([0.6,0.8,1.1,0.75,0.4,0.25,0.2,1.0,1.2,1.0,1.0,0.8,0.7,1.0,1.0,1.0,1.0])
t3=np.array([0,0.19,0.37,0.48,0.46,0.41,0.38,0.28,0.33,0.38,0.43,0.46,0.48,0.39,0.40,0.37,0.38])
def plotresonanz():
	plt.figure()
	plt.errorbar(w(U),A1,xerr=Sw(U),yerr=SA,fmt='.')
	plt.errorbar(w(U),A2,xerr=Sw(U),yerr=SA,fmt='.')
	plt.errorbar(w(U),A3,xerr=Sw(U),yerr=SA,fmt='.')
	plt.plot(np.sort(w(U)),nsort(w(U),A1))
	plt.plot(np.sort(w(U)),nsort(w(U),A2))
	plt.plot(np.sort(w(U)),nsort(w(U),A3))
	plt.xlabel("Erregerfrequenz w in Radianten/s")
	plt.ylabel(ur"Amplitude (willkürliche Einheiten)")
	plt.title("Resonanzkurven")
	plt.grid(True)
	plt.show()
def plot_dt():
	plt.figure()

	d1=t1*w(U)
	Sd1=d1*np.sqrt((Sw(U)/w(U))**2+(ST/t1)**2)
	d2=t2*w(U)
	Sd2=d2*np.sqrt((Sw(U)/w(U))**2+(ST/t2)**2)
	d3=t3*w(U)
	Sd3=d3*np.sqrt((Sw(U)/w(U))**2+(ST/t3)**2)

	plt.errorbar(w(U),d1,xerr=Sw(U),yerr=Sd1,fmt='.')
	plt.errorbar(w(U),d2,xerr=Sw(U),yerr=Sd2,fmt='.')
	plt.errorbar(w(U),d3,xerr=Sw(U),yerr=Sd3,fmt='.')

	plt.plot(np.sort(w(U)),nsort(w(U),d1))
	plt.plot(np.sort(w(U)),nsort(w(U),d2))
	plt.plot(np.sort(w(U)),nsort(w(U),d3))
		
	plt.xlabel("Erregerfrequenz w in Radianten/s")
	plt.ylabel(ur"Phasenverschiebung")
	plt.title("Phasenverschiebung")
	plt.grid(True)
	plt.show()
def plot_dt2():
	plt.figure()

	d1=t1
	Sd1=ST
	d2=t2
	Sd2=ST
	d3=t3
	Sd3=ST



	plt.errorbar(w(U),d1,xerr=Sw(U),yerr=Sd1,fmt='.')
	plt.errorbar(w(U),d2,xerr=Sw(U),yerr=Sd2,fmt='.')
	plt.errorbar(w(U),d3,xerr=Sw(U),yerr=Sd3,fmt='.')

	plt.plot(np.sort(w(U)),nsort(w(U),d1))
	plt.plot(np.sort(w(U)),nsort(w(U),d2))
	plt.plot(np.sort(w(U)),nsort(w(U),d3))
		
	plt.xlabel("Erregerfrequenz w in Radianten/s")
	plt.ylabel(ur"delta t")
	plt.title("Zeitdifferenzdiagramm")
	plt.grid(True)
	plt.show()

plot_dt2()
#plotresonanz()
