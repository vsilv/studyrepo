import numpy as np
import matplotlib.pyplot as plt
import re
def get(s):
	F=open(s)
	w=F.read()	
	F.close()
	w=re.sub(",",".",w).split()
	w=np.array([float(k)for k in w])
	return w
Np=get("np.txt")
Nf=get("nf.txt")
Tp=get("tp.txt")
Tf=get("tf.txt")
r=get("r.txt")
m=4.47
Sm=0.01
g=9.81
Sg=0.01
G=m*g
ST=0.5
Snp=0.2
Snf=1
Sr=0.1
SG=G*np.sqrt((Sg/g)**2+(Sm/m)**2)

wp=2*np.pi/Tp*Np
wf=2*np.pi/Tf*Nf
wp[21::]=wp[21::]*-1


Swp=wp*np.sqrt((ST/Tp)**2+(Snp/Np)**2)
Swf=wf*np.sqrt((ST/Tf)**2+(Snf/Nf)**2)

k=wp*wf/G
Sk=k*np.sqrt((Swp/wp)**2+(Swf/wf)**2)
import mylib
#x=get("data.txt")
(a,b,Sa,Sb,Sy)=mylib.gerade(r,k)
print "a",a,"b",b,"Sa",Sa,"Sb",Sb,"Sy",Sy
SI= Sb/b**2
print "I=",1/b,"+-",SI
print "schwerpunkt bei",-a/b,"+-",-a/b*np.sqrt((Sa/a)**2+(Sb/b)**2),"cm"
def plot1():
	plt.figure()
	plt.errorbar(r,k,xerr=Sr,yerr=Sk,fmt=".")
	plt.plot([r.min(),r.max()],[a+b*r.min(),a+b*r.max()])
	plt.plot([r.min(),r.max()],[a+Sa+(b+Sb)*r.min(),a+Sa+(b+Sb)*r.max()],"r--")
	plt.plot([r.min(),r.max()],[a-Sa+(b-Sb)*r.min(),a-Sa+(b-Sb)*r.max()],"r--")
	plt.grid(True)
	plt.xlabel("r in cm")
	plt.show()
#plot1()
