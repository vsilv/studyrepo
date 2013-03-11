import ocd
import sympy as sy
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import scipy as sc
def plot_messung1():
	messung1=ocd.open_csv("messung1.csv")
	n=messung1[0].x.magnitude
	t=messung1[1].x.magnitude

	mu,sigma=np.mean(n),np.std(n)
	fig= plt.figure()
	ax = fig.add_subplot(111)

	# the histogram of the data
	n, bins, patches = ax.hist(n, 32, normed=1, facecolor='yellow', alpha=0.75)


	b=np.linspace(0,50,1000)
	b2=np.arange(0,50,1)+0.5

	# add a 'best fit' line for the normal PDF
	poisson= lambda k: 1./(sc.factorial(k)*np.exp(mu))*mu**k
	y = mlab.normpdf( b, mu, sigma)
	y2 =mlab.normpdf( b2, mu, sigma)
	l = ax.plot(b, y, 'b--', linewidth=1)
	p = ax.plot(b, poisson(b), 'b--', linewidth=1)
	l = ax.scatter(b2, y2,marker="x" ,c="b")
	p = ax.scatter(b2, poisson(b2) ,marker="x" ,c="b")
	ax.set_xlabel('Anzahl der Impulse')
	ax.set_ylabel('Wahrscheinlichkeit')
	ax.grid(True)
	plt.ylim(0,0.09)
	plt.xlim(10,50)
	plt.show()
def plot_messung2():
	messung2=ocd.open_csv("messung2.csv")
	n=messung2[1].x.magnitude
	t=messung2[0].x.magnitude

	mu,sigma=np.mean(n),np.std(n)
	fig= plt.figure()
	ax = fig.add_subplot(111)

	# the histogram of the data
	n, bins, patches = ax.hist(n, 13, normed=1, facecolor='yellow', alpha=0.75)


	bincenters = 0.5*(bins[1:]+bins[:-1])
	b=np.linspace(0,13,1000)
	b2=np.arange(0,13,1)+0.5

	# add a 'best fit' line for the normal PDF
	poisson= lambda k: 1./(sc.factorial(k)*np.exp(mu))*mu**k
	y = mlab.normpdf( b, mu, sigma)
	y2 =mlab.normpdf( b2, mu, sigma)
	l = ax.plot(b, y, 'b--', linewidth=1)
	p = ax.plot(b, poisson(b), 'r--', linewidth=1)
	l = ax.scatter(b2, y2,marker="x" ,c="b")
	p = ax.scatter(b2, poisson(b2) ,marker="x" ,c="b")


	ax.set_xlabel('Anzahl der Impulse')
	ax.set_ylabel('Wahrscheinlichkeit')
	plt.xlim(0,13)
	plt.ylim(0,0.2)
	ax.grid(True)

	plt.show()
plot_messung2()
