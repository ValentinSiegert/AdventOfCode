
C, F = 71, 1024


def dijkstra(fallen_bytes: list[tuple[int, int]]) -> tuple[int, set[tuple[int, int]]]:
    xe, ye, stack, visited, path = C - 1, C - 1, [(0, 0, 0, {(0,0)})], dict(), set()
    while stack:
        x, y, c, p = stack.pop(0)
        if (x, y) in visited and visited[(x, y)] <= c: continue
        visited[(x, y)] = c
        if (x, y) == (xe, ye):
            path = p
            continue
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < C and 0 <= ny < C and (nx, ny) not in fallen_bytes:
                stack.append((nx, ny, (c + 1), p | {(nx, ny)}))
    return (visited[(xe, ye)], path) if (xe, ye) in visited else (-1, path)


def first_blocking_coord(data: str) -> str:
    fallen_bytes = [(int(x), int(y)) for x, y in [row.split(",") for row in data.splitlines()]][:F]
    shortest, path = dijkstra(fallen_bytes)
    for i in range(F+1, len(data.splitlines())):
        fallen_bytes = [(int(x), int(y)) for x, y in [row.split(",") for row in data.splitlines()]][:i]
        if fallen_bytes[-1] in path:
            shortest, path = dijkstra(fallen_bytes)
            print(f'{i}: {shortest}')
        if shortest == - 1:
            print(fallen_bytes[-1])
            return f'{fallen_bytes[-1][0]},{fallen_bytes[-1][1]}'


def solve(data: str, part: int):
    r1, _ = dijkstra([(int(x),int(y)) for x,y in [row.split(",") for row in data.splitlines()]][:F])
    print(r1)
    if part == 1:
        return r1
    if part == 2:
        return first_blocking_coord(data)
    return [r1, first_blocking_coord(data)]
