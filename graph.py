import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = x**2

plt.plot(x, y)
plt.title("y = x^2")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
