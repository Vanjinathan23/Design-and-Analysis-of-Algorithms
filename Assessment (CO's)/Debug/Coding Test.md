# Q38. Minimum Falling Path Sum

**Register No.:** 192425231
**Name:** VANJINATHAN S

## Problem Statement

Given a square matrix, find the minimum sum of a falling path from the top row to the bottom row. At each step, you can move to the cell directly below, or diagonally to the bottom-left or bottom-right cell. The objective is to determine the minimum possible sum using **Dynamic Programming**.

### Input Format
```
n = matrix size
matrix[][]
```

### Sample Input
```
matrix =
2 1 3
6 5 4
7 8 9
```

### Expected Output
```
Min Sum = 13
```

## Approach — Dynamic Programming

We build a table `dp` where `dp[i][j]` stores the minimum falling path sum needed to reach cell `(i, j)` starting anywhere in the top row.

- **Base case:** the first row of `dp` is the same as the first row of the matrix, since a path can start at any column in row 0.
- **Transition:** for every other cell, the path arriving at `(i, j)` must come from `(i-1, j-1)`, `(i-1, j)`, or `(i-1, j+1)` (whichever exist), so:

```
dp[i][j] = matrix[i][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])
```

- **Answer:** the smallest value in the last row of `dp`.

### Dry Run (Sample Input)

| Row | Values (dp) |
|---|---|
| Row 0 | 2, 1, 3 |
| Row 1 | 6+1=7, 5+1=6, 4+1=5 |
| Row 2 | 7+6=13, 8+5=13, 9+5=14 |

Minimum of last row → `min(13, 13, 14) = 13`

## Complexity

| Metric | Value |
|---|---|
| Time Complexity | O(n²) |
| Space Complexity | O(n²) (or O(1) extra if done in-place) |

## Files

- [`min_falling_path_sum.py`](./min_falling_path_sum.py) — Python implementation with the DP solution and a runnable `main()` demonstrating the sample input.

## How to Run

```bash
python3 min_falling_path_sum.py
```

**Output:**
```
Min Sum = 13
```
