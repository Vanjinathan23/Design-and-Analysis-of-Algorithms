def strassen_2x2(A, B):
    a, b = A[0]
    c, d = A[1]

    e, f = B[0]
    g, h = B[1]

    # Strassen's seven products.
    p1 = a * (f - h)
    p2 = (a + b) * h
    p3 = (c + d) * e
    p4 = d * (g - e)
    p5 = (a + d) * (e + h)
    p6 = (b - d) * (g + h)
    p7 = (a - c) * (e + f)

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    return [[c11, c12], [c21, c22]]


test_cases = [
    (
        [[1, 7], [3, 5]],
        [[1, 3], [7, 5]]
    ),
    (
        [[1, 7], [3, 5]],
        [[6, 8], [4, 2]]
    )
]

for A, B in test_cases:
    print("A =", A)
    print("B =", B)
    print("C =", strassen_2x2(A, B))
    print()
