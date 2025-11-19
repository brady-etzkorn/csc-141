import matplotlib.pyplot as plt
from random_walk import RandomWalk


rw = RandomWalk(5000)
rw.fill_randomwalk()

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(rw.x_values,rw.y_values,linewidth=1)

ax.plot(rw.x_values[0], rw.y_values[0], c='green',marker='o',label='Start')
ax.plot(rw.x_values[-1], rw.y_values[-1], c='red',marker='o',label='End')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

ax.legend()
plt.show()