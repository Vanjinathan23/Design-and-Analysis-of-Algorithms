"""
Design and Analysis of Algorithms - CSA0609
Closest Pair of Points & Convex Hull
Brute Force, Divide-and-Conquer, and Hybrid implementations.
"""
import math
import time
import random
import itertools

# ----------------------------------------------------------------------
# CLOSEST PAIR OF POINTS
# ----------------------------------------------------------------------

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair_brute_force(points):
    """O(n^2) - examine every pair exactly once."""
    n = len(points)
    min_d = float('inf')
    pair = None
    comparisons = 0
    for i in range(n):
        for j in range(i + 1, n):
            comparisons += 1
            d = dist(points[i], points[j])
            if d < min_d:
                min_d = d
                pair = (points[i], points[j])
    return min_d, pair, comparisons


def closest_pair_dc(points, leaf_size=3):
    """Classic O(n log n) divide and conquer (pure recursion, no brute-force
    shortcut other than the terminating base case) used as the theoretical
    baseline for comparison against the Hybrid version below."""
    comparisons = [0]

    def rec(px, py):
        n = len(px)
        if n <= leaf_size:
            best = float('inf')
            pair = None
            for i in range(n):
                for j in range(i + 1, n):
                    comparisons[0] += 1
                    d = dist(px[i], px[j])
                    if d < best:
                        best, pair = d, (px[i], px[j])
            return best, pair

        mid = n // 2
        midx = px[mid][0]
        Lx, Rx = px[:mid], px[mid:]
        Ly = [p for p in py if p[0] <= midx]
        Ry = [p for p in py if p[0] > midx]

        dl, pl = rec(Lx, Ly)
        dr, pr = rec(Rx, Ry)
        d, pair = (dl, pl) if dl < dr else (dr, pr)

        strip = [p for p in py if abs(p[0] - midx) < d]
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                comparisons[0] += 1
                dd = dist(strip[i], strip[j])
                if dd < d:
                    d, pair = dd, (strip[i], strip[j])
        return d, pair

    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    d, pair = rec(px, py)
    return d, pair, comparisons[0]


def closest_pair_hybrid(points, threshold=40):
    """Hybrid: Divide-and-Conquer that switches to Brute Force once a
    subproblem's size falls at/below `threshold`. This is the classic
    'crossover' optimisation used in production computational-geometry
    libraries because brute force has lower constant-factor overhead on
    tiny inputs (no recursion / merge-strip bookkeeping)."""
    comparisons = [0]

    def bf(pts):
        best = float('inf')
        pair = None
        n = len(pts)
        for i in range(n):
            for j in range(i + 1, n):
                comparisons[0] += 1
                d = dist(pts[i], pts[j])
                if d < best:
                    best, pair = d, (pts[i], pts[j])
        return best, pair

    def rec(px, py):
        n = len(px)
        if n <= threshold:
            return bf(px)

        mid = n // 2
        midx = px[mid][0]
        Lx, Rx = px[:mid], px[mid:]
        Ly = [p for p in py if p[0] <= midx]
        Ry = [p for p in py if p[0] > midx]

        dl, pl = rec(Lx, Ly)
        dr, pr = rec(Rx, Ry)
        d, pair = (dl, pl) if dl < dr else (dr, pr)

        strip = [p for p in py if abs(p[0] - midx) < d]
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                comparisons[0] += 1
                dd = dist(strip[i], strip[j])
                if dd < d:
                    d, pair = dd, (strip[i], strip[j])
        return d, pair

    px = sorted(points, key=lambda p: p[0])
    py = sorted(points, key=lambda p: p[1])
    d, pair = rec(px, py)
    return d, pair, comparisons[0]


# ----------------------------------------------------------------------
# CONVEX HULL
# ----------------------------------------------------------------------

def orientation(p, q, r):
    """> 0 -> counter-clockwise (left turn), < 0 -> clockwise, 0 -> collinear."""
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1


def convex_hull_brute_force(points):
    """O(n^3): for every ordered pair (edge candidate), test whether all
    remaining points lie strictly on one side. If so the segment is a hull
    edge. Collect the endpoints of all such edges to obtain the hull."""
    n = len(points)
    hull_edges = []
    candidate_edges_checked = 0
    hull_points = set()
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            candidate_edges_checked += 1
            pos = neg = 0
            for k in range(n):
                if k == i or k == j:
                    continue
                o = orientation(points[i], points[j], points[k])
                if o > 0:
                    pos += 1
                elif o < 0:
                    neg += 1
            if pos == 0 or neg == 0:
                hull_edges.append((points[i], points[j]))
                hull_points.add(points[i])
                hull_points.add(points[j])

    # order the hull points angularly around centroid for plotting
    cx = sum(p[0] for p in hull_points) / len(hull_points)
    cy = sum(p[1] for p in hull_points) / len(hull_points)
    ordered = sorted(hull_points, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    return ordered, candidate_edges_checked, hull_edges


def convex_hull_dc(points):
    """O(n log n) divide-and-conquer convex hull (merge of upper/lower
    hulls of the sorted point set), used as the theoretical baseline."""
    pts = sorted(set(points))
    if len(pts) <= 1:
        return pts

    def half(seq):
        h = []
        for p in seq:
            while len(h) >= 2 and orientation(h[-2], h[-1], p) >= 0:
                h.pop()
            h.append(p)
        return h

    lower = half(pts)
    upper = half(pts[::-1])
    return lower[:-1] + upper[:-1]


def convex_hull_hybrid(points, threshold=40):
    """Hybrid convex hull: below `threshold` points, use the O(n^3) brute
    force edge test (cheap for tiny n and simple to verify by hand);
    above it, use the O(n log n) divide-and-conquer / monotone-chain hull."""
    if len(points) <= threshold:
        ordered, _, _ = convex_hull_brute_force(points)
        return ordered
    return convex_hull_dc(points)


# ----------------------------------------------------------------------
# DATASET GENERATION
# ----------------------------------------------------------------------

def make_dataset(n, seed=42, low=0, high=1_000_000):
    rng = random.Random(seed)
    pts = set()
    while len(pts) < n:
        pts.add((rng.randint(low, high), rng.randint(low, high)))
    return list(pts)
