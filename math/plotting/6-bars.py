#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Generate random fruit data
np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# Define labels for people and fruit
people = ['Farrah', 'Fred', 'Felicia']
fruit_labels = ['apples', 'bananas', 'oranges', 'peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']

# Create the figure and axis
fig, ax = plt.subplots()

# Plot stacked bars for each person
bottom = np.zeros(3)  # Start the stacking from zero
for i in range(len(fruit)):
    ax.bar(people, fruit[i], bottom=bottom, color=colors[i], width=0.5, label=fruit_labels[i])
    bottom += fruit[i]  # Update stacking position

# Set labels, title, and legend
ax.set_ylabel("Quantity of Fruit")
ax.set_ylim(0, 80)
ax.set_yticks(np.arange(0, 81, 10))
ax.set_title("Number of Fruit per Person")
ax.legend()

plt.show()
