import ocd
import sympy as sy
import matplotlib.pyplot as plt
import numpy as np
ex1=ocd.open_csv("ex1.csv")
ex2=ocd.open_csv("ex2.csv")
ex3=ocd.open_csv("ex3.csv")
ex4=ocd.open_csv("ex4.csv")
ex5=ocd.open_csv("ex5.csv")
offsets=ocd.open_csv("offsets.csv")

e_=sy.Symbol("e_")
g_=sy.Symbol("g_")

xb=sy.Symbol("xb")
xs=sy.Symbol("xs")
xa=sy.Symbol("xa")
xl=sy.Symbol("xl")

var=[e_,g_,xb,xs,xa,xl]

e = e_ + xa + xs
g = g_ + xa + xb
b = e - g
beta = b / g
f = g*b/ (g+b)

def plot_gbe(ex,f_re):
	plt.figure()
	beta_r=np.linspace(0.2,5,1000)
	g_f=beta_r+1
	b_f=(beta_r+1)/beta_r
	plt.loglog(beta_r,g_f)
	plt.loglog(beta_r,b_f)
	plt.loglog(beta_r,g_f+b_f)
	ocd.plot_var(beta,e/f_re,var,ex+offsets)
	ocd.plot_var(beta,b/f_re,var,ex+offsets)
	ocd.plot_var(beta,g/f_re,var,ex+offsets)
	plt.xlabel(ur"$\beta$")
	plt.ylabel(ur"Theoretischer und gemessener Wert")
	plt.title(ur"Verlauf der Bildweite $b$, Gegenstandsweite $g$ und Gesamtabstand $e$ bei Gesamtbrennweite $f="+str(f_re)+"m$")	
	plt.show()

#plot_gbe(ex1,0.08)
#plot_gbe(ex2,0.0574)
#plot_gbe(ex3,0.0574)

def write_table(ex,f_re):
	global inner
	inner+=ocd.table_groesse(g,var,ex+offsets,"g",True)
	inner+=ocd.table_groesse(b,var,ex+offsets,"b",True)
	inner+=ocd.table_groesse(f,var,ex+offsets,"f",True)
	inner+=ocd.table_groesse(beta,var,ex+offsets,ur"beta",True)
	f_r= ocd.eval_expr(f,var,ex+offsets,"f")
	f_mean=np.mean(f_r.x.magnitude)
	f_std=np.std(f_r.x.magnitude)
	inner+=ur"Mittelwert: %.3f\\"%f_mean
	inner+=ur"Standartabweichung: %.3f\\" % np.std(f_r.x.magnitude)
	inner+=ur"gemessene Brechkraft: $\phi=\frac{1}{f}=%.3f +- %.3f\\ $"% ((1/f_mean),f_std/f_mean**2)

	inner+=ur"theoretische Brechkraft: %.3f\\ "% (1/f_re)

inner=ur"Experiment I \\ "
write_table(ex1,0.08)
inner+=ur"Experiment II 1. \\ "
write_table(ex2,0.0574)
inner+=ur"Experiment II 2. \\ "
write_table(ex3,0.0574)

inner+=ur"Experiment III 1.\\ "
B=sy.Symbol("B")
B_orginal=sy.Symbol("B_orginal")
b__=sy.Symbol("b__")
b_=e_-b__+xs
var+=[B,b__]
beta=B/B_orginal
inner+=ocd.table_groesse(beta,var,ex4+offsets,ur"beta",True)
inner+=ocd.table_groesse(beta,var,ex5+offsets,ur"beta",True)
plt.figure()
(a,b,Sa,Sb,Sy)=ocd.plot_var(b_,beta,var,ex4+offsets,True)
(a,b,Sa,Sb,Sy)=ocd.plot_var(b_,beta,var,ex5+offsets,True)
plt.xlim(0,0.9)
plt.ylim(0,7)
plt.xlabel(ur"${b}' $ in m ")
plt.ylabel(ur"$\beta$")
plt.title(ur"gemessene Brechkraft: $\phi=(%.3f \pm %.3f) \frac{1}{m}$ theoretische Brechkraft:  $\phi=%.3f \frac{1}{m}$"%(b,(Sb),(1/0.11429)))
plt.show()


ocd.write_tex(inner)

