import json, math, time, itertools, csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from algorithms import (dist, closest_pair_brute_force, closest_pair_dc,
                         closest_pair_hybrid, convex_hull_brute_force,
                         convex_hull_dc, convex_hull_hybrid, orientation,
                         make_dataset)

OUT = "imgs"

P = [(2,3),(5,8),(9,4),(12,10),(7,2),(3,11),(15,6),(10,14),(6,12),(1,7)]
labels = {p: f"P{i}" for i, p in enumerate(P, 1)}

# ---------- 1. Full pairwise distance table ----------
rows = []
for p1, p2 in itertools.combinations(P, 2):
    d = dist(p1, p2)
    rows.append((labels[p1], p1, labels[p2], p2, round(d, 3)))
rows.sort(key=lambda r: r[4])
with open("pairwise_table.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Point A", "Coord A", "Point B", "Coord B", "Euclidean Distance"])
    w.writerows(rows)

cp_dist, cp_pair, cp_comparisons = closest_pair_brute_force(P)
print("Closest pair:", cp_pair, cp_dist, cp_comparisons)

# ---------- 2. Convex hull on the 10 points ----------
hull_pts, edges_checked, hull_edges = convex_hull_brute_force(P)
print("Hull:", hull_pts, "edges_checked:", edges_checked)

with open("hull_edge_test.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Edge (i->j)", "Points left of line", "Points right of line", "Verdict"])
    n = len(P)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            pos = neg = 0
            for k in range(n):
                if k in (i, j):
                    continue
                o = orientation(P[i], P[j], P[k])
                if o > 0: pos += 1
                elif o < 0: neg += 1
            verdict = "HULL EDGE" if (pos == 0 or neg == 0) else "-"
            if verdict == "HULL EDGE":
                w.writerow([f"{labels[P[i]]}{P[i]} -> {labels[P[j]]}{P[j]}", pos, neg, verdict])

# ---------- 3. Figure: points + closest pair + convex hull ----------
fig, ax = plt.subplots(figsize=(7, 6), dpi=150)
xs = [p[0] for p in P]
ys = [p[1] for p in P]
ax.scatter(xs, ys, color="#2563eb", s=70, zorder=3, label="Input points")
for p in P:
    ax.annotate(f"{labels[p]}{p}", (p[0]+0.15, p[1]+0.15), fontsize=9)

# closest pair
cxs = [cp_pair[0][0], cp_pair[1][0]]
cys = [cp_pair[0][1], cp_pair[1][1]]
ax.plot(cxs, cys, color="#dc2626", linewidth=2.5, zorder=4,
        label=f"Closest pair (d={cp_dist:.3f})")
ax.scatter(cxs, cys, color="#dc2626", s=110, zorder=5)

# convex hull polygon (close the loop)
hxs = [p[0] for p in hull_pts] + [hull_pts[0][0]]
hys = [p[1] for p in hull_pts] + [hull_pts[0][1]]
ax.plot(hxs, hys, color="#16a34a", linewidth=2, linestyle="--", zorder=2,
        label="Convex hull boundary")
ax.fill(hxs, hys, color="#16a34a", alpha=0.08)

ax.set_title("Closest Pair and Convex Hull — Brute Force Result (n = 10)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend(loc="upper left", fontsize=8)
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{OUT}/fig1_points_hull_closestpair.png")
plt.close()

# ---------- 4. Scalability experiments ----------
# Closest pair: BF only for small n (O(n^2) explodes), DC & Hybrid for all sizes
sizes_bf = [200, 500, 1000, 2000, 4000, 8000]
sizes_big = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]

results_cp = {"n": [], "brute_force": [], "dc": [], "hybrid": []}
for n in sizes_bf:
    pts = make_dataset(n, seed=1)
    t0 = time.perf_counter(); closest_pair_brute_force(pts); t1 = time.perf_counter()
    results_cp["n"].append(n)
    results_cp["brute_force"].append(t1 - t0)

results_cp_big = {"n": [], "dc": [], "hybrid": []}
for n in sizes_big:
    pts = make_dataset(n, seed=1)
    t0 = time.perf_counter(); closest_pair_dc(pts); t1 = time.perf_counter()
    t2 = time.perf_counter(); closest_pair_hybrid(pts, threshold=40); t3 = time.perf_counter()
    results_cp_big["n"].append(n)
    results_cp_big["dc"].append(t1 - t0)
    results_cp_big["hybrid"].append(t3 - t2)
    print("cp", n, "dc", t1-t0, "hybrid", t3-t2)

with open("results_closest_pair.json", "w") as f:
    json.dump({"small_bf": results_cp, "large_dc_hybrid": results_cp_big}, f, indent=2)

# Convex hull: BF only for small n (O(n^3) explodes fast), DC & Hybrid for all sizes
sizes_bf_hull = [20, 40, 60, 80, 100, 140]
results_hull = {"n": [], "brute_force": []}
for n in sizes_bf_hull:
    pts = make_dataset(n, seed=2)
    t0 = time.perf_counter(); convex_hull_brute_force(pts); t1 = time.perf_counter()
    results_hull["n"].append(n)
    results_hull["brute_force"].append(t1 - t0)
    print("hull-bf", n, t1 - t0)

results_hull_big = {"n": [], "dc": [], "hybrid": []}
for n in sizes_big:
    pts = make_dataset(n, seed=2)
    t0 = time.perf_counter(); convex_hull_dc(pts); t1 = time.perf_counter()
    t2 = time.perf_counter(); convex_hull_hybrid(pts, threshold=40); t3 = time.perf_counter()
    results_hull_big["n"].append(n)
    results_hull_big["dc"].append(t1 - t0)
    results_hull_big["hybrid"].append(t3 - t2)
    print("hull", n, "dc", t1-t0, "hybrid", t3-t2)

with open("results_convex_hull.json", "w") as f:
    json.dump({"small_bf": results_hull, "large_dc_hybrid": results_hull_big}, f, indent=2)

print("DONE")
