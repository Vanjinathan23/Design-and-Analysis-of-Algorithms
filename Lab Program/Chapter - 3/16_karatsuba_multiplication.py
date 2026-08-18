def karatsuba(x, y):
    # Handle negative numbers.
    sign = -1 if (x < 0) != (y < 0) else 1
    x, y = abs(x), abs(y)

    if x < 10 or y < 10:
        return sign * (x * y)

    n = max(len(str(x)), len(str(y)))
    m = n // 2
    base = 10 ** m

    high_x, low_x = divmod(x, base)
    high_y, low_y = divmod(y, base)

    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba(low_x + high_x, low_y + high_y)
    z2 = karatsuba(high_x, high_y)

    result = z2 * (base ** 2) + (z1 - z2 - z0) * base + z0
    return sign * result


test_cases = [
    (1234, 5678),
    (1234, 5678)
]

for x, y in test_cases:
    print(f"{x} x {y} =", karatsuba(x, y))
