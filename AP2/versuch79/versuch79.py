# -*- coding: utf-8 -*-
import sympy as sy
import ocd
import matplotlib.pyplot as plt
Werte=ocd.open_csv("messung.csv")
alpha=sy.Symbol("alpha")
U=sy.Symbol("U")
U_rot=sy.Symbol("U_rot")
U_gruen=sy.Symbol("U_gruen")
var=[alpha,U,U_rot,U_gruen]
print sy.cos(90).evalf()
cos2=sy.cos(alpha)**2
plt.figure()
t1=ocd.plot_var(cos2,U,var,Werte,True)
t2=ocd.plot_var(cos2,U_rot,var,Werte,True)
t3=ocd.plot_var(cos2,U_gruen,var,Werte,True)
print "a: %.3f b: %.3f Sa: %.3f Sb: %.3f Sy: %.3f"%t1
print "a: %.3f b: %.3f Sa: %.3f Sb: %.3f Sy: %.3f"%t2
print "a: %.3f b: %.3f Sa: %.3f Sb: %.3f Sy: %.3f"%t3 
plt.xlabel(ur"$\cos(\alpha)^2$")
plt.ylabel(ur"$U$ in $mv$")
plt.title(ur"Bestätigung des Gesetzes ${I}'=\cos(\alpha)^2 I$")
plt.show()

