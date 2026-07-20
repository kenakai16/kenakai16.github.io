import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

# Set seed for reproducibility
np.random.seed(42)

# Roll a 6-sided die 10000 times
num_rolls = 10000
rolls = np.random.randint(1, 7, size=num_rolls)
# Calculate cumulative average
cum_avg = np.cumsum(rolls) / np.arange(1, num_rolls + 1)

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(0, num_rolls)
ax.set_ylim(1, 6)
ax.axhline(3.5, color='red', linestyle='--', label='Theoretical Expected Value (3.5)')
line, = ax.plot([], [], label='Empirical Cumulative Average', color='blue', alpha=0.8)
ax.set_xlabel('Number of Rolls')
ax.set_ylabel('Average Value')
ax.set_title('Simulation of the Law of Large Numbers (10,000 Die Rolls)')
ax.legend()
ax.grid(True, linestyle=':', alpha=0.6)

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Animation function called sequentially
def animate(i):
    # Step by 100 to speed up rendering for 10000 rolls (total 100 frames)
    current_limit = (i + 1) * 100
    x = np.arange(1, current_limit + 1)
    y = cum_avg[:current_limit]
    line.set_data(x, y)
    return line,

# Ensure images directory exists
os.makedirs("images", exist_ok=True)

# Create animation (100 frames, 50ms interval)
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

# Save as GIF
print("Saving 10000-roll animation as GIF...")
ani.save("images/lln_simulation.gif", writer='pillow', fps=20)
print("Animation saved successfully at images/lln_simulation.gif")
