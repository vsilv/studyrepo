# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
import ocd
Werte=[ocd.Groesse("l1","cm",np.array([4.62]),np.array([0.02])),ocd.Groesse("l2","cm",np.array([5.44]),np.array([0.05])),ocd.Groesse("l","cm",np.array([10]),np.array([0])),ocd.Groesse("Cb","F",np.array([48.5+107])*10**-9,np.array([0]))]

Werte2=[ocd.Groesse("l1","cm",np.array([6.95]),np.array([0.01])),ocd.Groesse("l2","cm",np.array([3.06]),np.array([0.02])),ocd.Groesse("l","cm",np.array([10]),np.array([0])),ocd.Groesse("Lb","H",np.array([4])*10**-3,np.array([0]))]

l1=sy.Symbol("l1")
l2=sy.Symbol("l2")
l=sy.Symbol("l")
Cb=sy.Symbol("Cb")
Lb=sy.Symbol("Lb")

Cx1=Cb*(l-l2)/l2
Cx2=Cb*l1/(l-l1)

Lx1=Lb*(l1)/(l-l1)
Lx2=Lb*(l-l2)/(l2)

(g,e,f)=ocd.eval_expr(Cx1,[l1,l2,l,Cb],Werte,"Cx")
(g,e,f)=ocd.eval_expr(Cx2,[l1,l2,l,Cb],Werte,"Cx")
(g,e,f)=ocd.eval_expr(Lx1,[l1,l2,l,Lb],Werte2,"Lx")
print g
sy.pprint(f)
(g,e,f)=ocd.eval_expr(Lx2,[l1,l2,l,Lb],Werte2,"Lx")
print g
sy.pprint(f)
