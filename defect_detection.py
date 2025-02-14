# Identifies and visualizes convexity defects—concave points 
# where a contour deviates inward from its convex hull.

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull, distance

# Generate random points forming a closed polygon
np.random.seed(777)
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

    # Visualize defect depth with dotted lines from concave points to hull edge
    for p in concave_points:
        min_dist = float('inf')
        nearest_edge = None
        projection_point = None

        # Iterate over each hull edge
        for simplex in hull.simplices:
            a, b = points[simplex[0]], points[simplex[1]]

            # Compute projection of p onto line segment AB
            ab = b - a
            ap = p - a
            t = np.dot(ap, ab) / np.dot(ab, ab) 

            # Clamp t to stay within the segment
            t = max(0, min(1, t))
            closest_point = a + t * ab  # Projection on segment

            # Compute distance from p to projected point
            dist = distance.euclidean(p, closest_point)

            # Update nearest edge if this one is closer
            if dist < min_dist:
                min_dist = dist
                nearest_edge = (a, b)
                projection_point = closest_point

        # Draw a dotted line from concave point to its projection on the hull
        if projection_point is not None:
            ax.plot([p[0], projection_point[0]], [p[1], projection_point[1]], 'b--', alpha=0.2, linewidth=1)

plt.legend()
plt.show()
