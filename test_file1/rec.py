import matplotlib.pyplot as plt
import math
import numpy as np
# plot = plt.figure()
x = [0, 2, 1]
y = [0, 0, math.sqrt(3)]

fig, ax = plt.subplots()
ax.fill(x,y)
x = np.linspace(1-math.sqrt(3)/3, 1+math.sqrt(3)/3, 500)
y1 = np.sin(x)
circle = plt.Circle((1, math.sqrt(3)/3), math.sqrt(3)/3, fill=False)
ax.add_artist(circle)
plt.show()