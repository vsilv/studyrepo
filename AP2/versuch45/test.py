import matplotlib.pyplot as plt
import numpy as np
I=np.linspace(0,10,1000)
U=np.log2(I)
U2=np.log10(I)
plt.figure()
plt.plot(I,U)
plt.plot(I,U2)
plt.xscale("log")
plt.grid()
plt.show()
