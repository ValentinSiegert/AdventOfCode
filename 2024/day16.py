
def shortest_visit(maze: str) -> tuple[int, int]:
    """
    Calculate the shortest path from S to E using Dijkstra's algorithm including directions and costs to find all shortest paths.
    :param maze: The maze to traverse.
    :return: A tuple containing the smallest cost to reach the end and the number of spots on the shortest paths.
    """
    directions = {
        'n': [(0, -1, 'n'), (-1, 0, 'w'), (1, 0, 'e')],
        'e': [(1, 0, 'e'), (0, -1, 'n'), (0, 1, 's')],
        's': [(0, 1, 's'), (1, 0, 'e'), (-1, 0, 'w')],
        'w': [(-1, 0, 'w'), (0, 1, 's'), (0, -1, 'n')],
    }
    xs, ys, xe, ye = 1, len(maze := maze.splitlines()) - 2, len(maze[0]) - 2, 1
    stack, visited, spots, best = [(xs, ys, 0, 'e', {(xs, ys)})], dict(), set(), 1e9
    while stack:
        x, y, c, d, p = stack.pop(0)
        if (x, y, d) in visited and visited[(x, y, d)] < c: continue
        visited[(x, y, d)] = c
        if x == xe and y == ye and c <= best:
            spots = p if c < best else spots | p
            best = c
        for dx, dy, nd in directions[d]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and maze[ny][nx] != '#':
                stack.append((nx, ny, (c + 1 if d == nd else c + 1001), nd, p | {(nx, ny)}))
    return best, len(spots)


def solve(data: str, part: int):
    best_score, best_spots = shortest_visit(data)
    if part == 1:
        return best_score
    if part == 2:
        return best_spots
    return [best_score, best_spots]
