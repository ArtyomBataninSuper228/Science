import matplotlib.pyplot as plt
import numpy as np
N = 16
theta = np.arange(0.,2 * np.pi, 2 * np.pi / N) # Углы для каждого направления
radii = np.array([3.9, 4.8, 4.3, 5.3, 16.4, 0.4, 4.3, 4.3, 3.6, 6, 4, 3.9, 4.5, 7.4, 4.2, 3.6]) #Значениея (начиная с востока в обратном порядке
# что бы углы соответствовали сторонам света)
plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
bars = plt.bar(theta, radii, width=(2*np.pi/N), bottom=0.0,)
plt.show()
