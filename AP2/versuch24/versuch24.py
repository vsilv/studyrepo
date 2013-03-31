# -*- coding: utf-8 -*-
import ocd
import sympy as sy
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import scipy as sc
def get_distance(f):
        poisson= lambda k,mu: 1./(sc.factorial(k)*np.exp(mu))*mu**k
        normal_k= lambda k,mu: 1./np.sqrt(2*np.pi*mu)*np.exp(-(k-mu)**2/(2*mu))
        mu_=np.arange(1,100+1,1)
        vals=np.zeros([100])
        for k in xrange(len(mu_)):
                mu=mu_[k]
                x=abs(poisson(0,mu)-normal_k(0,mu))
                xlim=x*10**(-f)
                s=0
                n=0
                while x>xlim:
                        n+=1
                        x=abs(poisson(n,mu)-normal_k(n,mu))
                        s+=x
                vals[k]=s
        plt.plot(mu_,vals)
def get_max_distance():
        poisson= lambda k,mu: 1./(sc.factorial(k)*np.exp(mu))*mu**k
        normal_k= lambda k,mu: 1./np.sqrt(2*np.pi*mu)*np.exp(-(k-mu)**2/(2*mu))
        mu_=np.arange(1,100+1,1)
        vals=np.zeros([100])
        for k in xrange(len(mu_)):
                mu=mu_[k]
                x=abs(poisson(0,mu)-normal_k(0,mu))
                xlim=x*10**(-3)
                s=0
                n=0
                while x>xlim:
                        n+=1
                        x=abs(poisson(n,mu)-normal_k(n,mu))
                        s=max(s,x)
                vals[k]=s
        plt.plot(mu_,vals)


def plot_messung(n,t,b_len,y_lim,lens,rate):
	mu,sigma=np.mean(n),np.std(n)
        print "Mittelwert: %.3f"%mu
        print "Varianz: %.3f Poisson: %.3f"%(sigma**2,mu)
        print "Standardabweichung: %.3f Poisson: %.3f"%(sigma,np.sqrt(mu))
        print "Standardabweichung des Mittelwerts: %.3f Poisson: %.3f"%(sigma/np.sqrt(len(n)),np.sqrt(mu)/np.sqrt(len(n)))
        print "Gesamtanzahl der Ereignisse:",np.sum(n)
        print "mittlere Zaehlrate: %.3f 1/s"%(np.mean(n)/(rate))
        print "Standardabweichung der Zaehlrate: %.3f 1/s"%(np.std(n)/rate)
        print "Standardabweichung der mittleren Zaehlrate: %.3f 1/s"%(np.std(n)/rate/np.sqrt(len(n)))
        print "Schiefe: %.3f Poisson: %.3f"%(np.mean((n-n.mean())**3)/sigma**3,1/np.sqrt(mu))
        print "Kurtosis: %.3f Poisson: %.3f"%(np.mean((n-n.mean())**4)/sigma**4-3,1/(mu))
        print ""
        fig=plt.figure(figsize=(16,12))
	ax = fig.add_subplot(111)

	# the histogram of the data
	n, bins, patches = ax.hist(n, lens, normed=1, facecolor='yellow', alpha=0.75)


	bincenters = 0.5*(bins[1:]+bins[:-1])
	b=np.linspace(0,b_len,1000)
	b2=np.arange(0,b_len,1)+0.5

	# add a 'best fit' line for the normal PDF
		#y = mlab.normpdf( b, mu, sigma)
	#y2 =mlab.normpdf( b2, mu, sigma)
	#l = ax.plot(b, y, 'b--', linewidth=1)
        poisson= lambda k: 1./(sc.factorial(k)*np.exp(mu))*mu**k
        poisson2= lambda k: 1./(sc.factorial(k)*np.exp(mu+sigma))*(mu+sigma)**k
        poisson3= lambda k: 1./(sc.factorial(k)*np.exp(mu-sigma))*(mu-sigma)**k
        normal_k= lambda k: 1./np.sqrt(2*np.pi*mu)*np.exp(-(k-mu)**2/(2*mu))
        normal_k2= lambda k: 1./np.sqrt(2*np.pi*(mu+sigma))*np.exp(-(k-(mu+sigma))**2/(2*(mu+sigma)))
        normal_k3= lambda k: 1./np.sqrt(2*np.pi*(mu-sigma))*np.exp(-(k-(mu-sigma))**2/(2*(mu-sigma)))


	nk= ax.plot(b, normal_k(b), 'g--', linewidth=1)
	nk= ax.plot(b, normal_k2(b), 'g--', linewidth=1)
	nk= ax.plot(b, normal_k3(b), 'g--', linewidth=1)
	p = ax.plot(b, poisson(b), 'r--', linewidth=1)
	p = ax.plot(b, poisson2(b), 'r--', linewidth=1)
	p = ax.plot(b, poisson3(b), 'r--', linewidth=1)
	l = ax.scatter(b2, normal_k(b2),marker="x" ,c="b")
	p = ax.scatter(b2, poisson(b2) ,marker="x" ,c="b")


	ax.set_xlabel('Anzahl der Impulse')
	ax.set_ylabel('Wahrscheinlichkeit')
	plt.xlim(0,b_len)
	plt.ylim(0,y_lim)
	ax.grid(True)

	plt.show()
def plot_messung3():
        H=np.array([6.45*10**2,3.45*10**2,9.5*10,14,2])	
	mu=np.sum(H*np.arange(0,5,1))/np.sum(H)
	n=np.arange(0,5,1)
	sigma=np.sqrt((np.sum(H*(np.arange(0,5,1)-mu)**2)/(np.sum(H)-1)))
        print "Mittelwert: %.3f"%mu
        print "Varianz: %.3f Poisson: %.3f"%(sigma**2,mu)
        print "Standardabweichung: %.3f Poisson: %.3f"%(sigma,np.sqrt(mu))
        print "Standardabweichung des Mittelwerts: %.3f Poisson: %.3f"%(sigma/np.sqrt(np.sum(H)),np.sqrt(mu)/np.sqrt(np.sum(H)))
        print "Gesamtanzahl der Ereignisse:",np.sum(H*n)
        print "mittlere Zaehlrate: %.3f 1/s"%(mu/(0.5))
        print "Standardabweichung der Zaehlrate: %.3f 1/s"%(sigma/0.5)
        print "Standardabweichung der mittleren Zaehlrate: %.3f 1/s"%(sigma/0.5/np.sqrt(np.sum(H)))
        print "Schiefe: %.3f Poisson: %.3f"%((np.sum(H*(n-mu)**3)/np.sum(H))/sigma**3,1/np.sqrt(mu))
        print "Kurtosis: %.3f Poisson: %.3f"%((np.sum(H*(n-mu)**4)/np.sum(H))/sigma**4-3,1/(mu))

        print ""

        fig=plt.figure(figsize=(16,12))
        plt.scatter(np.arange(0,4+1,1),H/1101,marker="^",s=80)
        poisson= lambda k: 1./(sc.factorial(k)*np.exp(mu))*mu**k
        normal_k= lambda k: 1./np.sqrt(2*np.pi*mu)*np.exp(-(k-mu)**2/(2*mu))
        b=np.linspace(0,5,100)
        b2=np.arange(0,5,1)
        plt.plot(b, normal_k(b), 'g--', linewidth=1)
	plt.plot(b, poisson(b), 'r--', linewidth=1)
	plt.scatter(b2, normal_k(b2),marker="x" ,c="b")
	plt.scatter(b2, poisson(b2) ,marker="x" ,c="b")
        plt.title("Messung 3")
        plt.xlabel("Anzahl der Pulse")
        plt.ylabel("Wahrscheinlichkeit")
        plt.grid(True)
        plt.xlim(0,5)
        plt.ylim(0,0.7)
        plt.show()

messung1=ocd.open_csv("messung1.csv")
n1=messung1[0].x.magnitude
t1=messung1[1].x.magnitude
plot_messung(n1,t1,50,0.1,32,1.5)
       
messung2=ocd.open_csv("messung2.csv")
n2=messung2[1].x.magnitude
t2=messung2[0].x.magnitude
plot_messung(n2,t2,12,0.2,13,0.5)

plot_messung3()
