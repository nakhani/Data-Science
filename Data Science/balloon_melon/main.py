import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



balloon_width = np.random.normal(4, 1, 400)
balloon_height = np.random.normal(9, 1, 400)
balloon_weight = np.random.normal(2, 0.5, 400)


melon_width = np.random.normal(6, 2, 400)
melon_height = np.random.normal(6, 2, 400)
melon_weight = np.random.normal(3, 1, 400)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(balloon_width, balloon_height, balloon_weight, color='b', marker='o', label='Balloons')


ax.scatter(melon_width, melon_height, melon_weight, color='orange', marker='^', label='Melons')


ax.set_xlabel('Width')
ax.set_ylabel('Height')
ax.set_zlabel('Weight')

ax.legend()

plt.show()