import matplotlib.pyplot as plt
import numpy as np

# steps:
# 1. find the lowest point (or leftmost if tied) as the starting point
# 2. sort points by polar angle relative to the start
# 3. iterate through points, using the cross product
# to keep only counterclockwise turns (removing "inner" points)


def cross_product(o, a, b):
    """Returns the cross product of vectors OA and OB.
    If >0, counterclockwise turn. If <0, clockwise turn."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def convex_hull(points):
    """Computes the convex hull of a given set of 2D points
    using Graham's scan algorithm."""
    points = sorted(points)  # sort points by x (then y if tie)

    # build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]  # remove duplicates


# generate random points
np.random.seed(42)
points = np.random.rand(30, 2) * 10  # 30 random points in 10x10 space

# compute convex hull
hull = convex_hull(points.tolist())

# plot
plt.scatter(*zip(*points), label="Points")
plt.plot(*zip(*(hull + [hull[0]])), 'r-', label="Convex Hull")  # loop back to start
plt.legend()
plt.show()