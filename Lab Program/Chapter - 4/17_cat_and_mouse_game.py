from functools import lru_cache

DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2

def cat_mouse_game(graph):
    n = len(graph)

    @lru_cache(None)
    def solve(mouse, cat, turn, moves):
        if moves >= 2 * n * n:
            return DRAW
        if mouse == 0:
            return MOUSE_WIN
        if mouse == cat:
            return CAT_WIN

        if turn == 0:  # Mouse turn
            result = CAT_WIN
            for nxt in graph[mouse]:
                outcome = solve(nxt, cat, 1, moves + 1)
                if outcome == MOUSE_WIN:
                    return MOUSE_WIN
                if outcome == DRAW:
                    result = DRAW
            return result
        else:  # Cat turn
            result = MOUSE_WIN
            for nxt in graph[cat]:
                if nxt == 0:
                    continue
                outcome = solve(mouse, nxt, 0, moves + 1)
                if outcome == CAT_WIN:
                    return CAT_WIN
                if outcome == DRAW:
                    result = DRAW
            return result

    return solve(1, 2, 0, 0)

graph1 = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
graph2 = [[1,3],[0],[3],[0,2]]

print("Example 1:", cat_mouse_game(graph1))
print("Example 2:", cat_mouse_game(graph2))
