from collections import Counter

def four_sum_count(A, B, C, D):
    # Store frequencies of A[i] + B[j].
    ab_counts = Counter(a + b for a in A for b in B)

    count = 0
    for c in C:
        for d in D:
            count += ab_counts.get(-(c + d), 0)

    return count


test_cases = [
    ([1, 2], [-2, -1], [-1, 2], [0, 2]),
    ([0], [0], [0], [0])
]

for A, B, C, D in test_cases:
    print("A =", A)
    print("B =", B)
    print("C =", C)
    print("D =", D)
    print("Output:", four_sum_count(A, B, C, D))
    print()
