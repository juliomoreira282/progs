import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)

f = 5

x = np.sin(2 * np.pi * f * t)

plt.plot(t, x)
plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.title("Sinal Senoidal de 5 Hz")
plt.grid()
plt.show()