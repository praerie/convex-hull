import matplotlib.pyplot as plt
import numpy as np


# Steps:
# 1. Find the lowest point (or leftmost if tied) as the starting point.
# 2. Sort points by polar angle relative to the start.
# 3. Iterate through points, using the cross product to keep only counterclockwise turns
#    (removing "inner" points that form concave angles).

def cross_product(o, a, b):
    """Computes the cross product of vectors OA and OB.

    Given three points (o, a, b), this determines whether the turn
    at point 'a' going towards 'b' is:

    - Counterclockwise (> 0): keep the point
    - Collinear (= 0): points are in a straight line
    - Clockwise (< 0): remove 'a' (it makes a right turn and should not be in the hull)

    Formula:
        (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    This is a determinant that represents the signed area of the parallelogram
    formed by vectors OA and OB.
    """
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points):
    """Computes the convex hull of a given set of 2D points using Graham's scan algorithm.

    The algorithm constructs the convex hull in two phases,
    the lower hull and the upper hull.
    1. Lower hull: processes points in sorted order from left to right,
       ensuring only counterclockwise turns are kept.
    2. Upper hull: processes points in reverse order from right to left,
       following the same counterclockwise rule.

    The result is a closed polygon that represents the smallest convex shape
    enclosing all given points.
    """

    # Sort points by x-coordinate (ascending). If x values tie, sort by y-coordinate.
    points = sorted(points)

    # Lower hull, left to right
    lower = []
    for p in points:
        # Ensure the last 3 points make a counterclockwise turn
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()  # Remove the last point since it's forming a right turn
        lower.append(p)  # Keep the current point

    # Upper hull, right to left
    upper = []
    for p in reversed(points):  # Process points in reverse order
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()  # Remove the last point since it's forming a right turn
        upper.append(p)

    # The last point of each half is repeated (connecting point), so remove duplicates
    return lower[:-1] + upper[:-1]


# Generate a random set of points, using seed for reproducibility
np.random.seed(327) 
points = np.random.rand(30, 2) * 10  

# Compute the convex hull
hull = convex_hull(points.tolist())

# Plot the points
plt.scatter(*zip(*points), label="Points", color="blue", alpha=0.6)

# Plot the convex hull (connect back to the first point to close the shape)
plt.plot(*zip(*(hull + [hull[0]])), 'r-', label="Convex Hull", linewidth=1)

plt.legend()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Convex Hull Visualization (Graham's Scan Algorithm)")
plt.show()
