# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
plt.figure()
beta=np.linspace(0.2,5,1000)
b_f=beta+1
g_f=(beta+1)/beta
e_f=b_f+g_f
plt.xlabel(ur"Abbildungsmaßstab", fontsize=24)
plt.ylabel(ur"Bildweite $\frac{b}{f}$, Gegenstandsweite $\frac{g}{f}$ und Gesamtabstand $\frac{e}{f}$",fontsize=20)
plt.title(ur"Theoretischer Verlauf von $g$, $b$ und $e$", fontsize=24)
plt.loglog(beta,b_f)
plt.loglog(beta,g_f)
plt.loglog(beta,e_f)
plt.legend([ur"Bildweite $\frac{b}{f}$",ur"Gegenstandsweite $\frac{g}{f}$",ur"Gesamtabstand $\frac{e}{f}$"])
plt.grid(True,which="majorminor",ls="-")
plt.show()
