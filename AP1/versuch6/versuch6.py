# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <markdowncell>

# Abmessungen
import numpy as np
import matplotlib.pyplot as plt
# <codecell>

st_breite=np.array([5.955,5.955,5.955,5.950,5.950])
st_hoehe =np.array([10.325,9.950,9.960,9.950,10.04])
print "Stahl:",st_breite.mean(),"x",st_hoehe.mean()
al_breite=np.array([5.940,5.940,5.940,5.940,5.935])
al_hoehe =np.array([9.910,9.900,9.885,9.890,9.955])
print "Aluminium:",al_breite.mean(),"x",al_hoehe.mean()
me_breite=np.array([5.950,5.945,5.945,5.950,5.950])
me_hoehe =np.array([9.940,9.935,9.940,9.935,9.935])
print "Messing:",me_breite.mean(),"x",me_hoehe.mean()

Sm=0.02 #g
Ss=0.02 #mm

# <codecell>

import mylib

# <markdowncell>

# Stahl, Hochkant

# <codecell>

g1=np.concatenate([np.arange(200,(8+1)*200,200),np.arange((8)*200,0,-200)])
s1=np.array([0.19,0.39,0.59,0.78,0.98,1.17,1.37,1.77,1.58,1.38,1.19,0.99,0.79,0.60,0.41,0.21])

# <markdowncell>

# Messing Hochkant

# <codecell>

g2=np.concatenate([np.arange(100,(8+1)*100,100),np.arange((7)*100,-100,-100)])
s2=np.array([0.2,0.42,0.65,0.84,1.05,1.29,1.51,1.73,1.51,1.29,1.06,0.87,0.65,0.43,0.21,0.00])

# <markdowncell>

# Aluminium, Hochkant

# <codecell>

g3=np.concatenate([np.arange(50,(8+1)*50,50),np.arange((7)*50,-50,-50)])
s3=np.array([0.14,0.35,0.43,0.60,0.72,0.92,1.06,1.25,1.09,0.90,0.76,0.60,0.43,0.27,0.13,0.00])

# <codecell>
Bs=[]
SBs=[]
def calc(m,s,hoehe_,breite_,laenge,Slaenge):
    global Bs,SBs
    hoehe=hoehe_.mean()
    Sh   =hoehe_.std()
    breite=breite_.mean()
    Sbreite=breite_.std()
    #f=m*9.81
    (a,b,Sa,Sb,Sy)=mylib.gerade(m,s)
    #plt.scatter(m,s)
    plt.errorbar(m,s,yerr=Sm,xerr=Ss,fmt=',')
    plt.xlabel(ur"Masse m in g",fontsize=20)
    plt.ylabel("Durchbiegung s in mm",fontsize=20)
    plt.title(u"Messung des Elastizitätsmodules, Materialabhängigkeit")
    x=np.linspace(0,m.max()*1.1,1000)
    plt.xlim(0,2000)
    plt.ylim(0,2)
    plt.grid(True)
    plt.plot(x,a+b*x)
    E=(laenge**3*9.81)/(4*hoehe**3*breite*b)/1000
    SE=E*np.sqrt((3*Slaenge/laenge)**2+((3*Sh/hoehe)**2+(Sbreite/breite)**2+(Sb/b)**2+(0.01/9.81)**2)/(4*hoehe**3*breite*b*9.81)**2)
    print "(",E,"+-",SE,")N/mm^2"
    Bs+=[ b]
    SBs+=[Sb]

# <codecell>

l1=780.0
Sl1=5.0

plt.figure()
calc(g1,s1,st_hoehe.mean(),st_breite.mean(),l1,Sl1)

calc(g2,s2,al_hoehe.mean(),al_breite.mean(),l1,Sl1)
calc(g3,s3,me_hoehe.mean(),me_breite.mean(),l1,Sl1)
plt.show()

# <codecell>


# <codecell>


# <markdowncell>

# Stahl, quer

# <codecell>

g4=np.concatenate([np.arange(100,(8+1)*100,100),np.arange((7)*100,-100,-100)])
s4=np.array([0.2,0.45,0.7,0.99,1.31,1.58,1.85,2.15,1.84,1.56,1.32,1.02,0.73,0.48,0.21,0.00])

def calc2(m,s,hoehe_,breite_,laenge,Slaenge):

    global Bs,SBs
    hoehe=hoehe_.mean()
    Sh   =hoehe_.std()
    breite=breite_.mean()
    Sbreite=breite_.std()
    #f=m*9.81
    (a,b,Sa,Sb,Sy)=mylib.gerade(m,s)
    #plt.scatter(m,s)
    plt.errorbar(m,s,yerr=Sm,xerr=Ss,fmt=',')
    plt.xlabel(ur"Masse m in g",fontsize=20)					#Kraft in $mm \cdot kg \cdot s^{-2}$
    plt.ylabel("Durchbiegung s in mm",fontsize=20)
    plt.title(u"Messung des Elastizitätsmodules, Ausrichtung des Stabprofiels")
    x=np.linspace(0,m.max()*1.1,1000)
    plt.xlim(0,2000)
    plt.ylim(0,2.5)
    plt.grid(True)
    plt.plot(x,a+b*x)
    E=(laenge**3*9.81)/(4*hoehe**3*breite*b)*9.81/1000
    #E=(1/s)*laenge**3/(4*hoehe**3*breite*b)*m*9,81
    SE=E*np.sqrt((3*Slaenge/laenge)**2+((3*Sh/hoehe)**2+(Sbreite/breite)**2+(Sb/b)**2+(0.01/9.81)**2)/(4*hoehe**3*breite*b*9.81)**2)
    print "(",E,"+-",SE,")N/mm^2"
    
    Bs+=[ b]
    SBs+=[Sb]



plt.figure()
calc2(g4,s4,st_hoehe.mean(),st_breite.mean(),l1,Sl1)
calc2(g1,s1,st_hoehe.mean(),st_breite.mean(),l1,Sl1)
plt.show()
# <markdowncell>

# Messing in Abhängigkeit der Länge, hochkant

# <codecell>

l5=680.0
Sl5=5.0
g5=g4
s5=np.array([0.11,0.25,0.39,0.53,0.69,0.82,0.98,1.11,0.99,0.84,0.69,0.59,0.41,0.27,0.12,0.00])

# <codecell>
def calc3(m,s,hoehe_,breite_,laenge,Slaenge):

    global Bs,SBs
    hoehe=hoehe_.mean()
    Sh   =hoehe_.std()
    breite=breite_.mean()
    Sbreite=breite_.std()
    (a,b,Sa,Sb,Sy)=mylib.gerade(m,s)
    #plt.scatter(m,s)
    plt.errorbar(m,s,yerr=Sm,xerr=Ss,fmt=',')
    plt.xlabel(ur"Masse m in g",fontsize=20)
    plt.ylabel("Durchbiegung s in mm",fontsize=20)
    plt.title(u"Messung des Elastizitätsmodules, Längenabhängigkeit ")
    x=np.linspace(0,m.max()*1.1,1000)
    plt.xlim(0,1000)
    plt.ylim(0,2.0)
    plt.grid(True)
    plt.plot(x,a+b*x)
    E=(laenge**3*9.81)/(4*hoehe**3*breite*b)*9.81/1000
    #E=(1/s)*laenge**3/(4*hoehe**3*breite*b)*m*9,81
    SE=E*np.sqrt((3*Slaenge/laenge)**2+((3*Sh/hoehe)**2+(Sbreite/breite)**2+(Sb/b)**2+(0.01/9.81)**2)/(4*hoehe**3*breite*b*9.81)**2)
    print "(",E,"+-",SE,")N/mm^2"
    Bs+=[ b]
    SBs+=[Sb]


plt.figure()
calc3(g5,s5,me_hoehe.mean(),me_breite.mean(),l5,Sl5)
calc3(g2,s2,me_hoehe.mean(),me_breite.mean(),l1,Sl1)
plt.show()

# <codecell>


# <markdowncell>

# T-Träger hochkant

# <codecell>

l6=880.0
Sl6=5.0
g6=g5
s6=np.array([0.11,0.27,0.41,0.57,0.72,0.85,1.01,1.16,1.03,0.87,0.73,0.57,0.44,0.27,0.13,-0.03])

# <codecell>
def calc4(m,s,hoehe_,breite_,laenge,Slaenge):

    global Bs,SBs
    hoehe=hoehe_.mean()
    Sh   =hoehe_.std()
    breite=breite_.mean()
    Sbreite=breite_.std()
    (a,b,Sa,Sb,Sy)=mylib.gerade(m,s)
    #plt.scatter(m,s)
    plt.errorbar(m,s,yerr=Sm,xerr=Ss,fmt=',')
    plt.xlabel(ur"Masse m in g",fontsize=20)
    plt.ylabel("Durchbiegung s in mm",fontsize=20)
    plt.title(u"Messung des Elastizitätsmodules, Doppel-T-Träger")
    x=np.linspace(0,m.max()*1.1,1000)
    plt.xlim(0,1000)
    plt.ylim(0,2.0)
    plt.grid(True)
    plt.plot(x,a+b*x)
    E=laenge**3/(4*hoehe**3*breite*b)*9.81/1000
    #E=(1/s)*laenge**3/(4*hoehe**3*breite*b)*m*9,81
    SE=E*np.sqrt((3*Slaenge/laenge)**2+((3*Sh/hoehe)**2+(Sbreite/breite)**2+(Sb/b)**2+(0.01/9.81)**2)/(4*hoehe**3*breite*b*9.81)**2)
    print "(",E,"+-",SE,")N/mm^2"
    Bs+=[ b]
    SBs+=[Sb]

plt.figure()
calc4(g6,s6,st_hoehe.mean(),st_breite.mean(),l5,Sl5)
print Bs
print SBs
