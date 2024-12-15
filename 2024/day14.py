import re


SPACEY, SPACEX, SECONDS, ROBOT_RE = 103, 101, 100, r'p=(?P<xp>-?\d+),(?P<yp>-?\d+)\sv=(?P<xv>-?\d+),(?P<yv>-?\d+)'


def part1(data: str):
    quad1 = quad2 = quad3 = quad4 = 0
    for robot_match in re.finditer(ROBOT_RE, data):
        xp, yp, xv, yv = map(int, robot_match.groups())
        x , y = (xp + (xv * SECONDS)) % SPACEX, (yp + (yv * SECONDS)) % SPACEY
        if 0 <= x < SPACEX // 2 and 0 <= y < SPACEY // 2: quad1 += 1  # robot in quadrant upper left
        elif SPACEX // 2 < x < SPACEX and 0 <= y < SPACEY // 2: quad2 += 1  # robot in quadrant upper right
        elif 0 <= x < SPACEX // 2 and SPACEY // 2 < y < SPACEY: quad3 += 1  # robot in quadrant lower left
        elif SPACEX // 2 < x < SPACEX and SPACEY // 2 < y < SPACEY: quad4 += 1  # robot in quadrant lower right
    return quad1 * quad2 * quad3 * quad4


def print_space(robots: list[list[int]], seconds_passed: int):
    """
    Required to find the Christmas Tree in robot space.

    Spoiler looks something like this: (81000 seconds passed for my input)
    1111111111111111111111111111111
    1.............................1
    1.............................1
    1.............................1
    1.............................1
    1..............1..............1
    1.............111.............1
    1............11111............1
    1...........1111111...........1
    1..........111111111..........1
    1............11111............1
    1...........1111111...........1
    1..........111111111..........1
    1.........11111111111.........1
    1........1111111111111........1
    1..........111111111..........1
    1.........11111111111.........1
    1........1111111111111........1
    1.......111111111111111.......1
    1......11111111111111111......1
    1........1111111111111........1
    1.......111111111111111.......1
    1......11111111111111111......1
    1.....1111111111111111111.....1
    1....111111111111111111111....1
    1.............111.............1
    1.............111.............1
    1.............111.............1
    1.............................1
    1.............................1
    1.............................1
    1.............................1
    1111111111111111111111111111111

    :param robots: list of robots, each robot is a list of 4 integers [x, y, vx, vy]
    :param seconds_passed: seconds passed
    """
    space = [['.' for _ in range(SPACEX)] for _ in range(SPACEY)]
    for robot in robots:
        x, y = robot[0], robot[1]
        space[y][x] = '1' if space[y][x] == '.' else str(int(space[y][x]) + 1)
    print(f'{seconds_passed} seconds passed')
    for row in space:
        print(''.join(row))
    print()


def part2(data: str):
    robots = [list(map(int, r)) for r in re.findall(ROBOT_RE, data)]
    for i in range(1, 81001):  # if 81000 seconds pass for my input, the Christmas Tree is visible
        for robot in robots: robot[0], robot[1] = (robot[0] + robot[2]) % 101, (robot[1] + robot[3]) % 103
        # print_space(robots, i) if i % 1000 == 0 else None
        space = [[0 for _ in range(SPACEX)] for _ in range(SPACEY)]
        for robot in robots: space[robot[1]][robot[0]] += 1
        if any('1111111111111111111111111111111' in str(''.join(map(str,row))) for row in space): return i
    return -1


def solve(data: str, part: int):
    if part == 1:
        return part1(data)
    if part == 2:
        return part2(data)
    return [part1(data), part2(data)]
