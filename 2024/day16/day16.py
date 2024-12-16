
def shortest_visit(data: str) -> tuple[dict[tuple[int, int], int], tuple[int, int], tuple[int, int]]:
    """
    Calculate the shortest path from S to E using Dijkstra's algorithm.
    :param data: The puzzle input as string.
    :return: A tuple containing a dictionary with the smallest cost to each point, the start and end coordinates.
    """
    xs, ys, xe, ye = 1, len(data := data.splitlines()) - 2, len(data[0]) - 2, 1
    stack, visited = [(xs, ys, 0, 'e')], dict()
    directions = {
        'n': [(0, -1, 'n'), (-1, 0, 'w'), (1, 0, 'e')],
        'e': [(1, 0, 'e'), (0, -1, 'n'), (0, 1, 's')],
        's': [(0, 1, 's'), (1, 0, 'e'), (-1, 0, 'w')],
        'w': [(-1, 0, 'w'), (0, 1, 's'), (0, -1, 'n')],
    }
    while stack:
        x, y, c, d = stack.pop(0)
        if (x, y) in visited and visited[(x, y)] <= c: continue
        visited[(x, y)] = c
        if x == xe and y == ye: continue
        for dx, dy, nd in directions[d]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(data[0]) and 0 <= ny < len(data) and data[ny][nx] != '#':
                nc = c + 1 if d == nd else c + 1001
                stack.append((nx, ny, nc, nd))
    return visited, (xs,ys), (xe,ye)


def best_spots(visited: dict[tuple[int, int], int], e: tuple[int, int]) -> set[tuple[int, int]]:
    """
    Calculate the best spot to stand on after the path from S to E has been calculated.
    :param visited: The dictionary containing the smallest cost to each point.
    :param e: The end coordinates.
    :return: Amount of spots that are on one of the shortest paths.
    """
    spots, stack, directions = {e}, [e], [(0, -1), (0, 1), (-1, 0), (1, 0)]
    while stack:
        x, y = stack.pop(0)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            old_min = min(om) \
                if len(om := {visited[(x0, y0)] for x0, y0 in spots if visited[(x0, y0)] > visited[(x,y)]}) else 0
            if ((nx, ny) in visited and (nx, ny) not in spots and
                    (visited[(nx, ny)] < visited[(x, y)] or visited[(nx, ny)] == old_min - 2)):
                stack.append((nx, ny))
                spots.add((nx, ny))
    # print()
    print(len(spots))
    print()
    return spots


def solve(data: str, part: int):
    # data = '#################\n#...#...#...#..E#\n#.#.#.#.#.#.#.#.#\n#.#.#.#...#...#.#\n#.#.#.#.###.#.#.#\n#...#.#.#.....#.#\n#.#.#.#.#.#####.#\n#.#...#.#.#.....#\n#.#.#####.#.###.#\n#.#.#.......#...#\n#.#.###.#####.###\n#.#.#...#.....#.#\n#.#.#.#####.###.#\n#.#.#.........#.#\n#.#.#.#########.#\n#S#.............#\n#################'
    visited, sc, ec = shortest_visit(data)
    if part == 1:
        return visited[ec]
    spots = best_spots(visited, ec)
    new_data = [list(row) for row in data.splitlines()]
    for x, y in spots:
        new_data[y][x] = 'O'
    for row in new_data:
        print(''.join(row))
    if part == 2:
        return len(spots)
    return [visited[ec], len(spots)]
