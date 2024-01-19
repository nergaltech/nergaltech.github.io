# dibujar la función seno con python

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi + 0.1,  0.1)
f = plt.figure(dpi=60)
plt.plot(x, np.sin(x))
plt.grid()
plt.show()
plt.close()

"""en aquí comentariooooo"""