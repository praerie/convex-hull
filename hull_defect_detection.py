# Identifies and visualizes convexity defects—concave points 
# where a contour deviates inward from its convex hull.

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# Generate random points forming a closed polygon
np.random.seed(33)
points = np.random.rand(15, 2) * 10

hull = ConvexHull(points)

# Identify concave points (not in the convex hull)
hull_vertices = set(hull.vertices)  
concave_points = [p for i, p in enumerate(points) if i not in hull_vertices]

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_title("Convexity Defect Detection")

# Plot original points (hull vertices)
ax.scatter(points[:, 0], points[:, 1], color="orange", label="Hull Vertices")

# Plot convex hull
# Simplex: simplest possible shape 
for simplex in hull.simplices:
    ax.plot(points[simplex, 0], points[simplex, 1], 'k-', linewidth=1.5)

# Color concave points
if concave_points:
    concave_x, concave_y = zip(*concave_points)
    ax.scatter(concave_x, concave_y, color="purple", label="Concave Points", zorder=3)

plt.legend()
plt.show()
