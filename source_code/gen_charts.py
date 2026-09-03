import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = "imgs"

# ---------------- Closest Pair ----------------
with open("results_closest_pair.json") as f:
    cp = json.load(f)

fig, ax = plt.subplots(figsize=(7.5, 5.5), dpi=150)
ax.plot(cp["small_bf"]["n"], cp["small_bf"]["brute_force"], 'o-', color="#dc2626", label="Brute Force O(n²)")
ax.plot(cp["large_dc_hybrid"]["n"], cp["large_dc_hybrid"]["dc"], 's-', color="#2563eb", label="Divide & Conquer O(n log n)")
ax.plot(cp["large_dc_hybrid"]["n"], cp["large_dc_hybrid"]["hybrid"], '^-', color="#16a34a", label="Hybrid (threshold=40)")
ax.set_xlabel("Number of points (n)")
ax.set_ylabel("Execution time (seconds)")
ax.set_title("Closest Pair of Points — Execution Time vs. Input Size")
ax.set_xscale("log")
ax.set_yscale("log")
ax.grid(alpha=0.3, which="both")
ax.legend()
plt.tight_layout()
plt.savefig(f"{OUT}/fig2_closest_pair_scaling.png")
plt.close()

# Zoomed overlapping region so BF is visible next to DC/Hybrid
fig, ax = plt.subplots(figsize=(7.5, 5.5), dpi=150)
ax.plot(cp["small_bf"]["n"], cp["small_bf"]["brute_force"], 'o-', color="#dc2626", label="Brute Force O(n²)")
n_big = cp["large_dc_hybrid"]["n"]
dc = cp["large_dc_hybrid"]["dc"]
hy = cp["large_dc_hybrid"]["hybrid"]
zoom = [(n, d, h) for n, d, h in zip(n_big, dc, hy) if n <= 10000]
ax.plot([z[0] for z in zoom], [z[1] for z in zoom], 's-', color="#2563eb", label="Divide & Conquer O(n log n)")
ax.plot([z[0] for z in zoom], [z[2] for z in zoom], '^-', color="#16a34a", label="Hybrid (threshold=40)")
ax.set_xlabel("Number of points (n)")
ax.set_ylabel("Execution time (seconds)")
ax.set_title("Closest Pair — Zoomed View (n ≤ 10,000)")
ax.grid(alpha=0.3)
ax.legend()
plt.tight_layout()
plt.savefig(f"{OUT}/fig3_closest_pair_zoom.png")
plt.close()

# ---------------- Convex Hull ----------------
with open("results_convex_hull.json") as f:
    hu = json.load(f)

fig, ax = plt.subplots(figsize=(7.5, 5.5), dpi=150)
ax.plot(hu["small_bf"]["n"], hu["small_bf"]["brute_force"], 'o-', color="#dc2626", label="Brute Force O(n³)")
ax.plot(hu["large_dc_hybrid"]["n"], hu["large_dc_hybrid"]["dc"], 's-', color="#2563eb", label="Divide & Conquer O(n log n)")
ax.plot(hu["large_dc_hybrid"]["n"], hu["large_dc_hybrid"]["hybrid"], '^-', color="#16a34a", label="Hybrid (threshold=40)")
ax.set_xlabel("Number of points (n)")
ax.set_ylabel("Execution time (seconds)")
ax.set_title("Convex Hull — Execution Time vs. Input Size")
ax.set_xscale("log")
ax.set_yscale("log")
ax.grid(alpha=0.3, which="both")
ax.legend()
plt.tight_layout()
plt.savefig(f"{OUT}/fig4_convex_hull_scaling.png")
plt.close()

fig, ax = plt.subplots(figsize=(7.5, 5.5), dpi=150)
ax.plot(hu["small_bf"]["n"], hu["small_bf"]["brute_force"], 'o-', color="#dc2626", label="Brute Force O(n³)")
ax.set_xlabel("Number of points (n)")
ax.set_ylabel("Execution time (seconds)")
ax.set_title("Convex Hull Brute Force — Cubic Blow-up (n ≤ 140)")
ax.grid(alpha=0.3)
ax.legend()
plt.tight_layout()
plt.savefig(f"{OUT}/fig5_convex_hull_bf_blowup.png")
plt.close()

# ---------------- Theoretical operation counts ----------------
import math
ns = [10, 50, 100, 500, 1000, 5000, 10000]
bf_ops = [n*(n-1)/2 for n in ns]
dc_ops = [n*math.log2(n) for n in ns]
fig, ax = plt.subplots(figsize=(7.5, 5.5), dpi=150)
ax.plot(ns, bf_ops, 'o-', color="#dc2626", label="Brute Force: n(n-1)/2 comparisons")
ax.plot(ns, dc_ops, 's-', color="#2563eb", label="Divide & Conquer: n·log₂n (order)")
ax.set_xlabel("Number of points (n)")
ax.set_ylabel("Number of operations (theoretical)")
ax.set_title("Theoretical Pairwise-Comparison Growth: Closest Pair")
ax.set_yscale("log")
ax.grid(alpha=0.3, which="both")
ax.legend()
plt.tight_layout()
plt.savefig(f"{OUT}/fig6_theoretical_growth.png")
plt.close()

print("charts done")
