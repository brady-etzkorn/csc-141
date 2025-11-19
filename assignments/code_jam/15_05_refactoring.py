import matplotlib.pyplot as plt
from random import choice

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self, direction_choices, distance_choices):
        """Determine direction and distance, then return the step."""
        direction = choice(direction_choices)
        distance = choice(distance_choices)
        return direction * distance

    def fill_walk(self):
        """Generate all the points in the walk."""
        while len(self.x_values) < self.num_points:
             x_step = self.get_step([1, -1], [0, 1, 2, 3, 4])
             y_step = self.get_step([1, -1], [0, 1, 2, 3, 4])

             if x_step == 0 and y_step == 0:
                continue

             next_x = self.x_values[-1] + x_step
             next_y = self.y_values[-1] + y_step

             self.x_values.append(next_x)
             self.y_values.append(next_y)

rw = RandomWalk()
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(rw.x_values, rw.y_values, linewidth=1)

# Highlight start and end points
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

plt.show()


