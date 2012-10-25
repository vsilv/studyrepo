# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import mylib
print " 2.1 Physikalisches Pendel"


l=95.4
Sl=0.3
t10 = np.array([16.09,16.12,16.12,16.08,16.09,16.03])/10
t20 = np.array([32.09,32.06,32.12,32.09,32.12,32.15])/20
t=np.concatenate([t10,t20])
print "T = (",t.mean(),"+-",t.std()," ) s"
print "T^2 = (",t.mean()**2,"+-",2*t.mean()*t.std()," ) s"
T2=t.mean()**2
ST2=2*t.mean()*t.std()
#reduzierte Länge
l1=2*l/3.0
Sl1=2*Sl/3.0
print "reduzierte Pendellänge",l1,"+-=",Sl1,"cm"
l2=981*t.mean()**2/(2*np.pi)**2
Sl2=l2*np.sqrt((2*t.std()/t.mean())**2+(1.0/981)**2)
print "bestimmte Pendellänge", l2,"+-",Sl2,"cm"
print l2/l1*100-100,"%"
# 2.2 Mathematisches Pendel

## 2.2.2 Bestimmung der Messgenauigkeit

l=59.7
t=np.array([15.56,15.50,15.59,15.53,15.43,15.53,15.56,15.56])/10
St=t.std()

# 2.2.1 Abhängigkeit von der Pändellänge

l=np.array([96.00,71.30,63.40,53.60,42.10])
Sl=0.3
t=np.array([19.59,17.03,16.09,14.75,13.15])/10
(a,b,Sa,Sb,Sy)=mylib.gerade(l,t**2)
def plot_abh():
	plt.figure()
	plt.errorbar(l,t**2,xerr=Sl,yerr=2*St*t,fmt='.')
	plt.plot([0,l.max()*1.1],[a,a+b*l.max()*1.1])
	plt.plot([0,l.max()*1.1],[a+Sa,a+Sa+(b+Sb)*l.max()*1.1],"m--")
	plt.plot([0,l.max()*1.1],[a-Sa,a-Sa+(b-Sb)*l.max()*1.1],"c--")
	plt.plot([0,l.max()*1.1],[0,4*np.pi**2/9.81])
	plt.xlabel(ur"Länge in $cm$",fontsize=20)
	plt.ylabel(ur"$T^2$ in $s^2$",fontsize=20)
	plt.title(ur"Mathematisches Pendel- Abhängigkeit der Länge")
	plt.legend([ur"Messwerte",ur"Ausgleichsgerade $a+b\cdot l$",ur"Obere Grenze $a+Sa+(b+Sb)\cdot l$",ur"Untere Grenze $a-Sa+(b-Sb)\cdot l$",ur"theoretische Gerade $T^2=4\pi^2\frac{l}{g}$"],loc=2)
	plt.grid(True)
	plt.show()
print "a:",a,"+-",Sa,"b",b,"+-",Sb,"Sy:",Sy
l=(T2-a)/b
Sl=l*np.sqrt((Sb/b)**2+((ST2/T2)**2+(Sa/a)**2)/(T2-a)**2)
print Sb/b,ST2/T2,Sa/a
print "berechnete reduzierte Pendellänge:",l,"+-",Sl
print 100-l/l2*100,"%"

# 2.2.3 Amplitudenabhängigkeit
t = np.array([15.46,15.56,15.75,15.85,15.53,15.59,15.79,15.43])/10
a1= np.array([10.00,20.00,30.00,40.00,15.00,25.00,35.00,18.00])*2*np.pi/360
a2= np.array([09.00,19.00,27.00,37.00,15.00,22.00,33.00,17.00])*2*np.pi/360

aa=( (a1+a2)/2)**2
(a,b,Sa,Sb,Sy)=mylib.gerade(aa,t)
T0=2*np.pi*np.sqrt(0.597/9.81)
ST0= 2*np.pi/32*np.sqrt((Sl/l)**2+(0.01/9.81)**2)/np.sqrt(l/9.81)
print "T0/16:",T0/16,"+-",ST0
def plot_Amplt():
	plt.figure()
	plt.errorbar(aa,t,yerr=Sy,xerr=2*np.pi/360*2*np.sqrt(aa),fmt='.')
	plt.plot([aa.min(),aa.max()],[a+b*aa.min(),a+b*aa.max()])
	plt.plot([aa.min(),aa.max()],[a+Sa+(b+Sb)*aa.min(),a+Sa+(b+Sb)*aa.max()],"m--")
	plt.plot([aa.min(),aa.max()],[a-Sa+(b-Sb)*aa.min(),a-Sa+(b-Sb)*aa.max()],"c--")
	plt.plot([aa.min(),aa.max()],[T0+aa.min()/16.0,T0+aa.max()/16])
	plt.legend([ur"Messwerte",ur"Ausgleichsgerade $a+b\cdot l$",ur"Obere Grenze $a+Sa+(b+Sb)\cdot l$",ur"Untere Grenze $a-Sa+(b-Sb)\cdot l$",ur"theoretische Gerade $T^2=4\pi^2\frac{l}{g}$"],loc=2)

	plt.ylabel("t in s",fontsize=20)
	plt.grid(True)
	plt.title(ur"Amplitudenabhängigkeit")
	plt.xlabel(ur"Amplitude $\barA^2$ in $Radianten^2$ ",fontsize=20)
	plt.show()
# 2.4 Steinersche Satz
d =11.9
Sd= 0.1
m =1159.2
Sm=   0.2
n=7
T= np.array([15.06,15.06,15.06,15.24,15.08,15.2])/7
coef=T.mean()**2/(2*np.pi)**2
Scoef= T.std()*2*coef
print "coef",coef,"+-",Scoef
ST=0.2/7
abst= 1.50
Sabst=0.05
T=np.array([16.99,17.56,18.17,19.34,20.67,22.48,24.51])/7
T2=T**2
absts=np.arange(0,(len(T))*1.5,1.5)
absts2=absts**2
(a,b,Sa,Sb,Sy)=mylib.gerade(absts2,T2)
D=4*np.pi**2*m/1000/b/10000
SD=D*np.sqrt((Sm/m)**2+(Sb/b)**2)
print "D=",D,"+-",SD
ID=coef*D
SID=ID*np.sqrt((Scoef/coef)**2+(SD/D)**2)
print "ID=",ID,"+-",SID
www =-ID+a*D/(2*np.pi)**2

SIO= np.sqrt(SID**2+(a*D/(2*np.pi)**2)**2*((Sa/a)**2+(SD/D)**2))
w2=0.5*m/1000*(d/200)**2
Sw2=w2* np.sqrt((Sm/m)**2+(Sd/d)**2)
print "I0",www,"+-",SIO
print "I0",w2,"+-",Sw2
print w2/www*100,"%"
def plot_ste():
	plt.figure()
	plt.errorbar(absts2,T2,xerr=2*absts*Sabst,yerr=Sy,fmt='.')
	plt.plot([absts2.min(),absts2.max()],[a+b*absts2.min(),a+b*absts2.max()])
	plt.plot([absts2.min(),absts2.max()],[a+Sa+(b+Sb)*absts2.min(),a+Sa+(b+Sb)*absts2.max()],"m--")
	plt.plot([absts2.min(),absts2.max()],[a-Sa+(b-Sb)*absts2.min(),a-Sa+(b-Sb)*absts2.max()],"c--")
	plt.legend([ur"Messwerte",ur"Ausgleichsgerade $a+b\cdot l$",ur"Obere Grenze $a+Sa+(b+Sb)\cdot l$",ur"Untere Grenze $a-Sa+(b-Sb)\cdot l$"],loc=2)

	plt.xlabel("Distanz $a^2$ in $cm^2$",fontsize=20)
	plt.grid(True)
	plt.title(ur"Prüfung des Steinerschen Satzes",fontsize=20)
	plt.ylabel(ur"Schwingungsdauer $T^2$ in $s^2$ ",fontsize=20)
	plt.show()
#plot_ste()
