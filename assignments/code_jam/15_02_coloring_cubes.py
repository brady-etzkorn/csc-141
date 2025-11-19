import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.plasma, s=10)

ax.set_title("Cubes Colored by Value ",fontsize=20)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Cube of Value",fontsize=14)
ax.tick_params(labelsize=14)

plt.savefig('colored_cubes_plot.png', bbox_inches='tight')
plt.show()