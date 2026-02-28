import matplotlib.pyplot as plt
import numpy as np
N = 16
theta = np.arange(0.,2 * np.pi, 2 * np.pi / N) # Углы для каждого направления
radii = np.array([6.5, 7.2, 3, 2.6, 1.9, 3.7, 2.2, 6, 6.9, 14.5, 7.4, 6.4, 5.3, 8.5, 4.8, 5.1]) #Значениея (начиная с востока в обратном порядке
# что бы углы соответствовали сторонам света)
print(len(radii))
plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
bars = plt.bar(theta, radii, width=(2*np.pi/N), bottom=0.0,)
plt.show()
