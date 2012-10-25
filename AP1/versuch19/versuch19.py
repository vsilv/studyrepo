# -*- coding: utf-8 -*-
import numpy as np
print "Überprüfung der Schwingungsdauer"
T1=np.array([18.49,18.49,18.5,18.55,18.42])/10
T2=np.array([18.47,18.6,18.44,18.23,18.38])/10
print T1.mean(),"+-",T1.std(),T2.mean(),"+-",T2.std()
print T1.mean()/T2.mean()*100-100,"%"
print "Daten"
l1 = 80.0
Sl1=  0.2
l2 = 80.0
Sl2=  0.2
L1 = 92.5
SL1=  0.2

print "1.Gegensinnige Schwingung"
T=np.array([29.5,29.24,29.27,29.44,29.29,29.27,29.2])/20
ST=0.2
wa=2*np.pi/T.mean()
Swa=2*np.pi*T.std()/T.mean()**2
print "wa=",wa,"+-",Swa

print "2.Gleichsinnige Schwingung"
T=np.array([37.09,36.87,37.13,37.06,37.21,37.09,37.09])/20
wb=2*np.pi/T.mean()
Swb=2*np.pi*T.std()/T.mean()**2
print "wb=",wb,"+-",Swb

print "3.Schwebung"
T=np.array([69.88,70.43,70.81,70.67,70.84,70.62])/5
ws=2*np.pi/T.mean()
Sws=2*np.pi*T.std()/T.mean()**2
print "ws=",ws,"+-",Sws
ws2=0.5*(wa-wb)
Sws2=0.5*np.sqrt(Swa**2+Swb**2)
print "ws2=",ws2,"+-",Sws2
print ws2/ws*100-100,"% Abweichung"
K1=(wa**2-wb**2)/(wa**2+wb**2)
SK1=np.sqrt((4*wb*wa**2/(wb**2+wa**2)**2)*Swb**2+(4*wa*wb**2/(wa**2+wb**2)**2)*Swa**2)

print "neue Längen"
l1 = l2= 71.0
Sl1= Sl2= 0.5

print "4.Schwebung"
T=np.array([87.89,87.96,88.28,88.2,88.91,88.17])/5
ws=2*np.pi/T.mean()
Sws=2*np.pi*T.std()/T.mean()**2
print "ws=",ws,"+-",Sws

print "5.Gegensinnig"
T=np.array([15.35,15.42,15.18,15.39,15.28,15.32])/10
wa=2*np.pi/T.mean()
Swa=2*np.pi*T.std()/T.mean()**2
print "wa=",wa,"+-",Swa


print "6.Gleichsinnig"
T=np.array([19.66,19.63,19.37,19.41,19.37,19.45])/10
wb=2*np.pi/T.mean()
Swb=2*np.pi*T.std()/T.mean()**2
print "wb=",wb,"+-",Swb

ws2=0.5*(wa-wb)
Sws2=0.5*np.sqrt(Swa**2+Swb**2)
print "ws2=",ws2,"+-",Sws2
print ws2/ws*100-100,"% Abweichung"

wb=-2*ws+wa
Swb=np.sqrt(4*Sws**2+Swa**2)
print "neues wb:",wb,"+-",Swb
K2=(wa**2-wb**2)/(wa**2+wb**2)
SK2=np.sqrt((4*wb*wa**2/(wb**2+wa**2)**2)*Swb**2+(4*wa**3/(wa**2+wb**2)**2)*Swa**2)
print "K1:",K1,"+-",SK1,"K2:",K2,"+-",SK2




