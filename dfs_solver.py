def dfs(start, goal):
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()
        if state == goal:
            return path

        visited.add(state)

        for neighbor in generate_moves(state):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))
    return None


def generate_moves(state):
    # Генерируем возможные состояния (повороты)
    moves = []
    state = list(state)

    # Пример: меняем местами первые две буквы
    s1 = state[:]
    s1[0], s1[1] = s1[1], s1[0]
    moves.append("".join(s1))

    # Меняем местами вторую и третью
    s2 = state[:]
    s2[1], s2[2] = s2[2], s2[1]
    moves.append("".join(s2))

    # Меняем местами третью и четвёртую
    s3 = state[:]
    s3[2], s3[3] = s3[3], s3[2]
    moves.append("".join(s3))

    return moves


if __name__ == "__main__":
    start = "ABCD"
    goal = "DCBA"
    path = dfs(start, goal)

    if path:
        print("Путь найден:", path)
    else:
        print("Решение не найдено")
