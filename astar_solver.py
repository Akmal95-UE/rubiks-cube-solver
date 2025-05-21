import heapq

def heuristic(state, goal):
    # Пример эвристики: количество несовпадающих букв
    return sum(1 for a, b in zip(state, goal) if a != b)


def astar(start, goal):
    heap = [(heuristic(start, goal), 0, start, [start])]
    visited = set()

    while heap:
        est_total, cost, state, path = heapq.heappop(heap)
        if state == goal:
            return path

        visited.add(state)

        for neighbor in generate_moves(state):
            if neighbor not in visited:
                new_cost = cost + 1
                est = new_cost + heuristic(neighbor, goal)
                heapq.heappush(heap, (est, new_cost, neighbor, path + [neighbor]))

    return None


def generate_moves(state):
    moves = []
    state = list(state)

    s1 = state[:]
    s1[0], s1[1] = s1[1], s1[0]
    moves.append("".join(s1))

    s2 = state[:]
    s2[1], s2[2] = s2[2], s2[1]
    moves.append("".join(s2))

    s3 = state[:]
    s3[2], s3[3] = s3[3], s3[2]
    moves.append("".join(s3))

    return moves


if __name__ == "__main__":
    start = "ABCD"
    goal = "DCBA"
    path = astar(start, goal)

    if path:
        print("Путь найден (A*):", path)
    else:
        print("Решение не найдено")
