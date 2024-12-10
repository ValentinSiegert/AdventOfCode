def hike(map: list[list[int]], position: tuple[int, int]) -> tuple[set[tuple[int, int]], int]:
    ends, rate, (y, x) = set(), 0, position
    if map[y][x] == 9:
        return {(y, x)}, 1
    if 0 < y and map[y - 1][x] == map[y][x] + 1:
        hiking, rating = hike(map, (y - 1, x))
        ends |= hiking
        rate += rating
    if 0 < x and map[y][x - 1] == map[y][x] + 1:
        hiking, rating = hike(map, (y, x - 1))
        ends |= hiking
        rate += rating
    if y < len(map) - 1 and map[y + 1][x] == map[y][x] + 1:
        hiking, rating = hike(map, (y + 1, x))
        ends |= hiking
        rate += rating
    if x < len(map[y]) - 1 and map[y][x + 1] == map[y][x] + 1:
        hiking, rating = hike(map, (y, x + 1))
        ends |= hiking
        rate += rating
    return ends, rate


def hike_map(data: str):
    map, start0 = [], []
    for y, line in enumerate(data.splitlines()):
        map.append([])
        for x, c in enumerate(line):
            c = int(c)
            map[y].append(c)
            if c == 0:
                start0.append((y, x))
    unique = rated = 0
    for start in start0:
        ends, rate = hike(map, start)
        unique += len(ends)
        rated += rate
    return unique, rated


def solve(data: str, part: int):
    r1, r2 = hike_map(data)
    print(r1, r2)
    if part == 1:
        return r1
    if part == 2:
        return r2
    return [r1, r2]
