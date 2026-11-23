import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi / 3, np.pi / 3, 500)
y = 3.22 * np.exp(0.1 * x) + np.tan(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, color="blue", linestyle="-.", label="y = 3,22·e^(0,1x) + tg x")
plt.title("Графік функції")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.savefig("drawings.jpg")
plt.show()
