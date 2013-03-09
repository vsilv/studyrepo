# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import mylib as mm
import numpy as np
sina=[0.483,0.482,0.457,0.375]
lambd=np.array([579.100,577.000,546.100,435.800])*10**-9
Ssina=[0.001,0.001,0.001,0.001]
def plot11():
	(a,b,Sa,Sb,Sy)=mm.gerade(lambd,sina)
	print "a:",a,"+-",Sa
	print "b:",b,"+-",Sb
	t=np.linspace(min(lambd),max(lambd),1000)
	plt.figure()
	plt.title(ur"Bestätigung der Linearität der Beugungsordnungen")
	plt.xlabel(ur"Beugungsordnung $k$")
	plt.ylabel(ur"$sin(\alpha)$")
	plt.plot(t,b*t+a)
	plt.plot(t,(b+Sb)*t+a+Sa,"m--")
	plt.plot(t,(b-Sb)*t+a-Sa,"c--")
	plt.errorbar(lambd,sina,fmt=".",yerr=Ssina)
	plt.grid()
	plt.show()
#plot11()
sina=[0.080,0.080,0.076,0.061]
#plot11()

lambd=[1,2,3]
sina=[0.061,0.121,0.181,0.302]
sina=[0.061,0.121,0.181]
Ssina=[0.001,0.001,0.001]
#plot11()
plt.figure()
plt.xlabel(ur"$\alpha$")
plt.ylabel(ur"$\lambda / nm$")
plt.title(ur"Überlappung der Maxima höherer Ordnungen")
la=np.linspace(400,700,1000)
alpha2=lambda a:la*0+a
alpha=lambda k,l:np.arcsin(k*l/7.25*10**-3)
for k in range(100):
        plt.plot(alpha2(alpha(k,400)),la,"m--")
        plt.plot(alpha2(alpha(k,700)),la,"c--")
        plt.plot(alpha(k,la),la,"r")
plt.show()
