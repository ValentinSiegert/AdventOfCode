
def part1(data: str):
    locks = [{(x, y) for y, row in enumerate(item.splitlines()) for x, c in enumerate(row) if c == '#'} for item in data.split('\n\n') if item[0] == '#']
    keys = [{(x, y) for y, row in enumerate(item.splitlines()) for x, c in enumerate(row) if c == '#'} for item in data.split('\n\n') if item[0] == '.']
    return sum(1 for key in keys for lock in locks if key.isdisjoint(lock))


def solve(data: str, part: int):
    if part == 1: return part1(data)
    if part == 2: return None  # no part 2 today
    return [part1(data), None]  # no part 2 today
