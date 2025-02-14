import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


def cross_product(o, a, b):
    """Computes the cross product of vectors OA and OB."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull_animated(points):
    """Generates convex hull steps for animation."""
    points = sorted(points)  # Sort by x first, then y if tie

    lower, upper = [], []
    animation_steps = []

    # Lower hull construction
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            animation_steps.append((lower.copy(), p, "remove"))  # Record removal step
            lower.pop()
        lower.append(p)
        animation_steps.append((lower.copy(), p, "add"))  # Record addition step

    # Upper hull construction
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            animation_steps.append((upper.copy(), p, "remove"))
            upper.pop()
        upper.append(p)
        animation_steps.append((upper.copy(), p, "add"))

    hull = lower[:-1] + upper[:-1]
    return hull, animation_steps


# Generate random points, using seed for reproducibility 
np.random.seed(50)
points = np.random.rand(30, 2) * 10

# Compute convex hull with animation steps
hull, steps = convex_hull_animated(points.tolist())

# Set up figure
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title("Convex Hull Construction (Animated)")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

# Scatter plot for the points
sc = ax.scatter(*zip(*points), label="Points", color="blue", alpha=0.6)

# Line to display the convex hull
hull_line, = ax.plot([], [], 'r-', linewidth=1, label="Convex Hull")

# Highlighting points being processed
active_point, = ax.plot([], [], 'mo', markersize=8, label="Current Point")
removed_point, = ax.plot([], [], 'co', markersize=8, label="Removed Point")


# Animation
def update(frame):
    current_hull, p, action = steps[frame]
    hull_x, hull_y = zip(*current_hull)

    # Update hull line
    hull_line.set_data(hull_x + (hull_x[0],), hull_y + (hull_y[0],))

    # Highlight active point (ensuring it's a sequence)
    active_point.set_data([p[0]], [p[1]])

    # Highlight removed point if applicable (ensuring it's a sequence)
    if action == "remove":
        removed_point.set_data([p[0]], [p[1]])
    else:
        removed_point.set_data([], [])

    return hull_line, active_point, removed_point


# Create and display animation
ani = animation.FuncAnimation(fig, update, frames=len(steps), interval=500, repeat=False)
plt.legend()
plt.show()
