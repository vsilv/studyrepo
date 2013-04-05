import ocd
import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

messung221=ocd.open_csv("211.csv")
messung222=ocd.open_csv("212.csv")
f = sy.Symbol("f")
Ue = sy.Symbol("Ue")
Ua = sy.Symbol("Ua")
var=[f,Ue,Ua]
f_=np.linspace(0,120000,1000)
def plot_ver():
	plt.figure()
	ocd.plot_var(f,Ua/Ue,var,messung221)
	ocd.plot_var(f,Ua/Ue,var,messung222)
	plt.plot(f_,5000/f_)
	plt.ylim(0,100)
	plt.xlabel("f in Hz")
	plt.ylabel(ur"Verstarkung A")
	plt.show()
plot_ver()
