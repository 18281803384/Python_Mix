import numpy as np
import matplotlib.pyplot as plt

sig = np.zeros(100, np.float64)
sig[30:60] = 1
fig, ax = plt.subplots()
ax.plot(sig)
ax.set_ylim(-0.1,1.1)
plt.show()