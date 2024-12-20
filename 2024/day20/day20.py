
def dijkstra(race_map: list[str], start: tuple[int, int],
             end: tuple[int, int]) -> tuple[dict[tuple[int,int], int], list[tuple[int, int]]]:
    stack, visited, path = [(start[0], start[1], [(start[0],start[1])])], dict(), []
    while stack:
        x, y, p = stack.pop(0)
        if (x, y) in visited and visited[(x, y)] <= len(p): continue
        visited[(x, y)] = len(p) - 1
        if (x, y) == end: path = p ; continue
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(race_map[0]) and 0 <= ny < len(race_map) and race_map[ny][nx] != '#':
                stack.append((nx, ny, p + [(nx, ny)]))
    return visited, path


def cheat(visited: dict[tuple[int,int], int], path: list[tuple[int, int]], cheat_max: int) -> int:
    cheats100 = 0
    for s, e, cl in [(p1, p2, clt) for i, p1 in enumerate(path) for p2 in path[i+1:]
                     if 1 < (clt := abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])) <= cheat_max]:
        if visited[e] - (visited[s] + cl) >= 100: cheats100 += 1
    return cheats100


def solve(data: str, part: int):
    race_map, s, e = [line for line in data.splitlines()], (-1, -1), (-1, -1)
    for y, row in enumerate(race_map):
        for x, cell in enumerate(row):
            s = (x, y) if cell == 'S' else s
            e = (x, y) if cell == 'E' else e
            if e != (-1, -1) != s: break
        if e != (-1, -1) != s: break
    visited, path = dijkstra(race_map, s, e)
    if part == 1:
        return cheat(visited, path, 2)
    if part == 2:
        return cheat(visited, path, 20)
    return [cheat(visited, path, 2), cheat(visited, path, 20)]
