def take_step(y: int, x: int, direction: str) -> tuple[int, int]:
    if direction == "urdl":
        return (y - 1, x)
    if direction == "dlur":
        return (y + 1, x)
    if direction == "lurd":
        return (y, x - 1)
    if direction == "rdlu":
        return (y, x + 1)


def guard_pathing(field: list[list[str]], y: int, x: int, d: str, obs: tuple[int, int] = None) -> tuple[set, bool]:
    visited = set()
    while 0 <= y < len(field) and 0 <= x < len(field[0]):
        ny, nx = take_step(y, x, d)
        if 0 <= ny < len(field) and 0 <= nx < len(field[0]) and (field[ny][nx] == '#' or (obs and (ny, nx) == obs)):
            d = d[1:] + d[0]
        else:
            y, x = ny, nx
        if (y, x, d) in visited:
            return {(y, x) for y, x, _ in visited}, True
        visited.add((y, x, d))
    return {(y, x) for y, x, _ in visited}, False


def solve(data: str, part: int):
    field, direction = [list(line) for line in data.splitlines()], "urdl"
    y, x = next((y, x) for y, row in enumerate(field) for x, cell in enumerate(row) if cell == "^")
    visited, _ = guard_pathing(field, y, x, direction)
    if part == 1:
        return len(visited) - 1
    obstacle_amount, obstacles = 0, visited - {(y, x)}
    for obs in obstacles:
        if guard_pathing(field, y, x, direction, obs)[1]:
            obstacle_amount += 1
    if part == 2:
        return obstacle_amount
    return len(visited) - 1, obstacle_amount
