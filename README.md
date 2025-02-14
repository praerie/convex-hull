# Hull Processing

Python-based computational geometry playground focused on convex hull construction and visualization.

## Graham's Scan: Convex Hull Construction

[convex_hull.py](/convex_hull.py) computes the convex hull of a set of 2D points using implements Graham's scan algorithm.

### Steps:
1. Find the lowest point (or leftmost if tied) as the starting point.
2. Sort points by polar angle relative to the start.
3. Iterate through points, using the cross product to keep only counterclockwise turns (removing "inner" points that form concave angles).

Visualized using `matplotlib`, the result is the smallest convex polygon enclosing all given points.

#### Processing time: `O(n log n)`



