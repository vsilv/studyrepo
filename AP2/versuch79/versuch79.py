# -*- coding: utf-8 -*-
import sympy as sy
import ocd
import matplotlib.pyplot as plt
import numpy as np
Werte=ocd.open_csv("messung.csv")
max_werte=[k.max() for k in Werte]
alpha=sy.Symbol("alpha")
U=sy.Symbol("U")
U_rot=sy.Symbol("U_rot")
U_gruen=sy.Symbol("U_gruen")
U_max=sy.Symbol("U_max")
U_rot_max=sy.Symbol("U_rot_max")
U_gruen_max=sy.Symbol("U_gruen_max")
var=[alpha,U,U_rot,U_gruen,U_max,U_rot_max,U_gruen_max]
cos2=sy.cos(alpha)**2
plt.figure()
t1=ocd.plot_var(alpha,U/U_max,var,Werte+max_werte,False)
t2=ocd.plot_var(alpha,U_rot/U_rot_max,var,Werte+max_werte,False)
t3=ocd.plot_var(alpha,U_gruen/U_gruen_max,var,Werte+max_werte,False)
x=np.linspace(-1.58,1.58,1000)
plt.plot(x,np.cos(x)**2)
#print "a: %.3f b: %.3f Sa: %.3f Sb: %.3f Sy: %.3f"%t1
#print "a: %.3f b: %.3f Sa: %.3f Sb: %.3f Sy: %.3f"%t2
#print "a: %.4f b: %.3f Sa: %.3f Sb: %.3f Sy: %.3f"%t3 
plt.xlabel(ur"$\alpha$")
plt.ylabel(ur"$\frac{I}{I}$")
plt.title(ur"Bestätigung des Gesetzes $I=\cos(\alpha)^3 I$")
plt.grid(True)
plt.show()

