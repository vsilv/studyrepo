import matplotlib.pyplot as plt
import numpy as np
t=np.linspace(0,10,1000)
fig = plt.figure(figsize=(16,12))

ax1 = fig.add_subplot(221)
ax1.plot(t,np.exp(-t))
ax1.set_ylabel("$U_r$ in V")
ax1.set_xlabel("t in s")
ax1.set_title("Aufladevorgang: Spannung am Widerstand")

ax2 = fig.add_subplot(222)
ax2.plot(t,1-np.exp(-t))
ax2.set_ylabel("$U_c$ in V")
ax2.set_xlabel("t in s")
ax2.set_title("Aufladevorgang: Spannung am Kondensator")

ax3 = fig.add_subplot(223)
ax3.plot(t,-np.exp(-t))
ax3.set_ylabel("$U_r$ in V")
ax3.set_xlabel("t in s")
ax3.set_title("Entladevorgang: Spannung am Widerstand")

ax4 = fig.add_subplot(224)
ax4.plot(t,np.exp(-t))
ax4.set_ylabel("$U_c$ in V")
ax4.set_xlabel("t in s")
ax4.set_title("Entladevorgang: Spannung am Kondensator")

plt.show()
