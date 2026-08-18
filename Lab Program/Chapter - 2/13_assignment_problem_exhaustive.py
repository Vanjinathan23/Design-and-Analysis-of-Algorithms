import itertools

def total_cost(assignment, cost_matrix):
    return sum(
        cost_matrix[worker][task]
        for worker, task in enumerate(assignment)
    )

def assignment_problem(cost_matrix):
    n = len(cost_matrix)
    best_assignment = None
    best_cost = float("inf")

    for assignment in itertools.permutations(range(n)):
        cost = total_cost(assignment, cost_matrix)

        if cost < best_cost:
            best_cost = cost
            best_assignment = assignment

    pairs = [
        (worker + 1, task + 1)
        for worker, task in enumerate(best_assignment)
    ]

    return pairs, best_cost

test_cases = [
    [[3, 10, 7], [8, 5, 12], [4, 6, 9]],
    [[15, 9, 4], [8, 7, 18], [6, 12, 11]]
]

for i, matrix in enumerate(test_cases, 1):
    assignment, cost = assignment_problem(matrix)
    print(f"Test Case {i}:")
    print("Optimal Assignment:", assignment)
    print("Total Cost:", cost)
    print()
