from collections import deque

def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path

        visited.add(state)

        for neighbor in generate_moves(state):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
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
    path = bfs(start, goal)

    if path:
        print("Путь найден (BFS):", path)
    else:
        print("Решение не найдено")
