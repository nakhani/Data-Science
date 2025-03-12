import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



balloon_width = np.random.normal(60, 15, 100)
balloon_height = np.random.normal(80, 30, 100)
balloon_weight = np.random.normal(2, 30, 100)


melon_width = np.random.normal(60, 30, 100)
melon_height = np.random.normal(60, 10, 100)
melon_weight = np.random.normal(75, 30, 100)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(balloon_width, balloon_height, balloon_weight, color='b', marker='o', label='Balloons')


ax.scatter(melon_width, melon_height, melon_weight, color='orange', marker='^', label='Melons')


ax.set_xlabel('Width')
ax.set_ylabel('Height')
ax.set_zlabel('Weight')

ax.legend()

plt.show()