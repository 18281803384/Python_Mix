import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2 * np.pi,2 * np.pi,200)
y = np.sin(x)

plt.subplot(221)

plt.plot(x,y)

plt.subplot(212)

plt.xlim(-2 * np.pi,2 * np.pi)

plt.xticks([-2 * np.pi,-3 * np.pi/2,-1 * np.pi,-1 * (np.pi) / 2,0,(np.pi) / 2,np.pi,3 * np.pi / 2,2 * np.pi],
           [r"$-2\pi$",r"$-3\pi/2$",r"$-\pi$",r"$-\pi/2$",r"$0$",r"$\pi/2$",r"$\pi$",r"$3\pi/2$",r"$2\pi$"])

plt.plot(x,y)

plt.show()